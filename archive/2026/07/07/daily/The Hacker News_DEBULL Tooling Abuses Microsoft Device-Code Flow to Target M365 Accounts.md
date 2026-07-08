---
title: DEBULL Tooling Abuses Microsoft Device-Code Flow to Target M365 Accounts
url: https://thehackernews.com/2026/07/debull-tooling-abuses-microsoft-device.html
source: The Hacker News
date: 2026-07-07
fetch_date: 2026-07-08T05:05:52.685808
---

# DEBULL Tooling Abuses Microsoft Device-Code Flow to Target M365 Accounts

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

# [DEBULL Tooling Abuses Microsoft Device-Code Flow to Target M365 Accounts](https://thehackernews.com/2026/07/debull-tooling-abuses-microsoft-device.html)

**Ravie Lakshmanan**Jul 07, 2026Identity Security / Threat Intelligence

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEg__v7vicSomxW52wnr8HsJgQKf0vg3kdjUicmIUCMCDexaBZ68pLZzXKVSJxNEeBuBuEzueOldcd5GhtGQI-8eMqd9j0QWMqGScmbZpqBS9RFkXxXSfOZYhBSGqD8BBDfVUEn4RN86sKhgkl9xkJtYMl-7a2zsIU6LCC5j_U2BkupJGr3JqP9_GZCHfHtl/s1700-e365/ms-device-code.jpg)

A Microsoft 365 [device code phishing](https://thehackernews.com/2026/03/device-code-phishing-hits-340-microsoft.html) campaign has been observed leveraging collaboration-themed lures to take control of victim accounts between the last week of June 2026 and into early July, per [findings](https://zerobec.com/blog/debull-storm-2372-microsoft-device-code-phishing-graphspy) from ZeroBEC.

"The campaign did not depend on a fake Microsoft password page. It used a malicious collaboration-style lure to push users into the legitimate Microsoft device login experience, while a backend broker generated and polled Microsoft Authentication Broker device-code tokens," the email security company said in a report shared with The Hacker News.

The activity is assessed to share "strong" overlaps with a campaign documented by Microsoft in February 2025 under the moniker [Storm-2372](https://thehackernews.com/2025/02/microsoft-russian-linked-hackers-using.html), including the use of messaging or Teams-style lures to trick unsuspecting victims into entering an attacker-provided device code, along with their credentials, effectively allowing the threat actor to recover the token and hijack their account.

Despite these similarities, it's assessed that the threat actors are employing Storm-2372-style tradecraft through what has been described as a reusable tooling layer called **DEBULL**.

Device code phishing refers to an identity theft technique where attackers exploit a legitimate OAuth 2.0 authentication mechanism, specifically the Device Authorization Grant flow, to bypass multi-factor authentication (MFA) and gain persistent account access without having to steal user passwords.

Unlike traditional phishing attacks that require the operators to set up bogus adversary-in-the-middle (AitM) login pages, device code phishing relies on manipulating a user into completing a real, trusted authentication prompt.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/ai-vuln-protection-d)

Device code authentication, per [Microsoft](https://www.microsoft.com/en-us/security/blog/2026/04/06/ai-enabled-device-code-phishing-campaign-april-2026/), is a legitimate OAuth flow designed for devices with limited interfaces, such as smart TVs or printers, that cannot support a traditional interactive login. In this scenario, a user is presented with a short code on the device they are trying to sign in from and is prompted to input that code into a web browser on a separate device to complete the authentication.

Threat actors have [abused](https://blog.knowbe4.com/what-is-device-code-phishing) this separation to insert themselves and [initiate the authentication flow](https://securelist.com/microsoft-device-code-phishing-attack/120350/). Then, they share that code with the target through a phishing lure. Thus, when the user enters the code, they authorize the threat actor's session without their knowledge, granting them access to the account.

"Device code phishing doesn't hack its way in," Huntress [notes](https://www.huntress.com/resources/what-is-device-code-phishing). "It uses a legitimate authentication flow to walk right through the front door, with no password required, MFA bypassed, and session tokens handed straight to the attacker."

Successful device code phishing attacks can facilitate full account takeover, theft of valuable information, fraud, business email compromise (BEC), lateral movement within a compromised environment, and even disruptive attacks like ransomware.

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEi7TDhc2XhP1l43CNLwdlWLLznNH7oG0hNRzfdqLZDhod52JHFG6ClV9HVQDxnruTykRj0s0p8tJvxA2IAb_dgbeQsGcAEkEjKMUcZnYYvtmtzRkT0aS_C6vcknNxZ0D_4DHNpzBSSWe2ZiVzoLA9mxJd_0LElWcSomAjLwKxPD-kCYzUW7GjQow6wpL1I4/s1700-e365/ms-account.png)

"In most current device code phishing attacks, the code is generated dynamically when a user clicks on the initial phishing link. This seemingly small change allows the user to view the email at any time to kickstart the attack chain," Proofpoint [said](https://www.proofpoint.com/us/blog/threat-insight/device-code-phishing-evolution-identity-takeover) in an analysis published in May 2026. "These new implementations of the device code attack chains can be purchased via phishing-as-a-service (PhaaS) offerings, like EvilTokens or Tycoon, or created and owned by the threat actor conducting the campaigns. "

These campaigns are also known to leverage account takeover (ATO) jumping, a technique where an attacker compromises an initial email account and then abuses it to send phishing links to a broader set of contacts in the form of a button, hyperlinked text, embedded within a document, or a QR code. The links, when visited by the recipient, initiate an attack sequence that employs the Microsoft device authorization process.

ZeroBEC said the campaign it observed involves using payment and shared-folder pretexts in phishing emails to deceive victims into clicking on a URL that takes them to a legitimate-but-compromised Croatian rental website, which, in turn, acts as a device code orchestrator used to initiate the Microsoft device code challenge chain.

The workflow is characterized by the presence of Turkish-language developer markers, although the clues aren't enough to definitively attribute the campaign's provenance. Further analysis of the infrastructure has revealed that DEBULL is likely a phishi...