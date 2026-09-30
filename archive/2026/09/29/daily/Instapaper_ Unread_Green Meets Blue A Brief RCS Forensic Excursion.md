---
title: Green Meets Blue A Brief RCS Forensic Excursion
url: https://www.forensicfocus.com/articles/green-meets-blue-a-brief-rcs-forensic-excursion/
source: Instapaper: Unread
date: 2026-09-29
fetch_date: 2026-09-30T07:43:10.136422
---

# Green Meets Blue A Brief RCS Forensic Excursion

[Skip to content](#content "Skip to content")

* [Login/Register](https://www.forensicfocus.com/sign-in/?redirect_to=https%3A%2F%2Fwww.forensicfocus.com%2Farticles%2Fgreen-meets-blue-a-brief-rcs-forensic-excursion%2F)

[![Forensic Focus](https://www.forensicfocus.com/stable/wp-content/themes/generatepress_child/assets/images/logo.png)](https://www.forensicfocus.com/ "Forensic Focus")

[Login](/sign-in/)
[Register](/sign-up/)

[![Forensic Focus](https://www.forensicfocus.com/stable/wp-content/uploads/2020/05/forensic-focus_logo.png)](https://www.forensicfocus.com/ "Forensic Focus")

Menu

* News
  + [Headlines](/news/headlines/latest/)
  + [More News](/news/)
* Articles
  + [Articles](/articles/)
  + [Interviews](/interviews/)
  + [Case Studies](/case-studies/)
  + [Reviews](/reviews/)
  + [Guides](/guides/)
  + [Digital Forensics Timeline](/digital-forensics-timeline/)
  + [Tool & Vendor Directory](/dfir-tool-directory/)
  + [Tool Release Tracker](/dfir-tool-release-tracker/)
* Webinars/Videos
  + [Webinars](/webinars/)
  + [Videos](/videos/)
* Careers & Jobs
  + [Browse Jobs](/jobs/)
  + [How to Start a Career](/articles/how-to-start-a-career-in-digital-forensics/)
  + [Education & Training Guide](/articles/digital-forensics-education-certification-and-training-guide/)
  + [Training Finder](/dfir-training-finder/)
  + [Salary Explorer](/dfir-salary-explorer/)
  + [Skills in Demand](/dfir-skills-demand-explorer/)
  + [Practice & CTFs](/dfir-practice-directory/)
* [Well-Being](/well-being/)
* Events
  + [Event Calendar](/events/)
  + [Event Info & Recaps](/event-info/)

* [Forums](/forums/)
* [Discord](https://discord.gg/97zKvTXHeS)
* [Podcast](/podcast/)
* [Newsletter](/newsletter/)
* [Links](/useful-links/)
* [Advertise](/advertising/)
* [About](/about/)

Menu

* News
  + [Headlines](/news/headlines/latest/)
  + [More News](/news/)
* Articles
  + [Articles](/articles/)
  + [Interviews](/interviews/)
  + [Case Studies](/case-studies/)
  + [Reviews](/reviews/)
  + [Guides](/guides/)
  + [Digital Forensics Timeline](/digital-forensics-timeline/)
  + [Tool & Vendor Directory](/dfir-tool-directory/)
  + [Tool Release Tracker](/dfir-tool-release-tracker/)
* Webinars/Videos
  + [Webinars](/webinars/)
  + [Videos](/videos/)
* Careers & Jobs
  + [Browse Jobs](/jobs/)
  + [How to Start a Career](/articles/how-to-start-a-career-in-digital-forensics/)
  + [Education & Training Guide](/articles/digital-forensics-education-certification-and-training-guide/)
  + [Training Finder](/dfir-training-finder/)
  + [Salary Explorer](/dfir-salary-explorer/)
  + [Skills in Demand](/dfir-skills-demand-explorer/)
  + [Practice & CTFs](/dfir-practice-directory/)
* [Well-Being](/well-being/)
* Events
  + [Event Calendar](/events/)
  + [Event Info & Recaps](/event-info/)

[Home](https://www.forensicfocus.com/) » [Articles](https://www.forensicfocus.com/articles/) » Green Meets Blue: A Brief RCS Forensic Excursion

# Green Meets Blue: A Brief RCS Forensic Excursion

29th September 2026 by [MSAB](https://www.forensicfocus.com/author/msab/ "View all posts by MSAB")

![](https://www.forensicfocus.com/stable/wp-content/uploads/2026/09/Green-meets-Blue-A-brief-RCS-forensic-excursion.png)

*by Markus Hess, MSAB Digital Forensic Specialist*

* What is RCS (Rich Communication Services)?
* What can it do?
* Who uses RCS, and how do they use it?
* And, above all, where can I find forensic evidence of this?

## What Is RCS Anyway?

All delivered in what I hope is a concise and accessible way, while still bringing in the right level of expertise where it matters. Think of it as too detailed for a TikTok, but not quite long enough for a podcast.

RCS is a modern messaging standard that was introduced to replace SMS and MMS and bring chat app functionality directly into the normal messaging app on mobile phones. This communication standard was developed by the GSM Association (GSMA) for IP-based messaging on mobile phones.

It is therefore binding for every device that is active on the GSM network and always uses the same standard, ensuring cross-platform communication. However, it is not mandatory for a provider to offer RCS.

### Important functions

* Sending high-resolution photos, videos, files and, in some cases, GIFs directly in the messaging app.
* Typing indicator (“someone is typing…”), read receipts, longer text lengths and improved group chats with renaming and leaving groups.
* Use of mobile data or Wi-Fi instead of the traditional SMS signaling network.

### Security and encryption

* RCS is fundamentally IP-based; many implementations encrypt messages at least during transmission.
* Provided that both participants are using compatible RCS implementations that support end-to-end encryption, 1:1 chats can be end-to-end encrypted.

## Understanding the Differences: SMS, iMessage and RCS

Before we address the forensic challenges, it is important to distinguish between these messaging protocols:

## Get The Latest DFIR News

### The monthly Forensic Focus newsletter, plus webinar invitations and occasional research surveys.

Unsubscribe or change what you receive at any time. We respect your privacy: read our [privacy policy](/privacy-policy).

Leave this field empty if you're human:

* **SMS** – This traditional text messaging standard is limited to 160-character text messages, offers no encryption and only supports basic metadata.
* **iMessage** – Apple’s own messaging service uses end-to-end encryption and synchronizes messages across devices. Messages are stored in iCloud backups.
* **RCS** – Unlike SMS, RCS works online and supports modern communication features like iMessage and other chat applications.

## What if My Conversation Partner Does Not Support RCS? And Who Supports It Anyway?

Two factors are important here: the mobile operating system and the network operator.

While the former is relatively easy and straightforward to address, all modern Android smartphones (from Android 6 with Google Messages onwards) and newer iPhones with iOS 18 or higher currently support RCS.

The second factor, network operator support, is somewhat more complicated. Although coverage is improving, it has not yet quite caught up with SMS. Many of the major providers worldwide, such as Telekom, Vodafone, Orange, AT&T, T-Mobile, Verizon and others, support RCS as standard at no extra charge.

Whether on Android or Apple iOS, RCS messages are always stored and sent in the normal standard app (Messages, for example). No extra RCS app is required.

Read the full blog here: [Green meets Blue: A brief RCS forensic excursion – MSAB](https://www.msab.com/blog/green-meets-blue-a-brief-rcs-forensic-excursion/)

Categories [Articles](https://www.forensicfocus.com/articles/) Tags [msab](https://www.forensicfocus.com/tag/msab/), [rcs](https://www.forensicfocus.com/tag/rcs/)

[DFIR News, 29 Sep 2026](https://www.forensicfocus.com/news/headlines/dfir-news-29-sep-2026/)

[Belkasoft Releases Belkasoft X v2.12, Adding Offline Translation And AI-Assisted Database Analysis](https://www.forensicfocus.com/news/belkasoft-releases-belkasoft-x-v2-12-adding-offline-translation-and-ai-assisted-database-analysis/)

### Leave a Comment [Cancel reply](/articles/green-meets-blue-a-brief-rcs-forensic-excursion/#respond)

You must be [logged in](https://www.forensicfocus.com/sign-in/?redirect_to=https%3A%2F%2Fwww.forensicfocus.com%2Farticles%2Fgreen-meets-blue-a-brief-rcs-forensic-excursion%2F) to post a comment.

### Latest Articles

[![Roadblocks Ahead! Navigating The Major Issues Of Mobile Forensics](https://www.forensicfocus.com/stable/wp-content/uploads/2026/09/Screenshot-2026-09-23-222817-870x570.png)](https://www.forensicfocus.com/webinars/roadblocks-ahead-navigating-the-major-issues-of-mobile-forensics/)

[Webinars](https://www.forensicfocus.com/webinars/)

### [Roadblocks Ahead! Navigating The Major Issues Of Mobile Forensics](https://www.forensicfocus.com/webinars/roadblocks-ahead-navigating-the-major-issues-of-m...