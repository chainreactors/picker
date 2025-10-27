---
title: How iCloud has changed in Sequoia pinning and more
url: https://eclecticlight.co/2024/09/30/how-icloud-has-changed-in-sequoia-pinning-and-more/
source: Instapaper: Unread
date: 2024-10-02
fetch_date: 2025-10-06T18:58:42.261727
---

# How iCloud has changed in Sequoia pinning and more

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
[September 30, 2024](https://eclecticlight.co/2024/09/30/how-icloud-has-changed-in-sequoia-pinning-and-more/)
[Macs](https://eclecticlight.co/category/macs/), [Technology](https://eclecticlight.co/category/technology/)

# **How iCloud has changed in Sequoia:** pinning and more

The biggest changes to iCloud and iCloud Drive came in macOS Sonoma, when the latter adopted the new FileProvider framework to manage its syncing. If you’re intending upgrading from Ventura or an earlier version of macOS to Sequoia, then you should read [this explanation](https://eclecticlight.co/2023/11/21/icloud-drive-in-sonoma-fileprovider-and-eviction/) and [this discussion](https://eclecticlight.co/2024/03/11/icloud-drive-in-sonoma-optimise-mac-storage-or-not/).

iCloud services for macOS fall into two broad categories: databases such as Contacts synced by CloudKit, and files stored in iCloud Drive, as managed in the Finder. Local copies of files stored in iCloud Drive can be kept downloaded or *materialised,* so that the whole of their data is stored locally, or their download can be removed, or *evicted,* so that their data isn’t stored on your Mac but only in iCloud, making the local file *dataless.*

FileProvider offers iCloud Drive users a choice of two schemes for syncing those files stored remotely:

* **replicated,** selected by turning **Optimise Mac Storage** off, in which FileProvider syncs between local and remote storage to ensure that their contents remain identical, and local files can’t be evicted to make them dataless;
* **nonreplicated,** when **Optimise Mac Storage** is turned on, which allows the user and macOS to remove local data from files, rendering them dataless by their eviction.

Although those options had been available long before Sonoma, their implementation had been flawed, allowing some to set iCloud Drive to operate in replicated mode, but still to evict files from local storage. Rather than using the current system of dataless files, older implementations used hidden stub files instead. Those issues were addressed by the adoption of FileProvider in Sonoma.

One curiosity here is that, according to [Apple’s documentation](https://developer.apple.com/documentation/fileprovider/), the public FileProvider API for macOS only offers replicated mode, but nonreplicated FileProvider is confined to iOS and iPadOS. In practice, iCloud Drive functions differently, in iOS and iPadOS only offering nonreplicated mode, while macOS offers the choice between either, according to the **Optimise Mac Storage** setting. I’ve been unable to find any explanation, but suspect this is the result of private APIs.

#### Pinning downloaded files

The most obvious change introduced in Sequoia is the ability to pin individual files to remain downloaded in local storage when operating in nonreplicated mode. I have [already explained](https://eclecticlight.co/2024/09/16/sequoia-introduces-pinning-to-icloud-drive/) how this is used, and how it works in detail. Further testing since then has revealed some strange behaviours you need be aware of.

![pinning1](https://eclecticlight.co/wp-content/uploads/2024/09/pinning1.png)

You can use the Finder’s contextual menu to pin multiple files and folders at once. When you pin a folder, its entire contents, including those of folders nested within it, are individually pinned, as is the folder itself. However, if you select more than 10 items in the Finder, the pinning option isn’t available in the menu. This appears to be an unintended oversight in this initial implementation, and should be rectified in a future macOS update.

If you pin an item that is currently evicted, then it will be automatically downloaded before being pinned, as you’d expect.

#### Pinning mechanism

![pinning4](https://eclecticlight.co/wp-content/uploads/2024/09/pinning4.png)

Files and folders that have been pinned are distinguished by their `com.apple.fileprovider.pinned` extended attribute. Apple doesn’t currently document any file attribute or other means for telling whether a file is pinned. Using a utility such as xattred, or the `xattr` command tool, it’s simple to demonstrate that merely pasting or cutting that extended attribute from files sets their pinning status.

Pinning is performed by FileProvider, as an FPPinOperation, and iCloudDriveFileProvider then records the change in the cloud service’s file system FSTree to reflect the file’s pinning status, which is synced up to iCloud. Unpinning follows a similar sequence in an FPUnpinOperation. Those are reflected in log entries, making pinning and unpinning easy to observe there.

#### Pinning pains

The introduction of FileProvider in Sonoma highlighted how many Macs now have so much stored in iCloud Drive that they’re unable to download all files stored there, as they have insufficient free space on their boot disk to accommodate them all. For those Macs that are unable to operate iCloud Drive in replicated mode because of insufficient local storage capacity, pinning can be dangerous unless managed carefully.

Consider a Mac with 1 TB of files in iCloud Drive, operating in nonreplicated mode with **Optimise Mac Storage** turned on, and only 100 GB of free space on its internal SSD; most of those files in iCloud Drive are likely to have been evicted. If many of those are pinned, they will be downloaded and local free space will fall until it may be insufficient to even update macOS.

Although the effect of pinning files is of course reflected in measurements of free space provided by the Finder and Disk Utility, keeping track of pinned files and the space they occupy is currently not possible. Pinning is only shown for individual files and folders in Finder views, and isn’t reflected in the Get Info dialog in any way, or anywhere else. The user thus has no idea of the total number or size of files currently pinned, nor of their location, without inspecting every folder in iCloud Drive.

It appears that the only way that a utility could provide this information is by exhaustive checking of every file in iCloud Drive for the presence of the extended attribute. I hope to address that shortly.

#### iCloud caches on external storage

FileProvider in Sequoia brings a new feature allowing a cloud service to cache files on external storage, rather than having to keep them on the Data volume in the boot volume group. This could give users the ability to reduce the space required by FileProvider on their Mac’s internal SSD. At present, this doesn’t appear to be offered as an option for iCloud Drive, but may be intended as a future enhancement.

#### Third party behaviours

I am very grateful to Bader for drawing my attention to the behaviour of some third-party apps that may explain extended syncing with iCloud for some users. This may affect WhatsApp, which offers its own option of backing up to iCloud. If that’s enabled, then each time the app connects to its backup it may download the entire backup from iCloud to reconcile its data. When that backup reaches significant size, this results in a large initial sync taking place. The only way to prevent that is to disable that backup feature. Other apps with similar behaviours may also result in large syncs occurring. This can occur ...