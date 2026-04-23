---
title: What to Make of AIUC-1, a New AI Agent Certification
url: https://zeltser.com/aiuc-1-cert
source: Lenny Zeltser
date: 2026-04-22
fetch_date: 2026-04-23T04:45:16.287591
---

# What to Make of AIUC-1, a New AI Agent Certification

[Lenny Zeltser](/)Security builder & leader

 [Projects](/projects) [Writing](/writing) [About](/about)

×

# What to Make of AIUC-1, a New AI Agent Certification

New certifications start as claims and earn credibility through cycles of scrutiny. AIUC-1, a compliance framework for AI agent vendors, is at that starting point. How its structure, governance, and market acceptance hold up will decide what the certificate is worth.

![What to Make of AIUC-1, a New AI Agent Certification - illustration](/assets/aiuc-1-cert.dlpo5x3B_ZnD5kj.webp)

AIUC-1 is a new compliance framework positioning itself as a “[SOC 2 for AI agents](https://www.aiuc-1.com/)”. It covers agent-specific risks such as “prompt injection” and “unauthorized AI agent actions,” which fall outside the scope of existing certifications.

As enterprise buyers start asking how these vendors handle security, AIUC-1 offers a structured answer backed by third-party audits. How much weight an AIUC-1 certificate ends up carrying depends on its structure, governance, and market acceptance. Vendors considering the certification and buyers reviewing one should understand both.

## What AIUC-1 covers.

AIUC-1 was launched in 2025 by the [Artificial Intelligence Underwriting Company (AIUC)](https://fortune.com/2025/07/23/ai-agent-insurance-startup-aiuc-stealth-15-million-seed-nat-friedman/), a venture-backed startup. Its [50+ controls](https://www.aiuc-1.com/changelog) span six domains (*Safety*, *Security*, *Reliability*, *Accountability*, *Data & Privacy*, *Society*) and map to threats in [MITRE ATLAS](https://atlas.mitre.org/) and the [OWASP Top 10 for Agentic Applications](https://genai.owasp.org/resource/agentic-ai-threats-and-mitigations/). AIUC runs quarterly technical retests between annual audits, with [Schellman as the first accredited auditor](https://www.schellman.com/blog/news/schellman-becomes-the-first-accredited-auditor-for-aiuc-1).

Adjacent frameworks address different concerns:

* [ISO 42001](https://www.iso.org/standard/81230.html) is certifiable through accredited bodies, but it targets the AI management system rather than agent behavior.
* [NIST AI RMF](https://www.nist.gov/itl/ai-risk-management-framework) is risk-management guidance with no direct certification path.
* NIST’s [Cyber AI Profile (IR 8596)](https://csrc.nist.gov/pubs/ir/8596/iprd), also risk-management guidance, addresses the intersection of cybersecurity and AI risk (draft released in 2025).

SOC 2 is a separate attestation that covers a vendor’s general service organization controls. Its scope doesn’t include the agent-specific risks AIUC-1 targets. The two frameworks coexist.

AIUC-1’s accreditation approach differs from its peers. [ISO 42001](https://www.iso.org/standard/81230.html) works through accredited certification bodies, SOC 2 is governed by the AICPA, and the NIST frameworks carry the authority of a federal standards agency. AIUC itself accredits AIUC-1’s auditors. Describing the framework as a “standard,” therefore, rests on AIUC’s own authority rather than an external accreditation body.

## Three structural questions apply to AIUC-1.

Two questions from [the SOC 2 checkbox](/soc2-checkbox-reality) carry forward to AIUC-1:

* **Scope definition:** AIUC-1 doesn’t define “AI agent,” so the vendor decides what counts as one and which agent to certify. That discretion extends to tools, data flows, and deployment context.
* **Auditor selection:** The vendor chooses its auditor, which collects evidence and writes reports while AIUC conducts the technical testing. Auditor firms compete for repeat business, and promises of [“fast and easy” have threatened SOC credibility](https://www.journalofaccountancy.com/issues/2026/feb/promises-of-fast-and-easy-threaten-soc-credibility/). The same dynamic can shape how closely an AIUC-1 auditor scrutinizes evidence and documentation.

The commercial design of AIUC-1 adds a third and most consequential consideration, the **incentive chain**:

AIUC authors the framework, runs the technical evaluations, issues the certificates, and sells the [AI agent insurance](https://aiuc.com/) that the certification enables. Accredited auditors collect evidence and write the reports. [Zack Korman has argued](https://x.com/i/web/status/2044526340133585242) that this vertical integration creates conflicts of interest at every step.

The closest precedent is the [issuer-pays credit rating model](https://en.wikipedia.org/wiki/Credit_rating_agency), in which companies pay the agencies that rate them. That arrangement [contributed to inflated ratings](https://www.justice.gov/opa/pr/justice-department-and-state-partners-secure-1375-billion-settlement-sp-defrauding-investors) before the 2008 financial crisis. [AIUC’s founders argue](https://www.cognitiverevolution.ai/underwriting-superintelligence-aiuc-s-insurance-standards-audits-to-accelerate-ai-adoption/) that their insurance business creates a counter-incentive, since losses on certified agents would hit AIUC directly.

## What to do with AIUC-1 today.

If you’re evaluating a vendor that holds AIUC-1, treat the report as useful evidence that agent-specific controls were tested. As part of your review:

* Identify which agent, tools, model versions, and data flows the audit covered. Vague scope such as “the agent” without these specifics usually means the certificate won’t cover what your organization actually uses.
* Review the specific testing behind [Domain C (Safety)](https://www.aiuc-1.com/safety) and [Domain F (Society)](https://www.aiuc-1.com/society). These controls cover judgment-based categories where documentation alone can satisfy the requirement.
* Check whether the vendor also holds [ISO 42001](https://www.iso.org/standard/81230.html). AIUC-1 attests to the agent itself, while ISO 42001 certifies the management system around it; without both, the governance picture is incomplete.
* Ask for evidence from the most recent quarterly retest, since the certificate reflects only the annual audit.

If you’re building an AI agent product, the clearest reason to pursue AIUC-1 would be buyers asking for it. Even without that demand, early adoption lets a vendor frame the security conversation and helps establish trust.

I’ve written about compliance certifications from [SAS 70](/cloud-security-beyond-sas-70) to [SOC 2](/soc2-checkbox-reality). Each new certification finds its level over several cycles as auditors compete, vendors learn, and buyers sharpen their diligence. AIUC-1 is at the start of that process.

Receive my blog posts by email.

Email addressSubscribe

### Related Articles

[![](/assets/scoring-security-product-strategy.BT3slf_v_gbB17.webp)Scoring Your Security Product Strategy in the AI Era](/scoring-security-product-strategy)[![](/assets/designing-for-humans-and-ai.BsDuNVx0_m1WIu.webp)Designing Security Products for Humans and AI Agents](/designing-for-humans-and-ai)

### About the Author

Lenny Zeltser is a cybersecurity executive with deep technical roots, product management experience, and a business mindset. He has built security products and programs from early stage to enterprise scale. He is also a Faculty Fellow at SANS Institute and the creator of REMnux, a popular Linux toolkit for malware analysis. Lenny shares his perspectives on security leadership and technology at [zeltser.com](/).

[Learn more →](/about)

Get posts by emailEmail addressSubscribe

Copy link

More on

[Artificial Intelligence](/topic/artificial-intelligence)[Risk Management](/topic/risk-management)[Leadership](/topic/leadership)

After 6+ years building the security program at [Axonius](https://www.axonius.com/) from startup to scale, I'm on a short sabbatical. I'm working on independent projects, advising a few startups, and writing here about what I'm learning.

My next chapter will be as a product leader at a security company or a CISO. Reach out on [LinkedIn](https://www.linkedin.com/in/lennyzeltser/) or email me at *my first name*...