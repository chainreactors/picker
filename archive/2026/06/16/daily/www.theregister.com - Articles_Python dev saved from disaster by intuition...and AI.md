---
title: Python dev saved from disaster by intuition...and AI
url: https://www.theregister.com/ai-and-ml/2026/06/16/python-dev-saved-from-disaster-by-intuitionand-ai/5256632
source: www.theregister.com - Articles
date: 2026-06-16
fetch_date: 2026-06-17T07:04:14.862577
---

# Python dev saved from disaster by intuition...and AI

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

AI AND ML

# Python dev saved from disaster by intuition...and AI

I'm sorry, Dave. I can't install that repo that will totally hose your system.

Thomas Claburn
[Thomas
Claburn](https://www.theregister.com/author/thomas-claburn)
Senior reporter

Published
tue 16 Jun 2026 // 21:15 UTC

Python developer Roman Imankulov nearly took the bait. The fact that he didn't can be chalked up to human intuition and AI code vetting.

A person claiming to be a recruiter from a small crypto startup got in touch through LinkedIn, looking for help with what she described as proof-of-concept code that didn't work. The company, she explained, needed a lead engineer.

As Imankulov described the exchange in a [blog post](https://roman.pt/posts/linkedin-backdoor/), the recruiter asked him to look into an issue with a deprecated Node module. Something about the request seemed off.

REG AD

"I'd heard, as probably all of us have, about those types of attacks," Imankulov explained in a phone interview. "And I was like, 'what if this could be I could be the target?' It was just based on the past experience that I had."

REG AD

So he took the unusual step of spinning up a VPS on Hetzner where he cloned the repo. He then used his Pi coding agent (running Codex) to conduct a read-only analysis of the code.

"I ran an agent to test how it worked, and I was almost certain that it would return to me 'everything is clear, the code is ugly but in general it's safe to run and just go ahead and perform your review,'" he explained. "To my surprise, almost immediately the agent returned a response like, 'Don't run this code, just walk away because there's a trap.'"

## MORE CONTEXT

* [### AI and brain-computer interface allow speechless ALS patient to work a full-time job](/science/2026/06/16/ai-and-brain-computer-interface-allow-speechless-als-patient-to-work-a-full-time-job/5256492)
* [### Three critical Fortinet sandbox bugs splattered by unknown attackers](/security/2026/06/16/three-critical-fortinet-sandbox-bugs-splattered-by-unknown-attackers/5256461)
* [### Commodore gets into the phone biz with Sailfish-powered retro 'Callback'](/personal-tech/2026/06/16/commodore-gets-into-the-phone-biz-with-sailfish-powered-retro-callback/5256186)
* [### HPE spruces up its AI infrastructure portfolio for agentic workloads](/ai-and-ml/2026/06/16/hpe-spruces-up-its-ai-infrastructure-portfolio-for-agentic-workloads/5256417)

The AI model had flagged one of the files, app/test/index.js.

The file contained a backdoor. It took the form of a server URL, fragmented to look like a test suite configuration, and a network request that will run anything the server sends in response to the request.

Imankulov credited his AI agent with catching details that he had missed.

"I opened this code myself and I skimmed through this code and it looked to me like just, you know, a regular sloppy file written by a sloppy developer," he said. "So I just scroll down, [thinking] 'Yeah, yeah, it's awful, but you know if they can pay me to fix this code, I don't mind.' But the agent in the very same file found the exact vulnerability that I overlooked."

Just installing the repo using npm would have been sufficient to trigger the backdoor. The repo's package.json file contained a "[prepare](https://docs.npmjs.com/cli/v8/using-npm/scripts#life-cycle-scripts)" post-installation hook designed to run the script following the installation process.

The referenced malicious repo is no longer accessible – presumably GitHub removed it in response to Imankulov's complaint – but [a clone can still be found](https://github.com/bitcoin2026a/coin-promoting/blob/main/app/test/index.js).

REG AD

"What makes this attack insidious is how it hijacks standard developer workflows," explained Devashri Datta, independent open source and security architect, in an email to The Register. "The adversary didn't rely on the target executing a suspicious binary; they relied on the target running a routine command: npm install.

"By burying the execution logic inside the prepare lifecycle hook within package.json, the malicious payload triggers automatically during dependency resolution. This isn't a novel technique, but it remains highly effective precisely because developers run npm install on autopilot. The string fragmentation used to assemble the malicious URL, piecing together a domain from small constants, was deliberate obfuscation designed to defeat static analysis tools that scan for hardcoded indicators of compromise."

Imankulov said that the commits in the malicious repo appeared to be the work of a developer with an established web presence and body of work. But when he contacted the supposed author, the dev said he had been impersonated on...