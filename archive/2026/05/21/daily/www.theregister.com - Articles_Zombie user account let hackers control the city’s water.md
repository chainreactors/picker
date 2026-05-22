---
title: Zombie user account let hackers control the city’s water
url: https://www.theregister.com/security/2026/05/21/zombie-user-account-let-hackers-control-the-citys-water/5243724
source: www.theregister.com - Articles
date: 2026-05-21
fetch_date: 2026-05-22T06:08:46.610118
---

# Zombie user account let hackers control the city’s water

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

Security

# Zombie user account let hackers control the city’s water

Failing to disable a former employee’s account was a huge mistake

Avram Piltch
[Avram
Piltch](https://www.theregister.com/author/avram-piltch)

Published
thu 21 May 2026 // 08:00 UTC

PWNED Welcome once again to PWNED, the column where security flubs are held up to the harsh, piercing red light of the vulture signal. This week’s sad story concerns a municipality that failed to perform basic account housekeeping and paid for it dearly.

Have a story about someone leaving a gaping hole in their network? Share it with us at pwned@sitpub.com. Anonymity is available upon request.

Our tale of tech missteps comes courtesy of Nicole Beckwith, who serves as the senior director for security engineering and operations at [Cribl](https://cribl.io/), an AI platform for telemetry. She used to work as a consultant, and at one point was hired to investigate breaches in an American city’s network.

REG AD

A threat actor took a “leisurely tour” of the city’s online resources and had started messing around with conference room projectors and other relatively harmless endpoints. Then they realized that they could change settings with the water utility where they switched many controls off, potentially endangering the water supply.

REG AD

When Beckwith investigated, she found that all of the mischief was performed by an account that belonged to “Greg from Auditing.” There was just one problem. Greg hadn’t worked for the city for many years.

Unfortunately, even though Greg was no longer around, his account was, and it retained extensive privileges, including domain admin rights, SCADA (Supervisory Control and Data Acquisition) operator access, and even the ability to perform help desk functions. It’s unclear if someone from auditing ever needed this level of access, but a former employee definitely did not.

## MORE CONTEXT

* [### To gain root access at this company, all an intruder had to do was ask nicely](/security/2026/05/14/to-gain-root-access-intruder-just-had-to-ask/5239853)
* [### The network password was a key plot point in one of the most famous movies of all time](/security/2026/05/07/guessable-admin-password-exposes-sloppy-network-security/5231161)
* [### Finance company stores DB credentials in helpfully labeled spreadsheet](/security/2026/04/30/finance-company-stored-their-db-credentials-in-spreadsheet/5224248)
* [### Using the password 'admin123' wasn't as bad as sharing it on Slack](/security/2026/04/23/using-password-admin123-wasnt-as-bad-as-slacking-it/5227590)

It wasn't Greg himself who hacked the network. But he had used his work email address to sign up for various online accounts, some of which may have been exposed in previous data leaks. She speculates the hackers saw an email address with a .gov in it and decided to try their luck with the leaked password that went along with it, and that Greg likely used the same password for work that he did for these outside services.

We have a few takeaways here. First, the people who ran IT security for the city should have both deleted Greg’s account when he left and done periodic audits to see who had access and whether they should still have it.

Second, Greg should have kept his work credentials separate from third-party services like shopping and social media sites. And he should not have used the same password in multiple places.

“The lesson, beyond the obvious 'please, for the love of all that is holy, audit your dormant accounts,' is that every forgotten user is an easy ticket to being on the 5 o’clock news,” Beckwith told The Register. “Quarterly access reviews should be mandatory because everyone seems to think when a user leaves, that is the end of it and someone surely terminated access, deprovisioned accounts, removed access to tools, mobile communications, email and other business critical systems, but sadly I’ve responded to way too many incidents like this one because of this simple control which is often overlooked."  ®

[scada](/tag/scada)
[pwned](/tag/pwned)
[former employee](/tag/former%20employee)
[cybersecurity](/tag/cybersecurity)
[user accounts](/tag/user%20accounts)
[security](/tag/security)
[water utility](/tag/water%20utility)

REG AD

[![](https://image.theregister.com/230011.jpg?imageId=230011&panox=0.00&panoy=0.00&panow=100.00&panoh=100.00&heightx=0.00&heighty=0.00&heightw=100.00&heighth=100.00&width=960&height=432&format=webp&format=jpg)

Security

## Cisco used AI to write security incident reports, with mixed results

You’ll need a lot of detailed prompts to get solid output - and even then it may have errors and typos](https://www.theregister.com/security/2026/05/22/cisco-used-ai-to-write-security-incident-reports-with-mixed-results/5244692)

[Systems

## Alibab...