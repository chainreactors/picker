---
title: Homebrew 6.0 released with new security mechanism, Linux sandbox and more
url: https://www.theregister.com/devops/2026/06/17/homebrew-60-released-with-new-security-mechanism-linux-sandbox-and-more/5257570
source: www.theregister.com - Articles
date: 2026-06-17
fetch_date: 2026-06-18T06:52:02.074027
---

# Homebrew 6.0 released with new security mechanism, Linux sandbox and more

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

DEVOPS

Homebrew logo

# Homebrew 6.0 released with new security mechanism, Linux sandbox and more

Homebrew was "less vulnerable 10 years ago than npm is today," project lead tells us

Tim Anderson
[Tim
Anderson](https://www.theregister.com/author/tim-anderson)

Published
wed 17 Jun 2026 // 14:31 UTC

The Homebrew team has released version 6.0 of this popular open-source package manager for macOS and Linux, with a new mechanism for trusting packages and support for sandboxing on Linux, to align with existing sandboxing on macOS.

Homebrew 6.0 introduces [tap trust](https://docs.brew.sh/Tap-Trust), a "tap" being a collection of formulae, casks (a package of pre-compiled binaries) and commands which usually reside in a Git repository. The tool trusts official Homebrew taps by default, but requires an explicit agreement before it will trust third-party taps (which can include arbitrary Ruby code) before they install or run any code.

## MORE CONTEXT

* [### Developers build the best tools for developers – and are now defanging the AI menace](/ai-and-ml/2026/06/17/developers-build-the-best-tools-for-developers-and-are-now-defanging-the-ai-menace/5255316)
* [### AI is code – and can't be prompted into being smarter](/ai-and-ml/2026/06/14/ai-is-code-and-cant-be-prompted-into-being-smarter/5254141)
* [### Arch Linux locks down AUR signups amid wave of malicious commits](/security/2026/06/15/arch-linux-locks-down-aur-signups-amid-wave-of-malicious-commits/5255511)
* [### GitHub pulls pin on npm's auto-run scripts](/devops/2026/06/10/github-pulls-pin-on-npms-auto-run-scripts/5253453)

Tap trust is part of Homebrew’s approach to supply chain security, which has a number of distinctive features. Package maintainers are Homebrew maintainers, not the authors of the package. Names are maintainer-curated, so typosquats (giving a package a misleading name designed to be similar to one that is popular) can be rejected. Each download is pinned to a sha256 checksum. Package binaries are built from source, which protected Homebrew from incidents like the [Trivy compromise](https://www.theregister.com/special-features/2026/03/24/1k-cloud-environments-infected-via-trivy-attack/5226043) earlier this year when official Trivy binaries were replaced with malicious versions. These and other features of Homebrew security are [described](https://docs.brew.sh/Supply-Chain-Security)  in the documentation.

REG AD

Project leader Mike McQuaid told us that "Homebrew was less vulnerable 10-15 years ago than npm is today. The trust model is radically different and, even today, we are much quicker to break backwards compatibility in the interest of security."

REG AD

A new security feature is sandboxing on Linux when Homebrew compiles software. This was already implemented on macOS (and has been for a decade). Version 6.0 adds a Linux implementation based on the Bubblewrap project, and this will be on by default for developers.

A new Homebrew sub-command, brew vulns, will check installed packages for known vulnerabilities, by checking against the OSV (vulnerability database for open source).

![Homebrew 6.0 adds a vulnerabiltity checker for installed packages](https://image.theregister.com/5257582.webp?imageId=5257582&x=0.00&y=0.00&cropw=99.26&croph=100.00&width=960&height=548&format=jpg)

Homebrew 6.0 adds a vulnerabiltity checker for installed packages

Tim Anderson

The commands brew install and brew upgrade will now show a dependency summary and require a conformation prompt before running, called ask mode, following a developer survey earlier this year where this was highly requested.

Another new command, brew exec, will run a Homebrew-provided executable, similar to the way npx works for npm packages.

Homebrew startup performance in 6.0 is said to be faster, thanks to parallelised bottle fetching (a bottle is a pre-built package) and other optimizations.

Apple is phasing out support for Intel macOS both for future versions of macOS and for Rosetta, the Intel compatibility layer. Homebrew is following: in September this year no new bottles will be built for macOS Intel and from September 2027 macOS Intel will be "unsupported entirely and all related code deleted," according to the [post](https://brew.sh/2026/06/11/homebrew-6.0.0/) introducing Homebrew 6.0.

Homebrew is well-liked by developers, and becoming more popular on Linux as well as macOS. There is some frustration though regarding the dropping of Intel support. "The deprecation of Intel support is agressive! Every Mac enthusiast I know who uses a Mac as a server uses their old machines, which are pretty much all Intel. We'll lose support from you guys a year before Apple!," [said one](https://news.ycombinator.com/item?id=484...