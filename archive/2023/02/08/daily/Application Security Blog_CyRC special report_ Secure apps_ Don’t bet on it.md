---
title: CyRC special report: Secure apps? Don’t bet on it
url: https://www.synopsys.com/blogs/software-security/cyrc-special-report-gaming-apps-security-analysis/
source: Application Security Blog
date: 2023-02-08
fetch_date: 2025-10-04T05:59:04.162705
---

# CyRC special report: Secure apps? Don’t bet on it

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

# CyRC special report: Secure apps? Don’t bet on it

[![Jonathan Knudsen](/content/dam/black-duck/blogs/application-security/authors/Johnathan-Knudsen.jpg)](/blog/authors/johnathan-knudsen.html)

Authored by [Jonathan Knudsen](/blog/authors/johnathan-knudsen.html)

Feb 06, 2023
/
11 min read

Table of Contents

* Executive summary
* How software is made
* A doughnut hole inside a doughnut hole
* About Black Duck Binary Analysis (BDBA)
* Method
* Components and vulnerabilities
* App permissions
* App A: So close and yet so far
* App B: Another sad story of transitive dependencies
* App C: This is what happens when you do not try
* App D: Leaving stuff inside the patient
* App E: Next to godliness
* What does it all mean?

## Subscribe

##

With the Super Bowl approaching in the U.S., the Black Duck Cybersecurity Research Center (CyRC) set out to evaluate the 10 most popular Android sports and betting apps through the lens of supply chain security. We used [Black Duck® Binary Analysis](/software-composition-analysis-tools/binary-analysis.html) (BDBA) to examine the open source components used in these apps.

## Executive summary

In aggregate, the 10 apps analyzed have over 21.5 million downloads from the Google Play Store. For perspective, these apps have been downloaded by as many people as the population of metropolitan São Paulo.

* Average number of components per app: 125
* Average number of vulnerable components per app: 10
* Average number of vulnerabilities per app: 179

Despite evidence of active development, many of the apps we analyzed use outdated open source components with their associated known vulnerabilities. In the software world, two or three years is a long time; in the apps we analyzed, we found open source components dating back to 2010.

Known vulnerabilities in open source components are not necessarily exposed in the app. However, risk increases with the age of the components and the number of known vulnerabilities. Furthermore, outdated components are an indication that development teams are not managing their open source dependencies, which could be an indication that they are not handling security well in general.

The sports and betting apps we analyzed scored significantly worse than the average numbers we encountered in our 2021 repor...