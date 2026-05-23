---
title: Techie claims Trump Mobile website was leaking thousands of people's data
url: https://www.theregister.com/security/2026/05/22/trump-mobile-site-leaks-customer-data-as-phone-finally-ships/5244828
source: www.theregister.com - Articles
date: 2026-05-22
fetch_date: 2026-05-23T05:43:04.756316
---

# Techie claims Trump Mobile website was leaking thousands of people's data

[Jump to main content](#main)

Search

TOPICS

* Security
  + [All Security](/security)
  + [Cyber-crime](/cyber_crime)
  + [Patches](/patches)
  + [Research](/research)
  + [CSO](/cso)
* Off-Prem
  + [All Off-Prem](/off_prem)
  + [Edge + IoT](/edge_iot)
  + [Channel](/channel)
  + [PaaS + IaaS](/tag/paas-iaas)
  + [SaaS](/saas)
* On-Prem
  + [All On-Prem](/on_prem)
  + [Systems](/systems)
  + [Storage](/storage)
  + [Networks](/networks)
  + [HPC](/hpc)
  + [Personal Tech](/personal_tech)
  + [Cx0](/cxo)
  + [Public Sector](/public-sector)
* Software
  + [All Software](/software)
  + [AI + ML](/tag/ai-ml)
  + [Applications](/applications)
  + [Databases](/databases)
  + [DevOps](/devops)
  + [OSes](/oses)
  + [Virtualization](/virtualization)
* Offbeat
  + [All Offbeat](/offbeat)
  + [Columnists](/columnists)
  + [Science](/science)
  + [BOFH](/bofh)
  + [Legal](/legal)
  + [Bootnotes](/bootnotes)
  + [Site News](/site_news)
  + [About Us](https://www.theregister.com/about_us)

* Special Features
  + [All Special Features](/tag/special_features)
  + [HPE: AI Explainers](/explainer/ai-explainer)
  + [RSA Conference](/special_features/rsa)
  + [Agentic AI](/special_features/agentic_ai)
  + [The Future of the Datacenter](/special_features/future_of_the_datacenter)
  + [AWS:Reinvent](/special_features/aws_reinvent)
  + [Nvidia GTC](/special_features/nvidia_gtc)
  + [SC25](/special_features/2025_11_sycomp_supercomputing)
  + [Supercomputing Month](/special_features/2025_11_supercomputing_month)
* Vendor Voice
  + [All Vendor Voice](https://vendorvoice.theregister.com/)
  + [Infinidat](https://vendorvoice.theregister.com/infinidat/)
  + [Everpure](https://vendorvoice.theregister.com/everpure/)
  + [Rubrik](https://vendorvoice.theregister.com/rubrik/)
  + [Make it real with Capgemini and AWS](https://vendorvoice.theregister.com/aws_capgemini/)
  + [Money Movement Hub](https://vendorvoice.theregister.com/aws_fis/)
  + [ZTE](https://vendorvoice.theregister.com/zte_news_and_stories/)
  + [Nutanix: Scale Kubernetes. Not Chaos.](https://vendorvoice.theregister.com/nutantix_cloud_native_apps/)
  + [AWS New Horizon](https://vendorvoice.theregister.com/aws_new_horizon/)
* Resources
  + [Intelligence](https://intelligence.theregister.com)
  + [Webinars & Events](https://intelligence.theregister.com/events/list/)
  + [Newsletters](https://account.theregister.com/login?r=https%3A%2F%2Faccount.theregister.com%2Fedit%2Fnewsletter%2F)

Search

[![Go to frontpage. Logo, The Register](/view-resources/dachser2/public/theregister/logo.svg)](https://www.theregister.com)

[![Go to frontpage. Logo, The Register](/view-resources/dachser2/public/theregister/logo.svg)](https://www.theregister.com)

[![Go to frontpage. Logo, The Register](/view-resources/dachser2/public/theregister/logo.svg)](https://www.theregister.com)

* [Sign in](https://account.theregister.com/login)

* [Datacenter](/tag/datacenter)
* [Security](/security)
* [Microsoft](/tag/microsoft)
* [AWS](/tag/aws)
* [Developer](/tag/developer)
* [Open Source](/tag/open%20source)
* [IT Careers](/tag/tech%20jobs)
* [Columnists](/tag/columnists)
* [Who, Me?](/tag/who%20me)
* [On Call](/tag/on%20call/)

REG AD

[security](https://www.theregister.com/security)

# Techie claims Trump Mobile website was leaking thousands of people's data

Customers' info potentially handed to anyone who could send an HTTP request

Connor Jones
[Connor
Jones](https://www.theregister.com/author/connor-jones)
Cybersecurity reporter

Published
fri 22 May 2026 // 11:59 UTC

The US President’s oft-maligned Trump Mobile venture may be facing another setback after a security buff claims he discovered a now-plugged website vulnerability that he says was leaking what could be tens of thousands of suckers' customers' details.

The individual behind the discovery, who goes by "Louis," says he's a self-taught tech tinkerer and described himself as "just a nerd between jobs with too much time on my hands." He reckons the website’s data could be scooped up with a simple POST request.

“It wasn't SQL. That wouldn't be as bad,” he told The Register. “It was a really simple HTTP request. POST, and then just asking for the info I wanted, basically.”

REG AD

More than 27,000 people who ordered from Trump Mobile, the President’s all-American smartphone and cell service brand, had their data flimsily secured online, Louis claimed.

REG AD

Louis, a long-serving IT professional who refuses to be called a security researcher, said the types of data he was able to gather included: first and last names, primary addresses, secondary addresses, email addresses, phone numbers, customer/account numbers, "enrollment ID" (pre-order number), and whether the order was placed by phone or online.

“I discovered it first by looking into the site to see if I could find how many orders there actually were, and noticing some API endpoints,” he added. “I tried a couple of basic commands, and then it started showing whatever data I wanted.

“It was as easy as going to the website and writing a very simple HTTP POST request into the console.”

## MORE CONTEXT

* [### Trump's gold-plated smartphone can't seem to decide which design to copy](/on-prem/2025/08/22/trump-mobile-steals-samsung-spigen-snap-for-t1-ad/363177)
* [### Lawmakers urge FTC to probe Trump Mobile over 'deceptive' marketing](/on-prem/2026/01/16/ftc-urged-to-examine-trump-mobile-marketing/4423851)
* [### Florida man expands crypto empire with new wireless service and phone](/on-prem/2025/06/16/trump-branded-mvno-and-gold-colored-phone-launches/1403211)
* [### Trump jumps from 'anything goes' to 'strict regulation' AI policy](/columnists/2026/05/08/trump-jumps-from-anything-goes-to-strict-regulation-ai-policy/5234687)

The website flaw only allowed him to return ten customer records at a time, he said, but these records all contained a customer number, which Louis used to loop through them all.

In the space of an hour, the method allowed him to access the records of around 5,000 Trump Mobile customers, he claimed.

After confirming the issue was valid and that all the data his script scooped up was deleted, Louis tried to disclose his findings to Trump Mobile, and anyone else who could take action, but received no response, although someone appears to have fixed the issue.

The Register also tried contacting Trump Mobile but similarly received nothing in return.

Out of options for disclosure, Louis decided to go public, informing two prominent YouTube creators and known orderers of the Trump T1 phone, [Stephen “Coffeezilla” Findeisen](https://www.youtube.com/watch?v=voxXDDq58Bk) and [Charles “penguinz0” White Jr.](https://www.youtube.com/watch?v=c8TwGH1B5wA), whose respective videos covering his findings have jointly gathered millions of views.

REG AD

## Trump T1 begins shipping

Trump Mobile’s flagship device, the  T1 Android smartphone with the gold-colored casing, began showing up at pre-order customers’ doors this week, after originally being slated for an August 2025 release.

The brand’s entire schtick since first being [announced in June 2025](https://www.theregister.com/on-prem/2025/06/16/trump-branded-mvno-and-gold-colored-phone-launches/1403211), around the time of a significant escalation in US-China trade war conflict, was that everything was going to be “Made in America.”

Early [renders](https://www.theregister.com/on-prem/2025/08/22/trump-mobile-steals-samsung-spigen-snap-for-t1-ad/363177) of the proposed T1 showed what appeared to be an iPhone-like device – gold-colored, of course – but those who [received their orders this week](https://www.youtube.com/watch?v=8d8EojYVtCs) confirm it is just a reskinned HTC U-24 Pro, a mid-range Android from the Taiwanese tech biz which first hit the market in June 2024.

The American flag embossed on the back of the device also only has 11 stripes instead of 13, although all the stars are present and accounted for, at least.

When the President’s sons launched the...