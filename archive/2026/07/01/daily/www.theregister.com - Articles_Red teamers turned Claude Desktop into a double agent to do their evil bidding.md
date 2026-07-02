---
title: Red teamers turned Claude Desktop into a double agent to do their evil bidding
url: https://www.theregister.com/security/2026/07/01/red-teamers-turned-claude-desktop-into-a-double-agent-to-do-their-evil-bidding/5264692
source: www.theregister.com - Articles
date: 2026-07-01
fetch_date: 2026-07-02T05:58:30.436015
---

# Red teamers turned Claude Desktop into a double agent to do their evil bidding

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

# Red teamers turned Claude Desktop into a double agent to do their evil bidding

People trust their AI assistants and it's easy to abuse this trust

Jessica Lyons
[Jessica
Lyons](https://www.theregister.com/author/jessica-lyons)

Published
wed 1 Jul 2026 // 18:00 UTC

EXCLUSIVE Pentera Labs’ red teamers compromised a developer’s AI agent via his Claude Desktop app and ultimately turned that access into full remote code execution on the dev’s machine – demonstrating how an attacker could turn a trusted, chatty AI assistant into a double agent operating on their behalf.

“Claude’s got a new voice,” Pentera's offensive security services team leader Dvir Avraham told The Register.

“We acknowledge the huge trust in AI models – everybody uses them,” he said in a phone interview. “We used this trust to manipulate the victim, like under the hood, the victim didn't see it coming.”

REG AD

It also prompted Avraham to check his own platforms. “I became a little bit paranoid,” he told us. “I'm not allowing any command to run without me examining it twice.”

REG AD

In a report set to publish Wednesday, and shared in advance exclusively with The Register, Avraham and research technical lead Reef Spektor detailed the attack and what it means for organizations using agentic AI tools with local code-execution access.

It began with a red-team assignment on a third-party platform that aggregates customer email inboxes into a single management interface. Avraham and Spektor won’t name the platform, or tell us exactly how they gained access to it. They used this compromised inbox – and told us any compromised inbox would work – to get into the victim’s Claude account.

As the duo noted, breaking into an email inbox in real life – via a [third-party management platform](https://www.theregister.com/security/2026/06/09/france-probes-compromise-of-gov-messaging-platform-after-account-hijack/5252717), [phishing link](https://www.theregister.com/security/2026/06/22/gizmodo-readers-hit-with-clickfix-malware-prompts-after-account-compromise/5259226), [social engineering password reset](https://www.theregister.com/special-features/2026/03/23/voice-phishing-skyrockets-as-smooth-crims-talk-their-way-in/5223759), or even using AI agents – isn’t too difficult. “AI agents today have access to connectors and to direct MCPs into inboxes,” Spektor added.

## MORE CONTEXT

* [### Claude Desktop changes app access settings for browsers you don't even have installed yet](/security/2026/04/20/claude-desktop-changes-software-permissions-without-consent/5219674)
* [### Even Claude agrees: hole in its sandbox was real and dangerous](/security/2026/05/20/even-claude-agrees-hole-in-its-sandbox-was-real-and-dangerous/5243662)
* [### Cookie thieves caught stealing dev secrets via fake Claude Code installers](/security/2026/05/11/cookie-thieves-caught-stealing-dev-secrets/5238248)
* [### Google told researcher 'Nice catch!' Then denied bug bounty for flaw it still hasn't fixed](/security/2026/06/18/google-told-researcher-nice-catch-then-denied-bug-bounty-for-flaw-it-still-hasnt-fixed/5258076)

In addition to this prerequisite (compromised inbox), the attack chain also requires the victim to have [Claude Desktop](https://www.theregister.com/security/2026/04/20/claude-desktop-changes-software-permissions-without-consent/5219674) installed. Anthropic’s desktop app works across macOS, Windows, and Linux systems. It provides the same AI chat for conversations as claude.ai, and it also syncs across all devices and sessions tied to the user’s account.

“We asked ourselves, can we leverage the sync behavior to infect other sessions and devices? (hint: yes!),” the red teamers wrote in the Wednesday report.

### Back to the AI Stone Age

As of January, the desktop app also includes Cowork for longer agentic tasks, and Code for software development. So, for example, a user can send Claude a task from their phone and instruct it to work on their computer. As Anthropic [says](https://claude.com/product/cowork): “Anything you can do on your computer, Claude can do. Open apps, fill spreadsheets, navigate your browser. No setup, no passwords handed off.”

The Cowork feature now makes Pentera Labs’ attack scenario even easier.

REG AD

However, when the security analysts were doing this research in November 2025, “back in the Stone Age in terms of AI, you didn't have Cowork or Claude Code, so we needed a way to actually execute commands because we wanted to take over the machine,” Avraham said.

For this part, they took a keen interest in Claude Desktop’s [personalization features](https://support.claude.com/en/articles/10...