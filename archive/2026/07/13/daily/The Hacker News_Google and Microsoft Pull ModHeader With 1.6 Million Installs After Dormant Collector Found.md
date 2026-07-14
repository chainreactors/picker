---
title: Google and Microsoft Pull ModHeader With 1.6 Million Installs After Dormant Collector Found
url: https://thehackernews.com/2026/07/google-and-microsoft-pull-modheader.html
source: The Hacker News
date: 2026-07-13
fetch_date: 2026-07-14T04:48:20.717981
---

# Google and Microsoft Pull ModHeader With 1.6 Million Installs After Dormant Collector Found

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

[![cybersecurity](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgrKWHErc__Wn0forfQ5eJ5sIR1hVKCHCTeNQOaAX4lbygJ8S1Xpemx6JXl78dpwiT65DDBGURp48A3EemKzmli-jXPI3v1928MnJm-1j2ZPUaFXCvuySFhyphenhyphenKR-Li6fAinFT2bhLgsqUSNUR_ggMAnOHi3jD1qYWHXvueX8WdtxAd6GYety9cBGYABo18hX/s728-e100/tt-d.jpg)](https://thehackernews.uk/ai-zero-trust-h-d)

# [Google and Microsoft Pull ModHeader With 1.6 Million Installs After Dormant Collector Found](https://thehackernews.com/2026/07/google-and-microsoft-pull-modheader.html)

**Swati Khandelwal**Jul 13, 2026Browser Security / Web Security

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhSvBtzUXyAbjgtvPJVS9zZ29ULkaIs0fMMa53ZKSip2pJbZ7_HMTGn3SV27X28JLwaq9atS1B_jvH_7qgfsjW0wyVDV_jGyqFSyO-z_vHuoigCy14xfb7DKuuWGIMUVeLiOhnap1yICNPEC2OUkA0d_e8RXtPs7oTo3BAz9I2DTxRwg67vgObResLQ7c4/s1700-e365/browser-edge.jpg)

Google and Microsoft have pulled **ModHeader**, a popular header-editing extension with roughly 1.6 million installs across Chrome and Edge, after researchers found a hidden browsing-history collector built into its official store version.

The collector was dormant. An empty allow-list kept it switched off, and no proof has emerged that it ever gathered or sent a single browsing domain.

The analysis came from [Stripe OLT](https://stripeolt.com/knowledge-hub/threat-research/chrome-extension-hidden-data-exfiltration-900k-users/), a UK security firm, which checked the code against Google's own Web Store signature and confirmed the collector shipped inside the genuine extension, not a counterfeit.

Its review covers the Chrome build and its roughly 900,000 users; third-party trackers put another 700,000 or so on Edge. Microsoft pulled the Edge listing on July 3, and Google removed the Chrome one a week later, on July 10.

Version 7.0.18 (extension ID idgpnmonknjnojddfkpgkljpfnnfcklj) still edits HTTP headers as advertised. The same minified background code also contains a second system. On first run, it builds a device fingerprint and loads a hardcoded encryption key. As you browse, it takes the domain from each page you open, encrypts it, and stores it locally, up to 1000 distinct domains.

Once a day, a scheduler bundles the encrypted list with your fingerprint, posts it to api.stanfordstudies[.]com, and wipes the local copy. The upload time is offset per install, so browsers running it would not all beacon at once if the collector were switched on. Separate teardowns, by [HackIndex](https://hackindex.io/research/modheader-malware-chrome-spyware) on version 7.0.18 and researcher [Yunus Aydin](https://aydinnyunus.github.io/2026/07/12/modheader-data-exfiltration-stanfordstudies/) on 7.0.17, describe the same pipeline.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/ai-vuln-protection-d)

The collector runs only if your browser matches an entry on an internal allow-list, and that list ships empty. The check fails every time, so the pipeline stops before it collects a single domain. Populating that list is a small change, with no new permissions and no click from you, delivered as a routine update. The hardcoded key, the endpoint URL, the scheduler, and the storage logic are already on the machine.

Not everything was asleep. On install, update, and uninstall, the extension pinged a second domain, extensions-hub[.]com, with the product, version, and browser. And a script that runs on every page had already logged real request metadata to local storage in plain text, so that piece had clearly been running.

Automated checkers had rated ModHeader low risk, some as high as 95 out of 100. Each part of the design can frustrate a different kind of check. The data is encrypted, so a scanner sees ciphertext. The upload is gated off, so a sandbox sees nothing leave.

The malicious code is minified into a legitimate codebase. The endpoints had no established malicious reputation to flag. And a signed, popular extension reads as trusted. A store signature proves where a file came from, not what it does.

## Where the domains lead

Stripe OLT tied the domains to real, maintained infrastructure. stanfordstudies[.]com has no link to Stanford; it is a repurposed old domain fronting an OpenSearch back end, while extensions-hub[.]com is set up for advertising.

The two API endpoints resolved to the same Amazon server at the time of analysis, which fits one operator without proving it. A handful of weak signals point loosely toward a Chinese-speaking operator: a Simplified Chinese locale, a "salt" marker written with the character 盐, and a China-origin mail provider. The researchers name no group, and neither do we.

The warning signs came earlier. ModHeader drew complaints for injecting ads into search results in 2023 and reportedly went ad-supported around then. Who took it over is unconfirmed, and the researchers make no claim about the original author.

ModHeader's own site still publishes [an ad plan that says it collects no user data](https://modheader.com/articles/ad-supported-plan), which is hard to square with a built-in browsing-history collector, even a switched-off one. The developer has not responded publicly to the findings as of publication.

The Hacker News has contacted ModHeader for comment and put further questions to Stripe OLT, and will update this story with any response.

[![Cybersecurity](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjHcvlLVmAqlffm6kG54_0cGVf8WfcgzqT9B0fBSizSSeIjh8tBepXnrf6BMqKiG344WgqNejcRtEFKT1PmOzQNQBhdmu2iz9Po10z0SSDlFuZ37iip2uYibJDoxTEkbUI7Bx8NJM2Io_z_nl5p4YA-ZhqFLfi0GW1axyu-lQx-iytCn9RGSJ2iqCwdyv8m/s1600/sy-d-2.jpg)](https://thehackernews.uk/sygnia-cyber-response-d-2)

In 2021, Brian Krebs [described](https://krebsonsecurity.com/2021/03/is-your-browser-extension-a-botnet-backdoor/) how [popular extensions get quietly bought and turned into data pipes](https://thehackernews.com/2026/03/chrome-extension-turns-malicious-after.html). This resembles that pattern, now with encryption and a gate that keeps scanners from seeing the upload. This year alone, a run of Chrome extensions was caught [collecting data under an "anonymous analytics" label](https://thehackernews.com/2026/01/two-chrome-extensions-caught-stealing.html), and a separate set [impersonated Workday and NetSuite](https://thehackernews.com/2...