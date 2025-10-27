---
title: Backdoor.Win32.PoisonIvy.ymw / Insecure Credential Storage
url: https://seclists.org/fulldisclosure/2024/Sep/13
source: Full Disclosure
date: 2024-09-07
fetch_date: 2025-10-06T18:31:15.480698
---

# Backdoor.Win32.PoisonIvy.ymw / Insecure Credential Storage

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

[![Previous](/images/left-icon-16x16.png)](12)
[By Date](date.html#13)
[![Next](/images/right-icon-16x16.png)](14)

[![Previous](/images/left-icon-16x16.png)](12)
[By Thread](index.html#13)
[![Next](/images/right-icon-16x16.png)](14)

![](/shared/images/nst-icons.svg#search)

# Backdoor.Win32.PoisonIvy.ymw / Insecure Credential Storage

---

*From*: malvuln <malvuln13 () gmail com>
*Date*: Tue, 3 Sep 2024 21:13:49 -0400

---

```
Discovery / credits: Malvuln (John Page aka hyp3rlinx) (c) 2024
Original source:
https://malvuln.com/advisory/b0748f1c1a17bad44dc9bd750fc97547.txt
Contact: malvuln13 () gmail com
Media: x.com/malvuln

Threat: Backdoor.Win32.PoisonIvy.ymw
Vulnerability: Insecure Credential Storage
Family: PoisonIvy
Type: PE32
MD5: b0748f1c1a17bad44dc9bd750fc97547
SHA256: 060c15f401ce4d38d70e7f60aabe31c81935d2c261e350c0ea34387886d48920
Vuln ID: MVID-2024-0688
Dropped files: PILib.dll, Poison Ivy.ini, .pip
Disclosure: 09/03/2024
Description: PoisonIvy listens on TCP port 3460 by default but that
can be changed. When generating PoisonIvy PE files, credentials are
stored in cleartext if not using the PasswordKey=1 option which gets
stored in ".pik" files. The "Ivy.ini" configuration and profile ".pip"
files also contain credentials in cleartext.

"malvuln.pip"

[Advanced]
PEbinary=1
PEc=0
PEd=0
PEp=0
PE=1
FileAlign=512
KeyLogger=0
InjectServer=0
Persistence=0
ProcessMutex=)!VoqA.I4
CustomInject=0
CustomInjectProc=msnmsgr.exe
[Connection]
Group=
HijackProxy=0
HijackProxyPersist=0
DNS=192.168.18.125:3460:0,
ID=malvuln
Password=apparitionsec
PasswordKey=0
Proxy=0
ProxyDNS=
[Install]
Startup=0
StartupHKLM=1
StartupActiveX=0
ActiveXKey=
HKLMName=
Copy=0
Filename=
CopySystem=1
CopyWindows=0
ADS=0
Melt=0
[Build]
Icon=
bThirdParty=0
ThirdParty=upx.exe "%s"

"Poison Ivy.ini"

[Disclaimer]
Show=1
[Settings]
RemoveKeyFile=1
StorePlugins=1
SDrounds=3
HidePW=0
PlaySound=0
SoundPath=%PI%\sound.wav
Cache=1
CachePath=%PI%\Users\%USR%\
ImagePath=%PI%\Users\%USR%\Images\
AudioPath=%PI%\Users\%USR%\Audio\
NotesPath=%PI%\Notes\
AutoRefresh=0
WindowColor=1
TimestampColor=1
KeynameColor=1
WindowName=008000
Timestamp=0000FF
Keyname=808080
AutoRemove=1
AutoLookUpdates=1
SimTransfers=2
DownloadPath=%PI%\Users\%USR%\Download\
ProfilePath=%PI%\Profiles\
PluginPath=%PI%\Plugins\
TreeLayout=1
CloseTray=0
MinimizeTray=1
BalloonTip=1
Prompt=0
PromptExit=0
PromptDelete=1
ColumnInfo=1
Groups=0
ColumnPath=%PI%\Data\
Thumbs=0
ThumbSize=96
Highlight=0
HighlightExt=
ScrSize=75
ScrBits=24
ShareTo=
ShareToSocks=
ShareSocks=0
[Placement]
DataTransfers=1
MaximizedState=0
Top=63
Left=416
Width=936
Height=540
ConTop=132
ConLeft=260
ConWidth=650
ConHeight=380
[Client0]
Port=3460
KeyFile=0
Password=admin

Exploit/PoC:

DE:0055DD64 aPassword_7     db 'Password: *****',0  ; DATA XREF:
sub_55D128+292↑o
CODE:0055DD74                 dd 0FFFFFFFFh, 5
CODE:0055DD7C aAdmin_2        db 'admin',0            ; DATA XREF:
sub_55D128:loc_55D3C6↑o

004016C0                 db  61h ; a
004016C1                 db  70h ; p
004016C2                 db  70h ; p
004016C3                 db  61h ; a
004016C4                 db  72h ; r
004016C5                 db  69h ; i
004016C6                 db  74h ; t
004016C7                 db  69h ; i
004016C8                 db  6Fh ; o
004016C9                 db  6Eh ; n
004016CA                 db  73h ; s
004016CB                 db  65h ; e
004016CC                 db  63h ; c

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

[![Previous](/images/left-icon-16x16.png)](12)
[By Date](date.html#13)
[![Next](/images/right-icon-16x16.png)](14)

[![Previous](/images/left-icon-16x16.png)](12)
[By Thread](index.html#13)
[![Next](/images/right-icon-16x16.png)](14)

### Current thread:

* **Backdoor.Win32.PoisonIvy.ymw / Insecure Credential Storage** *malvuln (Sep 05)*

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