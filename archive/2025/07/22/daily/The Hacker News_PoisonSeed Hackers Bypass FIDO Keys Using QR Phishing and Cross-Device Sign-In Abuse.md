---
title: PoisonSeed Hackers Bypass FIDO Keys Using QR Phishing and Cross-Device Sign-In Abuse
url: https://thehackernews.com/2025/07/poisonseed-hackers-bypass-fido-keys.html
source: The Hacker News
date: 2025-07-22
fetch_date: 2025-10-06T23:53:40.057048
---

# PoisonSeed Hackers Bypass FIDO Keys Using QR Phishing and Cross-Device Sign-In Abuse

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

# [PoisonSeed Attack Turns Out to Be Not a FIDO Bypass After All](https://thehackernews.com/2025/07/poisonseed-hackers-bypass-fido-keys.html)

**Jul 21, 2025**Ravie LakshmananThreat Intelligence / Authentication

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjilI91Ju0exOb_WYU9jgtvpUK1IVpGrqjK05wg5Yr2LfW0G6oxma_Tbwl0bwOLQPHDc1yMAr5-xef6cryal5hhdh-Nojn7qPGYwIqO4KDkSWRoZrDcphk1GGtoL1Bb74npgLAoLroWO7s-EnkN4dNT10BOlPbNigW76EQwSaSUKk04PkO-nbO98snVcX7J/s790-rw-e365/login-fido.jpg)

Cybersecurity firm Expel, in an update shared on July 25, 2025, said it's retracting its findings about a phishing attack that it said leveraged cross-device sign-in to get around FIDO account protections despite being not in physical proximity to the authenticating client device.

"The evidence does show the targeted user's credentials (username and password) being phished and that the attacker successfully passed password authentication for the targeted user," the company [said](https://expel.com/blog/an-important-update-and-apology-on-our-poisonseed-blog/).

"It also shows the user received a QR code from the attacker. This QR code, when scanned by a mobile device, initiates a FIDO Cross-Device Authentication flow, which according to FIDO specification requires local proximity to the device which generated the QR code (the WebAuthn client). When properly implemented, without proximity, the request will time out and fail."

The company further said that while the attackers managed to breach the password barrier, further analysis of the Okta logs revealed that all subsequent multi-factor authentication (MFA) challenges failed and that the attackers were not granted access to the requested resource.

Queries sent by The Hacker News to Expel asking for clarification on the exact method used to achieve a "bypass" received no responses until now. The original story continues below -

Cybersecurity researchers have disclosed a novel attack technique that allows threat actors to downgrade Fast IDentity Online ([FIDO](https://fidoalliance.org/)) key protections by deceiving users into approving authentication requests from spoofed company login portals.

FIDO keys are hardware- or software-based authenticators designed to eliminate phishing by binding logins to specific domains using public-private key cryptography. In this case, attackers exploit a legitimate feature—cross-device sign-in—to trick victims into unknowingly authenticating malicious sessions.

The activity, observed by Expel as part of a phishing campaign in the wild, has been attributed to a threat actor named [PoisonSeed](https://thehackernews.com/2025/04/poisonseed-exploits-crm-accounts-to.html), which was recently flagged as leveraging compromised credentials associated with customer relationship management (CRM) tools and bulk email providers to send spam messages containing cryptocurrency seed phrases and drain victims' digital wallets.

"The attacker does this by taking advantage of cross-device sign-in features available with FIDO keys," researchers Ben Nahorney and Brandon Overstreet [said](https://expel.com/blog/poisonseed-bypassing-fido-keys-to-fetch-user-accounts/). "However, the bad actors in this case are using this feature in adversary-in-the-middle (AitM) attacks."

This technique doesn't work in all scenarios. It specifically targets users authenticating via cross-device flows that don't enforce strict proximity checks—such as Bluetooth or local device attestation. If a user's environment mandates hardware security keys plugged directly into the login device, or uses platform-bound authenticators (like Face ID tied to the browser context), the attack chain breaks.

[![DFIR Retainer Services](data:image/png;base64...)](https://thehackernews.uk/cloud-insight-d)

[Cross-device sign-in](https://www.passkeycentral.org/design-guidelines/optional-patterns/cross-device-sign-in) allows users to sign-in on a device that does not have a passkey using a second device that does hold the cryptographic key, such as a mobile phone.

The attack chain documented by Expel commences with a phishing email that lures recipients to log into a fake sign-in page mimicking the enterprise's Okta portal. Once the victims enter their credentials, the sign-in information is stealthily relayed by the bogus site to the real login page.

The phishing site then instructs the legitimate login page to use the hybrid transport method for authentication, which causes the page to serve a QR code that's subsequently sent back to the phishing site and presented to the victim.

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjridz16c0l5OIA1x1yT_9z9sAFvyGj4Qn7ihf0KKtAF0ZcdHoMjQBiOkWLmN84yYsKyLV-sytw67sm4tK-04tjDwsXHwe7j2Du_TYeENSXZF4R8fUoOyij5lCGymKppL52qs_ubos-DVxAtHmlmUm3IYJ63F6dmM1srBfe_WbbaoIh0yRSAEISXcOLSgJ1/s790-rw-e365/attack.jpg)

Should the user scan the QR code with the authenticator app on their mobile device, it allows the attackers to gain unauthorized access to the victim's account.

"In the case of this attack, the bad actors have entered the correct username and password and requested cross-device sign-in," Expel said.

"The login portal displays a QR code, which the phishing site immediately captures and relays back to the user on the fake site. The user scans it with their MFA authenticator, the login portal and the MFA authenticator communicate, and the attackers are in."

What makes the attack noteworthy is that it gets around protections offered by FIDO keys and enables threat actors to obtain access to users' accounts. The compromise method does not exploit any flaw in the FIDO implementation. Rather, it abuses a legitimate feature to downgrade the authentication process.

While FIDO2 is designed to resist phishing, its cross-device login flow—known as hybrid transport—can be misused if proximity verification like Bluetooth is not enforced. In this flow, users can log in on a desktop by scanning a QR code with a mob...