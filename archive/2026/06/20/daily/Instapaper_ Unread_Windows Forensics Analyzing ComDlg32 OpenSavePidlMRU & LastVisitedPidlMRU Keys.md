---
title: Windows Forensics Analyzing ComDlg32 OpenSavePidlMRU & LastVisitedPidlMRU Keys
url: https://digitalinvestigator.blogspot.com/2026/06/windows-forensics-analyzing-comdlg32.html
source: Instapaper: Unread
date: 2026-06-20
fetch_date: 2026-06-21T06:50:21.692586
---

# Windows Forensics Analyzing ComDlg32 OpenSavePidlMRU & LastVisitedPidlMRU Keys

### Facebook SDK

* [Home](/)
* [whoami](https://digitalinvestigator.blogspot.com/p/trainingswebinars-attended.html?m=1)
* [Subscribe](https://blogspot.us14.list-manage.com/subscribe?u=f0561841d9ef7ca0687144c59&id=93ea8a701f)

[![Digital Investigator](https://blogger.googleusercontent.com/img/a/AVvXsEjCBXDAFtj3qeFsN0QARpauoOMU-9GGRJMhzK1L_edHwLn3gTy8NtKHApKnUjkKdWPgAEIcdSrosxULEGvjMszmWVhop1V0aiHOOEW8KeeKjSkfEk3bSEuXPRbuGgVQQJlHbfKNju9pNpyZOabgh-Oci700smDybZA3gHWWI5H2Mgy0h08GrB5-FiyV=s150)](https://digitalinvestigator.blogspot.com/)

* [Home](home-icon)
* [whoami](https://digitalinvestigator.blogspot.com/p/trainingswebinars-attended.html?m=1)
* [Subscribe](https://blogspot.us14.list-manage.com/subscribe?u=f0561841d9ef7ca0687144c59&id=93ea8a701f)

[Home](https://digitalinvestigator.blogspot.com/)[Windows Forensics](https://digitalinvestigator.blogspot.com/search/label/Windows%20Forensics)

# Windows Forensics: Analyzing ComDlg32 OpenSavePidlMRU & LastVisitedPidlMRU Keys

Joseph Moronwi
June 20, 2026
0

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgo_E7ouziqPabi6lvN8jEgIH21VAqZ5i5Neb9-wAPGsW7KT_PsX8Y4jYK2lMOFWXb9WafIZOZ7EyWOUIKoLQT1UrddpMMupGhNAWyFyRtMk2pg7bkMkGOCi7Xk7cYr83eQmzrGalPjJfg_XSIqjyMOKn0_X22oY8NmlkJkEJMmwVdTITZNy6UksfM0tdE/w654-h371/1.jpg)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgo_E7ouziqPabi6lvN8jEgIH21VAqZ5i5Neb9-wAPGsW7KT_PsX8Y4jYK2lMOFWXb9WafIZOZ7EyWOUIKoLQT1UrddpMMupGhNAWyFyRtMk2pg7bkMkGOCi7Xk7cYr83eQmzrGalPjJfg_XSIqjyMOKn0_X22oY8NmlkJkEJMmwVdTITZNy6UksfM0tdE/s867/1.jpg)

In digital forensic examinations of Windows systems, analysts frequently observe that applications that leverage the Common File Dialog interface persistently retain the most recent directory locations used for file open and save operations. These same dialogs routinely populate MRU (Most Recently Used) dropdown lists with filenames and full paths of previously accessed or created files, stratified by extension type. This valuable artifactual data is persisted within the Common Dialog registry keys under the user’s NTUSER.DAT hive.

Windows exposes a robust suite of shared system libraries to developers, most notably the Common Dialog Box Library. As documented by Microsoft, “The Common Dialog Box Library contains a set of dialog boxes for performing common application tasks, such as opening files, choosing color values, and printing documents. The common dialog boxes allow you to implement a consistent approach to your application’s user interface.” These registry entries are of particular forensic significance because they operate in a cross-application manner, capturing activity across a wide spectrum of software—including web browsers, productivity suites, encryption utilities, and countless third-party applications that invoke the standard Common Item Dialog or legacy Common Dialog APIs.

Owing to the pervasive adoption of these standardized dialog controls, investigators gain centralized visibility into substantial volumes of user activity that would otherwise be fragmented across disparate application-specific logs. Parsing these keys enables the recovery of full file paths for documents opened or saved by the subject user, the specific applications involved, and associated temporal metadata derived from shell item structures.

To extract this intelligence, examiners should target the following primary keys within the user’s NTUSER.DAT registry hive (applicable to Windows Vista and later versions):

* NTUSER\Software\Microsoft\Windows\CurrentVersion\Explorer\ComDlg32\OpenSavePidlMRU
* NTUSER\Software\Microsoft\Windows\CurrentVersion\Explorer\ComDlg32\LastVisitedPidlMRU
* NTUSER\Software\Microsoft\Windows\CurrentVersion\Explorer\ComDlg32\LastVisitedPidlMRULegacy

These values store binary PIDL (Pointer to ID List) data, which forensic tools decode into human-readable paths, application executables, and MRU ordering. Note that while highly effective, these artifacts are generated only by applications utilizing the common dialog framework; modern UWP/Store apps and those employing fully custom interfaces may bypass them, necessitating correlation with complementary sources such as ShellBags, RecentDocs, and UserAssist entries. Pre-Vista systems utilized the non-PIDL variants (OpenSaveMRU and LastVisitedMRU).

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjSPQE54nrI79PHkBmJaa_HZ1szWatlSiU5FwSHGuQny1YvkwM5yg5tuC7sTEUeymMgzqpG-WWGf2qcPveRPrSvMzbyxyYyxZ7xOqPQi5nuTHRO6w2AMvZzYB_5jY17RClFVKgr1103CofDFg6rTLE7hhBTQdCm3bLiniKZFL63xZmEbxZ55tievI_UsCE/w657-h373/1.jpg)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjSPQE54nrI79PHkBmJaa_HZ1szWatlSiU5FwSHGuQny1YvkwM5yg5tuC7sTEUeymMgzqpG-WWGf2qcPveRPrSvMzbyxyYyxZ7xOqPQi5nuTHRO6w2AMvZzYB_5jY17RClFVKgr1103CofDFg6rTLE7hhBTQdCm3bLiniKZFL63xZmEbxZ55tievI_UsCE/s867/1.jpg)

In this illustrative example, the Microsoft Office Excel application is shown invoking the standard Common File Dialog for a “Save As” operation. The dialog has automatically defaulted to the user’s This PC > Documents folder. This last-visited directory information is recorded in the LastVisitedPidlMRU key (and its legacy counterpart) within the user’s NTUSER.DAT hive. Forensic examiners value this artifact because it reflects the per-application “last used folder” memory maintained by the Common Dialog Box Library — a convenience feature that consistently returns the user to their preferred working directory for each application.

Additionally, the dropdown list beneath the “File name” field is dynamically populated from the OpenSavePidlMRU key. In this instance, the entries are exclusively .xlsx files, demonstrating that the Common Dialog MRU mechanisms maintain separate lists organized by file extension (with a wildcard \* subkey for unclassified types). Of significant forensic utility is the fact that these entries frequently contain fully qualified paths rather than simple filenames, enabling investigators to identify specific directories and folder structures the user has actively interacted with during file open and save operations.

When parsed, the binary PIDL structures within these keys can yield not only the complete file paths and MRU ordering but also linkage to the responsible application, providing a rich, cross-application chronology of document-related user activity that complements other Windows artifacts such as ShellBags, LNK files, and RecentDocs.

The **OpenSavePidlMRU** key (previously OpenSaveMRU in Windows XP) constitutes a rich forensic artifact that records detailed evidence of files opened or saved by the user through the Common File Dialog interface. Analogous to the RecentDocs key, it structures data according to file extension, resulting in potentially numerous subkeys—each corresponding to a distinct file type encountered during open or save operations. This organization holds considerable evidentiary value; for example, the presence of a ps1 subkey may indicate interaction with PowerShell scripts, a pst subkey can reveal engagement with email archives, and an exe subkey may document the execution or inspection of potentially malicious binaries. A notable exception is the wildcard \* subkey, which maintains the most recent twenty (20) files of any extension (including files with no extension) processed through common open/save dialogs.

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEidGe1AEjo6rqBE6OJ-x5AIJzERimWI5ZihA57A_afRUTGfHwQKXw0RPVDFydf7N_H2jfMJmcarpaqI7QFfZJj7n-4RDQCzAJY9hzxcCwj1vxpcVXILbXjL-2F5r7knaeBN9pE1kT8YJuFLpxySqyhIx4DBf2KfSwuB2tt_R-nsQg6SVvSLLs4s8Rpqk7U/w656-h317/2.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEidGe1AEjo6rqBE6OJ-x5AIJzERimWI5ZihA57A_afRUTGfHwQKXw0RPVDFydf7N_H2jfMJmcarpaqI7QFfZJj7n-4RDQCzAJY9hzxcCwj1vxpcVXILbXjL-2F5r7knaeBN9pE1kT8YJuFLpxySqyhIx4DBf2KfSwuB2tt_R-nsQg6SVvSLLs4s8Rpqk7U/s1167/2.png)

While manual traversal of each subkey is possible, it is inefficient. Registry Explorer’s dedicated “C...