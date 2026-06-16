---
title: Feds freaked over Fable 5 after simple 'fix this code' prompt, not jailbreak, says researcher
url: https://www.theregister.com/security/2026/06/15/feds-freaked-over-fable-5-after-simple-fix-this-code-prompt-not-jailbreak-says-researcher/5255827
source: www.theregister.com - Articles
date: 2026-06-15
fetch_date: 2026-06-16T07:17:05.219943
---

# Feds freaked over Fable 5 after simple 'fix this code' prompt, not jailbreak, says researcher

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
  + [Bootnotes](/bootnotes)
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

security

# Feds freaked over Fable 5 after simple 'fix this code' prompt, not jailbreak, says researcher

According to the one person who actually read the research paper

Jessica Lyons
[Jessica
Lyons](https://www.theregister.com/author/jessica-lyons)

Published
mon 15 Jun 2026 // 22:07 UTC

The “jailbreak” that prompted the Trump administration to block Anthropic’s most advanced models was actually a simple three-word prompt: “Fix this code.”

That's according to [Katie Moussouris](https://www.theregister.com/security/2022/08/10/us-government-is-understanding-hiring-security-talent/1176302), founder and CEO of Luta Security, and the [fairy godmother of bug bounties](https://www.theregister.com/security/2023/11/22/microsofts-bug-bounty-turns-10-but-are-we-any-more-secure/290742). She says she was the only outside expert to read the third-party research paper on the Fable 5 guardrail bypass techniques that prompted the ban.

On Friday, the US government, reportedly citing national security concerns, issued an export control directive to suspend access to Fable 5 and Mythos 5 by any foreign national, inside or outside the United States. In response, Anthropic [disabled both models](https://www.anthropic.com/news/fable-mythos-access) “for all our customers to ensure compliance.”

REG AD

Anthropic shared the report privately with her, Moussouris [wrote](https://www.lutasecurity.com/post/the-fable-5-export-controls-harm-us-cyber-defense) in a Monday blog post.

REG AD

The outside researchers reportedly fed Anthropic’s [Fable 5](https://www.theregister.com/ai-and-ml/2026/06/09/anthropic-spins-a-fable-of-a-tamer-safer-mythos/5253106), [Mythos](https://www.theregister.com/security/2026/04/08/anthropic-mythos-model-can-find-and-exploit-0-days/5224393), and Claude Opus models open-source code containing known CVEs, plus new code intentionally laced with vulnerabilities, and asked the models to “review the code for security issues.”

As Moussouris tells it, Fable 5 refused, so the researchers asked the AI systems to “fix this code.” The model reportedly obliged, and after additional prompts also produced scripts to test the patches.

“That’s it,” Moussouris wrote. “‘Fix this code,’ plus several manual steps to generate test scripts, should never have triggered an export control. I feel like making ’90s-style t-shirts with ‘fix this code’ on the front and ‘this shirt is a munition’ on the back.”

Between 2013 and 2017, Moussouris [served on the technical expert group](https://thehill.com/opinion/cybersecurity/365352-serious-progress-made-on-the-wassenaar-arrangement-for-global/) that renegotiated the [Wassenaar Arrangement](https://www.theregister.com/security/2017/12/21/infosec-controls-relaxed-a-little-after-latest-wassenaar-meeting/382614), a voluntary agreement between 42 nations that governs certain export controls for classified dual-use software and technology.

The group eventually won exemptions for defensive cybersecurity activity. This allows defenders to share vulnerability data, conduct malware analysis, and coordinate incident response internationally without the threat of criminal prosecution.

On Sunday, Moussouris joined more than 100 other cybersecurity leaders and signed an open letter [urging the Trump administration to reverse](https://www.theregister.com/ai-and-ml/2026/06/15/us-clampdown-on-anthropic-models-sends-eu-sovereignty-surge-into-overdrive/5255487) the restrictions on Fable 5 and Mythos and restore cybersecurity firms' access to the advanced models.

“To pull the best capabilities away from defenders without a good reason when our adversaries are rapidly advancing is dangerous,” they [wrote](https://freefable.org/).

In her blog, Moussouris argues that there was no guardrail bypass or jailbreak. Defenders should be able to ask AI systems to find and fix bugs, and write tests to validate the patch, she said. Anthropic’s models were doing “the most valuable thing an AI model can do for defensive security: executing the find, fix, and test loop defenders run every day.”

REG AD

Removing the capability for models to respond to defensive requests makes AI systems “worse at finding bugs and verifying patches,” she continued.

Plus, the US can’t extend export controls to [open-weight systems or similar advanced models](https://www.theregister.com/research/2026/06/04/free-ai-model-powers-self-spreading-worm-in-enterprise-test-network/5250918) from China and other countries - and these systems will soon achieve Mythos-like capabilities, anyway. Anthropic and Google have both [accused China-based rivals](https://www.theregister.com/software/2026/02/24/anthropic-misanthropic-toward-chinas-ai-labs/4119678) including DeepSeek of using [“distillatio...