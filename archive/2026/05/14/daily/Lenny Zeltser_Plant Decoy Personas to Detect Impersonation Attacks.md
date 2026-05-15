---
title: Plant Decoy Personas to Detect Impersonation Attacks
url: https://zeltser.com/the-notion-of-a-honeypot-persona
source: Lenny Zeltser
date: 2026-05-14
fetch_date: 2026-05-15T05:53:22.478361
---

# Plant Decoy Personas to Detect Impersonation Attacks

[Lenny Zeltser](/)Security builder & leader

 [Projects](/projects) [Writing](/writing) [About](/about)

×

# Plant Decoy Personas to Detect Impersonation Attacks

Decoy personas extend honeytoken thinking to user accounts and public profiles. The technique gives defenders a tripwire on the identity surface that other detection layers don't cover.

![Plant Decoy Personas to Detect Impersonation Attacks - illustration](/assets/the-notion-of-a-honeypot-persona.h63dEXxP_Z2t4o2g.webp)

A *decoy persona* is a fake identity established to catch attackers as they probe your workforce. Plant it wherever threat actors look for employees to pursue in scams and other attacks. The unexpected interaction lets you detect the incident, so you can curtail it before it escalates.

## No one legitimate should touch a decoy persona.

An effective decoy is a privileged-looking user account in your directory that fires when someone tries to use it. You can set up your SIEM tool to alert you when someone accesses the account. Customers of Microsoft Defender for Identity can also achieve this through the product’s [honeytoken tagging](https://learn.microsoft.com/en-us/defender-for-identity/entity-tags) feature.

On the public web, you can apply the same pattern to a LinkedIn profile representing a fictional employee (consider LinkedIn’s terms of use). Connection requests, recruiter outreach, and InMail attempts all become signals because the person doesn’t exist. A fake executive email address in a public org chart offers similar value after you filter out the spam. So does a decoy press contact an attacker reaches for during a social-engineering pretext.

Decoy personas rely on asymmetry. Since you know which identities are decoys and the attacker doesn’t, any contact with one is a useful alert.

## A convincing decoy needs a backstory and isolation from production.

Attackers can fingerprint thin LinkedIn profiles and dismiss them as bait. A convincing decoy incorporates prior employers, posting activities, and a social network that fits the role. The same principle applies to internal directory accounts: names like `test_admin` or `decoy01` give the bait away. Researchers cataloging [Canarytoken fingerprints](https://trufflesecurity.com/blog/canaries) make a similar point about file-based bait.

Isolate identity paths between the decoy and the production environment. A decoy account should never share SSO, MFA, or directory backends with production accounts. Use disposable credentials and a separate identity store. If session cookies, VPN configs, or outbound rules overlap with production services, the decoy can enable lateral movement.

## Plant a decoy persona this week.

Decoy personas are an identity tripwire in your [deception architecture](/protean-information-security-architecture), alongside [honeytokens](/plant-honeytokens) and [decoy MCP servers](/decoy-mcp-server-honeypot). They alert you early in the attack chain, giving you a chance to intervene before it escalates.

Receive my blog posts by email.

Email addressSubscribe

### Related Articles

[![](/assets/decoy-mcp-server-honeypot.Bz7gHKFH_Z2fPy7U.webp)Build a Decoy MCP Server to Catch AI Agent Attackers](/decoy-mcp-server-honeypot)[![](/assets/plant-honeytokens.CNZJoYK1_1paY3O.webp)Plant Honeytokens to Detect Intrusions](/plant-honeytokens)

### About the Author

Lenny Zeltser is a cybersecurity executive with deep technical roots, product management experience, and a business mindset. He has built security products and programs from early stage to enterprise scale. He is also a Faculty Fellow at SANS Institute and the creator of REMnux, a popular Linux toolkit for malware analysis. Lenny shares his perspectives on security leadership and technology at [zeltser.com](/).

Get posts by emailEmail addressSubscribe

Copy link

More on

[Deception](/topic/deception)[Social Engineering](/topic/social-engineering)

2 min to read

May 14, 2026

   [Projects](/projects) [Writing](/writing) [About](/about) [Newsletter](/newsletter) [RSS](/rss.xml)

© 2026 [Lenny Zeltser](/)