---
title: New government directives and persistent threats reinforce urgency of securing software
url: https://buaq.net/go-132591.html
source: unSafe.sh - 不安全
date: 2022-10-26
fetch_date: 2025-10-03T20:52:34.001168
---

# New government directives and persistent threats reinforce urgency of securing software

* [unSafe.sh - 不安全](https://unsafe.sh)
* [我的收藏](/user/collects)
* [今日热榜](/?hot=true)
* [公众号文章](/?gzh=true)
* [导航](/nav/index)
* [Github CVE](/cve)
* [Github Tools](/tools)
* [编码/解码](/encode)
* [文件传输](/share/index)
* [Twitter Bot](https://twitter.com/buaqbot)
* [Telegram Bot](https://t.me/aqinfo)
* [Search](/search/search)

[Rss](/rss.xml)

[ ]
黑夜模式

![](https://8aqnet.cdn.bcebos.com/6e7143e85e819e21234ae3c1410b127b.jpg)

New government directives and persistent threats reinforce urgency of securing software

Get a handle on essential software development best practices to achieve compliance and risk reduc
*2022-10-25 21:30:12
Author: [www.synopsys.com(查看原文)](/jump-132591.htm)
阅读量:20
收藏*

---

*Get a handle on essential software development best practices to achieve compliance and risk reduction before directives take effect.*

*By: David London, managing director, The Chertoff Group, and Jamie Boote, associate principal security consultant at Synopsys.*

![Synopsys and The Chertoff Group](https://images-cdn.welcomesoftware.com/Zz1lNjUzMjRiNDUzZDIxMWVkYmIxYzVlYjRmODBiMWQwNw==?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOlsiZTY1MzI0YjQ1M2QyMTFlZGJiMWM1ZWI0ZjgwYjFkMDciXSwiZXhwIjoxNjY2NjU4MzUyfQ.YZyH2rsxnpybpMgRXocZHyWQLZRHjEbRZH9PFeIPHrc)

More than a year after President Biden signed Executive Order (EO) 14028 on Improving the Nation’s Cybersecurity, standards and compliance expectations are coming into sharper focus.

The National Institute of Standards and Technology (NIST), the Office of Budget and Management (OMB), and other U.S. government bodies have released a series of best practice guidance and directives that will accelerate software supply chain visibility and security. While the standards are directed at federal departments and contractors, it is expected that they will also have broader implications on critical infrastructure sectors.

In addition, persistent threat activity and events serve as a reminder for software security vigilance.

* Lapsus$, a Latin American–based hacker group, breached leading technology vendors Samsung and NVIDIA, exposing source code, product schematics, as well as code-signing certificates. Threat actors can use this information to plan future attacks.
* Widespread exploitation of the [Apache Log4J](https://www.synopsys.com/blogs/software-security/mitigating-impact-of-log4j-log4shell/) vulnerability enabled remote code execution. The software library is broadly used in consumer and enterprise services, and the vulnerability reinforced the risk of open source code use without adequate software supply chain visibility.
* While not a security incident, Peter Zaitko’s Twitter whistleblower complaint underscores the security risks of inadequate [software development life cycle (SDLC)](https://www.synopsys.com/blogs/software-security/secure-sdlc/) security and access permission sprawl. The complaint detailed uneven implementation of [secure coding practices](https://www.synopsys.com/glossary/what-is-code-review.html) and an absence of privileged access management in the Twitter production environment.

## EO 14028: Raising the software security bar for federal vendors and beyond

The executive order addresses a range of cybersecurity expectations including breach notification, zero trust, and enhanced network visibility, but software supply chain security emerges as an overwhelming priority. Key directives include developing new software security standards and best practices, maturing the [software Bill of Materials](https://www.synopsys.com/blogs/software-security/software-bill-of-materials-bom/) (SBOM), formalizing software code testing expectations, and developing standards for Internet of Things (IoT) cybersecurity. Several agencies have generated guidance and directives to satisfy EO expectations.

* NIST’s [Definition of Critical Software](https://www.nist.gov/itl/executive-order-improving-nations-cybersecurity/critical-software-definition) establishes criteria and attributes for software deemed critical and [security measures for “EO-critical software” use](https://www.nist.gov/itl/executive-order-improving-nations-cybersecurity/security-measures-eo-critical-software-use-2)
* NIST Guidelines on [Minimum Standards for Developer Verification of Software](https://www.nist.gov/publications/guidelines-minimum-standards-developer-verification-software) establishes key testing and validation measures
* The Department of Commerce’s [Minimum Elements for an SBOM](https://www.ntia.doc.gov/files/ntia/publications/sbom_minimum_elements_report.pdf)

Most recently, and relevant to the implementation of the EO’s principles, OMB issued two memos that will drive adoption of NIST’s Secure Software Development Framework (SSDF). In March, OMB directed U.S. government agencies to adopt the NIST SSDF for any vendors supplying software products, thus formalizing the framework as the authoritative reference for best practices and compliance. Last month, the agency released a memo on [enhancing the security of the software supply chain through secure software development practices](https://www.whitehouse.gov/wp-content/uploads/2022/09/M-22-18.pdf). In the memo, OMB articulates the steps required for U.S. government vendors to implement EO guidelines including attestation of secure software development practices and tasks. While the memo leans into self-attestation leveraging a yet-to-be defined standardized form, it also indicates that self-attestation is the minimum level required. Based on software criticality, agencies may make risk-based determinations that would necessitate a third-party assessment. Given this ambiguity, U.S. government vendors should consider steps for both self-attestation and potential third-party support.

## The four core principles of the SSDF

The NIST SSDF ([SP 800-218](https://csrc.nist.gov/publications/detail/sp/800-218/final)) serves as the focal point for capturing and operationalizing U.S. government software security expectations. In February, SP 800-218 replaced the original 2020 NIST cybersecurity white paper, formalizing the SSDF as the government’s seminal software security organizing construct. The document describes a set of foundational practices for secure software development and is organized into four core principles.

* **Prepare the organization:** People, process, and technology should be adequately prepared to perform and sustain [secure software development](https://www.synopsys.com/software-integrity/code-sight.html).
* **Protect the software:** Organizations should protect all components of their software from tampering and unauthorized access.
* **Produce well-secured software:** Organizations should produce well-secured software with minimal vulnerabilities.
* **Respond to vulnerabilities:** Organizations should identify vulnerabilities and respond appropriately.

Within each principle are a set of corresponding practices, tasks, and implementation examples. In addition, the SSDF aligns to previously published best practice frameworks (e.g., [BSIMM](https://www.bsimm.com/), [OWASP](https://www.synopsys.com/glossary/what-is-owasp-top-10.html), etc.) in a references section, thus acknowledging the good work that’s already been achieved in this area.

The SSDF also provides a common language and a set of high-level practices, similar to the approach taken by the NIST Cybersecurity Framework. But the flexibility and opportunity for user customization in the SSDF could lead to interpretation challenges and ambiguity. For example, the SSDF illustrates a set of “notional implementation examples” that can satisfy each defined task, but this list is not exhaustive and can be open to interpretation. As an organizing framework, that flexibility is welcome but as a compliance regime, it could create interpretation and attestation challenges.

## New guidance helps practitioners align to SSDF

To help firms achieve compliance with the requirements laid out in the executive order, the ...