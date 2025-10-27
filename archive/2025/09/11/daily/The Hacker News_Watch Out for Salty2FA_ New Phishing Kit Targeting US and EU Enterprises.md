---
title: Watch Out for Salty2FA: New Phishing Kit Targeting US and EU Enterprises
url: https://thehackernews.com/2025/09/watch-out-for-salty2fa-new-phishing-kit.html
source: The Hacker News
date: 2025-09-11
fetch_date: 2025-10-02T20:00:55.074884
---

# Watch Out for Salty2FA: New Phishing Kit Targeting US and EU Enterprises

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

# [Watch Out for Salty2FA: New Phishing Kit Targeting US and EU Enterprises](https://thehackernews.com/2025/09/watch-out-for-salty2fa-new-phishing-kit.html)

**Sep 10, 2025**The Hacker NewsMalware Analysis / Enterprise Security

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhJi9QFUSwlPKRn3FHU83en34RJb1N5LLHP-KmyBaJnCNWXQr85kpCkIEjWimyZeJzOqqUHyL7D-WFwfKs1JChzylQ4Ov_yOZVLYyYwUlX9KreSFkMSxEOEBXSYFAOWeSkzZaBhJqUR8v3RDGQ9x3S7K0sCuVpzqZrLLsW8wMvLbniGL-Sazb8o8AtoKfI/s790-rw-e365/main.jpg)

Phishing-as-a-Service (PhaaS) platforms keep evolving, giving attackers faster and cheaper ways to break into corporate accounts. Now, researchers at **ANY.RUN** has uncovered a new entrant: **Salty2FA**, a phishing kit designed to bypass multiple two-factor authentication methods and slip past traditional defenses.

Already spotted in campaigns across the US and EU, Salty2FA puts enterprises at risk by targeting industries from finance to energy. Its multi-stage execution chain, evasive infrastructure, and ability to intercept credentials and 2FA codes make it one of the most dangerous PhaaS frameworks seen this year.

## Why Salty2FA Raises the Stakes for Enterprises

Salty2FA's ability to **bypass push, SMS, and voice-based 2FA** means stolen credentials can lead directly to account takeover. Already aimed at finance, energy, and telecom sectors, the kit turns common phishing emails into high-impact breaches.

### Who is Being Targeted?

ANY.RUN analysts mapped Salty2FA campaigns and found activity spanning multiple regions and industries, with the **US and EU enterprises most heavily hit**.

|  |  |
| --- | --- |
| **Region** | **Key Targeted Industries** |
| **United States** | Finance, healthcare, government, logistics, energy, IT consulting, education, construction |
| **Europe (UK, Germany, Spain, Italy, Greece, Switzerland)** | Telecom, chemicals, energy (including solar), industrial manufacturing, real estate, consulting |
| **Worldwide / Other** | Logistics, IT, metallurgy (India, Canada, France, LATAM) |

### When Did Salty2FA Start Hitting Enterprises?

Based on data from the ANY.RUN Sandbox and TI, Salty2FA activity began gaining momentum in June 2025, with early traces possibly dating back to March–April. Confirmed campaigns have been active since late July and continue to this day, generating dozens of fresh analysis sessions daily.

## Real-World Case: How Salty2FA Exploits Enterprise Employees

One recent case analyzed by ANY.RUN shows just how convincing Salty2FA can be in practice. An employee received an email with the subject line **"External Review Request: 2025 Payment Correction",** a lure designed to trigger urgency and bypass skepticism.

When opened in the ANY.RUN sandbox, the attack chain unfolded step by step:

[View real-world case of Salty2FA attack](https://app.any.run/tasks/7d8e3a4d-5226-40b9-9e94-0f833c784abc/?utm_source=thehackernews&utm_medium=article&utm_campaign=salty2fa&utm_content=task&utm_term=100925)

|  |
| --- |
| [![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgm2eUo7HRB3ecAszds9_Q9QQNDFeO7r9Jnh8bn5HApH9GzI2CEV_dYRfW6SeWHRAQSIigxS89aE-7erBQ2gwiEtTbHXnZJ-1DFIUB60Zr9dKIsSqL5dLMfTDHys8Y8UJSLjq3EM6GC6KsBnaKssP_HOXI_9Z7sbjWOOQyD3oeuc7uxEEnm1x9US4w8yzM/s790-rw-e365/1.png) |
| Malicious email with Salty2FA attack analyzed inside ANY.RUN sandbox |

#### **Stage 1: Email lure**

The email contained a payment correction request disguised as a routine business message.

Join 15K+ enterprises worldwide that cut investigation time and stop breaches faster with ANY.RUN

[Get started now](https://any.run/enterprise/?utm_source=thehackernews&utm_medium=article&utm_campaign=salty2fa&utm_content=enterprise_1&utm_term=100925)

#### **Stage 2: Redirect and fake login**

The link led to a Microsoft-branded login page, wrapped in Cloudflare checks to bypass automated filters. In the sandbox, ANY.RUN's Automated Interactivity handled the verification automatically, exposing the flow without manual clicks and cutting investigation time for analysts.

|  |
| --- |
| [![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEinHozjflFSk4UChyphenhyphenrNC_A3gweZSgXTbnS8nlJfV6HmRbczv_9mHWB4BZIYlPK9jGArAQ1CF3PZAG2Z-RW1Bl-B8tHsc2vWWQuZYmBGcZP2i5EQQj3ZeUv1VVhrnGiiZHX5qw9n1RZRGOKhdsCRyY6Rq_nw1-nl8eFWuFK3KJoVjyDoWkpEllY3wsXwYWc/s790-rw-e365/2.png) |
| Cloudflare verification completed automatically inside ANY.RUN sandbox |

#### **Stage 3: Credential theft**

Employee details entered on the page were harvested and exfiltrated to attacker-controlled servers.

|  |
| --- |
| [![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgP2f59RJpGeIvgTXbqCpTSAQSqhJyug0LvSTSmZHE1WPN97efWnk7HzCK8QeTWSHEh9ySttsT6jQh4CIJt1OqlwRYjvfUy3J4LEPNc-YzYZcfvcRVrBpmpe7Tiyw4vXfq0TZyphWjtceClVxjjgjxNroOZwnkhmmY5dRJkJHwxBFBiKeTZxK7c3xtCBPM/s790-rw-e365/3.png) |
| Fake Microsoft page, ready to steal credentials from victims |

#### **Stage 4: 2FA bypass**

If the account had multi-factor authentication enabled, the phishing page prompted for codes and could intercept push, SMS, or even voice call verification.

By running the file in the sandbox, SOC teams could see the full execution chain in real time, from the first click to credential theft and 2FA interception. This level of visibility is critical, because static indicators like domains or hashes mutate daily, but behavioral patterns remain consistent. Sandbox analysis gives faster confirmation of threats, reduced analyst workload, and better coverage against evolving PhaaS kits like Salty2FA.

## Stopping Salty2FA: What SOCs Should Do Next

Salty2FA shows how fast phishing-as-a-service is evolving and why static indicators alone won't stop it. For SOCs and security leaders, protection means shifting focus to behaviors and response speed:

* **Rely on behavioral detection:** Track recurring patterns like domain structures and page logic rather than chasi...