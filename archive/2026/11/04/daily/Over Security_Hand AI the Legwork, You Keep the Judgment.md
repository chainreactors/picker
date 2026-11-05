---
title: Hand AI the Legwork, You Keep the Judgment
url: https://www.intel471.com/blog/hand-ai-the-legwork-you-keep-the-judgment
source: Over Security
date: 2026-11-04
fetch_date: 2026-11-05T08:44:52.150443
---

# Hand AI the Legwork, You Keep the Judgment

[![Intel 471](https://cdn.sanity.io/images/fo9xc2x1/production/93fea1393c1c41cc700e939325848b7117804e8f-678x209.png?h=76&fm=webp&fit=max&auto=format)](/)PlatformUse Cases[Why Intel 471](/why-intel-471)ResourcesCompany

Search[Send a request](/company/contact)

# Hand AI the Legwork, You Keep the Judgment

Nov 4, 2026

![](https://cdn.sanity.io/images/fo9xc2x1/production/8e17f8259ee64d48b497a899616a4a8af4952a7e-1440x730.png?w=1920&h=800&fm=jpg&q=95&fit=crop&crop=center&auto=format)

*CTI teams serving many stakeholders can reclaim time when their AI agents work within guardrails: citing sources, flagging gaps and showing reasoning analysts can check.*

#### **Another day at the desk**

A week that isn’t disrupted by breaking threats is the outlier. October served up a trio of critical events: PHP2Shell, Brotli/HTTP2Shell and the eMudhra certificate authority key compromise.

When these events happen, the first question CTI analysts get is: “Have you heard about this?” Beyond answering “yes,” analysts need to say whether it matters to the organization, what they know and do not know, and provide a judgment stakeholders can act on.

[PHP2Shell](https://www.wiz.io/blog/php2shell-php-rce) shows why prioritization is getting harder. Researchers found the flaws with the help of frontier AI models, a sign of how quickly AI is accelerating vulnerability discovery. After the Oct. 21 disclosure, dozens of proof-of-concept exploits flooded GitHub, many apparently AI-generated. Exploitation attempts that had begun days before disclosure continued. Was there a working exploit, and how likely was imminent mass exploitation? Analysts had to advise leadership, infrastructure owners and the SOC in the same week HTTP2Shell and the eMudhra compromise demanded their attention too.

Hours go into research before judgment can happen. Analysts search across tools, read multiple reports, compare timestamps, check whether claims are corroborated and stitch fragments into a brief their stakeholders can use, whether that’s an executive report or a machine-readable detection query for SOC tools. That legwork is necessary for analysts to deliver their real value: judgment about what the evidence means for the business, how confident they are and what should happen next. That means putting intelligence in the context of their organization’s technology, controls and processes, and their stakeholders’ priorities.

Every new stakeholder means more questions and less time. CTI teams need tools that can take on the legwork, so analysts can stay focused on the judgment only they can provide.

#### **CTI teams turn to agents**

The [2026 SANS CTI Survey](https://www.intel471.com/blog/making-the-business-case-for-your-cti-budget) found that 45% of organizations already use AI in their CTI programs, most commonly for data summarization and report writing. But respondents stressed that analysts must keep oversight of high-stakes decisions, where accuracy and calibrated confidence matter. That caution is well founded. LLMs are non-deterministic, meaning they can give different answers to the same question, and inconsistent assessments quickly erode a team’s credibility.

Yet the pressure to adopt agents keeps growing. Teams face record volumes of threat reporting and [CVEs](https://www.cve.org/about/Metrics), while adversaries have started using open-source agentic frameworks to exploit familiar weaknesses at machine speed. It’s no surprise that many CTI teams are now exploring multi-source agentic workflows integrated into their own tools.

One challenge for CTI analysts is that analytical tradecraft doesn’t scale, as Renze Jongman, CEO of Liberty91, has pointed out. This tradecraft includes structured analytic techniques (SATs) such as the Diamond Model for analyzing attacks and the Analysis of Competing Hypotheses (ACH) for objectively evaluating ambiguous evidence.

Take the example of evaluating recent claims by a new threat actor that they had breached several major organizations. Rather than going with instinct, our analysts used ACH with the six grades of the NATO Admiralty Code (designed for grading human sources like this one) as competing hypotheses, from “completely reliable” to “cannot be judged.” They tested each piece of evidence against the six grades in an ACH matrix, supported by analyst comments explaining the reasoning and confidence behind each assessment. That rigor, and the transparent reasoning behind it, is what lets the in-house CTI teams who rely on our underground insights trust and reuse the assessment. But it took a group of analysts significant time, and no team can do it for every new actor that appears.

In-house CTI teams also need to apply these structured analytic techniques to their organization’s context (processes, controls, assets and supply chains) and to their stakeholders’ priorities. A plain LLM prompt can’t do this, because it lacks organizational context and tradecraft, and it carries hallucination risk.

#### **Guardrails for agentic CTI**

Jongman recently proposed one answer: the [Agentic Cyber Threat Intelligence Framework (ACTIF)](https://liberty91.com/blog/agentic-cyber-threat-intelligence-framework). It’s new and still a proposal rather than an established standard, but it offers a useful way to think about what agentic CTI should look like. ACTIF is aimed at in-house CTI teams that consume and act on intelligence from many sources, using orchestrated AI agents connected to their own tools (TIP, SIEM, SOAR, MISP) to run workflows grounded in their organization’s context.

ACTIF builds its guardrails from skills: packaged instructions an agent loads for a specific task, such as grading a source or testing hypotheses. Each skill encodes a piece of analyst tradecraft, so the agent has to follow it rather than improvise. The four guardrails are designed to stop agents from making the same mistakes human analysts are trained to avoid, such as an incorrect attribution or a fabricated indicator that could affect downstream security decisions:

* **Force grounding in source material:** Every assessment must rest on facts drawn from the source data. Agents can’t invent content to fill gaps.
* **Fact-check with topical knowledge:** Agents check new reporting against curated topical knowledge to judge whether it’s accurate, novel and likely to be true.
* **Apply analytical rigor and bias controls:** Agents can’t state an assessment as fact. They must rate the quality of sources and data, assign a confidence level and justify their logic, which leaves an audit trail. They also follow a structured process: analyzing the data, forming hypotheses, then weighing and presenting them.
* **Force adversarial review:** Several agents running stronger models than the original review the whole analytical process. When reviewers disagree, they either resolve it or present the disagreement.

ACTIF’s guardrails apply the same checks and balances we expect of human analysts, because agents fall into many of the same traps, such as confirmation bias. As with people, the aim is to reduce error to an acceptable level, not eliminate it. Agent workflows provide the scale; guardrails make it safer.

Not every team has the engineering capacity to build and maintain a multi-agent framework. But ACTIF’s guardrails offer a measure for any agentic tool that sits in an analyst’s workflow. Some of that rigor can also happen upstream. Intelligence that has already been through structured analysis, with graded sources and stated confidence like the ACH example above, gives an agent a far more trustworthy foundation than raw web content. For HUMINT from the cyber underground, which most teams can’t assess themselves, that means source reliability graded by the analysts closest to the source, ready for people or agents to use. And the same guardrails should apply to any vendor’s agentic tools that feed those workflows.

#### **What to look for in an agentic CTI tool**

In conversa...