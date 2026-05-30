---
title: Malicious Sicoob NuGet Steals Banking Credentials as npm Packages Target Cloud Secrets
url: https://thehackernews.com/2026/05/malicious-sicoob-nuget-steals-banking.html
source: The Hacker News
date: 2026-05-29
fetch_date: 2026-05-30T05:44:31.755523
---

# Malicious Sicoob NuGet Steals Banking Credentials as npm Packages Target Cloud Secrets

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

[![cybersecurity](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhyqUz0-ifa8jE9rCzud3wzxmhcuzTp1VOWFEvGMoZXDYfaB_4459fPyvyQw7wvAnzjzDL09PkyJM83QGheO69fC3esg1WA7WnJ89i_t_q3K8DxYmgV__QujU8RWRnCK4MpbKqu8nwuMFfLaiRVHy_ov7IZ16hoKI3rIu-5BcISmqXPjlQU7N0sa4lWI-n-/s728-e100/wiz-d.png)](https://thehackernews.uk/wiz-ai-state-d)

# [Malicious Sicoob NuGet Steals Banking Credentials as npm Packages Target Cloud Secrets](https://thehackernews.com/2026/05/malicious-sicoob-nuget-steals-banking.html)

**Ravie Lakshmanan**May 29, 2026Software Supply Chain / Threat Intelligence

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgUbmZyAOVZRXrWddG8PMuXbVyex9s5HPD2cH8rDjYP6EHuVadkyj72NdN9PreAnGX9iOCVGxWI2YmSLu818VmdLGEcPkb60qPIUgBYh5oBHsA4KKYufsHbFGhAQDD7SjpZU0In0TPiHN4TxCR4THBwmKa4Bus98vBgx5mO3QTQRpTM5RERk8bFWi4psF7d/s1700-e365/sdk.jpg)

Cybersecurity researchers have discovered a malicious NuGet package that masquerades as a C# software development kit for Sicoob, one of Brazil's largest cooperative financial systems, to siphon client IDs and PFX certificates.

According to [Socket](https://socket.dev/blog/malicious-nuget-package-impersonates-sicoob-sdk), versions 2.0.0 through 2.0.4 of "[Sicoob.Sdk](https://www.nuget.org/packages/Sicoob.Sdk)" contain functionality to exfiltrate sensitive information, including PFX certificates that are used to authenticate businesses with the Sicoob banking network in order to automate banking operations, such as processing instant payments and generating dynamic Pix QR codes. The package is estimated to have been downloaded nearly 500 times.

"When a developer instantiates SicoobClient with a client ID, a PFX file path, and a PFX password, the package reads the PFX file from disk, Base64-encodes its contents, and sends the supplied client ID, PFX password, and encoded PFX data to a hardcoded third-party Sentry endpoint," security researcher Kirill Boychenko said.

In addition, the package is designed to capture raw Boleto API responses via a separate Sentry path. [Boleto](https://en.wikipedia.org/wiki/Boleto) is a popular cash payment method in Brazil for making online and offline purchases. This can potentially expose sensitive transaction details, payment status, amounts, due dates, identifiers, and payer or payee data.

As a result, the stolen data could open the door to severe risks, as it can be abused by the threat actor to impersonate the victim's Sicoob banking API integration, Socket added. Following responsible disclosure, the package has been blocked by NuGet. The profile behind the package, named "sicoob," has also listed 11 other NuGet packages that have collectively racked up about 6,000 downloads.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/threatlabz-vpn-risk-2026-d)

The application security company also said the package was surfaced by Google Search AI Mode as a legitimate C# library for interacting with Sicoob banking APIs, thereby amplifying the malicious package to unsuspecting developers who may be searching for it.

Another important aspect of the attack is the source-to-package mismatch between the [linked GitHub repository](https://github.com/Sicoob-Cooperativa) and the artifact distributed via NuGet. It's suspected that the GitHub repository is designed to lend a veneer of legitimacy to the operation by keeping it clean, while the malicious data-stealing functionality is introduced only in the package uploaded to the registry.

What's more, the compromise of Sicoob API authentication material can also pose indirect risks to end users, as it could leak downstream financial data or enable payment abuse.

Organizations that have installed "Sicoob.Sdk" are recommended to immediately remove the package, treat PFX material as compromised, replace exposed PFX certificates, rotate PFX passwords, and change or disable affected client IDs where applicable. It's also advised to audit Sicoob authentication and API logs for signs of unusual activity.

The development coincides with the [discovery](https://www.microsoft.com/en-us/security/blog/2026/05/28/typosquatted-npm-packages-used-steal-cloud-ci-cd-secrets/) of 14 malicious npm packages that typosquat well-known OpenSearch, ElasticSearch, DevOps, and environment-configuration libraries to harvest AWS credentials, HashiCorp Vault tokens, npm tokens, and CI/CD pipeline secrets from the host environment using a purpose-built credential harvester that's launched through a preinstall hook.

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgl8GTYDoJnPuVc-Moe3_cvURFF5ffKE6oLQpRZZSqm_CpZMnLgWPCuuRic86H7eEi9hFAU0KGwT-DiK2QS8ZAh9fwW4ioenx91SS5g8SS8l8q6FRFk9FBeZ7fnCkBw9SvmA2mz68KzSihGNHC42TdYkl7ZP0PdJsngTIq-ep2xqPCOQN7X-Dpx8EfRYp4q/s1700-e365/signed.jpg)

Per the Microsoft Defender Security Research Team, the packages were published by a single threat actor named "vpmdhaj" ("a39155771@gmail.com") on May 28, 2026. The names of the packages are below -

* @vpmdhaj/devops-tools
* @vpmdhaj/elastic-helper
* @vpmdhaj/opensearch-setup
* @vpmdhaj/search-setup
* app-config-utility
* elastic-opensearch-helper
* env-config-manager
* opensearch-config-utility
* opensearch-security-scanner
* opensearch-setup
* opensearch-setup-tool
* search-cluster-setup
* search-engine-setup
* vpmdhaj-opensearch-setup

The findings are the latest in a staggering spate of supply chain attack campaigns that have targeted the npm ecosystem over the past few days -

* [164 malicious npm packages](https://safedep.io/oob-moika-tech-dependency-confusion-campaign/) across five scoped namespaces containing a postinstall payload that downloads second-stage JavaScript, spawns it as a detached process, and sends the victim's environment variables ("process.env") to "oob.moika[.]tech/report."
* [141 malicious npm packages](https://safedep.io/malicious-npm-terminal3airport-proxy-adware-spam/) published between May 7 and 27, 2026, that abuse npm as free static hosting for an ad-monetized web proxy targeting students, serving popunder ads to those who land these pages through search results or shared links.
* A malicious npm package called "[forge-jsxy](https://safedep.io/malicious-forge-jsxy-npm-rat-evolution/)" that's capable of keylogging, clipboard monitoring, .env scanning, shell hi...