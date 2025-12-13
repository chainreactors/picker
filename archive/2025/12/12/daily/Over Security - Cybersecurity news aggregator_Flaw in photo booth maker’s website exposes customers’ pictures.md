---
title: Flaw in photo booth maker’s website exposes customers’ pictures
url: https://techcrunch.com/2025/12/12/flaw-in-photo-booth-makers-website-exposes-customers-pictures/
source: Over Security - Cybersecurity news aggregator
date: 2025-12-12
fetch_date: 2025-12-13T03:16:00.525023
---

# Flaw in photo booth maker’s website exposes customers’ pictures

[![](https://techcrunch.com/wp-content/uploads/2024/09/tc-lockup.svg) TechCrunch Desktop Logo](https://techcrunch.com)

[![](https://techcrunch.com/wp-content/uploads/2024/09/tc-logo-mobile.svg) TechCrunch Mobile Logo](https://techcrunch.com)

* [Latest](/latest/)
* [Startups](/category/startups/)
* [Venture](/category/venture/)
* [Apple](/tag/apple/)
* [Security](/category/security/)
* [AI](/category/artificial-intelligence/)
* [Apps](/category/apps/)

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

![A black and white picture of two photo booths.](https://techcrunch.com/wp-content/uploads/2025/12/photo-booth.jpg?w=1024)

**Image Credits:**[Joel Rouse/Unsplash (opens in a new window)](https://unsplash.com/%40thebumpercrew)

[Security](https://techcrunch.com/category/security/)

# Flaw in photo booth maker’s website exposes customers’ pictures

[Lorenzo Franceschi-Bicchierai](https://techcrunch.com/author/lorenzo-franceschi-bicchierai/)

7:37 AM PST · December 12, 2025

A company that makes photo booths is exposing pictures and videos of its customers online thanks to a simple flaw in its website where the files are stored, according to a security researcher.

The researcher, who goes by Zeacer, alerted TechCrunch to the security issue in late November after reporting the vulnerability in October to [Hama Film](https://hamafilm.com.au/), the photo booth maker that has franchise presence in Australia, the [United Arab Emirates](https://www.instagram.com/hamakono_dubai/?hl=en), and the [United States](http://www.usahamafilm.com/#franchise), but did not hear back.

Zeacer shared with TechCrunch a sample of pictures taken from Hama Film’s servers, which showed groups of clearly young people posing in photo booths. Hama Film’s booths not only print out the photos like a typical photo booth, but booths also upload the customers’ photos to the company’s servers.

Vibecast, which owns Hama Film, has yet to respond to his messages alerting the company of the issues. Vibecast also hasn’t responded to several requests for comment from TechCrunch, nor did Vibecast’s co-founder Joel Park respond to a message we sent via LinkedIn.

As of Friday, the researcher said the company has still not fully resolved the security flaw and continues to expose customers’ data. As such, TechCrunch is withholding specific details of the vulnerability from publication.

When Zeacer first found this flaw, he noted that it appeared that photos were deleted from the photo booth maker’s servers every two to three weeks.

Now, he said, the pictures stored on the servers appear to get deleted after 24 hours, which limits the number of pictures exposed at any given time. But a hacker could still exploit the vulnerability he discovered each day and download the contents of every photo and video on the server.

Techcrunch event

### Join the Disrupt 2026 Waitlist

#### Add yourself to the Disrupt 2026 waitlist to be first in line when Early Bird tickets drop. Past Disrupts have brought Google Cloud, Netflix, Microsoft, Box, Phia, a16z, ElevenLabs, Wayve, Hugging Face, Elad Gil, and Vinod Khosla to the stages — part of 250+ industry leaders driving 200+ sessions built to fuel your growth and sharpen your edge. Plus, meet the hundreds of startups innovating across every sector.

### Join the Disrupt 2026 Waitlist

#### Add yourself to the Disrupt 2026 waitlist to be first in line when Early Bird tickets drop. Past Disrupts have brought Google Cloud, Netflix, Microsoft, Box, Phia, a16z, ElevenLabs, Wayve, Hugging Face, Elad Gil, and Vinod Khosla to the stages — part of 250+ industry leaders driving 200+ sessions built to fuel your growth and sharpen your edge. Plus, meet the hundreds of startups innovating across every sector.

San Francisco
|
October 13-15, 2026

[**W**AITLIST **NOW**](https://techcrunch.com/events/tc-disrupt-2026/)

Before this week, Zeacer said at one point he saw more than 1,000 pictures online for the Hama Film booths in Melbourne.

This incident is the latest example of a company that, at least for a time, was not implementing certain basic and widely accepted security practices, such as rate-limiting. Last month, [TechCrunch reported that government contractor giant Tyler Technologies](https://techcrunch.com/2025/11/26/bug-in-jury-systems-used-by-several-us-states-exposed-sensitive-personal-data/) was not rate-limiting its websites used for allowing courts to manage their jurors’ personal information. This meant anyone could break into any juror’s profile by running a computer script capable of mass-guessing their date of birth and their easy-to-guess numerical identifier.

Topics

[cybersecurity](https://techcrunch.com/tag/cybersecurity/), [Exclusive](https://techcrunch.com/tag/exclusive/), [hacking](https://techcrunch.com/tag/hacking/), [Hama Film](https://techcrunch.com/tag/hama-film/), [Photo Booths](https://techcrunch.com/tag/photo-booths/), [Security](https://techcrunch.com/category/security/), [security vulnerability](https://techcrunch.com/tag/security-vulnerability/)

![Lorenzo Franceschi-Bicchierai](https://techcrunch.com/wp-content/uploads/2025/07/Lorenzo-headshot-2023-cropped.jpeg?w=150)

Lorenzo Franceschi-Bicchierai

Senior Reporter, Cybersecurity

Lorenzo Franceschi-Bicchierai is a Senior Writer at TechCrunch, where he covers hacking, cybersecurity, surveillance, and privacy.

You can contact or verify outreach from Lorenzo by emailing lorenzo@techcrunch.com, via encrypted message at +1 917 257 1382 on Signal, and @lorenzofb on Keybase/Telegram.

[View Bio](https://techcrunch.com/author/lorenzo-franceschi-bicchierai/)

![Event Logo](https://techcrunch.com/wp-content/uploads/2025/12/strictlyvc-wordmark-orange_horizontal_cropped.png)

Dates TBD

Locations TBA

Plan ahead for the 2026 StrictlyVC events. Hear straight-from-the-source candid insights in on-stage fireside sessions and meet the builders and backers shaping the industry. Join the waitlist to get first access to the lowest-priced tickets and important updates.

[Waitlist Now](https://techcrunch.com/events/strictlyvc-2026-events/)

## Most Popular

* ### [Google launched its deepest AI research agent yet — on the same day OpenAI dropped GPT-5.2](https://techcrunch.com/2025/12/11/google-launched-its-deepest-ai-research-agent-yet-on-the-same-day-openai-dropped-gpt-5-2/)

  + [Julie Bort](https://techcrunch.com/author/julie-bort/)
* ### [Disney hits Google with cease-and-desist claiming ‘massive’ copyright...