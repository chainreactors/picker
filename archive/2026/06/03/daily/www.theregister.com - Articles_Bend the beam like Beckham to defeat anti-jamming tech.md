---
title: Bend the beam like Beckham to defeat anti-jamming tech
url: https://www.theregister.com/networks/2026/06/03/curving-beams-could-fool-anti-jamming-tech/5250872
source: www.theregister.com - Articles
date: 2026-06-03
fetch_date: 2026-06-04T06:32:22.032939
---

# Bend the beam like Beckham to defeat anti-jamming tech

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
  + [All Special Features](/special_features)
  + [HPE: AI Explainers](/explainer/ai-explainer)
  + [RSA Conference](/special_features/rsa)
  + [Agentic AI](/special_features/agentic_ai)
  + [The Future of the Datacenter](/special_features/future_of_the_datacenter)
  + [AWS:Reinvent](/special_features/aws_reinvent)
  + [Nvidia GTC](/special_features/nvidia_gtc)
  + [SC25](/special_features/2025_11_sycomp_supercomputing)
  + [Supercomputing Month](/special_features/2025_11_supercomputing_month)
  + [Computex 2026](/special_features/computex)
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

* [Computex 2026](/special_features/computex)
* [Security](/security)
* [Microsoft](/tag/microsoft)
* [AWS](/tag/aws)
* [Developer](/tag/developer)
* [Open Source](/tag/open%20source)
* [Columnists](/tag/columnists)
* [BOFH](/tag/bofh)
* [Who, Me?](/tag/who%20me)
* [On Call](/tag/on%20call/)

REG AD

networks

# Bend the beam like Beckham to defeat anti-jamming tech

It's hard to stop a signal jammer if you can't locate the source, say Rice University researchers

Brandon Vigliarolo
[Brandon
Vigliarolo](https://www.theregister.com/author/brandon-vigliarolo)

Published
wed 3 Jun 2026 // 21:57 UTC

Wireless jamming attacks are on the rise. Rice University researchers have shown how self-curving radio beams can make a jammer appear to be somewhere it isn't, potentially undermining some anti-jamming defenses.

Jamming relies on flooding a wireless receiver with noise that denies service. Some modern receivers identify and block jamming attempts using direction-of-arrival (DoA) estimation technology that pinpoints the jammer's direction and directs an array null that blocks signals emanating in the jammer’s direction. Were a jammer to transmit a self-curving beam, however, it could fool DoA-based anti-jamming defenses by appearing to come from somewhere else entirely, and that's exactly what the Rice researchers demonstrated.

Rice electrical and computer engineering professor Edward Knightly and doctoral student Caroline Spindel presented a [paper](https://networks.rice.edu/files/2026/04/curving_jamming.pdf) [PDF] last month in which they demonstrated a curving-beam jamming attack that caused "catastrophic bit-error-rate degradation" while also "fool[ing] the receiver's DoA estimator," preventing conventional DoA-based defenses from stopping the interference.

REG AD

Knightly and Spindel have done [prior research](https://www.youtube.com/watch?v=pUW0YRXcJnQ) developing wireless technology that could bend beams around objects to increase signal strength - particularly useful for short-range millimeter wave signals - and found that the same technology could be used to deploy jammers that are far harder to locate.

REG AD

Spindel gave the perfect analogy in a recent Rice [press release](https://news.rice.edu/news/2026/curving-wireless-beams-could-let-cyberattackers-hide-source-jamming-attacks) about the research for understanding how curved beams confuse DoA estimators by considering a soccer ball kick to the head.

“Imagine being hit on the right side of your head by a soccer ball - you would naturally look to the right,” Spindel said. “If the ball actually curved through the air, like a David Beckham free kick, then it was kicked from somewhere else entirely.”

Were Sir David to keep moving and kicking curveballs at your head you’d probably spot him eventually, but it might take a minute, and a few more smacks, to stop him.

A signal jammer at radio-wave distances will probably be far harder to spot, and it won’t even have to move: Knightly and Spindel were able to create the illusion that the jammer was mobile by modulating the beam parameters from a stationary position, making it even more difficult to locate the jamming signal and negating the point of blindly searching for the best spot to point an array null. Conventional recovery methods used to block jamming completely failed in laboratory tests, Spindel said.

## MORE CONTEXT

* [### Britain seeks views before it drops the hammer on signal jammers](/security/2026/04/10/uk-seeks-fresh-perspectives-to-shape-radio-jamming-laws/5225756)
* [### Researchers move in the right direction, develop powerful GPS interference alarm](/security/2026/04/29/ornl-builds-more-sensitive-gps-interference-detector/5223865)
* [### Jammin' on UK defence secretary's jet as Russia blamed for GPS interference](/networks/2026/05/29/jammin-on-uk-defence-secretarys-jet-as-russia-blamed-for-gps-interference/5247673)
* [### Pentagon has little to show for two decades of GPS modernization work](/software/2024/09/10/military-gps-modernization-way-behind-schedule-audit-finds/1508672)

“This is the first demonstration of a jammer that cannot be reliably localized and the first time self-curving wireless beams have been used as an attack,” Knightly added.

The pair sees their research not just as a way to point out a serious threat to wireless signals - GPS jamming of aircraft is on the rise, for example - but also something that can inform the direction of future wireless technologies as we move toward the 6G era. Until then, however, there’s the potential for even more devastating jamming attacks to come. ®

[security](/tag/security)
[networks](/tag/networks)
[gps](/tag/gps)
[gps jamming](/tag/gps%20jamming)
[telecommunications](/tag/telecommunications)
[wi-fi](/tag/wi-fi)

REG AD

**SPONSORED LINKS**

[Building the New Trust Architecture for AI - June 4, 10am PT](http://pubads.g.doubleclick.net/gampad/clk?id=7330361192&iu=/6978)

[![](https://image.theregister.com/5250915.jpg?imageId=5250915&panox=0.00&panoy=0.00&panow=100.00&panoh...