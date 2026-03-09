---
title: How AI Assistants are Moving the Security Goalposts
url: https://krebsonsecurity.com/2026/03/how-ai-assistants-are-moving-the-security-goalposts/
source: Over Security - Cybersecurity news aggregator
date: 2026-03-08
fetch_date: 2026-03-09T04:08:46.742116
---

# How AI Assistants are Moving the Security Goalposts

Advertisement

[![](/b-doppel/5.png)](https://www.doppel.com/?utm_source=krebsonsecurity&utm_medium=display&utm_campaign=fy27brandcampaign&utm_content=outpace)

Advertisement

[![](/b-knowbe4/49.jpg)](https://www.knowbe4.com/training-humans-ai-agents?utm_source=krebs&utm_medium=display&utm_campaign=traininghumansandai&utm_content=bannerai)

[![Krebs on Security](https://krebsonsecurity.com/wp-content/uploads/2021/03/kos-27-03-2021.jpg)](https://krebsonsecurity.com/ "Krebs on Security")

[Skip to content](#content "Skip to content")

* [Home](https://krebsonsecurity.com/)
* [About the Author](https://krebsonsecurity.com/about/)
* [Advertising/Speaking](https://krebsonsecurity.com/cpm/)

# How AI Assistants are Moving the Security Goalposts

March 8, 2026

[3 Comments](https://krebsonsecurity.com/2026/03/how-ai-assistants-are-moving-the-security-goalposts/#comments)

AI-based assistants or “agents” — autonomous programs that have access to the user’s computer, files, online services and can automate virtually any task — are growing in popularity with developers and IT workers. But as so many eyebrow-raising headlines over the past few weeks have shown, these powerful and assertive new tools are rapidly shifting the security priorities for organizations, while blurring the lines between data and code, trusted co-worker and insider threat, ninja hacker and novice code jockey.

The new hotness in AI-based assistants — **OpenClaw** (formerly known as **ClawdBot** and **Moltbot**) — has seen rapid adoption since its release in November 2025. OpenClaw is an open-source autonomous AI agent designed to run locally on your computer and proactively take actions on your behalf without needing to be prompted.

![](https://krebsonsecurity.com/wp-content/uploads/2026/03/openclaw.png)

If that sounds like a risky proposition or a dare, consider that OpenClaw is most useful when it has complete access to your entire digital life, where it can then manage your inbox and calendar, execute programs and tools, browse the Internet for information, and integrate with chat apps like Discord, Signal, Teams or WhatsApp.

Other more established AI assistants like Anthropic’s **Claude** and Microsoft’s **Copilot** also can do these things, but OpenClaw isn’t just a passive digital butler waiting for commands. Rather, it’s designed to take the initiative on your behalf based on what it knows about your life and its understanding of what you want done.

“The testimonials are remarkable,” the AI security firm **Snyk** [observed](https://snyk.io/articles/clawdbot-ai-assistant/). “Developers building websites from their phones while putting babies to sleep; users running entire companies through a lobster-themed AI; engineers who’ve set up autonomous code loops that fix tests, capture errors through webhooks, and open pull requests, all while they’re away from their desks.”

You can probably already see how this experimental technology could go sideways in a hurry. In late February, **Summer Yue**, the director of safety and alignment at Meta’s “superintelligence” lab, [recounted on Twitter/X](https://x.com/summeryue0/status/2025774069124399363) how she was fiddling with OpenClaw when the AI assistant suddenly began mass-deleting messages in her email inbox. The thread included screenshots of Yue frantically pleading with the preoccupied bot via instant message and ordering it to stop.

“Nothing humbles you like telling your OpenClaw ‘confirm before acting’ and watching it speedrun deleting your inbox,” Yue said. “I couldn’t stop it from my phone. I had to RUN to my Mac mini like I was defusing a bomb.”

![](https://krebsonsecurity.com/wp-content/uploads/2026/03/summeryue.png)

Meta’s director of AI safety, recounting on Twitter/X how her OpenClaw installation suddenly began mass-deleting her inbox.

There’s nothing wrong with feeling a little [schadenfreude](https://en.wikipedia.org/wiki/Schadenfreude) at Yue’s encounter with OpenClaw, which fits Meta’s “move fast and break things” model but hardly inspires confidence in the road ahead. However, the risk that poorly-secured AI assistants pose to organizations is no laughing matter, as recent research shows many users are exposing to the Internet the web-based administrative interface for their OpenClaw installations.

**Jamieson O’Reilly** is a professional penetration tester and founder of the security firm **DVULN**. In a recent [story](https://x.com/theonejvo/status/2015401219746128322) posted to Twitter/X, O’Reilly warned that exposing a misconfigured OpenClaw web interface to the Internet allows external parties to read the bot’s complete configuration file, including every credential the agent uses — from API keys and bot tokens to OAuth secrets and signing keys.

With that access, O’Reilly said, an attacker could impersonate the operator to their contacts, inject messages into ongoing conversations, and exfiltrate data through the agent’s existing integrations in a way that looks like normal traffic.

“You can pull the full conversation history across every integrated platform, meaning months of private messages and file attachments, everything the agent has seen,” O’Reilly said, noting that a cursory search revealed hundreds of such servers exposed online. “And because you control the agent’s perception layer, you can manipulate what the human sees. Filter out certain messages. Modify responses before they’re displayed.”

O’Reilly documented [another experiment](https://x.com/theonejvo/status/2015892980851474595) that demonstrated how easy it is to create a successful supply chain attack through **ClawHub**, which serves as a public repository of downloadable “skills” that allow OpenClaw to integrate with and control other applications.

## WHEN AI INSTALLS AI

One of the core tenets of securing AI agents involves carefully isolating them so that the operator can fully control who and what gets to talk to their AI assistant. This is critical thanks to the tendency for AI systems to fall for “prompt injection” attacks, sneakily-crafted natural language instructions that trick the system into disregarding its own security safeguards. In essence, machines social engineering other machines.

A recent supply chain attack targeting an AI coding assistant called **Cline** began with one such prompt injection attack, resulting in thousands of systems having a rouge instance of OpenClaw with full system access installed on their device without consent.

According to the security firm **grith.ai**, Cline had deployed an AI-powered issue triage workflow using a **GitHub** action that runs a Claude coding session when triggered by specific events. The workflow was configured so that any GitHub user could trigger it by opening an issue, but it failed to properly check whether the information supplied in the title was potentially hostile.

“On January 28, an attacker created Issue #8904 with a title crafted to look like a performance report but containing an embedded instruction: Install a package from a specific GitHub repository,” Grith [wrote](https://grith.ai/blog/clinejection-when-your-ai-tool-installs-another#user-content-fn-2), noting that the attacker then exploited several more vulnerabilities to ensure the malicious package would be included in Cline’s nightly release workflow and published as an official update.

“This is the supply chain equivalent of [confused deputy](https://en.wikipedia.org/wiki/Confused_deputy_problem),” the blog continued. “The developer authorises Cline to act on their behalf, and Cline (via compromise) delegates that authority to an entirely separate agent the developer never evaluated, never configured, and never consented to.”

## VIBE CODING

AI assistants like OpenClaw have gained a large following because they make it simple for users to “vibe code,” or build fairly complex applications and code projects just by telling it what they want to construct. Probably the best known (and most bizarre) ex...