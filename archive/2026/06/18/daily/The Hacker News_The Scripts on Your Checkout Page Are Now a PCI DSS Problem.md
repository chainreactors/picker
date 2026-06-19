---
title: The Scripts on Your Checkout Page Are Now a PCI DSS Problem
url: https://thehackernews.com/2026/06/the-scripts-on-your-checkout-page-are.html
source: The Hacker News
date: 2026-06-18
fetch_date: 2026-06-19T07:09:17.521309
---

# The Scripts on Your Checkout Page Are Now a PCI DSS Problem

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

[![cybersecurity](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjQl2axNwsfhbXOFynrg_uAZsvHi3OvNGSA8KJO-BKR8Xm3x7yjKV3EvfY4v5mwXx6LF0uWFb9h9d9iAV_Pi-YYhqimX9wx4OaLdDJEdR215Xrxq_PAtXkaLfQso4pTSjbj6fvh_ZTliLpzWZSZfcoZgyXtKwhN-SSDDlmbtUqGLshc0KqYQGWYHMN52Sl1/s728-e100/zz-d.jpg)](https://thehackernews.uk/ai-vuln-protection-d)

# [The Scripts on Your Checkout Page Are Now a PCI DSS Problem](https://thehackernews.com/2026/06/the-scripts-on-your-checkout-page-are.html)

**The Hacker News**Jun 18, 2026Payment Security / Compliance

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjHJHzi-rQqSIiD4wXw_HQpgvXGNTNgvJnxt42OupMrchYSmQPyeXbtsuH62zLqPHDq3bywvirdcqKSq9VQ-pZyL02RAw2IYYh1f4qcpUH4NZu50XLSDsQSSYvyqMAEwSN-8PQMcpwXZMtLC_pVYzqZMYm7qkygfMQeZEIHVWpIkYfUifJvX3oUMSBs3w0/s1700-e365/reflectiz.jpg)

An independent PCI assessor tested Reflectiz against the new PCI DSS rules. Here is the verdict: **[See the full QSA assessment here →](https://www.reflectiz.com/learning-hub/pci-dss-solution-assessment-integrity360/)**

When a customer types their card number into your checkout, their browser is running far more than your code. Analytics tags, a tag manager, a support widget, a payment iframe: a modern checkout loads dozens of third-party scripts, and any one of them can be turned into a skimmer.

This is how Magecart works. [Sansec has counted more than 100,000 sites](https://sansec.io/what-is-magecart) hit by web skimming and supply-chain attacks. The [2018 British Airways breach](https://techcrunch.com/2020/10/16/uks-ico-downgrades-british-airways-data-breach-fine-to-20m-after-originally-setting-it-at-184m/) alone exposed 380,000 transactions and a fine that started at £183 million.

The dangerous part: the malicious code usually arrives through a script you already approved. Attackers compromise a third-party vendor, and the payload rides in on a script you have run for months. Nothing looks new. What changed is the script's behavior, not its presence on the page.

PCI DSS v4.0.1 closes that gap with two requirements, now fully in force. **6.4.3** says to inventory every payment-page script, authorize it, and prove its integrity. **11.6.1** says to detect tampering with page content and HTTP headers as the browser receives them. Done by hand, across hundreds of scripts that change constantly, this does not scale. Reflectiz data shows roughly 30% of payment-page scripts change within any two-week window.

## **What the QSA Found**

Integrity360 Europe, a PCI Qualified Security Assessor and member of the PCI SSC Global Executive Assessor Roundtable, reviewed the Reflectiz PCI DSS Platform against both requirements and found it can effectively support compliance. Three things stood out:

* **It watches behavior, not just file hashes.** A hash check misses a silent vendor-side swap. Reflectiz catches the script the moment it starts reaching for card data.
* **It deploys agentless.** No code changes, no snippets, live in days, and it keeps working through refactors and CMS migrations.
* **It produces QSA-ready evidence in one click.** Full audit trail per page, ready for assessment.

## **The SAQ A Catch**

Since January 2025, merchants can drop 6.4.3 and 11.6.1 from SAQ A only if they confirm their site is not susceptible to script attacks. Full redirect to your processor? You are likely fine. Embed a payment iframe? A script on the parent page can still hijack the checkout before data reaches the secure frame, and you have to prove it cannot. PCI SSC FAQ #1588 points straight back to these same controls.

## **Get the Full Assessment**

The complete Integrity360 Europe white paper breaks down both requirements line by line, the monitoring workflow, and exactly what SAQ A now demands of iframe merchants.

**[Download the white paper →](https://www.reflectiz.com/learning-hub/pci-dss-solution-assessment-integrity360/)**

Found this article interesting? This article is a contributed piece from one of our valued partners. Follow us on [Google News](https://news.google.com/publications/CAAqLQgKIidDQklTRndnTWFoTUtFWFJvWldoaFkydGxjbTVsZDNNdVkyOXRLQUFQAQ), [Twitter](https://twitter.com/thehackersnews) and [LinkedIn](https://www.linkedin.com/company/thehackernews/) to read more exclusive content we post.

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

[browser security](https://thehackernews.com/search/label/browser%20security), [Compliance](https://thehackernews.com/search/label/Compliance), [Magecart](https://thehackernews.com/search/label/Magecart), [Payment Security](https://thehackernews.com/search/label/Payment%20Security), [PCI DSS](https://thehackernews.com/search/label/PCI%20DSS), [Reflectiz](https://thehackernews.com/search/label/Reflectiz), [Supply Chain Security](https://thehackernews.com/search/label/Supply%20Chain%20Security), [Web Skimming](https://thehackernews.com/search/label/Web%20Skimming)

⚡ Top Stories This Week

[![Chrome V8 Zero-Day CVE-2026-11645 Exploited in the Wild - Patch Now](data:image/svg+xml;base64... "Chrome V8 Zero-Day CVE-2026-11645 Exploited in the Wild - Patch Now")

Chrome V8 Zero-Day CVE-2026-11645 Exploited in the Wild - Patch Now](https://thehackernews.com/2026/06/chrome-v8-zero-day-cve-2026-11645.html)

[![Researchers Build Self-Replicating AI Worm That Operates Entirely on Local, Open-Weight Models](data:image/svg+xml;base64... "Researchers Build Self-Replicating AI Worm That Operates Entirely on Local, Open-Weight Models")

Researchers Build Self-Replicating AI Worm That Operates Entirely on Local, Open-Weight Models](https://thehackernews.com/2026/06/researchers-build-self-replicating-ai.html)

[![Microsoft Defender RoguePlanet Zero-Day Grants SYSTEM Access on Updated Windows](data:image/svg+xml;base64... "Microsoft Defender RoguePlanet Zero-Day Grants SYSTEM Access on Update...