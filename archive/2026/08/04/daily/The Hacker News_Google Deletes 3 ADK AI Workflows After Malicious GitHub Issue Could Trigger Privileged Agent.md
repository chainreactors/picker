---
title: Google Deletes 3 ADK AI Workflows After Malicious GitHub Issue Could Trigger Privileged Agent
url: https://thehackernews.com/2026/08/google-deletes-3-adk-ai-workflows-after.html
source: The Hacker News
date: 2026-08-04
fetch_date: 2026-08-05T04:59:45.761121
---

# Google Deletes 3 ADK AI Workflows After Malicious GitHub Issue Could Trigger Privileged Agent

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

![cybersecurity](data:image/svg+xml;base64...)

# [Google Deletes 3 ADK AI Workflows After Malicious GitHub Issue Could Trigger Privileged Agent](https://thehackernews.com/2026/08/google-deletes-3-adk-ai-workflows-after.html)

**Swati Khandelwal**Aug 04, 2026AI Security / DevSecOps

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhLUUlqxE9AYL9PyFAlWMsG9czDcrU9p2kMUsumVIYx5SnlMAO0z-n_weUWeX-CiMHQBbkGK1lV-78vp003-bAeRP4gQRyGXlq5blzx5dJdd9zFttd2tjhGlNUFLNk-6ro9GfXMkRCFVLs-ex3gWHoJh-87sZifOeTKohLNoypvvqLUUPLkGUsjKXfAj7A/s1700-e365/google.gif)

Google deleted three AI agent workflows from its [Agent Development Kit (ADK)](https://thehackernews.com/2026/06/cordyceps-cicd-flaws-expose-300-github.html) Python repository. Pillar Security showed that a public GitHub issue could manipulate a triage agent into triggering a privileged code-fixing agent.

The researchers said the public agent could be prompt-injected into posting `/adk-issue-fix` as `adk-bot`. They identified the bot as a collaborator, so that comment satisfied the privileged workflow's owner, member, or collaborator gate. The [trusted bot identity](https://thehackernews.com/2026/06/claude-code-github-action-flaw-let-one.html) became the authorization bridge.

The team demonstrated arbitrary code execution on the continuous integration (CI) runner and exfiltration of the bot personal access token (PAT). The privileged job also held a Google API key and a Google Cloud service-account credential. Its researcher-controlled proof-of-concept attacks do not identify in-the-wild exploitation or a compromised ADK release.

The exposed component was the repository automation, not a flaw in the distributed ADK Python package. For similar repositories, Pillar recommends separate bot identities, narrower token and tool scopes, and an authorization signal that untrusted text cannot generate.

The Hacker News contacted Google about the bot token's scopes, service-account permissions, and exploitation evidence, and Pillar Security about the proof-of-concept environment and credential access. Both responses were pending at the time of writing.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/threatlocker-d)

The attack path began in the public [`issue-analyze.yml` workflow](https://github.com/google/adk-python/blob/v2.2.0/.github/workflows/issue-analyze.yml), which ran automatically whenever an issue was opened. It authenticated with `ADK_GCP_SA_KEY`, supplied `ADK_TRIAGE_AGENT` and `GOOGLE_API_KEY` to Google's [Antigravity coding agent](https://thehackernews.com/2026/04/google-patches-antigravity-ide-flaw.html), and posted the generated analysis as a comment using the bot account.

A separate [`issue-fix.yml` workflow](https://github.com/google/adk-python/blob/v2.2.0/.github/workflows/issue-fix.yml) listened for `/adk-issue-fix` comments and restricted execution to an owner, member, or collaborator. The gate checked who posted the command, not whether an outsider had manipulated the trusted account behind it.

The privileged job declared write access to issues, repository contents, and pull requests. [Those settings applied to GitHub's generated `GITHUB_TOKEN`](https://docs.github.com/actions/using-workflows/workflow-syntax-for-github-actions#permissions), not the `ADK_TRIAGE_AGENT` PAT the job actually used.

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhXDO4btO1lmEH9MwgGUjls2gGbqg-CxFMVE6kEeMCi0sx4oRx0GG5lZwMfPoxO-lSfhv86JrsegF72eKRxiC_yYHg8kdd3440VHd6ATSuvsDZ9tPWcMBPqB9bKxnUVsj0ksILwDTupfrHz3_UJ29XNBYyGAEbU1cSFkJFOKuN0yyMsxN5-wFQFYzzQ0F4/s1700-e365/6a70809f2c071c0335958d4c_Two%20Chains%2C%20one%20identity%20failure.png)

[Pillar said](https://www.pillar.security/blog/ill-just-call-you-agent-to-agent-privilege-boundary-failures-in-ci-cd-on-googles-adk-repository) the PAT's exact scopes were not public. The job checked out the repository with the PAT, authenticated to Google Cloud, and ran the agent with the PAT and API key in its environment. The workflow was designed to edit code, create an `adk-bot` fork, push a branch, and open a pull request. A [bot-generated pull request from June 4](https://github.com/google/adk-python/pull/5968) shows that the automation was operating in the repository.

The [runner](https://github.com/google/adk-python/blob/v2.2.0/scripts/run_antigravity.py) rejected shell metacharacters and allowed only commands whose first token was `gh` or `git`. But the script enabled `CapabilitiesConfig()`, which Google's [Antigravity SDK documentation](https://github.com/google-antigravity/antigravity-sdk-python) says turns on all tools, including writes. The agent could therefore write a payload and make an allowed Git command execute it through a [custom hook path](https://thehackernews.com/2026/04/google-fixes-cvss-10-gemini-cli-ci-rce.html).

[Git's documentation](https://git-scm.com/docs/githooks) confirms that hooks are executable programs and that `core.hooksPath` can redirect Git to another directory. The allowlist narrowed command syntax, but file writes and Git still left a route to code execution.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/corelight-d)

Public artifacts do not establish whether the PAT could push directly to the main branch. Pillar said Google told it the service account had Vertex AI access in a dedicated GitHub-management project; broader permissions were not disclosed. Pillar's report describes runner execution and credential exposure, but the public record does not establish the downstream repository or cloud reach of those credentials.

The report also described an earlier chain that could create a false review trail through privileged Gemini workflows, but a maintainer still had to merge the pull request.

Google's [removal commit](https://github.com/google/adk-python/commit/66730e9d87915a9371b10ecf3ae9a0c37c4aba04) says the workflows processed untrusted issue and pull-request content with broad repository credentials. Google deleted `issue-analyze.yml`, `issue-fix.yml`, and `pr-analyze.yml` in a patch whose metadata carries a June 9, 2026 author date.

Pillar said it verified the workflows were absent on July 2 and that Google confirmed the issue fixed on July 21. A [check by The Hacker News](https://github.c...