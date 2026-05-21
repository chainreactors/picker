---
title: Even Claude agrees: hole in its sandbox was real and dangerous
url: https://www.theregister.com/security/2026/05/20/even-claude-agrees-hole-in-its-sandbox-was-real-and-dangerous/5243662
source: www.theregister.com - Articles
date: 2026-05-20
fetch_date: 2026-05-21T06:04:46.543365
---

# Even Claude agrees: hole in its sandbox was real and dangerous

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

# Even Claude agrees: hole in its sandbox was real and dangerous

Another day, another AI bug silently fixed with no CVE and no public disclosure

Jessica Lyons
[Jessica
Lyons](https://www.theregister.com/author/jessica-lyons)

Published
wed 20 May 2026 // 21:34 UTC

Two now-patched bypass bugs in Claude Code’s network sandbox put users at risk, and one of these allows baddies to send anything inside the sandbox - credentials, source code, other private data - to any server on the internet, according to a researcher who found and reported both flaws to Anthropic.

Aonan Guan, who leads cloud and AI security at Wyze Labs and has hunted down bugs in pretty much every AI system out there, told The Register that this is the second time in five months Anthropic has silently fixed a sandbox bypass vulnerability in Clade Code without issuing a CVE or security advisory specific to the agentic coding tool.

The [latest issue](https://oddguan.com/blog/claude-code-sandbox-2/README.md) was a SOCKS5 hostname null-byte injection that can be exploited to trick the sandbox allowlist filter into approving connections it should block. It’s especially dangerous when combined with prompt injection, which Guan previously detailed in his earlier [comment and control research](https://www.theregister.com/security/2026/04/15/anthropic-google-microsoft-paid-ai-bug-bounties-quietly/5221934).

REG AD

When paired with prompt injection, the new flaw can be abused to force Claude to read hidden instructions and then run attacker-controlled code in the sandbox, allowing miscreants to exfiltrate anything the sandbox could reach. This includes cloud and GitHub credentials, the GitHub token Claude authenticated with, cloud metadata and internal APIs.

REG AD

“For anyone who ran Claude Code with a wildcard allowlist on a credential-bearing system, the network boundary did not exist for the 5.5 months from sandbox GA to v2.1.90,” Guan wrote in [research](https://oddguan.com/blog/second-time-same-sandbox-anthropic-claude-code-network-allowlist-bypass-data-exfiltration/#the-disclosure-experience) published Wednesday. “Treat that window as a potential exfiltration event.”

Anthropic says it found and fixed the latest flaw before receiving Guan’s report. The fix, according to a spokesperson, is a public commit in the sandbox-runtime repository, which shipped in Claude Code 2.1.88 on March 31. “Anyone can view” the commit, they told us.

## MORE CONTEXT

* [### Agents hooked into GitHub can steal creds – but Anthropic, Google, and Microsoft haven't warned users](/security/2026/04/15/anthropic-google-microsoft-paid-ai-bug-bounties-quietly/5221934)
* [### I meant to do that! AI vendors shrug off responsibility for vulns](/security/2026/04/19/ai-vendors-response-to-security-flaws-it-wasnt-me/5228722)
* [### Anthropic quietly fixed flaws in its Git MCP server that allowed for remote code execution](/security/2026/01/20/anthropic-quietly-fixed-flaws-in-its-git-mcp-server/4676059)
* [### Anthropic won't own MCP 'design flaw' putting 200K servers at risk, researchers say](/security/2026/04/16/mcp-design-flaw-puts-200k-servers-at-risk-researcher/5222022)

Guan filed his bug bounty report with HackerOne on April 3.

“Because the report described a vulnerability Anthropic had already caught and patched, it was closed as a duplicate of an internal finding,” the spokesperson said. “We appreciate the researcher’s time on this report.”

Guan says he doesn’t dispute the timeline. “That is not the core issue,” he told The Register.

### Shipping a sandbox with a hole is worse than not shipping one. The user with no sandbox knows they have no boundary. The user with a broken sandbox thinks they do.

“The core issue is that this was a bypass of a user-configured network sandbox, and there's still no advisory CVE, and no changelog note," he said. "Shipping a sandbox with a hole is worse than not shipping one. The user with no sandbox knows they have no boundary. The user with a broken sandbox thinks they do.”

Claude, for its part, seems to side with Guan.

When he showed Claude its own hole, the bot responded “This is a real bypass of the network sandbox filter,” according to a screenshot published in his research.

REG AD

The earlier bug, which Guan reported and [detailed](https://oddguan.com/blog/anthropic-sandbox-cve-2025-66479/) in December 2025, was ultimately assigned a CVE tracker - [CVE-2025-66479](https://nvd.nist.gov/vuln/detail/cve-2025-66479) - and patched in v0.0.16.

But the CVE only applies to Anthropic's sandbox-runtime, an upstream package, and not specifically to Claude Code, which Guan says means users have no way to know if their AI coding assistant is reading “allow nothing” as “allow everything.” He requested a CVE for Claude Code, and Anthropic ...