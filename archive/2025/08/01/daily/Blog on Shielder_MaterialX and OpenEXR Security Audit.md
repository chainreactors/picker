---
title: MaterialX and OpenEXR Security Audit
url: https://www.shielder.com/blog/2025/07/materialx-and-openexr-security-audit/
source: Blog on Shielder
date: 2025-08-01
fetch_date: 2025-10-07T00:49:30.660621
---

# MaterialX and OpenEXR Security Audit

[![shielder logo homepage](https://www.shielder.com/img/logoshielder.svg)](https://www.shielder.com/ "homepage")

* [Home](https://www.shielder.com/ "Home")
* [Company](https://www.shielder.com/company "Company")
* [Services](https://www.shielder.com/services "Services")
* [Advisories](https://www.shielder.com/advisories "Advisories")
* [Blog](https://www.shielder.com/blog "Blog")
* [Careers](https://www.shielder.com/careers "Careers")
* [Contacts](https://www.shielder.com/contacts "Contacts")
* ENG

  [ENG](https://www.shielder.com/blog/2025/07/materialx-and-openexr-security-audit/ "ENG")
  [ITA](https://www.shielder.com/it/blog/2025/07/materialx-and-openexr-security-audit/ "ITA")

# MaterialX and OpenEXR Security Audit

## TL;DR

Shielder, together with [OSTIF](https://ostif.org/) and the [Academy Software Foundation (ASWF)](https://www.aswf.io), performed a Security Audit on the [MaterialX](https://materialx.org/) and [OpenEXR](https://openexr.com) projects.

The audit resulted in eleven (11) findings ranging from critical to informational severity. Most of them have been addressed by the project maintainers, but three of them - affecting MaterialX - are marked for a future iteration and are not disclosed in the public report yet.

**Today, we are publishing the reports of the audit in our [dedicated repository](https://github.com/ShielderSec/public-reports/)**.

## Introduction

In January 2025, Shielder was hired to perform a Security Audit of [MaterialX](https://materialx.org) and [OpenEXR](https://openexr.com), two projects of the [Academy Software Foundation](https://www.aswf.io/) developed for high-end visual effects, animation and digital content creation. The audit was facilitated by the [Open Source Technology Improvement Fund (OSTIF)](https://ostif.org/).

OpenEXR is an open-source image file format that supports a wide variety of features, such as multi-channel support, lossless and lossy compression and deep data. MaterialX is an open-source standard for defining material and shader in a way that is interoperable and provides consistent look and shading across different renderers and tools.

The OpenEXR source code is available at <https://github.com/AcademySoftwareFoundation/OpenEXR>, and the website provides documentation of the project at [https://openexr.com/en/latest/#](https://openexr.com/en/latest/).

The MaterialX source code is available at <https://github.com/AcademySoftwareFoundation/MaterialX>, and the website provides documentation of the project at <https://materialx.org/DeveloperReference.html>.

## Context and Scope

The aim of this *Preliminary Security Review and Threat Model Assessment* was to gain a general understanding of the attack surface and secure coding practices of the projects, to provide maintainers with valuable recommendations and starting points to gradually strengthen their security posture.

Specifically, the main goals were to:

* Perform a high-level (*bird’s-eye*) Threat Modeling to understand the most common use-cases and the features with the highest risk.
* Manually review the source code of the projects, looking for outstanding bugs and insecure coding practices.
* Perform automated source code analysis with SAST tools like Semgrep and CodeQL.
* Review the dependencies shipped to detect outdated and vulnerable dependencies.
* Review the use of CI and GitHub Workflows.
* Review the current state of fuzzing coverage, addressing potential issues with the fuzzers, and improving the coverage of critical codepaths.

Projects like OpenEXR and MaterialX are used across the industry in many different ways, by vendors with significantly different security requirements and threat models. For this reason, the Shielder team focused the majority of this audit on the risks related to the most generic and simple attack scenario, that is, a one-time parsing of an untrusted EXR or MTLX file.

For completeness, the team also explored risks connected to attacks against the supply chain, such as compromission of the GitHub repository, and risks connected to developer misusing the library, feeding untrusted input into APIs not meant to be used externally. Some attack scenarios would require the project to be used in a specific OS, e.g. Windows.

OpenEXR and MaterialX are both developed using memory unsafe language (C/C++). Due to this, most of the reported findings were discovered by fuzzing the libraries, collecting and performing RCA (Root Cause Analysis) on the crashes to establish impacts ranging from Denial Of Service (DoS) to leakage of information, or, in the worst case, Remote Code Execution (RCE).

This audit was performed on the commit with hash [`8bc3faebc66b92805f7309fa7a2f46a66e5cc5c9`](https://github.com/AcademySoftwareFoundation/openexr/commit/8bc3faebc66b92805f7309fa7a2f46a66e5cc5c9) (**January 1, 2025**) for OpenEXR and the commit tagged as [`v1.39.2-rc1`](https://github.com/AcademySoftwareFoundation/materialX/commits/v1.39.2-rc1) (**January 8, 2025**) for MaterialX.

## Findings Summary and Recommendations

The overall security posture of the MaterialX and OpenEXR projects is adequately mature for what concerns secure coding and design, but there’s still room for improvement when it comes to edge cases and untrusted input.

In the MaterialX project, the Shielder team was able to identify a total of 7 (seven) medium and low findings. *Three out of the seven issues discovered are still undisclosed, because they are still in the process of being addressed by the maintainers of the project. The complete list of findings will be included in a future report, once all the issues have been fixed and released.*

| ID | Vulnerability | Severity | Status |
| --- | --- | --- | --- |
| 1 | Lack of MTLX Import Depth Limit Leads to DoS (Denial-Of-Service) Via Stack Exhaustion | Low | Closed |
| 2 | Null Pointer Dereference in MaterialXCore Shader Generation Due to Unchecked implGraphOutput | Low | Closed |
| 3 | Null Pointer Dereference in getShaderNodes | Low | Closed |
| 4 | Stack Overflow via Lack of MTLX XML Parsing Recursion Limit | Low | Closed |

In the OpenEXR project, the Shielder team was able to identify 1 (one) critical, 1 (one) medium and 2 (two) low findings.

| ID | Vulnerability | Severity | Status |
| --- | --- | --- | --- |
| 1 | Heap-Based Buffer Overflow in Deep Scanline Parsing via Forged Unpacked Size | Critical | Closed |
| 2 | Out-Of-Memory via Unbounded File Header Values | Low | Closed |
| 3 | Out of Bounds Heap Read due to Bad Pointer Arithmetic in LossyDctDecoder\_execute | Medium | Closed |
| 4 | ScanLineProcess::run\_fill NULL Pointer Write in "reduceMemory" Mode | Low | Closed |

Moreover, the Shielder team developed a new grammar-based fuzzers for the [OpenEXR Simple Scanline file format](https://github.com/google/oss-fuzz/pull/13302/files).

If you are a developer using MaterialX or OpenEXR, the recommendation is to, whenever possible, update it to the latest release. Also, it is important to implement controls and fallbacks for events like crashes or memory exhaustion, so that applications using these libraries would not lose availability in case untrusted, malicious input is provided.

**The full details can be read in the following reports:**

* [OpenEXR report](https://github.com/ShielderSec/public-reports/blob/main/2025/%5BOSTIF%5D%20OpenEXR%20-%20Report%20v1.2.pdf)
* [MaterialX report](https://github.com/ShielderSec/public-reports/blob/main/2025/%5BOSTIF%5D%20MaterialX%20-%20Report%20v1.2.pdf)

## Conclusions

When assessing libraries and frameworks that are by-design highly flexible and customizable, it is crucial to perform effective threat modeling to understand where the most interesting attack surfaces lie.

Components that parse complex formats, such as images or similar data structures, have been proven over the years to be impacted by errors and vulnerabilities, especially when employing memory unsafe languages such as C/C++. This happens even with senior and exper...