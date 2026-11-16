---
title: If It's on the Internet, It Will Get Attacked.
url: https://pentester.ca/blog/if-its-on-the-internet-it-will-get-attacked
source: Over Security
date: 2026-11-15
fetch_date: 2026-11-16T08:48:44.668464
---

# If It's on the Internet, It Will Get Attacked.

[Skip to main content](#main)

[](/assets/images/Orbs/PT_Orb_LoopDark.webm)
![](/assets/images/Logos/Pentester.ca_Full_Logo_Dark.svg)

[](/assets/images/Orbs/PT_DarkPink_Orb.webm)

* Based in Tokyo,
  [E: [email protected]](/cdn-cgi/l/email-protection#45322d2c31202d24310535202b3120363120376b2624)
* Japan
  --:--:-- (GMT+9)

* [Home](/)
* [What You Get](/#what-you-get)
* [Why Hire Me?](/#why-hire-me)
* [Who Have I Helped?](/#who-helped)
* [The Feedback](/#feedback)
* [Blog](/blog)
* [Contact](#contact)

[![Pentester.ca - home](/assets/images/Logos/Pentester.ca_Full_Logo_Light.svg)](/)

[![](/assets/images/Title_Element_Black.svg)
BLOG](/blog)

# If It's on the Internet, It Will Get Attacked.

By Kaeden | Pentester.ca | March 27, 2026

A developer at a Fortune 500 company I work with had an attitude problem when it came to security. He didn't think it mattered much for the things he built. Nobody would bother attacking it. Nobody would be interested. It wasn't important enough to be a target.

He was wrong. And I have two stories that prove it.

## Tea: Reported, Paid, Ignored, Hacked

Tea was a dating safety app for women. Users could run background checks on potential partners, flag red flags, and share experiences. It climbed to the number one spot on the App Store in July 2025 with over 1.6 million users. Women uploaded selfies and government-issued IDs for verification.

In July 2025, I was looking through apps like I always do and found a dating safety app with an open Firebase database. I reported it responsibly. Roughly 12 hours later, someone else found the same open database and it wasn't to help. The app was hacked.

It wasn't until months later, when I was sending information to 404 Media, that I realized I had actually reported the exact same vulnerabilities to the exact same company eight months earlier, in November 2024. That's how many apps I look at. I didn't even remember.

Back in November 2024, Tea had responded quickly. They called me "obviously a talented engineer," thanked me for the responsible disclosure, and paid me $100 through Stripe, a lowball for a vulnerability exposing over a million users' data. They said their team would "get some fixes out asap."

They didn't fix it. Eight months later, I found the same open database, reported it again, and hours later their users' data was on 4chan.

Users on 4chan discovered the same open database I had reported twice. "DRIVERS LICENSES AND FACE PICS!" one post read. Over 70,000 images were leaked and posted publicly, including the government IDs and selfies women had uploaded for verification. Misogynist groups created websites to humiliate the women who had signed up. Maps were published showing 33,000 pins of users' approximate locations across the United States. Multiple women have since filed class action lawsuits, as reported by the BBC.

One woman who had joined Tea to protect herself from a stalker ex-boyfriend found her exact address pinned on a public map. She had to move in with family to feel safe.

404 Media broke the breach story on the same day it happened. The vulnerability they described was the exact same Firebase misconfiguration I had reported in November 2024 and again in July 2025.

They paid me. They thanked me. They told me they'd fix it. They didn't. And their users paid the price.

## Quittr: Reported, Ignored, Exposed

Quittr is an app that helps people stop watching porn. It tracks "abstinence" streaks, has community features, an AI therapist, and a "panic button." It has been downloaded 1.5 million times and brings in $500,000 per month, according to its founders.

In July 2025, I found that Quittr had the exact same problem: an open Firebase database with no security rules. I could list all users and their data. For an app that tracks masturbation habits, that's about as sensitive as data gets.

I emailed the founders and explained the vulnerability. A developer responded, said he was "looking into ways to make our security better," and asked how I found it. I walked him through it step by step, even explained that the API key being client-sided is normal for Firebase and that they just needed to implement security rules.

Then nothing. I followed up. No response. I followed up again. Nothing.

Many months later, after I had forgotten about the disclosure entirely, I saw that 404 Media and Mashable had published stories about an app called Quittr having its database exposed. The name sounded familiar. I searched my emails and found out I had reported the exact same vulnerability to them months earlier. They ignored me.

When 404 Media's Emanuel Maiberg called the founders, they denied there was even an issue. The same pattern as Tea, just without the $100.

## The Pattern

Two different apps. Two different industries. Same vulnerability. Same outcome.

Tea paid me and said they'd fix it. They didn't. Their users' driver's licenses ended up on 4chan.

Quittr didn't even respond. Their users' most private habits ended up in the press.

Something that stuck with me: another dating app in 2024 told me they were "aware of those security issues but did not prioritize them yet" because they were "still in our testing/market validation phase." They had real users, real data, and real ad campaigns running. But because they considered themselves still in testing, security could wait. I hear this constantly.

Both Tea and Quittr had the same Firebase misconfiguration that takes minutes to find and minutes to fix. All of them had months of warning. All of them chose to do nothing.

## The Developer Who Thinks Nobody Cares

Back to that Fortune 500 developer who assumed nobody would bother attacking what he built. He was wrong. Everything on the internet gets attacked. It doesn't matter if it's a dating safety app, a masturbation tracker, an internal tool at a company nobody has heard of, or the PC you're using to surf the web.

Automated scanners sweep the internet constantly. Researchers like me look at hundreds of apps. Hackers on 4chan do the same thing I do, except they don't send a polite email first. It doesn't even need to be an app or a website. If you have an IP address, you're being scanned. Bots crawl every IP range on the internet 24/7 looking for open ports, exposed databases, and misconfigured services. Most of it gets blocked, but it only takes one that doesn't.

The question isn't whether your app is important enough to be targeted. The question is whether your database is open right now, and whether you'll fix it before someone less friendly than me finds it.

[Get a Free Consultation
![](/assets/images/Top_Right_Arrow_Black.svg)](https://cal.com/whitehat/30min?user=whitehat)
[![](/assets/images/Top_Right_Arrow_Black.svg)Back to all posts](/blog)

## Read About My Work

* [![](/assets/images/Top_Right_Arrow_Black.svg)Blog](/blog)

© 2026 Designed by [PixelPonderer](https://pixelponderer.com/)

## Got Security?

[[email protected]](/cdn-cgi/l/email-protection#5126393825343930251121343f2534222534237f3230)

[Let's Connect
![](/assets/images/Top_Right_Arrow_Black.svg)](https://cal.com/whitehat/30min?user=whitehat)

## Where to Find Me

* [![](/assets/images/Top_Right_Arrow_Black.svg) LinkedIn](https://www.linkedin.com/in/kaeden69420/)

Based in Tokyo, Japan

Disclaimer: Got Vulnerabilities?® is a parody. Got Milk?® is a registered trademark of the California Milk Processor Board.