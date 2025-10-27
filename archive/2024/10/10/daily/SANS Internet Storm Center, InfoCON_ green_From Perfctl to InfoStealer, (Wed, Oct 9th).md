---
title: From Perfctl to InfoStealer, (Wed, Oct 9th)
url: https://isc.sans.edu/diary/rss/31334
source: SANS Internet Storm Center, InfoCON: green
date: 2024-10-10
fetch_date: 2025-10-06T18:57:16.760264
---

# From Perfctl to InfoStealer, (Wed, Oct 9th)

# [Internet Storm Center](/)

[Sign In](/login.html)
[Sign Up](/register.html)

Handler on Duty: [Johannes Ullrich](/handler_list.html#johannes-ullrich "Johannes Ullrich")

Threat Level: [green](/infocon.html)

* [previous](/diary/31330)
* [next](/diary/31336)

My next class:

|  |  |  |
| --- | --- | --- |
| [Reverse-Engineering Malware: Advanced Code Analysis](https://www.sans.org/event/live-online-europe-october-2025/course/reverse-engineering-malware-advanced-code-analysis) | Online | Greenwich Mean Time | Oct 27th - Oct 31st 2025 |

# [From Perfctl to InfoStealer](/forums/diary/From%2BPerfctl%2Bto%2BInfoStealer/31334/)

**Published**: 2024-10-09. **Last Updated**: 2024-10-09 07:18:37 UTC
**by** [Xavier Mertens](/handler_list.html#xavier-mertens) (Version: 1)

[0 comment(s)](/diary/From%2BPerfctl%2Bto%2BInfoStealer/31334/#comments)

A few days ago, a new stealthy malware targeting Linux hosts made a lot of noise: perfctl[[1](https://www.aquasec.com/blog/perfctl-a-stealthy-malware-targeting-millions-of-linux-servers/)]. The malware has been pretty well analyzed and I won’t repeat what has been already disclosed. I found a copy of the "httpd" binary (SHA256:22e4a57ac560ebe1eff8957906589f4dd5934ee555ebcc0f7ba613b07fad2c13)[[2](https://www.virustotal.com/gui/file/22e4a57ac560ebe1eff8957906589f4dd5934ee555ebcc0f7ba613b07fad2c13)]. I dropped the malware in my lab to see how it detonated. I infected the lab without root privileges and detected the same behavior except files were not written to some locations due to a lack of access (not root). When executing without root privileges, the rootkit feature is unavailable and the malware runs "disclosed".

![](https://isc.sans.edu/diaryimages/images/isc-20241009-1.png)

After the sandbox infection, I had two running processes:

* perfctl
* gnome-session-binary (This name can be different and mimic well-known Linux processes)

The resources used by the two processes are:

```

remnux@remnux:/$ sudo lsof -p 2637
COMMAND    PID   USER   FD      TYPE             DEVICE SIZE/OFF    NODE NAME
gnome-ses 2637 remnux  cwd       DIR                8,5     4096 1967470 /var/tmp/test
gnome-ses 2637 remnux  rtd       DIR                8,5     4096       2 /
gnome-ses 2637 remnux  txt       REG                8,5  9301499 2498448 /tmp/.perf.c/gnome-session-binary (deleted)
gnome-ses 2637 remnux  mem       REG                8,5 21444668  794483 /tmp/.xdiag/tordata/cached-microdescs
gnome-ses 2637 remnux  mem       REG                8,5     3552 2245832 /usr/share/zoneinfo/America/New_York
gnome-ses 2637 remnux    0r      CHR                1,3      0t0       6 /dev/null
gnome-ses 2637 remnux    1w      CHR                1,3      0t0       6 /dev/null
gnome-ses 2637 remnux    2w      CHR                1,3      0t0       6 /dev/null
gnome-ses 2637 remnux    3u     IPv4             186838      0t0     TCP remnux:44010->tor-exit-read-me.dfri.se:http (ESTABLISHED)
gnome-ses 2637 remnux    4u  a_inode               0,14        0   12517 [eventpoll]
gnome-ses 2637 remnux    5r     FIFO               0,13      0t0   58960 pipe
gnome-ses 2637 remnux    6w     FIFO               0,13      0t0   58960 pipe
gnome-ses 2637 remnux    7u     unix 0xffff8b2abaa0dc00      0t0   71705 type=STREAM
gnome-ses 2637 remnux    8u     unix 0xffff8b2abaa09800      0t0   58991 /tmp/.xdiag/int/.per.s type=STREAM
gnome-ses 2637 remnux    9u     unix 0xffff8b2abaa0e000      0t0   71704 type=STREAM
gnome-ses 2637 remnux   10u  a_inode               0,14        0   12517 [eventpoll]
gnome-ses 2637 remnux   11r     FIFO               0,13      0t0   71706 pipe
gnome-ses 2637 remnux   12w     FIFO               0,13      0t0   71706 pipe
gnome-ses 2637 remnux   13uW     REG                8,5        0  794471 /tmp/.xdiag/tordata/lock
gnome-ses 2637 remnux   14u     IPv4              68064      0t0     TCP localhost:37959 (LISTEN)
gnome-ses 2637 remnux   15u     IPv4              71708      0t0     TCP localhost:63582 (LISTEN)
gnome-ses 2637 remnux   16u     IPv4             187544      0t0     TCP localhost:44870->localhost:46606 (ESTABLISHED)
gnome-ses 2637 remnux   17u     IPv4             187546      0t0     TCP localhost:48816->localhost:63582 (ESTABLISHED)
gnome-ses 2637 remnux   18u     IPv4             187547      0t0     TCP localhost:63582->localhost:48816 (ESTABLISHED)
gnome-ses 2637 remnux   19u     IPv4              68080      0t0     TCP remnux:42126->tor-exit.exs.no:https (ESTABLISHED)
gnome-ses 2637 remnux   20r     FIFO               0,13      0t0  187612 pipe
gnome-ses 2637 remnux   21u     IPv4              71788      0t0     TCP localhost:44870 (LISTEN)
gnome-ses 2637 remnux   22u     IPv4              71790      0t0     TCP localhost:44869 (LISTEN)
gnome-ses 2637 remnux   23w     FIFO               0,13      0t0  187612 pipe
gnome-ses 2637 remnux   24r     FIFO               0,13      0t0  187613 pipe
gnome-ses 2637 remnux   25w     FIFO               0,13      0t0  187613 pipe

remnux@remnux:/$ sudo lsof -p 2791
COMMAND  PID   USER   FD      TYPE             DEVICE SIZE/OFF    NODE NAME
perfctl 2791 remnux  cwd       DIR                8,5     4096       2 /
perfctl 2791 remnux  rtd       DIR                8,5     4096       2 /
perfctl 2791 remnux  txt       REG                8,5  1727132 2498457 /tmp/.perf.c/perfctl
perfctl 2791 remnux    0r      CHR                1,3      0t0       6 /dev/null
perfctl 2791 remnux    1w      CHR                1,3      0t0       6 /dev/null
perfctl 2791 remnux    2w      CHR                1,3      0t0       6 /dev/null
perfctl 2791 remnux    3u  a_inode               0,14        0   12517 [eventpoll]
perfctl 2791 remnux    4r     FIFO               0,13      0t0   68184 pipe
perfctl 2791 remnux    5w     FIFO               0,13      0t0   68184 pipe
perfctl 2791 remnux    6r     FIFO               0,13      0t0   71857 pipe
perfctl 2791 remnux    7u     unix 0xffff8b2abaa0dc00      0t0   71705 type=STREAM
perfctl 2791 remnux    8w     FIFO               0,13      0t0   71857 pipe
perfctl 2791 remnux    9u  a_inode               0,14        0   12517 [eventfd]
perfctl 2791 remnux   10u  a_inode               0,14        0   12517 [eventfd]
perfctl 2791 remnux   11u  a_inode               0,14        0   12517 [eventfd]
perfctl 2791 remnux   12r      CHR                1,3      0t0       6 /dev/null
perfctl 2791 remnux   13u     IPv4             186859      0t0     TCP localhost:46606->localhost:44870 (ESTABLISHED)
```

That's exactly what has been described in the initial malware analysis: Tor is used for external communications and inter-process communications ate performed via sockets:

```

tor-exit-read-me.dfri.se:443 <-> (:42126) gnome-session-binary (127.0.0.1:46606) <-> (127.0.0.1:44870) perfctl
```

The malware also implants a backdoor allowing remote access to the Attacker.

Indeed, after approximately 30 minutes, I saw more activity ongoing. The Attacker dropped and executed a bunch of scripts to perform a footprint of the compromised host, search for interesting files/credentials, and exfiltrate them. All files were dropped in a sub-directory in the infected user's home directory:

```

remnux@remnux:~/.atmp/tmp/.applocal.xdiag$ ls -al
total 2752
drwx------  1 remnux  remnux   32768  8 Oct 14:34 .
drwx------  1 remnux  remnux   32768  8 Oct 10:03 ..
-rwx------  1 remnux  remnux      36  8 Oct 09:26 aa.txt
-rwx------  1 remnux  remnux       0  8 Oct 09:06 cloud_meta.txt
-rwx------  1 remnux  remnux      64  8 Oct 09:26 debug.txt
drwx------  1 remnux  remnux   32768  8 Oct 09:07 docker
-rwx------  1 remnux  remnux    7745  8 Oct 09:24 environs.txt
-rwx------  1 remnux  remnux  208084  8 Oct 09:07 files.txt
drwx------  1 remnux  remnux   32768  8 Oct 09:20 files_other
drwx------  1 remnux  remnux   32768  8 Oct 09:20 files_th
-rwx------  1 remnux  remnux       0  8 Oct 09:13 foi.cry.txt
-rwx------  1 remnux  remnux       0  8 Oct 09:13 foi.fds.txt
-rwx------  1 remnux  remnux     61...