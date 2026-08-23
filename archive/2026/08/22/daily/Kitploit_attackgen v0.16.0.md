---
title: attackgen v0.16.0
url: https://kitploit.com/en/posts/github-mrwadams-attackgen-v0160
source: Kitploit
date: 2026-08-22
fetch_date: 2026-08-23T02:57:04.840678
---

# attackgen v0.16.0

[Skip to content](#main-content)

[![Kitploit](/_next/image?url=%2Flogo.png&w=64&q=75)KITPLOIT](/en)[Tools](/en/tools)[Blog](/en/blog)Categories

EN

[Submit](/en/submit)

[Tools](/en/tools)[Blog](/en/blog)Categories

[Submit](/en/submit)

EN

Hacking, PenTest, and Cybersecurity Tools for Your Security Arsenal!

[Back to updates](/en/updates)

![](https://assets.kitploit.com/production/public/tools/6464/58525fd72c40f62c39a5defdd2565e26c374c60d481898a3abcd8d2b65f92b52.png)

New releaseAug 22, 2026

# attackgen v0.16.0

AttackGen is a cybersecurity incident response testing tool that leverages the power of large language models and the comprehensive MITRE ATT&CK framework. The tool generates tailored incident response scenarios based on user-selected threat actor groups and your organisation's details.

Share

# AttackGen

AttackGen is a cybersecurity incident response testing tool that leverages the power of large language models and the comprehensive MITRE ATT&CK and ATLAS frameworks. The tool generates tailored incident response scenarios based on user-selected threat actor groups, AI attack case studies, and your organisation's details.

## Table of Contents

* [Star the Repo](#star-the-repo)
* [Features](#features)
* [Releases](#releases)
* [Requirements](#requirements)
* [Installation](#installation)
* [LangSmith Setup](#langsmith-setup)
* [Data Setup](#data-setup)
* [Running AttackGen](#running-attackgen)
* [MCP Server](#mcp-server)
* [Agent Skills](#agent-skills)
* [Usage](#usage)
* [Security Best Practices](#security-best-practices)
* [Contributing](#contributing)
* [Licence](#licence)

## Star the Repo

If you find AttackGen useful, please consider starring the repository on GitHub. This helps more people discover the tool. Your support is greatly appreciated! ⭐

## Features

* Generates unique incident response scenarios based on chosen threat actor groups or ATLAS case studies.
* Allows you to specify your organisation's size and industry for a tailored scenario.
* Supports MITRE ATT&CK Enterprise, ICS (Industrial Control Systems), and ATLAS (Adversarial Threat Landscape for AI Systems) frameworks.
* Displays a detailed list of techniques used by the selected threat actor group or case study.
* Create custom scenarios based on a selection of ATT&CK or ATLAS techniques.
* Use scenario templates to quickly generate custom scenarios based on common types of cyber incidents, including AI/ML-specific attack patterns.
* Generate **AI Insider Threat Scenarios** - incident response exercises in which a frontier AI agent deployed inside your organisation behaves as an insider threat, based on the threat model from [*Actions Speak Louder Than Tokens: An Insider Threat Model for Frontier AI Agents*](https://ai-insider-threat.matt-adams.co.uk). Scenarios are shaped by the agent's deployment archetype (autonomy level), threat category, STRIDE threats, and an optional free-text scenario seed.
* AttackGen Assistant - a chat interface for updating and/or asking questions about generated scenarios.
* Capture user feedback on the quality of the generated scenarios.
* Downloadable scenarios in Markdown format.
* Use the OpenAI API, Anthropic API (Claude models), Google AI API, Mistral API, Groq API, or any custom OpenAI-compatible endpoint (Ollama, LM Studio, Azure OpenAI, OpenRouter, etc.) to generate incident response scenarios. All providers are routed through [LiteLLM](https://github.com/BerriAI/litellm) behind a single internal wrapper, so adding a new model is a one-line change.
* Available as a Docker container image for easy deployment.
* Optional integration with [LangSmith](https://docs.smith.langchain.com/) for powerful debugging, testing, and monitoring of model performance.
* Secure credential management using .env file for API keys and secrets.

![AttackGen Screenshot](https://assets.kitploit.com/production/public/readmes/6464/58525fd72c40f62c39a5defdd2565e26c374c60d481898a3abcd8d2b65f92b52.png)

## Releases

### v0.15

| What's new? | Why is it useful? |
| --- | --- |
| Evaluation Environment Escape Preset & Scenario Seed | - Rehearse a Specific Incident: A new AI insider-threat template rehearses an evaluation agent reaching real systems from an environment assumed to be isolated — forcing containment, credential rotation, third-party notification and evidence preservation. It covers the July 2026 disclosures of eval agents escaping their sandboxes, where the isolation boundary was *assumed* rather than enforced.  - Templates Now Reach the Prompt: Quick-start templates previously only pre-filled the page's widgets and never influenced the generated scenario. They now carry a narrative `brief` and the `required_decisions` the Discussion Questions must force, both threaded into the prompt — so a template produces a usable timed tabletop rather than a grab-bag of questions. This splits them into two classes: the six original **archetype** templates set decisions only, so the model invents the premise and re-running one yields a fresh exercise for the same threat profile; **incident** templates also set a brief, pinning the situation.  - Free-Text Scenario Seed: An optional seed box on the AI Insider Threat page steers the narrative on any scenario. Selecting a template pre-fills it, and you can edit it or write your own from scratch.  - Taxonomy Extended to 27 Threats / 6 Categories: Adds a sixth threat category (**Containment & Third-Party Impact**) and four STRIDE threats the exercise turns on — `S5` reusable workload credential replay, `R4` agent-side telemetry suppression, `I5` third-party & downstream compromise, and `E5` containment boundary assurance failure. AttackGen now *extends* the published threat model rather than mirroring it.  - Templates Usable Over MCP: `get_ai_insider_prompt` and `generate_ai_insider_scenario` accept `template=` and `scenario_seed=`, and `list_ai_insider_options` returns each template with the selections and brief it applies — so a client can pick a preset on merit and call with just a template, industry and company size. Previously the template names were listed but no tool accepted one. |
| attackgen-tabletop Skill: AI Insider-Threat Path | - A Second Exercise Path: The [Agent Skill](https://github.com/mrwadams/attackgen/blob/HEAD/skills/) now builds a tabletop from the AI insider-threat model as well as from a MITRE kill chain. Pick a quick-start template (or a deployment archetype and threat categories) and it turns `get_ai_insider_prompt`'s payload into an MSEL.  - Same Shape, Different Spine: The exercise keeps the same six sections, but the kill-chain table becomes an agent profile and STRIDE threat scope, the detection scorecard is judged against the deployment archetype's detection posture — so the rows that *wouldn't* fire become the finding — and the template's required decisions become mandatory discussion questions.  - Path Chosen for You: The skill's description now triggers on rogue-agent phrasing, so asking for an "AI insider threat tabletop" reaches the right path. An external actor with AI-accelerated tradecraft stays on the MITRE path.  - Response, Not Exploit: Both paths are explicitly bounded to rehearsing the decisions a response team must make — no exploit code, payloads or real unpatched vulnerabilities — and the AI path attributes agent behaviour to configuration, access and objective rather than human motive. |
| Fix: MCP AI-Insider Prompts Dropped the Agent Capabilities | - Same Template, Same Prompt: The frontier-agent capability block — the benchmark-grounded lines that make an AI insider scenario credible — was omitted from every `get_ai_insider_prompt` / `generate_ai_insider_scenario` call that didn't name `capabilities` explicitly. No template supplies them, so the argument fell through to empty and the prompt substituted a generic "assume a capable frontier coding agent" line, while page 3 sent all four for the same template.  - Defaults Now Match the App: Omitting `capabiliti...