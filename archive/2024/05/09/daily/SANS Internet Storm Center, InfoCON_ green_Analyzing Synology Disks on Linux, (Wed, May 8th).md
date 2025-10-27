---
title: Analyzing Synology Disks on Linux, (Wed, May 8th)
url: https://isc.sans.edu/diary/rss/30904
source: SANS Internet Storm Center, InfoCON: green
date: 2024-05-09
fetch_date: 2025-10-06T17:19:12.528090
---

# Analyzing Synology Disks on Linux, (Wed, May 8th)

# [Internet Storm Center](/)

[Sign In](/login.html)
[Sign Up](/register.html)

Handler on Duty: [Johannes Ullrich](/handler_list.html#johannes-ullrich "Johannes Ullrich")

Threat Level: [green](/infocon.html)

* [previous](/diary/30898)
* [next](/diary/30908)

My next class:

|  |  |  |
| --- | --- | --- |
| [Reverse-Engineering Malware: Advanced Code Analysis](https://www.sans.org/event/live-online-europe-october-2025/course/reverse-engineering-malware-advanced-code-analysis) | Online | Greenwich Mean Time | Oct 27th - Oct 31st 2025 |

# [Analyzing Synology Disks on Linux](/forums/diary/Analyzing%2BSynology%2BDisks%2Bon%2BLinux/30904/)

**Published**: 2024-05-08. **Last Updated**: 2024-05-08 07:00:07 UTC
**by** [Xavier Mertens](/handler_list.html#xavier-mertens) (Version: 1)

[0 comment(s)](/diary/Analyzing%2BSynology%2BDisks%2Bon%2BLinux/30904/#comments)

Synology NAS solutions are popular devices. They are also used in many organizations. Their product range goes from small boxes with two disks (I’m not sure they still sell a single-disk enclosure today) up to monsters, rackable with plenty of disks. They offer multiple disk management options but rely on many open-source software (like most appliances). For example, there are no expensive hardware RAID controllers in the box. They use the good old “MD” (“multiple devices”) technology, managed with the well-known mdadm tool[[1](https://en.wikipedia.org/wiki/Mdadm)]. Synology NAS run a Linux distribution called DSM. This operating system has plenty of third-party tools but lacks pure forensics tools.

In a recent investigation, I had to investigate a NAS that was involved in a ransomware attack. Many files (backups) were deleted. The attacker just deleted some shared folders. The device had two drives configured in RAID0 (not the best solution I know but they lack storage capacity). The idea was to mount the file system (or at least have the block device) on a Linux host and run forensic tools, for example, photorec.

In such a situation, the biggest challenge will be to connect all the drivers to the analysis host! Here, I had only two drives but imagine that you are facing a bigger model with 5+ disks. In my case, I used two USB-C/SATA adapters to connect the drives. Besides the software RAID, Synology volumes also rely on LVM2 (“Logical Volume Manager”)[[2](https://en.wikipedia.org/wiki/Logical_Volume_Manager_%28Linux%29)]. In most distributions, the packages mdadm and lvm2 are available (for example on SIFT Workstation). Otherwise, just install them:

```

# apt install mdadm lvm2
```

Once you connect the disks (tip: add a label on them to replace them in the right order) to the analysis host, verify if they are properly detected:

```

# lsblk
NAME    MAJ:MIN RM   SIZE RO TYPE  MOUNTPOINTS
sda       8:0    0 465.8G  0 disk
|-sda1    8:1    0 464.8G  0 part  /
|-sda2    8:2    0     1K  0 part
`-sda5    8:5    0   975M  0 part  [SWAP]
sdb       8:16   0   3.6T  0 disk
|-sdb1    8:17   0     8G  0 part
|-sdb2    8:18   0     2G  0 part
`-sdb3    8:19   0   3.6T  0 part
sdc       8:32   0   3.6T  0 disk
|-sdc1    8:33   0   2.4G  0 part
|-sdc2    8:34   0     2G  0 part
`-sdc3    8:35   0   3.6T  0 part
sr0      11:0    1  1024M  0 rom
```

"sdb3" and "sdc3" are the NAS partitions used to store data (2 x 4TB in RAID0). The good news, the kernel will detect that these disks are part of a software RAID! You just need to rescan them and "re-assemble" the RAID:

```

# mdadm --assemble --readonly --scan --force --run
```

Then, your data should be available via a /dev/md? device:

```

# cat /proc/mdstat
Personalities : [raid0]
md0 : active (read-only) raid0 sdb3[0] sdc3[1]
      7792588416 blocks super 1.2 64k chunks

unused devices: <none>
```

The next step is to detect how data are managed by the NAS. Synology provides a technology called SHR[[3](https://kb.synology.com/en-br/DSM/tutorial/What_is_Synology_Hybrid_RAID_SHR)] that uses LVM:

```

# lvdisplay
  WARNING: PV /dev/md0 in VG vg1 is using an old PV header, modify the VG to update.
  --- Logical volume ---
  LV Path                /dev/vg1/syno_vg_reserved_area
  LV Name                syno_vg_reserved_area
  VG Name                vg1
  LV UUID                08g9nN-Etde-JFN9-tn3D-JPHS-pyoC-LkVZAI
  LV Write Access        read/write
  LV Creation host, time ,
  LV Status              NOT available
  LV Size                12.00 MiB
  Current LE             3
  Segments               1
  Allocation             inherit
  Read ahead sectors     auto

  --- Logical volume ---
  LV Path                /dev/vg1/volume_1
  LV Name                volume_1
  VG Name                vg1
  LV UUID                fgjC0Y-mvx5-J5Qd-Us2k-Ppaz-KG5X-tgLxaX
  LV Write Access        read/write
  LV Creation host, time ,
  LV Status              NOT available
  LV Size                <7.26 TiB
  Current LE             1902336
  Segments               1
  Allocation             inherit
  Read ahead sectors     auto
```

You can see that the NAS has only one volume created ("volume\_1" is the default name in DSM).

From now on, you can use /dev/vg1/volume\_1 in your investigations. Mount it, scan it, image it, etc...

[1] <https://en.wikipedia.org/wiki/Mdadm>
[2] [https://en.wikipedia.org/wiki/Logical\_Volume\_Manager\_(Linux)](https://en.wikipedia.org/wiki/Logical_Volume_Manager_%28Linux%29)
[3] <https://kb.synology.com/en-br/DSM/tutorial/What_is_Synology_Hybrid_RAID_SHR>

Xavier Mertens (@xme)
Xameco
Senior ISC Handler - Freelance Cyber Security Consultant
[PGP Key](https://keybase.io/xme/key.asc)

Keywords: [LVM](/tag.html?tag=LVM) [Disk](/tag.html?tag=Disk) [Storage](/tag.html?tag=Storage) [mdstat](/tag.html?tag=mdstat) [madm](/tag.html?tag=madm) [NAS](/tag.html?tag=NAS) [Synology](/tag.html?tag=Synology) [volume](/tag.html?tag=volume) [RAID](/tag.html?tag=RAID) [forensics](/tag.html?tag=forensics) [DFIR](/tag.html?tag=DFIR)

[0 comment(s)](/diary/Analyzing%2BSynology%2BDisks%2Bon%2BLinux/30904/#comments)

My next class:

|  |  |  |
| --- | --- | --- |
| [Reverse-Engineering Malware: Advanced Code Analysis](https://www.sans.org/event/live-online-europe-october-2025/course/reverse-engineering-malware-advanced-code-analysis) | Online | Greenwich Mean Time | Oct 27th - Oct 31st 2025 |

* [previous](/diary/30898)
* [next](/diary/30908)

### Comments

[Login here to join the discussion.](/login)

Top of page

×

![modal content]()

[Diary Archives](/diaryarchive.html)

* [![SANS.edu research journal](https://isc.sans.edu/images/researchjournal5.png)](/j/research)
* [Homepage](/index.html)
* [Diaries](/diaryarchive.html)
* [Podcasts](/podcast.html)
* [Jobs](/jobs)
* [Data](/data)
  + [TCP/UDP Port Activity](/data/port.html)
  + [Port Trends](/data/trends.html)
  + [SSH/Telnet Scanning Activity](/data/ssh.html)
  + [Weblogs](/weblogs)
  + [Domains](/data/domains.html)
  + [Threat Feeds Activity](/data/threatfeed.html)
  + [Threat Feeds Map](/data/threatmap.html)
  + [Useful InfoSec Links](/data/links.html)
  + [Presentations & Papers](/data/presentation.html)
  + [Research Papers](/data/researchpapers.html)
  + [API](/api)
* [Tools](/tools/)
  + [DShield Sensor](/howto.html)
  + [DNS Looking Glass](/tools/dnslookup)
  + [Honeypot (RPi/AWS)](/tools/honeypot)
  + [InfoSec Glossary](/tools/glossary)
* [Contact Us](/contact.html)
  + [Contact Us](/contact.html)
  + [About Us](/about.html)
  + [Handlers](/handler_list.html)* [About Us](/about.html)

[Slack Channel](/slack/index.html)

[Mastodon](https://infosec.exchange/%40sans_isc)

[Bluesky](https://bsky.app/profile/sansisc.bsky.social)

[X](https://twitter.com/sans_isc)

![](/adimg.html?id=)

© 2025 SANS™ Internet Storm Center
Developers: We have an [API](/api/) for you!   [![Creative Commons License](/images/cc.png)](https://creativecommons.org/licenses/by-nc-sa/4.0/)

* [Link To Us](/linkback.html)
* [About Us](/about.html)
* [Handlers](/handler_list.html)
* [Privacy Policy](/privacy.html)