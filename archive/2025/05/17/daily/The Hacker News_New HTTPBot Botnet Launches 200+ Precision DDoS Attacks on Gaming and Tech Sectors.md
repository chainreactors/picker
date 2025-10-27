---
title: New HTTPBot Botnet Launches 200+ Precision DDoS Attacks on Gaming and Tech Sectors
url: https://thehackernews.com/2025/05/new-httpbot-botnet-launches-200.html
source: The Hacker News
date: 2025-05-17
fetch_date: 2025-10-06T22:33:18.224438
---

# New HTTPBot Botnet Launches 200+ Precision DDoS Attacks on Gaming and Tech Sectors

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

# [New HTTPBot Botnet Launches 200+ Precision DDoS Attacks on Gaming and Tech Sectors](https://thehackernews.com/2025/05/new-httpbot-botnet-launches-200.html)

**May 16, 2025**Ravie LakshmananUnited States

[![HTTPBot Botnet](data:image/png;base64... "HTTPBot Botnet")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEg6ZuMt2KPpcbyNQYKoEGWSfnho5XCjBP6WvQGULfrPq7ubmBLJo-jVUvEg9YZGxKBp2usM4v3O0LBBS0dNiXf26ioMDk5_DvluI8suFm1cTiNrbUO38pfd137klW3sanUZoUhINOVn5n0bTj_8IvDb7-NzRxJcUE5KckvPHlI9eCV_H1iJsBsfGK8dtRNV/s790-rw-e365/gamer-ddos.png)

Cybersecurity researchers are calling attention to a new botnet malware called **HTTPBot** that has been used to primarily single out the gaming industry, as well as technology companies and educational institutions in China.

"Over the past few months, it has expanded aggressively, continuously leveraging infected devices to launch external attacks," NSFOCUS [said](https://nsfocusglobal.com/high-risk-warning-for-windows-ecosystem-new-botnet-family-httpbot-is-expanding/) in a report published this week. "By employing highly simulated HTTP Flood attacks and dynamic feature obfuscation techniques, it circumvents traditional rule-based detection mechanisms."

HTTPBot, first spotted in the wild in August 2024, gets its name from the use of HTTP protocols to launch distributed denial-of-service attacks. Written in Golang, it's something of an anomaly given its targeting of Windows systems.

The Windows-based botnet trojan is noteworthy for its use in precisely targeted attacks aimed at high-value business interfaces such as game login and payment systems.

"This attack with 'scalpel-like' precision poses a systemic threat to industries that rely on real-time interaction," the Beijing-headquartered company said. "HTTPBot marks a paradigm shift in DDoS attacks, moving from 'indiscriminate traffic suppression' to 'high-precision business strangulation.'"

HTTPBot is estimated to have issued no less than 200 attack instructions since the start of April 2025, with the attacks designed to strike the gaming industry, technology companies, educational institutions, and tourism portals in China.

[![CIS Build Kits](data:image/png;base64...)](https://thehackernews.uk/platform-shield-d)

Once installed and run, the malware conceals its graphical user interface (GUI) to sidestep process monitoring by both users and security tools in an effort to increase the stealthiness of the attacks. It also resorts to unauthorized Windows Registry manipulation to ensure that it's run automatically on system startup.

The botnet malware then proceeds to establish contact with a command-and-control (C2) server to await further instructions to execute HTTP flood attacks against specific targets by sending a high volume of HTTP requests. It supports various attack modules -

* BrowserAttack, which involves using hidden Google Chrome instances to mimic legitimate traffic while exhausting server resources
* HttpAutoAttack, which makes use of a cookie-based approach to accurately simulate legitimate sessions
* HttpFpDlAttack, which uses the HTTP/2 protocol and opts for an approach that seeks to increase the CPU loader on the server by coercing it into returning large responses
* WebSocketAttack, which uses "ws://" and "wss://" protocols to establish WebSocket connections
* PostAttack, which forces the use of HTTP POST to conduct the attack
* CookieAttack, which adds a cookie processing flow based on the BrowserAttack attack method

"DDoS Botnet families tend to congregate on Linux and IoT platforms," NSFOCUS said. "However, the HTTPBot Botnet family has specifically targeted the Windows platform."

"By deeply simulating protocol layers and mimicking legitimate browser behavior, HTTPBot bypasses defenses that rely on protocol integrity. It also continuously occupies server session resources through randomized URL paths and cookie replenishment mechanisms, rather than relying on sheer traffic volume."

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

[botnet](https://thehackernews.com/search/label/botnet)[china](https://thehackernews.com/search/label/china)[cybersecurity](https://thehackernews.com/search/label/cybersecurity)[ddos attack](https://thehackernews.com/search/label/ddos%20attack)[Gaming](https://thehackernews.com/search/label/Gaming)[Malware](https://thehackernews.com/search/label/Malware)[Threat Intelligence](https://thehackernews.com/search/label/Threat%20Intelligence)[windows security](https://thehackernews.com/search/label/windows%20security)

[![c](data:image/svg+xml;base64...)](https://thehackernews.uk/cloud-defense)

Trending News

[![Stop Alert Chaos: Context Is the Key to Effective Incident Response](data:image/svg+xml;base64... "Stop Alert Chaos: Context Is the Key to Effective Incident Response")

Stop Alert Chaos: Context Is the Key to Effective Incident Response](https://thehackernews.com/2025/09/stop-alert-chaos-context-is-key-to.html)

[![Evolving Enterprise Defense to Secure the Modern AI Supply Chain](data:image/svg+xml;base64... "Evolving Enterprise Defense to Secure the Modern AI Supply Chain")

Evolving Enterprise Defense to Secure the Modern AI Supply Chain](https://thehackernews.com/2025/09/evolvin...