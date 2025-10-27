---
title: SEXi / APT Inc ransomware – what you need to know
url: https://www.tripwire.com/state-of-security/sexi-apt-inc-ransomware-what-you-need-know
source: Graham Cluley
date: 2024-07-26
fetch_date: 2025-10-06T17:48:52.855151
---

# SEXi / APT Inc ransomware – what you need to know

[Skip to main content](#main-content)

[![Fortra](https://static.fortra.com/fortra-global-assets/fortra-logo-full.svg?l=1911914025)
![Data Classification](https://static.fortra.com/fortra-global-assets/fortra-logo-small.svg?l=1494782003)

![Integrity and Compliance Monitoring](/themes/custom/tripwire/images/fta-integrity-and-compliance-monitoring-light.svg)](/ "Home")

[EN](/state-of-security/sexi-apt-inc-ransomware-what-you-need-know)

[EN](/state-of-security/sexi-apt-inc-ransomware-what-you-need-know)

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
3. SEXi / APT Inc Ransomware - What You Need To Know

# SEXi / APT Inc Ransomware - What You Need To Know

*Posted on July 25, 2024*

Image

[![sexi](/sites/default/files/2024-07/sexi.jpg)](https://www.tripwire.com/sites/default/files/2024-07/sexi.jpg "sexi")

Image

[![sexi](/sites/default/files/2024-07/sexi.jpg)](https://www.tripwire.com/sites/default/files/2024-07/sexi.jpg "sexi")

**SEXi? Seriously? What are you talking about this time?**

Don't worry, I'm not trying to conjure images in your mind of Rod Stewart in his iconic leopard print trousers. Instead, I want to warn you about a cybercrime group that has gained notoriety for attacking VMware ESXi servers since February 2024.

**Excuse me for not knowing, but what is VMWare EXSi?**

EXSi is a hypervisor - allowing businesses who want to reduce costs and simplify management to consolidate multiple servers onto a single physical machine.

ESXi is a popular choice with cloud providers and data centres that have a require to host thousands of virtual machines for their customers, but there are also use cases in healthcare, finance, education, and other sectors.

**So the SEXi gang breaks into EXSi servers and encrypts the data?**

That's correct. For instance, in April Chilean data centre and hosting provider IxMetro PowerHost had its [VMware ESXi servers and backups encrypted](https://www.bleepingcomputer.com/news/security/hosting-firms-vmware-esxi-servers-hit-by-new-sexi-ransomware/ "Link to Bleeping Computer article"). The attackers demanded a ransom of $140 million worth of Bitcoin.

**140 million dollars? Sheesh!**

It's a lot isn't, isn't it? Apparently, the ransomware group calculated the figure by demanding two Bitcoins for every PowerHost customer whose data had been encrypted.

Apparently, the ransomware group calculated the figure by demanding two Bitcoins for every customer of PowerHost who had had their data encrypted.

PowerHost's CEO says that he personally negotiated with the attackers, described the demand as "exorbitant", and refused to pay up.

**So how do you know if your computers have, err.. got SEXi?**

Encrypted files have their filenames appended with ".SEXi". Files related to virtual machines, such as virtual disks, storage, and backup images, are targeted.

In addition, a ransom note is dropped onto affected systems called SEXi.txt.

Image

![sexi message](/sites/default/files/2024-07/sexi-message.jpeg)

The ransom message tells victims to download the end-to-end encrypted messaging app Session, and make contact with the extortionists.

**Are there any known weaknesses in the encryption used in the SEXi attacks that could be used to recover your data without paying?**

Unfortunately not, and so there are no freely available tools to recover encrypted data. Businesses hit by SEXi ransomware attacks have to hope that they have made a backup of critical data that has not been compromised by the cybercriminals.

**None of this sounds very SEXI at all...**

I agree. And maybe the attackers do too. From last month onwards they appear to have attempted to rebrand themselves with the slightly less disturbing name of "APT Inc." Which, of course, means an update to the ransom note - although not much has changed in the way the criminals operate.

Image

![apt-inc-message](/sites/default/files/2024-07/apt-inc-message.jpeg)

**What can my company do to better protect its VMware EXSi servers?**

You can significantly strengthen the security of your VMware ESXi environment and protect valuable data by following these steps:

* Update and patch your VMware EXSi systems against vulnerabilities.
* Disable the default root account and create separate user accounts granting users only the permissions they need.
* Make sure that passwords are strong, cannot be guessed or cracked, and are unique.
* Proactively monitor and log events to detect potential security breaches.

For further advice, read [VMware's recommendations for securing EXSi](https://docs.vmware.com/en/VMware-vSphere/7.0/com.vmware.vsphere.security.doc/GUID-B39474AF-6778-499A-B8AB-E973BE6D4899.html).

---

**Editor’s Note: The opinions expressed in this guest author article are solely those of the contributor and do not necessarily reflect those of Tripwire.**

[![Graham Cluley](/sites/default/files/styles/thumbnail/public/2022-10/graham-cluley_profile_pic.jpg?itok=ffTH8VnN)](/profile/graham-cluley)

Meet the Expert

#### [Graham Cluley](/profile/graham-cluley)

Cybercrime Researcher and Blogger

[View Profile](/profile/graham-cluley)

Related Solutions

[Cybersecurity](/resources?f%5B0%5D=topic%3A2275)

Related Content

Blog

[30 Ransomware Prevention Tips](/state-of-security/22-ransomware-prevention-tips)

Blog

[HardBit Ransomware - What You Need To Know](/state-of-security/hardbit-ransomware-what-you-need-know)

Blog

[RansomHub Ransomware - What You Need To Know](/state-of-security/ransomhub-ransomware-what-you-need-know)

[![Fortra logo](/themes/custom/fortra_parent_2022/images/logo.svg)](https://www.fortra.com "Home")

* +1 800-328-1000
* [Email Us](/cdn-cgi/l/email-protection#e78e898188a7818895939586c984888a)
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
* [...