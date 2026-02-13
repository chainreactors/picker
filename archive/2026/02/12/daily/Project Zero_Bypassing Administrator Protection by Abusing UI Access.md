---
title: Bypassing Administrator Protection by Abusing UI Access
url: https://projectzero.google/2026/02/windows-administrator-protection.html
source: Project Zero
date: 2026-02-12
fetch_date: 2026-02-13T04:18:57.403801
---

# Bypassing Administrator Protection by Abusing UI Access

[Project Zero](/)

---

[ ]

* [blog archive](/archive.html)
* [bug reports](https://project-zero.issues.chromium.org/savedsearches/7162405)
* [about](/about-pz.html)
* [Working at PZ](/working-at-project-zero.html)
* [0day: spreadsheet](/0day.html)
* [0day: Root Cause Analyses](https://googleprojectzero.github.io/0days-in-the-wild/rca.html)
* [vulnerability disclosure policy](/vulnerability-disclosure-policy.html)
* [reporting transparency](/reporting-transparency.html)
* search

# Bypassing Administrator Protection by Abusing UI Access

[2026-Feb-12](/2026/02/windows-administrator-protection.html "Permalink to this post")
James Forshaw

In my last blog post I introduced the new Windows feature, Administrator Protection and how it aimed to create a secure boundary for UAC where one didnât exist. I described one of the ways I was able to bypass the feature before it was released. In total I found 9 bypasses during my research that have now all been fixed.

In this blog post I wanted to describe the root cause of 5 of those 9 issues, specifically the implementation of UI Access, how this has been a long standing problem with UAC thatâs been under-appreciated, and how itâs being fixed now.

## A Question of Accessibility

Prior to Windows Vista any process running on a userâs desktop could control any window created by another, such as by sending [window messages](https://learn.microsoft.com/en-us/windows/win32/learnwin32/window-messages). This behavior could be abused if a privileged user, such as SYSTEM, displayed a user interface on the desktop. A limited user could control the UI and potentially elevate privileges. This was referred to as a [Shatter Attack](https://en.wikipedia.org/wiki/Shatter_attack), and was usually fixed by removing user interface components from privileged code.

As UAC encouraged running processes at different privilege levels on the same desktop, Microsoft introduced an additional feature, User Interface Privacy Isolation (UIPI). This used the Mandatory Integrity Control feature in UAC to limit what windows a process could interact with. If the integrity level of a process was lower than the process which created a window then it would be blocked from operations such as sending messages to that window. As an additional protection, Vista no longer ran user processes on the âserviceâ desktop so that even if UIPI was inadequate a user interface exposed by a service process was not accessible to limited processes.

To take an example, a limited user process has an assigned integrity level of âMediumâ while a UAC administrator process is âHighâ. In this case UIPI would block the limited user process sending messages to any window created by the administrator process, excluding a small set of explicitly permitted messages. It would also block other UI functionality such as [windows hooks](https://learn.microsoft.com/en-us/windows/win32/winmsg/hooks).

This introduced a problem for any user who relied on accessibility technology, such as screen readers. If the accessibility process was running as the limited user it could no longer interact with administrator processes created on the desktop. It would be blocked from both reading the contents of windows as well as performing operations such as clicking a button. This was not an acceptable compromise, so Vista needed a way to allow these applications to continue to work.

The solution Microsoft chose was to allocate a flag for the access token of a process called UI Access. If the processâ access token had this flag set when it initialized its connection to the Win32 subsystem, the process would be granted special permissions to bypass many of the restrictions imposed by UIPI. Enabling this flag through a call to `NtSetInformationToken` with the `TokenUIAccess` information class was gated behind a check for [SE\_TCB\_NAME privilege](https://learn.microsoft.com/en-us/windows/win32/secauthz/privilege-constants), and so it couldnât be performed by a limited user. Therefore in order to create a UI Access capable process a system service was necessary to enable the flag and create the new process.

UAC already needed a system service, so creating a UI Access process was made part of the same flow that was used for launching an administrator process through the `RAiLaunchAdminProcess` RPC call. When a UI Access process is created through this RPC call it does not show the consent prompt unlike administrator elevation. This is important as otherwise there was a risk that a user couldnât create the accessibility application needed by them to click the consent prompt for elevation.

In order to prevent malware just claiming to be an accessibility application the service imposed [some additional checks](https://learn.microsoft.com/en-us/windows/win32/winauto/uiauto-securityoverview) on the executable file which must be met to enable the UI access flag on the new process:

* It must have an embedded manifest with the `uiAccess` attribute set to `true`.
* It must be signed by a code signing certificate thatâs trusted by the local machine root certificate store. There was no special requirement for the certificate outside of this, for example it doesnât need to have a special EKU or cross signing by Microsoft.
* It must be stored in an administrator only location on the system drive, such as:
  + The `Program Files` directory
  + The `Windows` directory (excluding some known writable locations)
  + The `System32` directory (excluding some known writable locations)

If all the criteria are met then when the process is launched via `RAiLaunchAdminProcess` the service will take a copy of the callerâs access token, enable the UI Access flag and increase the integrity level as follows based on the caller:

* If the caller is a limited user of an UAC administrator it will set the integrity level to High.
* If the caller is an administrator then it will set the integrity level to High (normally a no-op).
* If the caller is a normal user, the integrity level is set to the callerâs integrity plus 16 up to a maximum of High.

A High integrity level is the absolute maximum allowed to be set, although there exists a higher level, âSystemâ thatâs reserved for service processes. Also note that the integrity level of the token is not changed if the caller already has the UI Access flag enabled, this is only important for normal users who donât automatically get set to High integrity. One benefit of setting an elevated integrity level is the created process cannot be opened for read or write access by a lower integrity process, preventing a limited user from injecting code into the new process and by extension getting access to the UI Access flag.

*As an aside, you can disable the UI Access flag on the token without TCB privilege. A valid UI Access process running as a normal user can âratchetâ itself up to High integrity by clearing the flag on its own token then respawning another copy of itself via the UAC service. As thereâs 4096 levels between Medium and High that would require calling the UAC service 255 times which is a little on the noisy side but it does work.*

Importantly, the UI Access flag only permits bypassing a limited set of operations such as sending window messages to other higher integrity processes. It doesnât permit using things like windows hooks which allow for code injection into a process. Therefore for a UI Access process running as a normal user with integrity level less than High it can interact with a spawned administrator process through messages, but it couldnât do something more invasive like hooking the window message queue.

However, if a limited user creates a UI access process, it would run with a High integrity level and could take over any administrator process that contains a window. A service process with a System integrity level could only be interacted with using windows messages. But thereâs no security boundary...