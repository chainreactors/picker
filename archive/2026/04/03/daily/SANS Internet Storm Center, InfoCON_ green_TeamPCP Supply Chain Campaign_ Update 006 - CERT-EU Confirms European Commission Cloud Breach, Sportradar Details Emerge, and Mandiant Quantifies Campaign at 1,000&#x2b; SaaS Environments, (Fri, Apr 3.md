---
title: TeamPCP Supply Chain Campaign: Update 006 - CERT-EU Confirms European Commission Cloud Breach, Sportradar Details Emerge, and Mandiant Quantifies Campaign at 1,000&#x2b; SaaS Environments, (Fri, Apr 3rd)
url: https://isc.sans.edu/diary/rss/32864
source: SANS Internet Storm Center, InfoCON: green
date: 2026-04-03
fetch_date: 2026-04-04T04:17:48.419521
---

# TeamPCP Supply Chain Campaign: Update 006 - CERT-EU Confirms European Commission Cloud Breach, Sportradar Details Emerge, and Mandiant Quantifies Campaign at 1,000&#x2b; SaaS Environments, (Fri, Apr 3rd)

# [Internet Storm Center](/)

[Sign In](/login.html)
[Sign Up](/register.html)

Handler on Duty: [Johannes Ullrich](/handler_list.html#johannes-ullrich "Johannes Ullrich")

Threat Level: [green](/infocon.html)

* [previous](/diary/32860)

Click [HERE](https://www.sans.org/profiles/kenneth-g-hartman) to learn more about classes Kenneth is teaching for SANS

# [TeamPCP Supply Chain Campaign: Update 006 - CERT-EU Confirms European Commission Cloud Breach, Sportradar Details Emerge, and Mandiant Quantifies Campaign at 1,000+ SaaS Environments](/forums/diary/TeamPCP%2BSupply%2BChain%2BCampaign%2BUpdate%2B006%2BCERTEU%2BConfirms%2BEuropean%2BCommission%2BCloud%2BBreach%2BSportradar%2BDetails%2BEmerge%2Band%2BMandiant%2BQuantifies%2BCampaign%2Bat%2B1000%2BSaaS%2BEnvironments/32864/)

**Published**: 2026-04-03. **Last Updated**: 2026-04-03 13:18:01 UTC
**by** [Kenneth Hartman](/handler_list.html#kenneth-hartman) (Version: 1)

[0 comment(s)](/diary/TeamPCP%2BSupply%2BChain%2BCampaign%2BUpdate%2B006%2BCERTEU%2BConfirms%2BEuropean%2BCommission%2BCloud%2BBreach%2BSportradar%2BDetails%2BEmerge%2Band%2BMandiant%2BQuantifies%2BCampaign%2Bat%2B1000%2BSaaS%2BEnvironments/32864/#comments)

This is the sixth update to the TeamPCP supply chain campaign threat intelligence report, ["When the Security Scanner Became the Weapon"](https://www.sans.org/white-papers/when-security-scanner-became-weapon) (v3.0, March 25, 2026). [Update 005](https://isc.sans.edu/diary/32856) covered developments through April 1, including the first confirmed victim disclosure (Mercor AI), Wiz's post-compromise cloud enumeration findings, DPRK attribution of the axios compromise, and LiteLLM's release resumption after Mandiant's forensic audit. This update covers intelligence from April 1 through April 3, 2026.

## CRITICAL: CERT-EU Confirms European Commission Cloud Breach via Trivy Supply Chain Compromise

[CERT-EU disclosed](https://cert.europa.eu/blog/european-commission-cloud-breach-trivy-supply-chain) on April 2-3, 2026 that the European Commission's Europa web hosting platform on AWS was breached through the Trivy supply chain compromise (CVE-2026-33634). This is the highest-profile governmental victim disclosure to date.

Key details from the CERT-EU advisory:

* **Initial access:** AWS API keys stolen via the compromised Trivy scanner on March 19
* **Detection:** European Commission Security Operations Center fired alerts on March 24 (5 days after initial intrusion)
* **CERT-EU notified:** March 25; access revoked same day
* **Data exfiltrated:** 340 GB uncompressed (91.7 GB compressed archive) from the compromised AWS account
* **Email exposure:** Approximately 52,000 email-related files (2.22 GB) of outbound communications
* **Scope:** 71 clients affected: 42 internal European Commission departments plus 29 other EU entities, meaning at least 30 Union entities were potentially impacted
* **Data publication:** ShinyHunters published the stolen data on their dark web leak site on March 28
* **Lateral movement:** CERT-EU confirmed no lateral movement to other Commission AWS accounts was detected
* **[Europa.eu](http://Europa.eu) websites** remained unaffected throughout

Analysts assess this disclosure is significant on multiple dimensions. First, it confirms that TeamPCP-harvested credentials reached a major governmental institution, not just private-sector targets. Second, the involvement of ShinyHunters in the data publication raises questions about the credential distribution chain, as ShinyHunters is operationally distinct from TeamPCP's known LAPSUS$ and Vect partnerships. Third, the five-day dwell time between initial access (March 19) and detection (March 24) is consistent with the 24-hour operational tempo that [Wiz documented](https://www.wiz.io/blog/tracking-teampcp-investigating-post-compromise-attacks-seen-in-the-wild) for TeamPCP's post-compromise cloud enumeration.

**Recommended action:** EU institutions and organizations hosted on Europa infrastructure should review CERT-EU's advisory for specific exposure indicators. Organizations with AWS credentials that may have been exposed through the Trivy compromise should treat the EC breach as confirmation that stolen credentials are being actively used against high-value targets. The CERT-EU disclosure timeline (initial access March 19, detection March 24, notification March 25, public disclosure April 2) demonstrates that even well-resourced organizations required five days to detect the intrusion.

## HIGH: Sportradar AG Breach Details Confirmed: TeamPCP and Vect Joint Operation

VECERT reported on April 2, 2026 that the Sportradar AG breach (first claimed as a CipherForce victim in [Update 004](https://isc.sans.edu/diary/32846)) has been confirmed as a "systemic compromise" jointly operated by TeamPCP and Vect ransomware. Sportradar is a $4.98 billion Swiss sports technology company.

Confirmed breach details:

* **Entry vector:** Supply chain via compromised Trivy (CVE-2026-33634)
* **Personal data:** Approximately 26,000 users' personal information exposed
* **Athlete records:** 23,169 records including names, dates of birth, gender, and nationality
* **Client exposure:** Client table listing 161 organizations including ESPN, Nike, NBA Asia, and IMG Arena
* **Credential exposure:** 8 production RDS database passwords, 328 platform API key/secret pairs, Kafka SASL credentials, and New Relic monitoring tokens
* **CipherForce ransomware:** Listed on the CipherForce shame site with the original 14-15 day publication deadline (approaching approximately April 10-11)

This is the first confirmed case of TeamPCP and Vect operating jointly against a single target, validating the dual-track ransomware model documented in earlier updates. The exposure of 161 client organizations including major sports leagues and media companies creates a cascading notification and risk assessment obligation for Sportradar.

**Recommended action:** Organizations with Sportradar business relationships should proactively assess whether their data appears in the exposed client table. The 328 exposed API key/secret pairs create a secondary supply chain risk for Sportradar's integration partners.

## HIGH: Mandiant Quantifies Campaign Scale: Over 1,000 SaaS Environments, Estimated 500,000 Machines

Multiple vendor statements published April 1-2 have provided the first authoritative quantification of the campaign's total blast radius:

* **Mandiant CTO Charles Carmakal** stated that Google-owned Mandiant knew of ["over 1,000 impacted SaaS environments"](https://www.theregister.com/2026/04/02/mercor_supply_chain_attack/) actively dealing with cascading effects from the TeamPCP supply chain compromises.
* **Google Cloud researchers** warned that "hundreds of thousands of stolen secrets could potentially be circulating" from the credential trove.
* **[The Register](https://www.theregister.com/2026/04/02/mercor_supply_chain_attack/)** cited estimates suggesting attackers exfiltrated data and secrets from approximately **500,000 machines** total across all victims.
* **[Palo Alto Networks Unit 42](https://unit42.paloaltonetworks.com/teampcp-supply-chain-attacks/)** identified affected organizations across the US, Europe, Middle East, South Asia, and Australia, spanning financial services, technology, retail, legal, insurance, and education sectors.

These numbers move the campaign's assessed scale from qualitative ("thousands of downstream environments," per the FBI alert) to quantitative. The 1,000+ SaaS environments figure is particularly significant because it implies credential exploitation is ongoing across a far larger surface than the handful of publicly named victims suggests.

**Recommended action:** Organizations that have not yet completed credential rotation should treat the Mandiant quantification as definitive evidence that delayed rotation increases exposure to an actively exploited credential pool of industrial scale.

## MEDIUM: Elastic Secur...