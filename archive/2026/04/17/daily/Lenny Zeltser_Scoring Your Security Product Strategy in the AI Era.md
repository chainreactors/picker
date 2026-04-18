---
title: Scoring Your Security Product Strategy in the AI Era
url: https://zeltser.com/scoring-security-product-strategy
source: Lenny Zeltser
date: 2026-04-17
fetch_date: 2026-04-18T04:33:18.982375
---

# Scoring Your Security Product Strategy in the AI Era

[Lenny Zeltser](/)Security builder & leader

 [Projects](/projects) [Writing](/writing) [About](/about)

×

# Scoring Your Security Product Strategy in the AI Era

AI has made commodity software easy to produce, leaving traditional SaaS exposed. Applied to cybersecurity, a seven-dimension rubric scores security product strategies to help leaders identify weaknesses and strengths.

![Scoring Your Security Product Strategy in the AI Era - illustration](/assets/scoring-security-product-strategy.BT3slf_v_Z6QzwG.webp)

Investors and boards ask software executives what prevents a competitor or the customer from building a comparable product. The question is particularly pressing in the era of AI vibe-coding, as Ben Vierck explores in [The Cost of Software Is Now Zero](https://lit.ai/blog/2026/03/29/the-cost-of-software-is-now-zero/). His seven-dimension rubric assesses defensibility as customers become their own builders.

Ben’s analysis focuses on general-purpose SMB SaaS, but many security product strategies score well across his dimensions. Regulatory posture, proprietary telemetry, and threat research take years to accumulate, so homegrown vibe-coded replacements struggle to replicate them. However, security vendors whose products score poorly on the rubric might face the AI-equipped weekend builder as a real competitor.

## Security products score well on Ben’s rubric.

Ben offers a scoring rubric to assess the defensibility of a SaaS product. The dimensions are *Value Delivery*, *Switching Cost*, *Compliance Moat*, *Problem Complexity*, *Buyer Profile*, *Layer* (end-user app vs. infrastructure), and *Proprietary Data / Content / IP*. Each dimension scores from 1 (exposed) to 3 (defensible). His published rubric covers full definitions and scoring details.

Security vendors can score well on most of these dimensions with focused investment. Regulatory posture earns high *Compliance Moat* scores. Accumulated telemetry earns high *Proprietary Data* scores over time. ML-driven detection earns *Problem Complexity* that a vibe-coded replacement can’t easily match. As Ben puts it:

> “A vibe-coded app can approximate a dashboard. It can’t approximate a decade of algorithmic research.”

Consider a few security product categories to see how this works:

* A compliance automation platform wraps software around audit evidence and auditor relationships that can be hard to replicate.
* Managed detection and response services aggregate cross-customer threat data that a single customer can’t gather alone.
* Endpoint protection software incorporates proprietary telemetry and threat research that are impractical for vibe-coded projects to replicate.

## Three industry dynamics shape how security products score.

Ben’s rubric works well for cybersecurity companies. Three industry dynamics shape how security products score on his dimensions.

**Threat-Data Flywheel** (shapes *Proprietary Data*): Product deployments can generate telemetry that sharpens detection or other insights across the customer base. For example, CrowdStrike’s Threat Graph [correlates telemetry across its entire customer base](https://www.sec.gov/Archives/edgar/data/1535527/000153552725000009/crwd-20250131.htm), and each new customer improves detection for the rest. Neither a weekend build nor a general-purpose AI model can reach that scale; the value is in the data and the feedback loop that produced it.

**Insurer- and Regulator-Mandated Procurement** (shapes *Compliance Moat*): Companies often select security products to address compliance requirements from insurance providers and regulators. Cyber insurance has become [a purchasing factor for security products](/smb-security-product-strategy), with insurers listing EDR among underwriting requirements. US federal buyers require [FedRAMP authorization](https://www.fedramp.gov/program-basics/), which takes more than a year to obtain. EU regulations such as [NIS2](https://digital-strategy.ec.europa.eu/en/policies/nis2-directive) and [DORA](https://www.eiopa.europa.eu/digital-operational-resilience-act-dora_en) impose specific obligations on financial and critical-infrastructure suppliers. An AI-built replacement still needs to clear those hurdles, even if it matches the product’s features; few companies have the appetite or capacity to pursue them for homegrown apps.

**Adversarial Pressure** (shapes *Problem Complexity*): Threat actors are an outside force that keeps security products changing, while traditional products stabilize around company-controlled business processes. Vibe-coded security apps still need ongoing threat research and detection engineering that few companies can sustain.

These dynamics illustrate why cybersecurity products can earn high scores across Ben’s dimensions. A homegrown tool would need sustained investment to match any of them.

## Category scores reveal where the exposure sits.

When designing a security product strategy or vetting a vendor’s strategy, use Ben’s framework to identify AI-era defensibility gaps. Consider these hypothetical examples:

*An EDR platform with a shared data layer* scores high across most dimensions. This product addresses a hard problem with heavy data requirements. It defends the business from adversaries that evolve, draws on proprietary telemetry, and often satisfies an insurer’s EDR requirement.

| Dimension | Score | Why |
| --- | --- | --- |
| Value Delivery | 3 | Detection and response outcomes are the product. Code is the carrier. |
| Switching Cost | 3 | Tuning, baselines, and SOC integrations make replacement expensive. |
| Compliance Moat | 3 | EDR sits inside cyber insurance baselines, SOC 2 expectations, and federal control frameworks. |
| Problem Complexity | 3 | Kernel instrumentation, ML detection, and real-time response are hard to build. |
| Buyer Profile | 3 | Regulated enterprises with procurement and legal gates between purchase and use. |
| Layer | 2 | Endpoint layer, above infrastructure but below cloud workloads. |
| Proprietary Data / Content / IP | 3 | Labeled threat datasets and cross-customer telemetry compound into a detection flywheel. |

Total: 20 out of 21. A customer trying to rebuild this product would match the feature list. However, building the SOC integration, hiring staff, earning certifications, and accumulating operating data would take years.

These dimensions reinforce each other through [platform dynamics](/what-platform-means-cybersecurity). Enterprise buyers generate the cross-customer telemetry that sharpens detection. Better detection reduces incidents and strengthens the compliance posture that attracts the next enterprise buyer. A vibe-coded replacement can mimic any single dimension but can’t reproduce the loop.

*A GRC automation platform* may score low on Problem Complexity. Evidence dashboards, workflow automation, and control mapping are routine software work that AI tooling now accelerates. Compliance Moat holds because the product is how customers satisfy audits they can’t avoid. Switching Cost rises with accumulated evidence, auditor relationships, and cross-framework mappings, while Buyer Profile stays high with regulated enterprise customers.

*A single-purpose SMB web filter sold as standalone SaaS* scores low on almost every dimension, especially if it doesn’t offer hard-to-get proprietary data. It carries few compliance requirements beyond those already met by [bundled platforms](/smb-security-product-strategy). A buyer with an AI assistant and open-source data sources could build something comparable. Products of this shape tend to get bundled into platforms, absorbed by MSPs, or replaced by customers directly.

Running this exercise honestly identifies the gaps worth examining. Low scores name dimensions that need investment. High scores require continued reinvestment, since threat-data flywheels decay, regulatory moats shift as frameworks tighten, and platforms bundle competing capabilities.

## Turning the score into a p...