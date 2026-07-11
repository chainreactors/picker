---
title: Laser Attack Resets Tangem Wallet Passwords on Cards That Can't Be Patched
url: https://thehackernews.com/2026/07/laser-attack-resets-tangem-wallet.html
source: The Hacker News
date: 2026-07-10
fetch_date: 2026-07-11T05:04:36.906828
---

# Laser Attack Resets Tangem Wallet Passwords on Cards That Can't Be Patched

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

# [Laser Attack Resets Tangem Wallet Passwords on Cards That Can't Be Patched](https://thehackernews.com/2026/07/laser-attack-resets-tangem-wallet.html)

**Swati Khandelwal**Jul 10, 2026Vulnerability / Hardware Security

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEh0BbJcQ3TUJxFvOCpAChyC5saD3RGgDCtLtVG-Wupee7poBksO2TzSWFtzQmjjoXuZ-9hnCNR3HuWdSsBv7YZl477fdOcjoOBh72RY4vJ9R0hxUWktV2R7wgTsRa-_Zz5Bj_ZGfQOVT8v292QJ55C9hMumk-IgXd-PVZ6LFu2ZDyCGwjNtJhCYb4W-mPDO/s1700-e365/ll.jpg)

Researchers at **Ledger's Donjon security team** have shown that a precisely timed laser pulse, aimed at the chip inside a **Tangem** crypto wallet card, can reset the card's password to anything the attacker picks.

No old password. No backup card. Once it is reset, whoever did it controls the wallet and can move the coins out.

This is not an emergency for most owners. The attack needs the physical card in hand and a lab that Donjon puts at around $250,000. It also means cutting the card open, which leaves damage no one can miss. It cannot be done over the internet, and there is no fix coming: Tangem cards cannot take software updates, so every card already sold carries the flaw.

The one group that should act now is anyone whose card is lost or stolen and holds serious value.

## How the card is meant to protect you

A Tangem wallet looks like a plain bank card. Tap it to your phone, and a companion app talks to a Samsung S3D232A chip inside. That chip is a secure element, built to resist tampering and certified to a high grade called EAL6+.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/ai-vuln-protection-d)

It holds the secret key that controls your crypto and never lets it out. Two things are meant to stand between a thief and your money: holding the card and knowing the password.

The weak point is the password reset feature. Tangem sells its cards in linked sets, and if you forget your password, you can set a new one by holding two of your cards together. Deep inside that process, the card runs a single check: is this card in recovery mode? If yes, it accepts a new password without asking for the old one.

A laser pulse fired at the chip at the exact moment it runs that check does not quietly rewrite a stored value. It briefly disturbs the chip's own circuitry, so the check misfires and the card behaves as if it were in recovery mode when it is not.

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEh9utbDi4AC6trfMxi55y1ePtHrVUgQ0x3FFT_qZBat3geUfwd86b2JemyGnkdQZe83U2jvCCLQ_64708RjgIKJLnn0w_rrwR8PA53ysZsgcGHGeLWlJ_RMnosW7Tuyh6lrss_Gv0ZyI3Jg1mqoNS0ilSedkA6quK-RdgRrA_bJZwyetOFa4BOnEOHRkYFl/s1700-e365/laaser-flow.png)

With the check defeated, the card's ordinary SetPin command accepts a brand-new password: no old password, no second card, no recovery step. Turning the recovery feature off does not help, because the same check still runs on every card.

## Hard to do, and unfixable

None of this is easy. It took a laser rig, sensitive measuring gear, deep hardware skill, and a long stretch of up-front work to map the chip and find the exact spot and timing. The card has to be cut open and its chip exposed, which leaves obvious damage.

There is no doing this quietly and slipping the card back into a pocket. [Donjon reports](https://donjon.ledger.com/blog/bypassing-tangem-card-security-with-laser-attack/) that once the settings were locked in, the attack worked on every card it tried, at about two hours each. The team reported the flaw to Tangem on February 10, 2026.

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiHkgKEcO0Gmst3f3dNnKIzr1TngAXoqD4U0pZ8MiNV3anl48355NEkvAnFa9sRAJQgI9sVU63NqZoyulRweNx-QzErvw5r14uRieO_7q10eYBGH5hZBNBsLo9JVwT_0I9Ncshwp2QE7n7wzcGliUrQ6261gDmZfATZdkPxEDkzxfPJ7YDhIEwxiHaVp7cp/s1700-e365/laaser-1.jpg)

The bigger problem is permanence. Tangem builds its cards with no way to update the firmware, and presents that as a security feature: nothing can be changed, so nothing can be tampered with from a distance. Here, that same design cuts the other way, leaving a flaw in the code that can never be corrected.

As the researchers put it, "there's no patch, but the attack is physical and invasive", so it cannot be done remotely.

## What Tangem says

Tangem pushed back. In a [public response](https://tangem.com/en/blog/post/lfi-response/), the company called this a lab-only physical method that works against secure element chips in general, not something unique to its cards. It also noted that Donjon belongs to **Ledger**, one of its biggest rivals.

Its sharpest point is about money: a Tangem card carries nothing that says who owns it or how much it holds, so an attacker who spends $250,000 and wrecks cards to tune the attack has no way to tell whether a stolen card is worth $50 or $50 million. Tangem also says no one has lost funds to a laser attack on any hardware wallet so far, and that for everyday users, "the practical risk is virtually non-existent."

Both sides are partly right. Donjon researchers are right that the flaw is real, sits in every card, and can never be patched. Tangem is right that for almost everyone, the cost, the ruined cards, and the guesswork over what a card holds make it pointless.

The place they actually meet is narrow: a lost, stolen, or seized card that an attacker already has reason to think is worth the trouble.

## Not the first wallet chip broken this way

This is not Donjon's only laser attack on a hardware wallet this year. In early June, Trezor and its chip partner Tropic Square [disclosed](https://trezor.io/blog/news/Trezor-response-TROPIC01-chip-disclosure-no-impact-to-your-funds) a related result: Donjon used the same technique, laser fault injection, on the TROPIC01 chip in the new Trezor Safe 7.

This time, it slipped past the chip's firmware signature check to run its own code. Trezor said funds stayed safe bec...