---
title: Designing Security Products for Humans and AI Agents
url: https://zeltser.com/designing-for-humans-and-ai
source: Lenny Zeltser
date: 2026-04-06
fetch_date: 2026-04-07T04:30:36.246982
---

# Designing Security Products for Humans and AI Agents

[Lenny Zeltser](/)Security builder & leader

 [Projects](/projects) [Writing](/writing) [About](/about)

# Designing Security Products for Humans and AI Agents

AI agents are quickly joining humans as personas that use enterprise security products. Vendors who understand how to support all their users, from analysts to agents, will build products that fit how teams actually work.

![Designing Security Products for Humans and AI Agents - illustration](/assets/designing-for-humans-and-ai.BsDuNVx0_Zxb3r4.webp)

Poor usability in a security product often signals that the vendor doesn’t understand how their customers actually work. The products that win adoption aren’t necessarily the ones with the longest feature lists, but the ones that fit the team’s workflow so well that users don’t want to give them up.

AI not only makes this gap harder to spot but also requires special attention. Coding assistants produce polished front-ends that make all enterprise products look increasingly alike, so responsive layouts and clean navigation no longer differentiate them. Instead, product managers need to understand how every persona uses the product, including AI agents.

## The Next User Isn’t Human

AI agents are becoming a critical interface for enterprise products. Most products started as closed, self-contained tools, but market pressure forced vendors to add APIs for customer integrations. Now agents are the next layer, handling configuration, oversight, action, and output consumption.

Products that built their entire interaction model around a visual GUI now struggle to support AI agents. Before AI, vendors created drag-and-drop canvases so enterprise users could design automations without writing code. The approach caught on quickly, but users found the canvases complex and time-consuming. When AI agents offered a simpler path, many users preferred describing their intent to an agent rather than dragging components across a screen. Because these products treated the canvas as the primary interface, their APIs often don’t expose the full capability set.

Having a REST API doesn’t make a product agent-friendly. [REST’s small, composable endpoints aren’t great for AI agents](https://workos.com/blog/mcp-vs-rest). Each endpoint’s schema consumes tokens in the agent’s context window before the agent does any work, and responses return every field, whether the agent needs them or not. Simple tasks require multiple sequential calls, and the agent must pass context between each one.

Products that serve agents well provide dedicated agent interfaces, not just repurposed APIs. Cloudflare’s [EmDash CMS](https://blog.cloudflare.com/emdash-wordpress/), for example, ships with MCP, CLI, and LLM-ready documentation, enabling AI agents to manage content alongside human editors.

## The Right Interface for Each Persona

Products that present the right interface to each persona win adoption that spreads across the organization. A security exec needs a different view than a SOC analyst, who needs a different workflow than a GRC manager. AI agents are another persona in this mix, with their own requirements for structured data and efficient access. When each role finds value in its own view, displacing the product means a competitor has to win over every persona at once.

Getting personas right demands industry expertise, customer conversations, and product telemetry. Building usable security products starts with [deep knowledge of who will use them and how](/what-is-security-product-manager). But talking to customers isn’t enough on its own. Usage telemetry reveals which features users adopt, where they encounter friction, and which capabilities they ignore. That data feeds back into the product. More usage generates better telemetry, which drives better features, which drives more usage. Each cycle sharpens the product’s fit with how each persona actually works.

## Anticipate What Users Need Next

The best products anticipate what each user needs and present it as the default action. For human users, the interface should present the recommended next step with enough context that the user feels confident clicking “OK.” The user can adjust, but the default should be right most of the time.

AI agents need the same anticipatory design, delivered through APIs and MCP servers. For example, the [REMnux MCP server](/ai-malware-analysis-remnux) guides AI agents through malware analysis. It recommends which tools to run, how to interpret output, and when to reconsider conclusions. When the MCP server detects a packed executable, it steers the agent away from tools that won’t help. It recommends unpacking first.

## Visibility Has to Match the Persona

[Anton Chuvakin and Oliver Rochford found](https://medium.com/anton-on-security/on-trust-and-transparency-in-detection-52ae6a29afdf) that even a few visible false positives can erode trust in correct detections. When products surface every detail behind every automated decision, users stop paying attention, just as they do with excessive alerts.

Transparency matters, but different audiences need different forms of it. For example, when a security tool blocks a suspicious email:

* A human analyst might need to know which rule fired, what the ML model flagged, or whether similar messages were also blocked.
* An AI agent triaging the same alert needs structured metadata to decide its next autonomous action, not a prose explanation that burns tokens.
* A legal team needs documented evidence showing why the product blocked it and whether anyone could have overridden the decision.

Each audience defines “useful detail” differently, and a product that serves only one leaves a usability gap that the others will notice.

## The Feature List Doesn’t Matter If Nobody Uses It

Product managers who want to treat usability as a competitive advantage should ask these questions about their product:

* Does it present the right interface for each persona?
* Does it anticipate what users need next?
* Does it explain automated decisions in a way that each audience can act on?
* Can AI agents interact with it efficiently and effectively?

A product that humans adopt and agents can operate has a competitive advantage that a feature list alone can’t match.

ShareCopy link

More on

[Product Management](/topic/product-management)[Artificial Intelligence](/topic/artificial-intelligence)

After 6+ years building the security program at [Axonius](https://www.axonius.com/) from startup to scale, I'm exploring what's next. As I work on independent projects, I'm open to CISO or security product leadership roles where technical depth enables business growth. To talk, reach out on [LinkedIn](https://www.linkedin.com/in/lennyzeltser/) or email me at *my first name* at *my last name* dot com.

4 min to read

April 6, 2026

### About the Author

Lenny Zeltser is a cybersecurity executive with deep technical roots, product management experience, and a business mindset. He has built security products and programs from early stage to enterprise scale. He is also a Faculty Fellow at SANS Institute and the creator of REMnux, a popular Linux toolkit for malware analysis. Lenny shares his perspectives on security leadership and technology at [zeltser.com](/).

[Learn more →](/about)

© 2026 Lenny Zeltser