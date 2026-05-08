---
title: 60% of MD5 password hashes are crackable in under an hour
url: https://www.theregister.com/security/2026/05/07/60-of-md5-password-hashes-are-crackable-in-under-an-hour/5234954
source: www.theregister.com - Articles
date: 2026-05-07
fetch_date: 2026-05-08T04:57:03.327472
---

# 60% of MD5 password hashes are crackable in under an hour

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

security

# 60% of MD5 password hashes are crackable in under an hour

Happy World Password Day! Maybe it's finally time to kill this holiday in favor of World No-More-Passwords Day?

Brandon Vigliarolo
[Brandon
Vigliarolo](https://www.theregister.com/author/brandon-vigliarolo)

Published
thu 7 May 2026 // 17:47 UTC

It’s World Password Day, and there’s really no better way to celebrate than with news that a majority of supposedly secure password hashes can be cracked with a single GPU in less than an hour, some in less than a minute.

Using a dataset of more than 231 million unique passwords sourced from dark web leaks - including 38 million added since its previous study - and hashing them with MD5, researchers at security firm Kaspersky [found](https://www.kaspersky.com/blog/passwords-hacking-research-2026/55743/) that, using a single Nvidia RTX 5090 graphics card, 60 percent of passwords could be cracked in less than an hour, and a full 48 percent in under 60 seconds.

Sure, that’s not exactly your run-of-the-mill desktop graphics processor given its [price](https://marketplace.nvidia.com/en-us/consumer/graphics-cards/?locale=en-us&page=1&limit=12&gpu=RTX%205090&gpu_filter=RTX%205090~8,RTX%205080~4,RTX%204070%20Ti%20SUPER~6,RTX%204070%20Ti~4,RTX%204060%20Ti~3,RTX%204070%20SUPER~4,RTX%204070~4,RTX%204060~22,RTX%203080~1,RTX%203070%20Ti~1,RTX%203060%20Ti~1,RTX%203060~6,GTX%201650~1), but it highlights an important point: It takes surprisingly little to crack the average password hash. Aspiring cybercriminals don’t even really need their own 5090, Kaspersky notes, as they can easily rent one from a cloud provider and crack hashes for a few bucks.

REG AD

The bottom line is that passwords protected only by fast hashing algorithms such as MD5 are no longer safe if attackers obtain them in a data breach.

REG AD

“One hour is all an attacker needs to crack three out of every five passwords they’ve found in a leak,” Kaspersky noted.

Much of the reason password hashes have become so easy to crack is password predictability. Per Kaspersky, its analysis of more than 200 million exposed passwords revealed common patterns that attackers can use to optimize cracking algorithms, significantly reducing the time needed to guess the character combinations that grant access to target accounts.

In case you’re wondering whether there’s a trend to compare this to, Kaspersky ran a prior iteration of this study in 2024, and bad news: Passwords are actually a bit easier to crack in 2026 than they were a couple of years ago. Not by much, mind you - only a few percent - but it’s still a move in the wrong direction.

“Attackers owe this boost in speed to graphics processors, which grow more powerful every year,” Kaspersky explained. “Unfortunately, passwords remain as weak as ever.”

How about a World Let’s-Stop-Relying-On Passwords Day?

News of the death of the password has, unfortunately, been [greatly exaggerated](https://www.theregister.com/security/2019/03/05/you-shall-not-pass-word-soon-you-may-be-logging-into-websites-using-just-your-phone-face-fingerprint-or-token/311777) in the past couple of decades, yet most of us still rely on them multiple times a day. It likely won’t surprise El Reg readers to learn that us vultures are inundated with pitches for events like World Password Day, and most of them received this year had the same takeaway: We really need to get a move on with ditching passwords, or, at the very least, rethinking our security paradigms.

Chris Gunner, a CISO-for-hire at managed service provider giant Thrive, told us in emailed comments that there’s no reason to ditch passwords entirely, but they need to be just one part of a broader identity-based security strategy.

“Even a strong password can be undermined if the wider identity and access environment is not properly managed,” Gunner said. Passwords should be paired with a second factor, preferably biometric, said Gunner, because it’s the most difficult for hackers to bypass.

REG AD

“MFA controls should then be joined by identity governance and endpoint protection so gaps between systems are reduced,” Gunner added, recommending that a broader zero trust model be established as well, restricting lateral movement possibilities via a compromised account.

Senior IEEE member and University of Nottingham cybersecurity professor Steven Furnell said that World Password Day messaging shouldn’t stop at telling people to improve their personal security posture either. Passwords aren’t going anywhere for a long while, Furnell explained in an email, and inconsistent adoption of new security technologies will mean users will be left at risk as certain providers fail to adapt.

“Many sites and services still don’t offer passkey support, so users will find themselves with a mix...