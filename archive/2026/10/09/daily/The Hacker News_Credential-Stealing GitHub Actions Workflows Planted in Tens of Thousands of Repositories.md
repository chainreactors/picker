---
title: Credential-Stealing GitHub Actions Workflows Planted in Tens of Thousands of Repositories
url: https://thehackernews.com/2026/10/credential-stealing-github-actions.html
source: The Hacker News
date: 2026-10-09
fetch_date: 2026-10-10T07:58:20.870348
---

# Credential-Stealing GitHub Actions Workflows Planted in Tens of Thousands of Repositories

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

[![cybersecurity](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEj2IlqZRz59oSh813xvx6J6LZwp36zTJVBxQ-PeUsJRUAsFcG59ozpg3_EkL6lxZPOdBGD_o8YVUq2CVyutLmT7SgKt513yyCnRmX1J8e5b358cLIneCtSSp46pMvfQ-md9-VagqDnUxxJPuU1CFx7hjpZv75B2E77SI400cPs5PKE4H0uWsGfvEwg_lfzn/s728-nu-rw-lo-l85-e365/prompt-injection-response-d.png)](https://thehackernews.uk/prompt-injection-response-d)

# [Credential-Stealing GitHub Actions Workflows Planted in Tens of Thousands of Repositories](https://thehackernews.com/2026/10/credential-stealing-github-actions.html)

**Ravie Lakshmanan**Oct 09, 2026Supply Chain Attack / Cloud Security

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjoJXBEAVVijhwsYs32WSejvp0sG3ej-Qoi7Z6qHDp8rY5IZENkKOpexrbbU1BNyiCbbB0ZXHjEDL-UYqu7CDpPpoYLiGXkuLCZJTItgP5XeLD_Sb1galPzOGtrFZigEM5CGUbwi9gcL_-XCYY6NKu9j5FiakIWn5s66DZE-OjrLZO3sMGka3YNFvGUecJT/s1700-nu-rw-lo-l85-e365/gitworm.jpg)

Cybersecurity researchers have disclosed details of an ongoing credential-theft campaign that has compromised two high-profile open-source maintainer accounts to push a malicious workflow into over 340 repositories.

"Using the account of Takashi Kitao, author of the 18,400-star game engine pyxel, the attacker pushed a malicious workflow to 27 repositories starting at 13:20 UTC," StepSecurity [said](https://www.stepsecurity.io/blog/ghostaction-returns). "Eight hours later, the account of Henry Wu (henrywoo), the original author of Uber's athenadriver, was used to push the same workflow to 318 repositories in a 16-minute window, 21:10–21:26 UTC."

As of October 9, 2026, Socket [said](https://socket.dev/blog/ghostaction-cloud-credentials) it has identified more than 500 GitHub accounts that committed the malicious workflow to tens of thousands of repositories since October 7, 2026.

The activity has been attributed to **[GhostAction](https://thehackernews.com/2025/09/weekly-recap-drift-breach-chaos-zero.html#:~:text=GhostAction%20Supply%20Chain%20Attack%20Steals%203%2C325%20Secrets)**, a massive supply chain attack campaign that [first came to light](https://www.stepsecurity.io/blog/ghostaction-campaign-over-3-000-secrets-stolen-through-malicious-github-workflows) in September 2025. The activity impacted 817 repositories across 327 GitHub users, resulting in the exfiltration of 3,325 secrets, including PyPI, npm, and DockerHub tokens through compromised developer accounts.

Like before, both accounts have been found to push a workflow named Security Audit ("security-audit.yml") or GitHub Actions Security ("github\_actions\_security.yml"), which are designed to exfiltrate sensitive data to a hard-coded IP address ("193.32.204[.]199") over plain HTTP.

The captured data contains the repository's named GitHub Actions secrets, including CI/CD secrets, and cloud, AI, and SaaS credentials present in the working tree and the entire git history, such as AWS keys, Anthropic, OpenAI, and OpenRouter API keys, and GitHub and GitLab tokens.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/growth-ai-control-d)

The entire attack chain plays out as follows -

* The attacker obtains a maintainer's GitHub credentials, most likely a leaked personal access token (PAT) from infostealer logs or credential dumps.
* The repository's workflow files are scanned for secrets as part of a reconnaissance step.
* A workflow masquerading as a security audit is injected into the default branch under the victim's own identity.
* The embedded payload extracts the data and sends it to an attacker-controlled endpoint via curl.

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjG35D-j0cEU5l7t0JHurwPs-QY53geD3ORGunA9sSnIHFtpYgoF3LaekioeVBLamVISiHGFETaJHVjObbxzuJ0tKTL9R6YBYUzpPXQdjb-G0JHcbsc-BNGToT-ShaFnEhCSfVt3aoTwXZGClgxwJ-385CVCSWkJPVifPvKps8P60GrHvT5jYAVh02DrzjP/s1700-nu-rw-lo-l85-e365/gitcode.png)

"It triggers on workflow\_dispatch and an unfiltered push (any branch, any tag), checks out with fetch-depth: 0, and runs a single 'Audit' step that does four things," StepSecurity added. This includes -

* Append the repository's named secrets found during reconnaissance
* Scan the working tree for 13 credential patterns associated with AWS keys, AI services, source control services, and SaaS and cloud API keys
* Check the entire git history for the same 13 patterns to harvest credentials that may have inadvertently committed to the repository and subsequently deleted
* Pair AWS access key IDs with their matching secret access keys

Earlier this week, GitGuardian [reported](https://blog.gitguardian.com/ghostaction-github-actions-supply-chain-attack-returns/) that the **GhostAction** campaign pushed the malicious workflow to 772 public repositories belonging to 373 GitHub users and organizations between August 31 and September 30, 2026.

The injected workflows target 2,577 secrets, including SSH private keys, Azure credentials, DockerHub and GHCR container registry credentials, database credentials, AWS access keys, FTP credentials, Google Cloud and Firebase credentials, GitHub tokens, Telegram, Slack, and Discord bot tokens, and keys associated with Cloudflare, npm, PyPI, and AI providers.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/network-defense-d)

In at least one case observed on August 30, 2026, the threat actors altered the "kuafuai/DevOpsGPT" repository to embed an XMRig cryptocurrency miner in the project's Docker image. As of writing, no malicious package releases have been published using compromised publishing credentials.

Developers are advised to check their repositories for either of the two GitHub workflows since August 31, 2026, and assume compromise, if present. It's recommended to revoke the compromised GitHub credential, rotate credentials, delete the malicious workflow from all branches, and check forks of the infected repositories.

"The 279 forks in the henrywoo namespace each carry the workflow file. If Actions are enabled, subsequent pushes can trigger credential harvesting," Socket said. "Downstream forks are also at risk if they inherit the malicious workflow, either when newly created or by synchronizing with the affected upstream repository."

"Private forks and downstream mirrors are the most exposed, because private repositories ar...