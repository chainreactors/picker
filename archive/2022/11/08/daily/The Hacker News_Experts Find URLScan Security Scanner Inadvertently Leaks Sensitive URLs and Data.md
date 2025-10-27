---
title: Experts Find URLScan Security Scanner Inadvertently Leaks Sensitive URLs and Data
url: https://thehackernews.com/2022/11/experts-find-urlscan-security-scanner.html
source: The Hacker News
date: 2022-11-08
fetch_date: 2025-10-03T21:59:36.030806
---

# Experts Find URLScan Security Scanner Inadvertently Leaks Sensitive URLs and Data

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

# [Experts Find URLScan Security Scanner Inadvertently Leaks Sensitive URLs and Data](https://thehackernews.com/2022/11/experts-find-urlscan-security-scanner.html)

**Nov 07, 2022**Ravie Lakshmanan

[![Urlscan Security Scanner](data:image/png;base64... "Urlscan Security Scanner")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEg9s-ZHpRpOCHmCgxgsV4a_OIceRuWMouVUyqvXsFxficMqpmhOzcTdGxmpiKM_pWfR0p7MAcannyq1D2G15d073NrPVI0axhYIfbtHs7iDcZbkMDs_wkhhI6qO-dAOle4Kn2q90iWWM2J_x_KHv2jxE2FPcmzwVaI7PYPYSeEZLuwS63NS7IYVRFzG/s790-rw-e365/urlscan.jpg)

Security researchers are warning of "a trove of sensitive information" leaking through urlscan.io, a website scanner for suspicious and malicious URLs.

"Sensitive URLs to shared documents, password reset pages, team invites, payment invoices and more are publicly listed and searchable," Positive Security co-founder, Fabian Bräunlein, [said](https://positive.security/blog/urlscan-data-leaks) in a report published on November 2, 2022.

The Berlin-based cybersecurity firm said it started an investigation in the aftermath of a [notification](https://news.ycombinator.com/item?id=30348980) sent by GitHub in February 2022 to an unknown number of users about sharing their usernames and private repository names (i.e., [GitHub Pages URLs](https://docs.github.com/en/pages/getting-started-with-github-pages/about-github-pages)) to urlscan.io for metadata analysis as part of an automated process.

[![DFIR Retainer Services](data:image/png;base64...)](https://thehackernews.uk/cloud-insight-d)

Urlscan.io, which has been described as a [sandbox for the web](https://urlscan.io/about/), is [integrated](https://urlscan.io/docs/integrations/) into several security solutions [via its API](https://urlscan.io/docs/api/).

"With the type of integration of this API (for example via a security tool that scans every incoming email and performs a urlscan on all links), and the amount of data in the database, there is a wide variety of sensitive data that can be searched for and retrieved by an anonymous user," Bräunlein noted.

This included password reset links, email unsubscribe links, account creation URLs, API keys, information about Telegram bots, DocuSign signing requests, shared Google Drive links, Dropbox file transfers, invite links to services like SharePoint, Discord, and Zoom, PayPal invoices, Cisco Webex meeting recordings, and even URLs for package tracking.

[![Urlscan Security Scanner](data:image/png;base64... "Urlscan Security Scanner")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiwrUeLLS3BovnLelCQYpFVUGhbLK-Dm2aSZHxo6xe6lWKzdGLcR1Q9Ngj8Nswmd-uXkNeIlCq2BNRvNQopZ4EJGbGf1m8JRvYyZsuDgrM5_-GxZKnY0fiaY9aq_-pvE8WMUWxKrAEXjagszhr26m1gPTWp_9mTu7wMT41xP9W-ciVT1kdbHGM-aVmi/s790-rw-e365/url.jpg)

Bräunlein pointed out that an initial search in February revealed "juicy URLs" belonging to Apple domains, some of which also consisted of publicly-shared links to iCloud files and calendar invite responses. They have since been removed.

Apple is said to have requested an exclusion of its domains from the URL scans such that results matching certain predefined rules are periodically deleted.

Positive Security further added that it reached out to a number of those leaked email addresses, receiving one response from an unnamed organization that traced the leak of a DocuSign work contract link to a misconfiguration of its Security Orchestration, Automation, and Response ([SOAR](https://www.gartner.com/en/information-technology/glossary/security-orchestration-automation-response-soar)) solution, which was being integrated with urlscan.io.

On top of that, the analysis has also found that misconfigured security tools are submitting any link received via mail as a public scan to urlscan.io.

[![CIS Build Kits](data:image/png;base64...)](https://thehackernews.uk/platform-shield-d)

This could have serious consequences wherein a malicious actor can trigger password reset links for the affected email addresses and exploit the scan results to capture the URLs and take over the accounts by resetting to a password of the attacker's choice.

To maximize the effectiveness of such an attack, the adversary can search data breach notification sites like [Have I Been Pwned](https://haveibeenpwned.com/About) to determine the exact services that were registered using the email addresses in question.

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhXJ6zFHy-W_upFwPjkZkiJgLMvNRGijFJf7X7kg57G5jmjeM4GX2UDai9CUtDFbvM3_878cKYHWP_CotwWQzLUgFT-zFTvA51PKQQTw7qhO7FsLKQozTw1ghQBLiEHkLOe_hre1y6btcelCIhMYCe1ivY2YE1QjG-qQ2nehbxO3qZ56Ja-vW4-M-qgGQ/s790-rw-e365/linkscan.jpg)

Urlscan.io, following responsible disclosure from Positive Security in July 2022, has [urged](https://urlscan.io/blog/2022/07/27/scan-visibility-best-practices/) users to "understand the different scan visibilities, review your own scans for non-public information, review your automated submission workflows, [and] enforce a maximum scan visibility for your account."

It has also added deletion rules to regularly purge delete past and future scans matching the search patterns, stating it has domain and URL pattern blocklists in place to prevent scanning of particular websites.

"This information could be used by spammers to collect email addresses and other personal information," Bräunlein said. "It could be used by cyber criminals to take over accounts and run believable phishing campaigns."

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
[**Share on Twitter](#...