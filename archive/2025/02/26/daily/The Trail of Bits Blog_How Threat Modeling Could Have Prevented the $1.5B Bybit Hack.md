---
title: How Threat Modeling Could Have Prevented the $1.5B Bybit Hack
url: https://blog.trailofbits.com/2025/02/25/how-threat-modeling-could-have-prevented-the-1.5b-bybit-hack/
source: The Trail of Bits Blog
date: 2025-02-26
fetch_date: 2025-10-06T20:34:43.574252
---

# How Threat Modeling Could Have Prevented the $1.5B Bybit Hack

[The Trail of Bits Blog](/ "The Trail of Bits Blog")

[![Trail of Bits Logo](/img/tob.png)](https://trailofbits.com "Trail of Bits")

# How Threat Modeling Could Have Prevented the $1.5B Bybit Hack

[Benjamin Samuels](https://x.com/thebensams)

February 25, 2025

[blockchain](/categories/blockchain/), [threat modeling](/categories/threat-modeling/)

Page content

* + [Understanding Threat Modeling in Blockchain Security](#understanding-threat-modeling-in-blockchain-security)
  + [The Bybit Hack Through a Threat Modeling Lens](#the-bybit-hack-through-a-threat-modeling-lens)
  + [Introducing Threat Modeling Into Your Organization](#introducing-threat-modeling-into-your-organization)
  + [How Trail of Bits Can Help](#how-trail-of-bits-can-help)
  + [Threat Modeling as Strategic Defense](#threat-modeling-as-strategic-defense)

On February 21, 2025, cryptocurrency exchange Bybit suffered a [devastating $1.5 billion hack](https://x.com/gauthamzzz/status/1893004593979859410), the largest in crypto history. This wasn’t due to smart contract flaws or coding errors but rather a sophisticated operational security failure allowing attackers to compromise signers’ devices and manipulate transaction data.

This attack follows a disturbing pattern we’ve observed over the past year, with similar breaches at [WazirX ($230M)](https://blog.solidityscan.com/wazirx-hack-analysis-8bc8821928e9) and [Radiant Capital ($50M)](https://medium.com/%40RadiantCapital/radiant-post-mortem-fecd6cd38081). In each case, attackers targeted human and operational elements rather than exploiting code vulnerabilities.

As attackers shift from technical exploits to operational security gaps, threat modeling becomes essential. Traditional code audits find implementation issues in code, but only comprehensive threat modeling can reveal the systemic operational and design weaknesses that enabled these most recent breaches.

At Trail of Bits, we’ve conducted numerous threat models for blockchain organizations over the years, though most of these assessments remain confidential as clients typically decline to publish them. This creates an information gap in the industry about the effectiveness of threat models in preventing devastating attacks like the one Bybit experienced.

Building on our [previous analysis of the Bybit hack](https://blog.trailofbits.com/2025/02/21/the-1.5b-bybit-hack-the-era-of-operational-security-failures-has-arrived/) where we discussed how the era of operational security failures has arrived, we’ll now explore specific threat modeling techniques that could have identified these vulnerabilities before they were exploited.

### Understanding Threat Modeling in Blockchain Security

Threat modeling is a structured approach to identifying security risks in a system’s architecture, data flows, operational procedures, and human elements. Unlike code review audits, which find implementation bugs, threat models reveal systemic and operational weaknesses — precisely the kind that led to the Bybit hack.

Here’s how our approach breaks down:

1. **Establish a set of security controls.** We establish a set of security controls based on [NIST SP 800-53](https://csrc.nist.gov/pubs/sp/800/53/r5/upd1/final) and use these controls to guide the engagement.
2. **Component Identification**: We identify all in-scope system components, from wallet infrastructure to API services, user interfaces, internal admin tools, and third-party integrations.
3. **Actor Analysis**: We identify all actors interacting with the system, including legitimate users, administrators, and potential attackers. This helps us understand who can access what and what privileges they have.
4. **Trust Zone Mapping**: We group components into “trust zones” based on shared purpose, ownership, or level of potential damage. Trust zones are bounded by trust boundaries, which typically occur where authentication and authorization are required to obtain a higher level of privilege within the system.
5. **Data Flow Analysis**: We map how data moves between components and across trust boundaries, identifying where sensitive information might be exposed or manipulated and which threat actors could do so.
6. **Threat Scenario Development**: For each trust boundary crossing, we analyze potential attack vectors and develop realistic threat scenarios that show how design vulnerabilities could be exploited.

### The Bybit Hack Through a Threat Modeling Lens

The Bybit hack exemplifies a sophisticated operational security breach that we believe could have been identified and mitigated through comprehensive threat modeling tightly integrated into the exchange’s software development lifecycle. Let’s examine what happened through this lens.

#### Attack Mechanics and Failed Controls

Attackers compromised the Safe signing frontend which was used by all of the Bybit multisig signers. When these individuals thought they were authorizing routine transactions, they were actually signing transactions that changed the implementation address of their Safe multi-sig wallet and replaced it with a malicious implementation that granted the attacker control, bypassing the security intention of the multi-sig entirely.

Attackers exploited the contract’s EVM `delegatecall` function and deployed malware to manipulate the signing interface. The signers could not see what they were signing due to two critical issues: malware that modified the wallet interface and the limitation of blind signing on hardware wallets, which do not display complete semantic information on what is being signed by the user.

Performing a threat model during the design phase of the software development lifecycle (SDLC) may have informed Bybit that their system contains the following control failures that require mitigation:

#### 1. Endpoint Security Controls

* **Description:** The cold wallet’s signers likely used general-purpose workstations[1](#fn:1) for sensitive transaction signing operations, creating a broad attack surface for device compromise.
* **Identified Risk**: Compromise of signer devices could lead to transaction manipulation
* **Recommendation**: Implement dedicated signing workstations with limited connectivity, and if the devices must be online, add enhanced monitoring. In addition, smart contracts may be added to the system to time-lock the movement of funds to allow time for incident response or restrict where funds may be sent entirely.

#### 2. Transaction Verification Process

* **Description:** Cold wallet signers likely relied on a single verification interface without secondary confirmation mechanisms[1](#fn:1), leaving signers unable to detect manipulated transaction details.
* **Identified Risk**: Blind signing can hide transaction details
* **Recommendation**: Implement secondary verification using transaction verification scripts such as [the one maintained](https://github.com/pcaversaccio/safe-tx-hashes-util) by [@pcaversaccio](https://x.com/pcaversaccio/status/1848303346421047743). This should be performed on a separate secure workstation to reduce the impact of compromised signer workstations, and signers should thoroughly compare the transaction hashes displayed by the verification script and hardware wallet byte-by-byte.

#### 3. Safe Wallet Configuration

* **Description:** The multisig wallet was configured to allow `delegatecall` operations, which enabled attackers to alter the wallet’s concrete implementation.
* **Identified Risk**: `delegatecall` operations can change the semantics of transactions being signed by offline or partially offline signer workstations. While `delegatecall` operations are not a vulnerability on their own, their use in this system creates a design weakness.
* **Recommendation**: Disable `delegatecall` functionality entirely, or alternately, design the on-chain components so a signature is only valid for a specific implementation being called into by `delegatecall`.

#### 4. Operational Segregation

* **Description...