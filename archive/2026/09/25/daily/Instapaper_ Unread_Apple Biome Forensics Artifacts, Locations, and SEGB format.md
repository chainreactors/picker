---
title: Apple Biome Forensics Artifacts, Locations, and SEGB format
url: https://belkasoft.com/biome-forensics-artifacts
source: Instapaper: Unread
date: 2026-09-25
fetch_date: 2026-09-26T06:51:57.294106
---

# Apple Biome Forensics Artifacts, Locations, and SEGB format

* +1 (650) 272-0384
* [Sign in](/signin)

* Solutions

  [For Business

  Streamline internal investigations, cyber incident response, and eDiscovery.](/corporate)
  [For Law Enforcement

  Acquire, examine, and report on digital evidence in a forensically sound way.](/law-enforcement)
  [For Academia

  Learn the art of digital forensics with Belkasoft tools and training courses.](/academic)
* Products

  [Belkasoft X Forensic

  For government organizations: Acquire and analyze evidence from mobile devices, computers, drones, cars, and cloud sources.](/x)
  [Belkasoft X Corporate

  For business: Simplify corporate investigations and eDiscovery with advanced digital forensics and incident response tools.](/corporate)
  [Belkasoft Remote Acquisition

  Securely collect digital evidence from remote computers and mobile devices. Included with Belkasoft X Corporate.](/r)
  [BelkaGPT Hub

  Distribute AI processing across GPU-equipped machines in your lab to accelerate BelkaGPT-powered investigations.](/belkagpt-hub)
  [Belkasoft Triage (Free)

  Instantly detect and extract key digital evidence on Windows machines.](/t)

  [Belkasoft Live RAM Capturer (Free)

  Capture the full contents of volatile memory from Windows systems quickly and reliably.](/ram-capturer)
* Training

  [DFIR Training

  Advance your skills with Belkasoft's hands-on courses and certifications.](/digital-forensics-training)
  [Self-Paced Courses

  Choose an on-demand course to build skills at your own pace and deepen your expertise.](/dfir-training-on-demand)
  [Educational Events

  Join Belkasoft and partners for training and workshops across the globe.](/belkasoft-education)
* Resources

  [Blog](/articles#blog)
  [Articles](/articles#article)
  [Whitepapers](/whitepapers)
  [Webinars](/webinar)
  [Tutorials](/tutorials)
  [Newsroom](/news)
  [Product Releases](/new)
  [Testimonials](/testimonials)
  [Case Studies](/case_studies)
  [BelkaCTF](/ctf)
  [User Guide](/help)
* Company

  [About](/company)
  [News](/news)
  [Customers](/customers)
  [Partners](/partners)
  [Contact Us](/contact)
* [![Get started](https://hubspot-no-cache-eu1-prod.s3.amazonaws.com/cta/default/26836331/73846a5e-e69a-4352-8c78-bd41126272e8.png)](https://hubspot-cta-redirect-eu1-prod.s3.amazonaws.com/cta/redirect/26836331/73846a5e-e69a-4352-8c78-bd41126272e8)

[#article](/articles#article)

# Apple Biome Forensics: Artifacts, Locations, and SEGB format

![](/images/covers/biome-forensics-artifacts-cvr.webp)

Apple Biome artifacts are among the richest sources of pattern-of-life data on modern iPhones, iPads, and Mac computers. Biome is Apple’s on-device system for logging user and application activity. In earlier iOS versions, much of this data lived in the **knowledgeC.db** database. Apple then changed how it stores these records, and the same evidence reappeared in Biome folders. Most Biome data is stored in SEGB, Apple’s proprietary binary format that logs events into segment-based container files. Biome is harder to work with than the old SQLite database, but the effort pays off. It holds timestamped records of user actions that help you find leads, corroborate other findings, and sometimes recover deleted information.

In this article, you will learn:

* [What Apple Biome is and why it matters in forensics](#what-is-biome)
* [Where Biome files live on iOS](#biome-files)
* [How the SEGB format and its Protocol Buffer records are structured](#segb-format)

This is part one of a two-part series. Part two covers parsing a Biome file by hand and how [Belkasoft X](https://belkasoft.com/x) brings this data into your investigation.

## What Apple Biome is and why it matters

Biome is an internal iOS and macOS framework that logs what happens on the device: which applications run, how the device state changes, and what the user does. System services and applications report events to Biome, which saves them as records in binary files. Records of one kind, such as application launches or Wi-Fi connections, make up a **stream**. Apple uses this data for on-device features like Siri Suggestions and Spotlight recommendations but has not documented Biome publicly, so what we know comes from forensic research.

For examiners, the same records show which applications the user opened, which websites they visited, and when the device was locked, charging, or online. Before iOS 16, most of this evidence came from [**knowledgeC.db**](https://belkasoft.com/knowledgec-database-forensics-with-belkasoft), a SQLite database that Apple uses for the same purpose. It also sorts records into streams, and each record keeps its stream name, such as **/app/inFocus** or **/safari/history**, in the **ZSTREAMNAME** column of the **ZOBJECT** table.

In iOS 18, **knowledgeC.db** is still present and worth checking. But, since iOS 14, Apple started duplicating and, eventually, moving streams out of it to the Biome.

Biome is useful for examiners because it can provide:

* **A detailed activity timeline.** Its timestamped events can help reconstruct sequences of actions and identify broader patterns of device use and user behavior.
* **Activity from other Apple devices.** Some Biome data syncs between devices, so an examined device may contain records that originated on other devices associated with the same Apple ID.
* **Additional application evidence.** Biome records some application activity independently, so it can preserve information that is no longer present in the application databases.

## Where can you find Biome artifacts on iOS?

Biome data is available only through a full file system extraction, not through an iTunes-style backup.

Binary files with Biome data are primarily stored in two file system directories:

* **/private/var/mobile/Library/Biome/**
* **/private/var/db/biome/**

Inside each directory, a **streams** folder separates data into **public** and **restricted** subfolders, based on how sensitive Apple considers the data. Restricted streams generally cover more personal categories, such as messages and calls, while public streams cover broader device and app usage. Each tracked function then gets its own subdirectory. Many older **knowledgeC.db** streams reappear here with descriptive names. For example:

* App in focus moved to **/private/var/db/biome/streams/restricted/\_DKEvent.App.InFocus/**
* Application installs moved to **/private/var/mobile/Library/Biome/streams/restricted/\_DKEvent.App.Install/**
* Application launch moved to **/private/var/mobile/Library/Biome/streams/public/AppLaunch/**
* CarPlay connection state moved to **/private/var/mobile/Library/Biome/streams/restricted/\_DKEvent.CarPlay.IsConnected/**
* Safari history moved to **/private/var/db/biome/streams/restricted/\_DKEvent.Safari.History/**

**Note:** SEGB files are not limited to the two Biome directories. The Duet Expert Center service maintains its own streams in **/private/var/mobile/Library/DuetExpertCenter/streams/**. The most valuable one for examiners is **userNotificationEvents**, which records notifications the device received. These records can include message previews, social media alerts, and payment notifications. In some cases, they preserve information that is no longer available in the original application or message store. On recent iOS versions, the SEGB files sit in a numeric subfolder inside **userNotificationEvents/local/**.

Each Biome subdirectory usually contains a **local** folder and may also contain a **remote** folder.

* **local** contains Biome records generated on the device being examined.
* **remote** contains records synced from other iOS or macOS devices.

Each **remote** subfolder is named with the GUID of the device that generated the data. You can identify that device through the **sync.db** database located at **/private/var/mobile/Library/Biome/sync/**. Its **DevicePeer** table maps device GUIDs to syncing devices and records the last synchronization date.

The binary files inside the **local**...