---
title: Fake Madgicx Plus and SocialMetrics Extensions Are Hijacking Meta Business Accounts
url: https://thehackernews.com/2025/09/fake-madgicx-plus-and-socialmetrics.html
source: The Hacker News
date: 2025-09-12
fetch_date: 2025-10-02T20:04:12.013330
---

# Fake Madgicx Plus and SocialMetrics Extensions Are Hijacking Meta Business Accounts

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

# [Fake Madgicx Plus and SocialMetrics Extensions Are Hijacking Meta Business Accounts](https://thehackernews.com/2025/09/fake-madgicx-plus-and-socialmetrics.html)

**Sep 11, 2025**Ravie LakshmananMalvertising / Browser Security

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEi2ZkDGIehpXH948IGTxMRsWIkGYEVs1os4i3Iz1dafJzvP7XspDt0F852C4WJVx_39BS_ylL0mEUki4nWpbq3HDGhHg1efM2xKtSgdbE_YW3SMMEshq1R54Q71kt8ChPyAcq2EzUPmnPRcivExfJ6Gxb9KtoYGXApEafxA9AzgcA6kMUBj4LJ9VGUBgYpA/s790-rw-e365/meta.jpg)

Cybersecurity researchers have disclosed two new campaigns that are serving fake browser extensions using malicious ads and fake websites to steal sensitive data.

The malvertising campaign, per [Bitdefender](https://www.bitdefender.com/en-us/blog/hotforsecurity/malicious-facebook-ads-push-fake-meta-verified-browser-extensions-to-steal-accounts), is designed to push fake "[Meta Verified](https://www.meta.com/en-gb/meta-verified/)" browser extensions named **SocialMetrics Pro** that claim to unlock the blue check badge for Facebook and Instagram profiles. At least 37 malicious ads have been observed serving the extension in question.

"The malicious ads are bundled with a video tutorial that guides viewers through the process of downloading and installing a so-called browser extension, which claims to unlock the blue verification tick on Facebook or other special features," the Romanian cybersecurity vendor said.

But, in reality, the extension – which is hosted on a legitimate cloud service called Box -- is capable of collecting session cookies from Facebook and sending them to a Telegram bot controlled by the attackers. It's also equipped to obtain the victim's IP address by sending a query to ipinfo[.]io/json.

Select variants of the rogue browser add-on have been observed using the stolen cookies to interact with the Facebook Graph API to likely fetch additional information related to the accounts. In the past, malware like [NodeStealer](https://thehackernews.com/2024/11/nodestealer-malware-targets-facebook-ad.html) has leveraged the Facebook Graph API to collect budget details of the account.

The end goal of these efforts is to sell valuable Facebook Business and Ads accounts on underground forums for profit to other fraudsters, or repurpose them to fuel more malvertising campaigns, which, in turn, leads to more hijacked accounts – effectively creating a self-perpetuating cycle.

[![DFIR Retainer Services](data:image/png;base64...)](https://thehackernews.uk/cloud-insight-d)

The campaign exhibits all the "fingerprints" typically associated with [Vietnamese-speaking](https://thehackernews.com/2023/09/vietnamese-cybercriminals-targeting.html) threat actors, who are [known](https://thehackernews.com/2024/04/vietnam-based-hackers-steal-financial.html) to [adopt](https://thehackernews.com/2025/05/fake-ai-tools-used-to-spread.html) various [stealer families](https://thehackernews.com/2025/05/fake-kling-ai-facebook-ads-deliver-rat.html) to target and gain unauthorized access to Facebook accounts. This hypothesis is also bolstered by the use of Vietnamese to narrate the tutorial and add source code comments.

"By using a trusted platform, attackers can mass-generate links, automatically embed them into tutorials, and continuously refresh their campaigns," Bitdefender said. "This fits a larger pattern of attackers industrializing malvertising, where everything from ad images to tutorials is created en masse."

The disclosure coincides with another campaign that's targeting Meta advertisers with rogue Chrome extensions distributed via counterfeit websites posing as artificial intelligence (AI)-powered ad optimization tools for Facebook and Instagram. At the heart of the operation is a fake platform named **Madgicx Plus**.

"Promoted as a tool to streamline campaign management and boost ROI using artificial intelligence, the extension instead delivers potentially malicious functionalities capable of hijacking business sessions, stealing credentials, and compromising Meta Business accounts," Cybereason [said](https://www.cybereason.com/blog/chrome-extension-campaign-madgicx).

"The extensions are promoted as productivity or ad performance enhancers, but they operate as dual-purpose malware capable of stealing credentials, accessing session tokens, or enabling account takeover.

The extensions, the first of which is still available for download from the Chrome Web Store as of writing, are listed below -

* Madgicx Plus - The SuperApp for Meta Advertisers (ID: [eoalbaojjblgndkffciljmiddhgjdldh](https://dex.koi.security/reports/chrome/eoalbaojjblgndkffciljmiddhgjdldh/)) - Published in February 2025 (28 Installs)
* Meta Ads SuperTool (ID: [cpigbbjhchinhpamicodkkcpihjjjlia](https://dex.koi.security/reports/chrome/cpigbbjhchinhpamicodkkcpihjjjlia/)) - Published in March 2025 (11 Installs)
* Madgicx X Ads - The SuperApp for Meta Advertisers (ID: [cpigbbjhchinhpamicodkkcpihjjjlia](https://dex.koi.security/reports/chrome/cpigbbjhchinhpamicodkkcpihjjjlia/)) - Published in March 2025 (3 Installs)

[![CIS Build Kits](data:image/png;base64...)](https://thehackernews.uk/platform-shield-d)

Once installed, the extension gains full access to all websites the user visits, enabling the threat actors to inject arbitrary scripts, as well as intercept and modify network traffic, monitor browsing activity, capture form inputs, and harvest sensitive data.

It also prompts users to link their Facebook and Google accounts to access the service, while their identity information is covertly harvested in the background. Furthermore, the add-ons function similarly to the aforementioned fake Meta Verified extension in that it uses victims' stolen Facebook credentials to interact with the Facebook Graph API.

"This staged approach reveals a clear threat-actor strategy: first capturing Google identity data, then pivoting to Facebook to broaden access and increase the chances of hijacking valuable business or advertising assets," Cybereason...