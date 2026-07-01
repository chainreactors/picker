---
title: NTFS Forensics Detecting Timestamp Manipulation
url: https://digitalinvestigator.blogspot.com/2026/06/ntfs-forensics-detecting-timestamp.html
source: Instapaper: Unread
date: 2026-06-30
fetch_date: 2026-07-01T06:24:36.524594
---

# NTFS Forensics Detecting Timestamp Manipulation

### Facebook SDK

* [Home](/)
* [whoami](https://digitalinvestigator.blogspot.com/p/trainingswebinars-attended.html?m=1)
* [Subscribe](https://blogspot.us14.list-manage.com/subscribe?u=f0561841d9ef7ca0687144c59&id=93ea8a701f)

[![Digital Investigator](https://blogger.googleusercontent.com/img/a/AVvXsEjCBXDAFtj3qeFsN0QARpauoOMU-9GGRJMhzK1L_edHwLn3gTy8NtKHApKnUjkKdWPgAEIcdSrosxULEGvjMszmWVhop1V0aiHOOEW8KeeKjSkfEk3bSEuXPRbuGgVQQJlHbfKNju9pNpyZOabgh-Oci700smDybZA3gHWWI5H2Mgy0h08GrB5-FiyV=s150)](https://digitalinvestigator.blogspot.com/)

* [Home](home-icon)
* [whoami](https://digitalinvestigator.blogspot.com/p/trainingswebinars-attended.html?m=1)
* [Subscribe](https://blogspot.us14.list-manage.com/subscribe?u=f0561841d9ef7ca0687144c59&id=93ea8a701f)

[Home](https://digitalinvestigator.blogspot.com/)[Hard Disks and File System Forensics](https://digitalinvestigator.blogspot.com/search/label/Hard%20Disks%20and%20File%20System%20Forensics)

# NTFS Forensics: Detecting Timestamp Manipulation

Joseph Moronwi
June 28, 2026
0

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjhL6HHrYv4gHgMlK3od8htCyP4E1wXA08Esurtp8eg3Yj1fC2fk8317CyRChb5mwFv4ft9bRaq5z0O_Ao8YwaKAqjluq-rhKxGTmGjl85sj-73UsKU4uVxZpC08rU5Rd96gh6XbSaE5xWnphBfJUU1wSzPqd0WpTfCUlV0TTn9z2_Ep_x6v9ekpawReHk/w651-h248/4.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjhL6HHrYv4gHgMlK3od8htCyP4E1wXA08Esurtp8eg3Yj1fC2fk8317CyRChb5mwFv4ft9bRaq5z0O_Ao8YwaKAqjluq-rhKxGTmGjl85sj-73UsKU4uVxZpC08rU5Rd96gh6XbSaE5xWnphBfJUU1wSzPqd0WpTfCUlV0TTn9z2_Ep_x6v9ekpawReHk/s670/4.png)

Timestamp modification on NTFS volumes may arise from both legitimate operational requirements and malicious intent. A representative legitimate use case involves modern cloud synchronization clients. Services such as Dropbox strive to preserve temporal fidelity across devices: the last-modified timestamp of a file should reflect the actual moment of user modification, regardless of when or where the file is subsequently synced.

When the Dropbox client (or similar) is installed on a new host and performs an initial synchronization, the operating system perceives the incoming files as newly created. By default, Windows assigns the current system time to all $STANDARD\_INFORMATION timestamps of newly created files. To maintain consistency with the authoritative metadata stored in the cloud, the client invokes Windows APIs (e.g., SetFileTime) to deliberately backdate the relevant timestamps—most commonly the modified time and, in some implementations, the Creation time as well—to align with the cloud-recorded last-modified value. The precise timestamps propagated vary by provider and client version, but the preservation of the Modified timestamp is nearly universal.

Conversely, malicious actors routinely manipulate timestamps to achieve concealment. The primary objective is to embed malware within the temporal “noise” of the file system, reducing the likelihood of detection during forensic timeline analysis. A canonical tactic involves placing trojanized binaries in high-trust directories such as C:\Windows\System32, renaming them to mimic legitimate system processes, and adjusting their timestamps to harmonize with surrounding legitimate files. This practice, widely known as **timestomping** (derived from the seminal tool “timestomp”), enhances blending and complicates anomaly detection.

Historically, offensive tools exhibited limitations that aided detection. Many operated with only second-level precision, lacking the 100-nanosecond granularity native to Windows FILETIME structures. Consequently, timestamps landing exactly on the second boundary (with zero sub-second components) represented a statistical outlier and a strong indicator of manual intervention. Another reliable artifact was the divergence between the $STANDARD\_INFORMATION and $FILE\_NAME Creation timestamps, since most early tools could only modify the user-accessible $SI set.

Contemporary timestomping utilities have evolved to counter these detection vectors. Advanced tools can designate a “reference” legitimate file and atomically copy its full complement of $SI and $FN timestamps (including 100-nanosecond precision) to the target. This technique largely neutralizes both sub-second anomaly detection and cross-attribute comparison methods, necessitating more sophisticated analytic approaches—such as statistical timestamp distribution analysis, correlation with USN Journal entries, prefetch artifacts, and behavioral context—to identify sophisticated timestamp forgery.

Detecting timestomping relies on either finding traces of the very act itself, or on finding inconsistencies introduced by the tampering. While previous research had focused on using timestamp rules to identify specific user actions, Xiaoqin Ding and Hengming Zou (2010) were the first to use these rules to identify timestamp manipulation using a set of conditions. For all file types, timestamps should satisfy conditions: $SI.M <=$SI.E, $SI.C<=$FN.C, $SI.C<=$SI.A. If any is false, the timestamps were probably tampered with anti-forensic tools. They were able to prove timestamp manipulation in an example case by comparing the values in the $FNA to the values in the $SIA and identifying inconsistencies. But some intra volume replacement may cause $SI.C>$FN.C or $SI.C>$SI.A and the corresponding $SI.E indicates the time of replacement. If $SI.E< $FN.E, the timestamps are unreliable.

If $SI.C<$FN.C and $FN.M=$FN.A=$FN.C=$FN.E, we can conclude that the file was moved from another volume and $FN.C is the last moving time. Meanwhile, the file has not been renamed or moved after being relocated to the current volume.

If the condition $FN.M=$FN.A=$FN.C=$FN.E is false, while $SI.C<$FN.C and $SI.E>$FN.E is true, the file is replaced by another file with the same name and type in the same volume, and this file is created after the creation of the file that has been replaced. If $FN.M=$FN.A=$FN.C=$FN.E is false, but $SI.C=$FN.C, then $FN.MACE is copied from the $SI.MACE before the last renaming or moving within the volume.

If $SI.C>$SI.M, then the contents and the summary property of the file have not been modified in the current volume; If $SI.C=$SI.M, the file have not been modified since its creation; If $SI.C<$SI.M, $SI.M is the last modification time of the content or summary property of the file in the current volume.

For office files, if $FN.M=$FN.A=$FN.E>$SI.C, then $FN.M is the last modification time of the file contents in the current volume. If $SI.E=$FN.M also holds, then no renaming or intra-volume move happened after the modification. If $SI.E>$SI.M, the $SI.E is the time of last renaming/intra-volume moving/general property modification. If $SI.M=$FN.M is not satisfied, the timestamps must be altered. If $SI.M=$SI.E>$SI.A>=$SI.C, the $SI.M is the time of last modification on general property of the file.

For .exe files, $SI.E time of the .exe file must be newer or equal than the other seven timestamps. If this is not true, then they are not reliable.

For directories,  the timestamps should satisfy $SI.M<=$SI.E, $SI.C=$FN.C, $SI.C<=$SI.A. If anyone is false, the timestamps are unreliable. If $SI.M=$SI.A=$SI.E>$SI.C, $SI.E indicates the last time of content change in the target directory. For each file or subdirectory, if its $SI.E times is the same as that of the parent directory, then this file or subdirectory is recently added or renamed. If no such file or subdirectory is found, then delete operations must have been performed within the directory.

Because timestomping tools and techniques are capable of altering all eight timestamps in the $MFT with nanosecond precision, none of the aforementioned rules can be utilized to identify timestamp manipulation (as long as an attacker followed the rules). This, therefore, compels an analyst to consider other detection methods.

In practice, digital forensic examiners must evaluate timestamp sets holistically, remaining cognizant...