---
title: New React RSC Vulnerabilities Enable DoS and Source Code Exposure
url: https://thehackernews.com/2025/12/new-react-rsc-vulnerabilities-enable.html
source: The Hacker News
date: 2025-12-12
fetch_date: 2025-12-13T03:16:31.842303
---

# New React RSC Vulnerabilities Enable DoS and Source Code Exposure

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

[![Salesforce Security Handbook](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEi4PKjL50qMNKKq6z8Ofu7tXpz51soFtMEKzX6_qMTj-_Exp3EctK0Z7KiOlubgst1DxPrrk8TgthgjViGZmg4FlcOYG8L63G_dX8731tRGkOc42mbtdMv6KDyjdNKRdCPHkhUQJmcoxcFKLcQjeILTu-wEtAOXsTp7JyWMIuP0k1RJo9sZjTo5dYL8CyFQ/s728-e100/z-dd.png)](https://thehackernews.uk/zz--header-d)

# [New React RSC Vulnerabilities Enable DoS and Source Code Exposure](https://thehackernews.com/2025/12/new-react-rsc-vulnerabilities-enable.html)

**Dec 12, 2025**Ravie LakshmananSoftware Security / Vulnerability

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgQz6FV9qkD3ZQ34_-_te7LAvOtZNopi3bQRTQq3TCojcBmPoef7tp-tgxFhffuFYyC5kvbdfEJMIBjwMn-rPElYlnpKG9kj89lPIAde8h_lYZRKq6a4mfiH6VWDXwIqFwimchyQ8M7RUvLd2_cAUi2aqcDyXZI_uDJcjfl1SyScuC96LV9RPhcDan3FJpQ/s790-rw-e365/react-flaws.jpg)

The React team has [released](https://react.dev/blog/2025/12/11/denial-of-service-and-source-code-exposure-in-react-server-components) fixes for two new types of flaws in React Server Components (RSC) that, if successfully exploited, could result in denial-of-service (DoS) or source code exposure.

The team said the issues were found by the security community while attempting to exploit the patches released for CVE-2025-55182 (CVSS score: 10.0), a critical bug in RSC that has since been [weaponized in the wild](https://thehackernews.com/2025/12/react2shell-exploitation-escalates-into.html).

The three vulnerabilities are listed below -

* **[CVE-2025-55184](https://www.cve.org/CVERecord?id=CVE-2025-55184)** (CVSS score: 7.5) - A pre-authentication denial of service vulnerability arising from unsafe deserialization of payloads from HTTP requests to Server Function endpoints, triggering an infinite loop that hangs the server process and may prevent future HTTP requests from being served
* **[CVE-2025-67779](https://www.cve.org/CVERecord?id=CVE-2025-67779)** (CVSS score: 7.5) - An incomplete fix for CVE-2025-55184 that has the same impact
* **[CVE-2025-55183](https://www.cve.org/CVERecord?id=CVE-2025-55183)** (CVSS score: 5.3) - An information leak vulnerability that may cause a specifically crafted HTTP request sent to a vulnerable Server Function to return the source code of any Server Function

However, successful exploitation of CVE-2025-55183 requires the existence of a Server Function that explicitly or implicitly exposes an argument that has been converted into a string format.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/ransomware_dragon_d)

The flaws affecting the following versions of react-server-dom-parcel, react-server-dom-turbopack, and react-server-dom-webpack -

* **CVE-2025-55184 and CVE-2025-55183** - 19.0.0, 19.0.1 19.1.0, 19.1.1, 19.1.2, 19.2.0 and 19.2.1
* **CVE-2025-67779** - 19.0.2, 19.1.3 and 19.2.2

Security researchers RyotaK and Shinsaku Nomura have been credited with reporting the two DoS bugs to the Meta Bug Bounty program, while Andrew MacPherson has been acknowledged for reporting the information leak flaw.

Users are advised to update to **versions 19.0.3, 19.1.4, and 19.2.3** as soon as possible, particularly in light of active exploration of CVE-2025-55182.

"When a critical vulnerability is disclosed, researchers scrutinize adjacent code paths looking for variant exploit techniques to test whether the initial mitigation can be bypassed," the React team said. "This pattern shows up across the industry, not just in JavaScript. Additional disclosures can be frustrating, but they are generally a sign of a healthy response cycle."

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

[cybersecurity](https://thehackernews.com/search/label/cybersecurity)[denial of service](https://thehackernews.com/search/label/denial%20of%20service)[JavaScript](https://thehackernews.com/search/label/JavaScript)[Patch Management](https://thehackernews.com/search/label/Patch%20Management)[React](https://thehackernews.com/search/label/React)[software security](https://thehackernews.com/search/label/software%20security)[Vulnerability](https://thehackernews.com/search/label/Vulnerability)

Trending News

[![ThreatsDay Bulletin: Wi-Fi Hack, npm Worm, DeFi Theft, Phishing Blasts — and 15 More Stories](data:image/svg+xml;base64... "ThreatsDay Bulletin: Wi-Fi Hack, npm Worm, DeFi Theft, Phishing Blasts — and 15 More Stories")

ThreatsDay Bulletin: Wi-Fi Hack, npm Worm, DeFi Theft, Phishing Blasts — and 15 More Stories](https://thehackernews.com/2025/12/threatsday-bulletin-wi-fi-hack-npm-worm.html)

[![⚡ Weekly Recap: Hot CVEs, npm Worm Returns, Firefox RCE, M365 Email Raid and More](data:image/svg+xml;base64... "⚡ Weekly Recap: Hot CVEs, npm Worm Returns, Firefox RCE, M365 Email Raid and More")

⚡ Weekly Recap: Hot CVEs, npm Worm Returns, Firefox RCE, M365 Email Raid and More](https://thehackernews.com/2025/12/weekly-recap-hot-cves-npm-worm-returns.html)

[![Researchers Uncover 30+ Flaws in AI Coding Tools Enabling Data Theft and RCE Attacks](data:image/svg+xml;base64... "Researchers Uncover 30+ Flaws in AI Coding Tools Enabling Data Theft and RCE Attacks")

Researchers Uncover 30+ Flaws in AI Coding Tools Enabling Data Theft and RCE Attacks](https://thehackernews.com/2025/12/researchers-uncover-30-flaws-in-ai.html)

[![Zero-Click Agentic Browser Attack Can Delete Entire Google Drive Using Crafted Emails](data:image/svg+xml;base64... "Zero-Click Agentic Browser Attack Can Delete Entire Google Drive Using Crafted Emails")

Zero-Click Agentic Browser Attack Can Delete Entire Google Drive Using Crafted Emails](https...