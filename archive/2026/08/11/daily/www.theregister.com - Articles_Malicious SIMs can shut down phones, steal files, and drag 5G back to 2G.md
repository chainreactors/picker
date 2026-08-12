---
title: Malicious SIMs can shut down phones, steal files, and drag 5G back to 2G
url: https://www.theregister.com/security/2026/08/11/malicious-sims-can-shut-down-phones-steal-files-and-drag-5g-back-to-2g/5285482
source: www.theregister.com - Articles
date: 2026-08-11
fetch_date: 2026-08-12T04:02:53.720366
---

# Malicious SIMs can shut down phones, steal files, and drag 5G back to 2G

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

# Malicious SIMs can shut down phones, steal files, and drag 5G back to 2G

Researchers find standards-compliant functionality can be abused to hijack modems, downgrade connections, and even execute code

Carly Page
[Carly
Page](https://www.theregister.com/author/carly-page)

Published
tue 11 Aug 2026 // 10:37 UTC

Researchers have found that a malicious SIM card can tell some phones and cellular-connected devices to leak data, drop to 2G, shut themselves down, or even execute code, all thanks to functionality that's supposed to be there.

The [research](https://www.usenix.org/system/files/woot26-lisowski.pdf) [PDF], presented at the USENIX WOOT conference in Baltimore this week, examines proactive SIM functionality, which allows a SIM to issue commands to the device hosting it.

One of those is RUN AT, which allows the SIM to request the execution of AT commands, the instruction set that's been bossing modems around since the 1980s. Give that ability to a hostile SIM, and things get rather more interesting.

REG AD

Tomasz Piotr Lisowski and Marius Muench of the University of Birmingham, working with Fuzzware's Kristian Covic, built a toolkit called CATANA to see what a malicious SIM could get away with.

REG AD

They tested 26 devices – 18 smartphones and eight IoT modems – and found that nine exposed an AT command interface to the SIM. The IoT kit was particularly accommodating, with seven of the eight modems exposing it. The researchers uncovered four vulnerabilities and demonstrated attacks including code execution, arbitrary file reads, denial of service, and downgrading connections to 2G.

"The fascinating part here is that the proactive capabilities of a SIM and the resulting attack surface is explicitly defined in the technical specifications for cellular communication," said Muench, making the attacks "specification-compliant."

He added that hostile SIMs are still missing from many threat models despite previous research and leaked intelligence documents demonstrating the risks.

The researchers put that access to work on an Autel EV charger fitted with a Quectel EC25-AFX cellular module. By sending commands from the SIM, they were able to exploit a command injection bug in the modem's Linux-based application processor and achieve code execution.

On an Oppo Reno14 F 5G, meanwhile, they found 198 AT commands and variants available through the SIM interface. Among them were commands that could power down the handset, kill its modem, or shove it back onto 2G. The last trick was particularly stubborn: toggling airplane mode, disabling the SIM, and changing the phone's network settings all failed to reverse the downgrade.

The team also demonstrated file theft against a Quectel EG25-G modem, combining a malicious symbolic link with SIM-originating commands to email a targeted file to an attacker-controlled server.

## MORE CONTEXT

* [### MIT boffins' TONTOU attack slips through Spectre defenses on Intel and AMD CPUs](/security/2026/08/07/mit-boffins-tontou-attack-slips-through-spectre-defenses-on-intel-and-amd-cpus/5284081)
* [### I've gone from writing about SD-WAN to depending on it](/networks/2026/08/09/ive-gone-from-writing-about-sd-wan-to-depending-on-it/5285130)
* [### O2 joins UK 2G switch-off with summer 2029 start date](/networks/2026/06/23/o2-joins-uk-2g-switch-off-with-summer-2029-start-date/5260297)
* [### The tech that could make Marvell the next trillion dollar company](/networks/2026/06/03/the-tech-that-could-make-marvell-the-next-trillion-dollar-company/5250472)

Before you start eyeing your SIM tray suspiciously, there is a catch: the attacks require control of the SIM itself. That could come through compromised SIM software, physical tampering, abuse of remote administration by a malicious or breached operator, or supply chain shenanigans.

The researchers also found that vulnerable versions of Android allowed a hostile SIM to invoke the standardized LAUNCH BROWSER command and open an attacker-controlled website without user interaction, even while the phone was locked. Google tracked the flaw as CVE-2025-48618 and patched Android 13 through 16 in December 2025.

REG AD

The researchers disclosed their findings to Google, Oppo, Quectel, Semtech, and Qualcomm in March, followed by the G...