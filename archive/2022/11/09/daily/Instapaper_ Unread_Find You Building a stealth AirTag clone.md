---
title: Find You Building a stealth AirTag clone
url: https://positive.security/blog/find-you
source: Instapaper: Unread
date: 2022-11-09
fetch_date: 2025-10-03T22:10:29.382867
---

# Find You Building a stealth AirTag clone

![](https://cdn.prod.website-files.com/5f6498c074436c50c016e745/5f6498c074436cf0ef16e7ad_menu_icon_flipped.png)

[HOME](/)[About](/about)[Services](/services)[Blog](/blog)[Contact](/contact)

[![](https://cdn.prod.website-files.com/5f6498c074436c50c016e745/5f6498c074436c270016e798_purple.png)](/)

# Find You: Building a stealth AirTag clone

February 21, 2022

ByÂ

Fabian BrÃ¤unlein

![](https://cdn.prod.website-files.com/5f6498c074436c349716e747/6210d37a1cd882269988645e_cover_w_background_3.png)

* After AirTags are reportedly used more and more frequently for malicious purposes, Apple has published a statement that lists its current and future efforts to prevent misuse
* We built an AirTag clone that bypasses all those tracking protection features and confirmed it working in a real-world experiment (source code available [here](https://github.com/positive-security/find-you))
* We encourage Apple to include AirTag clones/modified AirTags into their threat model when planning the next changes to the Find My ecosystem

## Introduction

Recently, reports about AirTags being used to track other people and their belongings were [becoming](https://www.nytimes.com/2021/12/30/technology/apple-airtags-tracking-stalking.html) [much](https://www.theguardian.com/technology/2022/jan/20/apple-airtags-stalking-complaints-technology) [more](https://www.nbcnews.com/news/apple-airtag-showing-up-crimes-rcna9416) [frequent](https://www.fox2detroit.com/news/man-finds-apple-air-tag-tracker-on-his-dodge-charger).

[In one exemplary stalking case](https://swimsuit.si.com/swimnews/brooks-nader-shares-scary-stalking-story-involving-an-air-tag), a fashion and fitness model discovered an AirTag in her coat pocket after having received a tracking warning notification from her iPhone. [Other times](https://www.youtube.com/watch?v=WswKQxGOgWI), AirTags were placed in expensive cars or motorbikes to track them from parking spots to their ownerâs home, where they were then stolen.

On February 10, Apple addressed this by publishing [a news statement](https://www.apple.com/newsroom/2022/02/an-update-on-airtag-and-unwanted-tracking/) titled âAn update on AirTag and unwanted trackingâ in which they describe the way they are currently trying to prevent AirTags and the Find My network from being misused and what they have planned for the future.

Admittedly, I might be slightly more familiar with AirTags than the average hacker (having [designed](https://positive.security/blog/send-my) and [implemented](https://github.com/positive-security/send-my) a communication protocol on top of Find My for arbitrary data transmission), but even so I was quite surprised, that when reading Appleâs statement I was able to immediately devise quite obvious bypass ideas for every current and upcoming protection measure mentioned in that relatively long list.

The following section will discuss each anti-stalking feature and how it can be bypassed in theory. Thereafter I will describe how I implemented those ideas to build a stealth AirTag and successfully tracked an iPhone user (with their consent of course) for over 5 days without triggering a tracking notification.

The goal of this blog post is to raise awareness of these issues to hopefully also guide future changes. In particular, Apple needs to incorporate non-genuine AirTags into their threat model, thus implementing security and anti-stalking features into the Find My protocol and ecosystem instead of in the AirTag itself, which [can run modified firmware](https://www.vice.com/en/article/pkbpa7/hackers-are-having-a-field-day-with-airtags) or not be an AirTag at all (Apple devices currently have no way to distinguish genuine AirTags from clones via Bluetooth).

The source code used for the experiment can be found [here](https://github.com/positive-security/find-you).

Edit:Â I have been made aware of a research paper titled ["Who Tracks the Trackers?"](https://dl.acm.org/doi/abs/10.1145/3463676.3485616?sid=SCITRUS) (from November 2021) that also discusses this idea and includes more experiments. Make sure to check it out as well if you're interested in the topic!

## Table of Contents

-- MARKDOWN --
- [In Theory](#in-theory)
Â Â Â Â - [Current Features](#current-features)
Â Â Â Â Â Â Â Â - [Serial number](#serial-number)
Â Â Â Â Â Â Â Â - [Beeping](#beeping)
Â Â Â Â Â Â Â Â - [iPhone notifications](#iphone-notifications)
Â Â Â Â Â Â Â Â - [Android notifications](#android-notifications)
Â Â Â Â Â Â Â Â - [Side note: Apple-ID for querying location reports](#side-note-apple-id-needed-to-query-location-reports)
Â Â Â Â - [Upcoming Features](#upcoming-features)
Â Â Â Â Â Â Â Â - [New privacy warnings during AirTag setup](#new-privacy-warnings-during-airtag-setup)
Â Â Â Â Â Â Â Â - [Addressing alert issues for AirPods](#addressing-alert-issues-for-airpods)
Â Â Â Â Â Â Â Â - [Updated support documentation](#updated-support-documentation)
Â Â Â Â Â Â Â Â - [Precision Finding](#precision-finding)
Â Â Â Â Â Â Â Â - [Display alert with sound](#display-alert-with-sound)
Â Â Â Â Â Â Â Â - [Refining unwanted tracking alert logic](#refining-unwanted-tracking-alert-logic)
Â Â Â Â Â Â Â Â - [Tuning AirTagâs sound](#tuning-airtagâs-sound)
- [In Practice](#in-practice)
Â Â Â Â - [Test setup](#test-setup)
Â Â Â Â - [Android detection](#android-detection)
Â Â Â Â Â Â Â Â - [Tracker Detect](#tracker-detect)
Â Â Â Â Â Â Â Â - [AirGuard](#airguard)
Â Â Â Â - [iOS detection](#ios-detection)
- [Closing Thoughts](#closing-thoughts)
-- /MARKDOWN --

## In Theory

Letâs take a look at all of Appleâs (planned) tracking protection features and how we could bypass them with an [OpenHaystack](https://github.com/seemoo-lab/openhaystack)-based AirTag clone.

### Current Features

#### Serial number

From the news statement:

> âEvery AirTag has a unique serial number, and paired AirTags are associated with an Apple ID. Apple can provide the paired account details in response to a subpoena or valid request from law enforcement. We have successfully partnered with them on cases where information we provided has been used to trace an AirTag back to the perpetratorâ

Why this does not affect our scenario:

1. The microcontroller used to build the AirTag clone (e.g. an ESP32) does not have an AirTag serial number (neither in software nor on the hardware).
2. OpenHaystack-based clones are already not paired with an Apple ID (as this is not necessary as a result of the privacy-focused design).

#### Beeping

Initially, an AirTag that has not been in Bluetooth reach of its paired Apple device for over 3 days started to beep. With an update in June 2021, Apple decreased this to a random time frame between 8 and 24 hours.

This one is easy: Our ESP32 does not even have a speaker. Furthermore the OpenHaystack firmware does not implement [the BLE service to remotely trigger the sound](https://github.com/seemoo-lab/AirGuard/blob/1214230bd4b4059c5521068d6c96b6e21d8b07d2/app/src/main/java/de/seemoo/at_tracking_detection/util/ble/BluetoothLeService.kt#L113-L147), so the âPlay Soundâ-button is not even shown.

As a side note, there is already a market for so-called âSilent AirTagsâ (modified AirTags that had their speaker removed/disconnected).

[![](https://cdn.prod.website-files.com/5f6498c074436c349716e747/6210d43c1cd882b7a2886558_find_you_silent_airtag_ebay.png)](https://positive.security/#zoom)

Searching for âsilent airtagâ on [ebay.de](http://ebay.de) currently shows several options for AirTags with deactivated speakers

#### iPhone notifications

From the [docs](https://support.apple.com/en-us/HT212227):

> âIf any AirTag, AirPods, or other Find My network accessory separated from its owner is seen moving with you over time, you'll be notifiedâ

Here, things are becoming more interesting. From the news reports linked in the beginning, this also seems to be the most common way unwanted AirTags are detected.

Here, we have an interesting and quite unique...