---
title: Explainer sysdiagnose and logarchives
url: https://eclecticlight.co/2026/06/27/explainer-sysdiagnose-and-logarchives/
source: Instapaper: Unread
date: 2026-06-27
fetch_date: 2026-06-28T06:14:20.131150
---

# Explainer sysdiagnose and logarchives

[Skip to content](#content)

[![](https://eclecticlight.co/wp-content/uploads/2015/01/eclecticlightlogo-e1421784280911.png?w=103)](https://eclecticlight.co/)

# [The Eclectic Light Company](https://eclecticlight.co/)

Macs & painting – 🦉 No AI content

##### Main navigation

Menu

* [Downloads](https://eclecticlight.co/downloads/)
* [Freeware](https://eclecticlight.co/free-software-menu/)
* [All Macs](https://eclecticlight.co/mac-problem-solving-2-2/)
* [M1-M5 Macs](https://eclecticlight.co/m1-macs-2/)
* [Troubleshooting](https://eclecticlight.co/mac-troubleshooting-summary/)
* [Painting](https://eclecticlight.co/painting-topics-2-2/)
* [Mac Front Page](https://eclecticlight.co/category/macs/)

[hoakley](https://eclecticlight.co/author/hoakley/)
[June 27, 2026](https://eclecticlight.co/2026/06/27/explainer-sysdiagnose-and-logarchives/)
[Macs](https://eclecticlight.co/category/macs/), [Technology](https://eclecticlight.co/category/technology/)

# **Explainer:** sysdiagnose and logarchives

If you’ve ever reported a bug or problem to Apple, either as a developer using Feedback, or through Apple Support, there’s a rite of passage you may be familiar with, the dreaded `sysdiagnose`. System Diagnostics, as it’s more properly named, gathers together almost every piece of even vaguely diagnostic information about your Mac and what it has been doing for the last hour or more, in a large GZipped archive for Apple’s engineers to rake through looking for clues.

When you have a few minutes to spare, make one for yourself, unarchive it, and browse its contents. You’ll be surprised at some of the information it contains, particularly on Apple silicon Macs with AI in active use. Apple does warn those asked to submit `sysdiagnoses` that they do contain personal information, but if you’re a developer and submit a Feedback without one, you will be asked to provide it, even when it’s obviously not relevant to your report.

#### Create a `sysdiagnose`

There are three ways to create a `sysdiagnose` for a Mac:

* Using both hands, press Command-Option-Control-Shift-. [period or stop] at the same time.
* In Activity Monitor’s toolbar, open the … [ellipsis] menu and select the **System Diagnostics** command.
* In Terminal, type the command `sudo sysdiagnose`, although I prefer using `sudo sysdiagnose -f ~/Documents` to save the archive in my Documents folder. You will be shown a stern warning and have to press Enter to confirm you really do want to create the archive.

Several minutes later, you should be shown where the `sysdiagnose` archive has been saved, normally in /var/tmp/ unless you use the `-f` option at the command line.

You can also run `sysdiagnose` on Apple devices, for example using [these instructions](https://support.addigy.com/hc/en-us/articles/15849050849427-Gathering-a-Sysdiagnose-from-an-iPadOS-or-iOS-device) by Addigy for iOS or iPadOS. For most of us, this is the only practical way to obtain log records from a device.

When you have unarchived your `sysdiagnose`, look inside its contents for system\_logs.logarchive, as that is a complete copy of your Mac’s log records for the last hour or more.

#### Logarchives

Logarchives are bundles containing the contents of the two folders /var/db/diagnostics and /var/db/uuidtext, where macOS stores the contents of its Unified log. You can also make them directly using the `log collect` command such as
`log collect --output ~/Documents/my.logarchive --last 5m`
to create a logarchive in that bundle for the last 5 minutes of log records. One quirk of this command is that it refuses to write logarchives to external storage (unless it’s the boot disk), even when Terminal has been given Full Disk Access. It’s simple to cheat your way around that, though, by saving the logarchive somewhere on your Data volume, then copying it from there.

Recent versions of my free log browser [LogUI](https://eclecticlight.co/consolation-t2m2-and-log-utilities/) can also cobble together a logarchive bundle from copies of those two folders, as [described here](https://eclecticlight.co/2025/06/11/logui-build-65-introduces-a-logarchive-tool/). This also enables you to [create logarchives from full backups](https://eclecticlight.co/2026/02/25/investigate-a-past-event-in-the-log/) years after they were stored. Time Machine and most good backup utilities back up the two folders you can use to build a logarchive using LogUI, unless they are explicitly excluded from backups.

Although the bundled macOS log browser Console can’t look back at previous entries in the live log, it can open and display entries in a logarchive. My own LogUI and Ulbow can do both, but don’t display a live log stream as Console can.

Because of the [attrition that takes place](https://eclecticlight.co/2025/09/29/inside-the-unified-log-3-log-storage-and-attrition/) in log entries, a logarchive isn’t as comprehensive an account of log activity as directly accessing the live log immediately after an event. In the first five minutes after something has been recorded in the log, nearly 20% of entries are lost. Catching entries in an extract just a few seconds after it happened can retain important details that could be lost in a later logarchive or `sysdiagnose`.

However, a logarchive is a permanent record that you can return to years afterwards. I still have some saved from macOS Sierra, soon after the Unified log was introduced, and they remain accessible from current log browsers, including my own. The general rule is that you should always be able to access an older logarchive than the version of macOS you’re using, but forward compatibility isn’t guaranteed.

This will be particularly important in the future, as trying to access logarchives made by macOS 27 is only going to be possible from macOS 26.2 or later, according to Apple’s release notes. That also applies to logarchives saved in `sysdiagnoses` written by Apple devices. If you perform forensic or other analyses requiring access to logarchives written by iOS or iPadOS 27, you will therefore need a Mac running at least macOS 26.2.

### Share this:

* [Share on X (Opens in new window)
  X](https://eclecticlight.co/2026/06/27/explainer-sysdiagnose-and-logarchives/?share=twitter)
* [Share on Facebook (Opens in new window)
  Facebook](https://eclecticlight.co/2026/06/27/explainer-sysdiagnose-and-logarchives/?share=facebook)
* [Share on Reddit (Opens in new window)
  Reddit](https://eclecticlight.co/2026/06/27/explainer-sysdiagnose-and-logarchives/?share=reddit)
* [Share on Pinterest (Opens in new window)
  Pinterest](https://eclecticlight.co/2026/06/27/explainer-sysdiagnose-and-logarchives/?share=pinterest)
* [Share on Threads (Opens in new window)
  Threads](https://eclecticlight.co/2026/06/27/explainer-sysdiagnose-and-logarchives/?share=threads)
* [Share on Mastodon (Opens in new window)
  Mastodon](https://eclecticlight.co/2026/06/27/explainer-sysdiagnose-and-logarchives/?share=mastodon)
* [Share on Bluesky (Opens in new window)
  Bluesky](https://eclecticlight.co/2026/06/27/explainer-sysdiagnose-and-logarchives/?share=bluesky)
* Email a link to a friend (Opens in new window)
  Email
* [Print (Opens in new window)
  Print](https://eclecticlight.co/2026/06/27/explainer-sysdiagnose-and-logarchives/#print?share=print)

Like Loading...

### *Related*

Posted in [Macs](https://eclecticlight.co/category/macs/), [Technology](https://eclecticlight.co/category/technology/) and tagged [Apple](https://eclecticlight.co/tag/apple/), [Feedback](https://eclecticlight.co/tag/feedback/), [Golden Gate](https://eclecticlight.co/tag/golden-gate/), [log](https://eclecticlight.co/tag/log/), [logarchive](https://eclecticlight.co/tag/logarchive/), [LogUI](https://eclecticlight.co/tag/logui/), [macOS 27](https://eclecticlight.co/tag/macos-27/), [sysdiagnose](https://eclecticlight.co/tag/sysdiagnose/). Bookmark the [permalink](https://eclecticlight.co/2026/06/27/explainer-sysdiagnose-and-logarchives/).

## iThere are no comments

[A...