---
title: AWS CodeBuild Misconfiguration Exposed GitHub Repos to Potential Supply Chain Attacks
url: https://thehackernews.com/2026/01/aws-codebuild-misconfiguration-exposed.html
source: The Hacker News
date: 2026-01-15
fetch_date: 2026-01-16T03:30:36.265101
---

# AWS CodeBuild Misconfiguration Exposed GitHub Repos to Potential Supply Chain Attacks

#1 Trusted Cybersecurity News Platform

Followed by 5.20+ million[**](https://twitter.com/thehackersnews)
[**](https://www.linkedin.com/company/thehackernews/)
[**](https://www.facebook.com/thehackernews)

[![The Hacker News Logo](data:image/png;base64...)](/)

**

**

[** Subscribe – Get Latest News](#email-outer)

* [** Home](/)
* [** Newsletter](#email-outer)
* [** Webinars](/p/upcoming-hacker-news-webinars.html)

* [Home](/)
* [Data Breaches](/search/label/data%20breach)
* [Cyber Attacks](/search/label/Cyber%20Attack)
* [Vulnerabilities](/search/label/Vulnerability)
* [Webinars](/p/upcoming-hacker-news-webinars.html)
* [Expert Insights](https://thehackernews.com/expert-insights/)
* [Contact](/p/submit-news.html)

**

**

**

Resources

* [Webinars](/p/upcoming-hacker-news-webinars.html)
* [Free eBooks](https://thehackernews.tradepub.com)

About Site

* [About THN](/p/about-us.html)
* [Jobs](/p/careers-technical-writer-designer-and.html)
* [Advertise with us](/p/advertising-with-hacker-news.html)

Contact/Tip Us

[**

Reach out to get featured—contact us to send your exclusive story idea, research, hacks, or ask us a question or leave a comment/feedback!](/p/submit-news.html)

Follow Us On Social Media

[**](https://www.facebook.com/thehackernews)
[**](https://twitter.com/thehackersnews)
[**](https://www.linkedin.com/company/thehackernews/)
[**](https://www.youtube.com/c/thehackernews?sub_confirmation=1)
[**](https://www.instagram.com/thehackernews/)

[** RSS Feeds](https://feeds.feedburner.com/TheHackersNews)
[** Email Alerts](#email-outer)

[![Salesforce Security Handbook](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhlCcy_j509wX0FKMRQX-zVzeBNtSIDsH6oDFlljaAeQRz65xSx8g9jicghxtpvDC8yI10jCv1TPEcyPvfoCKOby_0ZjsnNc-3wZG5YeA8sZQBCbZxhzd00jR2ZG8rZr-vp3WLrbXaMVbsVrDwBEeBWBbNSSwFjeuNzhrVOigDqTM7VWfSUJqBwEoYALS58/s728-e100/z-header-d.png)](https://thehackernews.uk/modern-security-shift-d)

# [AWS CodeBuild Misconfiguration Exposed GitHub Repos to Potential Supply Chain Attacks](https://thehackernews.com/2026/01/aws-codebuild-misconfiguration-exposed.html)

**Jan 15, 2026**Ravie LakshmananCloud Security / Vulnerability

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgtz1db4ZW0v9IOmiEDYea5iRhI0pJ5FDJ1MjpzJMDkqBQVUR49G7UA9mmPRPG_tCtFMNFz_8K7nCdBsW_-V85RH4tgLY4jKk5Z0JGAVbcApWgXVb4TwmW1G5kHzydowLYHm36xV6XjcKQK5K1384NfjskWh54_MGL2J_FNx5aFTRUBuV3wxbp_DHaiy6mo/s790-rw-e365/wiz.jpg)

A critical misconfiguration in Amazon Web Services (AWS) [CodeBuild](https://aws.amazon.com/codebuild/) could have allowed complete takeover of the cloud service provider's own GitHub repositories, including its AWS JavaScript SDK, putting every AWS environment at risk.

The vulnerability has been codenamed **CodeBreach** by cloud security company Wiz. The issue was fixed by AWS in September 2025 following responsible disclosure on August 25, 2025.

"By exploiting CodeBreach, attackers could have injected malicious code to launch a platform-wide compromise, potentially affecting not just the countless applications depending on the SDK, but the Console itself, threatening every AWS account," researchers Yuval Avrahami and Nir Ohfeld [said](https://www.wiz.io/blog/wiz-research-codebreach-vulnerability-aws-codebuild) in a report shared with The Hacker News.

The flaw, Wiz noted, is the result of a weakness in the continuous integration (CI) pipelines that could have enabled unauthenticated attackers to breach the build environment, leak privileged credentials like GitHub admin tokens, and then use them to push malicious changes to the compromised repository – creating a pathway for supply chain attacks.

Put differently, the issue undermines [webhook filters](https://docs.aws.amazon.com/codebuild/latest/userguide/github-webhook.html) introduced by AWS to ensure that only certain events trigger a CI build. For example, AWS CodeBuild can be configured such that a build is triggered only when code changes are committed to a specific branch or when a GitHub or GitHub Enterprise Server account ID (aka ACTOR\_ID or actor ID) matches the regular expression pattern. These filters serve to secure against untrusted pull requests.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/zero-trust-summit-d)

The misconfiguration impacted the following AWS-managed open source GitHub repositories, which are configured to run builds on pull requests -

* aws-sdk-js-v3
* aws-lc
* amazon-corretto-crypto-provider
* awslabs/open-data-registry

The four projects, which implemented an ACTOR\_ID filter, suffered from a "fatal flaw" in that they failed to include two characters to ensure – namely the start ^ and end $ anchors – necessary to yield an exact regular expression (regex) match. Instead, the regex pattern allowed any GitHub user ID that was a superstring of an approved ID (e.g., 755743) to bypass the filter and trigger the build.

Because GitHub assigns numeric user IDs sequentially, Wiz said it was able to predict that the new user IDs (currently 9-digits long) would "eclipse" a trusted maintainer's six-digit ID approximately every five days. This insight, coupled with the use of [GitHub Apps](https://docs.github.com/en/apps/overview) to automate app creation (which, in turn, creates a corresponding bot user), made it possible to generate a target ID (e.g., 226755743) by triggering hundreds of new bot user registrations.

Armed with the actor ID, an attacker can now trigger a build and obtain the GitHub credentials of the aws-sdk-js-v3 CodeBuild project, a Personal Access Token (PAT) belonging to the aws-sdk-js-automation user, which has full admin privileges over the repository.

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgVXz5Nse8GqK_6PShb4z-had2gOEGp-fPzqg_sZjFfwyK3I1s0ZccAh4rKQ2A2hANfMtzlhACyJVSdCFDBQkJd0_NOs93Y4-n7hN8w7840RZO0qD1RmaWNWFm3IroQWzLIg6YWduLwB-8VXkKLNaJl3FSc-85r_ldNinz06ZfqId1_NnLuJS6RNaAtgQgD/s790-rw-e365/repo.gif)

The attacker can weaponize this elevated access to push code directly to the main branch, approve pull requests, and exfiltrate repository secrets, eventually setting the stage for supply chain attacks.

"The above repositories' configured regular expressions for AWS CodeBuild webhook filters intended to limit trusted actor IDs were insufficient, allowing a predictably acquired actor ID to gain administrative permissions for the affected repositories," AWS [said](https://aws.amazon.com/security/security-bulletins/2026-002-AWS/) in an advisory released today.

"We can confirm these were project-specific misconfigurations in webhook actor ID filters for these repositories and not an issue in the CodeBuild service itself."

Amazon also said it remediated the identified issues, along with implementing additional mitigations, such as credential rotations and steps to secure the build processes that contain GitHub tokens or any other credentials in memory. It further emphasized that it found no evidence of CodeBreach having been exploited in the wild.

To mitigate such risks, it's essential that untrusted contributions does not trigger privileged CI/CD pipelines by enabling the new [Pull Request Comment Approval](https://docs.aws.amazon.com/codebuild/latest/userguide/pull-request-build-policy.html) build gate, use [CodeBuild-hosted runners](https://docs.aws.amazon.com/codebuild/latest/userguide/action-runner.html) to manage build triggers via GitHub workflows, ensure regex patterns in webhook filters are anchored, generate a unique PAT for each CodeBuild project, limit the PAT's permissions to the minimum required, and consider using a dedicated unprivileged GitHub account for CodeBuild integration.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/attack-surface-insight-d)

"This vulnerability is a textbook example of why adversaries target CI/CD environments: a subtle, easily overlooked flaw that can be exploi...