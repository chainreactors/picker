---
title: Crooks found a new way to collaborate using Teams – by hiding command-and-control traffic
url: https://www.theregister.com/cyber-crime/2026/06/16/crooks-found-a-new-way-to-collaborate-using-teams-by-hiding-command-and-control-traffic/5256296
source: www.theregister.com - Articles
date: 2026-06-16
fetch_date: 2026-06-17T07:04:15.329499
---

# Crooks found a new way to collaborate using Teams – by hiding command-and-control traffic

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

Cyber-crime

# Crooks found a new way to collaborate using Teams – by hiding command-and-control traffic

Custom malware routed communications through legitimate Microsoft services, making malicious activity look like routine corporate collaboration

Carly Page
[Carly
Page](https://www.theregister.com/author/carly-page)

Published
tue 16 Jun 2026 // 15:41 UTC

Cybercrims deploying DragonForce ransomware appear to have gained access to a major US services company's network, then spent two months up to no good while disguising their command-and-control activities as legitimate Microsoft Teams traffic.

Researchers at security firm Symantec [said](https://www.security.com/threat-intelligence/dragonforce-msteams-backdoor) the intrusion began with attackers gaining access to the victim's environment before deploying a custom Go-based backdoor, tracked as "Backdoor.Turn," to maintain communication with the compromised systems. Rather than reaching out to attacker-controlled infrastructure that might raise alarms, the backdoor hid its activity inside traffic associated with Microsoft's widely used collaboration platform.

To anyone monitoring network traffic, the compromised systems appeared to communicate only with legitimate Microsoft servers.

REG AD

"The attackers in this campaign use exceptionally sophisticated cyber tradecraft," Symantec said. "The configuration of Backdoor.Turn means that security products only see C&C traffic going to legitimate Teams servers, leaving defenders unaware that data is being siphoned away by malicious actors."

REG AD

Symantec said the attackers installed Backdoor.Turn on systems after deploying DragonForce ransomware, potentially giving them a way back into compromised networks or access they could later sell to other criminals.

To connect to Microsoft's infrastructure, the backdoor first requested an anonymous visitor token from Microsoft Teams and Skype back-end services. It then used a Microsoft-operated TURN relay server – infrastructure typically used to help establish communication between users – before establishing a direct QUIC connection to a malicious command-and-control server.

## MORE CONTEXT

* [### Scammers keep scoring: Brits fleeced for £1.3B as Americans lose $3.5B to impersonators](/cyber-crime/2026/06/16/scammers-keep-scoring-brits-fleeced-for-13b-as-americans-lose-35b-to-impersonators/5256106)
* [### ShinyHunters hacked 100+ orgs by exploiting an Oracle PeopleSoft 0-day](/cyber-crime/2026/06/11/shinyhunters-claims-oracle-peoplesoft-0-day-hit-100-orgs/5254443)
* [### Ransomware crims got a month-long head start on Check Point VPN 0-day that now has a fix](/cyber-crime/2026/06/08/attackers-had-month-long-head-start-on-patched-check-point-vpn-zero-day/5252438)
* [### Pink is the latest goon squad to use fake helpdesk calls to steal creds](/cyber-crime/2026/06/04/pink-is-the-latest-goon-squad-to-use-fake-helpdesk-calls-to-steal-creds/5251434)

Symantec said this is the first known case of malware using this particular technique.

The security firm did not identify the victim beyond describing it as a major US services company, nor did it say whether the Teams-based communications channel had been observed in other DragonForce incidents.

The ransomware operation has become increasingly prominent over the past year, operating a ransomware-as-a-service model that allows affiliates to conduct attacks under the DragonForce banner. It has been linked to the prolific Scattered Spider group, which has conducted a string of high-profile attacks, including intrusions targeting major retailers in the UK.

While attackers have long abused legitimate cloud services to conceal malicious traffic, Symantec's findings suggest that DragonForce operators continue to look for ways to blend into the software and infrastructure that organizations trust most. ®

[security](/tag/security)
[microsoft](/tag/microsoft)
[cyber-crime](/tag/cyber-crime)
[microsoft teams](/tag/microsoft%20teams)
[ransomware](/tag/ransomware)

REG AD

[![](https://image.theregister.com/5227626.jpg?imageId=5227626&panox=0.00&panoy=0.00&panow=100.00&panoh=100.00&heightx=0.00&heighty=0.00&heightw=100.00&heighth=100.00&width=960&height=432&format=webp&format=jpg)

CYBER-CRIME

## Cyberattack sees crops kept in the ground

Bitter harvest for Australia's Mackay Sugar, attacked in peak cane crushing season](https://www.theregister.com/cyber-crime/2026/06/17/cyberattack-sees-crops-kept-in-the-ground/5256321)

[SYSTEMS

## AMD's Mext buy shows how AI could solve the RAM shortage it created

Running low on memory, can't afford more? The House of Zen's latest acquisition puts an AI spin on flash-based memory expansion](https://www.theregister.com/systems/2026/06/1...