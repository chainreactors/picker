---
title: OWASP-Top-10-AI-Infrastructure-Security-Risks
url: https://kitploit.com/en/tools/github/owasp/owasp-top-10-ai-infrastructure-security-risks
source: Kitploit
date: 2026-08-27
fetch_date: 2026-08-28T13:36:37.652716
---

# OWASP-Top-10-AI-Infrastructure-Security-Risks

[Skip to content](#main-content)

[![Kitploit](/_next/image?url=%2Flogo.png&w=64&q=75)KITPLOIT](/en)[Tools](/en/tools)[Blog](/en/blog)Categories

EN

[Submit](/en/submit)

[Tools](/en/tools)[Blog](/en/blog)Categories

[Submit](/en/submit)

EN

Hacking, PenTest, and Cybersecurity Tools for Your Security Arsenal!

Kitploit is a directory of hacking, cybersecurity, and pentesting tools. Discover the latest project updates to find vulnerabilities, analyze systems, automate testing, and strengthen your security.

·Analytics preferences·[Feeds](/en/feeds)·[Contact](/en/contact)·[Privacy](/en/privacy)·© 2026 Kitploit

Tool Directory

## Categories

[View all categories](/en/categories)

Loading categories

OWASP-Top-10-AI-Infrastructure-Security-Risks — A practical framework identifying and prioritizing the top security risks in AI datacenter infrastructure, covering hardware, networking, management planes, and supply chain, with mitigation strategies for providers and customers. | Kitploit

[Tools](/en/tools)/![GitHub](/providers/github.png)GitHub/owasp/owasp-top-10-ai-infrastructure-security-risks

![](https://assets.kitploit.com/production/public/tools/53283/89d01bd2d38f8c99b2f6e280056619b0ba43e70e5029f23051e919c9d945fd2d-display-v1.webp)

[Cloud Infrastructure Security](/en/categories/cloud-infrastructure-security)[Network Security](/en/categories/network-security)[Hardware Security](/en/categories/hardware-security)[Supply Chain Security](/en/categories/supply-chain-security)[Papers & Research](/en/categories/papers-research)[Learning & Education](/en/categories/education)[Curated Resources](/en/categories/curated-resources)[AI Security](/en/categories/ai-security)

### Most Popular

[View all →](/en/tools)

Discover the most used tools by our community.

Last 7 DaysLast 30 Days

Explore all tools

Browse our collection of tools

[View all tools →](/en/tools)

![GitHub](/providers/github.png)

owasp/owasp-top-10-ai-infrastructure-security-risks

# OWASP-Top-10-AI-Infrastructure-Security-Risks

A practical framework identifying and prioritizing the top security risks in AI datacenter infrastructure, covering hardware, networking, management planes, and supply chain, with mitigation strategies for providers and customers.

[View Repository](https://github.com/owasp/owasp-top-10-ai-infrastructure-security-risks)

362 days ago![Not yet reviewed](/_next/image?url=%2Fbadges%2Fkitploit_badge_not_reviewed_full.png&w=48&q=75)

Share

# The Top 10 Data Center and AI Infrastructure Security Risks

![FORGE - The Top 10 Data Center and AI Infrastructure Security Risks. Harden the metal beneath the model.](https://assets.kitploit.com/production/public/readmes/53283/51310978a8f3a271c3cda30bbda4d6caedeaff81021dc6816d12f2ce808f0870/6b6fdb007ba337699284cbc5022df0207b8c7bd7d493bbefac34e2ae4ab2c0eb-display-v1.webp)

> **FORGE** - Harden the metal beneath the model.
>
> 🌐 **Website:** <https://forge-framework.io>

## Executive Summary

**AI datacenters are being built faster than they are being secured.**

The rapid expansion of datacenters, GPU clouds, and specialized compute environments has introduced security risks across hardware, networking, storage, orchestration, identity, management planes, and physical operations. Many of these risks resemble traditional datacenter or cloud security issues, but modern data centers and AI infrastructure changes their severity: systems originally designed for trusted operators are now supporting high-value, multi-tenant workloads from unrelated customers.

The **Top 10 Data Centers & AI Infrastructure Security Risks** provides a practical framework for identifying, prioritizing, and reducing the most important security risks in the infrastructure layer that powers AI. The framework defines the most critical failure modes in AI infrastructure and helps translate them into concrete security requirements.

### What This Framework Covers

This framework focuses on the security of AI infrastructure and the datacenters that house it: the physical hardware, networking fabrics, management planes, orchestration systems, storage systems, and operational environments on which AI workloads run.

It does not focus on AI models themselves or application-layer risks such as prompt injection, insecure agent behavior, model abuse, or model-level evaluation. Those risks are addressed by frameworks focused on other parts of the AI stack, including the [OWASP Top 10 for LLM Applications](https://owasp.org/www-project-top-10-for-large-language-model-applications/), [MITRE ATLAS](https://atlas.mitre.org/), the [NIST AI Risk Management Framework](https://www.nist.gov/itl/ai-risk-management-framework), and [ISO/IEC 42001](https://www.iso.org/standard/81230.html). Together, these resources give practitioners a more complete picture of AI security, from governance and application-layer risks down to the underlying compute infrastructure.

Some risks in this document also exist in traditional datacenter and cloud environments. They are included here because AI infrastructure makes them materially more severe: shared high-value compute, complex accelerator clusters, dense management layers, and multi-tenant operations can turn ordinary infrastructure weaknesses into more severe security risks because the likelihood and impact of any incident are much higher than in traditional enterprise-level software and service deployments.

### Who This Framework Is For

**Neo-cloud providers** can benefit from the framework as a practical guide to the AI infrastructure threat landscape, attack surface review, environment hardening, security prioritization, and maturity demonstration.

**AI infrastructure customers** can benefit from the framework as a practical guide for procurement, security reviews, contractual requirements, provider comparison, and assessing resilience against realistic tenant-to-infrastructure compromise.

**Hybrid Cloud security teams** can benefit from this framework as a practical guide for configuring, maintaining, and securing their on-premise footprint against modern attacks, which can quickly pivot between environments.

## Acknowledgments

Built to evolve with the field, and kept open so the whole AI and security community can use it, challenge it, and improve it.

We would like to thank and acknowledge all experts which took part in reviewing and validating this document.

Have feedback or want to contribute? [[email protected]](/cdn-cgi/l/email-protection#5c2e392f393d2e3f341c303d2a3d303d3e2f723533)

### Authors

* Michael Katchinskiy (Head of Security Research @ Lava)
* Yakir Kadkoda (CTO @ Lava)

### Reviewers

* Tony Rea (Global AI Infrastructure Lead @ Dell)
* Daniel Iziourov (Director of Platform Security @ Nebius)
* Vjaceslavs Klimovs (Senior Technical Director @ Roblox)
* Assaf Namer (Head of AI Security @ Google)
* Tyson Macaulay (Deputy Director @ NC CIPSER)
* Golan Ben-Oni (CIO/CISO @ IDT)
* Florina Ciorba (Associate Professor, Head of High Performance Computing group @ University of Basel)
* Arthur Reed (Security Engineer @ PNNL)
* Deumens Erik (Director Research Computing @ University of Florida)
* Saad Malik (CTO @ Spectro Cloud)
* Selim Aissi (Former Vice President, Global Information Security @ Visa & Intel)
* Guy Bilitski (Leading AI Operations @ SDS AI)
* Dan Farmer (Security Researcher)
* Michael Bargury (CTO @ Zenity)
* Amir Jerbi (Former CTO @ Aqua Security)
* Bill Stout (Former Technical Director, AI Product Security @ ServiceNow)
* Roey Yaacovi (CTO, DSPM & AI Security @ IBM)
* Guy Shanny (Co-Founder & CEO, Polar Security, acquired by IBM)
* Ziv Karliner (CTO @ Pillar)
* Assaf Morag (Security Researcher)
* James Berthoty (Founder & CEO @ Latio)

## The Five Domains of the FORGE Lens

FORGE domains define the evaluation lens: the infrastructure areas where AI security risk lives. The Risk Matrix below maps individual risks into these domains.

| Domain | Name | Description |
| --- | --- | --- |
| **F** | Fleet integrit...