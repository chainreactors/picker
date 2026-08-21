---
title: Ransomware crook poses as recovery firm to steal payments from fellow extortionists
url: https://www.theregister.com/cyber-crime/2026/08/20/ransomware-crook-poses-as-recovery-firm-to-steal-payments-from-fellow-extortionists/5290344
source: www.theregister.com - Articles
date: 2026-08-20
fetch_date: 2026-08-21T03:05:14.383922
---

# Ransomware crook poses as recovery firm to steal payments from fellow extortionists

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

CYBER-CRIME

# Ransomware crook poses as recovery firm to steal payments from fellow extortionists

Because apparently even ransomware gangs can't trust the people they do business with

Carly Page
[Carly
Page](https://www.theregister.com/author/carly-page)

Published
thu 20 Aug 2026 // 15:27 UTC

A ransomware affiliate appears to have found a new way to squeeze victims for cash: pose as the good guy and undercut the criminals it was working with.

Researchers at [GuidePoint Security](https://www.guidepointsecurity.com/?utm_source=chatgpt.com) say an outfit calling itself "Ransom Busters" has been contacting ransomware victims before their attacks become public, offering to recover encrypted files and delete stolen data for a considerably smaller payment than the original extortion demand.

The catch, according to GuidePoint's Research and Intelligence Team (GRIT), is that Ransom Busters isn't an enterprising band of ransomware hunters at all. The researchers assess with "moderate confidence" that it's a ransomware affiliate working across several ransomware-as-a-service operations and attempting to steer payments away from its criminal partners.

REG AD

GuidePoint came across Ransom Busters while investigating attacks linked to DragonForce, Settra, and Anubis. The outfit emailed victims claiming it had hacked the ransomware gangs themselves and discovered their stolen data on the crooks' servers.

REG AD

Ransom Busters claimed it could delete that data and retrieve encryption keys, all for the bargain-basement price of between $20,000 and $60,000. It also demonstrated access to the same datasets held by the ransomware affiliate behind the attacks, GuidePoint said.

That alone raised eyebrows, but the forensic evidence proved rather harder to explain away.

GuidePoint examined two incidents in which Ransom Busters approached victims and found the intrusions shared a collection of unusually specific fingerprints. Both used SoftPerfect Network Scanner for reconnaissance, s5cmd to shovel data into AWS cloud storage, and the Remotely remote-management tool installed using PowerShell.

## MORE CONTEXT

* [### 'Not a theoretical risk,' feds warn as attackers use AI-made code to hack critical infrastructure controllers](/security/2026/08/19/not-a-theoretical-risk-feds-warn-as-attackers-use-ai-made-code-to-hack-critical-infrastructure-controllers/5289960)
* [### CISA gives feds 3 days to fix actively exploited Ray RCE bug](/security/2026/08/18/cisa-gives-feds-3-days-to-fix-actively-exploited-ray-rce-bug/5289007)
* [### Autonomous AI attacks pose 'clear and present danger' to critical infrastructure](/security/2026/08/14/autonomous-ai-attacks-pose-clear-and-present-danger-to-critical-infrastructure/5287594)
* [### Crypto wallet maker Trezor confirms 13,000 customers' details exposed in logistics breach](/security/2026/08/14/crypto-wallet-maker-trezor-confirms-13000-customers-details-exposed-in-logistics-breach/5287734)

More damningly, the attacker created a local backdoor account using the password "Numlock!123" in both environments. The same attacker-controlled hostname, "DESKTOP-BBETH6K," also turned up in both intrusions.

This might be explained by ransomware operators sharing tools or a prebuilt attack environment. GuidePoint said it has seen the same activity across several separate RaaS programs, however, leading it to conclude that one affiliate is likely moonlighting across multiple gangs and then cutting its employers out of the payday.

GuidePoint also warned that paying the supposed rescuers provides no assurance that stolen information will actually disappear.

So if a mysterious stranger somehow knows you've been ransomwared before you've told anyone, and generously offers to make the whole problem disappear for $20,000, you may want to question how they got your number in the first place. ®

[cyber-crime](/tag/cyber-crime)
[crime](/tag/crime)
[security](/tag/security)
[ransomware](/tag/ransomware)

REG AD

[![](https://image.theregister.com/5290804.jpg?imageId=5290804&panox=0.00&panoy=0.00&panow=100.00&panoh=100.00&heightx=0.00&heighty=0.00&heightw=100.00&heighth=100.00&width=960&height=432&format=webp&format=jpg)

## Supermicro fired staff after probe into $2.5 billion GPUs-to-China smuggling operation

Policie...