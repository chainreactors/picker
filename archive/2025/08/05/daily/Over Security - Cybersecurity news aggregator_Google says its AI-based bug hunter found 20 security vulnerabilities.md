---
title: Google says its AI-based bug hunter found 20 security vulnerabilities
url: https://techcrunch.com/2025/08/04/google-says-its-ai-based-bug-hunter-found-20-security-vulnerabilities/
source: Over Security - Cybersecurity news aggregator
date: 2025-08-05
fetch_date: 2025-10-07T00:49:25.927948
---

# Google says its AI-based bug hunter found 20 security vulnerabilities

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

![Google DeepMind presented onstage](https://techcrunch.com/wp-content/uploads/2023/05/google-io-2023-google-deepmind.jpg?w=1024)

**Image Credits:**Google

[Security](https://techcrunch.com/category/security/)

# Google says its AI-based bug hunter found 20 security vulnerabilities

[Lorenzo Franceschi-Bicchierai](https://techcrunch.com/author/lorenzo-franceschi-bicchierai/)

12:22 PM PDT · August 4, 2025

Google’s AI-powered bug hunter has just reported its first batch of security vulnerabilities.

Heather Adkins, Google’s vice president of security, [announced](https://x.com/argvee/status/1952390039700431184) Monday that its LLM-based vulnerability researcher Big Sleep found and reported 20 flaws in various popular open source software.

Adkins said that Big Sleep, which is developed by the company’s AI department DeepMind as well as its elite team of hackers Project Zero, [reported its first-ever vulnerabilities](https://issuetracker.google.com/issues?q=componentid:1836411&s=type:desc&s=issue_id:desc&pli=1), mostly in open source software such as audio and video library FFmpeg and image-editing suite ImageMagick.

Given that the vulnerabilities are not fixed yet, we don’t have details of their impact or severity, as Google [does not yet want to provide details](https://googleprojectzero.blogspot.com/2025/07/reporting-transparency.html), which is a standard policy when waiting for bugs to be fixed. But the simple fact that Big Sleep found these vulnerabilities is significant, as it shows these tools are starting to get real results, even if there was a human involved in this case.

“To ensure high quality and actionable reports, we have a human expert in the loop before reporting, but each vulnerability was found and reproduced by the AI agent without human intervention,” Google’s spokesperson Kimberly Samra told TechCrunch.

Royal Hansen, Google’s vice president of engineering, [wrote on X](https://x.com/royalhansen/status/1952424018663162235) that the findings demonstrate “a new frontier in automated vulnerability discovery.”

LLM-powered tools that can look for and find vulnerabilities [are already a reality](https://techcrunch.com/2025/07/24/ai-slop-and-fake-reports-are-exhausting-some-security-bug-bounties/). Other than Big Sleep, there’s [RunSybil](https://www.runsybil.com/) and XBOW, among others.

Techcrunch event

### Join 10k+ tech and VC leaders for growth and connections at Disrupt 2025

#### Netflix, Box, a16z, ElevenLabs, Wayve, Hugging Face, Elad Gil, Vinod Khosla — just some of the 250+ heavy hitters leading 200+ sessions designed to deliver the insights that fuel startup growth and sharpen your edge. Don’t miss the 20th anniversary of TechCrunch, and a chance to learn from the top voices in tech. **Grab your ticket before doors open to save up to $444.**

### Join 10k+ tech and VC leaders for growth and connections at Disrupt 2025

#### Netflix, Box, a16z, ElevenLabs, Wayve, Hugging Face, Elad Gil, Vinod Khosla — just some of the 250+ heavy hitters leading 200+ sessions designed to deliver the insights that fuel startup growth and sharpen your edge. Don’t miss a chance to learn from the top voices in tech. **Grab your ticket before doors open to save up to $444.**

San Francisco
|
October 27-29, 2025

[**REGISTER NOW**](https://techcrunch.com/events/tc-disrupt-2025/?utm_source=tc&utm_medium=ad&utm_campaign=disrupt2025&utm_content=ticketsales&promo=tc_inline_lb&display=)

XBOW has garnered headlines after [it reached the top](https://xbow.com/blog/top-1-how-xbow-did-it) of one of the U.S. leaderboards at bug bounty platform HackerOne. It’s important to note that in most cases, these reports have a human at some point of the process to verify that the AI-powered bug hunter found a legitimate vulnerability, as is the case with Big Sleep.

Vlad Ionescu, co-founder and chief technology officer at RunSybil, a startup that develops AI-powered bug hunters, told TechCrunch that Big Sleep is a “legit” project, given that it has “good design, people behind it know what they’re doing, Project Zero has the bug finding experience and DeepMind has the firepower and tokens to throw at it.”

There is obviously a lot of promise with these tools, but also significant downsides. Several people who maintain different software projects have complained of [bug reports that are actually hallucinations](https://techcrunch.com/2025/07/24/ai-slop-and-fake-reports-are-exhausting-some-security-bug-bounties/), with some calling them the bug bounty equivalent of AI slop.

“That’s the problem people are running into, is we’re getting a lot of stuff that looks like gold, but it’s actually just crap,” Ionescu previously told TechCrunch.

Topics

[AI](https://techcrunch.com/category/artificial-intelligence/), [Big Sleep](https://techcrunch.com/tag/big-sleep/), [cybersecurity](https://techcrunch.com/tag/cybersecurity/), [DeepMind](https://techcrunch.com/tag/deepmind/), [Google](https://techcrunch.com/tag/google/), [hackers](https://techcrunch.com/tag/hackers/), [infosec](https://techcrunch.com/tag/infosec/), [LLMs](https://techcrunch.com/tag/llms/), [Security](https://techcrunch.com/category/security/)

![Lorenzo Franceschi-Bicchierai](https://techcrunch.com/wp-content/uploads/2025/07/Lorenzo-headshot-2023-cropped.jpeg?w=150)

Lorenzo Franceschi-Bicchierai

Senior Reporter, Cybersecurity

Lorenzo Franceschi-Bicchierai is a Senior Writer at TechCrunch, where he covers hacking, cybersecurity, surveillance, and privacy.

You can contact or verify outreach from Lorenzo by emailing lorenzo@techcrunch.com, via encrypted message at +1 917 257 1382 on Signal, and @lorenzofb on Keybase/Telegram.

[View Bio](https://techcrunch.com/author/lorenzo-franceschi-bicchierai/)

![Event Logo](https://techcrunch.com/wp-content/uploads/2025/07/TC25_Disrupt-Color.png)

October 27-29, 2025

San Francisco

**Founders:** Your next big c...