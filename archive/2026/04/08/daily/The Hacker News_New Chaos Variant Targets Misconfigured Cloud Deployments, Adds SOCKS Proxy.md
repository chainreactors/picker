---
title: New Chaos Variant Targets Misconfigured Cloud Deployments, Adds SOCKS Proxy
url: https://thehackernews.com/2026/04/new-chaos-variant-targets-misconfigured.html
source: The Hacker News
date: 2026-04-08
fetch_date: 2026-04-09T04:32:33.592184
---

# New Chaos Variant Targets Misconfigured Cloud Deployments, Adds SOCKS Proxy

#1 Trusted Cybersecurity News Platform

Followed by 5.40+ million[**](https://twitter.com/thehackersnews)
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
* [Threat Intelligence](/search/label/Threat%20Intelligence)
* [Vulnerabilities](/search/label/Vulnerability)
* [Cyber Attacks](/search/label/Cyber%20Attack)
* [Webinars](/p/upcoming-hacker-news-webinars.html)
* [Expert Insights](https://thehackernews.com/expert-insights/)
* [Awards](https://awards.thehackernews.com/)

**

**

**

Resources

* [Webinars](/p/upcoming-hacker-news-webinars.html)
* [Awards](https://awards.thehackernews.com/)
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

[![Security Service Edge](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgWajeG0cdaapf1GKTZRUZUB7BzuYGegyw5k0eAorJXlmkFdYCCeLXXhXYJuXU9lWD33rV6rRnIyly3czoNfYifpxk1eGA5slItPmim3HkubXoQMgC4J7hdQPywxGbWq7Eqeff_o6s2Fq-WmSFd5guwdLn7IqpveMqULqtVnd-ndnljWYGj45EkMFB7m0qm/s728-e100/z-d.jpg)](https://thehackernews.uk/zscaler-threatlabz-d)

# [New Chaos Variant Targets Misconfigured Cloud Deployments, Adds SOCKS Proxy](https://thehackernews.com/2026/04/new-chaos-variant-targets-misconfigured.html)

**Ravie Lakshmanan**Apr 08, 2026Cryptomining / Network Security

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgjO6ntnqBUePhV2XQEQmTFh-IjdPR64u_T9ODhO3RY_BAv_8YohhRCwMg6OO9UKlvJJCd7rs1c391fbNZ59qDsSujaFJuso3h_94xKo2BX2L5Jj-osBqZ3VglM5kbgzt6OJGtkiNx4Am6NbgzrHtUa7fbdnfei8_xeJao4yvlMp3HkCurz9aNJkg9Xv934/s1700-e365/cloud.jpg)

Cybersecurity researchers have flagged a new variant ofmalware called **Chaos**that'scapable of hitting misconfigured cloud deployments, marking an expansion of the botnet's targeting infrastructure.

"Chaos malware is increasingly targeting misconfigured cloud deployments, expanding beyond its traditional focus on routers and edge devices," Darktrace [said](https://www.darktrace.com/blog/darktrace-identifies-new-chaos-malware-variant-exploiting-misconfigurations-in-the-cloud) in a new report.

Chaos was [first documented](https://thehackernews.com/2022/09/researchers-warn-of-new-go-based.html) by Lumen Black Lotus Labs in September 2022, describing it as a cross-platform malware capable of targeting Windows and Linux environments to run remote shell commands, drop additional modules, propagate to other hosts by brute-forcing SSH keys, mine cryptocurrency, and launch distributed denial-of-service (DDoS) attacks via HTTP, TLS, TCP, UDP, and WebSocket.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/vpn-risk-report-inside-d)

The malware is assessed to be an evolution of another DDoS malware known as [Kaiji](https://thehackernews.com/2025/12/react2shell-exploitation-delivers.html) that has singled out misconfigured Docker instances.It's currently not known who is behind the operation, but the presence of Chinese language characters and the use of China-based infrastructure suggest that the threat actor could be of Chinese origin.

Darktrace said it identified the new variant targeting its honeypot network last month, a deliberately misconfigured Hadoop instance that enables remote code execution on the service. In the attack spotted by the cybersecurity company, the intrusion commenced with an HTTP request to the Hadoop deployment to create a new application.

The application, for its part, embedded a sequence of shell commands to retrieve a Chaos agent binary from an attacker-controlled server ("pan.tenire[.]com"), set permissions to allow all users to read, modify, or run it ("chmod 777"), and then actually execute the binary and delete the artifact from disk to minimize the forensic trail.

An interesting aspect of the attack is that the domain was previously put to use in connection with an email phishing campaign carried out by the Chinese cybercrime group Silver Fox to deliver decoy documents and ValleyRAT malware. The campaign was codenamed [Operation Silk Lure](https://thehackernews.com/2025/10/silver-fox-expands-winos-40-attacks-to.html#operation-silk-lure-targets-china-with-valleyrat) by Seqrite Labs in October 2025.

The 64-bit ELF binary is a restructured and updated version of Chaos that reworks several of its functions, while keeping most of its core feature set intact. One of the more significant changes, however, concerns the removal of functions that enabled it to spread via SSH and exploit router vulnerabilities.

Taking their place is a new SOCKS proxy feature that allows the compromised system to be used for ferrying traffic, thereby concealing the true origins of malicious activity and making it harder for defenders to detect and block the attack.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/fast-response-not-fast-d)

"In addition, several functions that were previously believed to be inherited from Kaiji have also been changed, suggesting that the threat actors have either rewritten the malware or refactored it extensively," Darktrace added.

The addition of the proxy feature is likely a sign that threat actors behind the malware are lookingto further monetize the botnet beyond cryptocurrency mining and [DDoS-for-hire](https://thehackernews.com/2026/04/masjesu-botnet-emerges-as-ddos-for-hire.html), and keep up with their competitors in the cybercrime market by offering a diverse slate of illicit services.

"While Chaos is not a new malware, its continued evolution highlights the dedication of cybercriminals to expand their botnets and enhance the capabilities at their disposal," Darktrace concluded. "The recent shift in botnets such as [AISURU](https://thehackernews.com/2026/03/doj-disrupts-3-million-device-iot.html) and Chaos to include proxy services as core features demonstrates that denial-of-service is no longer the only risk these botnets pose to organizations and their security teams."

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

[botnet](https://thehackernews.com/search/label/botnet), [Cloud security](https://thehackernews.com/search/label/Cloud%20security), [Cryptomining](https://thehackernews.com/search/label/Cryptomining), [cybersecurity](https://thehackernews.com/search/label/...