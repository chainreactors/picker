---
title: Some notes on Windows 11 Notepad
url: https://www.hexacorn.com/blog/2024/10/26/some-notes-on-windows-11-notepad/
source: Hexacorn
date: 2024-10-27
fetch_date: 2025-10-06T18:49:09.966058
---

# Some notes on Windows 11 Notepad

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

[← Previous](https://www.hexacorn.com/blog/2024/10/25/going-reverse-on-reversing-tools/)
[Next →](https://www.hexacorn.com/blog/2024/11/05/procmonning-the-win11_24h2-build/)

# Some notes on Windows 11 Notepad

Posted on [2024-10-26](https://www.hexacorn.com/blog/2024/10/26/some-notes-on-windows-11-notepad/ "11:53 pm")  by  [adam](https://www.hexacorn.com/blog/author/adam/ "View all posts by adam")

The new win11 version of Notepad accepts a few command line options that i have not seen documented anywhere (or only documented partially).

* /A – forces Notepad to read the input file as ANSI
* /W – forces Notepad to read the input file as WIDE (Unicode 16LE)
* /.SETUP – tells Notepad it was launched by the Installer; AFAICT running Notepad with this option literally DoSes it
* /.SETUP <filename> – same as above except we try to open the file <filename> — still DoS though
* RestartByRestartManager:<GUID> – mentioned by [@nas\_bench](https://twitter.com/nas_bench) [here](https://x.com/nas_bench/status/1743085051267424584) – used to restore some of the AutoSaved documents; the information is saved under *HKCU\Software\Microsoft\Notepad\Autosave\GUID* in a form of three coma-separated values f.ex.:

[![](https://www.hexacorn.com/blog/wp-content/uploads/2024/10/notepad2.png)](https://www.hexacorn.com/blog/wp-content/uploads/2024/10/notepad2.png)

so analyzing this key and its children may have some DFIR value, potentially.

The first value is a code page (0,1=ANSI; 2,3=Unicode LE/BE; 4,5=UTF8 with or w/o BOM, 6=Chinese), second is probably a document path, and the third is a working directory. These all need to be confirmed as I am making quick&dirty assumptions here.

Launching *c:\windows\notepad.exe* under xdbg makes the old-fashioned Notepad window appear, with a banner encouraging the user to launch the new version of Notepad (Microsoft app):

[![](https://www.hexacorn.com/blog/wp-content/uploads/2024/10/notepad1.png)](https://www.hexacorn.com/blog/wp-content/uploads/2024/10/notepad1.png)

This behavior is a bit unexpected and am wondering if it could be somehow abused.

The Launch button executes the so-called Centennial version of Notepad located here:

```
%LOCALAPPDATA%\Microsoft\WindowsApps\Microsoft.WindowsNotepad_8wekyb3d8bbwe\notepad.exe
```

In some circumstances a file *probe.autosave* may be created by new Notepad.

The info about currently opened tabs seems to be stored in this folder:

```
C:\Users\<USER>\AppData\Local\Packages\Microsoft.WindowsNotepad_8wekyb3d8bbwe\LocalState
```

and there (already) is a [library](https://github.com/ogmini/Notepad-State-Library) for parsing these.

Launching *notepad.exe* leads to Windows App being executed, because of these [new settings](https://learn.microsoft.com/en-us/windows/apps/desktop/modernize/desktop-to-uwp-extensions) in the Registry:

```
HKLM\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Image File Execution Options\notepad.exe\0
AppExecutionAliasRedirect = 1
AppExecutionAliasRedirectPackages = *
FilterFullPath = C:\Windows\System32\notepad.exe
```

Changing the value of *AppExecutionAliasRedirect* from 1 to 0 will bring the old Notepad back. And lo and behold, there is a ‘legitimate’ way to disable new Notepad too – the Advanced App Settings allow us to disable the so-called Windows Apps aliases:

[![](https://www.hexacorn.com/blog/wp-content/uploads/2024/10/notepad3-1024x795.png)](https://www.hexacorn.com/blog/wp-content/uploads/2024/10/notepad3.png)

Once you disable the Notepad alias, the old Notepad will return. And if you want to disable that annoying banner showing up in this old Notepad you can add the following Registry entry:

```
HKCU\Software\Microsoft\Notepad
ShowStoreBanner (dword) = 0
```

And with that, we are back to the good ol’ Notepad version we all love 😉

[![](https://www.hexacorn.com/blog/wp-content/uploads/2024/10/notepad4.png)](https://www.hexacorn.com/blog/wp-content/uploads/2024/10/notepad4.png)

The Windows 11 changes are very interesting from the DFIR perspective. Many old programs we took for granted (for decades!) are now exhibiting new behaviors that need an additional research effort. This is actually quite exciting because we all want to close cases in a conclusive way and knowing how to interpret the superset of all forensic artifacts is of a paramount importance…

This entry was posted in [Archaeology](https://www.hexacorn.com/blog/category/archaeology/), [Forensic Analysis](https://www.hexacorn.com/blog/category/forensic-analysis/) by [adam](https://www.hexacorn.com/blog/author/adam/). Bookmark the [permalink](https://www.hexacorn.com/blog/2024/10/26/some-notes-on-windows-11-notepad/ "Permalink to Some notes on Windows 11 Notepad").

[Privacy Policy](https://www.hexacorn.com/blog/privacy-policy/) [Proudly powered by WordPress](https://wordpress.org/ "Semantic Personal Publishing Platform")