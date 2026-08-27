---
title: Fake Apple Support AI Calls Target Stolen-Device Owners for Passcodes and 2FA Codes
url: https://thehackernews.com/2026/08/fake-apple-support-ai-calls-target.html
source: The Hacker News
date: 2026-08-26
fetch_date: 2026-08-27T12:14:30.734415
---

# Fake Apple Support AI Calls Target Stolen-Device Owners for Passcodes and 2FA Codes

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

[![cybersecurity](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEipoZWeZ29mSf60rRpMZ3Ucnm7oeWBfslPFPT6xADBsdvBtjd20ovH2yLscUo8pS6OTK0ItATC25VeavJh73IgqJM6Nb3apqobQ9zEVISE-d0wEFAimLYUcnffWCTowCCqs5LofRTQP25xB32KzYhlTO8lUnkZfmtELv23LlgdeKY3nyS2etYQXGdPIQtnh/s728-e100/wiz-d.png)](https://thehackernews.uk/ai-security-playbook-d)

# [Fake Apple Support AI Calls Target Stolen-Device Owners for Passcodes and 2FA Codes](https://thehackernews.com/2026/08/fake-apple-support-ai-calls-target.html)

**Swati Khandelwal**Aug 26, 2026Artificial Intelligence / Cybercrime

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjZ7ibePn1YRPkAC27RIrMl_O-41pR7ieF0Mkpr8WUTkzCddWjpttUiIrXWI3CYGukgNR8eoppnOFUYjzSbEm66XiK4ttGge7-KicMnSf49N5L-wKXyf4NIzWi1Yi5JbKQXPYpmtWfZfMADrNswG9-ZfOOE9LjWwUFl7twHmvEskgU9iXPR5AGEQ4hUETo/s1700-e365/iphone-passcode.jpg)

Cybersecurity researchers have disclosed details of a phishing-as-a-service (PhaaS) platform built to strip Apple's Activation Lock from stolen devices, using rented AI voice agents that call theft victims posing as Apple Support and ask for their device passcode.

SOCRadar Threat Research Unit (STRU) said the platform, which it tracks as **AnonyMousKIT**, is credit-metered and drives lures across five channels from a single victim record, comprising email at 1.50 credits, SMS priced per sender ID, WhatsApp, a recorded voice call at 1 credit, and an AI voice agent at 2 credits.

The targets are owners of Apple devices that were recently lost or stolen, and the pages and calls ask each of them for the 4- or 6-digit device passcode, then the Apple ID credentials, and finally a live two-factor authentication (2FA) code. Apple's own guidance states that the company never asks for a password, device passcode, or 2FA code to provide support.

"AnonyMousKIT is best understood not as a phishing kit but a small software business with a criminal customer base. It features credit bundles, published pricing, tiered subscriptions, customer support, status tracking, and infrastructure replacement protocols," SOCRadar said [in a Monday report](https://socradar.io/blog/anonymouskit-ai-phaas-supply-chain/).

Activation Lock, introduced in iOS 7, ties the hardware to a specific Apple ID and renders a stolen handset unusable until the owner's account is removed.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/zero-trust-claude-d)

Lures cite the handset's internal Apple model identifier and its live Find My status, both pulled from the stolen device itself. Victims who follow the link reach an Apple-branded capture page that renders an animated map of the handset's reported location.

The AI voice channel is the best-documented vector after email, with 200 call records, 55 transcripts, and five configured personas recovered from the operator's account with the commercial voice platform **Vapi**.

The researchers' report does not say whether the account was reported to Vapi, and neither company has said publicly whether it is still active. All five personas carry the same translated identity, Alice from Apple Support, across English, Spanish, and Portuguese.

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiVqPy0GOC-txZsVja8YZYxQP7mZBGGUEU3Gv8F5cudFA-B1G-_Ig6JxJ6EkCacnfdfxUUUesd-qfrDTbYjVnwfUSP6aPDzaK_HcPr4rJtbf3qhjnN5IzlXOYSR1CKN7LzvgufH0pzouWb-fosRQhJROWXpPhKllC4eUxLpBSdLhmtXy6FBx5rwPG8-4Nw/s1700-e365/AnonyMousKIT.jpg)

The calls ran between August 31, 2025 and May 30, 2026, and 179 of the 200 went to numbers in Brazil. In the recovered transcript, the agent asks the victim to confirm ownership, then requests the four- or six-digit passcode and reads the digits back for confirmation.

It then explains that someone visited an Apple Store to remove the Activation Lock and asks whether a recovery link has arrived via text. The researchers put the total cost of the 200 calls at $19.24, or about 9.6 cents each.

The outcome table in the report assigns all 200 calls to one of four results, comprising 100 victims who hung up, 48 silence timeouts, 24 no-answers, and 28 platform errors or busy signals. No count of captured passcodes, Apple IDs, or 2FA codes appears in the report for any of the five channels.

The logs reached SOCRadar via two bare relative file paths in the shared codebase that resolve to the web root and allow unauthenticated HTTP access. Every deployment of that codebase inherits the flaw.

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiyRw_JGWbffzDdEGQslA4uGs1hmO1Zu_bs3q8ctrIe8c1l32rxsts_U89bx2ylofS9l194wXlsjTPL6vmsBtzta2keR86a7zBv7IQThAe1whg9WY-6MHGACX-IyLuyekOeEUP36M8-DmhhnwFAaCAMpNleySN3-41qptoU_5Hu-cuWlOyl8tUGxC79Kd4/s1700-e365/AnonyMousKIT-1.jpg)

A scan of 506 kit-family domains identified 30 distinct installations reachable on 42 domains, with 188 of the 506 live.

The AnonyMousKIT installation logged 691 send attempts between March and July 2026, compared with 6,092 across the 30 backends.

Three storefronts, i-Blocker, Key Unlock, and KG-KING, launched in the same second on April 10, 2026, sharing the same Gmail relay accounts. SOCRadar assessed that pattern as one buyer running three brands rather than three separate customers.

The researchers recorded the following characteristics of the email lures -

* The top two subject lines were "Your device has been found" (308 of 691) and "Alert" (157)
* Display names spoofed Apple, Find My, Apple Support, and Apple Assistance
* 627 of the logged sends relayed through a single free Gmail account, noreplyapple00000[@]gmail[.]com, against 20 and 2 for the two other relay accounts
* 678 of the 691 lures carried a location token naming a city, including Johannesburg, Abuja, Buenos Aires, Maputo, and Mumbai
* Victim-facing capture pages were served from tokenized /help?TOKEN URLs

South Africa accounts for 1,735 of the 6,092 family-wide sends, and 64 of AnonyMousKIT's own 691 sends reached non-consumer domains, including 27 to South African government addresses. SOCRadar said those recipients were selected because their devices were stolen, not because of their roles.

The report said the four unlock tools offered on the panel serve as bait, because 5,649 of the 6,092 targeted devices, or 92.7%, run A12 silicon o...