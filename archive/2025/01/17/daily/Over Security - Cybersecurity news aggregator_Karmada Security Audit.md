---
title: Karmada Security Audit
url: https://www.shielder.com/blog/2025/01/karmada-security-audit/
source: Over Security - Cybersecurity news aggregator
date: 2025-01-17
fetch_date: 2025-10-06T20:12:26.688408
---

# Karmada Security Audit

[![shielder logo homepage](https://www.shielder.com/img/logoshielder.svg)](https://www.shielder.com/ "homepage")

* [Home](https://www.shielder.com/ "Home")
* [Company](https://www.shielder.com/company "Company")
* [Services](https://www.shielder.com/services "Services")
* [Advisories](https://www.shielder.com/advisories "Advisories")
* [Blog](https://www.shielder.com/blog "Blog")
* [Careers](https://www.shielder.com/careers "Careers")
* [Contacts](https://www.shielder.com/contacts "Contacts")
* ENG

  [ENG](https://www.shielder.com/blog/2025/01/karmada-security-audit/ "ENG")
  [ITA](https://www.shielder.com/it/blog/2025/01/karmada-security-audit/ "ITA")

# Karmada Security Audit

## TL;DR

Shielder, together with [OSTIF](https://ostif.org/) and [CNCF](https://cncf.io/), performed a Security Audit on the [Karmada](https://karmada.io/) project.

The audit resulted in six (6) findings ranging from high to informational severity. Most of them have been addressed by the Karmada core team, while two of them are marked for a future iteration.

**Today, we are publishing the [full report](https://github.com/ShielderSec/public-reports/blob/main/2025/%5BOSTIF%5D%20Karmada%20-%20Report%20v1.1.pdf) in our [dedicated repository](https://github.com/ShielderSec/public-reports/)**.

## Introduction

In September 2024, Shielder was hired to perform a Security Audit of [Karmada](https://karmada.io/), an open, multi-cloud, multi-cluster Kubernetes orchestration and management system. The audit has been sponsored by the [CNCF](https://cncf.io/) and facilitated by the [Open Source Technology Improvement Fund (OSTIF)](https://ostif.org/).

Karmada aims to provide a unified control plane for multi-cluster applications. To do so, it extends the Kubernetes API to support management of resources across multiple clusters, exposing a single interface (the Karmada API) for operations. It is mainly written in Go.

The Karmada source code is available at <https://github.com/karmada-io/karmada>, and the website provides documentation of the project at <https://karmada.io/docs/>.

## Context and Scope

The aim of the audit was to assess the overall security posture of Karmada, from its design to its implementation, also including the documentation and provided examples.

For the assessment, the Shielder team has modeled the following attackers:

* Unauthenticated attacker: an attacker with no access to valid credentials to authenticate against neither the Karmada control plane nor its member clusters.
* Compromised cluster: an attacker that has compromised one of the member clusters, with the goal to move horizontally or vertically in the federation.
* Malicious operator: an attacker that owns valid credentials for either the control plane or one of the member clusters.

In this context, the goals were to assess if the Karmada project:

* Designs its multi-cluster federation in a way that does not introduce paths for vertical or horizontal movements between clusters.
* Correctly implements Golang *security by design* principles when handling user-controlled input.
* Employs the correct segregation/sandboxing mechanisms for network or local resources.
* Provides documentation that can be followed by users of the tool without introducing insecure defaults or additional risks in their Kubernetes federation.

The scope of this audit is the Karmada version **v.1.11.0** released on August 31, 2024.

## Findings Summary and Recommendations

The overall security posture of the Karmada project is mature from a code point-of-view.

The project correctly re-uses battle-tested and standard APIs from the Kubernetes project, and mostly follows best practices in terms of security.
The Shielder team was able to identify 1 (one) high, 1 (one) medium, 2 (two) low findings plus 2 (two) informational issues.

| ID | Vulnerability | Severity | Status |
| --- | --- | --- | --- |
| 1 | Insecure Design of Pull Mode | High | Closed |
| 2 | Multiple TarSlips in CRDs Archive Extraction | Medium | Closed |
| 3 | Insecure Default Configuration | Low | Closed |
| 4 | Bootstrap Token Leaked in Command Output | Informational | Closed |
| 5 | Denial of Service (DoS) in LuaVM Package | Low | Open1 |
| 6 | K8s Pods Executed with Unnecessary Privileges | Informational | Open2 |

> 1 The issue is caused by a third-party dependency ([gopher-lua](https://github.com/yuin/gopher-lua)). The maintainer has been contacted, and the issue will be fixed in a future iteration.
> 2 The issue does not have a direct security impact, but it is a good practice to harden the security configuration of containers. It will be fixed in a future iteration.

If you are a developer or cloud engineer using Karmada, the recommendation is to, whenever possible, update it to the latest release or to prefer the Push Mode of deployment to make sure that member clusters are not capable of directly contacting the Karmada control plane.

**The full details can be read in the [report](https://github.com/ShielderSec/public-reports/blob/main/2025/%5BOSTIF%5D%20Karmada%20-%20Report%20v1.1.pdf).**

## Conclusions

When assessing libraries, frameworks or more in general tools that are by-design highly flexible and customizable, it is crucial to perform effective threat modeling to understand where the most interesting attack surfaces lie.

In the context of multi-cloud, multi-cluster environments, it is important to assume that one of the clusters might be compromised (or operated by a malicious actor), and to design the system in a way that is resilient to that.

For Karmada, the main threats identified were caused by an insecure design of the Pull Mode, which allowed a member cluster to compromise other clusters in the federation, by a lack of input sanitization in the CRD archive extraction, and a DoS when custom Lua scripts are passed to the control plane, which might be used to stall or crash the control plane.

We would like to thank the Karmada core maintainers and community - notably *Kevin Wang*, *Hongcain Ren* and *Zhuang Zhang* - for being extremely collaborative in triaging and addressing the findings.

It was a pleasure for our team to work with OSTIF, the CNCF, and the Karmada core team.

## Pitch ð£

Did you know [OSTIF](https://ostif.org/) helps sensitive open-source projects in securing funds to perform security audits? They will also help you in scoping the assessment, finding a trusted partner to perform the analysis, and ensuring full transparency along the way.

P.S. if you need help in threat modeling and auditing your kubernetes-powered projects –> [get in touch with us!](https://www.shielder.com/contacts/)

3
min

Date

16 January 2025

[CVE](/tags/cve "CVE")
[OSTIF](/tags/ostif "OSTIF")
[Public Report](/tags/public-report "Public Report")

Author

[suidpit](/authors/suidpit "suidpit")

Security Researcher and Penetration Tester at Shielder.
Human, Chaotic Good. Disciple of Bushido & Disney.

Previous post

[A Journey From `sudo iptables` To Local Privilege Escalation](https://www.shielder.com/blog/2024/09/a-journey-from-sudo-iptables-to-local-privilege-escalation/ "A Journey From `sudo iptables` To Local Privilege Escalation")

Next post

[MaterialX and OpenEXR Security Audit](https://www.shielder.com/blog/2025/07/materialx-and-openexr-security-audit/ "MaterialX and OpenEXR Security Audit")

Info

Shielder S.p.A.

P.I. 11435310013

REA TO - 1213132

Registered Capital: 81.000,00 â¬

[Via
Palestro, 1/C
10064 Pinerolo (TO) Italy](https://www.google.it/maps/place/Shielder/%4044.8833849%2C7.3303863%2C17z/data%3D%213m1%214b1%214m5%213m4%211s0x4788250440849fa5%3A0x74cf10f2092abc85%218m2%213d44.8833849%214d7.332575 "corporate headquarters")

![ISO27001](/img/iso27001.png)

![ISO9001](/img/iso9001.png)

Contacts

info@shielder.com

Landline:
(+39) 0121 - 39 36 42

Commercial:
(+39) 345 - 57 18 634

Technical:
(+39) 393 - 16 66 814

Sitemap

[Home](https://www.shielder.com/ "Home")

[Company](https://www.shielder.com/company "Company")...