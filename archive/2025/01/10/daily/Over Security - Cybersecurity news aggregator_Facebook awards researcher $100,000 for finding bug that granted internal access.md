---
title: Facebook awards researcher $100,000 for finding bug that granted internal access
url: https://techcrunch.com/2025/01/09/facebook-awards-researcher-100000-for-finding-bug-that-granted-internal-access/
source: Over Security - Cybersecurity news aggregator
date: 2025-01-10
fetch_date: 2025-10-06T20:10:42.763722
---

# Facebook awards researcher $100,000 for finding bug that granted internal access

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

![An illustrations showing three broken Facebook logos.](https://techcrunch.com/wp-content/uploads/2019/10/Libra-Association-Broken-Up.png?w=1024)

**Image Credits:**Bryce Durbin / TechCrunch

[Security](https://techcrunch.com/category/security/)

# Facebook awards researcher $100,000 for finding bug that granted internal access

[Lorenzo Franceschi-Bicchierai](https://techcrunch.com/author/lorenzo-franceschi-bicchierai/)

9:48 AM PST · January 9, 2025

In October 2024, security researcher [Ben Sadeghipour](https://x.com/NahamSec) was analyzing Facebook’s ad platform when he found a security vulnerability that allowed him to run commands on the internal Facebook server housing that platform, essentially giving him control of the server.

After he reported the vulnerability to Facebook’s owner Meta, which Sadeghipour said took just one hour to fix it, the social networking giant awarded him $100,000 in a bug bounty payout.

“My assumption is that it’s something you may want to fix because it is directly inside of your infrastructure,” Sadeghipour wrote in the report he sent to Meta, he told TechCrunch. Meta responded to his report, telling Sadeghipour to “refrain from testing any further” while they fix the vulnerability.

The issue, according to Sadeghipour, was that one of the servers that Facebook used for creating and delivering ads was vulnerable to a previously fixed flaw found in the Chrome browser, which Facebook uses in its ads system. Sadeghipour said this unpatched bug allowed him to hijack it using a headless Chrome browser (essentially a version of the browser that users run from the computer’s terminal) to interact directly with Facebook’s internal servers.

Sadeghipour, who found the Facebook vulnerability working with independent researcher Alex Chapman, told TechCrunch that online advertising platforms make for juicy targets because, “there’s so much that happens in the background of making these ‘ads’ — whether they are video, text, or images.”

“But at the core of it all it’s a bunch of data being processed on the server-side and it opens up the door for a ton of vulnerabilities,” said Sadeghipour.

The researcher said he didn’t test out everything he could have done once inside the Facebook server, but “what makes this dangerous is this was probably a part of an internal infrastructure.”

Techcrunch event

### Join 10k+ tech and VC leaders for growth and connections at Disrupt 2025

#### Netflix, Box, a16z, ElevenLabs, Wayve, Hugging Face, Elad Gil, Vinod Khosla — just some of the 250+ heavy hitters leading 200+ sessions designed to deliver the insights that fuel startup growth and sharpen your edge. Don’t miss the 20th anniversary of TechCrunch, and a chance to learn from the top voices in tech. **Grab your ticket before doors open to save up to $444.**

### Join 10k+ tech and VC leaders for growth and connections at Disrupt 2025

#### Netflix, Box, a16z, ElevenLabs, Wayve, Hugging Face, Elad Gil, Vinod Khosla — just some of the 250+ heavy hitters leading 200+ sessions designed to deliver the insights that fuel startup growth and sharpen your edge. Don’t miss a chance to learn from the top voices in tech. **Grab your ticket before doors open to save up to $444.**

San Francisco
|
October 27-29, 2025

[**REGISTER NOW**](https://techcrunch.com/events/tc-disrupt-2025/?utm_source=tc&utm_medium=ad&utm_campaign=disrupt2025&utm_content=ticketsales&promo=tc_inline_lb&display=)

“Since we have code execution, we could’ve interacted with any of the sites within that infrastructure,” said Sadeghipour. “With an [[remote code execution](https://techcrunch.com/2024/12/23/techcrunch-reference-guide-to-security-terminology/#arbitrary-code-execution) vulnerability], you can bypass some of these limitations and also directly pull stuff from the server itself and the other machines that it has access to.”

Meta spokesperson Nicole Catalano acknowledged receipt of TechCrunch’s request for comment, but did not comment by press time.

Sadeghipour also said that similar ad platforms that other companies run, and which he has been analyzing, are vulnerable to similar vulnerabilities.

Topics

[Ads](https://techcrunch.com/tag/ads/), [bug bounty](https://techcrunch.com/tag/bug-bounty/), [bugs](https://techcrunch.com/tag/bugs/), [cybersecurity](https://techcrunch.com/tag/cybersecurity/), [Exclusive](https://techcrunch.com/tag/exclusive/), [Facebook](https://techcrunch.com/tag/facebook/), [hacking](https://techcrunch.com/tag/hacking/), [infosec](https://techcrunch.com/tag/infosec/), [Meta](https://techcrunch.com/tag/meta/), [Security](https://techcrunch.com/category/security/), [security vulnerability](https://techcrunch.com/tag/security-vulnerability/), [vulnerability](https://techcrunch.com/tag/vulnerability/)

![Lorenzo Franceschi-Bicchierai](https://techcrunch.com/wp-content/uploads/2025/07/Lorenzo-headshot-2023-cropped.jpeg?w=150)

Lorenzo Franceschi-Bicchierai

Senior Reporter, Cybersecurity

Lorenzo Franceschi-Bicchierai is a Senior Writer at TechCrunch, where he covers hacking, cybersecurity, surveillance, and privacy.

You can contact or verify outreach from Lorenzo by emailing lorenzo@techcrunch.com, via encrypted message at +1 917 257 1382 on Signal, and @lorenzofb on Keybase/Telegram.

[View Bio](https://techcrunch.com/author/lorenzo-franceschi-bicchierai/)

![Event Logo](https://techcrunch.com/wp-content/uploads/2025/07/TC25_Disrupt-Color.png)

October 27-29, 2025

San Francisco

**Founders:** Your next big connection and investor are here**.**

**Investors:** Meet startups that align with your investment goals.

**Innovators & Visionaries:** See the future of tech before everyone else.

**Register now and save up to $444 (or up to 30% on groups).**

[**Register Now**](https://techcrunch.com/events/tc-disrupt-2025/?utm_source=tc&utm_medium=ad&utm_campaign=disrupt2025&utm_content=ticketsales&...