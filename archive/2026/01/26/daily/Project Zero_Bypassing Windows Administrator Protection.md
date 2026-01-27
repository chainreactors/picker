---
title: Bypassing Windows Administrator Protection
url: https://projectzero.google/2026/26/windows-administrator-protection.html
source: Project Zero
date: 2026-01-26
fetch_date: 2026-01-27T03:39:39.435675
---

# Bypassing Windows Administrator Protection

[Project Zero](/)

---

[ ]

* [blog archive](/archive.html)
* [bug reports](https://project-zero.issues.chromium.org/savedsearches/7162405)
* [about](/about-pz.html)
* [Working at PZ](/working-at-project-zero.html)
* [0day: spreadsheet](/0day.html)
* [0day: Root Cause Analyses](https://googleprojectzero.github.io/0days-in-the-wild/rca.html)
* [vulnerability disclosure policy](/vulnerability-disclosure-policy.html)
* [reporting transparency](/reporting-transparency.html)
* search

# Bypassing Windows Administrator Protection

[2026-Jan-26](/2026/26/windows-administrator-protection.html "Permalink to this post")
James Forshaw

A headline feature introduced in the latest release of Windows 11, 25H2 is [Administrator Protection](https://blogs.windows.com/windowsdeveloper/2025/05/19/enhance-your-application-security-with-administrator-protection/). The goal of this feature is to replace User Account Control (UAC) with a more robust and importantly, securable system to allow a local user to access administrator privileges only when necessary.

This blog post will give a brief overview of the new feature, how it works and how itâs different from UAC. Iâll then describe some of the security research I undertook while it was in the insider preview builds on Windows 11. Finally Iâll detail one of the nine separate vulnerabilities that I found to bypass the feature to silently gain full administrator privileges. All the issues that I reported to Microsoft have been fixed, either prior to the feature being officially released (in optional update [KB5067036](https://support.microsoft.com/en-gb/topic/october-28-2025-kb5067036-os-builds-26200-7019-and-26100-7019-preview-ec3da7dc-63ba-4b1d-ac41-cf2494d2123a)) or as subsequent security bulletins.

*Note: As of 1st December 2025 the Administrator Protection feature has been disabled by Microsoft while an application compatibility issue is dealt with. The issue is unlikely to be related to anything described in this blog post so the analysis doesnât change.*

## The Problem Administration Protection is Trying to Solve

UAC was introduced in Windows Vista to facilitate granting a user administrator privileges temporarily, while the majority of the userâs processes run with limited privileges. Unfortunately, due to the way it was designed, it was quickly apparent it didnât represent a hard security boundary, and Microsoft downgraded it to a security feature. This was an important change as it made it no longer a priority to fix bypasses of the UAC which allowed a limited process to silently gain administrator privileges.

The main issue with the design of UAC was that both the limited user and the administrator user were the same account just with different sets of groups and privileges. This meant they shared profile resources such as the user directory and [registry hive](https://www.tiraniddo.dev/2017/05/exploiting-environment-variables-in.html). It was also possible to open an administrators processâ access token and [impersonate it](https://www.tiraniddo.dev/2017/05/reading-your-way-around-uac-part-1.html) to grant administrator privileges as the impersonation permission checks didnât originally consider if an access token was âelevatedâ or not, it just considered the user and the integrity level.

Even so, on Vista it wasnât that easy to silently acquire administrator privileges as most routes still showed a prompt to the user. Unfortunately, Microsoft decided to reduce the number of elevation prompts a user would see when modifying system configuration and introduced an âauto-elevationâ feature in Windows 7. Select Microsoft binaries could be opted in to be automatically elevated. However, it also meant that in some cases it was possible to repurpose the binaries to silently gain administrator privileges. It was possible to configure UAC to always show a prompt, but the default, which few people change, would allow the auto-elevation.

A good repository of known bypasses is the [UACMe](https://github.com/hfiref0x/UACME) tool which currently lists 81 separate techniques for gaining administrator privileges. A proportion of those have been fixed through major updates to the OS, even though Microsoft never officially acknowledges when a UAC bypass is fixed. However, there still exist silent bypasses that impact the latest version of Windows 11 that remain unfixed.

The fact that malware is regularly using known bypasses to gain administrator privileges is what Administrator Protection aims to solve. If the weaknesses in UAC can be mitigated then it can be made a secure boundary which not only requires more work to bypass but also any vulnerabilities in the implementation could be fixed as security issues.

In fact there is already a more secure mechanism that UAC can use that doesnât suffer from many of the problems of the so-called âadmin approvalâ elevation. This mechanism is used when the user is not a member of the administrators group, itâs referred to as âover-the-shoulderâ elevation. This mechanism requires a user to know the credentials of a local administrator user which must be input into the UAC elevation prompt. Itâs more secure than admin approval elevation for the following reasons:

* The profile data is no longer shared, which prevents the limited user from modifying files or registry keys which might be used by an elevated administrator process.
* Itâs no longer possible to get an access token for the administrator user and impersonate it as limited users cannot impersonate other user accounts.
* Auto-elevation of Microsoft binaries is not supported, all elevation requests require confirmation through a prompt.

Unfortunately, the mechanism is difficult to use securely in practice as sharing the credentials to another local administrator account would be a big risk. Thus itâs primarily useful as a means for technical support where a sysadmin types in the credentials over the userâs shoulder.

Administrator Protection improves on over-the-shoulder elevation by using a separate shadow administrator account that is automatically configured by the UAC service. This has all the benefits of over-the-shoulder elevation plus the following:

* The user does not need to know the credentials for the shadow administrator as there arenât any. Instead UAC can be configured to prompt for the limited userâs credentials, including using biometrics if desired.
* A separate local administrator account isnât required, only the user needs to be configured to be a member of the administrators group making deployment easier.

While Microsoft is referring to Administrator Protection as a separate feature it can really be considered a third UAC mechanism as it uses the same infrastructure and code to perform elevation, just with some tweaks. However, the feature replaces admin-approval mode so you canât use the âlegacyâ mode and Administrator Protection at the same time. If you want to enable it thereâs currently no UI to do so but you can [modify the local security policy](https://techcommunity.microsoft.com/blog/windows-itpro-blog/administrator-protection-on-windows-11/4303482) to do so.

The big question, will this make UAC a securable boundary so malware no longer has a free ride? I guess we better take a look and find out.

## Researching Administrator Protection

I typically avoid researching new Windows features before theyâre released. It hasnât been a good use of time in the past where Iâve found a security issue in a new feature during the insider preview stages only for that bug to be due to temporary code that is subsequently removed. Also if security issues are fixed in the insider preview stage they do not result in a security bulletin, making it harder to track when something is fixed. Therefore, thereâs little incentive to research features until they are released when I can be confident any bugs that are discovered are real security issue...