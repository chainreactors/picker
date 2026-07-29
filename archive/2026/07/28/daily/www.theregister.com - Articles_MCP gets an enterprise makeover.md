---
title: MCP gets an enterprise makeover
url: https://www.theregister.com/ai-and-ml/2026/07/29/mcp-gets-an-enterprise-makeover/5280027
source: www.theregister.com - Articles
date: 2026-07-28
fetch_date: 2026-07-29T05:04:45.870879
---

# MCP gets an enterprise makeover

[Jump to main content](#main)

Search

TOPICS

* Security
  + [All Security](/security)
  + [Cyber-crime](/cyber_crime)
  + [Patches](/patches)
  + [Research](/research)
  + [CSO](/cso)
* Off-Prem
  + [All Off-Prem](/off_prem)
  + [Edge and IoT](/edge_iot)
  + [Channel](/channel)
  + [PaaS and IaaS](/tag/paas-iaas)
  + [SaaS](/saas)
* On-Prem
  + [All On-Prem](/on_prem)
  + [Systems](/systems)
  + [Storage](/storage)
  + [Networks](/networks)
  + [HPC](/hpc)
  + [Personal Tech](/personal_tech)
  + [Cx0](/cxo)
  + [Public Sector](/public-sector)
* Software
  + [All Software](/software)
  + [AI and ML](/tag/ai%20and%20ml)
  + [Applications](/applications)
  + [Databases](/databases)
  + [DevOps](/devops)
  + [OS Platforms](/tag/os%20platforms)
  + [Virtualization](/virtualization)
* Offbeat
  + [All Offbeat](/offbeat)
  + [Columnists](/columnists)
  + [Science](/science)
  + [BOFH](/bofh)
  + [Legal](/legal)
  + [Site News](/site_news)
  + [About Us](https://www.theregister.com/about_us)

* Special Features
  + [All Special Features](/special_features)
  + [HPE: AI Explainers](/explainer/ai-explainer)
  + [RSA Conference](/special_features/rsa)
  + [Agentic AI](/special_features/agentic_ai)
  + [The Future of the Datacenter](/special_features/future_of_the_datacenter)
  + [AWS:Reinvent](/special_features/aws_reinvent)
  + [Nvidia GTC](/special_features/nvidia_gtc)
  + [Supercomputing Month](/special_features/2025_11_supercomputing_month)
  + [Computex 2026](/special_features/computex)
  + [AI Infrastructure Month 2026](/special_features/ai_infrastructure_month_2026)
  + [The State of Storage 2026](/special_features/state_of_storage_2026)
* Vendor Voice
  + [All Vendor Voice](https://vendorvoice.theregister.com/)
  + [Modernizing Financial Services with FIS and AWS](https://vendorvoice.theregister.com/aws_fis_capital_markets/)
  + [Barco](https://vendorvoice.theregister.com/barco/)
  + [Infinidat](https://vendorvoice.theregister.com/infinidat/)
  + [Everpure](https://vendorvoice.theregister.com/everpure/)
  + [Rubrik](https://vendorvoice.theregister.com/rubrik/)
  + [Make it real with Capgemini and AWS](https://vendorvoice.theregister.com/aws_capgemini/)
  + [Money Movement Hub](https://vendorvoice.theregister.com/aws_fis/)
  + [ZTE](https://vendorvoice.theregister.com/zte_news_and_stories/)
  + [Nutanix: Scale Kubernetes. Not Chaos.](https://vendorvoice.theregister.com/nutantix_cloud_native_apps/)
  + [AWS New Horizon](https://vendorvoice.theregister.com/aws_new_horizon/)
  + [Digicert](https://vendorvoice.theregister.com/digicert)
  + [Netscout](https://vendorvoice.theregister.com/netscout)
* Resources
  + [Intelligence](https://intelligence.theregister.com)
  + [Webinars & Events](https://intelligence.theregister.com/events/list/)
  + [Newsletters](https://account.theregister.com/login?r=https%3A%2F%2Faccount.theregister.com%2Fedit%2Fnewsletter%2F)

Search

[![Go to frontpage. Logo, The Register](/view-resources/dachser2/public/theregister/logo.svg)](https://www.theregister.com)

[![Go to frontpage. Logo, The Register](/view-resources/dachser2/public/theregister/logo.svg)](https://www.theregister.com)

[![Go to frontpage. Logo, The Register](/view-resources/dachser2/public/theregister/logo.svg)](https://www.theregister.com)

* [Sign in](https://account.theregister.com/login)
  + [Sign in](https://account.theregister.com/login)

* [AI](/tag/ai%20and%20ml)
* [Security](/security)
* [Microsoft](/tag/microsoft)
* [AWS](/tag/aws)
* [Developer](/tag/developer)
* [Open Source](/tag/open%20source)
* [Columnists](/tag/columnists)
* [BOFH](/tag/bofh)
* [Who, Me?](/tag/who%20me)
* [On Call](/tag/on%20call/)

REG AD

AI and ML

# MCP gets an enterprise makeover

Now happier running in a conventional K8s environment, with `an easier-to-live-with lifecycle

Thomas Claburn
[Thomas
Claburn](https://www.theregister.com/author/thomas-claburn)
AI AND SOFTWARE REPORTER

Published
wed 29 Jul 2026 // 00:08 UTC

The Agentic AI Foundation, part of the Linux Foundation, has released an update to the Model Context Protocol (MCP) that aims to help enterprises adopt AI-based automation.

Open-sourced by Anthropic in November 2024, [MCP](https://www.theregister.com/software/2025/04/21/what-is-mcp/1105570) provides a way for AI applications (agents) based on models like GPT-5.6 Sol or Claude Opus 5 to connect to existing data sources, tools, or other applications. It defines how content is exchanged in a client-server architecture.

"The new release is MCP’s most important since remote MCP first launched over a year ago," wrote David Soria Parra, a member of technical staff at Anthropic and co-inventor of MCP, in a [blog post](https://blog.modelcontextprotocol.io/posts/2026-07-28/). "It is a leap in serving scalable MCP servers and takes all the lessons learned over the last 18 months to provide a robust foundation for MCP’s future."

REG AD

The [latest version](https://modelcontextprotocol.io/docs/2026-07-28/getting-started/intro) of the specification [does away with the legacy stateful architecture](https://www.theregister.com/devops/2026/07/23/model-context-protocol-prepares-to-break-with-its-stateful-past/5276722), making it more like HTTP services where network requests do not need to retain the state of the session.

REG AD

"Historically, running MCP at scale required sticky routing or shared state to maintain continuity across sessions," explained Caitie McCaffrey, a Microsoft software engineer and core MCP maintainer, in a [blog post](https://aaif.io/blog/mcp-graduates-to-enterprise-infrastructure-stateless-architecture-formal-governance-and-security). "This made large-scale production deployments complex to implement and operate even when the capabilities being exposed were stateless."

The [revised protocol](https://github.com/modelcontextprotocol/modelcontextprotocol/pull/2575) changes the underlying architecture to eliminate the overhead of managing session state, which allows organizations to run MCP servers behind standard load balancers on existing Kubernetes and DevOps tooling.

The version 2026-07-28 release also includes a [Specification Feature Lifecycle and Deprecation Policy](https://modelcontextprotocol.io/seps/2596-spec-feature-lifecycle-and-deprecation#sep-2596-specification-feature-lifecycle-and-deprecation-policy), because large companies want clear roadmaps and timelines when it comes to software changes.

## MORE CONTEXT

* [### Perplexity's tokenmaxxing Model Council gives you multiple bot perspectives](/ai-and-ml/2026/07/28/perplexitys-tokenmaxxing-model-council-gives-you-multiple-bot-perspectives/5279972)
* [### War machines can run amok with AI in control](/ai-and-ml/2026/07/28/war-machines-can-run-amok-with-ai-in-control/5279937)
* [### Microsoft and Wiz mind-meld agents catch more than 90% of bugs](/security/2026/07/28/microsoft-and-wiz-mind-meld-agents-catch-more-than-90-of-bugs/5279914)
* [### AI is storage’s biggest opportunity - and biggest threat](/storage/2026/07/28/ai-is-storages-biggest-opportunity-and-biggest-threat/5279607)

"The goal is a predictable timeline that SDK authors and implementers can plan migrations against when protocol surface area is retired," the documentation explains.

The revised spec comes with a new policy that guarantees a minimum period of 12 months between feature deprecation and removal, which should please enterprise engineering teams, since they'll need to make fewer updates to MCP servers.

On the security front, the latest spec revision adds Specification Enhancement Proposal (SEP) [2468](https://modelcontextprotocol.io/seps/2468-recommend-issuer-claim-for-auth#sep-2468-recommend-issuer-iss-parameter-in-mcp-auth-responses), which calls for the inclusion and validation of an issuer (iss) parameter in authorization responses. This should help prevent [OAuth Mixup Attacks](https://datatracker.ietf.org/doc/html/rfc9207).

An attack of this sort can occur when an OAuth client connects to multiple OAuth prov...