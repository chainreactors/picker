---
title: Exploring the macOS Native Commands Behind Andrea Lazzarotto’s Fuji
url: https://mreerie.com/2025/05/12/exploring-macos-native-commands-andrea-lazzarotto-fuji/
source: Instapaper: Unread
date: 2025-06-08
fetch_date: 2025-10-06T22:53:44.223896
---

# Exploring the macOS Native Commands Behind Andrea Lazzarotto’s Fuji

* [X](https://x.com/MrEerie)
* [Bluesky](https://bsky.app/profile/mreerie.bsky.social)
* [LinkedIn](https://www.linkedin.com/in/dc80/)

Search

[mr. eerie](https://mreerie.com)

“It looks like we’ve got ourselves a digital forensic mystery!”

* [Home](/)
* [About](https://mreerie.com/about/)
* [Merch](https://mreerie.com/merch/)

![](https://mreerie.com/wp-content/uploads/2025/05/a-photo-featuring-a-macos-computer-with-the-terminal-displayed-10.png?w=1024)

## Exploring the macOS Native Commands Behind Andrea Lazzarotto’s Fuji

Derek explores the macOS native commands used in Andrea Lazzarotto’s open-source project, Fuji.

[Derek Eiri](https://mreerie.com/author/derekeerie/)

2025-05-12

[dfir](https://mreerie.com/tag/dfir/), [digital forensics](https://mreerie.com/tag/digital-forensics/), [macos](https://mreerie.com/tag/macos/)

When Andrea Lazzarotto publicly released [Fuji (Forensic Unattended Juicy Imaging)](https://github.com/Lazza/Fuji), I was actively maturing internal corporate processes to respond to security incidents involving macOS machines. Having experimented with Fuji, it became part of our overall data collection strategy as it is repeatable, accessible and efficient. As of May 2025, Fuji offers three acquisition capabilities named after their respective macOS utilities: ASR, Rsync, and Sysdiagnose.

True to Lazzarotto’s goal, Fuji has a user-friendly interface that allows the examiner to logically acquire the entire drive or a single folder that is open source. A short video by [Richard Davis of 13Cubed](https://training.13cubed.com/) is likely all you need or want to get started with Fuji.

For additional insight about Fuji’s development and Lazzarotto’s work, his [interview with Forensic Focus](https://www.forensicfocus.com/interviews/andrea-lazzarotto-digital-forensics-consultant-and-developer/) and [SANS presentation](https://www.sans.org/presentations/fuji-a-new-open-source-tool-for-full-file-system-acquisition-of-mac-computers/) are enlightening. In Lazzarotto’s interview with Forensic Focus, his response on why open-source software is important should be on the minds of all examiners:

> The most important aspect, I believe, is the ability to understand what a tool does and the chance to ensure the process is repeatable.

Rather than summarize how to use Fuji, I’m taking on that quote as a call to action; this post explores how Fuji uses native macOS utilities to logically preserve data on Mac machines.

## Background

Despite administrator access to a fleet of corporate Macs, they are generally more hardened and requires a different process to collect data from compared to a machine running Windows. With the newest generation of Macs, acquiring a physical image, and decrypting it, hasn’t been possible; for several years at least. For modern Silicon Macs, we must rely on native capabilities to logically preserve data that exists on a synthesized container disk.

In SANS [FOR518](https://mreerie.com/2024/11/14/for518-mac-and-ios-forensic-analysis-and-incident-response-re-sans-for518-ondemand-experience/), and Sumuri’s MFSC-101 and MFSC-201, a handful of methods were discussed to acquire data logically. FOR518 touched on using Apple System Restore (***asr***) and Sumuri reviewed the use of ***rsync***.

```
sudo asr restore --source /dev/disk3s5 --target /dev/disk4 --debug --erase --verbose

OR

rsync -avE /directory-to-copy/ /Volumes/[destination]
```

Using either requires a destination using an Apple native image format to preserve [Apple Extended Attributes](https://eclecticlight.co/2024/09/12/from-quarantine-to-provenance-extended-attributes/) like an [Apple Disk Image](https://theapplewiki.com/wiki/Apple_Disk_Image) (.dmg) with extra space:

```
hdiutil create -fs apfs -size 500GB apple_evidence.dmg

THEN

sudo hdiutil attach -nomount apple_evidence.dmg
```

SANS FOR518 and Sumuri present methods in their respective courses to collect Unified Logs from macOS devices.

```
log collect

OR

log show > /Volumes/[destination]
```

FOR518 additionally covers the command ***sysdiagnose***, a LOOBin (Living Off the Orchard Binary), to collect other pattern of life data, which includes Unified Logs as part of that data dump.

```
sudo sysdiagnose
```

If a response or collection process is well-defined and practiced, these commands are relatively straight-forward. With a tool like Fuji, however, I am less likely to make a mistake i.e., miss-type a command, create a .dmg file with the wrong filesystem or make it too small for the collection.

## Logical Acquisitions with Fuji

In Fuji, Fuji.py contains the code related to the graphical user interface. Abstract.py, in summary, prepares the acquisition process for all methods Fuji is capable of. It defines the parameters to create a temporary image (sparse image), convert it to an Apple Disk Image (.dmg), keep the system from sleeping during acquisition, and saves pertinent information about the macOS machine in an acquisition report.

![](https://mreerie.com/wp-content/uploads/2025/05/hdituil_create-2.png)
![](https://mreerie.com/wp-content/uploads/2025/05/hdituil_convert.png?w=628)
![](https://mreerie.com/wp-content/uploads/2025/05/screenshot-2025-05-20-at-12.17.06e280afam.png)

The resulting files after a Fuji acquisition.

### Fuji Acquisition Method: ASR

Intended for restoring and cloning macOS systems, ***asr*** may be repurposed for preserving data from volumes in a forensically-sound manner. The caveat, however, is that ***asr*** does not capture .fsevents of the target Mac, which records “[historical file system activity over time](https://www.osdfcon.org/presentations/2017/Ibrahim-Understanding-MacOS-File-Ststem-Events-with-FSEvents-Parser.pdf)“. The .fsevents directory may be copied out or collected with the ***rsync*** command to preserve as much metadata as possible.

![](https://mreerie.com/wp-content/uploads/2025/05/asr.png?w=630)

In Fuji, asr.py establishes the parameters to prepare an Apple Software Restore including the acquisition report. It then issues the ***asr*** command to restore the root volume and saves it to the temporary image set up by Fuji. When the temporary image is erased and data begins to save data to the target, the prompt to confirm to erase its contents is ignored.

[![](https://mreerie.com/wp-content/uploads/2025/05/erase_contents_prompt.png?w=603)](https://mreerie.com/wp-content/uploads/2025/05/erase_contents_prompt.png)

The prompt to confirm erasure of the target before executing in absence of the –noprompt option.

[![](https://mreerie.com/wp-content/uploads/2025/05/starting_asr.png?w=788)](https://mreerie.com/wp-content/uploads/2025/05/starting_asr.png)

A logical aquisition in progress with ***asr***.

### Fuji Acquisition Method: Rsync

The ***rsync*** command was featured in Sumuri’s MFSC-101 and MFSC-201 class as a method to logically copy data from a live Mac and preserve Apple Extended Attributes. It may also be piped after the ***find*** command of certain files, then copy to a destination. Fuji explains that while ***rysnc*** is slower, it may be used on any source directory. The *.fsevents* directory is a perfect candidate for this method.

![](https://mreerie.com/wp-content/uploads/2025/05/rsync.png?w=629)

The rsync.py script prepares parameters to run the ***rsync*** command to only look within the partition, perform the task recursively, preserve as much metadata as possible, show progress of the transfer and exclude files with the goal of preventing duplicates of the same file.

[![](https://mreerie.com/wp-content/uploads/2025/05/fuji_rsync_fsevents-1.png?w=491)](https://mreerie.com/wp-content/uploads/2025/05/fuji_rsync_fsevents-1.png)

Using ***rsync*** via Fuji to capture the .fsevents directory for the Data volume.

[![](https://mreerie.com/wp-content/uploads/2025/05/fuji_fsevents.png?w=1024)](https://mreerie.com/wp-content/uploads/2025/05/fuji_fsevents.png)

The .fsevents folder here corresponds with events on the .dm...