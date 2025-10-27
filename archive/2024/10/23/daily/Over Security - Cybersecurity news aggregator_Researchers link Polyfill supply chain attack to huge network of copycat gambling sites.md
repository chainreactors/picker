---
title: Researchers link Polyfill supply chain attack to huge network of copycat gambling sites
url: https://techcrunch.com/2024/10/22/researchers-link-polyfill-supply-chain-attack-to-huge-network-of-copycat-gambling-sites/
source: Over Security - Cybersecurity news aggregator
date: 2024-10-23
fetch_date: 2025-10-06T18:54:30.418219
---

# Researchers link Polyfill supply chain attack to huge network of copycat gambling sites

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

![](https://techcrunch.com/wp-content/uploads/2024/10/funnull-polyfill-supply-chain-hack.png?w=1024)

**Image Credits:**Bryce Durbin/TechCrunch

[Security](https://techcrunch.com/category/security/)

# Researchers link Polyfill supply chain attack to huge network of copycat gambling sites

[Lorenzo Franceschi-Bicchierai](https://techcrunch.com/author/lorenzo-franceschi-bicchierai/)

9:07 AM PDT · October 22, 2024

One of the biggest digital supply chain attacks of the year was launched by a little-known company that redirected large numbers of internet users to a network of copycat gambling sites, according to security researchers.

Earlier this year, a company called FUNNULL [purchased Polyfill.io](https://www.bleepingcomputer.com/news/security/polyfill-claims-it-has-been-defamed-returns-after-domain-shut-down/), a domain hosting an open source JavaScript library that — if embedded in websites — can allow outdated browsers to run features found in newer browsers. Once in control of Polyfill.io, FUNNULL used the domain to essentially carry out a supply chain attack, [as cybersecurity firm Sansec reported in June](https://sansec.io/research/polyfill-supply-chain-attack), where FUNNULL took over a legitimate service and abused its access to [potentially millions of websites](https://x.com/eastdakota/status/1806064925670080935) to push malware to their visitors.

At the time of the Polyfill.io takeover, the original Polyfill author [warned that he never owned the Polyfill.io domain](https://x.com/triblondon/status/1761852117579427975) and suggested websites remove the hosted Polyfill code completely to avoid risks. Also, content delivery network providers Cloudflare and Fastly put out their own mirrors of Polyfill.io to offer a safe trusted alternative for websites that wanted to keep using the Polyfill library.

It’s unclear what the goal of the supply chain attack was exactly, but Willem de Groot, the founder of Sansec, [wrote on X at the time](https://x.com/gwillem/status/1805741224189739170) that it appeared to be a “laughably bad” attempt at monetization.

Now, security researchers at Silent Push say they mapped out a network of thousands of Chinese gambling sites and linked it to FUNNULL and the Polyfill.io supply chain attack.

[According to the researchers’ report](https://www.silentpush.com/blog/triad-nexus-funnull), which was shared with TechCrunch in advance, FUNNULL was using its access to Polyfill.io to [inject malware and redirect](https://sansec.io/research/polyfill-supply-chain-attack) website visitors to that malicious network of casino and online gambling sites.

“It appears likely that this ‘online gambling network’ is a front,” Zach Edwards, a senior threat analyst and one of the researchers who worked on the Silent Push report, told TechCrunch. Edwards added that FUNNULL is “operating what appears to be one of the largest online gambling rings on the internet.”

Techcrunch event

### Join 10k+ tech and VC leaders for growth and connections at Disrupt 2025

#### Netflix, Box, a16z, ElevenLabs, Wayve, Hugging Face, Elad Gil, Vinod Khosla — just some of the 250+ heavy hitters leading 200+ sessions designed to deliver the insights that fuel startup growth and sharpen your edge. Don’t miss the 20th anniversary of TechCrunch, and a chance to learn from the top voices in tech. **Grab your ticket before doors open to save up to $444.**

### Join 10k+ tech and VC leaders for growth and connections at Disrupt 2025

#### Netflix, Box, a16z, ElevenLabs, Wayve, Hugging Face, Elad Gil, Vinod Khosla — just some of the 250+ heavy hitters leading 200+ sessions designed to deliver the insights that fuel startup growth and sharpen your edge. Don’t miss a chance to learn from the top voices in tech. **Grab your ticket before doors open to save up to $444.**

San Francisco
|
October 27-29, 2025

[**REGISTER NOW**](https://techcrunch.com/events/tc-disrupt-2025/?utm_source=tc&utm_medium=ad&utm_campaign=disrupt2025&utm_content=ticketsales&promo=tc_inline_lb&display=)

Silent Push researchers [said in their report](https://www.silentpush.com/blog/triad-nexus-funnull) that they were able to identify around 40,000 mostly Chinese-language websites hosted by FUNNULL, all with similarly looking and likely automatically generated domains made up of a scattering of seemingly random letters and numbers. These sites appeared to impersonate online gambling and casino brands, including Sands, a casino conglomerate that owns Venetian Macau, the Grand Lisboa in Macau, and SunCity Group; as well as the online gambling portals Bet365 and Bwin.

![](https://techcrunch.com/wp-content/uploads/2024/10/funnull-gambling-spammy-website.png?w=680)

A screenshot of one of the thousands of spammy online gambling websites hosted on FUNNULL’s CDN. (Image: TechCrunch)

Chris Alfred, a spokesperson for Entain, the parent company of Bwin, told TechCrunch that the company “can confirm that this is not a domain we own so it appears the site owner is infringing on our Bwin brand so we will be taking action to resolve this.”

Sands, SunCity Group, Macau Grand Lisboa, and Bet365 did not respond to multiple requests for comment.

Edwards told TechCrunch that he and his colleagues found a FUNNULL developer’s GitHub account, who discussed “money-moving,” an expression that they believe refers to money laundering. The GitHub page also contained links to Telegram channels that include mentions of the gambling brands impersonated in the network of spammy sites, as well as talk about moving money.

“And those sites are all for moving money, or is their primary purpose,” said Edwards.

The suspicious network of sites, according to Edwards and his colleagues, is hosted on [FUNNULL’s content delivery network](https://funnull.io/Contact/), or CDN, whose website [claims](https://funnull.io/Contact/#:~:text=%402022%20FUNNULL%20LLC%20Made%20in%20USA) ...