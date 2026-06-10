---
title: Evidence of Execution BAMDAM Forensics
url: https://digitalinvestigator.blogspot.com/2026/06/evidence-of-execution-bamdam-forensics.html
source: Instapaper: Unread
date: 2026-06-09
fetch_date: 2026-06-10T06:17:20.861526
---

# Evidence of Execution BAMDAM Forensics

### Facebook SDK

* [Home](/)
* [whoami](https://digitalinvestigator.blogspot.com/p/trainingswebinars-attended.html?m=1)
* [Subscribe](https://blogspot.us14.list-manage.com/subscribe?u=f0561841d9ef7ca0687144c59&id=93ea8a701f)

[![Digital Investigator](https://blogger.googleusercontent.com/img/a/AVvXsEjCBXDAFtj3qeFsN0QARpauoOMU-9GGRJMhzK1L_edHwLn3gTy8NtKHApKnUjkKdWPgAEIcdSrosxULEGvjMszmWVhop1V0aiHOOEW8KeeKjSkfEk3bSEuXPRbuGgVQQJlHbfKNju9pNpyZOabgh-Oci700smDybZA3gHWWI5H2Mgy0h08GrB5-FiyV=s150)](https://digitalinvestigator.blogspot.com/)

* [Home](home-icon)
* [whoami](https://digitalinvestigator.blogspot.com/p/trainingswebinars-attended.html?m=1)
* [Subscribe](https://blogspot.us14.list-manage.com/subscribe?u=f0561841d9ef7ca0687144c59&id=93ea8a701f)

[Home](https://digitalinvestigator.blogspot.com/)[Windows Forensics](https://digitalinvestigator.blogspot.com/search/label/Windows%20Forensics)

# Evidence of Execution: BAM/DAM Forensics

Joseph Moronwi
June 09, 2026
0

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEj2487hNcuaZdcoawtcjYkEw6YfVWzhSc2ClS8PhNmfAZ2eOxYxRLuHNJaBZT3wsEtXJCMd_C9cTzlcTN7YpaKvb4oU5cdad_zVECi6fzXmoKTIMqI1abtrb7KwJdZXyFkL5osTVoa8UUacpJYEKxJwvST-XjHsSMiS6Af9sXNqSp4JHz9iMGhl1oSdnXs/w654-h227/bam.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEj2487hNcuaZdcoawtcjYkEw6YfVWzhSc2ClS8PhNmfAZ2eOxYxRLuHNJaBZT3wsEtXJCMd_C9cTzlcTN7YpaKvb4oU5cdad_zVECi6fzXmoKTIMqI1abtrb7KwJdZXyFkL5osTVoa8UUacpJYEKxJwvST-XjHsSMiS6Af9sXNqSp4JHz9iMGhl1oSdnXs/s1149/bam.png)

The Background Activity Moderator (BAM) represents a key Windows execution artifact of significant forensic value, frequently examined in conjunction with the Desktop Activity Moderator (DAM) owing to their closely aligned telemetry and data structures.

BAM was first introduced in Windows 10 build 1709 (Fall Creators Update) and persists in the overwhelming majority of contemporary Windows 10 and Windows 11 deployments. Operating under user context, it records the full executable path along with the last execution timestamp, typically stored in FILETIME format. The primary registry location is `HKLM\SYSTEM\CurrentControlSet\Services\bam\State\UserSettings\{SID}`, with analogous structures for DAM.

Microsoft designates DAM as a core element of the Modern Standby (S0 Low-Power Idle) power management architecture. This framework enables the suspension and throttling of desktop application activity to extend battery life on compatible hardware while permitting background processes to maintain limited functionality—mirroring the behavior of mobile operating systems during screen-off states. Modern Standby support is hardware-dependent and is largely confined to ultra-portable laptops and tablet-class devices; it is unavailable or minimally implemented on many traditional desktop and workstation systems. Consequently, DAM population tends to be more robust on Modern Standby-capable platforms and may be sparse or absent on standard desktops.

Both BAM and DAM keys generate comparable execution metadata when active, furnishing digital forensics practitioners with reliable indicators of program activity. Registry updates are commonly flushed or synchronized during boot sequences or specific system events rather than in true real-time for every execution.

Empirical analysis by Maxim Suhanov has documented that BAM entries are subject to automated pruning after approximately seven days of inactivity. Windows Store (UWP/modern) applications are typically exempted from this routine cleanup operation and demonstrate substantially longer retention periods. Additional nuances include the purging of BAM records associated with deleted executables upon the subsequent system reboot. Importantly, no BAM entries are created for binaries executed from network shares or removable media, a limitation that examiners must account for during timeline reconstruction and artifact correlation.

These characteristics—combined with the retention policies, hardware dependencies, and environmental constraints—position BAM and DAM as valuable corroborative artifacts for establishing recent program execution. They are routinely cross-referenced with other execution evidence sources such as Prefetch, ShimCache, Amcache, and SRUM in comprehensive forensic examinations.

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgmq4bH6ue5KidbdP9vrbURfkfQwfyP8zHGBsLXTaMvUuovul-NY3N55s_9HY4a17MRDtg7CWBhJXnOSqSK7T0qWWUsrU9C8_sVvRu9bFNECjbLWnoEg8ljdjTJsd0my2Ai2gS4V5AUwASmyQOnqt02Z_TwtCBkmo9fgQwI29YU7Gc3yvV4uPDFW_iHlWc/w659-h228/bam.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgmq4bH6ue5KidbdP9vrbURfkfQwfyP8zHGBsLXTaMvUuovul-NY3N55s_9HY4a17MRDtg7CWBhJXnOSqSK7T0qWWUsrU9C8_sVvRu9bFNECjbLWnoEg8ljdjTJsd0my2Ai2gS4V5AUwASmyQOnqt02Z_TwtCBkmo9fgQwI29YU7Gc3yvV4uPDFW_iHlWc/s1149/bam.png)

In the above, the Background Activity Moderator (BAM) key yields compelling evidence of program execution. Registry Explorer (or equivalent hive analysis tools) surfaces the full executable paths alongside the last execution timestamps for each entry, with temporal data stored as 64-bit Windows FILETIME values within the respective value data. Observed artifacts include executed applications such as Windows Explorer, Microsoft Word, Microsoft Excel, Microsoft PowerPoint, WinRAR, and Kape.

It is noteworthy that, although the BAM and DAM keys reside within the Windows System registry hive, the underlying data is scoped to individual user profiles through the associated Security Identifier (SID). Forensic researchers have documented temporal discrepancies in these timestamps, which may deviate by up to several minutes from actual execution events. Consistent with best practices in digital forensics, findings derived from BAM/DAM should be systematically cross-referenced against complementary execution artifacts—such as Prefetch, UserAssist, ShimCache, Amcache, and SRUM—to construct a more accurate, corroborated timeline of activity.

# **Why Are BAM/DAM Important in Digital Forensics?**

1. **Persistence After Deletion**: BAM can preserve evidence of program execution even after an application has been deleted from the system. However, entries associated with deleted executables are typically purged during the subsequent system reboot (in addition to the standard ~7-day inactivity cleanup).
2. **Malware and Suspicious Execution Tracking**: BAM/DAM entries can provide valuable evidence of when and where a binary was executed (full path + last execution timestamp). This is particularly useful for identifying malware or unauthorized tools. **Important limitation**: No entries are created for executables running from removable media (e.g., USB drives) or network shares.
3. **User Activity Reconstruction**: Analysts can leverage these artifacts to determine which programs were executed under a specific user context (via SID), when they were last run, and to identify potentially unauthorized or anomalous applications. While BAM primarily tracks execution rather than direct user interaction (e.g., GUI clicks), it serves as a strong indicator of program usage, especially when correlated with artifacts like UserAssist, Prefetch, or SRUM.

## **Additional Context for Forensic Practitioners**

* Retention is generally limited to approximately seven days of inactivity for most entries, though UWP/Modern apps are often exempted and persist longer.
* Data is user-specific (tied to SIDs) despite residing in the System hive.
* Timestamp accuracy may vary by several minutes from actual execution events.
* Always corroborate BAM/DAM findings with complementary execution artifacts for a defensible timeline.

This makes BAM/DAM a high-value, quick-reference artifact for recent execution history in Windows 10/11 investigations.

Tags
[Windows Forensics](https://digitalinvestigator.blogspot.com/search/label/Windows%20Forensics)

* Share

### [Joseph Moronwi](https://www.blogger.com/profile/16921333364875033449)

DFIR and Adv...