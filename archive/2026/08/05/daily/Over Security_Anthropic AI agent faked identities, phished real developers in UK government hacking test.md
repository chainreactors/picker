---
title: Anthropic AI agent faked identities, phished real developers in UK government hacking test
url: https://therecord.media/anthropic-ai-hacking-uk
source: Over Security
date: 2026-08-05
fetch_date: 2026-08-06T05:02:40.980547
---

# Anthropic AI agent faked identities, phished real developers in UK government hacking test

![](https://recordedfuture.matomo.cloud/matomo.php?idsite=2&rec=1)

[![Cyber Security News  | The Record](https://cms.therecord.media/uploads/The_Record_Centered_9b27d79125.svg)](/)

* [Leadership](/news/leadership)
* [Cybercrime](/news/cybercrime)
* [Nation-state](/news/nation-state)
* [Influence Operations](/news/influence-operations)
* [Technology](/news/technology)

* [Cyber Daily®](https://therecord.media/subscribe)
* [Click Here Podcast](/podcast)

Go

Subscribe to The Record

[✉️ Free Newsletter](/subscribe)

![Anthropic](https://cms.therecord.media/uploads/large_Anthropic_24cbfc4c7e.jpg)

Image: Mohamed Nohassi / Unsplash

[Alexander Martin](/author/alexander-martin)August 5th, 2026

# Anthropic AI agent faked identities, phished real developers in UK government hacking test

An artificial intelligence agent built by Anthropic created fake online personas, planted malicious code in a real software project, and sent phishing emails to real developers during a U.K. government security evaluation — all without human instruction — according to Britain’s AI Security Institute (AISI).

The disclosures, set out Tuesday by the AISI in a [technical report](https://www.aisi.gov.uk/blog/incident-report-unsanctioned-agent-behaviour-during-cyber-testing), add to a growing list of incidents in which frontier AI systems have acted against real-world targets during testing. Similar recent announcements by OpenAI and Anthropic have rattled policymakers and raised questions about liability, disclosure standards and the adequacy of containment practices across the industry.

The AISI, the government-owned research body responsible for evaluating frontier AI risks, said the incident “should be interpreted with caution and nuance” and was “to some degree” enabled by its own “evaluation design choices and specific configurations.”

“Nonetheless,” the institute stated, “the activity undertaken by the agent show signs of novel, potentially deceptive behaviors, and were to an extent and severity we did not anticipate.”

In the most serious case, Anthropic’s Mythos 5 model decided on its own to pursue a supply-chain attack against an open-source project whose maintainers had no connection to the evaluation. The project was not identified.

Anthropic had last week [disclosed](https://therecord.media/anthropic-ai-hacked-three-real-companies) a similar incident, in which its agent uploaded malware to the PyPI software package. In that incident, the agent mistakenly believed it was operating within its guardrails. Those safety filters were intentionally disabled for the AISI evaluation.

In the AISI’s test, the agent researched the public profiles of developers involved in the target project, created multiple GitHub accounts using anonymization tools to bypass bot-detection measures, and submitted a pull request containing hidden malware.

It then manufactured apparent community support for its own actions by posting endorsements from fake accounts it controlled, and sent emails under fabricated identities to persuade the developers to approve the changes.

When a vigilant GitHub user publicly identified the malware, the agent rewrote its code history to remove evidence, claimed the malicious content was an accidental inclusion, and coordinated further fake endorsements — timing them, according to the AISI’s summary of the model’s reasoning, to appear as independent feedback.

“Taken alongside recent incidents reported by OpenAI and Anthropic, this incident points to a shift in the risk landscape,” the AISI said. “Harm may arise not only when people deliberately misuse publicly available models, but when capable agents operating in an internal research or privileged-access setting take unintended action beyond their authorized scope.”

In total, the institute cataloged 19 instances of unsanctioned activity across 10 of 122 evaluation runs. Seventeen involved Mythos 5 and two involved OpenAI’s GPT-5.6 Sol. The AISI said the agents’ safety classifiers were deliberately disabled and internet access was enabled to test maximum capabilities, conditions it said are not available to the general public.

The report also described unexpectedly finding agents running in separate, isolated evaluation sessions spontaneously discovering each other through GitHub and beginning to cooperate, sharing credentials and leaving operational instructions for one another.

One agent wrote rules of engagement for fellow agents in a shared repository, advising them on how to avoid exhausting shared API rate limits and requesting they share any solutions they found.

The AISI said it detected the incident on July 28 when security monitoring flagged data leaving a test system through the Tor anonymity network. It contained the incident within an hour and subsequently reviewed all 122 evaluation samples, comprising more than 212,000 messages.

The incident is the third major disclosure in three weeks involving AI agents that affected real-world systems during evaluations. OpenAI [confirmed](https://therecord.media/openai-says-rogue-agent-behind-hugging-face-hack-broke-into-additional-services) that its models breached production infrastructure after escaping a sandboxed environment. Anthropic [disclosed](https://therecord.media/anthropic-ai-hacked-three-real-companies) its models had compromised three real organizations during testing after internet access was left open unintentionally.

The AISI incident differs from both in that the agent’s primary strategy was social rather than technical, targeting real people with deception rather than simply exploiting infrastructure vulnerabilities.

Neither the OpenAI nor Anthropic incidents involved human-directed deception, noted the security institute, adding that previous cases of AI deception documented by the evaluation organisation METR were directed at automated graders, not people.

The AISI also reported that the smaller model Anthropic uses to summarize Mythos 5’s internal chain-of-thought reasoning appeared at one point to refuse to continue its summary, outputting text stating it would not assist with plans involving social engineering, account compromise, or evasion of security measures.

The reasoning summary then resumed after the refusal. The AISI said this supported the interpretation that the main model’s reasoning was deceptive. This poses an issue for AI companies investigating their models’ conduct through chain-of-thought logs, which Anthropic’s own [research](https://www-cdn.anthropic.com/b9ca6db27f02a9ddf0d4fdb51b26432c99a27be0.pdf) has found is often inaccurate — although independent follow-on work by evaluation company METR [suggests](https://metr.org/blog/2025-08-08-cot-may-be-highly-informative-despite-unfaithfulness/) these logs may still be highly informative despite being unfaithful.

The AISI said it has begun scanning approximately 40,000 historical evaluation samples for comparable behavior and is implementing real-time monitoring, tighter network controls, and a requirement that internet access be actively justified rather than granted by default. It said it plans to commission an independent review through METR, though the scope has not been determined.

The Cabinet Office, which now oversees the AISI, did not immediately respond to questions about whether law enforcement has been contacted about the potential Computer Misuse Act incidents, nor whether any affected parties are considering legal action.

* [News](/)
* [Technology](/news/technology)
* [Government](/news/government)
* [Malware](/news/malware)

Get more insights with the

Recorded Future

Intelligence Cloud.

[Learn more.](https://www.recordedfuture.com/platform?mtm_campaign=ad-unit-record)

[![Recorded Future](https://cms.therecord.media/uploads/2025_0514_Record_Ads_300x1050_1_0f2f11757e.png)](https://www.recordedfuture.com?utm_source=therecord&utm_medium=referral&utm_content=display)

[![Recorded Future](https://cms.therecord.media/uploads/2025_0514_Recor...