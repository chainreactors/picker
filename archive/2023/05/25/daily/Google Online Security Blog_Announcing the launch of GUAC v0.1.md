---
title: Announcing the launch of GUAC v0.1
url: http://security.googleblog.com/2023/05/announcing-launch-of-guac-v01.html
source: Google Online Security Blog
date: 2023-05-25
fetch_date: 2025-10-04T11:37:44.573149
---

# Announcing the launch of GUAC v0.1

![](https://ad.doubleclick.net/ddm/activity/src=2542116;type=gblog;cat=googl0;ord=1?)

[![](https://www.gstatic.com/images/branding/googlelogo/2x/googlelogo_color_150x54dp.png)](https://security.googleblog.com/)
[## Security Blog](/.)

The latest news and insights from Google on security and safety on the Internet

## [Announcing the launch of GUAC v0.1](https://security.googleblog.com/2023/05/announcing-launch-of-guac-v01.html "Announcing the launch of GUAC v0.1")

May 24, 2023

Brandon Lum and Mihai Maruseac, Google Open Source Security Team

Today, we are announcing the launch of the v0.1 version of [Graph for Understanding Artifact Composition](http://guac.sh) (GUAC). [Introduced](https://security.googleblog.com/2022/10/announcing-guac-great-pairing-with-slsa.html) at Kubecon 2022 in October, GUAC targets a critical need in the software industry to understand the software supply chain. In collaboration with [Kusari](http://kusari.dev), [Purdue University](http://purdue.edu), [Citi](http://citi.com), and [community members](https://github.com/guacsec/guac/contributors), we have incorporated feedback from our early testers to improve GUAC and make it more useful for security professionals. This improved version is now available as an API for you to start developing on top of, and integrating into, your systems.

# The need for GUAC

High-profile incidents such as [Solarwinds](https://www.npr.org/2021/04/16/985439655/a-worst-nightmare-cyberattack-the-untold-story-of-the-solarwinds-hack), and the [recent 3CX supply chain double-exposure](https://www.wired.com/story/3cx-supply-chain-attack-times-two/), are evidence that supply chain attacks are getting more sophisticated. As highlighted by the [U.S. Executive Order on Cybersecurity](https://www.whitehouse.gov/briefing-room/presidential-actions/2021/05/12/executive-order-on-improving-the-nations-cybersecurity/), there’s a critical need for security professionals, CISOs, and security engineers to be able to more deeply link information from different supply chain ecosystems to keep up with attackers and prevent exposure. Without linking different sources of information, it’s impossible to have a clear understanding of the potential risks posed by the software components in an organization.

GUAC aggregates software security metadata and maps it to a standard vocabulary of concepts relevant to the software supply chain. This data can be accessed via a GraphQL interface, allowing development of a rich ecosystem of integrations, command-line tools, visualizations, and policy engines.

We hope that GUAC will help the wider software development community better evaluate the supply chain security posture of their organizations and projects. Feedback from early adopters has been overwhelmingly positive:

“At Yahoo, we have found immense value and significant efficiency by utilizing the open source project GUAC. GUAC has allowed us to streamline our processes and increase efficiency in a way that was not possible before,” said Hemil Kadakia, Sr. Mgr. Software Dev Engineering, Paranoids, Yahoo.

# The power of GUAC

## Dynamic aggregation

## GUAC is not just a static database—it is the first application that is continuously evolving the database pertaining to the software that an organization develops or uses. Supply chains change daily, and by aggregating your Software Bill of Materials (SBOMs) and Supply-chain Levels for Software Artifacts (SLSA) attestations with threat intelligence sources (e.g., OSV vulnerability feeds) and OSS insights (e.g., deps.dev), GUAC is constantly incorporating the latest threat information and deeper analytics to help paint a more complete picture of your risk profile. And by merging external data with internal private metadata, GUAC brings the same level of reasoning to a company’s first-party software portfolio.

## Seamless integration of incomplete metadata

## Because of the complexity of the modern software stack—often spanning languages and toolchains—we discovered during GUAC development that it is difficult to produce high-quality SBOMs that are accurate, complete, and meet specifications and intents.

Following the [U.S. Executive Order on Cybersecurity](https://www.whitehouse.gov/briefing-room/presidential-actions/2021/05/12/executive-order-on-improving-the-nations-cybersecurity/), there are now a large number of SBOM documents being generated during release and build workflows to explain to consumers what’s in their software. Given the difficulty in producing accurate SBOMs, consumers often face a situation where they have incomplete, inaccurate, or conflicting SBOMs. In these situations, GUAC can fill in the gaps in the various supply chain metadata: GUAC can link the documents and then use heuristics to improve the quality of data and guess at the correct intent. Additionally, the GUAC community is now [working closely with SPDX](https://github.com/spdx/tools-golang/pull/204) to [advance SBOM tooling](https://github.com/anchore/syft/issues/1241) and improve the quality of metadata.

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgMrXpJaQ3dpIGxExrNWEryi7jlOaTnUWNrb6gc5hp8-F2doNguYr8XRS_x3-dBvchf-jcu1K1Xb_CPSTyL6xoAPyxCCDz7-c0Gs9RJxCSLeRgQG2fEmwKmKBqB4YaOG2tHmwJPcXrXdIf3HBBPn0aYGvR8CBwY5sW7ZKk19A0tlDiL43DB4_HE6g09aw/w564-h340/Screenshot%202023-05-24%20at%209.47.26%20AM.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgMrXpJaQ3dpIGxExrNWEryi7jlOaTnUWNrb6gc5hp8-F2doNguYr8XRS_x3-dBvchf-jcu1K1Xb_CPSTyL6xoAPyxCCDz7-c0Gs9RJxCSLeRgQG2fEmwKmKBqB4YaOG2tHmwJPcXrXdIf3HBBPn0aYGvR8CBwY5sW7ZKk19A0tlDiL43DB4_HE6g09aw/s641/Screenshot%202023-05-24%20at%209.47.26%20AM.png)

## GUAC's process for incorporating and enriching metadata for organizational insight

## Consistent interfaces

Alongside the boom in SBOM production, there’s been a rapid expansion of new standards, document types, and formats, making it hard to perform consistent queries. The multiple formats for software supply chain metadata often refer to similar concepts, but with different terms. To integrate these, GUAC defines a common vocabulary for talking about the software supply chain—for example, artifacts, packages, repositories, and the relationships between them.

This vocabulary is then exposed as a GraphQL API, empowering users to build powerful integrations on top of GUAC’s knowledge graph. For example, users are able to query seamlessly with the same commands across different SBOM formats like SPDX and CycloneDX.

According to Ed Warnicke, Distinguished Engineer at Cisco Systems, "Supply chain security is increasingly about making sense of many different kinds of metadata from many different sources. GUAC knits all of that information together into something understandable and actionable."

# Potential integrations

Based on these features, we envision potential integrations that users can build on top of GUAC in order to:

* Create policies based on trust
* Quickly react to security compromises
* Determine an upgrade plan in response to a security incident
* Create visualizers for data explorations, CLI tools for large scale analysis and incident response, CI checks, IDE plugins to shift policy left, and more

Developers can also build data source integrations under GUAC to expand its coverage. The entire GUAC architecture is plug-and-play, so you can write data integrations to get:

* Supply chain metadata from new sources like your preferred security vendors
* Parsers to translate this metadata into the GUAC ontology
* Database backends to store the GUAC data in either common databases or in organization-defined private data stores

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEibVrfQoo0lkUIl9wRTLqYSRT0zMECVnqzprq1B2vQwPWNy7_Tg9hJrUJro5ibgAjLq8JvCrqJ6BTgm3UTUaho1LDZJCKUUuVl_oZTyAGBvK4BHtGAF_wFvMBa30gquf1fLURqpxQxiSvIQaGnahVh5FKZfEck2BHYYZrOPz52RYFHdA0U1AUc3Cg17ew/w527-h458/Screenshot%202023-05-24%20at%209.47.34%20AM.png)](https://blogger.googleusercontent...