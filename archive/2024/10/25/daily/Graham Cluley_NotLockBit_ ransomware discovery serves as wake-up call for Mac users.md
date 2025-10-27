---
title: NotLockBit: ransomware discovery serves as wake-up call for Mac users
url: https://www.tripwire.com/state-of-security/notlockbit-rransomware-discovery-serves-wake-call-mac-users
source: Graham Cluley
date: 2024-10-25
fetch_date: 2025-10-06T18:59:45.715150
---

# NotLockBit: ransomware discovery serves as wake-up call for Mac users

[Skip to main content](#main-content)

[![Fortra](https://static.fortra.com/fortra-global-assets/fortra-logo-full.svg?l=513534936)
![Data Classification](https://static.fortra.com/fortra-global-assets/fortra-logo-small.svg?l=307010034)

![Integrity and Compliance Monitoring](/themes/custom/tripwire/images/fta-integrity-and-compliance-monitoring-light.svg)](/ "Home")

[EN](/state-of-security/notlockbit-rransomware-discovery-serves-wake-call-mac-users)

[EN](/state-of-security/notlockbit-rransomware-discovery-serves-wake-call-mac-users)

Secondary Navigation

* [Customer Portal](https://customers.tripwire.com/customers)
* [Partner Portal](https://partners.tripwire.com/partners/)
* [GET A DEMO](/demo)

* Products
  Toggle Dropdown
  + [Tripwire Enterprise](/products/tripwire-enterprise)
  + [Tripwire ExpertOps](/products/tripwire-expertops)
  + [Tripwire IP360](/products/tripwire-ip360)
  + [Tripwire LogCenter](/products/tripwire-logcenter)
  + [View all products](/products)
* Solutions
  Toggle Dropdown
  + [Security Configuration Management](/solutions/security-configuration-management)
  + [File Integrity and Change Monitoring](/solutions/file-integrity-and-change-monitoring)
  + [Vulnerability Management](/solutions/vulnerability-and-risk-management)
  + [Cloud](/solutions/cloud-cybersecurity)
  + [Compliance](/solutions/compliance)
  + [Industries](/industries)
  + [View all solutions](/solutions)
* [Services](/services)
* Resources
  Toggle Dropdown
  + [Upcoming Events](/resources?f%5B0%5D=type%3A1333&f%5B1%5D=type%3A1340&f%5B2%5D=type%3A1341)
  + [On-Demand Webinars](/resources?f%5B1%5D=type%3A1339&f%5B2%5D=type%3A1342)
  + [Datasheets](/resources?f%5B0%5D=type%3A1335)
  + [Case Studies](/resources?f%5B0%5D=type%3A1334)
  + [Guides](/resources?f%5B0%5D=type%3A1337)
  + [Training](/services/training)
  + [View all resources](/resources)
* [Blog](/state-of-security)
* About
  Toggle Dropdown
  + [About](/about)
  + [Careers](https://www.fortra.com/about/careers)
  + [Leadership](https://www.fortra.com/about/our-leadership-team)
  + [Newsroom](https://www.fortra.com/about/newsroom)
  + [Partners](/about/partner)
  + [Contact Us](/contact-us)

Keywords

Sort
Best matchNewest firstOldest firstTitle A-ZTitle Z-A

1. [Home](/)
2. [Blog](/state-of-security)
3. NotLockBit: Ransomware Discovery Serves As Wake-Up Call For Mac Users

# NotLockBit: Ransomware Discovery Serves As Wake-Up Call For Mac Users

*Posted on October 24, 2024*

Image

[![unhappy-mac](/sites/default/files/2024-10/unhappy-mac.jpg)](https://www.tripwire.com/sites/default/files/2024-10/unhappy-mac.jpg "unhappy-mac")

Image

[![unhappy-mac](/sites/default/files/2024-10/unhappy-mac.jpg)](https://www.tripwire.com/sites/default/files/2024-10/unhappy-mac.jpg "unhappy-mac")

Historically, Mac users haven't had to worry about malware as much as their Windows-using cousins.

Although malware targeting Apple devices actually predates viruses written for PCs, and there have been some families of malware that have presented a significant threat for both operating systems (for instance, the Word macro viruses that hit computers hard from 1995 onwards), it is generally the case that you're simply a lot less likely to encounter malware on your Mac than you are on your Windows PC.

But that doesn't mean that Mac users should be complacent. And the recent discovery of a new malware strain emphasises that the threat - even if much smaller than on Windows - remains real.

Security researchers at SentinelOne have [warned](https://www.sentinelone.com/blog/macos-notlockbit-evolving-ransomware-samples-suggest-a-threat-actor-sharpening-its-tools/) that the new malware, dubbed "NotLockBit", is targeting macOS systems - suggesting that cybercriminals are looking for victims who may have made the mistake of being more relaxed about their computer security.

Although it was initially suspected that the malware was linked to the notorious LockBit ransomware gang, further analysis suggests that the threat is a distinct strain falsely claiming affiliation.

In what could almost be described as a "false-flag" operation, NotLockBit uses LockBit's signature desktop wallpaper in what seems to be an attempt to mislead victims and security researchers of its origin.

Image

![notlockbit](/sites/default/files/2024-10/notlockbit.jpeg)

NotLockBit claims to be version 2.0, and yet LockBit 3.0 was released some time ago, and key members of the LockBit gang have been [arrested and its infrastructure seized](/state-of-security/lockbit-ransomware-what-you-need-know "LockBit ransomware - what you need to know").

Previous ransomware threats against macOS users have been largely [proof-of-concept](https://www.vice.com/en/article/we-now-have-proof-that-macs-can-get-ransomware/) or have [not become widespread](/state-of-security/destructive-mac-ransomware-spread-cracks-pirate-commercial-software "Destructive Mac ransomware spread as cracks to pirate commercial software").

The genuine LockBit ransomware group was responsible for producing a [version of its ransomware for macOS](https://grahamcluley.com/lockbit-ransomware-for-mac-coming-soon/) last year, but because it was buggy and crashed easily it was not considered a serious threat.

The new malware analysed by SentinelOne's researchers has been distributed as an x86-64 binary - meaning that it will only run on Intel-based Macs and Macs using the Rosetta emulation service.

According to experts NotLockBit appears to be "very much in development," and there are currently no known victims of the malware or evidence that it is being actively distributed in the wild.

But if you were to encounter NotLockBit, on a Mac that could run it, then it would attempt to exfiltrate files from your computer to AWS cloud storage buckets, encrypting data left behind on your Mac and adding a .abcd suffix to their filenames.

The immediate threat of this particular ransomware sample has been reduced by its discovery, after the threat actors brought it to the attention of researchers by uploading to VirusTotal (seemingly in an attempt to see if any anti-virus products would detect it as malicious).

That act prompted the security community to take action, and the AWS accounts used by the hackers during the data-exfiltration process have been removed.

But we would be foolish to think that more work won’t be done on this and other Mac ransomware in the months and years ahead. As ever, companies whose workers use Macs would be wise to protect them with security solutions to reduce the chance of them being the weak link through which a malicious hacker can wreak havoc throughout an organisation.

---

**Editor’s Note:** ***The opinions expressed in this guest author article are solely those of the contributor and do not necessarily reflect those of Tripwire.***

[![Graham Cluley](/sites/default/files/styles/thumbnail/public/2022-10/graham-cluley_profile_pic.jpg?itok=ffTH8VnN)](/profile/graham-cluley)

Meet the Expert

#### [Graham Cluley](/profile/graham-cluley)

Cybercrime Researcher and Blogger

[View Profile](/profile/graham-cluley)

Related Solutions

[Cybersecurity](/resources?f%5B0%5D=topic%3A2275)

Related Content

Blog

[Glimmer Of Good News On The Ransomware Front As Encryption Rates Plummet](/state-of-security/glimmer-good-news-ransomware-front-encryption-rates-plummet)

Blog

[30 Ransomware Prevention Tips](/state-of-security/22-ransomware-prevention-tips)

[![Fortra logo](/themes/custom/fortra_parent_2022/images/logo.svg)](https://www.fortra.com "Home")

* +1 800-328-1000
* [Email Us](/cdn-cgi/l/email-protection#771e191118371118050305165914181a)
* [Request Support](/support)

* [X Find us on
  X](https://twitter.com/tripwireinc)
* [LinkedIn Find us on
  LinkedIn](https://www.linkedin.com/company/tripwire/%20class%3D)
* [Youtube Find us on
  Youtube](https://www.youtube.com/user/tripwireinc)
* [Reddit Find us on Reddit](https://www.reddit.com/r/Fortra/)

Footer menu

### [Products & Services...