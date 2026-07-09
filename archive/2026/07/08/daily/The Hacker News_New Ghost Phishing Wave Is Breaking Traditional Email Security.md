---
title: New Ghost Phishing Wave Is Breaking Traditional Email Security
url: https://thehackernews.com/2026/07/new-ghost-phishing-wave-is-breaking.html
source: The Hacker News
date: 2026-07-08
fetch_date: 2026-07-09T06:03:33.773652
---

# New Ghost Phishing Wave Is Breaking Traditional Email Security

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

# [New Ghost Phishing Wave Is Breaking Traditional Email Security](https://thehackernews.com/2026/07/new-ghost-phishing-wave-is-breaking.html)

**The Hacker News**Jul 08, 2026

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgl6gaxMQBH0Bjb1ZhuaOiM5gKEk-zuSf821eRfV33ogx6YWwENunjyOPF8VXHtgtHgIevENLfBV2O04QI4TtjtDe2PGGevWptQEEagmp6q-G4FqOankGokz70XzVtz7dmNbEZ5G7-pV0yINgd2-ima7ap8xeOxuhZBKw2WPoUo81wKmGrwsPxbzYkW5Wk/s1700-e365/anyrun-main.jpg)

A recent EvilTokens campaign targeting businesses across the US and Europe is exposing a new email security blind spot. This “ghost phishing” technique keeps the malicious page hidden until it decrypts and comes to life inside the victim’s browser.

For security leaders, the risk is clear: traditional URL checks may miss the attack while Microsoft 365 access, sensitive data, and response time are already at stake.

## The Email Looks Safe. The Browser Tells a Different Story

A recent EvilTokens attack shows how a phishing link can appear harmless during initial inspection while still leading to Microsoft 365 account takeover.

The kit uses Microsoft Device Code Phishing to convince victims to complete a legitimate Microsoft login flow and unknowingly authorize access to their accounts. It does not need to steal the password directly.

The real attack remains hidden until the page opens in the browser. Its HTML is encrypted with AES-GCM and becomes visible only after the browser decrypts it and renders the phishing content in the DOM.

As a result, static URL checks and network-level controls may capture the initial response without seeing what the employee actually sees. This visibility gap can lead to:

* **Longer exposure** to the Microsoft 365 account takeover
* **Delayed containment** and response decisions
* **Unauthorized access** to corporate email, files, and cloud services
* More uncertain **alerts escalated** to senior analysts
* Higher investigation **workload and operational costs**
* **Incomplete evidence** for blocking related infrastructure

The complete attack flow, however, was uncovered inside ANY.RUN’s Interactive Sandbox. Explore the analysis session to see what the browser revealed and how teams can use this evidence to respond faster.

[Check recent EvilTokens attack and get relevant IOCs](https://app.any.run/tasks/55d3ead7-c07a-4fb1-aa42-8c397d1a0f8a?utm_source=thehackernews&utm_medium=article&utm_campaign=ghost_phishing&utm_content=task&utm_term=080726)

|  |
| --- |
| [![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEifPPxwUNUUdcSUjFFwXjrkpJP3q8gjx-hpOGomTjEMRiOSqIZ61nbIhWyT9GI7M086X9XcjGCoLT51rfER_hUAKkDIWpz9h7zWwadQTw1dkNQeIujdiZT4fkD7wWwajVjF-_y6z4mDv8CTjIqdRZUi51uIX5j0OSwIazFz1yWXmy6PQZFzMVaAawWh611W/s1700-e365/any-1.jpg) |
| Complicated ghost phishing revealed inside ANY.RUN’s sandbox |

## Where Ghost Phishing Is Hitting Hardest

ANY.RUN’s Threat Intelligence shows recent EvilTokens activity concentrated across the US and Europe, targeting technology, manufacturing, education, banking, consulting, financial services, and managed security providers.

|  |
| --- |
| [![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgsS4RnFvKBFIdAT5bIOfeYQPD2bi5f7zPEHhgk3nSVekf0S3nfCjfYxS8qJ_zkRHJR5iY7BKlw8TF3RCXpHzCVEGNxiwLjUpdFLy7Dkm-yNlsk_rvUGABUVAGrP0GZ71OYQ3Llo6mhrQl-KY93H_f-SbYU-2oj-vn5mUmPkJqjPVcukIHbkbxqheCLvxGB/s1700-e365/any-2.jpg) |
| ANY.RUN’s TI shows threat activity targeting specific regions |

The overlap is hard to ignore. Based on ANY.RUN’s sandbox submissions data from 15,000 organizations, phishing exposure in 2026 reached **75.6% in consulting, 72.8% in financial services, 71.9% in manufacturing, 67.9% in technology, 66.7% in banking, and 66.1% among MSSPs**.

This makes hidden phishing especially dangerous for these sectors. One compromised Microsoft 365 account can expose sensitive data, enable business email compromise and fraud, and trigger costly incident response.

The longer the attack stays hidden, the greater the chance that one account becomes a wider business incident.

**Stop hidden phishing before it costs your business.**

Reduce exposure, incident costs, and account takeover risk.

[Close Visibility Gap](https://any.run/enterprise/?utm_source=thehackernews&utm_medium=article&utm_campaign=ghost_phishing&utm_content=enterprise&utm_term=080726#contact-sales)

## Make the Ghost Visible Before the Business Pays the Price

The most effective way to expose ghost phishing is to open suspicious links in a sandbox that supports in-browser data inspection.

Inside ANY.RUN’s Interactive Sandbox, analysts move beyond the encrypted AES-GCM response and see what happens after the page decrypts. They can watch the phishing content appear in the DOM, connect the change to a Fetch/XHR request, and trace the Microsoft device code back to the /api/device/start endpoint.

|  |
| --- |
| [![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEii92diC7QiJevKW3lj8HsoFIVrY_VotnnJuEtAXrzzsQastnjqSYt0pC6_SwYPffiWonsEzi2sd9wWbcRIZyOpjhxwQjJbx5WObWLC0W6PHFt7JP8gFTYs9veKSm3abNjN_goqdCCFsPFgV7KhxMZ2arQk9pSUoVMf_dQGcnMS18_y__mszCDontPO4WD5/s1700-e365/any-3.jpg) |
| The decrypted HTML DOM viewed in the in-browser data investigation panel |

The in-browser data view brings the full attack flow into one investigation:

* DOM snapshots show when the hidden page changes and the user code appears.
* HTTP requests reveal the backend communication behind the device-code flow.
* URL details expose the final destination and triggered detection signatures.
* Indicators provide domains, endpoints, hashes, and infrastructure for further hunting.

Instead of reconstructing the attack manually, teams get direct evidence of how the page behaves, what it requests, and which artifacts support containment and detection.

|  |
| --- |
| [![](data:image/png;base64...)](https://blogger.googleusercontent.com/im...