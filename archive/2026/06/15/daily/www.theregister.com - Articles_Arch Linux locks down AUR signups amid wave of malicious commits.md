---
title: Arch Linux locks down AUR signups amid wave of malicious commits
url: https://www.theregister.com/security/2026/06/15/arch-linux-locks-down-aur-signups-amid-wave-of-malicious-commits/5255511
source: www.theregister.com - Articles
date: 2026-06-15
fetch_date: 2026-06-16T07:17:06.702891
---

# Arch Linux locks down AUR signups amid wave of malicious commits

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
  + [Supercomputing Month](/special_features/2025_11_supercomputing_month)
  + [Computex 2026](/special_features/computex)
* Vendor Voice
  + [All Vendor Voice](https://vendorvoice.theregister.com/)
  + [Barco](https://vendorvoice.theregister.com/barco/)
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

* [AI](/tag/ai%20and%20ml)
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

Security

# Arch Linux locks down AUR signups amid wave of malicious commits

Community repo freezes new accounts after attackers swamp it with poisoned package updates

Richard Speed
[Richard
Speed](https://www.theregister.com/author/richard-speed)

Published
mon 15 Jun 2026 // 14:30 UTC

A wave of malicious commits hit the Arch User Repository (AUR) over the weekend, prompting the team to disable new account registration on Monday morning while it cleans up the mess.

The issue was first acknowledged on June 12, with a [post](https://archlinux.org/news/active-aur-malicious-packages-incident/) stating: "We are currently experiencing a high volume of malicious package adoptions and updates in the Arch User Repository."

The team warned that users might have issues opening new accounts, pushing package updates, and adopting or creating fresh packages.

REG AD

Around 400 user-submitted packages were believed compromised; that figure climbed past 1,500 over the weekend. On June 14, a more sophisticated wave of malicious packages [was spotted](https://lists.archlinux.org/archives/list/aur-general%40lists.archlinux.org/message/TND7HA2KBQ46OHHUMMIAHKGXZE4WALM6/). The Arch Linux team this morning [disabled new account registration](https://lists.archlinux.org/archives/list/aur-general%40lists.archlinux.org/thread/4JRS73YVTE7JUYHHE3ZDUIHXYHXZ3YQQ/) "while we are working on the cleanup."

REG AD

The core Arch distribution itself is unaffected. The AUR is a community-run package repo – if something isn't in the official repo, it's probably here, assuming nobody's poisoned it. The AUR is user-submitted and unsupported, so users are expected to inspect package build files themselves before installation. The malicious packages attempted to pull in hostile JavaScript dependencies, including npm packages identified in the campaign.

Arch Linux is a fast, lightweight Linux distribution. It isn't for beginners – users need to pick their own display manager and desktop environment as well as their own applications. However, this makes it highly customizable.

The project's website [says](https://archlinux.org/): "Currently we have official packages optimized for the x86-64 architecture. We complement our official package sets with a community-operated package repository that grows in size and quality each and every day." Unless, of course, miscreants go wild with malicious commits, and the team has to wade in to deal with the problem.

[According](https://aur.archlinux.org/) to the AUR, there are just over 107,000 packages, with 5,586 updated and 273 packages added in the past seven days.

## MORE CONTEXT

* [### Arch Linux takes a pounding as DDoS attack enters week two](/software/2025/08/22/arch-linux-takes-a-pounding-as-ddos-attack-enters-week-two/547522)
* [### Arch Linux users told to purge Firefox forks after AUR malware scare](/software/2025/07/22/arch-user-contributed-browsers-compromised/717989)
* [### Arch Linux installer now slightly less masochistic](/software/2024/11/29/arch-linux-installer-now-slightly-less-masochistic/725951)
* [### Arch-based CachyOS promises speed but trips over its laces](/software/2024/07/23/arch-based-cachyos-promises-speed-but-trips-over-its-laces/1216992)

This isn't Arch Linux's first brush with trouble. In 2025, the project was [hit with a Distributed Denial of Service (DDoS) attack](https://www.theregister.com/software/2025/08/22/arch-linux-takes-a-pounding-as-ddos-attack-enters-week-two/547522) that disrupted its main web page, the AUR, and the project's forums. It also had to address [compromised browser packages](https://www.theregister.com/software/2025/07/22/arch-user-contributed-browsers-compromised/717989) that reportedly contained a Remote Access Trojan.

Both incidents highlight risks in the way the AUR is structured and maintained. It's an invaluable library of packages led by a community of smart Arch users, yet that open, community-driven model can be abused by attackers.

New account creation remains disabled at the time of writing. The Arch team will no doubt be pondering how to avoid this situation in the future. ®

[npm](/tag/npm)
[aur](/tag/aur)
[arch linux](/tag/arch%20linux)
[security](/tag/security)
[supply chain attack](/tag/supply%20chain%20attack)

REG AD

[![](https://image.theregister.com/5255961.jpg?imageId=5255961&panox=0.00&panoy=0.00&panow=100.00&panoh=100.00&heightx=0.00&heighty=0.00&heightw=100.00&heighth=100.00&width=960&height=432&format=webp&format=jpg)

AI + ML

## A modest proposal: Reformat everything to make documents more palatable to AI

What's up, DocLang?](https://www.theregister.com/ai-and-ml/2026/06/16/a-modest-proposal-reformat-everything-to-make-documents-more-palatable-to-ai/5255938)

[...