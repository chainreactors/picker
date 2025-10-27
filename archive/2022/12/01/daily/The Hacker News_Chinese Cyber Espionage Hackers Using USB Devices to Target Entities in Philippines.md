---
title: Chinese Cyber Espionage Hackers Using USB Devices to Target Entities in Philippines
url: https://thehackernews.com/2022/11/chinese-cyber-espionage-hackers-using.html
source: The Hacker News
date: 2022-12-01
fetch_date: 2025-10-04T00:14:00.454535
---

# Chinese Cyber Espionage Hackers Using USB Devices to Target Entities in Philippines

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

# [Chinese Cyber Espionage Hackers Using USB Devices to Target Entities in Philippines](https://thehackernews.com/2022/11/chinese-cyber-espionage-hackers-using.html)

**Nov 30, 2022**Ravie Lakshmanan

[![Cyber Espionage Hackers](data:image/png;base64... "Cyber Espionage Hackers")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgazMz1M9Jqx1bqZK7zqf8ETDiE7vMz8kmQfsNG2-5NVNySqo3TelXLy7JUwljfRoDSV8PrRDJM4yjee-5Z30K0jcLdHml6uPtgNoHAWeswI2IZPszKhjMJLTn0x7jEIgwr6guEy0RP1tUXuJZV7qy4wjrbYTLgc06u1pIOmlr3RT7oG2T6vd_hMPBv/s790-rw-e365/pen-drive.png)

A threat actor with a suspected China nexus has been linked to a set of espionage attacks in the Philippines that primarily relies on USB devices as an initial infection vector.

Mandiant, which is part of Google Cloud, is tracking the cluster under its uncategorized moniker **UNC4191**. An analysis of the artifacts used in the intrusions indicates that the campaign dates as far back as September 2021.

"UNC4191 operations have affected a range of public and private sector entities primarily in Southeast Asia and extending to the U.S., Europe, and APJ," researchers Ryan Tomcik, John Wolfram, Tommy Dacanay, and Geoff Ackerman [said](https://www.mandiant.com/resources/blog/china-nexus-espionage-southeast-asia).

[![DFIR Retainer Services](data:image/png;base64...)](https://thehackernews.uk/cloud-insight-d)

"However, even when targeted organizations were based in other locations, the specific systems targeted by UNC4191 were also found to be physically located in the Philippines."

The reliance on infected USB drives to propagate the malware is unusual if [not new](https://thehackernews.com/2022/04/fin7-hackers-leveraging-password-reuse.html). The [Raspberry Robin](https://thehackernews.com/2022/10/raspberry-robin-operators-selling.html) worm, which has [evolved](https://twitter.com/SophosXOps/status/1594703522993508352) into an initial access service for follow-on attacks, is known to use USB drives as an entry point.

[![Cyber Espionage Hackers](data:image/png;base64... "Cyber Espionage Hackers")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiAnhF4o5bEampqOWBwAMr0wJUnPdjZmksSvn38S9sAA1MKTuqR6zQA8qSE2StqQaZTdB_QDpgc2M44JAux5y6rSeBlbYgEEKa4Vto8lvD1dHLhtIM_n8X_2JvJPvpJmndPTbY6PiBjqOrwj9vO7uy-VO7nW6_0hsk02myA0dnAAuHm3bY74GQYGRws/s790-rw-e365/1.png)

The threat intelligence and incident response firm said that the attacks led to the deployment of three new malware families dubbed MISTCLOAK, DARKDEW, and BLUEHAZE, alongside [Ncat](https://nmap.org/ncat/), the latter of which is a command-line networking utility that's used to create a reverse shell on the victim system.

MISTCLOAK, for its part, gets activated when a user plugs in a compromised removable device to a system, acting as a launchpad for an encrypted payload called DARKDEW that's capable of infecting removable drives, effectively proliferating the infections.

[![Cyber Espionage Hackers](data:image/png;base64... "Cyber Espionage Hackers")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiiGWt9lbW_l_unOeayw-h3s-gV3XUTCeQwVpiXPY6tAlHbCen9-LpQyLxkRF7huAr0-rSIW_UQ6TMoNl-ZDCGW3Q7VRsT2ZsilCMJqTx7bmSllpjHEZQmTSIy8ATrXH2Df5dH8zn8VrAd0OksMCXabuAlqbPsItQIsmim3ScFn_fnv1ilurT7nTF86/s790-rw-e365/hack.png)

"The malware self-replicates by infecting new removable drives that are plugged into a compromised system, allowing the malicious payloads to propagate to additional systems and potentially collect data from [air-gapped](https://thehackernews.com/2022/08/new-air-gap-attack-uses-mems-gyroscope.html) [systems](https://thehackernews.com/2022/08/air-gapped-devices-can-send-covert.html)," the researchers explained.

[![CIS Build Kits](data:image/png;base64...)](https://thehackernews.uk/platform-shield-d)

The DARKDEW dropper further serves to launch another executable ("DateCheck.exe"), a renamed version of a legitimate, signed application known as "Razer Chromium Render Process" that invokes the BLUEHAZE malware.

BLUEHAZE, a launcher written in C/C++, takes the attack chain forward by starting a copy of Ncat to create a reverse shell to a hardcoded command-and-control (C2) address.

"We believe this activity showcases Chinese operations to gain and maintain access to public and private entities for the purposes of intelligence collection related to China's political and commercial interests," the researchers said.

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

[Chinese Hackers](https://thehackernews.com/search/label/Chinese%20Hackers)[cyber espionage](https://thehackernews.com/search/label/cyber%20espionage)[Raspberry Robin](https://thehackernews.com/search/label/Raspberry%20Robin)

[![c](data:image/svg+xml;base64...)](https://thehackernews.uk/cloud-defense)

Trending News

[![SolarWinds Releases Hotfix for Critical CVE-2025-26399 Remote Code Execution Flaw](data:image/svg+xml;base64... "SolarWinds Releases Hotfix for Critical CVE-2025-26399 Remote Code Execution Flaw")

SolarWinds Releases Hotfix for Critical CVE-2025-26399 Remote Code Execution Flaw](https://thehackernews.com/2025/09/solarwinds-releases-hotfix-for-critical.html)

[![Microsoft Patches Critical Entra ID Flaw Enabling Global Admin Impersonation Acros...