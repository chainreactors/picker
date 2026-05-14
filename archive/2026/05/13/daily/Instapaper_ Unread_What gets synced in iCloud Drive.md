---
title: What gets synced in iCloud Drive
url: https://eclecticlight.co/2026/05/12/what-gets-synced-in-icloud-drive/
source: Instapaper: Unread
date: 2026-05-13
fetch_date: 2026-05-14T05:47:18.882195
---

# What gets synced in iCloud Drive

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
[May 12, 2026](https://eclecticlight.co/2026/05/12/what-gets-synced-in-icloud-drive/)
[Macs](https://eclecticlight.co/category/macs/), [Technology](https://eclecticlight.co/category/technology/)

# What gets synced in iCloud Drive?

Following [yesterday’s surprise](https://eclecticlight.co/2026/05/11/does-icloud-drive-now-lose-almost-all-metadata/) about syncing of extended attributes via iCloud Drive, this article summarises what does and does not get synced in iCloud Drive in macOS Tahoe.

#### Attributes and data

File attributes are generally synced correctly and retained locally through eviction and download of each file. As those are saved in the inode data that is stored locally even when a file is dataless, they should remain reliable.

File data, complete with any embedded metadata such as EXIF fields and the optional Info section in RTF files, is retained and kept in sync with the copy in iCloud Drive while that file is kept downloaded. That is the only option when **Optimise Mac Storage** is turned off, and iCloud Drive is operating in replicated mode. When in nonreplicated mode, data is removed if the file is evicted from local storage, and synced down from iCloud Drive when it’s downloaded or materialised.

#### Extended attributes

As demonstrated in [yesterday’s article](https://eclecticlight.co/2026/05/11/does-icloud-drive-now-lose-almost-all-metadata/), only the following xattrs are expected to sync down from iCloud Drive:

* com.apple.metadata:\_kMDItemUserTags (Finder Tag)
* com.apple.lastuseddate#PS
* com.apple.quarantine
* com.apple.TextEncoding
* other xattrs explicitly assigned the S flag, with #S appended to their name.

Other xattrs including those with names starting with com.apple.metadata:kMDItem aren’t likely to sync down from iCloud Drive without explicit use of the S flag.

#### Versions

Document versions saved in that volume’s version database in the hidden .DocumentRevisions-V100 folder will normally only be saved locally, when the local copy of that file is saved, and aren’t synced up to iCloud Drive at all. This has complicated effects best illustrated in the example below.

[![](https://eclecticlight.co/wp-content/uploads/2026/05/versioninicloud1.png)](https://eclecticlight.co/wp-content/uploads/2026/05/versioninicloud1.png)

In this example, two Macs, A and B, are connected to the same iCloud Drive. At the start, Mac A creates and saves a new file, locally Version 1, in an iCloud Drive folder. This is synced up to iCloud Drive, from where it syncs down to Mac B, as the first version of that file.

Mac A then edits that file, saving it in two further versions. Each of those is synced up to iCloud Drive, and synced down to Mac B. However, as none of those versions is saved locally on Mac B, each is shown as the current and only version until the next one arrives.

Mac A is shut down after it has saved its version 3 of the file, and that has been synced up to iCloud Drive. Once that has synced down to Mac B, the document is edited there, and two versions are added to the first. Mac B’s Version 3 of that file is synced up to iCloud Drive, Mac B is shut down, and the file is opened and saved on Mac A, where that becomes its local Version 4.

At that stage, Mac A’s version database contains 4 versions, but no copy of Mac B’s Version 2. Mac B has 3 saved versions, including its Version 2 that isn’t saved in Mac A. iCloud Drive only has a single version, its Version 5, the same as Mac A’s Version 4 and Mac B’s Version 3.

The rules are simple:

* Each Mac only adds a version to its own local version database when that file is saved locally.
* At any moment, only the latest version is stored in iCloud Drive.

However, the behaviour can appear baffling, particularly when a document is observed in its QuickLook thumbnail as it’s being edited and saved on another Mac. You can then see its contents evolving with each save, but none of those are added to that Mac’s version database unless that version is saved there.

The end result is an incomplete version history on each Mac. The only way to unify those is in a third-party utility such as [Versatility or Revisionist](https://eclecticlight.co/revisionist-deeptools/) to consolidate them. As this doesn’t require any intervention by the File Provider framework, this is likely to be similar in third-party cloud services using that framework, such as Dropbox and Microsoft OneDrive.

#### Spotlight index content

No indexes from Spotlight are synced across iCloud Drive, but once a file has been synced down from iCloud Drive, its contents should be indexed locally, on the Data volume. Those indexed contents should remain accessible to search even when the file has been evicted from local storage.

#### QuickLook previews

QuickLook thumbnails and previews are also generated and stored locally. Those that have been cached to local storage remain accessible even when the file has been evicted. When there’s no cached version available, a generic icon for that file type will be displayed until an evicted file has been downloaded again. At one time, selecting an evicted file and calling for its thumbnail or preview was a simple way to force the file to be downloaded, but that has now been fixed.

### Share this:

* [Share on X (Opens in new window)
  X](https://eclecticlight.co/2026/05/12/what-gets-synced-in-icloud-drive/?share=twitter)
* [Share on Facebook (Opens in new window)
  Facebook](https://eclecticlight.co/2026/05/12/what-gets-synced-in-icloud-drive/?share=facebook)
* [Share on Reddit (Opens in new window)
  Reddit](https://eclecticlight.co/2026/05/12/what-gets-synced-in-icloud-drive/?share=reddit)
* [Share on Pinterest (Opens in new window)
  Pinterest](https://eclecticlight.co/2026/05/12/what-gets-synced-in-icloud-drive/?share=pinterest)
* [Share on Threads (Opens in new window)
  Threads](https://eclecticlight.co/2026/05/12/what-gets-synced-in-icloud-drive/?share=threads)
* [Share on Mastodon (Opens in new window)
  Mastodon](https://eclecticlight.co/2026/05/12/what-gets-synced-in-icloud-drive/?share=mastodon)
* [Share on Bluesky (Opens in new window)
  Bluesky](https://eclecticlight.co/2026/05/12/what-gets-synced-in-icloud-drive/?share=bluesky)
* Email a link to a friend (Opens in new window)
  Email
* [Print (Opens in new window)
  Print](https://eclecticlight.co/2026/05/12/what-gets-synced-in-icloud-drive/#print?share=print)

Like Loading...

### *Related*

Posted in [Macs](https://eclecticlight.co/category/macs/), [Technology](https://eclecticlight.co/category/technology/) and tagged [FileProvider](https://eclecticlight.co/tag/fileprovider/), [iCloud Drive](https://eclecticlight.co/tag/icloud-drive/), [QuickLook](https://eclecticlight.co/tag/quicklook/), [Revisionist](https://eclecticlight.co/tag/revisionist/), [search](https://eclecticlight.co/tag/search/), [Spotlight](https://eclecticlight.co/tag/spotlight/), [Versatility](https://eclecticlight.co/tag/versatility/), [version](https://eclecticlight.co/tag/version/), [xattr](https://eclecticlight.co/tag/xattr/). Bookmark the [permalink](https://eclecticlight.co/2026/05/12/what-gets-synced-in-icloud-drive/).

## 2Comments

[Add yours](#reply-title)

1. 1
   ![Chuck's avatar](http...