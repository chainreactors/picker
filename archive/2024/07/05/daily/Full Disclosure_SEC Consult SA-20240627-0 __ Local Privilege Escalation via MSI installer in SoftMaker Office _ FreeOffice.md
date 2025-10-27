---
title: SEC Consult SA-20240627-0 :: Local Privilege Escalation via MSI installer in SoftMaker Office / FreeOffice
url: https://seclists.org/fulldisclosure/2024/Jul/5
source: Full Disclosure
date: 2024-07-05
fetch_date: 2025-10-06T17:51:33.283571
---

# SEC Consult SA-20240627-0 :: Local Privilege Escalation via MSI installer in SoftMaker Office / FreeOffice

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

# SEC Consult SA-20240627-0 :: Local Privilege Escalation via MSI installer in SoftMaker Office / FreeOffice

---

*From*: SEC Consult Vulnerability Lab via Fulldisclosure <fulldisclosure () seclists org>
*Date*: Thu, 27 Jun 2024 10:18:16 +0000

---

```
SEC Consult Vulnerability Lab Security Advisory < 20240627-0 >
=======================================================================
               title: Local Privilege Escalation via MSI installer
             product: SoftMaker Office / FreeOffice
  vulnerable version: SoftMaker Office 2024 / NX before revision 1214
                      FreeOffice 2021 Revision 1068
                      FreeOffice 2024 before revision 1215
       fixed version: SoftMaker Office 2024 / NX - revision 1214
                      FreeOffice 2024 - revision 1215
          CVE number: CVE-2023-7270
              impact: high
            homepage: https://www.softmaker.com/en/
               found: 2023-11-27
                  by: Michael Baer (Office Fürth)
                      SEC Consult Vulnerability Lab

                      An integrated part of SEC Consult, an Eviden business
                      Europe | Asia

                      https://www.sec-consult.com

=======================================================================

Vendor description:
-------------------
"SoftMaker Office makes working with documents, spreadsheets and presentations
a breeze – whether you're on Windows, Linux, Mac, iOS or Android."

Source: https://www.softmaker.com/en/products/softmaker-office

Business recommendation:
------------------------
The vendor provides a patch which should be installed immediately.

SEC Consult highly recommends to perform a thorough security review of the
product conducted by security professionals to identify and resolve potential
further security issues.

Vulnerability overview/description:
-----------------------------------
1) Local Privilege Escalation via MSI installer (CVE-2023-7270)
The SoftMaker Office and FreeOffice MSI installer files were found to produce
a visible conhost.exe window running as the SYSTEM user when using the repair
function of msiexec.exe.

This allows a local, low-privileged attacker to use a chain of actions,
to open a fully functional cmd.exe with the privileges of the SYSTEM user.

Note:
This attack does not work using a recent version of the Edge Browser or
Internet Explorer. A different browser, such as Chrome or Firefox, needs to be
used. Also make sure, that Edge or IE have not been set as default browser
and that Firefox or Chrome are not running before attempting to exploit it.
Otherwise, the spawned process would be running with your own permissions and
the installer will just add a new tab to the browser, instead of spawning a
new process with SYSTEM.

Proof of concept:
-----------------
1) Local Privilege Escalation via MSI installer (CVE-2023-7270)
For the exploit to work, SoftMaker Office or FreeOffice have to be installed
via the MSI file. Afterwards, any low-privileged user can start the
repair of the software by double-clicking the installer and trigger
the vulnerable actions without a UAC popup. The installer, if deleted from it's
original location, can be found in C:\Windows\Installer with a randomized name.

During the repair process, a console application gets called with SYSTEM
privileges and performs a read action on some files.

SoftMaker Office: Executes 7z.exe, which reads
C:\Program Files\SoftMaker Office 2024\tb\7z.exe

FreeOffice: Executes syspin.exe, which reads
C:\Windows\SysWOW64\OneCoreCommonProxyStub.dll

This can be used by an attacker by simply setting an oplock on the files
mentioned before.

As soon as it gets read, the process is blocked until the lock is released.

To do that, one can use the 'SetOpLock.exe' tool from
"https://github.com/googleprojectzero/symboliclink-testing-tools";
with the following parameters:

while ($true) { SetOpLock.exe "C:\Program Files\SoftMaker Office 2024\tb\7z.exe" x }
while ($true) { SetOpLock.exe "C:\Windows\SysWOW64\OneCoreCommonProxyStub.dll" x }

See figure 1 [soft_lock.png] and figure 2 [lock.png]

During the repair process, the locked file is accessed multiple times. The lock
has to be released by pressing ENTER several times before the window opens.

If the window appears, the lock should not be released to keep the
window open. The window that gets opened when the console program is
executed doesn't close and can then be interacted with.

Note 1: The syspin.exe window is minimized. When the lock is triggered, it
is advised to check the taskbar whether a window with a blue arrow,
see figure 7 [taskbar.png], exists.

The attacker can then perform the following actions to spawn a SYSTEM shell:
- Right click on the top bar of the window
- Click on properties, see figure 3 [soft_openbrowser.png] and figure 4 [openbrowser.png]
- Under options, click on the "new console features" link
- Open the link with e.g. firefox
- In the opened browser window press the key combination CTRL+o
- Type cmd.exe in the top bar and press Enter, see figure 5 [soft_cmd.png] and figure 6 [cmd.png]

Note 2: This does not work using a recent version of the Edge Browser.

Note 3: The program syspin.exe is invoked several times, sometimes without
elevated privileges. If the final cmd.exe is not elevated, release the lock
and wait for the next syspin.exe invocation. During our test, the fifth
window was run with elevated privileges.

Vulnerable / tested versions:
-----------------------------
The following versions have been tested by SEC Consult which were the most recent
versions available at the time of the test:
* SoftMaker Office 2024 - 24.0.6034
* FreeOffice 2021 Revision 1068

According to the vendor, all versions of SoftMaker Office NX/2024 before revision 1214
and FreeOffice 2024 before revision 1215 with the MSI installer are affected.

FreeOffice 2021 is unsupported and will not be fixed according to the vendor.

Vendor contact timeline:
------------------------
2023-12-02: Contacting vendor through sales () softmaker de,
             asking for security contact.
2023-12-07: Contacting vendor through https://www.softmaker.com/en/support/customer-support
             asking for security contact.
2024-01-11: Contacting vendor through https://www.softmaker.com/en/support/customer-support
             asking for security contact.
2024-01-11: Vendor provides security contact and asks for advisory
             unencrypted
2024-01-12: Sending advisory draft unencrypted to security contact
2024-02-17: Asking for status of vulnerability, no response
2024-03-06: Asking for status of vulnerability, no response
2024-04-08: Asking for a status update, setting release date to
             17th April.
2024-04-08: Vendor response, seems not to have received our previous mails.
             Asking for deadline extension as a release it already planned.
2024-04-09: Sending advisory draft again, extending deadline.
2024-04-11: Asking whether email was received, confirmed. Sent proposed
             solution.
2024-04-22: Asking when new release is planned and whether fixes could be
             incorporated.
2024-04-23: Vendor response, current service pack update not including f...