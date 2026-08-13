---
title: 'Near-autonomous' AI agents attack Taiwan's nuclear safety agency
url: https://www.theregister.com/security/2026/08/12/near-autonomous-ai-agents-attack-taiwans-nuclear-safety-agency/5287055
source: www.theregister.com - Articles
date: 2026-08-12
fetch_date: 2026-08-13T04:05:22.372118
---

# 'Near-autonomous' AI agents attack Taiwan's nuclear safety agency

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
  + [Cloud Infrastructure Month 2026](/special_features/cloud_infrastructure_month_2026)
  + [HPE: AI Explainers](/explainer/ai-explainer)
  + [Agentic AI](/special_features/agentic_ai)
  + [The Future of the Datacenter](/special_features/future_of_the_datacenter)
  + [AWS:Reinvent](/special_features/aws_reinvent)
  + [Nvidia GTC](/special_features/nvidia_gtc)
  + [Supercomputing Month](/special_features/2025_11_supercomputing_month)
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
* [AWS](/tag/aws)
* [Microsoft](/tag/microsoft)
* [Developer](/tag/devops)
* [Open Source](/tag/open%20source)
* [BOFH](/tag/bofh)
* [Who, Me?](/tag/who%20me)
* [On Call](/tag/on%20call/)
* [Podcasts](/tag/kettle)

REG AD

Security

# 'Near-autonomous' AI agents attack Taiwan's nuclear safety agency

Some say the world will end in fire, some say an agentic swarm

Jessica Lyons
[Jessica
Lyons](https://www.theregister.com/author/jessica-lyons)
Cybersecurity Editor

Published
wed 12 Aug 2026 // 22:45 UTC

Suspected Chinese cyber operatives used publicly available AI tools to compromise Taiwanese government systems before expanding the attack to its nuclear safety agency, supply-chain vendors, and at least seven energy companies in what security researchers called a "near-autonomous attack."

Over the first four days of July, AI agents compromised 85 government user accounts and extracted more than 2,500 personnel records, according to Dream, an Israeli cybersecurity firm. Researchers uncovered evidence of the attack in a 160 MB online archive containing 1,395 files documenting the operation.

Dream, in [research](https://www.dreamgroup.com/blog/inside-a-multi-agent-ai-framework-used-to-compromise-government-entities-in-asia) published on Wednesday, detailed the intrusions and said that the suspected Chinese hackers hit “government entities in Asia” - but declined to say which government had been attacked.

REG AD

REG AD

A person familiar with the attack confirmed to The Register that Taiwan was the target.

The Financial Times first [reported](https://www.ft.com/content/7d2ab3e0-9085-48f6-b38a-d90260d58795) on Dream’s research and identified Taiwan.

While the security firm doesn’t attribute the agentic attack to the Chinese government or a specific hacking group, the operational documentation “points to a Chinese-language operator,” the researchers said.

According to Dream, the attack framework, built on open source Hermes and OpenClaw AI agents, deployed up to eight sub-agents, each assigned to its own targets and attack techniques, across 12 “attack waves” between July 1 and July 4.

First, the agents mapped the entire government ecosystem, extracting embedded URLs, API endpoints, OAuth client IDs, and Keycloak configuration objects from a single government portal. This portal allowed the agents to identify 21 connected government systems and every supported authentication flow.

“On one target alone, it discovered 36+ API endpoints spanning account management, user data retrieval, file upload, and administrative functions - many completely unauthenticated,” the Dream threat researchers wrote. “Critically, it found that one of the systems exposed its entire user database without any authentication - thousands of employee records including names, departments, and SSO account IDs.”

### Multiple entry points

After mapping the government’s attack surface, the agents found multiple entry points including three hidden API endpoints that accepted any request body and returned a valid authenticated session without requiring user credentials.

REG AD

Using employee usernames harvested from an unauthenticated API, the agents broke into a government department’s office automation portal, solving its CAPTCHAs with 100 percent accuracy. The agents also tested predictable password patterns based on each employee’s ID, and cracked 85 accounts across multiple password-spray rounds.

Eighty-four of the 85 cracked accounts successfully authenticated to the department's internal information system, giving the attackers access to internal dashboards, equipment management interfaces, and personnel statistics pages.

In total, the illicit access allowed the agents to exfiltrate a ton of government information, including more than 2,564 personnel records, a full JSON export of all department system users, seven SSO client secrets, six internal database credentials across MSSQL, Oracle, and Sybase, and internal network IP ranges.

### But wait, there's more

And then, the agents pivoted to the Taiwanese government’s supply chain.

## MORE CONTEXT

* [### 'Asimov was right' about rules for robots, says ex-US Cyber Director](/security/2026/08/07/asimov-was-right-about-rules-for-robots-says-ex-us-cyber-director/5284397)
* [### OpenAI reveals its rogue agent swarm went a little bit Borg ahead of Hugging Face hack](/security/2026/08/06/openai-reveals-its-rogue-agent-swarm-went-a-little-bit-borg-ahead-of-hugging-face-hack/5283741)
* [### North Korean spies are ru...