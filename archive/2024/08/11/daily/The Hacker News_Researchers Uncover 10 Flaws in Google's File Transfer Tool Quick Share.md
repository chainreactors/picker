---
title: Researchers Uncover 10 Flaws in Google's File Transfer Tool Quick Share
url: https://thehackernews.com/2024/08/researchers-uncover-10-flaws-in-googles.html
source: The Hacker News
date: 2024-08-11
fetch_date: 2025-10-06T18:07:00.372142
---

# Researchers Uncover 10 Flaws in Google's File Transfer Tool Quick Share

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

# [Researchers Uncover 10 Flaws in Google's File Transfer Tool Quick Share](https://thehackernews.com/2024/08/researchers-uncover-10-flaws-in-googles.html)

**Aug 10, 2024**Ravie LakshmananVulnerability / Mobile Security

[![Google's File Transfer Tool Quick Share](data:image/png;base64... "Google's File Transfer Tool Quick Share")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhfe4HB5eoeq60K4gOHiGpjcRPCdPXzmmUkhJoWtYsjNeuunQxNh1-j600PFOSJGsjnJpg6wadrH7tf-P0lEdryFXzoRp4nm01cOzhx_2nnsfGwSfPTV1oLUHxZzVjf7_zlZ6ozBEJJAtx5k3ln2E3ovwOozphrw5QOe-FzTpkYB0qWxOZlIa9QubFarbqV/s790-rw-e365/wifi.png)

As many as 10 security flaws have been uncovered in Google's [Quick Share](https://support.google.com/chromebook/answer/10751738?hl=en) data transfer utility for Android and Windows that could be assembled to trigger remote code execution (RCE) chain on systems that have the software installed.

"The Quick Share application implements its own specific application-layer communication protocol to support file transfers between nearby, compatible devices," SafeBreach Labs researchers Or Yair and Shmuel Cohen [said](https://www.safebreach.com/blog/rce-attack-chain-on-quick-share) in a technical report shared with The Hacker News.

"By investigating how the protocol works, we were able to fuzz and identify logic within the Quick Share application for Windows that we could manipulate or bypass."

The result is the discovery of 10 vulnerabilities – nine affecting Quick Share for Windows and one impacting Android – that could be fashioned into an "innovative and unconventional" RCE attack chain to run arbitrary code on Windows hosts. The RCE attack chain has been codenamed **QuickShell**.

[![DFIR Retainer Services](data:image/png;base64...)](https://thehackernews.uk/cloud-insight-d)

The shortcomings span six remote denial-of-service (DoS) flaws, two unauthorized files write bugs each identified in Android and Windows versions of the software, one directory traversal, and one case of forced Wi-Fi connection.

The issues have been addressed in Quick Share version 1.0.1724.0 and later. Google is collectively tracking the flaws under the below two CVE identifiers -

* **[CVE-2024-38271](https://nvd.nist.gov/vuln/detail/CVE-2024-38271)** (CVSS score: 5.9) - A vulnerability that forces a victim to stay connected to a temporary Wi-Fi connection created for sharing

* **[CVE-2024-38272](https://www.cve.org/cverecord?id=CVE-2024-38272)** (CVSS score: 7.1) - A vulnerability that allows an attacker to bypass the accept file dialog on Windows

Quick Share, formerly Nearby Share, is a peer-to-peer file-sharing utility that allows users to transfer photos, videos, documents, audio files or entire folders between Android devices, Chromebooks, and Windows desktops and laptops in close proximity. Both devices must be within 5 m (16 feet) of each other with Bluetooth and Wi-Fi enabled.

In a nutshell, the identified shortcomings could be used to remotely write files into devices without approval, force the Windows app to crash, redirect its traffic to a Wi-Fi access point under an attacker's control, and traverse paths to the user's folder.

[![CIS Build Kits](data:image/png;base64...)](https://thehackernews.uk/platform-shield-d)

But more importantly, the researchers found that the ability to force the target device into connecting to a different Wi-Fi network and create files in the Downloads folder could be combined to initiate a chain of steps that ultimately lead to remote code execution.

The findings, [first presented](https://defcon.org/html/defcon-32/dc-32-speakers.html#54485) at DEF CON 32 today, are a culmination of a deeper analysis of the Protobuf-based proprietary protocol and the logic that undergirds the system. They are significant not least because they highlight how seemingly harmless known issues could open the door to a successful compromise and could pose serious risks when combined with other flaws.

"This research reveals the security challenges introduced by the complexity of a data-transfer utility attempting to support so many communication protocols and devices," SafeBreach Labs said in a statement. "It also underscores the critical security risks that can be created by chaining seemingly low-risk, known, or unfixed vulnerabilities together."

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

[cybersecurity](https://thehackernews.com/search/label/cybersecurity)[DEF CON](https://thehackernews.com/search/label/DEF%20CON)[File sharing](https://thehackernews.com/search/label/File%20sharing)[Google](https://thehackernews.com/search/label/Google)[mobile security](https://thehackernews.com/search/label/mobile%20security)[remote code execution](https://thehackernews.com/search/label/remote%20code%20execution)[Vulnerability](https://thehackernews.com/search/label/Vulnerability)[windows security](https://thehackernews.com/search/label/windows%20security)

[![c](data:image/svg+xml;base64...)](https://thehackernews.uk/cloud-defense)

Trending News

[![Stop Alert Chaos: Context Is the Key to Effective Incident Response](data:image/svg+xml;base64... "Stop Alert Chaos: Context Is the Key to Effective Incident Response")

Stop Alert Chaos: Context...