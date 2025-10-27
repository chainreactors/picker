---
title: Inside the Unified Log 2 Why browse the log
url: https://eclecticlight.co/2025/09/25/inside-the-unified-log-2-why-browse-the-log/
source: Instapaper: Unread
date: 2025-09-27
fetch_date: 2025-10-02T20:48:09.483707
---

# Inside the Unified Log 2 Why browse the log

[Skip to content](#content)

[![](https://eclecticlight.co/wp-content/uploads/2015/01/eclecticlightlogo-e1421784280911.png?w=103)](https://eclecticlight.co/)

# [The Eclectic Light Company](https://eclecticlight.co/)

Macs & painting – 🦉 No AI content

##### Main navigation

Menu

* [Downloads](https://eclecticlight.co/downloads/)
* [Freeware](https://eclecticlight.co/free-software-menu/)
* [M-series Macs](https://eclecticlight.co/m1-macs/)
* [Mac Problems](https://eclecticlight.co/mac-troubleshooting-summary/)
* [Mac articles](https://eclecticlight.co/mac-problem-solving/)
* [Macs](https://eclecticlight.co/category/macs/)
* [Art](https://eclecticlight.co/painting-topics/)

[hoakley](https://eclecticlight.co/author/hoakley/)
[September 25, 2025](https://eclecticlight.co/2025/09/25/inside-the-unified-log-2-why-browse-the-log/)
[Macs](https://eclecticlight.co/category/macs/), [Technology](https://eclecticlight.co/category/technology/)

# **Inside the Unified Log 2:** *Why browse the log?*

Following the introduction of the Unified Log, a surprising number of folk you would expect to use it have stopped. Some experienced developers and those providing advice in Apple Support Communities seemingly take pride in their lack of log literacy, claiming that the log is now impossible to use, and only accessible to Apple’s engineers. While it does present obstacles, pretending that the log isn’t a vital tool in diagnosis and understanding is burying your head in the sand. This article shows why.

#### Why the log?

The log provides support for several purposes. It’s widely used to investigate events such as bugs and unexpected behaviours, to establish their cause before working out how to fix them, in diagnosis and troubleshooting. It’s also used to discover how subsystems within macOS work, and what they do. Examples of those include LaunchServices, DAS-CTS scheduling and dispatching, and RunningBoard, all of which are nearly invisible to other methods, but write copious and explicit entries in the log. With its precise time recording and special Signpost log entries, it’s also invaluable for measuring performance, hence in optimising code.

Concentrating on the log’s use in diagnosis, log entries can be used to answer most of the key questions:

* What happened?
* When did it happen?
* Who made it happen?
* How did it happen?
* Why did it happen?
* What can I do about it?

#### Diagnose a mystery update

To illustrate those in practice, I’ll use an example that happens to be fresh in my mind, the silent updating of XProtect data last week. The only two clues available outside the log were the fact that XProtect had been updated, and that had occurred at 06:46:43 GMT on the morning of 17 September. There was no record of this event anywhere else that might have given any better information on how it had occurred.

Browsing the log from one second earlier confirmed what and when that had happened. I quickly discovered who made it happen when I found the log entry
`2025-09-17 06:46:42.615072 com.apple.duetactivityscheduler REQUESTING START: 0:com.apple.security.syspolicy.xprotect-update:7874AD`
revealing that update had been accomplished by a background check scheduled and dispatched by DAS-CTS, and performed by an update service com.apple.security.syspolicy.xprotect-update.

That in turn fired up XProtectUpdateService, which recorded that it promptly completed and activated the update:
`2025-09-17 06:46:42.695517 com.apple.xprotect Connecting to XProtectUpdateService
2025-09-17 06:46:42.744182 com.apple.security.XProtectFramework.XProtectUpdateService XProtectUpdateService booting
2025-09-17 06:46:43.157255 com.apple.security.XProtectFramework.XProtectUpdateService Attempting to apply update: [private]
2025-09-17 06:46:43.191178 com.apple.security.XProtectFramework.XProtectUpdateService Update completed. Activated update [private]`

XProtectUpdateService initiated a connection to the iCloud service now used to update XProtect in Sequoia and later, but log entries didn’t show the update being downloaded from that source. Instead, there was an error reported in the entry
`2025-09-17 06:46:43.193159 com.apple.syspolicy.activities Finished Xprotect update in 496.4100122451782 ms: Error Domain=XProtectUpdateError Code=2 "Activated update LocalUpdate[5315]" UserInfo={NSLocalizedDescription=Activated update LocalUpdate[5315]}`

Although the messages in many of these log entries are opaque, that entry makes it clear that XProtectUpdateService hadn’t downloaded the new version from iCloud, but had activated a local update, which we know from experience means the copy already downloaded to the traditional XProtect location had been used to install that update in its new location. That used to be available to the user through the `xprotect update` command, but is no longer. Thus, the only way that update could have been installed was the result of com.apple.security.syspolicy.xprotect-update being run routinely.

If we can’t intervene and force the update manually, the final piece of information we need is how often com.apple.security.syspolicy.xprotect-update is run, and that’s revealed into a later log entry:
`2025-09-17 06:46:43.202474 com.apple.duetactivityscheduler Submitted: 0:com.apple.security.syspolicy.xprotect-update:58B6CE at priority 5 with interval 86400 (Wed Sep 17 22:58:51 2025 - Thu Sep 18 18:58:51 2025)`
i.e. every 86,400 seconds, or 24 hours.

#### Procedure

How difficult was that to discover? Even with minimal prior knowledge, consummately easy, and it only took a couple of minutes.

My starting point was the timestamp reported for the update by `xprotect version`, of 06:46:43 GMT. I therefore set [LogUI](https://eclecticlight.co/consolation-t2m2-and-log-utilities/) to display 5 seconds of log starting from one second before that. In the screenshots below, times are shown in BST, one hour in advance of GMT.

[![](https://eclecticlight.co/wp-content/uploads/2025/09/xprolog1.jpg)](https://eclecticlight.co/wp-content/uploads/2025/09/xprolog1.jpg)

This returned a total of 7,174 log entries, far too many to browse. Knowing that I was looking for entries concerning XProtect, I then typed that into the search box and pressed Return, to display only those entries whose message contained the text `xprotect`.

[![](https://eclecticlight.co/wp-content/uploads/2025/09/xprolog2.jpg)](https://eclecticlight.co/wp-content/uploads/2025/09/xprolog2.jpg)

That narrowed down the number of entries to just 65, starting with the scoring and dispatch of com.apple.security.syspolicy.xprotect-update by DAS-CTS at 42.608967 seconds, and containing all the entries quoted above. Just to be certain that I hadn’t missed anything relevant, I then cleared the search box and pressed Return to display all log entries again, scrolled down to 42.608967 seconds, and checked through those for the period to 43.19315 seconds, when the update had completed.

Of course, not all log investigations are as simple or successful, but many are just as straightforward. The main limitation isn’t the excessive number of log entries, but those from subsystems that make very few entries, as occurs in Spotlight indexing and search. There’s always a way to filter out unwanted entries, but you can’t magic in entries that were never made in the first place.

#### Conclusions

Browsing the log might appear daunting, even overwhelming or terrifying at first, but as you become more familiar with it you appreciate the rich information it can provide. Log literacy is one of the basic skills required for anyone who wants or needs to dig deeper into their Mac or Apple device. Without it diagnosis, research and performance measurement are like trying to paint a landscape while wearing a blindfold.

### Share this:

* [Click to share on X (Opens in new window)
  X](https://eclecticlight.co/2025/09/25/inside-the-unified-log-2-why-browse-the-log/?share=twitter)
* [Click to share on Facebook (Opens in new window)
  Fa...