---
title: Sneaky 2FA Phishing Kit Adds BitB Pop-ups Designed to Mimic the Browser Address Bar
url: https://thehackernews.com/2025/11/sneaky-2fa-phishing-kit-adds-bitb-pop.html
source: The Hacker News
date: 2025-11-18
fetch_date: 2025-11-19T03:14:53.995104
---

# Sneaky 2FA Phishing Kit Adds BitB Pop-ups Designed to Mimic the Browser Address Bar

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

[![Salesforce Security Handbook](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhjMQkm7Ao3yQkNVeqy3au4G4E34VWzSsT55GDPjHHGjbHksJqrJCyM1ChO1hB9WzaFzZcwNTn8fOLN8b3U599XinIlPZBBqNnwZYJFQD0i2dLVdAjszjU-a3Y0iLd5UHOg0H9-IFtS0nGf4MeOGk4NsNNAq-pMpFpi_aZrXHGV7UgoEEOlkFGBW5HOsJFC/s728-e100/zz--header-d.png)](https://thehackernews.uk/zz--header-d)

# [Sneaky 2FA Phishing Kit Adds BitB Pop-ups Designed to Mimic the Browser Address Bar](https://thehackernews.com/2025/11/sneaky-2fa-phishing-kit-adds-bitb-pop.html)

**Nov 18, 2025**Ravie LakshmananBrowser Security / Cybercrime

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiUazxCy3vEGn8LPbdlF5itqaRkz1hHoZICRwrw6N6eOk7fxRbRx1r304KEpLd-LeevEHDIwZ0pLukHppiGlxuU5juewH86IWmXorHFekbgYxQ1R2snVoZE8tqkrFIg4HOu_EaIV5bmVYaad4wUYA2ea9tiqqKaYAfIzj2icwv50ptIREdEy1NS8jPwsLrj/s2600/browser.gif)

The malware authors associated with a Phishing-as-a-Service (PhaaS) kit known as [Sneaky 2FA](https://thehackernews.com/2025/01/new-sneaky-2fa-phishing-kit-targets.html) have incorporated Browser-in-the-Browser (BitB) functionality into their arsenal, underscoring the continued evolution of such offerings and further making it easier for less-skilled threat actors to mount attacks at scale.

Push Security, in a [report](https://pushsecurity.com/blog/analyzing-the-latest-sneaky2fa-phishing-page) shared with The Hacker News, said it observed the use of the technique in phishing attacks designed to steal victims' Microsoft account credentials.

BitB was [first documented](https://thehackernews.com/2022/03/new-browser-in-browser-bitb-attack.html) by security researcher mr.d0x in March 2022, detailing how it's possible to leverage a combination of HTML and CSS code to create fake browser windows that can masquerade as login pages for legitimate services in order to [facilitate credential theft](https://thehackernews.com/2025/04/microsoft-warns-of-tax-themed-email.html).

"BitB is principally designed to mask suspicious phishing URLs by simulating a pretty normal function of in-browser authentication – a pop-up login form," Push Security said. "BitB phishing pages replicate the design of a pop-up window with an iframe pointing to a malicious server."

[![DFIR Retainer Services](data:image/png;base64...)](https://thehackernews.uk/zz--inside-d)

To complete the deception, the pop-up browser window shows a legitimate Microsoft login URL, giving the victim the impression that they are entering the credentials on a legitimate page, when, in reality, it's a phishing page.

In one attack chain observed by the company, users who land on a suspicious URL ("previewdoc[.]us") are served a Cloudflare Turnstile check. Only after the user passes the bot protection check does the attack progress to the next stage, which involves displaying a page with a "Sign in with Microsoft" button in order to view a PDF document.

Once the button is clicked, a phishing page masquerading as a Microsoft login form is loaded in an embedded browser using the BitB technique, ultimately exfiltrating the entered information and session details to the attacker, who can then use them to take over the victim's account.

Besides using bot protection technologies like CAPTCHA and Cloudflare Turnstile to prevent security tools from accessing the phishing pages, the attackers leverage [conditional loading techniques](https://phishing-techniques.pushsecurity.com/techniques/conditional-loading/) to ensure that only the intended targets can access them, while filtering out the rest or redirecting them to benign sites instead.

Sneaky 2FA, first highlighted by Sekoia earlier this year, is known to adopt various methods to resist analysis, including using obfuscation and disabling browser developer tools to prevent attempts to inspect the web pages. In addition, the phishing domains are [quickly rotated](https://www.centripetal.ai/threat-research/typhoon-versus-sneaky) to minimize detection.

"Attackers are continuously innovating their phishing techniques, particularly in the context of an increasingly professionalized PhaaS ecosystem," Push Security said. "With identity-based attacks continuing to be the leading cause of breaches, attackers are incentivized to refine and enhance their phishing infrastructure."

The disclosure comes against the backdrop of research that [found](https://labs.sqrx.com/passkeys-pwned-0dbddb7ade1a) that it's possible to employ a malicious browser extension to fake passkey registration and logins, thereby allowing threat actors to access enterprise apps without the user's device or biometrics.

The Passkey Pwned Attack, as it's called, takes advantage of the fact that there is no secure communication channel between a device and the service and that the browser, which serves as the intermediary, can be manipulated by means of a rogue script or extension, effectively hijacking the authentication process.

When registering or authenticating on websites using passkeys, the website communicates via the web browser by invoking WebAuthn APIs such as navigator.credentials.create() and navigator.credentials.get(). The attack manipulates these flows through JavaScript injection.

"The malicious extension intercepts the call before it reaches the authenticator and generates its own attacker-controlled key pair, which includes a private key and a public key," SquareX said. "The malicious extension stores the attacker-controlled private key locally so it can reuse it to sign future authentication challenges on the victim's device without generating a new key."

[![CIS Build Kits](data:image/png;base64...)](https://thehackernews.uk/endpoint-protect-d)

A copy of the private key is also transmitted to the attacker to permit them to access enterprise apps on their own device. Similarly, during the login phase, the call to "navigator.credentials.get()" is intercepted by the extension to sign the challenge with the attacker's private key created during registration.

That's not all. Threat actors have also found a way to sidestep phishing-resistant authentication methods like passkeys by means of what's known as a downgrade attack, where adversary-in-the-middle (AitM) phishing kits like [Tycoon](https://thehackernews.com/2025/08/attackers-use-fake-oauth-apps-with.html) can ask the victim to choose between a less secure option that's phishable instead of allo...