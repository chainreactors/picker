---
title: Microsoft 365 Android Apps Let Any App Steal Account Tokens via Leftover Debug Flag
url: https://thehackernews.com/2026/06/microsoft-365-android-apps-let-any-app.html
source: The Hacker News
date: 2026-06-03
fetch_date: 2026-06-04T06:32:18.061601
---

# Microsoft 365 Android Apps Let Any App Steal Account Tokens via Leftover Debug Flag

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

# [Microsoft 365 Android Apps Let Any App Steal Account Tokens via Leftover Debug Flag](https://thehackernews.com/2026/06/microsoft-365-android-apps-let-any-app.html)

**Swati Khandelwal**Jun 03, 2026Vulnerability / Mobile Security

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEh_pEYWDRVadGL0WYM3iSY6jqFgBez8snXgoyeyAzcXNmxiytv-FgiKoBJX3aPivuYhSJjXp4o_zO1dQSIPUfduaAlB-rvSti7pFhdDZSrAa-ennBdfdVpe1Xo0dMxKATB8te61pyJAf60x5CP6OJzjzmtpFIg_qHQqA7VP-rUnEpaT37Z0qBOmbZ52BfM/s1700-e365/ms-android.jpg)

A development flag left switched on in production builds of several Microsoft 365 Android apps disabled the check that limits account-token sharing to trusted Microsoft apps.

Any other app on the same phone could ask for the signed-in user's token and get it, then read email, open files, browse the calendar, and send messages as that user. No password, no login screen, no permission prompt.

Microsoft has patched it, and if you run Microsoft 365 apps on Android, update them.

The bug, which [Enclave](https://enclave.ai/blog/flagleft-microsoft-365-android-forgotten-flag-account-takeover) calls **FlagLeft**, hit Word, PowerPoint, Excel, Microsoft 365 Copilot, Microsoft Loop, and OneNote, six apps with billions of downloads between them. Teams shipped with the same flag set to false and were not affected, which Enclave reads as a slip rather than a design.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/ai-cant-stop-d)

Microsoft 365 apps share account access on purpose, so signing into Word means you do not sign in again for PowerPoint. The handoff is supposed to verify who is asking and turn away anything that is not a trusted Microsoft app.

Enclave's Yanir Tsarimi and Ofek Levin found the check was being skipped because of a single line left in the shipping code: **setIsDebugMode(true)**. The flaw sat in a shared Microsoft SDK, so the same hole showed up in app after app.

The tokens handed over were FOCI tokens, the family refreshes tokens Microsoft uses for single sign-on across its apps. They can be refreshed and reused over long stretches, and the resulting traffic looks routine in logs. From the user's side, nothing visible happens.

Enclave built a working proof of concept that pulled tokens through an unverified third-party app and read email with them. Microsoft classifies these as local spoofing flaws; in plain terms, a malicious app already on the device is all it takes.

Microsoft issued four CVEs on May 12, all classed as spoofing under improper access control (CWE-284): [CVE-2026-41100](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-41100) for Microsoft 365 Copilot (CVSS 4.4), [CVE-2026-41101](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-41101) for Word (CVSS 7.1), [CVE-2026-41102](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-41102) for PowerPoint (CVSS 7.1), and [CVE-2026-42832](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-42832) for Excel (CVSS 7.7). The four CVEs cover Copilot, Word, PowerPoint, and Excel.

Enclave reported the same flaw in Loop and OneNote, but neither got a separate CVE in the May batch. NVD lists the patched Word build for Android as 16.0.19822.20190, with earlier versions affected. The other apps were fixed through the same Google Play updates.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/vpn-threat-report-m)

Nothing in Microsoft's [May Patch Tuesday release](https://thehackernews.com/2026/05/microsoft-patches-138-vulnerabilities.html) was listed as publicly known or exploited, and there is no public evidence that the flaw was used before the fix.

What to do? Update Word, PowerPoint, Excel, Microsoft 365 Copilot, Loop, and OneNote from Google Play. Security teams managing Android fleets should push the updates through MDM and confirm devices are off builds earlier than 16.0.19822.20190.

The patch closes the hole, but it does not retroactively kill tokens that an attacker may already hold. FOCI refresh tokens outlive an app update, so for accounts on devices that ran an old build alongside untrusted apps, it is worth revoking refresh tokens and forcing a fresh sign-in.

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

[Android](https://thehackernews.com/search/label/Android), [cybersecurity](https://thehackernews.com/search/label/cybersecurity), [Microsoft](https://thehackernews.com/search/label/Microsoft), [Microsoft 365](https://thehackernews.com/search/label/Microsoft%20365), [mobile security](https://thehackernews.com/search/label/mobile%20security), [Patch Management](https://thehackernews.com/search/label/Patch%20Management), [Vulnerability](https://thehackernews.com/search/label/Vulnerability)

⚡ Top Stories This Week

[![Google June 2026 Android Update Patches 124 Flaws, One Actively Exploited](data:image/svg+xml;base64... "Google June 2026 Android Update Patches 124 Flaws, One Actively Exploited")

Google June 2026 Android Update Patches 124 Flaws, One Actively Exploited](https://thehackernews.com/2026/06/google-june-2026-android-update-patches.html)

[![Oracle WebLogic CVE-2024-21182 Added to KEV Catalog After...