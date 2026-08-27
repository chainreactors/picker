---
title: git-alerts v1.8.0
url: https://kitploit.com/en/posts/github-boringtools-git-alerts-v180
source: Kitploit
date: 2026-08-26
fetch_date: 2026-08-27T12:12:40.288922
---

# git-alerts v1.8.0

[Skip to content](#main-content)

[![Kitploit](/_next/image?url=%2Flogo.png&w=64&q=75)KITPLOIT](/en)[Tools](/en/tools)[Blog](/en/blog)Categories

EN

[Submit](/en/submit)

[Tools](/en/tools)[Blog](/en/blog)Categories

[Submit](/en/submit)

EN

Hacking, PenTest, and Cybersecurity Tools for Your Security Arsenal!

[Back to updates](/en/updates)

![](https://assets.kitploit.com/production/public/tools/6323/ecd727ba073c3629ffe952394fff88698bf5411065c11cc08f07ab9f1fb4995a.png)

New releaseAug 26, 2026

# git-alerts v1.8.0

Tool to detect and monitor GitHub org users' public repositories for secrets and sensitive files

Share

# GitAlerts

[![Go Report Card](https://goreportcard.com/badge/github.com/boringtools/git-alerts)](https://goreportcard.com/report/github.com/boringtools/git-alerts)
![License](https://img.shields.io/github/license/boringtools/git-alerts)
![Release](https://img.shields.io/github/v/release/boringtools/git-alerts)

## What problem does it solve?

GitHub repositories created under any organization can be controlled by the GitHub administrators. However any repository created under an organization's user account is not controllable unless the organisation has adopted the GitHub enterprise-managed user (EMU) model.

Any public repository under the organization's user account that was created accidentally or for testing purposes could leak secrets, internal information, code etc. GitAlerts helps you detect and monitor such cases

### Example

> Can be controlled by the administrator `https://github.com/<org>/<org-repo-name>`

> Can't be controlled by the administrator `https://github.com/<org-user>/<org-user-repo-name>`

## GitAlerts Platform (Web UI + API)

**Looking for a full platform?** [GitAlerts API](https://github.com/boringtools/git-alerts-api) is a self-hosted web platform built on the same concepts — with a modern React UI, async scanning via Celery, GitHub advanced search (code, commits, issues, repos, users), smart filtering, encrypted token storage, and an MCP server for AI/LLM integration.

📺 [Watch the walkthrough on YouTube](https://youtu.be/9AujWmTx9-w)

| Feature | CLI | Platform |
| --- | --- | --- |
| Scan org user repos | ✅ | ✅ |
| Secrets detection (TruffleHog/Gitleaks) | ✅ | ✅ |
| GitHub advanced search | ❌ | ✅ |
| Web UI & dashboard | ❌ | ✅ |
| Finding triage & filtering | ❌ | ✅ |
| Slack notifications | ✅ | ✅ |
| AI/MCP integration | ❌ | ✅ |
| Async scanning (Celery + Redis) | ❌ | ✅ |

## Getting Started

* Download the binary file for your operating system / architecture from the [Official GitHub Releases](https://github.com/boringtools/git-alerts/releases)
* You can also install `git-alerts` using homebrew in MacOS and Linux

root@kitploit:~

```
brew tap boringtools/tap
brew install boringtools/tap/git-alerts
```

* Alternatively, build from source

> Ensure $(go env GOPATH)/bin is in your $PATH

root@kitploit:~

```
go install github.com/boringtools/git-alerts@main
```

Setup GitHub personal access token [(PAT)](https://github.com/boringtools/git-alerts/blob/main/docs/github.md) as the environment variable, without PAT GitHub will only allow `60` request per hour.

root@kitploit:~

```
export GITHUB_PAT=YOUR_GITHUB_PAT
```

## Usage

### Scan

Scan GitHub repositories belonging to your organization users

root@kitploit:~

```
git-alerts scan --org your-org-name
```

Scan and generate report with custom path

root@kitploit:~

```
git-alerts scan --org your-org-name --report-path /your/file/path/
```

Scan custom list of GitHub users

root@kitploit:~

```
git-alerts scan --org your-org-name --users-file-path /path/to/csv/file
```

> Ensure to pass CSV file with the list of GitHub usernames

root@kitploit:~

```
username01
username02
username03
```

### Monitor

Monitor new public repositories being created by your organization users

root@kitploit:~

```
git-alerts monitor --org your-org-name
```

Monitor new public repositories being created by your organization users with slack notification

root@kitploit:~

```
git-alerts monitor --org your-org-name --slack-alert
```

Setup slack webhook token as the environment variable

root@kitploit:~

```
export SLACK_HOOK=SLACK_WEBHOOK_URL
```

Monitor new public repositories being created by your organization users along with secrets detection

root@kitploit:~

```
git-alerts monitor --org your-org-name --gitleaks
```

Monitor new public repositories being created by your organization users along with secrets detection and slack notification

root@kitploit:~

```
git-alerts monitor --org your-org-name --gitleaks --slack-alert
```

Monitor custom list of GitHub users

root@kitploit:~

```
git-alerts monitor --org your-org-name --users-file-path /path/to/csv/file
```

> Ensure to pass CSV file with the list of GitHub usernames

root@kitploit:~

```
username01
username02
username03
```

### Secrets

Scan with secrets detection using Trufflehog

> Ensure trufflehog is installed in your machine

root@kitploit:~

```
git-alerts detect --org your-org-name --trufflehog
git-alerts detect --org your-org-name --trufflehog-verified
```

Scan with secrets detection using Gitleaks

> Ensure Gitleaks is installed in your machine

root@kitploit:~

```
git-alerts detect --org your-org-name --gitleaks
```

Scan with secrets detection using custom list of GitHub users

root@kitploit:~

```
git-alerts detect --org your-org-name --users-file-path /path/to/csv/file --gitleaks
```

> Ensure to pass CSV file with the list of GitHub usernames

root@kitploit:~

```
username01
username02
username03
```

## Documentation

[docs](https://github.com/boringtools/git-alerts/tree/main/docs)

> Please feel to reach out for any feedback and suggestions

## Star History

[![Star History Chart](https://api.star-history.com/svg?repos=boringtools/git-alerts&type=Date)](https://star-history.com/#boringtools/git-alerts&Date)

[Read more](/en/tools/github/boringtools/git-alerts?expand=1)

## Categories

[Vulnerability Scanners](/en/categories/vulnerability-scanners)[Cloud Security](/en/categories/cloud-security)[DevSecOps](/en/categories/devsecops)[Secret Detection](/en/categories/secret-detection)[Threat Intelligence](/en/categories/threat-intelligence)

### Most Popular

[View all →](/en/tools)

Discover the most used tools by our community.

Last 7 DaysLast 30 Days

Explore all tools

Browse our collection of tools

[View all tools →](/en/tools)

Kitploit is a directory of hacking, cybersecurity, and pentesting tools. Discover the latest project updates to find vulnerabilities, analyze systems, automate testing, and strengthen your security.

·Analytics preferences·[Feeds](/en/feeds)·[Contact](/en/contact)·[Privacy](/en/privacy)·© 2026 Kitploit

Tool Directory

## Categories

[View all categories](/en/categories)

Loading categories