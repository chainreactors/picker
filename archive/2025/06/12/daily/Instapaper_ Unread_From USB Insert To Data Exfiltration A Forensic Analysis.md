---
title: From USB Insert To Data Exfiltration A Forensic Analysis
url: https://digitalinvestigator.blogspot.com/2025/05/from-usb-insert-to-data-exfiltration.html
source: Instapaper: Unread
date: 2025-06-12
fetch_date: 2025-10-06T22:56:09.451784
---

# From USB Insert To Data Exfiltration A Forensic Analysis

### Facebook SDK

* [Home](/)
* [whoami](https://digitalinvestigator.blogspot.com/p/trainingswebinars-attended.html?m=1)
* [Subscribe](https://blogspot.us14.list-manage.com/subscribe?u=f0561841d9ef7ca0687144c59&id=93ea8a701f)

[![Digital Investigator](https://blogger.googleusercontent.com/img/a/AVvXsEjCBXDAFtj3qeFsN0QARpauoOMU-9GGRJMhzK1L_edHwLn3gTy8NtKHApKnUjkKdWPgAEIcdSrosxULEGvjMszmWVhop1V0aiHOOEW8KeeKjSkfEk3bSEuXPRbuGgVQQJlHbfKNju9pNpyZOabgh-Oci700smDybZA3gHWWI5H2Mgy0h08GrB5-FiyV=s150)](https://digitalinvestigator.blogspot.com/)

* [Home](home-icon)
* [whoami](https://digitalinvestigator.blogspot.com/p/trainingswebinars-attended.html?m=1)
* [Subscribe](https://blogspot.us14.list-manage.com/subscribe?u=f0561841d9ef7ca0687144c59&id=93ea8a701f)

[Home](https://digitalinvestigator.blogspot.com/)[Windows Forensics](https://digitalinvestigator.blogspot.com/search/label/Windows%20Forensics)

# From USB Insert To Data Exfiltration: A Forensic Analysis

Joseph Moronwi
May 30, 2025
0

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEg4qYkdPT6ry-DowrQrIMGEncJaVQklLVbhdl9El_0tLgNn4WUZd-3HlnV2rCIL53M6ReqbGAHaEg71yoBeiMTHmTC4lPeV8Ecm6Wkil4FknNLhct_4a9hApOp__Ak-Zmj43ZIg9Kz0IqWCLZPtjN5zbqYIa1VUZPqgDDeb_lulsv1EKLmQz-lJ_Q5jBmE/w652-h344/images.jpeg)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEg4qYkdPT6ry-DowrQrIMGEncJaVQklLVbhdl9El_0tLgNn4WUZd-3HlnV2rCIL53M6ReqbGAHaEg71yoBeiMTHmTC4lPeV8Ecm6Wkil4FknNLhct_4a9hApOp__Ak-Zmj43ZIg9Kz0IqWCLZPtjN5zbqYIa1VUZPqgDDeb_lulsv1EKLmQz-lJ_Q5jBmE/s764/images.jpeg)

Insider threats remain one of the most difficult attack vectors to track and mitigate, especially when the culprit has physical access to a system. This post walks through a [**digital forensic challenge**](https://www.linkedin.com/posts/ahmedhashad_usb-insider-threat-challenge-activity-7323344613014941696-rxeK/?utm_source=share&utm_medium=member_desktop&rcm=ACoAADemZ3EBD1WuSvEvU-UZGgKkIijXrajtVIs) simulating such a scenario: an employee using a USB stick to exfiltrate confidential files from an unlocked corporate computer.

The following are questions posed in the USB insider threat forensic challenge:

1. What is the computer name?
2. What is the drive letter assigned to the USB drive?
3. What is the make and serial number of the connected USB stick? answer format (make, model, serial number).
4. What are the filenames of the 3 files copied to the USB? answer format (filename1.extension, filename2.extension, filename3.extension).
5. What is the MFT record number of the PPTX file from its original path on the unlocked computer?
6. Referring to the 3 files copied, what is the parent path of the files? (full path).
7. Examining the provided evidence, how many times did the admin user click on the Start button?
8. Which user was logged in when the USB drive connected? Please also specify the volume GUID of the flash drive. Answer format (username, volume GUID), example (john, {5d6f-d5f5-d5f5-d5f5}).
9. What is the last removal date and time of the USB drive? Answer format (date MM-DD-YYYY, time 24 hr 00:00:00), example (05-08-1990, 23:25:15).
10. What is the number of partitions and total sectors of every partition on the connected flash drive? answer format (number, number), example (3,5698458455).
11. What is the USB drive's file system ID and type (e.g., FAT32, NTFS)? answer format (0x00, type), example (0x05, FAT16).
12. What is the USB drive's Volume Serial Number (VSN) in hex? Answer in the format (only hex values without spaces), using an example (11CD11CD11CD11CD11CD11CD11CD).

### Q1 - What is the Computer name?

While a seemingly simple piece of information, the computer hostname is important for several reasons. Multiple Windows artifacts tag events using hostname instead of other identifiable information, like IP address. This is especially common when analyzing Windows event logs. Documenting the computer name is also one of DF's best practices since it is one way to establish that you are examining the correct system. This information is located within the following registry key.

```
SYSTEM\CurrentContolSet\Control\ComputerName\ComputerName
```

|  |
| --- |
| [![Computer Name](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEifrMvf1sHY7X5THfmOHXAlF5CAfwby4rqMHOPcUncRBdH4bbnVr4ItX83hkTGq5rF9Trc_GMZfxzIfzgXabc9CJ3ZZcHN8PtzCHSQHPSl7GFi9DcNXX5k97PD-YWEC_QDvVSnnnQZ-WafcwpUDn_qTgzcL6KfbQ-Cw3DyoD0jp7niJWDFYgl7bsT_1dWA/w620-h479/computername.png "Computer Name")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEifrMvf1sHY7X5THfmOHXAlF5CAfwby4rqMHOPcUncRBdH4bbnVr4ItX83hkTGq5rF9Trc_GMZfxzIfzgXabc9CJ3ZZcHN8PtzCHSQHPSl7GFi9DcNXX5k97PD-YWEC_QDvVSnnnQZ-WafcwpUDn_qTgzcL6KfbQ-Cw3DyoD0jp7niJWDFYgl7bsT_1dWA/s637/computername.png) |
| Figure 1: Computer Name |

The best location to commence a USB device audit is the `SYSTEM\CurrentControlSet\Enum\USB` key. This key tracks devices across a range of device classes, including USBSTOR, UASP, MTP, PTP, and HID. It gives a great overview of previously connected devices that could be of investigative value. This key is present in Windows XP and later versions. The USB key provides the following information:

- Device type (USBSTOR, UASP, HID, MTP, etc.)
- Vendor ID
- Product ID
- Device iSerialNumber
- ParentIdPrefix (UASP devices)

A computer system used frequently may have a very long list of previously connected USB devices, in which case, examining individual subkeys under the `SYSTEM\CurrentControlSet\Enum\USB` key may be tedious for the investigator. The Registry Explorer tool by Eric Zimmerman has a Plugin to extract information of interest from the key and present it in tabular form, as shown in the image below. Note that the timestamp reported by this plugin is the last write time of the VID/PID registry key and may not accurately represent when the device was last used.

|  |
| --- |
| [![USB registry key](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgGQcI8TJMVSVczwJn4yF2WmezQ5jb5x0Fd7yKmCJ3b1n0KMtLezLtZDoCO9xsDQkeqZ3vhTWDIhecV0JFhsXvWfOj7bsf8JGueo5YC5U9fzxF59-MjDzlBVFvZURaty4TvARBw6g9x2bkoRqk0LtHGnAUXsQ-b7UQRe2Sp2u9Ckf-JsQRbH077J4-cFPo/w655-h369/USB%20key.png "USB registry key")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgGQcI8TJMVSVczwJn4yF2WmezQ5jb5x0Fd7yKmCJ3b1n0KMtLezLtZDoCO9xsDQkeqZ3vhTWDIhecV0JFhsXvWfOj7bsf8JGueo5YC5U9fzxF59-MjDzlBVFvZURaty4TvARBw6g9x2bkoRqk0LtHGnAUXsQ-b7UQRe2Sp2u9Ckf-JsQRbH077J4-cFPo/s916/USB%20key.png) |
| Figure 2: The USB registry key |

It is important to note that a complete system USB device history stored in this key may not be obtained due to a not-so-often data clean-up by the operating system following major OS updates.

Since this is a data exfiltration case (involving the transfer of confidential files via a USB device medium), it is logical to conclude that the USB device that falls within the radar of my investigation is a USB Mass Storage Class (MSC) device. The two major USB protocols used in the USB Mass Storage Class devices are

* **Bulk-Only Transport** (**BOT**): This is the most widely used protocol for USB MSC devices. It uses bulk transfer mode for sending commands and data between the host and the device. It is common in USB flash drives and older external hard drives. It is simpler but generally less efficient. BOT devices are recorded in the `SYSTEM\CurrentControlSet\Enum\USBSTOR` registry key.
* **USB Attached SCSI Protocol** (**UASP**): This is a newer and faster protocol introduced with USB 3.0. It uses SCSI commands over USB and supports **command queuing** and **out-of-order processing**. It improves performance, especially for solid-state drives (SSDs) and high-speed external drives. UASP devices are recorded in the `SYSTEM\CurrentControlSet\Enum\SCSI` registry key.

If you have previously audited a suspect system for USB artifacts, you would have likely focused only on the USBSTOR registry key. In modern systems, this focus can lead to missing important devices. With the introductio...