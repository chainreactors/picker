---
title: Smooth AI criminal drives 'first' end-to-end agentic ransomware attack
url: https://www.theregister.com/security/2026/07/02/smooth-ai-criminal-drives-first-end-to-end-agentic-ransomware-attack/5266073
source: www.theregister.com - Articles
date: 2026-07-02
fetch_date: 2026-07-03T05:48:53.179047
---

# Smooth AI criminal drives 'first' end-to-end agentic ransomware attack

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
* [Microsoft](/tag/microsoft)
* [AWS](/tag/aws)
* [Developer](/tag/developer)
* [Open Source](/tag/open%20source)
* [Columnists](/tag/columnists)
* [BOFH](/tag/bofh)
* [Who, Me?](/tag/who%20me)
* [On Call](/tag/on%20call/)

REG AD

Security

# Smooth AI criminal drives 'first' end-to-end agentic ransomware attack

Don't count on the LLM to return your data - even if you pay up

Jessica Lyons
[Jessica
Lyons](https://www.theregister.com/author/jessica-lyons)

Published
thu 2 Jul 2026 // 19:05 UTC

They're not bad; they're just prompted that way. Sysdig threat hunters documented what they say is the first-ever documented agentic ransomware infection with an LLM - not a human - driving the entire extortion operation, from gaining initial access to compromising a production database server and destroying data.

The security shop’s research team named the agentic intruder JadePuffer and said it gained initial access to an internet-facing Langflow instance by exploiting [CVE-2025-3248](https://nvd.nist.gov/vuln/detail/CVE-2025-3248), and then ran a fully automated attack.

“The most striking characteristic, however, was the LLM's behavior,” Sysdig director of threat research Michael Clark [said](https://www.sysdig.com/blog/jadepuffer-agentic-ransomware-for-automated-database-extortion) in a blog about the agentic ransomware and extortion operation.

REG AD

REG AD

JadePuffer’s “self-narrating” payloads “contained natural language reasoning, target prioritization, and the kind of detailed annotations that human operators don’t often write but LLM-generated code produces reflexively,” Clark added. “The operation also adapted in real time, retrying failed steps within refined parameters. In one sequence, it went from a failed login to a working fix in 31 seconds.”

After exploiting CVE-2025-3248, a missing authentication vulnerability in [Langflow](https://github.com/langflow-ai/langflow) that allows remote, unauthenticated attackers to execute arbitrary Python on the host, the AI agent began scanning for and collecting secrets, including LLM provider API keys, cloud credentials “with explicit coverage of Chinese providers” including Alibaba, Aliyun, Tencent, and Huawei, while also scanning for AWS, Azure and Google Cloud Platform, cryptocurrency wallets, and database credentials.

The AI also installed a crontab entry on the Langflow server to maintain persistence and call back to the attacker’s infrastructure every 30 minutes.

JadePuffer’s intended target was a separate internet-exposed production server running a MySQL database and an Alibaba Nacos configuration service, we’re told. Nacos is an open-source service-discovery and dynamic configuration platform developed by Alibaba and used in the cloud provider’s microservices applications.

The agent connected to the server's exposed MySQL port using root credentials, although Sysdig doesn’t know how the attacker obtained them. These credentials weren’t stolen from the victim’s environment.

## MORE CONTEXT

* [### Somebody told DeepSeek to build in-browser ransomware and it gleefully complied](/security/2026/07/01/somebody-told-deepseek-to-build-in-browser-ransomware-and-it-gleefully-complied/5265311)
* [### AWS intruder achieved admin access in under 10 minutes thanks to AI assist, researchers say](/security/2026/02/04/aws-intruder-pulled-off-ai-assisted-cloud-break-in-in-8-mins/4945272)
* [### The crazy, true story behind the first AI-powered ransomware](/security/2025/09/05/the-crazy-true-story-behind-the-first-ai-powered-ransomware/624795)
* [### It looks like you’re ransoming data. Would you like some help?](/security/2025/09/03/heres-how-ransomware-crims-are-abusing-ai-tools/414963)
* [### Nobody needs Mythos or 0-days to build a chaos-causing computer worm – free open source models work just fine](/research/2026/06/04/free-ai-model-powers-self-spreading-worm-in-enterprise-test-network/5250918)

JadePuffer then attacked Nacos via multiple vectors including an authorization bypass flaw (CVE-2021-29441) and forging a valid JSON web token (JWT) using Nacos's default signing key. Additionally, using its root database access, the LLM injected a backdoor administrator into the Nacos backing database.

It ultimately encrypted all 1,342 Nacos service configuration items using MySQL's built-in AES encryption function, and created an extortion demand, ransom note, Bitcoin payment address, and a Proton Mail contact:

"YOUR DATA HAS BEEN ENCRYPTED. All NACOS configurations, REDACTED customer data, and REDACTED PII have been encrypted with AES-256.", "3J98t1WpEZ73CNmQviecrnyiWrnqRhWNLy", "e78393397[@]proton[.]me"

REG AD

However, according to the threat hunters, the victim can’t recover the encrypted data, even if they paid the ransom demand, because the agent escalated “from ro...