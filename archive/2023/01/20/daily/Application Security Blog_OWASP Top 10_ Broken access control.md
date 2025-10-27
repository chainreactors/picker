---
title: OWASP Top 10: Broken access control
url: https://www.synopsys.com/blogs/software-security/owasp-top-10-broken-access-control/
source: Application Security Blog
date: 2023-01-20
fetch_date: 2025-10-04T04:22:18.377825
---

# OWASP Top 10: Broken access control

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

# OWASP Top 10: Broken access control

[![Black Duck Cybersecurity Research Center](/content/dam/black-duck/blogs/application-security/authors/CYRC.jpg)](/blog/authors/cyrc.html)

Authored by [Cybersecurity Research Center](/blog/authors/cyrc.html)

Jan 19, 2023
/
1 min read

## Subscribe

![play button](/content/dam/black-duck/play-button-arrow-sm.svg)

![](data:image/png;base64...)

×

##

Access control ensures that people can only gain access to things they’re supposed to have access to. When access control is broken, an attacker can obtain unauthorized access to information or systems that can put an organization at risk of a data breach or system compromise.

In 2021, the OWASP Top 10 list moved broken access control from the fifth position to first on the list of top vulnerabilities in web applications. According to OWASP, [94% of applications](https://owasp.org/Top10/A01_2021-Broken_Access_Control/) were found to have some form of broken access control, with the average incidence rate of 3.81%.

In this [video](https://youtu.be/vfCbnqNZ4Xg), Jonathan Knudsen, head of global research at the Cybersecurity Research Center, shows an example of broken access control in an insecure bank application. This example uses a classic vulnerability, insecure direct object reference. You can check out the source code [here](https://github.com/xenserverarmy/insecure-bank).

##

[Learn more abut the OWASP Top 10](/glossary/what-is-owasp-top-10.html)

* [CyRC](/blog/category.cyrc.html "CyRC")
* [Build Security into DevOps](/blog/category.build-secure-software.html "Build Security into DevOps")

## Continue Reading

[![Contextualizing risk in the AI era](https://www.blackduck.com/content/dam/black-duck/blogs/thumbnails/blackduck-logo-thumbnail.png)](/blog/mitigating-ai-risks-in-software-development.html "Contextualizing risk in the AI era")

#### [Contextualizing risk in the AI era](/blog/mitigating-ai-risks-in-software-development.html)

![Natasha Gupta](/content/dam/black-duck/blogs/application-security/authors/Natasha-Gupta.jpg)

By
[Natasha Gupta](/blog/authors/natasha-gupta.html)

Sep 05, 2025
/

5 min read

Tags:
[Artificial Intelligence](/blog/category.artificial-intelligence.html),
[Build Security into DevOps](/blog/category.build-secure-software.html),
[AppSec Best ...