---
title: AI slop and fake reports are exhausting some security bug bounties
url: https://techcrunch.com/2025/07/24/ai-slop-and-fake-reports-are-exhausting-some-security-bug-bounties/
source: Over Security - Cybersecurity news aggregator
date: 2025-07-25
fetch_date: 2025-10-06T23:50:34.719670
---

# AI slop and fake reports are exhausting some security bug bounties

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

![Pattern of retro tin toy robots with clocks and displays painted on yellow background.](https://techcrunch.com/wp-content/uploads/2025/07/ai-slop-bug-bounty-reports-1646637201.jpg?w=1024)

**Image Credits:**DBenitostock / Getty Images

[Security](https://techcrunch.com/category/security/)

# AI slop and fake reports are coming for your bug bounty programs

[Lorenzo Franceschi-Bicchierai](https://techcrunch.com/author/lorenzo-franceschi-bicchierai/)

8:00 AM PDT · July 24, 2025

So-called AI slop, meaning [LLM](https://techcrunch.com/2025/05/25/from-llms-to-hallucinations-heres-a-simple-guide-to-common-ai-terms/#large-language-model)-generated low-quality images, videos, and text, has taken over the internet in the last couple of years, polluting [websites](https://techcrunch.com/2025/07/09/youtube-prepares-crackdown-on-mass-produced-and-repetitive-videos-as-concern-over-ai-slop-grows/), [social media platforms](https://www.404media.co/where-facebooks-ai-slop-comes-from/), at least [one newspaper](https://www.404media.co/viral-ai-generated-summer-guide-printed-by-chicago-sun-times-was-made-by-magazine-giant-hearst/), and even [real-world events](https://techcrunch.com/2025/01/08/ces-2025-was-full-of-irl-ai-slop/).

The world of cybersecurity is not immune to this problem, either. In the last year, people across the cybersecurity industry have raised concerns about AI slop bug bounty reports, meaning reports that claim to have found vulnerabilities that do not actually exist, because they were created with a [large language model](https://techcrunch.com/2024/06/01/what-is-ai-how-does-ai-work/) that simply made up the vulnerability, and then packaged it into a professional-looking writeup.

“People are receiving reports that sound reasonable, they look technically correct. And then you end up digging into them, trying to figure out, ‘oh no, where is this vulnerability?’,” Vlad Ionescu, the co-founder and CTO of [RunSybil](https://www.runsybil.com/), a startup that develops AI-powered bug hunters, told TechCrunch.

“It turns out it was just a hallucination all along. The technical details were just made up by the LLM,” said Ionescu.

Ionescu, who used to work at Meta’s red team tasked with hacking the company from the inside, explained that one of the issues is that LLMs are designed to be helpful and give positive responses. “If you ask it for a report, it’s going to give you a report. And then people will copy and paste these into the bug bounty platforms and overwhelm the platforms themselves, overwhelm the customers, and you get into this frustrating situation,” said Ionescu.

“That’s the problem people are running into, is we’re getting a lot of stuff that looks like gold, but it’s actually just crap,” said Ionescu.

Just in the last year, there have been real-world examples of this. Harry Sintonen, a security researcher, revealed that the open source security project Curl received a fake report. “The attacker miscalculated badly,” Sintonen wrote [in a post on Mastodon](https://infosec.exchange/%40harrysintonen/114455549143577092). “Curl can smell AI slop from miles away.”

In response to Sintonen’s post, Benjamin Piouffle of Open Collective, a tech platform for nonprofits, [said](https://framapiaf.org/%40Betree/114456180452192212) that they have the same problem: that their inbox is “flooded with AI garbage.”

One open source developer, who maintains the CycloneDX project on GitHub, [pulled their bug bounty down entirely](https://github.com/CycloneDX/cyclonedx-rust-cargo/commit/93b19cb4ac96d1b8f51647df2b89ec4359becae1) earlier this year after receiving “almost entirely AI slop reports.”

The leading bug bounty platforms, which essentially work as intermediaries between bug bounty hackers and companies who are willing to pay and reward them for finding flaws in their products and software, are also seeing a spike in AI-generated reports, TechCrunch has learned.

#### Contact Us

Do you have more information about how AI is impacting the cybersecurity industry? We’d love to hear from you. From a non-work device and network, you can contact Lorenzo Franceschi-Bicchierai securely on Signal at +1 917 257 1382, or via Telegram and Keybase @lorenzofb, or email.

Michiel Prins, the co-founder and senior director of product management at HackerOne, told TechCrunch that the company has encountered some AI slop.

“We’ve also seen a rise in false positives — vulnerabilities that appear real but are generated by LLMs and lack real-world impact,” said Prins. “These low-signal submissions can create noise that undermines the efficiency of security programs.”

Prins added that reports that contain “hallucinated vulnerabilities, vague technical content, or other forms of low-effort noise are treated as spam.”

Casey Ellis, the founder of Bugcrowd, said that there are definitely researchers who use AI to find bugs and write the reports that they then submit to the company. Ellis said they are seeing an overall increase of 500 submissions per week.

“AI is widely used in most submissions, but it hasn’t yet caused a significant spike in low-quality ‘slop’ reports,” Ellis told TechCrunch. “This’ll probably escalate in the future, but it’s not here yet.”

Ellis said that the Bugcrowd team that analyzes submissions reviews the reports manually using established playbooks and workflows, as well as with machine learning and AI “assistance.”

To see if other companies, including those that run their own bug bounty programs, are also receiving an increase in invalid reports or reports containing non-existent vulnerabilities hallucinated by LLMs, TechCrunch contacted Google, Meta, Microsoft, and Mozilla.

Damiano DeMonte, a spokesperson for Mozilla, which develops the Firefox browser, said that the company has “not seen a substantial increase in invalid or low-quality bug reports that would appear to be AI-generated,” a...