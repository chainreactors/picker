---
title: Android pattern of life hidden artifacts that reconstruct a user’s daily routine
url: https://andreafortuna.org/2026/04/23/android-pattern-of-life-hidden-artifacts-reconstruct-daily-routine/
source: Instapaper: Unread
date: 2026-04-24
fetch_date: 2026-04-25T04:38:29.574525
---

# Android pattern of life hidden artifacts that reconstruct a user’s daily routine

[Andrea Fortuna](/)
[ ]

[About](/about/)

Tools

[DFIR Toolkit](https://dfir-toolkit.andreafortuna.org)
[OSINT Toolkit](https://osint-toolkit.andreafortuna.org)

# Android pattern of life: hidden artifacts that reconstruct a user's daily routine

Apr 23, 2026

by [Andrea Fortuna](/about/)

When we talk about mobile forensics, the conversation often drifts toward flashy artifacts like chat messages, call logs, or photos. Those are important, of course. But there’s another category of evidence that doesn’t get nearly enough attention: the silent witnesses that reveal *how* someone uses their device, not just *what* they store on it.

![cover](/assets/2026/android-pattern-of-life-cover.jpg)

Think of pattern of life analysis as the difference between knowing someone owns a car and knowing they drive to work every morning at 8:15, stop at the same coffee shop, and rarely use the highway. On iOS, this kind of data is famously concentrated in `knowledgeC.db`, an artifact so well-documented that it’s become almost synonymous with iOS usage analysis. Accessing it requires full filesystem extraction, which is its own challenge, but at least investigators know where to look.

Android tells a different story. The platform’s usage tracking is distributed across multiple databases, each with its own schema, retention policy, and extraction requirements. There’s no single `knowledgeC.db` to rule them all. Instead, forensic analysts must piece together evidence from UsageStats, Digital Wellbeing, appops logs, and increasingly, device-specific systems like Samsung’s Rubin.

This fragmentation isn’t just a technical inconvenience. It creates real investigative risks. Relying on a single data source can lead to incomplete timelines, and on some devices, it can produce outright incorrect conclusions. The goal of this article isn’t to walk through acquisition methods I’ve covered elsewhere in my [mobile forensics overview](https://andreafortuna.org/2024/06/12/mobile-forensics-tools-and-techniques/), but to focus specifically on analyzing the pattern of life artifacts that Android leaves behind. If you’re working a case and need to reconstruct what a user did with their device, these are the databases you need to know.

## Android encryption, what matters for your investigation

Before diving into specific artifacts, we need to address the elephant in the room: Android’s encryption model determines whether you can even access these files in the first place.

Since Android 7.0, [File-Based Encryption (FBE)](https://source.android.com/docs/security/features/encryption/file-based) has been the standard. FBE separates storage into two distinct areas. Device Encrypted (DE) storage contains system files and data accessible immediately after boot, before any PIN or pattern is entered. Credential Encrypted (CE) storage holds everything else: user data, databases, app-specific files. CE is only decrypted after the user enters their credentials for the first time after boot.

This distinction matters enormously in practice. Files in DE storage, like `/data/system/` configuration files and certain system logs, are accessible without knowing the device PIN. But the databases that contain the richest usage information sit in CE storage. This means `usagestats/`, `dwbCommon.db`, `appops.xml`, and `telephony.db` all require what the industry calls AFU access (After First Unlock), a challenge that becomes even more complex with newer Android versions as I explored in my analysis of [Android 14 forensic challenges](https://andreafortuna.org/2024/08/15/digital-detectives-vs-android-14-overcoming-new-forensic-challenges/).

In real-world investigations, this creates a critical decision point. BFU (Before First Unlock) acquisitions capture only what’s in DE storage and can be severely limited. AFU acquisitions, where the examiner obtains the device after it’s been unlocked at least once, provide access to the CE storage where pattern of life data lives. As [Cellebrite’s documentation on FBE vs FDE](https://cellebrite.com/en/series/tip-tuesday/fbe-vs-fde-and-how-they-impact-android-device-data-collection/) explains, the choice between these acquisition strategies directly determines which artifacts you’ll be able to analyze.

If you’re acquiring an Android device, understanding FBE isn’t optional. It’s the foundation that determines whether your investigation will have access to the usage data you need or whether you’ll be working with an incomplete picture.

## UsageStats and what it reveals about app usage

The heart of Android pattern of life analysis lives in the UsageStats system. This is a directory, typically found at `/data/system/usagestats/`, that Android populates with granular data about application usage.

Every time an app moves to the foreground or background, UsageStats records it with millisecond-precision timestamps. The system tracks when each app was opened, how long it remained active, and aggregates this data into time buckets: daily, weekly, monthly, and yearly summaries. Even after an application is uninstalled, residual traces often remain in the monthly bucket files, documenting when that app was last used.

What’s particularly valuable for forensic investigators is the combination of granularity and persistence. The daily XML files typically retain the most detailed events for the past seven days. Weekly buckets cover approximately the last month. Monthly summaries can extend back six months or more, depending on the device and Android version. Beyond those retention windows, the data gets overwritten.

[ALEAPP](https://github.com/abrignoni/ALEAPP), the open-source parser created and maintained by Alexis Brignoni, handles both the legacy XML format and the Protobuf format introduced in Android 9. The `usagestats.py` script, last updated in March 2025, parses these files and produces timeline output that investigators can directly use. A typical query looks like this:

```
SELECT package_name,
       datetime(time/1000,'unixepoch') as event_time,
       type
FROM usageevents
ORDER BY time ASC;
```

This simple query reveals the exact sequence of app interactions, providing a minute-by-minute reconstruction of device usage. Combined with the aggregate duration data in the time bucket files, analysts can determine not just which apps were used, but for how long, and how that usage patterns evolved over days or weeks.

The limitations are worth noting. UsageStats doesn’t capture every user action within an app. It records app focus events, not individual actions like typing a message or taking a photo. And the retention window means older usage patterns may be lost entirely.

## Digital Wellbeing and dwbCommon.db in practice

If UsageStats tells you *which* apps were used, Digital Wellbeing tells you about the device itself. The app that Google built to help users track their screen time maintains its own usage database at `/data/com.google.android.apps.wellbeing/databases/dwbCommon.db`.

This database goes beyond simple app usage. The `usageEvents` table contains event types that are far more granular than what UsageStats provides. According to research documented by [Belkasoft](https://belkasoft.com/android-system-artifacts-forensic-analysis-of-application-usage) and corroborated by other forensic practitioners, the event type codes tell a detailed story:

| Event Type | Meaning |
| --- | --- |
| 1 | App in foreground |
| 2 | App in background |
| 15 | Screen on |
| 16 | Screen off |
| 18 | Device unlocked |
| 23 | Notification received |

This means Digital Wellbeing records not just app activity, but the physical interactions with the device. Screen on and off events reveal when the user picked up their phone. Unlock events, captured in `eventType=18`, show when and how often the device was accessed. Notifications received can indicate which apps were actively delivering content even when not directly used.

Here’s where things get interesting for Samsung device...