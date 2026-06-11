---
title: Ivanti tells Sentry customers to patch now as critical bugs hit 10.0 and 9.9
url: https://www.theregister.com/patches/2026/06/10/ivanti-urges-sentry-users-to-patch-two-critical-bugs/5253428
source: www.theregister.com - Articles
date: 2026-06-10
fetch_date: 2026-06-11T06:37:04.013327
---

# Ivanti tells Sentry customers to patch now as critical bugs hit 10.0 and 9.9

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

* [Space](/tag/space)
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

Patches

# Ivanti tells Sentry customers to patch now as critical bugs hit 10.0 and 9.9

Remote, unauthenticated RCE with root privileges is about as bad as it gets

Connor Jones
[Connor
Jones](https://www.theregister.com/author/connor-jones)
Cybersecurity reporter

Published
wed 10 Jun 2026 // 12:04 UTC

It's patch time for Ivanti customers again after the security shop disclosed another two critical vulnerabilities in one of its products.

Both bugs affect Ivanti Sentry, a mobile gateway that forms part of its broader unified endpoint management platform.

The first and worst of the two is CVE-2026-10520 (10.0), a max-severity vulnerability that allows a remote, unauthenticated attacker to execute code with root privileges.

REG AD

Flaws that allow root-level code execution without authentication are about as bad as vulnerabilities get, which explains the perfect-10 rating.

REG AD

The only saving grace is that, by the vendor's reckoning, no one has successfully exploited it in the wild… yet. Public disclosures tend to start a figurative countdown timer when it comes to attackers exploiting bugs, and although Ivanti gave little away about CVE-2026-10520 in its [advisory](https://hub.ivanti.com/s/article/Security-Advisory-Ivanti-Sentry-CVE-2026-10520-CVE-2026-10523?language=en_US), other researchers have already published breakdowns of the patch, offering clues as to how unpatched systems could still be attacked.

According to [watchTowr](https://labs.watchtowr.com/more-evidence-that-words-dont-mean-what-we-thought-they-meant-ivanti-sentry-pre-auth-os-command-injection-cve-2026-10520/), the vulnerability stemmed from an exposed API running under Apache Tomcat. An attacker could feed the API a specially crafted message, which is parsed as a MICS configuration command and executed by the backend handler with root privileges.

## MORE CONTEXT

* [### January blues return as Ivanti coughs up exploited EPMM zero-days](/security/2026/01/30/ivantis-january-bad-luck-continues-as-0-days-hit-customers/5147270)
* [### Dutch data watchdog snitches on itself after getting caught in Ivanti zero-day attacks](/security/2026/02/09/dutch-data-watchdog-caught-up-in-ivanti-zero-day-attacks/4332837)
* [### Credential-stealing crew spoofs VPN clients from Cisco, Fortinet, and others](/security/2026/03/13/credential-stealing-crew-spoofs-ivanti-fortinet-cisco-vpns/5223322)
* [### Ivanti patches two zero-days under active attack as intel agency warns customers](/security/2025/05/14/ivanti-patches-two-0-days-and-a-critical-make-me-admin-bug/1033529)

It looks like Ivanti fixed this by preventing this attacker-supplied string from being accepted, replacing it with a single, hard-coded command. It also updated the Apache configuration rules to block unauthenticated access to the affected endpoint.

The second critical Ivanti Sentry vulnerability is tracked as CVE-2026-10523, and is scarcely less serious, carrying a near-maximum 9.9 CVSS.

The authentication bypass bug allows remote, unauthenticated attackers to create admin accounts, granting themselves top privileges on an affected system.

Customers are advised to address both security flaws immediately. They can upgrade to versions 10.5.2, 10.6.2, or 10.7.1.

Ivanti's disclosure this week comes after it fixed two separate critical vulnerabilities affecting its Endpoint Manager Mobile (EPMM) in January.

The bugs were both handed 9.8 CVSS scores and were [exploited as zero-days](https://www.theregister.com/security/2026/01/30/ivantis-january-bad-luck-continues-as-0-days-hit-customers/5147270). Even the Dutch data protection authority [reported itself to parliament](https://www.theregister.com/security/2026/02/09/dutch-data-watchdog-caught-up-in-ivanti-zero-day-attacks/4332837) after attackers breached it as part of the pre-patch exploits. ®

[patch](/tag/patch)
[ivanti sentry](/tag/ivanti%20sentry)
[ivanti](/tag/ivanti)
[security](/tag/security)
[patches](/tag/patches)
[remote code execution](/tag/remote%20code%20execution)

REG AD

[![](https://image.theregister.com/5226078.jpg?imageId=5226078&panox=0.00&panoy=0.00&panow=100.00&panoh=100.00&heightx=0.00&heighty=0.00&heightw=100.00&heighth=100.00&width=960&height=432&format=webp&format=jpg)

Security

## Chinese agents caught rebuilding botnets and stirring the pot on AI datacenter debate

PRC eyes are watching you](https://www.theregister.com/security/2026/06/11/china-linked-operators-revive-botnet-stir-ai-datacenter-debate/5253873)

[AI + ML

## Memory and personalization make AI more likely to tell you what you want to hear

A little knowledge is a dangerous thing, particularly for enterprise applications](https://www.theregister.com/ai-and-ml/2026/06/11/memory-and-personalizati...