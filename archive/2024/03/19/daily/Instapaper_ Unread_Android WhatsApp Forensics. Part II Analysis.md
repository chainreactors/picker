---
title: Android WhatsApp Forensics. Part II Analysis
url: https://belkasoft.com/android-whatsapp-forensics-analysis
source: Instapaper: Unread
date: 2024-03-19
fetch_date: 2025-10-04T12:14:09.888289
---

# Android WhatsApp Forensics. Part II Analysis

* +1 (650) 272-0384
* [Sign in](/signin)

* Solutions

  [For Business

  Boost cyber incident response, eDiscovery and forensics capacity of your organization.](/corporate)
  [For Law Enforcement

  Acquire, examine and report digital evidence in a forensically sound way.](/law-enforcement)
  [For Academia

  Learn the art of digital forensics and cyber incident response with Belkasoft's training.](/academic)
* Products

  [Belkasoft X Forensic

  For law enforcement: Acquire, examine and analyze evidence from mobile, computer, drones, cars and cloud
  sources.](/x)
  [Belkasoft X Corporate

  For corporate customers: Carry out forensic examinations, conduct investigations into cyber incidents, and provide incident response.](/corporate)
  [Belkasoft Remote Acquisition

  A part of Belkasoft X Corporate for remotely acquiring data and evidence from computers and mobile devices
  around the world.](/r)
  [Belkasoft Incident Investigations

  A part of Belkasoft X Corporate for identifying infiltration points of malicious code and originating attack
  vectors to harden your cybersecurity.](/n)
  [Belkasoft Triage

  Instantly perform effective triage analysis of Windows devices in the
  field on scene.](/t)

  [Belkasoft Live RAM Capturer

  A tiny free forensic tool that allows to reliably extract the entire
  contents of computer’s volatile memory.](/ram-capturer)
* [Training](/training)
* Resources

  [Blog](/articles#blog)
  [Articles](/articles#article)
  [Whitepapers](/whitepapers)
  [Webinars](/webinar)
  [BelkaTalk](/belkatalk)
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

# Android WhatsApp Forensics. Part II: Analysis

![](/images/blog/162-android-whatsapp-analysis-cover.jpg)

## Introduction

Android WhatsApp is undeniably one of the most sought-after applications in mobile forensics. In [the first part of this article](/android-whatsapp-acquisition), we explored the folders and files that store WhatsApp data on Android devices and the methods that let you extract them. As you begin to examine Android WhatsApp data, you should consider the application features that create the database records. This knowledge helps you understand what evidence to look for and how to interpret your findings accurately.

In this part of the article, we will look into the forensic analysis of Android WhatsApp, covering the following topics:

* [Features to consider in WhatsApp forensics](#forensically-important-whatsapp-features)
* [Digital forensic evidence in Android WhatsApp databases: wa.db, msgstore.db, companion\_devices.db](#evidence-in-android-whatsapp-dbs)
* [Tips on how to analyze Android WhatsApp in Belkasoft X](#analyze-android-whatsapp-in-belkasoft)

[Belkasoft X](/x) provides a comprehensive toolset for analyzing and navigating data acquired from mobile devices and computers.

[![REQUEST A TRIAL OF BELKASOFT X](https://hubspot-no-cache-eu1-prod.s3.amazonaws.com/cta/default/26836331/interactive-250063757516.png)](https://cta-eu1.hubspot.com/web-interactives/public/v1/track/redirect?encryptedPayload=AVxigLIBoIBq37mDEC%2Fm8LzZWMYrjP5HIrFOcsP3v77mxbHDWAwnRQHrs6OUgAk3RAOcPPtR%2B09qQlqr5GICLm5Hv33VaFjlhArvIHiYszAWkMYeRPqoGhkpszH8roxEGc%2BurgLP9%2Fitn1RzamEpTyBkotisIxIyqf%2FXq4hLw4q91A%3D%3D&webInteractiveContentId=250063757516&portalId=26836331)

## Forensically important features of WhatsApp

You may be curious to know that the initial idea behind WhatsApp was to show its user's status updates—hence the name; though, quite quickly it grew into a messenger. Present-day WhatsApp users can engage in one-to-one and group chats by exchanging:

* Text messages
* Media files such as pictures, video, audio, and documents
* Location pins and live locations
* Contact cards
* Polls

WhatsApp messages can be [starred](https://faq.whatsapp.com/1221996151866148/?cms_platform=android), [edited](https://faq.whatsapp.com/1370476507114859/?cms_platform=android), and [deleted](https://faq.whatsapp.com/1370476507114859/?cms_platform=android). Users can also configure [disappearing messages](https://faq.whatsapp.com/673193694148537/) that are wiped from selected chats after a specified period of time.

The WhatsApp status transformed into several one-way communication features:

* The [multimedia status](https://faq.whatsapp.com/643144237275579/?cms_platform=androidhelpref=search&cms_platform=android) that lasts 24 hours
* The [broadcast](https://faq.whatsapp.com/861663048350950/?cms_platform=android) feature that allows sending messages to multiple conversations individually
* [Channels](https://faq.whatsapp.com/549900560675125/) used to post content for a group of followers

The application also supports VoIP and video calls, including conferences. Additionally, in some countries, it can be used for payments. With such a variety of features, WhatsApp users leave numerous digital traces that provide insights into their connections, interactions, behaviors, locations, and more.

Moreover, a single WhatsApp account can be used across [multiple devices](https://faq.whatsapp.com/378279804439436/). This feature can aid in identifying additional devices involved in the account usage.

## Evidence in Android WhatsApp databases

Now that you know how users can interact with the WhatsApp application, let us delve into the database records these activities create.

### wa.db

The wa.db table is your source of information about the account owner's contacts and groups.

**wa\_contacts** can reveal the names of the account owner's contacts, their phone numbers, "about" information, and other details. When exploring the **jid** column containing user's chat IDs, you may notice that several types of contact records are available:

* **@broadcast** indicates broadcast groups, with **status@broadcast** being reserved for the user's multimedia statuses
* **@s.whatsapp.net** stands for one-to-one chats
* **@g.us** indicates group chats
* **@newsletter** identifies channels

![WhatsApp contact records in wa.db, wa_contacts table](/images/articles/android-whatsapp-analysis/01-AWA-wadb-contacts.png)

***Figure 1:** WhatsApp contact records in wa.db, wa\_contacts table*

**wa\_bloc\_list** offers insights into the unwanted contacts in the user's list. Interestingly, it also includes the blocked contact's internal WhatsApp ID indicated by **@lid**.

![WhatsApp blocked contact records in wa.db, wa_block_list table](/images/articles/android-whatsapp-analysis/02-AWA-wadb-bloc.png)

***Figure 2:** WhatsApp blocked contact records in wa.db, wa\_block\_list table*

**wa\_group\_admin** provides one more notable piece of information. **creator\_jid** helps you define the admins of the group chats where the user participates.

![WhatsApp group records in wa.db, wa_group_admin_settings table](/images/articles/android-whatsapp-analysis/03-AWA-wadb-groupadmin.png)

***Figure 3:** WhatsApp group records in wa.db, wa\_group\_admin\_settings table*

### msgstore.db

**msgstore.db** is the largest database in the Android WhatsApp dataset. It contains the account owner's conversations stored in the **message** table and all associated information spread across other tables. Here are the columns of primary interest in the **message** table:

* **chat\_row\_id** indicates in what chat a message was exchanged; it is a foreign key that links to the **\_id** column in the **chat** table that stores chat details
* **sender\_jid\_row\_id** indicates the contact that sent the message; it is a ...