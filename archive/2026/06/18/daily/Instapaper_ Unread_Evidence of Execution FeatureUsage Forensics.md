---
title: Evidence of Execution FeatureUsage Forensics
url: https://digitalinvestigator.blogspot.com/2026/06/evidence-of-execution-featureusage.html
source: Instapaper: Unread
date: 2026-06-18
fetch_date: 2026-06-19T07:09:21.392662
---

# Evidence of Execution FeatureUsage Forensics

### Facebook SDK

* [Home](/)
* [whoami](https://digitalinvestigator.blogspot.com/p/trainingswebinars-attended.html?m=1)
* [Subscribe](https://blogspot.us14.list-manage.com/subscribe?u=f0561841d9ef7ca0687144c59&id=93ea8a701f)

[![Digital Investigator](https://blogger.googleusercontent.com/img/a/AVvXsEjCBXDAFtj3qeFsN0QARpauoOMU-9GGRJMhzK1L_edHwLn3gTy8NtKHApKnUjkKdWPgAEIcdSrosxULEGvjMszmWVhop1V0aiHOOEW8KeeKjSkfEk3bSEuXPRbuGgVQQJlHbfKNju9pNpyZOabgh-Oci700smDybZA3gHWWI5H2Mgy0h08GrB5-FiyV=s150)](https://digitalinvestigator.blogspot.com/)

* [Home](home-icon)
* [whoami](https://digitalinvestigator.blogspot.com/p/trainingswebinars-attended.html?m=1)
* [Subscribe](https://blogspot.us14.list-manage.com/subscribe?u=f0561841d9ef7ca0687144c59&id=93ea8a701f)

[Home](https://digitalinvestigator.blogspot.com/)[Windows Forensics](https://digitalinvestigator.blogspot.com/search/label/Windows%20Forensics)

# Evidence of Execution: FeatureUsage Forensics

Joseph Moronwi
June 12, 2026
0

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEg8RyGuxCQH20EAlimk5bLC9ZuOvtzDc0cOB2Ejaemj50vHKNkZiVsihlMTj7edw1d_agffMnfGTJK8EhSRoOHoJNDRoguQHX1AdGkmfe71VlH_cq5aQ8mo1pUhgBclAvnp1-NH3dN23LVg8N2olX46v420pPcQTHa065yEjzigl1EFjHnuW8SFoJ_GdHE/w641-h464/1-1.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEg8RyGuxCQH20EAlimk5bLC9ZuOvtzDc0cOB2Ejaemj50vHKNkZiVsihlMTj7edw1d_agffMnfGTJK8EhSRoOHoJNDRoguQHX1AdGkmfe71VlH_cq5aQ8mo1pUhgBclAvnp1-NH3dN23LVg8N2olX46v420pPcQTHa065yEjzigl1EFjHnuW8SFoJ_GdHE/s996/1-1.png)

**FeatureUsage** constitutes one of the most significant forensic artifacts identified in post-Windows 10 builds, having first appeared in build 1903. Initially publicly analyzed and reported by Jai Minton, this per-user registry key—located at `NTUSER.DAT\Software\Microsoft\Windows\CurrentVersion\Explorer\FeatureUsage`—provides high-granularity telemetry on both application execution and taskbar-centric user interactions that are largely unavailable through other conventional artifacts. Its subkeys deliver exceptionally detailed insights into user activity reconstruction, including:

* **AppLaunch**: Execution counts for applications, particularly those interacting with the taskbar or pinned shortcuts.
* **AppSwitched**: Frequency of focus switches, corresponding to user clicks on taskbar icons to foreground applications.
* **ShowJumpView**: Interactions with Jump Lists (right-click menu invocations on taskbar entries), revealing application knowledge and recent file access patterns.
* **TrayButtonClicked**: Direct clicks on various taskbar elements such as the system clock, Start button, Notification Center, and Search interface.
* **AppBadgeUpdated**: Badge (notification count) updates on taskbar icons.

Although these artifacts are not exhaustive—they predominantly capture GUI-oriented and taskbar-mediated activities and generally require an interactive logon session (console or RDP) for population—they afford investigators click-level visibility into user behavior that complements and corroborates other sources such as UserAssist, BAM, SRUM, and Jump Lists. Notably, the data exhibits strong persistence: entries are not purged upon application uninstallation, enabling the recovery of detailed usage telemetry for privacy tools, chat clients, VPN applications, and other items of interest long after the executables have been removed from the system. This combination of longevity, specificity, and uniqueness makes FeatureUsage a high-value registry artifact in timeline analysis and user activity reconstruction.

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhbvADWcjY8Kt1CmZ2xxIPc9pp1R5ASYxQGdZaEJaMW0xJvSxfooDhgdSYJEMEcSIWIpYwN4S4338fMM0DCwEFYGKLI2GbmekKK21p6Oo06cvI4S0B2Dc4sQ0ylo-c9vFWhpKtGx-h3LOnHmH17zB0JcsyV8ZGQ0bD1JFFle3pUiEaOEzii0tRUbpSI_H8/w654-h474/1-1.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhbvADWcjY8Kt1CmZ2xxIPc9pp1R5ASYxQGdZaEJaMW0xJvSxfooDhgdSYJEMEcSIWIpYwN4S4338fMM0DCwEFYGKLI2GbmekKK21p6Oo06cvI4S0B2Dc4sQ0ylo-c9vFWhpKtGx-h3LOnHmH17zB0JcsyV8ZGQ0bD1JFFle3pUiEaOEzii0tRUbpSI_H8/s996/1-1.png)

**AppLaunch** and **AppSwitched** represent the most probative subkeys within the FeatureUsage registry artifact for digital forensic examiners, offering complementary yet distinct perspectives on user-driven application interaction.

**AppLaunch** specifically enumerates execution counts for applications that have been pinned to the taskbar. Pinning inherently demonstrates deliberate user knowledge of, and intent toward, the application, as it requires an affirmative action to place and retain the shortcut on the taskbar for persistent access. Values within this subkey record the full executable path (frequently incorporating **KNOWNFOLDERID** GUIDs for well-known shell folders, consistent with UserAssist encoding) alongside a DWORD counter reflecting the total number of launches via the pinned shortcut. In the example above, you can see Windows Explorer appears to be the pinned application with the most executions (shortcut clicks). Critically, these entries exhibit strong persistence: records remain intact even after the application is unpinned or uninstalled, preserving evidence of historical usage. This enables identification of executables launched from anomalous or evasive paths (e.g., temporary directories, AppData subfolders, or non-standard locations), which is particularly valuable when correlating with malware persistence mechanisms or privacy tool deployment.

**AppSwitched**, by contrast, provides broader coverage, often encompassing the majority of GUI applications that have achieved foreground focus on the system. Untethered from pinning requirements, it tallies the number of times an application was brought into active focus—typically via left-clicking its taskbar icon—thereby indicating periods during which keyboard and mouse input were directed to that process. As a fundamentally graphical construct, it is limited to GUI applications and reliably captures installer wizards, setup executables, and other interactive binaries that require sustained user attention. In this example, it appears that NTFS Log Tracker v1.2.exe was by far the most in-focus application on the system. In investigative scenarios, elevated counts for tools such as credential-harvesting utilities or unauthorized applications can powerfully rebut claims of minimal knowledge or usage, furnishing quantitative evidence of deliberate, repeated engagement.

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEispzv-iwV548Rf8md3zUPV00yEZSBRi7SwaV5r_51ep1jTpXqvNXzlAFF0wZUAy5x09djgZazFrJO2opU9ur8C17YOGRCwHWEaQgy6-6egMol8hec2UkMkXZCIFbC69lnA2Bf_znw5ln5pfc-hi5Vp32cDkU5_LlPMZvn1UC1FOlXvmriu-Pm1enbUoGM/w654-h388/1-1-1.jpg)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEispzv-iwV548Rf8md3zUPV00yEZSBRi7SwaV5r_51ep1jTpXqvNXzlAFF0wZUAy5x09djgZazFrJO2opU9ur8C17YOGRCwHWEaQgy6-6egMol8hec2UkMkXZCIFbC69lnA2Bf_znw5ln5pfc-hi5Vp32cDkU5_LlPMZvn1UC1FOlXvmriu-Pm1enbUoGM/s859/1-1-1.jpg)

**AppBadgeUpdated** constitutes a supplementary yet uniquely valuable subkey within the **FeatureUsage** registry key, furnishing telemetry unavailable in other standard artifacts.

This subkey enumerates the cumulative number of badge (notification count) updates displayed on taskbar icons for individual applications. Taskbar badges—commonly observed as numeric overlays on application icons—serve as visual indicators of pending notifications, messages, or events. You can see an example of a WhatsApp icon with a badge showing 99+ new messages in the figure above. Looking at the AppBadgeUpdated values for that system, you can see a very active user with 13,191 total notifications to the user. While more prevalent in mobile ecosystems, they are prominently utilized by modern Windows desktop applications such as messaging clients (WhatsApp, Teams, Slack), email clients, and social media tools. In forensic examinations, a high aggregate count (such as 13,191 ...