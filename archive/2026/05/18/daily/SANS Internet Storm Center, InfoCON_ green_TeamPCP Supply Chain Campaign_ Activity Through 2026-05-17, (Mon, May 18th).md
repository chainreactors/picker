---
title: TeamPCP Supply Chain Campaign: Activity Through 2026-05-17, (Mon, May 18th)
url: https://isc.sans.edu/diary/rss/32994
source: SANS Internet Storm Center, InfoCON: green
date: 2026-05-18
fetch_date: 2026-05-19T06:05:06.964425
---

# TeamPCP Supply Chain Campaign: Activity Through 2026-05-17, (Mon, May 18th)

# [Internet Storm Center](/)

[Sign In](/login.html)
[Sign Up](/register.html)

Handler on Duty: [Jan Kopriva](/handler_list.html#jan-kopriva "Jan Kopriva")

Threat Level: [green](/infocon.html)

* [previous](/diary/32990)

Click [HERE](https://www.sans.org/profiles/kenneth-g-hartman) to learn more about classes Kenneth is teaching for SANS

# [TeamPCP Supply Chain Campaign: Activity Through 2026-05-17](/forums/diary/TeamPCP%2BSupply%2BChain%2BCampaign%2BActivity%2BThrough%2B20260517/32994/)

**Published**: 2026-05-18. **Last Updated**: 2026-05-18 20:08:00 UTC
**by** [Kenneth Hartman](/handler_list.html#kenneth-hartman) (Version: 1)

[0 comment(s)](/diary/TeamPCP%2BSupply%2BChain%2BCampaign%2BActivity%2BThrough%2B20260517/32994/#comments)

Since the [last update](https://isc.sans.edu/diary/32950), the TeamPCP supply chain campaign produced its loudest stretch since the March Trivy disclosure: an officially confirmed Checkmarx Jenkins plugin compromise and a new self-spreading Mini Shai-Hulud worm across npm and PyPI.

## Bottom line up front

Two TeamPCP events broke within 48 hours of each other and doubled attention on the campaign. Checkmarx confirmed its Jenkins AST plugin was trojanized, its third compromise in three months, validating an earlier single-researcher claim. In parallel, a new Mini Shai-Hulud worm poisoned roughly 170 npm and PyPI packages (42 @tanstack packages in about six minutes, downloads above 500 million) and was the first documented npm malware shipping with valid SLSA Build Level 3 provenance, plus a 1-in-6 disk-wipe payload on Israeli and Iranian locale hosts. NHS England issued the campaign's first government alert; CISA stayed silent. Action: audit CI for the indicators below, stop trusting provenance alone, pin and lockfile-verify dependencies.

## How this developed

The period opened quiet and derivative: the lead story was [PCPJack](https://www.sentinelone.com/labs/cloud-worm-evicts-teampcp-and-steals-credentials-at-scale/), a rival worm that evicts TeamPCP before stealing credentials, alongside a single-researcher claim that a Checkmarx Jenkins plugin had been backdoored. Days later it turned loud: Checkmarx officially confirmed that exact Jenkins compromise, and a new Mini Shai-Hulud worm hit the npm and PyPI ecosystems hard. The through-line is escalation: an unconfirmed rumor became a confirmed incident, and the campaign moved from a quiet competitor-eviction story to a high-impact, signed-malware supply chain wave.

## What changed, by theme

### Checkmarx Jenkins plugin: an unconfirmed claim, then official confirmation

**Takeaway: a single-researcher claim, explicitly logged as unconfirmed at the time, was confirmed by Checkmarx four days later.**

On 2026-05-09, researcher Berk Albayrak [reported on X](https://x.com/brkalbyrk7/status/2053175077194117590) that the Checkmarx Jenkins AST scanner plugin had been backdoored. No Tier 1 outlet, no vendor, and no Checkmarx statement corroborated it at the time, so it was carried as information-only pending confirmation. On 2026-05-11 Checkmarx published an [official update](https://checkmarx.com/blog/ongoing-security-updates/) acknowledging that a tampered plugin (version 2026.5.09) had been published to the Jenkins Marketplace, with an exposure window of 2026-05-09 01:25 UTC to 2026-05-10 08:47 UTC. [The Register](https://www.theregister.com/devops/2026/05/11/checkmarx-tackles-another-teampcp-intrusion-as-jenkins-plugin-sabotaged/5237780), [BleepingComputer](https://www.bleepingcomputer.com/news/security/official-checkmarx-jenkins-package-compromised-with-infostealer/), [SecurityWeek](https://www.securityweek.com/checkmarx-jenkins-ast-plugin-compromised-in-supply-chain-attack/), and [The Hacker News](https://thehackernews.com/2026/05/teampcp-compromises-checkmarx-jenkins.html) carried it the same day. This is the third TeamPCP compromise of Checkmarx in three months, and the malicious plugin was installed by several hundred Jenkins controllers. Last known-good build: 2.0.13-829.vc72453fa\_1c16 (2025-12-17). Remediated builds (both 2026-05-09): 2.0.13-848.v76e89de8a\_053 and 2.0.13-847.v08c0072b\_2fd5.

### The Mini Shai-Hulud TanStack wave

**Takeaway: a self-spreading worm poisoned roughly 170 npm and PyPI packages, and the publishes came from TanStack's own trusted release pipeline.**

Starting 2026-05-11 at 19:20 UTC, the worm published 84 malicious artifacts across 42 @tanstack npm packages in about six minutes, including @tanstack/react-router (roughly 12 million weekly downloads). It then propagated to Mistral AI, UiPath, OpenSearch, Guardrails AI, and roughly 170 packages across npm and PyPI, with combined cumulative downloads above 500 million. Primary technical disclosures came from [Wiz](https://www.wiz.io/blog/mini-shai-hulud-strikes-again-tanstack-more-npm-packages-compromised) and [StepSecurity](https://www.stepsecurity.io/blog/mini-shai-hulud-is-back-a-self-spreading-supply-chain-attack-hits-the-npm-ecosystem), with [Snyk](https://snyk.io/blog/tanstack-npm-packages-compromised/) and [BleepingComputer](https://www.bleepingcomputer.com/news/security/shai-hulud-attack-ships-signed-malicious-tanstack-mistral-npm-packages/) adding scope and counts. The tracking identifier is [CVE-2026-45321](/vuln.html?cve=2026-45321) (CVSS 9.6 per The Hacker News; advisory GHSA-g7cv-rxg3-hmpx per Snyk; Wiz and StepSecurity did not assign a CVE). A reported operator error matters for defenders: per Wiz's 2026-05-13 update, the credential stealer is non-functional in the @uipath and @mistralai variants because the payload is reassembled incorrectly there, which limits the harvest from the largest non-TanStack targets.

### Signed malware: the SLSA Build Level 3 first

**Takeaway: this is the first documented npm supply chain attack shipping malware with valid SLSA Build Level 3 provenance, so "has provenance" no longer means "not malicious."**

Per Wiz, StepSecurity, and Snyk, the malicious versions carried valid SLSA Build Level 3 provenance attestations. Analysts assess this is novel and material: the attacker never stole maintainer npm credentials. Instead the malicious versions were published by TanStack's legitimate release pipeline using its own trusted OIDC identity, so the provenance is genuine and proves only that TanStack's pipeline built the artifact, not that the artifact is safe. The practical consequence: provenance and attestation checks alone do not detect this class of attack. Pinning exact versions and verifying lockfile hashes against a known-good baseline are still required.

### Destructive and persistent: a 1-in-6 wipe and AI-agent persistence

**Takeaway: this wave added a sabotage payload and a developer-tool persistence mechanism not seen in earlier Mini Shai-Hulud waves.**

[BleepingComputer (Bill Toulas)](https://www.bleepingcomputer.com/news/security/shai-hulud-attack-ships-signed-malicious-tanstack-mistral-npm-packages/) reported a probabilistic sabotage mechanism with a 1-in-6 chance of running a recursive wipe on systems matching Israeli or Iranian locales, a new behavior class for this malware family. [Expel](https://expel.com/blog/mini-shai-hulud-cross-ecosystem-supply-chain-worm-targeting-npm-pypi/) reported that the worm injects persistence hooks into developer tooling, specifically `.vscode/tasks.json` and `~/.claude/settings.json`, so it survives reboots on developer endpoints. Defenders in the affected regions should treat the wipe behavior as a credible data-loss risk, and all teams should inspect those two file locations on engineer machines.

This destructive, geopolitically-targeted behavior is not new to the campaign. The original TeamPCP campaign report documented a conditional wiper in the earlier CanisterWorm payload that checked whether the infected system's timezone was set to Iran or its default language was Farsi, and on a match attempted to destroy data, wiping Kubernetes clusters node by node, or the local machine if no c...