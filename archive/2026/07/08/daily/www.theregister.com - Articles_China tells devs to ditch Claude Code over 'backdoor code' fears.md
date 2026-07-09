---
title: China tells devs to ditch Claude Code over 'backdoor code' fears
url: https://www.theregister.com/security/2026/07/08/china-ditch-older-claude-versions-with-backdoor-code/5268371
source: www.theregister.com - Articles
date: 2026-07-08
fetch_date: 2026-07-09T06:03:37.820865
---

# China tells devs to ditch Claude Code over 'backdoor code' fears

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

# China tells devs to ditch Claude Code over 'backdoor code' fears

National vulnerability database claims monitoring mechanism can forward Chinese users' data to remote servers

Connor Jones
[Connor
Jones](https://www.theregister.com/author/connor-jones)
Cybersecurity reporter

Published
wed 8 Jul 2026 // 14:58 UTC

China's National Vulnerability Database (CNVDB) is urging developers to uninstall recent Claude Code versions over the fear that they can scoop up sensitive user data without consent.

Referring to it as "backdoor code," the state-run body claimed over WeChat and in an online [statement](https://cnvdb.org.cn/announcement/2074682031259299842) that a "built-in monitoring mechanism" can gather details such as a user's location and identity, and forward them to remote servers.

It said the alert only applies to Claude Code versions 2.1.91 (April 2) to 2.1.196 (June 29). "It is recommended that relevant units and users immediately conduct a comprehensive investigation," CNVDB said on Wednesday.

REG AD

"For development terminals with the above-mentioned affected versions installed, immediately uninstall or upgrade to the latest secure version with the relevant backdoor code removed; strengthen the control of external access permissions and traffic monitoring of development tools within core business network segments to prevent the unauthorized transmission of sensitive data."

REG AD

The Register asked Claude maker Anthropic to comment, but it did not immediately respond.

Neither did Anthropic answer our questions last week about [its covert code](https://www.theregister.com/ai-and-ml/2026/07/01/anthropic-is-removing-its-covert-code-for-catching-chinese-competitors/5265366) designed to prevent competing AI companies from extracting intel about Claude's inner workings.

Claude Code engineer Thariq Shihipar stated publicly that Anthropic launched an experiment in March to protect against model distillation – a process by which AI companies try to improve their models by training them on the answers of those that are more advanced.

"The team has landed stronger mitigations since then and we've actually been meaning to take this down for a while," he said. The secret steganography system was removed in version 2.1.198, released on July 1.

## MORE CONTEXT

* [### Anthropic is removing its covert code for catching Chinese competitors](/ai-and-ml/2026/07/01/anthropic-is-removing-its-covert-code-for-catching-chinese-competitors/5265366)
* [### Anthropic reserves right to check ID for Claude subs](/ai-and-ml/2026/06/15/anthropic-reserves-right-to-check-id-for-claude-subs/5255804)
* [### New humanoid robots from China look like creepy pop star action figures – complete with slightly dodgy lip-synch](/ai-and-ml/2026/07/02/new-humanoid-robots-from-china-look-like-creepy-pop-star-action-figures-complete-with-slightly-dodgy-lip-synch/5265490)
* [### China's agentic AI policy wants to keep humans in the loop](/ai-and-ml/2026/05/11/chinas-agentic-ai-policy-wants-to-keep-humans-in-the-loop-1/5237632)

We had asked Anthropic whether it disclosed this mechanism in its terms of service documents, but it referred us to Shihipar's statement, which did not address the question.

Anthropic's alleged tracking of Chinese users is not the only matter contributing to souring relations between the AI company and China. It was also embroiled in a public spat with Chinese tech giant Alibaba, which it accused of using Claude's outputs to improve Alibaba models.

According to a letter to two US senators seen by [Reuters](https://www.reuters.com/world/china/anthropic-says-alibaba-illicitly-extracted-claude-ai-model-capabilities-2026-06-24/), it was the largest attack on Anthropic's AI that the company had ever seen.

More recently, Alibaba banned its staff from using Claude over fears it could be used to identify Chinese users, according to the [South China Morning Post](https://www.scmp.com/tech/big-tech/article/3359375/alibaba-bans-staff-using-claude-code-over-anthropic-spyware-concerns). ®

[security](/tag/security)

REG AD

[![](https://image.theregister.com/235728.jpg?imageId=235728&panox=0.00&panoy=0.00&panow=100.00&panoh=100.00&heightx=0.00&heighty=0.00&heightw=100.00&heighth=100.00&width=960&height=432&format=webp&format=jpg)

AI AND ML

## Singaporean sovereign wealth fund Temasek thinks AI has a future

Plans to lift portfolio exposure by 150 percent, and even more once it adds electrification ventures](https://www.theregister.com/ai-and-ml/2026/07/09/singaporean-sovereign-wealth-fund-temase...