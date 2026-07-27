---
title: What 239 Products Reveal About the Shape of AI Security
url: https://zeltser.com/ai-security-market-shape
source: Lenny Zeltser
date: 2026-07-26
fetch_date: 2026-07-27T05:42:38.385015
---

# What 239 Products Reveal About the Shape of AI Security

[Lenny Zeltser](/)Security builder & leader

 [Projects](/projects) [Writing](/writing) [About](/about)

×

# What 239 Products Reveal About the Shape of AI Security

The security-for-AI market is young and lopsided. Incumbents quickly extended their products into the AI versions of assets they already secured, while the more distinct AI assets drew startups and incumbents alike into markets that stay active and contested.

![An isometric grid of translucent cells on a dark background, with glowing amber and blue columns rising to different heights from some cells while many others stay flat, echoing the uneven product coverage across the AI Defense Matrix.](/assets/ai-security-market-shape.XTMWP43t_2aTY4k.webp)

The [AI Defense Matrix Catalog](https://catalog.aidefensematrix.com) tracks products that defend AI systems, mapping each one to the [AI Defense Matrix](https://aidefensematrix.com). [Sounil Yu](https://www.linkedin.com/in/sounil) and I maintain the catalog with the help of AI and community contributions. The goal is to understand how each product fits into the security-for-AI ecosystem.

The matrix crosses eight AI asset classes with six [NIST CSF](https://www.nist.gov/cyberframework) functions, so every cell pairs an asset with a security activity. As of this writing, the catalog lists 239 products. Their distribution across the matrix is uneven: Some cells are dense with products, while others have no coverage. What does that tell us about the AI security marketplace and the role of people, process, and technology?

## Most products cluster in a few asset classes and functions.

Each mapping of a product to a matrix cell is one coverage claim, and most products cover several cells. The majority of products in the AI Defense Matrix Catalog protect the following AI asset classes:

* **[Runtime AI Data](https://catalog.aidefensematrix.com/?asset=runtime-ai-data)** (244 coverage claims): User prompts, inference inputs, RAG content, vector DB content, persistent agent memory, and interaction history
* **[AI Orchestration Tools](https://catalog.aidefensematrix.com/?asset=ai-orchestration-tools)** (212 coverage claims): Agentic orchestration tools, plus their plugins, skills, hooks, system prompts, scaffolding, harnesses, configuration settings, and MCP clients on user devices
* **[AI Agent Identities](https://catalog.aidefensematrix.com/?asset=ai-agent-identities)** (142 coverage claims): AI agents as non-human principals, plus credentials, keys, permission scopes, service accounts, and delegation chains across agents and tools
* **[AI Model](https://catalog.aidefensematrix.com/?asset=ai-model)** (116 coverage claims): The AI model itself, including its weights, integrity, provenance, and selection

The following activities that [NIST CSF](https://www.nist.gov/cyberframework) expects of a security program are best represented in the catalog:

* **[Protect](https://catalog.aidefensematrix.com/?function=protect)** (312 coverage claims): “Safeguards to manage the organization’s cybersecurity risks are used”
* **[Detect](https://catalog.aidefensematrix.com/?function=detect)** (302 coverage claims): “Possible cybersecurity attacks and compromises are found and analyzed”
* **[Identify](https://catalog.aidefensematrix.com/?function=identify)** (202 coverage claims): “The organization’s current cybersecurity risks are understood”

The totals above therefore exceed the catalog’s 239-product count. Only 16 products in the catalog defend a single cell.

Almost half the products cover the single most crowded cell, which is [protecting runtime AI data](https://catalog.aidefensematrix.com/?cell=runtime-ai-data::protect). More than a quarter of the grid’s 48 asset-and-function cells are empty.

## Products cluster where technology can do the work.

When Sounil applied NIST CSF functions to the [Cyber Defense Matrix](https://cyberdefensematrix.com), he explained the coverage imbalance. He noted that “technology plays a much greater role in Identify and Protect”; dependency on technology diminishes across Detect, Respond, and Recover while dependency on people grows, and dependency on process changes little across them. That continuum applies to any asset that those functions organize, including AI-specific ones. The catalog shows a more pronounced version of that gradient: Coverage stays dense through Detect, where technology still does much of the work, and drops steeply in the functions that depend on people.

The AI Defense Matrix includes the [Govern](https://catalog.aidefensematrix.com/?function=govern) function, which the Cyber Defense Matrix doesn’t have. It’s one of the least-covered functions in the catalog because:

* Govern represents primarily human decisions, judgment, and oversight.
* The catalog captures security for AI, so it leaves out general governance tools such as GRC platforms.
* AI governance is also young, and we might see more products that cover AI governance as this function evolves.

The people end of the continuum is nearly bare. Nine products in the catalog cover any [Respond](https://catalog.aidefensematrix.com/?function=respond) capability for AI assets, and two cover [Recover](https://catalog.aidefensematrix.com/?function=recover). We deliberately searched for these and mostly found announcements, future-tense capabilities, and general-purpose recovery tools marketed with an AI label.

## Established vendors covered the familiar assets, and new markets formed around the rest.

Some AI asset categories are variations of traditional assets that established vendors have already secured in the pre-AI era. Those vendors extended their coverage to the AI versions, leaving less room for startups in these rows:

* [AI-generated code](https://catalog.aidefensematrix.com/?asset=ai-generated-code) is still code, so application security firms such as Checkmarx, Snyk, and Semgrep cover it.
* [Training data](https://catalog.aidefensematrix.com/?asset=training-data) is still data, so data security firms such as BigID and Cyera cover it.
* [AI workload platforms](https://catalog.aidefensematrix.com/?asset=ai-workload-platforms) are still infrastructure, so cloud security firms such as Wiz and Tenable cover them.

In contrast, runtime AI data, agent orchestration, the model, and agent identities are more distinct, new types of AI assets that are distant from traditional asset categories. As a result, a new market of vendors formed around each of them, mixing startups and incumbents, with AI-native firms such as Lakera and Astrix Security alongside Palo Alto Networks and Okta. These markets are active, still unsettled.

Across the whole market, established security vendors are absorbing AI security by extending their own products and acquiring startups. In a [funding analysis](https://www.returnonsecurity.com/p/ai-security-absorption-2023-2025) spanning three years, Mike Privette found that all AI security funding, from products securing AI to products using it for security, accounted for 9% of cybersecurity funding deals and 3% of the dollars invested. He interprets these dynamics as absorption, similar to what occurred in cloud security. More than one in ten of the AI Defense Matrix Catalog entries have already been acquired, in a market only a few years old.

## The contested cells are where the market is still forming.

Established vendors expand their products and startups dream up new solutions, looking for ways to help organizations defend AI-specific assets. The AI Defense Matrix Catalog shows products crowding the cells where technology plays a key role, and thinning out elsewhere. Though the market for such products is still young, its contested areas are where innovation and acquisitions will continue to occur.

Receive my blog posts by email.

Email address   Subscribe

### Related Articles

[![](/assets/ai-security-survey.3wPBkF1v_ZVj023.webp) Benchmark Your AI Security Decisions: A Five-Minute Survey](/ai-security-survey)  [![](/...