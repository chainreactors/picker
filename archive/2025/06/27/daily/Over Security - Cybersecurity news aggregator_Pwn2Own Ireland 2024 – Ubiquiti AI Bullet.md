---
title: Pwn2Own Ireland 2024 – Ubiquiti AI Bullet
url: https://blog.compass-security.com/2025/06/pwn2own-ireland-2024-ubiquiti-ai-bullet/
source: Over Security - Cybersecurity news aggregator
date: 2025-06-27
fetch_date: 2025-10-06T22:56:42.953076
---

# Pwn2Own Ireland 2024 – Ubiquiti AI Bullet

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

# [Pwn2Own Ireland 2024 – Ubiquiti AI Bullet](https://blog.compass-security.com/2025/06/pwn2own-ireland-2024-ubiquiti-ai-bullet/ "Pwn2Own Ireland 2024 – Ubiquiti AI Bullet")

[June 26, 2025](https://blog.compass-security.com/2025/06/pwn2own-ireland-2024-ubiquiti-ai-bullet/ "Pwn2Own Ireland 2024 – Ubiquiti AI Bullet")
 /
[Yves Bieri](https://blog.compass-security.com/author/ybieri/ "Posts by Yves Bieri")
 /
[0 Comments](https://blog.compass-security.com/2025/06/pwn2own-ireland-2024-ubiquiti-ai-bullet/#respond)

## Introduction

As you may know, Compass Security participated in the 2023 edition of the Pwn2Own contest in Toronto and was able to successfully compromise the Synology BC500 camera using a remote code execution vulnerability. If you missed this, head over to the blog post here <https://blog.compass-security.com/2024/03/pwn2own-toronto-2023-part-1-how-it-all-started/>

Unfortunately, the same vulnerability was also identified by other researchers, resulting in a so-called collision. So naturally, we wanted to participate again in 2024, hoping to find a unique exploit in one of the available targets.

As Trend Micro had closed their office in Toronto, the 2024 edition would take place in Cork, Ireland. This time all participants must be on-site which we were looking forward to, having had lots of interesting discussions with the on-site teams the previous year. <https://www.zerodayinitiative.com/blog/2024/7/16/announcing-pwn2own-ireland-2024>

## Target Selection

While in 2023 the Compass employees taking part in Pwn2Own pooled their company provided research time and focused on a single device, in the 2024 edition we approached the event by looking at multiple available targets. This included the Lorex 2K indoor Wi-Fi security camera, the Ubiquiti AI Bullet surveillance camera, the AeoTec Smart Home Hub, as well as the Synology BeeStation BST150-4T.

While we have identified (and reported to their vendors) multiple vulnerabilities in these products, the available time only allowed us to find one unauthenticated remote code execution vulnerability in the Ubiquiti AI Bullet camera running firmware version 4.72.38.

In the following we will describe how we analyzed the Ubiquiti AI Bullet, present the vulnerability we found and show how to exploit it.

## Device Overview

The Ubiquiti AI Bullet camera features a heavy metal enclosure. On the back, an ethernet port that is also used to power the camera via PoE is exposed.

As with some other devices, our first action was to try to open the device to have a look at the components. We wanted to look at the CPU, the memory and most importantly see if there were UART or other debugging ports exposed. This could hopefully help us to gain access to the firmware and get a shell on the device for easier debugging. Eager to explore, we forcefully pried the camera open – only to realize afterwards that there was an easier, intended way to do it.

[![](https://blog.compass-security.com/wp-content/uploads/2025/06/image-2.png)](https://blog.compass-security.com/wp-content/uploads/2025/06/image-2.png)

While it was interesting to have a look at the inner workings, we did not immediately notice a debugging port. So we decided to power up the camera and have a look at what services are exposed. At that moment we realized that the Ubiquiti AI Bullet exposes SSH. After a quick Google search, we learned that many Ubiquiti devices provide shell access with default credentials (`ubnt:ubnt`). This allows us to gain shell access to extract the firmware and also have a debugging environment. Another reason to think twice before trying to force open the next device we will examine.

## Attack Surface

Using netstat, we see that `lighthttpd` is listening on ports 80 and 443. Furthermore, `dropbear` is used as SSHserver and finally there is `infctld` that is listening on UDP port 10001.

```
UVC AI Bullet-4.72.38# netstat -tulpn
Active Internet connections (only servers)
Proto Recv-Q Send-Q Local Address  Foreign Address State  PID/Program name
tcp        0      0 0.0.0.0:443    0.0.0.0:*       LISTEN 1056/lighttpd
tcp        0      0 0.0.0.0:80     0.0.0.0:*       LISTEN 1056/lighttpd
tcp        0      0 0.0.0.0:22     0.0.0.0:*       LISTEN 1065/dropbear
udp        0      0 0.0.0.0:10001  0.0.0.0:*              1199/infctld
```

The web interface requires authentication for most actions. While we found some inconsistent behaviors, they couldn’t be leveraged for unauthenticated compromise.

Finally, the camera uses DHCP to obtain an IP address, meaning DHCP responses are an additional attack surface. This is the route we finally decided to go down and exploit.

## Unauthenticated Remote Code Execution

This chapter describes how we abused a missing input validation vulnerability to gain unauthenticated remote code execution (RCE) on the Ubiquiti AI Bullet camera.

### Root Cause

When a new DHCPv4 message is received, the `/bin/udhcpc` binary processes it by parsing and analyzing the incoming message. This binary then creates several environment variables for each value extracted from the received message and executes the script referenced inside the `-s` option:

```
# ps | grep udhcp
 1192 ui        3136 S    /bin/udhcpc --retries 9 -f -x hostname:uvc-ai-bullet -i eth0 -S -s /bin/udhcpc_cb.sh -v
```

The content of the `/bin/udhcpc_cb.sh` script is shown below. This script does not perform any validation on the environment values received from `udhcp`; instead, the domain (and other) variables are used to create a JSON message that is sent via IPC by the `/bin/ubnt_ipc_cli` binary in the final line:

```
#!/bin/sh

[...CUT...]

/bin/ubnt_ipc_cli -z -b -m="{\"functionName\":\"DhcpEvent\", \"reason\": \"$1\", \"interface\": \"$interface\", \"ip\": \"$ip\", \"subnet\": \"$subnet\", \"broadcast\": \"$broadcast\", \"router\": \"$router\", \"dns\": \"$dns\", \"domain\": \"$domain\", \"hostname\": \"$hostname\", \"serverid\": \"$serverid\", \"lease\": $lease, \"pid\": $$}"
```

The flags used in the call to `/bin/ubnt_ipc_cli` are the following:

* `-z`: If specified, no logging will be performed.
* `-b`: Will broadcast the message to all available IPC-enabled processes. Keep this in mind, as it will be important later.
* `-m`: The message to be sent. Must be specified inline with all the UNIX style constraints for a command-line parameter (e.g. escaping characters).

Since the script above does not validate any field from the DHCP message. This could allow us to escape the predefined JSON structure. In theory, we could send our payload in any of the variables present in the JSON message sent by the `/bin/ubnt_ipc_cli` binary. However, since these values are extracted from the incoming DHCP message, they must comply with the DHCP standard, which may impose strict validations on certain fields (e.g., IP addresses, subnet values, etc.). We decided to target the `domain` DHCP field because it is simply a string and can contain any value.

Using this, the idea is to break the JSON structure and insert additional JSON values into the message being sent. For example, if the domain value is set to `csnc1234","aaa":"bbb`, it would inject a new JSON key called `aaa` with the value `bbb` into the message:

```
/bin/ubnt_ipc_cli -z -b -m="{\"functionName\":\"DhcpEvent\", \"reason\": \"something\", \"interface\": \"something\", \"ip\": \"something\", \"s...