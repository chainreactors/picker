---
title: Why Amazon hates 'human-in-the-loop' AI governance
url: https://www.theregister.com/security/2026/06/20/why-amazon-hates-human-in-the-loop-ai-governance/5258639
source: www.theregister.com - Articles
date: 2026-06-20
fetch_date: 2026-06-21T06:50:23.246353
---

# Why Amazon hates 'human-in-the-loop' AI governance

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

Security

# Why Amazon hates 'human-in-the-loop' AI governance

VP Eric Brandwine explains people aren't all that great, actually

Jessica Lyons
[Jessica
Lyons](https://www.theregister.com/author/jessica-lyons)

Published
sat 20 Jun 2026 // 15:25 UTC

Humans tend to be “a little bit precious about humans,” according to Eric Brandwine, distinguished engineer and VP at Amazon Security.

We like to think we are all very good at our jobs, and we have high opinions of ourselves, he explained during a phone interview with The Register. “But when you actually get down to it, humans are not terribly consistent,” Brandwine said.

Humans, like AI agents and systems, are non-deterministic. Neither can be guaranteed to produce the same output given the same input twice. Both will make mistakes and even make stuff up. However, we’ve got millennia of experience dealing with humans and less than a decade with more modern LLMs and the AI systems built on top of them.

REG AD

“We know how humans fail,” Brandwine said. “We're comfortable with it. So human-in-the-loop isn’t necessarily the gold standard.”

REG AD

For years, vendors have told companies that the solution for dealing with any automated system was to put a human in the loop. That battle cry became much louder with the advent of modern AI systems and reached a fever pitch when enterprises started deploying agents into their IT environments.

More recently, however, big tech is changing the way it talks about agentic governance and rethinking the whole human-in-the-loop concept.

### Normalization of deviance

In 2017, Brandwine gave a talk on the [normalization of deviance](https://www.youtube.com/watch?v=KJiCfPXOW-U) at AWS’ annual re:Invent conference.

It’s a gradual process that happens when people in an organization take shortcuts, or don’t follow the established procedures or standards, and sometimes it occurs over years. As long as nothing catastrophic happens, this deviant behavior becomes the norm.

![](https://image.theregister.com/5258659.webp?imageId=5258659&x=0.00&y=0.00&cropw=100.00&croph=100.00&width=960&height=942&format=jpg)

Eric Brandwine, distinguished engineer and VP at Amazon Security

“It’s a thing all humans fall prey to, and one of the most heartbreaking stories I read in this area was about emergency departments and emergency rooms,” Brandwine said during a phone interview with The Register. “You’ve got all these machines, and they’re all beeping. Your first day on the job, you jump every single time one of the alarms beeps – but the patient is fine. It's a spurious alarm. You go back to your station, you sit down, and over time, after enough of these false alarms, enough of these repeated beeps with no actual consequence, your discipline slips, and you stop responding. And eventually some tragic outcome occurs.”

This, he admits, is a very high-stakes example. And yet it’s a documented occurrence among [healthcare workers](https://pmc.ncbi.nlm.nih.gov/articles/PMC2821100/), [firefighters](https://www.firefighterclosecalls.com/firefighter-safety-the-normalization-of-deviance/), and even [Army pilots](https://safety.army.mil/MEDIA/Risk-Management-Magazine/ArtMID/7428/ArticleID/7233/The-Normalization-of-Deviance).

REG AD

“Literally, someone’s life is on the line, and people still struggle to maintain discipline,” Brandwine said. “That’s the human condition.”

Here’s how this all applies to agentic AI governance and security. Humans build LLMs and AI systems, and having a “human-in-the-loop” ensures that a person reviews the AI’s output and approves (or not) any actions before the AI performs them.

“If you put a human inside of this tight loop, and ask them to make approval decisions for agentic tools repeatedly, time after time, they'll do a good job,” Brandwine said. “And then they'll do an okay job. And pretty quickly they'll be doing a poor job.”

This is why at Amazon, “we’re not huge fans of human-in-the-loop,” he added. “It's something that you should use judiciously, where you absolutely need it. But it’s not something that you can do at high velocity. You will not get the results that you want to get.”

### Big tech pulls the human-in-the-loop

Amazon isn’t the first or only tech giant to start talking differently about the role humans should play in agentic governance.

"It is very clear that we have moved from a human-led defense strategy, to a human-in-the-loop defense strategy, to an AI-led defense strategy that's overseen by humans," Google Cloud chief operating officer Francis deSouza [told reporters](https://www.theregister.com/security/2026/04/22/google-unleashes-even-more-ai-security-agents-to-fight-crims/5221298) during a press conference ahead of Google's annual Cloud...