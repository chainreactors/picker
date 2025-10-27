---
title: FIN7 Hacker Group Leverages Malicious Google Ads to Deliver NetSupport RAT
url: https://thehackernews.com/2024/05/fin7-hacker-group-leverages-malicious.html
source: The Hacker News
date: 2024-05-12
fetch_date: 2025-10-06T17:17:33.864537
---

# FIN7 Hacker Group Leverages Malicious Google Ads to Deliver NetSupport RAT

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

# [FIN7 Hacker Group Leverages Malicious Google Ads to Deliver NetSupport RAT](https://thehackernews.com/2024/05/fin7-hacker-group-leverages-malicious.html)

**May 11, 2024**Ravie LakshmananMalvertising / Malware

[![FIN7 Hacker Group](data:image/png;base64... "FIN7 Hacker Group")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEidGxM7ADAzrplKASUpJQ3bzcolJSyabMKaYKT4HClyzRgCOuWCVvr4duu8KJkPW_9Ga8ADrETgYfu0Pwx9QosFgHep34F7jq5lOwmpYTooakEW-L3-1pyG0UDv5s2UEUJ-etPxVPf3FsuaCnRzo-2SfgR6sBYGaiuMLgIfVMCeQ_eylo2l6zR3vJ-i3oYb/s790-rw-e365/browser.png)

The financially motivated threat actor known as **FIN7** has been observed leveraging malicious Google ads spoofing legitimate brands as a means to deliver MSIX installers that culminate in the deployment of [NetSupport RAT](https://thehackernews.com/2023/11/netsupport-rat-infections-on-rise.html).

"The threat actors used malicious websites to impersonate well-known brands, including AnyDesk, WinSCP, BlackRock, Asana, Concur, The Wall Street Journal, Workable, and Google Meet," cybersecurity firm eSentire [said](https://www.esentire.com/blog/fin7-uses-trusted-brands-and-sponsored-google-ads-to-distribute-msix-payloads) in a report published earlier this week.

FIN7 (aka Carbon Spider and Sangria Tempest) is a [persistent e-crime group](https://thehackernews.com/2024/04/fin7-cybercrime-group-targeting-us-auto.html) that's been active since 2013, initially dabbling in attacks targeting point-of-sale (PoS) devices to steal payment data, before pivoting to breaching large firms via ransomware campaigns.

[![DFIR Retainer Services](data:image/png;base64...)](https://thehackernews.uk/cloud-insight-d)

Over the years, the threat actor has refined its tactics and cyber weapon arsenal, adopting [various](https://thehackernews.com/2023/05/notorious-cyber-gang-fin7-returns-cl0p.html) [custom malware](https://thehackernews.com/2022/04/fin7-hackers-leveraging-password-reuse.html) families such as BIRDWATCH, Carbanak, DICELOADER (aka Lizar and Tirion), POWERPLANT, POWERTRASH, and TERMITE, among others.

FIN7 malware is commonly deployed through spear-phishing campaigns as an entry to the target network or host, although in recent months the group has utilized malvertising techniques to initiate the attack chains.

In December 2023, Microsoft said it observed the attackers relying on Google ads to lure users into downloading malicious MSIX application packages, which ultimately led to the execution of POWERTRASH, a PowerShell-based in-memory dropper that's used to load NetSupport RAT and Gracewire.

"Sangria Tempest [...] is a financially motivated cybercriminal group currently focusing on conducting intrusions that often lead to data theft, followed by targeted extortion or ransomware deployment such as Clop ransomware," the tech giant [noted](https://thehackernews.com/2023/12/microsoft-disables-msix-app-installer.html) at the time.

The [abuse of MSIX](https://redcanary.com/blog/threat-detection/installer-packages/) as a malware distribution vector by multiple threat actors -- likely owing to its ability to bypass security mechanisms like Microsoft Defender SmartScreen -- has since prompted Microsoft to disable the protocol handler by default.

[![FIN7 Hacker Group](data:image/png;base64... "FIN7 Hacker Group")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiUJMVmQ6-u9GkF3g_oblK_DNtebXZ7wl9TwnY_3OFbTDtG3XD3OzIW9Va5ojx3KAnolsNWOnrBh2Fpp2_IHaZ5wVAzkBfr8fDD10L3OgwBVyYFUMWrWPoH9k8psm430GFeJn2zy8IxgnddNKWQgGG0f1Bxim6K2fRu1nw-bsNzafu478421F3wTkPn9tBV/s790-rw-e365/powershell.png)

In the attacks observed by eSentire in April 2024, users who visit the bogus sites via Google ads are displayed a pop-up message urging them to download a phony browser extension, which is an MSIX file containing a PowerShell script that, in turn, gathers system information and contacts a remote server to fetch another encoded PowerShell script.

The second PowerShell payload is used to download and execute the NetSupport RAT from an actor-controlled server.

The Canadian cybersecurity company said it also detected the remote access trojan being used to deliver additional malware, which includes DICELOADER by means of a Python script.

"The incidents of FIN7 exploiting trusted brand names and using deceptive web ads to distribute NetSupport RAT followed by DICELOADER highlight the ongoing threat, particularly with the abuse of signed MSIX files by these actors, which has proven effective in their schemes," eSentire said.

Similar findings have been [independently reported](https://www.threatdown.com/blog/corporate-users-targeted-via-malicious-ads-and-modals/) by Malwarebytes, which characterized the activity as singling out corporate users via malicious ads and modals by mimicking high-profile brands like Asana, BlackRock, CNN, Google Meet, SAP, and The Wall Street Journal. It, however, did not attribute the campaign to FIN7.

[![CIS Build Kits](data:image/png;base64...)](https://thehackernews.uk/platform-shield-d)

News of FIN7's malvertising schemes coincides with a [SocGholish](https://thehackernews.com/2023/09/new-blister-malware-update-fuelling.html) (aka FakeUpdates) infection wave that's designed to target business partners.

"Attackers used living-off-the-land techniques to collect sensitive credentials, and notably, configured web beacons in both email signatures and network shares to map out local and business-to-business relationships," eSentire [said](https://www.esentire.com/blog/socgholish-sets-sights-on-victim-peers). "This behavior would suggest an interest in exploiting these relationships to target business peers of interest."

It also follows the discovery of a malware campaign targeting Windows and Microsoft Office users to propagate RATs and cryptocurrency miners via cracks for popular software.

"The malware, once installed, often registers commands in the task scheduler to maintain persistence, enabling continuous installation of new malware even after removal," Broadcom-owned Symante...