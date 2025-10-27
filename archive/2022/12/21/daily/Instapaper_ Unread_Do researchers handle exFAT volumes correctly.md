---
title: Do researchers handle exFAT volumes correctly
url: https://dfir.ru/2022/12/18/do-researchers-handle-exfat-volumes-correctly/
source: Instapaper: Unread
date: 2022-12-21
fetch_date: 2025-10-04T02:10:09.845051
---

# Do researchers handle exFAT volumes correctly

[Skip to content](#content)

[My DFIR Blog](https://dfir.ru/)

Digital Forensics & Incident Response & Reverse Engineering & Vulnerability Research

Menu

* [Home](/)
* [About Me](https://dfir.ru/me/)
* [My Tools](https://dfir.ru/tools/)

# Do researchers handle exFAT volumes correctly?

[December 18, 2022April 19, 2023](https://dfir.ru/2022/12/18/do-researchers-handle-exfat-volumes-correctly/) ~ [Maxim Suhanov](https://dfir.ru/author/msuhanov/)

Let’s conduct a simple experiment. In the Ext4 file system, I create two files (“1.txt” and “2.txt”).

```
touch 1.txt 2.txt
```

Then, I gather file system metadata (including timestamps) for these files:

```
sudo debugfs -R 'stat /path_to/the_file/1.txt' /dev/block_device
sudo debugfs -R 'stat /path_to/the_file/2.txt' /dev/block_device
```

In my case, the output is:

*For “1.txt”:*

```
Inode: 23918802   Type: regular    Mode:  0644   Flags: 0x80000
Generation: 2882061095    Version: 0x00000000:00000001
User:  1000   Group:  1000   Project:     0   Size: 0
File ACL: 0
Links: 1   Blockcount: 0
Fragment:  Address: 0    Number: 0    Size: 0
 ctime: 0x6399ee07:e1dbba28 -- Wed Dec 14 18:38:47 2022
 atime: 0x6399ee07:e1dbba28 -- Wed Dec 14 18:38:47 2022
 mtime: 0x6399ee07:e1dbba28 -- Wed Dec 14 18:38:47 2022
crtime: 0x6399ee07:e1dbba28 -- Wed Dec 14 18:38:47 2022
Size of extra inode fields: 32
Inode checksum: 0x9906b43e
EXTENTS:
```

**For “2.txt”:**

```
Inode: 23921678   Type: regular    Mode:  0644   Flags: 0x80000
Generation: 2369567438    Version: 0x00000000:00000001
User:  1000   Group:  1000   Project:     0   Size: 0
File ACL: 0
Links: 1   Blockcount: 0
Fragment:  Address: 0    Number: 0    Size: 0
 ctime: 0x6399ee07:e1dbba28 -- Wed Dec 14 18:38:47 2022
 atime: 0x6399ee07:e1dbba28 -- Wed Dec 14 18:38:47 2022
 mtime: 0x6399ee07:e1dbba28 -- Wed Dec 14 18:38:47 2022
crtime: 0x6399ee07:e1dbba28 -- Wed Dec 14 18:38:47 2022
Size of extra inode fields: 32
Inode checksum: 0x9b052019
EXTENTS:
```

Now, I’m going to store something in these files. I will use the *bash* shell to append some text to the first file (using the output redirection syntax) and the *gedit* text editor to modify the second one.

```
echo 123 >> 1.txt
gedit 2.txt # In the gedit window, I will type "456" and hit Ctrl-S.
```

And let’s get the timestamps for these files again…

*For “1.txt”:*

```
Inode: 23918802   Type: regular    Mode:  0644   Flags: 0x80000
Generation: 2882061095    Version: 0x00000000:00000001
User:  1000   Group:  1000   Project:     0   Size: 4
File ACL: 0
Links: 1   Blockcount: 8
Fragment:  Address: 0    Number: 0    Size: 0
 ctime: 0x6399eed2:68debfb8 -- Wed Dec 14 18:42:10 2022
 atime: 0x6399ee07:e1dbba28 -- Wed Dec 14 18:38:47 2022
 mtime: 0x6399eed2:68debfb8 -- Wed Dec 14 18:42:10 2022
crtime: 0x6399ee07:e1dbba28 -- Wed Dec 14 18:38:47 2022
Size of extra inode fields: 32
Inode checksum: 0x4a517d18
EXTENTS:
(0):95716043
```

**For “2.txt”:**

```
Inode: 23860507   Type: regular    Mode:  0644   Flags: 0x80000
Generation: 534549923    Version: 0x00000000:00000001
User:  1000   Group:  1000   Project:     0   Size: 4
File ACL: 0
Links: 1   Blockcount: 8
Fragment:  Address: 0    Number: 0    Size: 0
 ctime: 0x6399eed8:16d4b85c -- Wed Dec 14 18:42:16 2022
 atime: 0x6399eed8:14ec7284 -- Wed Dec 14 18:42:16 2022
 mtime: 0x6399eed8:16d4b85c -- Wed Dec 14 18:42:16 2022
crtime: 0x6399eed8:14ec7284 -- Wed Dec 14 18:42:16 2022
Size of extra inode fields: 32
Inode checksum: 0x2b67e3c3
EXTENTS:
(0):96358507
```

Do you see anything unusual?

In the first case (“1.txt”), the “ctime” (inode changed) and “mtime” (last modification) fields are updated.

But in the second case (“2.txt”), all four timestamps are updated (including “crtime” and “atime” — created and last access timestamps respectively). Moreover, the inode number isn’t the same as before.

**Actually, this is expected behavior!** Some text editors, including *gedit*, replace the file during the save operation. In particular, a temporary file with updated content is written to the drive, then this file is renamed to replace the original file. This is why we see a completely new inode in the second case (“2.txt”).

(It should be noted that an old file, which was replaced during the save operation, or at least some of its metadata can be recovered, just like with any other deleted file.)

Applications do so to perform “atomic” updates to files. This means that users will see either old or new file data, but not file data in the mid-update state (e.g., when a power outage interrupted an ongoing update to file data). (Such an “atomic” update is not really atomic — the underlying file system implementation may lose the file or retain its temporary name during the interrupted rename operation if there is no journaling or copy-on-write metadata support implemented, just like in the exFAT file system.)

To account this behavior, [Windows systems use file system tunnelling](https://devblogs.microsoft.com/oldnewthing/20050715-14/?p=34923):

> In other words, if you delete some file “File with long name.txt” and then create a new file with the same name, that new file will have the same short name and **the same creation time** as the original file.

But this feature doesn’t exist in the Linux world. If you create a new file, it’s a new file with its own timestamps. And this behavior can be observed across other file systems supported by Linux, including exFAT. File system drivers have no obligation to preserve the “old” value of the “crtime” field in such cases, userspace applications have no similar obligation too.

Even more, [Microsoft says that file system tunnelling merely exists to support old (16-bit) applications](https://web.archive.org/web/20091224090526/http%3A//support.microsoft.com/kb/172190):

> The idea is to mimic the behavior MS-DOS programs expect when they use the safe save method. They copy the modified data to a temporary file, delete the original and rename the temporary to the original. This should seem to be the original file when complete. **Windows performs tunneling on both FAT and NTFS file systems to ensure long/short file names are retained when 16-bit applications perform this safe save operation.**

[Some think that this feature is a hack](https://sourceforge.net/p/scintilla/feature-requests/1225/#1cd7/a284/cbab/7af1):

> Also: tunneling is a last-resort *hack* to help users avoid losing data. It has never been foolproof or robust: it will fail if there is too long a delay between when the file is replaced, or if too many files are replaced in too short a timespan. Put another way, it’s meant and designed for address the fact that programs are careless about how they handle user files, not as a substitute for proper file handling.

So, it’s okay if file system drivers don’t support the tunnelling feature.

However, some researchers seem to be unaware of the “atomic” update feature implemented in some applications and its implications on file system metadata.

[In a recent article, “It is about time–Do exFAT implementations handle timestamps correctly?”,](https://www.sciencedirect.com/science/article/pii/S2666281722001573) the following conclusions are drawn:

1. The MacOS and Linux changes the timestamp for creation when using TextEdit or Gedit to change the content of a file. This means the timestamps are changed by the driver, and it may already be inaccurate before parsing and interpretations of Digital Forensic tools. *(Page 12.)*
2. If the files are changed by using Gedit in Linux the UTCOffset are set to 0x00 and all timestamps are changed to the time of the update. Therefore, the original created date is lost. *(Page 11.)*
3. We recommend using X-Ways or FTK Imager to interpret exFAT, and use patterns to identify which OS has been used in order to make an accurate interpretation of the timestamps. *(…)* Further, we recommend law enforcement to reassess criminal cases where exFAT and timestamps have been an important evidence to make sure...