---
title: Angry bug hunter with Microsoft beef drops new Windows 0-day
url: https://www.theregister.com/security/2026/06/10/nightmare-eclipse-publishes-new-windows-defender-zero-day/5253725
source: www.theregister.com - Articles
date: 2026-06-10
fetch_date: 2026-06-11T06:37:03.522302
---

# Angry bug hunter with Microsoft beef drops new Windows 0-day

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

Security

# Angry bug hunter with Microsoft beef drops new Windows 0-day

Revenge is a dish best served code

Jessica Lyons
[Jessica
Lyons](https://www.theregister.com/author/jessica-lyons)

Published
wed 10 Jun 2026 // 19:45 UTC

They are angry at Redmond and will have their revenge. Nightmare Eclipse, the prolific bug hunter and possibly disgruntled ex-Microsoft employee, disclosed another zero-day vulnerability just hours after Redmond issued a record-breaking number of CVEs and fixes for June [Patch Tuesday](https://www.theregister.com/patches/2026/06/09/ai-is-making-patch-tuesday-kinda-fun-again/5253225).

The latest zero-day, RoguePlanet, targets Microsoft Defender and works against fully patched Windows 10 and Windows 11 systems, according to the researcher, who also released [proof-of-concept exploit code](https://git.projectnightcrawler.dev/NightmareEclipse/RoguePlanet) for the security flaw. Assuming the attacker can win a race condition, this bug allows local privilege escalation and leads to SYSTEM-level control over an affected machine.

Nightmare Eclipse (aka Chaotic Eclipse) is a disgruntled bug hunter with a deep understanding of Windows and an even deeper grudge against Microsoft. They [claim to be an ex-employee](https://infosec.exchange/%40briankrebs/116661298779426573), and accuse Redmond of ignoring vulnerability reports and refusing to communicate with them.

REG AD

"When I actively asked you to communicate with me, you refused, humiliated me and made sure to insult me in front of people," they wrote in an earlier blog post that also promised a [“bone shattering” drop](https://www.theregister.com/security/2026/05/28/microsoft-0-day-feud-escalates-as-researcher-threatens-another-windows-exploit-dump/5248085) on July 14.

REG AD

"You defame me in public with your CVE-2026-45585 advisory even though you literally deleted the Microsoft account I used to report bugs to you with and I got zero pennies from doing so and I still happily did like an idiot," the post [continued](https://deadeclipse666.blogspot.com/2026/05/july-14th.html).

Possibly as an outlet for this anger, and reportedly in response to Redmond's lack of action, Nightmare began releasing their findings to the public. [RoguePlanet](https://deadeclipse666.blogspot.com/2026/06/rogueplanet-quick-history.html) marks the [seventh Microsoft zero-day](https://git.projectnightcrawler.dev/NightmareEclipse) that they found and disclosed - accompanied by either a PoC exploit or technical details - before Redmond issued a fix.

Microsoft's initial [response](https://www.microsoft.com/en-us/msrc/blog/2026/05/a-shared-responsibility-protecting-customers-through-coordinated-vulnerability-disclosure) to those disclosures was widely interpreted as a threat of legal action, prompting [massive outrage](https://www.theregister.com/security/2026/06/02/microsoft-reaches-for-olive-branch-after-public-dustup-with-0-day-researcher/5249945) from the broader infosec community before Redmond sought to calm the backlash by stating it had "no intention to pursue action against individuals conducting or publishing security research."

As of Tuesday, the previous six zero-days all have patches.

Three of them, [RedSun](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-41091), [UnDefend](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-45498), and [BlueHammer](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-33825), came under attack soon after Nightmare published working exploit code for each and before Microsoft released security updates to address the flaws. The other three, [YellowKey, GreenPlasma](https://www.theregister.com/security/2026/05/13/disgruntled-researcher-releases-two-more-microsoft-zero-days/5239758), and MiniPlasma, all have been fixed as of June’s Patch Tuesday.

## MORE CONTEXT

* [### AI is making Patch Tuesday (kinda) fun again](/patches/2026/06/09/ai-is-making-patch-tuesday-kinda-fun-again/5253225)
* [### Disgruntled 0-day hunter 'humiliated' by Microsoft pledges 'bone shattering drop' as Redmond calls cops](/security/2026/05/28/microsoft-0-day-feud-escalates-as-researcher-threatens-another-windows-exploit-dump/5248085)
* [### Microsoft reaches for olive branch after public dustup with 0-day researcher](/security/2026/06/02/microsoft-reaches-for-olive-branch-after-public-dustup-with-0-day-researcher/5249945)
* [### Another bug hunter leaks Microsoft exploits in defiance of company’s handling of vulnerability disclosures](/security/2026/06/03/another-bug-hunter-leaks-microsoft-exploits-in-defiance-of-companys-handling-of-vulnerability-disclosures/5250590)

YellowKey (aka [CVE-2026-45585](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2...