---
title: Threat Actor Mimo Targets Magento and Docker to Deploy Crypto Miners and Proxyware
url: https://thehackernews.com/2025/07/threat-actor-mimo-targets-magento-and.html
source: The Hacker News
date: 2025-07-24
fetch_date: 2025-10-06T23:55:57.152818
---

# Threat Actor Mimo Targets Magento and Docker to Deploy Crypto Miners and Proxyware

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

# [Threat Actor Mimo Targets Magento and Docker to Deploy Crypto Miners and Proxyware](https://thehackernews.com/2025/07/threat-actor-mimo-targets-magento-and.html)

**Jul 23, 2025**Ravie LakshmananMalware / Cryptocurrency

[![Crypto Miners and Proxyware](data:image/png;base64... "Crypto Miners and Proxyware")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhWagiNcGILt3ATlZdarqQIXJfdqJBKyzSaYgOhtwJHHQg1iBWU3dqOfeRrRYiThfofoLGuX0YXc9uo50kgr9ApHUQadxdjSni3LBR868Rd2xWdQMtVYBc6Af63XofzXLZ13cAQ2JgXZb6fU2ktLZ5o8vC5R2E438GX5P6_8GqmXKM1kcs3ky7rN90fzSzT/s790-rw-e365/docker.jpg)

The threat actor behind the exploitation of vulnerable Craft Content Management System (CMS) instances has shifted its tactics to target Magento CMS and misconfigured Docker instances.

The activity has been attributed to a threat actor tracked as **Mimo** (aka Hezb), which has a long history of leveraging N-day security flaws in various web applications to deploy cryptocurrency miners.

"Although Mimo's primary motivation remains financial, through cryptocurrency mining and bandwidth monetization, the sophistication of their recent operations suggests potential preparation for more lucrative criminal activities," Datadog Security Labs [said](https://securitylabs.datadoghq.com/articles/beyond-mimolette-tracking-mimo-expansion-magento-cms-docker/) in a report published this week.

Mimo's exploitation of CVE-2025-32432, a critical security flaw in Craft CMS, for cryptojacking and proxyjacking was [documented](https://thehackernews.com/2025/05/mimo-hackers-exploit-cve-2025-32432-in.html) by Sekoia in May 2025.

[![DFIR Retainer Services](data:image/png;base64...)](https://thehackernews.uk/cloud-insight-d)

Newly observed attack chains associated with the threat actor involve the abuse of undetermined PHP-FPM vulnerabilities in Magento e-commerce installations to obtain initial access, and then using it to drop [GSocket](https://thehackernews.com/2025/01/python-based-bots-exploiting-php.html), a legitimate open-source penetration testing tool, to [establish persistent access](https://thehackernews.com/2024/10/alert-adobe-commerce-and-magento-stores.html) to the host by means of a reverse shell.

"The initial access vector is PHP-FPM command injection via a Magento CMS plugin, indicating that Mimo possesses multiple exploit capabilities beyond previously observed adversarial tradecraft," researchers Ryan Simon, Greg Foss, and Matt Muir said.

In an attempt to sidestep detection, the GSocket binary masquerades as a legitimate or kernel-managed thread so that it blends in with other processes that may be running on the system.

Another notable technique employed by the attackers is the use of in-memory payloads using [memfd\_create()](https://thehackernews.com/2024/02/fritzfrog-returns-with-log4shell-and.html) so as to launch an ELF binary loader called "4l4md4r" without leaving any trace on disk. The loader is then responsible for deploying the IPRoyal proxyware and the XMRig miner on the compromised machine but not before modifying the "/etc/ld.so.preload" file to inject a rootkit to conceal the presence of these artifacts.

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjrwtOIWj8NR7Mk0pZCTyasBlbcZClaX4hzE-v3TK_ZEoNTCsE7_ZKdZcuOIBayO1IsJA7rkCdN4Ctvk7E3OSkaffUViTKWj2am-WaMnNILJ9jakqwAmq5RFQ8meDasZ2b2J1h_a2OvRnEridFmRd2BrDExmgIfbWpFyKHKzhkN3jhAO-VPUTiOSVpYRlRp/s790-rw-e365/mimo.jpg)

The distribution of a miner and [proxyware](https://thehackernews.com/2021/09/cybercriminals-abusing-internet-sharing.html) underscores a two-pronged approach adopted by Mimo to maximize financial gain. The distinct revenue generation streams ensure that compromised machines' CPU resources are hijacked to mine cryptocurrency, while the victims' unused internet bandwidth is monetized for illicit residential proxy services.

"Furthermore, the use of proxyware, which typically consumes minimal CPU, enables stealthy operation that prevents detection of the additional monetization even if the crypto miner's resource usage is throttled," the researchers said. "This multi-layered monetization also enhances resilience: even if the crypto miner is detected and removed, the proxy component may remain unnoticed, ensuring continued revenue for the threat actor."

[![CIS Build Kits](data:image/png;base64...)](https://thehackernews.uk/platform-shield-d)

Datadog said it also observed the threat actors abusing misconfigured Docker instances that are publicly accessible to spawn a new container, within which a malicious command is executed to fetch an additional payload from an external server and execute it.

Written in Go, the modular malware comes fitted with capabilities to achieve persistence, conduct file system I/O operations, terminate processes, perform in-memory execution. It also serves as a dropper for GSocket and IPRoyal, and attempts to propagate to other systems via SSH brute-force attacks.

"This demonstrates the threat actor's willingness to compromise a diverse range of services – not just CMS providers – to achieve their objectives," Datadog said.

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

[CMS Security](https://thehackernews.co...