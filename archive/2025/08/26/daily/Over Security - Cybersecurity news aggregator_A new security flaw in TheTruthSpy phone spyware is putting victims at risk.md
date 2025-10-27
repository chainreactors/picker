---
title: A new security flaw in TheTruthSpy phone spyware is putting victims at risk
url: https://techcrunch.com/2025/08/25/a-new-security-flaw-in-thetruthspy-phone-spyware-is-putting-victims-at-risk/
source: Over Security - Cybersecurity news aggregator
date: 2025-08-26
fetch_date: 2025-10-07T00:49:31.548902
---

# A new security flaw in TheTruthSpy phone spyware is putting victims at risk

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

![an illustration of a laptop computer and a Texas driver's license on a colorful blue, red, and teal background](https://techcrunch.com/wp-content/uploads/2023/07/thetruthspy-2-hero-image.jpg?w=1024)

**Image Credits:**Bryce Durbin / TechCrunch

[Security](https://techcrunch.com/category/security/)

# A new security flaw in TheTruthSpy phone spyware is putting victims at risk

[Zack Whittaker](https://techcrunch.com/author/zack-whittaker/)

[Lorenzo Franceschi-Bicchierai](https://techcrunch.com/author/lorenzo-franceschi-bicchierai/)

10:27 AM PDT · August 25, 2025

A stalkerware maker with a history of multiple data leaks and breaches now has a critical security vulnerability that allows anyone to take over any user account and steal their victim’s sensitive personal data, TechCrunch has confirmed.

Independent security researcher Swarang Wade found the vulnerability, which allows anyone to reset the password of any user of the stalkerware app [TheTruthSpy](https://techcrunch.com/tag/thetruthspy/) and its many companion Android spyware apps, leading to the hijacking of any account on the platform. Given the nature of TheTruthSpy, it’s likely that many of its customers are operating it without the consent of their targets, who are unaware that their phone data is being siphoned off to somebody else.

This basic flaw shows, once again, that makers of consumer spyware such as TheTruthSpy — and its many competitors — cannot be trusted with anyone’s data. These surveillance apps not only facilitate illegal spying, often by abusive romantic partners, but they also have shoddy security practices that expose the personal data of both victims and perpetrators.

To date, TechCrunch has counted [at least 26 spyware operations that’ve leaked, exposed, or otherwise spilled data](https://techcrunch.com/2025/02/20/hacked-leaked-exposed-why-you-should-stop-using-stalkerware-apps/) in recent years. By our count, this is at least the fourth security lapse involving TheTruthSpy.

TechCrunch verified the vulnerability by providing the researcher with the username of several test accounts. The researcher quickly changed the passwords on the accounts. Wade attempted to contact the owner of TheTruthSpy to alert him of the flaw, but he did not receive any response.

When contacted by TechCrunch, the spyware operation’s director Van (Vardy) Thieu said the source code was “lost” and he cannot fix the bug.

As of publication, the vulnerability still exists and presents a significant risk to the thousands of people whose phones are believed to be unknowingly compromised by TheTruthSpy’s spyware.

Given the risk to the general public, we’re not describing the vulnerability in more detail so as to not aid malicious actors.

## A brief history of TheTruthSpy’s many security flaws

TheTruthSpy is a prolific spyware operation with roots that go back almost a decade. For a time, the spyware network was one of the largest known phone surveillance operations on the web.

TheTruthSpy is developed by 1Byte Software, [a Vietnam-based spyware maker](https://techcrunch.com/2022/02/22/stalkerware-network-spilling-data/) run by Thieu, its director. TheTruthSpy is one of a fleet of near-identical Android spyware apps with different branding, including [Copy9](https://www.vice.com/en/article/xnore-copy9-stalkerware-data-breach-thousands-victims/), and since-defunct brands iSpyoo, MxSpy, and others. The spyware apps share the same back-end dashboards that TheTruthSpy’s customers use to access their victim’s stolen phone data.

As such, the security bugs in TheTruthSpy also affect customers and victims of any branded or whitelabeled spyware app that relies on TheTruthSpy’s underlying code.

As part of an investigation into the stalkerware industry in 2021, [TechCrunch found that TheTruthSpy had a security bug](https://techcrunch.com/2022/02/22/stalkerware-network-spilling-data/) that was exposing the private data of its 400,000 victims to anyone on the internet. The exposed data included the victims’ most personal information, including their private messages, photos, call logs, and their historical location data.

TechCrunch later received a cache of files from TheTruthSpy’s servers, exposing the inner workings of the spyware operation. The files also contained a list of every Android device compromised by TheTruthSpy or one of its companion apps. While the list of devices did not contain enough information to personally identify each victim, it allowed [TechCrunch to build a spyware lookup tool for any potential victim to check](https://techcrunch.com/pages/thetruthspy-investigation/) whether their phone was found in the list.

Our subsequent reporting, based on hundreds of leaked documents from 1Byte’s servers sent to TechCrunch, revealed that [TheTruthSpy relied on a massive money-laundering operation](https://techcrunch.com/2023/07/20/thetruthspy-stalkerware-forged-passports-millions/) that used forged documents and false identities to skirt restrictions put in place by credit card processors on spyware operations. The scheme allowed TheTruthSpy to funnel millions of dollars of illicit customer payments into bank accounts around the world controlled by its operators.

In late 2023, TheTruthSpy had another data breach, exposing the [private data on another 50,000 new victims](https://techcrunch.com/2024/02/12/new-thetruthspy-stalkerware-victims-is-your-android-device-compromised/). TechCrunch was sent a copy of this data, and we added the updated records to our lookup tool.

## TheTruthSpy, still exposing data, rebrands to PhoneParental

As it stands, some of TheTruthSpy’s operations wound down, and other parts rebranded to escape reputational scrutiny. TheTruthSpy still exists today, and it has kept much of its buggy source code and vulnerable back-end dashboards while rebranding as a new spyware app called PhoneParental.

Thieu continu...