---
title: OSV-SCALIBR: A library for Software Composition Analysis
url: http://security.googleblog.com/2025/01/osv-scalibr-library-for-software.html
source: Google Online Security Blog
date: 2025-01-17
fetch_date: 2025-10-06T20:08:25.268863
---

# OSV-SCALIBR: A library for Software Composition Analysis

![](https://ad.doubleclick.net/ddm/activity/src=2542116;type=gblog;cat=googl0;ord=1?)

[![](https://www.gstatic.com/images/branding/googlelogo/2x/googlelogo_color_150x54dp.png)](https://security.googleblog.com/)
[## Security Blog](/.)

The latest news and insights from Google on security and safety on the Internet

## [OSV-SCALIBR: A library for Software Composition Analysis](https://security.googleblog.com/2025/01/osv-scalibr-library-for-software.html "OSV-SCALIBR: A library for Software Composition Analysis")

January 16, 2025

Posted by Erik Varga, Vulnerability Management, and Rex Pan, Open Source Security Team

In December 2022, we [announced OSV-Scanner](https://security.googleblog.com/2022/12/announcing-osv-scanner-vulnerability.html), a tool to enable developers to easily scan for vulnerabilities in their open source dependencies. Together with the open source community, we’ve continued to build this tool, adding [remediation features](https://opensource.googleblog.com/2024/04/osv-and-helping-developers-fix-known-vulnerabilities.html), as well as expanding ecosystem support to 11 programming languages and 20 package manager formats.

Today, we’re excited to release [OSV-SCALIBR](https://github.com/google/osv-scalibr) (Software Composition Analysis LIBRary), an extensible library for SCA and file system scanning. OSV-SCALIBR combines Google’s internal vulnerability management expertise into one scanning library with significant new capabilities such as:

* SCA for installed packages, standalone binaries, as well as source code
* OSes package scanning on Linux (COS, Debian, Ubuntu, RHEL, and much more), Windows, and Mac
* Artifact and lockfile scanning in major language ecosystems (Go, Java, Javascript, Python, Ruby, and much more)
* Vulnerability scanning tools such as weak credential detectors for Linux, Windows, and Mac
* SBOM generation in SPDX and CycloneDX, the two most popular document formats
* Optimization for on-host scanning of resource constrained environments where performance and low resource consumption is critical

OSV-SCALIBR is now the primary SCA engine used within Google for live hosts, code repos, and containers. It’s been used and tested extensively across many different products and internal tools to help generate SBOMs, find vulnerabilities, and help protect our users’ data at Google scale.

We offer OSV-SCALIBR primarily as an open source Go library today, and we're working on adding its new capabilities into OSV-Scanner as the primary CLI interface.

## Using OSV-SCALIBR as a library

All of OSV-SCALIBR's capabilities are modularized into plugins for software extraction and vulnerability detection which are [very simple to expand](https://github.com/google/osv-scalibr/blob/main/docs/new_extractor.md).You can use OSV-SCALIBR as a library to:

1.Generate SBOMs from the build artifacts and code repos on your live host:

|  |
| --- |
| import (   "context"   "github.com/google/osv-scalibr"   "github.com/google/osv-scalibr/converter"   "github.com/google/osv-scalibr/extractor/filesystem/list"   "github.com/google/osv-scalibr/fs"   "github.com/google/osv-scalibr/plugin"   spdx "github.com/spdx/tools-golang/spdx/v2/v2\_3"  )    func GenSBOM(ctx context.Context) \*spdx.Document {   capab := &plugin.Capabilities{OS: plugin.OSLinux}   cfg := &scalibr.ScanConfig{     ScanRoots: fs.RealFSScanRoots("/"),     FilesystemExtractors: list.FromCapabilities(capab),     Capabilities: capab,   }   result := scalibr.New().Scan(ctx, cfg)   return converter.ToSPDX23(result, converter.SPDXConfig{})  } |

2. Scan a git repo for SBOMs:

Simply replace "/" with the path to your git repo. Also take a look at the [various language extractors](https://github.com/google/osv-scalibr/blob/d4ea36720d4e700486fef2ba9b5f2ac2fd8ce6c8/extractor/filesystem/list/list.go#L70) to enable for code scanning.

3. Scan a remote container for SBOMs:

Replace the scan config from the above code snippet with

|  |
| --- |
| import (   ...   "github.com/google/go-containerregistry/pkg/authn"   "github.com/google/go-containerregistry/pkg/v1/remote"   "github.com/google/osv-scalibr/artifact/image"   ...  )    ...  filesys, \_ := image.NewFromRemoteName(   "alpine:latest",   remote.WithAuthFromKeychain(authn.DefaultKeychain),  )  cfg := &scalibr.ScanConfig{   ScanRoots: []\*fs.ScanRoot{{FS: filesys}},   ...  } |

4. Find vulnerabilities on your filesystem or a remote container:

Extract the PURLs from the [SCALIBR inventory results](https://github.com/google/osv-scalibr/blob/08fdef73ebdffae84479e5c900f6e2c0c2865034/scalibr.go#L157) from the previous steps:

|  |
| --- |
| import (   ...   "github.com/google/osv-scalibr/converter"   ...  )  ...  result := scalibr.New().Scan(ctx, cfg)  for \_, i := range result.Inventories {   fmt.Println(converter.ToPURL(i))  } |

And send them to [osv.dev](http://osv.dev), e.g.

|  |
| --- |
| $ curl -d '{"package": {"purl": "pkg:npm/dojo@1.2.3"}}' "https://api.osv.dev/v1/query" |

See [the usage docs](https://github.com/google/osv-scalibr?tab=readme-ov-file#how-to-use) for more details.

## OSV-Scanner + OSV-SCALIBR

Users looking for an out-of-the-box vulnerability scanning CLI tool should check out [OSV-Scanner](https://github.com/google/osv-scanner), which already provides comprehensive language package scanning capabilities using much of the same extraction as OSV-SCALIBR.

Some of OSV-SCALIBR’s capabilities are not yet available in OSV-Scanner, but we’re currently working on integrating OSV-SCALIBR more deeply into OSV-Scanner. This will make more and more of OSV-SCALIBR’s capabilities available in OSV-Scanner in the next few months, including installed package extraction, weak credentials scanning, SBOM generation, and more.

Look out soon for an announcement of OSV-Scanner V2 with many of these new features available. OSV-Scanner will become the primary frontend to the OSV-SCALIBR library for users who require a CLI interface. Existing users of OSV-Scanner can continue to use the tool the same way, with backwards compatibility maintained for all existing use cases.

For installation and usage instructions, have a look at OSV-Scanner’s documentation [here](https://google.github.io/osv-scanner/).

##

## What’s next

In addition to making all of OSV-SCALIBR’s features available in OSV-Scanner, we're also working on additional new capabilities. Here's some of the things you can expect:

* Support for more OS and language ecosystems, both for regular extraction and for [Guided Remediation](https://osv.dev/blog/posts/announcing-guided-remediation-in-osv-scanner/)
* Layer attribution and base image identification for container scanning
* Reachability analysis to reduce false positive vulnerability matches
* More vulnerability and misconfiguration detectors for Windows
* More weak credentials detectors

We hope that this library helps developers and organizations to secure their software and encourages the open source community to contribute back by sharing new plugins on top of OSV-SCALIBR.

If you have any questions or if you would like to contribute, don't hesitate to reach out to us at osv-discuss@google.com or by posting an issue in our [issue tracker](https://github.com/google/osv-scalibr/issues).

![Share on Twitter](https://www.gstatic.com/images/icons/material/system/2x/post_twitter_black_24dp.png)

![Share on Facebook](https://www.gstatic.com/images/icons/material/system/2x/post_facebook_black_24dp.png)

[Google](https://plus.google.com/112374322230920073195)

#### No comments :

[Post a Comment](https://www.blogger.com/comment/fullpage/post/1176949257541686127/8807395669079430849)

[**](https://security.googleblog.com/)

[**](https://security.googleblog.com/2025/01/android-theft-protection-identity-check-expanded-features.html "Newer Post")

[**](https://security.googleblog.com/2024/12/google-cloud-expands-vulnerability.html "Older Post")

![](data:image/png;base64...)

## Labels

**

* [#sharethemicincyber](https://securi...