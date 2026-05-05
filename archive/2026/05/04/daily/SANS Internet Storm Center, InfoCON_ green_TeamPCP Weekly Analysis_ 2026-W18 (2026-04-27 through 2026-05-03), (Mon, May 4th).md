---
title: TeamPCP Weekly Analysis: 2026-W18 (2026-04-27 through 2026-05-03), (Mon, May 4th)
url: https://isc.sans.edu/diary/rss/32950
source: SANS Internet Storm Center, InfoCON: green
date: 2026-05-04
fetch_date: 2026-05-05T05:04:08.616857
---

# TeamPCP Weekly Analysis: 2026-W18 (2026-04-27 through 2026-05-03), (Mon, May 4th)

# [Internet Storm Center](/)

[Sign In](/login.html)
[Sign Up](/register.html)

Handler on Duty: [Rob VandenBrink](/handler_list.html#rob-vandenbrink "Rob VandenBrink")

Threat Level: [green](/infocon.html)

* [previous](/diary/32948)

Click [HERE](https://www.sans.org/profiles/kenneth-g-hartman) to learn more about classes Kenneth is teaching for SANS

# [TeamPCP Weekly Analysis: 2026-W18 (2026-04-27 through 2026-05-03)](/forums/diary/TeamPCP%2BWeekly%2BAnalysis%2B2026W18%2B20260427%2Bthrough%2B20260503/32950/)

**Published**: 2026-05-04. **Last Updated**: 2026-05-04 17:12:18 UTC
**by** [Kenneth Hartman](/handler_list.html#kenneth-hartman) (Version: 1)

[0 comment(s)](/diary/TeamPCP%2BWeekly%2BAnalysis%2B2026W18%2B20260427%2Bthrough%2B20260503/32950/#comments)

## Summary

The most significant development of the week was the April 29 to 30 Mini Shai-Hulud worm, a self-propagating supply chain campaign that compromised four official SAP npm packages, two PyTorch Lightning PyPI versions, two intercom-client npm versions, and the intercom-php Packagist package across three package ecosystems. OX Security tracked roughly 1,800 GitHub repositories created with stolen credentials by the worm during the two day campaign, and Wiz attributed the operation to TeamPCP at high confidence based on a shared RSA public key with the prior Bitwarden CLI and Checkmarx KICS operations. Reporting suggests the campaign has now demonstrated cross-ecosystem worm propagation in production (npm to PyPI to Packagist), realizing the theoretical CanisterSprawl-style ecosystem-jump risk flagged in the W17 weekly. Separately, Check Point Research disclosed on April 27 to 28 that TeamPCP's extortion partner Vect ships a ChaCha20-IETF nonce-reuse flaw that effectively turns Vect 2.0 into a data wiper for any file larger than 128 KB, a finding analysts assess materially weakens the credibility of TeamPCP's Trivy-credential-trove monetization channel.

## Dated event log

* 2026-04-27: Check Point Research published "VECT: Ransomware by design, Wiper by accident", a primary technical analysis of TeamPCP-affiliated extortion partner Vect 2.0. Check Point documents that Vect's encryption routine reuses a single ChaCha20-IETF nonce buffer across each 128 KB chunk; only the last nonce written to disk is recoverable, so any file larger than 131,072 bytes (VM disks, databases, document stores) is permanently destroyed even if the ransom is paid. The report ships six SHA-256 hashes for Vect Windows, Linux, and ESXi variants, and confirms the prior Vect-TeamPCP partnership announcement on BreachForums targeting the Trivy, LiteLLM, Telnyx, Checkmarx, and European Commission credential pools. Source: Check Point Research, <https://research.checkpoint.com/2026/vect-ransomware-by-design-wiper-by-accident/>.
* 2026-04-28: BleepingComputer, The Register, and HelpNetSecurity independently covered the Vect 2.0 wiper-bug disclosure within 24 hours of Check Point's report. Each outlet emphasized that paying the ransom does not recover files larger than 128 KB and that the bug is operationally indistinguishable from a deliberate wiper for the most valuable data classes. No public Vect operator response was identified. Source: BleepingComputer, <https://www.bleepingcomputer.com/news/security/broken-vect-20-ransomware-acts-as-a-data-wiper-for-large-files/> and The Register, <https://www.theregister.com/2026/04/28/dont_pay_vect_a_ransom/> and HelpNetSecurity, <https://www.helpnetsecurity.com/2026/04/29/vect-ransomware-bug/>.
* 2026-04-28: CISA added CVE-2024-1708 (ConnectWise ScreenConnect path traversal, exploited by Kimsuky) and CVE-2026-32202 (Microsoft Windows Shell spoofing, no specific threat actor identified in the KEV entry) to the KEV catalog. Neither addition is TeamPCP-related; the entry is logged here to document that the federal silence on TeamPCP-tied artifacts continued into W18 despite the W17 cascade. Source: CISA, <https://www.cisa.gov/news-events/alerts/2026/04/28/cisa-adds-two-known-exploited-vulnerabilities-catalog>.
* 2026-04-29: Four official SAP npm packages were poisoned between approximately 09:55 and 12:14 UTC: mbt 1.2.48, @cap-js/db-service 2.10.1, @cap-js/postgres 2.2.2, and @cap-js/sqlite 2.2.2. Combined weekly downloads exceed 500,000 across SAP's Cloud Application Programming (CAP) model and Cloud MTA build tooling. The malicious preinstall hook downloads the Bun runtime from the legitimate oven-sh GitHub release path and executes execution.js, an obfuscated information stealer that targets npm and GitHub tokens, SSH keys, AWS, Azure, and GCP credentials, Kubernetes configs, CI/CD secrets, and environment variables. The malware uniquely weaponizes .claude/settings.json and .vscode/tasks.json for AI coding agent persistence, which Wiz characterizes as the first observed supply chain attack to target AI coding agent configurations. Command and control resolves to the malicious endpoint hxxps://zero[.]masscan[.]cloud:443/v1/telemetry. Wiz attributes the operation to TeamPCP at high confidence based on a shared RSA public key with the Bitwarden and Checkmarx operations, a Russian-locale evasion check ("Exiting as russian language detected!"), and a shared PBKDF2 cipher salt ("ctf-scramble-v2", 200,000 iterations) consistent with prior TeamPCP malware. Source: Wiz Blog, <https://www.wiz.io/blog/mini-shai-hulud-supply-chain-sap-npm> and Socket, <https://socket.dev/blog/sap-cap-npm-packages-supply-chain-attack> and StepSecurity, <https://www.stepsecurity.io/blog/a-mini-shai-hulud-has-appeared> and BleepingComputer, <https://www.bleepingcomputer.com/news/security/official-sap-npm-packages-compromised-to-steal-credentials/>.
* 2026-04-30: The Mini Shai-Hulud worm spread from the SAP npm compromise into PyTorch Lightning (PyPI versions 2.6.2 and 2.6.3, approximately 2.1 million weekly downloads) and intercom-client (npm versions 7.0.4 and 7.0.5, approximately 300,000 weekly downloads). OX Security tracked the running count of stolen-credential GitHub repositories from approximately 1,200 (post-SAP wave) to 1,800 by April 30. The Lightning packages were published April 30; intercom-client's compromise is documented by OX as a downstream effect of its Lightning dependency being infected during a local install, demonstrating live worm propagation through ordinary developer activity. Source: OX Security, <https://www.ox.security/blog/lightning-python-package-shai-hulud-supply-chain-attack/> and SecurityWeek, <https://www.securityweek.com/sap-npm-packages-targeted-in-supply-chain-attack/>.
* 2026-04-30: Socket reported that Mini Shai-Hulud also reached Packagist via intercom-php 5.0.2 (over 20.7 million lifetime installs, approximately 285,000 installs per month). The Packagist payload uses Composer's plugin system for install-time execution rather than the npm preinstall hook, and Socket published five SHA-256 hashes plus the same C2 endpoint. This converts the worm's cross-ecosystem capability from theoretical to demonstrated across npm, PyPI, and Packagist within a single 36 hour operational window. Source: Socket, <https://socket.dev/blog/mini-shai-hulud-packagist-malicious-intercom-php-package-compromise>.
* 2026-04-30: Dark Reading published "TeamPCP Hits SAP Packages With Mini Shai-Hulud Attack", returning TeamPCP to Tier 1 mainstream coverage for the second consecutive week. The article ties the Mini Shai-Hulud worm to the late-2025 Shai-Hulud npm worm lineage and to TeamPCP's prior 2026 Trivy and Checkmarx operations, and lists additional GitHub commit dead-drop strings ("beautifulcastle", "EveryBoiWeBuildIsAWormyBoi") plus the repository description marker "A Mini Shai-Hulud has Appeared". Source: Dark Reading, <https://www.darkreading.com/cloud-security/teampcp-sap-packages-mini-shai-hulud>.
* 2026-05-01: Five Eyes joint guidance "Careful Adoption of Agentic AI Services" was released by CISA, NSA, ASD ACSC (Australia), CCCS (Canada), NCSC-UK, and NCSC-NZ, with the underlying...