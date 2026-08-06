---
title: PSA: Apple’s Private Relay can leak your real IP address
url: https://techcrunch.com/2026/08/05/psa-apples-private-relay-can-leak-your-real-ip-address/
source: Over Security
date: 2026-08-05
fetch_date: 2026-08-06T05:02:37.928787
---

# PSA: Apple’s Private Relay can leak your real IP address

–:–:–:–

🚨 Flash Sale 🚨 [Get $100 off your Disrupt 2026 ticket](https://techcrunch.com/events/techcrunch-disrupt/tickets/?utm_source=tc&utm_medium=post&utm_campaign=disrupt2026&utm_content=ticketsales&promo=augflash&display=TR)

Get $400 off your Disrupt 2026 ticket: **[REGISTER NOW.](https://techcrunch.com/events/techcrunch-disrupt/tickets/?utm_source=tc&utm_medium=post&utm_campaign=disrupt2026&utm_content=ticketsales&promo=augflash&display=TRUE)**

Close

[![](https://techcrunch.com/wp-content/uploads/2026/05/tc-lockup-hp.svg) TechCrunch Desktop Logo](https://techcrunch.com)

[![](https://techcrunch.com/wp-content/uploads/2024/09/tc-logo-mobile.svg) TechCrunch Mobile Logo](https://techcrunch.com)

* [Latest](/latest/)
* [Startups](/category/startups/)
* [Venture](/category/venture/)
* [Apple](/tag/apple/)
* [Security](/category/security/)
* [AI](/category/artificial-intelligence/)
* [Apps](/category/apps/)
* [Disrupt 2026](https://techcrunch.com/events/techcrunch-disrupt/)

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

![Safari logo, Apple](https://techcrunch.com/wp-content/uploads/2024/11/GettyImages-1237753209.jpg?w=1024)

**Image Credits:**Pavlo Gonchar/SOPA Images/LightRocket / Getty Images

[Security](https://techcrunch.com/category/security/)

# PSA: Apple’s Private Relay can leak your real IP address

[Lorenzo Franceschi-Bicchierai](https://techcrunch.com/author/lorenzo-franceschi-bicchierai/)

9:52 AM PDT · August 5, 2026

Apple’s Private Relay, an opt-in feature designed to hide a user’s IP address when they browse the internet with Safari, can be circumvented to reveal the supposedly hidden IP address due to a series of flaws.

Researchers revealed the issues [in a blog post](https://mysk.blog/2026/08/04/webkit-proxy-icloud-private-relay-ip-leak/) on Tuesday. The researchers also [set up a website](https://leaks.psylo.app/) where anyone can check if their real IP address leaks, even if they use [Private Relay](https://support.apple.com/en-us/102602). In a test on Tuesday, TechCrunch verified that the site was able to reveal our real IP address.

The issue [was first reported](https://www.404media.co/apples-private-relay-is-exposing-users-real-ip-addresses/) by 404 Media.

Talal Haj Bakry and Tommy Mysk, the researchers who found the issue, wrote in their blog post that the problem lies with three features in Apple’s web browser engine WebKit, which is used by all browsers in iOS. Private Relay is [only available to iCloud+ subscribers](https://techcrunch.com/2021/06/07/apple-announces-icloud-with-privacy-focused-features/), and is not like a Virtual Private Network, or VPN, which protects someone’s IP address at the system level. Private Relay only works while using Safari.

Mysk [wrote in a post on X](https://x.com/mysk_co/status/2085026605529768261) that they chose not to report the issue to Apple because “our past experience with Apple tells us that reporting this issue would involve months of delays, inconsistent communication, and in some cases, denying the issue’s impact entirely.”

Apple did not immediately respond to a request for comment.

Mysk and his colleagues develop a private browser called Psylo, which they say now has mitigations that prevent users’ IP addresses from leaking when using Psylo.

Topics

[Apple](https://techcrunch.com/tag/apple/), [iCloud](https://techcrunch.com/tag/icloud/), [iCloud Private Relay](https://techcrunch.com/tag/icloud-private-relay/), [iOS](https://techcrunch.com/tag/ios/), [privacy](https://techcrunch.com/tag/privacy/), [safari](https://techcrunch.com/tag/safari/), [Security](https://techcrunch.com/category/security/)

*When you purchase through links in our articles, [we may earn a small commission](https://techcrunch.com/techcrunch-affiliate-monetization-standards/). This doesn’t affect our editorial independence.*

![Lorenzo Franceschi-Bicchierai](https://techcrunch.com/wp-content/uploads/2025/07/Lorenzo-headshot-2023-cropped.jpeg?w=150)

Lorenzo Franceschi-Bicchierai

Senior Reporter, Cybersecurity

Lorenzo Franceschi-Bicchierai is a Senior Writer at TechCrunch, where he covers hacking, cybersecurity, surveillance, and privacy.

You can contact or verify outreach from Lorenzo by emailing lorenzo@techcrunch.com, via encrypted message at +1 917 257 1382 on Signal, and @lorenzofb on Keybase/Telegram.

[View Bio](https://techcrunch.com/author/lorenzo-franceschi-bicchierai/)

![Event Logo](https://techcrunch.com/wp-content/uploads/2025/04/Disrupt2026-Color.png)

October 13 – 15

San Francisco

Scale faster. Grow your portfolio. Gain practical expertise. No matter your goal, Disrupt can empower you.

**Save up to $330 toda**y!

[**REGISTER NOW**](https://techcrunch.com/events/tc-disrupt-2026/?utm_source=tc&utm_medium=ad&utm_campaign=disrupt2026&utm_content=ticketsales&promo=rightrail_disrupt2025_rb&display=)

## Most Popular

* ### [Bending Spoons to buy Airtable for $1.28B](https://techcrunch.com/2026/08/04/bending-spoons-to-buy-airtable-for-1-28b/)

  + [Ivan Mehta](https://techcrunch.com/author/ivan-mehta/)
* ### [Influencers draw backlash for attending OpenAI’s first luxury trip](https://techcrunch.com/2026/08/03/influencers-draw-backlash-for-attending-openais-first-luxury-trip/)

  + [Dominic-Madori Davis](https://techcrunch.com/author/dominic-madori-davis/)
* ### [Sequoia’s Shaun Maguire leads $1B round for nuclear startup Valar Atomics](https://techcrunch.com/2026/08/03/sequoias-shaun-maguire-leads-1b-round-for-nuclear-startup-valar-atomics/)

  + [Julie Bort](https://techcrunch.com/author/julie-bort/)
* ### [Malaysia is reportedly shutting down Balaji Srinivasan’s Network School](https://techcrunch.com/2026/08/02/malaysia-is-reportedly-shutting-down-balaji-srinivasans-network-school/)

  + [Anthony Ha](https://techcrunch.com/author/anthony-ha/)
* ### [YouTuber Hank Green says his AI usage is ‘not healthy’](https://techcrunch.com/2026/08/01/youtuber-hank-green-says-his-ai-usage-is-not-healthy/)

  + [Anthony Ha](https://techcrunch.com/author/anthony-ha/)
* ### [VC-backed startups commit more fraud, and researchers think they know why](https://techcrunch.com/2026/07/31/vc-backed-startups-commit-more-fraud-and-researchers-think-they-know-why/)

  + [Dominic-Madori Davis](https://techcrunch.com/author/dominic-madori-davis/)
* ### [WhatsApp is testing a new folder for messages from large businesses](https://techcrunch.com/2026/07/31/whatsapp-is-testing-a-new-folder-for-messages-from-large-business...