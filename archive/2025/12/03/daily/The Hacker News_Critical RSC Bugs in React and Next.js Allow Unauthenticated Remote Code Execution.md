---
title: Critical RSC Bugs in React and Next.js Allow Unauthenticated Remote Code Execution
url: https://thehackernews.com/2025/12/critical-rsc-bugs-in-react-and-nextjs.html
source: The Hacker News
date: 2025-12-03
fetch_date: 2025-12-04T03:19:39.941035
---

# Critical RSC Bugs in React and Next.js Allow Unauthenticated Remote Code Execution

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

# [Critical RSC Bugs in React and Next.js Allow Unauthenticated Remote Code Execution](https://thehackernews.com/2025/12/critical-rsc-bugs-in-react-and-nextjs.html)

**Dec 03, 2025**Ravie LakshmananVulnerability / Cloud Security

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEh9GCiRWt_nzpetB4rbxY-IEBdnQfX50gIjlg82on8OkM-tBrMv_Mt6xTu_yEom3CAZt_KHo0CL5S3siR207cZmw839M_l9Oply6KnuHYelRsMMAqKDhDA0HqnsedjHhsfv6ng77Ah7YPkIZ-Cd3ZuDMqSM8oftGAJ4TaauI9n231fOjCi17uSgWY-Jd9U_/s790-rw-e365/nextjs-react.jpg)

A maximum-severity security flaw has been disclosed in React Server Components (RSC) that, if successfully exploited, could result in remote code execution.

The vulnerability, tracked as CVE-2025-55182, carries a CVSS score of 10.0.

It allows "unauthenticated remote code execution by exploiting a flaw in how React decodes payloads sent to React Server Function endpoints," the React Team [said](https://react.dev/blog/2025/12/03/critical-security-vulnerability-in-react-server-components) in an alert issued today.

"Even if your app does not implement any React Server Function endpoints, it may still be vulnerable if your app supports React Server Components."

According to cloud security firm [Wiz](https://www.wiz.io/blog/critical-vulnerability-in-react-cve-2025-55182), the issue is a case of logical deserialization that stems from processing RSC payloads in an unsafe manner. As a result, an unauthenticated attacker could craft a malicious HTTP request to any Server Function endpoint that, when deserialized by React, achieves execution of arbitrary JavaScript code on the server.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/ai-security-insights-d)

The vulnerability impacts versions 19.0, 19.1.0, 19.1.1, and 19.2.0 of the following npm packages -

* react-server-dom-webpack
* react-server-dom-parcel
* react-server-dom-turbopack

It has been addressed in versions 19.0.1, 19.1.2, and 19.2.1. New Zealand-based security researcher [Lachlan Davidson](https://lachlan.nz/about) has been credited with discovering and reporting the flaw on November 29, 2025.

It's worth noting that the vulnerability also [affects](https://vercel.com/changelog/cve-2025-55182) Next.js using App Router. The issue has been [assigned](https://github.com/vercel/next.js/security/advisories/GHSA-9qr9-h5gf-34mp) the CVE identifier CVE-2025-66478 (CVSS score: 10.0). It impacts versions >=14.3.0-canary.77, >=15, and >=16. Patched versions are 16.0.7, 15.5.7, 15.4.8, 15.3.6, 15.2.6, 15.1.9, and 15.0.5.

That said, any library that bundles RSC is likely to be affected by the flaw. This includes, but is not limited to, Vite RSC plugin, Parcel RSC plugin, React Router RSC preview, RedwoodJS, and Waku.

Wiz said 39% of cloud environments have instances vulnerable to CVE-2025-55182 and/or CVE-2025-66478. In light of the severity of the vulnerability, it's advised that users apply the fixes as soon as possible for optimal protection.

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

[Cloud security](https://thehackernews.com/search/label/Cloud%20security)[cybersecurity](https://thehackernews.com/search/label/cybersecurity)[Deserialization](https://thehackernews.com/search/label/Deserialization)[JavaScript](https://thehackernews.com/search/label/JavaScript)[Next.js](https://thehackernews.com/search/label/Next.js)[Open Source](https://thehackernews.com/search/label/Open%20Source)[React](https://thehackernews.com/search/label/React)[remote code execution](https://thehackernews.com/search/label/remote%20code%20execution)[Vulnerability](https://thehackernews.com/search/label/Vulnerability)

[![c](data:image/svg+xml;base64...)](https://thehackernews.uk/sentinelone-protect)

Trending News

[![⚡ Weekly Recap: Hot CVEs, npm Worm Returns, Firefox RCE, M365 Email Raid and More](data:image/svg+xml;base64... "⚡ Weekly Recap: Hot CVEs, npm Worm Returns, Firefox RCE, M365 Email Raid and More")

⚡ Weekly Recap: Hot CVEs, npm Worm Returns, Firefox RCE, M365 Email Raid and More](https://thehackernews.com/2025/12/weekly-recap-hot-cves-npm-worm-returns.html)

[![ShadowPad Malware Actively Exploits WSUS Vulnerability for Full System Access](data:image/svg+xml;base64... "ShadowPad Malware Actively Exploits WSUS Vulnerability for Full System Access")

ShadowPad Malware Actively Exploits WSUS Vulnerability for Full System Access](https://thehackernews.com/2025/11/shadowpad-malware-actively-exploits.html)

[![China-Linked APT31 Launches Stealthy Cyberattacks on Russian IT Using Cloud Services](data:image/svg+xml;base64... "China-Linked APT31 Launches Stealthy Cyberattacks on Russian IT Using Cloud Services")

China-Linked APT31 Launches Stealthy Cyberattacks on Russian IT Using Cloud Services](https://thehackernews.com/2025/11/china-linked-apt31-launches-stealthy.html)

[![Second Sha1-Hulud Wave Affects 25,000+ Repositories via npm Preinstall Credential Theft](data:image/svg+xml;base64... "Second Sha1-Hulud Wave Affects 25,000+ Repositories via npm Preinstall Credential Theft")

Second Sha1-Hulud Wave Affects 25,000+ Repositories via npm Preinstall Credential Theft](https://thehackernews.com/2025/11/second-sha1-hulud-wave-affects-25000.html)

[![CISA Warns of Act...