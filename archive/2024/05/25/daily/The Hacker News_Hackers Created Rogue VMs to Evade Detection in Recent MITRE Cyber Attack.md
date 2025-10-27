---
title: Hackers Created Rogue VMs to Evade Detection in Recent MITRE Cyber Attack
url: https://thehackernews.com/2024/05/hackers-created-rogue-vms-to-evade.html
source: The Hacker News
date: 2024-05-25
fetch_date: 2025-10-06T17:19:43.357555
---

# Hackers Created Rogue VMs to Evade Detection in Recent MITRE Cyber Attack

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

# [Hackers Created Rogue VMs to Evade Detection in Recent MITRE Cyber Attack](https://thehackernews.com/2024/05/hackers-created-rogue-vms-to-evade.html)

**May 24, 2024**Ravie LakshmananEndpoint Security / Threat Intelligence

[![MITRE Cyber Attack](data:image/png;base64... "MITRE Cyber Attack")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhd7DBL3q3NvlgpVS469muOptoIjz4_GdmMgcq63agM-VwgPgHclAOT1E5GRR5F0B9uqcBgcY-Sv5iL-k08uqLr54H35B8nMuX_tqPQS_fWoCueQJ2EPwtACUOQBfUBWt0XUI96IhVQmJhH_O9A2AJaTPUPAxcjkzB3UxbCzTriGbXDuwl1Y2sBl3sh7MBn/s790-rw-e365/server.png)

The MITRE Corporation has revealed that the cyber attack targeting the not-for-profit company towards late December 2023 by exploiting zero-day flaws in Ivanti Connect Secure (ICS) involved the threat actor creating rogue virtual machines (VMs) within its VMware environment.

"The adversary created their own rogue VMs within the VMware environment, leveraging compromised vCenter Server access," MITRE researchers Lex Crumpton and Charles Clancy [said](https://medium.com/mitre-engenuity/infiltrating-defenses-abusing-vmware-in-mitres-cyber-intrusion-4ea647b83f5b).

"They wrote and deployed a JSP web shell (BEEFLUSH) under the vCenter Server's Tomcat server to execute a Python-based tunneling tool, facilitating SSH connections between adversary-created VMs and the ESXi hypervisor infrastructure."

The motive behind such a move is to sidestep detection by obscuring their malicious activities from centralized management interfaces like vCenter and maintain persistent access while reducing the risk of being discovered.

[![DFIR Retainer Services](data:image/png;base64...)](https://thehackernews.uk/cloud-insight-d)

Details of the attack [emerged](https://thehackernews.com/2024/04/mitre-corporation-breached-by-nation.html) last month when MITRE revealed that the China-nexus threat actor -- tracked by Google-owned Mandiant under the name UNC5221 -- breached its Networked Experimentation, Research, and Virtualization Environment (NERVE) by exploiting two ICS flaws CVE-2023-46805 and CVE-2024-21887.

Upon bypassing multi-factor authentication and gaining an initial foothold, the adversary moved laterally across the network and leveraged a compromised administrator account to take control of the VMware infrastructure and [deploy various backdoors and web shells](https://thehackernews.com/2024/05/china-linked-hackers-used-rootrot.html) to retain access and harvest credentials.

This consisted of a Golang-based backdoor codenamed BRICKSTORM that was embedded within the rogue VMs and two web shells referred to as BEEFLUSH and BUSHWALK, allowing UNC5221 to execute arbitrary commands and communicate with command-and-control servers.

"The adversary also used a default VMware account, VPXUSER, to make seven API calls that enumerated a list of mounted and unmounted drives," MITRE said.

"Rogue VMs operate outside the standard management processes and do not adhere to established security policies, making them difficult to detect and manage through the GUI alone. Instead, one needs special tools or techniques to identify and mitigate the risks associated with rogue VMs effectively."

[![CIS Build Kits](data:image/png;base64...)](https://thehackernews.uk/platform-shield-d)

One effective countermeasure against threat actors' stealthy efforts to bypass detection and maintain access is to enable secure boot, which prevents unauthorized modifications by verifying the integrity of the boot process.

The company said it's also making available two PowerShell scripts named [Invoke-HiddenVMQuery](https://github.com/center-for-threat-informed-defense/public-resources/tree/master/nerve-incident#rogue-vm-detection-script) and [VirtualGHOST](https://github.com/CrowdStrike/VirtualGHOST) to help identify and mitigate potential threats within the VMware environment.

"As adversaries continue to evolve their tactics and techniques, it is imperative for organizations to remain vigilant and adaptive in defending against cyber threats," MITRE said.

Found this article interesting? Follow us on [Google News](https://news.google.com/publications/CAAqLQgKIidDQklTRndnTWFoTUtFWFJvWldoaFkydGxjbTVsZDNNdVkyOXRLQUFQAQ), [Twitter](https://twitter.com/thehackersnews) and [LinkedIn](https://www.linkedin.com/company/thehackernews/) to read more exclusive content we post.

SHARE
[**](#link_share)
[**](#link_share)
[**](#link_share)
**

[**Tweet](#link_share)

[**Share](#link_share)

[**Share](#link_share)

**Share

**
[**Share on Facebook](#link_share)
[**Share on Twitter](#link_share)
[**Share on Linkedin](#link_share)
[**Share on Reddit](#link_share)
[**Share on Hacker News](#link_share)
[**Share on Email](#link_share)
[**Share on WhatsApp](#link_share)
[![Facebook Messenger](data:image/png;base64...)Share on Facebook Messenger](#link_share)
[**Share on Telegram](#link_share)

SHARE **

[Cyber Attack](https://thehackernews.com/search/label/Cyber%20Attack)[cybersecurity](https://thehackernews.com/search/label/cybersecurity)[endpoint security](https://thehackernews.com/search/label/endpoint%20security)[Ivanti](https://thehackernews.com/search/label/Ivanti)[MITRE Corporation](https://thehackernews.com/search/label/MITRE%20Corporation)[privilege escalation](https://thehackernews.com/search/label/privilege%20escalation)[Threat Intelligence](https://thehackernews.com/search/label/Threat%20Intelligence)[Virtual Machine](https://thehackernews.com/search/label/Virtual%20Machine)[vmware](https://thehackernews.com/search/label/vmware)

[![c](data:image/svg+xml;base64...)](https://thehackernews.uk/cloud-defense)

Trending News

[![Stop Alert Chaos: Context Is the Key to Effective Incident Response](data:image/svg+xml;base64... "Stop Alert Chaos: Context Is the Key to Effective Incident Response")

Stop Alert Chaos: Context Is the Key to Effective Incident Response](https://thehackernews.com/2025/09/stop-alert-chaos-context-is-key-to.html)

[![Evolving Enterprise Defense to Secure the Modern AI Supply Chain](...