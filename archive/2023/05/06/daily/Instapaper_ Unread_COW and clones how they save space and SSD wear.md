---
title: COW and clones how they save space and SSD wear
url: https://eclecticlight.co/2023/05/04/cow-and-clones-how-they-save-space-and-ssd-wear/
source: Instapaper: Unread
date: 2023-05-06
fetch_date: 2025-10-04T11:42:58.771660
---

# COW and clones how they save space and SSD wear

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
[May 4, 2023](https://eclecticlight.co/2023/05/04/cow-and-clones-how-they-save-space-and-ssd-wear/)
[Macs](https://eclecticlight.co/category/macs/), [Technology](https://eclecticlight.co/category/technology/)

# ****COW** and clones:** how they save space and **SSD** wear

APFS was primarily developed for solid-state storage in Macs and Apple’s devices down to the 8 GB on the earliest series of Watch. As a modern file system it has features that cater for SSDs rather than hard disks, among them its use of copy-on-write and clone files. This article explains how they work, and their impact on different storage media and the user.

#### Copy on Write

One of the big enemies of hard disk storage is fragmentation. When the storage blocks containing a file’s data get split up and occupy different locations on the platter, reading and writing that file takes longer as the heads have to seek those locations. To minimise fragmentation and time spent seeking, hard disks try to store each file in contiguous storage, and where possible to overwrite existing blocks.

SSDs are in effect the exact opposite: there’s no seeking involved, but the erase-write cycle takes most time, and each erase eats into the expected life of the SSD. Overwriting existing storage would be painfully slow, though, as it would have to be erased first. Instead of trying to write in place, APFS therefore tries to copy on write (COW).

Take an example of a file initially occupying four contiguous blocks of storage FA-FD.

![cowclones1](https://eclecticlight.co/wp-content/uploads/2023/04/cowclones1.jpg?w=940)

When the content of block FC is changed in an edit, that block is written out to a new location, copied on writing. On a hard disk, that would be a bad move, as the file has become fragmented; when reading it from disk, the heads would have to seek from FB to AB and back to FD. On an SSD, AB will already have been erased during housekeeping, ready to be written to, so COW is quickest. It’s also a lot safer, as the old block FC won’t be erased immediately. If anything goes wrong during the write, the file system can easily fall back to its previous state. If snapshots are being made, then the data in FC won’t be erased until it’s no longer required by a snapshot. COW thus has multiple roles in APFS.

#### Clones

You’ll recall from my [previous article](https://eclecticlight.co/2023/04/28/apfs-hard-links-symlinks-aliases-and-clone-files-a-summary/) that an APFS clone pair consists of two File System Objects that share the same data to begin with. For this example, I’ll colour their shared storage blocks in purple, and their unique blocks in pink or blue depending on which file they belong to.

![cowclones2](https://eclecticlight.co/wp-content/uploads/2023/04/cowclones2.jpg?w=940)

When the clone pair is first made, they’re very efficient, as the pair only takes up the space of a single file, apart from the second File System Object, which is relatively small.

If you then open the blue clone and make changes to what has been stored in block FC, under COW those will be written out to a new block at AB.

![cowclones3](https://eclecticlight.co/wp-content/uploads/2023/04/cowclones3.jpg?w=940)

After this first edit, the pink file’s data is stored in blocks FA, FB, FC, and FD as it was originally; the blue file’s data is now stored in FA, FB, AB (changed data) and FD. As this follows COW, it minimises the amount of storage required, now a total of just 5 blocks, minimises erase cycles on the SSD, and is safest in the event of anything going wrong. It also doesn’t require any additional space to be kept in a snapshot.

Eventually, changes made to the cloned pair of files reach the point where they differ in each of their storage blocks, and are effectively completely separate files.

![cowclones4](https://eclecticlight.co/wp-content/uploads/2023/04/cowclones4.jpg?w=940)

Now the pink file’s data remains stored in FA, FB, FC and FD, but the blue file’s data is in AC, AD, AB and AE. The two files now take twice the storage space that they did when they were first cloned, and a total of four extra blocks that need to be retained in any snapshot.

This explains how the space occupied by clone files usually increases over time and editing, and how the disk space required by a snapshot also grows over time. Normally, file systems like APFS report the space actually used at that moment in time, and can’t predict its growth potential in the future. So when you are editing a clone file, even though the size of the file you’re editing may not change, the space it requires in storage is likely to increase.

In this simplified example, the end result wouldn’t be particularly bad on a hard disk. In reality, file changes are much messier and fragmentation is more severe. But in APFS the sting in the tail, that causes most performance problems, isn’t so much in the file data as the file system itself. As that changes it becomes fragmented, forcing many more seeks to access objects and their structures, until it all comes to a grinding halt, with no easy solution. No file system can be ideal for all storage media.

#### Summary

![cowclones0](https://eclecticlight.co/wp-content/uploads/2023/04/cowclones0.jpg?w=940)

### Share this:

* [Click to share on X (Opens in new window)
  X](https://eclecticlight.co/2023/05/04/cow-and-clones-how-they-save-space-and-ssd-wear/?share=twitter)
* [Click to share on Facebook (Opens in new window)
  Facebook](https://eclecticlight.co/2023/05/04/cow-and-clones-how-they-save-space-and-ssd-wear/?share=facebook)
* [Click to share on Reddit (Opens in new window)
  Reddit](https://eclecticlight.co/2023/05/04/cow-and-clones-how-they-save-space-and-ssd-wear/?share=reddit)
* [Click to share on Pinterest (Opens in new window)
  Pinterest](https://eclecticlight.co/2023/05/04/cow-and-clones-how-they-save-space-and-ssd-wear/?share=pinterest)
* [Click to share on Threads (Opens in new window)
  Threads](https://eclecticlight.co/2023/05/04/cow-and-clones-how-they-save-space-and-ssd-wear/?share=threads)
* [Click to share on Mastodon (Opens in new window)
  Mastodon](https://eclecticlight.co/2023/05/04/cow-and-clones-how-they-save-space-and-ssd-wear/?share=mastodon)
* [Click to share on Bluesky (Opens in new window)
  Bluesky](https://eclecticlight.co/2023/05/04/cow-and-clones-how-they-save-space-and-ssd-wear/?share=bluesky)
* Click to email a link to a friend (Opens in new window)
  Email
* [Click to print (Opens in new window)
  Print](https://eclecticlight.co/2023/05/04/cow-and-clones-how-they-save-space-and-ssd-wear/#print?share=print)

Like Loading...

### *Related*

Posted in [Macs](https://eclecticlight.co/category/macs/), [Technology](https://eclecticlight.co/category/technology/) and tagged [APFS](https://eclecticlight.co/tag/apfs/), [clone](https://eclecticlight.co/tag/clone/), [copy on write](https://eclecticlight.co/tag/copy-on-write/), [COW](https://eclecticlight.co/tag/cow/), [HFS+](https://eclecticlight.co/tag/hfs/), [snapshot](https://eclecticlight.co/tag/snapshot/), [SSD](https://eclecticlight.co/tag/ssd/), [storage](https://eclecticlight.co/tag/storage/). Bookmark the [permalink](https://eclecticlight.co/2023/05/04/cow-and-clones-how-they-save-space-...