---
title: Super Timeline Analysis with PlasoLog2timeline
url: https://digitalinvestigator.blogspot.com/2026/07/super-timeline-analysis-with.html
source: Instapaper: Unread
date: 2026-07-22
fetch_date: 2026-07-23T05:11:42.033848
---

# Super Timeline Analysis with PlasoLog2timeline

### Facebook SDK

* [Home](/)
* [whoami](https://digitalinvestigator.blogspot.com/p/trainingswebinars-attended.html?m=1)
* [Subscribe](https://blogspot.us14.list-manage.com/subscribe?u=f0561841d9ef7ca0687144c59&id=93ea8a701f)

[![Digital Investigator](https://blogger.googleusercontent.com/img/a/AVvXsEjCBXDAFtj3qeFsN0QARpauoOMU-9GGRJMhzK1L_edHwLn3gTy8NtKHApKnUjkKdWPgAEIcdSrosxULEGvjMszmWVhop1V0aiHOOEW8KeeKjSkfEk3bSEuXPRbuGgVQQJlHbfKNju9pNpyZOabgh-Oci700smDybZA3gHWWI5H2Mgy0h08GrB5-FiyV=s150)](https://digitalinvestigator.blogspot.com/)

* [Home](home-icon)
* [whoami](https://digitalinvestigator.blogspot.com/p/trainingswebinars-attended.html?m=1)
* [Subscribe](https://blogspot.us14.list-manage.com/subscribe?u=f0561841d9ef7ca0687144c59&id=93ea8a701f)

[Home](https://digitalinvestigator.blogspot.com/)[Hard Disks and File System Forensics](https://digitalinvestigator.blogspot.com/search/label/Hard%20Disks%20and%20File%20System%20Forensics)

# Super Timeline Analysis with Plaso/Log2timeline

Joseph Moronwi
July 22, 2026
0

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEj9Xc-kW7TpBWbOzJDOjhgO758S-2xjFW4bKJfJIq65NNEKAjxk4eyiwgQI-7dgp0PWXD-67NhSR6MR4KxCbqfWZykCEHguth97crdaO8FAigIAbaCuxHqrSdNs2rpgAE5SlePeKai44bSgyRNkAlIpzaovQ2hfvdEm91g9nUHQWgunjXWb6ICw1I7Ixys/w643-h344/plaso.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEj9Xc-kW7TpBWbOzJDOjhgO758S-2xjFW4bKJfJIq65NNEKAjxk4eyiwgQI-7dgp0PWXD-67NhSR6MR4KxCbqfWZykCEHguth97crdaO8FAigIAbaCuxHqrSdNs2rpgAE5SlePeKai44bSgyRNkAlIpzaovQ2hfvdEm91g9nUHQWgunjXWb6ICw1I7Ixys/s735/plaso.png)

Log2timeline was conceived by Kristinn Guðjónsson in conjunction with his GIAC Certified Forensic Analyst (GCFA) Gold Certification research at SANS. Inspired by discussions with SANS Faculty Fellow Rob Lee, who identified the operational necessity for aggregating disparate temporal data sources into a unified timeline artifact, Guðjónsson developed a modular framework capable of ingesting and normalizing a wide array of digital artifacts. The resulting tool surpassed initial expectations, emerging as a transformative contribution to the digital forensics community by enabling comprehensive super timeline construction—correlating filesystem metadata with application artifacts, registry entries, logs, and other evidential sources that had previously required disparate, labor-intensive parsing methods.

Guðjónsson’s project remains a cornerstone of forensic timeline analysis, providing investigators with a centralized reference for event reconstruction and temporal correlation across complex datasets. While not the sole utility for artifact parsing, it distinguishes itself through its breadth of supported parsers and its role as the de facto standard for super timeline generation. Development has been **continuous** and community-supported, with ongoing enhancements encouraged through contributions, issue reporting, or feature suggestions.

The original implementation was a Perl-based framework (log2timeline 0.x). Its successor is Plaso (Plaso Langar Að Safna Öllu—“Plaso wants to collect everything”), a robust Python-based backend engine that now underpins the toolset. In contemporary usage, the terms *"Plaso" and "log2timeline" (specifically "log2timeline.py")* are frequently employed interchangeably, with the latter serving as a primary frontend for storage file creation (e.g., .plaso repositories) that can subsequently be processed via tools such as psort.py. Analysts should utilize the current Plaso distribution for optimal performance, extensibility, and compatibility with modern forensic workflows.

# **Important Components of Plaso (log2timeline)**

**log2timeline.py**: This serves as the primary single-machine frontend to the Plaso backend engine. It is the core acquisition tool employed to recursively extract timestamped events from individual files, directories (including mount points), or full forensic images. The extracted events are consolidated into a structured Plaso storage file (.plaso), which functions as a centralized repository for subsequent examination and analysis.

**pinfo.py**: The Plaso storage file encapsulates comprehensive metadata regarding the collection process, including execution parameters, timestamps, source information, and any preprocessing artifacts applied during acquisition. The pinfo utility provides a straightforward mechanism to inspect and display this metadata, enabling analysts to validate the integrity, scope, and provenance of the stored data.

**psort.py**: This post-processing utility is responsible for filtering, sorting, tagging, and transforming the contents of a Plaso storage file into actionable output. It supports advanced operations such as time-based filtering, keyword searches, sessionization, and custom tagging. Because the native Plaso storage format is a binary/SQLite-based repository optimized for performance rather than direct human inspection, psort is typically required to generate human-readable exports (e.g., CSV, JSON, dynamic timelines) suitable for detailed forensic review and reporting.

These components form the foundational workflow for super timeline creation and analysis within the Plaso framework.

Plaso (Plaso Log2Timeline) is a digital forensic framework designed to automate the extraction, normalization, and correlation of timestamped artifacts from a wide range of forensic evidence sources. Originally developed to streamline timeline generation for Windows-based investigations, the framework has evolved to support numerous Windows, Linux, macOS, browser, cloud, and application-specific artifacts. Through targeted parser modules, it extracts and normalizes registry hive data; browser activity; shell-item artifacts (LNK files and jump lists); and execution evidence (Prefetch and Amcache), among other artifact classes—sources that frequently constitute the bulk of an investigator's evidentiary corpus during host-based analysis.

The principal strength of the framework lies in its robust normalization engine, which harmonizes disparate, heterogeneous data sources into a single, consistent chronological view. This unified super timeline significantly enhances an analyst’s ability to correlate events, identify behavioral patterns, and achieve rapid situational awareness regarding system activity.

### Windows Parsers

Plaso supports a comprehensive collection of parsers capable of extracting evidentiary metadata from numerous native and application-specific artifacts. Common Windows-relevant parsers include the following:

* **bencode**: Parses bencoded data files.
* **bencode\_transmission**: Parses Transmission bencoded files.
* **bencode\_utorrent**: Parses uTorrent bencoded files.
* **custom\_destinations**: Parses .customDestinations-ms Jump List files.
* **esedb**: Parses Extensible Storage Engine (ESE) database files.
* **filestat**: Extracts filesystem metadata and stat information.
* **hachoir**: Wrapper for the Hachoir binary file parser framework.
* **lnk**: Parses Windows Shortcut (LNK) files.
* **mcafee\_protection**: Parses McAfee AntiVirus Access Protection logs.
* **olecf\_document\_summary / olecf\_summary**: Parses OLE Compound File (OLECF) DocumentSummaryInformation and SummaryInformation streams.
* **onedrive\_log / skydrive\_log**: Parses OneDrive (formerly SkyDrive) log files.
* **onedrive\_log\_error / skydrive\_log\_error**: Parses OneDrive/SkyDrive error logs.
* **openxml**: Parses OpenXML (Office document) metadata.
* **pe**: Parses Portable Executable (PE) file metadata.
* **powershell\_transcript**: Parses PowerShell transcript events.
* **prefetch**: Parses Windows Prefetch files.
* **recycle\_bin**: Parses Windows Recycle Bin ($I) metadata.
* **sqlite**: Generic parser for SQLite database files.
* **symantec\_scanlog**: Parses Symantec AntiVirus scan logs.
* **winevt**: Parses legacy Windows Event Log (EVT) files.
* **winevtx**: Parses Windows XML Event Log (EVTX) files.
* **windefender\_history**: Parse...