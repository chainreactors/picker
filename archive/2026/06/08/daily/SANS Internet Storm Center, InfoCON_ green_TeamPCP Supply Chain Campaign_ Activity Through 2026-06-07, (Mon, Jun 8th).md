---
title: TeamPCP Supply Chain Campaign: Activity Through 2026-06-07, (Mon, Jun 8th)
url: https://isc.sans.edu/diary/rss/33060
source: SANS Internet Storm Center, InfoCON: green
date: 2026-06-08
fetch_date: 2026-06-09T06:03:39.514094
---

# TeamPCP Supply Chain Campaign: Activity Through 2026-06-07, (Mon, Jun 8th)

# [Internet Storm Center](/)

[Sign In](/login.html)
[Sign Up](/register.html)

Handler on Duty: [Xavier Mertens](/handler_list.html#xavier-mertens "Xavier Mertens")

Threat Level: [green](/infocon.html)

* [previous](/diary/33054)

Click [HERE](https://www.sans.org/profiles/kenneth-g-hartman) to learn more about classes Kenneth is teaching for SANS

# [TeamPCP Supply Chain Campaign: Activity Through 2026-06-07](/forums/diary/TeamPCP%2BSupply%2BChain%2BCampaign%2BActivity%2BThrough%2B20260607/33060/)

**Published**: 2026-06-08. **Last Updated**: 2026-06-08 17:07:37 UTC
**by** [Kenneth Hartman](/handler_list.html#kenneth-hartman) (Version: 1)

[0 comment(s)](/diary/TeamPCP%2BSupply%2BChain%2BCampaign%2BActivity%2BThrough%2B20260607/33060/#comments)

This diary continues the Internet Storm Center's tracking of the TeamPCP supply chain campaign, first documented in the SANS white paper [When the Security Scanner Became the Weapon](https://www.sans.org/white-papers/when-security-scanner-became-weapon) and most recently in the handler diary [Activity Through 2026-05-24](https://isc.sans.edu/diary/33014). Since that update, the story moved into two new places: the United States government, which formally caught up to the campaign, and the wider population of attackers now wielding the Mini Shai-Hulud framework that TeamPCP open-sourced last month.

## Bottom line up front

Two developments stand out since the last update. First, the federal response that prior coverage flagged as conspicuously absent arrived in a roughly 48-hour burst: on 2026-05-27 CISA added the campaign's primary tracking vulnerabilities to its Known Exploited Vulnerabilities catalog, and on 2026-05-28 it issued its first standalone advisory naming the Nx Console and GitHub repository compromises. Second, the leaked Mini Shai-Hulud framework produced its first significant in-the-wild npm wave: beginning 2026-06-01, a credential-stealing worm that Wiz named "Miasma" compromised dozens of @redhat-cloud-services packages, followed two days later by a "Phantom Gyp" variant that reached 57 more. Vendors trace the malware to the TeamPCP lineage but now explicitly caution that a copycat using the public toolkit cannot be ruled out. The affiliated extortion channels stayed frozen, so this period's activity was ecosystem-scale worming rather than named-victim extortion.

## How this developed

The last update closed with two open questions: whether CISA would act on a campaign it had so far left out of the KEV catalog, and whether the framework TeamPCP published to GitHub would produce copycat attacks. Both resolved in the affirmative. CISA's KEV addition and standalone advisory closed the government-silence gap within roughly a day of each other. A week later, the Red Hat npm compromise demonstrated that the open-sourced code is now operational in other hands. The throughline is that the campaign has entered a phase where its tradecraft outlives any single operator: the same techniques, subverted build pipelines that emit validly signed artifacts and install-time credential theft, now arrive from attackers who may have no direct connection to TeamPCP at all.

## What changed, by theme

### CISA formally caught up

On 2026-05-27, CISA added [three vulnerabilities to the KEV catalog](https://www.cisa.gov/news-events/alerts/2026/05/27/cisa-adds-three-known-exploited-vulnerabilities-catalog), including [CVE-2026-45321](/vuln.html?cve=2026-45321) (the TanStack / Mini Shai-Hulud tracking identifier) and [CVE-2026-48027](/vuln.html?cve=2026-48027) (the malicious code embedded in the Nx Console v18.95.0 build), both carrying a federal remediation due date of 2026-06-10, alongside [CVE-2026-8398](/vuln.html?cve=2026-8398) (DAEMON Tools Lite). This resolved the multi-week KEV omission that earlier coverage tracked as an open question. The additions were corroborated by [SC Media](https://www.scworld.com/brief/cisa-adds-daemon-tools-tanstack-and-nx-console-flaws-to-known-exploited-vulnerabilities-catalog) and [Security Affairs](https://securityaffairs.com/192776/security/u-s-cisa-adds-daemon-tools-tanstack-and-nx-console-flaws-to-its-known-exploited-vulnerabilities-catalog.html).

The next day, 2026-05-28, CISA published its first standalone advisory on the campaign, [Supply Chain Compromises Impact Nx Console and GitHub Repositories](https://www.cisa.gov/news-events/alerts/2026/05/28/supply-chain-compromises-impact-nx-console-and-github-repositories). The advisory documents the poisoned Nx Console VS Code extension auto-distributed through the editor update mechanism, the exfiltration of approximately 3,800 GitHub-internal repositories, the assignment of [CVE-2026-48027](/vuln.html?cve=2026-48027), and a separate "Megalodon" campaign that injected malicious GitHub Actions workflows to harvest CI/CD secrets and cloud credentials in public repositories. CISA urges forensic review of CI/CD logs and cloud audit trails and rotation of all CI/CD-accessible secrets. [TechRadar Pro](https://www.techradar.com/pro/security/cisa-warns-that-nx-console-and-github-repositories-abused-in-multiple-supply-chain-compromises-tools-across-enterprise-cloud-and-devops-environments-exploited) and [Cybersecurity Dive](https://www.cybersecuritydive.com/news/cisa-security-software-supply-chain-compromises-GitHub/821487/) carried the advisory to a wider audience.

### The leaked framework produced its first major wave: Red Hat npm

On 2026-06-01, a supply chain attack that Wiz named ["Miasma"](https://www.wiz.io/blog/miasma-supply-chain-attack-targeting-redhat-npm-packages) compromised at least 32 packages (across roughly 90 or more versions) published under the @redhat-cloud-services npm scope, with the affected packages cumulatively averaging about 80,000 weekly downloads. The attacker used a compromised Red Hat employee GitHub account to inject malicious GitHub Actions workflows into RedHatInsights repositories, so the malicious releases carried valid SLSA provenance attestations: the pipeline genuinely ran Red Hat code that contained attacker-injected steps. The payload was a credential-stealing worm with a preinstall script and new cloud-identity collectors for GCP and Azure, and the obfuscated index.js grew from roughly 200 KB to about 4.29 MB. Corroborated by [BleepingComputer](https://www.bleepingcomputer.com/news/security/red-hat-npm-packages-compromised-to-steal-developer-credentials/) and [Cybersecurity Dive](https://www.cybersecuritydive.com/news/dozens-red-hat-npm-packages-supply-chain-attack/821723/).

[Microsoft Threat Intelligence](https://www.microsoft.com/en-us/security/blog/2026/06/02/preinstall-persistence-inside-red-hat-npm-miasma-credential-stealing-campaign/) published its analysis on 2026-06-02, confirming the 32 packages across more than 90 versions and characterizing the payload as a lightly reskinned descendant of the Mini Shai-Hulud worm. [Unit 42](https://unit42.paloaltonetworks.com/monitoring-npm-supply-chain-attacks/) folded the compromise into its running npm tracker the same day.

### Install-time tradecraft advanced within days: Phantom Gyp

On 2026-06-03, a follow-on variant that StepSecurity named "Phantom Gyp" compromised 57 additional packages across 286 or more malicious versions in under two hours. Rather than modifying the package.json scripts field, the variant weaponized binding.gyp files to trigger node-gyp execution at install time, evading monitors that watch only package.json. The largest named victim was @vapi-ai/server-sdk, the official server SDK for the [Vapi.ai](http://Vapi.ai) voice platform, with over 408,000 monthly downloads. See [TechTimes](https://www.techtimes.com/articles/317832/20260605/red-hat-npm-packages-compromised-57-more-follow-signed-attestations-cannot-block-pipeline-hijack.htm), corroborated by Wiz and [Protos Labs](https://www.protoslabs.io/resources/teampcp-shai-hulud-megalodon-supply-chain-jun-2026).

### Attribution is now genuinely ambiguous

Wiz, Microso...