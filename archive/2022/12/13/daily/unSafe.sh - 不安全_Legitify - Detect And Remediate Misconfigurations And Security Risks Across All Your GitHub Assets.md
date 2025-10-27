---
title: Legitify - Detect And Remediate Misconfigurations And Security Risks Across All Your GitHub Assets
url: https://buaq.net/go-139704.html
source: unSafe.sh - 不安全
date: 2022-12-13
fetch_date: 2025-10-04T01:17:13.089602
---

# Legitify - Detect And Remediate Misconfigurations And Security Risks Across All Your GitHub Assets

* [unSafe.sh - 不安全](https://unsafe.sh)
* [我的收藏](/user/collects)
* [今日热榜](/?hot=true)
* [公众号文章](/?gzh=true)
* [导航](/nav/index)
* [Github CVE](/cve)
* [Github Tools](/tools)
* [编码/解码](/encode)
* [文件传输](/share/index)
* [Twitter Bot](https://twitter.com/buaqbot)
* [Telegram Bot](https://t.me/aqinfo)
* [Search](/search/search)

[Rss](/rss.xml)

[ ]
黑夜模式

![](https://8aqnet.cdn.bcebos.com/881428b5bd24f675d4b10672dc1e6285.jpg)

Legitify - Detect And Remediate Misconfigurations And Security Risks Across All Your GitHub Assets

Strengthen the security posture of your GitHub organization! Detect and remediate misconfigu
*2022-12-12 19:30:0
Author: [www.kitploit.com(查看原文)](/jump-139704.htm)
阅读量:26
收藏*

---

[![](https://blogger.googleusercontent.com/img/a/AVvXsEiQ-eQPrgaZqKEE2ItoCCXdxL8S7bniTLA_RD7KXsCu9VIQj56h5wsjPdZo0G6YmTMv3Tm4JXDfLoL9R0181w2xolxwchTBDUpP_yyvz-prWRV_AHE3ATPCVAjQdTS_aze0W7hZKqE8RVal85fuhyGRmKkXsoLpUJX5o5bU0amksI5EDXaMbGk6MfxxFg=w640-h442)](https://blogger.googleusercontent.com/img/a/AVvXsEiQ-eQPrgaZqKEE2ItoCCXdxL8S7bniTLA_RD7KXsCu9VIQj56h5wsjPdZo0G6YmTMv3Tm4JXDfLoL9R0181w2xolxwchTBDUpP_yyvz-prWRV_AHE3ATPCVAjQdTS_aze0W7hZKqE8RVal85fuhyGRmKkXsoLpUJX5o5bU0amksI5EDXaMbGk6MfxxFg)

Strengthen the security posture of your GitHub organization!

## Installation

1. You can download the latest legitify release from [https://github.com/Legit-Labs/legitify/releases](https://github.com/Legit-Labs/legitify/releases "https://github.com/Legit-Labs/legitify/releases"), each archive contains:

* Legitify binary for the desired platform
* Built-in policies provided by Legit Security

2. From source with the following steps:

## Provenance

To enhance the software [supply chain](https://www.kitploit.com/search/label/Supply%20Chain "supply chain") security of legitify's users, as of v0.1.6, every legitify release contains a [SLSA Level 3 Provenacne](https://github.com/slsa-framework/slsa-github-generator/blob/main/internal/builders/generic/README.md "SLSA Level 3 Provenacne") document.
 The provenance document refers to all artifacts in the release, as well as the generated docker image.
 You can use [SLSA framework's official verifier](https://github.com/slsa-framework/slsa-verifier "SLSA framework's official verifier") to verify the provenance.
 Example of usage for the darwin\_arm64 architecture for the v0.1.6 release:

```
VERSION=0.1.6
ARCH=darwin_arm64
./slsa-verifier verify-artifact --source-branch main --builder-id 'https://github.com/slsa-framework/slsa-github-generator/.github/workflows/[email protected]/tags/v1.2.2' --source-uri "git+https://github.com/Legit-Labs/legitify" --provenance-path multiple.intoto.jsonl ./legitify_${VERSION}_${ARCH}.tar.gz
```

## Requirements

1. To get the most out of legitify, you need to be an owner of at least one GitHub organization. Otherwise, you can still use the tool if you're an admin of at least one repository inside an organization, in which case you'll be able to see only repository-related policies results.
2. legitify requires a GitHub personal [access token](https://www.kitploit.com/search/label/Access%20Token "access token") (PAT) to analyze your resources successfully, which can be either provided as an argument (`-t`) or as an environment variable (`$GITHUB_ENV`). The PAT needs the following scopes for full analysis:

```
admin:org, read:enterprise, admin:org_hook, read:org, repo, read:repo_hook
```

See [Creating a Personal Access Token](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/creating-a-personal-access-token "Creating a Personal Access Token") for more information.
 Fine-grained personal [access tokens](https://www.kitploit.com/search/label/Access%20Tokens "access tokens") are currently not supported because they do not support GitHub's GraphQL ([https://github.blog/2022-10-18-introducing-fine-grained-personal-access-tokens-for-github/](https://github.blog/2022-10-18-introducing-fine-grained-personal-access-tokens-for-github/ "https://github.blog/2022-10-18-introducing-fine-grained-personal-access-tokens-for-github/"))

## Usage

```
LEGITIFY_TOKEN=<your_token> legitify analyze
```

By default, legitify will check the policies against all your resources (organizations, repositories, members, actions).

You can control which resources will be analyzed with command-line flags namespace and org:

* `--namespace (-n)`: will analyze policies that relate to the specified resources
* `--org`: will limit the analysis to the specified organizations

```
LEGITIFY_TOKEN=<your_token> legitify analyze --org org1,org2 --namespace organization,member
```

The above command will test organization and member policies against org1 and org2.

## GitHub Enterprise Support

You can run legitify against a GitHub Enterprise instance if you set the endpoint URL in the environment variable `SERVER_URL`:

```
export SERVER_URL="https://github.example.com/"
LEGITIFY_TOKEN=<your_token> legitify analyze --org org1,org2 --namespace organization,member
```

## GitLab Cloud/Server Support

To run legitify against GitLab Cloud set the scm flag to gitlab `--scm gitlab`, to run against GitLab Server you need to provide also SERVER\_URL:

```
export SERVER_URL="https://gitlab.example.com/"
LEGITIFY_TOKEN=<your_token> legitify analyze --namespace organization --scm gitlab
```

## Namespaces

Namespaces in legitify are resources that are collected and run against the policies. Currently, the following namespaces are supported:

1. `organization` - organization level policies (e.g., "Two-Factor [Authentication](https://www.kitploit.com/search/label/Authentication "Authentication") Is Not Enforced for the Organization")
2. `actions` - organization GitHub Actions policies (e.g., "GitHub Actions Runs Are Not Limited To Verified Actions")
3. `member` - organization members policies (e.g., "Stale Admin Found")
4. `repository` - repository level policies (e.g., "Code Review By At Least Two Reviewers Is Not Enforced")
5. `runner_group` - runner group policies (e.g, "runner can be used by public repositories")

By default, legitify will analyze all namespaces. You can limit only to selected ones with the `--namespace` flag, and then a comma separated list of the selected namespaces.

## Output Options

By default, legitify will output the results in a human-readable format. This includes the list of policy violations listed by severity, as well as a summary table that is sorted by namespace.

### Output Formats

Using the `--output-format (-f)` flag, legitify supports outputting the results in the following formats:

1. `human-readable` - Human-readable text (default).
2. `json` - Standard JSON.

### Output Schemes

Using the `--output-scheme` flag, legitify supports outputting the results in different grouping schemes. Note: `--output-format=json` must be specified to output non-default schemes.

1. `flattened` - No grouping; A flat listing of the policies, each with its violations (default).
2. `group-by-namespace` - Group the policies by their namespace.
3. `group-by-resource` - Group the policies by their resource e.g. specific organization/repository.
4. `group-by-severity` - Group the policies by their severity.

### Output Destinations

* `--output-file` - full path of the output file (default: no output file, prints to stdout).
* `--error-file` - full path of the error logs (default: ./error.log).

### Coloring

When outputting in a human-readable format, legitify support the conventional `--color[=when]` flag, which has the following options:

* `auto` - colored output if stdout is a terminal, uncolored otherwise (default).
* `always` - colored output regardless of the output destination.
* `none` - uncolored output regardless of the output destination.

### Misc

* Use the `--failed-only` flag to filter-out passed/skipped checks from the result.

## Scorecard Support

[scorecard](https://github.com/ossf/scorecard "scorecard") is an OSSF's open-source project:

> Scorecards is an automated tool that as...