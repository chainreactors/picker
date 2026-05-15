---
title: To gain root access at this company, all an intruder had to do was ask nicely
url: https://www.theregister.com/security/2026/05/14/to-gain-root-access-intruder-just-had-to-ask/5239853
source: www.theregister.com - Articles
date: 2026-05-14
fetch_date: 2026-05-15T05:53:30.072557
---

# To gain root access at this company, all an intruder had to do was ask nicely

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

Security

# To gain root access at this company, all an intruder had to do was ask nicely

Human IT managers thought they were being nice to the boss, but were assisting a threat actor

Avram Piltch
[Avram
Piltch](https://www.theregister.com/author/httpswwwtheregistercomauthoravram-piltch)
US Editor

Published
thu 14 May 2026 // 08:00 UTC

PWNED Welcome once again to PWNED, the column where we help you prepare for security success by studying others’ embarrassing failures. Today’s terrible tale involves individuals trying to do right by a company executive by letting their guard down, never a smart move.

Have a story about someone leaving a gaping hole in their network? Share it with us at pwned@sitpub.com. Anonymity is available upon request.

Our sad story comes from Brandon Dixon, who currently serves as CTO and co-founder of AI security firm [Ent](https://ent.ai/). In a prior life, however, Dixon was a penetration tester for hire and he saw some things that made all my remaining hairs stand on end just hearing about them.

REG AD

During one pentesting assignment, Dixon tried to find out how easy it would be to steal someone’s account using social engineering. The answer: barely an inconvenience.

REG AD

Dixon telephoned IT security and pretended that he was the head of security who had lost his password. When they asked him challenge questions, he said he had forgotten the answers to those also.

Then he gave them the password he wanted to use over the phone and they did a reset for him. After that, he was able to get into the network and do whatever he wanted there.

There’s so much that’s obviously wrong here that it’s hard to know where to begin with our lesson-taking. The IT support agents should not have taken Dixon’s word that he was the security manager, especially after he failed challenge questions, and should have denied his request to reset the password. They were probably thinking “this guy is an executive and we don’t want to piss him off” rather than “we have procedures that everyone must follow.”

The other problem here is that the IT department entered Dixon’s suggested password for him over the phone. First of all, the IT department should have sent a password reset to the real employee’s email or phone number. Second of all, it’s piss-poor security for anyone to know a user’s password other than the user themselves. And I say this as someone who used to work for a company where, if you had a problem, the IT support people would ask for your password via chat.

## MORE CONTEXT

* [### The network password was a key plot point in one of the most famous movies of all time](/security/2026/05/07/guessable-admin-password-exposes-sloppy-network-security/5231161)
* [### Finance company stores DB credentials in helpfully labeled spreadsheet](/security/2026/04/30/finance-company-stored-their-db-credentials-in-spreadsheet/5224248)
* [### Using the password 'admin123' wasn't as bad as sharing it on Slack](/security/2026/04/23/using-password-admin123-wasnt-as-bad-as-slacking-it/5227590)
* [### Sticky-note security turned gym into hall of '80s horrors](/security/2026/04/09/sticky-note-security-turned-gym-into-hall-of-80s-horrors/5227659)

Dixon also shared another story about social engineering from a time when he consulted for a pharmaceutical company. Members of the competition would call sales and marketing reps, pretend they were coworkers, and then extract information about upcoming drugs. This would allow competitors to know what was coming and how to respond to it.

To help solve the problem, Dixon instituted a system where real employees had to give a secret password at the beginning of a conversation.

“I built a system called 'Chal-Resp,' short for 'challenge-response,' that generated work pairings so a user could validate they were speaking with an actual employee,” he told The Register. “The caller would need to say the word and the end-user would need to respond with the proper challenge; only employees had access.”

What both of Dixon’s stories have in common is the proof that humans are eager to please and be helpful. But suspicion is the whole root of infosec, so it behooves us all to be a little less helpful to strangers in the workplace. ®

[pwned](/tag/pwned)
[security](/tag/security)
[social engineering](/tag/social%20engineering)

REG AD

[![](https://image.theregister.com/5240921.jpg?imageId=5240921&panox=0.00&panoy=0.00&panow=100.00&panoh=100.00&heightx=0.00&heighty=0.00&heightw=100.00&heighth=100.00&width=960&height=432&format=webp&format=jpg)

Off-Prem

## AWS racks M3 Ultra Macs that boast specs you can’t currently buy

Manages to get its hands on some Mac Studio machines before the OpenClaw machine grabs them](https://www.theregister.com/off-prem/2026/05/15/aws-racks-m3-ultra-macs-that...