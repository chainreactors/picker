---
title: Understand the Reality of the SOC 2 Checkbox
url: https://zeltser.com/soc2-checkbox-reality/
source: Lenny Zeltser
date: 2026-03-17
fetch_date: 2026-03-18T04:22:43.616296
---

# Understand the Reality of the SOC 2 Checkbox

[Lenny Zeltser](/)Security builder & leader

 [Projects](/projects) [Writing](/writing) [About](/about)

# Understand the Reality of the SOC 2 Checkbox

SOC 2 standardized security reporting, but it left the vendor in control of the system boundary and auditor selection. Understanding that structural gap helps vendors and buyers get the most value from the framework.

![Understand the Reality of the SOC 2 Checkbox - illustration](/assets/soc2-checkbox-reality.C5prU05O_Z2mpwqN.webp)

In 2010, I [wrote about](/cloud-security-beyond-sas-70) companies placing too much trust in providers’ SAS 70 reports. At the time, Gartner called the widespread misuse [“deceptive and harmful.”](/cloud-security-beyond-sas-70) Chris Schellman, who had led over 500 SAS 70 audits, [clarified](https://www.accountingtoday.com/news/gartner-report-on-sas-70-audits-creates-confusion) that the industry had been using it for something it was never built for. Turns out the AICPA was already [building a replacement](https://www.aicpa-cima.com/news/article/aicpa-auditing-standards-board-approves-revisions-to-attestation-standards); SOC 2 was born.

SOC 2 introduced prescribed trust criteria, required management accountability, and gave buyers a basis for risk-informed decisions. Fifteen years later, familiar patterns have resurfaced.

## SAS 70 wasn’t meant for security.

The AICPA [issued SAS 70](https://www.journalofaccountancy.com/issues/2010/aug/20103009/) in 1992 as a framework for auditors to report on controls at service organizations that could affect customers’ financial statements. Then [Sarbanes-Oxley](https://www.congress.gov/bill/107th-congress/house-bill/3763) arrived in 2002. Public companies needed their vendors to demonstrate control effectiveness, and SAS 70 [became the default](https://www.isaca.org/resources/isaca-journal/past-issues/2011/understanding-the-new-soc-reports).

Organizations began [requesting and marketing](https://www.cfo.com/news/the-truth-about-sas-70/669107/) SAS 70 reports for security assurance, well beyond the standard’s original design. SAS 70 [had no prescribed control criteria](https://www.datacenterknowledge.com/business/sas-70-ssae-16-soc-and-data-center-standards). The provider chose which controls to include, and the auditor evaluated only what the provider put forward.

By the late 2000s, the market had turned “SAS 70 certified” into marketing language for something that was neither a certification nor a security standard. The gap between what SAS 70 was and how the market used it had grown too wide to ignore.

## SOC 2 introduced the missing structure.

The AICPA [issued SSAE 16](https://www.aicpa-cima.com/resources/landing/system-and-organization-controls-soc-suite-of-services) in 2010 (superseded by [SSAE 18](https://www.aicpa-cima.com/resources/download/aicpa-statement-on-standards-for-attestation-engagements-no-18) in 2017), replacing SAS 70 with three distinct report types. SOC 2 addressed the security gap the market had tried to cover with SAS 70. SOC 1 continued financial controls reporting, and SOC 3 provided a public-facing summary of SOC 2.

Where SAS 70 let providers choose which controls to include, SOC 2 introduced the [Trust Services Criteria](https://cloudsecurityalliance.org/blog/2023/10/05/the-5-soc-2-trust-services-criteria-explained) for security, availability, processing integrity, confidentiality, and privacy. Unlike SAS 70, the new report [required a written management assertion](https://www.techtarget.com/searchsecurity/definition/SSAE-16), making organizations formally accountable for the report’s claims.

## SOC 2 became table stakes.

Enterprise buyers needed evidence of vendor security controls, and SOC 2 filled that gap as the cloud market grew. The framework’s adoption accelerated when compliance automation tools such as Vanta and Drata made it accessible to startups and smaller companies that previously couldn’t afford it.

Lower barriers changed what SOC 2 meant in practice. The report appeared in vendor questionnaires and RFPs as a checkbox, and for many companies the goal shifted from demonstrating a strong program to passing a binary check.

As a result, merely having a SOC 2 report no longer distinguishes a company. It’s the baseline expectation for SaaS providers selling to enterprises.

## SOC 2 concerns start to surface.

Broader adoption put more weight on SOC 2’s structural gaps. Despite the improvements over SAS 70, the audited organization still defines the system boundary and selects the auditor. These choices drive the concerns I hear from fellow CISOs:

* The [Trust Services Criteria](https://www.aicpa-cima.com/resources/download/2017-trust-services-criteria-with-revised-points-of-focus-2022) prescribe what to evaluate, but the provider decides which systems and services the report covers and how controls address each criterion. Organizations have an incentive to optimize for controls that produce favorable evidence.
* The rigor of examinations varies across auditors. Auditors who work quickly and keep clients satisfied win repeat business at the expense of examination rigor. As a result, promises of [“fast and easy” threaten SOC credibility](https://www.journalofaccountancy.com/issues/2026/feb/promises-of-fast-and-easy-threaten-soc-credibility/).

The AICPA has responded by [cataloging common examination deficiencies](https://www.aicpa-cima.com/resources/download/see-common-peer-review-deficiencies-from-soc-1-r-and-soc-2-r-engagements) and [requiring peer reviewers to examine firms’ SOC work](https://www.aicpa-cima.com/news/article/final-version-of-new-aicpa-peer-review-standards-update-now-available). However, I’m not aware of any firm that has faced disciplinary action for lax examinations.

## Use SOC 2 intentionally.

SOC 2 addressed real weaknesses in how the market used SAS 70, but the old pattern of treating reports as checkboxes persists.

SaaS companies have an incentive to draw scope boundaries that exclude their weakest processes and time observation windows to avoid known-bad periods. Controls might exist during the examination and atrophy once the report ships. These practices are the predictable result of letting the vendor define the scope and select the auditor.

Vendors that want their SOC 2 to carry weight should design controls around their actual product and threat model, not a default compliance template. And they should hold their auditors to high standards and avoid misrepresenting where the program actually stands.

From a buyer’s perspective, a SOC 2 report from a trusted audit firm offers visibility into a vendor’s security program. But due diligence requires not only reading control statements, but also asking which systems and processes were excluded from scope. If that boundary doesn’t match what you actually rely on, the assurance doesn’t either.

More on

[Risk Management](/topic/risk-management)[Leadership](/topic/leadership)

After 6+ years building the security program at [Axonius](https://www.axonius.com/) from startup to scale, I'm exploring what's next. As I work on independent projects, I'm open to CISO or security product leadership roles where technical depth enables business growth. To talk, reach out on [LinkedIn](https://www.linkedin.com/in/lennyzeltser/) or email me at *my first name* at *my last name* dot com.

4 min to read

March 17, 2026

### About the Author

Lenny Zeltser is a cybersecurity executive with deep technical roots, product management experience, and a business mindset. He has built security products and programs from early stage to enterprise scale. He is also a Faculty Fellow at SANS Institute and the creator of REMnux, a popular Linux toolkit for malware analysis. Lenny shares his perspectives on security leadership and technology at [zeltser.com](/).

[Learn more →](/about)

© 2026 Lenny Zeltser