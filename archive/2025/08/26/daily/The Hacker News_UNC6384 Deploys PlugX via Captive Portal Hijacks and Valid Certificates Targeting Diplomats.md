---
title: UNC6384 Deploys PlugX via Captive Portal Hijacks and Valid Certificates Targeting Diplomats
url: https://thehackernews.com/2025/08/unc6384-deploys-plugx-via-captive.html
source: The Hacker News
date: 2025-08-26
fetch_date: 2025-10-07T00:50:41.369422
---

# UNC6384 Deploys PlugX via Captive Portal Hijacks and Valid Certificates Targeting Diplomats

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

# [UNC6384 Deploys PlugX via Captive Portal Hijacks and Valid Certificates Targeting Diplomats](https://thehackernews.com/2025/08/unc6384-deploys-plugx-via-captive.html)

**Aug 25, 2025**Ravie LakshmananMalware / Cyber Espionage

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhoIojSn8T0xs4LrDA5a9xYIANt_qsMaoDtoaO_GZ2kcqO7-fxaMj9Fr3wzUiLI4eBEcxP7QvylXppjD0pgZO86JTyEJDEKmUVVnsPI1WltiIMa3Urxu359HVEwp_VGyz5wBmKAh7ufY_id-cZW1tcoMMqyfZD_5V0RKbwe7F_T4be0q7LzxQYAJC5p85dY/s790-rw-e365/data.jpg)

A China-nexus threat actor known as **UNC6384** has been attributed to a set of attacks targeting diplomats in Southeast Asia and other entities across the globe to advance Beijing's strategic interests.

"This multi-stage attack chain leverages advanced social engineering including valid code signing certificates, an adversary-in-the-middle (AitM) attack, and indirect execution techniques to evade detection," Google Threat Intelligence Group (GTIG) researcher Patrick Whitsell [said](https://cloud.google.com/blog/topics/threat-intelligence/prc-nexus-espionage-targets-diplomats/).

UNC6384 is assessed to share tactical and tooling overlaps with a known Chinese [hacking group](https://thehackernews.com/2025/04/mustang-panda-targets-myanmar-with.html) called [Mustang Panda](https://thehackernews.com/2025/06/pubload-and-pubshell-malware-used-in.html), which is also tracked as BASIN, Bronze President, Camaro Dragon, Earth Preta, HoneyMyte, RedDelta, Red Lich, Stately Taurus, TEMP.Hex, and Twill Typhoon.

The campaign, detected by GTIG in March 2025, is characterized by use of a captive portal redirect to hijack web traffic and deliver a digitally signed downloader called STATICPLUGIN. The downloader then paves the way for the in-memory deployment of a [PlugX](https://thehackernews.com/2025/02/chinese-linked-attackers-exploit-check.html) (aka Korplug or SOGU) variant called SOGU.SEC.

[![DFIR Retainer Services](data:image/png;base64...)](https://thehackernews.uk/cloud-insight-d)

[PlugX](https://thehackernews.com/2025/01/fbi-deletes-plugx-malware-from-4250.html) is a [backdoor](https://security.googlecloudcommunity.com/community-blog-42/finding-malware-detecting-sogu-with-google-security-operations-3869) that supports commands to exfiltrate files, log keystrokes, launch a remote command shell, upload/download files, and is able to extend its functionality with additional plugins. Often launched via DLL side-loading, the implant is spread through USB flash drives, targeted phishing emails containing malicious attachments or links, or compromised software downloads.

The malware has existed since at least 2008 and is widely used by Chinese hacking groups. It is believed that ShadowPad is the successor of PlugX.

The UNC6384 attack chain is fairly straightforward in that adversary-in-the-middle (AitM) and social engineering tactics are used to deliver the PlugX malware -

* The target's web browser tests if the internet connection is behind a captive portal
* An AitM redirects the browser to a threat actor-controlled website
* STATICPLUGIN is downloaded from "mediareleaseupdates[.]com"
* STATICPLUGIN retrieves an MSI package from the same website
* CANONSTAGER is DLL side-loaded and deploys the SOGU.SEC backdoor in memory

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEi0hyHjJg1gsOwTwBUTh1b2Q8jX3tZgx1Wy6wrpzRAk0EhDga5bGmbPGIPIF4lsmh5uBBiZZJF3Pi290CviKxMmTPDlWGI9BcbGfDLb0Uf7TpeIZPGZCwWz0JEhFTEJt3Ck3Ap9yCQNbsOWLSncR-6ZzCGtY0yfQhqh3_FfMAvPb2tfF_8um0zsnbPG0wJC/s790-rw-e365/google.png)

The [captive portal](https://thehackernews.com/2025/07/secret-blizzard-deploys-malware-in-isp.html) hijack is used to deliver malware masquerading as an Adobe Plugin update to targeted entities. On the Chrome browser, the captive portal functionality is accomplished by means of a request to a hard-coded URL ("www.gstatic[.]com/generate\_204") that redirects users to a Wi-Fi login page.

While "gstatic[.]com" is a legitimate Google domain used to store JavaScript code, images, and style sheets as a way to enhance performance, Google said the threat actors are likely carrying out an AitM attack to initiate redirection chains from the captive portal page to the threat actor's landing web page.

It's assessed that the AitM is facilitated by means of compromised edge devices on the target networks, although the attack vector used to pull this off remains unknown at this stage.

[![CIS Build Kits](data:image/png;base64...)](https://thehackernews.uk/platform-shield-d)

"After being redirected, the threat actor attempts to deceive the target into believing that a software update is needed, and to download the malware disguised as a 'plugin update,'" GTIG said. "The landing web page resembles a legitimate software update site and uses an HTTPS connection with a valid TLS certificate issued by Let's Encrypt."

The end result is the download of an executable named "AdobePlugins.exe" (aka STATICPLUGIN) that, when launched, triggers the SOGU.SEC payload in the background using a DLL referred to as CANONSTAGER ("cnmpaui.dll") that's sideloaded using the Canon IJ Printer Assistant Tool ("cnmpaui.exe").

The STATICPLUGIN downloader is signed by Chengdu Nuoxin Times Technology Co., Ltd with a valid certificate issued by GlobalSign. Over two dozen malware samples signed by Chengdu have been put to use by China-nexus activity clusters, with the earliest artifacts dating back to at least January 2023. Exactly how these certificates are obtained by the [subscriber](https://csrc.nist.gov/glossary/term/subscriber) is not clear.

"This campaign is a clear example of the continued evolution of UNC6384's operational capabilities and highlights the sophistication of PRC-nexus threat actors," Whitsell said. "The use of advanced techniques such as AitM combined with valid code signing and layered social engineering demonstrates this threat actor's capabilities."

Found this article interesting? Follow us on [Google Ne...