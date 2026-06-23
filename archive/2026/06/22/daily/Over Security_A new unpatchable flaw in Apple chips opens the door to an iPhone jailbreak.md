---
title: A new unpatchable flaw in Apple chips opens the door to an iPhone jailbreak
url: https://techcrunch.com/2026/06/22/a-new-unpatchable-flaw-in-apple-chips-opens-the-door-to-an-iphone-jailbreak/
source: Over Security
date: 2026-06-22
fetch_date: 2026-06-23T06:07:53.901035
---

# A new unpatchable flaw in Apple chips opens the door to an iPhone jailbreak

–:–:–:–

The first StrictlyVC of 2026 hits SF on April 30. Tickets are going fast. [Register now.](https://techcrunch.com/events/strictlyvc-san-francisco-2026/?utm_source=tc&utm_medium=ad&utm_campaign=svcsf2026&utm_content=ticketsales&promo=topbanner&display=)

[Founder Summit](https://techcrunch.com/events/techcrunch-founder-summit-2026/?utm_source=tc&utm_medium=ad&utm_campaign=tcfoundersummit2026&utm_content=eb&promo=tc_eventtimer&display=) ticket savings of up to $190 end June 26. Join 1,000+ founders and VCs for all-day bootcamp. **[REGISTER NOW.](https://techcrunch.com/events/techcrunch-founder-summit-2026/?utm_source=tc&utm_medium=ad&utm_campaign=tcfoundersummit2026&utm_content=eb&promo=tc_eventtimer&display=)**

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

![A Apple Lightning port charging cable is seen with with an iPhone.](https://techcrunch.com/wp-content/uploads/2026/06/iphone-usb-cable.jpg?w=1024)

**Image Credits:**STR/NurPhoto / Getty Images

[Security](https://techcrunch.com/category/security/)

# A new unpatchable flaw in Apple chips opens the door to an iPhone jailbreak

[Lorenzo Franceschi-Bicchierai](https://techcrunch.com/author/lorenzo-franceschi-bicchierai/)

11:50 AM PDT · June 22, 2026

A company that sells spyware and hacking tools to government agencies has published details of a vulnerability in Apple chips that can potentially help hackers unlock older iPhones.

This release opens the door for other researchers who specialize in finding iOS vulnerabilities, such as those working for governments or their contractors, to develop effective hacks for iPhones, provided they can find additional vulnerabilities to chain together with this one. This could help security researchers develop a so-called iPhone jailbreak, a technique to hack into Apple’s mobile operating system and remove all the restrictions the company puts on it.

The release is also a reminder that while Apple has made iPhones extremely hard to hack, there are and will always be vulnerabilities that sophisticated hackers can take advantage of to break in.

On Friday, Paradigm Shift, [an offensive cybersecurity company based in Barcelona](http://techcrunch.com/2025/01/13/how-barcelona-became-an-unlikely-hub-for-spyware-startups/), published [a blog post](https://ps.tc/pages/blog-usbliter8.html) about the vulnerability, which it dubbed “usbliter8.” The company also [published a proof of concept](https://ps.tc/pages/blog-usbliter8.html) that shows how to exploit the vulnerability, which requires physical access to the target phone.

The flaw and related exploit affect iPhones that have Apple-made chips A12 and A13, which were released in 2018 and 2019, and are included in older iPhones such as the XS, XR and up to the iPhone 11.

The release of usbliter8 is significant in the world of security research and spyware and hacking tools’ makers, but it does not mean that older iPhones are easily hackable by anyone.

The bug found by Paradigm Shift affects the [iPhone’s Boot ROM](https://support.apple.com/guide/security/boot-process-for-ipad-and-iphone-devices-secb3000f149/web), which is the first piece of code that runs when an iPhone is turned on and, consequently, its first line of defense against hackers. To hack an iPhone with physical access to it — meaning having the ability to connect a cable to it — hackers need to first exploit the Boot ROM. Now, they can do that thanks to usbliter8, which allows them to potentially defeat and bypass further security checks.

Paradigm Shift wrote in its blog that “as these vulnerabilities reside in immutable code, affected users should be aware that migrating to newer hardware remains the most effective mitigation.”

In other words, given that the Boot ROM is burned into the chip, it can’t be changed and flaws in it cannot be patched.

Generally speaking, companies that sell systems to hack iPhones seized by authorities, such as [Cellebrite](https://techcrunch.com/tag/cellebrite/) and [Magnet Forensics](https://techcrunch.com/2025/09/18/ice-unit-signs-new-3-million-contract-for-phone-hacking-tech/) need, and likely already have at their disposal, techniques similar to usbliter8 to break into iPhones. However, hackers still need to incorporate other techniques to access the user data stored in the phone.

Public iPhone jailbreaks [were relatively widespread in the past](https://www.vice.com/en/article/iphone-jailbreak-life-death-legacy/), but they have become rarer in the last decade. Jailbreaking an iPhone is often the first step to research other vulnerabilities on the system. Researchers — intent on [finding valuable iPhone flaws](https://www.vice.com/en/article/iphone-bugs-are-too-valuable-to-report-to-apple/) and ways to exploit them — have few incentives to release that information publicly, because that would lead to Apple fixing the flaws and setting the researchers back.

Paradigm Shift did not respond to a series of questions related to usbliter8.

Topics

[Apple](https://techcrunch.com/tag/apple/), [Cellebrite](https://techcrunch.com/tag/cellebrite/), [cybersecurity](https://techcrunch.com/tag/cybersecurity/), [Graykey](https://techcrunch.com/tag/graykey/), [hackers](https://techcrunch.com/tag/hackers/), [hacking](https://techcrunch.com/tag/hacking/), [iPhone](https://techcrunch.com/tag/iphone/), [iphone jailbreak](https://techcrunch.com/tag/iphone-jailbreak/), [jailbreak](https://techcrunch.com/tag/jailbreak/), [Security](https://techcrunch.com/category/security/), [Spyware](https://techcrunch.com/tag/spyware/)

*When you purchase through links in our articles, [we may earn a small commission](https://techcrunch.com/techcrunch-affiliate-monetization-standards/). This doesn’t affect our editorial independence.*

![Lorenzo Franceschi-Bicchierai](https://techcrunch.com/wp-content/uploads/2025/07/Lorenzo-headshot-2023-cropped.jpeg?w=150)

Lorenzo Franceschi-Bicchierai

Senior Reporter, Cybersecurity
...