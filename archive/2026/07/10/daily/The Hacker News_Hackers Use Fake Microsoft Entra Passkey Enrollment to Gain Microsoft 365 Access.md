---
title: Hackers Use Fake Microsoft Entra Passkey Enrollment to Gain Microsoft 365 Access
url: https://thehackernews.com/2026/07/hackers-use-fake-microsoft-entra.html
source: The Hacker News
date: 2026-07-10
fetch_date: 2026-07-11T05:04:37.883346
---

# Hackers Use Fake Microsoft Entra Passkey Enrollment to Gain Microsoft 365 Access

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

# [Hackers Use Fake Microsoft Entra Passkey Enrollment to Gain Microsoft 365 Access](https://thehackernews.com/2026/07/hackers-use-fake-microsoft-entra.html)

**Ravie Lakshmanan**Jul 10, 2026Enterprise Security / Authentication

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEh1L4YdSw3-1jg88TMzYxjsqRmu3Bq-VkmyGg742mMsJaIyhyaBk5MBeEFOxagE4H6GFjfH8ey1114iqyT0LuKYFdu7ocZhOrA3WQCvtNZGBknEJ1wTdb5vJ-M8w5kLXaUoBi39TXducoH8jZVrQ1xQQsBtEf0rrGJGfappdR1CrSB3xvaJC8Dgos2XdC37/s1700-e365/Microsoft-Entra-Passkey-Enrollment.jpg)

A threat actor has been targeting organizations spanning multiple sectors with voice-based fake security requests that prompt Microsoft 365 users to enroll a new Entra [passkey](https://thehackernews.com/2025/05/microsoft-sets-passkeys-default-for-new.html) with an aim to carry out data extortion attacks.

The threat actor, tracked by Okta under the moniker **O-UNC-066**, has deployed a panel-controlled phishing kit that's capable of targeting the [passkey enrollment process](https://support.microsoft.com/en-us/windows/security/identity-signin/create-and-save-a-passkey). The activity has singled out food and beverage, technology, healthcare, automotive, construction, and aviation industries.

"The threat actor registers domains that incorporate the word passkey as part of a voice-enabled phishing ('vishing') scheme," Okta researcher Houssem Eddine Bordjiba [said](https://www.okta.com/blog/threat-intelligence/vishing-actors-target-microsoft-entra-passkey-enrollment-/). "The threat actor then calls targeted users on the phone in an attempt to persuade them that they need to register a new passkey."

Users are then directed to a phishing kit that's identical to the Microsoft passkey enrollment process, giving the impression that they are adding a passkey with Microsoft, when, in reality, the threat actor registers their own passkey against their Microsoft account, granting them unauthorized access.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/ai-vuln-protection-d)

The development coincides with Microsoft allowing administrators to [configure registration campaigns](https://learn.microsoft.com/en-us/entra/fundamentals/whats-new#general-availability---support-for-passkeys-in-microsoft-entra-id-registration-campaign) to nudge users to register passkeys during sign-in in an attempt to help organizations drive passkey adoption at scale. In other words, threat actors are abusing the phishing-resistant security upgrade process as a lure to enroll their own passkeys within victims' accounts and facilitate follow-on activities.

Unlike adversary-in-the-middle ([AitM](https://thehackernews.com/2026/01/microsoft-flags-multi-stage-aitm.html)) landing pages that are prevalent in phishing campaigns designed to steal credentials and multi-factor authentication (MFA) tokens, the phishing kit used in these attacks is an operator-controlled PHP panel in which a victim is guided through the passkey enrollment process in almost real-time.

"The operator can use the kit to adapt the user experience to each victim's MFA requirements (TOTP, push notification with number matching, SMS OTP) during the session," the identity security company said. "The caller can control and adjust in real time what phishing pages and notifications a targeted user sees."

It's suspected that the threat actor is leveraging the kit to take over the victim account and trick the user into approving an attacker-initiated registration of a passkey. There is no indication at this stage to suggest that the kit is redirecting users to third-party identity providers like Okta.

The entire sequence of actions is below -

* The first page of the phishing kit (/gate) displays a page loading icon while the phishing kit performs anti-analysis checks in the background.
* The second page (/identify) requests a username.
* The next page (/password) challenges the user for a password.
* The harvested credentials are sent in a POST request to an operator panel at "/backend.php."
* The phishing kit operator (likely different from the individual calling the victim) enters the stolen credentials on the legitimate Microsoft sign-in page for the targeted tenant.
* The victim sees a "/processing" page that serves another loading screen as it awaits the operator's instruction based on the observed MFA challenges presented to them in the legitimate flow.
* The next page of the phishing kit is presented to the user: "/submit-otp" for an SMS-based one-time password (OTP) challenge, "/submit-authenticator" for time-based OTP challenge, or "/approve-authenticator" for a [push MFA challenge](https://learn.microsoft.com/en-us/entra/identity/authentication/how-to-mfa-number-match).
* The captured OTP is sent in a POST request to "/backend.php."

At this point, the victim has been deceived over the phone into approving the attacker's access to their Microsoft 365 account. The attack chain then initiates another set of actions focused around the passkey pretext -

* The victim is redirected to the "/passkey/register" page, which instructs the user to create a passkey.
* The Microsoft-branded "/passkey" page prompts the user to save their recovery key for confirming their passkey.
* The "/passkey/check" page asks the user to verify the final word used in the seed phrase.
* The "/done" page confirms that a passkey registration was successful.

[![Cybersecurity](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiBxLQDy7VdLze43eMmpRllTXaPKPfB_veNUxQlqIu3-68GBJtegkhDGCqtaiSymOQviROdxln1FSd4zdMp5Jv9jeF1xQxLPc9uo9H7zW2nWHNax0wT0Y8JRj-zyUfbaCLqhxSfQT2sCfhWMBPL6UVgsh5RYVNVxwus_mW_BY9Ptwz3z7iF0_LWOnte-gqg/s1600/sy-d-1.jpg)](https://thehackernews.uk/sygnia-cyber-response-d-1)

The recovery key contains a series of 12 words that's similar to secret recovery phrase or mnemonic phrase typically associated with cryptocurrency wallets. The step is assessed to be a distraction mechanism to keep the victim o...