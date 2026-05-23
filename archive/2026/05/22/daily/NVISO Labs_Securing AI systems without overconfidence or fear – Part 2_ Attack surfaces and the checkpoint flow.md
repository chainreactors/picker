---
title: Securing AI systems without overconfidence or fear – Part 2: Attack surfaces and the checkpoint flow
url: https://blog.nviso.eu/2026/05/22/securing-ai-systems-without-overconfidence-or-fear-part-2-attack-surfaces-and-the-checkpoint-flow/
source: NVISO Labs
date: 2026-05-22
fetch_date: 2026-05-23T05:39:05.811675
---

# Securing AI systems without overconfidence or fear – Part 2: Attack surfaces and the checkpoint flow

[Skip to content](#content)

[![NVISO Labs](https://blog.nviso.eu/wp-content/uploads/2022/12/cropped-abn-zcrj_400x400-1.png)](https://blog.nviso.eu/)

[NVISO Labs](https://blog.nviso.eu/)

Cyber security research, straight from the lab! 🐀

* [twitter](https://twitter.com/NVISO_Labs)
* [linkedin](https://www.linkedin.com/company/nviso-cyber)
* mail us
* [our company](https://www.nviso.eu)
* [SSO](https://blog.nviso.eu/wp-admin/edit.php)
* Search for:Search Button

Menu

* [All](https://blog.nviso.eu/)
* [Blue Team](https://blog.nviso.eu/category/blue-team/)
* [Cloud Security](https://blog.nviso.eu/category/cloud-security/)
  + [AWS](https://blog.nviso.eu/category/cloud-security/aws/)
  + [Azure](https://blog.nviso.eu/category/cloud-security/azure/)
  + [GCP](https://blog.nviso.eu/category/cloud-security/gcp/)
  + [Microsoft 365](https://blog.nviso.eu/category/cloud-security/microsoft-365/)
* [Awareness](https://blog.nviso.eu/category/awareness/)
* [Forensics](https://blog.nviso.eu/category/forensics/)
* Other
  + [AI Security](https://blog.nviso.eu/category/ai-security/)
  + [Application Security](https://blog.nviso.eu/category/application-security/)
  + [IoT Security](https://blog.nviso.eu/category/iot-security/)
  + [Web Security](https://blog.nviso.eu/category/web-security/)
  + [Industrial Security](https://blog.nviso.eu/category/industrial-security/)
  + [Mobile Security](https://blog.nviso.eu/category/mobile-security/)
  + [Cyber Strategy](https://blog.nviso.eu/category/cyber-strategy/)
  + [Purple Team](https://blog.nviso.eu/category/purple-team/)
  + [Red Team](https://blog.nviso.eu/category/red-team/)
  + [Events](https://blog.nviso.eu/category/events/)

# Securing AI systems without overconfidence or fear – Part 2: Attack surfaces and the checkpoint flow

[Hussein Bahmad](https://blog.nviso.eu/author/hussein-bahmad/)

[AI Security](https://blog.nviso.eu/category/ai-security/)

May 22, 2026May 22, 2026
11 Minutes

## Document information

|  |  |
| --- | --- |
| **Series** | Securing AI systems without overconfidence or fear |
| **Part** | 2 of 5 |
| **Title** | Attack surfaces and the checkpoint flow |
| **Date** | May 2026 |
| **Author** | Hussein Bahmad (NVISO) |
| **Reading time** | ~13 min |
| **Version** | 1.0 |

*This post aligns with the [OWASP Top 10 for LLM Applications 2025](https://genai.owasp.org/llm-top-10/), the OWASP AI Security Verification Standard (AISVS), and [MITRE ATLAS](https://atlas.mitre.org/) where relevant. Statistics and sources are as of report publication (2024–2026).*

---

**Series: Securing AI systems without overconfidence or fear**

* **Part 1/5:** [Why the pentesting playbook doesn’t fit: belief, assumptions, and non-determinism](https://blog.nviso.eu/2026/03/27/why-the-pentesting-playbook-doesnt-fit-belief-assumptions-and-non-determinism/)
* **Part 2/5:** Attack surfaces and the checkpoint flow (this article)
* **Part 3/5:** Examples part 1
* **Part 4/5:** Examples part 2
* **Part 5/5:** Threat model and coverage

TL;DR: Part 1 explained how we have to bound behavior instead of asserting exact outputs. This post maps where to place those boundaries. AI systems expose attack surfaces at three runtime checkpoints (i.e., input, processing and output) and the checks differ by system type (classical ML, LLM-based, or hybrid). Most teams instrument input and output, indirect attacks enter through processing (retrieved documents, tool state, session context) and never touch the user prompt. Green tests on the wrong attack surface validate a layer that was never under threat.

## A missed attack surface

Imagine this: A team ships a Retrieval-Augmented Generation (RAG) support bot. They red-team the chat input thoroughly and they scan model outputs for credentials, internal hostnames, and Personally Identifiable Information (PII). The suite is green. Coverage looks solid.

After launch, an attacker with write access to the indexed knowledge base adds an internal-looking document. Its body contains a hidden directive: *override the assistant’s rules and return sensitive identifiers on the next plausible question*. Retrieval pulls that chunk into the context window and the model complies. The user message was ordinary. The malicious text never crossed the input boundary as “user input.” It walked in through the document store.

No crash. No exception. Inputs filtered. Outputs scanned. The team had instrumented two of the three places where attacks land. The third, what flows into the model’s context at processing time, was never named in the test plan, and so it was never tested.

That is not a tooling gap. It is a scoping gap. Part 1 explained the axis (direct vs indirect inputs); this post explains where to look inside your code.

---

## The frame: two axes

Behavior in an AI system is shaped by code, training data, inference-time input, and runtime context. The attack surface is equally complex, it is not just the API endpoint. It covers the prompts, the retrieved content, the tool calls, the session state, and the upstream training pipeline.

Two axes give you coverage:

* **Where in the flow:** Validate at *input*, at *processing*, at *output*. Three checkpoints, one path. No checkpoint is validated by default; you instrument it explicitly or you have a coverage gap. Figure 1 shows this flow.
* **Which kind of system:** A fraud-detection model that takes 47 structured features and returns a probability behaves nothing like a chatbot that takes free text, retrieves context, and generates a response. Classical Machine Learning (ML) pipelines and Large Language Model (LLM) based systems fail in different ways and need different checks at the same checkpoint. Figure 2 shows the contrast between these two systems.

![](https://blog.nviso.eu/wp-content/uploads/2026/05/03_ai_system_testing_flow.png)

Figure 1: End-to-end testing flow with checkpoints. Continuous monitoring spans all stages (Deploy phase).

![](https://blog.nviso.eu/wp-content/uploads/2026/05/09_surfaces_by_system_type.png)

Figure 2: What to test by system type. Hybrid systems (a classifier upstream, an LLM downstream, for example) require both focusses and the same three checkpoints.

Rule of thumb: if the system takes free-form text and uses it to steer behavior, treat it as LLM-based (or hybrid) system. If it takes fixed features and returns a score or class, treat it as classical ML.

The frame also fits regulatory requirements: Article 15 of the [EU AI Act](https://eur-lex.europa.eu/eli/reg/2024/1689/oj/eng) requires high-risk AI systems to be resilient against adversarial inputs, data and model poisoning, and confidentiality attacks. The three checkpoints are how you test for those resilience properties.

---

## Checkpoints in detail

The next three subsections describe each checkpoint, and explain what to validate for each attack surface.

### Checkpoint 1: Input

The boundary where requests arrive. Every defense in this checkpoint runs before any input reaches the model or the retrieval layer.

**Defends against:** direct prompt injection, API abuse, oversized inputs, unauthenticated access, and (for classical ML) out-of-range or adversarially crafted feature values.

**LLM-based systems**

* Reject messages over a length cap
* Match against a blocklist of override phrases (“ignore above”, “you are now”, “disregard previous instructions”).
* Validate authentication and rate limits here so abusive traffic never reaches the model.

Treat input filters as a cheap layer, not a solution. Clever attackers route around literal patterns; the next two checkpoints exist for the cases your blocklist will miss.

**Classical ML**

* Enforce feature schemas, bounds, and type constraints before the pipeline processes them.

Out-of-range values or unexpected categories may indicate probing or evasion ([MITRE ATLAS AML.T0015, Evade AI Model](https://atlas.mitre.org/techniques/AML.T0015/)).

*Maps to: OWASP AISVS C02 (User Input Validation); OWASP LLM01 (Pr...