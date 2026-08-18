---
title: Code fixers have fired up the AI warp drive. Strange new worlds await
url: https://www.theregister.com/columnists/2026/08/17/code-fixers-have-fired-up-the-ai-warp-drive-strange-new-worlds-await/5287681
source: www.theregister.com - Articles
date: 2026-08-17
fetch_date: 2026-08-18T02:54:05.464220
---

# Code fixers have fired up the AI warp drive. Strange new worlds await

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
  + [Edge and IoT](/edge_iot)
  + [Channel](/channel)
  + [PaaS and IaaS](/tag/paas-iaas)
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
  + [AI and ML](/tag/ai%20and%20ml)
  + [Applications](/applications)
  + [Databases](/databases)
  + [DevOps](/devops)
  + [OS Platforms](/tag/os%20platforms)
  + [Virtualization](/virtualization)
* Offbeat
  + [All Offbeat](/offbeat)
  + [Columnists](/columnists)
  + [Science](/science)
  + [BOFH](/bofh)
  + [Legal](/legal)
  + [Site News](/site_news)
  + [About Us](https://www.theregister.com/about_us)

* Special Features
  + [All Special Features](/special_features)
  + [Cloud Infrastructure Month 2026](/special_features/cloud_infrastructure_month_2026)
  + [HPE: AI Explainers](/explainer/ai-explainer)
  + [Agentic AI](/special_features/agentic_ai)
  + [The Future of the Datacenter](/special_features/future_of_the_datacenter)
  + [AWS:Reinvent](/special_features/aws_reinvent)
  + [Nvidia GTC](/special_features/nvidia_gtc)
  + [Supercomputing Month](/special_features/2025_11_supercomputing_month)
  + [Computex 2026](/special_features/computex)
  + [AI Infrastructure Month 2026](/special_features/ai_infrastructure_month_2026)
  + [The State of Storage 2026](/special_features/state_of_storage_2026)
  + [RSA Conference](/special_features/rsa)
* Vendor Voice
  + [All Vendor Voice](https://vendorvoice.theregister.com/)
  + [Modernizing Financial Services with FIS and AWS](https://vendorvoice.theregister.com/aws_fis_capital_markets/)
  + [Barco](https://vendorvoice.theregister.com/barco/)
  + [Infinidat](https://vendorvoice.theregister.com/infinidat/)
  + [Everpure](https://vendorvoice.theregister.com/everpure/)
  + [Rubrik](https://vendorvoice.theregister.com/rubrik/)
  + [Make it real with Capgemini and AWS](https://vendorvoice.theregister.com/aws_capgemini/)
  + [Money Movement Hub](https://vendorvoice.theregister.com/aws_fis/)
  + [ZTE](https://vendorvoice.theregister.com/zte_news_and_stories/)
  + [Nutanix: Scale Kubernetes. Not Chaos.](https://vendorvoice.theregister.com/nutantix_cloud_native_apps/)
  + [AWS New Horizon](https://vendorvoice.theregister.com/aws_new_horizon/)
  + [Digicert](https://vendorvoice.theregister.com/digicert)
  + [Netscout](https://vendorvoice.theregister.com/netscout)
* Resources
  + [Intelligence](https://intelligence.theregister.com)
  + [Webinars & Events](https://intelligence.theregister.com/events/list/)
  + [Newsletters](https://account.theregister.com/login?r=https%3A%2F%2Faccount.theregister.com%2Fedit%2Fnewsletter%2F)

Search

[![Go to frontpage. Logo, The Register](/view-resources/dachser2/public/theregister/logo.svg)](https://www.theregister.com)

[![Go to frontpage. Logo, The Register](/view-resources/dachser2/public/theregister/logo.svg)](https://www.theregister.com)

[![Go to frontpage. Logo, The Register](/view-resources/dachser2/public/theregister/logo.svg)](https://www.theregister.com)

* [Sign in](https://account.theregister.com/login)

* [AI](/tag/ai%20and%20ml)
* [Security](/security)
* [AWS](/tag/aws)
* [Microsoft](/tag/microsoft)
* [Developer](/tag/devops)
* [Open Source](/tag/open%20source)
* [BOFH](/tag/bofh)
* [Who, Me?](/tag/who%20me)
* [On Call](/tag/on%20call/)
* [Podcasts](/tag/kettle)

REG AD

COLUMNISTS

# Code fixers have fired up the AI warp drive. Strange new worlds await

With more patches per month than at a pirate convention, the bug must be an endangered species. Well, about that

![Rupert G](https://image.theregister.com/1664769.webp?imageId=1664769&width=360&height=360)

Rupert Goodwins
[Rupert
Goodwins](https://www.theregister.com/author/rupert-goodwins)
Register columnist

Published
mon 17 Aug 2026 // 10:04 UTC

It is the best of times, it is the worst of times – especially if your job is keeping systems patched and up to date. Microsoft has gone from 60-90 Windows security fixes per month last year to a [record of 600+ this July](https://www.theregister.com/security/2026/07/14/patchpocalypse-now-microsoft-tops-last-months-record-with-622-patch-tuesday-cves/5271434). [Oracle](https://www.theregister.com/security/2026/07/23/oracle-drops-1449-security-patches-like-its-the-new-normal/5277114) and [Linux](https://www.theregister.com/os-platforms/2026/08/10/linus-torvalds-says-ai-has-made-huge-linux-kernel-updates-the-new-normal/5285268) are following the same path, and they are very much not alone. The good news is that a lot of bad things are getting fixed very quickly. The bad news is that patches can bring side effects of their own.

There are two mechanisms at work, both driven by the source of and solution to all our woes, AI. The first is that the appropriate LLMs and their humans have got very good at bug hunting. Like demon archaeologists, they've started thrashing their way down through the stratified layers of long-established code bases, bringing a huge backlog of previously buried bugs to the surface.

Complicating matters, LLMs are also writing an awful lot of code, some of which is not very good. It is making its way into production for all the old reasons – marketing-led deadline pressure, shape-shifting specs, and Brownian goalposts – until the implacable hostilities of reality spit it back out.

REG AD

The result is a very interesting dynamic of conflicting pressures that is changing the nature of patches. It's easy to assume that the current explosion of bug fixes will die down as the code bases are repeatedly refined and purified, and that this time next year we'll be seeing rather fewer patches than in the pre-AI days, let alone today. It's a nice thought. Similarly, with the old code in a new state of grace, attention can turn to properly generating and testing the AI-powered stuff, so that it too calms down.

REG AD

Other factors will work against this. Newer models may find new classes of bugs or start refactoring for efficiency or structural reasons. Not all patches fix bugs, and not all bugs are vulnerabilities. CVEs are easy to count, but aren't the full story. The pressure to release early won't go away either; better tools often encourage greater recklessness. Vibe check, anyone? Finally, the bad guys aren't going away and will be using all the new shiny to keep up their side of the arms race.

## MORE CONTEXT

* [### Smart glasses are only smart if we train them to be good. Then they'll be fantastic](/columnists/2026/08/10/smart-glasses-are-only-smart-if-we-train-them-to-be-good-then-theyll-be-fantastic/5284545)
* [### Claude Code is revolutionizing digital archaeology. Enterprise better dig it](/columnists/2026/08/03/claude-code-is-revolutionizing-digital-archaeology-enterprise-better-dig-it/5281676)
* [### FOSS smashed one Microsoft monopoly. After 20 years of failure, it's time to smash another](/columnists/2026/07/27/foss-smashed-one-microsoft-monopoly-after-20-years-of-failure-its-time-to-smash-another/5278040)
* [### Airbus takes flight from AWS. What happens next is critical](/columnists/2026/07/20/airbus-takes-flight-from-aws-what-happens-next-is-critical/5274109)

This whole system of conflicting pressures in a morphing environment has not been well studied, and the future shape of patching is unclear. One analogy suggests itself, that of stellar evolution.

Astrophysics fans know the score. After a star condenses out of gas and dust, gravity compresses its core until it becomes hot and dense enough for nuclear fusion. Hydrogen nuclei fuse to create helium, releasing energy that pushes outward against the gravity trying to squeeze the core further, and the star s...