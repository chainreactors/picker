---
title: Schrödinger's backup: not actually recovered until you try to restore IT
url: https://www.theregister.com/security/2026/08/27/sponsored-schroedingers-backup-not-actually-recovered-until-you-try-to-restore-it/5286772
source: www.theregister.com - Articles
date: 2026-08-27
fetch_date: 2026-08-28T13:38:12.216051
---

# Schrödinger's backup: not actually recovered until you try to restore IT

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
  + [VMware Explore 2026](/special_features/vmware_explore_2026)
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

# Schrödinger's backup: not actually recovered until you try to restore IT

SPONSORED FEATURE: Verify and survive: your backup isn't real 'til you test it

Guy Matthews
[Guy
Matthews](https://www.theregister.com/author/guy-matthews)

Published
thu 27 Aug 2026 // 16:00 UTC

Schrödinger's Cat, the famous 1935 thought experiment, imagines a cat that, for reasons rooted in quantum physics we need not dwell on here, is simultaneously alive and dead.

In a landscape of relentless cyberattacks and mounting infrastructural complexity, a routine backup task can appear finished, with every box ticked and every check made. The job is not actually done, however, until it has been verified as fully ready for recovery in the event of cyber disaster. A task that looks sorted can turn out, under scrutiny, to be anything but.

A backup can be logged as 'complete' once data has been copied to storage, but a recoverable workload is another matter entirely. It means that when a business goes down, its workloads can be restored to their state at the point of attack with nothing lost. By the time you realize you are on the wrong side of that ambiguity, it may be too late: your data is in the hands of the bad guys, or destroyed, and this time the cat really is dead.

This is not a problem to which IT bosses and managed service provider (MSP) management are entirely oblivious. Most organizations recognize to some degree that their backup may not be 100 percent watertight. Cybersecurity management specialist Kaseya recently partnered with 1105 Media to [survey](https://www.kaseya.com/resource/report-state-of-cyber-resilience-in-microsoft-environments/) 200 IT professionals about the realities shaping cyber resilience planning. Some 53 percent were no more than 'somewhat confident' in their organization's ability to fully recover from a ransomware attack, and admitted their backups were supported by no better than 'limited testing'. A significant proportion had even less faith in their recovery capabilities, while only 15 percent were 'very confident' they could get back on track with no loss.

### **Verify and survive**

Understanding what a verified backup means, and what role verification plays in the recovery challenge weighing on so many IT leaders, is where any sensible resilience plan begins. Backups are vital but they do not guarantee recovery on their own. What matters is confirming that a backup job will hold up in a disaster. Verification is the process of proving that backed-up data is complete, uncorrupted, and fully restorable in an emergency, offering evidence that recovery is possible during a critical outage, hardware failure or ransomware attack. It is essential whether you run an IT department or an MSP responsible for client protection: unless you can prove clients are protected, there is every chance they are not.

"Backup isn't done and entrustable until you've gone in and made sure that the application actually works and can be brought back to the recovery environment," explains Brent Torre, GM of cyber resilience at Kaseya. "Historically, it's just taken too much time and resource for a lot of people to even attempt that. And where they have been verifying, they haven't been doing it regularly enough to ensure real protection."

Not all approaches to verification are of equal value. IT departments still relying on intermittent manual verification are operating on blind trust: warnings thrown up by the process can be misread, failures overlooked, and the result is a dangerous mix of false negatives that waste time and false positives that expose the organization to real risk.

Manual screenshot verification is a proven way to squander a security budget , tying up highly qualified staff on needless work and pulling their expertise away from where it is genuinely needed. Nobody wants  seasoned engineers spending hours reviewing screenshots, second-guessing outputs and trying to determine whether a backup worked.

Where static verification methods once had a place, today's complex IT ecosystems have made them redundant. Across an estate spanning in-house systems, SaaS and cloud endpoints, basic verification cannot cope, picking up only surface-level signals and lacking t...