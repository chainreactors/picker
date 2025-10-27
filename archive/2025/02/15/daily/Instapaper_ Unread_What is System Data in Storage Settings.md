---
title: What is System Data in Storage Settings
url: https://eclecticlight.co/2025/02/11/what-is-system-data-in-storage-settings/
source: Instapaper: Unread
date: 2025-02-15
fetch_date: 2025-10-06T20:39:47.140097
---

# What is System Data in Storage Settings

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
[February 11, 2025](https://eclecticlight.co/2025/02/11/what-is-system-data-in-storage-settings/)
[Macs](https://eclecticlight.co/category/macs/), [Technology](https://eclecticlight.co/category/technology/)

# What is System Data in Storage Settings?

![](https://eclecticlight.co/wp-content/uploads/2025/02/storage1.jpg?w=996)

If you have an Apple device, you’ll be familiar with the idea behind Storage Settings in System Settings > General. What you might not be prepared for is what you’ll see there. Like its equivalent in the General section of the Settings app, the bar chart at the top often shows that much of your Mac’s storage is filled with System Data, and it neither breaks that down into anything more meaningful, nor does it offer a tool to do anything about it.

[![](https://eclecticlight.co/wp-content/uploads/2025/02/storage1.jpg)](https://eclecticlight.co/wp-content/uploads/2025/02/storage1.jpg)

Storage Settings on macOS has a [troubled history](https://eclecticlight.co/2017/03/18/how-reliable-is-about-this-macs-storage-tab/). It used to be part of About This Mac, and often took so long to complete its bar chart that folk gave up waiting. In some cases, it even crashed in the process. More often than not, the totals it gave for used and free space on the startup disk were substantially different from those reported by the Finder or Disk Utility.

In recent versions of macOS, Storage Settings has improved steadily. It does now complete its analysis in a reasonable period, and in most cases its figures aren’t too different from Disk Utility’s. But System Data remains a puzzle that confuses rather than enlightens.

[![](https://eclecticlight.co/wp-content/uploads/2025/02/storage3.jpg)](https://eclecticlight.co/wp-content/uploads/2025/02/storage3.jpg)

#### What is System Data?

From the information given by Apple, it’s most likely that this isn’t really what we’d consider to be data used or required by macOS, but the often substantial difference between how much space is used, and how much can be attributed to other categories, like Books and Music. It’s not a real category, but an etcetera, a ragbag including all sorts of files and other data.

Calculating some of the other categories seems difficult enough. For example, my Music folder contains over 100 GB of individual audio files and my Music library, but Storage Settings recognises less than 50 GB of that in its Music category. The remaining 50 GB has to be accounted for elsewhere, and that’s likely to be buried in System Data. With Photos and TV it’s the other way around, with almost all my libraries stored on an external SSD, but Storage Settings still claims I have 36 GB in TV and doesn’t even mention Photos.

So the categories it does list don’t always match with what we know is on the disk. When it adds all those together and takes that total away from the amount of disk space used, that difference is little more than a guesstimate, and unlikely to contain much data required by macOS. No wonder Storage Settings can’t suggest any way to reduce that size.

#### Dynamic storage

Unlike more traditional file systems, APFS is dynamic in its use of storage space, and macOS now uses aggressive caching policies. One of those came to light when we thought the Finder had a large memory leak, only to be told that, in the right circumstances, [it can retain](https://eclecticlight.co/2023/12/20/the-finder-doesnt-leak-memory-but-fills-it-with-cached-thumbnails/) GB of Quick Look thumbnails in memory, so that scrolling through them can be smooth. When there’s sufficient free disk space, macOS can maintain large caches without using any swap space on disk.

APFS features like snapshots can retain data we presumed had been deleted, but has to be kept until the snapshot referencing it has been deleted up to 24 hours later. That space has to be accounted for somewhere, and in many cases that too goes into the System Data category, although it has actually been created by Time Machine, which oddly doesn’t have its own category.

Although not given in the Storage bar chart, both the Finder and Disk Utility should state the amount of purgeable space in use. This could be freed when necessary, but that’s determined by macOS rather than the user. I have previously [looked at how purgeable](https://eclecticlight.co/2023/04/15/what-is-purgeable-disk-space/) some features like snapshots are, and in practice you shouldn’t rely on their automatic removal when you think your Mac needs more free space.

#### What is Storage Settings good for?

[![](https://eclecticlight.co/wp-content/uploads/2025/02/storage2.jpg)](https://eclecticlight.co/wp-content/uploads/2025/02/storage2.jpg)

Like its equivalent on iPhones and iPads, some of the tools it provides are of great value in housekeeping. Click on the ⓘ Info button for each of them to get further information and for actions you can take. Categories with the more useful tools include:

* Applications, shows apps by size, and which are Intel-only, and duplicates;
* Developer, if you have Xcode installed, can clean up build files and device support;
* Documents, lists by size and type, 32-bit apps;
* Messages, lists larger attachments and lets you delete them;
* Music Creation, helps you remove sound libraries;
* macOS, tells you how much space is used by Apple Intelligence.

Although Music might seem promising, it’s only interested in music video files you can remove.

[![](https://eclecticlight.co/wp-content/uploads/2025/02/storage4.jpg)](https://eclecticlight.co/wp-content/uploads/2025/02/storage4.jpg)

#### How to check free space

Don’t trust Storage Settings or the Finder to provide an accurate estimate of free space available on disk. Instead, open Disk Utility (with Show All Devices selected in its view) and in the list at the left in its main window, pick the volume you’re interested in, then go up to its container in the list and select that. Free space shown there is the most accurate estimate of that available to all volumes within that container, as in APFS volumes within the same container all share the same free space.

Select one of those volumes, and you’ll see free space given as a higher value, with a figure for the space that’s purgeable in brackets. That represents the maximum space that could be freed if all purgeable contents were to be deleted.

For example, free space shown here for a container is 619.72 GB, which is the space available without any purging. One volume within that container is given as having 864.5 GB available, with 244.78 GB purgeable:
864.5 = 619.72 + 244.78 GB

Figures given by the Finder are only refreshed periodically, while Disk Utility should recalculate them whenever you select a volume or container, so should always be up to date.

#### Summary

* System Data in Storage Settings isn’t just files and data for macOS, but everything not listed in another category, and even that is only approximate, a rough estimate.
* Storage Settings has useful tools for managing the contents of your startup disk.
* For an accurate estimate of free space, use Disk Utility, and the free space given there for the volume’s container.
* Don’t expect macOS to free up any purgeable space for you.

### Share this:

* [Cli...