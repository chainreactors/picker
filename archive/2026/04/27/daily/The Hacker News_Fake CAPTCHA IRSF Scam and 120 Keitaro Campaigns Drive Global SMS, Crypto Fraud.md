---
title: Fake CAPTCHA IRSF Scam and 120 Keitaro Campaigns Drive Global SMS, Crypto Fraud
url: https://thehackernews.com/2026/04/fake-captcha-irsf-scam-and-120-keitaro.html
source: The Hacker News
date: 2026-04-27
fetch_date: 2026-04-28T05:28:40.530519
---

# Fake CAPTCHA IRSF Scam and 120 Keitaro Campaigns Drive Global SMS, Crypto Fraud

#1 Trusted Cybersecurity News Platform

Followed by 5.40+ million[**](https://twitter.com/thehackersnews)
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

# [Fake CAPTCHA IRSF Scam and 120 Keitaro Campaigns Drive Global SMS, Crypto Fraud](https://thehackernews.com/2026/04/fake-captcha-irsf-scam-and-120-keitaro.html)

**Ravie Lakshmanan**Apr 27, 2026Threat Intelligence / Social Engineering

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEi-cI0h0qDxREUkTFlIqeT_9-QNxJHPv6SqDQXpMs00i8A26QWukWlxtk1iwdZvnar80HiymWGDY9148_CiWIdL2xj-t9xC9KDM-8WdGALuTRxhdZqDcaZf2MG9adEpZLkLqsaA2uMP-3e_E0Ru-A5JSv0_dvEjAAniYpsdS71SCxFVlmB1NhkL20oangQz/s1700-e365/sim-card.jpg)

Cybersecurity researchers have disclosed details of a telecommunications fraud campaign that uses fake CAPTCHA verification tricks to dupe unsuspecting users into sending international text messages that incur charges on their mobile bills, generating illicit revenue for the threat actors who lease the phone numbers.

According to a new report published by Infoblox, the operation is believed to have been active since at least June 2020, using methods like social engineering and [back button hijacking](https://thehackernews.com/2026/04/threatsday-bulletin-17-year-old-excel.html#crackdown-on-navigation-abuse) in web browsers. As many as 35 phone numbers spanning 17 countries have been observed as part of the international revenue share fraud ([IRSF](https://www.ndss-symposium.org/ndss-paper/understanding-and-detecting-international-revenue-share-fraud/)) campaign.

"The fake CAPTCHA has multiple steps, and each message crafted by the site is preconfigured with over a dozen phone numbers, meaning the victim isn't charged for just a single message – they're charged for sending SMSs to over 50 international destinations," researchers David Brunsdon and Darby Wise [said](https://www.infoblox.com/blog/threat-intelligence/hold-the-phone-international-revenue-share-fraud-driven-by-fake-captchas/) in an analysis.

"This type of scam also benefits from delayed billing, as the 'international SMS' charges often appear on the victim's bill weeks later and the experience with the fake CAPTCHA has been long forgotten."

What makes the threat notable is the coming together of revenue share fraud and malicious traffic distribution systems ([TDSs](https://unit42.paloaltonetworks.com/detect-block-malicious-traffic-distribution-systems/)), with the activity using the infrastructure -- traditionally responsible for routing traffic to malware or phishing pages though a redirection chain to evade detection – to conduct SMS scams at scale.

IRSF schemes involve fraudsters illegally acquiring international premium rate numbers (IPRN) or number ranges and artificially inflating the volume of international calls or messages to those numbers to receive a share of the revenue generated from these calls from termination charges obtained by the number range holder for inbound traffic to the number ranges.

In this context, a termination fee refers to the inter-carrier charges paid by an originating telecom operator to a terminating operator for completing a call on their network. It's the exploitation of these "revenue sharing" agreements that drives IRSF, as the originating carrier ends up paying termination fees to the destination network for the incoming calls to the high-cost destinations, a portion of which is split with the fraudsters.

Infoblox said the observed campaign specifically registers phone numbers in countries with high termination fees or lax regulations, such as Azerbaijan, Kazakhstan, or certain premium-rate number ranges in Europe, and colludes with local telecom providers to pull off the scam.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/ai-blindspot-d-2)

The entire campaign plays out like this: a user is redirected to a bogus web page using a commercial TDS, which serves a CAPTCHA that instructs them to send an SMS to "confirm you are human."This, in turn, triggers a multi-stage "verification" chain, with each step triggering a separate SMS message to the server-designated numbers by programmatically launching the SMS apps on both Android and iOS devices with the phone numbers and message content pre-filled.

In the process, as many as 60 SMS messages are sent to 15 unique numbers after four steps of CAPTCHA, which could end up costing a user $30. While it may be a relatively small amount, the DNS threat intelligence firm warned that they could quickly add up for the threat actor when carried out at scale. The list of phone numbers spans 17 countries, such as Azerbaijan, the Netherlands, Belgium, Poland, Spain, and Turkey.

The campaign heavily relies on cookies to track progression through the fake verification flow, using values stored in certain cookies (e.g., "successRate") to determine the next course of action.If a user is deemed not suitable for the campaign, the page is designed to redirect them to an entirely different CAPTCHA page that's likely part of a separate campaign or controlled by a different actor.

Another novel strategy adopted by the scam operators is the use of back button hijacking, which relies on JavaScript to alter the browsing history such that any attempt made by the site visitor to navigate away from the CAPTCHA page by hitting the browser's back button redirects the user back to the fake page, effectively trapping them in a navigation loop unless they opt to fully exit the browser.

|  |
| --- |
| [![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhb670rc1sgExTGEIDHKJ6qv6NcuizV6WFdQnwMLiSgQ514UTbQWxdNar84VUydenV4eTFF8Jai6l0gj6q6WP-vNJy1AfforY6Gk6flf9A_Vf845IMJ_Vg89hoKrX75XyQOwf7h14jLaXyVk9xGTiL7FSUu6RXQO7YN5_ApukhXs4L2JhBRRA20v1Lyh7cS/s1700-e365/time.jpg) |
| Redirection chain leading to a fake CAPTCHA page |

"This operation defrauds both individuals and telecommunication carriers simultaneously. Individual victims face unexpected premium SMS charges on their bills and would have difficulty identifying and reporting the fraud when it originates from such an unexpected source," Infoblox concluded. "Telecom carriers pay revenue share to the perpetrators while likely absorbing the losses from customer disputes or chargebacks."

### How Threat Actors Abuse Keitaro TDS

The disclosure comes as the company, in collaboration with [Confiant](https://blog.confiant.com/p/tracking-software-weaponized-...