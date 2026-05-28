---
title: From Prompt to Prod: Sicuranext Evaluates AI Integration in SOC Analysis
url: https://blog.sicuranext.com/llm-evaluation-soc-analysis/
source: Over Security
date: 2026-05-27
fetch_date: 2026-05-28T06:03:04.378086
---

# From Prompt to Prod: Sicuranext Evaluates AI Integration in SOC Analysis

[![Sicuranext Blog](https://blog.sicuranext.com/content/images/2026/03/sicuranext_h-accent-2.png)](https://blog.sicuranext.com)

* [Home](https://blog.sicuranext.com/)
* [WAAP](https://blog.sicuranext.com/tag/waap/)
* [SOC](https://blog.sicuranext.com/tag/soc/)
* [PWNPress](https://blog.sicuranext.com/tag/pwnpress/)
* [AI](https://blog.sicuranext.com/tag/ai/)

[Sign in](#/portal/signin)
[Subscribe](#/portal/signup)

# From Prompt to Prod: Sicuranext Evaluates AI Integration in SOC Analysis

#### [Hussein Husseini](/author/hussein/)

27 May 2026
• 12 min read

![From Prompt to Prod: Sicuranext Evaluates AI Integration in SOC Analysis](/content/images/size/w2000/2026/04/Gemini_Generated_Image_6fpr6u6fpr6u6fpr.png)

> At Sicuranext, we do not evaluate AI with artificial examples. We replay realistic SOC workflows, measure correctness and consistency, verify tool behavior, and put guardrails around automation before it touches our SOC.

AI in a SOC should not be judged by whether it can produce a convincing paragraph. It should be judged by whether it behaves correctly inside a real workflow: on noisy alerts, incomplete evidence, repeated executions, structured outputs, tool calls, and operational guardrails. A beautifully phrased mistake is still a mistake. In security operations, it can also be an expensive one.

That is why I approached LLM adoption as an engineering problem before treating it as a product feature. If AI is going to help in SOC triage and analysis, it has to earn trust the same way any serious component does: with testing, telemetry, thresholds, and rollback discipline.

![](https://blog.sicuranext.com/content/images/2026/04/Gemini_Generated_Image_ey1xbdey1xbdey1x.png)

## Disclaimer

Just a quick heads-up! While we’re diving deep into how we evaluate the ****intelligence**** and ****logic**** of our AI integrations, this post doesn't cover the heavy-duty ****security guardrails**** we have in place. Rest assured, we apply rigorous filtering, prompt injection protection, and data sanitization layers to keep the system locked down. We're just focusing on the "brain" and its performance for today!

### SOC AI Evaluation Starts at the Workflow Level

The first mistake teams make with LLMs in security is evaluating the model as if it were a chatbot. A SOC workflow is not a chat. It is an execution path.

An alert pops up, gets normalized, enriched, compared with historical patterns, optionally escalated to artifact retrieval, and only then turned into a structured verdict and possibly an analyst-attention-requiring note or a silenced false positive (hopefully). That means the real unit under test is not the prompt alone. It is the workflow: data in, context assembly, tool boundaries, output schema, safe routing, and operational side effects.

This is also where evaluation becomes honest. The question is no longer “does the answer sound reasonable?” The question becomes “did the workflow behave correctly under realistic conditions?” That is a much less glamorous question, and a much more useful one.

![](https://blog.sicuranext.com/content/images/2026/04/Gemini_Generated_Image_zdk4v5zdk4v5zdk4.png)

### What I measure

In practice, I score our AI-assisted SOC workflow across four dimensions:

* *`Truthfulness`*: does the model converge to the analyst-reviewed answer?
* *`Determinism`*: does the same alert produce stable outcomes across repeated runs?
* *`Tool discipline`*: does the agent retrieve extra evidence when it is actually needed?
* *`Operational reliability`*: does the whole pipeline stay valid, parseable, and robust across model and prompt profiles?

For simplicity, the math below focuses on a single output field: `risk_level`. In practice, the tests cover additional outputs, but `risk_level` is the clearest lens for explaining the methodology without turning this blog post into a research paper.

### 1. Truthfulness: are we converging to the right analysis?

Truthfulness is the part that requires a human-reviewed dataset. There is no shortcut around that. If you want to know whether the model is correct, you need something to compare it against.

For each alert `a`, I replay the workflow `R` times and compare the observed risk level against the expected analyst-reviewed risk level.
I map the ordinal risk levels to integers:

![](https://blog.sicuranext.com/content/images/2026/04/Gemini_Generated_Image_603sgl603sgl603s.png)

💡

****why ask the model for a risk\_level instead of a raw risk\_score?****
**Because a score like** *`67/100`* **can suggest a level of precision the model does not really have. For LLMs, a safer output is usually a bounded category such as** *`Low / Medium / High / Critical`***, which can then be mapped deterministically to an internal score range. E**mpirical work on LLM calibration has shown **that numeric confidence can be unreliable, so asking for a number may add false precision rather than real rigor. For automation, verbal categories are usually easier to constrain, test, and compare across runs.**

That lets us compute not only exact matches, but also distance from the correct answer. A model that predicts `low` instead of `medium` is wrong, but it is less wrong than predicting `low` instead of `critical`.

The three truthfulness metrics I like most are:
`Alert-level exact match`: The modal risk level across repeated runs for an alert must match its expected risk level.
`Run-level exact match`: Each individual run is checked against the expected risk level.
`Mean risk error`: The average absolute distance between observed and expected risk level.

A publication-safe version of that logic looks like this:

```
RISK_TO_INT = {"low": 1, "medium": 2, "high": 3, "critical": 4}

def risk_level_error(observed: str, expected: str) -> int:
    return abs(RISK_TO_INT[observed] - RISK_TO_INT[expected])

def modal_value(values: list[str]) -> str | None:
    return max(values, key=values.count) if values else None

modal_risk = modal_value(observed_risks_for_alert)
alert_pass = modal_risk == expected_risk
run_exact_rate = sum(r == expected_risk for r in observed_risks_for_alert) / len(observed_risks_for_alert)
mean_risk_error = sum(risk_level_error(r, expected_risk) for r in observed_risks_for_alert) / len(observed_risks_for_alert)
```

Why take into consideration all three? Because they answer different questions.

* `Alert-level exact match` tells us whether the workflow converges to the right operational conclusion for a case. (thus giving the possibility to detect specific patterns of cases where success rate was low, and take actions for improvement)
* `Run-level exact match` tells us how often the workflow is individually right. (if you get a 100% success here over a large test sample, just be sure that your system has a direct connection to God)
* `Mean risk error` tells us how wrong it is when it misses. In risk assessment terms, that matters. A one-step miss is not the same thing as falling off a cliff.

For a public production-grade benchmark posture, a reasonable target band might be:

* `alert-level risk success >= 85%`
* `run-level risk success >= 80%`
* `mean risk error <= 0.35`

Those are not a dump of our private gates. They are the kind of target bands I believe are aligned with serious evaluation practice in modern AI and security engineering.

### 2. Determinism: is the system stable, or is each run a fresh creative interpretation of reality?

Truthfulness asks whether the answer is correct. Determinism asks whether the answer is consistent. That sounds similar, but it is not the same test at all.

For determinism, I do not compare against human truth. I compare repeated runs against each other. This means determinism can be measured without a labeled dataset in the strict sense. You still need representative alerts to replay, but the metric itself does not require human annotation.

The first determinism metric is per-alert consistency:

* `consistency(a) = average( observed_risk(a,r) == m...