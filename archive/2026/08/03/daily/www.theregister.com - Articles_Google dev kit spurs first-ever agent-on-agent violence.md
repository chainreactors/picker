---
title: Google dev kit spurs first-ever agent-on-agent violence
url: https://www.theregister.com/security/2026/08/03/google-dev-kit-spurs-first-ever-agent-on-agent-violence/5282496
source: www.theregister.com - Articles
date: 2026-08-03
fetch_date: 2026-08-04T05:01:34.600966
---

# Google dev kit spurs first-ever agent-on-agent violence

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
* [Developer](/tag/developer)
* [Open Source](/tag/open%20source)
* [Columnists](/tag/columnists)
* [BOFH](/tag/bofh)
* [Who, Me?](/tag/who%20me)
* [On Call](/tag/on%20call/)

REG AD

Security

# Google dev kit spurs first-ever agent-on-agent violence

Poisoned pull requests contain prompt injection that allows one to control another

Jessica Lyons
[Jessica
Lyons](https://www.theregister.com/author/jessica-lyons)
Cybersecurity Editor

Published
mon 3 Aug 2026 // 21:30 UTC

In what they call the first-ever real-world agent-to-agent exploitation method, Pillar Security researchers say they discovered an exploit in the repository behind Google's Agent Development Kit for Python that could allow attackers to compromise supply chains. In other words, now we know that one AI agent can be used to control and compromise another one that has more privileges.

The security snafu existed in [google/adk-python](https://github.com/google/adk-python), an open source Python toolkit with [more than 90 million downloads](https://pepy.tech/projects/google-adk?timeRange=threeMonths&category=version&includeCIDownloads=true&granularity=daily&viewType=line&versions=1.17.0%2C1.16.0%2C1.15.1) used to build and deploy AI agents.

Google has since fixed the underlying issue in the repository but deemed the exploit non-rewardable because it involved social engineering. Even so, it illustrates the risks of using AI agents in CI/CD workflows for triage, pull request (PR) reviews, and discussions.

REG AD

It also shows how one AI agent could attack another in a production environment, according to Pillar’s Dan Lisichkin, who found and reported the vulnerability.

REG AD

“Our world is changing quickly, and new attack surfaces are not yet reflected in threat models because these attacks never could exist in the first place in the ‘pre-agent’ world,” Lisichkin [said](https://www.pillar.security/blog/ill-just-call-you-agent-to-agent-privilege-boundary-failures-in-ci-cd-on-googles-adk-repository) in a technical write-up published on Monday. He will also discuss the findings during a [poster talk](https://aivillage.org/posters/ill-just-call-you-agent-to-agent-privilege-boundary-failures-in-ci-cd/) at DEF CON's AI Village on Friday, August 7 at 1600 PDT.

“CISOs and security practitioners should start considering these scenarios, threat-modeling them, and calculating worst-case implications and blast radius,” Lisichkin wrote.

The issue stems from the way that the repo ran two classes of automated AI agents with different privilege levels that unintentionally share a trust boundary. One is a low-privilege, public-facing AI agent activated whenever a user opens a pull request (PR) or issue, and a second is a high-privilege, maintainer-only agent.

Pillar’s team found that the low-privilege, public-facing agent could be manipulated via prompt injection into triggering a maintainer-only agent that can execute malicious actions.

“Because workflows that explain how these agents work behind the scenes are also public, any person could have connected the dots that one agent should be able - at least theoretically - to 'call' the other,” Lisichkin told The Register. "When it comes to building the attack, you just need to know English to build the prompt injection (or just ask an AI to do it for you)."

There is one caveat: an attacker would first likely need to make legitimate contributions to the repository to build trust among the maintainers before moving on to prompt injection.

But assuming someone was willing to put in the time, here’s how the attack would play out.

First, an external user - this would be the attacker - creates a new PR. Lisichkin calls this PR A, and it combines a real fix with malicious code, such as a modified package.json or malicious dependency.

REG AD

Then, a public-facing agent tied to a high-privilege collaborator personal access token (PAT) reads the attacker’s PR text and marks the PR for review. This level of trust - the collaborator PAT - allows the attacker-generated text to trigger a gated workflow.

Once the PR A triage happens, the attacker opens a second PR - PR B - with the prompt injection, and the triage agent emits the trusted @gemini-cli handoff. This triggers the privileged-agent workflow and executes the malicious action.

“Strung together, they manufacture a complete, believable ‘a human asked for a review, gemini ran it, gemini approved’ trail on the poisoned PR, none of which ever ...