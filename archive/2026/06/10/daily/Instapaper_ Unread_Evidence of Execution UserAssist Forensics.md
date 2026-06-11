---
title: Evidence of Execution UserAssist Forensics
url: https://digitalinvestigator.blogspot.com/2026/06/evidence-of-execution-userassist.html
source: Instapaper: Unread
date: 2026-06-10
fetch_date: 2026-06-11T06:36:58.667767
---

# Evidence of Execution UserAssist Forensics

### Facebook SDK

* [Home](/)
* [whoami](https://digitalinvestigator.blogspot.com/p/trainingswebinars-attended.html?m=1)
* [Subscribe](https://blogspot.us14.list-manage.com/subscribe?u=f0561841d9ef7ca0687144c59&id=93ea8a701f)

[![Digital Investigator](https://blogger.googleusercontent.com/img/a/AVvXsEjCBXDAFtj3qeFsN0QARpauoOMU-9GGRJMhzK1L_edHwLn3gTy8NtKHApKnUjkKdWPgAEIcdSrosxULEGvjMszmWVhop1V0aiHOOEW8KeeKjSkfEk3bSEuXPRbuGgVQQJlHbfKNju9pNpyZOabgh-Oci700smDybZA3gHWWI5H2Mgy0h08GrB5-FiyV=s150)](https://digitalinvestigator.blogspot.com/)

* [Home](home-icon)
* [whoami](https://digitalinvestigator.blogspot.com/p/trainingswebinars-attended.html?m=1)
* [Subscribe](https://blogspot.us14.list-manage.com/subscribe?u=f0561841d9ef7ca0687144c59&id=93ea8a701f)

[Home](https://digitalinvestigator.blogspot.com/)[Windows Forensics](https://digitalinvestigator.blogspot.com/search/label/Windows%20Forensics)

# Evidence of Execution: UserAssist Forensics

Joseph Moronwi
June 10, 2026
0

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjZcGBEmqpoyzqlolomOn6WYAvHpP1rbbU4RlcM7PIreke6DE3JYe7JQ-fZdRBeVmcnT4CNLh8Jv89s3tyDh5ff7JBuA8kZ6-VnerXKgKvvetmslzpcu3dS_pqfh7e0-X7Vb7peobNYf7zDsKnmzT0FNYU7XCVsZc1iK0FydgG_TgcDFiLrlGbKjFzjLiY/w655-h219/binary.jpg)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjZcGBEmqpoyzqlolomOn6WYAvHpP1rbbU4RlcM7PIreke6DE3JYe7JQ-fZdRBeVmcnT4CNLh8Jv89s3tyDh5ff7JBuA8kZ6-VnerXKgKvvetmslzpcu3dS_pqfh7e0-X7Vb7peobNYf7zDsKnmzT0FNYU7XCVsZc1iK0FydgG_TgcDFiLrlGbKjFzjLiY/s832/binary.jpg)

UserAssist constitutes one of the most intricate and information-dense registry artifacts encountered during forensic examination of Windows NTUSER.DAT hives. Its evidentiary value lies in the comprehensive telemetry it provides regarding graphical application execution—data that is frequently unavailable or fragmented across other artifacts. Resident within each user profile under the path `NTUSER.DAT\Software\Microsoft\Windows\CurrentVersion\Explorer\UserAssist` or, on a live computer system, at `HKCU\Software\Microsoft\Windows\CurrentVersion\Explorer\UserAssist`, this key enables investigators to reconstruct a detailed execution history for a specific user context, including:

* **Last Execution Timestamp** (UTC, stored as FILETIME)
* **Execution Count**
* **Application Name** (often with full path)
* **Focus Time**: Cumulative duration (in milliseconds) during which the application’s primary window maintained foreground focus on the desktop
* **Focus Count**: Total instances in which the application window attained active/foreground status

Originally implemented to dynamically populate the user’s Start menu with frequently accessed programs, UserAssist exclusively records interactions involving graphical user interface (GUI) applications. It does not capture command-line, background service, or console-based executions—gaps that must be addressed through complementary artifacts such as Prefetch files, ShimCache, Amcache, or SRUM data.

The artifact is organized beneath the UserAssist root key as multiple subkeys identified by **Globally Unique Identifiers (GUIDs)**. Each GUID corresponds to a distinct execution vector or shell integration mechanism. While numerous GUIDs may appear, most remain sparsely populated in typical environments, as users rarely invoke applications through esoteric pathways. Forensic examiners should nevertheless enumerate all subkeys, with priority given to the two predominant GUIDs that account for the overwhelming majority of high-fidelity execution records on Windows 7 and later systems:

* **CEBFF5CD-ACE2-4F4F-9178-9926F41749EA** — Primarily records direct executable launches (.exe files), including those initiated via shell extensions, the Start menu, Run dialog, and document-to-application associations (e.g., double-clicking a file that spawns wordpad.exe or similar handlers). This GUID provides broad coverage of interactive program execution.
* **F4E57C4B-2036-45F0-A9AB-443BCFE33D9F** — Dedicated to executions originating from Windows shortcut (.lnk) files. This encompasses user-created desktop shortcuts, pinned taskbar items, Start menu tiles, system tray invocations, and other shell-mediated launches.

Value names within these GUID subkeys are obfuscated using ROT13 encoding (this means any alphabetic character a-zA-Z is shifted over by 13 places, i.e., Z becomes M, A becomes N, etc.), while the associated binary data blobs contain structured execution metadata at predictable offsets. Data duplication across GUIDs is common, reflecting the same underlying execution event captured through different shell pathways. In advanced “pattern of life” analysis, differentiation between execution methods (e.g., direct .exe vs. shortcut) can help attribute activity to distinct user sessions or actors on a shared system.

In pre-Windows 7 implementations, UserAssist employed a significantly different and more transparent structure based on **UEME** (User Environment Monitoring Extension) prefixes. These legacy value names provided clearer insight into the precise execution vector compared to modern GUID-based subkeys. Common UEME categories included:

* **UEME\_UISCUT**: Tracks programs launched via desktop shortcuts.
* **UEME\_RUNCPL**: Records execution of Control Panel applets (.cpl files).
* **UEME\_RUNPATH**: Captures data about executed programs, often including full paths (e.g., UEME\_RUNPATH:C:\Windows\System32\cmd.exe after ROT13 decoding).
* **UEME\_RUNPIDL**: Logs executions involving PIDLs (Pointer to ID List), typically shell namespace objects.
* **UEME\_UITOOLBAR**: Monitors user clicks on Windows Explorer toolbar buttons.

This older format made it relatively straightforward for examiners to determine *how* an application was launched. For instance, the ROT13-decoded value name directly revealed both the execution method (via the UEME prefix) and the target path. Such granularity is largely lost in the binary blob structure introduced with Windows 7 and later. When analyzing XP or Vista systems, these UEME entries remain highly useful for reconstructing execution context. However, on modern Windows 10/11 systems, examiners should focus primarily on the two dominant GUIDs (CEBFF5CD... and F4E57C4B...) while recognizing that legacy-style UEME entries are no longer used. Understanding this evolution is critical when performing cross-version forensic comparisons or examining older compromised systems.

The structure and content of UserAssist underwent significant revisions between Windows XP, Vista, and Windows 7+. Post-Windows 7 implementations (including Windows 10/11) utilize an expanded binary format that incorporates the focus time and focus count metrics. For legacy systems, Didier Stevens’ seminal research, particularly “**[Windows 7 UserAssist Registry Keys](https://intotheboxes.wordpress.com/wp-content/uploads/2010/04/intotheboxes_2010_q1.pdf)**,” remains the authoritative reference for decoding earlier formats.

# **Binary Data Structure Evolution: Windows XP/Vista vs. Windows 7 and Later**

The most significant modification to UserAssist in Windows 7 was the introduction of an expanded binary data format. While XP/Vista entries used a compact 16-byte structure, Windows 7 and subsequent versions (including Windows 10/11) employ a 72-byte blob. This format has remained largely consistent across modern Windows releases.

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjcgJNQqu2poO83xfJsJ6PPuQsGl8nszK4JOlu4aduLT6XvZdMdF2SJt3TBPGvg5FyGMwjhMUi5ixuSS4x8n4faOnn9hQq0ITRcelihMFhRZRY9tnxSxXGPz9W0CgztPd-2yh0sdmfXbsCTvOonZneeVUAn4ypnJRQzsI3l6UV4GCJs8dVqUyh6zWnaW38/w658-h219/binary.jpg)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjcgJNQqu2poO83xfJsJ6PPuQsGl8nszK4JOlu4aduLT6XvZdMdF2SJt3TBPGvg5FyGMwjhMUi5ixuSS4x8n4faOnn9hQq0ITRcelihMFhRZRY9tnxSxXGPz9W0CgztPd-2yh0sdmfXbsCTvOonZneeVUAn4ypnJRQzsI3l6UV4GCJs8dVqUyh6zWnaW38/s832/binary.jpg)

The table below illustrates the structural differences....