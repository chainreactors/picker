---
title: AWS vs Azure: A “Secure by default” comparison
url: https://securitycafe.ro/2024/09/03/aws-vs-azure-a-secure-by-default-comparison/
source: Security Café
date: 2024-09-04
fetch_date: 2025-10-06T18:27:51.987769
---

# AWS vs Azure: A “Secure by default” comparison

[Skip to content](#content)

[Security Café](https://securitycafe.ro/)

Security Research and Services

* [Things we do on a daily basis](https://securitycafe.ro/security-services-for-business/)
  + [Red Team (DORA/TIBER) exercises](https://securitycafe.ro/security-services-for-business/dora-tiber-exercises/)
  + [Web Application Penetration Testing](https://securitycafe.ro/security-services-for-business/web-application-penetration-testing/)
  + [Mobile Application Penetration Testing](https://securitycafe.ro/security-services-for-business/mobile-application-penetration-testing/)
  + [Infrastructure Penetration Testing](https://securitycafe.ro/security-services-for-business/infrastructure-penetration-testing/)
  + [Vulnerability Assessment](https://securitycafe.ro/security-services-for-business/vulnerability-assessment/)
* [CVEs, Talks and Tools](https://securitycafe.ro/cves-talks-and-tools/)
* [Contact](https://securitycafe.ro/contact/)
* [About](https://securitycafe.ro/about/)

[![](https://securitycafe.ro/wp-content/uploads/2015/01/cropped-cropped-coffee-banner-2-4.jpg)](https://securitycafe.ro/)

![](https://securitycafe.ro/wp-content/uploads/2024/08/awsvsaz.jpg?w=840)

# AWS vs Azure: A “Secure by default” comparison

[September 3, 2024](https://securitycafe.ro/2024/09/03/aws-vs-azure-a-secure-by-default-comparison/ "12:22 pm") [Stefan Tita](https://securitycafe.ro/author/stitakpmgcom/ "View all posts by Stefan Tita") [aws](https://securitycafe.ro/category/cloud-security/aws/), [Azure](https://securitycafe.ro/category/cloud-security/azure/), [Cloud Security](https://securitycafe.ro/category/cloud-security/) [Leave a comment](https://securitycafe.ro/2024/09/03/aws-vs-azure-a-secure-by-default-comparison/#respond)

Whether you are in charge of deciding what Cloud solution to choose for your organization or you are a Security Professional trying to decide what Cloud technology to learn, when it comes to choosing the right Cloud solution there are multiple factors that need to be reviewed such as ***Services***/***Features***, ***Costs*** and obviously ***Security*** which we will focus on.

AWS has been indeed first to market and has been a market leader ever since. However, as we will see, being second has its advantages and allowed Azure to design better and avoid some mistakes.

Even though other articles comparing these two cloud providers give an edge to AWS, based on our experience conducting both AWS and Azure assessments, we see misconfigurations affecting AWS more often than Azure due to a lack of “Secure by default” settings.

When deciding based on ***Services*** and ***Costs*** the choice between AWS and Azure would typically depend on your specific requirements and the needs of your organization. Both AWS and Azure offer a broad and deep set of capabilities with global coverage and both offer a pay-as-you-go pricing model with discounts applicable depending on the amount of resources consumed.

However, let’s take a closer look at the ***Security*** differences between the two cloud providers by reviewing the design choices, default settings and vulnerabilities that have been exploited over the years. We’ll focus on recurring issues that present constant problems, and not one time issues or CVEs.

#### Table of Contents

1. [Instance Metadata Service (Server-Side Request Forgery)](#instance-metadata-service-server-side-request-forgery)
2. [Lambda Functions (Local File Inclusion)](#lambda-functions-local-file-inclusion)
3. [Publicly Exposed Services](#publicly-exposed-services)
4. [Access Keys (AWS) vs Interactive Login (Azure)](#access-keys-aws-vs-interactive-login-azure)
5. [AWS IAM Policies vs Azure Roles (RBAC)](#aws-iam-policies-vs-azure-roles-rbac)
6. [Conclusions](#conclusions)

### Instance Metadata Service (Server-Side Request Forgery)

There are situations where a discovered Server-Side Request Forgery (SSRF) vulnerability (with read access) within a web application does not have a high impact because it cannot be leveraged to extract sensitive information.

However, SSRF has become a very high impact vulnerability if discovered on web applications hosted on AWS, mainly because the Instance Metadata Service API Version 1 (***IMDSv1***) can be interrogated through a simple GET request from the EC2 instance. Through the SSRF vulnerability it is possible to initiate the GET request and receive from the Metadata Service API a session token with the permissions of the EC2 instance. This could lead to privilege escalation within the cloud environment.

![](https://techproject.ro/wp-content/uploads/2024/07/image-1-1024x262.png)

Using SSRF to extract access keys from IMDSv1

AWS has introduced Instance Metadata Service *Version 2* (***IMDSv2***) which prevents Server-Side requests from interrogating the Metadata Service API and obtaining a session token by requiring a PUT request instead of a GET request, therefore it is not possible to initiate a session with IMDSv2 using a SSRF vulnerability.

However, when creating a new EC2 instance, Version 1 of IMDS is selected by default and during our assessments we find many cases of new EC2 instances still using IMDSv1. Therefore, even though AWS offers a secure option through IMDSv2, it also allows room for misconfiguration by having IMDSv1 selected by default when creating a new EC2 instance.

On the other side, Azure has mitigated this issue from the start by requiring the presence of the ***“Metadata: true” header*** when initiating a session with the Metadata Service, which cannot be added through a Server-Side request thus preventing SSRF.

More details about this issue: <https://hackingthe.cloud/aws/exploitation/ec2-metadata-ssrf>

### Lambda Functions (Local File Inclusion)

Similar to the previous attack vector but not as popular, ***Lambda functions*** affected by some kind of ***file read vulnerability (LFI, SSRF, XXE)*** can also lead to exposing IAM credentials stored in the Environment Variables (file:///proc/self/environ) of the container running the code. More details about this vulnerability: <https://hackingthe.cloud/aws/exploitation/lambda-steal-iam-credentials/>

Unlike AWS which stores these access credentials directly in Environment Variables, ***Azure Managed Identities*** that are used in multiple resource types (App Services, Azure Functions, Automation Accounts, etc.) use two environment variables called IDENTITY\_ENDPOINT and IDENTITY\_HEADER that contain information required to perform a specific HTTP GET request to a localhost endpoint that returns the Managed Identity access credentials (similar to how the Azure Metadata Service works). Therefore, you cannot retrieve access credentials through a file read vulnerability, instead you need full code execution on the container. Details about Azure Managed Identity headers: <https://learn.microsoft.com/en-us/azure/app-service/overview-managed-identity#rest-endpoint-reference>

![](https://techproject.ro/wp-content/uploads/2024/08/image-1.png)

Example of Azure Automation Account environment variables that are used to retrieve access credentials

Even though the Azure implementation is better designed to protect against credentials exposure which could lead to privilege escalation, mistakes have been made in the past that allowed critical Cross-Account ***unauthorized*** access to any other Azure customer accounts using services such as Azure Automation Account. This vulnerability was however mitigated promptly: <https://orca.security/resources/blog/autowarp-microsoft-azure-automation-service-vulnerability/>

### Publicly Exposed Services

One issue that we often encounter is regarding certain resource types, such as ***S3 Buckets***/***Storage Accounts*** and ***Container Registry images***, that are exposed unintentionally to the Internet. Often times these resources do not contain anything sensitive of value, but it can be time consuming to review all the exposed resources to identify if they contain sensitive i...