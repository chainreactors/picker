---
title: Browser fingerprint tool shows how easy you are to track using the latest sneaky tricks
url: https://www.theregister.com/security/2026/08/24/browser-fingerprint-tool-shows-how-easy-you-are-to-track-using-the-latest-sneaky-tricks/5292015
source: www.theregister.com - Articles
date: 2026-08-24
fetch_date: 2026-08-25T03:00:57.513094
---

# Browser fingerprint tool shows how easy you are to track using the latest sneaky tricks

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

security

# Browser fingerprint tool shows how easy you are to track using the latest sneaky tricks

Glassbox dev admits he had some help from Claude to build locally running tool

Brandon Vigliarolo
[Brandon
Vigliarolo](https://www.theregister.com/author/brandon-vigliarolo)
GOVERNMENT AND IT NEWS REPORTER

Published
mon 24 Aug 2026 // 22:07 UTC

### MOST POPULAR

* [SAAS

  #### Salesforce partners not seeing meaningful revenue from Agentforce AI platform, report says](/saas/2026/08/21/salesforce-partners-not-seeing-meaningful-revenue-from-agentforce-ai-platform-report-says/5291167)
* [AI and ml

  #### Google buys crashed airline Spirit’s data at auction, because AI](/ai-and-ml/2026/08/18/google-buys-crashed-airline-spirits-data-at-auction-because-ai/5288962)
* [SAAS

  #### GitHub blames 8-hour outage on autoscaling fail and VS Code retry storm](/saas/2026/08/19/github-blames-8-hour-outage-on-autoscaling-fail-and-vs-code-retry-storm/5289547)
* [security

  #### Expired credit cards revived by researchers to make unauthorized payments](/security/2026/08/18/expired-credit-cards-revived-by-researchers-to-make-unauthorized-payments/5289229)
* [ofbeat

  #### NASA estimates the size of the hole SpaceX made in the moon](/offbeat/2026/08/19/nasa-estimates-the-size-of-the-hole-spacex-made-in-the-moon/5289425)

If you're curious how easily tech companies can fingerprint your browser and device and potentially single them out from the crowd, a new utility [Glassbox](https://glassbox.codecanary.org/) will show you.

Aside from pinging a public geolocation API, it runs entirely in a user’s browser and doesn’t ship any info out to the web while acting just like all the various trackers, anti-fraud scripts, and other browser fingerprinting tricks one is likely to encounter online.

Unlike some [other](https://amiunique.org/fingerprint) available [tools](https://coveryourtracks.eff.org/) that do the same, Glassbox provides a whole bunch of raw, unfiltered data you can sift through to see what makes your browser stand out, along with an estimate of how identifiable its fingerprint may be.

REG AD

In this vulture’s testing, Glassbox's estimate ranged from 99 percent in the Chrome window I use daily for work to a low of 56 percent in Tor Browser with an active circuit.

REG AD

“The ‘identifiability’ number is an honest model, not a measurement,” Glassbox developer David Dale said of his tool in a Hacker News [thread](https://news.ycombinator.com/item?id=49421948). “It sums published per-signal entropy, discounts your browser masks, and caps at the [~33 bits](https://www.theregister.com/security/2009/05/21/scrubbed-geo-location-data-not-so-anonymous-after-all/1085602) needed to single out one person on Earth.”

Dale added in the thread that, since it runs locally, that identifiability number is an estimate, as Glassbox doesn’t have a live population to pull against. AmIUnique and the EFF’s Cover Your Tracks, the other tools mentioned above, provide real population numbers, he noted.

Dale got the idea for GlassBox after learning about silent sawtooth waves used by fingerprinting code found on Alibaba's AliExpress site to [identify browsers using audio](https://www.theregister.com/security/2026/08/24/aliexpress-accused-of-fingerprinting-shoppers-with-silent-audio-trick-that-also-muted-a-devs-headphones/5291662).

Rather than fork one of the existing open source tools - both EFF's Cover Your Tracks and AmIUnique have GitHub repos - he decided to build his own, with some help from AI.

“I'm a solo entrepreneur and long-time security engineer; tools like Claude Code have made it much easier to polish ideas and offer the useful ones to a wider audience,” Dale told us in an email.

“I knew a fair number of fingerprinting methods but not that one, and I wanted to see all of them in one place, running against my own browser,” he said on Hacker News.

In other words, Glassbox factors Alibaba’s tricks into its identifiability estimates alongside 30 other probes for unique browser data - things like canvas, WebGL, font libraries, WASM features, API matrices, and cross-site login states.

According to Glassbox, my particular Chrome session I use for work is unique to around 1 in 7.6 billion browsers, and my IP address narrows that further (my ISP...