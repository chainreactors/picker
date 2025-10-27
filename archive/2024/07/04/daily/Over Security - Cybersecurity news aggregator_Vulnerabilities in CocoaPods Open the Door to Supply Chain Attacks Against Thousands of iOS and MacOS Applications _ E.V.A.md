---
title: Vulnerabilities in CocoaPods Open the Door to Supply Chain Attacks Against Thousands of iOS and MacOS Applications | E.V.A
url: https://www.evasec.io/blog/eva-discovered-supply-chain-vulnerabities-in-cocoapods
source: Over Security - Cybersecurity news aggregator
date: 2024-07-04
fetch_date: 2025-10-06T17:45:41.614803
---

# Vulnerabilities in CocoaPods Open the Door to Supply Chain Attacks Against Thousands of iOS and MacOS Applications | E.V.A

[![](https://cdn.prod.website-files.com/6637ec84acdca762bbea2e39/6637ec84acdca762bbea2ea5_Asset%202.png)](/)

* [Home](/)
* [Services](/services)
* [Blog](/blog)
* [About us](/about-us)
* [Contact us](/contact-us)

Research

July 1, 2024

# Vulnerabilities in CocoaPods Open the Door to Supply Chain Attacks Against Thousands of iOS and MacOS Applications

Multiple vulnerabilities affecting the CocoaPods ecosystem, have been discovered, posing a major risk of supply chain attacks.

![](https://cdn.prod.website-files.com/6637ec84acdca762bbea2e55/667edfaf3163605ea44d1da0_portrait2.jpg)

![](https://cdn.prod.website-files.com/6637ec84acdca762bbea2e55/665519d6eeeaa979ade532b3_PHOTO-2024-05-28-01-38-28.jpg)

[Reef Spektor](https://www.linkedin.com/in/reef-spektor-02988418b)

[![](https://cdn.prod.website-files.com/6637ec84acdca762bbea2e39/6637ec84acdca762bbea2ea5_Asset%202.png)](/)

* [Home](/)
* [Services](/services)
* [Blog](/blog)
* [About us](/about-us)
* [Contact us](/contact-us)

,

[Eran Vaknin](https://www.linkedin.com/in/eran-vaknin)

[![](https://cdn.prod.website-files.com/6637ec84acdca762bbea2e39/6637ec84acdca762bbea2ea5_Asset%202.png)](/)

* [Home](/)
* [Services](/services)
* [Blog](/blog)
* [About us](/about-us)
* [Contact us](/contact-us)

,

X

minutes read

![](https://cdn.prod.website-files.com/6637ec84acdca762bbea2e39/6637ec84acdca762bbea2ee7_x.svg)![](https://cdn.prod.website-files.com/6637ec84acdca762bbea2e39/6637ec84acdca762bbea2ee8_linkedin.svg)![](https://cdn.prod.website-files.com/6637ec84acdca762bbea2e39/6637ec84acdca762bbea2ee9_reddit.svg)

![](https://cdn.prod.website-files.com/6637ec84acdca762bbea2e55/666ee5b3de77bc88bb5dc068_EVA_Infographics_Cover_A.jpg)

Contents

## TL;DR

* E.V.A Information Security researchers uncovered several vulnerabilities in the CocoaPods dependency manager that allows any malicious actor to claim ownership over thousands of unclaimed pods and insert malicious code into many of the most popular iOS and MacOSÂ applications. These vulnerabilities have since been patched.
* Such an attack on theÂ mobile app ecosystem could infect almost every Apple device, leaving thousands of organizations vulnerable to catastrophic financial and reputational damage. One of the vulnerabilities could also enable zero day attacks against the most advanced and secure organizationsâ infrastructure.Â Â
* Developers and DevOps teams that have used CocoaPods in recent years should verify the integrity of open source dependencies used in their application code.
* Dependency managers are an often-overlooked aspect of software supply chain security. Security leaders should explore ways to increase governance and oversight over the use these tools.

## Spilling the CocoaBeans

Open source code is ubiquitous in modern software development. When reviewing client code, itâs not unusual for us to find that 70-80% is composed of open source libraries, packages, or frameworks. While adoption of open source is practically inevitable, it also increases the risk of software supply chain attacks. Once an open source package is integrated into a company's continuous integration and continuous delivery (CI/CD) pipeline, there is a risk that the package could be compromised or manipulated to inject malicious code or vulnerabilities into any applications built using that pipeline. In recent years, many such attacks have occurred ([Log4Shell](https://en.wikipedia.org/wiki/Log4Shell) is probably the most famous example).

With about 100,000 libraries used in over 3 million mobile apps, [CocoaPods](https://cocoapods.org/) is an open source dependency manager for Swift and Objective-C projects. Dependency managers such as CocoaPods and others (including NPM, Maven, and PyPI) play a critical role in open source software supply chains. By checksumming and cryptographically signing packages, they allow developers to verify the integrity and authenticity of the components theyâre using. However, compromise of the dependency manager itself poses a severe threat. Attackers who infiltrate the servers or developer accounts of these tools could push malicious updates that spread widely.Â

As part of a red team exercise for a customer, we have discovered several critical vulnerabilities in the mechanisms used to manage packages and verify their owners on the CocoaPods server.

## Vulnerabilities in the CocoaPods Ecosystem

* A 2014 migration process left thousands of orphaned packages (where the original owner is unknown), many of which are still widely used in other libraries. Using a public API and an email address that was available in the CocoaPods source code, an attacker could claim ownership over any of these packages, which would then allow the attacker to replace the original source code with their own malicious code.
* An insecure email verification workflow could be exploited to run arbitrary code on the CocoaPods âTrunkâ server (manages the distribution and metadata of Â [Podspecs](https://guides.cocoapods.org/syntax/podspec.html)), which would allow an attacker to manipulate or replace the packages being downloaded.Â
* By spoofing an HTTP header and taking advantage of misconfigured email security tools, attackers could execute a zero-click attack that grants them access to a developerâs account verification token. This would allow attackers to change packages on the CocoaPods server and result in supply chain and zero day attacks.Â
* A separate vulnerability would allow an attacker to infiltrate the CocoaPods âTrunkâ server and perform a near-unlimited range of exploits..Â

## Who is Vulnerable

The short answer is that a significant percentage of the Swift and Objective-C application ecosystem (including iOS, macOS, and other Apple device software) was susceptible to supply chain and zero-click attacks, with an estimated range of thousands to millions of apps.

As with many software supply chain attacks, opaque dependencies in closed-source code mean it is almost impossible to understand the potential harm. The vulnerabilities we discovered could be used to control the dependency manager itself, and any published package.
[Downstream dependencies](https://en.wikipedia.org/wiki/Downstream_%28software_development%29) could mean that thousands of applications and millions of devices were exposed over the last few years.Â

Special attention needs to be paid to **software that relies on orphaned CocoaPod packages** (i.e., which do not have an owner assigned to them - more on this below).Â

<figure class="w-richtext-align-fullwidth w-richtext-figure-type-image"><div><img src="https://eva-research.imgix.net/EVA\_Infographics\_gif1.gif" loading="lazy" alt="" class="medium-zoom-image"></div></figure>

## The Potential Impact

CocoaPods is the most popular choice among iOS developers. Many of the potentially impacted artifacts are dependencies for projects maintained by major companies such as Google, GitHub, Amazon, Dropbox, and more - which puts the projects and downstream dependencies at risk.

These potential affected end-user apps deployed on millions (billions?)Â of devices could damage users and companies reputations. Many applications can access a userâs most sensitive information: credit card details, medical records, private materials, and more. Injecting code into these applications could enable attackers to access this information for almost any malicious purpose imaginable - ransomware, fraud, blackmail, corporate espionageâ¦ In the process, it could expose companies to major legal liabilities and reputational risk.

## Actions Developers Should Take

Developers and organizations are advised to review dependency lists and package managers used in their applications, validate checksums of third-party libraries, perform periodic scans to detect malicious code or suspicious changes, keep software updated and limit use of orphaned or unmaintained packages.

If CocoaPods was in use in your organization before October 2023, y...