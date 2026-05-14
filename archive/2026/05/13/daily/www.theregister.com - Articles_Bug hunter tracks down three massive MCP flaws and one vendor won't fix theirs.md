---
title: Bug hunter tracks down three massive MCP flaws and one vendor won't fix theirs
url: https://www.theregister.com/security/2026/05/13/bug-hunter-tracks-down-three-serious-mcp-database-flaws-one-left-unpatched/5238916
source: www.theregister.com - Articles
date: 2026-05-13
fetch_date: 2026-05-14T05:47:25.358269
---

# Bug hunter tracks down three massive MCP flaws and one vendor won't fix theirs

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
  + [Edge + IoT](/edge_iot)
  + [Channel](/channel)
  + [PaaS + IaaS](/paas_iaas)
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
  + [AI + ML](/ai_ml)
  + [Applications](/applications)
  + [Databases](/databases)
  + [DevOps](/devops)
  + [OSes](/oses)
  + [Virtualization](/virtualization)
* Offbeat
  + [All Offbeat](/offbeat)
  + [Columnists](/columnists)
  + [Science](/science)
  + [BOFH](/bofh)
  + [Legal](/legal)
  + [Bootnotes](/bootnotes)
  + [Site News](/site_news)
  + [About Us](https://www.theregister.com/about_us)

* Special Features
  + [All Special Features](/tag/special_features)
  + [HPE: AI Explainers](/explainer/ai-explainer)
  + [RSA Conference](/special_features/rsa)
  + [Agentic AI](/special_features/agentic_ai)
  + [The Future of the Datacenter](/special_features/future_of_the_datacenter)
  + [AWS:Reinvent](/special_features/aws_reinvent)
  + [Nvidia GTC](/special_features/nvidia_gtc)
  + [SC25](/special_features/2025_11_sycomp_supercomputing)
  + [Supercomputing Month](/special_features/2025_11_supercomputing_month)
* Vendor Voice
  + [All Vendor Voice](https://vendorvoice.theregister.com/)
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

* [Datacenter](/tag/datacenter)
* [Security](/security)
* [Microsoft](/tag/microsoft)
* [AWS](/tag/aws)
* [Developer](/tag/developer)
* [Open Source](/tag/open%20source)
* [IT Careers](/tag/tech%20jobs)
* [Columnists](/tag/columnists)
* [Who, Me?](/tag/who%20me)
* [On Call](/tag/on%20call/)

REG AD

Security

# Bug hunter tracks down three massive MCP flaws and one vendor won't fix theirs

Apache, Alibaba databases vulnerable and only one has a patch

Jessica Lyons
[Jessica
Lyons](https://www.theregister.com/author/jessica-lyons)

Published
wed 13 May 2026 // 21:17 UTC

Security vulnerabilities in MCP servers for three popular database projects could let attackers execute unintended SQL statements on Apache Doris, exfiltrate sensitive metadata from Alibaba RDS, and potentially take over Apache Pinot instances exposed to the internet. Alibaba, meanwhile, declined to patch its flaw.

Apache issued a patch and a CVE tracker for Doris MCP, and there’s an open ticket in the MCP Pinot Github repository for the flaw, we're told. However, Alibaba decided not to patch the vulnerability in RDS MCP, according to Akamai security analyst Tomer Peled, who [wrote about the flaws](https://www.akamai.com/blog/security-research/one-fluke-3-pattern-mcp-back-end-vulnerabilities) on Tuesday and will present his full research next month at [x33fcon](https://www.x33fcon.com/#!index.md).

[MCP](https://www.theregister.com/software/2025/04/21/a-friendly-introduction-to-mcp-the-usb-of-ai/1105570), or Model Context Protocol, is an open source protocol originally developed by Anthropic that allows LLMs, AI applications, and agents to connect to external data, systems, and one another.

REG AD

## MORE CONTEXT

* [### Anthropic response to 1-click pwn: Shouldn't have clicked 'ok'](/security/2026/05/07/claude-code-trust-prompt-can-trigger-one-click-rce/5235319)
* [### Anthropic won't own MCP 'design flaw' putting 200K servers at risk, researchers say](/security/2026/04/16/mcp-design-flaw-puts-200k-servers-at-risk-researcher/5222022)
* [### Agents gone wild! Companies give untrustworthy bots keys to the kingdom](/special-features/2026/01/29/unaccounted-for-ai-agents-are-being-handed-wide-access/5120939)
* [### I meant to do that! AI vendors shrug off responsibility for vulns](/security/2026/04/19/ai-vendors-response-to-security-flaws-it-wasnt-me/5228722)

While [security issues are never a good thing](https://www.theregister.com/security/2026/04/19/ai-vendors-response-to-security-flaws-it-wasnt-me/5228722) - and they are [especially concerning](https://www.theregister.com/security/2026/04/16/mcp-design-flaw-puts-200k-servers-at-risk-researcher/5222022) when they exist in a [server sitting between an AI agent](https://www.theregister.com/security/2026/01/20/anthropic-quietly-fixed-flaws-in-its-git-mcp-server/4676059) and a production database, these in particular point to a larger problem in the way MCPs are developed.

REG AD

“There is missing or faulty security validation between the MCP server and its back end,” Peled wrote, adding that these security “gaps will become high-value targets for attackers and we expect more of these issues to surface.”

Here’s a closer look at all three, starting with the flaw that has since been fixed and assigned a CVE.

[Apache Doris](https://doris.apache.org/) is a high-speed analytics and search database with more than 10,000 mid- and large-enterprise users. Its MCP server allows AI agents to interact with and perform operations on Doris instances. This includes SQL queries or retrieving table and schema metadata - and foreshadows the found flaw: [CVE-2025-66335](https://nvd.nist.gov/vuln/detail/CVE-2025-66335), a SQL injection vulnerability, that affects Apache Doris MCP Server versions earlier than 0.6.1.

When an MCP tool is called, the server’s “exec\_query” function fails to validate one of the five parameters (the db\_name parameter) before constructing the SQL query. This means an attacker can invoke the function and inject malicious SQL through the db\_name parameter, which gets prepended to the beginning of the final SQL statement. Plus, the SQL validator only checks the first portion of the query, so all it sees is the attacker’s directive.

“As a result, any attacker that gains access to a client connected to the Doris MCP server can execute arbitrary commands on the victim’s Apache Doris instance,” Peled said.

Apache issued a patch in December to fix this flaw.

The second issue, an authentication validation bypass in Apache Pinot MCP, can also lead to SQL injection attacks and full database takeover.

[Apache Pinot](https://pinot.apache.org/) is another super-fast analytics database, and [StarTree’s MCP integration for Pinot](https://startree.ai/resources/startree-mcp-server-for-apache-pinot/) before v2.0.0 allowed users to run queries directly from their AI agent against their Pinot instance.

REG AD

The open-source project uses HTTP as the transport layer without requiring any type of authentication. This exposes the endpoint to remote attackers who can reach it, allowing them to invoke MCP too...