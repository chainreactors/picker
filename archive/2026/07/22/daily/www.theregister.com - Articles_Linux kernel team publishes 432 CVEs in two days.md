---
title: Linux kernel team publishes 432 CVEs in two days
url: https://www.theregister.com/security/2026/07/22/linux-kernel-team-publishes-432-cves-in-two-days/5276497
source: www.theregister.com - Articles
date: 2026-07-22
fetch_date: 2026-07-23T05:11:45.805076
---

# Linux kernel team publishes 432 CVEs in two days

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
  + [HPE: AI Explainers](/explainer/ai-explainer)
  + [RSA Conference](/special_features/rsa)
  + [Agentic AI](/special_features/agentic_ai)
  + [The Future of the Datacenter](/special_features/future_of_the_datacenter)
  + [AWS:Reinvent](/special_features/aws_reinvent)
  + [Nvidia GTC](/special_features/nvidia_gtc)
  + [Supercomputing Month](/special_features/2025_11_supercomputing_month)
  + [Computex 2026](/special_features/computex)
  + [AI Infrastructure Month 2026](/special_features/ai_infrastructure_month_2026)
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

security

# Linux kernel team publishes 432 CVEs in two days

Sunday-to-Monday onslaught fuels speculation over AI-assisted bug reports

Brandon Vigliarolo
[Brandon
Vigliarolo](https://www.theregister.com/author/brandon-vigliarolo)
GOVERNMENT AND IT NEWS REPORTER

Published
wed 22 Jul 2026 // 17:58 UTC

If you're responsible for Linux security, someone just dumped a pile of work onto your desk: 432 Linux kernel CVEs were published across Sunday and Monday this week. Linux watchers at nixCraft [pointed](https://mastodon.social/%40nixCraft/116953574480188144) out the volume on Monday morning, and it didn’t take long for seasoned sysadmins to start expressing concerns.

Jan Schaumann, chief information security architect at Akamai Technologies, took to the OSS-SEC mailing list Tuesday to express [concerns](https://seclists.org/oss-sec/2026/q3/198) over the sheer volume of Linux kernel CVEs published in recent days. Aside from noting that the CVE system isn’t the best way to track security changes, Schaumann also wondered in his post whether there was any good way to deal with so many kernel security issues.

“This onslaught really shows it's not feasible to attempt to prioritize individual kernel changes,” Schaumann said.

REG AD

“You might attempt to process this large set of changes by pointing an LLM at the intake and asking it to prioritize them,” he suggested, “but if it spits out a dozen today and another 25 the next, you haven't won much.”

REG AD

Schaumann also suggested waiting to see which ones emerge as serious issues and focusing on those in the weeks to come, or updating one’s entire fleet of Linux machines on a weekly basis.

“I sure would like to be able to do [that], but reality keeps getting in my way,” Schaumann said. “I'm not sure what to do here going forward.”

In an email to The Register, Schaumann said that individually reviewing vulnerabilities for patching was already difficult enough before things rose to this level, and that automation may be the only option - but it's not a great one.

"Automated, regular, and frequent updates that pull in all changes within a given time window of tolerance seem to me the only reasonable approach, but that is very difficult for many large organizations," Schaumann explained. Those orgs often rely on lengthy QA processes, slow and staged development cycles, and may even have contractual requirements for long-term support that make an automated approach an impossible one.

The nixCraft team speculated on social media that AI bug reports are a likely reason for all those kernel CVEs, which wouldn’t be without precedent - Linus Torvalds himself said in May that the Linux kernel security mailing list had become “[almost entirely unmanageable](https://www.theregister.com/security/2026/05/18/linus-torvalds-says-ai-powered-bug-hunters-have-made-linux-security-mailing-list-almost-entirely-unmanageable/5241633)” due to AI-assisted bug hunting. Nonetheless, Torvalds [has described AI](https://www.theregister.com/ai-and-ml/2026/07/15/linus-torvalds-tells-ai-haters-to-fork-off/5271894) as a useful tool for Linux development while still noting it can be a drag for maintainers, both from a workload standpoint and the fact "it keeps finding embarrassing bugs."

On that note, it's worth understanding what a Linux kernel CVE actually means - many of the vulnerabilities included in the Sunday-to-Monday batch are small in scope, but they're vulnerabilities nonetheless.

As senior Linux maintainer Greg Kroah-Hartman noted in a February [blog post](http://www.kroah.com/log/blog/2026/02/16/linux-cve-assignment-process/), the Linux kernel CVE team follows the CVE Program's definition of a vulnerability: a weakness in a product that can negatively affect a system's confidentiality, integrity, or availability.

“At the level that the Linux kernel runs, almost any type of bug that can affect a running system can be classified as a vulnerability,” Kroah-Hartman noted. The kernel team looks at every bugfix that is added to stable kernel releases, he added, and if it fixes an issue that meets that CVE criteria, a CVE is assigned.

REG AD

## MORE CONTEXT

* [### AI eyes scanning for bugs create a worrisome Linux security trend](/security/2026/05/23/ai-eyes-scanning-for-bugs-create-a-worrisome-linux-security-trend/5244742)
* [### Cisco's open-weight bug busters take on Google and OpenAI](/security/2026/07/21/ciscos-open-weight-bug-busters-take-on-google-and-openai/5275817)
* [### Torvalds challenged the haters to fork Linux. Someone said 'hold my beer'](/os-pla...