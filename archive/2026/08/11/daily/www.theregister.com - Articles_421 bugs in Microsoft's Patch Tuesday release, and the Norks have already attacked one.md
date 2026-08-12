---
title: 421 bugs in Microsoft's Patch Tuesday release, and the Norks have already attacked one
url: https://www.theregister.com/security/2026/08/11/421-bugs-in-microsofts-patch-tuesday-release-and-the-norks-have-already-attacked-one/5286483
source: www.theregister.com - Articles
date: 2026-08-11
fetch_date: 2026-08-12T04:02:51.837379
---

# 421 bugs in Microsoft's Patch Tuesday release, and the Norks have already attacked one

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

# 421 bugs in Microsoft's Patch Tuesday release, and the Norks have already attacked one

Sysadmins, welcome to your new norm

Jessica Lyons
[Jessica
Lyons](https://www.theregister.com/author/jessica-lyons)
Cybersecurity Editor

Published
tue 11 Aug 2026 // 22:31 UTC

This is an epic month for Microsoft patches, though not a record-setting one. Redmond addressed [421 bugs](https://msrc.microsoft.com/update-guide/releaseNote/2026-Aug) in its own products this month - about [200 fewer CVEs than last month](https://www.theregister.com/security/2026/07/14/patchpocalypse-now-microsoft-tops-last-months-record-with-622-patch-tuesday-cves/5271434), but [likely the new norm](https://www.theregister.com/security/2026/06/27/its-looking-like-a-hot-messy-summer-for-security-teams-as-ai-finds-countless-previously-hidden-vulns/5260478) with [AI-assisted vulnerability disclosures and fixes](https://www.theregister.com/cyber-crime/2026/08/03/ai-is-both-the-weapon-and-the-target-in-latest-wave-of-cyberattacks/5281534).

The big news is that North Korea’s Lazarus Group (and possibly other miscreants) found and attacked one of these flaws as a zero-day in early June.

The bug, tracked as [CVE-2026-68820](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-68820), is a use-after-free in the Windows Ancillary Function Driver for WinSock. “A locally authenticated attacker could run a specially crafted application on an affected system to trigger a race condition,” Redmond warned, adding that successful exploitation could allow an attacker to execute code with SYSTEM-level privileges, and with no user interaction required.

REG AD

REG AD

Microsoft credited Check Point researchers Moshe Marelus and David Driker with finding and reporting CVE-2026-68820, and the security shop’s threat intel lead told us that his analysts first observed attackers - namely [North Korea’s Lazarus Group](https://www.theregister.com/security/2026/02/24/lazarus-group-targets-healthcare-orgs-with-medusa-ransomware/4589498) - battering this CVE at the beginning of June.

“We are familiar with one successful implementation of the CVE - but we assume it was used widely in the campaign,” Sergey Shykevich, director of threat intelligence at Check Point, told The Register.

He’s talking about [Operation Dream Job](https://www.theregister.com/special-features/2025/10/23/north-korean-dream-job-attacks-hit-europes-uav-sector/409295), a long-running campaign targeting organizations worldwide, especially those in the defense sector, and attributed to Lazarus, an umbrella term for Pyongyang's government-sponsored goons who specialize in [cryptocurrency theft](https://www.theregister.com/2024/09/05/fbi_north_korean_scammers_prepping/), extortion attacks, and [IT worker scams](https://www.theregister.com/2025/07/13/fake_it_worker_problem/).

It’s probably best known for the [Sony Pictures Entertainment hack](https://www.theregister.com/2015/01/07/sony_pictures_hack_was_definitely_the_norks_insists_fbi_chief/) in late 2014 and the [WannaCry ransomware outbreak](https://www.theregister.com/2017/05/13/wannacrypt_ransomware_worm/) in 2017, although the group has been active since at least 2009.

Lazarus’ DreamJob campaigns have been [around since 2020](https://www.clearskysec.com/operation-dream-job/), and they use social engineering to lure job seekers with fake offers for high-profile positions, then trick the victims into clicking on malicious links or opening malware-laced documents. The goal in these attacks involves stealing IP and other sensitive data, conducting cyber spying missions, and collecting financial information.

### When Dream Job and Patch Tuesday collide

This new wave of attacks focuses on the defense sector in Europe and India with dream jobs impersonating Lockheed Martin and privacy-tech firm Enveil. Attackers created at least three fake Enveil sites, and some even ranked as the top search result, making them even more believable to job seekers - and harder to spot a phish.

“In this campaign, the threat actor expanded its delivery method by leveraging impersonation websites and search engine optimization (SEO) techniques to distribute the trojanized applications, increasing its credibility and helping it evade some phishing-based detections...