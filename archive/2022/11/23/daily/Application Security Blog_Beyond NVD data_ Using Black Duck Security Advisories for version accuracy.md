---
title: Beyond NVD data: Using Black Duck Security Advisories for version accuracy
url: https://www.synopsys.com/blogs/software-security/comparing-bdsa-with-nvd-version-accuracy/
source: Application Security Blog
date: 2022-11-23
fetch_date: 2025-10-03T23:29:34.282767
---

# Beyond NVD data: Using Black Duck Security Advisories for version accuracy

[![Black Duck Home Page](https://www.blackduck.com/content/dam/black-duck/en-us/images/BlackDuckLogo-OnDark.svg)](/)

[![Black Duck Home Page](https://www.blackduck.com/content/dam/black-duck/en-us/images/BlackDuckLogo-OnDark.svg)](/)
[True Scale Application Security](/)

* [Support](https://community.blackduck.com)

* English
* 日本語
* 简体中文

close search bar

Sorry, not available in this language yet

close language selection

* English
* 日本語
* 简体中文

* Solutions
* Products & Services
* [Partners](/partners.html)
* Resources
* [Blog](/blog.html)
* Company
* [Contact Sales](/contact-sales.html)

Company

go back
Go Back

## [About Black Duck](/company.html)

* [Leadership* [Newsroom](https://news.blackduck.com)
  * [Blog](/blog.html)
  * [Partners](/partners.html)
  * [Careers](/company/careers.html)
  * [Contact Sales](/contact-sales.html)](/company/leadership.html)

![Gartner Magic Quadrant](https://www.blackduck.com/content/dam/black-duck/en-us/images/Gartner_Magic_Quadrant_AST_2023-final-bg.svg)

2023 Gartner® Magic Quadrant™ for AppSec Testing
[Read more](/resources/analyst-reports/gartner-magic-quadrant-appsec.html)

![Forrester Wave Leader 2023 Software Analysis](https://www.blackduck.com/content/dam/black-duck/en-us/images/forrester-wave-sca-smallNav.jpg)

Forrester Wave Leader for SCA
[Read more](/resources/analyst-reports/forrester-wave-software-composition-analysis.html)

close sub navigation

Products

go back
Go Back

## Integrated SaaS Platform

* [Polaris Platform](/platform.html)
* [fAST Static](/platform.html#A)
* [fAST SCA](/platform.html#A)
* [fAST Dynamic](/platform.html#A)

## Tools

* [Coverity Static](/static-analysis-tools-sast/coverity.html)
* [Black Duck SCA](/software-composition-analysis-tools/black-duck-sca.html)
* [Continuous Dynamic](/dast/continuous-dynamic.html)
* [Seeker Interactive](/interactive-application-security-testing.html)
* [Software Risk Manager ASPM](/software-risk-manager.html)
* [Defensics Protocol Fuzzing](/fuzz-testing.html)

## [Integrations](/integrations.html)

* [Code Sight IDE Plug-in](/code-sight.html)
* [SCM Integrations](/integrations.html#scm)
* [Build & CI Tool Integrations](/integrations.html#build-ci)
* [Developer Workflow Integrations](/integrations.html#workflow)
* [3rd-Party AST Tool Integrations](/integrations.html#security)
* [Cloud Deployment Integrations](/integrations.html#cloud)

## Services

* [Program Strategy & Planning](/services/security-program.html)
* [Open Source & Security Audits](/services/open-source-software-audit.html)
* [Implementation & Deployment](/customer-success/implementation.html)
* [Customer Success & Support](/customer-success.html)

close sub navigation

Solutions

go back
Go Back

## Use Cases

* [AI-generated code](/solutions/artificial-intelligence-software-development.html)
* [API Security Testing](/solutions/api-security-testing.html)
* [AppSec Program Consolidation](/solutions/appsec-consolidation.html)
* [Application Security Testing](/solutions/application-security-testing.html)
* [DevSecOps](/solutions/devsecops.html)
* [EU Cyber Resilience Act Compliance](/solutions/eu-cyber-resilience-act-compliance.html)
* [Software Supply Chain Security](/solutions/software-supply-chain-security.html)
* [Manage Enterprise AppSec Risk](/solutions/enterprise-application-security-risk-management.html)
* [Container Security](/solutions/container-security.html)
* [Open Source License Compliance](/solutions/open-source-security.html)
* [M&A Due Diligence](/solutions/mergers-and-acquisitions.html)
* [Quality and Security Standards Compliance](/solutions/compliance.html)

## By Technology

* [Static Analysis (SAST)](/static-analysis-tools-sast.html)
* [Software Composition Analysis (SCA)](/software-composition-analysis-tools.html)
* [Dynamic Analysis (DAST)](/dast.html)
* [Interactive Analysis (IAST)](/interactive-application-security-testing.html)
* [Application Security Posture Management (ASPM)](/software-risk-manager.html)
* [Fuzz Testing Solutions](/fuzz-testing.html)

## By Industry

* [Automotive](/solutions/automotive.html)
* [Financial Services](/solutions/financial-services.html)
* [IoT & Embedded](/solutions/iot-embedded.html)
* [Medical Devices](/solutions/healthcare.html)
* [Public Sector](/solutions/government.html)

## By Role

* [Dev and DevOps Teams](/solutions/dev-devops.html)
* [Security Teams](/solutions/security-teams.html)
* [Legal Teams](/solutions/legal-teams.html)

close sub navigation

Resources

go back
Go Back

## Latest Updates

* [Newsroom](https://news.blackduck.com)
* [Blog](/blog.html)
* [Cybersecurity Research Center](/resources/cybersecurity-research-center.html)

## Customer Resources

* [Support](https://community.blackduck.com)
* [Documentation](https://documentation.blackduck.com)
* [Black Duck Academy](https://blackduck.skilljar.com)
* [Search Knowledge Base](https://community.blackduck.com/s/global-search/%40uri)
* [Community Q&A](https://community.blackduck.com/s/synopsys-product-directory)

## Other Resources

* [Datasheets](/resources/datasheets.html)
* [eBooks](/resources/ebooks.html)
* [Case Studies](/resources/case-studies.html)
* [Research & Reports](/resources/analyst-reports.html)
* [Webinars](/resources/webinars.html)
* [White Papers](/resources/white-papers.html)
* [AppSec Glossary](/glossary.html)
* [Resource Library](/resources.html)

[![Gartner Magic Quadrant](https://www.blackduck.com/content/dam/black-duck/en-us/images/Gartner_Magic_Quadrant_AST_2023-final-bg.svg)

2023 Gartner® Magic Quadrant™ for AppSec Testing
See why Black Duck is a Leader](/resources/analyst-reports/gartner-magic-quadrant-appsec.html)

close sub navigation

* [Blog Home](/blog.html)

# Beyond NVD data: Using Black Duck Security Advisories for version accuracy

[![Editorial Team](/content/dam/black-duck/en-us/BlackDuckIcon.svg)](/blog/authors/black-duck-editorial-team.html)

Authored by [Black Duck Editorial Staff](/blog/authors/black-duck-editorial-team.html)

Nov 21, 2022
/
5 min read

Table of Contents

* How BDSAs provide more-accurate vulnerable ranges
* Accurate detection is key
* False positives

## Subscribe

##

*Black Duck Security Advisories provide more-accurate information on vulnerable software version ranges to help customers get more out of NVD data.*

*\*\*Disclaimer\*\* The information contained within this blog post was accurate at the time of writing.*

The National Vulnerability Database (NVD) is considered the go-to source for accurate information on vulnerability management data, including vulnerable open source software versions. But is it the most accurate and thorough source?

The full range of vulnerable software versions is considered the most important and useful vulnerability data—it’s vital for determining whether a given piece of software is within the range of versions affected by a vulnerability. There is no room for error when identifying vulnerable ranges. Inaccuracies can lead to false alarms, or worse, the release of misleading information that software is fixed or safe when in fact it is vulnerable.

But the vulnerable ranges that the NVD identifies are often too short or too long, meaning that vulnerable versions may be missed, or a fixed version may be included. [Black Duck® Security Advisories](/blog/black-duck-security-advisories-benefits.html) (BDSAs), created by the Black Duck [Cybersecurity Research Center](/resources/cybersecurity-research-center.html) (CyRC), address this issue by performing thorough research from public sources and tracing vulnerable code within source repositories. These techniques enable the CyRC to discover more-precise vulnerable version ranges and produce BDSAs with more accurate and secure information to customers.

## How BDSAs provide more-accurate vulnerable ranges

A BDSA is a handcrafted report delivering detailed and concise open source vulnerability information to customers, tailored to their [software Bill of Materials](/blog/software-bill-of-materials-bom.html).

E...