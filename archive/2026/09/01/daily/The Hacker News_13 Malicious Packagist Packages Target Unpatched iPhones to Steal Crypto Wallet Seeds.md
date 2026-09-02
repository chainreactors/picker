---
title: 13 Malicious Packagist Packages Target Unpatched iPhones to Steal Crypto Wallet Seeds
url: https://thehackernews.com/2026/09/13-malicious-packagist-packages-target.html
source: The Hacker News
date: 2026-09-01
fetch_date: 2026-09-02T06:41:52.485142
---

# 13 Malicious Packagist Packages Target Unpatched iPhones to Steal Crypto Wallet Seeds

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

# [13 Malicious Packagist Packages Target Unpatched iPhones to Steal Crypto Wallet Seeds](https://thehackernews.com/2026/09/13-malicious-packagist-packages-target.html)

**Ravie Lakshmanan**Sep 01, 2026Malware / Web Security

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhB8expOvrNoEO7Mb5MSWWRnW2eVksJz4NGRldHmcBuWZ76ojuMDD6HJk_i043g-KHOi2zjcYQtsvYGXL2lyzPNy-vwRTD5jzMz5qdEXwfvYqt9K1Uu0Z5fpEMV2EVh9Ap0JRUD391nDM_TjgEXXGnI_dHRpxwv1H5VLiyQN4F3LBpRaEnmtbmCqdllIob2/s1700-nu-rw-lo-l85-e365/iphone.jpg)

Cybersecurity researchers have identified a set of 13 malicious Composer theme packages on Packagist that are designed to inject JavaScript into Vietnamese movie and comic streaming sites that install those libraries and initiate the deployment of spyware aimed at unpatched iOS devices.

"The injected code runs two operations against a site's visitors: a mobile ad-fraud and gambling-redirect chain, and, on iPhones, a WebKit-to-kernel exploit chain that installs spyware," Socket security researcher Kush Pandya [said](https://socket.dev/blog/packagist-themes-ios-spyware).

The activity is assessed to be part of a campaign that was [first documented](https://thehackernews.com/2026/03/threatsday-bulletin-fortigate-raas.html#malicious-themes-inject-ads-and-redirects) by the application security company back in March 2026 that leveraged six malicious Packagist packages posing as OphimCMS themes to redirect visitors, exfiltrate URLs, inject ads, and serve from [Funnull](https://thehackernews.com/2025/05/us-sanctions-funnull-for-200m-romance.html)-hosted infrastructure a second-stage payload to lead victims to gambling and adult content sites.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/trust-world-update-d)

The complete set of packages, which span five vendor namespaces, is below -

* vsmov: theme-dy, theme-rrdyw, theme-motchill, theme-vsmov
* vsphim: theme-heovl, theme-thempho
* haiau009: kkphim-legend, kkphim-motchill
* chilltvcms: theme-legend
* ophimcms: theme-dy, theme-motchill, theme-pcc, theme-rrdyw

At a high level, the trojanized Composer theme injects JavaScript that runs a mobile gambling and ad-fraud redirect and, on iPhones, a Funnull-hosted WebKit-to-kernel exploit chain ending in spyware and cryptocurrency-wallet theft.

The iOS attack chain is designed to insert a hidden iframe element that determines the iOS version and loads an operating system-specific version of the exploit. Specifically, it weaponizes two WebKit vulnerabilities -- CVE-2025-31277 (Patched in version 18.6) and CVE-2025-43529 (Patched in versions 18.7.3 and 26.2) -- in a manner that's analogous to the [DarkSword](https://thehackernews.com/2026/03/darksword-ios-exploit-kit-uses-6-flaws.html) exploit kit.

The payload then pivots out of the WebContent sandbox into the GPU process, followed by a second stage that reaches the kernel through the AppleM2ScalerCSCDriver IOKit user client and ultimately obtains read and write privileges. Apple is said to have addressed the kernel escape flaw in [iOS and macOS 26.1](https://support.apple.com/en-us/125632).

Pandya told The Hacker News that Apple did not share a CVE identifier for the kernel escape vulnerability, but that the iPhone maker confirmed the issue had already been patched in iOS 26.1 and macOS 26.1 before receiving their report. It's suspected to be [CVE-2025-43398](https://nvd.nist.gov/vuln/detail/CVE-2025-43398), [CVE-2025-43510](https://nvd.nist.gov/vuln/detail/CVE-2025-43510), or [CVE-2025-43520](https://nvd.nist.gov/vuln/detail/CVE-2025-43520), all of which were kernel-related bugs fixed late last year.

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEj6M7wdqbGcgHtxk1nrQ-kFxyble4cwPzfMICpii9-frIPpbWSVcRYSFCqqP3pB2QQ-veXaultFDKnePqRKV-XoAPYIXCktsL2tvkUdEX162GcG0KSXWyo5jaVy2oI073Viq9sdqwAdyP-TnnKsRqFN_y8Z6N0uuecr8vM3PKuHupkGgU_HncnHm0pYRao8/s1700-nu-rw-lo-l85-e365/pdf.jpg)

"On success, the final payload uses the kernel read to collect keychain databases, Wi-Fi passwords, the SMS database, the address book, Photos, browser cookies, call history, location history, and account databases, encrypts them with AES, and uploads them over HTTPS POST /upload to a rotating pool of command and control domains," Pandya explained. "The worker beacons exploitation progress to cloudfareintcdn[.]com/wd-status.html."

The threat actors behind the campaign have been found to redeploy the whole iOS chain around August 12, 2026, mainly targeting iOS devices running versions 18.4 through 18.6.x with a new payload that adds an iOS Keychain cryptocurrency wallet seed and mnemonic stealer.

The malware queries the password store for wallet material from Bitget, BitKeep, Bitpie, Phantom, Tonkeeper, Trust Wallet, and OKX, extending beyond device data collection to direct financial theft.

Socket said the same five vendor namespaces have published additional theme packages that carry no active payload at the time of analysis, although they have been configured such that the malicious code could be activated via "Custom JS" fields rendered into every page on the websites.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/ai-security-guide-b)

It's not clear who is behind the campaign, although it's believed to be the work of a Vietnamese-operated group based on commit metadata timestamps. It's worth pointing out that the iOS exploit hosts run on infrastructure provided by [Funnull](https://thehackernews.com/2025/05/us-sanctions-funnull-for-200m-romance.html), an entity sanctioned by the U.S. last May for facilitating romance baiting scams that led to over $200 million in cryptocurrency losses.

"A visitor to a site that installed one of these themes, on an iPhone that has not been updated past iOS 18.6.x (iPhone XS through iPhone 16), can have their keychain, Wi-Fi passwords, SMS, Photos, contacts, cookies, location history, account databases, and crypto...