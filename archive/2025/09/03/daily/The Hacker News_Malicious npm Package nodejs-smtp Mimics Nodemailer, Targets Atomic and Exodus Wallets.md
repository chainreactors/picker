---
title: Malicious npm Package nodejs-smtp Mimics Nodemailer, Targets Atomic and Exodus Wallets
url: https://thehackernews.com/2025/09/malicious-npm-package-nodejs-smtp.html
source: The Hacker News
date: 2025-09-03
fetch_date: 2025-10-02T19:34:49.770330
---

# Malicious npm Package nodejs-smtp Mimics Nodemailer, Targets Atomic and Exodus Wallets

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

[![Salesforce Security Handbook](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjWa8tsMNqlevi1HGF1ALQRGIq7hROPFAbHd3R1RTEOe73T8_Q2xW_-91t2jSGjU5peiPb8QYblGp4igNW-u2Qmlxbp2BKzTVMSvyXDZJmC-BYpiiJHrcnG5drmSP97iZ9PVIf1DeEr7U-7vWpe4HXwfMjt8FGNgq5mOycOJluYr9wF7YOKrQY9MfArwgjt/s728-e100/ai-agent-security-d.png)](https://thehackernews.uk/ai-agent-security-d)

# [Malicious npm Package nodejs-smtp Mimics Nodemailer, Targets Atomic and Exodus Wallets](https://thehackernews.com/2025/09/malicious-npm-package-nodejs-smtp.html)

**Sep 02, 2025**Ravie LakshmananCryptocurrency / Malware

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiRcOy1Zd5SkNC2FkVCAg2Qy-UKCj2kPIvWKA_pI4s8nt9Xlyl5h-KczhHriB1Vne7GA5AbAbVwd9HubZXnbdnCBWWbzUGEVEB0jue2opsZha9zUT5YDwIxCxaSCk6nETP7cUTVP1DdbhOce70hszHPDHY1Pkiyb9e0URgHsYudc_xKDae0-8WQO1-fPBtR/s790-rw-e365/crypto-wallter.jpg)

Cybersecurity researchers have discovered a malicious npm package that comes with stealthy features to inject malicious code into desktop apps for cryptocurrency wallets like Atomic and Exodus on Windows systems.

The package, named [nodejs-smtp](https://www.npmjs.com/package/nodejs-smtp), impersonates the legitimate email library [nodemailer](https://www.npmjs.com/package/nodemailer) with an identical tagline, page styling, and README descriptions, attracting a total of [347 downloads](https://npm-stat.com/charts.html?package=nodejs-smtp) since it was [uploaded](https://socket.dev/npm/package/nodejs-smtp/versions/0.0.1-security) to the npm registry in April 2025 by a user named "nikotimon." It's currently no longer available.

"On import, the package uses Electron tooling to unpack Atomic Wallet's app.asar, replace a vendor bundle with a malicious payload, repackage the application, and remove traces by deleting its working directory," Socket researcher Kirill Boychenko [said](https://socket.dev/blog/wallet-draining-npm-package-impersonates-nodemailer).

[![CIS Build Kits](data:image/png;base64...)](https://thehackernews.uk/platform-shield-d)

The main objective is to overwrite the recipient address with hard-coded wallets controlled by the threat actor, redirecting Bitcoin (BTC), Ethereum (ETH), Tether (USDT and TRX USDT), XRP (XRP), and Solana (SOL) transactions, effectively acting as a cryptocurrency clipper.

That having said, the package delivers on its stated functionality by acting as an SMTP-based mailer in an attempt to avoid raising developers' suspicion.

The package still works as a mailer and exposes a drop-in interface compatible with nodemailer. That functional cover lowers suspicion, allows application tests to pass, and gives developers little reason to question the dependency.

The development comes months after ReversingLabs [discovered](https://thehackernews.com/2025/04/malicious-npm-package-targets-atomic.html) an npm package named "pdf-to-office" that achieved the same goals by unpacking the "app.asar" archives associated with Atomic and Exodus wallets and modifying within them a JavaScript file to introduce the clipper function.

"This campaign shows how a routine import on a developer workstation can quietly modify a separate desktop application and persist across reboots," Boychenko said. "By abusing import time execution and Electron packaging, a lookalike mailer becomes a wallet drainer that alters Atomic and Exodus on compromised Windows systems."

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

[Atomic Wallet](https://thehackernews.com/search/label/Atomic%20Wallet)[Bitcoin](https://thehackernews.com/search/label/Bitcoin)[cryptocurrency](https://thehackernews.com/search/label/cryptocurrency)[cybersecurity](https://thehackernews.com/search/label/cybersecurity)[Electron](https://thehackernews.com/search/label/Electron)[Ethereum](https://thehackernews.com/search/label/Ethereum)[Malware](https://thehackernews.com/search/label/Malware)[NPM](https://thehackernews.com/search/label/NPM)[supply chain attack](https://thehackernews.com/search/label/supply%20chain%20attack)

[![c](data:image/svg+xml;base64...)](https://thehackernews.uk/cloud-defense)

Trending News

[![SolarWinds Releases Hotfix for Critical CVE-2025-26399 Remote Code Execution Flaw](data:image/svg+xml;base64... "SolarWinds Releases Hotfix for Critical CVE-2025-26399 Remote Code Execution Flaw")

SolarWinds Releases Hotfix for Critical CVE-2025-26399 Remote Code Execution Flaw](https://thehackernews.com/2025/09/solarwinds-releases-hotfix-for-critical.html)

[![Microsoft Patches Critical Entra ID Flaw Enabling Global Admin Impersonation Across Tenants](data:image/svg+xml;base64... "Microsoft Patches Critical Entra ID Flaw Enabling Global Admin Impersonation Across Tenants")

Microsoft Patches Critical Entra ID Flaw Enabling Global Admin Impersonation Across Tenants](https://thehackernews.com/2025/09/microsoft-patches-critical-entra-id.html)

[![Hackers Exploit Pandoc CVE-2025-51591 to Target AWS IMDS and Steal EC2 IAM Credentials](data:image/svg+xml;base64... "Hackers Exploit Pandoc CVE-2025-51591 to Target AWS IMDS and Steal EC2 IAM Credentials")

Hackers Exploit Pandoc CVE-2025-51591 to Target AWS IMDS and Steal EC2 IAM Credentials](https://thehackernews.com/2025/09/hackers-exploit-pandoc-cve-2025-51591.html)

[![China-Linked PlugX and Bookworm Malware Attacks Target Asian Telecom and ASEAN Networks](data:image/svg+xml;base64... "China-Linked PlugX and Bookworm Malware Attacks Target Asian Telecom and ASEAN Networks")

China-Linked PlugX and Bookworm Malware Attacks Target Asian Telecom and ASEAN Networks](https://th...