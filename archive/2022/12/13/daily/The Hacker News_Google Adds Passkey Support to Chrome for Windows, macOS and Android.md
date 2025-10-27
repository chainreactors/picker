---
title: Google Adds Passkey Support to Chrome for Windows, macOS and Android
url: https://thehackernews.com/2022/12/google-adds-passkey-support-to-chrome.html
source: The Hacker News
date: 2022-12-13
fetch_date: 2025-10-04T01:21:13.375840
---

# Google Adds Passkey Support to Chrome for Windows, macOS and Android

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

# [Google Adds Passkey Support to Chrome for Windows, macOS and Android](https://thehackernews.com/2022/12/google-adds-passkey-support-to-chrome.html)

**Dec 12, 2022**Ravie LakshmananPassword Management

[![Chrome Passkey](data:image/png;base64... "Chrome Passkey")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgpbq-VJYQIHq-dkwcEoQQeboqNNhOWHIAk78dq6P9IAspoZsSQ38XX68diDsMRyxI1yyX5kR8kkgjKMQXXNlsVUCrL5p0qWj3c9HfFDgWvL9vg_I7rZvq6OgyKxMJkMScYvgCxbTyN9TN5W3ObBM3jM3Zn5Wz55uIxrbGnfbxPmkad5IRlgTkJEpRS/s790-rw-e365/google-1.gif)

Google has officially begun rolling out support for [passkeys](https://fidoalliance.org/passkeys/), the next-generation passwordless login standard, to its stable version of Chrome web browser.

"Passkeys are a significantly safer replacement for passwords and other phishable authentication factors," the tech giant's Ali Sarraf [said](https://blog.chromium.org/2022/12/introducing-passkeys-in-chrome.html). "They cannot be reused, don't leak in server breaches, and protect users from phishing attacks."

The improved security feature, which is available in version 108, comes nearly two months after Google [began testing the option](https://thehackernews.com/2022/10/google-rolling-out-passkey-passwordless.html) across Android, macOS, and Windows 11.

[![DFIR Retainer Services](data:image/png;base64...)](https://thehackernews.uk/cloud-insight-d)

[Passkeys](https://www.passkeys.io/) obviate the need for passwords by requiring users to authenticate themselves during sign in by unlocking their nearby Android or iOS device using biometrics. This, however, calls for websites to build passkey support on their sites using the [WebAuthn API](https://webauthn.guide/).

Essentially, the technology works by creating a unique cryptographic key pair to associate with an account for the app or website during account registration. One of these keys, the public key, is stored in the server. The private key, on the other hand, never leaves the device in which the keys are generated.

[![Chrome Passkey](data:image/png;base64... "Chrome Passkey")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhlTscVa7-JPDX72RyyJEccZdAUeq3b4gsD4SPrOeO6FPE_ozqfzn8_UmeuZmtTEzkvDbhdLLyxsEl3SdYEKq9pxn295Q7mnQdeFluqH1oj8Ok_ug4eOHjk2BF_t1WEoRBV214zolvIXSkaD_v6_LGlx-zvB8_oOqiBTCoV3yXKaNwxyUrYycMb-McH/s790-rw-e365/google-2.gif)

On Android, the "keys" are uploaded to Google Password Manager (or a third party like [1Password](https://www.future.1password.com/passkeys/) or [Dashlane](https://support.dashlane.com/hc/en-us/articles/7888558064274-Passkeys-in-Dashlane)) to prevent lockouts. Passkeys are [synced](https://support.apple.com/en-us/HT213305) via iCloud Keychain on iOS and macOS, while Microsoft Windows is set to offer support in 2023.

[![CIS Build Kits](data:image/png;base64...)](https://thehackernews.uk/platform-shield-d)

"When a passkey is backed up, its private key is uploaded only in its encrypted form using an encryption key that is only accessible on the user's own devices," Google software engineer Arnar Birgisson previously noted in October 2022.

The idea is to protect the passkeys from Google such that a rogue actor inside the company cannot use them to log in to the corresponding online services without access to the private key.

The internet and advertising company is also [expected](https://developers.google.com/identity/passkeys/supported-environments) to make available a new API to provide passkeys support for Android apps.

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

[Google](https://thehackernews.com/search/label/Google)[Passkey](https://thehackernews.com/search/label/Passkey)[Password Management](https://thehackernews.com/search/label/Password%20Management)[Passwordless Authentication](https://thehackernews.com/search/label/Passwordless%20Authentication)

[![c](data:image/svg+xml;base64...)](https://thehackernews.uk/cloud-defense)

Trending News

[![SolarWinds Releases Hotfix for Critical CVE-2025-26399 Remote Code Execution Flaw](data:image/svg+xml;base64... "SolarWinds Releases Hotfix for Critical CVE-2025-26399 Remote Code Execution Flaw")

SolarWinds Releases Hotfix for Critical CVE-2025-26399 Remote Code Execution Flaw](https://thehackernews.com/2025/09/solarwinds-releases-hotfix-for-critical.html)

[![Microsoft Patches Critical Entra ID Flaw Enabling Global Admin Impersonation Across Tenants](data:image/svg+xml;base64... "Microsoft Patches Critical Entra ID Flaw Enabling Global Admin Impersonation Across Tenants")

Microsoft Patches Critical Entra ID Flaw Enabling Global Admin Impersonation Across Tenants](https://thehackernews.com/2025/09/microsoft-patches-critical-entra-id.html)

[![Hackers Exploit Pandoc CVE-2025-51591 to Target AWS IMDS and Steal EC2 IAM Credentials](data:image/svg+xml;base64... "Hackers Exploit Pandoc CVE-2025-51591 to Target AWS IMDS and Steal EC2 IAM Credentials")

Hackers Exploit Pandoc CVE-2025-51591 to Target AWS IMDS and Steal EC2 IAM Credentials](https://thehackernews.com/2025/09/hackers-exploit-pandoc-cve-2025-51591.html)

[![China-Linked PlugX and Bookworm Malware Attacks Target Asian Telecom and ASEAN Networks](data:image/svg+xml;base64... "China-Linked PlugX and Boo...