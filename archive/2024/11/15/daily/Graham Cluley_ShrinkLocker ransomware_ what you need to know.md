---
title: ShrinkLocker ransomware: what you need to know
url: https://www.tripwire.com/state-of-security/shrinklocker-ransomware-what-you-need-know
source: Graham Cluley
date: 2024-11-15
fetch_date: 2025-10-06T19:22:19.813152
---

# ShrinkLocker ransomware: what you need to know

[Skip to main content](#main-content)

[![Fortra](https://static.fortra.com/fortra-global-assets/fortra-logo-full.svg?l=859342710)
![Data Classification](https://static.fortra.com/fortra-global-assets/fortra-logo-small.svg?l=282076459)

![Integrity and Compliance Monitoring](/themes/custom/tripwire/images/fta-integrity-and-compliance-monitoring-light.svg)](/ "Home")

[EN](/state-of-security/shrinklocker-ransomware-what-you-need-know)

[EN](/state-of-security/shrinklocker-ransomware-what-you-need-know)

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
3. ShrinkLocker Ransomware: What You Need To Know

# ShrinkLocker Ransomware: What You Need To Know

*Posted on November 14, 2024*

Image

[![shrinklocker](/sites/default/files/2024-11/shrinklocker.jpg)](https://www.tripwire.com/sites/default/files/2024-11/shrinklocker.jpg "shrinklocker")

Image

[![shrinklocker](/sites/default/files/2024-11/shrinklocker.jpg)](https://www.tripwire.com/sites/default/files/2024-11/shrinklocker.jpg "shrinklocker")

**What is ShrinkLocker?**

ShrinkLocker is a family of ransomware that encrypts an organisation's data and demands a [ransom payment](/state-of-security/75-million-record-breaking-ransom-paid-cybercriminals-say-researchers "$75 Million Record-Breaking Ransom Paid To Cybercriminals, Say Researchers") in order to restore access to their files. It was first identified by security researchers in May 2024, after attacks were observed in Mexico, Indonesia, and Jordan.

**So far, so normal. What makes it noteworthy?**

The ShrinkLocker ransomware is unusual because it uses VBScript and Microsoft Windows's legitimate security tool BitLocker to assist with the encryption of victims' files.

**Hang on. You mean BitLocker, the full-disk-encryption feature that's supposed to** ***boost*** **security by preventing anyone without proper authentication from accessing your files?**

That's the one. Ironic isn't it? BitLocker, for anyone who doesn't know, is a feature built into Windows that uses strong encryption to scramble data on your computer's hard drive. If you don't know the password to unlock a computer, you can't access its data.

**Which is great if your laptop is stolen by a thief...**

...but not so good if ShrinkLocker is the one that's chosen to scramble your data with Bitlocker, and not told you the password it used. Your computer won't be able to tell the difference between you and a thief - and keep you both locked out. Anyone starting up the computer will be faced with the standard BitLocker prompt for a password.

**Has BitLocker been used in this way before by cybercriminals?**

Yes, for instance in January 2021 a Belgian hospital had [100TB of its data encrypted on 40 of its servers](https://www.bleepingcomputer.com/news/security/chwapi-hospital-hit-by-windows-bitlocker-encryption-cyberattack/ "Link to Bleeping Computer article") using BitLocker. The following year a Moscow-based meat producer and distributor [reportedly](https://www.bleepingcomputer.com/news/security/top-russian-meat-producer-hit-with-windows-bitlocker-encryption-attack/ "Link to Bleeping Computer article") had its systems encrypted by a malicious attacker using BitLocker.

Perhaps the most high-profile abuse of the built-in BitLocker tool has been by the Iranian cybercrime gang Storm-0270 (also known as Nemesis Kitten), which Microsoft claimed in September 2022 had been [responsible for multiple ransomware attacks](https://www.microsoft.com/en-us/security/blog/2022/09/07/profiling-dev-0270-phosphorus-ransomware-operations/ "Link to Microsoft blog").

**So, does ShrinkLocker leave a ransom note?**

No, instead it changes the names of all of your system drives to a contact address for the attacker.

**So how do I get my hands on the password without paying up?**

Unfortunately, the password used to encrypt your drive has been stored on the attacker's own server.

But the good news is that security firm Bitdefender has released a [free decryption tool](https://www.bitdefender.com/en-us/blog/businessinsights/shrinklocker-decryptor-from-friend-to-foe-and-back-again "Link to free decryption tool for ShrinkLocker ransomware") that can help ShrinkLocker victims recover their files.

---

**Editor’s Note:** ***The opinions expressed in this guest author article are solely those of the contributor and do not necessarily reflect those of Tripwire.***

[![Graham Cluley](/sites/default/files/styles/thumbnail/public/2022-10/graham-cluley_profile_pic.jpg?itok=ffTH8VnN)](/profile/graham-cluley)

Meet the Expert

#### [Graham Cluley](/profile/graham-cluley)

Cybercrime Researcher and Blogger

[View Profile](/profile/graham-cluley)

Related Solutions

[Cybersecurity](/resources?f%5B0%5D=topic%3A2275)

Related Content

Blog

[DragonForce Ransomware - What You Need To Know](/state-of-security/dragonforce-ransomware-what-you-need-know)

Blog

[Cicada Ransomware - What You Need To Know](/state-of-security/cicada-ransomware-what-you-need-know)

Blog

[Qilin Ransomware: What You Need To Know](/state-of-security/qilin-ransomware-what-you-need-know)

[![Fortra logo](/themes/custom/fortra_parent_2022/images/logo.svg)](https://www.fortra.com "Home")

* +1 800-328-1000
* [Email Us](/cdn-cgi/l/email-protection#234a4d454c63454c515751420d404c4e)
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
* [By Compliance Need](/solutions/compliance)
* [By Industry](/industries)

### [Resources](/resources)

* [Upcoming Events](/resources?f%5B0%5D=type%3A1333&f%5B1%5D=type%3A1340&f%5B2%5D=type%3A1341)
* [On-Demand Webinars](/resources?f%5B0%5D=type%3A1342)
* [Datasheets...