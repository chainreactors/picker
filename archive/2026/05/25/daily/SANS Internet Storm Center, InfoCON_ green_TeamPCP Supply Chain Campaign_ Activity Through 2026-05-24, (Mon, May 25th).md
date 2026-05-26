---
title: TeamPCP Supply Chain Campaign: Activity Through 2026-05-24, (Mon, May 25th)
url: https://isc.sans.edu/diary/rss/33014
source: SANS Internet Storm Center, InfoCON: green
date: 2026-05-25
fetch_date: 2026-05-26T06:11:04.897847
---

# TeamPCP Supply Chain Campaign: Activity Through 2026-05-24, (Mon, May 25th)

# [Internet Storm Center](/)

[Sign In](/login.html)
[Sign Up](/register.html)

Handler on Duty: [Brad Duncan](/handler_list.html#brad-duncan "Brad Duncan")

Threat Level: [green](/infocon.html)

* [previous](/diary/33012)
* [next](/diary/33016)

Click [HERE](https://www.sans.org/profiles/kenneth-g-hartman) to learn more about classes Kenneth is teaching for SANS

# [TeamPCP Supply Chain Campaign: Activity Through 2026-05-24](/forums/diary/TeamPCP%2BSupply%2BChain%2BCampaign%2BActivity%2BThrough%2B20260524/33014/)

**Published**: 2026-05-25. **Last Updated**: 2026-05-25 13:25:47 UTC
**by** [Kenneth Hartman](/handler_list.html#kenneth-hartman) (Version: 1)

[0 comment(s)](/diary/TeamPCP%2BSupply%2BChain%2BCampaign%2BActivity%2BThrough%2B20260524/33014/#comments)

TeamPCP now operates across three package ecosystems in parallel, it reached GitHub's own internal codebase, it trojanized an officially Microsoft-published Python SDK, and it appears to have open-sourced its own framework on GitHub.

## Bottom line up front

Three escalations stacked inside a single week. First, GitHub's CISO Alexis Wales publicly named a malicious Nx Console VS Code extension build (v18.95.0, publisher nrwl.angular-console, verified-publisher badge, roughly 2.2 million installs) as the root of an intrusion that exfiltrated approximately 3,800 GitHub-internal repositories; OpenAI, Grafana Labs, and Mistral AI were named as downstream victims. The poisoned extension was live on the Visual Studio Marketplace for roughly 18 minutes. Second, an officially Microsoft-published Python SDK on PyPI ([durabletask](https://pypi.org/project/durabletask/), the Azure Durable Functions client, roughly 417,000 monthly downloads) was trojanized across three versions (1.4.1 through 1.4.3) inside an approximately 35-minute window, and independent reporting characterizes the second-stage payload as carrying a Linux disk wiper. Third, the same operator pushed a third Mini Shai-Hulud wave through the @antv npm ecosystem: 639 malicious package versions across 323 packages, including echarts-for-react (roughly 1.1 million weekly downloads) and size-sensor (roughly 4.2 million weekly downloads). Action: rotate any developer or CI/CD credentials exposed during the windows below, stop treating publisher-verified or attestation badges as install-time safety signals, and inspect AI coding agent configuration files for persistence.

## How this developed

The week opened with a credentials-to-publish chain that nobody had previously walked end-to-end in public. Reporting from [BleepingComputer](https://www.bleepingcomputer.com/news/security/github-links-repo-breach-to-tanstack-npm-supply-chain-attack/) and [Help Net Security](https://www.helpnetsecurity.com/2026/05/21/github-grafana-breach-root-cause-nx-console/) ties OIDC credentials harvested in the May 11 TanStack wave to the Nx Console publish on May 18, which means the same operator that built the worm two weeks earlier used its loot to push a trojanized VS Code extension through a verified-publisher account. In parallel, the same operator poisoned the @antv npm ecosystem through a compromised maintainer account ("atool") and dropped a trojanized build of Microsoft's own durabletask SDK on PyPI. Within 72 hours, GitHub itself, Microsoft, and several named AI-lab developer endpoints were affected. By Friday, multiple vendors reported the Shai-Hulud framework source had been published to GitHub, and copycat forks were already running.

## What changed, by theme

### The GitHub-internal breach: a multi-stage operation that worked

**Takeaway: TanStack-harvested credentials from May 11 were used to publish the trojanized Nx Console extension that breached GitHub itself. This is the first publicly confirmed multi-stage operation in the campaign.**

On 2026-05-18 a malicious build of the Nx Console VS Code extension (v18.95.0, publisher nrwl.angular-console) was published to the Visual Studio Marketplace and was live for approximately 18 minutes before it was pulled. Per [Help Net Security](https://www.helpnetsecurity.com/2026/05/20/github-breached-teampcp/) and [OX Security](https://www.ox.security/blog/teampcp-strikes-again-how-a-trojan-vs-code-extension-brought-down-github/), an Nx maintainer credential was used to publish; per [BleepingComputer](https://www.bleepingcomputer.com/news/security/github-links-repo-breach-to-tanstack-npm-supply-chain-attack/), that credential traces back to the TanStack OIDC abuse chain tracked as [CVE-2026-45321](/vuln.html?cve=2026-45321). On a GitHub employee endpoint, the extension auto-updated during the 18-minute window, exfiltrated developer secrets, and was then used to move laterally through GitHub's internal CI/CD. The intrusion exfiltrated approximately 3,800 GitHub-internal repositories before containment; reporting suggests no customer-tenant data was affected. On 2026-05-21, GitHub CISO Alexis Wales publicly named Nx Console as the root and confirmed OpenAI, Grafana Labs, and Mistral AI as named downstream victims whose developers had auto-update enabled.

The practical lesson is uncomfortable: the malicious extension carried the Visual Studio Marketplace verified-publisher badge. Treating that badge as a safety signal at install time would not have prevented this intrusion. A publisher account being legitimate and a specific publish event being legitimate are different claims, and the campaign now operationalizes that gap.

### The official Microsoft SDK: durabletask 1.4.1 through 1.4.3

**Takeaway: For the first time in this campaign, an officially Microsoft-published package surface was trojanized. The second-stage payload reportedly carries a Linux disk wiper.**

Three malicious versions of the [durabletask](https://pypi.org/project/durabletask/) Python client (Microsoft's official Azure Durable Functions SDK, roughly 417,000 monthly downloads) were published to PyPI on 2026-05-19 and yanked within hours. Per [Wiz](https://www.wiz.io/blog/durabletask-teampcp-supply-chain-attack), [Aikido](https://www.aikido.dev/blog/durabletask-package-compromised-mini-shai-hulud), and [Endor Labs](https://www.endorlabs.com/learn/trojanized-microsoft-sdk-durabletask-1-4-1-through-1-4-3-deliver-credential-stealing-malware), the dropper is injected into the package's Python source files, so importing the SDK is sufficient to execute it. The second stage is a credential stealer and worm that targets AWS, Azure, GCP, HashiCorp Vault, 1Password, and Bitwarden, and that propagates inside cloud environments via AWS SSM (inside EC2) and `kubectl exec` (inside Kubernetes). [iTnews reporting](https://www.itnews.com.au/news/mini-shai-hulud-worm-injects-disk-wiper-into-microsoft-azure-pypi-package-625988) characterizes the second stage as carrying a Linux disk wiper, materially extending the campaign's destructive capability beyond the W20 1-in-6 locale-conditional wipe.

If any team installed durabletask versions 1.4.1, 1.4.2, or 1.4.3 on 2026-05-19, the import alone is the trigger. Treat any environment that pulled one of those builds as exposed, including ephemeral CI runners.

### The @antv npm wave: the largest single burst by package count

**Takeaway: 639 malicious versions across 323 packages, including echarts-for-react (roughly 1.1 million weekly downloads). Forty-two of the malicious packages were observed displaying fake Sigstore verification badges in the npm UI.**

On 2026-05-19, a compromised maintainer account ("atool") published a third Mini Shai-Hulud wave across the @antv ecosystem. Independent counts from [StepSecurity](https://www.stepsecurity.io/blog/shai-hulud-here-we-go-again-mass-npm-supply-chain-attack-hits-the-antv-ecosystem), [Snyk](https://snyk.io/blog/mini-shai-hulud-antv-npm-supply-chain-attack/), and [Socket](https://socket.dev/blog/antv-packages-compromised) agree on 639 malicious versions across 323 packages, which makes this the largest single-hour Shai-Hulud burst the campaign has produced. The ro...