---
title: Cybercriminals Use Unicode to Hide Mongolian Skimmer in E-Commerce Platforms
url: https://thehackernews.com/2024/10/cybercriminals-use-unicode-to-hide.html
source: The Hacker News
date: 2024-10-11
fetch_date: 2025-10-06T19:01:07.639974
---

# Cybercriminals Use Unicode to Hide Mongolian Skimmer in E-Commerce Platforms

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

# [Cybercriminals Use Unicode to Hide Mongolian Skimmer in E-Commerce Platforms](https://thehackernews.com/2024/10/cybercriminals-use-unicode-to-hide.html)

**Oct 10, 2024**Ravie LakshmananCybercrime / Malware

[![Mongolian Skimmer](data:image/png;base64... "Mongolian Skimmer")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiFJZxKkmbaY7u7Pd-8e-lC6RTxSr-A3UMV63LoDST-yAEuw5rPqqXfS1XQQOV5BuBRlzQdte2o4dtZ4GiTkcB0wT10YS84L_G46ivrFk3t4NjfRy1TdcMJ-UiLGYqDnyDlo-rWudPTSMTicBzN6Wp_DlnzLZqFwGa_1TwSCE9cGrCujWlLNCRjZ5GJffcB/s790-rw-e365/shopping.png)

Cybersecurity researchers have shed light on a new digital skimmer campaign that leverages Unicode obfuscation techniques to conceal a skimmer dubbed Mongolian Skimmer.

"At first glance, the thing that stood out was the script's obfuscation, which seemed a bit bizarre because of all the accented characters," Jscrambler researchers [said](https://jscrambler.com/blog/the-mongolian-skimmer) in an analysis. "The heavy use of Unicode characters, many of them invisible, does make the code very hard to read for humans."

The script, at its core, has been found to leverage [JavaScript's capability](https://tc39.es/ecma262/#sec-identifier-names) to use any Unicode character in identifiers to hide the malicious functionality.

[![DFIR Retainer Services](data:image/png;base64...)](https://thehackernews.uk/cloud-insight-d)

The end goal of the malware is to steal sensitive data entered on e-commerce checkout or admin pages, including financial information, which are then exfiltrated to an attacker-controlled server.

The skimmer, which typically manifests in the form of an inline script on compromised sites that fetches the actual payload from an external server, also attempts to evade analysis and debugging efforts by disabling certain functions when a web browser's [developer tools](https://developer.mozilla.org/en-US/docs/Learn/Common_questions/Tools_and_setup/What_are_browser_developer_tools) is opened.

"The skimmer uses well-known techniques to ensure compatibility across different browsers by employing both modern and legacy event-handling techniques," Jscrambler's Pedro Fortuna said. "This guarantees it can target a wide range of users, regardless of their browser version."

[![Mongolian Skimmer](data:image/png;base64... "Mongolian Skimmer")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiSTe-einr_iq3p0iNqVxHNv6A0_z-Vc7-ksJ-5Z_yIDD4bFk84T4joSA7rIghQkGL9x0V85h_k4EtVDPsXMXxdJU2EiMlJUNjeF1aVJ51eYkr7UP6XD59-LBYsSYwvGNywOIWLmN6-HRUUHPjjRKZBy1BqY9IWsxNd3sUFkqUy6Poe4raN6TTlbywjbgyI/s790-rw-e365/code.png)

The client-side protection and compliance company said it also observed what it described as an "unusual" loader variant that loads the skimmer script only in instances where user interaction events such as scrolling, mouse movements, and [touchstart](https://developer.mozilla.org/en-US/docs/Web/API/Element/touchstart_event) are detected.

This technique, it added, could serve both as an effective anti-bot measure and a way to ensure that the loading of the skimmer is not causing performance bottlenecks.

One of the Magento sites compromised to deliver the Mongolian skimmer is also said to have targeted by a [separate skimmer actor](https://jscrambler.com/blog/defcon-skimming-a-new-batch-of-web-skimming-attacks), with the two activity clusters leveraging source code comments to interact with each other and divide the profits.

[![CIS Build Kits](data:image/png;base64...)](https://thehackernews.uk/platform-shield-d)

"50/50 maybe?," remarked one of the threat actors on September 24, 2024. Three days later, the other group responded: "I agree 50/50, you can add your code :)"

Then on September 30, the first threat actor replied back, stating "Alright ) so how can I contact you though? U have acc on exploit? [sic]," likely referring to the Exploit cybercrime forum.

It's currently not known as to how the skimmer malware is delivered to target websites, although it's believed that the attackers are setting their sights on misconfigured or vulnerable Magento or Opencart instances.

"We have multiple victim websites, which might have been breached using different methods," Fortuna told The Hacker News. "We don't know exactly how they got there and were able to inject the web skimmer, but all signs point to compromised Magento or Opencart instances, either because they were poorly configured or because they had vulnerable components that the attackers exploited to get in."

"The obfuscation techniques found on this skimmer may have looked to the untrained eye as a new obfuscation method, but that was not the case," Fortuna noted. "It used old techniques to appear more obfuscated, but they are just as easy to reverse."

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

[browser security](https://thehackernews.com/search/label/browser%20security)[Cybercrime](https://thehackernews.com/search/label/Cybercrime)[cybersecurity](https://thehackernews.com/search/label/cybersecurity)[data breach](https://thehackernews.com/search/label/data%20breach)[E-commerce](https://thehackernews.com/search/label/E-commerce)[JavaScript](https://thehackernews.com/search/label/JavaScript)[Malware](https://thehacke...