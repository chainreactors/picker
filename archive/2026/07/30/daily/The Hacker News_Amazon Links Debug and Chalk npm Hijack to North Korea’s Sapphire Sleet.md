---
title: Amazon Links Debug and Chalk npm Hijack to North Korea’s Sapphire Sleet
url: https://thehackernews.com/2026/07/amazon-links-debug-and-chalk-npm-hijack.html
source: The Hacker News
date: 2026-07-30
fetch_date: 2026-07-31T05:31:18.202840
---

# Amazon Links Debug and Chalk npm Hijack to North Korea’s Sapphire Sleet

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

# [Amazon Links Debug and Chalk npm Hijack to North Korea’s Sapphire Sleet](https://thehackernews.com/2026/07/amazon-links-debug-and-chalk-npm-hijack.html)

**Swati Khandelwal**Jul 30, 2026Software Security / Threat Intelligence

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjgWsCKCTbRf4kZF1zcu1cmfHaf-pPPKTo2q21iPUibGu2jsDaxT92LByZdMAi0d_luVH-yt263qlWE5uDFAh4Ue21dIUk_eu08YXHqwgHI_R9bziAK9nBUiht_lMbaL9bqBH800A0HtxNSYNISi1sZ4SKv1DanwxXBPj4rd6OFBk3ogNn9iTUmsiISve0/s1700-e365/northkorean-npm.jpg)

Amazon has tied the [September 2025 hijack of the npm packages](https://thehackernews.com/2025/09/20-popular-npm-packages-with-2-billion.html) `debug` and `chalk` to North Korea. For ten months, the incident sat in the public record as crypto theft: a maintainer phished through a lookalike npm domain and a wallet-draining script pushed into at least 18 packages carrying more than 2 billion weekly downloads between them.

The original Aikido and Wiz reports did not attribute the incident to North Korea. In research published July 29, Amazon Threat Intelligence assesses with medium confidence that the group behind the March 2026 axios compromise was behind it.

The same group planted a trojanized file in a small package called `typo-crypto` in March 2025, according to Amazon, a full year before it reached axios. Analysts found it while chasing a domain registered in 2025 that surfaced during the axios investigation.

Downloads were low, but the tradecraft "aligns with what we later observed in attacks on more popular packages," Amazon wrote, and the company reads the package as a test run. Amazon's attribution spans four named packages across three campaigns in twelve months. All three, it says, began the same way: socially engineer a trusted maintainer, then publish an update.

Amazon reported no new compromise. The response scope for debug and chalk, browser bundles and caches, still matched the published mechanism. Only the attribution moved.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/ai-vuln-protection-d)

The evidence Amazon published is thinner than the claim. [Its post](https://aws.amazon.com/blogs/security/amazon-identifies-north-korean-hacker-group-behind-open-source-supply-chain-attacks/) cites shared tradecraft across the campaigns, trojanized packages, post-install hooks and code reuse, plus overlapping command-and-control indicators, but does not say which evidence ties which incident.

That gap matters most for debug and chalk, where [Aikido](https://www.aikido.dev/blog/npm-debug-and-chalk-packages-compromised) and [Wiz](https://www.wiz.io/blog/widespread-npm-supply-chain-attack-breaking-down-impact-scope-across-debug-chalk) documented a browser-side interceptor that hooked `fetch`, `XMLHttpRequest` and wallet APIs to rewrite transaction addresses before a user signed. It left no persistence on the machine. Unlike the axios payload, this code did not depend on an npm post-install hook. Neither did typo-crypto, which waited for a trigger instead.

[Google](https://cloud.google.com/blog/topics/threat-intelligence/north-korea-threat-actor-targets-axios-npm-package) independently attributed axios to UNC1069, citing the WAVESHAPER.V2 backdoor and an AstrillVPN node the group had used before. [Microsoft](https://www.microsoft.com/en-us/security/blog/2026/04/01/mitigating-the-axios-npm-supply-chain-compromise/) attributed the same compromise to Sapphire Sleet, which it says overlaps with activity other vendors track as UNC1069, STARDUST CHOLLIMA, BlueNoroff, Alluring Pisces, CageyChameleon, and CryptoCore.

The naming gap is resolved; Amazon's evidence gap is not. Among the sources reviewed here, no other vendor's published research names an actor for the debug, chalk and typo-crypto compromises. The axios attributions landed within two days of the compromise. The other two were attributed ten and sixteen months after the fact.

Amazon reads the pattern as financially motivated. Socket [told The Hacker News](https://thehackernews.com/2025/09/20-popular-npm-packages-with-2-billion.html) at the time that the September wallets had netted about $600.

The malicious file Amazon describes, `core.js`, posed as the legitimate core-js package inside the repository. It triggered on a hash input beginning `0098273` and pulled an operating-system-specific second stage from a hardcoded C2, obfuscated with base64 over an XOR cipher keyed to `01042025`. The network indicators are `npmjs[.]store` and `216[.]74[.]123[.]126`.

Amazon's post cites the OSV record without naming a version. The Hacker News checked it: [`MAL-2026-3400`](https://osv.dev/vulnerability/MAL-2026-3400) identifies `typo-crypto@4.3.0`, credits Amazon Inspector, and was published on May 8, nearly three months before the attribution.

The Hacker News checked the registry on July 30, 2026. `typo-crypto@4.3.0` is still published and still installable. It declares no install script, so pulling it down does not on its own run anything. The tarball npm serves matches the registry's own integrity hashes.

The registry lists one version, created and published 204 milliseconds apart on March 31, 2025. The publishing account does not match the developer named in the package's author field. Its description and keywords are copied from `crypto-js`, at a version one release ahead of crypto-js's own latest, `4.2.0`. crypto-js is a different project from the core-js the file impersonated.

That record does not fit a maintainer compromise followed by a malicious update, which is how Amazon characterizes all three campaigns. It fits a package built to impersonate crypto-js from the first publish. The record cannot show how the account was obtained, only that there was no earlier version to update.

[![Cybersecurity](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhleDdO_4O9-8Pkmidym8Pi9yV4V4jI_M5U0iNRDuoW5Jz3pq7DskZI9OqIChqmY1soaW1ppsC8VLeO55vxSh1m5Q8MJ9ZHuEOSNO5q7K-LwrF6IxrRfCIJOFyo...