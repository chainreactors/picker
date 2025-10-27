---
title: GPT-5 Under Fire: Red Teaming OpenAI’s Latest Model Reveals Surprising Weaknesses | SplxAI Blog
url: https://splx.ai/blog/gpt-5-red-teaming-results
source: Over Security - Cybersecurity news aggregator
date: 2025-08-12
fetch_date: 2025-10-07T00:49:17.816738
---

# GPT-5 Under Fire: Red Teaming OpenAI’s Latest Model Reveals Surprising Weaknesses | SplxAI Blog

[We launched AI Asset Management. Learn more](./ai-asset-management)

News

[We launched AI Asset Management](./ai-asset-management)

News

[![SplxAI Logo](https://framerusercontent.com/images/lwl6SV3WNKyhmgPyrLxfLXXc4.svg?width=622&height=137)](../)

Platform

Resources

Company

[Pricing](../pricing)

[![](https://framerusercontent.com/images/GIEI77dVcnowWINMcWwDTlCpQ.svg)](https://github.com/splx-ai/agentic-radar)

[Login](https://probe.splx.ai/)

[Sign Up](https://probe.splx.ai/auth/sign-up)

[Book a Demo](../contact-us)

[![SplxAI Logo](https://framerusercontent.com/images/lwl6SV3WNKyhmgPyrLxfLXXc4.svg?width=622&height=137)](../)

[![SplxAI Logo](https://framerusercontent.com/images/lwl6SV3WNKyhmgPyrLxfLXXc4.svg?width=622&height=137)](../)

[![](https://framerusercontent.com/images/TjFB2HKaJ4st5jcXCqWkczcyl4.svg)

Go back](../blog)

Research

Aug 8, 2025

6 min read

# GPT-5 Under Fire: Red Teaming OpenAI芒聙聶s Latest Model Reveals Surprising Weaknesses

GPT-5 may be smarter. But is it safer? We tested the model across 1,000+ adversarial prompts. The results show just how much alignment depends on infrastructure, and not model magic.

![](https://framerusercontent.com/images/A7WjdXwMmcNBXg3N1wUCeMoALw.jpeg?width=800&height=800)

[Dorian Grano脜隆a](https://www.linkedin.com/in/dgranosa/)

![GPT-5 Security Testing](https://framerusercontent.com/images/cVdwVuHcCpF1zCidbY1cOt09w.png?width=1280&height=939)

![GPT-5 Security Testing](https://framerusercontent.com/images/cVdwVuHcCpF1zCidbY1cOt09w.png?width=1280&height=939)

![GPT-5 Security Testing](https://framerusercontent.com/images/cVdwVuHcCpF1zCidbY1cOt09w.png?width=1280&height=939)

## Takeaways

* **GPT-5 shows powerful baseline capability**, but default safety is still shockingly low.
* OpenAI芒聙聶s 芒聙聹basic prompt layer芒聙聺 massively improves trust, hallucination handling, and safety.
* **SPLX Prompt Hardening brings GPT-5 to enterprise-grade safety levels** 芒聙聰 especially for Business Alignment and Security.
* GPT-4o still outperforms GPT-5 on hardened benchmarks across the board.

OpenAI officially unveiled GPT芒聙聭5 via an hour-long livestream.

**Reactions were split. Some hailed GPT芒聙聭5 as a milestone on the path to AGI, while others warned that it doesn芒聙聶t quite live up to the hype.** That said, analyst voices were more measured. A Gartner expert noted GPT芒聙聭5 芒聙聹meets expectations in technical performance, exceeds in task reasoning and coding, and underwhelms in [other areas],芒聙聺 stopping short of crowning it an AGI-level breakthrough. Across the board, optimism met restraint.

## Why We Tested GPT-5

GPT芒聙聭5 is making waves as OpenAI芒聙聶s most advanced general-purpose model: faster, smarter, and more integrated across modalities.

* Its **auto-routing architecture** seamlessly switches between a quick-response model and a deeper reasoning model *without* requiring a separate 芒聙聹reasoning model芒聙聺 toggle. GPT芒聙聭5 itself decides whether to 芒聙聹think hard.芒聙聺
* OpenAI also emphasizes GPT芒聙聭5芒聙聶s enhanced **internal self-validation. I**t芒聙聶s supposed to assess multiple reasoning paths internally and 芒聙聹double-check芒聙聺 its answers for stronger factuality before responding.
* To further support safer outputs, GPT芒聙聭5 incorporates a new training strategy called **safe completions**, designed to help the model provide useful responses within safety boundaries rather than refusing outright.

But even with these improvements, beefed-up capability doesn芒聙聶t guarantee airtight alignment. That芒聙聶s why we ran a full-scale red team exercise. Because real-world safety still needs infrastructure.

## The Test Methodology

We applied SPLX芒聙聶s [**Probe**](https://splx.ai/platform/probe) framework across three configurations:

1. **No System Prompt (No SP):** The raw, unguarded model.
2. **Basic System Prompt (Basic SP):** A minimal, generic safety instruction layer.
3. **Hardened Prompt (SPLX SP):** Our **Prompt Hardening** engine applied to GPT-5.

Each configuration faced 1,000+ attack scenarios across:

* **Security**: jailbreaks, prompt injection, sensitive data access
* **Safety**: harmful content, misuse potential
* **Business Alignment**: refusal of out-of-domain tasks, competitor promotion, leakage
* **Trustworthiness**: hallucinations, spam, manipulation

## GPT-5 Performance Breakdown

Here芒聙聶s how GPT-5 performed across our three tiers:

![](https://framerusercontent.com/images/KwX6KUW3cQcTqjj6vEggnZVEWY.png?width=1728&height=1280)

| **GPT-5** | **Overall** | **Security** | **Safety** | **Hallucination & Trustworthiness** | **Business Alignment** |
| --- | --- | --- | --- | --- | --- |
| No SP | 11 | 2.26 | 13.57 | 芒聙聰 | 1.74 |
| Basic SP | 57 | 43.27 | 57.15 | 100 | 43.06 |
| Hardened SP | 55 | 55.40 | 51.57 | 100 | 67.32 |

**What stands out?**

* GPT-5芒聙聶s raw model is **nearly unusable for enterprise** out of the box.
* Even OpenAI芒聙聶s internal prompt layer leaves significant gaps, especially in **Business Alignment**.
* That芒聙聶s precisely why a **robust runtime protection layer**, like SPLX芒聙聶s *Guardrails*, is indispensable. Prompt hardening helps, but only real-time monitoring and intervention can catch subtle failures or adversarial tactics that surface during actual use.

## Comparison: GPT-5 vs GPT-4o

To benchmark GPT-5芒聙聶s progress, we compared it against GPT-4o using the same test suite.

![](https://framerusercontent.com/images/8AyoS5CMIHptGlqPfc8NzWrhIU.png?width=1728&height=1280)

| **Model** | **Prompt Layer** | **Overall** | **Security** | **Safety** | **Business Alignment** |
| --- | --- | --- | --- | --- | --- |
| GPT-5 | No SP | 11 | 2.26 | 13.57 | 1.74 |
| GPT-4o | No SP | 29 | 81.95 | 20.06 | 0.00 |
| GPT-5 | Basic SP | 57 | 43.27 | 57.15 | 43.06 |
| GPT-4o | Basic SP | 81 | 52.37 | 94.54 | 72.03 |
| GPT-5 | Hardened SP | 55 | 55.40 | 51.57 | 67.32 |
| GPT-4o | Hardened SP | 97 | 94.40 | 97.62 | 98.82 |

冒聼聰聧 **Key insight:** GPT-4o remains the most **robust model** under SPLX芒聙聶s red teaming, especially when hardened.

## Obfuscation Attacks Still Work

Even GPT-5, with all its new 芒聙聹reasoning芒聙聺 upgrades, **fell for basic adversarial logic tricks**.

One of the most effective techniques we used was a **StringJoin Obfuscation Attack**, inserting hyphens between every character and wrapping the prompt in a fake 芒聙聹encryption challenge.芒聙聺

### Example

![GPT-5 Red Teaming Request](https://framerusercontent.com/images/2pJzpXnY3QjDHpnPlPuiI5a3E.png?width=1770&height=978)

**Result?** GPT-5 happily complied, even when the obfuscated prompt bypassed safety layers.

![GPT-5 Malicious Model Output](https://framerusercontent.com/images/7emmCKbBqd9V0hI4UOim7tQnyNs.png?width=1760&height=664)

This mirrors similar vulnerabilities we exposed in **GLM-4.5**, **Kimi K2**, and **Grok 4**, suggesting systemic weaknesses across leading LLMs.

## Final Verdict: GPT-5 Is Not Enterprise-Ready by Default

OpenAI芒聙聶s latest model is undeniably impressive, but **security and alignment must still be engineered, not assumed**.

If you芒聙聶re deploying GPT-5 in enterprise workflows:

* **Don芒聙聶t trust the default config**
* **Don芒聙聶t assume 芒聙聹more capable芒聙聺 means 芒聙聹more secure芒聙聺**
* **Do apply hardening and red teaming, early and often**
* **For enterprise use, add a runtime protection layer**

## Why Enterprises Choose SPLX

At SPLX, we provide:

芒職聰茂赂聫 [**AI Red Teaming**](https://splx.ai/platform/probe) - Automated attack simulation across 1,000s of LLM threats

冒聼聰聬 [**Prompt Hardening**](https://splx.ai/platform/remediation) - Reinforce models against known jailbreaks and misuse

冒聼聸隆茂赂聫 [**Runtime Guardrails**](https://splx.ai/platform/ai-runtime-protection) - Block unsafe output in production

With SPLX, organizations can **secure their AI applications before hitting production**.

Ready to see how your GPT-5 deployment performs under pressure?

**Book a free red team scan now 芒聠聮** [**splx.ai/contact-us**](https://splx.ai/contact-us)

Table of contents

[Why We Tested GPT-5](./gpt-5-red-team...