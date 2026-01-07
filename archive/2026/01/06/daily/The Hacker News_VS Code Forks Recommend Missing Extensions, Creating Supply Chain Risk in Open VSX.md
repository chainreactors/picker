---
title: VS Code Forks Recommend Missing Extensions, Creating Supply Chain Risk in Open VSX
url: https://thehackernews.com/2026/01/vs-code-forks-recommend-missing.html
source: The Hacker News
date: 2026-01-06
fetch_date: 2026-01-07T03:30:45.616776
---

# VS Code Forks Recommend Missing Extensions, Creating Supply Chain Risk in Open VSX

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

[![Salesforce Security Handbook](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhlCcy_j509wX0FKMRQX-zVzeBNtSIDsH6oDFlljaAeQRz65xSx8g9jicghxtpvDC8yI10jCv1TPEcyPvfoCKOby_0ZjsnNc-3wZG5YeA8sZQBCbZxhzd00jR2ZG8rZr-vp3WLrbXaMVbsVrDwBEeBWBbNSSwFjeuNzhrVOigDqTM7VWfSUJqBwEoYALS58/s728-e100/z-header-d.png)](https://thehackernews.uk/modern-security-shift-d)

# [VS Code Forks Recommend Missing Extensions, Creating Supply Chain Risk in Open VSX](https://thehackernews.com/2026/01/vs-code-forks-recommend-missing.html)

**Jan 06, 2026**Ravie LakshmananThreat Intelligence / Cloud Security

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEg0cvjE-uBAOipvEWs5BsHAt3ztw9IYIHxKGLFRdgCKnxYAJ1UHFZs0b3Zl_xw729c3-7WMgT3G4uLN2kLzwHpwZ3HZFXJ6KwgPg4v6JH3k02OsrQVFHF8BDsf4XKhKjuOajrGqcmNxvmE4LKCru_S6L2wV8SfI38McnPrcI4WC_r_wZHOfLYcOgACPmTvQ/s2600/koi.jpg)

Popular artificial intelligence (AI)-powered Microsoft Visual Studio Code (VS Code) forks such as Cursor, Windsurf, Google Antigravity, and Trae have been found to recommend extensions that are non-existent in the Open VSX registry, potentially opening the door to supply chain risks when bad actors publish malicious packages under those names.

The problem, [according to Koi](https://www.koi.ai/blog/how-we-prevented-cursor-windsurf-google-antigravity-from-recommending-malware), is that these integrated development environments (IDEs) inherit the list of officially recommended extensions from Microsoft's extensions marketplace. These extensions don't exist in Open VSX.

The VS Code extension recommendations can take two different forms: file-based, which are displayed as toast notifications when users open a file in specific formats, or software-based, which are suggested when certain programs are already installed on the host.

"The problem: these recommended extensions didn't exist on Open VSX," Koi security researcher Oren Yomtov said. "The namespaces were unclaimed. Anyone could register them and upload whatever they wanted."

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/zero-trust-summit-d)

In other words, an attacker could weaponize the absence of these VS Code extensions and the fact that the AI-powered IDEs are VS Code forks to upload a malicious extension to the Open VSX registry, such as ms-ossdata.vscode-postgresql.

As a result, any time a developer with PostgreSQL installed opens one of the aforementioned IDEs and sees the message "Recommended: PostgreSQL extension," a trivial install action is enough to result in the deployment of the rogue extension on their system instead.

This simple act of trust can have severe consequences, potentially leading to the theft of sensitive data, including credentials, secrets, and source code. Koi said its placeholder PostgreSQL extension attracted no less than 500 installs, indicating that developers are downloading it simply because the IDE suggested it as a recommendation.

The names of some of the extensions that have been claimed by Koi with a placeholder are listed below -

* ms-ossdata.vscode-postgresql
* ms-azure-devops.azure-pipelines
* msazurermtools.azurerm-vscode-tools
* usqlextpublisher.usql-vscode-ext
* cake-build.cake-vscode
* pkosta2005.heroku-command

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/attack-surface-insight-d)

In response to responsible disclosure, Cursor, Windsurf, and Google have rolled out fixes to address the issue. The Eclipse Foundation, which oversees Open VSX, has since removed non-official contributors and enforced broader registry-level safeguards.

With threat actors increasingly focusing on exploiting the security gaps in extension marketplaces and open-source repositories, it's essential that developers exercise caution prior to downloading any packages or approving installs by verifying they come from a trusted publisher.

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

[Cloud security](https://thehackernews.com/search/label/Cloud%20security)[cybersecurity](https://thehackernews.com/search/label/cybersecurity)[Malware](https://thehackernews.com/search/label/Malware)[Open Source](https://thehackernews.com/search/label/Open%20Source)[Supply Chain Security](https://thehackernews.com/search/label/Supply%20Chain%20Security)[Threat Intelligence](https://thehackernews.com/search/label/Threat%20Intelligence)

Trending News

[![DarkSpectre Browser Extension Campaigns Exposed After Impacting 8.8 Million Users Worldwide](data:image/svg+xml;base64... "DarkSpectre Browser Extension Campaigns Exposed After Impacting 8.8 Million Users Worldwide")

DarkSpectre Browser Extension Campaigns Exposed After Impacting 8.8 Million Users Worldwide](https://thehackernews.com/2025/12/darkspectre-browser-extension-campaigns.html)

[![CSA Issues Alert on Critical SmarterMail Bug Allowing Remote Code Execution](data:image/svg+xml;base64... "CSA Issues Alert on Critical SmarterMail Bug Allowing Remote Code Execution")

CSA Issues Alert on Critical SmarterMail Bug Allowing Remote Code Execution](https://thehackernews.com/2025/12/csa-issues-alert-on-critical.html)

[![⚡ Weekly Recap: MongoDB Attacks, Wallet Breaches, Android Spyware, Insider Crime and More](data:image/svg+xml;base64... "⚡ Weekly Recap: MongoDB Attacks, Wallet Breaches, Android Spyware, Insider Crime and More")

⚡ Weekly Recap: MongoDB Attacks, Wallet Breaches, Android Spyware, Insider Crime and More](https://thehackernews.com/2025/12/weekly-recap-mongodb-attacks-wallet.html)

[![MongoDB Vulnerability CVE-2025-14847 Under Active Exploitation Wo...