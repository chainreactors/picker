---
title: Explainer Disk images
url: https://eclecticlight.co/2026/03/21/explainer-disk-images/
source: Instapaper: Unread
date: 2026-03-23
fetch_date: 2026-03-24T04:18:06.080699
---

# Explainer Disk images

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
[March 21, 2026](https://eclecticlight.co/2026/03/21/explainer-disk-images/)
[Macs](https://eclecticlight.co/category/macs/), [Technology](https://eclecticlight.co/category/technology/)

# **Explainer:** Disk images

A disk image is a file, or a folder containing files, that stores the contents of a physical storage medium. In contemporary usage most can be mounted as a disk or volume, so giving access to their contents. Originally developed to aid the manufacture of floppy disks, they go back long before the Mac, and now see wide use in all parts of macOS and its apps.

Since they were used in Classic Mac OS, they have come in a multitude of different formats and variants, many of which are listed in the Appendix. They’re an essential part of macOS installers, home to Recovery mode, and the basis for cryptexes. They’ve been used to burn and replicate optical disks, to archive disk contents, extensively in network backups, and for the distribution of software.

#### History

[![](https://eclecticlight.co/wp-content/uploads/2025/04/diskcopyprefs2001.jpg)](https://eclecticlight.co/wp-content/uploads/2025/04/diskcopyprefs2001.jpg)

As early as Mac OS 9 in 1999, variants of formats had become complex. Here, Disk Copy is configured to create a read-only compressed .img file containing the contents of a standard 1.4 MB floppy disk. In the upper window, it has completed validating the checksum on a self-mounting .smi disk image that’s part of a DiskSet. Those could also be signed using certificates issued not by Apple but by DigiSign.

Mac OS X 10.1 Puma in 2001 brought a new standard with Universal Disk Image Format (UDIF) used in DMG disk images. Support for compression options in Apple Data Compression (ADC) unified what had previously been two disk image types, and extended support for images larger than a floppy disk. This new format enabled disk images to represent entire storage devices, complete with a partition map and disk-based drivers.

Mac OS X 10.5 Leopard in 2007 introduced the sparse bundle format, with its folder of smaller band files containing data. These enable the image to grow and shrink in size, and became a popular means of storing mountable Mac file systems on servers using different file systems.

#### Use

In their most common use, Disk Utility or a third-party app such as [DropDMG](https://c-command.com/dropdmg/) creates and mounts an empty container file, then copies a hierarchy of files and folders into its virtual file system. While the disk image remains mounted, it’s presented as a removable volume, and when unmounted it’s just a regular file that can be moved, copied and backed up like any other.

Its virtual file system can be any supported by macOS, but in recent years is most likely to be APFS. As the disk image can be hosted on a completely different file system, this enables you to store APFS volumes on systems that don’t themselves support APFS. This is essential for networked storage being hosted on a different file system such as Btrfs. SMB can then be used to access the contents of that disk image over the network.

Disk Utility offers a limited range of formats and variants, including RAW images (UDIF), sparse bundles (UDSB), optical disk masters (UDTO), and the new Apple Sparse Image (ASIF). They can be encrypted, and contain file systems in APFS, HFS+, FAT or ExFAT. Two command tools extend those formats and variants, `diskutil` with its `image` verb being the equivalent of Disk Utility, and `hdiutil` providing the most extensive support.

Opening a disk image in the Finder performs two distinct operations: first the file or bundle is attached, much in the way that you might attach physical storage. Once that has occurred, the image is probed by macOS for file structures and systems, and those that can be mounted are mounted as external file systems, normally in the path /Volumes. Cryptexes are an exception to this, as APFS will graft the image’s file system into arbitrary locations in the host file system.

#### Verification

Two types of verification can be performed during an attach-and-mount procedure. The first can compare the file’s checksum against a stored value to determine if the file has become corrupted, while the second is performed during probing and mounting of file structures and systems within the image. The command tools provide options to attach an image without mounting that can be used to attempt repairs on its file systems, although those seldom seem successful.

[![](https://eclecticlight.co/wp-content/uploads/2025/04/diskimageerror2020.jpg)](https://eclecticlight.co/wp-content/uploads/2025/04/diskimageerror2020.jpg)

This ‘warning’ alert from 2020 illustrates one of the longstanding issues with disk images. Although integrity checking of disk images using checksums has been valuable, when an error is found there’s no possibility of repair or recovery as the image fails to attach, so its file system can’t be made accessible.

#### Properties

There are two other issues to consider before using disk images, their read-write performance, and use of storage space.

![xferdiskimage24](https://eclecticlight.co/wp-content/uploads/2024/10/xferdiskimage24.png)

This table summarises read and write performance of the most popular types of disk image prior to macOS Tahoe, and demonstrates how sparse bundles have consistently performed best and most consistently, and sparse images (now dropped from Disk Utility’s options) fare worst, particularly when encrypted.

[![](https://eclecticlight.co/wp-content/uploads/2025/09/tahoediskimages.png)](https://eclecticlight.co/wp-content/uploads/2025/09/tahoediskimages.png)

The introduction of ASIF in Sequoia has added another option, although sparse bundles remain fastest overall. I will be re-examining these in the coming weeks, now that new format has had more time to mature.

Before macOS Monterey, sparse bundles and sparse images were the only formats that made efficient use of disk space, as they grow to accommodate their contents, and should shrink again when some or all of their contents are removed. Monterey is thought to be the first version in which UDIF read/write images (UDRW) have been stored in APFS sparse file format. This has transformed what had previously been space-inefficient disk images that retained empty storage, into a format that can prove almost as space-efficient as sparse bundles.

#### Summary

* Disk images of various formats are widely used in macOS, as they are a file or folder containing a removable file system, like an external disk.
* Basic tools for the most common formats and variants are provided in Disk Utility; third-party utilities such as DropDMG are more versatile. The command tool `diskutil` with its `image` verb extends those, and `hdiutil` is the most comprehensive.
* Errors can and do occur, and may prevent a disk image from being mounted successfully. Those are hard to repair.
* Sparse bundles remain fastest, most consistent, and most space-efficient.
* UDIF read/write images generally perform well, and are now space-efficient too.
* Experience with more recent ASIF images remains limited, although they show promise in both speed and efficiency.

#### Appendix: Disk ima...