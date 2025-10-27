---
title: SinoTrack GPS Devices Vulnerable to Remote Vehicle Control via Default Passwords
url: https://thehackernews.com/2025/06/sinotrack-gps-devices-vulnerable-to.html
source: The Hacker News
date: 2025-06-12
fetch_date: 2025-10-06T22:56:25.417461
---

# SinoTrack GPS Devices Vulnerable to Remote Vehicle Control via Default Passwords

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

# [SinoTrack GPS Devices Vulnerable to Remote Vehicle Control via Default Passwords](https://thehackernews.com/2025/06/sinotrack-gps-devices-vulnerable-to.html)

**Jun 11, 2025**Ravie LakshmananIoT Security / Vulnerability

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgJxLk8qZyEML8cI6rxFLnJSFHBJWvTnXfx2_K2XscOelaL9r5L6sKuhw3wUnOYTZ9LLATc3NYUP-Dw0bsZC1BdcIANbHqOr96cxO851THhyVGdOC6Pog8vTplONpP_SdsQ7j_z2Oc2iPOFfvK7aX_jGRekqk5wBdcq0CoQKjG4x4hY5IHY2NKIPZ-wxFQJ/s790-rw-e365/gps.jpg)

Two security vulnerabilities have been disclosed in SinoTrack GPS devices that could be exploited to control certain remote functions on connected vehicles and even track their locations.

"Successful exploitation of these vulnerabilities could allow an attacker to access device profiles without authorization through the common web management interface," the U.S. Cybersecurity and Infrastructure Security Agency (CISA) [said](https://www.cisa.gov/news-events/ics-advisories/icsa-25-160-01) in an advisory.

"Access to the device profile may allow an attacker to perform some remote functions on connected vehicles such as tracking the vehicle location and disconnecting power to the fuel pump where supported."

[![DFIR Retainer Services](data:image/png;base64...)](https://thehackernews.uk/cloud-insight-d)

The vulnerabilities, per the agency, affect all versions of the SinoTrack IoT PC Platform. A brief description of the flaws is below -

* **CVE-2025-5484** (CVSS score: 8.3) - Weak authentication to the central SinoTrack device management interface stems from the use of a default password and a username that's an identifier printed on the receiver.
* **CVE-2025-5485** (CVSS score: 8.6) - The username used to authenticate to the web management interface, i.e., the identifier, is a numerical value of no more than 10 digits.

An attacker could retrieve device identifiers with either physical access or by capturing identifiers from pictures of the devices posted on publicly accessible websites such as eBay. Furthermore, the adversary could enumerate potential targets by incrementing or decrementing from known identifiers or through enumerating random digit sequences.

"Due to its lack of security, this device allows remote execution and control of the vehicles to which it is connected and also steals sensitive information about you and your vehicles," security researcher Raúl Ignacio Cruz Jiménez, who reported the flaws to CISA, told The Hacker News in a statement.

[![CIS Build Kits](data:image/png;base64...)](https://thehackernews.uk/platform-shield-d)

There are currently no fixes that address the vulnerabilities. The Hacker News has reached out to SinoTrack for comment, and we will update the story if we hear back.

In the absence of a patch, users are advised to change the default password as soon as possible and take steps to conceal the identifier. "If the sticker is visible on publicly accessible photographs, consider deleting or replacing the pictures to protect the identifier," CISA said.

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

[CISA](https://thehackernews.com/search/label/CISA)[cybersecurity](https://thehackernews.com/search/label/cybersecurity)[Information theft](https://thehackernews.com/search/label/Information%20theft)[iot security](https://thehackernews.com/search/label/iot%20security)[Patch Management](https://thehackernews.com/search/label/Patch%20Management)[Vulnerability](https://thehackernews.com/search/label/Vulnerability)

[![c](data:image/svg+xml;base64...)](https://thehackernews.uk/cloud-defense)

Trending News

[![Stop Alert Chaos: Context Is the Key to Effective Incident Response](data:image/svg+xml;base64... "Stop Alert Chaos: Context Is the Key to Effective Incident Response")

Stop Alert Chaos: Context Is the Key to Effective Incident Response](https://thehackernews.com/2025/09/stop-alert-chaos-context-is-key-to.html)

[![Evolving Enterprise Defense to Secure the Modern AI Supply Chain](data:image/svg+xml;base64... "Evolving Enterprise Defense to Secure the Modern AI Supply Chain")

Evolving Enterprise Defense to Secure the Modern AI Supply Chain](https://thehackernews.com/2025/09/evolving-enterprise-defense-to-secure.html)

[![First Malicious MCP Server Found Stealing Emails in Rogue Postmark-MCP Package](data:image/svg+xml;base64... "First Malicious MCP Server Found Stealing Emails in Rogue Postmark-MCP Package")

First Malicious MCP Server Found Stealing Emails in Rogue Postmark-MCP Package](https://thehackernews.com/2025/09/first-malicious-mcp-server-found.html)

[![CometJacking: One Click Can Turn Perplexity’s Comet AI Browser Into a Data Thief](data:image/svg+xml;base64... "CometJacking: One Click Can Turn Perplexity’s Comet AI Browser Into a Data Thief")

CometJacking: One Click Can Turn Perplexity's Comet AI Browser Into a Data Thief](https://thehackernews.com/2025/10/cometjacking-one-click-can-turn.html)

[![⚡ Weekly Recap: Oracle 0-Day, BitLocker Bypass, VMScape, WhatsApp Worm and More](data:image/svg+xml;base64... "⚡ Weekly Recap: Oracle 0-Day, BitLocker Bypass, VMScape, WhatsApp Worm and More")

⚡ Weekly Recap: Oracle 0-Day, BitLocker Bypass, VMScape, WhatsApp Worm and ...