---
title: FortiBleed 2.0: 975 New Domains & 40,573 Exposed Secrets - Claim Your Ethical Disclosure
url: https://www.infostealers.com/article/fortibleed-2-0-975-new-domains-40573-exposed-secrets-claim-your-ethical-disclosure/
source: Over Security
date: 2026-10-27
fetch_date: 2026-10-28T07:49:24.141903
---

# FortiBleed 2.0: 975 New Domains & 40,573 Exposed Secrets - Claim Your Ethical Disclosure

[Skip to content](#site-main)

[![](https://www.infostealers.com/wp-content/themes/infostealers-sage/resources/images/infostealers-icon-black.png)
![](https://www.infostealers.com/wp-content/themes/infostealers-sage/resources/images/infostealers-icon-white.png)

INFOSTEALERS

By HudsonRock](https://www.infostealers.com/)

[Home](https://www.infostealers.com/)
[Blog](https://www.infostealers.com/learn-info-stealers/)
[Reports](https://www.infostealers.com/info-stealers-reports/)
[Threat Feeds](https://www.infostealers.com/threat-feeds/)
[Victims](https://www.infostealers.com/infostealer-victims/)

Resources

* [Infostealer Index
  Intelligence vendors ranked and compared](https://www.infostealers.com/infostealer-index/)
* [Techniques
  MITRE ATT&CK mapped by stealer family](https://www.infostealers.com/info-stealers-techniques/)
* [Glossary
  Cybercrime terms in plain language](https://www.infostealers.com/glossary/)

[About](https://www.infostealers.com/about-info-stealers/)

Search
`⌘K`

Free Individual Protection

![](https://www.infostealers.com/wp-content/uploads/2026/10/header_fortibleed_2.png)

1. [Home](https://www.infostealers.com/)/
2. [Blog](https://www.infostealers.com/learn-info-stealers/)/
3. FortiBleed 2.0: 975 New Domains & 40,573 Exposed Secrets – Claim Your Ethical Disclosure

Blog Post

# FortiBleed 2.0: 975 New Domains & 40,573 Exposed Secrets – Claim Your Ethical Disclosure

![](https://secure.gravatar.com/avatar/a917127d480b5b9fb3257b42447749cf299758c29d41b3c7cb28c470ecc8cbff?s=28&d=mm&r=g) InfoStealers

Oct 27, 2026

15 min read

![](https://www.infostealers.com/wp-content/uploads/2026/10/header_fortibleed_2.png)

FortiBleed 2.0: 975 New Domains & 40,573 Exposed Secrets – Claim Your Ethical Disclosure | Hudson Rock

Hudson Rock Threat Intelligence
FortiBleed 2.0
Configuration & Credential Exposure

# FortiBleed 2.0: 975 New Domains & 40,573 Exposed Secrets – Claim Your Ethical Disclosure

Newly obtained FortiGate configuration reports reveal **40,573 records containing cleartext secrets**, including **37,076 local-user records** and **1,576 Active Directory LDAP bind records**. The analysis also identifies **975 domain labels absent from FortiBleed 1.0**. The configuration material dates to around February 2026, earlier than the likely May/June material examined in the first investigation.

Earlier Evidence, Obtained Later

**FortiBleed 2.0 names the follow-up investigation.** Researchers obtained the files only recently. In the CSV, 1,672 of the 1,703 source files have report timestamps on **February 20, 2026**; 31 are undated. These are report dates, not independently established dates of first compromise or configuration extraction. The comparison below measures exposure recorded in the datasets, not organizations’ responses to the later FortiBleed 1.0 disclosure.

**Check your organization:** Search the FortiBleed exposure records through Hudson Rock’s free portal.

[Check Your Domain →](https://www.hudsonrock.com/fortinet)

Inside the Investigation

* [01What the Files Reveal](#section-1)
* [02From Configuration Theft to Internal Access](#section-2)
* [03How the Datasets Compare](#section-3)
* [04What the Overlapping Hosts Reveal](#section-4)
* [05Behind the Registration Email](#section-5)
* [06The Network Details in the Backup](#section-6)
* [07What Affected Organizations Should Check](#section-7)

## 1. What the Configuration Files Reveal

A firewall backup can expose remote-access accounts, the secrets connecting an appliance to Active Directory, and the addresses of internal systems. Across **1,703 configuration-report files**, FortiBleed 2.0 shows how much information can become available through administrative access to a network’s perimeter.

The combined export contains **101,419 credential and account records** associated with **1,689 nonempty host identifiers**. Of those records, **40,573 contain cleartext secrets**. Local users account for most of that exposure, but the dataset also includes directory bind accounts, administrator logins, SMTP credentials, and HA cluster secrets. Each category connects the firewall to another part of the organization’s infrastructure.

101,419

Credential & Account Records

From 1,703 source files associated with 1,689 host identifiers.

40,573

Cleartext Secret Records

Across local users, administrator logins, LDAP, SMTP, and HA settings.

1,576

Cleartext LDAP Bind Records

Service-account secrets recovered within 2,163 LDAP records.

54.7%

Hosts Absent from 1.0

924 of 1,689 host identifiers add coverage beyond the compared perimeter list.

[Hudson Rock’s first FortiBleed investigation](https://www.hudsonrock.com/blog/fortibleed-75000-fortinet-firewalls-compromised-global-enterprises-exposed-claim-your-ethical-disclosure) described a much broader perimeter credential list. Rechecking the FortiBleed 1.0 text dataset yields **73,932 login rows across 69,055 host identifiers**. The smaller configuration corpus adds depth: the account tables and directory connections behind those logins, plus records for hosts absent from that larger list.

Research Credit: NyxLab

Hudson Rock credits **NyxLab** for its foundational technical research into the threat actor known as **k0t** and the associated extraction tooling. For background on the actor’s operational infrastructure, read NyxLab’s investigation, [*“Stray Cat, Open Doors: How k0t Wanders Through the Network Edge”*](https://www.nyxlab.com/blog/stray-cat-open-doors-how-k0t-wanders-through-the-network-edge/)

Campaign context and the vulnerability timeline

FortiCloud SSO abuse is part of the wider campaign context. **CVE-2026-24858** (CVSS 9.4) affects FortiOS, FortiProxy, and FortiSwitchManager. [Fortinet records issuing its advisory on January 27, 2026](https://www.fortinet.com/blog/psirt-blogs/analysis-of-sso-abuse-on-fortios), before the February report timestamps. Its [June assessment](https://www.fortinet.com/blog/psirt-blogs/analysis-of-reported-credential-compromise-of-fortigate-devices) also discusses reused credentials and brute-force activity. These records do not establish one initial-access mechanism for every host.

Related [Group-IB and NyxLab research](https://www.group-ib.com/blog/stray-cat-network-edge/) describes victim overlap with Qilin and The Gentlemen. A direct affiliation or supplier relationship remains unconfirmed.

## 2. From Configuration Theft to Internal Access

The associated tooling connects three stages: extracting a configuration, recovering secrets, and attempting access to internal systems. The reports expose the accounts and settings that make this progression possible.

1. **Extract the configuration and recover secrets.** The parsing workflow described around forti\_parse.py collects administrator entries, local users, LDAP connections, HA settings, and email-server credentials. The CSV records **37,076 cleartext local-user entries** and **1,576 cleartext LDAP bind entries**. It also retains hashes and undecrypted values, so the export distinguishes recovered secrets from values whose cleartext is not present in the export.
2. **Attempt VPN access.** The reported vpn\_checker.py / openconnect workflow uses eligible VPN credentials to attempt connections. The account’s status, VPN policy, MFA requirements, and reachability determine whether a session is possible. Firewall-management privileges and VPN-user permissions are separate.
3. **Identify directory servers and assess access.** The LDAP server and distinguished-name fields identify directory infrastructure and its bind identities. Research into the associated toolchain describes nxc / NetExec activity against internal systems. An overprivileged bind identity can expose a much wider environment; ordinary LDAP query rights alone do not confer domain-administrator privileges, directory replication rights, or access to NTDS.dit.

Why a Backup Can Expose Working Secrets

The reports distinguish administrator hashes such as SHA-256 (SH2) and...