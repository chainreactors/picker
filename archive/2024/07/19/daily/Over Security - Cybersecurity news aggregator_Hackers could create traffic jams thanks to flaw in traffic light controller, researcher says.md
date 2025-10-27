---
title: Hackers could create traffic jams thanks to flaw in traffic light controller, researcher says
url: https://techcrunch.com/2024/07/18/hackers-could-create-traffic-jams-thanks-to-flaw-in-traffic-light-controller-researcher-says/
source: Over Security - Cybersecurity news aggregator
date: 2024-07-19
fetch_date: 2025-10-06T17:42:40.716578
---

# Hackers could create traffic jams thanks to flaw in traffic light controller, researcher says

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

![A confusing traffic light system with multiple signal heads.](https://techcrunch.com/wp-content/uploads/2024/07/traffic-lights.jpg?w=1024)

**Image Credits:**Richard Newstead / Getty Images

[Security](https://techcrunch.com/category/security/)

# Hackers could create traffic jams thanks to flaw in traffic light controller, researcher says

[Lorenzo Franceschi-Bicchierai](https://techcrunch.com/author/lorenzo-franceschi-bicchierai/)

6:13 AM PDT · July 18, 2024

A security researcher says he found a flaw in a traffic light controller that would potentially allow malicious hackers to change the lights and create traffic jams.

Andrew Lemon, a researcher at cybersecurity firm Red Threat, published two [blog](https://www.redthreatsec.com/blog/give-me-the-green-light-part2-dirty-little-secrets) [posts](https://www.redthreatsec.com/blog/give-me-the-green-light-part2-dirty-little-secrets) on Thursday detailing his findings of a wider research project investigating the security of traffic controllers.

One of the devices Lemon looked at is the Intelight X-1, where [he said he found a bug](https://gist.github.com/LemonSec/6aaea8320187a38e1a398fa321f12303) that allows anyone to take full control of the traffic lights. According to Lemon, the bug is very simple and basic: There is no authentication on the internet-exposed web interface of the device.

“I was just in disbelief,” Lemon told TechCrunch. “I was just shocked that something so glaring could have been missed.”

Lemon said he tried to see if it was possible to trigger a scenario like the one shown in movies like [The Italian Job](https://youtu.be/kLCmDCMTq4A?si=HrcjUxHmUntrmVT4&t=191), where hackers switch all lights in an intersection to green. But Lemon said he found another device called the Malfunction Management Unit prevents that scenario from happening.

“You can still make changes to the lights and the timing. So if you wanted to set the timing to be three minutes one way and three seconds the other way. Basically it’s a denial of service in the physical world, so you could clog up traffic,” said Lemon.

It’s unclear how many vulnerable Intelight devices are accessible from the internet. Lemon said he and his team found about 30 exposed devices.

Techcrunch event

### Join 10k+ tech and VC leaders for growth and connections at Disrupt 2025

#### Netflix, Box, a16z, ElevenLabs, Wayve, Hugging Face, Elad Gil, Vinod Khosla — just some of the 250+ heavy hitters leading 200+ sessions designed to deliver the insights that fuel startup growth and sharpen your edge. Don’t miss the 20th anniversary of TechCrunch, and a chance to learn from the top voices in tech. **Grab your ticket before doors open to save up to $444.**

### Join 10k+ tech and VC leaders for growth and connections at Disrupt 2025

#### Netflix, Box, a16z, ElevenLabs, Wayve, Hugging Face, Elad Gil, Vinod Khosla — just some of the 250+ heavy hitters leading 200+ sessions designed to deliver the insights that fuel startup growth and sharpen your edge. Don’t miss a chance to learn from the top voices in tech. **Grab your ticket before doors open to save up to $444.**

San Francisco
|
October 27-29, 2025

[**REGISTER NOW**](https://techcrunch.com/events/tc-disrupt-2025/?utm_source=tc&utm_medium=ad&utm_campaign=disrupt2025&utm_content=ticketsales&promo=tc_inline_lb&display=)

Lemon said he reached out to Q-Free, the company that owns Intelight, to report the bug. Instead of responding and engaging with him to fix the flaw, Q-Free sent him a legal letter, according to Lemon, who published a copy of it in his blog post.

“We only accept vulnerability reports that relate to Q-Free products that are currently offered for sale. We do not have the resources necessary to consider analyses of outdated items,” read the copy of the letter, which appears to be signed by Steven D. Tibbets, Q-Free’s general counsel.

The copy of the letter said that the device Lemon analyzed is not for sale, and that the way he and Red Threat researched it may have been a violation of the anti-hacking law, [the Computer Fraud and Abuse Act](https://techcrunch.com/2022/05/19/justice-department-good-faith-hackers-cfaa/). The company did not specify how Lemon’s research could have violated the law. The letter then asked Lemon and Red Threat to commit that they would not publish details of the vulnerability because it could hurt national security.

“We also urge Red Threat to consider the impact of publication on the security of critical infrastructure in which Q-Free devices are used. Contrary to your stated aims of improving cybersecurity, publication of vulnerabilities may encourage attacks on infrastructure and generate associated liability for Red Threat,” the letter read.

Lemon said he was surprised by the letter, and that “it really felt like they were just trying to silence me with legal threats and everything.”

Q-Free’s spokesperson Trisha Tunilla told TechCrunch that “it is important to note that the controller in question has not been in production for nearly a decade.”

“Our records cannot confirm that all these controllers have since been updated. However, if any of these legacy controllers are still in use, we strongly encourage customers to contact us immediately so we can provide guidance and a path forward,” Tunilla wrote in an email.

Regarding the letter sent by Q-Free’s general counsel, Tunilla said that “it is our standard procedure to have our legal department respond to inquiries like this.”

Lemon said that during his research he also found some traffic controller devices made by Econolite exposed to the internet, and run a protocol that is potentially vulnerable.

The protocol is called [NTCIP](https://www.ntcip.org/about/) and it’s an industry standard for traffic light controllers. Lemon said that for the devices that are exposed on the internet, it is possible to change the values in the ...