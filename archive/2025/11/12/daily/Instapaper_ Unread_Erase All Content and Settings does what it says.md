---
title: Erase All Content and Settings does what it says
url: https://eclecticlight.co/2025/11/12/erase-all-content-and-settings-does-what-it-says/
source: Instapaper: Unread
date: 2025-11-12
fetch_date: 2025-11-13T03:16:12.375071
---

# Erase All Content and Settings does what it says

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
[November 12, 2025](https://eclecticlight.co/2025/11/12/erase-all-content-and-settings-does-what-it-says/)
[Macs](https://eclecticlight.co/category/macs/), [Technology](https://eclecticlight.co/category/technology/)

# Erase All Content and Settings does what it says

Erasing SSDs securely has been a longstanding problem that has been solved in Macs with T2 or Apple silicon chips, with the introduction of Erase All Content and Settings (EACAS) four years ago in macOS Monterey. This article explains how it works, what it does, and when you should use it.

#### Boot disk

While Intel Macs are simpler, the internal SSD of an Apple silicon Mac is divided into three APFS containers/partitions.

![BootDiskStructureMSeq](https://eclecticlight.co/wp-content/uploads/2024/10/bootdiskstructuremseq.jpg)

Intel Macs have the same Apple APFS container with the Boot Volume Group in it, but the other two containers are replaced by a single small EFI partition.

macOS manages and uses the first two containers, ISC and Recovery, and that containing the Boot Volume Group is the one we’re concerned with. That includes the System and Data volumes, the former being made into a read-only snapshot that’s mounted as the Signed System Volume and contains macOS. Everything you install as a user, including apps and your Home folder, is in the Data volume, which is encrypted automatically even if you don’t have FileVault turned on.

#### Data volume

As the Data volume is invariably encrypted, the best way to securely erase its entire contents is to destroy its encryption key. Provided that can be performed robustly, so the key can never be recovered, no one will be able to decrypt its contents. (There is an expectation that one day it might be possible to break the encryption using quantum computing, but that’s not something you should be concerned with at present.)

The encryption key used to encrypt the Data volume is itself encrypted, and forms part of the mechanism used by FileVault when that’s enabled. To ensure that those encryption keys don’t leave the Secure Enclave, they’re encrypted again, and the key that’s destroyed by EACAS is one of those. macOS also employs anti-replay techniques to ensure that previous keys can’t be reused.

#### Additional features

In addition to destroying the encryption key for the Data volume, EACAS performs other useful tasks. These include signing out of your Apple Account, including iCloud and iCloud Drive, destroying all fingerprints used for Touch ID, and turning off Location Sharing to disable Find My and Activation Lock.

Although I can’t find any official account of additional data being erased by EACAS, I believe that all LocalPolicy records stored in Apple silicon Macs are also destroyed. LocalPolicy authorises access to external bootable disks, so those who have configured an external disk to boot their Mac are likely to be required to re-authorise it before it will boot that Mac again.

What EACAS doesn’t do, though, is sign you out of third-party cloud or other services such as Adobe’s Creative Cloud, or deauthorise that Mac for Apple media such as Music. Neither will it do anything to your Mac’s SSV: that’s left intact, still running the same version of macOS.

#### How to use EACAS

Start EACAS from System Settings > General > Transfer or Reset > Erase All Content and Settings…. In older versions of macOS still using System Preferences, open them and it’s offered as a command in the app menu.

![eacas](https://eclecticlight.co/wp-content/uploads/2021/11/eacas.jpg?w=940)

If you continue, you should see one final warning before the contents of the Data volume are blown away into the great bit-bucket in the sky.

[![](https://eclecticlight.co/wp-content/uploads/2025/11/eacas1.png)](https://eclecticlight.co/wp-content/uploads/2025/11/eacas1.png)

What’s left of your Data volume, shown here in Recovery mode, is a mere 300 MB or so.

[![](https://eclecticlight.co/wp-content/uploads/2025/11/eacas2.jpg)](https://eclecticlight.co/wp-content/uploads/2025/11/eacas2.jpg)

#### When to use EACAS

If you want to wipe your Mac’s Data volume so you can reinstall its user(s), EACAS is the simplest and quickest way to do that, and doesn’t require starting up in Recovery. Its additional features ensure that, when you install its new primary user, everything should work properly and you don’t end up with ghost Macs left over from the past.

It’s the method of choice when preparing your Mac for disposal, particularly if you’re passing it on to someone else, as it ensures that no one can recover any of the data stored in your Home folder, or anywhere else on its Data volume. Performing that manually requires you to work through a list of additional procedures, almost all of which are automatic in EACAS.

The only time when you’re likely to prefer a different method is when you want to erase both the Data and System volumes, perhaps to return to an older version of macOS. Although you can do that using Disk Utility in Recovery mode, that doesn’t install the matching firmware. If you really want to return to factory-fresh conditions, the best way is to put that Mac into DFU mode, then [restore it](https://eclecticlight.co/2023/07/07/when-to-revive-or-restore-in-dfu-mode/) from the IPSW image file for that version of macOS. Although that does require a second Mac, it’s quick and comprehensive.

One other caution: never use EACAS on a macOS VM, as it’s unlikely to recover. It makes more sense just to delete the whole VM and be done with it.

#### Summary

* EACAS performs a secure erase of the Data volume, as well as some useful extras.
* It’s the method of choice for preparing your Mac for disposal.
* It’s also suitable for wiping user data before setting your Mac up afresh, using its existing macOS.
* If you want to wipe the System volume as well, to reinstall macOS, restore from an IPSW in DFU mode.

### Share this:

* [Click to share on X (Opens in new window)
  X](https://eclecticlight.co/2025/11/12/erase-all-content-and-settings-does-what-it-says/?share=twitter)
* [Click to share on Facebook (Opens in new window)
  Facebook](https://eclecticlight.co/2025/11/12/erase-all-content-and-settings-does-what-it-says/?share=facebook)
* [Click to share on Reddit (Opens in new window)
  Reddit](https://eclecticlight.co/2025/11/12/erase-all-content-and-settings-does-what-it-says/?share=reddit)
* [Click to share on Pinterest (Opens in new window)
  Pinterest](https://eclecticlight.co/2025/11/12/erase-all-content-and-settings-does-what-it-says/?share=pinterest)
* [Click to share on Threads (Opens in new window)
  Threads](https://eclecticlight.co/2025/11/12/erase-all-content-and-settings-does-what-it-says/?share=threads)
* [Click to share on Mastodon (Opens in new window)
  Mastodon](https://eclecticlight.co/2025/11/12/erase-all-content-and-settings-does-what-it-says/?share=mastodon)
* [Click to share on Bluesky (Opens in new window)
  Bluesky](https://eclecticlight.co/2025/11/12/erase-all-content-and-settings-does-what-it-says/?share=bluesky)
* Click to email a link to a friend (Opens in new window)
  Email
* [Click to print (Opens in new window)
  Print](https://eclecticlight.co/2025/11/12/erase-all-content-and-settings-does-what-it-...