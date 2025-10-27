---
title: Skype Forensics Postmortem Why DFIR Specialists Should Still Care
url: https://belkasoft.com/skype-forensics-postmortem
source: Instapaper: Unread
date: 2025-05-06
fetch_date: 2025-10-06T22:31:40.669864
---

# Skype Forensics Postmortem Why DFIR Specialists Should Still Care

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

# Skype Forensics Postmortem: Why DFIR Specialists Should Still Care

![](/images/blog/skype-forensics-postmortem-cover.jpg)

Microsoft will officially retire [Skype on May 5, 2025](https://www.microsoft.com/en-us/microsoft-365/blog/2025/02/28/the-next-chapter-moving-from-skype-to-microsoft-teams/). Once a dominant platform in online communication, Skype is now being replaced by Microsoft Teams. While this reflects a broader shift in enterprise communication, it does not make Skype forensics any less relevant. Legacy data from Skype may still surface in investigations involving long-term employees, archived backups, or older devices. That is why forensic tools must remain compatible with legacy applications.

In this article, we will explore:

* [Why Skype still matters for forensic investigations](#why-skype-forensic-legacy-matters)
* [Where to find Skype forensic artifacts and how to extract them](#where-to-find-skype-data)
* [Challenges involved in analyzing legacy data](#challenges-in-legacy-data-forensics)
* [How Belkasoft X helps you work with outdated applications like Skype](#belkasoft-x-for-legacy-data-analysis)

Deprecated and legacy software can still hold crucial evidence. Choosing the right tool ensures you do not miss it. Read on to explore how [Belkasoft X](/x) can extract valuable evidence from Skype data, even after the platform is decommissioned.

## Why Skype's legacy still matters

Launched in 2003, Skype became a cornerstone of internet-based communication. At its peak, it supported hundreds of millions of users and generated vast volumes of digital data—text messages, voice and video calls, shared files, and contact records.

Although Microsoft allows users to export their Skype data before shutdown, those exports will not include deleted records and may not provide reliable timestamps or other metadata essential for forensic timelines. When possible, investigators should rely on data remaining on dated systems.

![A person's hand holding a mobile phone that displays Skype's splash screen](/images/articles/skype-forensics-postmortem/skype-forensics-01-unsplash-image.jpeg)

*Image by Unsplash*

From a forensic perspective, legacy Skype artifacts continue to be valuable sources of evidence. They can help you:

* Reconstruct conversations
* Map user relationships
* Establish communication timelines
* Recover exchanged files or media

With billions of call minutes logged annually and hundreds of millions of users over two decades, the platform has left behind a large footprint. Many of these records are still available on older devices, and in many cases, they remain relevant.

Many organizations continue to rely on aging hardware due to budget constraints, software dependencies, or deferred upgrade cycles. As a result, DFIR specialists frequently encounter legacy systems where Skype is still installed and where evidence may still reside.

Furthermore, despite the individual users' shift towards newer messaging platforms like [WhatsApp](/android-whatsapp-forensics-analysis) and [Telegram](/ios-telegram-forensics-acquisition-and-database-analysis), some devices may still contain long-forgotten Skype installations and conversations having evidential value.

## Where to find Skype data

Although Microsoft offers data export tools before deprecation, exported files may not include deleted records, timestamps, or metadata critical to forensic timelines. Capturing data directly from its source on the target system, without using intermediate formats or tools that might alter it, remains highly important.

Skype predominantly saves its data in a central location called **main.db** or **skype.db.** It is an SQLite database found on both Windows and macOS computers, as well as mobile devices running Android or iOS. This file typically contains:

* **Chat logs:** The textual content of conversations.
* **Call history:** Details about incoming and outgoing calls, including timestamps, duration, and participants.
* **File transfers:** Records of files sent and received through Skype.
* **Contact lists:** Information about added contacts.

Depending on the configuration, Skype may also store voicemail, SMS data, geolocation metadata, and images shared through the interface.

![Belkasoft X's Artifacts window displaying a chat extracted from Skype](/images/articles/skype-forensics-postmortem/skype-forensics-02-skype-extraction-in-belkasoft-x.png)

*Skype chats extracted by Belkasoft X*

Additional files and structures may contain recoverable data:

* **main.db-journal:** A journal file used by SQLite for transactional integrity.
* **Freelists and unallocated space within the database:** Areas within the SQLite file that may contain remnants of deleted data.
* **User profile folders:** Directories containing configuration files and potentially shared media

Below is a breakdown of common locations for different systems. Locations may vary by operating system, Skype version, and user preferences.

**Windows**

| Version | Path | Contents |
| --- | --- | --- |
| **Older Skype** | %appdata%\​Skype\​<SkypeUsername>\ | main.db, config files |
| **Newer Skype** | %appdata%\​Microsoft\​Skype for Desktop\ | skype.db, config files |
| **Skype UWP** | %localappdata%\​Packages\​Microsoft.SkypeApp\_\*\​LocalState\​<SkypeUsername>\​LocalCache\​Roaming\​Microsoft\​Skype for Store\ | skype.db, config files, cacheLogs are mostly cloud-based |
| **Skype for Business** | %LocalAppData%\​Microsoft\​Office\\*\​Lync\  Registry: HKCU\​Software\​Microsoft\​Communicator, HKCU\​Software\​Microsoft\​Office\\*\​Lync | Chat history (Outlook), cache, logs, registry config |

**macOS**

| Version | Path | Contents |
| --- | --- | --- |
| **Older Skype** | ~/Library/​Application Support/​Skype/​<SkypeUsername>/  ~/Library/​Preferences/​com.skype.​skype.plist  ~/Library/​Caches/...