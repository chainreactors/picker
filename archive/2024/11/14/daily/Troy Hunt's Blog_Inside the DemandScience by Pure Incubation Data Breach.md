---
title: Inside the DemandScience by Pure Incubation Data Breach
url: https://www.troyhunt.com/inside-the-demandscience-by-pure-incubation-data-breach/
source: Troy Hunt's Blog
date: 2024-11-14
fetch_date: 2025-10-06T19:32:17.258440
---

# Inside the DemandScience by Pure Incubation Data Breach

* [Home](https://www.troyhunt.com/)
* [Workshops](https://www.troyhunt.com/workshops/)
* [Speaking](https://www.troyhunt.com/speaking/)
* [Media](https://www.troyhunt.com/media/)
* [About](https://www.troyhunt.com/about/)
* [Contact](https://www.troyhunt.com/contact/)
* [Sponsor](https://www.troyhunt.com/sponsorship/)

**Sponsored by:**

# Inside the DemandScience by Pure Incubation Data Breach

13 November 2024

Apparently, before a child reaches the age of 13, [advertisers will have gathered more 72 *million* data points on them](https://humanrights.gov.au/about/news/opinions/protect-children-data-surveillance?ref=troyhunt.com). I knew I'd seen a metric about this sometime recently, so I went looking for "7,000", which perfectly illustrates how unaware we are of the extent of data collection on all of us. I started [Have I Been Pwned](https://haveibeenpwned.com/?ref=troyhunt.com) (HIBP) in the first place because I was surprised at where my data had turned up in breaches. 11 years and 14 billion breached records later, I'm *still* surprised!

Jason (not his real name) was also recently surprised at where his data had appeared. He found it in a breach of a service called "Pure Incubation", a company whose records had appeared on a popular hacking forum earlier this year:

> [#DataLeak](https://twitter.com/hashtag/DataLeak?src=hash&ref_src=twsrc%5Etfw&ref=troyhunt.com) Alert ⚠️⚠️⚠️
>
> 🚨Over 183 Million Pure Incubation Ventures Records for Sale 🚨
>
> 183,754,481 records belonging to Pure Incubation Ventures ([https://t.co/m3sjzAMlXN](https://t.co/m3sjzAMlXN?ref=troyhunt.com)) have been put up for sale on a hacking forum for $6,000 negotiable.
>
> Additionally, the threat actor with… [pic.twitter.com/tqsyb8plPG](https://t.co/tqsyb8plPG?ref=troyhunt.com)
>
> — HackManac (@H4ckManac) [February 28, 2024](https://twitter.com/H4ckManac/status/1762838131055702398?ref_src=twsrc%5Etfw&ref=troyhunt.com)

When Jason found his email address and other info in this corpus, he had the same question so many others do when their data turns up in a place they've never heard of before - how? *Why?!* So, he asked them:

> I seem to have found my email in your data breach. I am interested in finding how my information ended up in your database.

To their credit, he got a very comprehensive answer, which I've included below:

![](https://www.troyhunt.com/content/images/2024/11/image.png)

Well, that answers the "how" part of the equation; they've aggregated data from public sources. And the "why" part? It's the old "data is the new oil" analogy that recognises how valuable our info is, and as such, there's a market for it. There are lots of terms used to describe what DemandScience does, including "B2B demand generation", "buyer intelligence solutions provider", "empowering technology companies to accelerate ROI", "supercharging pipelines" and "account intelligence". Or, to put it in a more lay-person-friendly fashion, they sell data on people.

DemandScience is what we refer to as a "data aggregator" in that they combine identity data from multiple locations, bundle it up, and then sell it. Occasionally, data aggregators end up having sizeable data breaches; before today, HIBP already contained [Adapt](https://haveibeenpwned.com/PwnedWebsites?ref=troyhunt.com#Adapt) (9M records), [Data & Leads](https://haveibeenpwned.com/PwnedWebsites?ref=troyhunt.com#DataAndLeads) (44M records), [Exactis](https://haveibeenpwned.com/PwnedWebsites?ref=troyhunt.com#Exactis) (132M records), [Factual](https://haveibeenpwned.com/PwnedWebsites?ref=troyhunt.com#Factual) (2M records), and [You've Been Scraped](https://haveibeenpwned.com/PwnedWebsites?ref=troyhunt.com#YouveBeenScraped) (66M records). According to DemandScience, "none of our current operational systems were exploited", yet simultaneously, "the leaked data originated from a system that has been decommissioned". So, it's a breach of an old system.

Does it matter? I mean, if it's just public data, should people care? Jason cared, at least enough to make the original enquiry and for DemandScience to look him up and realise he's not in their *current* database. Still, he existed in the breached one (I later sent Jason his record from the breach, and he confirmed the accuracy). As I often do in these cases, I reached out to a bunch of recent HIBP subscribers in the breach and asked them three simple questions:

1. Is the data about you accurate and if not, which bits are wrong?
2. Is this data you would consider to be in the public domain already?
3. Would you expect to be notified about your data being used in this fashion, and consequently appearing a breach?

The answers were all the same: the data is accurate, it's already in the public domain, and people aren't too concerned about it appearing in this breach. Well that was easy 🙂 However...

There are two nuances that aren't captured here, and the first one is that this *is* valuable data, that's why DemandScience sells it! It comes back to that "new oil" analogy and if you have enough of it, you can charge good money for it. Companies typically use data such as this to do precisely the sort of catchphrasey stuff the company talks about, primarily around maximising revenue from their customers by understanding them better.

The second nuance is that whilst this data may already be in the public domain, did the owners of it expect it to be used in this fashion? For example, if you publish your details in a business directory, is your expectation that this info may then be sold to other companies to help them upsell you on their products? Probably not. And if, like many of the records in the data, someone's row is accompanied by their LinkedIn profile, would they expect that data to matched and sold? I suggest the responses would likely be split here, and that in itself is an important observation: how we view the sensitivity of our data and the impact of it being exposed (whether personal or business) is extremely personal. Some people take the view of "I have nothing to hide", whilst others become irate if even just their email address is exposed.

Whilst considering how to add more insights to this blog post, I thought I'd do a quick check on just one more email address:

```
"54543060",,"0","TROY","HUNT","PO BOX 57",,"WEST RYDE",,,"AU","61298503333",,,,"troy.hunt@pfizer.com","pfizer.com","PFIZER INC",,"250-499","$50 - 99 Million","Healthcare, Pharmaceuticals and Biotech","VICE PRESIDENT OF INFORMATION TECHNOLOGY","VP Level","2834",,"Senior Management (SVP/GM/Director)","IT",,"1","GemsTarget INTL","GEMSTARGET_INTL_648K_10.17.18",,,,,,,,,"18/10/2018 05:12:39","5/10/2021 16:47:56","PFIZER.COM",,,,,"IT Management General","Information Technology"
```

I'll be entirely transparent and honest here - my exact words after finding this were "*motherfucker!*" True story, told uncensored here because I want to impress on the audience how *I* feel when my data turns up somewhere publicly. And I do feel like it's "my" data; it's certainly *my* name and even though it's my old Pfizer email address [I've not used for almost a decade now](https://www.troyhunt.com/today-marks-two-important-milestones/), that also has my name in it. *My* job title is also there... and it's completely wrong! I never had a VP-level role, even though the other data around my tech role is at least in the vicinity of being correct. But other than the initial shock of finding myself in yet another data breach, personally, I'm in the same boat as the HIBP subscribers I contacted, and this doesn't bother me too much. But I also agree with the following responses I received to my third question:

> I think it is useful to be notified of such breaches, even if it is just to confirm no sensitive data has been compromised. As I said, our IT department recently notified me that some of my data was leaked and a pre-emptive password reset was enforced as they didn't know what was leaked.

> It would be good to see it as an in...