---
title: Somebody told DeepSeek to build in-browser ransomware and it gleefully complied
url: https://www.theregister.com/security/2026/07/01/somebody-told-deepseek-to-build-in-browser-ransomware-and-it-gleefully-complied/5265311
source: www.theregister.com - Articles
date: 2026-07-01
fetch_date: 2026-07-02T05:58:30.121222
---

# Somebody told DeepSeek to build in-browser ransomware and it gleefully complied

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

# Somebody told DeepSeek to build in-browser ransomware and it gleefully complied

'The original incomplete DeepSeek sample can be transformed into a fully functional attack with minimal effort,' Check Point researcher tells The Reg

Jessica Lyons
[Jessica
Lyons](https://www.theregister.com/author/jessica-lyons)

Published
wed 1 Jul 2026 // 20:57 UTC

You can't ask most models to help you make "ransomware" directly, but many will be more than willing if you give them the right prompt. DeepSeek and other LLMs with fewer safety and security controls make theoretical cyberthreats - like browser-only ransomware - much more likely to be used in real-world infections, according to Check Point researchers.

The Israeli cybersecurity company analyzed a DeepSeek-generated sample in a Wednesday report that its threat hunters describe as in-browser ransomware.

Over the past year, the team has tracked almost 3,000 files attributed to DeepSeek, and classified nearly half (1,383 files) as malicious or dangerous using VirusTotal or static source analysis.

REG AD

REG AD

“Within this dataset, we found a sample that implemented a dangerous browser-native technique we have not observed exploited in the wild,” researcher Alexey Bukhteyev [wrote](https://research.checkpoint.com/2026/browser-only-ransomware-from-llm-hallucinations-to-a-practical-attack-technique/).

And while the sample was incomplete, and unable to pull off an in-the-wild infection, the security shop’s testing showed “little effort” would be required to make it attack-ready.

“Our research shows that the original incomplete DeepSeek sample can be transformed into a fully functional attack with minimal effort,” Pedro Drimel Neto, malware analysis team leader at Check Point Research, told The Register.

“Very little effort is needed,” Neto said. “Low-level expertise is sufficient. You don't need to be a sophisticated cybercriminal or advanced persistent threat group. In fact, we've already observed evidence of actual threat actors attempting this attack using straightforward LLM prompts.”

### Known threat gets an AI boost

The risk ransomware poses to browsers isn’t a new idea. The [File System Access specification](https://wicg.github.io/file-system-access/#security-ransomware) lists ransomware as a security consideration, and a 2023 USENIX Security paper on [Ransomware over Modern Web Browsers](https://www.usenix.org/conference/usenixsecurity23/presentation/oz) described how File System Access API could be abused to encrypt local files from a malicious web application.

The File System Access API is a browser capability, primarily supported by Chrome and Chromium-based browsers, that allows developers to build web applications, such as editors, IDEs, and creative tools, that can read, write, and manage files on the user’s local device.

“Even though it can be used to develop rich web applications, it greatly extends the attack surface, which can be abused by adversaries to cause significant harm,” Google’s Güliz Seray Tuncay and Florida International University researchers Harun Oz, Ahmet Aris, Abbas Acar, Leonardo Babun and Selcuk Uluagac wrote in 2023, long before LLMs could develop working malware and attack chains.

REG AD

What’s new, according to Check Point, is that an [AI model](https://www.theregister.com/ai-ml/2026/05/11/google-says-criminals-used-ai-built-zero-day-in-planned-mass-hack-spree/5237982) put these previously documented ideas into a “realistic and enforceable attack scenario leveraging a method that defenders had originally thought was unfeasible due to browser sandboxing limits: a DeepSeek-attributed malicious sample, generated as an all-in-one malware fantasy, connected this documented platform risk to a realistic phishing-style web application, demonstrating a viable end-to-end attack chain.”

This technique is especially appealing to attackers because it doesn’t require a native payload, APK installation, browser exploit, or root access to a compromised device. Instead, it uses social engineering - tricking a user into clicking on a malicious button - combined with a legitimate permission prompt exposed by the File System Access API in Chrome.

### Meet InfernoGrabber 9000

This particular sample that Check Point uncovered is a Python Flask application that targets Android users. It’s named [InfernoGrabber 9000](https://www.virustotal.com/gui/file/07c39f79ab92fb21557b82283472dce1c112f577d796111fb752c3c6d84c86b5), and VirusTotal calls it a “fully functional information stealer and ransomware toolkit.”

While the security sleuths don’t have the prompt submitted to DeepSeek to produce the...