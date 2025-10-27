---
title: Combining dns-pydivert And dnsresolver
url: https://blog.didierstevens.com/2022/12/27/combining-dns-pydivert-and-dnsresolver/
source: Didier Stevens
date: 2022-12-28
fetch_date: 2025-10-04T02:35:43.543964
---

# Combining dns-pydivert And dnsresolver

# [Didier Stevens](https://blog.didierstevens.com/)

## Tuesday 27 December 2022

### Combining dns-pydivert And dnsresolver

Filed under: [Malware](https://blog.didierstevens.com/category/malware/),[My Software](https://blog.didierstevens.com/category/my-software/),[Networking](https://blog.didierstevens.com/category/networking/) — Didier Stevens @ 0:00

I use my tools [dns-pydivert](https://blog.didierstevens.com/2022/12/26/new-tool-dns-pydivert-py/) and [dnsresolver.py](https://blog.didierstevens.com/2022/12/25/update-dnsresolver-py-version-0-0-2/) for dynamic analysis of software (malware and benign software).

On the virtual machine where I’m doing dynamic analysis, I disable IPv6 support.

I install [dnslib](https://pypi.org/project/dnslib/) and run dnsresolver.py with a command like this, for example:

```
dnsresolver.py "type=resolve,label=example.com,answer=. 1 IN A 127.0.0.1" "type=forwarder,server=8.8.8.8"
```

![](https://blog.didierstevens.com/wp-content/uploads/2022/12/20221224-100411.png)

The first command is a resolve command: DNS A queries for example.com will be resolved to IPv4 address 127.0.0.1 with TTL 1 minute.

The second command is a forwarder command: all DNS requests not handled by other commands, are forwarded to 8.8.8.8. Make sure that the IPv4 address of the DNS server you forward requests to, is different from the VM’s default DNS server, otherwise this forwarding will be redirected by dns-pydivert too.

I don’t use this second resolver command if the VM is isolated from the Internet, I only use it when I want to allow some interaction with the Internet.

Then I install [pydivert](https://pypi.org/project/pydivert/) and run dns-pydivert.py as administrator.

![](https://blog.didierstevens.com/wp-content/uploads/2022/12/20221224-095050.png)
![](https://blog.didierstevens.com/wp-content/uploads/2022/12/20221224-095132.png)

You can’t run dns-pydivert.py properly without administrative permissions:

![](https://blog.didierstevens.com/wp-content/uploads/2022/12/20221224-095939.png)

When dns-pydivert.py and dnsresolver.py are running, DNS traffic is altered according to our settings.

![](https://blog.didierstevens.com/wp-content/uploads/2022/12/20221224-100703.png)

For example (picture above), when I issue a “ping google.com” command inside the VM, dns-pydivert sees this first DNS packet and configures itself with the addresses in this packet: 192.168.32.129 is the IPv4 address of the Windows VM and 192.168.32.2 is the IPv4 address of this Windows VM’s DNS server.

It alters this first request to be redirected to the VM itself (192.168.32.2 -> 192.168.32.129).

Then dnsresolver receives this packet, and forwards it to DNS server 8.8.8.8. It receives a reply from DNS server 8.8.8.8, and forwards it to the Windows VM (192.168.32.129).

Then dns-pydivert sees this reply, and changes its source from 192.168.32.129 to 192.168.32.2, so that it appears to come from the Windows VM’s default DNS server.

![](https://blog.didierstevens.com/wp-content/uploads/2022/12/20221224-100719-1.png)

When I do the same (picture above) for example.com (ping example.com), the query is redirected to dnsresolver, which resolves this to 127.0.0.1 with a TTL of 1 minute (per resolve commands configuration).

Thus the ping command pings the localhost, instead of example.com’s web server.

![](https://blog.didierstevens.com/wp-content/uploads/2022/12/20221224-100813.png)

And when I kill dns-pydivert (picture above) and issue a “ping example.com” again after waiting for 1 minute, the query is no longer redirected and example.com’s web server is pinged this time.

I used ping here to illustrate the process, but often it’s HTTP(S) traffic that I want to redirect, and then I also use my [simple-listener.py](https://blog.didierstevens.com/2022/07/09/simple_listener-py/) tool to emulate simple web servers.

Remark that this will only redirect DNS traffic (per the configuration). This does not redirect traffic “directed” at IPv4 addresses (as opposed to hostnames).

This can be done too with pydivert, and I will probably release a tool for that too.

### Share this:

* [Click to share on Facebook (Opens in new window)
  Facebook](https://blog.didierstevens.com/2022/12/27/combining-dns-pydivert-and-dnsresolver/?share=facebook)
* [Click to share on X (Opens in new window)
  X](https://blog.didierstevens.com/2022/12/27/combining-dns-pydivert-and-dnsresolver/?share=x)

### *Related*

[Leave a Comment](https://blog.didierstevens.com/2022/12/27/combining-dns-pydivert-and-dnsresolver/#respond)

## Leave a Comment [»](#postcomment "Leave a comment")

No comments yet.

[RSS feed for comments on this post.](https://blog.didierstevens.com/2022/12/27/combining-dns-pydivert-and-dnsresolver/feed/) [TrackBack URI](https://blog.didierstevens.com/2022/12/27/combining-dns-pydivert-and-dnsresolver/trackback/)

### Leave a Reply (comments are moderated)

Δ

This site uses Akismet to reduce spam. [Learn how your comment data is processed.](https://akismet.com/privacy/)

* ## Pages

  + [About](https://blog.didierstevens.com/about/)
  + [Didier Stevens Suite](https://blog.didierstevens.com/didier-stevens-suite/)
  + [Links](https://blog.didierstevens.com/links/)
  + [My Python Templates](https://blog.didierstevens.com/my-python-templates/)
  + [My Software](https://blog.didierstevens.com/my-software/)
  + [Professional](https://blog.didierstevens.com/professional/)
  + [Programs](https://blog.didierstevens.com/programs/)
    - [Ariad](https://blog.didierstevens.com/programs/ariad/)
    - [Authenticode Tools](https://blog.didierstevens.com/programs/authenticode-tools/)
    - [Binary Tools](https://blog.didierstevens.com/programs/binary-tools/)
    - [CASToggle](https://blog.didierstevens.com/programs/castoggle/)
    - [Cobalt Strike Tools](https://blog.didierstevens.com/programs/cobalt-strike-tools/)
    - [Disitool](https://blog.didierstevens.com/programs/disitool/)
    - [EICARgen](https://blog.didierstevens.com/programs/eicargen/)
    - [ExtractScripts](https://blog.didierstevens.com/programs/extractscripts/)
    - [FileGen](https://blog.didierstevens.com/programs/filegen/)
    - [FileScanner](https://blog.didierstevens.com/programs/filescanner/)
    - [HeapLocker](https://blog.didierstevens.com/programs/heaplocker/)
    - [MyJSON Tools](https://blog.didierstevens.com/programs/myjson-tools/)
    - [Network Appliance Forensic Toolkit](https://blog.didierstevens.com/programs/network-appliance-forensic-toolkit/)
    - [Nokia Time Lapse Photography](https://blog.didierstevens.com/programs/nokia-time-lapse-photography/)
    - [oledump.py](https://blog.didierstevens.com/programs/oledump-py/)
    - [OllyStepNSearch](https://blog.didierstevens.com/programs/ollystepnsearch/)
    - [PDF Tools](https://blog.didierstevens.com/programs/pdf-tools/)
    - [Shellcode](https://blog.didierstevens.com/programs/shellcode/)
    - [SpiderMonkey](https://blog.didierstevens.com/programs/spidermonkey/)
    - [Translate](https://blog.didierstevens.com/programs/translate/)
    - [USBVirusScan](https://blog.didierstevens.com/programs/usbvirusscan/)
    - [UserAssist](https://blog.didierstevens.com/programs/userassist/)
    - [VirusTotal Tools](https://blog.didierstevens.com/programs/virustotal-tools/)
    - [XORSearch & XORStrings](https://blog.didierstevens.com/programs/xorsearch/)
    - [YARA Rules](https://blog.didierstevens.com/programs/yara-rules/)
    - [ZIPEncryptFTP](https://blog.didierstevens.com/programs/zipencryptftp/)
  + [Public Drafts](https://blog.didierstevens.com/public-drafts/)
    - [Cisco Tricks](https://blog.didierstevens.com/public-drafts/cisco-tricks/)
  + [Screencasts & Videos](https://blog.didierstevens.com/screencasts-videos/)
* Search for:
* ## Top Posts

  + [PDF Tools](https://blog.didierstevens.com/programs/pdf-tools/)
  + [Update: pdf-parser.py Version 0.7.13](https://blog.didierstevens.com/2025/08/31/update-pdf-parser-py-version-0-7-13/)
  + [Overview of Content Publish...