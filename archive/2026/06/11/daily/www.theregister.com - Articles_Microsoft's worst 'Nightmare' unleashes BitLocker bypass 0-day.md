---
title: Microsoft's worst 'Nightmare' unleashes BitLocker bypass 0-day
url: https://www.theregister.com/security/2026/06/11/nightmare-eclipse-drops-claimed-bitlocker-bypass-for-microsoft-windows/5254371
source: www.theregister.com - Articles
date: 2026-06-11
fetch_date: 2026-06-12T06:28:15.640306
---

# Microsoft's worst 'Nightmare' unleashes BitLocker bypass 0-day

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

# Microsoft's worst 'Nightmare' unleashes BitLocker bypass 0-day

Another day, another Windows exploit code

Jessica Lyons
[Jessica
Lyons](https://www.theregister.com/author/jessica-lyons)

Published
thu 11 Jun 2026 // 18:51 UTC

Nightmare Eclipse, the prolific zero-day vulnerability hunter with an axe to grind against Microsoft, released yet another exploit late Wednesday that the researcher claims will spawn a command prompt that provides total access to the BitLocker volume.

This bug, called [GreatXML](https://deadeclipse666.blogspot.com/2026/06/greatxml-bitlocker-that-seems-to-only.html), was “an accidental discovery,” according to the researcher, who said it only took four hours to find. They claim this exploit (published on [GitHub](https://github.com/MSNightmare/GreatXML) and [Git](https://git.projectnightcrawler.dev/NightmareEclipse/GreatXML)-based code-hosting platforms) can bypass BitLocker on any system that has ever run a [Microsoft Defender Offline scan](https://learn.microsoft.com/en-us/defender-endpoint/microsoft-defender-offline) at any point in the past.

GreatXML comes just a day after Nightmare released exploit code for RoguePlanet, which allows local privilege escalation and leads to SYSTEM-level control over an affected machine. This brings the researcher’s zero-day count to eight. The earlier six - [RedSun](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-41091), [UnDefend](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-45498), [BlueHammer](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-33825), [YellowKey, GreenPlasma,](https://www.theregister.com/security/2026/05/13/disgruntled-researcher-releases-two-more-microsoft-zero-days/5239758) and [MiniPlasma](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2020-17103) - all have patches as of this week’s [Patch Tuesday](https://www.theregister.com/patches/2026/06/09/ai-is-making-patch-tuesday-kinda-fun-again/5253225) event.

REG AD

REG AD

Redmond on Wednesday [told](https://www.theregister.com/security/2026/06/10/nightmare-eclipse-publishes-new-windows-defender-zero-day/5253725) The Register that it is aware of RoguePlanet, and “actively investigating the validity and potential applicability of these claims.” The Windows giant didn’t immediately respond to our inquiries about GreatXML, including when it planned to issue a patch.

Microsoft has said none of the vulnerabilities were reported via its official channels prior to being made public. The company also banned Nightmare’s earlier GitHub account, and [seemingly threatened legal action](https://www.theregister.com/security/2026/05/28/microsoft-0-day-feud-escalates-as-researcher-threatens-another-windows-exploit-dump/5248085) before [dialing back its rhetoric](https://www.theregister.com/security/2026/06/02/microsoft-reaches-for-olive-branch-after-public-dustup-with-0-day-researcher/5249945) after steep backlash from the security community.

## MORE CONTEXT

* [### Angry bug hunter with Microsoft beef drops new Windows 0-day](/security/2026/06/10/nightmare-eclipse-publishes-new-windows-defender-zero-day/5253725)
* [### Another bug hunter leaks Microsoft exploits in defiance of company’s handling of vulnerability disclosures](/security/2026/06/03/another-bug-hunter-leaks-microsoft-exploits-in-defiance-of-companys-handling-of-vulnerability-disclosures/5250590)
* [### Microsoft reaches for olive branch after public dustup with 0-day researcher](/security/2026/06/02/microsoft-reaches-for-olive-branch-after-public-dustup-with-0-day-researcher/5249945)
* [### Disgruntled 0-day hunter 'humiliated' by Microsoft pledges 'bone shattering drop' as Redmond calls cops](/security/2026/05/28/microsoft-0-day-feud-escalates-as-researcher-threatens-another-windows-exploit-dump/5248085)

Nightmare Eclipse, who some researchers [suggest](https://infosec.exchange/%40briankrebs/116661298779426573) is an ex-Microsoft employee, harbors a very personal grudge against the Windows giant and its communications with bug hunters. They have promised to keep the zero-days coming, but waffle on the timing.

Last month, the researcher [pledged](https://deadeclipse666.blogspot.com/2026/05/) a big July 14 drop: “I will make sure your bones are shattered that day,” and then added, “nothing will be released this June (or maybe I will release smtg, depending on circumstances).”

On Tuesday, they [changed course](https://deadeclipse666.blogspot.com/2026/06/regarding-july-14th.html). “I will be unable to mass disclose zerodays in July 14th, RoguePlanet took way more time than expected and truly drained me. I might take a break but I can't say for sure what I will be doing for next month, maybe it's nothing, maybe...