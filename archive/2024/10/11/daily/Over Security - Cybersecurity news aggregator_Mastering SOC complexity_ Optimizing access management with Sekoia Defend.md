---
title: Mastering SOC complexity: Optimizing access management with Sekoia Defend
url: https://blog.sekoia.io/mastering-soc-complexity-optimizing-access-management-with-sekoia-defend/
source: Over Security - Cybersecurity news aggregator
date: 2024-10-11
fetch_date: 2025-10-06T18:55:34.274821
---

# Mastering SOC complexity: Optimizing access management with Sekoia Defend

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

# Mastering SOC complexity: Optimizing access management with Sekoia Defend

In hybrid and outsourced SOC models, managing access for different stakeholders—including internal security teams, MSSP personnel, and other IT departments—can be complex. Even different teams than security ones may need access to specific data,...

[![](https://t7f4e9n3.delivery.rocketcdn.me/wp-content/uploads/2023/04/logo-sekoia-symbol-6.png)](#molongui-disabled-link)

[Maxime Hugon](#molongui-disabled-link)
October 10 2024

0

8 minutes reading

## Table of contents

* [Managing access across teams: The challenge in SOC models](#h-managing-access-across-teams-the-challenge-in-soc-models)
* [How Sekoia Defend streamlines SOC access management](#h-how-sekoia-defend-streamlines-soc-access-management)
  + [Multi-Tenant architecture: Enhancing large operations](#h-multi-tenant-architecture-enhancing-large-operations)
  + [Entities & Intakes: The foundation for segmentation](#h-entities-amp-intakes-the-foundation-for-segmentation)
  + [Role-Based Access Control (RBAC): Ensuring secure permissions](#h-role-based-access-control-rbac-ensuring-secure-permissions)
  + [Restricted roles to segregate access to data by Intakes](#h-restricted-roles-to-segregate-access-to-data-by-intakes)
* [Use-cases](#h-use-cases)
* [Multi-Tenant architecture: Simplifying complex environments](#h-multi-tenant-architecture-simplifying-complex-environments)
  + [Use Case 1: MSSP managing multiple clients](#h-use-case-1-mssp-managing-multiple-clients)
  + [Use Case 2: Large companies with subsidiaries](#h-use-case-2-large-companies-with-subsidiaries)
* [Data segregation by Intakes: Fine-tuned data access control](#h-data-segregation-by-intakes-fine-tuned-data-access-control)
  + [Use Case 3: Managing access for IT and security teams](#h-use-case-3-managing-access-for-it-and-security-teams)
* [Maximizing Efficiency by Combining Multi-Tenant and Data Segregation](#h-maximizing-efficiency-by-combining-multi-tenant-and-data-segregation)
  + [Use Case 4: Managing global security in international groups](#h-use-case-4-managing-global-security-in-international-groups)
  + [Use Case 5: MSSPs streamlining operations](#h-use-case-5-mssps-streamlining-operations)
* [Conclusion: Empowering security operations with Sekoia Defend](#h-conclusion-empowering-security-operations-with-sekoia-defend)

In today’s evolving cybersecurity landscape, organizations face the challenge of monitoring and responding to threats efficiently through their Security Operations Centers (SOC). Depending on an organization’s size and security priorities, different SOC models are adopted, each with its own approach to security management.

Some companies opt for a **fully in-house SOC**, with internal teams managing all aspects of security operations. Large corporations, in particular, benefit from this model, given their resources to maintain a dedicated security staff. On the other hand, **hybrid SOCs** combine internal expertise with external Managed Security Service Providers (MSSPs), allowing businesses to maintain control over some aspects of security while outsourcing monitoring and threat detection. Smaller organizations often rely on **outsourced SOCs**, entirely managed by MSSPs, which offer scalability and expert monitoring without the need for a full in-house team.

Each SOC model offers unique advantages:

* **In-house SOCs** provide complete control over security operations.
* **Hybrid SOCs** offer a balance of internal oversight and outsourced expertise.
* **Outsourced SOCs** bring cost-effective security solutions with scalability.

However, each SOC model presents challenges, particularly when it comes to managing access to sensitive security data across multiple teams.

## Managing access across teams: The challenge in SOC models

In hybrid and outsourced SOC models, managing access for different stakeholders—including internal security teams, MSSP personnel, and other IT departments—can be complex. Even different teams than security ones may need access to specific data, such as network logs for infrastructure team, without being exposed to broader security intelligence. This situation calls for **fine-grained control** over permissions, ensuring teams only access the data necessary for their role, while maintaining strict data segregation to prevent unauthorized exposure.

Effective access management becomes increasingly complex as organizations rely on both internal and external teams, requiring **robust security tools** to manage permissions and safeguard sensitive information.

## How Sekoia Defend streamlines SOC access management

Sekoia Defend addresses these access challenges with two standout features: **multi-tenant support** and **data segregation by Intakes (data sources)**. These features offer flexibility and control, allowing organizations to segment security environments and manage data access with precision.

### Multi-Tenant architecture: Enhancing large operations

For MSSPs managing multiple clients or large companies managing multiple subsidiaries, **multi-tenant architecture** is crucial. Sekoia Defend allows to operate a **parent tenant** (called “**workspace**”) to oversee all clients, while each client is provided with an isolated **child tenant** (called \*\*\*\*“**community**” \*\*\*\*in the product). This ensures complete data segregation between clients while enabling centralized management from the parent tenant. MSSPs or large companies can customize security configurations for each client, maintaining full control without cross-contaminating environments. This structure simplifies complex environments, enabling flexible management of security operations across multiple structures.

### Entities & Intakes: The foundation for segmentation

In Sekoia Defend, an **entity** represents a distinct organizational unit within a community. Each entity serves as a functio...