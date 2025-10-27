---
title: Scattered Spider Hijacks VMware ESXi to Deploy Ransomware on Critical U.S. Infrastructure
url: https://thehackernews.com/2025/07/scattered-spider-hijacks-vmware-esxi-to.html
source: The Hacker News
date: 2025-07-29
fetch_date: 2025-10-06T23:58:28.926666
---

# Scattered Spider Hijacks VMware ESXi to Deploy Ransomware on Critical U.S. Infrastructure

#1 Trusted Cybersecurity News Platform

Followed by 5.20+ million[**](https://twitter.com/thehackersnews)
[**](https://www.linkedin.com/company/thehackernews/)
[**](https://www.facebook.com/thehackernews)

[![The Hacker News Logo](data:image/png;base64...)](/)

**

**

[** Subscribe – Get Latest News](#email-outer)

* [** Home](/)
* [** Newsletter](#email-outer)
* [** Webinars](/p/upcoming-hacker-news-webinars.html)

* [Home](/)
* [Data Breaches](/search/label/data%20breach)
* [Cyber Attacks](/search/label/Cyber%20Attack)
* [Vulnerabilities](/search/label/Vulnerability)
* [Webinars](/p/upcoming-hacker-news-webinars.html)
* [Expert Insights](https://thehackernews.com/expert-insights/)
* [Contact](/p/submit-news.html)

**

**

**

Resources

* [Webinars](/p/upcoming-hacker-news-webinars.html)
* [Free eBooks](https://thehackernews.tradepub.com)

About Site

* [About THN](/p/about-us.html)
* [Jobs](/p/careers-technical-writer-designer-and.html)
* [Advertise with us](/p/advertising-with-hacker-news.html)

Contact/Tip Us

[**

Reach out to get featured—contact us to send your exclusive story idea, research, hacks, or ask us a question or leave a comment/feedback!](/p/submit-news.html)

Follow Us On Social Media

[**](https://www.facebook.com/thehackernews)
[**](https://twitter.com/thehackersnews)
[**](https://www.linkedin.com/company/thehackernews/)
[**](https://www.youtube.com/c/thehackernews?sub_confirmation=1)
[**](https://www.instagram.com/thehackernews/)

[** RSS Feeds](https://feeds.feedburner.com/TheHackersNews)
[** Email Alerts](#email-outer)

[![Salesforce Security Handbook](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjWa8tsMNqlevi1HGF1ALQRGIq7hROPFAbHd3R1RTEOe73T8_Q2xW_-91t2jSGjU5peiPb8QYblGp4igNW-u2Qmlxbp2BKzTVMSvyXDZJmC-BYpiiJHrcnG5drmSP97iZ9PVIf1DeEr7U-7vWpe4HXwfMjt8FGNgq5mOycOJluYr9wF7YOKrQY9MfArwgjt/s728-e100/ai-agent-security-d.png)](https://thehackernews.uk/ai-agent-security-d)

# [Scattered Spider Hijacks VMware ESXi to Deploy Ransomware on Critical U.S. Infrastructure](https://thehackernews.com/2025/07/scattered-spider-hijacks-vmware-esxi-to.html)

**Jul 28, 2025**Ravie LakshmananCyber Attack / Ransomware

[![Deploy Ransomware on Critical U.S. Infrastructure](data:image/png;base64... "Deploy Ransomware on Critical U.S. Infrastructure")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgsN72I_dig68jgOwgDvQxWOb2WmMGMNoMpQUgE1XYTkbWN5kwQAnLzTeP7E9Iz-P9yO_n5V6NitcgNegiC-NUm9kkl8nwolpY3BNbUOaZaVhFw-UFZbDkxEQ8EH2K-EAIUATc3Rx-l-L_ptgBcqtUywatOaNhMbuzT3DAYc2nnvDWwXHOMdWikyM2POger/s790-rw-e365/ransomware.jpg)

The notorious cybercrime group known as [Scattered Spider](https://thehackernews.com/2025/06/google-warns-of-scattered-spider.html) is targeting VMware ESXi hypervisors in attacks targeting retail, airline, and transportation sectors in North America.

"The group's core tactics have remained consistent and do not rely on software exploits. Instead, they use a proven playbook centered on phone calls to an IT help desk," Google's Mandiant team [said](https://cloud.google.com/blog/topics/threat-intelligence/defending-vsphere-from-unc3944/) in an extensive analysis.

"The actors are aggressive, creative, and particularly skilled at using social engineering to bypass even mature security programs. Their attacks are not opportunistic but are precise, campaign-driven operations aimed at an organization's most critical systems and data."

Also called 0ktapus, Muddled Libra, Octo Tempest, and UNC3944, the threat actors have a [history](https://thehackernews.com/2025/06/fbi-warns-of-scattered-spiders.html) of conducting advanced social engineering attacks to obtain initial access to victim environments and then adopting a "living-off-the-land" (LotL) approach by manipulating trusted administrative systems and leveraging their control of Active Directory to pivot to the VMware vSphere environment.

[![DFIR Retainer Services](data:image/png;base64...)](https://thehackernews.uk/cloud-insight-d)

Google said the method, which provides a pathway for data exfiltration and ransomware deployment directly from the hypervisor, is "highly effective," as it bypasses security tools and leaves few traces of compromise.

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhb0eL51J-5BaysAyudq8UZKdTGwHZctDAz-9UrXI8h48dIwpTG8g4FPVqT6-xMU2mxN29dwZ6IZE7peoSbAnYhEuPBEkf2qF7_yIUASdznT4YJEPq0XUwqm_RfZqBt4CUdxM9Y7PrTcOAfrNNN0SWRaKaIpduQqX5bE1sKKabVY2MubGgKnRrF_yXh2cHn/s790-rw-e365/2.png)

"The group's heavy use of social engineering has revealed recurring patterns, particularly in how they register domains that closely mimic legitimate company infrastructure or login portals," NCC Group [pointed out](https://insights.nccgroup.com/july-2025-scattered-spider-threat-intel-update).

Some of their typical naming conventions include:

* victimname-sso[.]com
* victimname-okta[.]com
* victimname-servicedesk[.]com
* sso-victimname[.]com
* servicenow-victimname[.]com

The attack chain unfolds over five distinct phases -

* Initial compromise, reconnaissance, and privilege escalation, allowing the threat actors to harvest information related to IT documentation, support guides, organization charts, and vSphere administrators, as well as enumerate credentials from password managers like HashiCorp Vault or other Privileged Access Management (PAM) solutions. The attackers have been found to make additional calls to the company's IT help desk to impersonate a high-value administrator and request a password reset to gain control of the account.
* Pivoting to the virtual environment using the mapped Active Directory to vSphere credentials and gaining access to VMware vCenter Server Appliance (vCSA), after which teleport is executed to create a persistent and encrypted reverse shell that bypasses firewall rules.
* Enabling SSH connections on ESXi hosts and resetting root passwords, and executing what's called a "disk-swap" attack to extract the NTDS.dit Active Directory database. The attack works by powering off a Domain Controller (DC) virtual machine (VM) and detaching its virtual disk, only to attach it to another, unmonitored VM under their control. After copying the NTDS.dit file, the entire process is reversed and the DC is powered on.
* Weaponizing the access to delete backup jobs, snapshots, and repositories to inhibit recovery.
* Using the SSH access to the ESXi hosts to push their custom ransomware binary via SCP/SFTP.

"UNC3944's playbook requires a fundamental shift in defensive strategy, moving from EDR-based threat hunting to proactive, infrastructure-centric defense," Google said. "This threat differs from traditional Windows ransomware in two ways: speed and stealth."

The tech giant also called out the threat actors' "extreme velocity," stating the whole infection sequence from initial access to data exfiltration and final ransomware deployment can transpire within a short span of a few hours.

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiqj4lvYHjB8g7ORWxDQNCBih6YzPkjDkiGZI_5TmyynKMuSsd56NbQdfQYHFPguo_BOwUKd1WL3ifscl0wwDK2NDlPX_ISIlp3PwF24-CotDHEO-yts8qz68_zWefhLAOc8hp8mDpMH31nwjVAsPSX9netC08bbMXn1apGYZiukf9WhxgMcAawGVLXHvdn/s790-rw-e365/1.png)

According to [Palo Alto Networks Unit 42](https://unit42.paloaltonetworks.com/muddled-libra/), Scattered Spider actors have not only become adept at social engineering, but also have partnered with the DragonForce (aka Slippery Scorpius) ransomware program, in one instance exfiltrating over 100 GB of data during a two-day period.

To counter such threats, organizations are advised to follow three layers of protections -

* Enable vSphere lockdown mode, enforce execInstalledOnly, use vSphere VM encryption, decommission old VMs, harden the help desk
* Implement phishing-resistant multi-factor authentication (MFA), isolate critical identity infrastructure, avoid authentication loops
* Centralize and moni...