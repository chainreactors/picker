---
title: Secure Unix ancestor KSOS did type safety before Rust made it cool
url: https://www.theregister.com/os-platforms/2026/07/06/secure-unix-ancestor-ksos-did-type-safety-before-rust-made-it-cool/5266458
source: www.theregister.com - Articles
date: 2026-07-06
fetch_date: 2026-07-07T06:05:07.278608
---

# Secure Unix ancestor KSOS did type safety before Rust made it cool

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

OS PLATFORMS

# Secure Unix ancestor KSOS did type safety before Rust made it cool

Modula-based source code resurfaces after nearly four decades

Liam Proven
[Liam
Proven](https://www.theregister.com/author/liam-proven)

Published
mon 6 Jul 2026 // 10:30 UTC

For the first time, the source code of KSOS, backed by the US Department of Defense in the late 1970s and 1980s, is available to the public in the archives of [The Unix Heritage Society](https://www.tuhs.org/) (TUHS).

TUHS volunteers preserve the historical source code and documentation of the original UNIX – or as much of it as is left. A few days ago, in an [email](https://www.tuhs.org/pipermail/tuhs/2026-June/033976.html) to its mailing list, TUHS founder [Warren Toomey](https://minnie.tuhs.org/warren.html) announced the addition of [KSOS](https://www.tuhs.org/Archive/Distributions/Other/KSOS/) to the collection.

"KSOS was the US Department of Defense (DoD) Kernelized Secure Operating System (KSOS, formerly called Secure UNIX). KSOS is intended to provide a provably secure operating system for larger minicomputers," he wrote.

REG AD

Despite its age, KSOS sounds surprisingly modern. It was a Unix-compatible OS, implemented in a type-safe programming language, Modula, rather than C. Modula was the [late great Niklaus Wirth](https://www.theregister.com/software/2024/01/04/rip-software-design-pioneer-niklaus-wirth/1417086)'s successor to Pascal and, in turn, the forerunner to Modula-2 – which we described when it was [added to the GNU Compiler Collection in 2022](https://www.theregister.com/software/2022/12/16/gcc-13-to-support-modula-2/512766). KSOS was designed to be formally verifiable, so that it could be trusted for use in highly secure systems. It ran on commodity hardware, and its development was sponsored by the US DOD.

REG AD

Very few OS kernels have been formally verified, and one of the best-known modern examples is the [seL4 microkernel](https://www.theregister.com/security/2009/08/17/researchers-forge-secure-kernel-from-maths-proofs/1394189), as used in the [Ironclad OS we covered last year](https://www.theregister.com/software/2025/11/10/ironclad-os-crafts-unix-like-kernel-in-ada-and-spark/541310), and also in the [new QSOE RISC-V RTOS](https://www.theregister.com/software/2026/06/26/one-man-two-kernels-and-a-lot-of-risc-v/5262858). KSOS isn't some cutting-edge experimental new Rust effort, like the [Asterinas project we described last year](https://www.theregister.com/software/2025/09/12/three-alternative-microkernels-show-devs-dont-need-linux/1428275) or the even newer [Maestro project](https://github.com/maestro-os/maestro).

What became KSOS started in 1978 at Ford Aerospace (yes, that Ford). On the team were Peter Neumann, who later ran the RISKS Digest – *The Register* [was quoting him](https://www.theregister.com/security/2004/04/08/tracking-the-blackout-bug/1431138) in 2004 – and Tom Perrine, who described it and its modern relevance in a 2002 article for the USENIX journal ;login:. It's titled "[The Kernelized Secure Operating system (KSOS)](https://www.usenix.org/system/files/login/articles/1255-perrine.pdf)" [PDF], and at only three and a bit pages long, it's well worth a read. Even then, 24 years ago, projects were struggling to reinvent things KSOS did successfully a couple of decades earlier. That's even more true today. To learn more about how KSOS worked, there's a 1978 [Executive Summary](https://seclab.cs.ucdavis.edu/projects/history/papers/ford78.pdf) [PDF] – which, despite its title, runs to 15 pages. Clearly, executives back then had longer attention spans.

Perrine gave a talk about KSOS at [DEF CON 20](https://defcon.org/html/defcon-20/dc-20-index.html) in 2012, which you can watch on YouTube.

KSOS isn't forgotten. For instance, it came up in a talk at last year's FOSDEM: [Confidential Computing's Recent Past, Emerging Present, and Long-Lasting Future](https://archive.fosdem.org/2025/schedule/event/fosdem-2025-5002-confidential-computing-s-recent-past-emerging-present-and-long-lasting-future/). Page 8 of the [slide deck](https://archive.fosdem.org/2025/events/attachments/fosdem-2025-5002-confidential-computing-s-recent-past-emerging-present-and-long-lasting-future/slides/237828/Confident_fRySvCW.pdf) [PDF] says KSOS was "among the first security-focused kernels, emphasizing formal verification" and "source code was publicly available, rejecting 'security through obscurity.'"

KSOS was not confined to academic research. It was used in production. Last October, Perrine explained more in another...