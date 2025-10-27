---
title: Supply chain security for Go, Part 3: Shifting left
url: http://security.googleblog.com/2023/07/supply-chain-security-for-go-part-3.html
source: Google Online Security Blog
date: 2023-07-21
fetch_date: 2025-10-04T11:51:02.900740
---

# Supply chain security for Go, Part 3: Shifting left

![](https://ad.doubleclick.net/ddm/activity/src=2542116;type=gblog;cat=googl0;ord=1?)

[![](https://www.gstatic.com/images/branding/googlelogo/2x/googlelogo_color_150x54dp.png)](https://security.googleblog.com/)
[## Security Blog](/.)

The latest news and insights from Google on security and safety on the Internet

## [Supply chain security for Go, Part 3: Shifting left](https://security.googleblog.com/2023/07/supply-chain-security-for-go-part-3.html "Supply chain security for Go, Part 3: Shifting left")

July 20, 2023

Julie Qiu, Go Security & Reliability and Jonathan Metzman, Google Open Source Security Team

Previously in our Supply chain security for Go series, we covered [dependency and vulnerability management tools](https://security.googleblog.com/2023/04/supply-chain-security-for-go-part-1.html) and how [Go ensures package integrity and availability](https://security.googleblog.com/2023/06/supply-chain-security-for-go-part-2.html) as part of the commitment to countering the [rise in supply chain attacks in recent years](https://www.sonatype.com/state-of-the-software-supply-chain/introduction).

In this final installment, we’ll discuss how “shift left” security can help make sure you have the security information you need, when you need it, to avoid unwelcome surprises.

## Shifting left

The software development life cycle (SDLC) refers to the series of steps that a software project goes through, from planning all the way through operation. It’s a cycle because once code has been released, the process continues and repeats through actions like coding new features, addressing bugs, and more.

![](https://lh4.googleusercontent.com/vVCd_nqJ69ITVlp1SiNkfjFhY65vI8bh0LTdqgYfzy02oTcXQmFb_vYiMSFI-2EJwcG6DIVeVGGvO7eVLlJrGmCKmIDuUpKvS8QPoUGVtmnmmBWbXaJJqz_xyPy1SQEnX8P60d5Sdr0NK1S_e6IIGxZL4M-47p2waQI3s06jEMsQkSFOUScUn8YsVOGq1eV7DfOK774m8XOMWEjH4M6hMIsR5NPqRYBq1iOFFQ)

Shifting left involves implementing security practices earlier in the SDLC. For example, consider scanning dependencies for known vulnerabilities; many organizations do this as part of continuous integration (CI) which ensures that code has passed security scans before it is released. However, if a vulnerability is first found during CI, significant time has already been invested building code upon an insecure dependency. Shifting left in this case means allowing developers to run vulnerability scans locally, well before the CI-time scan, so they can learn about issues with their dependencies prior to investing time and effort into creating new code built upon vulnerable dependencies or functions.

## Shifting left with Go

Go provides several features that help you address security early in your process, including [govulncheck](https://go.dev/blog/govulncheck) and [pkg.go.dev](http://pkg.go.dev) discussed in [Supply chain security for Go, Part 1](https://security.googleblog.com/2023/04/supply-chain-security-for-go-part-1.html). Today’s post covers two more features of special interest to supply chain security: the Go extension for Visual Studio Code and built-in fuzz testing.

## VS Code Go extension

## The [VS Code Go extension](https://marketplace.visualstudio.com/items?itemName=golang.Go) helps developers shift left by surfacing problems directly in their code editor. The plugin is loaded with [features](https://github.com/golang/vscode-go/wiki/features) including built in [testing](https://github.com/golang/vscode-go/wiki/features#run-and-test-in-the-editor) and [debugging](https://github.com/golang/vscode-go/wiki/debugging) and [vulnerability information](https://go.dev/security/vuln/editor) right in your IDE. Having these features at your fingertips while coding means good security practices are incorporated into your project as early as possible. For example, by running the govulncheck integration early and often, you'll know whether you are invoking a compromised function before it becomes difficult to extract. Check out [the tutorial](https://go.dev/doc/tutorial/govulncheck-ide) to get started today.

## Fuzz testing in Go

In 2022, Go became the first major programming language to include fuzz testing in its standard toolset with the release of [Go 1.18](https://go.dev/blog/go1.18). [Fuzzing](https://go.dev/security/fuzz/) is a type of automated testing that continuously alters program inputs to find bugs. It plays a huge role in keeping the Go project itself secure – [OSS-Fuzz](https://github.com/google/oss-fuzz) has discovered [eight vulnerabilities](https://github.com/golang/go/issues?q=is%3Aissue+is%3Aclosed+label%3ASecurity+%22OSS-Fuzz%22+-label%3ACherryPickApproved) in the Go Standard library since 2020.

Fuzz testing can find security exploits and vulnerabilities in edge cases that humans often miss, not only your code, but also in your dependencies—which means more insight into your supply chain. With fuzzing included in the standard Go tool set, developers can more easily shift left, fuzzing earlier in their development process. [Our tutorial](https://go.dev/doc/tutorial/fuzz) walks you through how to set up and run your fuzzing tests.

If you maintain a Go package, your project may be eligible for free and continuous fuzzing provided by [OSS-Fuzz](https://google.github.io/oss-fuzz/getting-started/accepting-new-projects/), which supports [native Go fuzzing](https://google.github.io/oss-fuzz/getting-started/new-project-guide/go-lang/#native-go-fuzzing-support). Fuzzing your project, whether on demand through the standard toolset or continuously through OSS-Fuzz is a great way to help protect the people and projects who will use your module.

## Security at the ecosystem level

In the same way that we’re working toward "[secure Go practices](https://go.dev/security/best-practices)" becoming "standard Go practices," the future of software will be more secure for everyone when they’re simply “standard development practices.” Supply chain security threats are real and complex, but we can contribute to solving them by building solutions directly into open source ecosystems.

If you’ve enjoyed this series, come meet the Go team at Gophercon this September! And check out our [closing keynote](https://www.gophercon.com/agenda/session/1160526)—all about how Go’s vulnerability management can help you write more secure and reliable software.

![Share on Twitter](https://www.gstatic.com/images/icons/material/system/2x/post_twitter_black_24dp.png)

![Share on Facebook](https://www.gstatic.com/images/icons/material/system/2x/post_facebook_black_24dp.png)

[Google](https://plus.google.com/112374322230920073195)

#### No comments :

[Post a Comment](https://www.blogger.com/comment/fullpage/post/1176949257541686127/6748517568293147074)

[**](https://security.googleblog.com/)

[**](https://security.googleblog.com/2023/07/the-ups-and-downs-of-0-days-year-in.html "Newer Post")

[**](https://security.googleblog.com/2023/07/a-look-at-chromes-security-review.html "Older Post")

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
* [chrome enterprise](https://security.googl...