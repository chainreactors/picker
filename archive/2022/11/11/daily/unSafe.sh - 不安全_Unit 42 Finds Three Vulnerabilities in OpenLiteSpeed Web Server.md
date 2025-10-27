---
title: Unit 42 Finds Three Vulnerabilities in OpenLiteSpeed Web Server
url: https://buaq.net/go-135097.html
source: unSafe.sh - 不安全
date: 2022-11-11
fetch_date: 2025-10-03T22:21:19.500227
---

# Unit 42 Finds Three Vulnerabilities in OpenLiteSpeed Web Server

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

![](https://8aqnet.cdn.bcebos.com/eead04c8e79abbfbda6d8588fb74d048.jpg)

Unit 42 Finds Three Vulnerabilities in OpenLiteSpeed Web Server

This post is also available i
*2022-11-10 22:0:11
Author: [unit42.paloaltonetworks.com(查看原文)](/jump-135097.htm)
阅读量:42
收藏*

---

![Cloud vulnerabilities conceptual image, covering topics such as OpenLiteSpeed vulnerabilities](https://unit42.paloaltonetworks.com/wp-content/uploads/2022/11/Unit42-blog-2by1-characters-r4d1-2020_Cloud-malware-v1.png)

This post is also available in:
[日本語 (Japanese)](https://unit42.paloaltonetworks.jp/openlitespeed-vulnerabilities/)

## Executive Summary

The Unit 42 research team has researched and discovered three different vulnerabilities in the open source [OpenLiteSpeed Web Server](https://github.com/litespeedtech/openlitespeed). These vulnerabilities also affect the enterprise version, [LiteSpeed Web Server](https://www.litespeedtech.com/). By chaining and exploiting the vulnerabilities, adversaries could compromise the web server and gain fully privileged remote code execution. The vulnerabilities discovered include:

1. Remote Code Execution ([CVE-2022-0073](https://www.cve.org/CVERecord?id=CVE-2022-0073)) rated High severity (CVSS 8.8)
2. Privilege Escalation ([CVE-2022-0074](https://www.cve.org/CVERecord?id=CVE-2022-0074)) rated High severity (CVSS 8.8)
3. Directory Traversal ([CVE-2022-0072](https://www.cve.org/CVERecord?id=CVE-2022-0072)) rated Medium severity (CVSS 5.8)

[OpenLiteSpeed](https://openlitespeed.org/) is the [Open Source edition](https://www.litespeedtech.com/open-source/openlitespeed) of [LiteSpeed Web Server Enterprise](https://www.litespeedtech.com/products/litespeed-web-server), which is developed and maintained by LiteSpeed Technologies. LiteSpeed Web Server is ranked the sixth most popular web server. Analysis from Palo Alto Networks [Cortex Xpanse](https://www.paloaltonetworks.com/cortex/cortex-xpanse) and [Shodan](https://www.shodan.io/) reveals that LiteSpeed serves roughly 2% of all Web Server applications, with nearly 1.9 million unique servers globally.

Unit 42 responsibly disclosed the vulnerabilities to LiteSpeed Technologies with suggested remediation on Oct. 4, 2022. LiteSpeed Technologies swiftly released a patch version ([v1.7.16.1](https://github.com/litespeedtech/openlitespeed/tree/v1.7.16.1)) on Oct. 18, 2022, to mitigate the reported vulnerabilities.

Organizations using OpenLiteSpeed versions 1.5.11 up to 1.7.16 and LiteSpeed versions 5.4.6 up to 6.0.11 are advised to update their software to the latest matching release – v1.7.16.1 and [6.0.12](https://store.litespeedtech.com/store/index.php?rp=/announcements/451).

Palo Alto Networks customers using [Prisma Cloud WAAS](https://docs.paloaltonetworks.com/prisma/prisma-cloud/prisma-cloud-admin-compute/waas) or [Next-Generation Firewalls](https://www.paloaltonetworks.com/network-security/next-generation-firewall) with [Advanced](https://www.paloaltonetworks.com/network-security/advanced-threat-prevention) [Threat Prevention](https://www.paloaltonetworks.com/products/secure-the-network/subscriptions/threat-prevention) receive protection from these vulnerabilities by new rules and signatures that block the attack.

## Table of Contents

[Background](#post-125677-_enmvbv7j5unn)

## Background

LiteSpeed is a performance-focused web server. According to our findings there are 1.9 million internet facing LiteSpeed Server instances online.

As part of our initiative to contribute to the community to improve security and increase security awareness, we decided to audit OpenLiteSpeed, which is the open source version of the LiteSpeed Web Server.

We tried to imitate the actions of an adversary and engaged in research with the intention of finding vulnerabilities and disclosing them to the vendor. This research has resulted in finding three vulnerabilities that affect both the enterprise and open source solutions. These could be chained and exploited by an adversary who has the credentials for the admin dashboard, in order to gain privileged code execution on vulnerable components.

## Remote Code Execution

*This vulnerability has been assigned the CVE ID of* [*CVE-2022-0073*](https://www.cve.org/CVERecord?id=CVE-2022-0073)*.*

At the first stage of the attack, we tried to gain remote code execution and found that the OpenLiteSpeed Web Server admin dashboard is vulnerable to a command injection vulnerability. A threat actor who managed to gain the credentials to the dashboard, whether by brute force attacks or social engineering, could exploit the vulnerability in order to execute code on the server.

The vulnerability exists in the External App Command field, which allows users to specify a command that will be executed when the server starts.

This functionality is considered dangerous and therefore mitigations for abusing it were implemented. We managed to bypass the mitigations and abuse this functionality to download and execute a malicious file on the server with the privileges of the user [nobody](https://en.wikipedia.org/wiki/Nobody_%28username%29), which is an unprivileged user that traditionally exists in Linux machines.

## Privilege Escalation

*This vulnerability has been assigned the CVE ID of* [*CVE-2022-0074*](https://www.cve.org/CVERecord?id=CVE-2022-0074)*.*

After gaining code execution on the server we wanted to take it a step further and escalate our privileges from nobody to root.

While exploring the OpenLiteSpeed Docker image as nobody, we found a misconfiguration in the PATH environment variable that could be exploited into a privilege escalation using the CWE [untrusted search path](https://cwe.mitre.org/data/definitions/426.html).

When executing a binary with a relative path, the operating system will look at the PATH variable, which contains a list of directories. It will then search for that binary in the listed folders, in the same order that the directories are presented.

The issue in this case was that the second directory in PATH was /usr/local/bin, which is a directory that the user nobody controls.

This leads to a situation where an attacker could execute code as an unprivileged user (such as nobody) to place a malicious file and disguise it as a legitimate binary in /usr/local/bin, with the intention for it to be executed by highly privileged processes because it is in the second directory on the PATH environment variable.

We were able to exploit this by abusing the script entrypoint.sh as shown in Figure 1, which runs as root and executes the binary grep repeatedly.

![Code snippet from the entrypoint.sh script which runs as root and executes the binary grep repeatedly.](https://unit42.paloaltonetworks.com/wp-content/uploads/2022/11/word-image-16.png)

Figure 1. Entrypoint.sh script showing vulnerable usage of the grep command.

By chaining these vulnerabilities, we were able to gain remote code execution and escalate our privileges to root, as shown in Figure 2.

![Code snippet chaining the vulnerabilities to gain remote code execution and escalate privileges to root.](https://unit42.paloaltonetworks.com/wp-content/uploads/2022/11/word-image-17.png)

Figure 2. Proof of successful exploitation.

This vulnerability requires the controlled user to have write permissions to /usr/local/bin, which is usually not the case by default. In the OpenLiteSpeed docker container, this directory is writable by the user nobody by default.

## Directory Traversal

*This vulnerability has been assigned the CVE ID of* [*CVE-2022-0072*](https://www.cve.org/CVERecord?id=CVE-2022-0072)*.*

The last issue we found was a directory tra...