---
title: Introducing rules_oci
url: http://security.googleblog.com/2023/05/introducing-rulesoci.html
source: Google Online Security Blog
date: 2023-05-06
fetch_date: 2025-10-04T11:38:25.588272
---

# Introducing rules_oci

![](https://ad.doubleclick.net/ddm/activity/src=2542116;type=gblog;cat=googl0;ord=1?)

[![](https://www.gstatic.com/images/branding/googlelogo/2x/googlelogo_color_150x54dp.png)](https://security.googleblog.com/)
[## Security Blog](/.)

The latest news and insights from Google on security and safety on the Internet

## [Introducing rules\_oci](https://security.googleblog.com/2023/05/introducing-rulesoci.html "Introducing rules_oci")

May 5, 2023

Appu Goundan, Google Open Source Security Team

Today, we are announcing the General Availability 1.0 version of rules\_oci, an open-sourced Bazel plugin (“ruleset”) that makes it simpler and more secure to build container images with Bazel. This effort was a collaboration we had with [Aspect](https://aspect.build/) and the [Rules Authors Special Interest Group](https://bazel-contrib.github.io/SIG-rules-authors/). In this post, we’ll explain how rules\_oci differs from its predecessor, rules\_docker, and describe the benefits it offers for both container image security and the container community.

# Bazel and Distroless for supply chain security

Google’s popular build and test tool, known as Bazel, is gaining fast adoption within enterprises thanks to its ability to scale to the largest codebases and handle builds in almost any language. Because Bazel manages and caches dependencies by their integrity hash, it is uniquely suited to make assurances about the supply chain based on the Trust-on-First-Use principle. One way Google uses Bazel is to build widely used Distroless base images for Docker.

Distroless is a series of minimal base images which improve supply-chain security. They restrict what's in your runtime container to precisely what's necessary for your app, which is a best practice employed by Google and other tech companies that have used containers in production for many years. Using minimal base images reduces the burden of managing risks associated with security vulnerabilities, licensing, and governance issues in the supply chain for building applications.

# rules\_oci vs rules\_docker

Historically, building container images was supported by rules\_docker, which is [now in maintenance mode](https://github.com/bazelbuild/rules_docker#status). The new ruleset, called [rules\_oci](https://github.com/bazel-contrib/rules_oci), is better suited for Distroless as well as most Bazel container builds for several reasons:

* The [Open Container Initiative](https://opencontainers.org/) standard has changed the playing field, and there are now multiple container runtimes and image formats. rules\_oci is not tied to running a docker daemon already installed on the machine.
* rules\_docker was created before many excellent container manipulation tools existed, such as Crane, Skopeo, and Zot. rules\_oci is able to simply rely on trusted third-party toolchains and avoid building or maintaining any Bazel-specific tools.
* rules\_oci doesn’t include any language-specific rules, which makes it much more maintainable than rules\_docker. Also, it avoids the pitfalls of stale dependencies on other language rulesets.

# Other benefits of rules\_oci

There are other great features of rules\_oci to highlight as well. For example, it uses Bazel’s downloader to fetch layers from a remote registry, improving caching and allowing transparent use of a private registry. Multi-architecture images make it more convenient to target platforms like ARM-based servers, and support Windows Containers as well. Code signing allows users to verify that a container image they use was created by the developer who signed it, and was not modified by any third-party along the way (e.g. person-in-the-middle attack). In combination with the work on [Bazel team’s roadmap](https://bazel.build/about/roadmap#software_bill_of_materials_data_generation_sboms_oss_license_compliance_tools), you’ll also get a Software Bill of Materials (SBOM) showing what went into the container you use.

Since adopting rules\_oci and Bazel 6, the Distroless team has seen a number of improvements to our build processes, image outputs, and security metadata:

* Native support for signing allows us to eliminate a race condition that could have left some images unsigned. We now sign on immutable digests references to images during the build instead of tags after the build.
* Native support for oci indexes (multi platform images) allowed us to remove our dependency on docker during build. This also means more natural and debuggable failures when something goes wrong with multi platform builds.
* Improvements to fetching and caching means our CI builds are faster and more reliable when using remote repositories.
* Distroless images are now accompanied by SBOMs embedded in a signed attestation, which you can view with cosign and some jq magic:

cosign download attestation gcr.io/distroless/base:latest-amd64 | jq -rcs '.[0].payload' | base64 -d | jq -r '.predicate' | jq

In the end, rules\_oci allowed us to modernize the Distroless build while also adding necessary supply chain security metadata to allow organizations to make better decisions about the images they consume.

# Get started with rules\_oci

Today, we’re happy to announce that rules\_oci is now a 1.0 version. This stability guarantee follows the semver standard, and promises that future releases won’t include breaking public API changes. Aspect provides resources for using rules\_oci, such as a [Migration guide](https://docs.aspect.build/guides/rules_oci_migration) from rules\_docker. It also provides support, training, and consulting services for effectively adopting rules\_oci to build containers in all languages.

If you use rules\_docker today, or are considering using Bazel to build your containers, this is a great time to give rules\_oci a try. You can help by filing actionable issues, contributing code, or donating to the [Rules Authors SIG OpenCollective](https://opencollective.com/bazel-rules-authors-sig). Since the project is developed and maintained entirely as community-driven open source, your support is essential to keeping the project healthy and responsive to your needs.

Special thanks to Sahin Yort and Alex Eagle from Aspect.

![Share on Twitter](https://www.gstatic.com/images/icons/material/system/2x/post_twitter_black_24dp.png)

![Share on Facebook](https://www.gstatic.com/images/icons/material/system/2x/post_facebook_black_24dp.png)

[Google](https://plus.google.com/112374322230920073195)

#### No comments :

[Post a Comment](https://www.blogger.com/comment/fullpage/post/1176949257541686127/7390451789545080658)

[**](https://security.googleblog.com/)

[**](https://security.googleblog.com/2023/05/making-authentication-faster-than-ever.html "Newer Post")

[**](https://security.googleblog.com/2023/05/so-long-passwords-thanks-for-all-phish.html "Older Post")

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
* [chrome security](https://security.googleblog.com/search/label/chrome%20se...