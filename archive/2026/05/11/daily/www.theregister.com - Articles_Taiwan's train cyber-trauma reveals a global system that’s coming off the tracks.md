---
title: Taiwan's train cyber-trauma reveals a global system that’s coming off the tracks
url: https://www.theregister.com/security/2026/05/11/taiwans-train-cyber-trauma-reveals-a-global-system-thats-coming-off-the-tracks/5237248
source: www.theregister.com - Articles
date: 2026-05-11
fetch_date: 2026-05-12T05:39:15.507984
---

# Taiwan's train cyber-trauma reveals a global system that’s coming off the tracks

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
  + [PaaS + IaaS](/paas_iaas)
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
  + [AI + ML](/ai_ml)
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

[Security](https://www.theregister.com/security)

# Taiwan's train cyber-trauma reveals a global system that’s coming off the tracks

That’s not a radio. THIS is a radio

![Rupert Goodwins](https://image.theregister.com/1664769.webp?imageId=1664769&width=360&height=360)

Rupert Goodwins
[Rupert
Goodwins](https://www.theregister.com/author/rupert-goodwins)
Register columnist

Published
mon 11 May 2026 // 09:30 UTC

OPINION There are three little words to make the heart beat faster in anyone who knows what they mean: critical infrastructure resilience. If you run that infrastructure or a country dependent on it, you need energy, communication and transport to be impregnable to cyber attacks.

This is doubly so if that country is five minutes by incoming missile from an implacable hyper-competent enemy sworn to invade you. One that is building and equipping its military as fast as it can with this one thing in mind. One with the most invasive and brazen state hacking machinery on the planet.

Thus it was a very bad day indeed when [Taiwan’s entire bullet train system was disabled for nearly an hour by an unknown attacker](https://www.theregister.com/cyber-crime/2026/05/06/taiwan-student-pwns-rail-comms-halts-high-speed-trains/5230489). It got even worse when that attacker turned out not to be the implacable and hyper-resourced state actor over the Taiwan Strait, but a university student with a yen for radio and some kit he bought online. On the one hand, it’s good to see the good repair of the grand tradition of young hackers causing havoc from their bedrooms. On the other, WTRF?

REG AD

The information released by the Taiwanese authorities is scant on details, but enough to be pretty sure what actually happened. It’s bad news not just for Taiwan but for more than [100 countries that also use the TETRA two-way radio standard](https://www.chelton.com/tetra-around-the-world/) involved, often for emergency services. In many cases, it was the default replacement for unencrypted FM two-way radios, adding encryption, flexibility and network security. These were state of the art when TETRA was developed in the 1980s and 1990s — and [work as well in 2026 as you might expect](https://www.theregister.com/security/2023/07/25/tetra-comms-used-by-emergency-workers-easily-cracked/1152574). Oops.

REG AD

There have been upgrades and, especially after the 2023 vulnerability disclosures, an accelerated program of making things better. A lot of the installed base globally is old, lacks over-the-air updates for security, and in any case spending money on new radios is normally at the bottom of the list for any state or public service organizations. Things have to get really bad first. Perhaps they just have.

## MORE CONTEXT

* [### Microsoft's bad obsession is showing up in shabby services and slipshod software. Here's proof](/software/2026/05/05/microsofts-code-shack-shaken-as-redmond-chases-ai-ghosts/5219761)
* [### Apple's chips are the core of a new landscape, but its biggest win is Windows](/on-prem/2026/04/07/apples-chips-are-winners-but-windows-fails-help-it-most/5228949)
* [### Age verification isn't sage verification when it's inside operating systems](/software/2026/03/16/age-verification-isnt-sage-verification-inside-oses/5224054)
* [### Every day in every way, passwords are getting worse and worse](/security/2026/02/23/every-day-in-every-way-passwords-are-getting-worse/4318120)

(North America is the only region where TETRA is uncommon, as it isn’t approved for public service use. This was either acute foresight or the fact that the TE in TETRA, now officially TErrestrial, used to stand for Trans-Europe. The American system, P.25, has never, however, been renamed Freedom Frequencies. Now on with the show)

The network vulnerabilities are one side of the story. Our doughty hacker is the other. Reportedly, he didn’t have any TETRA hardware, but a laptop connected to a radio and an ‘SDR filter’. The latter makes little sense, it is far more likely that he had a software defined radio (SDR) called a HackRF. There are plenty of other devices that could have been used, but the HackRF is the weapon of choice for the gung-ho radio nut.

SDR is a technique that has completely changed the rules of how to radio. All radios before it had to be entirely or mostly analog, with precision hardware dedicated to whatever job each radio had to do. This hardware could also be looked at as an analog computer, as it can be modelled as a set of mathematical transformations on the received signal. Analog computers have their place, just not in the 21st century.

SDR is radio as digital computer. At heart, it has three components: an analog to digital converter to turn the incoming signal to a stream of numbers, very fast processing to do the radio math,...