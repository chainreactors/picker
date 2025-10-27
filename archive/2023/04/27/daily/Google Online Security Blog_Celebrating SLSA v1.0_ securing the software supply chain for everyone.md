---
title: Celebrating SLSA v1.0: securing the software supply chain for everyone
url: http://security.googleblog.com/2023/04/celebrating-slsa-v10-securing-software.html
source: Google Online Security Blog
date: 2023-04-27
fetch_date: 2025-10-04T11:31:28.277888
---

# Celebrating SLSA v1.0: securing the software supply chain for everyone

![](https://ad.doubleclick.net/ddm/activity/src=2542116;type=gblog;cat=googl0;ord=1?)

[![](https://www.gstatic.com/images/branding/googlelogo/2x/googlelogo_color_150x54dp.png)](https://security.googleblog.com/)
[## Security Blog](/.)

The latest news and insights from Google on security and safety on the Internet

## [Celebrating SLSA v1.0: securing the software supply chain for everyone](https://security.googleblog.com/2023/04/celebrating-slsa-v10-securing-software.html "Celebrating SLSA v1.0: securing the software supply chain for everyone ")

April 26, 2023

Bob Callaway, Staff Security Engineer, Google Open Source Security team

Last week the Open Source Security Foundation (OpenSSF) [announced the release of SLSA v1.0](https://openssf.org/press-release/2023/04/19/openssf-announces-slsa-version-1-0-release/), a framework that helps secure the software supply chain. Ten years of using an [internal version of SLSA at Google](https://cloud.google.com/docs/security/binary-authorization-for-borg) has shown that it’s crucial to warding off tampering and keeping software secure. It’s especially gratifying to see SLSA reaching v1.0 as an open source project—contributors have come together to produce solutions that will benefit everyone.

### SLSA for safer supply chains

Developers and organizations that adopt SLSA will be protecting themselves against a variety of supply chain attacks, which have continued rising since Google first donated SLSA to OpenSSF in 2021. In that time, the industry has also seen a [U.S. Executive Order on Cybersecurity](https://www.whitehouse.gov/briefing-room/presidential-actions/2021/05/12/executive-order-on-improving-the-nations-cybersecurity/) and the associated NIST [Secure Software Development Framework](https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-218.pdf) (SSDF) to guide national standards for software used by the U.S. government, as well as the [Network and Information Security](https://www.europarl.europa.eu/thinktank/en/document/EPRS_BRI%282021%29689333) (NIS2) Directive in the European Union. SLSA offers not only an onramp to meeting these standards, but also a way to prepare for a climate of increased scrutiny on software development practices.

As organizations benefit from using SLSA, it’s also up to them to shoulder part of the burden of spreading these benefits to open source projects. Many maintainers of the critical open source projects that underpin the internet are volunteers; they cannot be expected to do all the work when so many of the rewards of adopting SLSA roll out across the supply chain to benefit everyone.

### Supply chain security for all

That’s why beyond contributing to SLSA, we’ve also been laying the foundation to integrate supply chain solutions directly into the ecosystems and platforms used to create open source projects. We’re also directly supporting open source maintainers, who often cite lack of time or resources as limiting factors when making security improvements to their projects.

Our Open Source Security Upstream Team consists of developers [who spend 100% of their time contributing to critical open source projects](https://opensource.googleblog.com/2023/04/googles-open-source-security-upstream-team-one-year-later.html) to make security improvements. For open source developers who choose to adopt SLSA on their own, we’ve funded the [Secure Open Source Rewards Program](https://www.sos.dev), which pays developers directly for these types of security improvements.

Currently, open source developers who want to secure their builds can use the free [SLSA L3 GitHub Builder](https://github.com/slsa-framework/slsa-github-generator), which requires only a one-time adjustment to the traditional build process implemented through GitHub actions. There’s also the [SLSA Verifier](https://github.com/slsa-framework/slsa-verifier) tool for software consumers. Users of npm—or Node Package Manager, the world’s largest software repository—can take advantage of their [recently released beta SLSA integration](https://github.blog/2023-04-19-introducing-npm-package-provenance/), which streamlines the process of creating and verifying SLSA provenance through the npm command line interface. We’re also supporting the integration of [Sigstore](https://www.sigstore.dev) into many major package ecosystems, meaning that users can sign and verify artifacts directly from package management tooling, without having to manage keys. Our intention is to continue to expand these types of integrations across open source ecosystems so supply chain security solutions are universal and easily accessible.

We’re also making it easier for everyone to understand their dependencies. Vulnerabilities like [Log4Shell](https://security.googleblog.com/2021/12/understanding-impact-of-apache-log4j.html) have shown the importance (and difficulty) of knowing what projects you depend on and where their security weaknesses might be. Developers can use the [deps.dev API](https://security.googleblog.com/2023/04/announcing-depsdev-api-critical.html) to generate real dependency graphs, with [OpenSSF Scorecard](https://github.com/ossf/scorecard) security scores and other security metadata for each dependency they use. They can also use [OSV-Scanner](https://google.github.io/osv-scanner/) to generate a high quality list of actionable vulnerabilities in those dependencies. In the future, we hope to support automatic remediation and patching through the [OSV database service](https://osv.dev/), minimizing the effort that open source developers spend on securing their projects.

### Continued community contributions

Ultimately, our goal is to make supply chain security invisible and available to everyone, built directly into each ecosystem for frictionless adoption. To get there, we’ll continue contributing to these efforts and encouraging other organizations who rely on open source to similarly dedicate developers to upstream support. The internet as we know it today wouldn’t be available without open source software, and it’s in everyone’s best interests to give back to the communities that make modern software development possible.

![Share on Twitter](https://www.gstatic.com/images/icons/material/system/2x/post_twitter_black_24dp.png)

![Share on Facebook](https://www.gstatic.com/images/icons/material/system/2x/post_facebook_black_24dp.png)

[Google](https://plus.google.com/112374322230920073195)

#### No comments :

[Post a Comment](https://www.blogger.com/comment/fullpage/post/1176949257541686127/1511228391917384974)

[**](https://security.googleblog.com/)

[**](https://security.googleblog.com/2023/04/how-we-fought-bad-apps-and-bad-actors.html "Newer Post")

[**](https://security.googleblog.com/2023/04/google-authenticator-now-supports.html "Older Post")

![](data:image/png;base64...)

## Labels

**

* [#sharethemicincyber](https://security.googleblog.com/search/label/%23sharethemicincyber)
* [#supplychain #security #opensource](https://security.googleblog.com/search/label/%23supplychain%20%23security%20%23opensource)
* [AI Security](https://security.googleblog.com/search/label/AI%20Security)
* [android](https://security.googleblog.com/search/label/android)
* [android security](https://security.googleblog.com/search/label/android%20security)
* [android tr](https://security.googleblog.com/search/label/android%20tr)
* [app security](https://security.googleblog.com/search/label/app%20security)
* [big data](https://security.googleblog.com/search/label/big%20data)
* [biometrics](https://security.googleblog.com/search/label/biometrics)
* [blackhat](https://security.googleblog.com/search/label/blackhat)
* [C++](https://security.googleblog.com/search/label/C%2B%2B)
* [chrome](https://security.googleblog.com/search/label/chrome)
* [chrome enterprise](https://security.googleblog.com/search/label/chrome%20enterprise)
* [chrome security](https://security.googleblog.com/search/label/chrome%20security)
* [connected devices...