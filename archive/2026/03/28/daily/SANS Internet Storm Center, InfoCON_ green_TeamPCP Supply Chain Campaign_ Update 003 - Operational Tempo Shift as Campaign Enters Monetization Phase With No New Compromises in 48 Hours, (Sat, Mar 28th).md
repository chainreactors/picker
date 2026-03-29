---
title: TeamPCP Supply Chain Campaign: Update 003 - Operational Tempo Shift as Campaign Enters Monetization Phase With No New Compromises in 48 Hours, (Sat, Mar 28th)
url: https://isc.sans.edu/diary/rss/32842
source: SANS Internet Storm Center, InfoCON: green
date: 2026-03-28
fetch_date: 2026-03-29T04:42:38.685716
---

# TeamPCP Supply Chain Campaign: Update 003 - Operational Tempo Shift as Campaign Enters Monetization Phase With No New Compromises in 48 Hours, (Sat, Mar 28th)

# [Internet Storm Center](/)

[Sign In](/login.html)
[Sign Up](/register.html)

Handler on Duty: [Brad Duncan](/handler_list.html#brad-duncan "Brad Duncan")

Threat Level: [green](/infocon.html)

* [previous](/diary/32838)

Click [HERE](https://www.sans.org/profiles/kenneth-g-hartman) to learn more about classes Kenneth is teaching for SANS

# [TeamPCP Supply Chain Campaign: Update 003 - Operational Tempo Shift as Campaign Enters Monetization Phase With No New Compromises in 48 Hours](/forums/diary/TeamPCP%2BSupply%2BChain%2BCampaign%2BUpdate%2B003%2BOperational%2BTempo%2BShift%2Bas%2BCampaign%2BEnters%2BMonetization%2BPhase%2BWith%2BNo%2BNew%2BCompromises%2Bin%2B48%2BHours/32842/)

**Published**: 2026-03-28. **Last Updated**: 2026-03-28 15:09:12 UTC
**by** [Kenneth Hartman](/handler_list.html#kenneth-hartman) (Version: 1)

[0 comment(s)](/diary/TeamPCP%2BSupply%2BChain%2BCampaign%2BUpdate%2B003%2BOperational%2BTempo%2BShift%2Bas%2BCampaign%2BEnters%2BMonetization%2BPhase%2BWith%2BNo%2BNew%2BCompromises%2Bin%2B48%2BHours/32842/#comments)

This is the third update to the TeamPCP supply chain campaign threat intelligence report, ["When the Security Scanner Became the Weapon"](https://www.sans.org/white-papers/when-security-scanner-became-weapon) (v3.0, March 25, 2026). Update 002 covered developments through March 27, including the Telnyx PyPI compromise and Vect ransomware partnership. This update covers developments from March 27-28, 2026.

## HIGH: First 48-Hour Window Without a New Supply Chain Compromise

The most operationally significant development in the last 24 hours is what did not happen: no new package compromises have been confirmed since the Telnyx disclosure on March 27. This is the first 48-hour window without a new ecosystem compromise since TeamPCP began active operations on March 19.

The prior operational cadence was aggressive -- a new target every 1-3 days (Trivy March 19, CanisterWorm March 20-22, Checkmarx March 23, LiteLLM March 24, Telnyx March 27). The current pause, combined with the Vect ransomware affiliate announcement, suggests TeamPCP has shifted primary operational focus from supply chain expansion to monetization of existing credential harvests.

Analysts assess this pause should not be interpreted as the end of supply chain operations. TeamPCP explicitly stated they intend to be "around for a long time," and stolen credentials from the estimated 300 GB trove could enable future package compromises at any time. The absence of new compromises may also reflect improved vigilance by package registries -- PyPI has quarantined two TeamPCP campaigns in rapid succession, which may be raising the attacker's cost of operations on that platform.

**Recommended action:** Maintain heightened monitoring posture. Use this operational window to complete credential rotations and IOC sweeps if not already done. The CISA KEV remediation deadline for CVE-2026-33634 is now 11 days away (April 8, 2026).

## HIGH: Palo Alto Networks Publishes Behavioral Detection Rules for CI/CD Pipeline Attacks

[Palo Alto Networks](https://www.paloaltonetworks.com/blog/cloud-security/trivy-supply-chain-attack/) has published detection rules specifically designed to identify TeamPCP-style CI/CD pipeline attacks at the behavioral level rather than relying solely on IOC matching. This is significant because TeamPCP has demonstrated the ability to rotate infrastructure across each new compromise wave -- each phase used different C2 domains, different exfiltration endpoints, and different packaging techniques (raw scripts, npm worm, .pth exploitation, WAV steganography).

Behavioral detection approaches focus on anomalous CI/CD runner behavior: unexpected credential directory enumeration, bulk secret reads from `/proc/<pid>/mem`, large encrypted archive creation, and outbound data transfers to newly registered domains during workflow execution. These patterns have been consistent across all five TeamPCP compromise phases even as specific IOCs changed.

**Recommended action:** Organizations with Palo Alto Networks security products should review and deploy the published detection rules. All organizations should evaluate whether their CI/CD monitoring can detect the behavioral patterns described -- process memory reads of Runner.Worker, creation of `tpcp.tar.gz` or similarly named archives, and outbound HTTPS to domains registered within the past 30 days.

## MEDIUM: Cloud Security Alliance Publishes Kubernetes Wiper Lab Analysis

The [Cloud Security Alliance](https://labs.cloudsecurityalliance.org/research/csa-research-note-teampcp-supply-chain-ci-cd-20260324-csa-st/) has published a detailed lab analysis of TeamPCP's Kubernetes wiper component -- the Iran-targeted DaemonSet that deletes all host filesystem contents when Farsi language settings are detected. The analysis reconstructs the wiper's deployment mechanism and provides detection queries for Kubernetes audit logs.

This component was mentioned in the parent report but has received less attention than the credential-stealing payloads. The CSA analysis provides the first detailed defensive playbook specifically for the wiper TTP, including Kubernetes admission controller policies that would block the privileged DaemonSet deployment pattern.

**Recommended action:** Kubernetes operators should review the CSA analysis and implement admission controller policies that prevent privileged DaemonSets from mounting hostPath `/` with write access. This is good hygiene regardless of TeamPCP exposure.

## MEDIUM: GitGuardian Quantitative Analysis Maps Credential Exposure Blast Radius

[GitGuardian](https://blog.gitguardian.com/team-pcp-snowball-analysis/) has published a quantitative "snowball effect" analysis tracing how a single compromised token cascaded across ecosystems. The analysis maps the amplification factor at each stage: one stolen PAT led to 76+ poisoned GitHub Action tags, which harvested credentials from hundreds of CI/CD pipelines, which enabled compromise of packages with a combined 100+ million monthly downloads.

The analysis introduces a metric they call "credential fan-out" -- the ratio of credentials stolen to credentials used for initial access. For TeamPCP, this ratio is estimated at greater than 10,000:1, meaning each compromised credential potentially exposed thousands of downstream secrets. This quantitative framing is useful for communicating risk to executive stakeholders who need to understand why a single supply chain compromise requires organization-wide credential rotation.

## INFO: Deep Analysis of GitHub Repository-Based Exfiltration Technique Published

I have published a [detailed analysis](https://kennethghartman.com/blog/github-as-exfiltration-channel-teampcp/) of TeamPCP's novel GitHub repository-based data exfiltration technique. The post examines how the campaign used the GitHub Releases API as a fallback exfiltration channel -- programmatically creating repositories on the victim's own account and uploading stolen data as release assets. This technique is significant because corporate firewalls and DLP solutions that whitelist `api.github.com` traffic cannot distinguish this exfiltration from legitimate GitHub API usage. The analysis includes organizational controls, alternative attack permutations, and threat hunting queries.

## INFO: AstraZeneca Breach Claim Remains Unconfirmed at 48 Hours

LAPSUS$'s claimed 3GB AstraZeneca breach (reported in Update 002) remains unconfirmed. [Security Affairs](https://securityaffairs.com/189936/data-breach/cybercrime-group-lapsus-claims-the-hack-of-pharma-giant-astrazeneca.html) characterized the claim as "potentially one of the most serious healthcare cyber incidents this year" if verified. AstraZeneca has not issued a public statement confirming or denying the breach as of March 28, 2026. No additional named victim claims have been disclosed in the past 24 hours, though the Vect affiliate program distribution may shift the extor...