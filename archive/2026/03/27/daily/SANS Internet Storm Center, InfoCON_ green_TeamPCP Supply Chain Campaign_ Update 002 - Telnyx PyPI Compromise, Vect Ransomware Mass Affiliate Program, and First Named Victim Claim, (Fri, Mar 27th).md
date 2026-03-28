---
title: TeamPCP Supply Chain Campaign: Update 002 - Telnyx PyPI Compromise, Vect Ransomware Mass Affiliate Program, and First Named Victim Claim, (Fri, Mar 27th)
url: https://isc.sans.edu/diary/rss/32838
source: SANS Internet Storm Center, InfoCON: green
date: 2026-03-27
fetch_date: 2026-03-28T04:20:09.394156
---

# TeamPCP Supply Chain Campaign: Update 002 - Telnyx PyPI Compromise, Vect Ransomware Mass Affiliate Program, and First Named Victim Claim, (Fri, Mar 27th)

# [Internet Storm Center](/)

[Sign In](/login.html)
[Sign Up](/register.html)

Handler on Duty: [Brad Duncan](/handler_list.html#brad-duncan "Brad Duncan")

Threat Level: [green](/infocon.html)

* [previous](/diary/32834)

Click [HERE](https://www.sans.org/profiles/kenneth-g-hartman) to learn more about classes Kenneth is teaching for SANS

# [TeamPCP Supply Chain Campaign: Update 002 - Telnyx PyPI Compromise, Vect Ransomware Mass Affiliate Program, and First Named Victim Claim](/forums/diary/TeamPCP%2BSupply%2BChain%2BCampaign%2BUpdate%2B002%2BTelnyx%2BPyPI%2BCompromise%2BVect%2BRansomware%2BMass%2BAffiliate%2BProgram%2Band%2BFirst%2BNamed%2BVictim%2BClaim/32838/)

**Published**: 2026-03-27. **Last Updated**: 2026-03-27 14:34:44 UTC
**by** [Kenneth Hartman](/handler_list.html#kenneth-hartman) (Version: 1)

[0 comment(s)](/diary/TeamPCP%2BSupply%2BChain%2BCampaign%2BUpdate%2B002%2BTelnyx%2BPyPI%2BCompromise%2BVect%2BRansomware%2BMass%2BAffiliate%2BProgram%2Band%2BFirst%2BNamed%2BVictim%2BClaim/32838/#comments)

This is the second update to the TeamPCP supply chain campaign threat intelligence report, ["When the Security Scanner Became the Weapon"](https://www.sans.org/white-papers/when-security-scanner-became-weapon) (v3.0, March 25, 2026). Update 001 covered developments through March 26. This update covers developments from March 26-27, 2026.

## CRITICAL: Telnyx Python SDK Compromised on PyPI -- New WAV Steganography TTP

TeamPCP compromised the [telnyx](https://pypi.org/project/telnyx/) Python SDK (670,000+ monthly downloads) on PyPI, publishing malicious versions 4.87.1 and 4.87.2 at approximately 03:51 UTC on March 27, 2026. No corresponding GitHub releases or tags exist for these versions -- the attacker used stolen PyPI credentials rather than a repository compromise.

The most significant technical finding is a new TTP: **WAV audio file steganography**. Payloads are embedded inside `.wav` files, which blend naturally with Telnyx's purpose as a voice and telecom API provider. Platform-specific payloads are delivered:

* **Windows:** A persistent binary dropped to the Startup folder as `msbuild.exe`
* **Linux/macOS:** A credential harvester following the same pattern as the LiteLLM compromise

Forensic analysis by [Aikido Security](https://www.aikido.dev/blog/telnyx-pypi-compromised-teampcp-canisterworm), [JFrog](https://research.jfrog.com/post/team-pcp-strikes-again-telnyx-popular-library-hit/), and [SafeDep](https://safedep.io/malicious-telnyx-pypi-compromise/) confirms the same RSA-4096 public key and `tpcp.tar.gz` exfiltration pattern seen in the LiteLLM compromise. Both malicious versions have been quarantined by PyPI.

**Recommended action:** Check your Python environments and CI/CD pipelines for telnyx versions 4.87.1 or 4.87.2. If found, treat all credentials accessible to that environment as compromised and rotate immediately. The last known-safe version is 4.87.0. Also search for `.wav` files in unexpected locations, `msbuild.exe` in Windows Startup folders, and outbound connections to known TeamPCP exfiltration domains.

This confirms the "expansion to additional PyPI packages" watch item from Update 001. TeamPCP's PyPI campaign is not limited to LiteLLM -- they are actively working through stolen credentials to compromise additional high-value packages.

## CRITICAL: TeamPCP Partners with Vect Ransomware and BreachForums for Mass Affiliate Program

TeamPCP has formally partnered with the [Vect ransomware-as-a-service](https://www.halcyon.ai/ransomware-alerts/emerging-ransomware-group-vect) operation and BreachForums. Per [Cybernews](https://cybernews.com/security/litellm-hack-spawning-massive-cybercrime-alliance/) and [Infosecurity Magazine](https://www.infosecurity-magazine.com/news/researchers-warn-new-vect-raas/), the announcement states that all approximately 300,000 registered BreachForums users will receive personal Vect affiliate keys.

The operational model: TeamPCP provides initial access via compromised supply chain packages and stolen credentials, Vect provides encryption and extortion tooling, and BreachForums provides the operator base.

Analysts assess this represents a fundamental shift from supply chain credential theft to industrialized ransomware deployment. If even a small fraction of 300,000 users activate, this could become one of the largest coordinated ransomware affiliate mobilizations observed. The convergence of supply chain compromise, ransomware-as-a-service, and dark web forum mobilization at this scale is, to the best of our knowledge, unprecedented.

**Recommended action:** Organizations that were exposed to any phase of the TeamPCP campaign (Trivy, Checkmarx, LiteLLM, Telnyx) should assume their stolen credentials may now be distributed to a large affiliate network. Credential rotation is no longer optional -- it is urgent. Monitor for Vect ransomware indicators.

## HIGH: LAPSUS$ Claims 3GB AstraZeneca Breach Using TeamPCP Credentials

LAPSUS$ is publicly claiming a 3GB breach of AstraZeneca, as reported by [SecurityWeek](https://www.securityweek.com/extortion-group-claims-it-hacked-astrazeneca/) and [CSO Online](https://www.csoonline.com/article/4149938/trivy-supply-chain-breach-compromises-over-1000-saas-environments-lapsus-joins-the-extortion-wave.html). The claimed data includes internal code repositories, cloud infrastructure configurations (AWS, Azure, Terraform), Spring Boot configs, GitHub Enterprise user information, and employee data. LAPSUS$ is selling access via Session encrypted messaging.

This is the **first named victim claim** from the TeamPCP/LAPSUS$ partnership, confirming the "named victim breach disclosures" watch item from Update 001. AstraZeneca has not confirmed or denied the breach as of publication time.

**Recommended action:** Organizations should not wait for public victim disclosures to take action. If you were exposed to any TeamPCP-compromised component, assume credential theft occurred and rotate proactively. The extortion timeline is accelerating.

## HIGH: LiteLLM CEO's Personal GitHub Account Was the Compromise Vector

[ReversingLabs](https://www.reversinglabs.com/blog/teampcp-supply-chain-attack-spreads) has published new intelligence identifying the specific mechanism behind the LiteLLM PyPI compromise: TeamPCP compromised **Krish Dholakia's personal GitHub account** (LiteLLM co-founder and CEO) on March 23-24. This was not a generic CI/CD token sweep -- the attacker specifically identified and targeted a named executive's account from the stolen credential trove harvested during the Trivy/Checkmarx phase.

This detail refines the attack chain narrative. TeamPCP appears to be triaging stolen credentials for maximum impact, targeting package maintainers with PyPI publishing privileges rather than indiscriminately using every credential they harvested.

## MEDIUM: CISA KEV Remediation Deadline Correction -- April 8, Not April 3

Update 001 reported the CISA KEV remediation deadline for CVE-2026-33634 as April 3, 2026. The [official CISA KEV catalog entry](https://www.cisa.gov/known-exploited-vulnerabilities-catalog) shows the actual deadline is **April 8, 2026**. This update corrects the previously reported date.

Additionally, [Help Net Security](https://www.helpnetsecurity.com/2026/03/27/cve-2026-33017-cve-2026-33634-exploited/) reports that CISA simultaneously added **CVE-2026-33017** (Langflow unauthenticated RCE, affecting versions prior to 1.8.2) alongside the Trivy CVE in the same KEV update. The pairing of two AI/ML infrastructure tool vulnerabilities in a single KEV addition signals that CISA is treating AI toolchain supply chain security as a systemic risk category.

Federal agencies now face remediation deadlines of April 8 for CVE-2026-33634 (Trivy) and April 9 for CVE-2026-33017 (Langflow).

## INFO: LiteLLM's Compliance Certifications Performed by Embattled Auditor

[TechCrunch](https://techcrunch.com/2026/03/26/delve-did-the-security-compliance-o...