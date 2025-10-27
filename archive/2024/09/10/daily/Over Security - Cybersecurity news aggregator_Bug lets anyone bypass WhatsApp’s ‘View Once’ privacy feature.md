---
title: Bug lets anyone bypass WhatsApp’s ‘View Once’ privacy feature
url: https://techcrunch.com/2024/09/09/bug-lets-anyone-bypass-whatsapps-view-once-privacy-feature/
source: Over Security - Cybersecurity news aggregator
date: 2024-09-10
fetch_date: 2025-10-06T18:29:52.291238
---

# Bug lets anyone bypass WhatsApp’s ‘View Once’ privacy feature

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

![The WhatsApp logo on a burning piece of paper.](https://techcrunch.com/wp-content/uploads/2024/09/whatsapp-view-once-media-feature-illustration.jpg?w=1024)

**Image Credits:**Simonkr / Getty Images

[Security](https://techcrunch.com/category/security/)

# Bug lets anyone bypass WhatsApp’s ‘View Once’ privacy feature

[Lorenzo Franceschi-Bicchierai](https://techcrunch.com/author/lorenzo-franceschi-bicchierai/)

7:16 AM PDT · September 9, 2024

WhatsApp, the most popular end-to-end encrypted messaging app in the world [with more than two billion users](https://techcrunch.com/2024/07/25/mark-zuckerberg-says-whatsapp-has-100-million-daily-active-users-in-the-u-s/), allows users to exchange pictures and videos that disappear soon after opening.

But a bug in how WhatsApp implements its so-called “View Once” feature in its browser-based web app allows any malicious recipient to display and save the picture and video, which should vanish immediately after being viewed.

The “[View Once](https://faq.whatsapp.com/578442220724722/?cms_platform=android)” feature is designed to work only on WhatsApp’s mobile apps on Android and iOS. WhatsApp [rolled out the feature in 2021](https://techcrunch.com/2021/08/03/whatsapp-view-once-disappearing-photos-video/).

In typical circumstances, when a user receives a “View Once” picture or video while using WhatsApp on the desktop app or on the web app, the user will see a warning that the picture or video can only be opened using WhatsApp on their phone.

![](https://techcrunch.com/wp-content/uploads/2024/09/WhatsApp-View-Once-Warning.png)

The warning that WhatsApp displays on its desktop app and web app when a user receives a “View Once” media. **Image Credits:**TechCrunch/screenshot

As an added privacy protection, WhatsApp prevents users from taking screenshots or screen recordings of “View Once” pictures and videos in its Android and iOS apps.

![](https://techcrunch.com/wp-content/uploads/2024/09/whatsapp-screenshot-blocked.png?w=314)

The warning that WhatsApp displays on its mobile apps when a user tries to take a screenshot of a “View Once” picture or video. **Image Credits:**TechCrunch/screenshot

Tal Be’ery, a [security researcher who has been researching WhatsApp privacy issues for several months](https://techcrunch.com/2024/01/17/psa-whatsapp-number-desktop-computer/), recently discovered the bug. On Monday, [Be’ery published a blog post detailing his findings](https://zengo.com/whatsapps-view-once-privacy-issue/).

Be’ery provided TechCrunch with a live demo of the bug last week, in which he showed he was able to capture and save a copy of a picture that TechCrunch sent as “View Once,” while he was using WhatsApp on the web.

Techcrunch event

### Join 10k+ tech and VC leaders for growth and connections at Disrupt 2025

#### Netflix, Box, a16z, ElevenLabs, Wayve, Hugging Face, Elad Gil, Vinod Khosla — just some of the 250+ heavy hitters leading 200+ sessions designed to deliver the insights that fuel startup growth and sharpen your edge. Don’t miss the 20th anniversary of TechCrunch, and a chance to learn from the top voices in tech. **Grab your ticket before doors open to save up to $444.**

### Join 10k+ tech and VC leaders for growth and connections at Disrupt 2025

#### Netflix, Box, a16z, ElevenLabs, Wayve, Hugging Face, Elad Gil, Vinod Khosla — just some of the 250+ heavy hitters leading 200+ sessions designed to deliver the insights that fuel startup growth and sharpen your edge. Don’t miss a chance to learn from the top voices in tech. **Grab your ticket before doors open to save up to $444.**

San Francisco
|
October 27-29, 2025

[**REGISTER NOW**](https://techcrunch.com/events/tc-disrupt-2025/?utm_source=tc&utm_medium=ad&utm_campaign=disrupt2025&utm_content=ticketsales&promo=tc_inline_lb&display=)

“The only thing that is worse than no privacy, is a false sense of privacy in which users are led to believe some forms of communication are private when in fact they are not,” said Be’ery, who is the CTO and co-founder of crypto wallet Zengo, [in his blog post](https://zengo.com/whatsapps-view-once-privacy-issue/). “Currently, WhatsApp’s ‘View Once’ is a blunt form of false privacy and should either be thoroughly fixed or abandoned,” wrote Be’ery.

#### Contact Us

Do you have more information about bugs in WhatsApp or other messaging apps? From a non-work device, you can contact Lorenzo Franceschi-Bicchierai securely on Signal at +1 917 257 1382, or via Telegram and Keybase @lorenzofb, or email. You also can contact TechCrunch via [SecureDrop](https://techcrunch.com/got-a-tip/).

Be’ery reported the bug to WhatsApp’s parent company Meta through its official bug bounty platform on August 26.

In response to TechCrunch’s request for comment last week, and days after Be’ery filed his bug report, WhatsApp spokesperson Zade Alsawah sent a statement: “We are already in the process of rolling out updates to view once on web. We continue to encourage users to only send view once messages to people they know and trust.”

Be’ery is not the first person to find out about this bug. Be’ery and TechCrunch saw posts promoting multiple browser extensions that make it trivially easy to bypass the “View Once” feature while using WhatsApp’s web app. TechCrunch has also seen active discussions on how to bypass the feature on social media. TechCrunch is not linking to the posts as to not aid malicious actors in exploiting the bug.

WhatsApp did not provide a timeline for when it plans to complete its updates to View Once.

Topics

[Exclusive](https://techcrunch.com/tag/exclusive/), [Meta](https://techcrunch.com/tag/meta/), [Privacy](https://techcrunch.com/category/privacy/), [privacy](https://techcrunch.com/tag/privacy/), [Security](https://techcrunch.com/category/security/), [WhatsApp](https://techcrunch.com/tag/whatsapp/)

![Lorenzo Franceschi-Bicchierai](https://tech...