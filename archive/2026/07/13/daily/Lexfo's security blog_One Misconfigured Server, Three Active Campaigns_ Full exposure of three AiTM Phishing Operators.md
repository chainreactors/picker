---
title: One Misconfigured Server, Three Active Campaigns: Full exposure of three AiTM Phishing Operators
url: https://blog.lexfo.fr/opendir-to-phishing-operator.html
source: Lexfo's security blog
date: 2026-07-13
fetch_date: 2026-07-14T04:47:39.410954
---

# One Misconfigured Server, Three Active Campaigns: Full exposure of three AiTM Phishing Operators

[BLOG POSTS](/index.html) [CATEGORIES](/categories.html) [ARCHIVES](/archives.html)

[CONTACT US](https://lexfo.fr/contact/)

One Misconfigured Server, Three Active Campaigns: Full exposure of three AiTM Phishing Operators

Mon 13 July 2026 by **Lexfo CTI team** in [CTI](category/cti.html)

## Key Findings

* A single misconfigured Python HTTP server exposed the complete operational stack of a live phishing operator, configs, logs, RMM installers, combolists, and Telegram session files.
* Three distinct threat actors were identified from one entry point: **codemado**, **mail-argenta**, and **saroula01**, each running independent campaigns on custom Evilginx forks sourced from the same public GitHub repositories.
* **codemado** is an Egyptian operator with roots in the hacking underground dating back to 2018, operating a full AiTM platform with a seven-tool RMM arsenal on a Budapest VPS.
* **saroula01**'s Device Code Flow campaign ran undetected for over a year, accumulating 218 confirmed victims across 12 countries, with tokens silently auto-refreshed in the background.
* **mail-argenta** is a Nigerian operator who was identified through infostealer logs containing his own credentials, including the MySQL password hardcoded in his phishing panel, reused across personal accounts.
* Both AiTM proxying and Device Code Flow abuse bypass MFA entirely.
* **codemado's MaDoO Blaster** is promoted within RockyBelling's The Quarry ecosystem, reported by SOCRadar's investigation.
* All three operators built functional MFA-bypass infrastructure from public GitHub repositories with minimal customization, using AI-assisted development.

## Context

On a late April 2026 afternoon, a routine internet scan flagged an open directory on `185.163.204.7`: a server located in Budapest, running `python3 -m http.server 8080` on a public interface with directory listing enabled. What was exposed was not a misconfigured web root, it was a complete operational snapshot of a live attack platform. Phishing configurations, credential harvesting logs, backup archives, RMM installers, combolists and the operator's own Telegram session files were all publicly accessible. The command that left it open was still sitting in the `.bash_history` file, readable through the same listing.

Behind the open directory was an active threat actor running an Evilginx-based Adversary-in-the-Middle (AiTM) phishing platform and a SimpleHelp remote management console, all on the same host.

![](../images/from_open_dir_to_phishing_operator/dirlist.png)

*The exposed directory at `http://185.163.204[.]7:8080`. Visible at a glance: `.bash_history`, `.evilginx/`, `.red-queen/`, `.black-queen/`, `ScreenConnect_Patch[@hackers_assemble].zip`, `tele/`, and the full kit source in `gi.zip`*

With our curiosity piqued, we carried out an investigation into the malicious infrastructure and the associated malicious actor in order to gather intelligence on their operations.

What started as a single open directory unraveled into the identification of three distinct active phishing campaigns, runned by three different threat actors, all leveraging custom variants of the Evilginx AiTM framework, with potential ties to the "The Quarry" ecosystem.

This article documents what we found, how we pivoted from the open directory, and what the full operations looked like once pieced together.

## Identifying the Operator

Attributing the threat actor behind this infrastructure turned out to be surprisingly straightforward. Several artefacts left on the server provided a clear path to identification.

The `.bash_history` file contained multiple `git clone` commands pointing to repositories belonging to a GitHub user operating under the handle **codemado**. His public repositories hosted staging files tied to active operations, malware droppers, suspicious executables, and hardcoded credentials for various panels and malicious scripts. Pivoting through those repositories surfaced a recurring email address: `codemadooo@gmail[.]com`.

The Telegram session file present in the open directory proved equally revealing. Parsed as a SQLite database, it contained the full entity cache of the operator's Telegram account, including his username, `@mad0o0o0o0o`, and an Egyptian phone number (`+20 10XX XXXXXX`). That same number appeared hardcoded in multiple Python scripts found on the server. Arabic-language comments embedded throughout those scripts further corroborate the Egyptian origin.

![](../images/from_open_dir_to_phishing_operator/code.png)

*Comments in Arabic from one of the script in the GitHub repository*

Among the files accessible through the directory listing was a screenshot of a web panel titled **MaDoO Blaster v4.7.3**, a custom spam and credential management interface.

![](../images/from_open_dir_to_phishing_operator/photo_ta.jpg)

*MaDoO Blaster v4.7.3, the operator's custom bulk mailer, screenshot from April 19, 2026*

The handle "MaDoO" appeared in the title bar. Further confirmation came from the operator's Telegram profile: the bio of `@MaD0o0o0o0o` contained a direct link to a Telegraph article published April 21, 2026 under the same account, serving as the official usage guide for MaDoO Blaster. The article's metadata explicitly lists `MaD0o0o0o0o` as author, closing the loop between the tool, the handle, and the Telegram identity.

![](../images/from_open_dir_to_phishing_operator/madosc.png)

*codemado's Telegram profile*

Additional pivoting on `codemadooo@gmail[.]com` through breach datasets and password-based correlation surfaced two older addresses potentially associated with the same persona. While these addresses were also linked to Egyptian-registered profiles across multiple platforms, a confirmed attribution to a specific individual could not be established. The username also appeared on several dating platforms; however, it remains unclear whether these represent genuine personal accounts or profiles used for scam purposes, a common practice in the eCrime ecosystem.

![](../images/from_open_dir_to_phishing_operator/mawada.png)

*Egyptian-registered dating profile*

OSINT pivoting further revealed a persistent forum presence spanning several years. On **Black Hat World**, the account `codemado` dates back to **2018**, where the actor posted under a logo reading *"MADO - security and pentesting"* and declared an interest in *"VoIP, SIP, voice gateway, and exploits"* alongside a greeting of *"Hello from Egypt"*.

![](../images/from_open_dir_to_phishing_operator/BFH.png)

*codemado's Black Hat World presence*

This same brand identity resurfaced eight years later on Telegram under the name **"MaDosc For Pentesting"**, the MADO acronym and "security and pentesting" positioning carried forward verbatim, confirming long-term continuity of persona. On **CrackingX**, the account `codemadooo`, directly matching his operational email address, was registered in **August 2025**, with a last recorded visit on **April 16, 2026**. The account carries zero posts, suggesting passive monitoring rather than active participation.

![](../images/from_open_dir_to_phishing_operator/CrackingX.png)

*Egyptian-registered dating profile*

Taken together, these artefacts paint a consistent picture: **codemado** is an Egyptian threat actor with roots in the hacking and VoIP underground dating back to at least 2018, operating under the aliases **MaDoO**, **MaDosc**, and **MADO**. By 2026, he had evolved from an eCrime hobbyist into a fully operational phishing actor, sourcing AiTM tooling from third-party developers, deploying it against Microsoft 365 targets, and monetising stolen credentials through a custom bulk-mailing platform of his own making.

## The Tooling Layer

### Operator's Toolbox

The open directory at `185.163.204.7:8080` did not just expose an operator, it exposed his entire toolkit. Beyond the phishing infrastructure and credential dumps, the server revealed an assembled collection of offensive tools spanning...