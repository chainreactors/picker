---
title: Inside the Unified Log 1 Goals and architecture
url: https://eclecticlight.co/2025/09/23/inside-the-unified-log-1-goals-and-architecture/
source: Instapaper: Unread
date: 2025-09-25
fetch_date: 2025-10-02T20:40:30.078243
---

# Inside the Unified Log 1 Goals and architecture

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
[September 23, 2025](https://eclecticlight.co/2025/09/23/inside-the-unified-log-1-goals-and-architecture/)
[Macs](https://eclecticlight.co/category/macs/), [Technology](https://eclecticlight.co/category/technology/)

# **Inside the Unified Log 1:** Goals and architecture

The introduction of Mac OS X in 2000-01 brought conventional text-based logging to the Mac, with standard logs including system.log and console.log.

![console2005](https://eclecticlight.co/wp-content/uploads/2024/12/console2005.jpg)

With the release of macOS 10.12 Sierra in 2016, those were almost completely replaced by the **Unified Log**, which has continued evolving since. Intended to provide a single efficient logging mechanism for user and kernel modes, its design goals are:

* to maximise information collection with minimum observer effect;
* as much logging on as much of the time as possible;
* compression of log data for efficient use of space;
* a managed log message lifecycle;
* designed-in privacy protection;
* to be common across all Apple’s operating systems;
* all legacy APIs (NSLog, asl\_log\_message, syslog, etc.) to be redirected into the single log;
* to support debugging, but *not* system administration or audit.

To achieve this, log entries are written using the [OSLog API](https://developer.apple.com/documentation/os/generating-log-messages-from-your-code) (or Logger from Swift), handled by the `logd` daemon and compressed into a buffer. From there entries are either retained in memory if intended to be ephemeral, or written out to a file. Log entries are only made from the start of kernel boot; earlier phases of the boot process instead save *breadcrumbs* that are largely inaccessible and unintelligible.

![mul102LogdFlow](https://eclecticlight.co/wp-content/uploads/2018/03/mul102logdflow.png?w=940)

Performance of writing log entries [is excellent](https://eclecticlight.co/2025/05/30/can-you-trust-times-shown-in-the-log/), with a single process able to write sequential entries every 400 ns from a code loop, a rate of 2.5 million entries per second, although that rate is unlikely to be sustainable for long.

#### Log storage

There are two main groups of files that store log entries: those kept in /var/db/diagnostics/Persist/ in the form of tracev3 files containing regular log entries, and further tracev3 files in /var/db/diagnostics/Special/ containing additional shorter-life entries. Additional and lengthier log data can instead be stored in files named by UUID in /var/db/uuidtext/, and there’s also support for special Signpost entries intended for performance measurement, and scope for high-volume collection.

tracev3 files use a proprietary compressed binary format that remains undocumented to this day, but has been [largely reversed](https://github.com/mandiant/macos-UnifiedLogs). Apple’s APIs don’t give direct access to their contents, only through closed-source utilities such as the `log` command tool and programmatically through the OSLog API. Where users want a more portable format, Apple recommends conversion to a logarchive package, although that’s also undocumented and only directly accessible using `log`, the Console app and some third-party utilities. Logarchives still store all log entries in tracev3 files.

Collection and retention of entries from different subsystems is configured in logging profiles, XML property lists stored in /System/Library/Preferences/Logging (read-only, in the System volume) and /Library/Preferences/Logging, which the user controls. You can create your own custom profiles, or modify them on the fly using the `log` command.

The `logd` service maintains tracev3 files and their ancillaries, weeding them to remove time-expired entries. It does so to constrain the total size of log files in the system, rather than rolling them to retain all entries for a specified period. Most ephemeral entries are weeded within 5 minutes of being written to the log, leaving persistent entries to remain for the following days, depending on the volume of new entries being written. For example, in a 3 second period of collection, when all entries were obtained within a minute of being written, 22,783 entries were found. Five minutes after they had been written, only 82% of those remained, and over 8 hours later that had fallen to 80%, or 18,309.

#### Log content

In contrast to traditional text-based logs, entries in the macOS log contain structured data in set fields, such as the datestamp, subsystem and log message. The number of fields available from the `log` command has risen from 16 to over 25, but entries are constrained in which fields are available, according to their type. Currently there are four types, Regular, Activity, Boundary and Signpost.

Some log entries, notably those written to /var/db/uuidtext/, can have very long message fields, extending to dozens of lines. Among the most verbose is the com.apple.runningboard subsystem, which not infrequently writes the whole of its records for an app into the message field of a single log entry.

#### Privacy

Privacy protection censors content of log entries when they’re written, replacing sections of the message field with `<private>` in accordance with the formatting string for that message. This protection can be disabled, but as entries are censored when they’re written, that only affects those written after censorship has been removed, and can’t be applied retrospectively.

One significant change in macOS 26 Tahoe is that the message contents of all log entries written using the old NSLog interface are replaced with `<private>`, rendering them essentially useless. Since macOS 10.12.4, all access to log entries has required admin privileges.

#### Access

macOS provides users with two means of accessing entries in the log: the `log` command tool, and Console app. In common use, `log` generates text output, so losing the original data fields, one of the major advantages of the Unified Log. Console offers two methods of access: a live stream of entries, or browsing past entries in a saved logarchive.

I have four main tools that provide extensive log access:

* LogUI, using the OSLog API and displaying entries as formatted SwiftUI Lists;
* Mints, offering special-purpose browsers for Time Machine, APFS, and other domains;
* Ulbow, using the `log` tool and displaying entries as formatted Rich Text using AppKit;
* Consolation, using the `log` tool and displaying entries as formatted Rich Text using AppKit.

These are available from [their product page](https://eclecticlight.co/consolation-t2m2-and-log-utilities/), and [here for Mints](https://eclecticlight.co/mints-a-multifunction-utility/).

### Share this:

* [Click to share on X (Opens in new window)
  X](https://eclecticlight.co/2025/09/23/inside-the-unified-log-1-goals-and-architecture/?share=twitter)
* [Click to share on Facebook (Opens in new window)
  Facebook](https://eclecticlight.co/2025/09/23/inside-the-unified-log-1-goals-and-architecture/?share=facebook)
* [Click to share on Reddit (Opens in new window)
  Reddit](https://eclecticlight.co/2025/09/23/inside-the-unified-log-1-goals-and-architecture/?share=reddit)
* [Click to share on Pinterest (Opens in new window)
  Pinterest](https://eclecticlig...