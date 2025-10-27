---
title: Disabling ClamAV as an Unprivileged User
url: https://buaq.net/go-150108.html
source: unSafe.sh - 不安全
date: 2023-02-20
fetch_date: 2025-10-04T07:32:27.079304
---

# Disabling ClamAV as an Unprivileged User

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

![](https://8aqnet.cdn.bcebos.com/89877441b85d209e14f3a7846755e22b.jpg)

Disabling ClamAV as an Unprivileged User

About The ProjectClamAV is an Open Source antivirus engine that is w
*2023-2-19 08:0:0
Author: [www.archcloudlabs.com(查看原文)](/jump-150108.htm)
阅读量:29
收藏*

---

## About The Project

[ClamAV](https://www.clamav.net/) is an Open Source antivirus engine that is widely used on mail servers to scan incoming messages. On February 15, 2023 ClamAV [published a security advisory](https://blog.clamav.net/2023/02/clamav-01038-01052-and-101-patch.html) detailing a potential remote code execution vulnerability in its HFS+ file parser. This vulnerability was given the CVE identifier of [CVE-2023-20032](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-20032). While reading about this vulnerability, I stumbled across an [open pull request](https://github.com/Cisco-Talos/clamav/pull/347) indicating that its possible for non-privileged users to disable clamav. This blog post explores the underlying bug, how to disable ClamAV manually, and finally building a Metasploit module to automate this process.

![logo_clamav.png](https://www.archcloudlabs.com/projects/disabling-clamav-as-unprivileged-user/logo_clamav.png)

## More Eyes Leads to Bug Discovery

When reading about CVEs, and associated bugs in a given piece of software, its not-uncommon to discover additional bugs. As the industry saw with [CVE-2022-44228](https://nvd.nist.gov/vuln/detail/CVE-2021-44228)(Log4Shell), some patches were incomplete leading to continued exploitation of the Log4J library during December of 2021 and additional CVEs ([1](https://www.cve.org/CVERecord?id=CVE-2021-44228),[2](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-45105),[3](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-4104)). For Open Source software, this is especially true given that the code is easily available for researchers/sysadmins/developers/etc… to look at. Exploring open pull requests within [clamav](https://github.com/Cisco-Talos/clamav), led to discovering an existing pull request with an interesting [title](https://github.com/Cisco-Talos/clamav/pull/347) of “Check for root user when processing SHUTDOWN command.” Immediately, this captured my attention as typically any anti-virus solution runs as a privileged user and disabling this outright as a non-privileged user is a pretty nasty vulnerability. For the ATT&CK aficionados reading today this is [T1562.001](https://attack.mitre.org/techniques/T1562/001/), Impair Defenses: Disable or Modify Tools. The image below shows this bug originally being discovered and reported by [Todd Rinaldo](https://github.com/toddr). After reading this PR and examining the issue we’re left with the following question “if I, as an unprivileged user can shutoff the daemon, can I do….anything else?”. Lets explore!

![pr.png](https://www.archcloudlabs.com/projects/disabling-clamav-as-unprivileged-user/pr.png)

## Creating The Environment

ClamAV is available in the majority of repositories for Linux distributions. Simple installing with your package manager should lead you to setting up an environment described below. For my demonstration, I’ll be using [Vagrant](https://vagrant.com) to create a clean Arch Linux environment to test with.
This is accomplished with the following commands below.

```
$> vagrant box add archlinux/archlinux;
$> vagrant init; // Create Vagrant template
$> vagrant up;   // start Archlinux vm
$> vagrant ssh;  // login to newly created machine
```

Next, we’ll sync the package database and install ClamAV.

```
$> pacman -Syy; // sync packages
$> pacman -Ss clamav;
extra/clamav 1.0.0-1
    Anti-virus toolkit for Unix

$> pacman -S clamav; // install clamav
```

Now that ClamAV is installed, the next step is to execute the `freshclam` command to download the latest signatures before starting the daemon.

```
$> sudo freshclam;
$> sudo clamd; //manually starting the service, you could also leverage systemd to start this.
```

At this point, a fresh environment within vagrant has been established to poke at ClamAV.

## Examining The Bug

According to the pull request, any user can interact with the ClamAV socket to disable the daemon.
With `clamd`, the ClamAV daemon running in the background we’ll explore open files this process has to identify the attack surface.

```
$> lsof -p `pidof clamav`
```

The [lsof](https://man7.org/linux/man-pages/man8/lsof.8.html) command lists open files of a given process, user, etc… depending on user specified flags.
The command above will list all open files for a given process id. The string captures within the backticks of `pidof clamav` will return a integer indicating the process id of clamav, and then give the open files of the process. The abbreivated image below shows a unix socket, hmmmmmmm let’s investigate further!

![clam_av_disable.png](https://www.archcloudlabs.com/projects/disabling-clamav-as-unprivileged-user/clam_av_disable.png)

As a refresher, [sockets](https://man7.org/linux/man-pages/man2/socket.2.html) are a form of communication on Linux. Typically, when talking about sockets, one tends to think about network communication, AF\_INET sockets are used for network based communication. However, [Unix sockets](https://man7.org/linux/man-pages/man7/unix.7.html) enable the developer to use the same type of syscalls (read/write/etc…) for achieving interprocess communication without listening on a port and handling all of the additional overhead of sending data over a network connection. Just like poking at open ports with netcat, we can also leverage netcat to interact with unix sockets and start understanding our attack surface with ClamAV.

Next steps, lets see the file permissions on this socket file.
![clamd_file_perms.png](https://www.archcloudlabs.com/projects/disabling-clamav-as-unprivileged-user/clamd_file_perms.png)

Whoa! look at that, the file permissions permit **ANYONE** to read or write to this file. Thus, a non-privileged user will be able to issue commands such as SHUTDOWN to result in disabling ClamAV scanning. Additional commands that can be executed can be seen via `man clamd`. The image below demonstrates achieving shutting off the ClamAV daemon manually via netcat.

![shutdown_clam.png](https://www.archcloudlabs.com/projects/disabling-clamav-as-unprivileged-user/shutoff_clam.png)

The crux of the issue is a user needs be able to trigger file scans, thus writing to this domain socket is required. Typically this functionality is triggered through [clamscan](https://linux.die.net/man/1/clamscan). However, there’s no restrictions on what commands can be executed by an end user. Therefore, commands that result in disabling default behavior (ex: shutdown) should require elevated permissions, and that is exactly what the pull request is addressing.

## Automating The Exploitation

The Metasploit framework contains an [auxiliary module](https://github.com/rapid7/metasploit-framework/blob/master/modules/auxiliary/scanner/misc/clamav_control.rb) for executing commands against the ClamAV daemon **if** the daemon is listening on an interface (AF\_INET socket). However, in this situation we want to execute against a unix socket, with less than 60 lines of Ruby, we have a new post-execution module that is captured below and [in my repo as well](https://github.com/rapid7/metasploit-framework/blob/f61c3bcefc376d72631ae4f8fcfa5895d462d44c/modules/post/linux/manage/disable_clamav.rb).

```
require "socket"
 class MetasploitModule < Msf::Post
   Rank = ExcellentRanking

   include Msf::Post::File
   include Msf::Post::Unix

   def initializ...