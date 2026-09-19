---
title: An Abandoned CDN Domain Was Re-Registered. Thousands of Sites Still Call It.
url: https://thehackernews.com/2026/09/an-abandoned-cdn-domain-was-re.html
source: The Hacker News
date: 2026-09-18
fetch_date: 2026-09-19T07:02:43.573744
---

# An Abandoned CDN Domain Was Re-Registered. Thousands of Sites Still Call It.

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

[![cybersecurity](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiHP9KRFkaxKFUKQNRU3CkfxCyJLEuIfmo6ov7iWHHRBE1ShJKfXdPvozMZMVuvOJipQ8Qbap3UBmtjKvZh-xBqLeUartPWmRuQj2W8nqdCk2_XlYLXpj15R4Du2oJ1nNVPqIuR-TwbMyPQe4gxxCcMYvUMbFO_Nin2OdhyzkJvX8Sn83aEbM1C5sgaaCqI/s728-nu-rw-lo-l85-e365/wiz-sep-d.png)](https://thehackernews.uk/claude-security-guide-d)

# [An Abandoned CDN Domain Was Re-Registered. Thousands of Sites Still Call It.](https://thehackernews.com/2026/09/an-abandoned-cdn-domain-was-re.html)

**The Hacker News**Sep 18, 2026Web Security / Compliance

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEh4A312zOZ7ftKXmWapCccs7ZW6g3d61vCPFzToGj6Y9nRb2cXUHcQ9__5Taotig6y1W_tljoo5ih74cJCTxZzfz5Ii0MMoLcBuUZS6fQCgn_L4zmq92Zamf2FJM-oT3ptyyzPM-2c1oyZSZSn3eYiUp0QidqC2N2tYT9GFrqAYitjrco1cmrDJRCm6HEk/s1700-nu-rw-lo-l85-e365/report-uri.jpg)

In July 2025, someone registered a domain that used to belong to a content delivery network. The CDN had been wound down years earlier, and the domain it served assets from was allowed to expire. What it had not lost were its callers. Thousands of websites, code repositories, and documentation pages still carry hard-coded references to hostnames beneath it.

The new owner holds wildcard DNS across the entire domain, and any hostname under it now resolves to infrastructure that person controls. Today the apex serves an ad-heavy media downloader page, which is unremarkable. The remarkable part is that the decision about what those thousands of pages load next belongs to a stranger, and nobody involved has been notified, because from the outside nothing broke.

This pattern is not hypothetical, and it's not unheard of either. In June 2024, the polyfill.io domain (a JavaScript shim embedded in more than 110,000 sites) changed ownership and began serving conditional redirects to mobile visitors. The sites running it had not been hacked, they had simply outsourced a <script> tag years earlier and never revisited the decision.

Both of these cases share a problem that most security teams have no control for: the malicious code was never on their server, and it arrived long after the last deployment happened.

## **Server-side tooling is looking in the wrong place**

Static analysis, dependency scanning and software composition analysis all examine what an organisation builds and ships, but a third-party script is none of those things. It is fetched by the visitor's browser, from a server the organisation does not run and has no control over, live on every page view.

That makes it uniquely hostile to conventional testing because the response can vary by geography, user agent, referrer, time of day and session. A crawler pulling the file once from a data-centre IP range gets shown a clean version; the shopper on a mobile network in another country gets something more sinister.

Meanwhile, the third-party script itself holds the same privileges as your first-party code. It can read the DOM, read form fields character by character as they are typed, read cookies and local storage, and make outbound requests to anywhere it likes. [Client-side attacks](https://report-uri.com/client-side-security?utm_source=thn&utm_medium=article&utm_campaign=abandoned-cdn) of the Magecart type do not require a server breach at all, they require one approved script tag to start behaving differently.

## **The browser sees everything**

There is one observer that's reliably present for every one of those page views: the browser that executed the code. Content Security Policy is usually discussed as a defense against cross-site scripting, and it is a good one, but its second function is more useful to a security team that does not yet know what code it is running. A CSP can control what code is allowed to run on your website, block code that is not authorised to run, and let you know when that happens.

Those alerts are coming from real sessions, in real geographies, from your real users on their real devices. A malicious payload that only fires for logged-in users in one country still gets reported, because the browser that ran it is the thing sending the alert.

This is not a theoretical benefit. In September 2026, these alerts collected by Report URI surfaced a cluster of compromised e-commerce sites running a social-engineering campaign of the "ClickFix" family. Base64-encoded loaders had been planted inside CMS content after an administrative compromise, chaining through a redirector to a fake "verify you are human" overlay that placed a PowerShell command on the victim's clipboard and persisted it as a scheduled task. The attacker-controlled hostnames turned up in alerts from victims' browsers while several of those domains were still rated clean by mainstream reputation services. No scanner had flagged the pages, because on the server they were fine.

## **You can start with CSP without blocking anything**

The common objection is that a Content Security Policy will break the site, but in report-only mode it cannot. Content-Security-Policy-Report-Only enforces nothing, blocks nothing and changes no behaviour, it only reports what a policy *would* have blocked.

That turns the first deployment into a safe measurement exercise and allows you to gather all of the data needed about what code is running on your site. For most organisations, that list is a lot longer than they expected.

## **Compliance turned this into an obligation**

For anyone handling card payments on their site, this argument is already settled. PCI DSS v4.0.1 requirements 6.4.3 and 11.6.1 stopped being best practice and became mandatory on 31 March 2025. Together, they require that every script on a payment page is authorised, that its integrity is assured, that a written inventory with business justification exists, and that a mechanism detects and alerts on unauthorised modification of payment page content and HTTP headers.

A QSA can and will ask for the inventory, the alerting mechanism and the evidence trail it produced. Report URI can give you all three.

## **What a working deployment looks like**

1. Deploy and gather initial data for a week.
2. Build your inventory from what was reported.
3. Monitor changes over time and approve or deny those changes.

A [ten-year daily crawl of the top one million sites](ht...