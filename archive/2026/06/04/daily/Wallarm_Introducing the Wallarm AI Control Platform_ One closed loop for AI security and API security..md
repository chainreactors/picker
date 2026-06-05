---
title: Introducing the Wallarm AI Control Platform: One closed loop for AI security and API security.
url: https://lab.wallarm.com/introducing-the-wallarm-ai-control-platform-one-closed-loop-for-ai-security-and-api-security/
source: Wallarm
date: 2026-06-04
fetch_date: 2026-06-05T06:12:58.322475
---

# Introducing the Wallarm AI Control Platform: One closed loop for AI security and API security.

[Register now —>](https://www.wallarm.com/regular-live-demo)

Join [Wallarm regular demo](https://www.wallarm.com/regular-live-demo)

[Live demo](https://www.wallarm.com/regular-live-demo)

Join [Wallarm regular demo](https://www.wallarm.com/regular-live-demo)
[Register now—>](https://www.wallarm.com/regular-live-demo#weekly-demo-form)

[Wallarm](https://lab.wallarm.com "Go to Wallarm.") — [AI Security](https://lab.wallarm.com/category/ai-security/ "Go to the AI Security category archives.") — Introducing the Wallarm AI Control Platform: One closed loop for AI security and API security.

In
[AI Security](https://lab.wallarm.com/category/ai-security/)

# Introducing the Wallarm AI Control Platform: One closed loop for AI security and API security.

[June 2, 2026](https://lab.wallarm.com/introducing-the-wallarm-ai-control-platform-one-closed-loop-for-ai-security-and-api-security/)

5 Mins Read

[![The Wallarm AI Control Loop](data:image/svg+xml... "Introducing the Wallarm AI Control Platform: One closed loop for AI security and API security.")](https://i0.wp.com/lab.wallarm.com/wp-content/uploads/2026/06/blog-feature-image_AICP-launch.png?fit=2080%2C1390&ssl=1)

```
TL;DR
- AI deployment has outpaced AI governance. Most enterprises running AI on AWS cannot answer four basic security questions about what's running, what it's doing,how to stop it, and how to prove it's under control.
- The Wallarm AI Control Platform closes this gap: one platform for Discover, Observe,Enforce, and Govern — running natively in your AWS environment.
- Infrastructure Discovery maps your AWS estate in minutes. AI Hypervisor instruments EKS in minutes with zero code changes, enforces at the kernel level, and generates continuous compliance evidence for EU AI Act and SOC 2.
```

Every week, someone in your organization stands up an AI service. Maybe they told security about it, but probably not. By the time it shows up in your inventory, it has been running for weeks, processing data, calling external APIs, and doing things nobody formally reviewed.

According to McKinsey, 88% of organizations now use AI in at least one business function, but only 30% have reached a meaningful level of maturity in AI governance.The gap between what security teams think is running and what is actually running compounds at AWS scale: a mid-size enterprise following AWS's recommended multi-account strategy runs 100 to 200 AWS accounts, each an independent security boundary, each able to spin up AI services in minutes without security's knowledge.

And the tools most teams are using were not built for this. SIEMs see logs after the fact. WAFs see HTTP payloads but not what the AI is actually deciding. GuardDuty fires alerts nobody can contextualize because nobody knows what workload was involved, who triggered it, or what it was doing at the time.

**Detection without context is noise. Noise without enforcement is a liability.**

## **What Four Questions Do AI Security Teams Need to Answer?**

When security teams start taking AI governance seriously, they run into the same four walls:

**What AI is actually running in our environment?** Not what was approved. Not what is in the manifest. What is actually running, including the services nobody told IT about.

**What is our AI doing at runtime?** Which agents are making calls to external services? What data are they touching? Which user triggered which chain of actions?

**Can we stop bad AI behavior before the damage is done?** Not log it. Not alert on it after the fact. Stop it, right now, at the connection level.

**Can we prove to auditors that our AI is under control?** EU AI Act enforcement starts in August 2026. Fines run up to 3% of global annual turnover for governance failures, and that is before you account for the third-party risk exposure. Every AI service that bypassed vendor review is also a potential unmanaged third-party relationship under OCC guidance, NYDFS Part 500, and model risk frameworks like SR 11-7. The question is not whether regulators care. It is whether you can show them a defensible record when they ask.

*If your honest answer to any of those is “not really,” you are not alone. But you are exactly who we built this for.*

## **What is the Wallarm AI Control Platform?**

![](https://i0.wp.com/lab.wallarm.com/wp-content/uploads/2026/06/image.png?resize=770%2C567&ssl=1)

The Wallarm AI Control Platform is a runtime AI governance platform that discovers, observes, enforces, and governs AI workloads across AWS environments. It’s the only platform that integrates AI security and API security into one closed loop. Wallarm has protected APIs for years. The same platform that secures the APIs underneath your AI now governs the AI itself. That continuity matters: you are not bolting on a new vendor for a new problem. You are extending a platform you already trust into the layer that sits above it.

The Wallarm AI Control Platform delivers what the industry has been missing: The Wallarm AI control loop (discover, observe, enforce, govern) automated and continuous. This is what AI governance in production looks like: not a compliance checkbox, but a continuously running control layer that gives every AI workload in your AWS estate a behavioral owner. Here is what that looks like in practice. A new AI agent spins up in an AWS account your security team does not know exists. Infrastructure Discovery finds it within minutes and surfaces it on the relationship graph, attributed to the engineer who created it. AI Hypervisor begins instrumenting it at the kernel level, tracing every call it makes to external services. When it routes a request that carries PII outside an approved boundary, the enforcement engine blocks it before it reaches the model provider. And the entire sequence is logged in the compliance record that will be ready when your auditor asks for it.

That loop does not require a ticket, a deploy cycle, or a security review that happens three sprints later. It closes automatically.

The AI Control Platform launches today with two products.

## **Infrastructure Discovery: The Territory Map**

![](https://i0.wp.com/lab.wallarm.com/wp-content/uploads/2026/06/image-1.png?resize=770%2C770&ssl=1)

Before you can govern your AI, you need to know what you have. And that does not just mean an inventory of AI agents. It means knowing every EKS cluster, Lambda function, API Gateway, VPC, and load balancer across every AWS account in your environment, because that is the infrastructure your AI workloads run on. If you cannot see the stack underneath the AI, you cannot govern the AI sitting on top of it.

That sounds obvious. It turns out to be genuinely hard at scale.

If you follow AWS’s recommended multi-account strategy, you might be running hundreds of AWS accounts. Each one is an independent security boundary. Each one can spin up EKS clusters, Lambda functions, AI agents, and model API integrations in minutes, often without security knowing it happened. And each undisclosed service is potentially a third-party vendor relationship that has not gone through your risk management process.

Infrastructure Discovery uses cross-account IAM role assumption to scan every registered AWS account, across every region, and builds a live relationship graph of everything it finds: compute, network, API Gateway, Lambda, and IAM resources, with CloudTrail attribution showing who created each asset. That shadow AI service spinning up in an account your team does not monitor surfaces within minutes, not weeks.

Discovery also makes your existing AWS security investments work harder. It syncs the findings Security Hub aggregates from GuardDuty, Inspector, IAM Access Analyzer, Macie, and AWS Config, placing each one directly on the relationship graph node it affects, rewritten in plain language so analysts can act on them. GuardDuty fired in account 847? You see which asset the finding is attached to, what it connects to, and who created it.

**...