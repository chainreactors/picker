---
title: Beyond good ol’ Run key, Part 150
url: https://www.hexacorn.com/blog/2025/08/17/beyond-good-ol-run-key-part-150/
source: Hexacorn
date: 2025-08-18
fetch_date: 2025-10-07T00:17:15.081889
---

# Beyond good ol’ Run key, Part 150

[Skip to primary content](#content)

# [Hexacorn](https://www.hexacorn.com/blog/)

## Hexacorn

Search

### Main menu

* [Home](https://www.hexacorn.com/)
* [Services](https://www.hexacorn.com/services.html)
* [Products & Freebies](https://www.hexacorn.com/products_and_freebies.html)
* [Case Studies](https://www.hexacorn.com/case_studies.html)
* [Contact Us](https://www.hexacorn.com/contact.html)

### Post navigation

[← Previous](https://www.hexacorn.com/blog/2025/07/12/1-little-known-secret-of-advpack-dll-launchinfsection/)
[Next →](https://www.hexacorn.com/blog/2025/08/19/dll-forwardsideloading/)

# Beyond good ol’ Run key, Part 150

Posted on [2025-08-17](https://www.hexacorn.com/blog/2025/08/17/beyond-good-ol-run-key-part-150/ "12:08 am")  by  [adam](https://www.hexacorn.com/blog/author/adam/ "View all posts by adam")

I decided to add this post to this old series, but the scope of this post is – as you will find out soon – much wider.

You will find *servercoreshell.exe* program to be present on both Windows Server 2022 and 2025. It is an interesting binary, because it does a lot of stuff that, well… makes it interesting!

When you execute it, it displays the following screen:

[![](https://www.hexacorn.com/blog/wp-content/uploads/2025/08/servercoreshell_0-1024x577.png)](https://www.hexacorn.com/blog/wp-content/uploads/2025/08/servercoreshell_0.png)

I have not explored these options.

Because… the far more interesting things happen under the hood. If you start Process Monitor before you execute *servercoreshell.exe* program and then look at the events collected during a single test session you will find out that some of them are… well.. interesting!

It accesses a lot of interesting Registry locations, including:

* *HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\Explorer\DisableCurrentUserRunOnce*
* *HKCU\Software\Microsoft\Windows\CurrentVersion\RunOnce*
* *HKLM\Software\Microsoft\Windows\CurrentVersion\RunOnce*
* *HKLM\Software\Microsoft\Windows\CurrentVersion\RunOnceEx*
* *HKLM\Software\WOW6432Node\Microsoft\Windows\CurrentVersion\RunOnceEx*
* *HKLM\SOFTWARE\Microsoft\ServerCore\Shell Launcher\Shell*
* *HKLM\SOFTWARE\Microsoft\ServerCore\Shell Launcher\<SID>*\Shell
* HKEY\_LOCAL\_MACHINE\SOFTWARE\Microsoft\ServerCore\Shell Launcher\Users\Local\<user>\Shell
* HKEY\_LOCAL\_MACHINE\SOFTWARE\Microsoft\ServerCore\Shell Launcher\Users\Domain\<user>\Shell

And that *HKLM\SOFTWARE\Microsoft\ServerCore\Shell Launcher\Shell* is a DEFAULT persistent location that allows me to put this post in the *Beyond good ol’ Run key* series:

[![](https://www.hexacorn.com/blog/wp-content/uploads/2025/08/servercoreshell_1.png)](https://www.hexacorn.com/blog/wp-content/uploads/2025/08/servercoreshell_1.png)

For starters, we can modify the content of the file *c:\WINDOWS\System32\servercoreshelllaunch.bat*. We can also change the value of the Registry entry that *shell* points to. Then the only remaining bit is to ensure the *servercoreshell.exe* program is executed at some time during system start, or after user logs in.

Bad news though — need Trusted Installer rights for that.

Still, this single program runs through many ‘shell’ initialization routines that Windows Symbols describe as:

* ProcessHKLMRunOnce
* \_RunStartupGroup
* ProcessPackagedStartupTasks
* ProcessRun6432
* LaunchCustomShellAndWait

During my tests, I played around and pointed some of the aforementioned registry settings to calculator, notepad, etc. and I discovered that the *servercoreshell.exe* program often goes into a never-ending loop. When you launch it, then kill the main window, it will just continue to spawn its own copies. And when I set *shell* value to a randomly named user under *HKEY\_LOCAL\_MACHINE\SOFTWARE\Microsoft\ServerCore\Shell Launcher\Users\Domain\<user>\Shell* to calculator, I ended up with a never-ending loop of new Calculator instances being spawn:

[![](https://www.hexacorn.com/blog/wp-content/uploads/2025/08/servercoreshell_4.png)](https://www.hexacorn.com/blog/wp-content/uploads/2025/08/servercoreshell_4.png)

I suspect it’s a little buggy…

I also believe the *servercoreshell.exe* program is related to this documented [Shell Launcher](https://learn.microsoft.com/en-us/windows/configuration/shell-launcher/) feature:

> Shell Launcher is a Windows feature that you can use to replace the default Windows Explorer shell (Explorer.exe) with a Windows desktop application or a Universal Windows Platform (UWP) app. This feature is useful for creating a custom user experience on devices that are used for a specific purpose, including kiosks, ATMs, and digital signage.

[![](https://www.hexacorn.com/blog/wp-content/uploads/2025/08/servercoreshell_2.png)](https://www.hexacorn.com/blog/wp-content/uploads/2025/08/servercoreshell_2.png)

Installing the latter on Windows 11 introduces a slightly different executable to the system though: *ShellLauncherConfig.exe* and the *shell* keys it relies on are located in a different place too:

* *HKEY\_LOCAL\_MACHINE\SOFTWARE\Microsoft\Windows Embedded\Shell Launcher*
* *HKEY\_LOCAL\_MACHINE\SOFTWARE\Microsoft\Windows Embedded\Shell Launcher cached*

[![](https://www.hexacorn.com/blog/wp-content/uploads/2025/08/servercoreshell_3.png)](https://www.hexacorn.com/blog/wp-content/uploads/2025/08/servercoreshell_3.png)

Looks like the feature has at least 2 different, distinctive versions for server and non-server versions of Windows.

This entry was posted in [Autostart (Persistence)](https://www.hexacorn.com/blog/category/autostart-persistence/), [LOLBins](https://www.hexacorn.com/blog/category/living-off-the-land/lolbins/) by [adam](https://www.hexacorn.com/blog/author/adam/). Bookmark the [permalink](https://www.hexacorn.com/blog/2025/08/17/beyond-good-ol-run-key-part-150/ "Permalink to Beyond good ol’ Run key, Part 150").

[Privacy Policy](https://www.hexacorn.com/blog/privacy-policy/) [Proudly powered by WordPress](https://wordpress.org/ "Semantic Personal Publishing Platform")