---
title: OpenAI caught in TanStack npm supply chain chaos after employee devices compromised
url: https://www.theregister.com/security/2026/05/15/openai-caught-in-tanstack-npm-supply-chain-chaos-after-employee-devices-compromised/5241019
source: www.theregister.com - Articles
date: 2026-05-15
fetch_date: 2026-05-16T05:15:44.161426
---

# OpenAI caught in TanStack npm supply chain chaos after employee devices compromised

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

# OpenAI caught in TanStack npm supply chain chaos after employee devices compromised

Attackers stole a limited amount of internal credential material after malware hidden in poisoned packages reached two staff machines

Carly Page
[Carly
Page](https://www.theregister.com/author/carly-page)

Published
fri 15 May 2026 // 11:08 UTC

OpenAI says attackers behind the TanStack npm supply chain compromise stole internal credentials after reaching two employee devices, forcing the company to rotate signing certificates for several desktop products.

The company [disclosed](https://openai.com/index/our-response-to-the-tanstack-npm-supply-chain-attack/) this week that it had been caught up in the wider "Mini Shai-Hulud" campaign targeting npm ecosystems and developer infrastructure, though it said there was no evidence that customer data, production systems, or deployed software were compromised.

OpenAI said the incident happened during a phased rollout of new supply chain security controls introduced after a previous [Axios-related incident](https://openai.com/index/axios-developer-tool-compromise/). According to the company, the two compromised employee devices had not yet received updated package management protections that would have blocked the malicious dependency.

REG AD

The attackers carried out "credential-focused exfiltration activity" against a limited set of internal repositories reachable from the affected employee machines, according to OpenAI. It said "only limited credential material was successfully exfiltrated from these code repositories."

REG AD

That was apparently enough to trigger a precautionary reset across multiple products. OpenAI is rotating the certificates used to sign macOS versions of ChatGPT Desktop, Codex App, Codex CLI, and Atlas, and is requiring users to update the affected software by June 12.

The incident ties OpenAI to the increasingly messy supply chain campaign that has spent the past several weeks worming through npm ecosystems, CI/CD infrastructure, and GitHub Actions workflows. Security firm [Socket linked the TanStack compromise](https://www.theregister.com/cyber-crime/2026/05/12/cache-poisoning-caper-turns-tanstack-npm-packages-toxic/5238650) to the [broader "Mini Shai-Hulud" operation](https://www.theregister.com/security/2026/05/01/ongoing-supply-chain-attacks-worm-into-sap-npm-packages/5228837), which abused poisoned automation workflows and stolen publishing credentials to push malicious package updates into trusted software pipelines.

## MORE CONTEXT

* [### Checkmarx tackles another TeamPCP intrusion as Jenkins plugin sabotaged](/devops/2026/05/11/checkmarx-tackles-another-teampcp-intrusion-as-jenkins-plugin-sabotaged/5237780)
* [### The never-ending supply chain attacks worm into SAP npm packages, other dev tools](/security/2026/05/01/ongoing-supply-chain-attacks-worm-into-sap-npm-packages/5228837)
* [### Nearly half of UK businesses pwned last year as phishing keeps doing the job like it's 2005](/security/2026/04/30/uk-business-breach-rate-stuck-at-43-blame-the-phishing/5220326)
* [### Two different attackers poisoned popular open source tools - and showed us the future of supply chain compromise](/security/2026/04/11/two-different-attackers-poisoned-popular-open-source-tools/5221008)

Researchers tracking the wider Mini Shai-Hulud campaign have connected the activity to a threat group known as TeamPCP, which appears to have developed an unhealthy interest in poisoning npm ecosystems and rifling through developer credentials.

TanStack [confirmed this week](https://socket.dev/blog/tanstack-npm-packages-compromised-mini-shai-hulud-supply-chain-attack) that 84 malicious package versions spanning 42 @tanstack/\* packages had been published after attackers compromised parts of its release infrastructure. The poisoned packages were designed largely to steal credentials, including GitHub tokens, cloud secrets, npm credentials, and CI/CD authentication material.

The campaign appears [linked](https://www.aikido.dev/blog/mini-shai-hulud-is-back-tanstack-compromised) to earlier Mini Shai-Hulud attacks involving SAP-related npm packages, suggesting the same credential-stealing operation is spreading across multiple developer ecosystems.

OpenAI said it is continuing to investigate the incident and monitor for any downstream abuse tied to the stolen credentials.

The reassuring news is that OpenAI says no production systems were breached. The less reassuring news is that attackers keep getting deeper into the software assembly line before anybody notices. ®

[openai](/tag/openai)
[npm](/tag/npm)
[mini shai-hulud](/tag/mini%20shai-hulud)
[tanstack](/tag/tanstack)
[supply chain attack](/tag/supply%20chain%20attack)
[security](/tag/security)

REG AD

[![](https://image.there...