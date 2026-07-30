---
title: Flying Eagle Android RAT Traces Found on 170 Servers as Source Code Circulates
url: https://thehackernews.com/2026/07/flying-eagle-android-rat-traces-found.html
source: The Hacker News
date: 2026-07-29
fetch_date: 2026-07-30T04:52:45.510083
---

# Flying Eagle Android RAT Traces Found on 170 Servers as Source Code Circulates

#1 Trusted Cybersecurity News Platform

Followed by 5.70+ million[**](https://twitter.com/thehackersnews)
[**](https://www.linkedin.com/company/thehackernews/)
[**](https://www.facebook.com/thehackernews)

[![The Hacker News Logo](data:image/png;base64...)](/)

**

**

[** Get the Latest News](#email-outer)

* [Home](/)
* [Newsletter](#email-outer)
* [Webinars](/p/upcoming-hacker-news-webinars.html)

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

[![cybersecurity](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgrKWHErc__Wn0forfQ5eJ5sIR1hVKCHCTeNQOaAX4lbygJ8S1Xpemx6JXl78dpwiT65DDBGURp48A3EemKzmli-jXPI3v1928MnJm-1j2ZPUaFXCvuySFhyphenhyphenKR-Li6fAinFT2bhLgsqUSNUR_ggMAnOHi3jD1qYWHXvueX8WdtxAd6GYety9cBGYABo18hX/s728-e100/tt-d.jpg)](https://thehackernews.uk/ai-zero-trust-h-d)

# [Flying Eagle Android RAT Traces Found on 170 Servers as Source Code Circulates](https://thehackernews.com/2026/07/flying-eagle-android-rat-traces-found.html)

**Swati Khandelwal**Jul 29, 2026Mobile Security / Threat Intelligence

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhOpdosdOAoAjpR73DY5i_8YN9dHOY7KsBws53ivjlY3iVg0-EZAO6CliWbdg61_hT6eI9_Im9aiH_c312ttIHamIl4IIxe2omPSWjC4OaCfbNKZC7Gr85jXs12NObtpiSAK1PNljccRdmzvITRijNNh16c2IDK3kWmL5Ce3lbzQNCJaMy4wgKwWyB2oiI/s1700-e365/android-rat.jpg)

Source code for the **Flying Eagle** Android remote access trojan (RAT) framework is circulating through criminal Telegram channels. Hunt.io and independent researcher NetAskari traced matching control panels and certificates to 170 internet servers.

They linked the framework to a fake "公安一网通办" Public Security service application targeting Android users in China. The kit supports payment-password and keystroke capture, screen recording, camera access, and phishing prompts for financial, adult-content, and government-service applications.

Hunt.io's search of the preceding 30 days of telemetry found infrastructure fingerprints on 170 servers, a count that does not establish 170 infected phones, victims, operators, or confirmed command-and-control (C2) systems.

The researchers found 158 servers through the AdminPro page title, HTTPS redirect behaviour, and matching response headers, then identified 12 more through a default certificate packaged with Flying Eagle. They said the total is likely conservative because it excluded otherwise similar servers that did not return the expected 302 redirect.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/ai-vuln-protection-d)

Chinese authorities advised anyone who installed the fraudulent application to remove it, scan the device, change affected account passwords, freeze payment channels if funds moved, and report the incident to police.

[China's National Cybersecurity Notification Center](https://www.jswx.gov.cn/anquan/guanli/202606/t20260618_1338409.shtml) warned on June 18 that the fake application was being distributed from 110gongan[.]com, associated with 207.56.30[.]188, and could steal payment data and remotely control devices.

According to [joint research](https://hunt.io/blog/flying-eagle-android-rat-170-servers-night-dragon) published July 28, the Flying Eagle code was distributed as a 388 MB archive called **中国龙.zip**, or **Chinese Dragon**. It contains a full Docker deployment with nginx, PHP, MySQL, a Node.js WebSocket server, Android build tools, phishing templates, and a default Transport Layer Security certificate.

The panel lets an operator choose an app name, icon, lure text, and C2 address, then produces a signed APK from one of two templates. The builder randomises package and class names, encrypts embedded C2 URLs using AES-128-CBC, and adds 2.8 MB to 3.5 MB of low-entropy JSON padding designed to resemble legitimate software development kit configuration data.

Flying Eagle is the builder and control framework; Hunt.io said samples it analysed from the builder were detected as [SpyNote](https://thehackernews.com/2023/10/spynote-beware-of-this-android-trojan.html) and used Android accessibility services for privilege escalation and gesture injection.

The researchers observed two Telegram channels, SQLRCE0 and Yx Technology, distributing modified versions of the framework. Messages reviewed by them claimed an unidentified party had compromised customer infrastructure containing 189 Flying Eagle servers and exfiltrated database data, but neither claim has been independently confirmed. Yx Technology also advertised cash-out services charging 20% to 50% of the transaction value.

[![Cybersecurity](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhrEy9jEFSadp95ztaH87-97Z_U9V94nUsE-BsrdwSR8ETPJDyCjy63vNxc-O26z6VhA3nDOrU24lJqNdy24bfNxGPxGxXNRvM_XCwnZ7ukY5wDnXKsvDZN42aCT1JFYXZZGoZFEtSQgbba742oPTEgEbtoa0GBYWWkkkU43P1wPq-LByZPJfbzwZsb1RiI/s728-e100/sygnia-d-1.png)](https://thn.news/sygnia-webinar)

The server count and the source-code circulation are documented, but no causal relationship between them has been established.

SQLRCE0 introduced a separate Android control kit called **Night Dragon** on June 23, 2026. The researchers found two associated servers and an exposed panel that listed 46 devices as online and 29 as actively connected, but said it could not determine whether the entries represented victims or test data.

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgrfU5uKPGPa_6vWvxdOeiGrULyqxP2X5vYjVFPv-w2hd10C_knnEdh99zEQsC06k8TuBIRx7Vgq-7gmwBQ3-pcyNnnk4If5yjYegO-u0-hcARIXan7RtNG9xwNsUv1sSuVDKt_ZjU68pITx6evnSMLuYPr5diQU6ZUkmXLhLTAeKKHyuAAY7_MhZYwsa4/s1700-e365/Night.png)

Hunt.io says Night Dragon appears to be an independent build, with a second version in development as of July 12. The report establishes that SQLRCE0 distributed Flying Eagle and promoted Night Dragon, but it does not establish shared code. This is not the 2011 China-linked espionage campaign [McAfee](https://www.mcafee.com/blogs/wp-content/uploads/2011/02/McAfee_NightDragon_wp_draft_to_customersv1-1.pdf) named [Night Dragon](https://thehackernews.com/2011/02/chinese-hackers-penetrate-multinational.html). The 2026 kit is financially motivated Android crimeware.

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
[**Share on Reddit](#lin...