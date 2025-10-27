---
title: Defense in depth -- the Microsoft way (part 84): (no) fun with	%COMSPEC%
url: https://seclists.org/fulldisclosure/2023/Mar/15
source: Full Disclosure
date: 2023-03-25
fetch_date: 2025-10-04T10:40:59.640702
---

# Defense in depth -- the Microsoft way (part 84): (no) fun with	%COMSPEC%

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

[![Previous](/images/left-icon-16x16.png)](14)
[By Date](date.html#15)
[![Next](/images/right-icon-16x16.png)](16)

[![Previous](/images/left-icon-16x16.png)](14)
[By Thread](index.html#15)
[![Next](/images/right-icon-16x16.png)](16)

![](/shared/images/nst-icons.svg#search)

# Defense in depth -- the Microsoft way (part 84): (no) fun with %COMSPEC%

---

*From*: "Stefan Kanthak" <stefan.kanthak () nexgo de>
*Date*: Wed, 22 Mar 2023 19:50:40 +0100

---

```
Hi @ll,

the documentation of the builtin START command
<https://technet.microsoft.com/en-us/library/cc770297.aspx>
of Windows NT's command processor CMD.EXE states:

| When you run a command that contains the string "CMD" as the first
| token without an extension or path qualifier, "CMD" is replaced
| with the value of the COMSPEC variable.
| This prevents users from picking up cmd from the current directory.
  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

REALLY?

Demonstration:
~~~~~~~~~~~~~~

0) Start the command processor via Start->Run %COMSPEC%

1) Show that START CMD ... works:

   START CMD /C PAUSE

2) Change the current directory to your TEMP directory
   (or any other directory where you are allowed to create files)
   and create an empty file CMD.EXE there:

   CHDIR /D "%TEMP%"
   COPY NUL: CMD.EXE

3) (Try to) execute this file to show the error messages to expect:

   .\CMD.EXE
   "%CD%\CMD.EXE"
   "%TEMP%\CMD.EXE"

   This yields a popup "This app can't run on your PC. ..." and an
   error message "Access denied".

4) Run the command from step 1) again:

   START CMD /C PAUSE

   Popup and error message from step 3) are shown again!

   OUCH: Contrary to the documentation cited above,
         START CMD <anything>
         but "picks up" CMD.EXE from the current directory.

5) Rename the empty file CMD.EXE to CMD.COM and repeat step 4)

   RENAME CMD.EXE CMD.COM
   START CMD /C PAUSE

   Popup and error message from steps 4) and 5) are shown again!

   OUCH: Contrary to the documentation cited above,
         START CMD <anything>
         also "picks up" CMD.COM from the current directory.

6) Rename the empty file CMD.COM to CMD.BAT, write the strings
   ECHO and VERIFY to it and repeat step 4)

   RENAME CMD.COM CMD.BAT
   ECHO 1>CMD.BAT ECHO
   ECHO 1>>CMD.BAT VERIFY
   START CMD /C PAUSE

   This yields the following output

| ECHO is on
| VERFIY is on

   OUCH: Contrary to the documentation cited above,
         START CMD <anything>
         also "picks up" CMD.BAT from the current directory.

   JFTR: repetition of step 6) with other extensions from the
         environment variable PATHEXT is left as an exercise
         to the reader.

7) Give another START command a try:

   START EXIT

   A second command processor starts and exits immediately.

8) Set the variable COMSPEC to the pathname of an arbitrary
   program (here: %SystemRoot%\System32\REG.EXE) and run the
   START command from step 7) again:

   SET COMSPEC=%SystemRoot%\System32\REG.EXE
   START EXIT

   This yields the following output

| ERROR: Invalid Argument/Option - '/K'.
| Type "REG /?" for usage.

   OOPS: START <anything> evaluates the variable COMSPEC and
         runs an ARBITRARY executable!

   JFTR: notice the switch /K fed to the executable.

9) Run 2 arbitrary (builtin) commands in a pipeline

   ECHO | SHIFT

   This yields the following output

| ERROR: Invalid Argument/Option - '/S'.
| Type "REG /?" for usage.
| ERROR: Invalid Argument/Option - '/S'.
| Type "REG /?" for usage.

   OOPS: the command processor runs each command of a pipeline in
         a NEW process determined by the contents of the variable
         COMSPEC!

   JFTR: notice the switch /S fed to the executable.

10) Set the variable COMSPEC to an EMPTY value, i.e. remove it,
    and repeat step 8)

    SET COMSPEC=
    START EXIT

    This yields the MISLEADING error message
    "The environment variable COMSPEC does not point to CMD.EXE."

    The correct error message is but
    "The environment variable COMSPEC is missing."

11) Repeat step 9)

    BREAK | TYPE

    OUCH: the command processor CRASHES with an access violation
          reading address 0

    This ABSOLUTE BEGINNER's programming error is listed as
    "CWE 476: NULL Pointer Dereference"
    <https://cwe.mitre.org/data/definitions/476.html>

    The weakness demonstrated in steps 8) and 9) is listed as
    "CWE-73: External Control of File Name or Path"
    <https://cwe.mitre.org/data/definitions/73.html>, the
    WELL-KNOWN attacks on it are listed as
    "CAPEC-13: Subverting Environment Variable"
    <https://capec.mitre.org/data/definitions/13.html>

    The weakness demonstrated in steps 4) to 6) is listed as
    "CWE-426: Untrusted Search Path"
    <https://cwe.mitre.org/data/definitions/426.html> and/or
    "CWE-427: Uncontrolled Search Path Element"
    <https://cwe.mitre.org/data/definitions/427.html>, the
    WELL-KNOWN attacks on it are listed as
    "CAPEC-471: Search Order Hijacking"
    <https://capec.mitre.org/data/definitions/471.html>

stay tuned, and far away from Microsoft's POORLY written crap
Stefan
_______________________________________________
Sent through the Full Disclosure mailing list
https://nmap.org/mailman/listinfo/fulldisclosure
Web Archives & RSS: https://seclists.org/fulldisclosure/
```

---

[![Previous](/images/left-icon-16x16.png)](14)
[By Date](date.html#15)
[![Next](/images/right-icon-16x16.png)](16)

[![Previous](/images/left-icon-16x16.png)](14)
[By Thread](index.html#15)
[![Next](/images/right-icon-16x16.png)](16)

### Current thread:

* **Defense in depth -- the Microsoft way (part 84): (no) fun with %COMSPEC%** *Stefan Kanthak (Mar 24)*

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