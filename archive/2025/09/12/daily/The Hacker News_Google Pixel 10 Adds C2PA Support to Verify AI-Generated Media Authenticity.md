---
title: Google Pixel 10 Adds C2PA Support to Verify AI-Generated Media Authenticity
url: https://thehackernews.com/2025/09/google-pixel-10-adds-c2pa-support-to.html
source: The Hacker News
date: 2025-09-12
fetch_date: 2025-10-02T20:04:07.656796
---

# Google Pixel 10 Adds C2PA Support to Verify AI-Generated Media Authenticity

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

# [Google Pixel 10 Adds C2PA Support to Verify AI-Generated Media Authenticity](https://thehackernews.com/2025/09/google-pixel-10-adds-c2pa-support-to.html)

**Sep 11, 2025**Ravie LakshmananArtificial Intelligence / Mobile Security

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjiND-z6FdGroBwhkfZkICZE_a3n4Z0Zuv-Lt9_h07Z-PZXd3uJGpn71IErD1z2AZwtd_ezsUQYmBQZkqTfPyEQiOKgui5srkxLrkuwfWPFnf-Lq4aJT6li0saJGnkUtq_MSELJn4OsWoZLjJ_DGETm2jSCSnMieUaH-lQX5Z4FDonKkiMFgCiLZTIkKl97/s790-rw-e365/media.jpg)

Google on Tuesday announced that its new Google Pixel 10 phones support the Coalition for Content Provenance and Authenticity (C2PA) standard out of the box to verify the origin and history of digital content.

To that end, support for C2PA's [Content Credentials](https://contentcredentials.org) has been added to Pixel Camera and Google Photos apps for Android. The move, Google said, is designed to further digital media transparency.

C2PA's Content Credentials are a tamper-evident, cryptographically signed digital manifest providing verifiable provenance for digital content such as images, videos, or audio files. The metadata type, according to [Adobe](https://helpx.adobe.com/creative-cloud/apps/adobe-content-authenticity/content-credentials/overview.html), serves as a "digital nutrition label," giving information about the creator, how it was made, and if it was generated using artificial intelligence (AI).

"The Pixel Camera app achieved Assurance Level 2, the highest security rating currently defined by the C2PA Conformance Program," Google's Android Security and C2PA Core teams [said](https://security.googleblog.com/2025/09/pixel-android-trusted-images-c2pa-content-credentials.html). "Assurance Level 2 for a mobile app is currently only possible on the Android platform."

"Pixel 10 phones support on-device trusted time-stamps, which ensures images captured with your native camera app can be trusted after the certificate expires, even if they were captured when your device was offline."

The capability is made possible using a combination of Google Tensor G5, Titan M2 security chip, and hardware-backed security features built into the Android operating system.

[![CIS Build Kits](data:image/png;base64...)](https://thehackernews.uk/platform-shield-d)

Google said it has implemented C2PA to be secure, verifiable, and usable offline, thereby ensuring that provenance data is trustworthy, the process is not personally identifiable, and works even when the device is not connected to the internet.

This is achieved using -

* [Android Key Attestation](https://source.android.com/docs/security/features/keystore/attestation) to allow Google C2PA Certification Authorities (CAs) to verify that they are communicating with a genuine physical device
* Hardware-backed Android Key Attestation certificates that include the package name and signing certificates associated with the app that requested the generation of the C2PA signing key to verify the request originated from a trusted, registered app
* Generating and storing C2PA claim signing keys using Android StrongBox in the Titan M2 security chip for tamper-resistance
* Anonymous, hardware-backed attestation to certify new cryptographic keys generated on-device without knowing who is using it
* Unique certificates to sign each image, making it "cryptographically impossible" to deanonymize the creator
* On-device, offline Time-Stamping Authority (TSA) component within the Tensor chip to generate cryptographically-signed time-stamps when the camera's shutter is pressed

"C2PA Content Credentials are not the sole solution for identifying the provenance of digital media," Google said. "They are, however, a tangible step toward more media transparency and trust as we continue to unlock more human creativity with AI."

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

[Android](https://thehackernews.com/search/label/Android)[artificial intelligence](https://thehackernews.com/search/label/artificial%20intelligence)[cryptography](https://thehackernews.com/search/label/cryptography)[cybersecurity](https://thehackernews.com/search/label/cybersecurity)[data privacy](https://thehackernews.com/search/label/data%20privacy)[Google Pixel](https://thehackernews.com/search/label/Google%20Pixel)[mobile security](https://thehackernews.com/search/label/mobile%20security)[security](https://thehackernews.com/search/label/security)

[![c](data:image/svg+xml;base64...)](https://thehackernews.uk/cloud-defense)

Trending News

[![SolarWinds Releases Hotfix for Critical CVE-2025-26399 Remote Code Execution Flaw](data:image/svg+xml;base64... "SolarWinds Releases Hotfix for Critical CVE-2025-26399 Remote Code Execution Flaw")

SolarWinds Releases Hotfix for Critical CVE-2025-26399 Remote Code Execution Flaw](https://thehackernews.com/2025/09/solarwinds-releases-hotfix-for-critical.html)

[![Microsoft Patches Critical Entra ID Flaw Enabling Global Admin Impersonation Across Tenants](data:image/svg+xml;base64... "Microsoft Patches Critical Entra ID Flaw Enabling Global Admin Impersonation Across Tenants")

Microsoft Patches Critical Entra ID Flaw Enabling Global Admin Impersonation Across Tenan...