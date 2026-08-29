---
title: grype v0.118.0
url: https://kitploit.com/en/posts/github-anchore-grype-v01180
source: Kitploit
date: 2026-08-28
fetch_date: 2026-08-29T08:31:20.166266
---

# grype v0.118.0

[Skip to content](#main-content)

[![Kitploit](/_next/image?url=%2Flogo.png&w=64&q=75)KITPLOIT](/en)[Tools](/en/tools)[Blog](/en/blog)Categories

EN

[Submit](/en/submit)

[Tools](/en/tools)[Blog](/en/blog)Categories

[Submit](/en/submit)

EN

Hacking, PenTest, and Cybersecurity Tools for Your Security Arsenal!

[Back to updates](/en/updates)

![](https://assets.kitploit.com/production/tools/168/243150ef263a85416b83a708411795f9dc8a93fb0411a197e33aad8bbfe9a58b.gif)

New releaseAug 28, 2026

# grype v0.118.0

A vulnerability scanner for container images and filesystems

Share

![Grype logo](https://assets.kitploit.com/production/public/readmes/168/c73939c5003a9bd10bbe79b7efaa6dde2f04c2ae05260d1c63b344bf646fb70d.png)

# Grype

**A vulnerability scanner for container images and filesystems.**

[![Static Analysis + Unit + Integration](https://github.com/anchore/grype/workflows/Static%20Analysis%20+%20Unit%20+%20Integration/badge.svg)](https://github.com/anchore/grype/actions?query=workflow%3A%22Static+Analysis+%2B+Unit+%2B+Integration%22)
 [![Validations](https://github.com/anchore/grype/workflows/Validations/badge.svg)](https://github.com/anchore/grype/actions/workflows/validations.yaml)
 [![Go Report Card](https://goreportcard.com/badge/github.com/anchore/grype)](https://goreportcard.com/report/github.com/anchore/grype)
 [![GitHub release](https://img.shields.io/github/release/anchore/grype.svg)](https://github.com/anchore/grype/releases/latest)
 [![GitHub go.mod Go version](https://img.shields.io/github/go-mod/go-version/anchore/grype.svg)](https://github.com/anchore/grype)
 [![License: Apache-2.0](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](https://github.com/anchore/grype/blob/main/LICENSE)
 [![Join our Discourse](https://img.shields.io/badge/Discourse-Join-blue?logo=discourse)](https://anchore.com/discourse)
 [![Follow on Mastodon](https://img.shields.io/badge/Mastodon-Follow-blue?logoColor=white&logo=mastodon)](https://fosstodon.org/%40grype)

![grype-demo](https://assets.kitploit.com/production/public/readmes/168/243150ef263a85416b83a708411795f9dc8a93fb0411a197e33aad8bbfe9a58b.gif)

## Features

* Scan **container images**, **filesystems**, and **SBOMs** for known vulnerabilities (see the docs for a full list of [supported scan targets](https://oss.anchore.com/docs/guides/vulnerability/scan-targets/))
* Supports major OS package ecosystems (Alpine, Debian, Ubuntu, RHEL, Oracle Linux, Amazon Linux, and [more](https://oss.anchore.com/docs/capabilities/all-os/))
* Supports language-specific packages (Ruby, Java, JavaScript, Python, .NET, Go, PHP, Rust, and [more](https://oss.anchore.com/docs/capabilities/all-packages/))
* Supports Docker, OCI, and [Singularity](https://github.com/sylabs/singularity) image formats
* Threat & risk prioritization with **EPSS**, **KEV**, and **risk scoring** (see [interpreting the results docs](https://oss.anchore.com/docs/guides/vulnerability/interpreting-results/))
* [OpenVEX](https://github.com/openvex) support for filtering and augmenting scan results

> [!TIP]
> New to Grype? Check out the [Getting Started guide](https://oss.anchore.com/docs/guides/vulnerability/getting-started/) for a walkthrough!

## Installation

The quickest way to get up and going:

root@kitploit:~

```
curl -sSfL https://get.anchore.io/grype | sudo sh -s -- -b /usr/local/bin
```

> [!TIP]
> See [Installation docs](https://oss.anchore.com/docs/installation/grype/) for more ways to get Grype, including Homebrew, Docker, Chocolatey, MacPorts, and more!

## The basics

Scan a container image or directory for vulnerabilities:

root@kitploit:~

```
# container image
grype alpine:latest

# directory
grype ./my-project
```

Scan an SBOM for even faster vulnerability detection:

root@kitploit:~

```
# scan a Syft SBOM
grype sbom:./sbom.json

# pipe an SBOM into Grype
cat ./sbom.json | grype
```

> [!TIP]
> Check out the [Getting Started guide](https://oss.anchore.com/docs/guides/vulnerability/getting-started/) to explore all of the capabilities and features.
>
> Want to know all of the ins-and-outs of Grype? Check out the [CLI docs](https://oss.anchore.com/docs/reference/grype/cli/) and [configuration docs](https://oss.anchore.com/docs/reference/grype/configuration/).

## Contributing

We encourage users to help make these tools better by [submitting issues](https://github.com/anchore/grype/issues) when you find a bug or want a new feature.
Check out our [contributing overview](https://oss.anchore.com/docs/contributing/) and [developer-specific documentation](https://oss.anchore.com/docs/contributing/grype/) if you are interested in providing code contributions.

Grype development is sponsored by [Anchore](https://anchore.com/), and is released under the [Apache-2.0 License](https://github.com/anchore/grype?tab=Apache-2.0-1-ov-file).
The [Grype logo](https://anchore.com/wp-content/uploads/2024/11/grype-logo.svg) by [Anchore](https://anchore.com/) is licensed under [CC BY 4.0![](https://mirrors.creativecommons.org/presskit/icons/cc.svg)![](https://mirrors.creativecommons.org/presskit/icons/by.svg)](https://creativecommons.org/licenses/by/4.0/)

For commercial support options with Syft or Grype, please [contact Anchore](https://get.anchore.com/contact/).

## Come talk to us!

The Grype Team holds regular community meetings online. All are welcome to join to bring topics for discussion.

* Check the [calendar](https://calendar.google.com/calendar/u/0/r?cid=Y182OTM4dGt0MjRtajI0NnNzOThiaGtnM29qNEBncm91cC5jYWxlbmRhci5nb29nbGUuY29t) for the next meeting date.
* Add items to the [agenda](https://docs.google.com/document/d/1ZtSAa6fj2a6KRWviTn3WoJm09edvrNUp4Iz_dOjjyY8/edit?usp=sharing) (join [this group](https://groups.google.com/g/anchore-oss-community) for write access to the [agenda](https://docs.google.com/document/d/1ZtSAa6fj2a6KRWviTn3WoJm09edvrNUp4Iz_dOjjyY8/edit?usp=sharing))
* See you there!

[Read more](/en/tools/github/anchore/grype?expand=1)

## Categories

[Static Analysis](/en/categories/static-analysis)[Vulnerability Scanners](/en/categories/vulnerability-scanners)[Container Security](/en/categories/container-security)[DevSecOps](/en/categories/devsecops)[Secret Detection](/en/categories/secret-detection)[Supply Chain Security](/en/categories/supply-chain-security)[Container Escape](/en/categories/container-escape)

### Most Popular

[View all →](/en/tools)

Discover the most used tools by our community.

Last 7 DaysLast 30 Days

Explore all tools

Browse our collection of tools

[View all tools →](/en/tools)

Kitploit is a directory of hacking, cybersecurity, and pentesting tools. Discover the latest project updates to find vulnerabilities, analyze systems, automate testing, and strengthen your security.

·Analytics preferences·[Feeds](/en/feeds)·[Contact](/en/contact)·[Privacy](/en/privacy)·© 2026 Kitploit

Tool Directory

## Categories

[View all categories](/en/categories)

Loading categories