---
title: Supply chain security for Go, Part 2: Compromised dependencies
url: http://security.googleblog.com/2023/06/supply-chain-security-for-go-part-2.html
source: Google Online Security Blog
date: 2023-06-24
fetch_date: 2025-10-04T11:46:08.264497
---

# Supply chain security for Go, Part 2: Compromised dependencies

![](https://ad.doubleclick.net/ddm/activity/src=2542116;type=gblog;cat=googl0;ord=1?)

[![](https://www.gstatic.com/images/branding/googlelogo/2x/googlelogo_color_150x54dp.png)](https://security.googleblog.com/)
[## Security Blog](/.)

The latest news and insights from Google on security and safety on the Internet

## [Supply chain security for Go, Part 2: Compromised dependencies](https://security.googleblog.com/2023/06/supply-chain-security-for-go-part-2.html "Supply chain security for Go, Part 2: Compromised dependencies")

June 23, 2023

Julie Qiu, Go Security & Reliability, and Roger Ng, Google Open Source Security Team

“Secure your dependencies”—it’s the new supply chain mantra. With attacks targeting software supply chains [sharply rising](https://www.sonatype.com/state-of-the-software-supply-chain/introduction), open source developers need to monitor and judge the risks of the projects they rely on. Our [previous installment](https://security.googleblog.com/2023/04/supply-chain-security-for-go-part-1.html) of the Supply chain security for Go series shared the ecosystem tools available to Go developers to manage their dependencies and vulnerabilities. This second installment describes the ways that Go helps you trust the integrity of a Go package.

Go has built-in protections against three major ways packages can be compromised before reaching you:

* A new, malicious version of your dependency is published
* A package is withdrawn from the ecosystem
* A malicious file is substituted for a currently used version of your dependency

In this blog post we look at real-world scenarios of each situation and show how Go helps protect you from similar attacks.

# Reproducible builds and malicious new versions

In 2018, control of the JavaScript package [event-stream](https://thehackernews.com/2018/11/nodejs-event-stream-module.html) passed from the original maintainer to a project contributor. The new owner purposefully published version 3.3.6 with a new dependency named flatmap-stream, which was [found](https://github.com/dominictarr/event-stream/issues/116) to be maliciously executing code to steal cryptocurrency. In the two months that the compromised version was available, it had been downloaded 8 million times. This poses the question - how many users were unaware that they had adopted a new indirect dependency?

Go ensures [reproducible builds](https://go.dev/blog/supply-chain) thanks to automatically fixing dependencies to a specific version (“pinning”). A newly released dependency version will not affect a Go build until the package author explicitly chooses to upgrade. This means that all updates to the dependency tree must pass code review. In a situation like the event-stream attack, developers would have the opportunity to investigate their new indirect dependency.

# Go Module Mirror and package availability

In 2016, an open-source developer [pulled his projects](https://qz.com/646467/how-one-programmer-broke-the-internet-by-deleting-a-tiny-piece-of-code) from npm after a disagreement with npm and patent lawyers over the name of one of his open-source libraries. One of these pulled projects, left-pad, seemed to be small, but was used indirectly by some of the largest projects in the npm ecosystem. Left-pad had [2.5 million](https://www.theregister.com/2016/03/23/npm_left_pad_chaos/) downloads in the month before it was withdrawn, and its disappearance left developers around the world scrambling to diagnose and fix broken builds. Within a few hours, npm took the unprecedented action to restore the package. The event was a wake up call to the community about what can happen when packages go missing.

Go guarantees the availability of packages.The [Go Module Mirror](https://proxy.golang.org/) serves packages requested by the go command, rather than going to the origin servers (such as GitHub). The first time any Go developer requests a given module, it’s fetched from upstream sources and cached within the module mirror. When a module has been made available under a standard open source license, all future requests for that module simply return the cached copy, even if the module is deleted upstream.

# Go Checksum Database and package integrity

In December 2022, users who installed the package [pyTorch-nightly](https://pytorch.org/blog/compromised-nightly-dependency/) via pip, downloaded something they didn’t expect: a package that included all the functionality of the original version but also ran a [malicious binary](https://thehackernews.com/2023/01/pytorch-machine-learning-framework.html) that could gain access to environment variables, host names, and login information.

This compromise was possible because pyTorch-nightly had a dependency named torchtriton that shipped from the pyTorch-nightly package index instead of [PyPI](https://pypi.org/). An attacker claimed the unused torchtriton namespace on PyPI and uploaded a malicious package. Since pip checks PyPI first when performing an install, the attacker got their package out in front of the real package—a dependency confusion attack.

Go protects against these kinds of attacks in two ways. First, it is harder to hijack a namespace on the module mirror because publicly available projects are added to it automatically—there are no unclaimed namespaces of currently available projects. Second, package authenticity is automatically verified by Go's [checksum database](https://sum.golang.org/).

The checksum database is a global list of the SHA-256 hashes of source code for all publicly available Go modules. When fetching a module, the go command verifies the hashes against the checksum database, ensuring that all users in the ecosystem see the same source code for a given module version. In the case of pyTorch-nightly, a checksum database would have detected that the torchtriton version on PyPI did not match the one served earlier from pyTorch-nightly.

## Open source, transparent logs for verification

How do we know that the values in the Go checksum database are trustworthy? The Go checksum database is built on a [Transparent Log](https://research.swtch.com/tlog) of hashes of every Go module. The transparent log is backed by [Trillian](https://transparency.dev/#trillian), a production-quality, open-source implementation also used for [Certificate Transparency](https://certificate.transparency.dev/). Transparent logs are [tamper-evident by design](https://transparency.dev/verifiable-data-structures/) and append-only, meaning that it's impossible to delete or modify Go module hashes in the logs without the change being detected.

# Secure by default

The Go team supports the checksum database and module mirror as services so that Go developers don't need to worry about disappearing or hijacked packages. The future of supply chain security is ecosystem integration, and with these services built directly into Go, you can develop with confidence, knowing your dependencies will be available and uncorrupted.

The final part of this series will discuss the Go tools that take a “shift left” approach to security—moving security earlier in the development life cycle. For a sneak peek, check out our recent [supply chain security talk](https://youtu.be/HSt6FhsPT8c) from Google I/O!

![Share on Twitter](https://www.gstatic.com/images/icons/material/system/2x/post_twitter_black_24dp.png)

![Share on Facebook](https://www.gstatic.com/images/icons/material/system/2x/post_facebook_black_24dp.png)

[Google](https://plus.google.com/112374322230920073195)

#### No comments :

[Post a Comment](https://www.blogger.com/comment/fullpage/post/1176949257541686127/3747453223453348072)

[**](https://security.googleblog.com/)

[**](https://security.googleblog.com/2023/06/gmail-client-side-encryption-deep-dive.html "Newer Post")

[**](https://security.googleblog.com/2023/06/google-cloud-awards-313337-in-2022-vrp.html "Older Post")

![](data:image/png;base64...)

## Labels

**

* [#sharethemicincyber](https...