---
title: A Practitioner's Guide for Creating Cybersecurity Products
url: https://zeltser.com/security-product-creation-framework/
source: Lenny Zeltser
date: 2026-03-04
fetch_date: 2026-03-05T04:07:37.014511
---

# A Practitioner's Guide for Creating Cybersecurity Products

[Lenny Zeltser](/)Security builder & leader

 [Projects](/projects) [Writing](/writing) [About](/about)

# A Practitioner's Guide for Creating Cybersecurity Products

Strong technology alone doesn't make a successful security product. This guide presents the strategic questions that security product managers and startup founders should answer early, covering market segmentation, AI advantages, go-to-market strategy, pricing, delivery, customer trust, and ecosystem positioning.

![A Practitioner's Guide for Creating Cybersecurity Products - illustration](/assets/security-product-creation-framework.oEFOJiWd_24Yg3w.webp)

If you’re working to create or improve your security product strategy, this guide will help [startups and teams in established organizations](/security-product-management-large-companies-vs-startups). Having a strong value proposition is necessary but not sufficient to build a successful product. Vendors often stumble because the team didn’t ask the right questions early enough. The following framework presents those questions, drawing on my experience as a CISO practitioner and a security product manager.

* [Strategic Market Segmentation](#strategic-market-segmentation)
* [Product Capabilities](#product-capabilities)
* [Sales Engagement and Go-To-Market](#sales-engagement-and-go-to-market)
* [The Pricing Model](#the-pricing-model)
* [Product Delivery and Operations](#product-delivery-and-operations)
* [Earning Customers’ Trust](#earning-customers-trust)
* [Platform Strategy and Ecosystem Positioning](#platform-strategy-and-ecosystem-positioning)
* [Bringing It All Together](#bringing-it-all-together)

## Strategic Market Segmentation

The idea of market segmentation stems from the notion that different customer types have distinct needs. How to group customers with similar needs depends on your vision for the company and its products:

* Geographic segmentation recognizes that product requirements differ across regions. A startup often begins with customers in its own locale, where the founders’ familiarity builds credibility before expanding to a broader market.
* Industry segmentation groups customers by vertical. A company building an anti-ransomware product might focus on hospitals or law firms, where the need is acute, rather than financial services firms that value different capabilities and would overextend a startup’s resources.
* Size-based segmentation considers the number of devices, employees, or workloads that need protection. Smaller businesses have different security needs and price expectations than enterprises. The expected deal size also affects whether you can build and motivate a sales force to reach those customers.

Also consider who inside the customer’s organization will evaluate, champion, and use your product. A CISO evaluates risk reduction and vendor trust differently than a security engineer assessing daily workflow fit. Both differ from a developer evaluating friction in a deployment pipeline. Your product capabilities, messaging, and sales motion all shift depending on which persona you’re building for. This distinction becomes especially important if you pursue a bottom-up adoption model, which is discussed later in this guide.

*Questions on market segmentation:*

* Which geographic, industry, and size-based segments will you target first?
* How do security needs and price expectations differ across those segments?
* Does your expected deal size support the sales force needed to reach those customers?
* Which personas will evaluate, champion, and use your product, and how do their priorities differ?

## Product Capabilities

Once you understand the type of customers the product will target, dig deeper into their needs, and then map them to the product’s capabilities. Think beyond generic security requirements such as data protection, threat detection, or incident response. Be more specific to understand which gaps might exist in the products currently available to relieve infosec-related pain points.

### AI and Data Advantages

If your product incorporates AI capabilities, what specific advantages does it offer over rule-based detection systems? Think about a scenario in which a company offering a frontier model adds capabilities similar to your solution. Make sure you provide unique value to customers even in that scenario. Also, if your product depends heavily on third-party AI models, understand your cost structure and how it might affect your burn rate and product pricing.

The most durable AI advantage in security products often comes from proprietary data that frontier model vendors lack. Raw telemetry is relatively easy to collect, but the real moat lies in labeled threat datasets, curated detection rules, and validated ground truth. A growing customer base can also create network effects, where each new deployment improves detection accuracy for everyone, provided your product architecture supports learning across customers.

Think carefully about which data assets your company can accumulate that others will find difficult to replicate. Building this data flywheel requires earning customers’ trust. As organizations become more cautious about how vendors use their telemetry, you should be transparent about what data you collect, how you train your AI models, and what controls customers have over their data.

> CrowdStrike’s Threat Graph, which aggregates correlated telemetry from all Falcon agents, illustrates this dynamic. Its detection improves with every deployment because it correlates telemetry across its entire customer base. Each new customer [adds behavioral patterns and threat data that sharpen detection for all the others](https://seekingalpha.com/article/4857835-crowdstrike-the-hidden-network-effect-in-cybersecurity). A general-purpose AI model can’t replicate that feedback loop on its own because the value comes from the data, not the model.

*Questions on AI and data advantages:*

* How does your AI advantage hold up if a frontier model vendor adds similar capabilities?
* What proprietary data can you accumulate that others will find difficult to replicate?

### Designing for AI Agents

Your product’s users will likely include AI agents, not just people. For example, a customer’s automated workflow might query your product’s API to check an asset’s risk posture, then feed that data into a decision engine that prioritizes remediation. Design your APIs and automation interfaces so that AI agents can interact with your product as effectively as a human analyst using the console. Consider the role your product will play in these automated workflows, and ensure your value proposition holds up when the AI “user” is software acting on behalf of a security team.

Designing for agent users raises questions that don’t arise when your product serves only human users. How will agents authenticate to your product, and how will customers govern what those agents are permitted to do? Most vendors today rely on API keys or service account tokens that struggle with granular scoping and audit trails that agent workflows will eventually require. Getting ahead of this challenge, even modestly, can differentiate your product.

Agent users also affect your pricing and competitive positioning. If customers meter their agent workflows by API call volume, your pricing model needs to accommodate that usage pattern. When an automated workflow chains your product with several others, your differentiation can become invisible to customers. Ensure your product delivers value that is apparent in the data it returns, not only in the experience of using its console.

*Questions on designing for agents:*

* Can AI agents interact with your product as effectively as human analysts?
* How will agents authenticate, and how will customers govern what they can do?

### Competitive Positioning

If you’ve spotted a customer need, others may be racing to address it. Understand who your competitors are and be realistic ...