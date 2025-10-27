---
title: An Elf walks into the bar…
url: https://www.hexacorn.com/blog/2023/05/11/an-elf-walks-into-the-bar/
source: Hexacorn
date: 2023-05-12
fetch_date: 2025-10-04T11:39:43.950424
---

# An Elf walks into the bar…

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

[← Previous](https://www.hexacorn.com/blog/2023/05/05/malware-some-musings-about-the-meaning-of-the-word/)
[Next →](https://www.hexacorn.com/blog/2023/05/11/pe-section-names-re-visited-again-in-2023/)

# An Elf walks into the bar…

Posted on [2023-05-11](https://www.hexacorn.com/blog/2023/05/11/an-elf-walks-into-the-bar/ "10:29 pm")  by  [adam](https://www.hexacorn.com/blog/author/adam/ "View all posts by adam")

Windows 11’s advapi32.dll includes interesting export functions:

* ElfBackupEventLogFileA
* ElfBackupEventLogFileW
* ElfChangeNotify
* ElfClearEventLogFileA
* ElfClearEventLogFileW
* ElfCloseEventLog
* ElfDeregisterEventSource
* ElfFlushEventLog
* ElfNumberOfRecords
* ElfOldestRecord
* ElfOpenBackupEventLogA
* ElfOpenBackupEventLogW
* ElfOpenEventLogA
* ElfOpenEventLogW
* ElfReadEventLogA
* ElfReadEventLogW
* ElfRegisterEventSourceA
* ElfRegisterEventSourceW
* ElfReportEventA
* ElfReportEventAndSourceW
* ElfReportEventW

And I know nothing about them… while they are obviously exported by advapi32.dll and for some unknown reason, they do not seem to be imported … by anything (no .exe, .dll import these functions, at least directly!). Plus, most of these apis’ code reference NDR functions (RPC), so unless you are really well-versed in these, it’s hard to reverse them 🙁

BUT

A [quick google](https://learn.microsoft.com/en-us/windows/win32/eventlog/event-log-file-format) suggests that these are not Linux-related (refrerence to ‘ELF’), and are actually Event Log File (also ‘ELF’)-related. In a trivial pursuit of the truth, we look at the code of Elf\* functions and their invocations and we can almost immediately see that f.ex. that [RegisterEventSourceW](https://learn.microsoft.com/en-us/windows/win32/api/winbase/nf-winbase-registereventsourcew) is calling ElfRegisterEventSourceW internally. So… looks like either intentionally, or accidentally the MS coders exposed a lower-level interface to Event Logs.

As such, functions:

* ElfClearEventLogFileA
* ElfClearEventLogFileW

may be perhaps of interest?

This entry was posted in [Windows 11](https://www.hexacorn.com/blog/category/windows-11/) by [adam](https://www.hexacorn.com/blog/author/adam/). Bookmark the [permalink](https://www.hexacorn.com/blog/2023/05/11/an-elf-walks-into-the-bar/ "Permalink to An Elf walks into the bar…").

[Privacy Policy](https://www.hexacorn.com/blog/privacy-policy/) [Proudly powered by WordPress](https://wordpress.org/ "Semantic Personal Publishing Platform")