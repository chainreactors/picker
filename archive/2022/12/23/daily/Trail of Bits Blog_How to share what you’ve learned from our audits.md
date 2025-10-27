---
title: How to share what you’ve learned from our audits
url: https://blog.trailofbits.com/2022/12/22/curl-security-audit-threat-model/
source: Trail of Bits Blog
date: 2022-12-23
fetch_date: 2025-10-04T02:20:12.589269
---

# How to share what you’ve learned from our audits

[The Trail of Bits Blog](/ "The Trail of Bits Blog")

[![Trail of Bits Logo](/img/tob.png)](https://trailofbits.com "Trail of Bits")

# How to share what you’ve learned from our audits

Nick Selby

December 22, 2022

[audits](/categories/audits/), [guides](/categories/guides/)

Trail of Bits recently completed a security review of [cURL](https://curl.se/), which is an amazing and ubiquitous tool for transferring data. We were really thrilled to see cURL founder and lead developer Daniel Stenberg [write a blog post](https://daniel.haxx.se/blog/2022/12/21/the-2022-curl-security-audit/) about the engagement and [the report](https://github.com/trailofbits/publications/blob/master/reviews/2022-12-curl-securityreview.pdf), and wanted to highlight some important things he pointed out.

In this post, Daniel dives into cURL’s growth since its last audit in 2016: the project; the codebase; and then into the work with Trail of Bits. He touched on both the engagement experience and the final report.

His blog post provides terrific and meaningful context. He gives us high praise, as well as actionable and meaningful critiques that our teams are considering for the future. He also highlights an area in which he disagrees with a finding, providing context on why, and provides links to the responses cURL made to each of the audit points.

We believe software providers should follow Daniel’s lead if they choose to publish their security reviews. This supplementary reading is deeply needed so software developers can provide greater context and clarity around their security decisions. This is a great example of how engineering teams can work with us, and we are very proud of the compliments and cognizant of our responsibility to diligently consider his critiques.

There is one vulnerability highlighted in Daniel’s post that is not included in the final report, because the bug was found after the review ended (our engineers [kept a fuzzer rolling after](https://github.com/trailofbits/curl-fuzzer/blob/master/argv_fuzzing/Dockerfile) the conclusion of the review). That bug, a use-after-free, is now known as [CVE-2022-43552](https://cve.report/CVE-2022-43552). The details are available [on cURL’s website](https://curl.se/docs/CVE-2022-43552.html) and were released in sync with the patch. Trail of Bits will have a blog post about the bug in the future.

While the bug itself isn’t a critical one, the process Daniel and other cURL maintainers took to fix it is a great example of a commitment to excellence. While some software developers think of discovering and patching vulnerabilities as something akin to failure, we believe it is a hallmark of how developers should handle security issues.

We highly recommend [giving the audit report](https://github.com/trailofbits/publications/blob/master/reviews/2022-12-curl-securityreview.pdf), [the threat model](https://github.com/trailofbits/publications/blob/master/reviews/2022-12-curl-threatmodel.pdf), and [Daniel’s post](https://daniel.haxx.se/blog/2022/12/21/the-2022-curl-security-audit/) a read!

#### If you enjoyed this post, share it:

[X](https://x.com/trailofbits "X")

[LinkedIn](https://linkedin.com/company/trail-of-bits "LinkedIn")

[GitHub](https://github.com/trailofbits "GitHub")

[Mastodon](https://infosec.exchange/%40trailofbits "Mastodon")

[Hacker News](https://news.ycombinator.com/from?site=trailofbits.com "Hacker News")

#### Page content

#### Recent Posts

* [Taming 2,500 compiler warnings with CodeQL, an OpenVPN2 case study](/2025/09/25/taming-2500-compiler-warnings-with-codeql-an-openvpn2-case-study/)
* [Supply chain attacks are exploiting our assumptions](/2025/09/24/supply-chain-attacks-are-exploiting-our-assumptions/)
* [Use mutation testing to find the bugs your tests don't catch](/2025/09/18/use-mutation-testing-to-find-the-bugs-your-tests-dont-catch/)
* [Fickling’s new AI/ML pickle file scanner](/2025/09/16/ficklings-new-ai/ml-pickle-file-scanner/)
* [How Sui Move rethinks flash loan security](/2025/09/10/how-sui-move-rethinks-flash-loan-security/)

© 2025 Trail of Bits.
Generated with [Hugo](https://gohugo.io/) and [Mainroad](https://github.com/Vimux/Mainroad/) theme.