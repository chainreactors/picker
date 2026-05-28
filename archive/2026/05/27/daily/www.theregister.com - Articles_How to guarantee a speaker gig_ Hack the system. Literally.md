---
title: How to guarantee a speaker gig: Hack the system. Literally
url: https://www.theregister.com/security/2026/05/27/pretalx-xss-flaw-exposed-conference-cfp-systems/5246598
source: www.theregister.com - Articles
date: 2026-05-27
fetch_date: 2026-05-28T06:03:51.514321
---

# How to guarantee a speaker gig: Hack the system. Literally

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
  + [PaaS + IaaS](/tag/paas-iaas)
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
  + [AI + ML](/tag/ai-ml)
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
  + [All Special Features](/special_features)
  + [HPE: AI Explainers](/explainer/ai-explainer)
  + [RSA Conference](/special_features/rsa)
  + [Agentic AI](/special_features/agentic_ai)
  + [The Future of the Datacenter](/special_features/future_of_the_datacenter)
  + [AWS:Reinvent](/special_features/aws_reinvent)
  + [Nvidia GTC](/special_features/nvidia_gtc)
  + [SC25](/special_features/2025_11_sycomp_supercomputing)
  + [Supercomputing Month](/special_features/2025_11_supercomputing_month)
  + [Computex 2026](/special_features/computex)
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

# How to guarantee a speaker gig: Hack the system. Literally

Make your mark on the call-for-proposal platform

Jessica Lyons
[Jessica
Lyons](https://www.theregister.com/author/jessica-lyons)

Published
wed 27 May 2026 // 13:00 UTC

A security researcher found a foolproof way to guarantee tech conferences accept his speaker submissions: hack their systems.

[CVE-2026-41241](https://nvd.nist.gov/vuln/detail/CVE-2026-41241) is a stored cross-site scripting (XSS) vulnerability in pretalx, a popular open source tool that conference organizers use to manage speaker submissions and schedules, that could allow attackers to effectively take over an organizer's session. Any user controlling searchable fields – including submission titles, speaker display names, and user names or email addresses – could inject arbitrary HTML or JavaScript. When an organizer's search query matched the malicious record, the payload would execute in the organizer interface.

"Once triggered, the injected script executed in the context of the pretalx organiser interface and could read the page's [Cross-Site Request Forgery] CSRF token, submit authenticated requests on the victim's behalf (including requests modifying data due to access to the CSRF token), or exfiltrate data visible to the victim," according to pretalx's [security advisory](https://github.com/pretalx/pretalx/security/advisories/GHSA-cjcx-jfp2-f7m2).

REG AD

Project maintainers patched the flaw in April, and it has been fixed in pretalx 2026.1.0.

REG AD

Elad Meged, founding engineer and security researcher at AI penetration-testing and offensive-security startup Novee, found and disclosed the flaw when he was preparing conference speaker submissions. He noticed the exact same call for proposals (CFP) submission form appearing underneath all of these different hacker conferences and academic symposiums' logos.

## MORE CONTEXT

* [### Anthropic to release Mythos-class models to the public](/security/2026/05/25/anthropic-to-release-mythos-class-models-to-the-public/5245596)
* [### Welcome to the vulnpocalypse, as vendors use AI to find bugs and patches multiply like rabbits](/patches/2026/05/14/welcome-to-the-vulnpocalypse-as-vendors-use-ai-to-find-bugs-and-patches-multiply-like-rabbits/5240027)
* [### A Russian speaker and jailbroken Gemini went on a hacking spree and emptied at least one MAGA victim's crypto wallets](/cyber-crime/2026/05/22/jailbroken-gemini-helped-russian-speaking-fraudster-target-maga-crypto-users/5245390)
* [### Google says criminals used AI-built zero-day in planned mass hack spree](/ai-ml/2026/05/11/google-says-criminals-used-ai-built-zero-day-in-planned-mass-hack-spree/5237982)

### 'One codebase serving them all'

While the events are unique, with different parent companies and organizers, "underneath, it is one codebase serving them all," Meged said in [research](https://novee.security/blog/pretalx-stored-xss-vulnerability-account-takeover/) published on Wednesday and shared in advance with The Register.

Meged then used the flaw to auto-apply for 40 conferences - and got accepted to present his proposed talk, "Securing Modern Web Apps," at every single one of them.

While Meged did submit real entries, he did not submit a live exploit payload into the conference systems. The Novee team validated all of their findings on a local instance. They didn't do any testing on [pretalx.com](http://pretalx.com/) or a third-party-hosted instance.

### I agree something outrageous would have been funnier, but it would also have been less responsible

"The goal was to validate the vulnerable workflow in the exact real-world setup while avoiding unnecessary harm," Meged told The Register. "So, we used realistic, normal-looking talk submissions and then validated exploitability through controlled, version-specific testing."

Some of the events that use pretalx-based CFP infrastructure include OffensiveCon, TROOPERS, FOSDEM, HEXACON, and Recon, he told us, stressing that this does not mean any of these conferences were actively exploited or compromised.

For any conferences that used pretalx for talk submissions, but weren't accepting submissions at the time, Meged followed up with them via responsible disclosure.

REG AD

And yes, Meged admits that he could have had more fun with the talk title, but he wanted to make it "intentionally boring and plausible," to blend in with other proposals. "I agree something outrageous would have been funnier, but it would also have been less responsible," he said.

### Human led, AI agent assist

Meged described the research as "human-led vulnerability research, agent-assisted at internet scale."

Once they understood the type of vulnerability, any "capable web security researche...