---
title: Daily Blog #805: Mount That Thing!
url: https://www.hecfblog.com/2025/04/daily-blog-805-mount-that-thing.html
source: Hacking Exposed Computer Forensics Blog
date: 2025-04-13
fetch_date: 2025-10-06T22:05:35.913875
---

# Daily Blog #805: Mount That Thing!

[![Hacking Exposed Computer Forensics Blog](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhV1r9Fx_K3sKHfI8wnPUPPQFkxWhuxayNz8tT11sG8lYQgY1gGiwV9Qdlfeq-b80FMkRdsOwimMVCo2VbnE0aXyGxaTX1YYhUB5IZ4yK1LhASjfZxFmkAstIM9DnylPabPqQ15WEAFysbZ/s384/unnamed.png)](https://www.hecfblog.com/)

* [Extended Mapi](https://www.hecfblog.com/search/label/extended%20mapi)
* [ObjectID](https://www.hecfblog.com/search/label/objectid)
* [Amcache](https://www.hecfblog.com/search/label/amcache)
* [CTF](https://www.hecfblog.com/search/label/ctf)
* [Python](https://www.hecfblog.com/search/label/python)
* [Syscache](https://www.hecfblog.com/search/label/syscache)
* [Daily Blogs](https://www.hecfblog.com/search/label/Daily%20Blog?max-results=6)
  + [Saturday Reading](https://www.hecfblog.com/search/label/Saturday%20reading)
  + [Solution Saturday](https://www.hecfblog.com/search/label/solution%20saturday)
  + [Forensic Lunch](https://www.hecfblog.com/search/label/forensic%20lunch?&max-results=8)
  + [Sunday Funday](https://www.hecfblog.com/search/label/sunday%20funday?&max-results=8)

[Home](https://www.hecfblog.com/)

[mtt](https://www.hecfblog.com/search/label/mtt)

Daily Blog #805: Mount That Thing!

# Daily Blog #805: Mount That Thing!

By
[David Cowen](https://www.blogger.com/profile/17629115910611763170 "author profile")
•
April 11, 2025
•

[Daily Blog](https://www.hecfblog.com/search/label/Daily%20Blog?&max-results=8)
[hal pomeranz](https://www.hecfblog.com/search/label/hal%20pomeranz?&max-results=8)
[linux forensics](https://www.hecfblog.com/search/label/linux%20forensics?&max-results=8)
[mtt](https://www.hecfblog.com/search/label/mtt?&max-results=8)
•

Comments :
0

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjvYRt8Y_BjAy_5jJ_3l2fLlfyEQ3CMOozw3OCFbnoENtnxNe2oR1wsMXfALfIhCk4DpNNpJcu6tsgSobQWAcmCO1re4IuYNmC6ldClMPzRrOQrYTGRsKl17b70TJIXYPZmRd-T002mgYssex4iawS1UkSfhBzQfcHHc1kEGn7WTFSlR4tm-r7UfEnbCBw/s320/mtt.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjvYRt8Y_BjAy_5jJ_3l2fLlfyEQ3CMOozw3OCFbnoENtnxNe2oR1wsMXfALfIhCk4DpNNpJcu6tsgSobQWAcmCO1re4IuYNmC6ldClMPzRrOQrYTGRsKl17b70TJIXYPZmRd-T002mgYssex4iawS1UkSfhBzQfcHHc1kEGn7WTFSlR4tm-r7UfEnbCBw/s1024/mtt.png)

Hello Reader,

If you've ever done forensics on modern linux systems disk images you may have encountered the dread that comes with dealing with lots of LVMs (Logical Volume Management) which none of the commercial forensics tools seem to be able to fully handle, yes even Xways.  Well instead of being full of existential dread of having to export, reimport and handle all of these partitions you can take advantage of the command line kung fu of Hal Pomeranz to automate this process for you!

Hal wrote a tool called MTT or Mount That Thing which .. well it's mounts things! You provide it with the linux disk images and it takes care of finding, identifying and mounting all of the LVMs and partitions within it so the data is accessible.

### Overview of the Script

This script is designed to automate the following operations:

* Mounting disk images (E01 or raw)
* Handling LVM volumes
* Automatically identifying and mounting partitions
* Exporting mounted partitions into E01 format if desired
* Safely unmounting and cleaning up devices and volumes when finished

All mount operations are performed read-only, with noexec and other conservative options to preserve evidence integrity.

---

### Key Features

#### Mounting Disk Images

* **E01 support**: If the image is in Expert Witness format, the script uses `ewfmount` to extract the raw image and proceed with analysis.
* **Partition detection**: For full disk images (e.g., MBR), it uses `losetup -P` to enumerate partitions and identify associated file systems.
* **LVM support**: Detects and activates volume groups, carefully handling potential naming collisions with already mounted LVM volumes.
* **Filesystem recognition**: Supports EXT2/3/4, XFS, BTRFS, and FAT file systems, with logic to apply the appropriate mount options for each.
* **Root partition detection**: Identifies the likely root partition via `fstab` or naming heuristics and mounts it first.
* **Command logging**: All mount operations are logged to a `MOUNTING` file within the target directory for reproducibility and audit trails.

#### Export to E01 Format

When invoked with the `-E` flag, the script will:

* Export each mounted partition using `ewfacquire`
* Segment the output if required via the `-S` option (e.g., for 2 GB chunks)
* Name exports based on their mount point or partition origin to maintain clear context
* Store exports and logs in an `exported/` subdirectory of the target mount path

This is especially useful for archiving or handing off discrete pieces of evidence.

#### Safe and Comprehensive Unmounting

Using the `-U` flag, the script will:

* Unmount all associated filesystems
* Deactivate volume groups via `vgchange -a n`
* Detach all loopback devices with `losetup -d`
* Kill any `ewfmount` processes by unmounting their working directory

This ensures that the analyst can return the system to a clean state after analysis or re-run the script on a new image without residual device conflicts.

---

### Usage Example

Mount and export an image:

```
./mount_image.sh -d /mnt/evidence -E -S 2147483648 image.E01
```

Unmount everything cleanly:

```
./mount_image.sh -U /mnt/evidence
```

Default behavior places mount artifacts under a `mount/` directory, but this can be overridden with the `-d` flag.

Give it a shot!

<https://github.com/halpomeranz/dfis/blob/master/mtt.sh>

#### Post a Comment

[Newer Post](https://www.hecfblog.com/2025/04/daily-blog-806-solution-saturday-41225.html "Newer Post")

[Older Post](https://www.hecfblog.com/2025/04/daily-blog-804-introducing-puck.html "Older Post")
[Home](https://www.hecfblog.com/)

Subscribe to:
[Post Comments
(
Atom
)](https://www.hecfblog.com/feeds/8610252375975548341/comments/default)

## Top Posts/Right Now

* [![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiS4Zw9KQkjNkc2JCwa0rDb1zPUCypCWZgocTE2voitZGOwzeZ2L_4D63LJ0j9JPosWO-nLahPLJYL-tsQMEgmfVhxmjpJ6Smn6FKVk2_JhClTq_WWhvcE13R76fsdeVWnJb-lPNFnJnif0HpOq-5yuADLWqHUQjQG4zpbLb46P0PM-dvHaM9rsb-D39qs/s72-c/sundayfunday.png)](https://www.hecfblog.com/2025/04/daily-blog-814-sunday-funday-42025.html)

  [Daily Blog #814: Sunday Funday 4/20/25](https://www.hecfblog.com/2025/04/daily-blog-814-sunday-funday-42025.html)
* [![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEj5GWh0tXGteqxfrTQFDzW2kMooGHcwNkA6h9f_bfBDpsRMJtvg0UR1SHfIqx4UYxViUSiLEJFeWq9SryUdFz5gwlrOlXEFCZDoNnqRlbU3pn_lGfYxr60W3HgTAXc7b3IqLHYN3F0kW72JbkCoEID0IEVH-rls7Q1LRd_0awNugK97uT7EDxugHyuXvFM/s72-c/forgive.png)](https://www.hecfblog.com/2025/04/daily-blog-815-i-missed-day.html)

  [Daily Blog #815: I missed a day](https://www.hecfblog.com/2025/04/daily-blog-815-i-missed-day.html)
* [![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEi60iLy5WiSNWWSyeIoM9JsOK9Xwv5L7GT5g4NxBmdQwyQNbbHzgWoiG4FbwefVVrqg1yDaz0ripRAlyXSWNX4xJ3tACOcH7a0_YyoPVT2XMPnI2-0aE3gKc9hJWhMWYqDWlTUDM2XM3DEHiJB5Z1iSrtjQeP0qG5xKxmt4RewUfbqA0FR7cw1DXPwxYNM/s72-c/solutionsaturday.png)](https://www.hecfblog.com/2025/04/daily-blog-813-solution-saturday-41925.html)

  [Daily Blog #813: Solution Saturday 4/19/25](https://www.hecfblog.com/2025/04/daily-blog-813-solution-saturday-41925.html)
* [![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhK3OAgdGTujkTy5X-nM4364yuWc8TJa-ct4GGE-Phw3vdXX9DApDT_kRhIvjELWVYLvnTPIrJTGFuz2hhkhVoklmY6bixe4fypY1X1A8RuJgAoPUUK597HYTBKVrOgLMn11x2g6b0azfhNnVv7CE6p-ZZRcfmAnaIIB-RNEBL_rIakVyr80MUyDhMQGgI/s72-c/removefromgroup.png)](https://www.hecfblog.com/2025/04/daily-blog-812-testing-aws-log-latency.html)

  [Daily Blog #812: Testing AWS Log latency - Removing Users from Groups](https://www.hecfblog.com/2025/04/daily-blog-812-testing-aws-log-latency.html)
* [![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEitgwVMjukTzCuo_bdlGs6epwr95Xl8x8_1MJt_...