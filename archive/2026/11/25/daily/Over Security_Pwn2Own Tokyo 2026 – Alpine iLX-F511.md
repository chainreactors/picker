---
title: Pwn2Own Tokyo 2026 – Alpine iLX-F511
url: https://blog.compass-security.com/2026/11/pwn2own-tokyo-2026-alpine-ilx-f511/
source: Over Security
date: 2026-11-25
fetch_date: 2026-11-26T10:14:52.975062
---

# Pwn2Own Tokyo 2026 – Alpine iLX-F511

## [Compass Security Blog](https://blog.compass-security.com "Compass Security Blog — Offensive Defense")

### Offensive Defense

* [Home](https://blog.compass-security.com/)
* [Archive](https://blog.compass-security.com/archive/)
* [Contact](https://blog.compass-security.com/contact/)
* [Newsletter](https://blog.compass-security.com/mailing-list-tigerinfo/)

* [Home](https://blog.compass-security.com/)
* [Archive](https://blog.compass-security.com/archive/)
* [Contact](https://blog.compass-security.com/contact/)
* [Newsletter](https://blog.compass-security.com/mailing-list-tigerinfo/)

# [Pwn2Own Tokyo 2026 – Alpine iLX-F511](https://blog.compass-security.com/2026/11/pwn2own-tokyo-2026-alpine-ilx-f511/ "Pwn2Own Tokyo 2026 – Alpine iLX-F511")

[November 25, 2026](https://blog.compass-security.com/2026/11/pwn2own-tokyo-2026-alpine-ilx-f511/ "Pwn2Own Tokyo 2026 – Alpine iLX-F511")
 /
[Yves Bieri](https://blog.compass-security.com/author/ybieri/)
 /
[0 Comments](https://blog.compass-security.com/2026/11/pwn2own-tokyo-2026-alpine-ilx-f511/#respond)

## Introduction

Compass Security has been competing in Pwn2Own Small Office / IoT since 2023. In 2025, we registered for the first time for Pwn2Own Automotive but unfortunately failed our attempt on stage because of a small mistake. Our payload was one byte too long as the IP address at the competition was longer than the one we had tested with during preparation, and we failed to realize it on stage. So, when ZDI announced that Pwn2Own Automotive 2026 would take place in Tokyo this January, we were eager to prove that we could also succeed in the Automotive competition.

The targets for Pwn2Own automotive included In-Vehicle Infotainment (IVI) systems, electric chargers, automotive operating systems, and more. As the research had to be done around the busy Christmas time, we decided to limit ourselves to two targets: the Alpine IVI, against which we failed the year before, and the Grizzl-E charger, which was a new target for this year’s competition.

In this first blog, we’ll cover the vulnerability we exploited against the Alpine IVI.

## Alpine iLX-F511

**Overview**

The latest firmware for the Alpine when we started the research was version `A.25.D0.07.00.00.00`. This was a newer version than the one we looked at the year before. After some analysis, we concluded though that not many security relevant changes had been made.

[![](https://blog.compass-security.com/wp-content/uploads/2026/06/5109b993-b8b0-43f1-8d21-5b03e15bfb431-1024x768.jpg)](https://blog.compass-security.com/wp-content/uploads/2026/06/5109b993-b8b0-43f1-8d21-5b03e15bfb431-scaled.jpg)

In general, Alpine did not fix any of the RCE bugs reported in previous Pwn2Own competitions. Thus, our firmware decryption script based on NCC Group’s work ([link](https://www.nccgroup.com/research/romhack-revving-up-the-journey-to-pwn2own-automotive-2024/)) and our exploit from the previous year got us the firmware and a shell very quickly.

**Attack Surface**

The attack surfaces of IVIs are large compared to the IoT targets we were used to. For the competition, it was valid to target the exposed network ports, the Bluetooth interface, the USB ports, and anything reachable through clicking on the display. From the previous contest we knew that the contact import feature was prone to memory corruption. However, as Alpine did not fix their previous bugs, it was very hard for us to discern if a crash our fuzzer found was a new vulnerability or a duplicate. This year, the vulnerabilities disclosed against Alpine the previous years were explicitly marked as out of scope, as in the last years some team used those against the Alpine. Thus, we decided to focus on different attack surfaces.

A quick nmap scan shows that the Alpine IVI exposes the following network ports:

```
$ nmap -p- <TARGET_IP>
PORT      STATE SERVICE
22/tcp    open  ssh
2086/tcp  open  gnunet
3490/tcp  open  colubris
5355/tcp  open  llmnr
30515/tcp open  unknown
```

What surprised us is that SSH was exposed. This was not the case with the previous year’s firmware. This was especially interesting, as we cracked/guessed the password of the low-privileged user telechips the year before. While we did not find a way to abuse this user the year before, the exposed SSH would provide a new entry point to look at.

As the SSH config allows password-based authentication, we had initial access to the device.

```
$ cat /etc/sshd_config
Port 22
ListenAddress 0.0.0.0
PermitRootLogin yes
PasswordAuthentication yes
PermitEmptyPasswords yes
```

There was just one issue. The Pwn2Own rules state “If the entry leverages hardcoded credentials and/or exposed encryption keys, the entry must leverage an additional vulnerability to gain code execution to be in scope.”. Thus, we had to find a way to escalate to root or ideally find a vulnerability that doesn’t leverage the hardcoded credentials at all.

When looking at the authenticated attack surface, the netstat output reveals an internal service listening on localhost on port 2009:

```
$ netstat -tulpn
Active Internet connections (only servers)
Proto Recv-Q Send-Q Local Address     Foreign Address         State       PID/Program name
tcp        0      0 0.0.0.0:30515     0.0.0.0:*       LISTEN      670/aoa_con_server_
tcp        0      0 127.0.0.1:2009    0.0.0.0:*       LISTEN      382/widgets --remot
tcp        0      0 0.0.0.0:2086      0.0.0.0:*       LISTEN      386/framework-servi
tcp        0      0 0.0.0.0:5355      0.0.0.0:*       LISTEN      260/systemd-resolve
tcp        0      0 :::22             :::*            LISTEN      1/systemd
tcp        0      0 :::3490           :::*            LISTEN      235/dlt-daemon
tcp        0      0 :::5355           :::*            LISTEN      260/systemd-resolve
udp        0      0 0.0.0.0:5353      0.0.0.0:*                   271/mdnsd
udp        0      0 0.0.0.0:5355      0.0.0.0:*                   260/systemd-resolve
udp        0      0 127.0.0.53:53     0.0.0.0:*                   260/systemd-resolve
udp        0      0 0.0.0.0:68        0.0.0.0:*                   1078/dhclient
udp        0      0 0.0.0.0:68        0.0.0.0:*                     1058/dhclient
udp        0      0 0.0.0.0:42898     0.0.0.0:*                   271/mdnsd
udp        0      0 :::5353           :::*                        271/mdnsd
udp        0      0 :::5355           :::*                        260/systemd-resolve
udp        0      0 :::54642          :::*                        271/mdnsd
```

Using the `telechips` user’s credentials, we can establish an SSH port forwarding to expose this internal port:

`ssh -L 2009:127.0.0.1:2009 telechips@<TARGET_IP>`

**Discovery of Chrome DevTools Protocol**

The process listening on port 2009 is the main UI application (called `fiv` internally) of the IVI. The UI component is implemented using the Chromium Embedded Framework (CEF) for human machine interaction (HMI). It communicates with the framework-service binary to relay different events, e.g. touchscreen interactions, to the operating system.

The process exposes the Chrome DevTools Protocol (CDP) on port 2009 via the `--remote-debugging-port` flag. Also note that the process is started with the `--no-sandbox` flag, which disables Chromium’s security sandbox:

```
/opt/app/ve5/fiv45/fiv --no-sandbox --lua-dir=/opt/app/ve5/lua
  --search-dir=/opt/app/ve5/widgets --remote-debugging-port=2009
  --emulate-touch --enable-v8-cache --num-raster-threads=4
  --disable-accelerated-2d-canvas --disable-extensions
```

This is something we briefly looked at the year before but discarded as we had no reliable way of communicating with the internally exposed port. As this had changed now, we decided to dig in once again and analyze this in more detail.

Thanks to the SSH port forwarding, we can now reach this debugging port. The CDP interface can be accessed by visiting `chrome://inspect/#devices` or by directly connecting to the WebSocket endpoin...