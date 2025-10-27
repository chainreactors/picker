---
title: Toshiba Multi-Function Printers 40 Vulnerabilities
url: https://buaq.net/go-248847.html
source: unSafe.sh - 不安全
date: 2024-07-05
fetch_date: 2025-10-06T17:38:55.359064
---

# Toshiba Multi-Function Printers 40 Vulnerabilities

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

![]()

Toshiba Multi-Function Printers 40 Vulnerabilities

Hello,Please find a text-only version below sent to security mailing lists.The complete version on "
*2024-7-4 23:29:28
Author: [packetstormsecurity.com(查看原文)](/jump-248847.htm)
阅读量:70
收藏*

---

`` Hello,

Please find a text-only version below sent to security mailing lists.

The complete version on "40 vulnerabilities in Toshiba Multi-Function

The text version is also posted here:
 https://pierrekim.github.io/advisories/2024-toshiba-mfp.txt

=== text-version of the advisory ===

-----BEGIN PGP SIGNED MESSAGE-----
Hash: SHA512

## Advisory Information

Title: 40 vulnerabilities in Toshiba Multi-Function Printers
Advisory URL: https://pierrekim.github.io/advisories/2024-toshiba-mfp.txt
Blog URL: https://pierrekim.github.io/blog/2024-06-27-toshiba-mfp-40-vulnerabilities.html
Date published: 2024-06-27
Vendors contacted: Toshiba
Release mode: Released
CVE: CVE-2024-27141, CVE-2024-27142, CVE-2024-27143, CVE-2024-27144,
CVE-2024-27145, CVE-2024-27146, CVE-2024-27147, CVE-2024-27148,
CVE-2024-27149, CVE-2024-27150, CVE-2024-27151, CVE-2024-27152,
CVE-2024-27153, CVE-2024-27154, CVE-2024-27155, CVE-2024-27156,
CVE-2024-27157, CVE-2024-27158, CVE-2024-27159, CVE-2024-27160,
CVE-2024-27161, CVE-2024-27162, CVE-2024-27163, CVE-2024-27164,
CVE-2024-27165, CVE-2024-27166, CVE-2024-27167, CVE-2024-27168,
CVE-2024-27169, CVE-2024-27170, CVE-2024-27171, CVE-2024-27172,
CVE-2024-27173, CVE-2024-27174, CVE-2024-27175, CVE-2024-27176,
CVE-2024-27177, CVE-2024-27178, CVE-2024-27179, CVE-2024-27180

## Product description

> e-STUDIO Multi-Function Printers (MFPs) are fast and productive, providing businesses and organisations the capability to produce what you need, when you need it.
>
> From https://www.toshibatec.co.uk/workplace-solutions/products-and-solutions/mfps-and-printers/

## Vulnerability Summary

Vulnerable versions: 103 different models of Toshiba Multi-Function
Printers (MFP) are vulnerable. It is recommended to visit the official
Toshiba advisory
(https://www.toshibatec.com/information/20240531_01.html), review the
list of affected printers
(https://www.toshibatec.com/information/pdf/information20240531_01.pdf)
and apply security patches and replace unsupported MFP models.

The summary of the vulnerabilities is as follows:

1. CVE-2024-27141 - Pre-authenticated Blind XML External Entity (XXE)
injection - DoS
2. CVE-2024-27142 - Pre-authenticated XXE injection
3. CVE-2024-27143 - Pre-authenticated Remote Code Execution as root
4. CVE-2024-27144 - Pre-authenticated Remote Code Execution as root or
apache and multiple Local Privilege Escalations
4.1. Remote Code Execution - Upload of a new .py module inside WSGI
Python programs
4.2. Remote Code Execution - Upload of a new .ini configuration files
inside WSGI Python programs
4.3. Remote Code Execution - Upload of a malicious script
`/tmp/backtraceScript.sh` and injection of malicious gdb commands
4.4. Remote Code Execution - Upload of a malicious
`/home/SYSROM_SRC/build/common/bin/sapphost.py` program
4.5. Remote Code Execution - Upload of malicious libraries
4.6. Other ways to get Remote Code Execution
5. CVE-2024-27145 - Multiple Post-authenticated Remote Code Executions as root
6. CVE-2024-27146 - Lack of privileges separation
7. CVE-2024-27147 - Local Privilege Escalation and Remote Code
Execution using snmpd
8. CVE-2024-27148 - Local Privilege Escalation and Remote Code
Execution using insecure PATH
9. CVE-2024-27149 - Local Privilege Escalation and Remote Code
Execution using insecure LD_PRELOAD
10. CVE-2024-27150 - Local Privilege Escalation and Remote Code
Execution using insecure LD_LIBRARY_PATH
11. CVE-2024-27151 - Local Privilege Escalation and Remote Code
Execution using insecure permissions for 106 programs
11.1. 3 vulnerable programs not running as root
11.2. 103 vulnerable programs running as root
12. CVE-2024-27152 - Local Privilege Escalation and Remote Code
Execution using insecure permissions for libraries
12.1. Example with `/home/SYSROM_SRC/bin/syscallerr`
13. CVE-2024-27153 - Local Privilege Escalation and Remote Code
Execution using CISSM
14. CVE-2024-27154 and CVE-2024-27155 - Passwords stored in clear-text
logs and insecure logs
14.1. Clear-text password written in logs when an user logs into the printer
14.2. Clear-text password written in logs when a password is modified
15. CVE-2024-27156 - Leak of authentication sessions in insecure logs
in /ramdisk/work/log directory
16. CVE-2024-27157 - Leak of authentication sessions in insecure logs
in /ramdisk/al/network/log directory
17. CVE-2024-27158 - Hardcoded root password
18. CVE-2024-27159 - Hardcoded password used to encrypt logs
19. CVE-2024-27160 - Hardcoded password used to encrypt logs and use
of a weak digest cipher
20. CVE-2024-27161 - Hardcoded password used to encrypt files
21. CVE-2024-27162 - DOM-based XSS present in the /js/TopAccessUtil.js file
22. CVE-2024-27163 - Leak of admin password and passwords
23. CVE-2024-27164 - Hardcoded credentials in telnetd
24. CVE-2024-27165 - Local Privilege Escalation using PROCSUID
25. CVE-2024-27166 - Insecure permissions for core files
26. CVE-2024-27167 - Insecure permissions used for Sendmail - Local
Privilege Escalation
27. CVE-2024-27168 - Hardcoded keys found in Python applications used
to generate authentication cookies
28. CVE-2024-27169 - Lack of authentication in WebPanel - Local
Privilege Escalation
29. CVE-2024-27170 - Hardcoded credentials for WebDAV access
30. CVE-2024-27171 - Insecure permissions
31. CVE-2024-27172 - Remote Code Execution - command injection as root
32. CVE-2024-27173 - Remote Code Execution - insecure upload
33. CVE-2024-27174 - Remote Code Execution - insecure upload
34. CVE-2024-27175 - Local File Inclusion
35. CVE-2024-27176 - Remote Code Execution - insecure upload
36. CVE-2024-27177 - Remote Code Execution - insecure upload
37. CVE-2024-27178 - Remote Code Execution - insecure copy
38. CVE-2024-27179 - Session disclosure inside the log files in the
installation of applications
39. CVE-2024-27180 - TOCTOU vulnerability in the installation of
applications, allowing to install rogue applications and get RCE

CVE-2024-27171 to CVE-2024-27180 affect the implementation of
third-party application system and third-party applications installed
by default in Toshiba printers - this is an extremely interesting
attack surface for persistence.

TL;DR: An attacker can compromise Toshiba Multi-Function Printers
using multiple vulnerabilities.

List of vulnerable models of Toshiba Multi-Function Printers (103 models):

2021AC, 2521AC, 2020AC, 2520AC, 2025NC, 2525AC, 3025AC, 3525AC,
3525ACG, 4525AC, 4525ACG, 5525AC, 5525ACG,
 6525AC, 6525ACG, 2528A, 3028A, 3528A, 3528AG, 4528A, 4528AG,
5528A, 6528A, 6526AC, 6527AC, 7527AC, 6529A,
 7529A, 9029A, 330AC, 400AC, 2010AC, 2110AC, 2510AC, 2610AC,
2015NC, 2515AC, 2615AC, 3015AC, 3115AC, 3515AC,
 3615AC, 4515AC, 4615AC, 5015AC, 5115AC, 2018A, 2518A, 2618A,
3018A, 3118A, 3018AG, 3518A, 3518AG, 3618A,
 3618AG, 4518A, 4518AG, 4618A, 4618AG, 5018A, 5118A, 5516AC,
5616AC, 6516AC, 6616AC, 7516AC, 7616AC, 5518A,
 5618A, 6518A, 6618A, 7518A, 7618A, 8518A, 8618A, 2000AC, 2500AC,
2005NC, 2505AC, 3005AC, 3505AC, 4505AC,
 5005AC, 2008A, 2508A, 3008A, 3008AG, 3508A, 3508AG, 4508A, 4508AG,
5008A, 5506AC, 6506AC, 7506AC, 5508A,
 6508A, 7508A, 8508A, 3508LP, 4508LP, 5008LP.

_Miscellaneous notes_:

This security assessment was entirely done using a blackbox approach
and fully-remote - I only had some IPs of printers (no physical access
and no credentials for admin or normal users). Consequently, the
physical security of the printers...