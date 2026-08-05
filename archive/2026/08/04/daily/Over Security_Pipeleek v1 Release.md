---
title: Pipeleek v1 Release
url: https://blog.compass-security.com/2026/08/pipeleek-v1-release/
source: Over Security
date: 2026-08-04
fetch_date: 2026-08-05T05:00:01.595379
---

# Pipeleek v1 Release

## [Compass Security Blog](https://blog.compass-security.com "Compass Security Blog — Offensive Defense")

### Offensive Defense

* [Home](https://blog.compass-security.com/)
* [Archive](https://blog.compass-security.com/archive/)
* [Contact](https://blog.compass-security.com/contact/)
* [Newsletter](https://blog.compass-security.com/mailing-list-tigerinfo/)

* [Home](https://blog.compass-security.com/)
* [Archive](https://blog.compass-security.com/archive/)
* [Contact](https://blog.compass-security.com/contact/)
* [Newsletter](https://blog.compass-security.com/mailing-list-tigerinfo/)

# [Pipeleek v1 Release](https://blog.compass-security.com/2026/08/pipeleek-v1-release/ "Pipeleek v1 Release")

[August 4, 2026](https://blog.compass-security.com/2026/08/pipeleek-v1-release/ "Pipeleek v1 Release")
 /
[Jan Friedli](https://blog.compass-security.com/author/jfriedli/)
 /
[0 Comments](https://blog.compass-security.com/2026/08/pipeleek-v1-release/#respond)

[![](https://blog.compass-security.com/wp-content/uploads/2026/05/Pipeleak-2-1024x512.png)](https://blog.compass-security.com/wp-content/uploads/2026/05/Pipeleak-2.png)

## Intro

In 2024 I released the initial version of Pipeleek. At the time the tool was a simple GitLab CI/CD pipeline secrets scanner, not much more. Since then, it has evolved quite a bit: I’ve added support for new CI/CD platforms, integrated the Renovate security research published last year, and built a range of helper commands on top of the scanner. Today it’s time to release version 1.0 of Pipeleek!

## Features

### Secret Scanner Platform Additions

At its core Pipeleek is still a secrets scanner for exposed credentials in CI/CD pipelines. While many products scan for secrets at the version control level, Pipeleek covers leaked credentials in pipeline logs and artifacts. With version 1, Pipeleek supports the following CI/CD platforms:

* GitLab
* GitHub
* Bitbucket
* Azure DevOps
* Gitea
* CircleCI
* Jenkins

### **Pentest Helpers**

Most of the new helpers were added to the GitLab platform commands. These are commands that can be used to further abuse credentials found in an earlier scan. For example, if you find a leaked personal access token, Pipeleek can help harvest Secure Files, CI/CD Variables, Terraform states and more. See the [GitLab guide](https://compasssecurity.github.io/pipeleek/guides/gitlab/#enumerating-cicd-variables-and-secure-files) for details on how to use and combine these. These helpers tailor Pipeleek for penetration testing use.

#### **Runner Exploitation Helper**

If you identify a misconfigured self-hosted runner during an engagement, Pipeleek can help take it further. The [runner exploitation helper](https://compasssecurity.github.io/pipeleek/gl/runners/exploit/) automates spinning up a job and obtaining an interactive shell, letting you perform further post-exploitation steps such as container escape checks.

### **Renovate Enumeration and Exploitation**

A major addition to Pipeleek since the last blog post is support for Renovate misconfiguration exploitation, mostly on GitLab. If you are not familiar with the attack surface, have a look at the [Renovate blog post](https://blog.compass-security.com/2025/05/renovate-keeping-your-updates-secure).

The GitLab Renovate commands support identifying and exploiting vulnerable Renovate configurations. Pipeleek can scan repositories for Renovate configuration files and scan users for potential Renovate bot accounts. Once a misconfigured Renovate bot is identified, Pipeleek helps exploit it to e.g. gain access to all repositories the bot user can reach, enabling lateral movement across repositories.

Additionally, Renovate can be abused to bypass branch protection rules and introduce commits into protected branches of repositories you only have limited access to.

A guide on how to enumerate and abuse Renovate bots is part of the Pipeleek [documentation](https://compasssecurity.github.io/pipeleek/guides/renovate).

## Real-World Examples

To show these aren’t just theoretical capabilities, here are two real findings from using Pipeleek in the wild.

### Renovate Autodiscovery – Tor Project

The Tor Project operates their own GitLab instance where they use a [Renovate Bot](https://gitlab.torproject.org/renovate-bot) globally for all their projects.

As the pipeline [logs](https://gitlab.torproject.org/tpo/tpa/renovate-cron/-/jobs/1512754#L32) show, the Renovate Bot autodiscovers repositories across the whole instance without any filtering. The bot finds all repositories it has access to. It’s noticeable that the bot also renovates repositories which are not in the `tpo/` (Tor Project) namespace.

[![](https://blog.compass-security.com/wp-content/uploads/2026/05/image-14.png)](https://blog.compass-security.com/wp-content/uploads/2026/05/image-14.png)

This is exactly what the `pipeleek gl renovate autodiscovery` command [replicates](https://compasssecurity.github.io/pipeleek/guides/renovate/#2-exploit-autodiscovery-with-a-malicious-project): an attacker could have requested a GitLab account, created a malicious repository, and invited the Renovate Bot to it. The repository would then have been renovated, letting the attacker dump the bot’s access token and thereby compromise every repository it has access to. This problem was fixed in the following two commits: [13d48769](https://gitlab.torproject.org/tpo/tpa/renovate-cron/-/commit/13d48769d3f9ac47c83c1895a5563bbc872efb35) and [aeb43ef8](https://gitlab.torproject.org/tpo/tpa/renovate-cron/-/commit/aeb43ef8cbe00d4c3807472dc876c0e875c58318).

The fix was to introduce an autodiscovery filter that only allows `tpo/` projects to be renovated:

[![](https://blog.compass-security.com/wp-content/uploads/2026/05/image-15.png)](https://blog.compass-security.com/wp-content/uploads/2026/05/image-15.png)

### GitLab Personal Access Token Leaks

During a secret scan using Pipeleek, I stumbled upon the following hit in one of GitLab’s own repositories:

```
2026-05-07T10:23:56+02:00 hit SECRET confidence=high file=combined_report/20250404_0940_dedicated_instance.log jobName=report ruleName=Gitlabv2 type=archive url=https://gitlab.com/gitlab-com/cs-tools/gitlab-cs-tools/deprecation-migration-tools/advanced-search-deprecations/-/jobs/9624848232 value="Command: python3 advanced_search_deprecations.py \"glpat-fz8iCFHoAG2aryuf7piD\" 18.0_config.yml --gitlab sales.gitlab-private.or"
2026-05-07T10:23:56+02:00 hit SECRET confidence=high file=combined_report/20250404_0940_dedicated_instance.log jobName=report ruleName="Gitlab - Personal Access Token v2" type=archive url=https://gitlab.com/gitlab-com/cs-tools/gitlab-cs-tools/deprecation-migration-tools/advanced-search-deprecations/-/jobs/9624848232 value="Command: python3 advanced_search_deprecations.py \"glpat-fz8iCFHoAG2aryuf7piD\" 18.0_config.yml --gitlab sales.gitlab-private.or"
2026-05-07T10:24:01+02:00 hit SECRET confidence=high file=combined_report/20250404_0940_project_18_test.log jobName=report ruleName="Gitlab - Personal Access Token v2" type=archive url=https://gitlab.com/gitlab-com/cs-tools/gitlab-cs-tools/deprecation-migration-tools/advanced-search-deprecations/-/jobs/9624848232 value="Command: python3 advanced_search_deprecations.py \"glpat-bzoxCnU6N2c2MXCgJM0AQbO6SCAGATNIkAF2EA.121r5m3ui\" test_logs/configs/proj"
```

The secret scanner found two personal access tokens leaked in log files that were stored as pipeline artifacts. Luckily, GitLab had already detected the issue, fixed it, and rotated the PATs.

## Getting Started

Ready to try Pipeleek yourself? Here’s where to start.

### Installation

Besides features, a lot of work went into ease of installation and portability. Pipeleek can be installed with a simple bash one-liner, via Go, or by downloading binaries from GitHub Releases. Builds are available for Linux, Windows and macOS. Per-platform builds are also available to reduce binary sizes. The configuration now supports CLI flags, environment variables as ...