---
title: AI Governance on AWS: The Runtime Control Loop: AI Governance on AWS: Four Functions, One Loop, and a Deadline That Already Passed
url: https://lab.wallarm.com/runtime-ai-governance-aws-control-loop/
source: Wallarm
date: 2026-09-30
fetch_date: 2026-10-01T07:59:03.515865
---

# AI Governance on AWS: The Runtime Control Loop: AI Governance on AWS: Four Functions, One Loop, and a Deadline That Already Passed

[Register now —>](https://www.wallarm.com/regular-live-demo)

Join [Wallarm regular demo](https://www.wallarm.com/regular-live-demo)

[Live demo](https://www.wallarm.com/regular-live-demo)

Join [Wallarm regular demo](https://www.wallarm.com/regular-live-demo)
[Register now—>](https://www.wallarm.com/regular-live-demo#weekly-demo-form)

[Wallarm](https://lab.wallarm.com "Go to Wallarm.") — [AI Security](https://lab.wallarm.com/category/ai-security/ "Go to the AI Security category archives.") — AI Governance on AWS: The Runtime Control Loop: AI Governance on AWS: Four Functions, One Loop, and a Deadline That Already Passed

In
[AI Security](https://lab.wallarm.com/category/ai-security/)

# AI Governance on AWS: The Runtime Control Loop: AI Governance on AWS: Four Functions, One Loop, and a Deadline That Already Passed

[September 30, 2026](https://lab.wallarm.com/runtime-ai-governance-aws-control-loop/)

6 Mins Read

[![AI Governance on AWS: The Runtime Control Loop Blog](data:image/svg+xml... "AI Governance on AWS: The Runtime Control Loop: AI Governance on AWS: Four Functions, One Loop, and a Deadline That Already Passed")](https://i0.wp.com/lab.wallarm.com/wp-content/uploads/2026/09/blog-feature-image_AWS.png?fit=2080%2C1390&ssl=1)

Answer this without checking: how many AI agents are running in your environment right now?

Most security leaders give an estimate and a shrug. That is a fair response, because agents get spun up by an engineer solving a problem on a Tuesday afternoon, through a path that puts them on nobody's radar. In August 2026, researchers found AI agents connected to Hugging Face running loose inside enterprise networks with no owner and no audit trail. We wrote about that incident in AI Agent Security Readiness, and the detail that should worry you is this: the agents were known. What nobody could see was what they were actually doing, until it was already done.

That gap has a shape, and it is measurable. Generative AI was the top 2025 budget priority for 45% of the IT decision-makers AWS surveyed for its Generative AI Adoption Index, ahead of security tools at 30%. McKinsey finds 88% of organizations now use AI in at least one business function, while only 30% have reached meaningful AI governance maturity. Money moved first. Deployment followed. Governance is still assembling itself.

Tim Erlin, VP of Product at Wallarm, and Aliaksei Ivanou, Worldwide Security and Identity Senior Partner Solutions Architect at AWS, spent a recent webinar on how to close that distance. Here is the argument they landed on, and why the four functions only work when they run as one loop.

## The Layer Your Existing Controls Cannot See

Defense in depth still applies. AI stacks a new floor on top of it: the AI application layer.

Your infrastructure and identity controls were built to answer different questions. They miss prompt injection, because it arrives looking like normal HTTPS traffic. They stay quiet when an agent quietly exceeds its authorized scope, because the request was technically authorized. Ivanou put the organizational version of this plainly: "Most organizations have adopted AI in some form. But very few have structured governance around it. The adoption pressure from the business is real. Security teams are trying to catch up."

We have watched this pattern before. As we argued in [From Shadow APIs to Shadow AI](https://lab.wallarm.com/shadow-ai-api-security-risk/), shadow AI is the shadow API problem running at higher speed, with autonomous action and machine-to-machine decisions raising what a single gap costs you.

## **Three Questions Before You Build**

Ivanou's framework starts with what you are building. AWS sorts AI workloads into three use cases, each inheriting everything the previous one demanded.

**AI that answers** generates responses with no connection to external data. Even here, prompts leak information you did not intend to expose, and unsanctioned use spreads quietly.

**AI that connects** reaches into enterprise data, which turns every query into an access request. When it returns data a user should never see, your access model has already broken, silently.

**AI that acts** hands agents the ability to decide, call APIs, and coordinate with each other. One misconfigured agent repeats bad permissions at machine speed.

"You don't start fresh when you move from a chatbot to an agent," Ivanou said. "You add layers."

Then, where do the controls live? Infrastructure asks whether the environment is isolated and hardened. Identity and data asks who this is and whether they are allowed, now including non-human identities, since an agent needs credentials scoped to itself instead of a copy of a human's. The AI application layer asks whether what happens at the model boundary is safe and intended.

And where are you in the journey? Teams prototyping build security in through configuration. Teams moving to production add threat detection and incident response. Teams at scale automate governance, because manual review stops functioning there.

Ivanou's summary of all three: "You aren't adding security to AI. You are building AI on top of security."

## **The Loop Is the Unit**

Erlin layered four capability pillars on top of that framework. They are the operating model behind the [Wallarm AI Control Platform](https://lab.wallarm.com/introducing-the-wallarm-ai-control-platform-one-closed-loop-for-ai-security-and-api-security/), which launched with Infrastructure Discovery for your AWS estate and AI Hypervisor for what the AI does inside it. Ivanou mapped it to AWS's own instincts: "Visibility, monitoring, enforcement, and evidence. Same principles apply to AI."

Read the four functions separately and they look like four purchase orders. Run them separately and each one hollows out. Discovery with no enforcement produces a report. Enforcement with no evidence fails the audit. Evidence with no runtime observation is attestation theater. The loop is what makes any of it hold.

**Discover**. Engineers stand up AI services and agents call [MCP tools](https://www.wallarm.com/what/what-is-model-context-protocol-mcp) without security knowing. Coverage has to include the AI objects (agents, LLM providers, MCP servers, data sources) and the infrastructure carrying them (accounts, VPCs, EKS clusters, APIs, Lambda functions, load balancers). On AWS, the Amazon Bedrock AgentCore agent registry catalogs natively built agents and CloudTrail captures every Bedrock and SageMaker invocation. The moment you add an external provider, you need visibility at the network layer.

[Wallarm Infrastructure Discovery](https://www.wallarm.com/product/infrastructure-discovery) scans every registered account and region through cross-account IAM role assumption, detects drift when configurations change, and places ingested Security Hub findings on the graph node they affect, with CloudTrail attribution naming who created each asset. [AI Hypervisor](https://docs.wallarm.com/ai-hypervisor/overview/) builds a live registry from observed traffic. It runs as a Kubernetes DaemonSet on Amazon EKS, attaching through eBPF and non-invasive memory analysis with no SDK, sidecar, code change, or pod restart. Every asset it finds lands in one of three governance states: sanctioned, tolerated, or unsanctioned.

**Observe**. Discovery produces a list. Observation produces a chain: the prompt that started it, the agent or model it reached, the internal API it touched, the MCP server it passed through, the database it queried, the external LLM it called outside your environment entirely. "A single user request can trigger a chain of actions," Ivanou noted. AWS instruments this deeply through CloudTrail, Bedrock invocation logs, GuardDuty, and full session tracing for agents built on AgentCore.

His question for the room was the useful one: "Do all your AI workloads run through that instrumented path?" For everything outside it, AI Hypervisor watches at the connection ...