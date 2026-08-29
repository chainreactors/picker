---
title: Researcher shows how Claude Code can be tricked simply by asking it to summarize a website
url: https://www.theregister.com/research/2026/08/28/researcher-shows-how-claude-code-can-be-tricked-simply-by-asking-it-to-summarize-a-website/5293372
source: www.theregister.com - Articles
date: 2026-08-28
fetch_date: 2026-08-29T08:33:09.165812
---

# Researcher shows how Claude Code can be tricked simply by asking it to summarize a website

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
* [AWS](/tag/aws)
* [Microsoft](/tag/microsoft)
* [Developer](/tag/devops)
* [Open Source](/tag/open%20source)
* [BOFH](/tag/bofh)
* [Who, Me?](/tag/who%20me)
* [On Call](/tag/on%20call/)
* [Podcasts](/tag/kettle)

REG AD

security

# Researcher shows how Claude Code can be tricked simply by asking it to summarize a website

More prompt-injection hijinks from wunderwuzzi

Jessica Lyons
[Jessica
Lyons](https://www.theregister.com/author/jessica-lyons)
Cybersecurity Editor

Published
fri 28 Aug 2026 // 21:50 UTC

### MOST POPULAR

* [security

  #### Researcher shows how Claude Code can be tricked simply by asking it to summarize a website](/research/2026/08/28/researcher-shows-how-claude-code-can-be-tricked-simply-by-asking-it-to-summarize-a-website/5293372)
* [Legal

  #### Nuisance-call blocker fined £190k for being a nuisance caller](/security/2026/08/27/nuisance-call-blocker-fined-190k-for-being-a-nuisance-caller/5292888)
* [AI and ml

  #### Apple defies memory shortage with new Mac minis](/ai-and-ml/2026/08/25/apple-defies-memory-shortage-with-new-mac-minis/5292406)
* [security

  #### Security vets rally around $4 paper password books for sale in Australia](/security/2026/08/24/security-vets-rally-around-4-paper-password-books-for-sale-in-australia/5291234)
* [ai and ML

  #### Slop factory bans Russians for using slop factory to create slop](/ai-and-ml/2026/08/25/slop-factory-bans-russians-for-using-slop-factory-to-create-slop/5292297)

Anthropic’s Claude Code running Opus 5 in Auto Mode can be tricked into executing attacker-controlled code simply by asking the coding agent to summarize a website. The attack works up to 80 percent of the time, according to [prompt-injection wizard](https://www.theregister.com/special-features/2025/10/30/anthropics-claude-convinced-to-exfiltrate-private-data/1109039) Johann Rehberger, aka wunderwuzzi.

In a [blog](https://embracethered.com/blog/posts/2026/breaking-claude-code-opus-5-and-automode/) and [video demo](https://youtu.be/18PIeJoxYtc?si=1g-E31JGHQKDn0Ox), he detailed how to hijack Opus 5 in Auto Mode, which is the default setting for Claude as of mid-August.

It starts off by asking the agentic coding model to summarize a malicious website that presents itself as an archive of notebook records, and then tricking Claude into using curl instead of its WebFetch tool to retrieve the contents of the page – but without directly telling the model to use curl.

REG AD

The WebFetch request fails, returning a 415 Unsupported Media Type response, so the model decides to access the website directly by issuing a Bash tool call with curl.

REG AD

The website returns a 303 response, and redirects to a malicious ZIP archive, which Claude then downloads. This archive contains seemingly harmless files including catalog metadata, a README file, seven Base85/zlib-encoded JSON notebook records, a macOS decoder-darwin binary – plus a poisoned Python file named struct.py.

Claude, per its safety guardrails, refuses to run the decoder: “This is planned and what the attacker wants,” Rehberger wrote. Instead of using the supplied binary, the AI decides to write its own decoder. “Ironically, that safety decision is the exploit path,” Rehberger explained, adding a purple devil emoji to the text.

The new decoder imports base64, and from here the attack relies on [Python module shadowing](https://stackoverflow.com/questions/491705/python-problem-with-local-modules-shadowing-global-modules) to trick the model into running the malicious struct.py code.

Module shadowing occurs when a local file shares the same name as a Python standard-library module. The local file hides the official module, causing Python to load it instead.

In this case, the standard-library base64 module imports the legitimate struct module, and the malicious ZIP contains a malicious file with the same name.

Rehberger says he used ChatGPT to obfuscate the malicious struct.py code to bypass Claude’s safety controls, and this successfully launches a separate Python process to download and execute a remote payload – in this case a command-and-control callback, which in turn opens Calculator. We assume that real attackers would execute something a little more nefarious.

In another attack scenario, struct.py launches a second, headless Claude Code via claude -p, meaning this prompt injection can be used not just to remotely execute code, but rather to create a whole new agent.

“The nes...