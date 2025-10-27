---
title: Wipeout! Detecting Android Factory Resets
url: https://dfir.pubpub.org/pub/xmjxofpd/release/1
source: Instapaper: Unread
date: 2022-11-09
fetch_date: 2025-10-03T22:10:23.801398
---

# Wipeout! Detecting Android Factory Resets

[Skip to main content](#main-content)

[![](https://resize-v3.pubpub.org/eyJidWNrZXQiOiJhc3NldHMucHVicHViLm9yZyIsImtleSI6ImhuZHdvMDAzLzYxNjc1Mzc0NjMxMDQ5LnBuZyIsImVkaXRzIjp7InJlc2l6ZSI6eyJoZWlnaHQiOjUwLCJmaXQiOiJpbnNpZGUiLCJ3aXRob3V0RW5sYXJnZW1lbnQiOnRydWV9fX0=)](/)

[Search](/search)Dashboardcaret-down[Login](/login?redirect=/pub/xmjxofpd/release/1)[Login or Signup](/login?redirect=/pub/xmjxofpd/release/1)

* [DFIR Review](/)
* [Stats](/blog)
* [Reviewers](/reviewers)
* [Submission Guidance](/submission-guidance)
* [Publications](/pub)
* [Aims & Scope](/about)
* [Review Guidance](/review-guidance)
* [Community](/community)
* [DFRWS.org](/dfrws)

**Published on** Nov 03, 2022**DOI**10.21428/b0ac9c28.24a2cc13

# Wipeout! Detecting Android Factory Resets

by [Joshua Hickman](/user/josh-hickman)

Published onNov 03, 2022

Cite

Social

[PDF Download](https://s3.amazonaws.com/assets.pubpub.org/rvhtidveixlwxw04umwo20h3hrrkusau.pdf)[Word Download](https://assets.pubpub.org/gvmymdiv/24a2cc13-7be0-40ee-8ea4-cc854b81488a.docx)[Markdown Download](https://assets.pubpub.org/r53mat2c/24a2cc13-7be0-40ee-8ea4-cc854b81488a.md)[EPUB Download](https://assets.pubpub.org/rr1px0d6/24a2cc13-7be0-40ee-8ea4-cc854b81488a.epub)[HTML Download](https://assets.pubpub.org/pvju2l39/24a2cc13-7be0-40ee-8ea4-cc854b81488a.html)[OpenDocument Download](https://assets.pubpub.org/djf051sh/24a2cc13-7be0-40ee-8ea4-cc854b81488a.odt)[Plain Text Download](https://assets.pubpub.org/do7w0eph/24a2cc13-7be0-40ee-8ea4-cc854b81488a.txt)[JATS XML Download](https://assets.pubpub.org/4g1sa9ni/24a2cc13-7be0-40ee-8ea4-cc854b81488a.xml)[LaTeX Download](https://assets.pubpub.org/mk8y4m8e/24a2cc13-7be0-40ee-8ea4-cc854b81488a.tex)

Download

Contents

last released

3 years ago

[Wipeout! Detecting Android Factory Resets - Release #1](https://dfir.pubpub.org/pub/xmjxofpd/release/1)

Show details

Wipeout! Detecting Android Factory Resets

ContentsÂ·

# Synopsis

|  |  |
| --- | --- |
| **Forensics Question:**  Is there a way to determine when an Android phone has been reset? | ![](https://resize-v3.pubpub.org/eyJidWNrZXQiOiJhc3NldHMucHVicHViLm9yZyIsImtleSI6Im90bTdoc3BsLzAxNjA0MzI0NjIzMDg0LnBuZyIsImVkaXRzIjp7InJlc2l6ZSI6eyJ3aWR0aCI6ODAwLCJmaXQiOiJpbnNpZGUiLCJ3aXRob3V0RW5sYXJnZW1lbnQiOnRydWV9fX0=) |
| **OS Version:**   * Android 12 (Pixel â Hickman public image) * Android 11 (Pixel - August 2021 patch, Samsung - April 2021 patch) * Android 10 (Pixel â Hickman public image, Samsung â March 2020 patch) | ![](https://resize-v3.pubpub.org/eyJidWNrZXQiOiJhc3NldHMucHVicHViLm9yZyIsImtleSI6InN5MXZ4d2Z5LzYxNjY3NDc2NTAyNzI0LnBuZyIsImVkaXRzIjp7InJlc2l6ZSI6eyJ3aWR0aCI6ODAwLCJmaXQiOiJpbnNpZGUiLCJ3aXRob3V0RW5sYXJnZW1lbnQiOnRydWV9fX0=) |
| **Tools:**   * Autopsy (4.17.0) * Cellebrite Physical Analyzer 7.46.0.64) * Cellebrite UFED (7.45.1.43) * DB Browser for SQLite (3.12.2) * TextMate for macOS (2.0.19) * Android Triage Tool (1.2) * Magisk 23.0 |  |

*Iâd like to thankÂ**[Alexis Brignoni](https://linqapp.com/abrignoni)**,Â**[Heather Mahalik](https://twitter.com/HeatherMahalik)**, andÂ**[Jared Barnhart](https://twitter.com/bizzybarney?lang=en)**Â for their insight and validation, and Alexis for toolingÂ**[ALEAPP](https://github.com/abrignoni/ALEAPP)**Â for these artifacts.Â  DFIR truly is a team effort.*

They say imitation is the sincerest form of flattery, and that is my intention here. Late last year Heather Mahalik & Ian Whiffan put out an article describing how examiners can detect when an iOS device is wiped. It is a great article, one every examiner should bookmark and read because it is guaranteed an examiner will have that question asked of them at some point if they do mobile forensics. The article can be foundÂ [here](https://doi.org/10.21428/b0ac9c28.9fc29261).

Recently I saw a couple of users on DFIR Discord ask the same question about Android devices. After doing some digging, I discovered no one had really addressed Android factory resets (wipes) before (if they have, I was unable to find it), so I thought it would be great to look into it.

Like Heather and Ian, I want to make it clear that just because a wipe is detected does not mean the user was intentionally trying to be malicious. There are a lot of legitimate reasons a user may wipe their device, so it is up to the examiner/investigator to determine the motivation of the user.

The Setup

Testing involved a few different sources:Â  my Android 10 and 11 images, and new data generated using my Pixel 3 running Android 11 (August 2021 patch).Â  I also used a Samsung Galaxy A30 running Android 10 (March 2020 patch) & Android 11 (April 2021 - latest supported patch at the time).Â  The Samsung was upgraded from Android 10 to 11 during this exercise (more on that later).Â  I considered what was available in both rooted and non-rooted states, what was available using open source tools, and considered four different scenarios which I may refer to occasionally in this article:

1. A user resets their phone and completes the setup process.
2. A user resets their phone, partially completes the setup process, but leaves the phone in the setup state for an extended period of time prior to completion. Then the user starts to use the phone and completes the setup process at a later time.
3. A user resets their phone, but leaves the device at the initial setup screen. The phone is seized in this state and requires the examiner to set the phone up offline in order to perform the extraction.
4. A user resets their phone, sets the phone up âofflineâ but contemporaneous to the wipe, and then completes the online setup (i.e. signs into their Google account) at a later time.

During testing the devices were wiped using two different methods:Â  via the Android UI and via Recovery.Â  After the wipes, the phones were setup as both new and restored from backups.

As far as tools, a few different ones were used:

DB Browser for SQLite (3.12.2)

Autopsy (4.17.0)

Cellebrite UFED (7.45.1.43)

Cellebrite Physical Analyzer (7.46.0.64)

TextMate for macOS (2.0.19)

Android Triage Tool (1.2)

The good news is that there are artifacts examiners can use to determine the approximate time an Android phone was wiped. There were a few files that initially appeared to be good candidates, but, because there were so many caveats with them, I decided not to document them here as they could be unreliable depending on the scenario. Some of the files documented here do have caveats, which I will describe so that an examiner can make a determination about the usability of the timestamp as it relates to their examination.

Because this is Android, things are a little messy as the artifacts are scattered throughout the operating system.Â  The availability of these files depends on the OEM, how the OEM implemented Android, the version of Android itself, and the level of access to the phone file system (i.e. root/not root).Â  This blog post only addresses the Pixel (the "purest" version of Android) and Samsung (one of if not the most popular Android OEMs) line of phones, but other OEMs may implement Android in different ways that may alter the artifacts available on their respective devices.

Additionally, mobile carriers may install custom applications on Android that may also contain artifacts that can help an examiner approximate a time of wipe.Â  Those types of artifacts are not addressed in this blog post.

Nuts & Bolts

The first file is *suggestions.xml*, and it is found in the same location in Android 10, & 11: /**data/data/com.google.android.settings.intelligence/shared\_prefs**. There is an additional location in Android 11: **/data/user/%USER%/com.google.android.settings.intelligence/shared\_prefs**. Because of its location, an examiner would need a full file system extraction (or access to /data/data). There was good news, however, for Android 11:Â  Â the file was available in both a full file system and advanced logical extraction in Cellebrite.

There are two XML tags in this f...