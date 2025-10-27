---
title: 13,000 MikroTik Routers Hijacked by Botnet for Malspam and Cyberattacks
url: https://thehackernews.com/2025/01/13000-mikrotik-routers-hijacked-by.html
source: Instapaper: Unread
date: 2025-01-23
fetch_date: 2025-10-06T20:14:36.092659
---

# 13,000 MikroTik Routers Hijacked by Botnet for Malspam and Cyberattacks

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

# [13,000 MikroTik Routers Hijacked by Botnet for Malspam and Cyberattacks](https://thehackernews.com/2025/01/13000-mikrotik-routers-hijacked-by.html)

**Jan 21, 2025**Ravie LakshmananEmail Security / Botnet

[![MikroTik Routers Hijacked](data:image/png;base64... "MikroTik Routers Hijacked")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiEiAnJveYyoW4VkzfDJ7Ni1ob0o_THRgJ9xi6t0VQd4vaCq4Wx99H6sIMRTwlcNhw0ua58HV5KFqHFTpx7DXwhWi8uVXgPEW_uokr9AGzpJTc0Mh2VoB6uVcWwzuHshshMu39XXED_EiBsrYNbnr3nABzQ8YafjHv6JpjqHZ5iyhDMonyEqowvyaUYKBYl/s790-rw-e365/dns.png)

A global network of about 13,000 hijacked Mikrotik routers has been employed as a botnet to propagate malware via spam campaigns, the [latest addition](https://thehackernews.com/2022/03/over-200000-microtik-routers-worldwide.html) to a [list of botnets](https://thehackernews.com/2024/07/ovhcloud-hit-with-record-840-million.html) powered by MikroTik devices.

The activity "take[s] advantage of misconfigured DNS records to pass email protection techniques," Infoblox security researcher David Brunsdon [said](https://blogs.infoblox.com/threat-intelligence/one-mikro-typo-how-a-simple-dns-misconfiguration-enables-malware-delivery-by-a-russian-botnet/) in a technical report published last week. "This botnet uses a global network of Mikrotik routers to send malicious emails that are designed to appear to come from legitimate domains."

The DNS security company, which has codenamed the campaign **Mikro Typo**, said its analysis sprang forth from the discovery of a malspam campaign in late November 2024 that leveraged freight invoice-related lures to entice recipients into launching a ZIP archive payload.

[![DFIR Retainer Services](data:image/png;base64...)](https://thehackernews.uk/cloud-insight-d)

The ZIP file contains an obfuscated JavaScript file, which is then responsible for running a PowerShell script designed to initiate an outbound connection to a command-and-control (C2) server located at the IP address 62.133.60[.]137.

The exact initial access vector used to infiltrate the routers is unknown, but various firmware versions have been affected, including those vulnerable to [CVE-2023-30799](https://thehackernews.com/2023/07/critical-mikrotik-routeros.html), a critical privilege escalation issue that could be abused to achieve arbitrary code execution.

"Regardless of how they've been compromised, it seems as though the actor has been placing a script onto the [Mikrotik] devices that enables SOCKS (Secure Sockets), which allow the devices to operate as TCP redirectors," Brunsdon said.

"Enabling SOCKS effectively turns each device into a proxy, masking the true origin of malicious traffic and making it harder to trace back to the source."

Elevating the concern is the lack of authentication required to use these proxies, thereby allowing other threat actors to weaponize specific devices or the entire botnet for malicious purposes, ranging from distributed denial-of-service (DDoS) attacks to phishing campaigns.

The malspam campaign in question has been found to exploit a misconfiguration in the sender policy framework ([SPF](https://thehackernews.com/2025/01/neglected-domains-used-in-malspam-to.html)) TXT records of 20,000 domains, giving the attackers the ability to send emails on behalf of those domains and bypass various email security protections.

[![CIS Build Kits](data:image/png;base64...)](https://thehackernews.uk/platform-shield-d)

Specifically, it has emerged that the SPF records are configured with the extremely permissive "+all" option, essentially defeating the purpose of having the safeguard in the first place. This also means that any device, such as the compromised MikroTik routers, can spoof the legitimate domain in email.

MikroTik device owners are recommended to keep their routers up-to-date and change default account credentials to prevent any exploitation attempts.

"With so many compromised MikroTik devices, the botnet is capable of launching a wide range of malicious activities, from DDoS attacks to data theft and phishing campaigns," Brunsdon said. "The use of SOCKS4 proxies further complicates detection and mitigation efforts, highlighting the need for robust security measures."

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

[botnet](https://thehackernews.com/search/label/botnet)[cybersecurity](https://thehackernews.com/search/label/cybersecurity)[ddos attack](https://thehackernews.com/search/label/ddos%20attack)[DNS Security](https://thehackernews.com/search/label/DNS%20Security)[email security](https://thehackernews.com/search/label/email%20security)[Malspam](https://thehackernews.com/search/label/Malspam)[MikroTik](https://thehackernews.com/search/label/MikroTik)[Phishing](https://thehackernews.com/search/label/Phishing)

[![c](data:image/svg+xml;base64...)](https://thehackernews.uk/cloud-defense)

Trending News

[![Stop Alert Chaos: Context Is the Key to Effective Incident Response](data:image/svg+xml;base64... "Stop Alert Chaos: Context Is the Key to Effective Incident Response")

Stop Alert Chaos: Context Is the Key to Effective Incident Response](https://thehackernews.com/2025/09/stop-alert-chaos-context-is-key-to.html)

[![Evolving Enterp...