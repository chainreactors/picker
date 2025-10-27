---
title: Defense in depth -- the Microsoft way (part 94): BACKDOOR	planted in AppLocker
url: https://seclists.org/fulldisclosure/2025/Sep/66
source: Full Disclosure
date: 2025-09-24
fetch_date: 2025-10-02T20:36:09.363940
---

# Defense in depth -- the Microsoft way (part 94): BACKDOOR	planted in AppLocker

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

[![Previous](/images/left-icon-16x16.png)](65)
[By Date](date.html#66)
[![Next](/images/right-icon-16x16.png)](67)

[![Previous](/images/left-icon-16x16.png)](65)
[By Thread](index.html#66)
[![Next](/images/right-icon-16x16.png)](67)

![](/shared/images/nst-icons.svg#search)

# Defense in depth -- the Microsoft way (part 94): BACKDOOR planted in AppLocker

---

*From*: Stefan Kanthak via Fulldisclosure <fulldisclosure () seclists org>
*Date*: Mon, 22 Sep 2025 16:18:01 +0200

---

```
Hi @ll,

since several years Microsoft installs the DLLs domain_actions.dll
and well_known_domains.dll as part of their Edge browser as well as
Windows' WebView component into each and every user profile,
 UNPROTECTED against tampering.

On Windows 11 24H2 their paths are currently
"%LOCALAPPDATA%\Microsoft\Edge\User Data\Domain Actions\3.0.0.16\domain_actions.dll"
"%LOCALAPPDATA%\Microsoft\Edge\User Data\Domain Actions\3.0.0.16\well_known_domains.dll"
"%LOCALAPPDATA%\Microsoft\Windows\SharedWebView\EBWebView\Domain Actions\3.0.0.16\domain_actions.dll"
"%LOCALAPPDATA%\Microsoft\Windows\SharedWebView\EBWebView\Domain Actions\3.0.0.16\well_known_domains.dll"

Security-conscious Windows administrators of course block execution
of DLLs in user-writable locations since more than 24 years via
SAFER alias Software Restriction Policies, AppLocker or WDAC alias
Windows Defender Application Control: see for example
"Using Software Restriction Policies to Protect Against Unauthorized Software"
<https://technet.microsoft.com/en-us/library/cc507878.aspx> or my
own <https://skanthak.hier-im-netz.de/SAFER.html>

The release notes for Edge 135.0.3179.11 (Beta) published 2025-03-13
and the release notes for Edge 135.0.3179.54 (Stable) published
2025-04-03 contain the following tell-tale section:

| Fixes
| * Fixed an issue where AppLocker blocked well-known DLLs such as
|   well_known_domains.dll and domain_actions.dll.

In other words: in March/April 2025 Microsoft planted a BACKDOOR in
AppLocker which allows execution of said DLLs!

Remediation: add EXPLICIT deny rules to your AppLocker configuration!

stay tuned, and far away from UNTRUSTWORTHY crap
Stefan Kanthak
_______________________________________________
Sent through the Full Disclosure mailing list
https://nmap.org/mailman/listinfo/fulldisclosure
Web Archives & RSS: https://seclists.org/fulldisclosure/
```

---

[![Previous](/images/left-icon-16x16.png)](65)
[By Date](date.html#66)
[![Next](/images/right-icon-16x16.png)](67)

[![Previous](/images/left-icon-16x16.png)](65)
[By Thread](index.html#66)
[![Next](/images/right-icon-16x16.png)](67)

### Current thread:

* **Defense in depth -- the Microsoft way (part 94): BACKDOOR planted in AppLocker** *Stefan Kanthak via Fulldisclosure (Sep 22)*
  + <Possible follow-ups>
  + [Defense in depth -- the Microsoft way (part 94): BACKDOOR planted in AppLocker](67) *Stefan Kanthak via Fulldisclosure (Sep 22)*

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