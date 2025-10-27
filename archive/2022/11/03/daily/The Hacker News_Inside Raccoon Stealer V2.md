---
title: Inside Raccoon Stealer V2
url: https://thehackernews.com/2022/11/inside-raccoon-stealer-v2.html
source: The Hacker News
date: 2022-11-03
fetch_date: 2025-10-03T21:41:21.506126
---

# Inside Raccoon Stealer V2

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

# [Inside Raccoon Stealer V2](https://thehackernews.com/2022/11/inside-raccoon-stealer-v2.html)

**Nov 02, 2022**The Hacker News

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgCpSguz8tfo2ScoXeg7032e5zmHXSJhHbVTntNnKXsJoh1OeMStq2UDe1RTULlBSlFcdK0kOUzEUXMNitrFuCjl2kvEtgdF4nXUd69joLZukQ-Py10H8HjkdIySHJRKhSIrHdgxD9SB02bqHocxrNGeLNsnK6194sgnDlMZ-CqNycNtOcJxsXxor_z/s790-rw-e365/racoon.jpg)

Raccoon Stealer is back on the news again. US officials arrested Mark Sokolovsky, one of the malware actors behind this program. In July 2022, after several months of the shutdown, a Raccoon Stealer V2 went viral. Last week, the Department of Justice's press release stated that the malware collected 50 million credentials.

This article will give a quick guide to the latest info stealer's version.

## What is Raccoon infostealer V2?

[Raccoon Stealer](https://any.run/malware-trends/raccoon?utm_source=hacker_news&utm_medium=article&utm_campaign=raccoon&utm_content=mtt) is a kind of malware that steals various data from an infected computer. It's quite a basic malware, but hackers have made Raccoon popular with excellent service and simple navigation.

In 2019, Raccoon infostealer was one of the most discussed malware. In exchange for $75 per week and $200 per month, cybercriminals sold this simple but versatile info stealer as a MaaS. The malware was successful in attacking a number of systems. In March 2022, however, threat authors ceased to operate.

An updated version of this malware was released in July 2022. As a result, Raccoon Stealer V2 has gone viral and gained a new name - RecordBreaker.

|  |
| --- |
| [![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjmpy2b2NI9WS_MWpyuNrjKdHwfzi0QJWjXFJkw3vmGcwyjk-chaHWFAxswbua3_nHcf9Ne9rWXGql1w9OVt5Ig_0vU8zm4NA26g8svzFnoSU4X5meJdzjazVVb-BRmuOhbj3rF6RavgK5kL2XyGQBKWTkzJq30kOtvegiKqEoC4X0zPUWv5I1Owq2C/s790-rw-e365/1.jpg) |
| Raccoon v2's tactics & techniques in ANY.RUN Sandbox |

## How to analyze Raccoon stealer V2

|  |  |
| --- | --- |
| **Execution process** | **What Raccoon malware does** |
| Downloads WinAPI libraries | Uses kernel32.dll!LoadLibraryW |
| Gets WinAPI functions’ addresses | Uses kernel32.dll!GetProcAddress |
| Strings and C2 servers encryption | Encrypts with RC4 or XOR algorithm, can be no encryption at all, or combination of different option |
| Crash triggers | CIS countries locale, mutex |
| System/LocalSystem level privilege check | Uses Advapi32.dll!GetTokenInformation and Advapi32.dll!ConvertSidToStringSidW comparing StringSid with L "S-1-5-18" |
| Process enumeration | Uses the TlHelp32 API (kernel32.dll!CreateToolhelp32Snapshot to capture processes and kernel32.dll!Process32First / kernel32.dll!Process32Next). |
| Connecting to C2 servers | Creates a string:  machineId={machineguid}|{username}&configId={rc4\_c2\_key}  Then sends a POST request |
| User and system data collection | * the OS bitness * information about RAM, CPU * applications installed in the system * cookies * autofill data * autofill form data |
| Sending of collected data | POST requests to C2. |
| Getting an answer from the C2 | C2 sends "received" |
| Finishing operations | Takes a screenshot(s), releases the remaining allocated resources, unloads the libraries, and finishes its work |

We have triaged multiple Raccoon stealer V2 samples, collected typical behavior activities, and briefly described its execution process.

Read deeper and more detailed [Raccoon stealer 2.0 malware analysis](https://any.run/cybersecurity-blog/raccoon-stealer-v2-malware-analysis/?utm_source=hacker_news&utm_medium=article&utm_campaign=raccoon&utm_content=blog). In the article, you can follow all steps and get a complete picture of the info stealer's behavior. Besides this profound research, you get a chance to extract malware configuration by yourselves – copy the Python script of Raccoon stealer and unpack memory dumps to extract C&C servers and keys.

|  |
| --- |
| [![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjegV9OwuuckID_YXeG2af_wMNe46nGIaHh8oYn0TnFVEi0g70md4IBE5JaM6edmLA6Qv2y4mBBucHPWzI_NxQQJ-gQls_zmXQIO_z9xbkttPRjlZa-pPqO0AsAfXgEsUIjehoKdPsvEI-e-F9TG-LJAmGYc2iUH0JqEVYXBclHhwBniXVHmfspel00/s790-rw-e365/2.jpg) |
| Raccoon v2 malware configuration |

## Where to analyze malware

Do you want to analyze malicious files and links? There is a fast and easy solution: get ready-made configurations in [ANY.RUN online malware sandbox](https://any.run/?utm_source=hacker_news&utm_medium=article&utm_campaign=raccoon&utm_content=landing) and investigate suspicious files inside and out. Try to crack any malware using an interactive approach:

> **Write the "HACKERNEWS" promo code at support@any.run using your business email address and get 14 days of ANY.RUN premium subscription for free!**

The ANY.RUN sandbox lets you analyze malware quickly, navigate through the research process easily, detect even sophisticated malware, and get detailed reports. Use smart tools and hunt malware successfully.

Found this article interesting? This article is a contributed piece from one of our valued partners. Follow us on [Google News](https://news.google.com/publications/CAAqLQgKIidDQklTRndnTWFoTUtFWFJvWldoaFkydGxjbTVsZDNNdVkyOXRLQUFQAQ), [Twitter](https://twitter.com/thehackersnews) and [LinkedIn](https://www.linkedin.com/company/thehackernews/) to read more exclusive content we post.

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

SHARE ...