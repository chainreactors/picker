---
title: Sysrv Infection (Linux Edition)
url: https://dfir.ch/posts/sysrv/
source: Over Security - Cybersecurity news aggregator
date: 2024-08-31
fetch_date: 2025-10-06T18:08:05.572849
---

# Sysrv Infection (Linux Edition)

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

# Sysrv Infection (Linux Edition)

14 Apr 2024

**Table of Contents**

* [Introduction](#introduction)
* [Loader](#loader)
* [GO-Binary Reversing](#go-binary-reversing)
* [strace](#strace)
* [Exploits](#exploits)
* [And the moral of the story is …](#and-the-moral-of-the-story-is-)
* [Outlook](#outlook)

## Introduction

On a recent incident response case, a customer contacted us regarding their EDR detecting a crypto miner on a Linux endpoint. The identified malicious file, named **41hs1z**, is accessible on [VirusTotal](https://www.virustotal.com/gui/file/24788e4f29cc4c28e92bb0aad2c3f7d56666f850afbc6eb02957f066b99d6fb3). The folders and paths associated with each execution of the crypto miner may differ; however, here are some paths we encountered:

* /backup/files/excel/41hs1z
* /backup/files/xml/dotnet115/BeID/41hs1z
* /backup/files/xml/dotnet115/layouts/defaults/41hs1z

Upon analysis, we discovered that the malware is a component of the **Sysrv** botnet. In this short blog post, we will examine the ELF binary to uncover its capabilities and identify IOCs associated with the sample.

For further insights into Sysrv, we recommend referring to the following three informative blog posts:

* [Crypto miner attack â Sysrv-Hello Botnet targeting WordPress pods (sysdig.com)](https://sysdig.com/blog/crypto-sysrv-hello-wordpress/)
* [Not Another Coin Miner (ultimacybr.co.uk)](https://ultimacybr.co.uk/2023-10-04-Sysrv/)
* [The Sysrv Botnet and How It Evolved (cujo.com)](https://cujo.com/blog/the-sysrv-botnet-and-how-it-evolved/)

## Loader

At the time of writing this blog post, the loader script remains available online at http://194.38.23.2/ldr[.]sh ([VirusTotal](https://www.virustotal.com/gui/file/872faff822551dcecad301d1024420ccb7182019797124cdd8693a18fa8655a9)). This shell script was executed on the target host, presumably after exploiting a vulnerability in the internet-facing web application. While the server was no longer accessible for a thorough investigation, we discovered traces of the script’s execution.
![Part of the ldr.sh file](/images/sysrv/ldr.png "Part of the ldr.sh file")

Figure 1: Part of the ldr.sh file

Many other blogs, including [UltimaCybr’s](https://ultimacybr.co.uk/2023-10-04-Sysrv/), have thoroughly examined the loader script (which is why we won’t duplicate the analysis here). One notable difference in our case is that the loader does not possess the capabilities to gather and use SSH keys for subsequent propagation, as highlighted in a report by [TheDFIRReport](https://thedfirreport.com/2023/12/18/lets-opendir-some-presents-an-analysis-of-a-persistent-actors-activity/).

*A recovered version of this script shows that it uses a clever technique for self-propagation on Linux. In addition to disabling UFW and killing several running services, the script then turns to enumerating all the private keys stored on the hosts, parsing all the hosts in the known\_hosts files, as well as username associated with any keys found.*

## GO-Binary Reversing

Upon opening the binary with Ghidra, we are presented with… not much information. The functions pane appears largely empty.
![Functions within Ghidra](/images/sysrv/functions_basic.png "Functions within Ghidra")

Figure 2: Functions within Ghidra

Additionally, the included strings from the binary do not make much sense.
![Defined strings within Ghidra](/images/sysrv/strings_basic.png "Defined strings within Ghidra")

Figure 3: Defined strings within Ghidra

[Dorka Palotay](https://www.linkedin.com/in/padorka/) wrote an excellent article titled **Reverse Engineering Go Binaries with Ghidra**, shedding light on why extracting strings from our GO binary poses challenges. After reading about the problems in the blog of Dorka, I stumbled upon the [GhidraScripts](https://github.com/advanced-threat-research/GhidraScripts) maintained by [Max Kersten](https://www.linkedin.com/in/libranalysis/). After loading the scripts into the Script Manager from Ghidra and running them (the GhidraScripts GitHub repository contains a README that will guide through every step), the magic behind those scripts found more function names and readable strings (Figure 4).
![Script Manager within Ghidra](/images/sysrv/script_manager.png "Script Manager within Ghidra")

Figure 4: Script Manager within Ghidra

Returning to the functions pane, we now have function names that are more or less meaningful:
![More functions within Ghidra<](/images/sysrv/functions_elaborated.png "More functions within Ghidra<")

Figure 5: More functions within Ghidra

Performing the same search for “cron,” as previously demonstrated (refer to Figure 3), yields more meaningful results:
![Readable strings within Ghidra](/images/sysrv/strings_elaborated.png "Readable strings within Ghidra")

Figure 6: Readable strings within Ghidra

## strace

We utilize strace for the dynamic analysis of the malware. See my post [[s|l]trace - Linux Malware Analysis](https://dfir.ch/posts/strace/) as a strace primer. Upon executing the binary in a controlled environment (with strace and logging activated), the binary operates under the name **kthreaddk**, a frequently observed identifier for this strain of malware, as numerous Google search results indicate infections attributed to Sysrv.

```
2530  execve("./9d9150e2def883bdaa588b47cf5300934ef952bea3acd5ad0e86e1deaa7d89c5", ["./9d9150e2def883bdaa588b47cf5300934ef952bea3acd5ad0e86e1deaa7d89c5"], 0x7fff61b40138 /* 17 vars */) = 0
2537  execve("kthreaddk", ["kthreaddk"], 0xc420138090 /* 17 vars */ <unfinished ...>
```

**Persistence**

One of the initial steps following execution involves establishing persistence through a cronjob, utilizing randomized paths, as we will explore subsequently. Take note of the string “/usr/bin/crontab -,” which matches the string we uncovered within Ghidra after utilizing the Ghidra Scripts to extract readable strings from the binary (refer to Figure 6).

```
2550  execve("/bin/sh", ["/bin/sh", "-c", "echo '* * * * * /dev/disk/by-partuuid/3hxr47' | /usr/bin/crontab -"], 0xc420138120 /* 17 vars */ <unfinished ...>
```

**Mutex**

At intervals of one minute, the sample establishes a connection to localhost through a predetermined port (in our instance, 51933). The malware refrains from re-infecting the system if the port is open.

```
src_port = 44388
dst_ip = 0.0.0.0
dst_port = 51933
protocol = TCP
```

**Process listing**

The binary is copied around to different paths. Here’s an example of running *ps* on the infected machine, revealing the malicious binary executed under the following path: */etc/apparmor.d/abstractions/ubuntu-browsers.d/3hxr47*.

```
# ps aux

root 3711  0.0  0.0   2616   496 ? Ss 15:12 0:00 /bin/sh -c /etc/apparmor.d/abstractions/ubuntu-browsers.d/3hxr47
root 3712  2.4  2.8 115804 100868 ? Sl 15:12 1:06 /etc/apparmor.d/abstractions/ubuntu-browsers.d/3hxr47
```

**Cron Jobs**

The various and changing paths of the malware are recorded within the cron log files, as illustrated in the following excerpt:

```
Feb 18 15:11:01 miner cron[752]: (root) RELOAD (crontabs/root)
Feb 18 15:11:01 miner CRON[3692]: (root) CMD (/etc/apparmor.d/abstractions/ubuntu-browsers.d/3hxr47)
Feb 18 15:12:01 miner CRON[3711]: (root) CMD (/etc/apparmor.d/abstractions/ubuntu-browsers.d/3hxr47)
Feb 18 15:12:03 miner crontab[3725]: (root) REPLACE (root)
Feb 18 15:13:01 miner CRON[3819]: (root) CMD (/dev/block/mujqjo)
Feb 18 15:13:04 miner crontab[3830]: (root) REPLACE (root)
Feb 18 15:14:01 miner cron[752]: (root) RELOAD (crontabs/root)
```

**config.json**

Steven Folek ([@Pir00t](https://twitter.com/Pir00t)) used the *watch* command in his blog post (see the link in the introduction section) to fetch a copy of the *config.json* file. We can employ strace once more to observe the contents of the JSON file as it’s being written to disk. However, we need to augment the...