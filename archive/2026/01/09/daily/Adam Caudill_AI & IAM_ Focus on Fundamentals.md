---
title: AI & IAM: Focus on Fundamentals
url: https://adamcaudill.com/2026/01/09/ai-iam-focus-on-fundamentals/?utm_source=atom_feed
source: Adam Caudill
date: 2026-01-09
fetch_date: 2026-01-10T03:31:50.468749
---

# AI & IAM: Focus on Fundamentals

# [Adam Caudill](https://adamcaudill.com/)

* [Exposera](https://exposera.com/u/adamcaudill "Exposera")

*Security Leader, Researcher, Developer, Writer, & Photographer*

* [Home](https://adamcaudill.com/)
* [Blog](https://adamcaudill.com/blog/)
* [Research](https://adamcaudill.com/research/)
* [Speaking](https://adamcaudill.com/speaking/)
* [Photography](https://adamcaudill.com/photography/)
* [Writing](https://adamcaudill.com/writing/)
* [About](https://adamcaudill.com/about/)

# AI & IAM: Focus on Fundamentals

On the need to address fundamental issues when integrating new technologies.

Today
|
9 minute read
|
[News](https://adamcaudill.com/categories/news)

A recent article, *The Future of Cybersecurity Includes Non-Human Employees*[1](#fn:1), discussed the growing need to manage access granted to the rapidly expanding number of AI agents being deployed in companies. This is a deeply important topic, and particularly timely, as many are facing this challenge today. While I do want to address that topic, I also want to address how this is being framed.

Aside from leaning into an inflammatory tone with the use of “Non-Human Employees” as part of the title of the piece, there’s a deeper issue I see with how this is being framed, and it’s also related to AI. Importantly, this is far from unique to this article, but a trend across discussions of AI (and other new & emerging technologies). For the pragmatic security practitioner, a clear understanding of this framing device and the danger of accepting it unchallenged is of particular import.

Let’s take a closer look.

## Reframing for AI [#](#reframing-for-ai)

“Everything old is new again,” a phrase first uttered by Jonathan Swift, or Winston Churchill, or maybe it was Mark Twain[2](#fn:2) - whoever it was, it’s a simple phrase that’s apt as ever. With each substantial new technology, every existing challenge, every solved problem, every known risk gets reframed and repackaged and relabelled. For marketing teams, this is a fantastic opportunity to stake a claim on new territory, to assert leadership in solving some critical issue, to announce their solutions for these “new” problems.

AI is here, and everything is new again.

> Non-human employees are becoming the future of cybersecurity, and enterprises need to prepare accordingly. As organizations scale Artificial Intelligence (AI) and cloud automation, there is exponential growth in Non-Human Identities (NHIs), including bots, AI agents, service accounts and automation scripts. In fact, 51% of respondents in ConductorOne’s 2025 Future of Identity Security Report said the security of NHIs is now just as important as that of human accounts. - *The Hacker News*

Here, in these first two sentences, my main objections to the framing are already clear.

Many of the challenges and risks aren’t actually new at all; they are the same as those that we in the security industry have been addressing for years. It’s new names for an old problem. They call it “Non-Human Identities” - for the last few decades this was called a service account. A new name for an old and well understood thing.

The danger of this framing is that it seeks to leverage new names and the association with a new technology to separate it from the well-established and well-understood approaches that have been refined over years of diligent work and careful analysis. This is great when you can sell something that addresses the problem. It’s the only thing this reframing is good for.

In reality, service accounts for AI are effectively the same as service accounts for any other form of automation[3](#fn:3). As such, the mitigations for service accounts apply to agentic AI, and should be applied. This includes all of the controls that should always be applied, such as:

* Least Privilege: As always, accounts should have the tightest possible set of privileges to complete the task, no more.
* Separation of Concerns: Credentials and other secrets should be used for a single well-defined purpose, and nothing else. They should not be re-used for other processes or systems.
* Credential Lifetime: Credentials should have the shortest possible lifetime, and be easily rotated.
* Actionable Logging & Alerts: All automation should have clear logs, and alerts for unusual activity.
* IP & Location Restrictions: Credentials used for automation should only be permitted within a known environment, any use outside of this controlled environment, should trigger accounts being disabled and immediate alerts.
* Leak Detection: Logs and other automation artefacts should be automatically checked for secrets, authentication tokens, and other sensitive material.
* Clear Ownership: The automated processes, data, and credential should have clear documented owners, with clear responsibilities – especially should issues arise.
* Human Validation: When taking substantial actions, actions that can’t be reverted, or otherwise have significant impact, a human should be in the loop to validate that the action is intended and the results are desired.

These apply to agentic AI just as much as they apply to any other service accounts. In other words: the key is to focus on the fundamentals. Regardless of the underlying technology, the key to achieving meaningful security is to focus on the fundamentals first, *then* moving on to looking at the unique challenges.

## Non-Deterministic Automation [#](#non-deterministic-automation)

Agentic AI and other forms of LLM-based automation are fundamentally similar to other forms of automation, though there is a substantial point that is critical to understand: it’s non-deterministic. If I automate a process using Python, the process is fixed, and the behaviour is deterministic – which is to say, it will always do the same thing[4](#fn:4). With AI, it will by its very nature, do something different each time it’s used[5](#fn:5).

It is this factor that presents the first meaningful difference between traditional automation and LLM-based automation. As the automation can’t be assumed to produce a consistent result, and may misbehave in truly unpredictable ways, this introduces some new risks that need to be addressed.

* AI may attempt to perform actions beyond the intended scope, making the limitation of permissions particularly important. Implementing the principle of least privilege and maintaining strict separation of concerns are critical to avoid unintended activities.
* AI may send secrets to search engines or other third-parties, making it important to restrict traffic and build deeper monitoring & leak detection[6](#fn:6) into the process. This results in short credential lifetimes and IP & location restrictions being more important than normal[7](#fn:7). It also shows the value of integrating proxies for web traffic, and wrappers & frameworks for code, to provide additional controls directly in the automation.
* AI is subject to prompt injection, intentional or otherwise, which can cause radical departures from the intended behaviour, and thus any credentials or access the automation has can be abused in ways that would entirely defy expectations. This results in all input being potentially dangerous, and thus putting secrets at risk. This furthers the need to take the most restrictive and cautious approach possible.
* AI agents can take unexpected paths to achieve results, as such, it’s critical that the permissions granted don’t include the ability to mint new tokens, assign permissions, or assume other roles. It would not be surprising to see an AI agent attempt this to circumvent an access control that resulted in an error message.
* *et cetera*. This list could grow, though there is a clear pattern, and it’s that pattern that matters.

There are a number of unique risks that come with giving agentic AI credentials and access to systems, though all of them are addressed by existing high-level controls. Yes, the details of the controls, and the best approach to effectua...