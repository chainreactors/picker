---
title: DNS Triage Cheatsheet
url: https://www.blackhillsinfosec.com/dns-triage-cheatsheet/
source: Black Hills Information Security, Inc.
date: 2025-08-07
fetch_date: 2025-10-07T00:48:14.893476
---

# DNS Triage Cheatsheet

[![Black Hills Information Security, Inc.](https://www.blackhillsinfosec.com/wp-content/uploads/2025/03/BHIS_TEXT_BHIS.png)](https://www.blackhillsinfosec.com "Black Hills Information Security, Inc.")

[RSS](https://www.blackhillsinfosec.com/feed/)

* [All Services](https://www.blackhillsinfosec.com/services/)
  + [Complete Service Guide](https://www.blackhillsinfosec.com/services/complete-service-guide/)
  + [Active SOC](https://www.blackhillsinfosec.com/services/active-soc/)
  + [AI Security Assessments](https://www.blackhillsinfosec.com/services/ai-security-assessments/)
  + [Blockchain Security](https://www.blackhillsinfosec.com/services/blockchain-security/)
  + [Blue Team Services](https://www.blackhillsinfosec.com/services/blue-team-services/)
  + [Continuous Penetration Testing](https://www.blackhillsinfosec.com/services/antisoc/)
  + [High-Profile Risk Assessments](https://www.blackhillsinfosec.com/services/high-profile-risk-assessments/)
  + [Incident Response](https://www.blackhillsinfosec.com/services/incident-response/)
  + [Penetration Testing](https://www.blackhillsinfosec.com/services/)
* [Contact Us](https://www.blackhillsinfosec.com/contact-us/)
  + [Contact Us](https://www.blackhillsinfosec.com/contact-us/)
  + [Email Sign-Up](https://mailchi.mp/blackhillsinfosec.com/bhis-sign-up)
* [About Us](https://www.blackhillsinfosec.com/who-we-are/)
  + [Security Consultants](https://www.blackhillsinfosec.com/about/security-analysts/)
  + [Admin](https://www.blackhillsinfosec.com/about/admin-staff/)
  + [SOC Team](https://www.blackhillsinfosec.com/about/soc-team/)
  + [BHIS Family of Companies](https://www.blackhillsinfosec.com/bhis-tribe-of-companies/)
* [Free Resources](https://www.blackhillsinfosec.com/free-cybersecurity-tools/)
  + [Blogs](https://www.blackhillsinfosec.com/blog/)
  + [Free Cybersecurity Tools](https://www.blackhillsinfosec.com/free-cybersecurity-tools/)
  + [Free Cybersecurity Webcasts](https://www.blackhillsinfosec.com/free_cybersecurity_webcasts/)
  + [Podcasts](https://podcasts.apple.com/us/podcast/black-hills-information-security/id1410835265)
  + [RITA](https://www.activecountermeasures.com/free-tools/rita/)
* [Training](https://www.blackhillsinfosec.com/bhis-and-antisyphon-training/)
  + [BHIS & Antisyphon Training](https://www.blackhillsinfosec.com/bhis-and-antisyphon-training/)
  + [WWHF Conference](https://wildwesthackinfest.com)
* [Online Community](https://blackhillsinfosec.com/community)
  + [Discord](https://discord.gg/BHIS)
  + [LinkedIn](https://www.linkedin.com/company/black-hills-information-security/)
  + [YouTube](https://www.youtube.com/c/BlackHillsInformationSecurity/videos)
  + [Bluesky](https://bsky.app/profile/bhinfosecurity.bsky.social)
  + [Twitter/X](https://twitter.com/BHinfoSecurity)
  + [Upcoming Events](https://blackhillsinfosec.com/events)
* [Fun Stuff](https://spearphish-general-store.myshopify.com/)
  + [Backdoors & Breaches](https://www.blackhillsinfosec.com/tools/backdoorsandbreaches/)
  + [Merch, Zines & More](https://spearphish-general-store.myshopify.com/)
  + [PROMPT# Zine](https://www.blackhillsinfosec.com/prompt-zine/)
  + [REKCAH](https://www.blackhillsinfosec.com/rekcah/)
  + [Books](https://www.blackhillsinfosec.com/tools/books/)

6
Aug
2025

[General InfoSec Tips & Tricks](https://www.blackhillsinfosec.com/category/infosec-101/general-infosec-tips-tricks/), [Informational](https://www.blackhillsinfosec.com/category/informational/), [InfoSec 101](https://www.blackhillsinfosec.com/category/infosec-101/), [Michael Allen](https://www.blackhillsinfosec.com/category/author/michael-allen/), [Red Team Tools](https://www.blackhillsinfosec.com/category/red-team/tool-red-team/)
[Cheatsheet](https://www.blackhillsinfosec.com/tag/cheatsheet/), [DNS Triage](https://www.blackhillsinfosec.com/tag/dns-triage/), [Infosec for Beginners](https://www.blackhillsinfosec.com/tag/infosec-for-beginners/), [InfoSec Survival Guide](https://www.blackhillsinfosec.com/tag/infosec-survival-guide/)

# [DNS Triage Cheatsheet](https://www.blackhillsinfosec.com/dns-triage-cheatsheet/)

Written by [Michael Allen](http://linkedin.com/in/wh1t3rh1n0) || Reviewed by [Dale Hobbs](https://www.linkedin.com/in/dale-hobbs/)

![](https://www.blackhillsinfosec.com/wp-content/uploads/2025/08/BLOG_cheatsheet_10.png)

**This blog is part of **Offensive Tooling Cheatsheets: An Infosec Survival Guide Resource**. You can learn more and find all of the cheatsheets HERE:** **<https://www.blackhillsinfosec.com/offensive-tooling-cheatsheets/>**

**DNS Triage Cheatsheet**: [PRINT-FRIENDLY PDF](https://www.blackhillsinfosec.com/wp-content/uploads/2025/08/CheetSheet_DNSTriage.pdf)

Find the tool here: <https://github.com/Wh1t3Rh1n0/dns-triage>

---

## What is it?

*Fast, actionable, tech reconnaissance for attackers.*

DNS Triage is a reconnaissance tool that finds information about an organization’s infrastructure, software, and third-party services *as fast as possible*. The goal of DNS Triage is not to exhaustively find every technology asset that exists on the internet. The goal is to find the most commonly abused items of interest for real attackers.

## How does it work?

DNS Triage uses a combination of DNS queries and web requests to collect interesting information. Specifically:

1. It gathers TXT, MX, and NS records of the target domain.
2. It queries DNS records of commonly abused Microsoft services and checks whether they are hosted in Microsoft’s cloud or on-premises.
3. It resolves a hand-picked selection of very common subdomains on the target domain, where abusable services and infrastructure are often found.
4. It makes targeted DNS and/or HTTP queries of third-party services to determine which services are used by the organization.
5. Whenever possible, it displays additional details that may be useful for abusing the resources that have been discovered.

## How do I install it?

1. Download and extract the ZIP archive from the project repository at <https://github.com/Wh1t3Rh1n0/dns-triage> or run the following command to download DNS Triage with git:

```
  git clone https://github.com/Wh1t3Rh1n0/dns-triage
```

2. Open a terminal window in the folder where you downloaded/extracted the DNS Triage files, and run the following command to install Python libraries used by DNS Triage:

```
 python3 -m pip install -r requirements.txt
```

## How do I use it?

The recommended way to launch DNS Triage is simply to run dns-triage.py command followed by the domain name that you want to target. An example command targeting example.com is shown below.

```
python3 dns-triage.py example.com
```

***Tip:*** *Help documentation describing other additional options can be shown by running DNS Triage without specifying any other arguments.*

## What does all the output mean?

DNS Triage can sometimes generate a *lot* of output. Here are some examples of the output it displays and key information you should look for.

### **TXT Records**

Clues in TXT records often reveal technology products and services used by the organization. This information can be very useful, both for social engineering and for technical attacks.

![](https://www.blackhillsinfosec.com/wp-content/uploads/2025/07/DNSTriage_01.png)

### **MX Records**

May indicate the organization’s email defenses. In this case, ProofPoint has been detected.

![](https://www.blackhillsinfosec.com/wp-content/uploads/2025/07/DNSTriage_02.png)

### **Microsoft Services**

On-premises and cloud-hosted Microsoft services are frequently affected by known vulnerabilities and exploitation paths. In the example below, a Microsoft Exchange Smart Host has been detected, which is often vulnerable to email spoofing attacks. The link to a relevant blog, with exploitation details, is included in the output.

![](https://www.blackhillsinfosec.com/wp-content/uploads/2025/07/DNSTriage_03.png)

### **Interesting Subdomains**

Subdomains often indicate the presence of abusable infrastructure. In ...