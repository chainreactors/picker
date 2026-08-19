---
title: SQLite Database Analysis Tips and Tricks with DB Browser
url: https://iverify.io/blog/sqlite-database-analysis-db-browser
source: Instapaper: Unread
date: 2026-08-18
fetch_date: 2026-08-19T03:00:33.074857
---

# SQLite Database Analysis Tips and Tricks with DB Browser

[Blog](../blog)

# SQLite Database Analysis Tips and Tricks with DB Browser

![Headshot of Sarah Edwards, Head of Digital Forensics and Incident Response at iVerify](https://framerusercontent.com/images/VzvVp9sO0BGHJcAQFyzAP87TYLc.png?width=1200&height=1200)

Sarah

Edwards

Â·

Published Jul 17, 2026

![Cover: a database cylinder under a magnifying glass beside a data table, for SQLite analysis with DB Browser](https://framerusercontent.com/images/UI74RICZ9EMJRwFnYQkZ8h3nq0I.png?width=1024&height=576)

As a forensic analyst, I can often spend the majority of my day diving into SQLite databases looking for various forensic artifacts from mobile spyware cases. It could be looking for anomalies of data that has been cleaned up, researching potential IOCs, or device usage to determine how a device got compromised. I often joke that my favorite forensic tools are a terminal window and a database browser, and in reality - it's mostly true (give or take a few vibe-coded custom tools - donât judge me.)

One of the databases I spend an inordinate amount of time in is iOS Powerlog databases. This is because it is available in an iOS sysdiagnose dump - something we work with every day here at [iVerify](../). The Powerlogs database is a particularly large database with upwards of 700+ tables (this can vary depending on OS version, hardware, etc.) but it is also one of the most powerful datasets in that sysdiagnose dump. For more information on this database, see my presentations here at [Objective by the Sea](https://www.youtube.com/watch?v=dLEZgIwjcPY) or [Out of the Box](https://www.youtube.com/watch?v=ASVtaoBQ45w).

Folks who are new to SQLite databases, just the number of tables this database has can be very intimidating - let alone performing analysis on its contents. In this blog, Iâd like to offer up some of my favorite tips and tricks to analyze SQLite databases using one of my favorite tools, [DB Browser for SQLite](https://sqlitebrowser.org/). Iâve chosen DB Browser because it is open source and is available across many platforms. This post will be slightly macOS focused (Iâm unapologetically an Apple fan girl), so while hotkeys may be slightly different, DB Browser will generally work the same across platforms.

I wanted to get this blog out for our upcoming [iOS Threat Hunting and Malware Analysis](https://blackhat.com/us-26/training/schedule/index.html#ios-threat-hunting-and-malware-analysis-51038) training at Black Hat in a couple weeks. Our students are sometimes introduced to SQLite databases and they donât really know how to go about analyzing them, so perhaps these tips and tricks will make that easier!

## **Fonts and Cell Colorization**

One of the first things I change when I install DB Browser on a new system is the look and feel of DB Browser. On first launch, youâll see a bunch of windows already opened on the right-hand side. You can close all of these. Youâll want as much screen real estate as possible for analysis. You can always open them later using the **View** menu.

Next I open up the **Preferences**. Fonts can make a huge difference in how easy data can be read. While this is certainly a personal preference, I prefer a clean monospace font like Menlo versus the default American Typewriter. If you want to change the font to some of the classics like Papyrus or Comic Sans, you do you - there are many options available and I wonât judge. I also adjust the font size, something that seems to increase with every birthday. Note that font size and fonts are distributed across a few settings tabs so make sure to adjust all of them as needed.

The cell colorization may be one of my favorite settings to change. When Iâm digging into large databases with hundreds of tables each with hundreds of columns, I need to quickly triage the data in each table. In my **Preferences** example below, I keep NULL entries as white, Binary BLOBs in hot pink, formatted cells in a bright blue, and Regular data in purple. You will see many examples of this colorization in my other tips.

![](https://framerusercontent.com/images/GUyjuAdlM3Yl34SYcA2JMQKDKZk.png)

## **Browsing Tables**

When Iâm reviewing an unknown database for the first time, I often peruse each table to get a sense of what type of data I can expect to find. This often helps determine which tables to create SQL queries on later on for my research needs.

Tables in DB Browser are best reviewed in the **Browse Data** tab. To review each table, you would need to select the table of interest in the drop down menu. This is fine for smaller databases, but with Powerlogs - you would likely get a hand cramp trying to do this for 700+ tables!

![](https://framerusercontent.com/images/S5m9lvLEGKqGJlYPTTmQhJdUz4.gif)

Instead, I like to use the **fn+command+Up or Down Arrow Keys** keyboard shortcut on macOS to quickly review each table. [Other platform keyboard shortcuts can be found here](https://github.com/sqlitebrowser/sqlitebrowser/wiki/Keyboard-shortcuts). With this shortcut, you can quickly (relatively speaking) iterate through hundreds of tables to see what is available.

![](https://framerusercontent.com/images/NduN1GddcmUttHQkwsOPHm7u0Q.gif)

## **Timestamp Conversion**

Many databases will use some sort of timestamp to organize its data. In forensics timestamps are extremely important to us to create timelines of events. While SQLite has capabilities for a variety of [timestamp formats](https://sqlite.org/lang_datefunc.html), we can usually expect to find an even mix of Mac Epoch (aka NSDate, Cocoa, CFAbsolute) or Unix Epoch timestamps in databases on iOS devices.

These can be easily converted in a SQL query, however sometimes Iâm lazy and I just want to see human readable timestamps while triaging my table. We can use the internal conversion utilities to make these epoch values a bit more useful.

Selecting the column using a context-click, select **Choose display format** and select one of the following options for the appropriate timestamp. You may also notice the cell background color changes to show its been converted. This is a good example of one of my tips above.

* Mac Epoch (seconds starting on January 1, 2001 00:00:00 UTC)

  + **Apple NSDate to date** (UTC)
* Unix Epoch (seconds starting on January 1, 1970 00:00:00 UTC)

  + **Unix epoch to date**  (UTC)
  + **Unix epoch to local time**  (local system time zone)

    - While Iâm a UTC or GTFO kind of gal, I find this one to be very useful for testing on your own data without having to do time zone math.

*Worth an honorary mention: The Powerlog database uses Unix epoch timestamp, however it also uses a time offset so some folks may see a wildly different number depending on that offset so this conversion method may not work.* [*You can find more information about this offset in my Power of Powerlogs presentation*](https://www.youtube.com/watch?v=dLEZgIwjcPY)*. It can be obnoxious if you are not prepared for it, Iâve only ever seen this time offset in Powerlogs, other databases should be ok.*

![](https://framerusercontent.com/images/nhsfwK7Ftnxzk2LPGNpgsLiRI.gif)

## **Open Multiple DB Browser Instances**

At any given moment I likely have a dock that looks like the example below. Iâm often pivoting between various databases across different devices. If you happen to double-click open a database expecting it to open in an additional window, youâll find it does not open in a new DB Browser window and instead replaces the database within that window.

![](https://framerusercontent.com/images/kNyuXvpdSQ3NrWGiyIZqwZvcs.png)

On macOS, I use the "open" command to facilitate opening multiple instances, or more directly open up databases that have a non-conventional file extensions (like Powerlogs with its \*.PLSQL extension.)

```
open -n -a "DB Browser for SQLite" powerlog_2026-06-25_13-37_C4AB843F.PLSQL
```

```
open -n -a "DB Browser for SQLite" powerlog_2026-06-25_13-37_C4AB843F.PLSQL
```

```
open -n...