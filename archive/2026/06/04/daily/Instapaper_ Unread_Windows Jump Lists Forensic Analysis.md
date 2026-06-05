---
title: Windows Jump Lists Forensic Analysis
url: https://digitalinvestigator.blogspot.com/2026/06/windows-jump-lists-forensic-analysis.html
source: Instapaper: Unread
date: 2026-06-04
fetch_date: 2026-06-05T06:14:39.218669
---

# Windows Jump Lists Forensic Analysis

### Facebook SDK

* [Home](/)
* [whoami](https://digitalinvestigator.blogspot.com/p/trainingswebinars-attended.html?m=1)
* [Subscribe](https://blogspot.us14.list-manage.com/subscribe?u=f0561841d9ef7ca0687144c59&id=93ea8a701f)

[![Digital Investigator](https://blogger.googleusercontent.com/img/a/AVvXsEjCBXDAFtj3qeFsN0QARpauoOMU-9GGRJMhzK1L_edHwLn3gTy8NtKHApKnUjkKdWPgAEIcdSrosxULEGvjMszmWVhop1V0aiHOOEW8KeeKjSkfEk3bSEuXPRbuGgVQQJlHbfKNju9pNpyZOabgh-Oci700smDybZA3gHWWI5H2Mgy0h08GrB5-FiyV=s150)](https://digitalinvestigator.blogspot.com/)

* [Home](home-icon)
* [whoami](https://digitalinvestigator.blogspot.com/p/trainingswebinars-attended.html?m=1)
* [Subscribe](https://blogspot.us14.list-manage.com/subscribe?u=f0561841d9ef7ca0687144c59&id=93ea8a701f)

[Home](https://digitalinvestigator.blogspot.com/)[Windows Forensics](https://digitalinvestigator.blogspot.com/search/label/Windows%20Forensics)

# Windows Jump Lists Forensic Analysis

Joseph Moronwi
June 04, 2026
0

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjADM6vSKgkhcE6HQzDCwQ77siL2RpePU9YAr-OnqGD-HI8aEgd-WiPXtva3zEqgs-t1kEPP4iRUOMag9dV2as24O_TH3egZXpcT9FKeki8hXVp7z3S22KyMpXfa1oRiSvMhsJt2WqQZf972ZjTlErMAP7JFOFD8LJUuHFDmk6HQlHyrRPChsSqxwpYrqU/w642-h192/Auto.jpg)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjADM6vSKgkhcE6HQzDCwQ77siL2RpePU9YAr-OnqGD-HI8aEgd-WiPXtva3zEqgs-t1kEPP4iRUOMag9dV2as24O_TH3egZXpcT9FKeki8hXVp7z3S22KyMpXfa1oRiSvMhsJt2WqQZf972ZjTlErMAP7JFOFD8LJUuHFDmk6HQlHyrRPChsSqxwpYrqU/s963/Auto.jpg)

Microsoft introduced Jump Lists in the Windows 7 desktop operating system as a mechanism to enhance user interaction efficiency by presenting dynamic lists of recently accessed files, directories, and application-specific tasks. These structures are instantiated across the majority of modern applications, affording rapid access to documents, web resources, Remote Desktop Protocol (RDP) connections, and contextual tasks such as initiating Incognito sessions, creating compressed archives, or launching virtual machines.

From a digital forensics perspective, the advent of Jump Lists represented a significant evolution in the recovery of user activity artifacts. Before their introduction, forensic examiners were largely reliant on Windows Registry keys—principally the Most Recently Used (MRU) and Most Frequently Used (MFU) entries—to reconstruct user behavior. In contrast, Jump List data files constitute substantially richer and more probative sources of evidentiary information. These artifacts enable the extraction of comprehensive metadata, including MRU and MFU sequences for both users and applications; full file paths; logical file names; Modified/Accessed/Created (MAC) timestamps; originating volume names and serial numbers; as well as unique volume and object identifiers. Notably, such records frequently persist in an intact state even after the deletion or removal of the associated files and hosting applications.

Jump Lists are maintained on a per-application basis through AutomaticDestinations and CustomDestinations files, each keyed by a unique Application ID (AppID). However, not all executables generate Jump Lists; native system utilities such as Regedit, Command Prompt, and the Run dialog, among others, typically do not produce these artifacts.

Forensically, Jump Lists represent an exceptionally robust repository for reconstructing user interaction history. While overlapping data may reside in artifacts such as the Registry’s RecentDocs key or LNK files within the Recent folder, Jump Lists frequently preserve significantly greater depth and temporal coverage. Each entry within a Jump List encapsulates a structured shell item equivalent to a full LNK file, thereby providing an extensive array of metadata identical to that recoverable from traditional shortcut files. Furthermore, consistent with LNK behavior, references to deleted, overwritten, or wiped items are not purged from Jump List records, creating a valuable forensic opportunity to identify historical artifacts long absent from the active filesystem. In high-volume usage scenarios, a single application may yield hundreds or even thousands of embedded LNK-equivalent entries.

By default, Jump Lists are enabled for all user accounts. They may be disabled via the Control Panel through **Personalization → Start → "Show recently opened items in Jump Lists on Start or the taskbar"**. Activation of this setting not only disables future population but also clears the contents of both Automatic and Custom Jump Lists, thereby impacting the preservation of potentially critical evidentiary material.

Windows Jump Lists are fundamentally composed of two distinct categories: **Destinations** and **Tasks**. These elements are primarily defined and implemented by the application developer, reflecting both user-specific activity and application-wide functionality.

In their default configuration, Jump Lists typically expose the most recently accessed or frequently used items (such as documents, media files, or other content) alongside standard tasks, including pinning the application to the taskbar, launching the executable, and closing all associated windows. Additional or customized functionality beyond these automatic entries is achieved through **Custom Jump Lists**, which allow developers to expose application-specific actions. As defined in the Windows Software Development Kit (SDK):

> "...*Destinations are items that appear in the Recent, Frequent, or custom categories, based on an individual’s usage. Destinations can be files, folders, websites, or other content-based items, but are not necessarily file-backed. Destinations can be thought of as things or nouns. Destinations can be pinned or removed from the Jump List by the user*."

> "...*Tasks are common actions performed in an application that apply to all users of that application regardless of an individual’s usage patterns. Tasks can be thought of as actions or verbs. Tasks cannot be pinned or removed*."

From a forensic standpoint, two primary Jump List structures facilitate this functionality:

* **AutomaticDestinations**: Generated automatically by the Windows operating system for each application based on user interaction patterns.
* **CustomDestinations**: Explicitly created and populated according to developer-defined logic and application-specific features.

Both Automatic and Custom Jump List files are stored within the user’s **Recent** folder (`C:\Users\<username>\AppData\Roaming\Microsoft\Windows\Recent\`), the same directory that houses traditional LNK shortcut files, under the subfolders `AutomaticDestinations` and `CustomDestinations`. Each file is identified by a unique Application Identifier (`AppID`). Automatic and Custom Jump Lists are stored in different formats and hence hold different information.

## Automatic Jump Lists

Automatic Jump Lists constitute the most forensically significant component of the Jump List ecosystem. They consistently yield a greater volume of entries, contain substantially richer metadata, and preserve a more comprehensive set of user activity artifacts compared to their Custom counterparts.

These files are stored in the Microsoft Object Linking and Embedding (OLE) Compound File Binary (CFB) format—also referred to as "Structured Storage"—and bear the .automaticDestinations-ms file extension. AutomaticDestinations files contain two primary categories of streams that are of critical importance to forensic examiners: **SHLLINK** streams and the **DestList** stream.

Multiple **SHLLINK** streams may exist within a single AutomaticDestinations file. Each of these streams mirrors the binary structure of a standard Windows Shortcut (LNK) file, encapsulating rich metadata such as full target paths, file sizes, MAC timestamps, volume serial numbers, and object identifiers. In contrast, the **DestList** stream possesses a specialized structure unique to Jump Lists. This stream is of particular forensic value be...