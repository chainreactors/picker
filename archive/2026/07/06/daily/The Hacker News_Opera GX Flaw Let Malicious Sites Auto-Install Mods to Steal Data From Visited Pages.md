---
title: Opera GX Flaw Let Malicious Sites Auto-Install Mods to Steal Data From Visited Pages
url: https://thehackernews.com/2026/07/opera-gx-flaw-let-malicious-sites-auto.html
source: The Hacker News
date: 2026-07-06
fetch_date: 2026-07-07T06:05:06.018468
---

# Opera GX Flaw Let Malicious Sites Auto-Install Mods to Steal Data From Visited Pages

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

# [Opera GX Flaw Let Malicious Sites Auto-Install Mods to Steal Data From Visited Pages](https://thehackernews.com/2026/07/opera-gx-flaw-let-malicious-sites-auto.html)

**Swati Khandelwal**Jul 06, 2026Vulnerability / Web Security

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjZ_WItJUaS3rk5pAYa5yOsKuUt0Yovlv1T-jIz2GBBhcmMjToCgnWuEApyWfgDwngwAPcEGke0zwo_2DKKHaN9vzzHMAnd7Z3esepEvjSM022BzOdjo0sJW2bSMlslKXVv5Fg701ozva1HDgZPJV4Qya8Xevye-eT4dB0UmIJK9CKq-_wLnEGgNYigRLzh/s1700-e365/opera-data-leak.jpg)

Researchers found a flaw in [Opera GX](https://www.opera.com/gx), the gaming-focused version of the Opera browser, that let a malicious website silently install a browser add-on and use it to lift specific data from the pages a victim visits.

In a proof of concept, they reconstructed a signed-in user's full Gmail address from a single visit, with no click. Opera has patched the flaw and says it found no evidence that it was ever used in the wild.

The fix shipped in Opera GX version 130.0.5847.89, so anyone on a current build is already covered; you can confirm yours at opera://about. There is no CVE.

Because the attack needed no clicks or approvals, there was no workaround short of the patch. Opera's bug bounty team rated the issue P1, its top severity, and paid the maximum $5,000 award for a critical bug.

## How the attack works

GX Mods let you reskin Opera GX with custom sounds, themes, wallpapers, and CSS that restyles the sites you visit. They ship as .crx files, like browser extensions, but they cannot run JavaScript and hold no permissions.

The weakness is in how they install: Opera's mod pipeline downloads and enables a mod automatically, with no approval prompt. So a malicious page can install one silently, for instance by loading a hidden iframe pointed at a .crx file.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/ai-vuln-protection-d)

The only sign is a notification bar below the address bar telling you a mod was added, with a Remove button.

This auto-install behavior is not new. The researcher [Renwa identified it back in 2023](https://medium.com/%40renwa/you-are-not-where-you-think-you-are-opera-browsers-address-bar-spoofing-vulnerabilities-aa36ad8321d8) and, by escalating an installed mod into a full extension, used it to spoof the browser's address bar. Opera patched that specific attack in March 2023 but left the underlying auto-install in place, which is what this new research builds on.

A silent look-and-feel mod sounds harmless on its own. But a mod's CSS is applied to every page you visit, not just one. Ordinary CSS injection is confined to the page it lands on; here, the attacker's styling reaches every site the browser opens, a technique the researchers call a universal CSS injection.

CSS cannot read a page and send it off on its own. But it can be coaxed into leaking a value one piece at a time. The trick relies on attribute selectors: a rule can test whether an element's attribute value, like an email tucked into a hidden field, begins with a given letter, and fetch a background image from the attacker's server only when it does. Fire enough of these, and you learn the value character by character.

[Researchers call](https://zhero-web-sec.github.io/research-and-things/one-trigram-at-a-time-xsleak-via-universal-css-injection-and-dos-in-opera-%28gx%29) this an **XS-Leak**, short for cross-site leak. To pull a Gmail address, the researchers aimed this at a Google account page, myaccount.google.com/contactemail, that carries the address inside three of its HTML attributes.

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiIpKIuzDz34xVqd5DNkthsAXPJZrooWynLxy2jLp5FHBP6tuVdJ4Z7hOUXn9hy-XO7_w4sTSQVyeCmFXMIgpS4tXAcn_3wOjzbg78leNIfB75EcZEEbq3XCJ0mByr594E-Dpr4vz7MCsOy2AmYJLDiO2ULxS85Ke8x3ZBW5ZnfiHFqDuWg3d9ppXM7qO_6/s1700-e365/opera-leaks.gif)

They packed a mod with roughly 150,000 CSS rules, one set for every possible three-letter piece of the address, and let a reconstruction script stitch the matches back together. They first tried four-letter pieces, which needed 5.6 million rules and about 880 MB of CSS. The browser choked, so they scaled down to three-letter chunks that overlap just enough to reassemble.

Chaining it together took only a nudge. The victim lands on the attacker's page, the mod installs within seconds, and a few lines of JavaScript then redirect the browser to the Google account page. The mod's CSS is already loaded there, so it fires the requests and leaks the address as the page renders, before the victim can reach the notice's Remove button.

The Gmail address was just the proof of concept; the same approach can lift other values a page exposes in its markup, like a username.

The same auto-install path has a second, cruder use the researchers documented: loading a .crx while in private (Incognito) mode crashes the browser and dumps every open tab. This one hits regular Opera too, not just Opera GX, since any .crx trips the extension-install pipeline, whatever it contains. Opera's advisory addresses the data-theft fix and does not mention the crash.

## Severity and the bigger picture

The report almost did not get its due. Opera runs its bounty program on Bugcrowd, and the triage analysts struggled to grasp what the bug did, first rating it a middling P3.

The researchers made their case in an unusually direct way: while an analyst was reproducing the attack, they caught the analyst's own trigrams, rebuilt the analyst's Gmail address, and pasted it into the report. Opera's team then raised the severity to P1 and paid the $5,000 critical-tier maximum.

[![Cybersecurity](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhr7HGzx4ULDSqwnN820pPGxlPxqqVxKgIrI5II1iWdspOL6yHZsdB5lWoXU3LmhIU4dtnph89fLZ0CxrQSs-ufs6Mo4eD-d-Cpx-DsV1G15eC-phLACF7hyaKSIH1zIdj3AuD7lHSHnVelmKVMoVV-_zvtJuodsSIDKu6uSRfU6fZBkO-2PERqKSfIn6dA/s728-e100/sygnia-d-2.jpg)](https:...