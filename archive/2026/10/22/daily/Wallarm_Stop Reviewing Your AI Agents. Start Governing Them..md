---
title: Stop Reviewing Your AI Agents. Start Governing Them.
url: https://lab.wallarm.com/stop-reviewing-your-ai-agents-start-governing-them/
source: Wallarm
date: 2026-10-22
fetch_date: 2026-10-23T06:45:34.629295
---

# Stop Reviewing Your AI Agents. Start Governing Them.

[Register now —>](https://www.wallarm.com/regular-live-demo)

Join [Wallarm regular demo](https://www.wallarm.com/regular-live-demo)

[Live demo](https://www.wallarm.com/regular-live-demo)

Join [Wallarm regular demo](https://www.wallarm.com/regular-live-demo)
[Register now—>](https://www.wallarm.com/regular-live-demo#weekly-demo-form)

[Wallarm](https://lab.wallarm.com "Go to Wallarm.") — [API Security](https://lab.wallarm.com/category/api-security/ "Go to the API Security category archives.") — Stop Reviewing Your AI Agents. Start Governing Them.

In
[API Security](https://lab.wallarm.com/category/api-security/)

# Stop Reviewing Your AI Agents. Start Governing Them.

[October 22, 2026](https://lab.wallarm.com/stop-reviewing-your-ai-agents-start-governing-them/)

3 Mins Read

[![blog post ai control loop](data:image/svg+xml... "Stop Reviewing Your AI Agents. Start Governing Them.")](https://i0.wp.com/lab.wallarm.com/wp-content/uploads/2026/10/blog-feature-image_Brookings.png?fit=2080%2C1390&ssl=1)

*Brookings and the World Economic Forum say agent governance must be continuous, scoped in advance, evidenced, and monitored at runtime. We think that bar is correct, and that most organizations are nowhere near it.*

Most of what companies call AI agent governance today is paperwork.

A review board approves the use case. A policy document says agents must follow least privilege. A risk assessment gets filed. Then the agent ships, and nobody can say what it actually did on Tuesday.

That isn't governance. It's a record of good intentions, and the latest Brookings and World Economic Forum analysis explains why it's no longer enough.

In ["Shaping global governance of AI agents"](https://www.brookings.edu/articles/shaping-global-governance-of-ai-agents/), Landry Signé and Karla Yee Amezaga argue that the central question has changed. It is no longer only what the model said. It is "what the system did, why it was allowed to do it, and who is accountable." Their conclusion: governance "must become continuous, with permissions scoped in advance, traceable evidence, and runtime monitoring replacing stage-based oversight."

**If you can't show what an agent did, why it was allowed to, and who answers for it, you are not governing that agent. You are hoping.**

## **The checkpoint model is broken**

Stage-based oversight assumed a human sat between a model and anything consequential. Review the output, then act. Agents remove that gap on purpose. As the authors note, a chatbot can be reviewed before action is taken, but agents "are structured specifically to invoke another system or action before a human intervenes."

Once an agent holds tools and permissions, it starts to resemble a delegated decision-maker, with risks like behavioral drift and tool misuse. Those risks appear after deployment, at runtime. A pre-launch review can't catch them, however thorough it was.

The scale makes the gap worse. Gartner predicts the average Fortune 500 enterprise will have more than 150,000 AI agents by 2028, while only 13% of organizations believe they have the right governance in place today. Nobody is going to review 150,000 agents by committee.

And don't count on regulation to fill the gap soon. The authors point out that the EU's high-risk AI rules are delayed until December 2027 and August 2028, so "organizational controls rather than law will govern agents in high-stakes domains for now." Your controls are the only controls. That makes this a security and compliance problem today.

## **Four positions we'll defend**

The Brookings/WEF language maps onto the four steps of the [Wallarm AI Control Loop](https://www.wallarm.com/platform): Discover, Observe, Enforce, Govern. For each, here is where we stand.

### **1. Discover: inventory is the first security control, not a housekeeping task.**

Brookings calls for "permissions scoped in advance." You cannot scope permissions for an agent you don't know exists. Yet many teams still can't list the agents, MCP servers, model providers, and tools running in their own environment, or say who stood them up. Shadow AI is not an edge case. It is the default state of any fast-moving estate. If your discovery is a quarterly spreadsheet, your governance starts out wrong.

### **2. Observe: governance without runtime evidence is guesswork.**

The authors call for runtime monitoring and end-to-end tracing. We'd add a caution: visibility that depends on every agent being configured to route through one choke point has holes exactly where drift and tool misuse happen, in agent-to-tool and agent-to-agent traffic. Real observation means seeing what workloads actually send, not what they were supposed to send.

### **3. Enforce: policy that can't act at agent speed is a suggestion.**

Runtime governance has to keep pace with "autonomous decisions happening in seconds," in the authors' words. A ticket queue doesn't. If the only response to a policy violation is an alert someone reads tomorrow, you have monitoring, not control. Enforcement means blocking the violation and cutting off the misbehaving session while it is happening.

### **4. Govern: evidence is the product. Everything else is a means to it.**

The authors list "logging, auditability, and redress" as core to runtime governance. We'd go further: the test of a governance program is whether you can answer an auditor, a regulator, or your board from runtime records, without reconstructing a story after the fact. What changed, who changed it, what data moved where, which policy applied. If that takes a project, you don't have governance yet.

## **The loop is the point**

These are not four separate purchases or four separate teams. Discovery feeds observation. Observation shows enforcement what to act on. Enforcement produces the evidence that governance runs on. Break any link and the rest degrades.

That is also why the common approach fails. Most organizations assemble this from disconnected tools: AI security products that focus on models and miss the APIs connecting them to the business, cloud posture tools that see infrastructure but not runtime behavior, and governance platforms that define policy but can't enforce it. Each tool covers one piece. None of them closes the loop. The result is fragmented visibility, inconsistent enforcement, and governance that exists on paper.

We built [Wallarm](https://www.wallarm.com) on the opposite premise: runtime behavior determines real risk, and governance has to be demonstrated, not declared. That is what the [Wallarm platform](https://www.wallarm.com/platform) and its AI Control Loop are for.

* **Discover:** [Infrastructure Discovery](https://www.wallarm.com/product/infrastructure-discovery) ([docs](https://docs.wallarm.com/infrastructure-discovery/overview)) maps AWS-native estates read-only, including Bedrock models, agents, and knowledge bases, with per-asset creator attribution and field-level change history. [AI Hypervisor](https://www.wallarm.com/product/ai-hypervisor) ([docs](https://docs.wallarm.com/ai-hypervisor/overview)) maintains a registry of agents, MCP servers, providers, and tools, and flags workloads reaching unregistered AI providers.
* **Observe:** [Kernel-level runtime visibility](https://docs.wallarm.com/ai-hypervisor/overview) into what AI workloads actually send, including internal AI-to-AI and agent-to-tool traffic, without rerouting it through a gateway.
* **Enforce:** Inline policy enforcement and in-kernel session revocation, with no pod restart required.
* **Govern:** Continuous compliance reporting, session logs, and records of which sensitive data moved to which destination (see the [findings and risk model](https://docs.wallarm.com/ai-hypervisor/findings)).

## **What to do this quarter**

If you run security or compliance for an organization deploying agents, three questions are worth asking before your next review meeting:

1. Can we list every agent, tool, and AI provider in our environment tod...