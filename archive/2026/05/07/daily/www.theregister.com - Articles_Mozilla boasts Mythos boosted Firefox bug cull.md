---
title: Mozilla boasts Mythos boosted Firefox bug cull
url: https://www.theregister.com/security/2026/05/08/mozilla-says-ai-helped-squash-423-firefox-security-bugs/5235438
source: www.theregister.com - Articles
date: 2026-05-07
fetch_date: 2026-05-08T04:57:02.854165
---

# Mozilla boasts Mythos boosted Firefox bug cull

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

security

# Mozilla boasts Mythos boosted Firefox bug cull

Yet it remains unclear if Anthropic's uber model was effective, or if better model middleware is what makes the difference

Thomas Claburn
[Thomas
Claburn](https://www.theregister.com/author/thomas-claburn)

Published
fri 8 May 2026 // 00:32 UTC

Mozilla fixed 423 Firefox security bugs in April, a repair rate more than five times higher than the 76 fixes issued in March and almost 20 times higher than its 21.5 monthly average last year.

The browser maker previously said Anthropic's ballyhooed Mythos Preview model found [271 of these](https://www.theregister.com/software/2026/04/22/mythos-found-271-firefox-flaws-none-a-human-couldnt-spot/5223657) in Firefox 150.

Now, a trio of technical types has come forward to provide a bit more detail about what Mythos (and its less storied sibling Opus 4.6) actually found. But they also highlight something that may matter more than the model: the agentic harness – the middleware mediating between AI and the end user.

REG AD

## MORE CONTEXT

* [### Dyna Software's AI assistant promises to massage your toughest ServiceNow configs](/devops/2026/05/07/dyna-softwares-ai-assistant-promises-to-massage-your-toughest-servicenow-configs/5235392)
* [### Fake IT workers rented laptops to Nork scammers, got prison time](/cyber-crime/2026/05/07/fake-it-workers-rented-laptops-to-nork-scammers-got-prison-time/5235342)
* [### Anthropic response to 1-click pwn: Shouldn't have clicked 'ok'](/security/2026/05/07/claude-code-trust-prompt-can-trigger-one-click-rce/5235319)
* [### 60% of MD5 password hashes are crackable in under an hour](/security/2026/05/07/60-of-md5-password-hashes-are-crackable-in-under-an-hour/5234954)

Brian Grinstead, Firefox distinguished engineer, Christian Holler, Firefox tech lead, and Frederik Braun, head of the Firefox security team, [observe](https://hacks.mozilla.org/2026/05/behind-the-scenes-hardening-firefox/) that over the past few months, AI-generated security reports have gone from slop to rather more tasty.

REG AD

They attribute the transformation to better models and development of better ways of harnessing those models – steering them in a way that increases the ratio of signal to noise.

But they also appear to be aware that there's some skepticism in the security community about Mythos. So they've decided to publicize selected wins in an effort to encourage others to jump aboard the AI bug remediation train.

"Ordinarily we keep detailed bug reports private for several months after shipping fixes and issuing security advisories, largely as a precaution to protect any users who, for whatever reason, were slow to update to the latest version of Firefox," they said.

"Given the extraordinary level of interest in this topic and the urgency of action needed throughout the software ecosystem, we’ve made the calculated decision to unhide a small sample of the reports behind the fixes we recently shipped."

The post links to a dozen Firefox bugs with varying degrees of severity. The list includes, for example, a 20-year-old [heap use-after-free bug](https://bugzilla.mozilla.org/show_bug.cgi?id=2025977) (high severity) that a web page could trigger using the XSLTProcessor DOM API without any user interaction.

Many of these bugs are sandbox escapes, they note, which are difficult to find using techniques like fuzzing. AI analysis, they say, helps provide broader security coverage. And they add that it has helped validate prior browser hardening work designed to prevent [prototype pollution](https://developer.mozilla.org/en-US/docs/Web/Security/Attacks/Prototype_pollution) attacks – audit logs showed AI models making unsuccessful exploitation attempts using this technique.

Following Anthropic's announcement of Project Glasswing – a program for companies to gain early access to Mythos because it's touted as too dangerous for public release – security experts expressed skepticism.

For example, Davi Ottenheimer, president of security consultancy flyingpenguin, wrote in an April 13 [blog post](https://www.flyingpenguin.com/the-boy-that-cried-mythos-verification-is-collapsing-trust-in-anthropic/), "The supposedly huge Anthropic 'step change' appears to be little more than a rounding error. The threat narrative so far appears to be ALL marketing and no real results. The Glasswing consortium is regulatory capture dressed up poorly as restraint."

REG AD

He subsequently ran a test in which he strapped Anthropic's lesser models Sonnet 4.6 and Haiku 4.5 into a harness called [Wirken](https://github.com/gebruder/wirken/tree/main) with an auditing skill called [Lyrik](https://github.com/gebruder/wirken/blob/main/docs/lyrik-overview.md). The result was [eight findings in two minutes at a cost of about $0.75](https://www.fl...