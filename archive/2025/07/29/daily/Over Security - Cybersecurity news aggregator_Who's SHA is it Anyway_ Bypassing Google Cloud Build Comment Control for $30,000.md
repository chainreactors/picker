---
title: Who's SHA is it Anyway: Bypassing Google Cloud Build Comment Control for $30,000
url: https://adnanthekhan.com/posts/cloud-build-toctou/
source: Over Security - Cybersecurity news aggregator
date: 2025-07-29
fetch_date: 2025-10-06T23:56:25.969791
---

# Who's SHA is it Anyway: Bypassing Google Cloud Build Comment Control for $30,000

[Adnan Khan's Blog](https://adnanthekhan.com/ "Adnan Khan's Blog (Alt + H)")

* [Search](https://adnanthekhan.com/search/ "Search (Alt + /)")
* [All Posts](https://adnanthekhan.com/archives/ "All Posts")
* [Conference Talks](https://adnanthekhan.com/talks/ "Conference Talks")
* [About Me](https://adnanthekhan.com/about/ "About Me")

[Home](https://adnanthekhan.com/) » [Posts](https://adnanthekhan.com/posts/)

# Who's SHA is it Anyway: Bypassing Google Cloud Build Comment Control for $30,000

July 21, 2025 · 12 min · adnanthekhan

![cloudbuild_toctou](https://adnanthekhan.com/images/posts/cloudbuild-toctou/post-logo.png)

Table of Contents

* [Overview](#overview)
* [Cloud Build <-> GitHub Deep Dive](#cloud-build---github-deep-dive)
  + [Cloud Build](#cloud-build)
  + [What the Fork](#what-the-fork)
  + [Cloud Build App and Hooks](#cloud-build-app-and-hooks)
  + [GitHub Integration](#github-integration)
  + [An Old Suspect](#an-old-suspect)
  + [The Vulnerability and Proof of Concept](#the-vulnerability-and-proof-of-concept)
    - [Environment Setup](#environment-setup)
    - [Winning The Race Condition](#winning-the-race-condition)
    - [Impact](#impact)
    - [Disclosure Timeline](#disclosure-timeline)
  + [Fix Analysis](#fix-analysis)
    - [Fix Mechanism](#fix-mechanism)
      * [Commit tied to Check](#commit-tied-to-check)
      * [Full SHA Requirement](#full-sha-requirement)
    - [Bypass Attempts](#bypass-attempts)
      * [Sub-Second Race](#sub-second-race)
      * [Commit Stamp Forgery](#commit-stamp-forgery)
  + [Conclusion](#conclusion)
  + [References](#references)

# Overview[#](#overview)

I reported a subtle race condition in Google Cloud Build’s GitHub integration that could have allowed someone to bypass maintainer review when running pull request integrations tests.

Google Cloud Build is a managed CI/CD platform that integrates with third-party source code management systems like GitHub. Since CI/CD systems are essentially code execution as a service, access control becomes very important.

When a Google Cloud Build customer integrates with GitHub, they can configure a number of triggers - essentially events on GitHub that will trigger a Google Cloud Build execution. One of these triggers is on pull request. To reduce the risk of poisoned pipeline execution on public and inner-source repositories, Google Cloud Build has a “comment-control” feature that requires maintainers to create a comment in order to trigger a build from an untrusted contributor. I found that developers had baked a Time-of-Check-Time-of-Use (TOCTOU) vulnerability into this feature. Google has since mitigated the issue.

# Cloud Build <-> GitHub Deep Dive[#](#cloud-build---github-deep-dive)

First, I’m going to start with a deep dive into Cloud Build and how it integrates with GitHub. I’ll also cover some fundamental knowledge on *how* most systems integrate with GitHub. This knowledge is key for testing systems that integrate with GitHub - I’ve seen so many issues in systems that integrate with GitHub. I believe the reason for this is that GitHub has a very unique security model, and securely building GitHub integrations requires understanding what GitHub’s security boundaries are *and* how Git works.

## Cloud Build[#](#cloud-build)

Cloud Build is a managed, serverless CI/CD platform that allows users to perform software builds from connected Source Code Management (SCM) systems. It supports integrations with GitHub, BitBucket, GitLab, and Google’s own Cloud Source service - which is deprecated and closed to new customers.

Like other managed build services, Cloud Build supports secrets and running builds with privileged roles. Users might provide a build with credentials to additional repositories or IAM permissions to publish to build artifact registries.

Since builds can have credentials, it’s important to limit who can trigger a build. I’ll use GitHub as an example - what if a user can trigger a build by pushing code or creating a pull request, but the privileges required to push code are *less* than the privileges attached to the pipeline? That’s a privilege escalation vector.

Cloud Build offers a variety of configuration settings to help users control access to their Cloud Build jobs.

## What the Fork[#](#what-the-fork)

To understand how all of this works - you need some background knowledge on how Pull Requests on GitHub work.

On GitHub, a pull request is a request for the PR target to pull changes from a PR head branch. This branch can be within the repository (a feature branch PR), or a forked repository (Fork PR). For public repositories, anyone can fork a repository and create a fork pull request.

Some organizations follow an “InnerSource” model, where developers have read access to a large number of private repositories. If an organization has private forks enabled, then anyone with read access can create forks and fork pull requests.

They will not have *write* access to repositories that do not belong to their immediate team, but they can fork and create pull requests to other inner source repositories. Among organizations that follow an innersource model, pipeline access control is still important - otherwise a single compromised developer account could quickly escalate privileges.

**Terminology**:

Git and GitHub terminology can sometimes be confusing, and different terms map to the same thing.

* PR Head / PR Source: The PR head is the repository and branch containing newer changes that the PR creator wants to contribute into a repository. If I create a fork of a public repository and create a pull request, my repository is the PR head repository.
* PR Base / PR Target: The PR base is the repository and branch that a PR creator wants to add their contribution to.
* Merge Commit: Commit created by GitHub by merging the pull request head commit with commit at tip of the target branch. Timestamp generated by GitHub.
* Head Commit: Commit at the tip of the PR source - this is the last commit pushed by the external contributor.
* Push Timestamp: This is the timestamp that GitHub actually received new code in a branch.
* Commit Timestamp: This is the timestamp attached to a Git commit. For local commits, this is fully user controlled.

## Cloud Build App and Hooks[#](#cloud-build-app-and-hooks)

Cloud Build uses a GitHub App to integrate with GitHub. GitHub has two flavors of applications: OAuth apps and GitHub Apps. The latter is newer and specific to GitHub. Applications can have app registered webhooks - this means when a user or organization installs an app they also register a set of webhooks defined by the app.

Webhooks are typically how apps receive information from GitHub. Events such as pushing code or creating a pull request will trigger a webhook. This webhook will transit GitHub’s backend system and travel over the internet to an address defined by the system.

## GitHub Integration[#](#github-integration)

When Cloud Build users connect their project to a GitHub repository, they can configure a variety of triggers to run builds. One of the triggers is the pull request trigger. When enabled, creation of a pull request or updates to a pull request head branch will trigger new Cloud Build jobs.

One common risk in CI/CD pipelines is [Poisoned Pipeline Execution](https://owasp.org/www-project-top-10-ci-cd-security-risks/CICD-SEC-04-Poisoned-Pipeline-Execution). To quote the OWASP entry:

> Poisoned Pipeline Execution (PPE) risks refer to the ability of an attacker with access to source control systems - and without access to the build environment, to manipulate the build process by injecting malicious code/commands into the build pipeline configuration, essentially ‘poisoning’ the pipeline and running malicious code as part of the build process.

To prevent poisoned pipeline execution from pull requests, Cloud Build offers a “Comment Control” feature. By default, Cloud Build requires comment control if the pull request creator do...