---
title: Defense in depth -- the Microsoft way (part 96): yet another	SAFER (SRPv1) and AppLocker (SRPv2) loophole
url: https://seclists.org/fulldisclosure/2026/Mar/5
source: Full Disclosure
date: 2026-03-12
fetch_date: 2026-03-13T04:08:10.130029
---

# Defense in depth -- the Microsoft way (part 96): yet another	SAFER (SRPv1) and AppLocker (SRPv2) loophole

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

[![Previous](/images/left-icon-16x16.png)](4)
[By Date](date.html#5)
[![Next](/images/right-icon-16x16.png)](6)

[![Previous](/images/left-icon-16x16.png)](4)
[By Thread](index.html#5)
[![Next](/images/right-icon-16x16.png)](6)

![](/shared/images/nst-icons.svg#search)

# Defense in depth -- the Microsoft way (part 96): yet another SAFER (SRPv1) and AppLocker (SRPv2) loophole

---

*From*: Stefan Kanthak via Fulldisclosure <fulldisclosure () seclists org>
*Date*: Mon, 23 Feb 2026 17:36:44 +0100

---

```
Hi @ll,

about 2 months ago I posted
<https://seclists.org/fulldisclosure/2025/Dec/29>
"Defense in depth -- the Microsoft way (part 94):
 SAFER (SRPv1 and AppLocker alias SRPv2) bypass for dummies"

Here's the continuation...

About 23 years ago, 64-bit Windows introduced the WoW64 subsystem, which
performs a transpatent redirection of file system and registry accesses
for 32-bit applications.
To allow consistent appearance and behaviour of 64-bit and 32-bit variants
of applications like the "command processor" which reads its settings from
the registry key [HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Command Processor],
several branches or single keys of the split registry where joined: until
Vista via "registry reflection", since Windows 7 via "shared keys".

Some applications, for example the Windows Script Host, were but lobotomized:
the registry keys [HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows Script Host]
and [HKEY_LOCAL_MACHINE\SOFTWARE\WoW6432Node\Microsoft\Windows Script Host]
are separate, NOT joined.

Demonstration
~~~~~~~~~~~~~

The article <https://technet.microsoft.com/en-us/library/ee198684.aspx>
"Disabling Windows Script Host" states:

| To disable WSH for all users of a particular computer, create this
| entry:
|
| [HKEY_LOCAL_MACHINE\Software\Microsoft\Windows Script Host\Settings]
| "Enabled"=dword:00000000

It but needs a second, UNDOCUMENTED entry to enforce this setting:

| "IgnoreUserSettings"=dword:00000001

Without this entry, unprivileged users can enable WSH or exempt it from
SAFER, either Software Restriction Policies or AppLocker:

| [HKEY_CURRENT_USER\Software\Microsoft\Windows Script Host\Settings]
| "Enabled"=dword:00000001
| "UseWINSAFER"=dword:00000000

With the first 2 entries for the computer in place, and NO entries set for
the user, start a command prompt, run %SystemRoot%\SysWoW64\CSCRIPT.EXE or
%SystemRoot%\SysWoW64\WSCRIPT.EXE without arguments and admire their help
messages on the console or in a dialog box: OOPS!

Due to the lobotomy the same entries MUST be set in the 32-bit branch of
the registry too! Since the key name \WoW6432Node\ is an implementation
detail you should NEVER use, run the proper command lines:

REG.EXE ADD "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows Script Hosts\Settings" /REG:32 /V Enabled /D 0
REG.EXE ADD "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows Script Hosts\Settings" /REG:32 /V IgnoreUserSettings /D 1

stay tuned, and far away from split brains
Stefan Kanthak
_______________________________________________
Sent through the Full Disclosure mailing list
https://nmap.org/mailman/listinfo/fulldisclosure
Web Archives & RSS: https://seclists.org/fulldisclosure/
```

---

[![Previous](/images/left-icon-16x16.png)](4)
[By Date](date.html#5)
[![Next](/images/right-icon-16x16.png)](6)

[![Previous](/images/left-icon-16x16.png)](4)
[By Thread](index.html#5)
[![Next](/images/right-icon-16x16.png)](6)

### Current thread:

* **Defense in depth -- the Microsoft way (part 96): yet another SAFER (SRPv1) and AppLocker (SRPv2) loophole** *Stefan Kanthak via Fulldisclosure (Mar 12)*

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