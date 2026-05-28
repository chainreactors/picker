---
title: ShellBags Forensics Practical Casework Considerations
url: https://digitalinvestigator.blogspot.com/2026/05/shellbags-forensics-practical-casework.html
source: Instapaper: Unread
date: 2026-05-27
fetch_date: 2026-05-28T06:03:57.034179
---

# ShellBags Forensics Practical Casework Considerations

### Facebook SDK

* [Home](/)
* [whoami](https://digitalinvestigator.blogspot.com/p/trainingswebinars-attended.html?m=1)
* [Subscribe](https://blogspot.us14.list-manage.com/subscribe?u=f0561841d9ef7ca0687144c59&id=93ea8a701f)

[![Digital Investigator](https://blogger.googleusercontent.com/img/a/AVvXsEjCBXDAFtj3qeFsN0QARpauoOMU-9GGRJMhzK1L_edHwLn3gTy8NtKHApKnUjkKdWPgAEIcdSrosxULEGvjMszmWVhop1V0aiHOOEW8KeeKjSkfEk3bSEuXPRbuGgVQQJlHbfKNju9pNpyZOabgh-Oci700smDybZA3gHWWI5H2Mgy0h08GrB5-FiyV=s150)](https://digitalinvestigator.blogspot.com/)

* [Home](home-icon)
* [whoami](https://digitalinvestigator.blogspot.com/p/trainingswebinars-attended.html?m=1)
* [Subscribe](https://blogspot.us14.list-manage.com/subscribe?u=f0561841d9ef7ca0687144c59&id=93ea8a701f)

[Home](https://digitalinvestigator.blogspot.com/)[Windows Forensics](https://digitalinvestigator.blogspot.com/search/label/Windows%20Forensics)

# ShellBags Forensics: Practical Casework Considerations

Joseph Moronwi
May 26, 2026
0

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEh67w-kZs7mf0_iIvu1zVjVy1UTUKOTt9VM-dvG0735jbhid6KUNJn2xqR2rzNaY6kwLdxfw9xiJOYD1Xmv4AltNOj5GwaG9ptTIQWgsXTyCFOhfKvz1A4D_fORLqbnRoIZJ7tDoilQrGAvk2tpf-1O7RMizGm3NuzkF13wMsb2gEwQdPE1-kUo7J9kKBg/w564-h536/shellbags.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEh67w-kZs7mf0_iIvu1zVjVy1UTUKOTt9VM-dvG0735jbhid6KUNJn2xqR2rzNaY6kwLdxfw9xiJOYD1Xmv4AltNOj5GwaG9ptTIQWgsXTyCFOhfKvz1A4D_fORLqbnRoIZJ7tDoilQrGAvk2tpf-1O7RMizGm3NuzkF13wMsb2gEwQdPE1-kUo7J9kKBg/s485/shellbags.png)

ShellBags constitute Windows forensic artifacts that capture shell-mediated folder enumeration and associated view-state persistence. They are frequently misinterpreted in investigative contexts as definitive proof of directory access, user awareness of specific files, or demonstrable intent. Such attributions are not defensible when resting solely on ShellBags without substantial corroboration from complementary artifacts.

These structures are more accurately conceptualized as the Windows Shell’s mechanism for recording directories it has been explicitly instructed to render within a user’s namespace. This yields robust evidentiary value for establishing GUI-driven navigation patterns and exploratory behavior. However, their probative strength diminishes sharply when extrapolated beyond that scope. Interpretations extending to broader file system activity must be tempered by factors such as the nature of the interaction, the surrounding system environment, and the presence of supporting indicators from other sources.

ShellBags are instantiated as a consequence of the Windows Shell’s architectural imperative to maintain view-state persistence across folder enumerations. When a user profile engages with a directory via File Explorer or common shell namespace dialogs, the operating system records granular presentation metadata—including layout configuration, sorting criteria, and icon view parameters—to ensure subsequent shell-mediated access restores the prior visual context. Many unusual items are treated and tracked as folders in Windows, including Zip archives, mobile device systems, and control panel applets. Beginning in Windows 11 22H2, this list was greatly expanded with native support for nearly a dozen new archive formats, including 7-Zip, RAR, TAR, and Gzip archives. In DFIR practice, these registry-derived structures function as high-fidelity artifacts documenting folders that have been explicitly instantiated within the user’s shell namespace. This mechanism furnishes investigators with a critical evidentiary by-product: a persistent, user-contextualized record of shell-accessed directories, often surviving deletion of the underlying filesystem objects. Such artifacts frequently provide the sole corroboration of interaction with folders residing on removable media, network shares, or those subsequently purged from the volume.

Nevertheless, several intrinsic constraints must govern their interpretive application. Foremost, ShellBags are strictly scoped to shell-interface provenance. They chronicle only those directories enumerated through the graphical shell and its associated namespace extensions; they do not encompass command-line, API-level, or non-shell application filesystem interactions. This boundary renders them exceptionally probative for reconstructing GUI-driven navigation behaviors, while limiting their standalone utility in establishing broader file system access patterns without rigorous correlative analysis.

Second, the artifacts remain fundamentally folder-centric. They furnish no direct attribution regarding file-level operations—such as opening, execution, exfiltration, modification, or deletion—within the referenced directories. In investigative workflows, ShellBags serve best as directional intelligence, enabling targeted hypothesis testing and plausibility assessment rather than conclusive demonstration of specific file interactions.

Third, ShellBags constitute cumulative state artifacts rather than sequential event records. Although MRU ordering, LastWrite timestamps, and bag modifications may yield temporal inferences, the structure was not engineered to preserve a comprehensive chronological audit of shell engagements. Analysts must therefore exercise caution against over-extrapolation when deriving precise timelines from these artifacts.

These delimitations do not undermine the forensic reliability of ShellBags; they refine their proper evidentiary domain. When interpreted within these boundaries, ShellBags frequently emerge as among the most robust indicators of user exploration involving transient, deleted, or extrinsically located directory structures.

# Location of ShellBags

The storage location of ShellBags artifacts underwent a significant architectural transition beginning with Windows Vista. In Windows XP, these structures resided primarily within the NTUSER.dat registry hive. From Windows Vista onward, the preponderance of ShellBags data was relocated to the USRCLASS.dat hive, reflecting changes in shell namespace management. Nonetheless, limited residual artifacts persist in the NTUSER.dat hive, particularly entries pertaining to user desktop items and mapped network shares. Comprehensive forensic examination, therefore, necessitates review of both registry hives to ensure complete artifact recovery.

**ShellBags Locations – Windows 7 and Later:**

* NTUSER.DAT\Software\Microsoft\Windows\Shell\BagMRU
* NTUSER.DAT\Software\Microsoft\Windows\Shell\Bags
* USRCLASS.DAT\Local Settings\Software\Microsoft\Windows\Shell\BagMRU
* USRCLASS.DAT\Local Settings\Software\Microsoft\Windows\Shell\Bags

**ShellBags Locations – Windows XP:**

* NTUSER.DAT\Software\Microsoft\Windows\Shell\Bags
* NTUSER.DAT\Software\Microsoft\Windows\Shell\BagMRU
* NTUSER.DAT\Software\Microsoft\Windows\ShellNoRoam\Bags
* NTUSER.DAT\Software\Microsoft\Windows\ShellNoRoam\BagMRU
* NTUSER.DAT\Software\Microsoft\Windows\CurrentVersion\Explorer\StreamMRU

This delineation underscores the importance of version-specific registry parsing strategies in DFIR workflows to maximize recovery of shell navigation artifacts.

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjVjViIT-9xvI9yo4yAfPsqmAHWSsIMmuLFvGTq2MAlowR1zloY16yuSqNOusjNJ9TnYYGXoIzQ1dTn4tznZl3wCdGDuvd5JqwiWP0_BRyKbWvxAG_-eJpiUigUkqK-5wwbLi_w-xS2VJl3ywvC4YHnbJtNm5n895LUepecPgx0sUEKDt_WEOHtHDLutGw/w614-h582/shellbags.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjVjViIT-9xvI9yo4yAfPsqmAHWSsIMmuLFvGTq2MAlowR1zloY16yuSqNOusjNJ9TnYYGXoIzQ1dTn4tznZl3wCdGDuvd5JqwiWP0_BRyKbWvxAG_-eJpiUigUkqK-5wwbLi_w-xS2VJl3ywvC4YHnbJtNm5n895LUepecPgx0sUEKDt_WEOHtHDLutGw/s485/shellbags.png)

The two primary keys for this artifact are BagMRU and Bags. The Bags key preserves the granular view-state configurations applied by the user, encompassing parameters such as icon dimensions, column layouts, sorting criteria, and other display preferences. The presence of subs...