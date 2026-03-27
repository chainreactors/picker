---
title: TeamPCP Supply Chain Campaign: Update 001 - Checkmarx Scope Wider Than Reported, CISA KEV Entry, and Detection Tools Available, (Thu, Mar 26th)
url: https://isc.sans.edu/diary/rss/32834
source: SANS Internet Storm Center, InfoCON: green
date: 2026-03-26
fetch_date: 2026-03-27T04:33:39.020691
---

# TeamPCP Supply Chain Campaign: Update 001 - Checkmarx Scope Wider Than Reported, CISA KEV Entry, and Detection Tools Available, (Thu, Mar 26th)

# [Internet Storm Center](/)

[Sign In](/login.html)
[Sign Up](/register.html)

Handler on Duty: [Brad Duncan](/handler_list.html#brad-duncan "Brad Duncan")

Threat Level: [green](/infocon.html)

* [previous](/diary/32830)

Click [HERE](https://www.sans.org/profiles/kenneth-g-hartman) to learn more about classes Kenneth is teaching for SANS

# [TeamPCP Supply Chain Campaign: Update 001 - Checkmarx Scope Wider Than Reported, CISA KEV Entry, and Detection Tools Available](/forums/diary/TeamPCP%2BSupply%2BChain%2BCampaign%2BUpdate%2B001%2BCheckmarx%2BScope%2BWider%2BThan%2BReported%2BCISA%2BKEV%2BEntry%2Band%2BDetection%2BTools%2BAvailable/32834/)

**Published**: 2026-03-26. **Last Updated**: 2026-03-26 17:42:22 UTC
**by** [Kenneth Hartman](/handler_list.html#kenneth-hartman) (Version: 2)

[0 comment(s)](/diary/TeamPCP%2BSupply%2BChain%2BCampaign%2BUpdate%2B001%2BCheckmarx%2BScope%2BWider%2BThan%2BReported%2BCISA%2BKEV%2BEntry%2Band%2BDetection%2BTools%2BAvailable/32834/#comments)

This is the first update to the TeamPCP supply chain campaign threat intelligence report, ["When the Security Scanner Became the Weapon"](https://www.sans.org/white-papers/when-security-scanner-became-weapon) (v3.0, March 25, 2026). That report covers the full campaign from the February 28 initial access through the March 24 LiteLLM PyPI compromise. This update covers developments since publication.

## Checkmarx ast-github-action: All 91 Tags Were Compromised, Not Just v2.3.28

The most significant new finding since the report's publication: the scope of the Checkmarx `ast-github-action` compromise was substantially larger than publicly reported.

Checkmarx's official security advisory stated that "all older versions have been permanently deleted" but did not quantify how many tags were affected. This ambiguity allowed the security community to anchor on a single confirmed version — v2.3.28 — as the extent of the compromise. Sysdig's analysis characterized it as "Checkmarx/ast-github-action/2.3.28: (possibly more)." Even Wiz, which assessed that "it is likely all tags were impacted," only observed the single tag directly.

An independent security researcher who was working this incident firsthand at a Checkmarx customer has now provided primary evidence that **all 91 published tags** were overwritten — every version from v0.1-alpha through v2.3.32. The evidence is publicly visible in the [GitHub activity log](https://github.com/Checkmarx/ast-github-action/activity), which shows 91 tag deletions performed during Checkmarx's remediation between 19:09 and 19:16 UTC on March 23, 2026.

Three of the malicious commits are still visible on GitHub:

* [f1d2a3477e0d](https://github.com/Checkmarx/ast-github-action/commit/f1d2a3477e0d8e42a4e7ad15b6fc376cf910e373)
* [f58de2470825](https://github.com/Checkmarx/ast-github-action/commit/f58de2470825e8ee7c0b3ecc194a948056381003)
* [aa52a82cddf2](https://github.com/Checkmarx/ast-github-action/commit/aa52a82cddf2fa5ad54a519a0a56fd430264dbbe)

Each malicious commit follows an identical pattern: the legitimate Docker-based `action.yml` was replaced with a composite action that executes a credential-stealing `setup.sh` before delegating to the legitimate Checkmarx action at pinned SHA `327efb5d`. Each commit was individually crafted with a version-appropriate backdated timestamp and fake commit message (e.g., "2.0.30: PR #"). The attacker did not reuse a single malicious commit across multiple tags — they created individual poisoned commits for individual versions.

**The impact of this under-reporting is material.** Organizations that searched their CI/CD logs only for `[[email protected]](/cdn-cgi/l/email-protection)` would have missed compromised runs referencing any of the other 90 poisoned tags. The credential stealer executed regardless of which tag version was referenced.

**Recommended action:** Search your CI/CD workflow logs for ANY reference to `checkmarx/ast-github-action` that executed between 12:58 and 19:16 UTC on March 23, 2026. If found, treat all secrets accessible to that workflow as compromised and rotate immediately. The only safe version is v2.3.33, released during remediation.

For comparison, the companion `kics-github-action` received accurate "all 35 tags" reporting from the outset, largely because [GitHub Issue #152](https://github.com/Checkmarx/kics-github-action/issues/152) was filed publicly with the title "Malware injected in all Git Tags." No equivalent public issue was filed for `ast-github-action`.

## CISA Adds CVE-2026-33634 to Known Exploited Vulnerabilities Catalog

CISA has added [CVE-2026-33634](https://www.cve.org/CVERecord?id=CVE-2026-33634) (CVSS 9.4) to the Known Exploited Vulnerabilities (KEV) catalog, confirming active exploitation. Federal agencies are required to remediate by **April 3, 2026**. All organizations using Trivy, `trivy-action`, or `setup-trivy` should verify they are running safe versions:

* **Trivy binary:** ≥ v0.69.2
* **trivy-action:** v0.35.0 (or pin to SHA `57a97c7e7821a5776cebc9bb87c984fa69cba8f1`)
* **setup-trivy:** v0.2.6 (re-released clean)

## PyPI Quarantine Lifted; LiteLLM Freezes All Releases

PyPI lifted its quarantine of the LiteLLM package on March 25 at 20:15 UTC. Malicious versions 1.82.7 and 1.82.8 have been yanked. However, BerriAI has announced they are [pausing all new LiteLLM releases](https://docs.litellm.ai/blog/security-update-march-2026) pending a complete supply chain security review. Google's Mandiant has been engaged for forensic analysis. The last known-safe version is v1.82.6.rc.2.

Any installation of LiteLLM v1.82.7 or v1.82.8 should be treated as compromised — rotate all credentials that were present as environment variables, in configuration files, or in Kubernetes secrets on the affected system.

## Community Detection Tools Now Available

Two community-developed detection tools are now available:

* **[jthack/litellm-vuln-detector](https://github.com/jthack/litellm-vuln-detector)** — Scans for malicious `.pth` files, persistence backdoors (`~/.config/sysmon/sysmon.py`, systemd user services), exfiltration domains (`models.litellm.cloud`), and attacker Kubernetes pods (`node-setup-*` in `kube-system`).
* **[Community detection gist](https://gist.github.com/sorrycc/30a765b9a82d0d8958e756b251828a19)** — Checks for compromised LiteLLM versions and TeamPCP indicators.

Run these against your CI/CD runners, developer workstations, and any systems where LiteLLM was installed during the March 24 exposure window.

## Additional Intelligence

**TeamPCP Telegram statement:** The threat actor posted to their Telegram channel: "These companies were built to protect your supply chains yet they can't even protect their own... we're gonna be around for a long time stealing terrabytes [sic] of trade secrets with our new partners." [Socket.dev](https://socket.dev/blog/teampcp-targeting-security-tools-across-oss-ecosystem) characterizes this as confirmation that TeamPCP is deliberately and systematically targeting security tools as a strategy.

**Wiz publishes third analysis:** Wiz Research published ["Three's a Crowd: TeamPCP Trojanizes LiteLLM"](https://www.wiz.io/blog/threes-a-crowd-teampcp-trojanizes-litellm-in-continuation-of-campaign), confirming LiteLLM is present in 36% of cloud environments they monitor. This is the third Wiz blog post covering the campaign arc (Trivy, KICS, LiteLLM).

**RSA Conference timing:** Analysts assess that TeamPCP may have deliberately timed the LiteLLM attack to coincide with RSA Conference, when many security teams had reduced staffing. This assessment, reported by [CSO Online](https://www.csoonline.com/article/4149938/trivy-supply-chain-breach-compromises-over-1000-saas-environments-lapsus-joins-the-extortion-wave.html), is based on temporal correlation and has not been confirmed by the threat actor or forensic evidence.

**Parallel campaign — ForceMemo:** [SecurityWeek reports](https://www.securityweek.com/forcememo-python-r...