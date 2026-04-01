---
title: TeamPCP Supply Chain Campaign: Update 004 - Databricks Investigating Alleged Compromise, TeamPCP Runs Dual Ransomware Operations, and AstraZeneca Data Released, (Mon, Mar 30th)
url: https://isc.sans.edu/diary/rss/32846
source: SANS Internet Storm Center, InfoCON: green
date: 2026-03-31
fetch_date: 2026-04-01T04:47:45.501031
---

# TeamPCP Supply Chain Campaign: Update 004 - Databricks Investigating Alleged Compromise, TeamPCP Runs Dual Ransomware Operations, and AstraZeneca Data Released, (Mon, Mar 30th)

# [Internet Storm Center](/)

[Sign In](/login.html)
[Sign Up](/register.html)

Handler on Duty: [Xavier Mertens](/handler_list.html#xavier-mertens "Xavier Mertens")

Threat Level: [green](/infocon.html)

* [previous](/diary/32842)
* [next](/diary/32850)

Click [HERE](https://www.sans.org/profiles/kenneth-g-hartman) to learn more about classes Kenneth is teaching for SANS

# [TeamPCP Supply Chain Campaign: Update 004 - Databricks Investigating Alleged Compromise, TeamPCP Runs Dual Ransomware Operations, and AstraZeneca Data Released](/forums/diary/TeamPCP%2BSupply%2BChain%2BCampaign%2BUpdate%2B004%2BDatabricks%2BInvestigating%2BAlleged%2BCompromise%2BTeamPCP%2BRuns%2BDual%2BRansomware%2BOperations%2Band%2BAstraZeneca%2BData%2BReleased/32846/)

**Published**: 2026-03-30. **Last Updated**: 2026-03-31 00:52:44 UTC
**by** [Kenneth Hartman](/handler_list.html#kenneth-hartman) (Version: 1)

[0 comment(s)](/diary/TeamPCP%2BSupply%2BChain%2BCampaign%2BUpdate%2B004%2BDatabricks%2BInvestigating%2BAlleged%2BCompromise%2BTeamPCP%2BRuns%2BDual%2BRansomware%2BOperations%2Band%2BAstraZeneca%2BData%2BReleased/32846/#comments)

This is the fourth update to the TeamPCP supply chain campaign threat intelligence report, ["When the Security Scanner Became the Weapon"](https://www.sans.org/white-papers/when-security-scanner-became-weapon) (v3.0, March 25, 2026). Update 003 covered developments through March 28, including the first 48-hour pause in new compromises and the campaign's shift to monetization. This update consolidates intelligence from March 28-30, 2026 -- two days since our last update.

## HIGH: Databricks Investigating Alleged Compromise Linked to TeamPCP Credential Harvest

[CybersecurityNews](https://cybersecuritynews.com/databricks-teampcp-supply-chain/amp/) reports that Databricks, the cloud data analytics platform, is investigating an alleged security compromise linked to the TeamPCP credential harvest. International Cyber Digest [stated on X](https://x.com/IntCyberDigest/status/2038552600375648701) that they "notified them last week" and Databricks "scaled up to investigate." A separate analyst corroborated that screenshots showing AWS artifacts, CloudFormation dumps, and STS tokens "match TeamPCP's exact playbook."

Databricks has not issued an official statement. If confirmed, this would be the first major cloud platform identified as a downstream victim of TeamPCP's credential trove -- distinct from the security tool vendors (Aqua, Checkmarx, BerriAI, Telnyx) directly compromised in the supply chain phase. The distinction matters: tool vendor compromises expanded TeamPCP's credential pool, while a Databricks compromise would represent the monetization of that pool against an enterprise target processing sensitive data across AWS, GCP, and Azure.

***U*pdate (2026-03-30):** Databricks' Head of Global Communications and their external PR agency FGS Global have confirmed the authenticity of the new @DatabricksSec X account.  In their https://x.com/DatabricksSec/status/2038649955401794042, Databricks says they "thoroughly investigated this information in our internal systems and found nothing" and have "asked for more information beyond this screenshot." They state they will "transparently continue to share any new updates on all security matters."

**Recommended action:** Organizations using Databricks should monitor for an official statement. If your CI/CD pipelines were exposed to any TeamPCP-compromised component AND those pipelines had access to Databricks credentials, treat those credentials as potentially compromised regardless of whether Databricks confirms the breach.

## HIGH: TeamPCP Operates Dual Ransomware Tracks - CipherForce Is Their Own Operation

Update 002 documented TeamPCP's partnership with the Vect ransomware-as-a-service operation and BreachForums mass affiliate key distribution. New intelligence reveals that Vect is not TeamPCP's only ransomware channel.

According to [Flare](https://flare.io/learn/resources/blog/teampcp-cloud-native-ransomware) and corroborated by [Rami McCarthy's IOC tracker](https://ramimac.me/teampcp/), TeamPCP operates under five confirmed aliases: **PCPcat, ShellForce, DeadCatx3, CipherForce, and Persy\_PCP**. TeamPCP's own Telegram channel states: "you may already know us as TeamPCP or Shellforce... CipherForce is a newer project we are starting to find affiliates."

**CipherForce is TeamPCP's own ransomware operation**, separate from the Vect partnership. This means TeamPCP is running two parallel ransomware tracks simultaneously: their proprietary CipherForce program for direct operations, and the mass Vect affiliate program via BreachForums for distributed operations. The [SANS ISC Stormcast for March 30](https://isc.sans.edu/podcastdetail/9870) also notes "more and more links between the TeamPCP crew and various ransomware actors" -- plural -- consistent with this dual-track model.

Analysts assess this dual-track approach allows TeamPCP to maintain direct control over high-value targets (via CipherForce) while simultaneously flooding the ecosystem with mass affiliate operations (via Vect). The 300 GB stolen credential trove can feed both tracks simultaneously.

**Recommended action:** Detection teams monitoring for Vect ransomware indicators should also add CipherForce to their watchlist. The strongest attribution link across all TeamPCP operations is a shared RSA-4096 public key embedded in payloads -- search for this key in forensic artifacts from any suspected TeamPCP exposure.

## HIGH: LAPSUS$ Releases AstraZeneca Data Free After Failed Sale Attempt

The LAPSUS$/AstraZeneca breach claim documented in Updates 002-003 has escalated. [Cybernews](https://cybernews.com/security/astrazeneca-hackers-claim-source-code-breach/) and [Cybersecurity Insiders](https://www.cybersecurity-insiders.com/lapsus-hackers-disclose-more-about-astrazeneca-data-breach/) report two developments:

1. **LAPSUS$ released the claimed 3 GB archive for free** after failing to find buyers via Session encrypted messaging. This shifts the incident from an extortion attempt to a full data exposure event.
2. **Cybernews research team has partially verified the dump's contents** -- GitHub user information for internal AstraZeneca software developers, employee data spanning clinical research subsidiaries, and internal source code tree structures were assessed as consistent with legitimate AstraZeneca infrastructure.

AstraZeneca has still not issued any public statement confirming or denying the breach at approximately 96 hours since the initial claim. Analysts assess that AstraZeneca's continued silence, combined with GDPR obligations if EU employee data is in the dump, creates increasing regulatory exposure with each passing day.

**Recommended action:** Organizations should treat this as a probable confirmed breach for defensive planning purposes. If your organization shares integrations, data, or credentials with AstraZeneca, assess whether the exposed repository structures and configurations could affect your security posture. Given AstraZeneca's clinical research operations, the dump may contain protected health information (PHI) subject to HIPAA in the US and GDPR in the EU. Organizations with data-sharing agreements with AstraZeneca should evaluate whether their data may be in the exposed archive and prepare breach notification workflows accordingly.

## MEDIUM: ownCloud Discloses Build Infrastructure Impact From CVE-2026-33634

[ownCloud](https://central.owncloud.org/t/security-notice-impact-of-cve-2026-33634-on-owncloud-build-infrastructure/65655) published a security notice confirming their build infrastructure -- the systems producing container images and client binaries -- was affected by CVE-2026-33634 (the Trivy compromise). ownCloud confirms: no customer data compromised, no source code altered, impact limited to build systems only.

This is one of the first named downstream organizations to publicly disclose that th...