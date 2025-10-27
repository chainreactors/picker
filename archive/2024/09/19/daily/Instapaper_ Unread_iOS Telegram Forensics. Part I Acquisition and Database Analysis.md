---
title: iOS Telegram Forensics. Part I Acquisition and Database Analysis
url: https://belkasoft.com/ios-telegram-forensics-acquisition-and-database-analysis
source: Instapaper: Unread
date: 2024-09-19
fetch_date: 2025-10-06T18:28:24.935930
---

# iOS Telegram Forensics. Part I Acquisition and Database Analysis

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

# iOS Telegram Forensics. Part I: Acquisition and Database Analysis

![](/images/blog/178-ios-telegram-forensics-acqisuistition-and-database-analysis.jpg)

In digital forensic investigations and cyber incident response procedures, Telegram, like many messengers and social apps, can reveal a considerable amount of information about its users. In our [first article in the Telegram forensics series](/telegram-forensics-getting-started), we have covered how the app works and what you can find in Telegram cloud data. Telegram files acquired from a device can open up a broader spectrum of details, yet their examination requires special knowledge.

In this article, we will explain how to approach iOS Telegram forensics, focusing on the following topics:

* [How to acquire Telegram data from iOS devices](#acquire-ios-telegram)
* [iOS Telegram files of interest](#ios-telegram-files)
* [How to read the iOS Telegram database:](#understanding-ios-telegram-data)

+ [Big-endian and little-endian formats](#ios-telegram-endianness)
+ [Decoding account information](#account-settings-t0)
+ [Understanding chat records](#chat-details-t2)
+ [Deciphering messages](#message-records-t7)

We will show how to work with iOS Telegram's SQLite database in [Belkasoft X](/x), a digital forensics tool that not only extracts data from applications but also provides low-level analysis instruments that help efficiently validate digital artifacts.

[![REQUEST A TRIAL OF BELKASOFT X](https://hubspot-no-cache-eu1-prod.s3.amazonaws.com/cta/default/26836331/interactive-250065764586.png)](https://cta-eu1.hubspot.com/web-interactives/public/v1/track/redirect?encryptedPayload=AVxigLKwcGSeH%2FXoBeZz3kf9eG3cHaXtJbrU7NI2qPqkRxhuN2%2BrvtTlbTmqeipeGSF1%2FipzEgYLVOv6pdYDlC4Kc5S04hVCUVt6e3Wr81cED5blU20XMU4vfj%2FiOHYlTg57UFxlMXzDkgl%2BtPiw55kwEi9vJRQQHP9AhLlRls1GqA%3D%3D&webInteractiveContentId=250065764586&portalId=26836331)

## Acquiring iOS Telegram data

Telegram stores messaging data on its servers and does not save it using iOS backup mechanisms such as iTunes and iCloud. On the one hand, this approach is beneficial for digital forensics because it allows you [to obtain user data from the cloud](/telegram-forensics-getting-started#tg-cloud-acquisition) if the device is damaged or unavailable. On the other hand, it does not let you access Telegram data using the iTunes and iCloud backup acquisition methods that are less technically demanding.

Telegram data stored on iOS devices can only be obtained with a [full file system copy](/checkm8_glossary) of the device. To [acquire iOS devices](/mobile_acquisition), you need a digital forensics tool that provides advanced iOS acquisition methods.

With Belkasoft X, you can extract the full file system of Apple mobile phones and tablets on different iOS versions with the help of [agent-based acquisition](/agent_based_ios_acquisition) or [checkm8-based acquisition](/checkm8), and acquire jailbroken devices (with checkra1n, odyssey, unc0ver, or other jailbreaks installed).

Here are the sought-after Telegram artifacts you can find on mobile devices:

* Secret chats
* Private channels whose content can only be viewed online by participants
* Deleted messages and previous versions of edited messages (under favorable conditions)

## Exploring iOS Telegram files

After you obtain the full file system copy of an iOS device, you can find Telegram files in the **..\private\var\mobile\Containers\Shared\AppGroup\{GUID}** folder. The GUID is an alphanumeric number that the system assigned to the application when it was installed on the device.

![](/images/articles/ios-telegram-forensics-acquisition-and-database-analysis/01-iOSTg-filesystem.png)

*Figure 1: Telegram folder structure in an iPhone file system*

Data related to Telegram accounts used on the device is located in the **telegram-data** directory. One client instance (device) can house up to three accounts (as of Telegram version 11.0.2), each having a separate folder. In the example above, one account folder is available.

When looking for Telegram artifacts related to an account, you will typically be interested in the **postbox** folder that contains the following:

* a **db** folder with the application database and
* a **media** folder with exchanged files.

Note that the amount of data stored in the **media** folder may be limited as it depends on the application settings. Since Telegram stores user data in the cloud, users do not have to keep all exchanged files on their devices. They can configure the application to auto-remove cached files after a certain period and when the application cache reaches a certain size.

![](/images/articles/ios-telegram-forensics-acquisition-and-database-analysis/02-iOSTg-cache-settings.jpg)

*Figure 2: iOS Telegram media storage settings*

## Understanding iOS Telegram data

Telegram stores messaging data in the **db\_sqlite** database and the associated transactional files. The database, as you may guess by its name, has the SQLite format, which is familiar to many forensic examiners. However, unlike many other applications, Telegram stores most of the records in the serialized binary format. What does it mean? When a user takes some action within the application, the database entry associated with it (for example, a message and all associated details) is recorded as a stream of bytes organized in a series. This process helps transmit information more easily, but when it comes to forensic examination, you must know how to deserialize the records to read their contents.

In this section, we will explore how to understand **db\_sqlite** records in the columns of interest:

* **t0** that includes account settings
* **t2** that stores the information about the user's chats
* **t7** that includes chat messages and their properties

### Before you begin

When reading b...