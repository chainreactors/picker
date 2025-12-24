---
title: Defense in depth -- the Microsoft way (part 94): SAFER (SRPv1	and AppLocker alias SRPv2) bypass for dummies
url: https://seclists.org/fulldisclosure/2025/Dec/29
source: Full Disclosure
date: 2025-12-23
fetch_date: 2025-12-24T03:23:09.649994
---

# Defense in depth -- the Microsoft way (part 94): SAFER (SRPv1	and AppLocker alias SRPv2) bypass for dummies

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

[![Previous](/images/left-icon-16x16.png)](28)
[By Date](date.html#29)
![Next](/images/right-icon-16x16.png)

[![Previous](/images/left-icon-16x16.png)](28)
[By Thread](index.html#29)
![Next](/images/right-icon-16x16.png)

![](/shared/images/nst-icons.svg#search)

# Defense in depth -- the Microsoft way (part 94): SAFER (SRPv1 and AppLocker alias SRPv2) bypass for dummies

---

*From*: Stefan Kanthak via Fulldisclosure <fulldisclosure () seclists org>
*Date*: Sat, 20 Dec 2025 20:44:01 +0100

---

```
Hi @ll,

since 30 years Microsoft ships Windows with "Windows Script Host",
an empty registry key and the following registry entries:

[HKEY_CURRENT_USER\Software\Microsoft\Windows Script Host\Settings]

[HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows Script Host\Settings]
"ActiveDebugging"="1"
"DisplayLogo"="1"
"SilentTerminate"="0"
"UseWINSAFER"="1"

The last registry entry (which is not writeable by unprivileged users)
enables SAFER, i.e. both Software Restriction Policies and AppLocker,
for the various script engines (JScript, VBScript, PerlScript, ...)
run inside of Windows Script Host.

Windows Script Host supports the following additional registry entries:

"Enabled"=...
"LogSecurityFailures"=...
"LogSecuritySuccesses"=...
"TimeOut"=...
"IgnoreUserSettings"=...

Except for the last one, which is evaluated only in the
[HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows Script Host\Settings]
registry key, (unprivileged) users can but overrule the (read-only)
settings shown above by adding the same registry entries to their
[HKEY_CURRENT_USER\Software\Microsoft\Windows Script Host\Settings]
registry key, i.e. UNLESS disabled via

[HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows Script Host\Settings]
"IgnoreUserSettings"="1"

they can enable a disabled Windows Script Host or disable SAFER for
it via the following registry entries:

[HKEY_CURRENT_USER\Software\Microsoft\Windows Script Host\Settings]
"Enabled"="1"
"UseWINSAFER"="0"

stay tuned
Stefan Kanthak

PS: these registry entries can be either REG_SZ or REG_DWORD
_______________________________________________
Sent through the Full Disclosure mailing list
https://nmap.org/mailman/listinfo/fulldisclosure
Web Archives & RSS: https://seclists.org/fulldisclosure/
```

---

[![Previous](/images/left-icon-16x16.png)](28)
[By Date](date.html#29)
![Next](/images/right-icon-16x16.png)

[![Previous](/images/left-icon-16x16.png)](28)
[By Thread](index.html#29)
![Next](/images/right-icon-16x16.png)

### Current thread:

* **Defense in depth -- the Microsoft way (part 94): SAFER (SRPv1 and AppLocker alias SRPv2) bypass for dummies** *Stefan Kanthak via Fulldisclosure (Dec 22)*

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