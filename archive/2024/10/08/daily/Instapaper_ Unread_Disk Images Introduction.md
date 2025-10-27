---
title: Disk Images Introduction
url: https://eclecticlight.co/2024/10/07/disk-images-introduction/
source: Instapaper: Unread
date: 2024-10-08
fetch_date: 2025-10-06T18:53:53.342639
---

# Disk Images Introduction

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
[October 7, 2024](https://eclecticlight.co/2024/10/07/disk-images-introduction/)
[Macs](https://eclecticlight.co/category/macs/), [Technology](https://eclecticlight.co/category/technology/)

# **Disk Images:** Introduction

A disk image is a file or a bundle containing what could otherwise be the contents of a disk. It’s a common way to store and move complete file systems in a neat package, for items that need to be separated from the physical storage provided by a drive. macOS uses disk images for some tasks of great importance, including:

* Recovery and Hardware Diagnostics systems,
* additions to macOS such as Safari, its supporting frameworks, and dyld caches, in cryptexes,
* networked storage for Time Machine backups, in sparse bundles,
* lightweight virtual machines on Apple silicon Macs.

You could use them to store encrypted data on unencrypted volumes, and they’re often used for delivering Apple and third-party software.

Disk images are poorly documented for both users and developers, and have changed significantly over the last few years. Articles in this series explain how to choose between different types of disk image, how to create and use them, and what to do when they go wrong.

#### Containers and file systems

Disk images consist of two distinct components: the file or bundle itself functioning as a container, and the file system contained inside it. When referred to in this context, disk image containers are completely unrelated to the sandbox containers found in ~/Library/Containers.

This distinction is important in several respects, although it isn’t apparent when you use disk images in the Finder. Preparing a disk image for access involves two separate functions: *attaching* its container, and *mounting* any file systems found inside it. When that’s performed by the Finder, perhaps by double-clicking the disk image, those two actions appear fused into one. Similarly, removing the disk image requires all its mounted file systems to be unmounted first, then the container is detached.

One feature that’s widely confused is the encrypted disk image. This involves encryption of the whole container, rather than using an encrypted file system within it. Now that Disk Utility no longer supports the creation of encrypted HFS+ volumes, one remaining alternative is to use an encrypted disk image containing an HFS+ volume.

If you want an analogy for disk images, attaching the container is like connecting an external disk, and once that has been performed, the file systems contained by that disk have to be mounted before you can access their contents.

#### Types

There are many different types of disk image in use, of which the two this series is most concerned with are plain UDIF read-write disk images (UDRW), and sparse bundles (UDSB). Others you may encounter include:

* plain UDIF read-only (UDRO),
* various compressed versions of UDRW,
* CD/DVD master for export (UDTO),
* sparse disk image (UDSP), a single file rather than a bundle.

Those specify the container format; within each, there’s the usual choice of file systems, although throughout these articles it will normally be assumed that APFS will be used unless otherwise specified.

The word *sparse* in sparse bundle and sparse disk image doesn’t refer to APFS sparse files, but to the fact that those types of disk image can grow and diminish in size, and normally try to occupy the minimum amount of disk space. This is an unfortunate name collision.

#### Structure

With the exception of sparse bundles, all disk images are contained within a single file of opaque structure.

Sparse bundles consist of a single bundle folder containing:

* **bands**, a folder containing the contents of the disk image in *band files*
* **info.plist** and its backup copy **info.bckup**, containing settings including band size
* **lock**, an empty file
* **mapped**, a folder containing small data files to match all of the band files except the first
* **token**, an empty file.

#### Container size

Until this changed in Monterey (or thereabouts), non-sparse disk images had fixed container sizes. Create a UDIF read-write disk image (UDRW) of 10 GB, and the space occupied by it on disk was approximately 10 GB, whether it was empty or full. Although it remains undocumented, when stored on APFS volumes, UDRW disks can now take advantage of APFS sparse file format, and will normally only occupy the disk space required for the contents of their file system.

This is only true once the disk image has been mounted for the first time after it has been created, mounted and unmounted. To see this, create a test read-write disk image (for example, using Disk Utility) of 10 GB size. Then unmount it, and use the Finder’s Get Info command to inspect its size on disk. That will be 10 GB. Then mount the disk image again, pause a couple of seconds, unmount it, and Get Info will show its size on disk is now much smaller.

As I’ll explain in detail in a later article, this is because each time that disk image is mounted, if its internal file system is HFS+ or APFS, its contents will be trimmed, and saved to disk in sparse file format, which omits all its empty space. This only applies to read-write disk images when they’re stored in APFS file systems; copy them to HFS+ and they’ll explode to full size, as HFS+ doesn’t support the sparse file format.

Considering just the two leading types, empty sizes for a 100 GB disk image are:

* a sparse bundle is 35.4 MB empty, 53.3 GB when containing about 51 GB files, stored across 6,359 band files.
* a read-write disk image (UDRW) shrinks to 333.8 MB once stored as an empty sparse file, 53.6 GB when containing about 51 GB files, in a single file container.

#### Performance

Some types of disk image perform poorly, and can be very slow to write to. Recent versions of macOS have brought improvements, although some options such as encryption can still impair performance significantly. For the two leading types, when their container is stored on the internal SSD of an Apple silicon Mac, with native read and write speeds of around 6-7 GB/s:

* an initially empty unencrypted sparse bundle reads at 5.1 GB/s, and writes at 4.8 GB/s.
* an initially empty unencrypted read-write disk image (UDRW) reads at 5.3 GB/s, and writes at only 1 GB/s.

Tests were performed using my utility Stibium, across a range of 160 files of 2 MB to 2 GB size in randomised order, with macOS 15.0.1.

#### Key points

* Disk images consist of a file or bundle containing one or more file systems; the container and its contents are distinct.
* To access the contents of a disk image, the container is first attached, then the file system(s) within it are mounted. In the Finder, those two processes appear as a single action.
* Encrypted disk images encrypt the container, and don’t necessarily contain encrypted file systems.
* Disk images come in many different types, and can contain different file systems.
* Sparse bundles have a file and folder structure inside their bundle folder, with their data saved in band files; all other disk images are single files.
* Sparse bundles grow and shrink according to the size of files stored within them.
* In recent macOS, and on APFS, read-write disk images ...