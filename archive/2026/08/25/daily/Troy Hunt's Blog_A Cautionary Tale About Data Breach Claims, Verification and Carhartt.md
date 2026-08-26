---
title: A Cautionary Tale About Data Breach Claims, Verification and Carhartt
url: https://www.troyhunt.com/a-cautionary-tale-about-data-breach-claims-verification-and-carhartt/
source: Troy Hunt's Blog
date: 2026-08-25
fetch_date: 2026-08-26T03:06:57.517574
---

# A Cautionary Tale About Data Breach Claims, Verification and Carhartt

* [Home](https://www.troyhunt.com/)
* [Workshops](https://www.troyhunt.com/workshops/)
* [Speaking](https://www.troyhunt.com/speaking/)
* [Media](https://www.troyhunt.com/media/)
* [About](https://www.troyhunt.com/about/)
* [Contact](https://www.troyhunt.com/contact/)
* [Sponsor](https://www.troyhunt.com/sponsorship/)

**Sponsored by:**

# A Cautionary Tale About Data Breach Claims, Verification and Carhartt

26 August 2026

You're not going to believe this, but turns out you can't always take criminals at their word. Actually, I'll walk that back a bit as it may not even be the cybercrime guys who got this wrong, but it all starts here:

> 🚨Cyber Alert ‼️
>
> 🇺🇸US - 𝗖𝗮𝗿𝗵𝗮𝗿𝘁𝘁
>
> ShinyHunters hacking group claims to have compromised Carhartt and allegedly stolen more than 50 GB of compressed data containing millions of customer records, employee information, customer metadata, loyalty-related information, and… [pic.twitter.com/BvzsEQS54l](https://t.co/BvzsEQS54l?ref=troyhunt.com)
>
> — Hackmanac (@H4ckmanac) [August 13, 2026](https://x.com/H4ckmanac/status/2087815969796149378?ref_src=twsrc%5Etfw&ref=troyhunt.com)

My usual Have I Been Pwned (HIBP) workflow after a breach emerges is to run [our open source Email Address Extractor tool](https://github.com/HaveIBeenPwned/EmailAddressExtractor/?ref=troyhunt.com) over the corpus of data, get a count of the unique addresses then drop it into the processing pipeline. Having a count helps prioritise: it's roughly the same effort to process a breach with 10M addresses in it as it is 100k addresses, but we obviously reach 100x more people with the larger corpus so that goes first. So, following the release of the Carhartt data above, I ran the tool and got 24,876,077 addresses. That's a biggy, let's dive in.

One of the first things I do when analysing a breach is look for news and industry commentary. Once you get through all the results for class actions ([ugh](https://www.troyhunt.com/data-breaches-class-actions-and-ambulance-chasing/)), you usually find various other services and news sites reporting on the incident. One such example (which I won't name, because they're wrong) cited a very similar number to my initial pass, which at face value, reinforced my thinking. But here's where it all takes a turn because, inevitably, this is where the other analysts stopped...

I've been using OpenClaw pretty extensively this year to help with a number of tasks, including breach analysis. Here's how I normally begin (timestamps are AEST and yes, I called it "PwnedClaw"):

```
[24/08/2026 17:30] Troy Hunt: Let's look at the ShinyHunters Carhartt breach. I'm seeing nearly 25M unique email addresses so it's very large, tell me about what they do.

[24/08/2026 17:30] PwnedClaw: Carhartt is an American workwear brand founded in 1889, headquartered in Dearborn, Michigan. They make rugged, durable clothing primarily for tradespeople and outdoor workers: heavy-duty jackets, bibs, coveralls, work pants, boots, and accessories. Think construction workers, farmers, hunters.

They've also crossed over into streetwear/fashion in recent years (particularly through Carhartt WIP, their Work In Progress line), which massively expanded their demographic beyond blue-collar workers into urban fashion, skateboarding, and hip-hop culture. That crossover likely explains a 25M email count — they're not just selling to contractors anymore, they're a mainstream lifestyle brand.

Strong US base but significant global presence, especially in Europe where WIP is huge.

For HIBP context: broad demographic mix (blue-collar workers + fashion/streetwear), real names, physical addresses, and purchase history are likely present given it's a retail breach. Want me to pull the tracker entry for current status?
```

Ok, cool, nothing too revolutionary there. Let's start analysing the data, and the first thing I do is begin with the report of our open source [Email Address Extractor](https://github.com/HaveIBeenPwned/EmailAddressExtractor/?ref=troyhunt.com) tool, which lists every file an address was found in, and then how many unique ones are in there:

```
[24/08/2026 17:32] Troy Hunt: Let's start looking at data, and we'll begin with the email extractor report at "\scratch\Carhartt\Carhartt.txt.report.txt"

[24/08/2026 17:32] PwnedClaw: Interesting. The data is from Databricks (their analytics/data lakehouse platform) and follows the TPC-DS benchmark schema (tpcds_sf1000) — that's a standard retail analytics benchmark format. The "sf1000" means scale factor 1000, which is massive.

Key observations:

• All emails are in customer_chunk_XXXX.csv files, numbered 0000-0599+, so ~600 chunks
• Each chunk has ~19,300 unique emails, remarkably uniform distribution
• ~600 chunks × ~19,300 = ~11.6M from this directory alone — but you said ~25M total, so there are likely more directories

The TPC-DS schema is telling — it means this was Carhartt's customer analytics warehouse in Databricks, not their production transactional database. TPC-DS models: customer demographics, store sales, web sales, catalog sales, dates, etc. So the data likely includes purchase history and behavioral analytics on top of PII.

Want me to look at an actual chunk file to see what columns are present?
```

Think of it as using the AI to distil large volumes of information down into something much more workable. In this case, I gave it four of the files in question and let the analysis run:

```
[24/08/2026 17:33] PwnedClaw: The columns from the TPC-DS customer table:

• c_customer_sk / c_customer_id — internal IDs
• c_current_cdemo_sk — customer demographic key (links to demo table with age/gender/education/marital status/income band)
• c_current_hdemo_sk — household demographic key
• c_current_addr_sk — current address key (links to full address table)
• c_first_shipto_date_sk / c_first_sales_date_sk — date of first purchase/shipment
• c_salutation — Mr/Mrs/Miss/Sir etc.
• c_first_name / c_last_name
• c_preferred_cust_flag — loyalty/preferred customer flag
• c_birth_day / c_birth_month / c_birth_year — full DOB
• c_birth_country
• c_login — empty in the samples
• c_email_address
• c_last_review_date_sk / c_last_review_date

So: full name, email, DOB, salutation, birth country, preferred customer status, first purchase date. Address is a foreign key here (in a separate address table that's presumably also in the dump).

Notable: c_login appears empty — so no passwords in this table. DOB is split across three columns which is a bit unusual but all three are there. Birth year goes back to 1949 in the sample, so this spans a wide age range.

Want me to check how many rows have DOB fully populated, and whether there are other tables in the dump (address, demographics) in what you have locally?
```

I'll save you from all the to-and-fro of my questions and PwnedClaw's responses, here's where it gets interesting and where AI plays a genuinely valuable role:

```
[24/08/2026 17:41] PwnedClaw: TLD anomaly worth flagging:

• 4M .edu and 3.9M .org is extremely high for a retail brand. That's likely noise from the TPC-DS synthetic data generation mixed with real records, or it could indicate Carhartt ran promotions targeting institutions. Worth sanity checking a sample of those.

Want me to pull 20 random .edu and .org samples to see if they look real or synthetic?
```

Huh, yeah, that feels odd. Let's drill down further, and just a quick caveat: I'm *highly* confident that all the data I'm about to show is fabricated and that I'm not inadvertently putting someone else's PII on display here.

```
[24/08/2026 17:47] Troy Hunt: Give me some examples of what you consider synthetic addresses

[24/08/2026 17:48] PwnedClaw: From the earlier sample:

Clearly synthetic (TPC-DS generated):

• roy.griffin@mbfhz82d0vkpes4x.edu — random hex-like domain
• violet.day@ob7.edu — 3-char alphanumeric
• michael.ware@c.edu — single character domain
• manuel.baugh@p.edu — single character domain
• april.garza@r3zc...