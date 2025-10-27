---
title: Researchers Uncover Stealthy Techniques Used by Cranefly Espionage Hackers
url: https://thehackernews.com/2022/10/researchers-uncover-stealthy-techniques.html
source: The Hacker News
date: 2022-10-29
fetch_date: 2025-10-03T21:16:35.675229
---

# Researchers Uncover Stealthy Techniques Used by Cranefly Espionage Hackers

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

# [Researchers Uncover Stealthy Techniques Used by Cranefly Espionage Hackers](https://thehackernews.com/2022/10/researchers-uncover-stealthy-techniques.html)

**Oct 28, 2022**Ravie Lakshmanan

[![Cranefly Espionage Hackers](data:image/png;base64... "Cranefly Espionage Hackers")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgK4STuvuzTbV9U2M2MqG0XRlkPBc6lZRO4z_ejtHGHzZIlzqma4WBjdTN3AerNceak7ey5wBjTwFbTqAIo9gfRGBMzxUrjyO9VpJhqxZ7w-ABl_bTpen5l7eV84Lpais-7B0xzaiX8y3nfZkou9RDWMmCs1FCYlHK_z5sFOik1wqWWqUJ4KCxm6Btc/s790-rw-e365/hackers.jpg)

A recently discovered hacking group known for targeting employees dealing with corporate transactions has been linked to a new backdoor called **Danfuan**.

This hitherto undocumented malware is delivered via another dropper called Geppei, researchers from Symantec, by Broadcom Software, [said](https://symantec-enterprise-blogs.security.com/blogs/threat-intelligence/cranefly-new-tools-technique-geppei-danfuan) in a report shared with The Hacker News.

The dropper "is being used to install a new backdoor and other tools using the novel technique of reading commands from seemingly innocuous Internet Information Services ([IIS](https://thehackernews.com/2021/08/several-malware-families-targeting-iis.html)) logs," the researchers said.

[![DFIR Retainer Services](data:image/png;base64...)](https://thehackernews.uk/cloud-insight-d)

The toolset has been attributed by the cybersecurity company to a suspected espionage actor called UNC3524, aka Cranefly, which [first came to light](https://thehackernews.com/2022/05/new-hacker-group-pursuing-corporate.html) in May 2022 for its focus on bulk email collection from victims who deal with mergers and acquisitions and other financial transactions.

One of the group's key malware strains is QUIETEXIT, a backdoor deployed on network appliances that do not support antivirus or endpoint detection, such as load balancers and wireless access point controllers, enabling the attacker to fly under the radar for extended periods of time.

Geppei and Danfuan add to Cranefly's custom cyber weaponry, with the former acting a dropper by reading commands from IIS logs that masquerade as harmless web access requests sent to a compromised server.

"The commands read by Geppei contain malicious encoded .ashx files," the researchers noted. "These files are saved to an arbitrary folder determined by the command parameter and they run as backdoors."

[![CIS Build Kits](data:image/png;base64...)](https://thehackernews.uk/platform-shield-d)

This includes a web shell called [reGeorg](https://malpedia.caad.fkie.fraunhofer.de/details/win.regeorg), which has been put to use by other actors like [APT28](https://thehackernews.com/2021/07/nsa-fbi-reveal-hacking-methods-used-by.html), [DeftTorero](https://securelist.com/defttorero-tactics-techniques-and-procedures/107610/), and [Worok](https://thehackernews.com/2022/09/worok-hackers-target-high-profile-asian.html), and a never-before-seen malware dubbed Danfuan, which is engineered to execute received C# code.

Symantec said it hasn't observed the threat actor exfiltrating data from victim machines despite a long dwell time of 18 months on compromised networks.

"The use of a novel technique and custom tools, as well as the steps taken to hide traces of this activity on victim machines, indicate that Cranefly is a fairly skilled threat actor," the researchers concluded.

"The tools deployed and efforts taken to conceal this activity [...] indicate that the most likely motivation for this group is intelligence gathering."

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

[hacking news](https://thehackernews.com/search/label/hacking%20news)[Malware](https://thehackernews.com/search/label/Malware)

[![c](data:image/svg+xml;base64...)](https://thehackernews.uk/cloud-defense)

Trending News

[![SolarWinds Releases Hotfix for Critical CVE-2025-26399 Remote Code Execution Flaw](data:image/svg+xml;base64... "SolarWinds Releases Hotfix for Critical CVE-2025-26399 Remote Code Execution Flaw")

SolarWinds Releases Hotfix for Critical CVE-2025-26399 Remote Code Execution Flaw](https://thehackernews.com/2025/09/solarwinds-releases-hotfix-for-critical.html)

[![Microsoft Patches Critical Entra ID Flaw Enabling Global Admin Impersonation Across Tenants](data:image/svg+xml;base64... "Microsoft Patches Critical Entra ID Flaw Enabling Global Admin Impersonation Across Tenants")

Microsoft Patches Critical Entra ID Flaw Enabling Global Admin Impersonation Across Tenants](https://thehackernews.com/2025/09/microsoft-patches-critical-entra-id.html)

[![Hackers Exploit Pandoc CVE-2025-51591 to Target AWS IMDS and Steal EC2 IAM Credentials](data:image/svg+xml;base64... "Hackers Exploit Pandoc CVE-2025-51591 to Target AWS IMDS and Steal EC2 IAM Credentials")

Hackers Exploit Pandoc CVE-2025-51591 to Target AWS IMDS and Steal EC2 IAM Credentials](https://thehackernews.com/2025/09/hackers-exploit-pandoc-cve-2025-51591.html)

[![China-Linked PlugX and Bookworm Malware Attacks Target Asian Telecom and ASEAN Networks](data:image/svg+xml;base64... "China-Linked PlugX and Bookworm Malware Attacks Target Asian Telecom and ASEAN Networks")

China-Linked PlugX and B...