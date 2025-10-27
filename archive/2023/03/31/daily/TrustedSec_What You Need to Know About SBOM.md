---
title: What You Need to Know About SBOM
url: https://www.trustedsec.com/blog/what-you-need-to-know-about-sbom/
source: TrustedSec
date: 2023-03-31
fetch_date: 2025-10-04T11:16:48.192225
---

# What You Need to Know About SBOM

[Skip to Main Content](#main)

All Trimarc services are now delivered through TrustedSec!
[Learn more](https://trustedsec.com/about-us/news/trimarc-joins-forces-with-trustedsec-to-strengthen-security-advisory-services)

Close

[TrustedSec](https://trustedsec.com/)

* [Solutions](https://trustedsec.com/solutions)

  ## Solutions

  Our custom solutions are tailored to address the unique challenges of different roles in security.

  [Solutions](https://trustedsec.com/solutions)

  + [01

    For Leadership

    We understand the challenges facing modern executives and develop solutions unique to leaders.](https://trustedsec.com/solutions/for-leadership)
  + [02

    For Operations

    We stay one step ahead to proactively safeguard our clients and partners.](https://trustedsec.com/solutions/for-operations)
  + [03

    For Infrastructure

    From architecture to resiliency and maintainability, we keep your tech aligned to best practices.](https://trustedsec.com/solutions/for-infrastructure)
  + [04

    For Assurance

    Our compliance experts guide partners through regulatory requirements to ensure standards are met.](https://trustedsec.com/solutions/for-assurance)
* [Services](https://trustedsec.com/services)

  ## Services

  From building to testing to hardening, our services support security at every stage.

  [Services](https://trustedsec.com/services)

  + [01

    Design

    Design an exceptional, custom security program alongside our security experts.](https://trustedsec.com/services/design)
  + [02

    Evaluate

    Evaluate your security program with proven assessment methodologies.](https://trustedsec.com/services/evaluate)
  + [03

    Harden

    Harden your security program with the help of our security experts.](https://trustedsec.com/services/harden)
  + [04

    Respond

    Respond to threats to your security program with the help of our security experts.](https://trustedsec.com/services/respond)
* [Research](https://trustedsec.com/research)
* [Blog](https://trustedsec.com/blog)
* [Resources](https://trustedsec.com/resources)
* [About Us](https://trustedsec.com/about-us)

  ## About Us

  Driven by purpose, fueled by experts.

  [About Us](https://trustedsec.com/about-us)

  + [01

    Our Team

    Meet our security experts.](https://trustedsec.com/about-us/our-team)
  + [02

    Our Partners

    Become a TrustedSec partner to help your customers anticipate and prepare for potential attacks.](https://trustedsec.com/about-us/our-partners)
  + [03

    News

    Our team is trusted by local and national media to be the subject matter experts for security news.](https://trustedsec.com/about-us/news)
  + [04

    Events

    See our upcoming webinars, conferences, talks, trainings, and more!](https://trustedsec.com/about-us/events)

Search

Menu

Search Input

Search

* [Contact Us](https://trustedsec.com/contact)
* [Report a breach](https://trustedsec.com/report-a-breach)

* [Solutions](https://trustedsec.com/solutions)
* [Services](https://trustedsec.com/services)
* [Research](https://trustedsec.com/research)
* [Blog](https://trustedsec.com/blog)
* [Resources](https://trustedsec.com/resources)
* [About Us](https://trustedsec.com/about-us)

Search

* [Contact Us](https://trustedsec.com/contact)
* [Report a breach](https://trustedsec.com/report-a-breach)

* [Blog](https://trustedsec.com/blog)
* [What You Need to Know About SBOM](https://trustedsec.com/blog/what-you-need-to-know-about-sbom)

March 30, 2023

# What You Need to Know About SBOM

Written by
Charles Yost

![](https://trusted-sec.transforms.svdcdn.com/production/images/Blog-Covers/SBOM_WebHero.jpg?w=320&h=320&q=90&auto=format&fit=crop&dm=1695562340&s=9f2906b54335f6ba3972c0c68df12aff)

Share

* Share URL
* [Share via Email](/cdn-cgi/l/email-protection#57682422353d3234236a143f32343c726567382223726567233f3e247265673625233e343b327265673125383a7265670325222423323304323472656671363a276c3538332e6a003f36237265670e38227265671932323372656723387265671c39382072656716353822237265670415181a7264167265673f23232724726416726511726511232522242332332432347934383a726511353b3830726511203f36237a2e38227a393232337a23387a3c3938207a36353822237a2435383a "Share via Email")
* [Share on Facebook](http://www.facebook.com/sharer.php?u=https%3A%2F%2Ftrustedsec.com%2Fblog%2Fwhat-you-need-to-know-about-sbom "Share on Facebook")
* [Share on X](http://twitter.com/share?text=What%20You%20Need%20to%20Know%20About%20SBOM%3A%20https%3A%2F%2Ftrustedsec.com%2Fblog%2Fwhat-you-need-to-know-about-sbom "Share on X")
* [Share on LinkedIn](https://www.linkedin.com/shareArticle?url=https%3A%2F%2Ftrustedsec.com%2Fblog%2Fwhat-you-need-to-know-about-sbom&mini=true "Share on LinkedIn")

![](https://www.trustedsec.com/wp-content/uploads/2023/03/CharlesPostGraphic.jpg)

## What is an SBOM?

A Software Bill of Materials (SBOM) is a hierarchical, itemized list of all dependencies, their version numbers and provenance for a given piece of software. It may also include other data, such as the license type or details about which database to query for vulnerability disclosure. SBOMs are not restricted to applications and can be created for many things, such as a Docker image, an operating system, or even hardware components.

## What is an SBOM Used For?

While highly dependent on your goals, SBOMs can have many uses. Having all the relevant data at hand can lead to faster outcomes during incident response, better policy decisions backed by facts, and a greater awareness of your software security at large. SBOMs are valuable during the entire lifetime of a security program and are in some cases pivotal in customer acquisition.

When should you begin collecting, creating, and using SBOMs? Now. Or right after you read through this blog. SBOMs are the sort of resource you want to invest in before you are impacted by an incident that they could help solve.

## How do SBOMs Look?

### Example SBOM Entry

Here is an example of what an entry may look like in practice:

```
{
  <strong>"id"</strong>: "6374b5ebf62f54ea",
  <strong>"name"</strong>: "@types/node",
  <strong>"version"</strong>: "17.0.21",
  <strong>"type"</strong>: "npm",
  <strong>"foundBy"</strong>: "javascript-package-cataloger",
  <strong>"locations"</strong>: [
    {
      <strong>"path"</strong>: "/usr/local/lib/python3.8/dist-packages/playwright/driver/package/node_modules/@types/node/package.json",
      <strong>"layerID"</strong>: "sha256:062e37f31d9f5b9bcdcdac59e1138ac60b2a4997aeb916f1d140f5b55c6c7144"
    }
  ],
  <strong>"licenses"</strong>: [
    "MIT"
  ],
  <strong>"language"</strong>: "javascript",
  <strong>"cpes"</strong>: [
    "cpe:2.3:a:\\@types\\/node:\\@types\\/node:17.0.21:*:*:*:*:*:*:*",
    "cpe:2.3:a:*:\\@types\\/node:17.0.21:*:*:*:*:*:*:*"
  ],
  <strong>"purl"</strong>: "pkg:npm/%40types/[email protected]",
  <strong>"metadataType"</strong>: "NpmPackageJsonMetadata",
  <strong>"metadata"</strong>: {
    <strong>"name"</strong>: "@types/node",
    <strong>"version"</strong>: "17.0.21",
    <strong>"author"</strong>: "",
    <strong>"licenses"</strong>: [
      "MIT"
    ],
    <strong>"homepage"</strong>: "https://github.com/DefinitelyTyped/DefinitelyTyped/tree/master/types/node",
    <strong>"description"</strong>: "",
    <strong>"url"</strong>: "https://github.com/DefinitelyTyped/DefinitelyTyped.git",
    <strong>"private"</strong>: <strong>false</strong>
  }
}
```

Here we can see that many aspects are recorded: the license, version number, package URL, and even where the package is installed.

This SBOM is in a format from the tool [***syft***](https://github.com/anchore/syft). Some other formats for SBOMs include CycloneDX and SPDX. You may find controversy online over which format to use, but having an SBOM in any format is better than not having one while trying to decide which is best for your usecase. (Also, ***syft*** can convert between formats.)

### Formats

#### CycloneDX

[CycloneDX](https://cyclonedx.org) was created by the [Open W...