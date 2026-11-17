---
title: Has AI’s ‘Black October’ changed the way you secure your code?
url: https://www.theregister.com/security/2026/11/16/partner-content-has-ais-black-october-changed-the-way-you-secure-your-code/5309775
source: www.theregister.com - Articles
date: 2026-11-16
fetch_date: 2026-11-17T09:57:53.514075
---

# Has AI’s ‘Black October’ changed the way you secure your code?

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
  + [Supercomputing](/special_features/supercomputing_month_2026)
  + [BOFH](/bofh)
  + [Legal](/legal)
  + [Site News](/site_news)
  + [About Us](https://www.theregister.com/about_us)

* Special Features
  + [All Special Features](/special_features)
  + [SC 26](/special_features/sc26)
  + [Supercomputing Month 2026](/special_features/supercomputing_month_2026)
  + [Nvidia GTC Berlin 2026](/special_features/nvidia_gtc_berlin_2026)
  + [Cybersecurity Month 2026](/special_features/cybersecurity_month_2026)
  + [VMware Explore 2026](/special_features/vmware_explore_2026)
  + [Cloud Infrastructure Month 2026](/special_features/cloud_infrastructure_month_2026)
  + [HPE: AI Explainers](/explainer/ai-explainer)
  + [Agentic AI](/special_features/agentic_ai)
  + [The Future of the Datacenter](/special_features/future_of_the_datacenter)
  + [AWS:Reinvent](/special_features/aws_reinvent)
  + [Nvidia GTC](/special_features/nvidia_gtc)
  + [Computex 2026](/special_features/computex)
  + [AI Infrastructure Month 2026](/special_features/ai_infrastructure_month_2026)
  + [The State of Storage 2026](/special_features/state_of_storage_2026)
  + [RSA Conference](/special_features/rsa)
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

* [AI](/tag/ai%20and%20ml)
* [Security](/security)
* [Software](/software)
* [Microsoft](/tag/microsoft)
* [Developer](/devops)
* [Open Source](/tag/open%20source)
* [BOFH](/tag/bofh)
* [Who, Me?](/tag/who%20me)
* [On Call](/tag/on%20call/)
* [Supercomputing](/special_features/supercomputing_month_2026)

security

# Has AI’s ‘Black October’ changed the way you secure your code?

PARTNER CONTENT: AI agents are making security vulnerabilities easier to find and exploit in your code. Software engineering and application security teams need new ways to find and fix them

Sahil M Bansal
Sahil M
Bansal
CodeRabbit

Published
mon 16 Nov 2026 // 16:00 UTC

[Make us preferred on Google](https://google.com/preferences/source?q=theregister.com)

October ’26 might be remembered as a seminal moment for software developers and application security teams. AI agents are investigating unfamiliar systems, testing ways to get in and adjusting their next move when an attempt fails. Anyone with a credit card can use that capability to come after your application.

Coding agents and their tool integrations have introduced new entry points and surface areas that can be exploited. [Pillar’s OpenCode disclosure in October](https://www.pillar.security/blog/open-and-shut-remote-code-execution-in-opencode-via-mcp-oauth) showed how a malicious Model Context Protocol (MCP) server could execute commands on a developer’s Windows or WSL machine during authentication. A server-supplied URL reached a shell without tricking the model. In the same month, the discovery of the two [PHP2Shell](https://openai.com/index/coordinated-disclosure-of-critical-vulnerabilities/) vulnerabilities, remote code execution bugs in the PHP runtime uncovered with the help of OpenAI’s models, brought new urgency to securing longstanding code across much of the internet.

[Microsoft revealed](https://www.microsoft.com/en-us/security/blog/2026/11/05/threat-actors-use-agentic-ai-tooling-to-find-and-abuse-exposed-secrets/) that an agent moved from searching GitHub for exposed credentials to stealing Azure Key Vault data in five minutes. When its cloud API requests failed, the agent corrected the API versions and tried again until they succeeded.

[A report by Anthropic](https://www.anthropic.com/threat-intelligence-report-september-2026) described individual operators using agent frameworks for multi-victim campaigns that previously required specialist teams. Agents carried out reconnaissance, exploitation and data theft across targets in parallel, making sophisticated operations accessible with less hands-on work.

In a [recent analysis, Tomasz Tunguz](https://tomtunguz.com/a-90-dollar-key-into-your-companys-secrets/) estimated the model cost of a 100-million-token attack workload using GLM-5.3, a low-cost model: 100 million tokens × $0.902 per million = $90.20. That is roughly 98% to 99% below the [$5,000 to $10,000 frontier-model estimate cited by Bank for International Settlements (BIS) for a comparable cyber attack. Tunguz’s figure covers model usage only, not the](https://www.bis.org/publications/bulletin-129-mythos-moment-frontier-ai-and-cyber-risk.pdf) full cost of an attack. Even still, it shows how trivially cheap it is now for attackers to go after any codebase, with the spend falling from thousands of dollars to under $100.

These new agentic attacks should make every team take another look at the code they’ve been running for years. Engineering and security teams need to find and fix weaknesses in their own applications before an attacker with an army of AI agents gets there first.

### Security has to become every developer’s responsibility

Traditional AppSec checks such as rule-based static analysis, dependency scanning and secret detection are no longer enough on their own. Developers, engineering leaders, and security teams also need defensive AI agents that trace attack paths, uncover missing safeguards and business-logic vulnerabilities, and help fix them.

Developers’ responsibility doesn’t stop at the code they’re writing now. An application already in production without known vulnerabilities might still get exploited by an AI agent looking for ways to skip a permission check or business rule. The gap only shows up when a request is traced thro...