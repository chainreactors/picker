---
title: Mimic ransomware: what you need to know
url: https://www.tripwire.com/state-of-security/mimic-ransomware-what-you-need-know
source: Graham Cluley
date: 2024-11-29
fetch_date: 2025-10-06T19:20:03.608047
---

# Mimic ransomware: what you need to know

[Skip to main content](#main-content)

[![Fortra](https://static.fortra.com/fortra-global-assets/fortra-logo-full.svg?l=320109643)
![Data Classification](https://static.fortra.com/fortra-global-assets/fortra-logo-small.svg?l=533428582)

![Integrity and Compliance Monitoring](/themes/custom/tripwire/images/fta-integrity-and-compliance-monitoring-light.svg)](/ "Home")

[EN](/state-of-security/mimic-ransomware-what-you-need-know)

[EN](/state-of-security/mimic-ransomware-what-you-need-know)

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
3. Mimic Ransomware: What You Need To Know

# Mimic Ransomware: What You Need To Know

*Posted on November 28, 2024*

Image

[![mimic](/sites/default/files/2024-11/mimic.jpg)](https://www.tripwire.com/sites/default/files/2024-11/mimic.jpg "mimic")

Image

[![mimic](/sites/default/files/2024-11/mimic.jpg)](https://www.tripwire.com/sites/default/files/2024-11/mimic.jpg "mimic")

**What is Mimic?**

Mimic is family of ransomware, first found in-the-wild in 2022. In common with many other ransomware attacks, Mimic encrypts a victim's files, and demands a ransom payment in cryptocurrency for the release of a decryption key.

**Does Mimic also steal data?**

Yes, some variants of Mimic can also exfiltrate data from a user's computers before it is encrypted - the stolen data is typically used as an additional bargaining chip by the extortionists, who may threaten to release it online or sell it to other criminals.

**Where did Mimic come from?**

Mimic reuses code from the Conti ransomware, which was [leaked](https://grahamcluley.com/conti-ransomware-which-leaked-ransomware-victims-data-has-its-own-data-leaked/) after the Conti gang [publicly announced](https://grahamcluley.com/conti-ransomware-gang-you-attack-russia-well-hack-you-back/) its support for Russia's invasion of Ukraine. Unfortunately it is not possible to confidently say which part of the world Mimic originates from, but it does appear that it specifically targets English and Russian speakers.

**So what makes Mimic noteworthy?**

What makes Mimic particularly unusual is that it exploits the API of a legitimate Windows file search tool ("Everything" by Voidtools) to quickly locate files for encryption.

Image

![everything](/sites/default/files/2024-11/everything.jpeg)

**Phew! I don't use Everything. In fact, I've never heard of it**

Unfortunately, the Mimic ransomware doesn't rely upon your computer having the Everything app installed. The ransomware typically comes packaged with Everything, as well as programs to impair the effectiveness of Windows Defender and Sysinternals' Secure Delete tool, which is used to wipe backups and hinder recovery.

**Nasty. What are the makers of Voidtools doing about this?**

There isn't much Voidtools can do about this. There's nothing wrong with the Everything app - it is just being abused by the ransomware to accerate the process of encrypting files. It's the same story for Secure Delete, which is being exploited to erase backup copies of data.

**So how will I know if my computer systems have been infected with Mimic?**

Files encrypted by the Mimic ransomware are given the “.QUIETPLACE” extension. You could always use a tool like Everything to quickly determine if you have any files that have that extension. :) Mimic also leaves a ransom note that US $3000 worth of cryptocurrency in exchange for the decryption key.

Image

![ransom](/sites/default/files/2024-11/ransom.jpeg)

**What can expect in the future from Mimic?**

Well, a new variant of Mimic has recently been discovered called Elpaco, which has been used in attacks where malicious hackers accessed victims' systems via RDP after successfully brute-forcing their way in. According to security experts, the attackers were able to escalate their privileges through [exploitation of the "Zerologon" (CVE-2020-1472) vulnerability](/state-of-security/22-ransomware-prevention-tips "Link to SecureList blog post").

Image

![elpaco-ransom-note](/sites/default/files/2024-11/elpaco-ransom-note.jpeg)

Security researchers [say](/state-of-security/22-ransomware-prevention-tips "Link to Cyfirma blog post") that they have received reports of Mimic's Elpaco variant from Russia and South Korea.

**So the threat continues to evolve. What should I do to defend my systems?**

Here are [30 ransomware prevention tips](/state-of-security/22-ransomware-prevention-tips "30 Ransomware Prevention Tips") that can help prevent a ransomware infection from succeeding in your organisation.

---

**Editor's Note: The opinions expressed in this and other guest author articles are solely those of the contributor and do not necessarily reflect those of Tripwire.**

[![Graham Cluley](/sites/default/files/styles/thumbnail/public/2022-10/graham-cluley_profile_pic.jpg?itok=ffTH8VnN)](/profile/graham-cluley)

Meet the Expert

#### [Graham Cluley](/profile/graham-cluley)

Cybercrime Researcher and Blogger

[View Profile](/profile/graham-cluley)

Related Solutions

[Cybersecurity](/resources?f%5B0%5D=topic%3A2275)

Related Content

Blog

[ShrinkLocker Ransomware: What You Need To Know](/state-of-security/shrinklocker-ransomware-what-you-need-know)

Blog

[NotLockBit: Ransomware Discovery Serves As Wake-Up Call For Mac Users](/state-of-security/notlockbit-rransomware-discovery-serves-wake-call-mac-users)

[![Fortra logo](/themes/custom/fortra_parent_2022/images/logo.svg)](https://www.fortra.com "Home")

* +1 800-328-1000
* [Email Us](/cdn-cgi/l/email-protection#5831363e37183e372a2c2a39763b3735)
* [Request Support](/support)

* [X Find us on
  X](https://twitter.com/tripwireinc)
* [LinkedIn Find us on
  LinkedIn](https://www.linkedin.com/company/tripwire/%20class%3D)
* [Youtube Find us on
  Youtube](https://www.youtube.com/user/tripwireinc)
* [Reddit Find us on Reddit](https://www.reddit.com/r/Fortra/)

Footer menu

### [Products & Services](/products)

* [Tripwire Enterprise](https://www.tripwire.com/products/tripwire-enterprise)
* [Tripwire IP360](/products/tripwire-ip360)
* [Tripwire LogCenter](/products/tripwire-logcenter)
* [Tripwire ExpertOps](/products/tripwire-expertops)
* [Services](/services)
* [View All Products](/products)
* [Fortra Products](/products/fortra)

### [Solutions](/solutions)

* [By Security Need](/solutions)
* [By ...