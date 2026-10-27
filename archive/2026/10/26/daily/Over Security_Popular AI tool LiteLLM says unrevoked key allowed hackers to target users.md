---
title: Popular AI tool LiteLLM says unrevoked key allowed hackers to target users
url: https://therecord.media/litellm-hackers-ai-malware
source: Over Security
date: 2026-10-26
fetch_date: 2026-10-27T07:05:38.050497
---

# Popular AI tool LiteLLM says unrevoked key allowed hackers to target users

![](https://recordedfuture.matomo.cloud/matomo.php?idsite=2&rec=1)

[![Cyber Security News  | The Record](https://cms.therecord.media/uploads/The_Record_Centered_9b27d79125.svg)](/)

* [Leadership](/news/leadership)
* [Cybercrime](/news/cybercrime)
* [Nation-state](/news/nation-state)
* [Influence Operations](/news/influence-operations)
* [Technology](/news/technology)

* [Cyber Daily®](https://therecord.media/subscribe)
* [Click Here Podcast](/podcast)

Go

Subscribe to The Record

[✉️ Free Newsletter](/subscribe)

![LiteLLM](https://cms.therecord.media/uploads/large_Lite_LLM_be1a113cd2.jpg)

[Alexander Martin](/author/alexander-martin)October 26th, 2026

# Popular AI tool LiteLLM says unrevoked key allowed hackers to target users

LiteLLM, an open-source tool widely used by artificial intelligence developers, said Friday that a key accidentally exposed in May was behind a supply-chain attack that is believed to have hit tens of thousands of users last week.

In a root-cause analysis [published](https://docs.litellm.ai/blog/security-incident-oct-21-2026-attack-chain) Friday, the project traced the attack to the company's own mistaken exposure months before of a configuration file containing the master key to an internal tool used by LiteLLM to run AI agents.

Although the company spotted the publication at the time and removed the file, it failed to revoke the exposed key. Earlier this month, an unidentified attacker used the key to access LiteLLM’s tooling and grab an access token giving them control over all of LiteLLM’s repositories on GitHub.

According to the [initial incident report](https://docs.litellm.ai/blog/security-incident-oct-21-2026), the attacker then exploited "multiple independent security controls” last week to distribute a version of the tool containing credential-harvesting malware to the software’s users.

Google-owned cloud security company Wiz [said](https://www.wiz.io/blog/litellm-compromised-steals-credentials) the compromised package was downloaded about 49,000 times and that the cloud credentials stolen from LiteLLM users were being tested within hours.

The malicious package remained on the Python Package Index (PyPI) for about two hours. Within about four and a half hours of it being initially uploaded, the attacker was trying out stolen login credentials for Amazon’s AWS cloud service to see which of Amazon’s AI models the accounts could access.

Wiz said this matched a pattern known as “LLMjacking,” in which criminals use stolen cloud accounts to run AI services and leave the victims with the bill. No affected organization has publicly confirmed a breach linked to the release.

According to [Microsoft](https://www.microsoft.com/en-us/security/blog/2026/10/23/inside-the-litellm-1-107-0-supply-chain-compromise-credential-theft-through-python-startup-hooks/), the malware was designed to run whenever the Python programming language started up on an infected machine, even if the program that was being run never used LiteLLM itself.

LiteLLM warned that anyone who installed the compromised version (1.107.0) on an internet-connected computer should assume their credentials were stolen. Those entities were advised to change every password and access key that the affected computer could reach.

LiteLLM said it too was revoking tokens across its internal systems and vendor platforms.

The incident is the second supply chain compromise of LiteLLM this year. In March, attackers [published malicious versions to PyPI](https://therecord.media/supply-chain-attack-hits-widely-used-ai-package) in a campaign later linked to the TeamPCP hacking group. Australian police have since [charged two men](https://therecord.media/australia-teampcp-hackers-arrested) alleged to be TeamPCP members.

* [News](/ukraine-says-starshield-working-again-after-disruption)
* [Cybercrime](/news/cybercrime)
* [Malware](/news/malware)

[![Recorded Future](https://cms.therecord.media/uploads/2025_0514_Record_Ads_300x1050_1_0f2f11757e.png)](https://www.recordedfuture.com/?utm_source=therecord&utm_medium=referral&utm_content=post-sidebar-ad)

[![Recorded Future](https://cms.therecord.media/uploads/2025_0514_Record_Ads_970x250_1_d144dbf901.png)](https://www.recordedfuture.com/?utm_source=therecord&utm_medium=referral&utm_content=post-footer-ad)

No previous article

No new articles

[![Alexander Martin](https://cms.therecord.media/uploads/headshot_79eb085f87.jpeg)](/author/alexander-martin)

[Alexander Martin](/author/alexander-martin)

is the UK Editor for Recorded Future News. He was previously a technology reporter for Sky News and a fellow at the European Cyber Conflict Research Initiative, now Virtual Routes. He can be reached securely using Signal on: AlexanderMartin.79

## Briefs

* [FCC bans two devices with surveillance chips linked to HuaweiOctober 23rd, 2026](/fcc-bans-devices-huawei-surveillance-chips)
* [Quest Diagnostics warns of potential data theft after attack on lab service systemOctober 23rd, 2026](/quest-diagnostics-network-intrusion)
* [23andMe successor settles with California for $6 million over cybersecurity failings October 20th, 2026](/23andme-california-data-breach-settlement)
* [Ahold Delhaize confirms 'malicious actions' behind cyber outages affecting grocery brandsOctober 19th, 2026](/ahold-delhaize-cyberattack-grocery)
* [Hackers steal customer data from major Russian hosting provider FirstVDSOctober 19th, 2026](/russia-cyberattack-firstvds-cloud)
* [Proofpoint lines up $6.3 billion deal for Varonis’ data securityOctober 16th, 2026](/proofpoint-varonis-cybersecurity-acquisition)
* [North Macedonian police arrest alleged administrator behind OLVX cybercrime marketOctober 14th, 2026](/olvx-cybercrime-marketplace-arrest-north-macedonia)
* [Russian travel booking platform suspends reservations after cyberattackOctober 14th, 2026](/russia-anywayanyday-travel-website-cyberattack)
* [Ledger says hardware implant in cryptocurrency wallets stole recovery phrasesOctober 13th, 2026](/ledger-cryptocurrency-wallet-implant-theft)

[## Russia Is Tightening Internet Controls, Leading to Operational Risks

![Russia Is Tightening Internet Controls, Leading to Operational Risks](https://www.recordedfuture.com/research/media_15293b1d04e3625addc9744aee1fd4f5d351f20d5.gif?width=1200&format=pjpg&optimize=medium)](https://www.recordedfuture.com/research/russia-restrictive-info-environment?utm_source=therecord&utm_medium=referral&utm_content=post-sidebar-insikt)

[## Japan Adopts Proactive Cyber Defense Strategy

![Japan Adopts Proactive Cyber Defense Strategy](https://www.recordedfuture.com/research/media_1a84dcf04185d74b31dd79c69ae7b02f3abdd3ac5.gif?width=1200&format=pjpg&optimize=medium)](https://www.recordedfuture.com/research/japan-cyber-defense-strategy?utm_source=therecord&utm_medium=referral&utm_content=post-sidebar-insikt)

[## Tajin Group: Guarantee Marketplace Vendor Involved in Phishing and Chinese Money Laundering Group

![Tajin Group: Guarantee Marketplace Vendor Involved in Phishing and Chinese Money Laundering Group](https://www.recordedfuture.com/research/media_19443a31217a8436e06a126301298ec61f9f5d1f3.gif?width=1200&format=pjpg&optimize=medium)](https://www.recordedfuture.com/research/tajin-group-gurantee-marketplace?utm_source=therecord&utm_medium=referral&utm_content=post-sidebar-insikt)

[## H1 2026 Malware Vulnerability Trends

![H1 2026 Malware Vulnerability Trends](https://www.recordedfuture.com/research/media_10e2d2b0a84b6ce4d9cf7dd1adb4821a04fe3a574.gif?width=1200&format=pjpg&optimize=medium)](https://www.recordedfuture.com/research/h1-2026-malware-vulnerability-trends?utm_source=therecord&utm_medium=referral&utm_content=post-sidebar-insikt)

[## BlueDelta Targets Defense and Diplomacy with HOOKEDGE

![BlueDelta Targets Defense and Diplomacy with HOOKEDGE](https://www.recordedfuture.com/research/media_15e5a0dd42b0a3fdefe4c79a19da6050a2f0cf2e4.gif?width=1200&format=pjpg&optimize=medium)](https://www.recordedfuture.com/research/blued...