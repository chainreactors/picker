---
title: Malicious PyPI Package Impersonates SymPy, Deploys XMRig Miner on Linux Hosts
url: https://thehackernews.com/2026/01/malicious-pypi-package-impersonates.html
source: The Hacker News
date: 2026-01-22
fetch_date: 2026-01-23T03:33:36.495137
---

# Malicious PyPI Package Impersonates SymPy, Deploys XMRig Miner on Linux Hosts

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

# [Malicious PyPI Package Impersonates SymPy, Deploys XMRig Miner on Linux Hosts](https://thehackernews.com/2026/01/malicious-pypi-package-impersonates.html)

**Ravie Lakshmanan**Jan 22, 2026Cryptojacking / Malware

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjWCefYaSp9ssGTQkdK58gL2QbQurY3rXLBGBTEC2hXq1qGh88LxThrqrtejW9sVCnoXsrwoAZQwlbdrwOl-O0fEz509vXrbK235fZ0tl9iPWgiKBJt49PqTRB6uu_ZDyeaMl6F6zqfVmJFw8PU4e8-0MgYh-qxJpn1xRcLN9NfnQQ_X47nJxdz3N47s3z8/s1600-e365/pypi-cryptocurrency-malware.jpg)

A new malicious package discovered in the Python Package Index (PyPI) has been found to impersonate a popular library for symbolic mathematics to deploy malicious payloads, including a cryptocurrency miner, on Linux hosts.

The package, named **[sympy-dev](https://pypi.org/project/sympy-dev/)**, mimics [SymPy](https://www.sympy.org/en/index.html), replicating the latter's project description verbatim in an attempt to deceive unsuspecting users into thinking that they are downloading a "development version" of the library. It has been downloaded over 1,100 times since it was first published on January 17, 2026.

Although the download count is not a reliable yardstick for measuring the number of infections, the figure likely suggests some developers may have fallen victim to the malicious campaign. The package remains available for download as of writing.

According to [Socket](https://socket.dev/blog/pypi-package-impersonates-sympy-to-deliver-cryptomining-malware), the original library has been modified to act as a downloader for an XMRig cryptocurrency miner on compromised systems. The malicious behavior is designed to trigger only when specific polynomial routines are called so as to fly under the radar.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/attack-surface-insight-d)

"When invoked, the backdoored functions retrieve a remote JSON configuration, download a threat actor-controlled ELF payload, then execute it from an anonymous memory-backed file descriptor using Linux memfd\_create and /proc/self/fd, which reduces on-disk artifacts," security researcher Kirill Boychenko said in a Wednesday analysis.

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgMnLH_jR6XiILoBWhk2c5QqCDdd5sxoEITLVrYlv5ysUuLxqT8b6As16b5IYBbsjDSeEmSyHccmkmsREdqzVBs46QhRHBW_19G36LLdaC0M27S2IGV7hdpUdAxpimyC_RTWHzs-tQxLeRRcaN0vf0hxyhXFYbkprmXWOKjG7faZ9HPuqsfZ0UIRtlez17-/s1600-e365/python.png)

The altered functions are used to execute a downloader, which fetches a remote JSON configuration and an ELF payload from "63.250.56[.]54," and then launches the ELF binary along with the configuration as input directly in memory to avoid leaving artifacts on disk. This technique has been previously adopted by cryptojacking campaigns orchestrated by [FritzFrog](https://thehackernews.com/2024/02/fritzfrog-returns-with-log4shell-and.html) and [Mimo](https://thehackernews.com/2025/07/threat-actor-mimo-targets-magento-and.html).

The end goal of the attack is to download two Linux ELF binaries that are designed to mine cryptocurrency using XMRig on Linux hosts.

"Both retrieved configurations use an XMRig compatible schema that enables CPU mining, disables GPU backends, and directs the miner to Stratum over TLS endpoints on port 3333 hosted on the same threat actor-controlled IP addresses," Socket said.

"Although we observed cryptomining in this campaign, the Python implant functions as a general purpose loader that can fetch and execute arbitrary second stage code under the privileges of the Python process."

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

[cryptojacking](https://thehackernews.com/search/label/cryptojacking)[cybersecurity](https://thehackernews.com/search/label/cybersecurity)[linux](https://thehackernews.com/search/label/linux)[Malware](https://thehackernews.com/search/label/Malware)[Open Source](https://thehackernews.com/search/label/Open%20Source)[PyPI](https://thehackernews.com/search/label/PyPI)[Python](https://thehackernews.com/search/label/Python)[supply chain attack](https://thehackernews.com/search/label/supply%20chain%20attack)[Threat Research](https://thehackernews.com/search/label/Threat%20Research)

Trending News

[![⚡ Weekly Recap: Fortinet Exploits, RedLine Clipjack, NTLM Crack, Copilot Attack and More](data:image/svg+xml;base64... "⚡ Weekly Recap: Fortinet Exploits, RedLine Clipjack, NTLM Crack, Copilot Attack and More")

⚡ Weekly Recap: Fortinet Exploits, RedLine Clipjack, NTLM Crack, Copilot Attack and More](https://thehackernews.com/2026/01/weekly-recap-fortinet-exploits-redline.html)

[![n8n Supply Chain Attack Abuses Community Nodes to Steal OAuth Tokens](data:image/svg+xml;base64... "n8n Supply Chain Attack Abuses Community Nodes to Steal OAuth Tokens")

n8n Supply Chain Attack Abuses Community Nodes to Steal OAuth Tokens](https://thehackernews.com/2026/01/n8n-supply-chain-attack-abuses.html)

[![New Advanced Linux VoidLink Malware Targets Cloud and container Environments](data:image/svg+xml;base64... "New Advanced Linux VoidLink Malware Targets Cloud and container Environments")

New Advanced Linux VoidLink Malware Targets Cloud and container Environments](https://thehackernews.com/2026/01/new-advanced-linux-voidlink-malware.html)

[![Critical Node.js Vulnerability Can Cause Server Crashes via async_hooks Stack Overflow](data:image/svg+xml;base64... "Critical Node.js Vulnerability Can Cause Server Crashes via async_hooks Stack Overflow")

Critical Node.js Vulnerability Can Cause Server Crashes...