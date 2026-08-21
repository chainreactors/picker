---
title: Grok chat duped into swallowing injected instructions
url: https://www.theregister.com/ai-and-ml/2026/08/20/grok-chat-duped-into-swallowing-injected-instructions/5290019
source: www.theregister.com - Articles
date: 2026-08-20
fetch_date: 2026-08-21T03:05:14.852467
---

# Grok chat duped into swallowing injected instructions

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
* [Developer](/tag/devops)
* [Open Source](/tag/open%20source)
* [BOFH](/tag/bofh)
* [Who, Me?](/tag/who%20me)
* [On Call](/tag/on%20call/)
* [Podcasts](/tag/kettle)

REG AD

ai and ml

# Grok chat duped into swallowing injected instructions

A spoonful of encryption helps the malware go down

Thomas Claburn
[Thomas
Claburn](https://www.theregister.com/author/thomas-claburn)
AI AND SOFTWARE REPORTER

Published
thu 20 Aug 2026 // 14:00 UTC

xAI's Grok web chat agent is currently vulnerable to a novel form of prompt injection, according to security researchers with Adversa AI.

The technique allows an attacker to create a web page poisoned with malicious instructions that induce an AI model summarizing the page to carry out harmful actions.

That describes a well-known attack known as [indirect prompt injection](https://www.theregister.com/security/2026/01/08/openai-patches-dej-vu-prompt-injection-vuln-in-chatgpt/4312959). Frontier AI models have become better at dealing with such attempts through existing guardrails, though the issue is far from resolved.

REG AD

Adversa's approach comes with a twist: It relies on encrypted malicious instructions, which attackers place on a web page alongside an encryption key. The model guardrail scanner – an input filter – can't read the encrypted text despite the presence of the key. The scanner therefore passes it on to the model, which can use the key to decrypt the instructions.

REG AD

The model then carries out instructions in the decrypted text as would be the case in any other indirect prompt injection attack.

Adversera calls its method "cryptographic context injection."

"An attacker ships ciphertext along with the key material and an instruction to decrypt it, and the model runs that decryption inside its own code execution sandbox," wrote Rony Utevsky, lead researcher at Adversa AI, in a [blog post](https://adversa.ai/blog/cryptographic-context-injection-grok-data-theft). "Everything a guardrail’s scanner would need is right there on the page, but recovering the plaintext means running PBKDF2 and AES-256-GCM, which no content classifier does at inspection time."

Other attacks on AI models have relied on cipher-based evasion, such as base64 encoding. But because these are weak and reversible cipher mechanisms, models can decode them natively from their own training data, Utevsky said.

That doesn't work for strong encryption, so decryption must be done through the code execution runtime. The runtime thus becomes a mechanism for trust laundering – the model trusts its own output, namely the malicious instructions that it decrypted.

In a proof-of-concept [demo](https://www.youtube.com/watch?v=FBcHUjnyyY0), Adversa shows how the technique can be used to exfiltrate the victim's chat history with Grok.com. The attack transmits the user’s name, coarse location, subscription tier, and the full set of the user’s prompts in the conversation by appending them to a URL as parameters.

## MORE CONTEXT

* [### 'Not a theoretical risk,' feds warn as attackers use AI-made code to hack critical infrastructure controllers](/security/2026/08/19/not-a-theoretical-risk-feds-warn-as-attackers-use-ai-made-code-to-hack-critical-infrastructure-controllers/5289960)
* [### SvelteKit 3 puts heat on Next.js with radical approach to RPCs](/devops/2026/08/19/sveltekit-3-puts-heat-on-nextjs-with-radical-approach-to-rpcs/5289925)
* [### Google pits Marvell against Broadcom as it chases AI crown](/off-prem/2026/08/19/google-pits-marvell-against-broadcom-as-it-chases-ai-crown/5289902)
* [### Dev taps Claude Code to craft custom printer driver for macOS](/ai-and-ml/2026/08/19/dev-taps-claude-code-to-craft-custom-printer-driver-for-macos/5289875)

Other models may be vulnerable to varying degrees. With Google's Gemini public chat interface ([gemini.google.com](http://gemini.google.com)), Utevsky told The Register, the Grok scenario doesn't work because Gemini doesn't provide Python with access to external websites.

"So it's useful only to sneak bad questions and answers past guardrails," he explained.

REG AD

When Adversa tested cryptographic context injection on Gemini, they were able to get the model to produce content that normally would be blocked by safety filters – instructions for how to build an incendiary weapon.

xAI, according to Utevsky, was informed about the attack on June 3, 2026, directly and through its HackerOne bug bounty program. We're told xAI acknowledged...