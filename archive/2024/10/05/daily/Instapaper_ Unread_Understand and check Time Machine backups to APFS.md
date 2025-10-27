---
title: Understand and check Time Machine backups to APFS
url: https://eclecticlight.co/2024/10/03/understand-and-check-time-machine-backups-to-apfs/
source: Instapaper: Unread
date: 2024-10-05
fetch_date: 2025-10-06T18:55:48.728548
---

# Understand and check Time Machine backups to APFS

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
[October 3, 2024](https://eclecticlight.co/2024/10/03/understand-and-check-time-machine-backups-to-apfs/)
[Macs](https://eclecticlight.co/category/macs/), [Technology](https://eclecticlight.co/category/technology/)

# Understand and check Time Machine backups to **APFS**

Over the last 17 years, Time Machine has backed up many millions of Macs, ranging from the last Power Macs to the latest M3 models, every hour. It has changed greatly over that time. This article uses my free utility [T2M2](https://eclecticlight.co/consolation-t2m2-and-log-utilities/) to explain how Time Machine now makes automatic backups to APFS storage, and how to check that. This account is based primarily on what happens in macOS Sonoma and Sequoia, when they’re backing up automatically every hour to local storage.

T2M2 offers three features to see what’s happening with Time Machine and backups:

* **Check Time Machine** button, to analyse backups made over the last few hours.
* **Speed** button, to view progress reports in the log during a long backup.
* **Browse log** button, to show filtered log extracts in fullest detail.

These are each detailed in T2M2’s Help book. Here I’ll concentrate on the first and last, and defer speed checks to that documentation.

#### *Browse log* for detail

In practice, you’re most likely to view T2M2’s analysis using the **Check Time Machine** button first, but here I’ll walk through the greater detail available in log extracts, to build understanding of the sequence of events in each automatic backup.

![t2m2rept1](https://eclecticlight.co/wp-content/uploads/2024/10/t2m2rept1.jpg)

To help you see which subsystems are involved in each stage, T2M2 displays their entries in different colours, and you can show or hide each of those.

Automatic backups are called off by the DAS-CTS dispatching mechanism, whose entries are shown in red (DAS) and blue (CTS). They schedule backups so they don’t occur when the Mac is heavily loaded with other tasks, and call a chain of services to start the backup itself. Dispatching is now reliable over long time periods, but can be delayed or become irregular in some situations. Inspecting those DAS-CTS entries usually reveals the cause.

From there on, most informative log entries are made by Time Machine itself.

Preparations are to:

* Find each destination backup storage, decide whether any rotation scheme applies, so determine the destination for this backup.
* Check write performance to the backup destination.
* Find the machine store on the destination.
* Determine which local snapshots should be removed, and delete them.
* Create local snapshot(s) as ‘stable’ snapshot(s), and mount them.
* Mount previous local snapshot(s) as ‘reference’ snapshot(s).
* Determine how to compute what needs to be backed up from each source. This should normally use FSEvents to build the EventDatabase.
* Scan the volumes to be backed up to determine what needs to be backed up.
* Estimate the total size of the new backup to be created.

Once backing up starts, entries cover:

* Copying designated items to the destination.
* Posting periodic progress reports during longer backups.

When that’s complete, closing stages are to:

* Report details of the backup just completed.
* Set local snapshots ready for the next backup, with the ‘stable’ snapshot(s) marked as ‘reference’, and unmount local snapshots.
* Delete working folder used during the previous backup as ‘incomplete’.
* Create the destination backup snapshot.
* Delete any old backups due for removal.
* Report backup success or other outcome.

They’re summarised in this diagram. Although derived from Sonoma, Sequoia brings no substantial change.

![tmbackup14a](https://eclecticlight.co/wp-content/uploads/2023/10/tmbackup14a.png?w=940)

Or its PDF tear-out version: [tmbackup14b](https://eclecticlight.co/wp-content/uploads/2023/10/tmbackup14b.pdf "tmbackup14b")

#### *Check Time Machine* summaries

![t2m2rept2](https://eclecticlight.co/wp-content/uploads/2024/10/t2m2rept2.jpg)

T2M2 analyses all those log entries to produce a summary of how Time Machine has performed over the last few hours. That is broken down into sections as follows.

**Backup destination**. This is given with the free space currently available on that volume, followed by the results of write speed measurements made before each backup starts.
`Backing up 1 volumes to ThunderBay2 (/dev/disk10s1,TMBackupOptions(rawValue: 257)): /Volumes/ThunderBay2
Current free space on backup volumes:
✅ /Volumes/ThunderBay2 = 1.67 TB
Destination IO performance measured:
Wrote 1 50 MB file at 286.74 MB/s to "/Volumes/ThunderBay2" in 0.174 seconds
Concurrently wrote 500 4 KB files at 23.17 MB/s to "/Volumes/ThunderBay2" in 0.088 seconds`

**Backup summary**. This should be self-evident.
`Started 4 auto backup cycles, and 0 manual backups;
completed 4 volume backups successfully,
last backup completed successfully 53.4 minutes ago,
Times taken for each auto backup were 0.3, 0.3, 0.2, 0.2 minutes,
intervals between the start of each auto backup were 61.4, 60.2, 60.3 minutes.`

**Backups created and deleted** (or ‘thinned’).
`Created 4 new backups
Thinned:
Thinning 1 backups using age-based thinning, expected free space: 1.67 TB actual free space: 1.67 TB trigger 50 GB thin 83.33 GB dates: (
"2024-10-01-043437")`

**Local snapshots created and deleted**.
`Created 4 new snapshots, and deleted 4 old snapshots.`

**How the items to be backed up were determined**. This shows which methods Time Machine used to work out which items needed to backed up, and should normally be FSEvents, once a first full backup has been made.
`Of 4 volume backups:
0 were full first backups,
0 were deep scans,
4 used FSEvents,
0 used snapshot diffs,
0 used consistency scans,
0 used cached events.`

**Backup results**. For each completed backup, Time Machine’s report on how many items were added, and their size.
 `Finished copying from volume "External1"
1 Total Items Added (l: Zero KB p: Zero KB)
3 Total Items Propagated (shallow) (l: Zero KB p: Zero KB)
403274 Total Items Propagated (recursive) (l: 224.93 GB p: 219.31 GB)
403275 Total Items in Backup (l: 224.93 GB p: 219.31 GB)
1 Directories Copied (l: Zero KB p: Zero KB)
2 Files Move Skipped (l: Zero KB p: Zero KB) | 2 items propagated (l: 6 KB p: 12 KB)
1 Directories Move Skipped (l: Zero KB p: Zero KB) | 403269 items propagated (l: 224.93 GB p: 219.31 GB)`

**Error messages**.
`✅ No error messages found.`

#### iCloud Drive and pinning

Backing up the contents of iCloud Drive is a longstanding problem for Time Machine, if **Optimise Mac Storage** is enabled. Those files in iCloud Drive that are stored locally should be backed up, but any that have been evicted from local storage could only be included if they were to be downloaded prior to the backup starting.

In Sonoma and earlier, the only way to ensure that an evicted file in iCloud Drive is included in a Time Machine backup is to manually download it. Sequoia now lets you ‘pin’ individual files and whole folders so that they aren’t evicted, so will always be included in Time Machine backups. This is [explained here](https://eclecticlight.co/2024/09/30/how-icloud-has-changed-in-sequoia-pinning-and-more/).

#### Discrepancies ...