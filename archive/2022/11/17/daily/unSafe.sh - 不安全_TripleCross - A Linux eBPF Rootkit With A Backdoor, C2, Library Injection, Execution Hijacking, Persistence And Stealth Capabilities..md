---
title: TripleCross - A Linux eBPF Rootkit With A Backdoor, C2, Library Injection, Execution Hijacking, Persistence And Stealth Capabilities.
url: https://buaq.net/go-135920.html
source: unSafe.sh - 不安全
date: 2022-11-17
fetch_date: 2025-10-03T22:58:17.996110
---

# TripleCross - A Linux eBPF Rootkit With A Backdoor, C2, Library Injection, Execution Hijacking, Persistence And Stealth Capabilities.

* [unSafe.sh - 不安全](https://unsafe.sh)
* [我的收藏](/user/collects)
* [今日热榜](/?hot=true)
* [公众号文章](/?gzh=true)
* [导航](/nav/index)
* [Github CVE](/cve)
* [Github Tools](/tools)
* [编码/解码](/encode)
* [文件传输](/share/index)
* [Twitter Bot](https://twitter.com/buaqbot)
* [Telegram Bot](https://t.me/aqinfo)
* [Search](/search/search)

[Rss](/rss.xml)

[ ]
黑夜模式

![](https://8aqnet.cdn.bcebos.com/71def1bbd5ea63b6377c0b327b95be6c.jpg)

TripleCross - A Linux eBPF Rootkit With A Backdoor, C2, Library Injection, Execution Hijacking, Persistence And Stealth Capabilities.

TripleCross is a Linux eBPF rootkit that demonstrates the offensive capabilities of the eBPF
*2022-11-16 19:30:0
Author: [www.kitploit.com(查看原文)](/jump-135920.htm)
阅读量:44
收藏*

---

[![](https://blogger.googleusercontent.com/img/a/AVvXsEgRZ6H0xqq6KbEssmh0HkeVAWJvbzp16ctTmzOn118UcZRaRiEVLR__ZotG1oPIFheyW3IAUlRL_nd2ZtwL6DqdFz2JPX0y4jDz_spEvDTaqMKbjs48e-jJ6A3NktLdpQ-gwBee8LW745BCXazNCoWxbjQ3tgSXR6wla96lypiXEWG3nWsGgxvcwmY09Q=w640-h444)](https://blogger.googleusercontent.com/img/a/AVvXsEgRZ6H0xqq6KbEssmh0HkeVAWJvbzp16ctTmzOn118UcZRaRiEVLR__ZotG1oPIFheyW3IAUlRL_nd2ZtwL6DqdFz2JPX0y4jDz_spEvDTaqMKbjs48e-jJ6A3NktLdpQ-gwBee8LW745BCXazNCoWxbjQ3tgSXR6wla96lypiXEWG3nWsGgxvcwmY09Q)

TripleCross is a Linux eBPF rootkit that demonstrates the offensive capabilities of the eBPF technology.

TripleCross is inspired by previous implant designs in this area, notably the works of Jeff Dileo at DEFCON 27[1](https://github.com/h3xduck/TripleCross#user-content-fn-1-254dd230abf4f1f0c19463c387281aa0 "1"), Pat Hogan at DEFCON 29[2](https://github.com/h3xduck/TripleCross#user-content-fn-2-254dd230abf4f1f0c19463c387281aa0 "2"), Guillaume Fournier and Sylvain Afchain also at DEFCON 29[3](https://github.com/h3xduck/TripleCross#user-content-fn-3-254dd230abf4f1f0c19463c387281aa0 "3"), and Kris Nóva's Boopkit[4](https://github.com/h3xduck/TripleCross#user-content-fn-4-254dd230abf4f1f0c19463c387281aa0 "4"). We reuse and extend some of the techniques pioneered by these previous explorations of the offensive capabilities of eBPF technology.

This rootkit was created for my Bachelor's Thesis at UC3M. More details about its design are provided in the [thesis document](https://github.com/h3xduck/TripleCross/blob/master/docs/ebpf_offensive_rootkit_tfg.pdf "thesis document").

### Disclaimer

This rookit is **purely for educational and academic purposes**. The software is provided "as is" and the authors are not responsible for any damage or mishaps that may occur during its use.

Do not attempt to use TripleCross to violate the law. Misuse of the provided software and information may result in criminal charges.

## Features

1. A **library injection** module to execute malicious code by writing at a process' virtual memory.
2. An **execution hijacking** module that modifies data passed to the kernel to execute malicious programs.
3. A **local privilege escalation** module that allows for running malicious programs with root privileges.
4. A **backdoor with C2** capabilities that can monitor the network and execute commands sent from a remote rootkit client. It incorporates multiple activation triggers so that these actions are transmitted stealthily.
5. A **rootkit client** that allows an attacker to establish 3 different types of shell-like connections to send commands and actions that control the rootkit state remotely.
6. A **persistence** module that ensures the rootkit remains installed maintaining full privileges even after a reboot event.
7. A **stealth** module that hides rootkit-related files and directories from the user.

## TripleCross overview

The following figure shows the architecture of TripleCross and its modules.

[![](https://blogger.googleusercontent.com/img/a/AVvXsEgRZ6H0xqq6KbEssmh0HkeVAWJvbzp16ctTmzOn118UcZRaRiEVLR__ZotG1oPIFheyW3IAUlRL_nd2ZtwL6DqdFz2JPX0y4jDz_spEvDTaqMKbjs48e-jJ6A3NktLdpQ-gwBee8LW745BCXazNCoWxbjQ3tgSXR6wla96lypiXEWG3nWsGgxvcwmY09Q=w640-h444)](https://blogger.googleusercontent.com/img/a/AVvXsEgRZ6H0xqq6KbEssmh0HkeVAWJvbzp16ctTmzOn118UcZRaRiEVLR__ZotG1oPIFheyW3IAUlRL_nd2ZtwL6DqdFz2JPX0y4jDz_spEvDTaqMKbjs48e-jJ6A3NktLdpQ-gwBee8LW745BCXazNCoWxbjQ3tgSXR6wla96lypiXEWG3nWsGgxvcwmY09Q)

The raw sockets library RawTCP\_Lib used for rootkit transmissions is of my authorship and has [its own repository](https://github.com/h3xduck/RawTCP_Lib "its own repository").

The following table describes the main source code files and directories to ease its navigation:

| DIRECTORY | COMMAND |
| --- | --- |
| docs | Original thesis document |
| src/client | Source code of the rootkit client |
| src/client/lib | RawTCP\_Lib shared library |
| src/common | Constants and configuration for the rootkit. It also includes the implementation of elements common to the eBPF and user space side of the rootkit, such as the ring buffer |
| src/ebpf | Source code of the eBPF programs used by the rootkit |
| src/helpers | Includes programs for testing the functionality of several rootkit modules, and also the malicious program and library used at the execution hijacking and library injection modules, respectively |
| src/libbpf | Contains the libbpf library integrated with the rootkit |
| src/user | Source code of the userland programs used by the rootkits |
| src/vmlinux | Headers containing the definition of kernel data structures (this is the recommended method when using libbpf) |

### Build and Install

#### Requirements

This [research project](https://www.kitploit.com/search/label/Research%20Project "research project") has been tested under the following environments:

|  | DISTRIBUTION | KERNEL | GCC | CLANG | GLIBC |
| --- | --- | --- | --- | --- | --- |
| **VERSION** | Ubuntu 21.04 | 5.11.0 | 10.3.0 | 12.0.0 | 2.33 |

We recommend using Ubuntu 21.04, which by default will incorporate the software versions shown here. Otherwise, some of the problems you may run into are described [here](https://github.com/h3xduck/TripleCross/issues/41#issuecomment-1176642139 "here").

#### Compilation

The rootkit source code is compiled using two Makefiles.

```
# Build rootkit
```

The following table describes the purpose of each Makefile in detail:

| MAKEFILE | COMMAND | DESCRIPTION | RESULTING FILES |
| --- | --- | --- | --- |
| src/client/Makefile | make | Compilation of the rootkit client | src/client/injector |
| src/Makefile | make help | Compilation of programs for testing rootkit capabilities, and the malicious program and library of the execution hijacking and library injection modules, respectively | src/helpers/simple\_timer, src/helpers/simple\_open, src/helpers/simple\_execve, src/helpers/lib\_injection.so, src/helpers/execve\_hijack |
| src/Makefile | make kit | Compilation of the rootkit using the libbpf library | src/bin/kit |
| src/Makefile | make tckit | Compilation of the rootkit TC egress program | src/bin/tc.o |

### Installation

Once the rootkit files are generated under src/bin/, the *tc.o* and *kit* programs must be loaded in order. In the following example, the rootkit backdoor will operate in the network interface *enp0s3*:

```
// TC egress program
sudo tc qdisc add dev enp0s3 clsact
sudo tc filter add dev enp0s3 egress bpf direct-action obj bin/tc.o sec classifier/egress
// Libbpf-powered rootkit
sudo ./bin/kit -t enp0s3
```

### Attack scenario scripts

There are two scripts, *packager.sh* and *deployer.sh*, that compile and install the rootkit automatically, just as an attacker would do in a real attack scenario.

* Executing packager.sh will generate all rootkit files under the *apps/* directory.
* Executing deployer.sh will install the rootkit and create the [persistence](https://www.kitploit.com/search/label/Persistence "persistence") files.

These scripts must first be configured with the following parameters for the proper functioning of the persistence module:

| SCRIPT | CONSTANT | DESCRIPTION |
| --- | --- | --- |
| src/helpers/deployer.sh | CRON\_PERSIST | Cron job to execute after reboot |
| src/he...