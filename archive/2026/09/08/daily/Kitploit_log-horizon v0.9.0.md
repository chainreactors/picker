---
title: log-horizon v0.9.0
url: https://kitploit.com/en/posts/github-lnfernux-log-horizon-v090
source: Kitploit
date: 2026-09-08
fetch_date: 2026-09-09T06:55:18.171746
---

# log-horizon v0.9.0

[Skip to content](#main-content)

[![Kitploit](/_next/image?url=%2Flogo.png&w=64&q=75)KITPLOIT](/en)[Tools](/en/tools)[Blog](/en/blog)Categories

EN

[Submit](/en/submit)

[Tools](/en/tools)[Blog](/en/blog)Categories

[Submit](/en/submit)

EN

Hacking, PenTest, and Cybersecurity Tools for Your Security Arsenal!

[Back to updates](/en/updates)

![](https://assets.kitploit.com/production/public/tools/13110/ff9d1da85043d02a216df72913ecf63520310b8d820b1bd1278b8e4aca718494.png)

New releaseSep 8, 2026

# log-horizon v0.9.0

Microsoft Sentinel SIEM Log Source Analyzer

Share

![](https://assets.kitploit.com/production/public/readmes/13110/5c77f4fe02962fd0004a21eda7576c9eaa94dceec8f92c6317358723a3909ad9.png)

### Microsoft Sentinel SIEM Log Source Analyzer

![PowerShell 7+](https://img.shields.io/badge/PowerShell-7+-blue)
![Module Version](https://img.shields.io/badge/version-0.9.0-green)

---

I've had to answer *"what are we actually getting out of these logs?"* or *"what is the recommended logs for Microsoft Sentinel"* more times than I can count. The answer always depend on so many things, but we can be generic. So I built this thingy right here.

**Log Horizon** connects to your Microsoft Sentinel workspace (and optionally Defender XDR), goes through every log table you're ingesting, and tells you whether you're getting security value from it or just burning money. It classifies tables, scores them against your detection rules, and gives you concrete recommendations with savings estimates.

> **Important**: This is a generic approach. If you know a log source is important to your environment, that context always takes precedence over what this tool tells you. The classifications are a starting point, not gospel.

**Want to read more? I have some posts about Log Horizon on my blog:**

1. [Tool Release: Log Horizon](https://infernux.no/blog/loghorizon-toolrelease/)
2. [Update: Log Horizon v0.5.0](https://infernux.no/blog/loghorizon-update1/)
3. [Building a practical log baseline and how Log Horizon helps you do that](https://infernux.no/blog/buildingapracticallogbaseline/)
4. [How to use Log Horizon](https://infernux.no/blog/loghorizon-howtouse/)

## Features

| Feature | Description |
| --- | --- |
| **Classification Engine** | 481-entry knowledge base covering 240+ connectors, 22 categories, with lifecycle status (deprecated/legacy plus replacement tables) and automatic heuristic fallback for unknown tables |
| **Cost-Value Scoring** | Per-table cost tier vs detection tier matrix with combined assessment (High Value to Low Value), priced per observed plan (Analytics, Basic, Data Lake) |
| **Recommendations** | 13 prioritised action types: data lake or Basic candidates, zero-detection tables, XDR streaming waste, ingest-time filtering, split candidates, plan usage, deprecated sources, retention shortfalls, XDR Checker and Detection Analyzer findings, each with savings estimates |
| **Detection Mapping** | Maps analytics rules, hunting queries, and XDR detections to each table to spot coverage gaps |
| **Correlation Tags** | Detects `#DONT_CORR#` / `#INC_CORR#` tags in rule descriptions and flags rules excluded from Defender correlation |
| **Retention Compliance** | Compares actual retention against recommended minimums based on industry standards and security best practices |
| **SOC Optimisation** | Pulls Microsoft's own SOC improvement recommendations from the Security Insights API |
| **Keyword Gap Analysis** | Flag tables you should be ingesting but aren't based on vendor/product keywords |
| **Transform Discovery** | Discovers Data Collection Rules (DCRs) targeting the workspace (subscription list filtered on destination, the workspace transformation DCR, and workspace associations), parses inline and multi-stage transforms, and labels every operation (filter, projection, column removal, enrichment, aggregation) |
| **Split Table Detection** | Identifies `_SPLT_CL` split tables and links them back to parent tables in the classification engine |
| **Split KQL Generator** | Generates portal-ready split KQL from a curated knowledge base, live rule analysis, and community field frequency stats -- condition-only format that pastes straight into the Sentinel split rule editor. Field lists are intersected with the table's live schema; anything not present is reported as dropped |
| **Detection Analyzer** | Scores analytic rules for potential noisiness using incident outcomes (auto-close ratio, false positive ratio, and incident volume percentiles) |
| **XDR Checker** | Adds an XDR-focused advisory layer: streaming coverage checks and one-year Data Lake retention guidance for XDR-related telemetry |
| **Custom Classifications** | Provide your own JSON to add or override the built-in classification database |
| **Collection Cache** | Collected workspace data is cached locally (default 60 minutes) so re-runs and re-exports take seconds; opt out with `-NoCache` |
| **Sovereign Clouds** | ARM, Log Analytics and Graph endpoints follow the signed-in Azure environment (public, US Government, China) |
| **Interactive TUI** | Spectre.Console dashboard with menus, colour-coded tables, drill-downs, retention wizard and ASCII art |
| **Export** | JSON, Markdown, or static HTML report for sharing with the team |

## Disclaimer

> [!CAUTION]
> **Disclaimer**
>
> **This tool is developed and maintained with the help of AI.** Please exercise caution when using this solution and always understand what are you running before you run it in production. The developer assumes no liability for any vulnerabilities or issues.
>
> By downloading, installing, or using this tool, you acknowledge that you have read, understood, and agree to these terms.

## Prerequisites

| What you need | Version |
| --- | --- |
| PowerShell | 7.0+ |
| Az modules | `Az.Accounts` |
| Other modules | `PwshSpectreConsole` 2.6.3+ |
| Optional | `Microsoft.Graph.Authentication` (for `-IncludeDefenderXDR` as a signed-in user) |

Endpoints follow the Azure environment of the current `Connect-AzAccount` session, so Azure Government and Azure China workspaces work without extra parameters. The public cloud values are used when no environment is available.

If you're not already logged into Azure, the module will fire up `Connect-AzAccount` for you. If you are, it'll just carry on.

Permissions: Log Analytics Reader and Microsoft Sentinel Reader on the workspace cover the analysis. Transform discovery also needs `Microsoft.Insights/dataCollectionRules/read` (Monitoring Reader) on the subscription or resource group; without it the run continues and prints a warning naming the missing permission. `-IncludeDefenderXDR` uses Microsoft Graph with `CustomDetection.Read.All`, which for a signed-in user means the optional `Microsoft.Graph.Authentication` module.

## Getting started

Pretty straight forward:

root@kitploit:~

```
# Grab the dependencies
Install-Module -Name Az.Accounts -Scope CurrentUser
Install-Module -Name PwshSpectreConsole -Scope CurrentUser

# Clone and import
git clone https://github.com/lnfernux/log-horizon
Import-Module ./log-horizon/LogHorizon.psd1
```

## Usage

### The basics

Start by connecting to Azure and making sure you select the right account and subscription:

root@kitploit:~

```
Connect-AzAccount
```

Then we can invoke the tool:

root@kitploit:~

```
Invoke-LogHorizon -SubscriptionId '00000000-0000-0000-0000-000000000000' -ResourceGroup 'rg-sentinel' -WorkspaceName 'my-sentinel-ws'
```

Output should look something like this:

![{F4FFA929-B24F-490C-BD3D-F75E214BCD93}](https://assets.kitploit.com/production/public/readmes/13110/ff9d1da85043d02a216df72913ecf63520310b8d820b1bd1278b8e4aca718494.png)

Also has a menu to dig deeper into other outputs:

![{83CE9E6E-F373-49CD-BE05-182DB69F36BE}](https://assets.kitploit.com/production/public/readmes/13110/0606a575b10640bd13ebb87b930f74b2438167b5578cb843b412b4fcf273fc26.png)

### Keyword gaps + Defender XDR

Want to know if you're missin...