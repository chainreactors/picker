---
title: Researcher finds flaw in a16z website that exposed some company data
url: https://techcrunch.com/2024/07/18/researcher-finds-flaw-in-a16z-website-that-exposed-some-company-data/
source: Over Security - Cybersecurity news aggregator
date: 2024-07-23
fetch_date: 2025-10-06T17:44:19.659510
---

# Researcher finds flaw in a16z website that exposed some company data

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

![Marc Andreessen, co-founder and general partner of Andreessen Horowitz, speaks during the TechCrunch Disrupt San Francisco 2016 Summit in San Francisco, California, U.S., on Tuesday, Sept. 13, 2016.](https://techcrunch.com/wp-content/uploads/2024/07/marc-andreessen-a16-z.jpg?w=1024)

**Image Credits:**David Paul Morris/Bloomberg / Getty Images

[Security](https://techcrunch.com/category/security/)

# Researcher finds flaw in a16z website that exposed some company data

[Lorenzo Franceschi-Bicchierai](https://techcrunch.com/author/lorenzo-franceschi-bicchierai/)

2:41 PM PDT · July 18, 2024

At the end of June, a security researcher found a vulnerability in a web app used by [a16z](https://techcrunch.com/tag/a16z/), one of the most powerful and influential Silicon Valley venture capital firms, which exposed some data about the firm’s portfolio companies. The bug has since been fixed.

On June 30, a security researcher who goes by xyzeva [wrote on X](https://x.com/xyz3va/status/1807330215955177937) that she was looking for someone from a16z to reach out, hinting that she had found a security issue.

“Get in touch, now. its bad. security related,” she wrote.

When reached by TechCrunch, xyzeva said that she found “a really simple bug” that “basically gave access to everything” on a16z portfolio portal. More specifically, she said that she found exposed API keys on the site portfolio.a16z.com. xyzeva said that the information she was able to see included: emails, passwords, and “company details and employees.” Also, she added, she could have sent emails as a16z and access previously sent emails from the company’s account with Mailgun, an email delivery service.

In a statement to TechCrunch, Bryan Green, the chief information security officer at a16z, confirmed that the company fixed the bug on the same day xyzeva wrote the post and got in touch with the company, but said that the issue didn’t affect any sensitive data.

“On June 30th, a16z addressed a misconfiguration in a web app that is used for the specific use case of updating publicly available information on our website such as company logos and social media profiles. The issue was resolved quickly and no sensitive data was compromised,” said Green. “We remain committed to collaborating with the security community on ethical disclosures and will continue to do so through responsible means.”

In a text conversation seen by TechCrunch, where xyzeva inquired about a bug bounty program — a way for security researchers to get rewarded for their findings — a company employee told her that the firm doesn’t provide one. “However, after we complete the analysis I’m very happy to try to set something up specifically for you in this case,” the employee said.

Techcrunch event

### Join 10k+ tech and VC leaders for growth and connections at Disrupt 2025

#### Netflix, Box, a16z, ElevenLabs, Wayve, Hugging Face, Elad Gil, Vinod Khosla — just some of the 250+ heavy hitters leading 200+ sessions designed to deliver the insights that fuel startup growth and sharpen your edge. Don’t miss the 20th anniversary of TechCrunch, and a chance to learn from the top voices in tech. **Grab your ticket before doors open to save up to $444.**

### Join 10k+ tech and VC leaders for growth and connections at Disrupt 2025

#### Netflix, Box, a16z, ElevenLabs, Wayve, Hugging Face, Elad Gil, Vinod Khosla — just some of the 250+ heavy hitters leading 200+ sessions designed to deliver the insights that fuel startup growth and sharpen your edge. Don’t miss a chance to learn from the top voices in tech. **Grab your ticket before doors open to save up to $444.**

San Francisco
|
October 27-29, 2025

[**REGISTER NOW**](https://techcrunch.com/events/tc-disrupt-2025/?utm_source=tc&utm_medium=ad&utm_campaign=disrupt2025&utm_content=ticketsales&promo=tc_inline_lb&display=)

Days later, however, the employee told xyzeva that “unfortunately, there are a couple of things getting in the way,” according to another text exchange seen by TechCrunch.

“First, there’s the disclosure method. Posting that there was a serious issue publicly meant that potential attackers likely scanning our sites to search for the issue, which increased risk for us unnecessarily and is outside the norm of how vulnerability disclosures are performed,” said the employee. “Second, the follow-up post that incorrectly described ‘full access to basically everything’ and promised a write-up didn’t signal the best intentions to the team. If any of this is being misunderstood, please let me know.”

It’s not uncommon for security researchers to disclose their findings when the vulnerability or issue is fixed and no longer at risk.

As of this writing, the portal where xyzeva found the issue is not available. “This application is being deprecated,” [read a message](https://portfolio.a16z.com/) on the site.

Over the years, a16z has invested in several well-known companies like Airbnb, Coinbase, Instacart, Lyft, and Slack, [among many others](https://a16z.com/portfolio/). The firm’s founders Marc Andreesen and Ben Horowitz have recently said that [they are supporting Donald Trump in the upcoming presidential elections](https://techcrunch.com/2024/07/16/andreessen-horowitz-co-founders-explain-why-theyre-supporting-trump/).

Topics

[a16z](https://techcrunch.com/tag/a16z/), [Andreessen Horowitz](https://techcrunch.com/tag/andreessen-horowitz/), [bugs](https://techcrunch.com/tag/bugs/), [cybersecurity](https://techcrunch.com/tag/cybersecurity/), [Exclusive](https://techcrunch.com/tag/exclusive/), [infosec](https://techcrunch.com/tag/infosec/), [Security](https://techcrunch.com/category/security/)

![Lorenzo Franceschi-Bicchierai](https://techcrunch.com/wp-content/uploads/2025/07/Lorenzo-headshot-2023-cropped.jpeg?w=150)

Lorenzo Franceschi-Bicchierai

Senior Reporter, Cybersecurity

Lorenzo Franceschi-Bicchierai is a Senior Wri...