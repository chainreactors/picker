---
title: Jack Dorsey says his ‘secure’ new Bitchat app has not been tested for security
url: https://techcrunch.com/2025/07/09/jack-dorsey-says-his-secure-new-bitchat-app-has-not-been-tested-for-security/
source: Over Security - Cybersecurity news aggregator
date: 2025-07-10
fetch_date: 2025-10-06T23:39:49.211620
---

# Jack Dorsey says his ‘secure’ new Bitchat app has not been tested for security

[![](https://techcrunch.com/wp-content/uploads/2024/09/tc-lockup.svg) TechCrunch Desktop Logo](https://techcrunch.com)

[![](https://techcrunch.com/wp-content/uploads/2024/09/tc-logo-mobile.svg) TechCrunch Mobile Logo](https://techcrunch.com)

* [Latest](/latest/)
* [Startups](/category/startups/)
* [Venture](/category/venture/)
* [Apple](/tag/apple/)
* [Security](/category/security/)
* [AI](/category/artificial-intelligence/)
* [Apps](/category/apps/)
* [Disrupt 2025](https://techcrunch.com/events/tc-disrupt-2025/)

* [Events](/events/)
* [Podcasts](/podcasts/)
* [Newsletters](/newsletters/)

Search

Submit

Site Search Toggle

Mega Menu Toggle

### Topics

[Latest](/latest/)

[AI](/category/artificial-intelligence/)

[Amazon](/tag/amazon/)

[Apps](/category/apps/)

[Biotech & Health](/category/biotech-health/)

[Climate](/category/climate/)

[Cloud Computing](/tag/cloud-computing/)

[Commerce](/category/commerce/)

[Crypto](/category/cryptocurrency/)

[Enterprise](/category/enterprise/)

[EVs](/tag/evs/)

[Fintech](/category/fintech/)

[Fundraising](/category/fundraising/)

[Gadgets](/category/gadgets/)

[Gaming](/category/gaming/)

[Google](/tag/google/)

[Government & Policy](/category/government-policy/)

[Hardware](/category/hardware/)

[Instagram](/tag/instagram/)

[Layoffs](/tag/layoffs/)

[Media & Entertainment](/category/media-entertainment/)

[Meta](/tag/meta/)

[Microsoft](/tag/microsoft/)

[Privacy](/category/privacy/)

[Robotics](/category/robotics/)

[Security](/category/security/)

[Social](/category/social/)

[Space](/category/space/)

[Startups](/category/startups/)

[TikTok](/tag/tiktok/)

[Transportation](/category/transportation/)

[Venture](/category/venture/)

### More from TechCrunch

[Staff](/about-techcrunch/)

[Events](/events/)

[Startup Battlefield](/startup-battlefield/)

[StrictlyVC](https://strictlyvc.com/)

[Newsletters](/newsletters/)

[Podcasts](/podcasts/)

[Videos](/video/)

[Partner Content](/sponsored/)

[TechCrunch Brand Studio](/brand-studio/)

[Crunchboard](https://www.crunchboard.com/)

[Contact Us](/contact-us/)

![Jack Dorsey, co-founder and chief executive officer of Twitter Inc. and Square Inc., listens during the Bitcoin 2021 conference in Miami, Florida, U.S., on Friday, June 4, 2021.](https://techcrunch.com/wp-content/uploads/2025/07/jack-dorsey-bitcoin-2021-conference.jpg?w=1024)

**Image Credits:**Eva Marie Uzcategui/Bloomberg / Getty Images

[Security](https://techcrunch.com/category/security/)

# Jack Dorsey says his ‘secure’ new Bitchat app has not been tested for security

[Lorenzo Franceschi-Bicchierai](https://techcrunch.com/author/lorenzo-franceschi-bicchierai/)

11:37 AM PDT · July 9, 2025

On Sunday, Block CEO and Twitter co-founder Jack Dorsey [launched an open source chat app called Bitchat](https://techcrunch.com/2025/07/07/jack-dorsey-working-on-bluetooth-messaging-app-bitchat/), [promising](https://github.com/jackjackbits/bitchat/blob/main/WHITEPAPER.md#:~:text=secure%2C%20private%20messaging) to deliver “secure” and “private” messaging without a centralized infrastructure.

The app relies on Bluetooth and end-to-end encryption, unlike traditional messaging apps that rely on the internet. By being decentralized, Bitchat has potential for being a secure app in high-risk environments where the internet is monitored or inaccessible. According to Dorsey’s [white paper](https://github.com/jackjackbits/bitchat/blob/main/WHITEPAPER.md#encryption-and-security) detailing the app’s protocols and privacy mechanisms, Bitchat’s system design “prioritizes” security.

But the claims that the app is secure, however, are already facing scrutiny by security researchers, given that the app and its code have not been reviewed or tested for security issues at all — by Dorsey’s own admission.

Since launching, Dorsey has [added a warning](https://github.com/jackjackbits/bitchat/commit/d296f1d6a4ff8ee60c5c15d19e9178a244cf3e5c) to Bitchat’s GitHub page: “This software has not received external security review and may contain vulnerabilities and does not necessarily meet its stated security goals. Do not use it for production use, and do not rely on its security whatsoever until it has been reviewed.”

This warning now also appears on Bitchat’s main GitHub project page but was not there at the time the app debuted.

As of Wednesday, Dorsey [added](https://github.com/jackjackbits/bitchat/commit/ad3afab943efac33505e247e5567a17e5d4c6b90#diff-b335630551682c19a781afebcf4d07bf978fb1f8ac04c6bf87428ed5106870f5L5): “Work in progress,” next to the warning on GitHub.

This latest disclaimer came after security researcher Alex Radocea found that it’s possible to impersonate someone else and trick a person’s contacts into thinking they are talking to the legitimate contact, [as the researcher explained in a blog post](https://www.supernetworks.org/pages/blog/agentic-insecurity-vibes-on-bitchat).

Techcrunch event

### Join 10k+ tech and VC leaders for growth and connections at Disrupt 2025

#### Netflix, Box, a16z, ElevenLabs, Wayve, Hugging Face, Elad Gil, Vinod Khosla — just some of the 250+ heavy hitters leading 200+ sessions designed to deliver the insights that fuel startup growth and sharpen your edge. Don’t miss the 20th anniversary of TechCrunch, and a chance to learn from the top voices in tech. **Grab your ticket before doors open to save up to $444.**

### Join 10k+ tech and VC leaders for growth and connections at Disrupt 2025

#### Netflix, Box, a16z, ElevenLabs, Wayve, Hugging Face, Elad Gil, Vinod Khosla — just some of the 250+ heavy hitters leading 200+ sessions designed to deliver the insights that fuel startup growth and sharpen your edge. Don’t miss a chance to learn from the top voices in tech. **Grab your ticket before doors open to save up to $444.**

San Francisco
|
October 27-29, 2025

[**REGISTER NOW**](https://techcrunch.com/events/tc-disrupt-2025/?utm_source=tc&utm_medium=ad&utm_campaign=disrupt2025&utm_content=ticketsales&promo=tc_inline_lb&display=)

Radocea wrote that Bitchat has a “broken identity authentication/verification” system that allows an attacker to intercept someone’s “identity key” and “peer id pair” — essentially a digital handshake that is supposed to establish a trusted connection between two people using the app. Bitchat calls these “Favorite” contacts and marks them with a star icon. The goal of this feature is to allow two Bitchat users to interact, knowing that they are talking to the same person they talked to before.

Dorsey did not respond to TechCrunch’s request for comment sent to his Block email address.

![](https://techcrunch.com/wp-content/uploads/2025/07/bitchat-aitm-alice-bob.png?w=680)

A screenshot showing an example of a chat where an attacker has impersonated “Bob” in a chat with “Alice,” which Bitchat made it seem like it was really coming from Bob.**Image Credits:**Alex Radocea

On Monday, Radocea filed a ticket on the GitHub project to ask how to report the security flaw he discovered in the Bitchat Favorites system. Soon after, Dorsey marked it as “completed,” without comment. ([Dorsey reopened the ticket](https://github.com/jackjackbits/bitchat/issues/19) on Wednesday, saying security issues can be reported by posting on GitHub directly.)

Another person [reported](https://github.com/jackjackbits/bitchat/issues/78) concerns with Dorsey’s claims that Bitchat has “forward secrecy,” a cryptographic technique that ensures that even if an attacker steals or compromises an encryption key, that attacker still cannot decrypt previously sent messages.

Someone also [pointed out](https://github.com/jackjackbits/bitchat/pull/96) a potential buffer overflow bug, which is a common type of security vulnerability where a hacker can force a device’s memory to spill out to other locations, opening the door for a data compromise.

Radocea warned that Bitchat users should not trust the app yet.

“Security is a great feature to have for going viral. But a basic sanity che...