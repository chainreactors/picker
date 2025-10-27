---
title: Renovate – Keeping Your Updates Secure?
url: https://blog.compass-security.com/2025/05/renovate-keeping-your-updates-secure/
source: Over Security - Cybersecurity news aggregator
date: 2025-05-28
fetch_date: 2025-10-06T22:30:44.225520
---

# Renovate – Keeping Your Updates Secure?

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

# [Renovate – Keeping Your Updates Secure?](https://blog.compass-security.com/2025/05/renovate-keeping-your-updates-secure/ "Renovate – Keeping Your Updates Secure?")

[May 27, 2025](https://blog.compass-security.com/2025/05/renovate-keeping-your-updates-secure/ "Renovate – Keeping Your Updates Secure?")
 /
[Jan Friedli](https://blog.compass-security.com/author/jfriedli/ "Posts by Jan Friedli")
 /
[0 Comments](https://blog.compass-security.com/2025/05/renovate-keeping-your-updates-secure/#respond)

[![Mend Renovate CLI Logo](https://blog.compass-security.com/wp-content/uploads/2025/02/mend-renovate-cli-banner-1024x349.jpg)](https://blog.compass-security.com/wp-content/uploads/2025/02/mend-renovate-cli-banner.jpg)

https://docs.renovatebot.com/assets/images/mend-renovate-cli-banner.jpg

[Renovate](https://docs.renovatebot.com/) is an OSS CLI/bot that updates your software dependencies automatically. It is usually integrated into the CI/CD process and runs on a schedule. It will create a Pull Request / Merge Request (PR/MR) to your repository with dependency updates. It can optionally auto-merge them. If you host it for several repositories or an organization, it can auto-discover new projects and create an onboarding MR/PR, which introduces the repository configuration.

## Self-Hosting

If you decide to self-host Renovate, many possibilities exist which range from using GitLab Pipelines, GitHub Actions, manually using the CLI to Docker and more. Alternatively you could use the Mend-hosted Renovate [GitHub App](https://github.com/apps/renovate), which takes care of hosting Renovate for you.

## Basic Mode of Operation

When Renovate runs, it usually performs these most basic [steps](https://docs.renovatebot.com/key-concepts/how-renovate-works/):

[![](https://blog.compass-security.com/wp-content/uploads/2025/02/process.cleaned-1024x387.png)](https://blog.compass-security.com/wp-content/uploads/2025/02/process.cleaned.png)

A design decision by Renovate is to use the language native package manager to update the dependencies. This means that it will invoke the package manager during its update process.

## Configuration

Renovate consists of two different main configuration files. The Renovate bot **global configuration** is where the self-hosting configuration takes place. Additionally, every repository that is being renovated can have a `renovate.json` configuration file. It only allows a subset of options and cannot override global configurations.

If you self-host your bot you need to be aware of Renovates security model.

Renovates self-hosting [security stance](https://docs.renovatebot.com/security-and-permissions/#self-hosted-renovate-oss-cli-mend-renovate-on-premises):

> All self-hosted Renovate instances must operate under a **trust relationship** with the **developers** of the **monitored repositories**. This has the following implications: **Access to information, execution of code**

As this assumption sometimes clashes with the security boundaries of an organization that makes use of different repository access levels (owner, maintainer, developer) and runs one or multiple shared Renovate bots, this can quickly cause security implications, if the bot is badly configured.

This means depending on the hosting type, the impact of a compromised Renovate bot can be quite high. Assume a Renovate shared bot that has maintainer access in a whole organization. If it is compromised the attacker has access to all repositories which can be accessed by the bot.

**Thus when hosting a Renovate bot you must always assume that each renovated repository can run code in the Renovate process and potentially take over the bot and all renovated repositories.**

## Autodiscovery

When configuring a self-hosted Renovate runner, one can decide whether to create a hardcoded list of projects in the global configuration or to let Renovate auto-discover new repositories. If enabled Renovate will renovate all repositories it has access to. This behavior can be restricted using the [autodiscoverFilter](https://docs.renovatebot.com/self-hosted-configuration/#autodiscoverfilter) or [autodiscoverNamespaces](https://docs.renovatebot.com/self-hosted-configuration/#autodiscovernamespaces) option to renovate only repositories of specific groups/namespaces.

Let’s assume an organization created a bot configuration that allows `autodiscovery` without using the `autodiscoverFilter` or `autodiscoverNamespaces` or a fixed repository list.

On GitLab specifically, an attacker that has access to the same GitLab instance as its victim and who knows (or enumerates) the name of the victim bot, can invite the bot to their project (on GitLab invitations are accepted by default). This and additional issues are described in the official [documentation](https://docs.renovatebot.com/gitlab-bot-security/#risks-of-hosting-a-renovate-gitlab-appbotservice) and the reason why Mend does not provide a bot for GitLab.

Alternatively the attacker must be able to create a repository in a namespace that matches the autodiscovery configuration.

Given these preconditions, the next time Renovate runs, it picks up the malicious repository and renovates it. This results in a situation where the malicious actor gains code execution in the Renovate process, as their repository was never meant to be processed.

The described situation can be easily exploited with the following steps: In a new emtpy repository initiate a new Gradle project, using `gradle init --type java-application`. This creates the following file structure.

```
$ ls -l
total 32
-rw-rw-r-- 1 kali kali 1075 Feb 18 16:28 build.gradle
drwxrwxr-x 3 kali kali 4096 Feb 18 16:23 gradle
-rwxrwxr-x 1 kali kali 5519 Feb 18 16:24 gradlew
-rw-rw-r-- 1 kali kali 2260 Feb 18 16:21 gradlew.bat
-rw-rw-r-- 1 kali kali  123 Feb 18 16:31 renovate.json
-rw-rw-r-- 1 kali kali  582 Feb 18 16:21 settings.gradle
drwxrwxr-x 4 kali kali 4096 Feb 18 16:21 src
```

The attacker now adds their malicious script to the Gradle wrapper script:

```
$ head gradlew
#!/usr/bin/env sh

# malicious script
echo "Greetings from Compass Security"

##############################################################################
##
##  Gradle start up script for UN*X
```

The `renovate.json` is a very minimal configuration and ensures to skip the onboarding step and to be renovated immediately.

```
{
    "$schema": "https://docs.renovatebot.com/renovate-schema.json",
    "extends": [
       "config:recommended"
    ]
}
```

The next time Renovate runs, it picks up the malicious repository it has been invited to or which is in its scope, invokes the `gradlew` script, and executes the malicious code in its Renovate context. Then the attacker can leak the GitLab access token from the [`RENOVATE_TOKEN`](https://docs.renovatebot.com/self-hosted-configuration/#token) environment variable and abuse the bot identity and access/modify other repositories.

## Auto-Merging

[Auto-merging](https://docs.renovatebot.com/noise-reduction/#automerging-and-scheduling) is a Renovate feature that can be used to automatically accept Renovate’s PR/MR. When enabled, Renovate tries to merge the proposed update once the tests pass into the default branch. By [default](https://docs.renovatebot.com/configuration-options/#platformautomerge) it uses the platform-native auto-merge.

Example of auto-merging non-major updates:

`...