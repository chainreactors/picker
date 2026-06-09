---
title: VS Code Adds 2-Hour Extension Auto-Update Delay to Limit Supply Chain Attacks
url: https://thehackernews.com/2026/06/vs-code-adds-2-hour-extension-auto.html
source: The Hacker News
date: 2026-06-08
fetch_date: 2026-06-09T06:03:51.486617
---

# VS Code Adds 2-Hour Extension Auto-Update Delay to Limit Supply Chain Attacks

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

# [VS Code Adds 2-Hour Extension Auto-Update Delay to Limit Supply Chain Attacks](https://thehackernews.com/2026/06/vs-code-adds-2-hour-extension-auto.html)

**Ravie Lakshmanan**Jun 08, 2026Software Supply Chain / Malware

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjPMxcu3ZcBpbZRC5rw9BlnoZMoXgrA-dRRquG6F6PSZZUc0JNzGHbl6c50yqTxs60QyQ5ut5ZC2qP9Csk_mR1Aqi48DO0wwDbUZ6zei45FNO2UgXaU0pOf8gWk8iAT81Ee1XJGrYyFgjYJqCeGTlnYeq-U8Nh4i5cxskA5n3eWyaQqMQPmyMAAR30bDKf2/s1700-e365/ms-delay.jpg)

Microsoft has announced that Visual Studio Code (VS Code) will apply a two-hour delay before extensions for the integrated development environment (IDE) are updated automatically to a newer version in an attempt to tackle software supply chain threats.

"When automatic updates are enabled, new versions are auto-updated two hours after they are published, adding an extra layer of protection against problematic or potentially compromised releases," Microsoft [said](https://code.visualstudio.com/updates/v1_123#_delayed-extension-autoupdates).

The new feature is available starting in VS Code 1.123.

The tech giant noted that users still have the option to update any extension immediately at any point in time by using the "Update" button. When extensions have pending updates, a reason for why they haven't been updated yet will be available in the details view, along with when the automatic update will take place.

That said, this two-hour delay does not apply to extensions from trusted publishers such as Microsoft, GitHub, and OpenAI, it added. Extensions from such publishers will continue to be updated immediately.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/vpn-threat-report-m)

The development comes days after RubyGems [added](https://thehackernews.com/2026/06/threatsday-bulletin-ai-agents-gone.html#supply-chain-delay-defense) an opt-in cooldown feature to Bundler 4.0.13 that delays installation of newly published gem versions for a pre-defined period.

Specifically, the feature allows developers to configure Bundler to introduce a time-based install delay with an aim to reduce potential exposure arising from newly published malicious versions.

Over the past year, similar installation controls have also been added to Bun, pnpm, npm, and Yarn -

* [Bun](https://bun.com/blog/bun-v1.3) - minimumReleaseAge (Bun 1.3+)
* [npm](https://docs.npmjs.com/cli/v11/using-npm/config#min-release-age) - min-release-age (npm v11.10.0+)
* [pnpm](https://pnpm.io/blog/releases/10.16) - minimumReleaseAge (pnpm 10.16+)
* [Yarn](https://github.com/yarnpkg/berry/releases/tag/%40yarnpkg/cli/4.10.0) - npmMinimalAgeGate (Yarn Berry 4.10.0+)

These changes arrive against the backdrop of a surge in software supply chain incidents targeting various ecosystems to breach developer systems and propagate malware to downstream users.

By enforcing a minimum age threshold before a particular package version can be installed, the defensive control minimizes the window during which it spreads before it's flagged as malicious and taken down by the registry maintainers.

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

[Bundler](https://thehackernews.com/search/label/Bundler), [Microsoft](https://thehackernews.com/search/label/Microsoft), [NPM](https://thehackernews.com/search/label/NPM), [Package Management](https://thehackernews.com/search/label/Package%20Management), [pnpm](https://thehackernews.com/search/label/pnpm), [RubyGems](https://thehackernews.com/search/label/RubyGems), [Software Supply Chain](https://thehackernews.com/search/label/Software%20Supply%20Chain), [Visual Studio Code](https://thehackernews.com/search/label/Visual%20Studio%20Code), [Yarn](https://thehackernews.com/search/label/Yarn)

⚡ Top Stories This Week

[![Google June 2026 Android Update Patches 124 Flaws, One Actively Exploited](data:image/svg+xml;base64... "Google June 2026 Android Update Patches 124 Flaws, One Actively Exploited")

Google June 2026 Android Update Patches 124 Flaws, One Actively Exploited](https://thehackernews.com/2026/06/google-june-2026-android-update-patches.html)

[![Oracle WebLogic CVE-2024-21182 Added to KEV Catalog After Active Exploitation](data:image/svg+xml;base64... "Oracle WebLogic CVE-2024-21182 Added to KEV Catalog After Active Exploitation")

Oracle WebLogic CVE-2024-21182 Added to KEV Catalog After Active Exploitation](https://thehackernews.com/2026/06/oracle-weblogic-cve-2024-21182-added-to.html)

[![Dashlane Discloses Brute-Force Attack, Encrypted Vaults of Fewer Than 20 Users Downloaded](data:image/svg+xml;base64... "Dashlane Discloses Brute-Force Attack, Encrypted Vaults of Fewer Than 20 Users Downloaded")

Dashlane Discloses Brute-Force Attack, Encrypted Vaults of Fewer Than 20 Users Downloaded](https://thehackernews.com/2026/06/dashlane-discloses-brute-force-attack.html)

[![Miasma Supply Chain Attack Compromises Red Hat npm Packages with Credential-Stealing Worm](data:image/svg+xml;base64... "Miasma Supply Chain Attack Compromises Red Hat npm Packages with Credential-Stealing Worm")

Miasma Supply Chain Attack Compromises Red Hat npm Packages with Credential-Stealing Worm](https://...