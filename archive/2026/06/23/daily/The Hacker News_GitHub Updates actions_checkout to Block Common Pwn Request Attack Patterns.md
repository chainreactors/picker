---
title: GitHub Updates actions/checkout to Block Common Pwn Request Attack Patterns
url: https://thehackernews.com/2026/06/github-updates-actionscheckout-to-block.html
source: The Hacker News
date: 2026-06-23
fetch_date: 2026-06-24T06:06:31.259324
---

# GitHub Updates actions/checkout to Block Common Pwn Request Attack Patterns

#1 Trusted Cybersecurity News Platform

Followed by 5.70+ million[**](https://twitter.com/thehackersnews)
[**](https://www.linkedin.com/company/thehackernews/)
[**](https://www.facebook.com/thehackernews)

[![The Hacker News Logo](data:image/png;base64...)](/)

**

**

[** Get the Latest News](#email-outer)

* [Home](/)
* [Newsletter](#email-outer)
* [Webinars](/p/upcoming-hacker-news-webinars.html)

* [Home](/)
* [Threat Intelligence](/search/label/Threat%20Intelligence)
* [Vulnerabilities](/search/label/Vulnerability)
* [Cyber Attacks](/search/label/Cyber%20Attack)
* [Webinars](/p/upcoming-hacker-news-webinars.html)
* [Expert Insights](https://thehackernews.com/expert-insights/)
* [Awards](https://awards.thehackernews.com/)

**

**

**

Resources

* [Webinars](/p/upcoming-hacker-news-webinars.html)
* [Awards](https://awards.thehackernews.com/)
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

[![cybersecurity](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjQl2axNwsfhbXOFynrg_uAZsvHi3OvNGSA8KJO-BKR8Xm3x7yjKV3EvfY4v5mwXx6LF0uWFb9h9d9iAV_Pi-YYhqimX9wx4OaLdDJEdR215Xrxq_PAtXkaLfQso4pTSjbj6fvh_ZTliLpzWZSZfcoZgyXtKwhN-SSDDlmbtUqGLshc0KqYQGWYHMN52Sl1/s728-e100/zz-d.jpg)](https://thehackernews.uk/ai-vuln-protection-d)

# [GitHub Updates actions/checkout to Block Common Pwn Request Attack Patterns](https://thehackernews.com/2026/06/github-updates-actionscheckout-to-block.html)

**Ravie Lakshmanan**Jun 23, 2026Workflow Security / Software Supply Chain

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjcacTEKD_LZFda1wwX5aClbAVOb6mwah2lVUY-jUZwNsrSZGDOFL18LP5zYLX3M2DwKng0qknZ5qo_hMk4q-NExgZv1ozhCy7DJuZwvviZE0sv36PQ2k8Y2emv1KMDFplakFwVzulOFPteWkmVoLO6Le912KAbJGFW0nkqKWHEkwJQLbsGhz5npWO3aJaR/s1700-e365/github-actions.jpg)

GitHub is moving to strengthen software supply chain security by updating "[actions/checkout](https://github.com/actions/checkout)" to block **pwn request attacks** that exploit the risky use of the "pull\_request\_target workflow" trigger to run malicious code with the workflow's full privileges.

Effective June 18, 2026, the latest version of "actions/checkout," the official GitHub action for checking out a repository into the workflow's runner, refuses common pwn request patterns by default. The change is expected to be backported to all currently supported major versions on July 16, 2026.

"Actions/checkout v7 refuses to fetch fork pull request code in [pull\_request\_target](https://docs.github.com/en/actions/reference/workflows-and-actions/events-that-trigger-workflows#pull_request_target) and [workflow\_run](https://docs.github.com/en/actions/reference/workflows-and-actions/events-that-trigger-workflows#workflow_run) workflows (the latter only when workflow\_run.event is a pull\_request\* event)," it [added](https://github.blog/changelog/2026-06-18-safer-pull_request_target-defaults-for-github-actions-checkout/).

The refusal occurs when the pull request is from a fork, and any of the following criteria is met, unless workflow authors explicitly opt out of it by setting the "[allow-unsafe-pr-checkout](https://docs.github.com/en/actions/reference/security/securely-using-pull_request_target)" flag to "true" in "actions/checkout" -

* repository: resolves to the fork pull request' repository
* ref: matches refs/pull/number/head or refs/pull/number/merge
* ref: resolves to a fork pull request's head or merge commit SHA

The change is aimed at preventing the most common form of pwn requests in the Actions ecosystem. As a result, "actions/checkout" will fail for "pull\_request\_target events" from forks with insecure inputs.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/ai-cant-stop-d)

"Pull\_request\_target" is a workflow trigger that's automatically run without requiring manual approval when a pull request is opened or reopened, or when the head branch of the pull request is updated. It's important to note that the event runs in the context of the default branch of the base repository, potentially exposing secrets and a privileged GITHUB\_TOKEN with both read and write permissions.

"Running untrusted code on the pull\_request\_target trigger may lead to security vulnerabilities," GitHub notes in its documentation. "These vulnerabilities include [cache poisoning](https://adnanthekhan.com/2024/05/06/the-monsters-in-your-build-cache-github-actions-cache-poisoning/) and granting unintended access to write privileges or secrets."

The danger arises when a "pull\_request\_target" is combined with "actions/checkout" to download and execute code submitted by an untrusted fork. Should a bad actor submit a pull request containing malicious scripts and the workflow checks out and runs the code, it can allow the attacker to steal the GITHUB\_TOKEN and other secrets, leading to what's [called](https://www.endorlabs.com/learn/pwn-request-threat-a-hidden-danger-in-github-actions) a [pwn request attack](https://securitylab.github.com/resources/github-actions-preventing-pwn-requests/).

"Workflows triggered by pull\_request\_target run with the base repository's GITHUB\_TOKEN, secrets, and default-branch cache access," GitHub said. "Checking out the head of an unreviewed pull request from a fork inside one of these workflows typically lets attacker-controlled code execute with the workflow's full privileges."

In recent months, a number of software chain attacks have weaponized this behavior. The most severe of them was the [compromise](https://thehackernews.com/2026/03/unc6426-exploits-nx-npm-supply-chain.html) of multiple packages associated with the Nx build system as part of a campaign codenamed s1ngularity, as well as the breach of [PostHog](https://thehackernews.com/2025/11/shai-hulud-v2-campaign-spreads-from-npm.html), [TanStack](https://thehackernews.com/2026/05/mini-shai-hulud-worm-compromises.html), and the popular Emacs package, "[kubernetes-el/kubernetes-el](https://thehackernews.com/2026/04/36-malicious-npm-packages-exploited.html)."

"Pull\_request\_target was designed for trusted automation around pull requests, such as labeling, commenting, or applying project metadata," Socket said. "But the checkout step controls which code actually lands in the runner workspace. If it pulls code from a forked pull request, the workflow can end up running attacker-controlled code with the base repository's privileges."

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/vpn-threat-report-m)

That said, the Microsoft-owned subsidiary emphasized that pwn requests triggered via other event types besides pull\_request\_target (e.g., issue\_comment) or through other means, such as git or the GitHub CLI, are out of scope of this change.

"This change only blocks checkouts of the fork pull request head and merge commits," it added. "It does not block checkouts of other untrusted repositories. For example, setting repository: to an unrelated third-party repository is not blocked. Checking out and executing any untrusted code in a privileged event remains a pwn request risk that should be reviewed."

To counter the risk posed by "pull\_request\_target," developers are [advised](https://github.blog/changelog/2025-11-07-actions-pull_request_t...