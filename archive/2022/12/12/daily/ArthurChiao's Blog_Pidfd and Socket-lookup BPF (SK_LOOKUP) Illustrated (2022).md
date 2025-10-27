---
title: Pidfd and Socket-lookup BPF (SK_LOOKUP) Illustrated (2022)
url: https://arthurchiao.github.io/blog/pidfd-and-socket-lookup-bpf-illustrated/
source: ArthurChiao's Blog
date: 2022-12-12
fetch_date: 2025-10-04T01:14:16.098574
---

# Pidfd and Socket-lookup BPF (SK_LOOKUP) Illustrated (2022)

# [ArthurChiao's Blog](https://arthurchiao.github.io/)

* [Home](/index.html)
* [Articles (EN)](/articles)
* [Articles (中文)](/articles-zh)
* [Categories](/categories)
* [About](/about)
* [Donate](/donate)

# Pidfd and Socket-lookup BPF (SK\_LOOKUP) Illustrated (2022)

Published at 2022-12-11 | Last Update 2022-12-11

### TL; DR

Most unix programming text books as well as practices hold the following statements to be true:

1. **One socket** could be opened by **one and only one process** (application);
2. **One socket** could listen/serve on **one and only one port**;

   Recall the `bind` system call
   `int bind(int sockfd, const struct sockaddr *addr, socklen_t addrlen)` where
   `addr` is determined by `IP+Port` (and socket address family).

However, with some advanced techniques like **`pidfd_getfd()`**
system call in Linux kernel `5.4+` and **`SK_LOOKUP`** BPF in
kernel `5.6+`, we could easily break the above limitations, supporting scenarios like below:

```
       +-----------+  +-----------+  +----------+                              +------------------+
       | Process 1 |  | Process 2 |  | Process 3|                              |   Process(app)   |
       |           |  |           |  |          |                              |                  |
       |  SockFD1  |  |  SockFD2  |  |  SockFD3 |                              |     SockFD       |
       +-----------+  +-----------+  +----------+                              +------------------+
                \         |         /                                                   |
                +--------------------+                                         +------------------+
                |       Socket       |                                         |     Socket       |
                +--------------------+                                         +------------------+
                          |                                                    /        |         \
                +--------------------+                                 +--------+  +---------+  +----------+
                |       TCP@80       |                                 |  TCP@7 |  | TCP@77  |  | TCP@777  |
                +--------------------+                                 +--------+  +---------+  +----------+
                          |                                                     \       |         /
                +--------------------+                                          +------------------+
                |      ServerIP      |                                          |    ServerIP      |
                +--------------------+                                          +------------------+
                          /\                                                            /\
                          ||                                                            ||
                       requests                                                      requests

                       Scenario 1:                                                  Scenario 2:
  Multiple processes serve requests over the same socket.         Single socket listens/serves on multiple ports.
  E.g. Three HTTP servers share the same TCP@localhost:80         E.g. one socket servers on TCP@localhost
  socket.                                                         {:6, :66, :666} simultaneously.
```

This post explains the underlying working mechanism of the `SK_LOOKUP` BPF,
and provides example codes based on [cilium/ebpf](https://github.com/cilium/ebpf)
library, which has minimal dependencies and doesn’t require header files to be installed.

Demo codes in this post: [github.com/arthurchiao/pidfd-and-sk-lookup-bpf-illustrated](https://github.com/arthurchiao/pidfd-and-sk-lookup-bpf-illustrated).

---

* [TL; DR](#tl-dr)
* [1 Introduction](#1-introduction)
* [2 Multiple processes serving on the same socket](#2-multiple-processes-serving-on-the-same-socket)
  + [2.1 Background](#21-background)
    - [2.1.1 `pidfd` and `pidfd_open()` system call (kernel `5.4+`)](#211-pidfd-and-pidfd_open-system-call-kernel-54)
    - [2.1.2 `pidfd_getfd()` system call (kernel `5.6+`)](#212-pidfd_getfd-system-call-kernel-56)
  + [2.2 `share-socket`: a demo of multiple servers share the same socket (listen fd)](#22-share-socket-a-demo-of-multiple-servers-share-the-same-socket-listen-fd)
    - [2.2.1 Source code (golang)](#221-source-code-golang)
    - [2.2.2 Test](#222-test)
  + [2.3 `graceful-upgrade`: a demo for graceful L4/L7 service upgrade](#23-graceful-upgrade-a-demo-for-graceful-l4l7-service-upgrade)
    - [2.3.1 Source code (golang)](#231-source-code-golang)
    - [2.3.2 Test](#232-test)
  + [2.4 Summary](#24-summary)
* [3 Single process (socket) serving on multiple ports](#3-single-process-socket-serving-on-multiple-ports)
  + [3.1 `BPF_PROG_TYPE_SK_LOOKUP` program](#31-bpf_prog_type_sk_lookup-program)
    - [3.1.1 Motivation](#311-motivation)
    - [3.1.2 Attachment](#312-attachment)
    - [3.1.3 Hooks](#313-hooks)
  + [3.2 Create a simple echo server](#32-create-a-simple-echo-server)
    - [3.2.1 Create server with `ncat/nc`](#321-create-server-with-ncatnc)
    - [3.2.2 Test accessing](#322-test-accessing)
  + [3.3 BPF program](#33-bpf-program)
    - [3.3.1 Kernel/BPF code](#331-kernelbpf-code)
    - [3.3.2 Userspace code](#332-userspace-code)
    - [3.3.3 Compile, load, attach](#333-compile-load-attach)
    - [3.3.4 Configure with `bpftool map update`](#334-configure-with-bpftool-map-update)
    - [3.3.5 Test](#335-test)
  + [3.4 Improvement: pin the BPF program and BPF link to bpffs](#34-improvement-pin-the-bpf-program-and-bpf-link-to-bpffs)
* [4 Summary](#4-summary)
* [References](#references)

---

# 1 Introduction

This post explains the underlying working mechanism of the `SK_LOOKUP` BPF.
We’ll have several examples to implement the following scenarios.

```
       +-----------+  +-----------+  +----------+                              +------------------+
       | Process 1 |  | Process 2 |  | Process 3|                              |   Process(app)   |
       |           |  |           |  |          |                              |                  |
       |  SockFD1  |  |  SockFD2  |  |  SockFD3 |                              |     SockFD       |
       +-----------+  +-----------+  +----------+                              +------------------+
                \         |         /                                                   |
                +--------------------+                                         +------------------+
                |       Socket       |                                         |     Socket       |
                +--------------------+                                         +------------------+
                          |                                                    /        |         \
                +--------------------+                                 +--------+  +---------+  +----------+
                |       TCP@80       |                                 |  TCP@7 |  | TCP@77  |  | TCP@777  |
                +--------------------+                                 +--------+  +---------+  +----------+
                          |                                                     \       |         /
                +--------------------+                                          +------------------+
                |      ServerIP      |                                          |    ServerIP      |
                +--------------------+                                          +------------------+
                          /\                                                            /\
                          ||                                                            ||
                       requests                                                      requests

                       Scenario 1:                                                  Scenario 2:
  Multi...