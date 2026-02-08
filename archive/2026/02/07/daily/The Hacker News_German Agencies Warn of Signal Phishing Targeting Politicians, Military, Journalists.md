---
title: German Agencies Warn of Signal Phishing Targeting Politicians, Military, Journalists
url: https://thehackernews.com/2026/02/german-agencies-warn-of-signal-phishing.html
source: The Hacker News
date: 2026-02-07
fetch_date: 2026-02-08T04:32:19.807049
---

# German Agencies Warn of Signal Phishing Targeting Politicians, Military, Journalists

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

[![Security Service Edge](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEg5Ij_-TeqFMEsRFzgRRFzSRlVK6oHCncN_eJ2fkOdsA_1tN9HQbAlEEife2Z2JUt1lPv4st5n9KZP84jGEYY9Up6BQ7QE-N5rs6OhzL5thxGzVxnMx3JH9cGRLi9S5Kl-iV5PgjBeTdkBLnv_inF8UUAo88iqdmgJuPIc_6qiPyUMXwFyZWbZvkZkcRXSw/s728-e100/gartner-d.jpg)](https://thehackernews.uk/sse-awards-insight-d)

# [German Agencies Warn of Signal Phishing Targeting Politicians, Military, Journalists](https://thehackernews.com/2026/02/german-agencies-warn-of-signal-phishing.html)

**Ravie Lakshmanan**Feb 07, 2026Threat Intelligence / Cyber Espionage

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgZLxiSHzgB4jnGhqSTb5U-LmLyQn1DAEdjL73NAKb8oapBTIPlINZbiOL3pHZNBlOHYI9yuZgxV8aRvGefuo5OzaP8TVtvoHYznKe-5Lr493T9s7hOHGCqNqXhgm-4r_biXNbYjuaRGDTcfNNwqoZNVBkKwfdAud8ropOXgONMa7xizOHOWM0DCpDQaFZ9/s1700-e365/signal.jpg)

Germany's Federal Office for the Protection of the Constitution (aka Bundesamt für Verfassungsschutz or BfV) and Federal Office for Information Security (BSI) have issued a joint advisory warning of a malicious cyber campaign undertaken by a likely state-sponsored threat actor that involves carrying out phishing attacks over the Signal messaging app.

"The focus is on high-ranking targets in politics, the military, and diplomacy, as well as investigative journalists in Germany and Europe," the agencies [said](https://www.verfassungsschutz.de/SharedDocs/kurzmeldungen/DE/2026/2026-02-06-gemeinsamer-sicherheitshinweis-phishing.html). "Unauthorized access to messenger accounts not only allows access to confidential private communications but also potentially compromises entire networks."

A noteworthy aspect of the campaign is that it does not involve the distribution of malware or the exploitation of any security vulnerability in the privacy-focused messaging platform. Rather, the end goal is to weaponize its legitimate features to obtain covert access to a victim's chats, along with their contact lists.

The attack chain is as follows: the threat actors masquerade as "Signal Support" or a support chatbot named "Signal Security ChatBot" to initiate direct contact with prospective targets, urging them to provide a [PIN](https://support.signal.org/hc/en-us/articles/360007059792-Signal-PIN) or verification code received via SMS, or risk facing data loss.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/sse-customer-awards-d)

Should the victim comply, the attackers can register the account and gain access to the victim's profile, settings, contacts, and block list through a device and mobile phone number under their control. While the stolen PIN does not enable access to the victim's past conversations, a threat actor can use it to capture incoming messages and send messages posing as the victim.

That target user, who has by now lost access to their account, is then instructed by the threat actor disguised as the support chatbot to register for a new account.

There also exists an alternative infection sequence that takes advantage of the [device linking option](https://support.signal.org/hc/en-us/articles/360007320551-Linked-Devices) to trick victims into scanning a QR code, thereby granting the attackers access to the victim's account, including their messages for the last 45 days, on a device managed by them.

In this case, however, the targeted individuals continue to have access to their account, little realizing that their chats and contact lists are now also exposed to the threat actors.

The security authorities warned that while the current focus of the campaign appears to be Signal, the attack can also be extended to WhatsApp since it also incorporates similar [device linking](https://faq.whatsapp.com/1317564962315842/) and PIN features as part of [two-step verification](https://faq.whatsapp.com/1278661612895630/).

"Successful access to messenger accounts not only allows confidential individual communications to be viewed, but also potentially compromises entire networks via group chats," BfV and BSI said.

While it's not known who is behind the activity, similar attacks have been orchestrated by multiple Russia-aligned threat clusters tracked as [Star Blizzard](https://thehackernews.com/2025/01/russian-star-blizzard-shifts-tactics-to.html), [UNC5792 (aka UAC-0195), and UNC4221 (aka UAC-0185)](https://thehackernews.com/2025/02/hackers-exploit-signals-linked-devices.html), per reports from Microsoft and Google Threat Intelligence Group early last year.

In December 2025, Gen Digital also [detailed](https://thehackernews.com/2025/12/threatsday-bulletin-whatsapp-hijacks.html#whatsapp-hijack-campaign) another campaign codenamed GhostPairing, where cybercriminals have resorted to the device linking feature on WhatsApp to seize control of accounts to likely impersonate users or commit fraud.

To stay protected against the threat, users are advised to refrain from engaging with support accounts and entering their Signal PIN as a text message. A crucial line of defense is to enable Registration Lock, which prevents unauthorized users from registering a phone number on another device. It's also advised to periodically review the list of linked devices and remove any unknown devices.

The development comes as the [Norwegian government](https://www.pst.no/trusselbilde/dagens-trusselbilde/artikkel-dagens-trusselbilde/) accused the Chinese-backed hacking groups, including [Salt Typhoon](https://thehackernews.com/2025/08/salt-typhoon-exploits-cisco-ivanti-palo.html), of breaking into several organizations in the country by exploiting vulnerable network devices, while also calling out Russia for closely monitoring military targets and allied activities, and Iran for keeping tabs on dissidents.

Stating that Chinese intelligence services attempt to recruit Norwegian nationals to gain access to classified data, the Norwegian Police Security Service (PST) noted that these sources are then encouraged to establish their own "human source" networks by advertising part-time positions on job boards or approaching them via LinkedIn.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/ztw-hands-on-d)

The agency further warned that China is "systematically" exploiting collaborative research and development efforts to strengthen its own security and intelligence capabilities. It's wort...