---
title: How To Process A Clear-Key BitLocker Image File To Generate A Decrypted Raw Image
url: https://www.forensicfocus.com/articles/how-to-process-a-clear-key-bitlocker-image-file-to-generate-a-decrypted-raw-image/
source: Instapaper: Unread
date: 2026-08-12
fetch_date: 2026-08-13T04:05:26.778361
---

# How To Process A Clear-Key BitLocker Image File To Generate A Decrypted Raw Image

[Skip to content](#content "Skip to content")

[![Forensic Focus](https://www.forensicfocus.com/stable/wp-content/themes/generatepress_child/assets/images/logo.png)](https://www.forensicfocus.com/ "Forensic Focus")

[Login](/sign-in/)
[Register](/sign-up/)

[![Forensic Focus](https://www.forensicfocus.com/stable/wp-content/uploads/2020/05/forensic-focus_logo.png)](https://www.forensicfocus.com/ "Forensic Focus")

Menu

* [News](/news/)
* Articles
  + [Articles](/articles/)
  + [Interviews](/interviews/)
  + [Case Studies](/case-studies/)
  + [Reviews](/reviews/)
  + [Guides](/guides/)
  + [Digital Forensics Timeline](/digital-forensics-timeline/)
  + [Tool & Vendor Directory](/dfir-tool-directory/)
  + [Tool Release Tracker](/dfir-tool-release-tracker/)
* Webinars/Videos
  + [Webinars](/webinars/)
  + [Videos](/videos/)
* Careers & Jobs
  + [Browse Jobs](/jobs/)
  + [How to Start a Career](/articles/how-to-start-a-career-in-digital-forensics/)
  + [Education & Training Guide](/articles/digital-forensics-education-certification-and-training-guide/)
  + [Training Finder](/dfir-training-finder/)
  + [Salary Explorer](/dfir-salary-explorer/)
  + [Skills in Demand](/dfir-skills-demand-explorer/)
  + [Practice & CTFs](/dfir-practice-directory/)
* [Well-Being](/well-being/)
* Events
  + [Event Calendar](/events/)
  + [Event Info & Recaps](/event-info/)

* [Forums](/forums/)
* [Discord](https://discord.gg/97zKvTXHeS)
* [Podcast](/podcast/)
* [Newsletter](/newsletter/)
* [Links](/useful-links/)
* [Advertise](/advertising/)
* [About](/about/)

Menu

* [News](/news/)
* Articles
  + [Articles](/articles/)
  + [Interviews](/interviews/)
  + [Case Studies](/case-studies/)
  + [Reviews](/reviews/)
  + [Guides](/guides/)
  + [Digital Forensics Timeline](/digital-forensics-timeline/)
  + [Tool & Vendor Directory](/dfir-tool-directory/)
  + [Tool Release Tracker](/dfir-tool-release-tracker/)
* Webinars/Videos
  + [Webinars](/webinars/)
  + [Videos](/videos/)
* Careers & Jobs
  + [Browse Jobs](/jobs/)
  + [How to Start a Career](/articles/how-to-start-a-career-in-digital-forensics/)
  + [Education & Training Guide](/articles/digital-forensics-education-certification-and-training-guide/)
  + [Training Finder](/dfir-training-finder/)
  + [Salary Explorer](/dfir-salary-explorer/)
  + [Skills in Demand](/dfir-skills-demand-explorer/)
  + [Practice & CTFs](/dfir-practice-directory/)
* [Well-Being](/well-being/)
* Events
  + [Event Calendar](/events/)
  + [Event Info & Recaps](/event-info/)

[Home](https://www.forensicfocus.com/) » [Articles](https://www.forensicfocus.com/articles/) » How To Process A Clear-Key BitLocker Image File To Generate A Decrypted Raw Image

# How To Process A Clear-Key BitLocker Image File To Generate A Decrypted Raw Image

11th August 2026 by [Pieces0310](https://www.forensicfocus.com/author/pieces0310/ "View all posts by Pieces0310")

![](https://www.forensicfocus.com/stable/wp-content/uploads/2026/08/ChatGPT-Image-Aug-10-2026-12_24_58-PM.png)

*[Pieces0310](https://www.forensicfocus.com/author/pieces0310/) is a digital forensics practitioner with many years of experience in computer and mobile investigations, strengthened by a solid background in cybersecurity.*

When forensic examiners complete the acquisition of an evidence image file but find that the partition content is unrecognizable upon mounting, they must consider whether encryption is the cause. A BitLocker volume protected by a Clear Key contains the key material needed to unlock the encrypted volume within the forensic image itself, so no external recovery key or password is required. I will use [dislocker](https://github.com/aorimn/dislocker) and [bdeinfo](https://github.com/libyal/libbde/tree/main/bdetools) to unveil the mystery behind BitLocker Clear Key.

## Identifying the BitLocker-Encrypted Partition

First, let’s look at a BitLocker-encrypted image file that uses a clear key. There is indeed a partition suspected of being encrypted and protected, causing the file system structure within it to be unrecognizable. Based on the presence of the classic signature “-FVE-FS-” in its partition header, we can tell it is BitLocker encryption, where FVE stands for Full Volume Encryption, as shown in the figure below.

![](https://www.forensicfocus.com/stable/wp-content/uploads/2026/08/image-6.jpg)

## Preparing the Forensic Image

Next, for compatibility with the tools and workflow used in this example, I converted the forensic image file (`.E01`) to raw (`.dd`) format and then copied it to an external hard drive. Since the ultimate goal is to decrypt this BitLocker partition and produce a decrypted raw image to an external drive, I first confirmed that the external drive was successfully mounted and in rw (read-write) mode, as shown in the figure below.

![](https://www.forensicfocus.com/stable/wp-content/uploads/2026/08/image-11.jpg)

Let’s  take a look at this image file named bitlocker-clearkey.dd. The signature “-FVE-FS-” can be clearly observed at this point viewed via the hexdump command or the dislocker tool, as shown in the figure below.

## Get The Latest DFIR News

### The monthly Forensic Focus newsletter, plus webinar invitations and occasional research surveys.

Unsubscribe or change what you receive at any time. We respect your privacy: read our [privacy policy](/privacy-policy).

Leave this field empty if you're human:

![](https://www.forensicfocus.com/stable/wp-content/uploads/2026/08/image-3.jpg)

![](https://www.forensicfocus.com/stable/wp-content/uploads/2026/08/image-8.jpg)

## Using Dislocker

Some might be curious: what is this tool named dislocker used for? It is a super powerful tool on Linux used to decrypt, mount, and access BitLocker-encrypted partitions or image files. I use dislocker to decrypt the BitLocker image file and output the decrypted virtual NTFS device to a specified path. The full command is shown in the figure below.

![](https://www.forensicfocus.com/stable/wp-content/uploads/2026/08/image-5.jpg)

## Understanding the Dislocker Command

To help everyone understand what the command is doing, the command and its parameters are broken down as follows:

-V: Specifies the volume, followed by the BitLocker partition or image file

–: These are two hyphens indicating the end of parameters; any strings following them will no longer be treated as parameters

The `~/decrypted` at the very end of the command is the output path I specified. After execution, a file named dislocker-file will be generated in the decrypted folder under the home directory, as shown in the figure below.

![](https://www.forensicfocus.com/stable/wp-content/uploads/2026/08/image-13.jpg)

## Understanding the Dislocker File

However, it is not an ordinary file, but a “virtual decrypted disk interface” provided through FUSE (Filesystem in Userspace). What makes the dislocker-file special is that although it reports approximately the same apparent size as the BitLocker volume, it is a virtual decrypted disk interface and does not consume an equivalent amount of storage space. This is a thoughtful design by dislocker for space utilization, avoiding the hassle of directly generating a massive decrypted image file. The decrypted raw image is only obtained when forensic examiners copy it to a destination disk.

![](https://www.forensicfocus.com/stable/wp-content/uploads/2026/08/image-14.jpg)

## Monitoring the Copy Progress

To monitor the copy progress in real time, monitor the size of the destination image file:

> watch -n1 ‘ls -lh {path}/dislocker-file’

![](https://www.forensicfocus.com/stable/wp-content/uploads/2026/08/image-15.jpg)

![](https://www.forensicfocus.com/stable/wp-content/uploads/2026/08/image-12.jpg)

## Verifying the Decrypted Image

So how do we verify that the image file named dislocker-file is indeed a successfully decrypted raw image? Forensic examiners only need to mount it to find out that the partition’s file system is NTFS. Its file system structure and the...