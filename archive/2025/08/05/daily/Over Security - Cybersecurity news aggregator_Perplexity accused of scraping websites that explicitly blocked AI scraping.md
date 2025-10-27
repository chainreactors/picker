---
title: Perplexity accused of scraping websites that explicitly blocked AI scraping
url: https://techcrunch.com/2025/08/04/perplexity-accused-of-scraping-websites-that-explicitly-blocked-ai-scraping/
source: Over Security - Cybersecurity news aggregator
date: 2025-08-05
fetch_date: 2025-10-07T00:49:30.676657
---

# Perplexity accused of scraping websites that explicitly blocked AI scraping

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

![Aravind Srinivas, Co-Founder & CEO of Perplexity, speaks onstage during TechCrunch Disrupt 2024](https://techcrunch.com/wp-content/uploads/2024/11/GettyImages-2181996346.jpg?w=1024)

**Image Credits:**Kimberly White/Getty Images for TechCrunch

[Security](https://techcrunch.com/category/security/)

# Perplexity accused of scraping websites that explicitly blocked AI scraping

[Lorenzo Franceschi-Bicchierai](https://techcrunch.com/author/lorenzo-franceschi-bicchierai/)

8:41 AM PDT · August 4, 2025

AI startup Perplexity is crawling and scraping content from websites that have explicitly indicated they don’t want to be scraped, according to internet infrastructure provider Cloudflare.

On Monday, Cloudflare [published research](https://blog.cloudflare.com/perplexity-is-using-stealth-undeclared-crawlers-to-evade-website-no-crawl-directives/) saying it observed the AI startup ignore blocks and hide its crawling and scraping activities. The network infrastructure giant accused Perplexity of obscuring its identity when trying to scrape web pages “in an attempt to circumvent the website’s preferences,” Cloudflare’s researchers wrote.

AI products like those offered by Perplexity rely on gobbling up large amounts of data from the internet, and AI startups have long scraped text, images, and videos from the internet many times without permission to make their products work. In recent times, websites have tried to fight back by using the web standard Robots.txt file, which tells search engines and AI companies which pages can be indexed and which shouldn’t, efforts [that have seen mixed results so far](https://www.reuters.com/technology/artificial-intelligence/multiple-ai-companies-bypassing-web-standard-scrape-publisher-sites-licensing-2024-06-21/).

Perplexity appears to be willingly circumventing these blocks by changing its bots’ “user agent,” meaning a signal that identifies a website visitor by their device and version type, as well as changing their autonomous system networks, or ASN, essentially a number that identifies large networks on the internet, according to Cloudflare.

“This activity was observed across tens of thousands of domains and millions of requests per day. We were able to fingerprint this crawler using a combination of machine learning and network signals,” read Cloudflare’s post.

Perplexity spokesperson Jesse Dwyer dismissed Cloudflare’s blog post as a “sales pitch,” adding in an email to TechCrunch that the screenshots in the post “show that no content was accessed.” In a follow-up email, Dwyer claimed the bot named in the Cloudflare blog “isn’t even ours.”

Cloudflare said it first noticed the behavior after its customers complained that Perplexity was crawling and scraping their sites, even after they added rules on their Robots file and for specifically blocking Perplexity’s known bots. Cloudflare said it then performed tests to check and confirmed that Perplexity was circumventing these blocks.

Techcrunch event

### Join 10k+ tech and VC leaders for growth and connections at Disrupt 2025

#### Netflix, Box, a16z, ElevenLabs, Wayve, Hugging Face, Elad Gil, Vinod Khosla — just some of the 250+ heavy hitters leading 200+ sessions designed to deliver the insights that fuel startup growth and sharpen your edge. Don’t miss the 20th anniversary of TechCrunch, and a chance to learn from the top voices in tech. **Grab your ticket before doors open to save up to $444.**

### Join 10k+ tech and VC leaders for growth and connections at Disrupt 2025

#### Netflix, Box, a16z, ElevenLabs, Wayve, Hugging Face, Elad Gil, Vinod Khosla — just some of the 250+ heavy hitters leading 200+ sessions designed to deliver the insights that fuel startup growth and sharpen your edge. Don’t miss a chance to learn from the top voices in tech. **Grab your ticket before doors open to save up to $444.**

San Francisco
|
October 27-29, 2025

[**REGISTER NOW**](https://techcrunch.com/events/tc-disrupt-2025/?utm_source=tc&utm_medium=ad&utm_campaign=disrupt2025&utm_content=ticketsales&promo=tc_inline_lb&display=)

“We observed that Perplexity uses not only their declared user-agent, but also a generic browser intended to impersonate Google Chrome on macOS when their declared crawler was blocked,” according to Cloudflare.

The company also said that it has de-listed Perplexity’s bots from its verified list and added new techniques to block them.

Cloudflare has recently taken a public stance against AI crawlers. Last month, Cloudflare [announced the launch of a marketplace](https://techcrunch.com/2025/07/01/cloudflare-launches-a-marketplace-that-lets-websites-charge-ai-bots-for-scraping/) allowing website owners and publishers to charge AI scrapers who visit their sites. Cloudflare’s chief executive Matthew Prince [sounded the alarm](https://www.cfr.org/event/bernard-l-schwartz-annual-lecture-matthew-prince-cloudflare) at the time, saying AI is breaking the business model of the internet, particularly publishers. Last year, Cloudflare also [launched a free tool](https://techcrunch.com/2024/07/03/cloudflare-launches-a-tool-to-combat-ai-bots/#:~:text=Cloudflare%20has%20set%20up%20a,demand%20for%20model%20training%20data.) to prevent bots from scraping websites to train AI.

This is not the first time Perplexity is accused of scraping without authorization.

Last year, news outlets, [such as Wired](https://www.wired.com/story/perplexity-is-a-bullshit-machine/), alleged [Perplexity was plagiarizing their content](http://techcrunch.com/2024/07/02/news-outlets-are-accusing-perplexity-of-plagiarism-and-unethical-web-scraping/). Weeks later, Perplexity’s CEO Aravind Srinivas [was unable to immediately answer](http://techcrunch.com/2024/10/30/perplexitys-ceo-punts-on-defining-plagiarism/) when asked to provide the company’s definition of plagiarism during an interview with TechCrunch’s Devin Coldewey at the Disrupt 20...