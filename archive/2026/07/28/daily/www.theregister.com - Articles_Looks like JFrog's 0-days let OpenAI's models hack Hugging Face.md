---
title: Looks like JFrog's 0-days let OpenAI's models hack Hugging Face
url: https://www.theregister.com/security/2026/07/28/looks-like-jfrogs-0-days-let-openais-models-hack-hugging-face/5280001
source: www.theregister.com - Articles
date: 2026-07-28
fetch_date: 2026-07-29T05:04:46.154108
---

# Looks like JFrog's 0-days let OpenAI's models hack Hugging Face

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
  + [The State of Storage 2026](/special_features/state_of_storage_2026)
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
  + [Sign in](https://account.theregister.com/login)

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

# Looks like JFrog's 0-days let OpenAI's models hack Hugging Face

The vendor won't confirm or deny

Jessica Lyons
[Jessica
Lyons](https://www.theregister.com/author/jessica-lyons)
Cybersecurity Editor

Published
tue 28 Jul 2026 // 23:01 UTC

We now have a better idea of how OpenAI's models broke out of their cages to attack Hugging Face. The rogue models found zero-day vulnerabilities in JFrog’s universal binary repository manager Artifactory around the time they escaped, according to JFrog CTO Yoav Landman.

While Landman doesn’t outright admit that the JFrog flaws were the [zero-days that OpenAI’s models found and exploited](https://www.theregister.com/ai-and-ml/2026/07/22/openai-admits-it-was-the-source-of-the-agent-swarm-that-attacked-hugging-face/5275939), ultimately allowing them to [breach the massive model mart](https://www.theregister.com/cyber-crime/2026/07/20/frontier-llms-couldnt-help-hugging-face-fight-off-evil-agents/5275168), it definitely looks and quacks like a duck - err, frog.

Landman says OpenAI's models discovered the Artifactory zero-days during a security evaluation. The AI giant notes the incident occurred while its models were being evaluated on the [ExploitGym benchmark](https://www.theregister.com/ai-and-ml/2026/07/28/openais-agent-siege-forced-significant-rebuild-at-hugging-face/5279577).

REG AD

“During a security evaluation, OpenAI’s models identified previously unknown zero-day vulnerabilities in self-hosted Artifactory installations that could be exploited to gain unintended internet access,” Landman [said](https://jfrog.com/blog/jfrog-and-openai-collaboration-on-zero-day-security-findings/) on Monday.

REG AD

[JFrog Artifactory](https://jfrog.com/blog/what-is-artifactory-jfrog/) is a central platform that organizations use to store and distribute all the software artifacts across their supply chains. It supports more than 60 package formats including Docker, Maven, npm, PyPI, Helm, and AI/ML models.

OpenAI “responsibly and immediately” disclosed the vulnerabilities to JFrog, Landman continued. “Our security team treated the report with the urgency it deserved, as a genuine zero-day unknown to the world, and moved accordingly. We developed, validated, and released a fix for all JFrog customers, self-hosted and cloud alike.”

## MORE CONTEXT

* [### Hugging Face rebuilt a third of its infrastructure after OpenAI agents ran amok](/ai-and-ml/2026/07/28/openais-agent-siege-forced-significant-rebuild-at-hugging-face/5279577)
* [### Tech giants link hands to praise open AI models after OpenAI - Hugging Face attack](/ai-and-ml/2026/07/27/tech-giants-link-hands-to-praise-open-ai-models-after-openai-hugging-face-attack/5279061)
* [### OpenAI's Hugging Face debacle makes a great case for open models](/ai-and-ml/2026/07/27/openais-hugging-face-debacle-makes-a-great-case-for-open-models/5278498)
* [### OpenAI-Hugging Face attack doesn't mean agents are evil – unless you tell them to be](/security/2026/07/24/openai-hugging-face-attack-doesnt-mean-agents-are-evil-unless-you-tell-them-to-be/5277881)

On Monday, JFrog released the [fixed versions](https://docs.jfrog.com/releases/docs/artifactory-self-managed-releases#artifactory-7161), and credited OpenAI researchers for reporting at least eight of the now-patched Artifactory vulnerabilities: [CVE-2026-65617](https://www.cve.org/CVERecord?id=CVE-2026-65617), [CVE-2026-65925](https://www.cve.org/CVERecord?id=CVE-2026-65925), [CVE-2026-65921](https://www.cve.org/CVERecord?id=CVE-2026-65921), [CVE-2026-65923](https://www.cve.org/CVERecord?id=CVE-2026-65923), [CVE-2026-66018](https://www.cve.org/CVERecord?id=CVE-2026-66018), [CVE-2026-66014](https://www.cve.org/CVERecord?id=CVE-2026-66014), [CVE-2026-66015](https://www.cve.org/CVERecord?id=CVE-2026-66015), and [CVE-2026-65924](https://www.cve.org/CVERecord?id=CVE-2026-65924).

The Register asked JFrog whether at least some of these were abused by OpenAI’s rogue models to access the internet and compromise Hugging Face, but the DevOps firm isn’t talking.

JFrog's admission comes about a week after [OpenAI said two of its models](https://www.theregister.com/security/2026/07/24/openai-hugging-face-attack-doesnt-mean-agents-are-evil-unless-you-tell-them-to-be/5277881), GPT-5.6 Sol and a second pre-release model, escaped thei...