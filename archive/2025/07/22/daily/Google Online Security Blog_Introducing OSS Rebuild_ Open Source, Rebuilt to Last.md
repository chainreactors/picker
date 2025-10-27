---
title: Introducing OSS Rebuild: Open Source, Rebuilt to Last
url: http://security.googleblog.com/2025/07/introducing-oss-rebuild-open-source.html
source: Google Online Security Blog
date: 2025-07-22
fetch_date: 2025-10-06T23:23:03.222770
---

# Introducing OSS Rebuild: Open Source, Rebuilt to Last

![](https://ad.doubleclick.net/ddm/activity/src=2542116;type=gblog;cat=googl0;ord=1?)

[![](https://www.gstatic.com/images/branding/googlelogo/2x/googlelogo_color_150x54dp.png)](https://security.googleblog.com/)
[## Security Blog](/.)

The latest news and insights from Google on security and safety on the Internet

## [Introducing OSS Rebuild: Open Source, Rebuilt to Last](https://security.googleblog.com/2025/07/introducing-oss-rebuild-open-source.html "Introducing OSS Rebuild: Open Source, Rebuilt to Last")

July 21, 2025

Posted by Matthew Suozzo, Google Open Source Security Team (GOSST)

Today we're excited to announce OSS Rebuild, a new project to strengthen trust in open source package ecosystems by reproducing upstream artifacts. As supply chain attacks continue to target widely-used dependencies, OSS Rebuild gives security teams powerful data to avoid compromise without burden on upstream maintainers.

The project comprises:

* Automation to derive declarative build definitions for existing PyPI (Python), npm (JS/TS), and Crates.io (Rust) packages.
* [SLSA Provenance](https://slsa.dev) for thousands of packages across our supported ecosystems, meeting SLSA Build Level 3 requirements with no publisher intervention.
* Build observability and verification tools that security teams can integrate into their existing vulnerability management workflows.
* Infrastructure definitions to allow organizations to easily run their own instances of OSS Rebuild to rebuild, generate, sign, and distribute provenance.

#### Challenges

Open source software has become the foundation of our digital world. From critical infrastructure to everyday applications, OSS components now account for [77%](https://static.carahsoft.com/concrete/files/1617/1597/8665/2024_Open_Source_Security_and_Risk_Analysis_Report_WRAPPED.pdf) of modern applications. With an estimated value exceeding [$12 trillion](https://www.hbs.edu/ris/Publication%20Files/24-038_51f8444f-502c-4139-8bf2-56eb4b65c58a.pdf), open source software has never been more integral to the global economy.

Yet this very ubiquity makes open source an attractive target: Recent high-profile supply chain attacks have demonstrated sophisticated methods for compromising widely-used packages. Each incident erodes trust in open ecosystems, creating hesitation among both contributors and consumers.

The security community has responded with initiatives like [OpenSSF Scorecard](http://scorecard.dev/), [pypi's Trusted Publishers](https://blog.pypi.org/posts/2023-04-20-introducing-trusted-publishers/), and [npm's native SLSA support](https://github.blog/2023-04-19-introducing-npm-package-provenance/). However, there is no panacea: Each effort targets a certain aspect of the problem, often making tradeoffs like shifting work onto publishers and maintainers.

#### Our Aim

Our aim with OSS Rebuild is to empower the security community to deeply understand and control their supply chains by making package consumption as transparent as using a source repository. Our rebuild platform unlocks this transparency by utilizing a declarative build process, build instrumentation, and network monitoring capabilities which, within the [SLSA Build](https://slsa.dev/spec/v1.0/levels#build-track) framework, produces fine-grained, durable, trustworthy security metadata.

Building on the hosted infrastructure model that we pioneered with [OSS Fuzz](https://github.com/google/oss-fuzz) for memory issue detection, OSS Rebuild similarly seeks to use hosted resources to address security challenges in open source, this time aimed at securing the software supply chain.

Our vision extends beyond any single ecosystem: We are committed to bringing supply chain transparency and security to all open source software development. Our initial support for the PyPI (Python), npm (JS/TS), and Crates.io (Rust) package registries—providing rebuild provenance for many of their most popular packages—is just the beginning of our journey.

#### How OSS Rebuild Works

[![](https://blogger.googleusercontent.com/img/a/AVvXsEjfsIwZQ4rw9fIh98NeN_LIDA02i6bu13nW4MHLQtGXCLKxdCQU3IMNCoy2eYlVrnTE3ntDMAwVgplosBHL-_ElPhAQNh1kBN3Hgz6QPq0mFcSIPlVC_pUqrsnF9_s6nNRg2j6DIfrDqLGt33Futda6HmSletctGX72E7d4_s-TQ7g_dNvZPtKIboF9esHb=w641-h274)](https://blogger.googleusercontent.com/img/a/AVvXsEjfsIwZQ4rw9fIh98NeN_LIDA02i6bu13nW4MHLQtGXCLKxdCQU3IMNCoy2eYlVrnTE3ntDMAwVgplosBHL-_ElPhAQNh1kBN3Hgz6QPq0mFcSIPlVC_pUqrsnF9_s6nNRg2j6DIfrDqLGt33Futda6HmSletctGX72E7d4_s-TQ7g_dNvZPtKIboF9esHb)

Through automation and heuristics, we determine a prospective build definition for a target package and rebuild it. We semantically compare the result with the existing upstream artifact, normalizing each one to remove instabilities that cause bit-for-bit comparisons to fail (e.g. archive compression). Once we reproduce the package, we publish the build definition and outcome via [SLSA Provenance](https://slsa.dev/spec/v0.1/provenance). This attestation allows consumers to reliably verify a package's origin within the source history, understand and repeat its build process, and customize the build from a known-functional baseline (or maybe even use it to generate more detailed [SBOMs](https://slsa.dev/spec/v1.0/faq#q-how-does-slsa-and-slsa-provenance-relate-to-sbom)).

With OSS Rebuild's existing automation for PyPI, npm, and Crates.io, most packages obtain protection effortlessly without user or maintainer intervention. Where automation isn't currently able to fully reproduce the package, we offer manual build specification so the whole community benefits from individual contributions.

And we are also excited at the potential for AI to help reproduce packages: Build and release processes are often described in natural language documentation which, while difficult to utilize with discrete logic, is increasingly useful to language models. Our initial experiments have demonstrated the approach's viability in automating exploration and testing, with limited human intervention, even in the most complex builds.

#### Our Capabilities

OSS Rebuild helps detect several classes of supply chain compromise:

* Unsubmitted Source Code - When published packages contain code not present in the public source repository, OSS Rebuild will not attest to the artifact.

+ Real world attack: [solana/webjs (2024)](https://www.theregister.com/2024/12/05/solana_javascript_sdk_compromised/)

* Build Environment Compromise - By creating standardized, minimal build environments with comprehensive monitoring, OSS Rebuild can detect suspicious build activity or avoid exposure to compromised components altogether.

+ Real world attack: [tj-actions/changed-files (2025)](https://www.wiz.io/blog/github-action-tj-actions-changed-files-supply-chain-attack-cve-2025-30066)

* Stealthy Backdoors - Even sophisticated backdoors like xz often exhibit anomalous behavioral patterns during builds. OSS Rebuild's dynamic analysis capabilities can detect unusual execution paths or suspicious operations that are otherwise impractical to identify through manual review.

+ Real world attack: [xz-utils (2024)](https://www.akamai.com/blog/security-research/critical-linux-backdoor-xz-utils-discovered-what-to-know)

For enterprises and security professionals, OSS Rebuild can...

* Enhance metadata without changing registries by enriching data for upstream packages. No need to maintain custom registries or migrate to a new package ecosystem.
* Augment SBOMs by adding detailed build observability information to existing Software Bills of Materials, creating a more complete security picture.
* Accelerate vulnerability response by providing a path to vendor, patch, and re-host upstream packages using our verifiable build definitions.

For publishers and maintainers of open source packages, OSS Rebuild can...

* Strengthen package trust by providing consumers with independent verification of the packages' build integrity, regardless of the sophistication of the original b...