---
title: Getting started with Detection-as-Code and Sekoia Platform
url: https://blog.sekoia.io/getting-started-with-detection-as-code-and-sekoia-platform/
source: Over Security - Cybersecurity news aggregator
date: 2024-10-05
fetch_date: 2025-10-06T18:53:55.175495
---

# Getting started with Detection-as-Code and Sekoia Platform

### Log in

Username or Email Address

Password

[ ]  Remember Me

 [Forgot password?](https://blog.sekoia.io/wp-login.php?action=lostpassword)

### Search the site...

Search for

* All categories
* [Threat Research & Intelligence](https://blog.sekoia.io/category/threat-research/)
* [Product News](https://blog.sekoia.io/category/product-news/)
* [SOC Insights & Other News](https://blog.sekoia.io/category/soc-insights-other-news/)
* [Detection Engineering](https://blog.sekoia.io/category/detection-engineering/)

####

Reset

[![logo sekoia.io blog light](https://t7f4e9n3.delivery.rocketcdn.me/wp-content/uploads/2023/03/cropped-logo-sekoia-io-blog-light.png)](https://blog.sekoia.io/)

* [Threat Research](https://blog.sekoia.io/category/threat-research/)
* [Detection](https://blog.sekoia.io/category/detection-engineering/)
* [Product News](https://blog.sekoia.io/category/product-news/)
* [Other](https://blog.sekoia.io/category/soc-insights-other-news/)
* [Sign up](https://go.sekoia.io/Preference-center-EN.html)
* [About Sekoia.io](https://www.sekoia.io/en/about/)
  + [TDR Team](https://www.sekoia.io/en/about-threat-detection-research-team/)
  + [AI-SOC platform](https://www.sekoia.io/en/homepage/)
  + [Interactive demo](https://sekoia.storylane.io/share/8zdjfok9atpn)
  + [Contact Us](https://www.sekoia.io/en/contact/)

* [Threat Research](https://blog.sekoia.io/category/threat-research/)
* [Detection](https://blog.sekoia.io/category/detection-engineering/)
* [Product News](https://blog.sekoia.io/category/product-news/)
* [Other](https://blog.sekoia.io/category/soc-insights-other-news/)
* [Sign up](https://go.sekoia.io/Preference-center-EN.html)
* [About Sekoia.io](https://www.sekoia.io/en/about/)
  + [TDR Team](https://www.sekoia.io/en/about-threat-detection-research-team/)
  + [AI-SOC platform](https://www.sekoia.io/en/homepage/)
  + [Interactive demo](https://sekoia.storylane.io/share/8zdjfok9atpn)
  + [Contact Us](https://www.sekoia.io/en/contact/)

Log in

[Product News](https://blog.sekoia.io/category/product-news/ "Product News")

# Getting started with Detection-as-Code and Sekoia Platform

Whether you're an MSSP looking to enhance client offerings or an internal SOC team striving for operational excellence, adopting Detection-as-Code can be a game-changer. Here’s why it matters.

[![](https://t7f4e9n3.delivery.rocketcdn.me/wp-content/uploads/2023/04/logo-sekoia-symbol-6.png)](#molongui-disabled-link)

[Antoine Heuzé](#molongui-disabled-link)
October 4 2024

0

9 minutes reading

## Table of contents

* [Introduction](#h-introduction)
* [What is Detection-as-Code?](#h-what-is-detection-as-code)
* [Key benefits for MSSPs and internal SOC teams](#h-key-benefits-for-mssps-and-internal-soc-teams)
* [Key Sekoia capabilities for enabling Detection-as-Code](#h-key-sekoia-capabilities-for-enabling-detection-as-code)
  + [First steps: Create and deploy a Sigma detection rule in Sekoia](#h-first-steps-create-and-deploy-a-sigma-detection-rule-in-sekoia)
    - [Create a Sigma Detection](#h-create-a-sigma-detection)
    - [POST Request to Sekoia API](#h-post-request-to-sekoia-api)
* [Leverage GitHub to store and deploy custom detections](#h-leverage-github-to-store-and-deploy-custom-detections)
  + [Create and configure a GitHub repository](#h-create-and-configure-a-github-repository)
  + [Add a GitHub workflow to deploy rules](#h-add-a-github-workflow-to-deploy-rules)
  + [Create and deploy your detections](#h-create-and-deploy-your-detections)
* [Conclusion](#h-conclusion)

## Introduction

Managed Security Service Providers (MSSPs) and internal SOC teams face major challenges in the current cybersecurity landscape. Managing different SOC deployments across various clients or business units can lead to inconsistencies, inefficiencies, and vulnerabilities. Traditional approaches often fall short, struggling with scalability, agility, and accuracy. This is where Detection-as-Code can play a crucial role, offering transformative solutions to elevate your security operations.

Whether you’re an MSSP looking to enhance client offerings or an internal SOC team striving for operational excellence, adopting Detection-as-Code can be a game-changer. Here’s why it matters.

## What is Detection-as-Code?

Detection-as-Code is a modern approach to threat detection that allows security teams to define, manage, and deploy detection logic using code. This methodology enhances accuracy, fosters collaboration, and enables rapid scaling by adopting practices similar to DevOps.

## Key benefits for MSSPs and internal SOC teams

1. **Scalability**: Automate and standardize detection rules to easily scale across different environments and clients.
2. **Consistency**: Ensure uniform application of detection logic, reducing false positives and missed detections.
3. **Flexibility**: Quickly adapt to emerging threats by updating detection logic on-the-fly.
4. **Efficiency**: Streamline collaboration and knowledge sharing within your security team using version control and code repositories.
5. **Quality assurance**: Leverage code reviews, testing, and continuous integration to maintain high standards for detection rules.

## Key Sekoia capabilities for enabling Detection-as-Code

Sekoia SOC Platform has been designed to handle Detection-as-Code natively, leveraging:

1. **Detection logic with Sigma:** Detection rules are defined using Sigma, a generic and open standard for writing SIEM detections. These can be easily managed, versioned, and shared in git repositories, enabling:

* **Collaboration:** Allow security teams to collaboratively develop and refine detection logic using familiar tools.
* **Version control:** Track changes, review updates, and maintain a history of detection rules with git repositories.
* **Portability:** Facilitate the seamless transfer and sharing of detection logic across different systems and environments.

2. **API-based configuration:** All aspects of the Sekoia platform can be configured through APIs, ensuring seamless integration and automation with third party code repositories and CI/CD tools. This API-first approach allows for the comprehensive management of detection logic, workflows, and policies without manual intervention. More details on Sekoia APIs on the public documentation here: <https://docs.sekoia.io/xdr/develop/rest_api/quickstart/>

3. **Fine-tuned detections:** All built-in and custom detections can be enabled and fine-tuned through the API across several levels, including:

* **Communities (Tenants):** Manage detection rules at the tenant level, ensuring consistent security policies across all clients or business units.
* **Entities:** Tailor detection rules to specific entities within your organization for more precise threat detection.
* **Assets:** Customize detection logic based on the criticality and context of individual assets, enhancing protection where it matters most.
* **Alert filters:** Ignore specific cases by creating Sigma patterns to be excluded from the detection.

### First steps: Create and deploy a Sigma detection rule in Sekoia

To illustrate how Detection-as-Code can be implemented with the Sekoia platform, here’s a quick example of creating a Sigma detection rule and deploying it via the Sekoia API.

#### Create a Sigma Detection

Create a file named `my_detection.yml` containing a Sigma pattern, such as the following simple content:

```
name: failed_logon
detection:
    selection:
        event.category: authentication
        action.outcome: failure
    condition: selection
---
correlation:
    type: event_count
    rules:
        - failed_logon
    group-by:
        - action.properties.TargetUserName
        - action.properties.TargetDomainName
    timespan: 5m
    condition:
        gte: 10
```

This example was taken from the [Sigma v2.0](https://blog.sigmahq.io/introducing-sigma-specification-v2-0-25f81a926ff0) and [Sigma Correlation](https://blog.sigmahq.io/introducing-sigma-correlations-52fe377f252...