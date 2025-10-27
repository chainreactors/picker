---
title: The $1.5B Bybit Hack: The Era of Operational Security Failures Has Arrived
url: https://blog.trailofbits.com/2025/02/21/the-1.5b-bybit-hack-the-era-of-operational-security-failures-has-arrived/
source: The Trail of Bits Blog
date: 2025-02-22
fetch_date: 2025-10-06T20:35:49.273161
---

# The $1.5B Bybit Hack: The Era of Operational Security Failures Has Arrived

[The Trail of Bits Blog](/ "The Trail of Bits Blog")

[![Trail of Bits Logo](/img/tob.png)](https://trailofbits.com "Trail of Bits")

# The $1.5B Bybit Hack: The Era of Operational Security Failures Has Arrived

[Dan Guido](https://x.com/dguido), [Benjamin Samuels](https://x.com/thebensams), Anish Naik

February 21, 2025

[blockchain](/categories/blockchain/), [policy](/categories/policy/)

Page content

* [The Attack](#the-attack)
* [The DPRK’s Cryptocurrency Theft Infrastructure](#the-dprks-cryptocurrency-theft-infrastructure)
* [The New Reality of Cryptocurrency Security](#the-new-reality-of-cryptocurrency-security)
* [Moving Forward](#moving-forward)

Two weeks ago at the [DeFi Security Summit](https://x.com/trailofbits/status/1893008382677659893), Trail of Bits’ Josselin Feist (@Montyly) was asked if we’d see a billion-dollar exploit in 2025. His response: “If it happens, it won’t be a smart contract, it’ll be an operational security issue.”

Today, that prediction was validated.

## The Attack

On February 21, 2025, cryptocurrency exchange [Bybit suffered the largest cryptocurrency theft](https://x.com/gauthamzzz/status/1893004593979859410) in history when attackers stole approximately $1.5B from their multisig cold storage wallet. At this time, it appears the attackers compromised multiple signers’ devices, manipulated what signers saw in their wallet interface, and collected the required signatures while the signers believed they were conducting routine transactions.

This hack is one of many that represent a dramatic shift in how centralized exchanges are compromised. For years, the industry has focused on hardening code and improving their technical security practices, but as the ecosystem’s secure development life cycle has matured, attackers have shifted to targeting the human and operational elements of cryptocurrency exchanges and other organizations.

These attacks reveal an escalating pattern, with each compromise building on the last:

* [WazirX Exchange](https://blog.solidityscan.com/wazirx-hack-analysis-8bc8821928e9) ($230M, July 2024)
* [Radiant Capital](https://medium.com/%40RadiantCapital/radiant-post-mortem-fecd6cd38081) ($50M, October 2024)
* [Bybit Exchange](https://www.bloomberg.com/news/articles/2025-02-21/bybit-says-exchange-wallet-hacked-1-5-billion-estimated-loss?utm_source=website&utm_medium=share&utm_campaign=copy) ($1.5B, February 2025)

In each case, the attackers didn’t exploit smart contract or application-level vulnerabilities. Instead, they compromised the computers used to manage those systems using sophisticated malware to manipulate what users saw versus what they actually signed.

## The DPRK’s Cryptocurrency Theft Infrastructure

These hacks are not isolated incidents. According to [Arkham Intelligence](https://x.com/arkham/status/1893033424224411885), famed researcher [ZachXBT](https://x.com/zachxbt) has provided definitive proof linking this attack to North Korea, including detailed analysis of test transactions and connected wallets used ahead of the exploit. These incidents represent the maturation of sophisticated attack capabilities developed by [North Korean state-sponsored threat actors](https://www.fbi.gov/news/press-releases/fbi-dc3-and-npa-identification-of-north-korean-cyber-actors-tracked-as-tradertraitor-responsible-for-theft-of-308-million-from-bitcoindmmcom), specifically groups tracked as [TraderTraitor](https://www.cisa.gov/news-events/cybersecurity-advisories/aa22-108a%20), [Jade Sleet](https://www.microsoft.com/en-us/security/security-insider/intelligence-reports/east-asia-threat-actors-employ-unique-methods), [UNC4899](https://cloud.google.com/blog/topics/threat-intelligence/north-korea-supply-chain), and [Slow Pisces](https://unit42.paloaltonetworks.com/threat-assessment-north-korean-threat-groups-2024/) under the DPRK’s Reconnaissance General Bureau (RGB).

![Figure 1: Organizational structure of DPRK cyber threat actors under the Reconnaissance General Bureau (RGB). This chart shows the relationship between different threat groups and their various industry designations. Source: Palo Alto Networks Unit 42, September 2024](/img/dprk-rgb-structure.png)

Figure 1: Organizational structure of DPRK cyber threat actors under the Reconnaissance General Bureau (RGB). This chart shows the relationship between different threat groups and their various industry designations. Source: Palo Alto Networks Unit 42, September 2024

The attack chain typically begins with [aggressive social engineering campaigns](https://github.blog/security/vulnerability-research/security-alert-social-engineering-campaign-targets-technology-industry-employees/) targeting multiple employees simultaneously within an organization. The RGB identifies key personnel in system administration, software development, and treasury roles, then creates detailed pretexts - often elaborate job recruitment schemes - customized to each target’s background and interests. These aren’t mass phishing campaigns; they’re meticulously crafted approaches designed to compromise specific individuals with access to critical systems.

What makes these attacks particularly concerning is their repeatability. The RGB has built a sophisticated cross-platform toolkit that can:

* Operate seamlessly across Windows, MacOS, and various wallet interfaces
* Show minimal signs of compromise while maintaining persistence
* Function as backdoors to execute arbitrary commands
* Download and execute additional malicious payloads
* Manipulate what users see in their interfaces

[Each successful compromise](https://github.com/tayvano/lazarus-bluenoroff-research) has allowed the RGB to refine their tools and techniques. They’re not starting from scratch with each target - they’re executing a tested playbook that’s specifically engineered to defeat standard cryptocurrency security controls when those controls are used in isolation.

Organizations below a certain security threshold are now at serious risk. Without comprehensive security controls including:

* Air-gapped signing systems
* Multiple layers of transaction verification
* Endpoint detection and response (EDR) systems like CrowdStrike or SentinelOne
* Regular security training and war games

They are likely to face an adversary that has already built and tested the exact tools needed to defeat their existing protections.

## The New Reality of Cryptocurrency Security

This attack highlights a fundamental truth: no single security control, no matter how robust, can protect against sophisticated attackers targeting operational security. While secure code remains crucial, it must be part of a comprehensive security strategy.

Organizations must adopt new processes and controls that operate under the assumption that their infrastructure will eventually face compromise:

1. **Infrastructure Segmentation:** Critical operations like transaction signing require both physical and logical separation from day-to-day business operations. This isolation ensures that a breach of corporate systems cannot directly impact signing infrastructure. Critical operations should use dedicated hardware, separate networks, and strictly controlled access protocols.
2. **Defense-in-Depth:** Security controls must work in concert - hardware wallets, multi-signature schemes, and transaction verification tools each provide important protections, but true security emerges from their coordinated operation. Organizations need multiple, overlapping controls that can detect and prevent sophisticated attacks.
3. **Organizational Preparedness:** Technical controls must be supported by comprehensive security programs that include:
   * Thorough threat modeling incorporating both technical and operational risks
   * Regular third-party security assessments of infrastructure and procedures
   * Well-documented and frequently tested incident response plans
   * Ongoing security awareness training tailored to specific roles
   * War games and atta...