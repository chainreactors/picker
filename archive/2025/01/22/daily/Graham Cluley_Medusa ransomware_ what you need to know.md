---
title: Medusa ransomware: what you need to know
url: https://www.tripwire.com/state-of-security/medusa-ransomware-what-you-need-know
source: Graham Cluley
date: 2025-01-22
fetch_date: 2025-10-06T20:16:21.683232
---

# Medusa ransomware: what you need to know

[Skip to main content](#main-content)

[![Fortra](https://static.fortra.com/fortra-global-assets/fortra-logo-full.svg?l=747254669)
![Data Classification](https://static.fortra.com/fortra-global-assets/fortra-logo-small.svg?l=55630199)

![Integrity and Compliance Monitoring](/themes/custom/tripwire/images/fta-integrity-and-compliance-monitoring-light.svg)](/ "Home")

[EN](/state-of-security/medusa-ransomware-what-you-need-know)

[EN](/state-of-security/medusa-ransomware-what-you-need-know)

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
3. Medusa Ransomware: What You Need To Know

# Medusa Ransomware: What You Need To Know

*Posted on January 21, 2025*

Image

[![medusa-ransomware](/sites/default/files/2025-01/medusa-ransomware.jpg)](https://www.tripwire.com/sites/default/files/2025-01/medusa-ransomware.jpg "medusa-ransomware")

Image

[![medusa-ransomware](/sites/default/files/2025-01/medusa-ransomware.jpg)](https://www.tripwire.com/sites/default/files/2025-01/medusa-ransomware.jpg "medusa-ransomware")

**What is the Medusa ransomware?**

Medusa is a ransomware-as-a-service (RaaS) platform that first came to prominence in 2023. The ransomware impacts organisations running Windows, predominantly exploiting vulnerable and unpatched systems and hijacking accounts through initial access brokers.

**Initial access brokers?**

Initial access brokers (IABs) specialise in gaining unauthorised access to the networks of organisations, and then sell that access to other cybercriminals - such as ransomware gangs like Medusa.

**So the ransomware attackers may not be the ones who initially hacked you?**

Correct. IABs may be skilled at breaking into a network, but not necessarily be interested in stealing your data and/or negotiating a ransom. IABs enable ransomware gangs to attack multiple targets simultaneously, helping them to reduce the overall time it takes to deploy ransomware, increase the chances of success, and maximise their profits.

**And the attacks aren't spotted?**

Like any other malicious hackers, the Medusa attackers do their best to avoid detection. In the case of Medusa ransomware attacks, they appear to take advantage of the "living off the land" technique, where attackers use legitimate tools and resources already present on a victim's network to carry out malicious activities. Instead of relying on external malware, this technique mimics legitimate activity and helps the attackers to evade detection.

**So Medusa provides a platform for others to carry out ransomware attacks?**

Yes, their affiliates use the Medusa platform to launch the attacks, and when a ransom is received, it is shared between the different parties.

**And I guess what the ransomware does is the standard fare?**

Copies of sensitive files are exfiltrated by the attackers, and the versions left on the victim's systems are encrypted. The extension .MEDUSA is appended to the end of the names of encrypted files.

The ransomware also makes efforts to make recovery more difficult after an attack, wiping a form of Microsoft Windows data backups called volume shadow copies, and deleting files with backup programs such as Windows Backup.

In addition, virtual disk hard drives (VHDs) used by virtual machines are deleted. A ransom note is left, demanding payment for a decryption of the encrypted files - with the threat that the stolen files will be published if a ransom is not paid by a deadline.

Image

![medusa-ransomware-note](/sites/default/files/2025-01/medusa-ransomware-note.jpeg)

**Where are the stolen files published?**

Medusa, like many other ransomware gangs, operates a leak site on the dark web. The so-called "Medusa blog" publicises a list of hacked organisations, alongside a countdown informing the victims of their payment deadline.

Image

![medusa-blog](/sites/default/files/2025-01/medusa-blog.jpeg)

In addition to the dark web leak site, accessible via Tor, Medusa also publicises hacks and publishes stolen data on its public Telegram channel. Making it more accessible than many other ransomware groups.

**What types of organisation does Medusa target?**

Medusa targets a wide variety of industry sectors, but judging by those it has listed on its leak website those sectors most affected include high tech, manufacturing, and education. The largest proportion of Medusa's targets appear to be located in the United States, followed by the United Kingdom, Canada, Australia, France, and Italy. It's noticeable that organisations based in Belarus, Kazakhstan, Kyrgyzstan, Russia, and Tajikistan do not appear in the list of victims.

**Presumably the lack of attacks on CIS countries is quite intentional?**

It's hard to argue otherwise. That's small consolation, of course, for those organisations based in countries that Medusa has no qualms about attacking.

**What organisations have been hit by Medusa?**

Past victims have included Minneapolis Public Schools (MPS) district, which failed to pay a million-dollar ransom and saw approximately [92 GB of its stolen data released to the public](https://www.the74million.org/article/days-after-missed-ransomware-deadline-stolen-mn-schools-files-appear-online/ "Link to media report"). It has also [bragged](https://www.theregister.com/2023/04/19/medusa_microsoft_data_dump/ "Link to The Register article") about stealing the source code of the Microsoft products Bing Maps and Cortona in the past. Other Medusa ransomware victims have included [cancer centres](https://theconversation.com/a-cancer-centre-is-the-latest-victim-of-cyber-attacks-why-health-data-hacks-keep-happening-205131 "Link to The Conversation article"), and [British high schools](https://www.theregister.com/2025/01/20/blacon_high_school_ransomware/ "Link to The Register article").

**And these ransomware victims have had their data leaked by Medusa?**

Yes, and not just on the group's site on the dark web. Medusa has its own "media team" that publicises its leaks, posting on its public Telegram channel, and even going so far as to publish videos showing evidence of stolen data.

**So how can my company protect itself from Medusa?**

The [best advice](https://tripwire.com/state-of-security/ransomware-on-the-rise-how-to-keep-your-company-safe) is to follow the same recommendations on [how to protect...