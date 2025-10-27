---
title: 3AM ransomware: what you need to know
url: https://www.tripwire.com/state-of-security/3am-ransomware-what-you-need-know
source: Graham Cluley
date: 2024-12-11
fetch_date: 2025-10-06T19:43:31.831971
---

# 3AM ransomware: what you need to know

[Skip to main content](#main-content)

[![Fortra](https://static.fortra.com/fortra-global-assets/fortra-logo-full.svg?l=512372746)
![Data Classification](https://static.fortra.com/fortra-global-assets/fortra-logo-small.svg?l=1326211232)

![Integrity and Compliance Monitoring](/themes/custom/tripwire/images/fta-integrity-and-compliance-monitoring-light.svg)](/ "Home")

[EN](/state-of-security/3am-ransomware-what-you-need-know)

[EN](/state-of-security/3am-ransomware-what-you-need-know)

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
3. 3AM Ransomware: What You Need To Know

# 3AM Ransomware: What You Need To Know

*Posted on December 10, 2024*

Image

[![3am-ransomware](/sites/default/files/2024-12/3am-ransomware.jpg)](https://www.tripwire.com/sites/default/files/2024-12/3am-ransomware.jpg "3am-ransomware")

Image

[![3am-ransomware](/sites/default/files/2024-12/3am-ransomware.jpg)](https://www.tripwire.com/sites/default/files/2024-12/3am-ransomware.jpg "3am-ransomware")

**What is 3AM?**

3AM (also known as ThreeAM) is a ransomware group that first emerged in late 2023. Like other ransomware threats, 3AM exfiltrates victims' data (threatening to release it publicly unless a ransom is paid) and encrypts the copies left on targeted organisations' computer systems.

**So it's the normal story with ransomware - exfiltrate, encrypt, extort?**

Pretty much - but there are some notable aspects of 3AM that are worthy of mentioning.

**Such as what?**

The 3AM ransomware is unusual in so much it is written in Rust. The Rust programming language was probably chosen by the ransomware's creators because it prioritises performance.

**Why does speed matter?**

If you have potentially millions of files to encrypt across a victim's network, speed matters a lot. The longer you take to steal and garble your victim's data, the greater the chance your attack might be noticed while it's happening and disrupted.

**Anything else notable about the 3AM ransomware?**

The 3AM ransomware renames encrypted files so they have a ".threeamtime" extension and adds a marker string of "0x666". It also wipes Volume Shadow copies to make recovery more difficult for victims. Furthermore, it appears that 3AM was initially developed as a "backup" for the notorious [LockBit ransomware](/state-of-security/lockbit-ransomware-what-you-need-know "LockBit ransomware - what you need to know").

**What do you mean by "backup"?**

Not "backup" as in a "backup of your data" unfortunately but rather as a "backup plan". It appears that 3AM would sometimes be deployed when a LockBit ransomware attack was not successfully deployed.

**As I recall LockBit had connections with Russia. So is that true of 3AM too?**

Yes, that's right. The authorities have named Dmitry Khoroshev, a Russian national, as the administrator of LockBit and even [offered a US $10 million reward](/state-of-security/hit-lockbit-fbi-waiting-help-you-over-7000-decryption-keys "Hit by LockBit? The FBI is waiting to help you with over 7,000 decryption keys") for information leading to his arrest. The cybercriminals behind 3AM appear to have strong links to LockBit, speak Russian, and mostly target Western-affiliated countries. 3AM has also been linked to the [BlackSuit ransomware](/state-of-security/blacksuit-ransomware-what-you-need-know "BlackSuit ransomware - what you need to know").

**I see. So how will I know if my systems have been attacked with the 3AM ransomware?**

3AM drops a ransom note on attacked systems, warning victims that their sensitive data has been stolen and proposing "a deal" to prevent it from being sold on the dark web.

Image

![3am-ransom-message](/sites/default/files/2024-12/3am-ransom-message.jpeg)

**Who has been bit by the 3AM ransomware?**

A number of organisations have fallen foul of 3 AM, including New York's [Brunsick Hospital Center](https://cybernews.com/news/brunswick-hospital-psychiatric-center-ransomware-attack-3am-threeam-new-york/ "Link to Cybernews article"), a Louisiana-based HVAC company, and the [city of Hoboken](https://www.nj.com/hudson/2024/12/massive-breach-social-security-numbers-health-info-and-much-more-stolen-in-hoboken-cyberattack.html "Link to NJ article"). The latter of those not only saw social security numbers, driver’s licenses, payroll, health and other personal data of Hoboken workers and residents leaked, but also erotic short stories found on an employee's computer.

**Ouch! That's embarrassing. Presumably, 3AM will release the stolen data if no payment is made?**

I'm afraid that does appear to be the case. 3AM's dark web leak site lists past victims and includes links to the sensitive stolen data.

Image

![3am-leaked-data](/sites/default/files/2024-12/3am-leaked-data.jpeg)

**So, what action should I take right now?**

The best thing to do is to ensure that you have hardened your defences *before* ransomware strikes. It would be wise to follow Tripwire's general [recommendations on how to protect your organisation from ransomware](/state-of-security/ransomware-on-the-rise-how-to-keep-your-company-safe "Ransomware on the Rise: How to Keep You & Your Company Safe"). Those include:

* making secure offsite backups.
* running up-to-date security solutions and ensuring that your computers are protected with the latest security patches against vulnerabilities.
* Restrict an attacker's ability to spread laterally through your organisation via network segmentation.
* using hard-to-crack unique passwords to protect sensitive data and accounts, as well as enabling multi-factor authentication.
* encrypting sensitive data wherever possible.
* reducing the attack surface by disabling functionality that your company does not need.
* educating and informing staff about the risks and methods used by cybercriminals to launch attacks and steal data.

Stay safe, and don't allow your organisation to be the next victim to fall foul of the 3AM ransomware group.

---

**Editor’s Note:** ***The opinions expressed in this guest author article are solely those of the contributor and do not necessarily reflect those of Tripwire.***

[![Graham Cluley](/sites/default/files/styles/thumbnail/public/2022-10/graham-cluley_profile_pic.jpg?itok=ffTH8VnN)](/profile/graham-cluley)

Meet the Expert

#### [Graham Cluley](/profile...