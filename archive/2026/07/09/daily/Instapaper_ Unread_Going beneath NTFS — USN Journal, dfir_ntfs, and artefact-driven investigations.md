---
title: Going beneath NTFS — USN Journal, dfir_ntfs, and artefact-driven investigations
url: https://andreafortuna.org/2026/07/06/ntfs-forensics-deep-dive/
source: Instapaper: Unread
date: 2026-07-09
fetch_date: 2026-07-10T06:00:02.461203
---

# Going beneath NTFS — USN Journal, dfir_ntfs, and artefact-driven investigations

[Andrea Fortuna](/)
[ ]

[About](/about/)[Search](/search/)

Tools

[DFIR Toolkit](https://dfir-toolkit.andreafortuna.org)
[OSINT Toolkit](https://osint-toolkit.andreafortuna.org)

# Going beneath NTFS: USN Journal, dfir\_ntfs, and artefact-driven investigations

Jul 6, 2026

by [Andrea Fortuna](/about/)

A skilled attacker who has spent any time studying forensics will know to modify file timestamps. Some will go further and delete their tools, clear event logs, and rename artefacts before exfiltrating or detonating. What most do not account for, because most training does not cover it carefully, is that NTFS keeps a layered audit trail spread across at least three separate structures, and cleaning one of them rarely touches the others.

![cover](/assets/2026/ntfs-forensics-deep-dive.jpg)

The **Master File Table**, the **USN Journal**, and the **$LogFile** each capture a different dimension of file system activity, at a different granularity and with different retention characteristics. When an analyst knows how to correlate all three, the story they tell is significantly harder to fully suppress than anything a single log or a timestamp suggests.

This article walks through that structure in practical terms: what each artefact contains, how to extract it, and where the intersections between them are most useful for investigations.

## In brief

* NTFS stores file metadata in at least two independent locations per file: **$STANDARD\_INFORMATION** and **$FILE\_NAME** inside the MFT. Attackers can modify one but not both through standard APIs.
* The **USN Journal** logs every file system change event sequentially, survives file deletion, and typically retains approximately 20 days of activity on an active volume.
* The **$LogFile** is a low-level transaction log that records redo/undo operations on NTFS metadata, providing independent evidence of when attributes were last written.
* **dfir\_ntfs** and **MFTECmd** are complementary tools: one gives you programmatic access to raw NTFS structures; the other gives you analyst-ready CSV output for timeline correlation.
* File carving remains useful when MFT metadata is corrupted or missing, but it is best treated as a last resort.
* Correlating all three artefact layers produces a more robust timeline than any single source can provide.

## The structure underneath the filesystem

Before getting into tooling, it helps to have a clear model of what NTFS actually stores about a file, because the forensic value of these artefacts only becomes obvious once you understand the redundancy involved.

Every file on an NTFS volume has at least one entry in the **Master File Table**, or **$MFT** ([earlier overview](https://andreafortuna.org/2017/10/11/some-thoughts-about-ntfs-filesystem/)). Each MFT entry is 1024 bytes and contains, among other things, two distinct sets of timestamps. The first set lives in the **$STANDARD\_INFORMATION** attribute: the four MACB timestamps (Modified, Accessed, Created, $MFT entry modified) that most tools and the Windows Explorer interface expose. The second set lives in the **$FILE\_NAME** attribute, which the NTFS kernel driver writes when the file is created and updates under a narrower set of circumstances. The critical forensic implication is that **$FILE\_NAME timestamps are written by the kernel and cannot be modified through standard Win32 APIs** like `SetFileTime`. Most timestomping tools only reach $STANDARD\_INFORMATION.

That asymmetry is the most reliable single indicator of timestamp manipulation available in NTFS forensics. A file where `$STANDARD_INFORMATION` Born is earlier than `$FILE_NAME` Born is, under normal filesystem operation, an impossibility. The kernel copies $SI values from $FN at creation time; any later backdating of $SI will diverge from the kernel-written $FN values. When you see that divergence, you are reading a contradiction in the metadata record, not making an inference.

The MFT also stores the file’s logical size, physical allocation, attribute list, and, for small files (typically under around 700 bytes), the file content itself as a **resident attribute** inside the MFT entry. This matters for carving: deleting a resident file does not free any cluster, it just marks the MFT entry as available for reuse. The content survives until the entry is overwritten.

## USN Journal: the filesystem’s event stream

The **USN Journal** (`\$Extend\$UsnJrnl`) is an NTFS feature that has been available since Windows 2000 ([dedicated post](https://andreafortuna.org/2025/09/06/usn-journal/)) and is enabled by default on modern Windows systems. Its primary stream, `$J`, records a sequential log of every file system change on the volume: file creates, renames, deletes, attribute changes, security descriptor updates, and more. Each record contains a 64-bit USN identifier, the filename, a parent MFT reference, a reason code bitmask (for example, `USN_REASON_FILE_CREATE`, `USN_REASON_RENAME_OLD_NAME`, `USN_REASON_BASIC_INFO_CHANGE`), and a timestamp.

The `$MAX` alternate data stream stores metadata about the journal itself, including the configured maximum size, which controls how far back the journal extends. On an active volume, this typically covers approximately 20 days of activity, though heavily active systems may retain significantly less. You can inspect this on a live system:
fsutil usn queryjournal C:

For DFIR purposes, the USN Journal is valuable because it tracks **changes** rather than static file states. A file that has been deleted, timestomped, or renamed still leaves records behind. Consider the case of a tool deployed by an attacker that was later cleaned up with **SDelete** or a similar secure deletion utility. SDelete’s characteristic behaviour is to rename the target file multiple times before deleting it (`AAA.AAA`, `BBB.BBB`, and so on), then issue the delete. Each rename operation generates a `RENAME_OLD_NAME` and `RENAME_NEW_NAME` record in the USN Journal, producing a distinctive signature that survives the deletion itself.

The timestomping detection case is equally clean. A `USN_REASON_BASIC_INFO_CHANGE` record at a specific timestamp, correlated with the $SI/$FN discrepancy in the MFT, gives you two independent sources converging on the same event. Adding a Prefetch file for the timestomping binary, if it executed, gives you a third.

To extract the `$J` stream from a forensic image, you need to bypass the filesystem layer, since Windows will not give you direct access to NTFS metadata files through normal file operations. Two approaches work well in practice.

Using **MFTECmd** (Eric Zimmerman’s tool):
MFTECmd.exe -f “E:\Evidence$J” –csv C:\output\ –csvf usn.csv

The resulting CSV includes `UpdateTimestamp`, `Name`, `FileAttributes`, `UpdateReasons`, `ParentEntryNumber`, and `ParentSequenceNumber`. To reconstruct full paths, you need to parse the $MFT alongside it and join on the parent MFT entry number:
MFTECmd.exe -f “E:\Evidence$MFT” –csv C:\output\ –csvf mft.csv

Load both in Timeline Explorer and join on `ParentEntryNumber`. From there, filtering on `USN_REASON_FILE_DELETE` within your incident window, or looking for `FILE_CREATE` followed by `FILE_DELETE` within 60 seconds, covers a large fraction of malicious tool deployment and cleanup patterns.

## dfir\_ntfs: going below the surface

**dfir\_ntfs**, the Python library developed by [Maxim Suhanov](https://github.com/msuhanov/dfir_ntfs) ([original post](https://andreafortuna.org/2021/06/05/dfir_ntfs-a-forensic-parser-for-ntfs-filesystems/)), targets a different use case than MFTECmd. Where MFTECmd is optimised for analyst-facing CSV output, dfir\_ntfs is a programmatic interface to raw NTFS internals. It parses `$MFT`, `$UsnJrnl:$J`, and `$LogFile` directly, can work against volume images and volume shadow copies, and exposes the underlying structures in Python objects rather than spreadsheet rows.

Installation is straightforward:

```
pip3 install https://github.com/msuh...