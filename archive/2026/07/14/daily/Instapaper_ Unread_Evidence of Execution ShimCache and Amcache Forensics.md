---
title: Evidence of Execution ShimCache and Amcache Forensics
url: https://digitalinvestigator.blogspot.com/2026/07/evidence-of-execution-shimcache-and.html
source: Instapaper: Unread
date: 2026-07-14
fetch_date: 2026-07-15T04:49:52.881169
---

# Evidence of Execution ShimCache and Amcache Forensics

### Facebook SDK

* [Home](/)
* [whoami](https://digitalinvestigator.blogspot.com/p/trainingswebinars-attended.html?m=1)
* [Subscribe](https://blogspot.us14.list-manage.com/subscribe?u=f0561841d9ef7ca0687144c59&id=93ea8a701f)

[![Digital Investigator](https://blogger.googleusercontent.com/img/a/AVvXsEjCBXDAFtj3qeFsN0QARpauoOMU-9GGRJMhzK1L_edHwLn3gTy8NtKHApKnUjkKdWPgAEIcdSrosxULEGvjMszmWVhop1V0aiHOOEW8KeeKjSkfEk3bSEuXPRbuGgVQQJlHbfKNju9pNpyZOabgh-Oci700smDybZA3gHWWI5H2Mgy0h08GrB5-FiyV=s150)](https://digitalinvestigator.blogspot.com/)

* [Home](home-icon)
* [whoami](https://digitalinvestigator.blogspot.com/p/trainingswebinars-attended.html?m=1)
* [Subscribe](https://blogspot.us14.list-manage.com/subscribe?u=f0561841d9ef7ca0687144c59&id=93ea8a701f)

[Home](https://digitalinvestigator.blogspot.com/)[Windows Forensics](https://digitalinvestigator.blogspot.com/search/label/Windows%20Forensics)

# Evidence of Execution: ShimCache and Amcache Forensics

Joseph Moronwi
July 11, 2026
0

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEi4wvXl7CMB-CcwP0oIo27Q3bu3crw2Ed6gSuyggUTArvov7wpUMW3ubhHzth8Jfi-cbyi42UFVXgudqmLISXGgnnloxXiXFi56qpa3jbaZLc-K_MSk_CBKmHvLKyxpF01i905lbSu0f2bvxno0S5t7uwtujvq8x3B7YpNww2vDpjN3RmgbqwYHtj3Yqy0/w659-h247/5.jpg)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEi4wvXl7CMB-CcwP0oIo27Q3bu3crw2Ed6gSuyggUTArvov7wpUMW3ubhHzth8Jfi-cbyi42UFVXgudqmLISXGgnnloxXiXFi56qpa3jbaZLc-K_MSk_CBKmHvLKyxpF01i905lbSu0f2bvxno0S5t7uwtujvq8x3B7YpNww2vDpjN3RmgbqwYHtj3Yqy0/s1109/5.jpg)

In the high-stakes world of incident response and digital forensics, few artifacts provide as much immediate insight into an adversary’s actions as Windows application execution artifacts. When attackers breach a network, the tools they run — whether custom malware, living-off-the-land binaries, or post-exploitation frameworks — leave traces that can reveal their objectives, techniques, and timeline.

Among the most valuable and enduring of these artifacts are **ShimCache (AppCompatCache)** and **Amcache.hve**. Long trusted by veteran responders for rapid triage, these artifacts offer a lightweight yet remarkably persistent record of executable presence, file metadata, cryptographic hashes, and behavioral patterns. Despite schema changes across Windows versions and important interpretive caveats, they remain indispensable for modern threat hunting and compromise assessments.

In this comprehensive guide, we explore the inner workings of ShimCache and Amcache, their forensic strengths and limitations, optimal parsing strategies, and advanced analytical techniques that scale effectively across enterprise environments. Whether you are triaging a single compromised host or hunting across thousands of systems, mastering these artifacts will significantly enhance your ability to detect, understand, and respond to sophisticated intrusions.

# Application Compatibility: ShimCache

Microsoft’s Application Compatibility Cache (AppCompatCache), commonly referred to as ShimCache, forms a core component of the Windows Application Compatibility Infrastructure (shim infrastructure). Introduced with Windows XP, it facilitates the detection and application of compatibility shims—user-mode fixes that enable legacy binaries to invoke behaviors associated with prior operating system versions, thereby mitigating compatibility issues during program execution.

This subsystem is frequently engaged by end users via the Program Compatibility Troubleshooter (compatibility wizard) and maintains an internal database of hundreds of built-in shims (as enumerated in files such as sysmain.sdb). The cache itself serves as a lookup mechanism to determine whether a given executable requires shimming. Critically, from a digital forensics perspective, entries are populated in the cache upon program launch attempts—regardless of whether a shim is ultimately applied—and may also be inserted when executables are merely browsed via Explorer.exe (particularly on Windows Vista through 8.1).

Forensic artifacts derived from ShimCache typically include the executable’s full path, the $STANDARD\_INFORMATION last modification timestamp of the file at the time of cache insertion/update, and, depending on the OS version, additional metadata such as file size. On Windows XP 32-bit systems, entries further record file size and a last-update timestamp. Subsequent versions introduced execution flags (most reliable on pre-Windows 10 systems) and varying cache capacities (approximately 96 entries on XP 32-bit, up to 1,024 on modern Windows).

**Key caveats for forensic practitioners**: ShimCache constitutes strong evidence of file presence (or prior existence) on the system, including binaries executed from removable media or network paths. However, it does not record actual execution timestamps. The stored modification time reflects the file’s M-time at cache insertion rather than runtime. On Windows 10 and later, the artifact is best interpreted as evidence of presence rather than definitive proof of execution. Cache data resides in memory and is persisted to the registry (in the SYSTEM hive) only upon proper system shutdown or reboot, potentially resulting in the absence of the most recent entries in live or abruptly terminated systems. The cache operates as a rolling buffer, with older entries overwritten as new ones are added.

This artifact remains a high-value, relatively persistent source for reconstructing application execution history in incident response and forensic timelines, particularly when correlated with AmCache, Prefetch, or other execution artifacts. AppCompatCache (ShimCache) is persisted within the SYSTEM registry hive under the following paths, with implementation details and capacity varying by operating system version:

### Windows 7 and Later (including Windows 8/8.1/10/11 and Server 2008–2022)

* **Primary Registry Path**: SYSTEM\CurrentControlSet\Control\Session Manager\AppCompatCache\AppCompatCache
* **Maximum Entries**: 1,024 (rolling buffer; oldest entries are overwritten as new ones are added)
* **Notable Metadata**: Includes an InsertFlag (or execution flag) in certain versions (most informative on Windows 7–8.1/Server 2012 R2), which provides **partial indication of execution** but is **not definitive**, particularly on Windows 10 and newer, where the artifact is best regarded as evidence of file presence rather than conclusive proof of execution.

### Windows XP (32-bit)

* **Registry Path**: SYSTEM\CurrentControlSet\Control\Session Manager\AppCompatibility\AppCompatCache
* **Maximum Entries**: Limited to 96
* **Additional Metadata**: Includes file size and last-update timestamp alongside the full path and $STANDARD\_INFORMATION last modification time

### Windows Server 2003 (and XP 64-bit)

* Up to **512 entries**
* Path generally aligns with the post-XP structure (AppCompatCache\AppCompatCache)

**Forensic Note**: The cache is maintained in kernel/memory during runtime and flushed to the registry only upon clean system shutdown or reboot. Analysts should examine historical ControlSets when possible and cross-reference with memory artifacts (e.g., via Volatility) for more recent activity. Entry ordering can support relative timeline construction, though absolute execution times are not recorded.

When parsing and interpreting AppCompatCache (ShimCache) output, forensic examiners should consider the following operational characteristics and limitations:

1. **Entry Ordering**: On modern Windows versions lacking explicit execution timestamps, the most recent entries appear at the top of the cache (reflecting the rolling insertion order).
2. **Persistence Mechanics**: New entries are committed to the registry **only upon system shutdown or reboot**. In Windows 10 and later, a reboot reliably flushes the in-memory cache. Consequently, executables processed or identified since the last clean shutdown/reboot exist solely in volatile memory and will be absent from the on-disk...