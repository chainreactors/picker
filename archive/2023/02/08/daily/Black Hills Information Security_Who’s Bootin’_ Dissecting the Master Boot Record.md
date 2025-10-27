---
title: Who’s Bootin’? Dissecting the Master Boot Record
url: https://www.blackhillsinfosec.com/dissecting-the-master-boot-record/
source: Black Hills Information Security
date: 2023-02-08
fetch_date: 2025-10-04T05:59:28.810461
---

# Who’s Bootin’? Dissecting the Master Boot Record

[![Black Hills Information Security, Inc.](https://www.blackhillsinfosec.com/wp-content/uploads/2025/03/BHIS_TEXT_BHIS.png)](https://www.blackhillsinfosec.com "Black Hills Information Security, Inc.")

[RSS](https://www.blackhillsinfosec.com/feed/)

* [All Services](https://www.blackhillsinfosec.com/services/)
  + [Complete Service Guide](https://www.blackhillsinfosec.com/services/complete-service-guide/)
  + [Active SOC](https://www.blackhillsinfosec.com/services/active-soc/)
  + [AI Security Assessments](https://www.blackhillsinfosec.com/services/ai-security-assessments/)
  + [Blockchain Security](https://www.blackhillsinfosec.com/services/blockchain-security/)
  + [Blue Team Services](https://www.blackhillsinfosec.com/services/blue-team-services/)
  + [Continuous Penetration Testing](https://www.blackhillsinfosec.com/services/antisoc/)
  + [High-Profile Risk Assessments](https://www.blackhillsinfosec.com/services/high-profile-risk-assessments/)
  + [Incident Response](https://www.blackhillsinfosec.com/services/incident-response/)
  + [Penetration Testing](https://www.blackhillsinfosec.com/services/)
* [Contact Us](https://www.blackhillsinfosec.com/contact-us/)
  + [Contact Us](https://www.blackhillsinfosec.com/contact-us/)
  + [Email Sign-Up](https://mailchi.mp/blackhillsinfosec.com/bhis-sign-up)
* [About Us](https://www.blackhillsinfosec.com/who-we-are/)
  + [Security Consultants](https://www.blackhillsinfosec.com/about/security-analysts/)
  + [Admin](https://www.blackhillsinfosec.com/about/admin-staff/)
  + [SOC Team](https://www.blackhillsinfosec.com/about/soc-team/)
  + [BHIS Family of Companies](https://www.blackhillsinfosec.com/bhis-tribe-of-companies/)
* [Free Resources](https://www.blackhillsinfosec.com/free-cybersecurity-tools/)
  + [Blogs](https://www.blackhillsinfosec.com/blog/)
  + [Free Cybersecurity Tools](https://www.blackhillsinfosec.com/free-cybersecurity-tools/)
  + [Free Cybersecurity Webcasts](https://www.blackhillsinfosec.com/free_cybersecurity_webcasts/)
  + [Podcasts](https://podcasts.apple.com/us/podcast/black-hills-information-security/id1410835265)
  + [RITA](https://www.activecountermeasures.com/free-tools/rita/)
* [Training](https://www.blackhillsinfosec.com/bhis-and-antisyphon-training/)
  + [BHIS & Antisyphon Training](https://www.blackhillsinfosec.com/bhis-and-antisyphon-training/)
  + [WWHF Conference](https://wildwesthackinfest.com)
* [Online Community](https://blackhillsinfosec.com/community)
  + [Discord](https://discord.gg/BHIS)
  + [LinkedIn](https://www.linkedin.com/company/black-hills-information-security/)
  + [YouTube](https://www.youtube.com/c/BlackHillsInformationSecurity/videos)
  + [Bluesky](https://bsky.app/profile/bhinfosecurity.bsky.social)
  + [Twitter/X](https://twitter.com/BHinfoSecurity)
  + [Upcoming Events](https://blackhillsinfosec.com/events)
* [Fun Stuff](https://spearphish-general-store.myshopify.com/)
  + [Backdoors & Breaches](https://www.blackhillsinfosec.com/tools/backdoorsandbreaches/)
  + [Merch, Zines & More](https://spearphish-general-store.myshopify.com/)
  + [PROMPT# Zine](https://www.blackhillsinfosec.com/prompt-zine/)
  + [REKCAH](https://www.blackhillsinfosec.com/rekcah/)
  + [Books](https://www.blackhillsinfosec.com/tools/books/)

7
Feb
2023

[Blue Team](https://www.blackhillsinfosec.com/category/blue-team/), [DFIR](https://www.blackhillsinfosec.com/category/dfir/), [General InfoSec Tips & Tricks](https://www.blackhillsinfosec.com/category/infosec-101/general-infosec-tips-tricks/), [Hal Denton](https://www.blackhillsinfosec.com/category/author/hal-denton/), [How-To](https://www.blackhillsinfosec.com/category/how-to/), [Informational](https://www.blackhillsinfosec.com/category/informational/)
[Digital Forensics and Incident Response](https://www.blackhillsinfosec.com/tag/digital-forensics-and-incident-response/), [Master Boot Record](https://www.blackhillsinfosec.com/tag/master-boot-record/)

# [Who’s Bootin’? Dissecting the Master Boot Record](https://www.blackhillsinfosec.com/dissecting-the-master-boot-record/)

[Hal Denton](https://www.linkedin.com/in/hal-denton-439b7a227/) //

![](https://www.blackhillsinfosec.com/wp-content/uploads/2023/02/BLOG_chalkboard_00612-1024x576.jpg)

Have you ever been given an encrypted hard drive to perform forensic analysis on? What could go wrong?

Probably the first thought rolling through your mind is wondering if the decryption key was included with the drive. If so, you are spot on in questioning that, as the analysis would be pretty much undoable without the decryption key. What if you have the decryption key but your forensic software doesn’t prompt you for the challenge/response to decrypt the drive? What do you do next?

In this blog, I will be talking about a scenario where things went wrong with what was supposed to be an acquisition of an encrypted full disk image, but… I received an encrypted volume. At the end of this post, you should understand the Master Boot Record (MBR) and how to manipulate it.

As a forensic practitioner, sometimes we need to dig in and figure out how things work.

![](https://www.blackhillsinfosec.com/wp-content/uploads/2023/02/Picture1.png)

Before we get started, one core term you will need to know: what is a sector on a hard drive? A sector is the smallest storage unit on disk and, typically, 512 bytes in size (it could also be bigger depending on the capacity of the drive). Additionally, you will need to know common sector address types, such as Cylinder Head Sector (CHS) and Logical Block Address (LBA). CHS uses disk geometry to map sectors to a head and cylinder number per platter, which requires a translation from the OS to BIOS to find the data on disk. CHS does not work on disks larger than 8.1GB. A predecessor to CHS is LBA, and it assigns sequential addresses to each sector, which eliminates the need to do a translation. The Operating System tells BIOS the address for where to find it on disk. LBA works on disks as large a 2TB due to the limitation of the MBR 32bit addressing.

# Master Boot Record (MBR) Summary

The MBR is assembly code that is 512 bytes in length and is located at sector 0 on a hard drive. Below is an example of an MBR viewed in a hex editor that I will be using to breakdown the 3 data structures that make up the MBR.

To help understand the hex editor view, the one I am using displays data into 3 columns, as labeled below. Column 1 tells you the byte offset of the first byte in the row. For example, if I wanted to manually check what the value is at byte offset 450, I can use column 1 to find the closest offset to 450, which is 448 (value 21) below, and count to the right two bytes (value 07). Column 2 shows the hex values of the data that was loaded into the hex editor, and column 3 shows the ASCII character conversion of the hex values.

![](https://www.blackhillsinfosec.com/wp-content/uploads/2023/02/Picture2-500x388.png)

## MBR – Data Structure Overview

The 3 data structures that make up the MBR is boot code, partition data, and the end of MBR signature. I will break down each structure by byte range and byte length so you will have a general understanding of each.

![](https://www.blackhillsinfosec.com/wp-content/uploads/2023/02/Picture3-500x236.png)

To validate our MBR by math, the total byte size should be 512 bytes (446+16+16+16+16+2=512 bytes).

## MBR – Boot Code Summary

Boot code holds instructions to tell the computer how to process the partition tables and locate the operating system.

![](https://www.blackhillsinfosec.com/wp-content/uploads/2023/02/Picture4.png)
![](https://www.blackhillsinfosec.com/wp-content/uploads/2023/02/Picture5.png)

## MBR – Partition Information Summary

Partitions are 16 bytes in length and hold up to four standard partitions for drives with 512 byte sectors. There can be more than 4 partitions by using an extended partition. A type field identifies what type of data should exist, such as FAT, NTFS, etc. Below shows where all 4 pa...