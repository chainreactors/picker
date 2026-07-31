---
title: A Field Guide to the AI Security Market
url: https://zeltser.com/ai-security-market-field-guide
source: Lenny Zeltser
date: 2026-07-30
fetch_date: 2026-07-31T05:31:15.582712
---

# A Field Guide to the AI Security Market

[Skip to main content](#main-content)

[Lenny Zeltser](/)Security builder & leader

 [Projects](/projects) [Writing](/writing) [About](/about)

×

# A Field Guide to the AI Security Market

The market for products that secure AI is crowded and hard to read, with overlapping categories and products that each do many jobs. With the AI Defense Matrix, you can ask the right questions, tell what a product was built for, and staff the gaps no product fills yet.

![A dark museum cabinet of glowing blue specimens in a six-by-eight grid, the middle columns densely stocked and the outer columns nearly bare, echoing where products cluster on the AI Defense Matrix.](/assets/ai-security-market-field-guide.BicigIO9_n9xui.webp)

[Sounil Yu](https://www.linkedin.com/in/sounil) compares the general security product marketplace to a [disorganized grocery store](https://cyberdefensematrix.com), where products pile up without aisles to organize them. The AI security market is such a store, too. Product categories overlap, vendors name products after ambitions rather than capabilities, and the same demo can support multiple pitches. Buyers can’t find what they need, and sellers struggle to explain what their products do.

Sounil and I built the [AI Defense Matrix Catalog](https://catalog.aidefensematrix.com) to make sense of the AI security marketplace. The catalog maps each product to the cells of the [AI Defense Matrix](https://aidefensematrix.com), which crosses eight AI asset classes with six [NIST CSF](https://www.nist.gov/cyberframework) functions, so each cell pairs one asset class with one security function. It illustrates where products cluster and where coverage is light. I explored what that distribution reveals about the market’s structure in the [shape of AI security](/ai-security-market-shape) article. This guide is the buyer’s companion, with cluster-by-cluster questions to ask vendors when evaluating a product that secures AI.

## Four clusters fill the crowded cells.

There are four product clusters in the catalog’s crowded cells, each with its own questions to ask before you buy.

**AI runtime guardrails:** The products in the catalog’s largest cluster protect and monitor runtime AI data, meaning prompts, inference traffic, RAG content, and agent memory. These products filter what enters and leaves models, redact sensitive data, and flag policy violations. The pattern is familiar from web application firewalls and DLP, and most bundle protection and detection in one product. The catalog lists more than a hundred products that cover runtime AI data. Frank Wang writes in *Frankly Speaking* that “as an industry, we haven’t even fully figured out [what guardrails we should be enforcing](https://franklyspeaking.substack.com/p/has-ai-made-security-easier), or what level of autonomy we should grant an internal agent.” Ask where the product inspects traffic, which prompts and other data leave your boundary, and what happens to your AI application when the vendor’s service goes down.

**Agent identity and access:** Products in the second major cluster treat AI agents as non-human principals that need credentials, permission scopes, and lifecycle management. Identity incumbents such as SailPoint and Saviynt extended their platforms here, and dozens of startups joined them. Agents are a new kind of principal in the familiar discipline of identity management. Ask how the product handles delegation chains, where an agent acts for a human or through another agent, and how quickly you can revoke a misbehaving agent’s credentials, including what happens to its in-flight delegations.

**Model scanning and posture:** Products in the third cluster inspect AI models and pipelines, scanning model files for tampering, testing for adversarial weaknesses, and inventorying which models run where. Think of it as vulnerability management and red teaming aimed at models. Ask whether your team can turn the findings into fixes, and which model formats and pipelines the scanner supports.

**Orchestration and MCP security:** Products in the fourth cluster secure AI orchestration tools, including MCP servers, plugins, and the scaffolding around agents. Ask what the product can see across your agents and plugins, what it can restrict, and how it detects an agent acting outside its scope.

## A few products cover the near-empty cells.

Fewer than a dozen products cover any Respond or Recover capability, and those few are an early sketch of AI incident response tooling, including agent containment through identity suspension, machine unlearning positioned as model recovery (Hirundo), and rollback of agent actions (Rubrik Agent Cloud). These functions depend on people more than on technology, as I explored in the [shape of AI security](/ai-security-market-shape) article. Treat response and recovery for AI incidents as work for your people, your playbooks, and the recovery tooling you already own.

## Most products cover more cells than they were built for.

The AI Defense Matrix Catalog records how central each coverage claim is to the product’s purpose. About a third of the coverage claims in the catalog are “secondary” or “adjacent,” meaning areas the product supports rather than its central purpose. Most products in the catalog cover three or more cells. When a vendor pitches broad coverage, ask what the product was built to do and which capabilities the vendor added along the way, then check the answers against the product’s catalog entry.

Add vendor viability to your evaluation checklist as well. Acquirers have already absorbed more than one in ten of the products in the catalog, and the market is only a few years old. Expect the crowded cells to keep consolidating. Ask about change-of-control terms, data portability, and the migration path if another vendor absorbs the product.

## Decide which cells you need before you evaluate products.

Review the AI Defense Matrix against your AI security requirements to prepare for vendor discussions:

* List the matrix cells that matter most for your AI deployments by pairing each AI asset you use with the functions your program needs for it.
* Check whether the products you already run cover those cells before you evaluate new ones.
* For crowded cells, select a few vendors and evaluate them in your own environment. Products within a cluster differ more in operations than in demos.
* Check each product’s AI Defense Matrix mappings in the [catalog](https://catalog.aidefensematrix.com) to better steer those discussions.
* For cells you need to address that are empty in the catalog, devise a process, owned by a named person, instead of waiting for a product.

Match products to the cells your AI deployments need, and staff the rest with people and processes.

Receive my blog posts by email.

Email address   Subscribe

### Related Articles

[![](/assets/cyber-company-profiles.BuEKcZVR_ZJTY0f.webp) Cyber Company Profiles: Independent Analysis of Security Vendors](/cyber-company-profiles)  [![](/assets/ai-security-market-shape.XTMWP43t_Z1VHqi5.webp) What 239 Products Reveal About the Shape of AI Security](/ai-security-market-shape)

### About the Author

Lenny Zeltser is a cybersecurity executive with deep technical roots, product management experience, and a business mindset. He has built security products and programs from early stage to enterprise scale. He is also a Faculty Fellow at SANS Institute and the creator of REMnux, a popular Linux toolkit for malware analysis. Lenny shares his perspectives on security leadership and technology at [zeltser.com](/).

Get posts by email   Email address   Subscribe

  Copy link

More on

[Artificial Intelligence](/topic/artificial-intelligence)[Risk Management](/topic/risk-management)

4 min to read

July 30, 2026

   [Projects](/projects) [Writing](/writing) [About](/about) [Newsletter](/newsletter) [RSS](/rss.xml)

© 2026 [Lenny Zeltser](/)