---
title: Warning: New RapperBot Campaign Aims to Launch DDoS Attacks at Game Servers
url: https://thehackernews.com/2022/11/warning-new-rapperbot-campaign-aims-to.html
source: The Hacker News
date: 2022-11-17
fetch_date: 2025-10-03T23:02:40.125922
---

# Warning: New RapperBot Campaign Aims to Launch DDoS Attacks at Game Servers

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

# [Warning: New RapperBot Campaign Aims to Launch DDoS Attacks at Game Servers](https://thehackernews.com/2022/11/warning-new-rapperbot-campaign-aims-to.html)

**Nov 16, 2022**Ravie Lakshmanan

[![DDoS Attacks](data:image/png;base64... "DDoS Attacks")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEj46rD4JirBV04bIevqK64k5D3iOuE82i5JSJuSV4QjDoK7fCaC4ldIghI_-hhkv1fNylwKmh2OTMmTUulOY63EEWr5mhrUi5N4GCz8MndKIrS7L-gLTdm89msN7cjPSoDNOqvT8LnUVz4WOyd7ucrKtTVWKkVL79xf_tprO96ZSDT5-K8B8vwJnQcC/s790-rw-e365/ddos-gaming.jpg)

Cybersecurity researchers have unearthed new samples of malware called RapperBot that are being used to build a botnet capable of launching Distributed Denial of Service (DDoS) attacks against game servers.

"In fact, it turns out that this campaign is less like RapperBot than an older campaign that appeared in February and then mysteriously disappeared in the middle of April," Fortinet FortiGuard Labs researchers Joie Salvio and Roy Tay [said](https://www.fortinet.com/blog/threat-research/new-rapperbot-campaign-ddos-attacks) in a Tuesday report.

RapperBot, which was first [documented](https://thehackernews.com/2022/08/new-iot-rapperbot-malware-targeting.html) by the network security firm in August 2022, is known to exclusively brute-force SSH servers configured to accept [password authentication](https://www.hostinger.com/tutorials/vps/how-to-disable-ssh-password-authentication-on-vps).

[![DFIR Retainer Services](data:image/png;base64...)](https://thehackernews.uk/cloud-insight-d)

The nascent malware is heavily inspired by the [Mirai botnet](https://thehackernews.com/2022/04/hackers-exploiting-spring4shell.html), whose source code leaked in October 2016, leading to the rise of several variants.

What's notable about the updated version of RapperBot is its ability to perform Telnet brute-force, in addition to supporting DoS attacks using the Generic Routing Encapsulation ([GRE](https://en.wikipedia.org/wiki/Generic_Routing_Encapsulation)) tunneling protocol as well as [UDP floods](https://www.cloudflare.com/learning/ddos/udp-flood-ddos-attack/) targeting game servers running Grand Theft Auto: San Andreas.

"The Telnet brute-forcing code is designed primarily for self-propagation and resembles the old Mirai Satori botnet," the researchers said.

[![DDoS Attacks](data:image/png;base64... "DDoS Attacks")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjhU9CZxrNVjPFNDPeaJMfqIoUm14wsis4Gcp3Fio8_tg-YB2mX1yA4JXiscPkEjz23KIYFkqMShXJIeG4Kt9yRh20qgi8romq3OsFNrhg2mKNTMbbhyej1_FRhP5EyY1jztwIXNZ0c1re4ruSn5LkH9bsYde0q1ERDJrPNqxxnebZPp31o3zmBVq0I/s790-rw-e365/traffic.jpg)

This list of hard-coded plaintext credentials, which are default credentials associated with IoT devices, are embedded into the binary as opposed to retrieving it from a command-and-control (C2) server, a behavior that was observed in artifacts detected after July 2022.

A successful break-in is followed by reporting the credentials used back to the C2 server and installing the RapperBot payload on the hacked device.

[![CIS Build Kits](data:image/png;base64...)](https://thehackernews.uk/platform-shield-d)

Fortinet said the malware is designed to only target appliances that run on ARM, MIPS, PowerPC, SH4, and SPARC architectures, and halt its self-propagation mechanism should they be running on Intel chipsets.

What's more, the October 2022 campaign has been found to share overlaps with other operations involving the malware as far back as May 2021, with the Telnet spreader module making its first appearance in August 2021, only to be removed in later samples and reintroduced last month.

"Based on the undeniable similarities between this new campaign and the previously reported RapperBot campaign, it is highly likely that they are being operated by a single threat actor or by different threat actors with access to a privately-shared base source code," the researchers concluded.

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

[botnet](https://thehackernews.com/search/label/botnet)[ddos attack](https://thehackernews.com/search/label/ddos%20attack)[Distributed Denial of Service](https://thehackernews.com/search/label/Distributed%20Denial%20of%20Service)

[![c](data:image/svg+xml;base64...)](https://thehackernews.uk/cloud-defense)

Trending News

[![SolarWinds Releases Hotfix for Critical CVE-2025-26399 Remote Code Execution Flaw](data:image/svg+xml;base64... "SolarWinds Releases Hotfix for Critical CVE-2025-26399 Remote Code Execution Flaw")

SolarWinds Releases Hotfix for Critical CVE-2025-26399 Remote Code Execution Flaw](https://thehackernews.com/2025/09/solarwinds-releases-hotfix-for-critical.html)

[![Microsoft Patches Critical Entra ID Flaw Enabling Global Admin Impersonation Across Tenants](data:image/svg+xml;base64... "Microsoft Patches Critical Entra ID Flaw Enabling Global Admin Impersonation Across Tenants")

Microsoft Patches Critical Entra ID Flaw Enabling Global Admin Impersonation Across Tenants](https://thehackernews.com/2025/09/microsoft-patches-critical-entra-id.html)

[![Hackers Exploit Pandoc CVE-2025-51591 to Target AWS IMDS and Steal EC2 IAM Credentials](data:image/svg+xml;base64... "Hackers Exploit Pandoc CVE-2025-51591...