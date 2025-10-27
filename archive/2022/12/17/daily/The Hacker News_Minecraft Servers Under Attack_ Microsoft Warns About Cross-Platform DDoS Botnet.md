---
title: Minecraft Servers Under Attack: Microsoft Warns About Cross-Platform DDoS Botnet
url: https://thehackernews.com/2022/12/minecraft-servers-under-attack.html
source: The Hacker News
date: 2022-12-17
fetch_date: 2025-10-04T01:50:27.558349
---

# Minecraft Servers Under Attack: Microsoft Warns About Cross-Platform DDoS Botnet

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

# [Minecraft Servers Under Attack: Microsoft Warns About Cross-Platform DDoS Botnet](https://thehackernews.com/2022/12/minecraft-servers-under-attack.html)

**Dec 16, 2022**Ravie LakshmananServer Security / Botnet

[![Cross-Platform DDoS Botnet](data:image/png;base64... "Cross-Platform DDoS Botnet")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEijHp6HLAxY5_9Ebf7eDGCnoLv-IfiweMuwzggWMSgxZV5fodqa3xdNQn6BeAhOwTX6fSYMpaosIEPJpOOqX7CZvaDqfcLQ8-Oa7QZyXdnELfpI-VkqA-5wexMnqbgKVxQef41c5Eh9-wUufI9ONBDQMjDrWiFBCwJtkiiog_DNFQWL3rfaecQX7jlX/s790-rw-e365/minecraft.png)

Microsoft on Thursday flagged a cross-platform botnet that's primarily designed to launch distributed denial-of-service (DDoS) attacks against private Minecraft servers.

Called **MCCrash**, the botnet is characterized by a unique spreading mechanism that allows it to propagate to Linux-based devices despite originating from malicious software downloads on Windows hosts.

"The botnet spreads by enumerating default credentials on internet-exposed Secure Shell (SSH)-enabled devices," the company [said](https://www.microsoft.com/en-us/security/blog/2022/12/15/mccrash-cross-platform-ddos-botnet-targets-private-minecraft-servers/) in a report. "Because IoT devices are commonly enabled for remote configuration with potentially insecure settings, these devices could be at risk to attacks like this botnet."

[![DFIR Retainer Services](data:image/png;base64...)](https://thehackernews.uk/cloud-insight-d)

This also means that the malware could persist on IoT devices even after removing it from the infected source PC. The tech giant's cybersecurity division is tracking the activity cluster under its emerging moniker DEV-1028.

A majority of the infections have been reported in Russia, and to a lesser extent in Kazakhstan, Uzbekistan, Ukraine, Belarus, Czechia, Italy, India, Indonesia, Nigeria, Cameroon, Mexico, and Columbia. The company did not disclose the exact scale of the campaign.

The initial infection point for the botnet is a pool of machines that have been compromised through the installation of cracking tools that claim to provide illegal Windows licenses.

[![Cross-Platform DDoS Botnet](data:image/png;base64... "Cross-Platform DDoS Botnet")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhZ6l8XvGz-j7FJdMU8EtCyHIKr7A0wCSruPPGJHoOJO9OA24BxB24F10YXTH5J6wVi_74DPwT01KuZMQlxfa9exL-Mj8RMTo7Jj18D8UbWtC_t_U6oCfxnDZGc92HyFV3Xf_EYMQkArnAdYCpGfUa4OJUyfbn4JTWBsH0Y3x4xCCe6lbjqkLY6JWan/s790-rw-e365/windows-crack.png)

The software subsequently acts as a conduit to execute a Python payload that contains the core features of the botnet, including scanning for SSH-enabled Linux devices to launch a [dictionary attack](https://en.wikipedia.org/wiki/Dictionary_attack).

Upon breaching a Linux host using the propagation method, the same Python payload is deployed to run DDoS commands, one of which is specifically set up to crash Minecraft servers ("ATTACK\_MCCRASH").

[![CIS Build Kits](data:image/png;base64...)](https://thehackernews.uk/platform-shield-d)

Microsoft described the method as "highly efficient," noting it's likely offered as a service on underground forums.

[![Cross-Platform DDoS Botnet](data:image/png;base64... "Cross-Platform DDoS Botnet")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgT0s98oBwWzBYAZxIFMLemks5SjJ2MosTKtlutMJBBV15Vq2ccCJLGP05DYqOunwxkAdqTJGK-CdWLrfcDSqs_dHZDbc0k67o4D__JAx6dYqruQWKCM736adW_y27TQHN2IhOx5mkCLSB71AqIBsMZJRBWQ6tUqFUmThc7POqx0mkTgrEBu-ezUGCp/s790-rw-e365/botnet-map.png)

"This type of threat stresses the importance of ensuring that organizations manage, keep up to date, and monitor not just traditional endpoints but also IoT devices that are often less secure," researchers David Atch, Maayan Shaul, Mae Dotan, Yuval Gordon, and Ross Bevington said.

The findings come days after Fortinet FortiGuard Labs revealed details of a new botnet dubbed [GoTrim](https://thehackernews.com/2022/12/new-gotrim-botnet-attempting-to-break.html), which has been observed brute-forcing self-hosted WordPress websites.

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

[ddos attack](https://thehackernews.com/search/label/ddos%20attack)[Microsoft](https://thehackernews.com/search/label/Microsoft)[minecraft game](https://thehackernews.com/search/label/minecraft%20game)

[![c](data:image/svg+xml;base64...)](https://thehackernews.uk/cloud-defense)

Trending News

[![SolarWinds Releases Hotfix for Critical CVE-2025-26399 Remote Code Execution Flaw](data:image/svg+xml;base64... "SolarWinds Releases Hotfix for Critical CVE-2025-26399 Remote Code Execution Flaw")

SolarWinds Releases Hotfix for Critical CVE-2025-26399 Remote Code Execution Flaw](https://thehackernews.com/2025/09/solarwinds-releases-hotfix-for-critical.html)

[![Microsoft Patches Critical Entra ID Flaw Enabling Global Admin Impersonation Across Tenants](data:image/svg+xml;base64... "Microsoft Patches Critical Entra ID Flaw Enabling Global Admin Impersonation Across Tenants")

Microsoft Patches Critical Entra ID Flaw Enabling Global Admin Impersonation Across Tenants](https://thehackernews.com/2025/09/microsoft-patches-critical-entra-id.html)

[![Hackers Exploit Pandoc CVE-2025-51591 t...