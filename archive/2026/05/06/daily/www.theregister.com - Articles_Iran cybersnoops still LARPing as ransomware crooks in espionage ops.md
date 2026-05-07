---
title: Iran cybersnoops still LARPing as ransomware crooks in espionage ops
url: https://www.theregister.com/security/2026/05/06/iran-cyberspies-larping-as-ransomware-crims-in-espionage-ops/5230993
source: www.theregister.com - Articles
date: 2026-05-06
fetch_date: 2026-05-07T05:35:30.756829
---

# Iran cybersnoops still LARPing as ransomware crooks in espionage ops

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
  + [PaaS + IaaS](/paas_iaas)
  + [SaaS](/saas)
* On-Prem
  + [All On-Prem](/on_prem)
  + [Systems](/systems)
  + [Storage](/storage)
  + [Networks](/networks)
  + [HPC](/hpc)
  + [Personal Tech](/personal_tech)
  + [Cx0](/cxo)
  + [Public Sector](/public_sector)
* Software
  + [All Software](/software)
  + [AI + ML](/ai_ml)
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
* [Amazon](/tag/amazon)
* [Developers](/tag/developer)
* [Open Source](/tag/open%20source)
* [IT Careers](/tag/tech%20jobs)
* [Digital Sovereignty](/tag/digital%20sovereignty)
* [Columnists](/tag/columnists)
* [Who, Me?](/tag/who%20me)
* [On Call](/tag/on%20call/)

REG AD

Security

# Iran cybersnoops still LARPing as ransomware crooks in espionage ops

MOIS-linked cyber outfit puts on a ransomware show to disguise the wide-open backdoor behind the scenes

Connor Jones
[Connor
Jones](https://www.theregister.com/author/connor-jones)
Cybersecurity reporter

Published
wed 6 May 2026 // 17:03 UTC

Researchers at Rapid7 say that they have spotted what they believe was an Iranian intelligence cyber unit masquerading as the Chaos ransomware gang to hide a state-sponsored espionage operation.

The intrusion was spotted earlier this year, and investigators say breadcrumbs left behind give them "medium confidence" in saying it was the work of MuddyWater, which has been linked to intrusions affecting Western government and banking networks in recent months.

Attackers began with a [Microsoft Teams](https://www.theregister.com/2026/04/25/new_crime_crew_impersonates_help_desks/) phishing campaign, which is not uncommon. They also encouraged targets to share their screens. Again, it was nothing too out of the ordinary.

REG AD

However, what must have required some expert persuasion work was that they convinced these individuals to enter their credentials into local text files, and even modify MFA settings to allow attacker-controlled devices to complete authentication.

REG AD

Rapid7 researchers Alexandra Blia and Ivan Feigl [wrote](https://www.rapid7.com/blog/post/tr-muddying-tracks-state-sponsored-shadow-behind-chaos-ransomware/): "While connected, the [threat actor (TA)] executed basic discovery commands, accessed files related to the victim's VPN configuration, and instructed users to enter their credentials into locally-created text files.

"In at least one instance, the TA also deployed a remote management tool (AnyDesk) to further facilitate access."

From there, browser artifacts suggested that attackers lifted credentials through phishing pages. At least one mimicked a [Microsoft Quick Assist](https://www.theregister.com/2024/05/16/microsoft_quick_assist_crime/) page.

Armed with valid credentials, the attackers then executed various commands via RDP, which downloaded payloads using curl. These payloads included a backdoor malware dubbed Darkcomp, a malicious Microsoft WebView2 loader to disguise traffic, and an encrypted configuration file that sent instructions to Darkcomp.

Then it was a case of performing lateral movement by using additional compromised accounts and scooping up sensitive data along the way.

The attackers used the same accounts to send emails internally notifying organization leaders about the intrusion and data theft, and included an onion link leading to Chaos ransomware’s data leak site (DLS), where a corresponding entry appeared with all data redacted and hidden behind a countdown timer.

Follow-up emails aimed to build the illusion of a genuine ransomware attack, although the illusion was short-lived.

## MORE CONTEXT

* [### Pro-Iran crew turns DDoS into shakedown as Ubuntu.com stays down](/security/2026/05/01/pro-iran-group-turns-ubuntu-ddos-into-shakedown/5224575)
* [### 'Hundreds' of Iranian hacking attempts have hit surveillance cameras since the missile strikes](/security/2026/03/04/hundreds-of-iranian-hacking-attempts-hit-ip-cameras/4336780)
* [### Cyber insurers paid out over twice as much for UK ransomware attacks last year](/security/2025/11/11/ransomware-fuels-230-increase-in-uk-cyber-insurance-payouts/1188367)
* [### Yet another ex-ransomware negotiator admits turning rogue after payoff from crimelords](/security/2026/04/21/third-ransomware-pro-pleads-guilty-to-cybercrime-u-turn/5222277)

The attackers instructed recipients to look for a file containing "access credentials" they could use to begin [ransom negotiations](https://www.theregister.com/2026/04/21/yet_another_ex_ransomware_negotiator_pleads/). Unlike the plaintext credential files the attackers had [socially engineered](https://www.theregister.com/2026/03/23/voice_phishing_skyrockets_as_smooth/) the original targets into creating, this file did not actually exist. There was no way to contact the attackers, whereas in a typical scenario the intruders would be looking for a payout.

REG AD

There was also no file encryption, which is inconsistent with Chaos affiliates' typical way of working.

"Despite these inconsistencies in the initial proof-of-compromise, the TA later published the stolen data on its DLS in line with modern extortion tactics," Blia and Feigl wrote. "The leaked data was assessed to be legitimate."

### If not for financial gain, then what?

MuddyWater – if that is indeed the group behind this – did not extort the organizations in question, nor did they deploy a ransomware payload, but they did pose as an established ranso...