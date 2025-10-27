---
title: Bumble and Hinge allowed stalkers to pinpoint users’ locations down to 2 meters, researchers say
url: https://techcrunch.com/2024/07/31/bumble-and-hinge-allowed-stalkers-to-pinpoint-users-locations-down-to-2-meters-researchers-say/
source: Over Security - Cybersecurity news aggregator
date: 2024-08-01
fetch_date: 2025-10-06T18:07:52.399537
---

# Bumble and Hinge allowed stalkers to pinpoint users’ locations down to 2 meters, researchers say

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

![The Bumble app on a smartphone arranged in New York, US, on Monday, Nov. 6, 2023.](https://techcrunch.com/wp-content/uploads/2024/07/bumble-app.jpg?w=1024)

**Image Credits:**Gabby Jones/Bloomberg / Getty Images

[Security](https://techcrunch.com/category/security/)

# Bumble and Hinge allowed stalkers to pinpoint users’ locations down to 2 meters, researchers say

[Lorenzo Franceschi-Bicchierai](https://techcrunch.com/author/lorenzo-franceschi-bicchierai/)

1:00 AM PDT · July 31, 2024

A group of researchers said they found that vulnerabilities in the design of some dating apps, including the popular Bumble and Hinge, allowed malicious users or stalkers to pinpoint the location of their victims down to 2 meters.

In [a new academic paper](https://lepoch.at/files/dating-apps-usesec24.pdf), researchers from the Belgian university KU Leuven detailed their findings when they analyzed 15 popular dating apps. Of those, Badoo, Bumble, Grindr, happn, Hinge and Hily all had the same vulnerability that could have helped a malicious user identify the near-exact location of another user, according to the researchers.

While neither of those apps share exact locations when displaying the distance between users on their profiles, they did use exact locations for the “filters” feature of the apps. Generally speaking, by using filters, users can tailor their search for a partner based on criteria like age, height, what type of relationship they are looking for and, crucially, distance.

To pinpoint the exact location of a target user, the researchers used a novel technique they call “oracle trilateration.” In general, [trilateration](https://www.youtube.com/watch?v=4O3ZVHVFhes), which for example is used in GPS, works by using three points and measuring their distance relative to the target. This creates three circles, which intersect at the point where the target is located.

Oracle trilateration works slightly differently. The researchers wrote in their paper that the first step for the person who wants to identify their target’s location “roughly estimates the victim’s location,” for example, based on the location displayed in the target’s profile. Then the attacker moves in increments “until the oracle indicates that the victim is no longer within proximity, and this for three different directions. The attacker now has three positions with a known exact distance, i.e., the preselected proximity distance, and can trilaterate the victim,” the researchers wrote.

“It was somewhat surprising that known issues were still present in these popular apps,” Karel Dhondt, one of the researchers, told TechCrunch. While this technique doesn’t reveal the exact GPS coordinates of the victim, “I’d say 2 meters is close enough to pinpoint the user,” Dhondt said.

The good news is that all the apps that had these issues, and that the researchers reached out to, have now changed how distance filters work and are not vulnerable to the oracle trilateration technique. The fix, according to the researchers, was to round up the exact coordinates by three decimals, making them less precise and accurate.

Techcrunch event

### Join 10k+ tech and VC leaders for growth and connections at Disrupt 2025

#### Netflix, Box, a16z, ElevenLabs, Wayve, Hugging Face, Elad Gil, Vinod Khosla — just some of the 250+ heavy hitters leading 200+ sessions designed to deliver the insights that fuel startup growth and sharpen your edge. Don’t miss the 20th anniversary of TechCrunch, and a chance to learn from the top voices in tech. **Grab your ticket before doors open to save up to $444.**

### Join 10k+ tech and VC leaders for growth and connections at Disrupt 2025

#### Netflix, Box, a16z, ElevenLabs, Wayve, Hugging Face, Elad Gil, Vinod Khosla — just some of the 250+ heavy hitters leading 200+ sessions designed to deliver the insights that fuel startup growth and sharpen your edge. Don’t miss a chance to learn from the top voices in tech. **Grab your ticket before doors open to save up to $444.**

San Francisco
|
October 27-29, 2025

[**REGISTER NOW**](https://techcrunch.com/events/tc-disrupt-2025/?utm_source=tc&utm_medium=ad&utm_campaign=disrupt2025&utm_content=ticketsales&promo=tc_inline_lb&display=)

“This is approximately an uncertainty of one kilometer,” Dhondt said.

Bumble’s vice president of global communications Gabrielle Ferree said that the company was “made aware of these findings in early 2023 and swiftly resolved the issues outlined.” Ferree also said the issues were fixed in Badoo, which is owned by Bumble.

Dmytro Kononov, CTO and co-founder of Hily, told TechCrunch in a statement that the company received a report on the vulnerability in May 2023 and then did an investigation to assess the researchers’ claims.

“The findings indicated a potential possibility for trilateration. However, in practice, exploiting this for attacks was impossible. This is due to our internal mechanisms designed to protect against spammers and the logic of our search algorithm,” Kononov said. “Despite this, we engaged in extensive consultations with the authors of the report and collaboratively developed new geocoding algorithms to completely eliminate this type of attack. These new algorithms have been successfully implemented for over a year now.”

A Hinge spokesperson said the company “immediately took action” when they received the researchers’ report in early 2023.

Happn CEO and president Karima Ben Abdelmalek told TechCrunch in an emailed statement that the company was contacted by the researchers last year.

“After review by our Chief Security Officer of the research findings, we had the opportunity to discuss the trilateration method with the researchers. However, happn has an additional layer of protection beyond just rounding distances,” said Ben Abdelmalek. “This additional protection was not taken into account in their analysis and we mutua...