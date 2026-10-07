---
title: Zombie instructions on carefully constructed web pages could trick GitHub Copilot CLI into sharing secrets
url: https://www.theregister.com/ai-and-ml/2026/10/06/zombie-instructions-on-carefully-constructed-web-pages-could-trick-github-copilot-cli-into-sharing-secrets/5301206
source: www.theregister.com - Articles
date: 2026-10-06
fetch_date: 2026-10-07T07:55:46.682191
---

# Zombie instructions on carefully constructed web pages could trick GitHub Copilot CLI into sharing secrets

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
  + [Cybersecurity Month 2026](/special_features/cybersecurity_month_2026)
  + [VMware Explore 2026](/special_features/vmware_explore_2026)
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
* [Software](/software)
* [Microsoft](/tag/microsoft)
* [Developer](/devops)
* [Open Source](/tag/open%20source)
* [BOFH](/tag/bofh)
* [Who, Me?](/tag/who%20me)
* [On Call](/tag/on%20call/)
* [Science](/science)

REG AD

[ai and ml](/tag/ai%20and%20ml)

# Zombie instructions on carefully constructed web pages could trick GitHub Copilot CLI into sharing secrets

Run the CLI in autopilot mode and take your chances

Thomas Claburn
[Thomas
Claburn](https://www.theregister.com/author/thomas-claburn)
AI AND SOFTWARE REPORTER

Published
tue 6 Oct 2026 // 14:00 UTC

### READ MORE

* [#### South Korean president calls for creation of tools that stop all cyber-attacks

  2 hours ago](/public-sector/2026/10/07/south-korean-president-calls-for-creation-of-tools-that-stop-all-cyber-attacks/5301533)
* [#### Anthropic reconfigures its cool kids security program

  7 hours ago](/security/2026/10/07/anthropic-reconfigures-its-cool-kids-security-program/5301509)
* [#### Trump Mobile customers' data dumped - and some never even received their gold device

  13 hours ago](/security/2026/10/06/trump-mobile-customers-data-dumped-and-some-never-even-received-their-gold-device/5301433)
* [#### Microsoft extends the Outlook naughty step with two more file types

  15 hours ago](/software/2026/10/06/microsoft-extends-the-outlook-naughty-step-with-two-more-file-types/5301350)
* [#### Asos app delivers a data leak threat instead of fast fashion

  18 hours ago](/security/2026/10/06/asos-app-delivers-a-data-leak-threat-instead-of-fast-fashion/5301332)

GitHub Copilot CLI may reveal developer secrets if it comes across instructions that tell it to do so, depending on the underlying model.

The coding agent tool was flagged earlier this year for being [susceptible to indirect prompt injection](https://www.promptarmor.com/resources/github-copilot-cli-downloads-and-executes-malware). That's when a model ingests text from a source other than the user that directs it to take some action outside the scope of its intended function.

This is more of the same, with a twist. According to security researchers at Adversa AI, GitHub Copilot CLI suffers from the same vulnerability [identified in Grok two months ago](https://www.theregister.com/ai-and-ml/2026/08/20/grok-chat-duped-into-swallowing-injected-instructions/5290019): Cryptographic Context Injection (CCI).

REG AD

Imagine a GitHub Copilot CLI user is working on a project and running the agent in [autopilot mode](https://docs.github.com/en/enterprise-cloud%40latest/copilot/concepts/agents/copilot-cli/autopilot). In other agentic coding tools [like Anthropic's Claude](https://claude.com/blog/auto-mode-default-in-claude-code), that's the default, but it remains optional for GitHub Copilot CLI.

REG AD

Given that condition, the next requirement is for the CLI tool to read a web page with a malicious set of instructions that have been encrypted with a private key published on the same site.

"Static guardrails read text; they do not run it," explained Rony Utevsky in [a blog post](https://adversa.ai/blog/cryptographic-context-injection-github-copilot/) provided to The Register. "CCI ships malicious instructions as strong ciphertext, along with the key material and an instruction to decrypt, and induces the agent to run that decryption in its own code execution runtime."

Active content classifiers that might be reading ingested text as a model defense would miss the encrypted code, unlike encodings like base64 or substitution ciphers that can be undone because the model learned how to decode in training.

### The model lottery

The attack chain goes like this: The user runs Copilot CLI and asks it to fetch a specific URL. The page contains encrypted content, decryption instructions calling for use of Python, and two possible decryption keys.

The first key is fake. It's a template that the agent tries to build by reading targeted files from disk (e.g., the user's .env file). Those secrets then get added to the key string. The initial decryption is attempted with this phony key but fails.

So the second key is tried, the decryption works, and the agent is presented with instructions to fetch another URL for more context – but that URL contains the harvested secrets and the network request transmits them to the attacker.

This doesn't work all the time, however. It depends on the model, whic...