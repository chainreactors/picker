---
title: How the NTFS USN Journal Powers DFIR Investigations
url: https://andreafortuna.org/2025/09/06/usn-journal.html
source: Instapaper: Unread
date: 2025-09-12
fetch_date: 2025-10-02T20:03:37.845285
---

# How the NTFS USN Journal Powers DFIR Investigations

[Andrea Fortuna](/)
[ ]

[About](/about/)[Rss](/feed.xml)

# NTFS artefacts for investigators: Using USN Journal in digital forensics

Sep 6, 2025

## TL;DR

In digital forensics and incident response, uncovering hidden artefacts often makes the difference between a stalled investigation and a break-through. One such powerful yet under-appreciated artefact is the **[USN Journal](https://en.wikipedia.org/wiki/USN_Journal)** (Update Sequence Number Journal), an NTFS feature that quietly logs every change on a volume, and can be a **forensic goldmine**, especially when tackling anti-forensic techniques like timestomping.

![ntfs](/assets/2025/ntfs-file-system-structure.jpg)

The **USN Journal** should be part of every DFIR investigator’s toolkit. It offers **accurate, tamper-resistant logs**, enables detection of anti-forensic techniques, enriches timeline analysis, and even supports real-time monitoring. Whether you’re reconstructing a deleted file timeline or uncovering timestomping, leveraging the USN Journal can give you clarity where other artifacts fall short.

---

## What is the USN Journal?

The **USN Journal** is a change-logging mechanism built into NTFS volumes, first introduced with NTFS v3.0 (Windows 2000). Each NTFS volume with journaling enabled maintains a log file located in `\$Extend\$UsnJrnl`. This journal uses two alternate data streams:

* `\$J` — the main stream recording changes (file creations, deletions, metadata updates, etc.),
* `\$MAX` — a metadata summary about the journal itself ([Haboob DFIR – Advanced USN Journal Forensics](https://blog.haboob.sa/blog/advanced-usn-journal-forensics)).

Every record in the USN Journal includes:

* A 64-bit **USN identifier**
* The **filename**
* The **parent MFT (Master File Table) reference**
* A bit-flag **reason code** (e.g. file created, deleted, renamed, metadata changed)
* The **timestamp** of the change.

This means that **every file event** leaves a trace—even if the file itself is later deleted or timestomped—making it invaluable for timeline reconstruction and anti-forensic detection.

---

## Why is useful in DFIR

### 1. **Timeline reconstruction, even if files disappear**

Because the USN Journal logs each event sequentially and remains even if files are deleted, DFIR investigators can reconstruct event sequences that other artifacts (like file contents or event logs) may no longer reflect ([Velociraptor – The Windows USN Journal](https://docs.velociraptor.app/blog/2020/2020-11-13-the-windows-usn-journal-f0c55c9010e/)).

### 2. **Spotting timestomping techniques**

Attackers often use timestomping—altering a file’s MACB timestamps to cover tracks. However, the USN Journal records the **actual metadata change event**. For example, if a file’s timestamp is reverted to 1996, but the USN Journal shows a “BasicInfoChange” at the actual time of manipulation, that mismatch is a red flag ([Medium – Determining Time-Stomping Activities with USN Journal](https://medium.com/%40matchadonutforensics/determining-time-stomping-activities-with-usn-journal-usnjrnl-3c797c1dbf4a)).

### 3. **Extending prefetch insight**

Prefetch files store only the last eight execution timestamps of an application. But each prefetch file update leaves a record in the USN Journal (`.pf` gets updated). Correlating those can provide a **much more extensive execution history** ([Haboob DFIR – Advanced USN Journal Forensics](https://blog.haboob.sa/blog/advanced-usn-journal-forensics)).

### 4. **Reconstructing deleted file paths (“Journal Rewind”)**

Even when parent folders or MFT entries are overwritten, the USN Journal can enable **path reconstruction** by reading events in reverse and tracking parent-child relationships across time ([CyberCX – NTFS USNJrnl Rewind](https://cybercx.com.au/blog/ntfs-usnjrnl-rewind/)).

---

## Use Cases & Tools

### A) **Detecting timestomping**

A great walkthrough is provided in [*Determining Time-Stomping Activities with USN Journal*](https://medium.com/%40matchadonutforensics/determining-time-stomping-activities-with-usn-journal-usnjrnl-3c797c1dbf4a):

1. A dummy file, **MyStory.docx**, is created with normal timestamps.
2. A tool like **nTimestomp** changes the MACB timestamps to an arbitrary past date.
3. Using **MFTECmd**, the `\$J` stream is parsed along with the MFT to resolve file paths and analyze events.
4. The USN Journal reveals a **“BasicInfoChange”** at the actual time of timestomping, exposing the manipulation despite the altered timestamps visible in Explorer.

---

### B) **Tracking a fictional intrusion (e.g. Stuxnet Scenario)**

In the post [*Timeline Analysis using $USNJrnl (Living off the land Wipers – Stuxnet Case Study)*](https://4n6shetty.in/timeline_analysis_using_usnjrnl/), the author constructs a toy scenario:

* A hacker (dubbed “Jinmori”) uses **SDelete**, a wiper that renames a file multiple times (`AAA.AAA`, `BBB.BBB`, etc.), then deletes it.
* Analysts extract `\$USNJrnl:$J` and parse it with **MFTECmd**, merging with MFT entries and using Timeline Explorer.
* The USN entries show all file rename names, allowing investigators to piece together the entire timeline and link it to file wiping behavior.

---

### C) **Advanced forensic techniques and tools**

The **Haboob DFIR Team** in [*Advanced USN Journal Forensics*](https://blog.haboob.sa/blog/advanced-usn-journal-forensics) highlights several key techniques and limitations:

* Tools like **MFTECmd** and **UsnJrnl2Csv** help parse and convert `\$J` into actionable data.
* The USN Journal typically retains approximately **20 days** of changes on active volumes (check via `fsutil usn queryjournal C:`).
* Use cases include:
  + Retrieving evidence of deleted files.
  + Detecting timestomping via “BasicInfoChange” flags.
  + Enhancing prefetch artifact history by correlating `.pf` updates.

---

### D) **Automated live monitoring (Velociraptor)**

The [Velociraptor framework](https://docs.velociraptor.app/blog/2020/2020-11-13-the-windows-usn-journal-f0c55c9010e/) brings realtime power to USN Journal analysis:

* Its **parse\_usn()** plugin parses `\$J` directly to extract entries including path and change reasons.
* Its **watch\_usn()** plugin enables real-time monitoring, e.g., for detecting new file executions or tracking hash changes as soon as they appear.

This opens possibilities for proactive detection and automation during incidents.

---

## Key Takeaways

| Feature | Value in DFIR |
| --- | --- |
| USN Journal `\$J` stream | Records file system changes—even after deletion |
| Reason codes (e.g. BasicInfoChange) | Reveal timestamp manipulation |
| MFT correlation | Allows full-path resolution |
| Prefetch enhancement | Extends provenance beyond 8 runs |
| Journal rewind | Reconstructs file paths of deleted or overwritten entries |
| Velociraptor | Enables live monitoring and detection |

In essence, the **USN Journal is a powerful, persistent forensic log** residing at a level of the file system that most attackers overlook. It **tracks changes**, not just states, so it can reveal manipulation, even when presented data has been sanitized.

---

## Related Reads

* Check out my **[Some thoughts about NTFS filesystem](https://andreafortuna.org/2017/10/11/some-thoughts-about-ntfs-filesystem/)** post, where I explain NTFS metafiles, including `\$MFT`, `\$Extend`, and the concept behind journaling, and the post [MAC(b) times in Windows forensic analysis](https://andreafortuna.org/2017/10/06/macb-times-in-windows-forensic-analysis/), with some additional information about **timestomping**.

Please enable JavaScript to view the [comments powered by Disqus.](https://disqus.com/?ref_noscript)

## Andrea Fortuna

* Andrea Fortuna
* andrea@andreafortuna.org

* [andreafortuna](https://github.com/andreafortuna)
* [andreafortunaig](https://instagram.com/andreafortunaig)
* [andrea-fortuna](https://www.linkedin.com/in/andrea-fortuna)
* [andrea](https://social.privacytools.click/%40andrea)
* [andreafortun...