---
title: Latest Multi-Stage Attack Scenarios with Real-World Examples
url: https://thehackernews.com/2024/11/latest-multi-stage-attack-scenarios.html
source: Instapaper: Unread
date: 2024-11-29
fetch_date: 2025-10-06T19:20:16.617296
---

# Latest Multi-Stage Attack Scenarios with Real-World Examples

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

# [Latest Multi-Stage Attack Scenarios with Real-World Examples](https://thehackernews.com/2024/11/latest-multi-stage-attack-scenarios.html)

**Nov 27, 2024**The Hacker NewsMalware / Threat Intelligence

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEifxU36dFq-0_Nr2b9YqWPBv4ezRzaAEW_ZaWB8KeTjpw2rC_teoIQEwdr0wQSpEBejQL-XMfVm19Vi0P16i3zxw9eo_HMut-ZFYqIlODzr54NbyakLKAuS1G7jRu3OkW3KNaPFCDCe9dPNb45rkAMAWVDebFz2ShiGG5Ulna_G9CrfFNe_Pry7g4nzuKs/s1500/main.png)

Multi-stage cyber attacks, characterized by their complex execution chains, are designed to avoid detection and trick victims into a false sense of security. Knowing how they operate is the first step to building a solid defense strategy against them. Let's examine real-world examples of some of the most common multi-stage attack scenarios that are active right now.

## URLs and Other Embedded Content in Documents

Attackers frequently hide malicious links within seemingly legitimate documents, such as PDFs or Word files. Upon opening the document and clicking the embedded link, users are directed to a malicious website. These sites often employ deceptive tactics to get the victim to download malware onto their computer or share their passwords.

Another popular type of embedded content is QR codes. Attackers conceal malicious URLs within QR codes and insert them into documents. This strategy forces users to turn to their mobile devices to scan the code, which then directs them to phishing sites. These sites typically request login credentials, which are immediately stolen by the attackers upon entry.

### Example: PDF File with a QR Code

To demonstrate how a typical attack unfolds, let's use the [ANY.RUN Sandbox](https://any.run/?utm_source=hacker_news&utm_medium=article&utm_campaign=attack_scenarios&utm_content=landing&utm_term=271124), which offers a safe virtual environment for studying malicious files and URLs. Thanks to its interactivity, this cloud-based service allows us to engage with the system just like on a standard computer.

[Get up to 3 ANY.RUN licenses as a gift with a Black Friday offer→](https://app.any.run/plans?utm_source=hacker_news&utm_medium=article&utm_campaign=attack_scenarios&utm_content=plans_1&utm_term=271124)

To simplify our analysis, we'll enable the Automated Interactivity feature that can perform all the user actions needed to trigger attack or sample execution automatically.

|  |
| --- |
| [![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgh4cUipRY4-wTdM6SsRZq5th4BzDvfGZmb65LIswaNzdmBa3aJSsFtnumE4XgDgnVDYroe08fn-4MZhyfhAEUbwUEuLKVjRSmEzY4HHAAAbHZPikTv41zPzXzcJ_FpAuLXiBFxKDczELysNtmgaA9kM6EOYsD9A0CZTukVCLpRof-f3p4wJZYZJ3z2Nv8/s1500/2.png) |
| Phishing PDF with malicious QR code opened in the ANY.RUN sandbox |

Consider [this sandbox session](https://app.any.run/tasks/757d88cf-897a-4b85-8c6a-9dab81b7466b?utm_source=hacker_news&utm_medium=article&utm_campaign=attack_scenarios&utm_content=task&utm_term=271124), which features a malicious .pdf file that contains a QR code. With automation switched on, the service extracts the URL inside the code and opens it in the browser by itself.

|  |
| --- |
| [![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEg5exUvrFLTo_Ey0X5eMdB3tBVSASu3fMR6QOCYuA91qbSPazPxlQn-4J2Z2fsazS3k-PZZG8UgMrdiAQ6N8CrbVZnX2K5ucw9PIPzQlLb7FQmGBzOfJs0QWG8FsV3WEhtihe84fielD3CgSlZK7U6JtLPnSGlSWqLxlr8w4tJKiP-ND6QfA2a42SmJcgQ/s1500/image2.png) |
| The final phishing page where victims are offered to share their credentials |

After a few redirects, the attack takes us to the final phishing page designed to mimic a Microsoft site. It is controlled by threat actors and configured to steal users' login and password data, as soon as it is entered.

|  |
| --- |
| [![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgaP_-ckIN-GXPkmnojnnX2GAXQgRxSNxJdqH2TY7PA8IxWpSAUu0oU-gMLfKTGtTYtu36ctzmSoN9WQ7RPheh5-J8vDE1hHnYL8a0PKSYn56rafsxKwQ7FNYkUkxtqanEvsNALY6UuaF-2MA4_NQJZvTdNxaTNLmKZUanaB0Yze079Pp6gsMjVj3ZBwxY/s1500/image3.png) |
| Suricata IDS rule identified a phishing domain chain during analysis |

The sandbox makes it possible to observe all the network activity occurring during the attack and see triggered Suricata IDS rules

After completing the analysis, the ANY.RUN sandbox provides a conclusive "malicious activity" verdict and generates a report on the threat that also includes a list of IOCs.

## Multi-stage Redirects

Multi-stage redirects involve a sequence of URLs that move users through multiple sites, ultimately leading to a malicious destination. Attackers often utilize trusted domains, such as Google's or popular social media platforms like TikTok, to make the redirects appear legitimate. This method complicates the detection of the final malicious URL by security tools.

Some redirect stages may include CAPTCHA challenges to prevent automated solutions and filters from accessing malicious content. Attackers might also incorporate scripts that check for the user's IP address. If a hosting-based address, commonly used by security solutions, is detected, the attack chain gets interrupted and the user is redirected to a legitimate website, preventing access to the phishing page.

### Example: Chain of Links Leading to a Phishing Page

Here is a [sandbox session](https://app.any.run/tasks/471b4e2e-ac66-47d9-a5c6-8b246a852236?utm_source=hacker_news&utm_medium=article&utm_campaign=attack_scenarios&utm_content=task&utm_term=271124) showing the entire chain of attack starting from a seemingly legitimate TikTok link.

|  |
| --- |
| [![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiBjX-lcyTlm35EJgUx7hYLrtgbigE1hljLEa-XbQsnhoz26dWetDVhjUNuh5ly2v-Q1uEbkiFCoThb6fGcZ9F9VJOybDctYgmrM7vqT2maUBAeCubCGGgquLxS28kVOZfsKbD3cXD-mIJhIXc9wbk0AnKtK9knAG5Xfjsgu19u6y2DsH0KvfkpSdF6mU0/s1500/image4.png) |
| TikTok URL containing a redirect to a Google domain |...