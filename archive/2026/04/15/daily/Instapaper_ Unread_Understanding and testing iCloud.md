---
title: Understanding and testing iCloud
url: https://eclecticlight.co/2026/04/06/understanding-and-testing-icloud/
source: Instapaper: Unread
date: 2026-04-15
fetch_date: 2026-04-16T04:53:57.085441
---

# Understanding and testing iCloud

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
[April 6, 2026](https://eclecticlight.co/2026/04/06/understanding-and-testing-icloud/)
[Macs](https://eclecticlight.co/category/macs/), [Technology](https://eclecticlight.co/category/technology/)

# Understanding and testing iCloud

![](https://eclecticlight.co/wp-content/uploads/2018/03/cirrus01.png?w=535)

iCloud has changed a great deal in the nearly 15 years since its introduction, and now provides many discrete services. These include synchronisation of app databases using CloudKit, file storage and sharing using iCloud Drive, update and support services for macOS and Apple’s other OSes, and a loose group of miscellaneous services including Private Relay.

Well-known examples of those include:

* CloudKit – shared calendars, address books and notes;
* iCloud Drive – folders and files in the Finder’s iCloud Drive location;
* macOS support – XProtect updates for Sequoia and Tahoe, optional language support and additional dictionaries downloaded on demand;
* miscellaneous – iCloud+ Private Relay, Find My.

One of the most common confusions is to assume that a problem with one service cause problems with others. Although they can, that all depends on where the fault lies.

There are also two major online services provided by Apple that are separate from iCloud: its software update servers to deliver OS updates as well as security data and other system support through Software Update; Private Cloud Compute to deliver off-device AI services.

#### Network basics

All iCloud services have their own local client, such as CloudKit for syncing shared data, which in turn relies on low-level network services in macOS. Those communicate through your network’s router, and so pass out to the Internet to connect with a remote server. Although Apple does have at least one of its own data centres, much of iCloud is thought to be hosted on Amazon Web Services (AWS) and/or Google Cloud Platform.

These are important details when investigating iCloud problems. There’s no point in fiddling with local iCloud settings if the problem results from any link in this chain beyond your Mac. One of the most valuable early steps is to point your browser at Apple’s local [service status page](https://www.apple.com/support/systemstatus/) and check whether that service is reported as working normally. If that loads briskly, works as expected, and claims the iCloud service you’re having problems with should be working normally, you can turn your attention to what might be going wrong in your Mac.

One important factor to be taken into account is whether a local Content Caching server is in use. Unless iCloud content is excluded, a local server should cache changes in iCloud data, enabling other Macs and devices to sync within the local network. Enabling a Content Caching server can itself address some iCloud problems, and is well worth considering.

#### Testing

The most common fault with iCloud’s services is failure to sync local contents with those stored in iCloud. Failures are hard to investigate even in a controlled test, as there’s no way for a user to tell directly what’s going on in iCloud without relying on another Mac or device syncing (or the iCloud.com web service updating). The following tests are relatively quick and simple, and can provide helpful information about the state of iCloud services on your Mac.

#### CloudKit

The only controls provided for CloudKit are those in the iCloud section of your Apple Account settings, and any in apps that use CloudKit. For each service you use, ensure that **Sync this Mac** is enabled before going any further.

To test syncing of Notes, open the app on your test Mac and other Macs and devices. Write one note in the test app and wait for it to sync to the others. On one of the other systems, write another note, and wait for that to sync to the test Mac. Syncing isn’t immediate even if you’re using a local Caching server, but it should occur within a couple of minutes when there are good connections to iCloud.

There are times when syncing can take much longer. To ensure that CloudKit server resources are shared fairly, CloudKit imposes limits on transfers, and can throttle traffic. Throttling is likely to occur when a CloudKit app issues many requests over a short period, or uses CloudKit inappropriately, perhaps triggering simultaneous peaks in request rates from several devices at the same time. In some situations, where you suspect that one or more CloudKit-based apps are causing throttling or hitting limits, you can disable their syncing to see if that enables other apps to sync better.

The definitive way to investigate CloudKit problems is in the log, and is a fearsome task even for developers, as [detailed here](https://developer.apple.com/documentation/technotes/tn3163-understanding-the-synchronization-of-nspersistentcloudkitcontainer).

#### iCloud Drive

The most important control over iCloud Drive is in the **Drive** item of the iCloud section of Apple Account settings, where **Sync this Mac** must be enabled. You should also check syncing in the list of apps there.

The **Optimise Mac Storage** control determines how iCloud Drive works. In the past, it relied on its own features in macOS, and for many those were flawed. Evicting a file from local storage left a local stub file as a place-marker, but in 2021-23 iCloud migrated to use a new FileProvider framework common to all cloud services.

Since then, iCloud Drive has worked in either of two distinct modes:

* When **Optimise Mac Storage** is turned *off,* iCloud Drive is a *replicating FileProvider,* and maintains complete local copies of all files stored in iCloud servers. This prevents you or macOS from removing their downloaded data.
* When **Optimise Mac Storage** is turned *on,* iCloud Drive is a *non-replicating FileProvider,* and can remove the downloaded data of local files, a process known as *eviction.* Rather than leaving stub files, the same files remain but they are dataless. You and macOS can thus choose whether to evict files or download them, and you can opt to keep them downloaded, or ‘pinned’ locally.

iCloud Drive syncing is also believed to be subject to throttling to prevent servers from being overwhelmed, although that appears infrequent and lasts but a few hundred milliseconds if it does occur. Files for transfer are divided into chunks of just over 15 KB, although the system maximum may be as large as 28 MB or even 33 MB. Some iCloud servers may also impose a maximum limit on the number of connections.

The simplest way to test iCloud Drive syncing reproducibly is using the **Test Upload** feature available in the Window menu of [Cirrus](https://eclecticlight.co/cirrus-bailiff/). This transfers a 1 MB file named *co.eclecticlight.Cirrus.data,* which should appear almost instantly at the top level of the iCloud Drive folder, so is readily visible on Macs and devices connected to the same iCloud Drive account. There’s also a **Clean up Test** command to delete that test file.

Having established that your iCloud Drive does sync promptly using that test file, the more difficult problem is to discover why some files appear to be stuck. Unfortunately, the best way to identify them is from the log.

#...