---
title: Dirty Frag, Copy Fail, Fragnesia: The start of a worrisome Linux security trend
url: https://www.theregister.com/security/2026/05/23/dirty-frag-copy-fail-fragnesia-the-start-of-a-worrisome-linux-security-trend/5244742
source: www.theregister.com - Articles
date: 2026-05-23
fetch_date: 2026-05-24T06:01:20.989005
---

# Dirty Frag, Copy Fail, Fragnesia: The start of a worrisome Linux security trend

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

# Dirty Frag, Copy Fail, Fragnesia: The start of a worrisome Linux security trend

Or is it just life today, with AI constantly digging through code repositories in search of security holes?

![Steven J Vaughan Nichols](https://image.theregister.com/1665302.webp?imageId=1665302&x=0.00&y=17.50&cropw=100.00&croph=50.00&width=360&height=360)

Steven J. Vaughan-Nichols
[Steven
J. Vaughan-Nichols](https://www.theregister.com/author/steven-j-vaughan-nichols)

Published
sat 23 May 2026 // 11:59 UTC

OPINION [Dirty Frag](https://www.theregister.com/security/2026/05/08/dirty-frag-linux-flaw-one-ups-copyfail-with-no-patches-and-public-root-exploit/5237230), [Copy Fail](https://www.theregister.com/software/2026/04/30/linux-cryptographic-code-flaw-offers-fast-route-to-root/5229187), and [Fragnesia](https://www.theregister.com/security/2026/05/14/dirty-frag-gets-a-sequel-as-fragnesia-hands-linux-attackers-root-level-access/5240270) are less a random cluster of Linux bugs and more the public unveiling of how AI tools can pry open security holes with just a prompt or two. What they also have in common is their shared abuse of a core kernel abstraction: The page cache. What does this mean for you and me? Is this the rainstorm before a downpour of killer Linux security problems, or is this just a shower? It depends on who you ask.

Whatever else may be true, these problems must be addressed. As Igor Seletskiy, CEO of [CloudLinux](https://cloudlinux.com/), said: "The real story here is that we typically see one or two kernel-level LPE (Linux privilege escalations) vulnerabilities that affect multiple distros/versions per year. And now we see two such vulnerabilities one week apart. We should expect this trend to continue for quite a few months, meaning companies might have to reboot servers weekly."

Ouch!

REG AD

But is this the start of a trend? Linus Torvalds, who knows a thing or two about Linux, said at [Open Source Summit North America](https://events.linuxfoundation.org/open-source-summit-north-america/) in Minneapolis that until recently, the kernel community would quietly notify distributions about a bug and ask them to upgrade without detailing the vulnerability, and "most of the time, nobody would figure out what happened." That was then. This is now. With AI‑accelerated analysis, he recalled that "[last week, we fixed the bug; within three hours, there was a blog post](https://www.zdnet.com/article/linus-torvalds-has-a-love-hate-relationship-with-ai/) about the implications of that bug fix, because security people love getting attention."

REG AD

As a result of this kind of thing, Torvalds has changed how the Linux security community will deal with AI-discovered security holes. "[AI-detected bugs are pretty much by definition not secret](https://www.theregister.com/security/2026/05/18/linus-torvalds-says-ai-powered-bug-hunters-have-made-linux-security-mailing-list-almost-entirely-unmanageable/5241633), and treating them on some private list is a waste of time for everybody involved – and only makes that duplication worse because the reporters can't even see each other's reports."

In addition, Torvalds added, in the case of AI-discovered bugs, you need to keep in mind that just "because you found it with AI, 100 other people also found it with AI."

That means we're going to hear a lot more about Linux security problems. But are they getting worse? I asked Greg Kroah-Hartman, the Linux stable kernel maintainer, and he told me: "Maybe? It's hard to tell; the 'recent' ones really are very minor, as the number of systems that have 'untrusted users' is not common anymore. I don't see any real uptick in our actual bug fixes that I can tell."

He continued: "We fix bugs like that on a daily basis, it's just the rise of people wanting to 'name a bug' and release a public exploit seems to be all the rage at the moment."

An important point that Chris Wright, Red Hat's CTO, made at [Red Hat Summit](https://www.redhat.com/en/summit), the week before, is that in "security, all things aren't created equal. There will always be a spectrum of vulnerabilities that will surface. Some of those will be really critical and we will need to respond very quickly, so that becomes a clear priority. Others will have a longer tail of lower severity."

## MORE CONTEXT

* [### Trump jumps from 'anything goes' to 'strict regulation' AI policy](/columnists/2026/05/08/trump-jumps-from-anything-goes-to-strict-regulation-ai-policy/5234687)
* [### Locked, stocked, and losing budget: AI vendor lock-in bites back](/software/2026/04/28/locked-stocked-and-losing-budget-ai-vendor-lock-in-bites/5229050)
* [### Project Glasswing and open source software: The good, the bad, and the ugly](/security/2026/04/10/project-glasswing-and-open-source-the-good...