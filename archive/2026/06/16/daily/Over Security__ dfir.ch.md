---
title: | dfir.ch
url: https://dfir.ch/course/linux_rootkits/
source: Over Security
date: 2026-06-16
fetch_date: 2026-06-17T07:03:52.950246
---

# | dfir.ch

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

#

**Table of Contents**

* [[X] A (Short) History of Linux Rootkits](#x-a-short-history-of-linux-rootkits)
* [[X] Current Landscape](#x-current-landscape)
* [Userspace vs. Kernelspace](#userspace-vs-kernelspace)
* [[X] Application-Level Rootkits](#x-application-level-rootkits)
* [[X] Overview of Userland Rootkits](#x-overview-of-userland-rootkits)
  + [[Azazel](https://github.com/chokepoint/azazel)](#azazelhttpsgithubcomchokepointazazel)
  + [Symbiote](#symbiote)
  + [Orbit](#orbit)
  + [[Bedevil](https://github.com/Error996/bdvl)](#bedevilhttpsgithubcomerror996bdvl)
  + [[BEURK](https://github.com/unix-thrust/beurk)](#beurkhttpsgithubcomunix-thrustbeurk)
* [[X] LD\_PRELOAD](#x-ld_preload)
  + [Detection for LD\_PRELOAD](#detection-for-ld_preload)
  + [LD\_PRELOAD: libprocesshider](#ld_preload-libprocesshider)
* [[X] Analysis of Userland Rootkits](#x-analysis-of-userland-rootkits)
  + [Hooked Functions](#hooked-functions)
  + [Backdoor methods](#backdoor-methods)
  + [Hiding techniques](#hiding-techniques)
* [[X] Overview of Kernelspace Rootkits](#x-overview-of-kernelspace-rootkits)
  + [Diamorphine](#diamorphine)
  + [Reptile](#reptile)
  + [Syslogk](#syslogk)
  + [Adore-ng](#adore-ng)
* [[X] /dev/mem](#x-devmem)
* [[X] Loadable Kernel Modules (LKM)](#x-loadable-kernel-modules-lkm)
* [[X] eBPF](#x-ebpf)
* [[X] Hooking: Using Kprobes](#x-hooking-using-kprobes)
* [[X] Hooking: Using Uprobe](#x-hooking-using-uprobe)
* [[X] Hooking: Tracepoints](#x-hooking-tracepoints)
* [[X] Syscall table modification](#x-syscall-table-modification)
* [[X] ftrace](#x-ftrace)
* [[X] VFS (Virtual File System) manipulation](#x-vfs-virtual-file-system-manipulation)
* [[X] Detection Strategies for Linux Rootkits](#x-detection-strategies-for-linux-rootkits)
* [Look for unexpected kprobes loaded:](#look-for-unexpected-kprobes-loaded)

* [Monitoring](#monitoring)
  + [Tainted Kernels](#tainted-kernels)
  + [Command Line](#command-line)
  + [Disable](#disable)
  + [Linux Kernel Runtime Guard](#linux-kernel-runtime-guard)
  + [Memory](#memory)
  + [Varc - Test it](#varc---test-it)
* [[X] Overview of Tools](#x-overview-of-tools)
  + [Tracee](#tracee)
  + [nitara2](#nitara2)
  + [Syslog](#syslog)

* + [KProbes](#kprobes)
  + [More detections](#more-detections)

* [[X] Hardening](#x-hardening)
  + [Block loading](#block-loading)
  + [Disable](#disable-1)

* + [Sign eBPF programs](#sign-ebpf-programs)
* [[X] What else?](#x-what-else)
* [[X] References](#x-references)
  + [Presentations](#presentations)
  + [Blogs & Papers](#blogs--papers)
  + [Notes:](#notes)

## [X] A (Short) History of Linux Rootkits

Early rootkits were designed primarily to hide malicious processes or files, allowing attackers to maintain stealthy access to compromised systems. Initially, their capabilities were relatively simple, often targeting basic system directories or command utilities.

Over time, rootkits evolved in sophistication, exploiting more advanced techniques to bypass detection, including kernel-level manipulation and anti-forensic measures. In the next section, we will take a trip down the Linux rootkit memory lane.

2001: [KNARK Rootkit](https://web.archive.org/web/20021224232518/http%3A//online.securityfocus.com/guest/4871)

![TODO](/images/linux_rootkits/history_2001.png "TODO")

Figure X: Analysis of the KNARK Rootkit (2001)

2002: [The t0rn rootkit](https://www.giac.org/paper/gcih/321/t0rn-rootkit/103430)

![TODO](/images/linux_rootkits/history_2002.png "TODO")

Figure X: The t0rn rootkit (2002)

2004: [UNIX and Linux based Rootkits Techniques and Countermeasures](https://www.first.org/resources/papers/conference2004/c17.pdf)

![TODO](/images/linux_rootkits/history_2004.png "TODO")

Figure X: UNIX and Linux based Rootkits Techniques and Countermeasures (2004)

2006: [Detecting and categorizing kernel-level rootkits to aid future detection](https://colab.ws/articles/10.1109/msp.2006.11)

![TODO](/images/linux_rootkits/history_2006.png "TODO")

Figure X: Detecting and categorizing kernel-level rootkits to aid future detection

2011: [Rootkit Detection Mechanism: A Survey](https://www.researchgate.net/profile/Jestin-Joy-2/publication/216463350_Rootkit_Detection_Mechanism_A_Survey/links/0fcfd50dd917ba9538000000/Rootkit-Detection-Mechanism-A-Survey.pdf)

![TODO](/images/linux_rootkits/history_2011.png "TODO")

Figure X: Rootkit Detection Mechanism: A Survey

2012: [MoVP 2.4 Analyzing the Jynx rootkit and LD\_PRELOAD](https://volatility-labs.blogspot.com/2012/09/movp-24-analyzing-jynx-rootkit-and.html)

![TODO](/images/linux_rootkits/history_2012.png "TODO")

Figure X: MoVP 2.4 Analyzing the Jynx rootkit and LD\_PRELOAD

## [X] Current Landscape

![TODO](/images/linux_rootkits/landscape.png "TODO")

Figure X: Linux rootkit landscape and primary features

Source: [The Hidden Threat: Analysis of Linux Rootkit Techniques and Limitations of Current Detection Tools](https://dl.acm.org/doi/10.1145/3688808), Fraunhofer Institute for Communication, Information Processing and Ergonomics FKIE, JAKOB STÃHN, JAN-NICLAS HILGERT, and MARTIN LAMBERTZ

Also here: <https://github.com/milabs/awesome-linux-rootkits>

## Userspace vs. Kernelspace

TODO

## [X] Application-Level Rootkits

The [t0rn](https://www.giac.org/paper/gcih/321/t0rn-rootkit/103430) rookits swaps several key system binaries, amongst them ps, ls, netstat , top

Still a thing today..âIn our attacks the malware droppedÂ crontab,Â lsof,Â lddÂ andÂ top. These tweaked binaries will hide malicious activities, in case someone is using them.âperfctl: A Stealthy Malware Targeting Millions of Linux Servers, Aqua Blog, October 2024
Source:https://www.aquasec.com/blog/perfctl-a-stealthy-malware-targeting-millions-of-linux-servers/

## [X] Overview of Userland Rootkits

### [Azazel](https://github.com/chokepoint/azazel)

*Azazel is a userland rootkit based off of the original LD\_PRELOAD technique from Jynx rootkit. It is more robust and has additional features, and focuses heavily around anti-debugging and anti-detection.*

**Press Coverage**

* *The library used to hide Winntiâs system activity is a copy of the open-source userland rootkit Azazel, with minor changes. When executed, it will register symbols for multiple commonly used functions, including: open(), rmdir(), and unlink(), and modify their returns to hide the malwareâs operations.* [Chronicle Blog, 2019](https://medium.com/chronicle-blog/winnti-more-than-just-windows-and-gates-e4f03436031a)
* *Azazel rootkit is an open-source rootkit that targets older Linux kernels. Azazel is based on the LD\_PRELOAD technique. Figure 2 shows how the rootkit uses PAM APIs (pam\_open\_session, pam\_authenticate and pam\_acct\_mgmt()) to allow remote entry into the victimâs machine.* [Unit42 Blog, 2023](https://unit42.paloaltonetworks.com/linux-pam-apis/)
* *HiddenWasp authors have adopted a large amount of code from various publicly available open-source malware, such as Mirai and the Azazel rootkit.* [Intezer Blog, 2019](https://intezer.com/blog/research/hiddenwasp-malware-targeting-linux-systems/)

### Symbiote

Not public available - sold on underground markets.

**Press Coverage**

* *Instead of being a standalone executable file that is run to infect a machine, it is a shared object (SO) library that is loaded into all running processes using LD\_PRELOAD, and parasitically infects the machine. Once it has infected all the running processes, it provides the threat actor with rootkit functionality, the ability to harvest credentials, and remote access capability.* [Intezer Blog, 2022](https://intezer.com/blog/research/new-linux-threat-symbiote/)

### Orbit

Not public available - sold on underground markets.

**Press Coverage**

* *To install the payload and add it to the shared libraries that are being loaded by the dynamic linker, the dropper calls a function called pa...