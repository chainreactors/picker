---
title: The Top Ten List of Why You Got Hacked This Year (2023/2024)
url: https://www.blackhillsinfosec.com/top-ten-list-of-why-you-got-hacked-this-year-2023-2024/
source: Black Hills Information Security
date: 2024-12-13
fetch_date: 2025-10-06T19:38:47.569262
---

# The Top Ten List of Why You Got Hacked This Year (2023/2024)

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

12
Dec
2024

[Author](https://www.blackhillsinfosec.com/category/author/), [External/Internal](https://www.blackhillsinfosec.com/category/red-team/external/), [Finding](https://www.blackhillsinfosec.com/category/finding/), [Informational](https://www.blackhillsinfosec.com/category/informational/), [Jordan Drysdale](https://www.blackhillsinfosec.com/category/author/jordan-drysdale/), [Kent Ickler](https://www.blackhillsinfosec.com/category/author/kent-ickler/)
[Buzzwords](https://www.blackhillsinfosec.com/tag/buzzwords/), [Clickbait](https://www.blackhillsinfosec.com/tag/clickbait/), [Report Findings](https://www.blackhillsinfosec.com/tag/report-findings/), [Statistical Analysis](https://www.blackhillsinfosec.com/tag/statistical-analysis/), [Zero AI Mentions](https://www.blackhillsinfosec.com/tag/zero-ai-mentions/)

# [The Top Ten List of Why You Got Hacked This Year (2023/2024)](https://www.blackhillsinfosec.com/top-ten-list-of-why-you-got-hacked-this-year-2023-2024/)

by [Jordan Drysdale](https://www.blackhillsinfosec.com/team/jordan-drysdale/) and [Kent Ickler](https://www.blackhillsinfosec.com/team/kent-ickler/)

![](https://www.blackhillsinfosec.com/wp-content/uploads/2024/12/BLOG_chalkboard_00701-1.png)

*tl;dr: BHIS does a lot of penetration testing in both traditional and continuous penetration testing (CPT) formats. This top ten style list was derived from an analysis of our findings across our penetration testing services.*

Anywho… This list is based on the last couple years of analyzing our report findings, mostly the findings that lead to compromise. We threw out stuff related to SSL and TLS, SSH ciphers, and yeah, we biased our study results a bit doing so. However, little has changed in the last few years. We still use the same and similar techniques as the previous ten years to gain initial access, move laterally, execute code, escalate privileges, access database content, and generally make a mess.

### **Number 10: Firewalls**

This finding should read more like “Lack of Firewall-Based Restrictions.” Your organization should really enable East-West firewalls on workstations and servers where appropriate. Allowing everyone unfettered access to their workstation network is a serious risk. If you actively disable workstation and server firewalls with group policies, we advise you to begin unravelling the cultural history of this configuration, because it is not a great strategy for security. Actually, it’s a terrible strategy.  We also consider a lack of network segmentation and generalized any:any rulesets across your VLANs and routable networks to be a concern.

In our opinion, the most dangerous port you have exposed is SMB TCP port 445. Close it– and don’t let it egress your network.

Remote procedure calls allow for everything from configuration changes to security memory access. It is time to start reducing this exposure.

![](https://www.blackhillsinfosec.com/wp-content/uploads/2024/12/001_firewalls.jpg)

### **Number 9: Message Integrity**

Don’t know what this means? That’s normal and okay.

Message integrity checks (MICs) provide the foundation for validating who sent or started a conversation.

![](https://www.blackhillsinfosec.com/wp-content/uploads/2024/12/002_mic.jpg)

Additionally, this may mean proving oneself to a remote file share via a quick message digest exchange validated by a client and a server. Simpler yet? A service checks to make sure you are who you say you are.

Why? Message integrity checks reduce and mostly eliminate the effectiveness of credential relay attacks. The two primary relay attacks we use as attackers are SMB relay and LDAP relay. Both of these protocols support message signing.

SMB Signing: <https://learn.microsoft.com/en-us/troubleshoot/windows-server/networking/overview-server-message-block-signing>

LDAP Signing: <https://learn.microsoft.com/en-us/troubleshoot/windows-server/active-directory/enable-ldap-signing-in-windows-server>

### **Number 8: Defaults**

![](https://www.blackhillsinfosec.com/wp-content/uploads/2024/12/003_defaults.jpg)

Default configuration settings include things like:

* Default machine account quota

* Lack of SMB and LDAP signing

* High fidelity endpoint logging

* Really bad password policies

* NTLM authentication

* *un*Protected Users

* Enrollee Supplies Subject (ADCS ESC1)

* LLMNR, mDNS, and NBNS

* LAPS passwords in clear

* SCCM and MECM credentials

* Panther unattend.xml

* Browser WPAD

* Attack technique blindness

There are a lot of ways to take advantage of these weak default settings. As testers, we use some combination of the previous list to establish a foothold, escalate permissions, and move around networks.

### **Number 7: Patching**

The n...