---
title: Vietnamese Hacker Group Deploys New PXA Stealer Targeting Europe and Asia
url: https://thehackernews.com/2024/11/vietnamese-hacker-group-deploys-new-pxa.html
source: The Hacker News
date: 2024-11-16
fetch_date: 2025-10-06T19:20:42.230878
---

# Vietnamese Hacker Group Deploys New PXA Stealer Targeting Europe and Asia

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

# [Vietnamese Hacker Group Deploys New PXA Stealer Targeting Europe and Asia](https://thehackernews.com/2024/11/vietnamese-hacker-group-deploys-new-pxa.html)

**Nov 15, 2024**Ravie LakshmananMalware / Credential Theft

[![Vietnamese Hacker](data:image/png;base64... "Vietnamese Hacker")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEi1ZRZNW4Cka8usveAEJBq27NNJ5_kg-EoSuM2WySJi5M_mW9tx8rPX8tJ1qSPJIEGoHP68dozTMwx4ur_RCE0GtqPbafhc9tDx6uW6ktMBORzAm1hXNGLZ1O3oUOLApS6t2_nJldFN-eJwWDaVd0WKBV7mHko1_UtG7DHE_URf-YLkZ5o6wj5pfvJBMkon/s790-rw-e365/hacking.png)

A Vietnamese-speaking threat actor has been linked to an information-stealing campaign targeting government and education entities in Europe and Asia with a new Python-based malware called **PXA Stealer**.

The malware "targets victims' sensitive information, including credentials for various online accounts, VPN and FTP clients, financial information, browser cookies, and data from gaming software," Cisco Talos researchers Joey Chen, Alex Karkins, and Chetan Raghuprasad [said](https://blog.talosintelligence.com/new-pxa-stealer/).

"PXA Stealer has the capability to decrypt the victim's browser master password and uses it to steal the stored credentials of various online accounts"

The connections to Vietnam stem from the presence of Vietnamese comments and a hard-coded Telegram account named "[Lone None](https://t.me/lonenone)" in the stealer program, the latter of which includes an icon of Vietnam's national flag and a picture of the emblem for Vietnam's Ministry of Public Security.

[![DFIR Retainer Services](data:image/png;base64...)](https://thehackernews.uk/cloud-insight-d)

Cisco Talos said it observed the attacker selling Facebook and Zalo account credentials, and SIM cards in the Telegram channel "Mua Bán Scan MINI," which has been [previously](https://blog.talosintelligence.com/coralraider-targets-socialmedia-accounts/) linked to another threat actor called [CoralRaider](https://thehackernews.com/2024/04/coralraider-malware-campaign-exploits.html). Lone None has also been found to be active on another Vietnamese Telegram group operated by CoralRaider called "[Cú Black Ads - Dropship](https://t.me/cudemads)."

That said, it's currently not clear if these two intrusion sets are related, if they are carrying out their campaigns independently of each other.

[![PXA Stealer](data:image/png;base64... "PXA Stealer")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgNzHRshDW8zsJAGBWqzZgIWDvjHy39iivOxQEXGRyfuvA5KDTX4oQOx_oPITJOZWUVUxbCgJEhxazis6PtDlH7lOeM_dtaljXU6zdD_LLa-PozfHLfFwPH5X-yqbPC19EHXHw7XnF8OWcBMeRoNueM19a7uPc1oWPKZqLacyTu4pWi2uGKJRBp-bDNei9X/s790-rw-e365/attack-flow.jpeg)

"The tools shared by the attacker in the group are automated utilities designed to manage several user accounts. These tools include a Hotmail batch creation tool, an email mining tool, and a Hotmail cookie batch modification tool," the researchers said.

"The compressed packages provided by the threat actor often contain not only the executable files for these tools but also their source code, allowing users to modify them as needed."

There is evidence to suggest that such programs are offered for sale via other sites like aehack[.]com that claim to provide free hack and cheat tools. Tutorials for using these tools are shared via [YouTube channels](https://www.youtube.com/%40fvia/videos), further highlighting that there is a concerted effort to market them.

Attack chains propagating PXA Stealer commence with a phishing email containing a ZIP file attachment, which includes a Rust-based loader and a hidden folder that, in turn, packs in several Windows batch scripts and a decoy PDF file.

The execution of the loader triggers the batch scripts, which are responsible for opening the lure document, a Glassdoor job application form, while also running PowerShell commands to download and run a payload capable of disabling antivirus programs running on the host, followed by deploying the stealer itself.

A noteworthy feature of PXA Stealer is its emphasis on stealing Facebook cookies, using them to authenticate a session and interacting with Facebook Ads Manager and Graph API to gather more details about the account and their associated ad-related information.

[![CIS Build Kits](data:image/png;base64...)](https://thehackernews.uk/platform-shield-d)

The targeting of Facebook business and advertisement accounts has been a [recurring pattern](https://thehackernews.com/2024/04/vietnam-based-hackers-steal-financial.html) among Vietnamese threat actors, and PXA Stealer proves to be no different.

The disclosure comes as IBM X-Force detailed an ongoing campaign since mid-April 2023 that delivers [StrelaStealer](https://thehackernews.com/2024/03/new-strelastealer-phishing-attacks-hit.html) to victims across Europe, specifically Italy, Spain, Germany, and Ukraine. The activity has been attributed to a "rapidly maturing" initial access broker (IAB) it tracks as Hive0145, which is believed to be the sole operator of the stealer malware.

[![PXA Stealer](data:image/png;base64... "PXA Stealer")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEh2jM-6ZGxN0HmvH0AtqHKeo_rihiwJpGK9RqzXTRfX6BpF5dUMAyaTBM1ZdYIn9nYjsWD0_EnDkqX-iGpezbc07Ka1_P1vopw-4nuaZvk10atacCLKJ8epK7-luKwij__griVLs4EC-6MB3NweVRjhlLeAl4Qfml7E1ENN4RAF2-P4U11UVKMEXBUubzJd/s790-rw-e365/rowsers.jpeg)

"The phishing emails used in these campaigns are real invoice notifications, which have been stolen through previously exfiltrated email credentials," researchers Golo Mühr, Joe Fasulo, and Charlotte Hammond [said](https://securityintelligence.com/x-force/strela-stealer-todays-invoice-tomorrows-phish/). "StrelaStealer is designed to extract user credentials stored in Microsoft Outlook and Mozilla Thunderbird."

The popularity of stealer malware is evidenced by the continuous evolution of existing families like [RECORDSTEALER](https://www.googlecloudcommunity.com/gc/Community-Blog/Finding-Malware-Unveiling-RECORDSTEALER-with-Google-...