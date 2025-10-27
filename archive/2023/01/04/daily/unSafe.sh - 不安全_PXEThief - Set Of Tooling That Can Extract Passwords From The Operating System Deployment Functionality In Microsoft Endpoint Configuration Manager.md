---
title: PXEThief - Set Of Tooling That Can Extract Passwords From The Operating System Deployment Functionality In Microsoft Endpoint Configuration Manager
url: https://buaq.net/go-143993.html
source: unSafe.sh - 不安全
date: 2023-01-04
fetch_date: 2025-10-04T02:58:44.572602
---

# PXEThief - Set Of Tooling That Can Extract Passwords From The Operating System Deployment Functionality In Microsoft Endpoint Configuration Manager

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

![](https://8aqnet.cdn.bcebos.com/2330cbaa49b97da066d4533886d2fd6b.jpg)

PXEThief - Set Of Tooling That Can Extract Passwords From The Operating System Deployment Functionality In Microsoft Endpoint Configuration Manager

PXEThief is a set of tooling that implements attack paths discussed at the DEF CON 30 talk P
*2023-1-3 19:30:0
Author: [www.kitploit.com(查看原文)](/jump-143993.htm)
阅读量:34
收藏*

---

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjBzMTak97XNV2Szy6hR6kSHcs7XrrCRodEfrhUWOXCsby2hEjKTDPLD6sh1Nx5lZtweW7E_7_K2QMdj4qRL0GNQS5P9P0HNkgH2JAoUeCuuNjJS5_FTnevyWMU02MUvBXwXtpg0JCfjpIeFX-kVy4Bx1ZhoUsDIiFxzuv1YykoMM3kSQ9dzQlwmrlelQ/w640-h436/PXEThief.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjBzMTak97XNV2Szy6hR6kSHcs7XrrCRodEfrhUWOXCsby2hEjKTDPLD6sh1Nx5lZtweW7E_7_K2QMdj4qRL0GNQS5P9P0HNkgH2JAoUeCuuNjJS5_FTnevyWMU02MUvBXwXtpg0JCfjpIeFX-kVy4Bx1ZhoUsDIiFxzuv1YykoMM3kSQ9dzQlwmrlelQ/s1000/PXEThief.png)

PXEThief is a set of tooling that implements attack paths discussed at the DEF CON 30 talk *Pulling Passwords out of Configuration Manager* ([https://forum.defcon.org/node/241925](https://forum.defcon.org/node/241925 "https://forum.defcon.org/node/241925")) against the Operating System Deployment functionality in Microsoft Endpoint Configuration Manager (or ConfigMgr, still commonly known as SCCM). It allows for credential gathering from configured Network Access Accounts ([https://docs.microsoft.com/en-us/mem/configmgr/core/plan-design/hierarchy/accounts#network-access-account](https://docs.microsoft.com/en-us/mem/configmgr/core/plan-design/hierarchy/accounts#network-access-account "https://docs.microsoft.com/en-us/mem/configmgr/core/plan-design/hierarchy/accounts#network-access-account")) and any Task Sequence Accounts or credentials stored within ConfigMgr Collectio n Variables that have been configured for the "All Unknown Computers" collection. These [Active Directory](https://www.kitploit.com/search/label/Active%20Directory "Active Directory") accounts are commonly over permissioned and allow for [privilege escalation](https://www.kitploit.com/search/label/Privilege%20Escalation "privilege escalation") to administrative access somewhere in the domain, at least in my personal experience.

Likely, the most serious attack that can be executed with this tooling would involve PXE-initiated deployment being supported for "All unknown computers" on a distribution point without a password, or with a weak password. The overpermissioning of ConfigMgr accounts exposed to OSD mentioned earlier can then allow for a full Active Directory attack chain to be executed with only network access to the target environment.

## Usage Instructions

```
python pxethief.py -h
```

`pxethief.py 5 <variables-file-name>` should be used to generate a 'hash' of a media variables file that can be used for password guessing attacks with the Hashcat module published at [https://github.com/MWR-CyberSec/configmgr-cryptderivekey-hashcat-module](https://github.com/MWR-CyberSec/configmgr-cryptderivekey-hashcat-module "https://github.com/MWR-CyberSec/configmgr-cryptderivekey-hashcat-module").

## Configuration Options

A file contained in the main PXEThief folder is used to set more static configuration options. These are as follows:

```
[SCAPY SETTINGS]
automatic_interface_selection_mode = 1
manual_interface_selection_by_id =

[HTTP CONNECTION SETTINGS]
use_proxy = 0
use_tls = 0

[GENERAL SETTINGS]
sccm_base_url =
auto_exploit_blank_password = 1
```

### Scapy settings

* `automatic_interface_selection_mode` will attempt to determine the best interface for Scapy to use automatically, for convenience. It does this using two main techniques. If set to `1` it will attempt to use the interface that can reach the machine's default GW as output interface. If set to `2`, it will look for the first interface that it finds that has an IP address that is not an autoconfigure or localhost IP address. This will fail to select the appropriate interface in some scenarios, which is why you can force the use of a specific inteface with 'manual\_interface\_selection\_by\_id'.
* `manual_interface_selection_by_id` allows you to specify the integer index of the interface you want Scapy to use. The ID to use in this file should be obtained from running `pxethief.py 10`.

### General settings

* `sccm_base_url` is useful for overriding the Management Point that the tooling will speak to. This is useful if DNS does not resolve (so the value read from the media variables file cannot be used) or if you have identified multiple Management Points and want to send your traffic to a specific one. This should be provided in the form of a base URL e.g. `http://mp.configmgr.com` instead of `mp.configmgr.com` or `http://mp.configmgr.com/stuff`.
* `auto_exploit_blank_password` changes the behaviour of `pxethief 1` to automatically attempt to exploit a non-password protected PXE Distribution Point. Setting this to `1` will enable auto exploitation, while setting it to `0` will print the tftp client string you should use to download the media variables file. Note that almost all of the time you will want this set to `1`, since non-password protected PXE makes use of a binary key that is sent in the DHCP response that you receive when you ask the Distribution Point to perform a PXE boot.

### HTTP Connection Settings

Not implemented in this release

## Setup Instructions

1. Create a new Windows VM
2. Install Python (From [https://www.python.org/](https://www.python.org/ "https://www.python.org/") or through the store, both should work fine)
3. Install all the requirements through pip (`pip install -r requirements.txt`)
4. Install Npcap ([https://npcap.com/#download](https://npcap.com/#download "https://npcap.com/#download")) (or Wireshark, which comes bundled with it) for Scapy
5. Bridge the VM to the network running a ConfigMgr Distribution Point set up for PXE/OSD
6. If using `pxethief.py 1` or `pxethief.py 2` to identify and generate a media variables file, make sure the interface used by the tool is set to the correct one, if it is not correct, manually set it in 'settings.ini' by identifying the right index ID to use from `pxethief.py 10`

## Limitations

* Proxy support for HTTP requests - Currently only configurable in code. Proxy support can be enabled on line 35 of `pxethief.py` and the address of the proxy can be set on line 693. I am planning to move this feature to be configurable in 'settings.ini' in the next update to the code base
* HTTPS and mutual TLS support - Not implemented at the moment. Can use an intercepting proxy to handle this though, which works well in my experience; to do this, you will need to configure a proxy as mentioned above
* Linux support - PXEThief currently makes use of `pywin32` in order to utilise some built-in Windows [cryptography](https://www.kitploit.com/search/label/Cryptography "cryptography") functions. This is not available on Linux, since the Windows cryptography APIs are not available on Linux :P The Scapy code in `pxethief.py`, however, is fully functional on Linux, but you will need to patch out (at least) the include of `win32crypt` to get it to run under Linux

## Proof of Concept note

Expect to run into issues with error handling with this tool; there are subtle nuances with everything in ConfigMgr and while I have improved the error handling substantially in preparation for the tool's release, this is in no way complete. If there are edge cases that fail, make a detailed issue or fix it and make a pull request :) I'll review these to see where reasonable improvements can be made. R...