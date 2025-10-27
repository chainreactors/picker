---
title: Preinstalled Apps on Ulefone, Krüger&Matz Phones Let Any App Reset Device, Steal PIN
url: https://thehackernews.com/2025/06/preinstalled-apps-on-ulefone-kruger.html
source: The Hacker News
date: 2025-06-03
fetch_date: 2025-10-06T23:07:19.721671
---

# Preinstalled Apps on Ulefone, Krüger&Matz Phones Let Any App Reset Device, Steal PIN

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

# [Preinstalled Apps on Ulefone, Krüger&Matz Phones Let Any App Reset Device, Steal PIN](https://thehackernews.com/2025/06/preinstalled-apps-on-ulefone-kruger.html)

**Jun 02, 2025**Ravie LakshmananMobile Security / Vulnerability

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjDxoyU_Qn9QuBXEZLlYQwGcrTOkjaqmR2sQxmYBxQAZaih8X7ItCQhybJcybYGjKTOuJPMapIloK1xjEIRhrqrali3Yf0rmZgpL5CYEU_ci9LfKv3uCF79TYrC5U9X-cMuydU2ScqBjc2ZudJsrNNA7JuceS6qjk0H3s4xf8g4UBxbNau-KT_sAkCvm6hc/s790-rw-e365/android-phone.jpg)

Three security vulnerabilities have been [disclosed](https://cert.pl/en/posts/2025/05/CVE-2024-13915/) in preloaded Android applications on smartphones from Ulefone and Krüger&Matz that could enable any app installed on the device to perform a factory reset and encrypt an application.

A brief description of the three flaws is as follows -

* **[CVE-2024-13915](https://www.cve.org/CVERecord?id=CVE-2024-13915)** (CVSS score: 6.9) - A pre-installed "com.pri.factorytest" application on Ulefone and Krüger&Matz smartphones exposes a "com.pri.factorytest.emmc.FactoryResetService" service that allows any installed application to perform a factory reset of the device.
* **[CVE-2024-13916](https://www.cve.org/CVERecord?id=CVE-2024-13916)** (CVSS score: 6.9) - A pre-installed "com.pri.applock" application on Kruger&Matz smartphones allows a user to encrypt any application using user-provided PIN code or by using biometric data. The app also exposes a "com.android.providers.settings.fingerprint.PriFpShareProvider" content provider's "query()" method that permits any malicious app already installed on the device by some other means to exfiltrate the PIN code.
* **[CVE-2024-13917](https://www.cve.org/CVERecord?id=CVE-2024-13917)** (CVSS score: 8.3) - A pre-installed "com.pri.applock" application on Kruger&Matz smartphones exposed an "com.pri.applock.LockUI" activity that allows any other malicious application, with no granted Android system permissions, to inject an arbitrary [intent](https://developer.android.com/guide/components/intents-filters) with system-level privileges to a protected application.

[![DFIR Retainer Services](data:image/png;base64...)](https://thehackernews.uk/cloud-insight-d)

While exploiting CVE-2024-13917 requires an adversary to know the protecting PIN number, it could be chained with CVE-2024-13916 to leak the PIN code.

CERT Polska, which detailed the vulnerabilities, credited Szymon Chadam for responsibly disclosing them. However, the exact patch status of these flaws remain unclear. The Hacker News has reached out to both Ulefone and Krüger&Matz for additional comment and we will update the story if we hear back.

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

[Android](https://thehackernews.com/search/label/Android)[Application Security](https://thehackernews.com/search/label/Application%20Security)[cybersecurity](https://thehackernews.com/search/label/cybersecurity)[Malware](https://thehackernews.com/search/label/Malware)[mobile security](https://thehackernews.com/search/label/mobile%20security)[Threat Intelligence](https://thehackernews.com/search/label/Threat%20Intelligence)[Vulnerability](https://thehackernews.com/search/label/Vulnerability)

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

⚡ Weekly Recap: Oracle 0-Day, BitLocker Bypass, VMScape, WhatsApp Worm and More](https://thehackernews.com/2025/10/weekly-recap-oracle-0-day-bitlocker.html)

[![Researchers Warn of Self-Spreading WhatsApp Malware Named SORVEPOTEL](data:image/svg+xml;base64... "Researchers Warn of Self-Spreading WhatsApp Malware Named SORVEPOTEL")

Researchers...