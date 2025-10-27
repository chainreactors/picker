---
title: Researchers Shed Light on CatB Ransomware's Evasion Techniques
url: https://thehackernews.com/2023/03/researchers-shed-light-on-catb.html
source: The Hacker News
date: 2023-03-21
fetch_date: 2025-10-04T10:11:55.596053
---

# Researchers Shed Light on CatB Ransomware's Evasion Techniques

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

# [Researchers Shed Light on CatB Ransomware's Evasion Techniques](https://thehackernews.com/2023/03/researchers-shed-light-on-catb.html)

**Mar 20, 2023**Ravie LakshmananEndpoint Security / Ransomware

[![CatB ransomware](data:image/png;base64... "CatB ransomware")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhfUzpIOIx2h6lQD82z36I552Ne7thvde104A4cCQdzQuVMA1EZypMzoL4KWaod6VU67-IGIFVu5BP_SoCs0Y-SYFlxk7xyH5SvF7tYxe9QvAAQz67XDy3mJ9N1R_Mu40DbS0P-ah2mqtbcUolmUBH4FBnUuvt38oTW0FJGTN_yGjLvILgIVGrL-82E/s790-rw-e365/cmd.png)

The threat actors behind the CatB ransomware operation have been observed using a technique called [DLL search order hijacking](https://attack.mitre.org/techniques/T1574/001/) to evade detection and launch the payload.

CatB, also referred to as CatB99 and Baxtoy, emerged late last year and is said to be an "evolution or direct rebrand" of another ransomware strain known as Pandora based on code-level similarities.

It's worth noting that the use of Pandora has been attributed to [Bronze Starlight](https://thehackernews.com/2022/06/state-backed-hackers-using-ransomware.html) (aka DEV-0401 or Emperor Dragonfly), a China-based threat actor that's known to employ [short-lived ransomware families](https://thehackernews.com/2022/10/researchers-link-cheerscrypt-linux.html) as a ruse to likely conceal its true objectives.

One of the key defining characteristics of CatB is its reliance on DLL hijacking via a legitimate service called Microsoft Distributed Transaction Coordinator ([MSDTC](https://en.wikipedia.org/wiki/Microsoft_Distributed_Transaction_Coordinator)) to extract and launch the ransomware payload.

[![DFIR Retainer Services](data:image/png;base64...)](https://thehackernews.uk/cloud-insight-d)

"Upon execution, CatB payloads rely on DLL search order hijacking to drop and load the malicious payload," SentinelOne researcher Jim Walter [said](https://www.sentinelone.com/blog/decrypting-catb-ransomware-analyzing-their-latest-attack-methods/) in a report published last week. "The dropper (versions.dll) drops the payload (oci.dll) into the System32 directory."

[![CatB ransomware](data:image/png;base64... "CatB ransomware")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgSB__pCCaY5Vs4ziZptQAHsFd50JDPd-KWbAqtfBROWDQhBw20Ts1KVl_ZaCFIWVGXV3BZltXkC3unejBvTqdkcEYPrF4vnOBhnIFrt_i39YNf2TnfDsZU-GimIF2lB72dcK9B8xyMSeV_rbrGgoeW3uUl3Kw3ybHxGvYiOX3_U0qAba3r4Yxp-6lX/s790-rw-e365/code.png)

The dropper is also responsible for carrying out anti-analysis checks to determine if the malware is being executed within a virtual environment, and ultimately abusing the MSDTC service to inject the rogue oci.dll containing the ransomware into the msdtc.exe executable upon system restart.

"The [MSDTC] configurations changed are the name of the account under which the service should run, which is changed from Network Service to Local System, and the service start option, which is changed from Demand start to Auto start for persistency if a restart occurs," Minerva Labs researcher Natalie Zargarov [explained](https://minerva-labs.com/blog/new-catb-ransomware-employs-2-year-old-dll-hijacking-technique-to-evade-detection/) in a previous analysis.

One striking aspect of the ransomware is its absence of a ransom note. Instead, each encrypted file is updated with a message urging the victims to make a Bitcoin payment.

[![CIS Build Kits](data:image/png;base64...)](https://thehackernews.uk/platform-shield-d)

Another trait is the malware's ability to harvest sensitive data such as passwords, bookmarks, history from web browsers Google Chrome, Microsoft Edge (and Internet Explorer), and Mozilla Firefox.

[![CatB ransomware](data:image/png;base64... "CatB ransomware")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhT_3-sAA17UUdvsMtFw--uqQfLRDCyNblQCn90g0t26p85BGja2ZxKE5ACVBlUkAoBW2l8dQdDkQkgYblV4kDnEERxfYOYol25vLNTMlwXAchxzNWM4sZXHBnS-eHSoictrQrum3yJree4WIqVwO2hf3LpS-eNznDLXPm2sw2jvlEAuXcagA5NiqfM/s790-rw-e365/note.png)

"CatB joins a long line of ransomware families that embrace semi-novel techniques and atypical behaviors such as appending notes to the head of files," Walter said. "These behaviors appear to be implemented in the interest of detection evasion and some level of anti-analysis trickery."

This is not the first time the MSDTC service has been weaponized for malicious purposes. In May 2021, Trustwave disclosed a novel malware dubbed [Pingback](https://thehackernews.com/2021/05/new-pingback-malware-using-icmp.html) that leveraged the same technique to achieve persistence and bypass security solutions.

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

[hacking news](https://thehackernews.com/search/label/hacking%20news)[Malware](https://thehackernews.com/search/label/Malware)[ransomware](https://thehackernews.com/search/label/ransomware)

[![c](data:image/svg+xml;base64...)](https://thehackernews.uk/cloud-defense)

Trending News

[![SolarWinds Releases Hotfix for Critical CVE-2025-26399 Remote Code Execution Flaw](data:image/svg+xml;base64... "SolarWinds Releases Hotfix for Critical CVE-2025-26399 Remote Code Execution Flaw")

SolarWinds Releases Hotfix for Critical CVE-2025-26399 Remote Code Execution F...