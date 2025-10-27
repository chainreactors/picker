---
title: Taiwan Web Servers Breached by UAT-7237 Using Customized Open-Source Hacking Tools
url: https://thehackernews.com/2025/08/taiwan-web-servers-breached-by-uat-7237.html
source: The Hacker News
date: 2025-08-16
fetch_date: 2025-10-07T00:49:50.843063
---

# Taiwan Web Servers Breached by UAT-7237 Using Customized Open-Source Hacking Tools

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

# [Taiwan Web Servers Breached by UAT-7237 Using Customized Open-Source Hacking Tools](https://thehackernews.com/2025/08/taiwan-web-servers-breached-by-uat-7237.html)

**Aug 15, 2025**Ravie LakshmananMalware / Open Source

[![Open-Source Hacking Tools](data:image/png;base64... "Open-Source Hacking Tools")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjR9fovBuFsajdkbWIURI1JjvNXtyGra7b8Z9XkjFEw4c4Ay2UQdZtYsMjec2Nua1GlV0IaCyQBor6RvQllwFRPiNJNeTOdECFopovC_CCPaXiemS6IylHqtwJzdt4vHRlR7YUVcdcU-gdu5HclXokqegg7_V7VYFCBUEOsZSHyYl1B5YM3hcbI3EGcy09z/s790-rw-e365/cyberattack-on-servers.jpg)

A Chinese-speaking advanced persistent threat (APT) actor has been observed targeting web infrastructure entities in Taiwan using customized versions of open-sourced tools with an aim to establish long-term access within high-value victim environments.

The activity has been attributed by Cisco Talos to an activity cluster it tracks as **UAT-7237**, which is believed to be active since at least 2022. The hacking group is assessed to be a sub-group of [UAT-5918](https://thehackernews.com/2025/03/uat-5918-targets-taiwans-critical.html), which is known to be attacking critical infrastructure entities in Taiwan as far back as 2023.

"UAT-7237 conducted a recent intrusion targeting web infrastructure entities within Taiwan and relies heavily on the use of open-sourced tooling, customized to a certain degree, likely to evade detection and conduct malicious activities within the compromised enterprise," Talos [said](https://blog.talosintelligence.com/uat-7237-targets-web-hosting-infra/).

[![DFIR Retainer Services](data:image/png;base64...)](https://thehackernews.uk/cloud-insight-d)

The attacks are characterized by the use of a bespoke shellcode loader dubbed SoundBill that's designed to decode and launch secondary payloads, such as Cobalt Strike.

Despite the tactical overlaps with UAT-5918, UAT-7237's tradecraft exhibits notable deviations, including its reliance on Cobalt Strike as a primary backdoor, the selective deployment of web shells after initial compromise, and the incorporation of direct remote desktop protocol (RDP) access and SoftEther VPN clients for persistent access.

The attack chains begin with the exploitation of known security flaws against unpatched servers exposed to the internet, followed by conducting initial reconnaissance and fingerprinting to determine if the target is of interest to the threat actors for follow-on exploitation.

"While UAT-5918 immediately begins deploying web shells to establish backdoored channels of access, UAT-7237 deviates significantly, using the [SoftEther VPN client](https://thehackernews.com/2023/08/china-linked-flax-typhoon-cyber.html) (similar to Flax Typhoon) to persist their access, and later access the systems via RDP," researchers Asheer Malhotra, Brandon White, and Vitor Ventura said.

Once this step is successful, the attacker pivots to other systems across the enterprise to expand their reach and carry out further activities, including the deployment of SoundBill, a shellcode loader based on [VTHello](https://github.com/cdxiaodong/some-function-in-binary/blob/08b66e5504f03373bd70341a4493a7450091c471/%E5%BC%82%E6%88%96%2B%E6%B7%B7%E6%B7%86/%E5%BC%82%E6%88%96%2B%E6%B7%B7%E6%B7%86/%E5%BC%82%E6%88%96%2B%E6%B7%B7%E6%B7%86.cpp), for launching Cobalt Strike.

Also deployed on compromised hosts is JuicyPotato, a privilege escalation tool widely used by various Chinese hacking groups, and Mimikatz to extract credentials. In an interesting twist, subsequent attacks have leveraged an updated version of SoundBill that embeds a Mimikatz instance into it in order to achieve the same goals.

Besides using [FScan](https://thehackernews.com/2025/07/ivanti-zero-days-exploited-to-drop.html) to identify open ports against IP subnets, UAT-7237 has been observed attempting to make Windows Registry changes to disable User Account Control (UAC) and turn on storage of cleartext passwords.

"UAT-7237 specified Simplified Chinese as the preferred display language in their [SoftEther] VPN client's language configuration file, indicating that the operators were proficient with the language," Talos noted.

[![CIS Build Kits](data:image/png;base64...)](https://thehackernews.uk/platform-shield-d)

The disclosure comes as Intezer said it discovered a new variant of a known backdoor called FireWood that's associated with a China-aligned threat actor called Gelsemium, albeit with low confidence.

FireWood was [first documented](https://thehackernews.com/2024/11/chinese-apt-gelsemium-targets-linux.html) by ESET in November 2024, detailing its ability to leverage a kernel driver rootkit module called usbdev.ko to hide processes, and run various commands sent by an attacker-controlled server.

"The core functionality of the backdoor remains the same but we did notice some changes in the implementation and the configuration of the backdoor," Intezer researcher Nicole Fishbein [said](https://intezer.com/blog/threat-bulletin-firewood/). "It is unclear if the kernel module was also updated as we were not able to collect it."

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

[Advanced Persistent Threat](https://thehackernews.com...