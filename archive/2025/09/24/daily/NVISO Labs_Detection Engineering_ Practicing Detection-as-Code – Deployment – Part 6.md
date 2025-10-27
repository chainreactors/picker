---
title: Detection Engineering: Practicing Detection-as-Code – Deployment – Part 6
url: https://blog.nviso.eu/2025/09/23/detection-engineering-practicing-detection-as-code-deployment-part-6/
source: NVISO Labs
date: 2025-09-24
fetch_date: 2025-10-02T20:34:28.605384
---

# Detection Engineering: Practicing Detection-as-Code – Deployment – Part 6

[Skip to content](#content)

[![NVISO Labs](https://blog.nviso.eu/wp-content/uploads/2022/12/cropped-abn-zcrj_400x400-1.png)](https://blog.nviso.eu/)

[NVISO Labs](https://blog.nviso.eu/)

Cyber security research, straight from the lab! 🐀

* [twitter](https://twitter.com/NVISO_Labs)
* [linkedin](https://www.linkedin.com/company/nviso-cyber)
* mail us
* [our company](https://www.nviso.eu)
* [SSO](https://blog.nviso.eu/wp-admin/edit.php)

Menu

* [All](https://blog.nviso.eu/)
* [Blue Team](https://blog.nviso.eu/category/blue-team/)
* [Cloud Security](https://blog.nviso.eu/category/cloud-security/)
  + [AWS](https://blog.nviso.eu/category/cloud-security/aws/)
  + [Azure](https://blog.nviso.eu/category/cloud-security/azure/)
  + [GCP](https://blog.nviso.eu/category/cloud-security/gcp/)
  + [Microsoft 365](https://blog.nviso.eu/category/cloud-security/microsoft-365/)
* [Awareness](https://blog.nviso.eu/category/awareness/)
* [Forensics](https://blog.nviso.eu/category/forensics/)
* Other
  + [Application Security](https://blog.nviso.eu/category/application-security/)
  + [IoT Security](https://blog.nviso.eu/category/iot-security/)
  + [Web Security](https://blog.nviso.eu/category/web-security/)
  + [Industrial Security](https://blog.nviso.eu/category/industrial-security/)
  + [Mobile Security](https://blog.nviso.eu/category/mobile-security/)
  + [Cyber Strategy](https://blog.nviso.eu/category/cyber-strategy/)
  + [Purple Team](https://blog.nviso.eu/category/purple-team/)
  + [Red Team](https://blog.nviso.eu/category/red-team/)
  + [Events](https://blog.nviso.eu/category/events/)

# Detection Engineering: Practicing Detection-as-Code – Deployment – Part 6

[Stamatis Chatzimangou](https://blog.nviso.eu/author/stamatis-chatzimangou/ "Posts by Stamatis Chatzimangou")

[Blue Team](https://blog.nviso.eu/category/blue-team/), [Detection Engineering](https://blog.nviso.eu/category/detection-engineering/)

September 23, 2025September 25, 2025
24 Minutes

The deployment phase is one of the most challenging steps in the Detection Development Life Cycle due to its implementation complexity. Factors that must be considered when designing a deployment pipeline are secret management, request timeouts, API response codes, and API request limits. Each of these elements must be carefully addressed during the implementation of the deployment pipeline.

In this part, we will explore the principles and practices of deploying rules to target platforms. Additionally, we will go through some of the challenges encountered when designing and implementing a deployment pipeline, along with suggestions on how to overcome them, to ensure that our Continuous Deployment pipeline operates smoothly. We are going to provide examples, from different deployment pipelines that you could refer to when deciding on your own design.

## Deployment Components

To be able to understand more about the CD pipeline design, we’ll go through the key components we will be using.

### API Consumer

Most modern SIEM or XDR platforms provide an API that can be used to manage the detection rules. To utilize this API, detection engineers must develop an API consumer. An API consumer is software designed to interact with the API by sending requests and receiving responses, enabling integration and utilization of the functionalities provided by the API provider. The API consumer should be able to use the API for listing, creating, updating, or deleting the detection rules in the target platform.

Key considerations when developing the API consumer include:

* **Authentication and Authorization** – Typically the API will require the use of API keys, OAuth or other authentication mechanisms, to ensure secure access. It is essential to handle credential material with care when storing and retrieving them to ensure security.
* **Rate Limiting** – Often, the API provider may impose limits on the number of requests an API consumer can make within a specific timeframe to prevent abuse of the application. Rate limiting should be taken into account when developing the API consumer and a required sleep time should be enforced to ensure that we adhere to the limitations.
* **Response and** **Error Handling** – The API consumer must be able to manage responses and errors, such as HTTP 400 or 500 status codes or read timeouts, in a graceful manner. It is important to log verbose messages related to the status codes and error messages provided by the API, so that we are able to troubleshoot potential issues with ease when we deploy our detections.

In our example for Sentinel, we will be using the Microsoft documentation as a reference to the authentication mechanism [1], the expected API Responses [2], as well as the API rate limits. Similar documentation is typically available for other products as well, like Microsoft Defender for Endpoint for example [3] (even though it’s still in beta).

A sample screenshot from our API consumer is provided below. The consumer class implements methods for basic functionalities that we are going to use, like fetching all the platform rules, deploying a rule and deleting a rule.

![](https://blog.nviso.eu/wp-content/uploads/2025/08/image-34-1024x241.png)

### App Registration

In order to be able to access the Sentinel API we need to create an App registration in Azure. The App registration connects an application with Azure Active Directory (Azure AD) to enable it to authenticate and access Azure resources and services.

The App registration for Sentinel must be assigned with the Sentinel Contributor role [4] that allows it to perform actions under *Microsoft.SecurityInsights/\** which includes the API endpoints that we need to manage the rules [2]. This is a necessary step, so that the API consumer will be able authenticate and use the API. The assignment can be done under the *Log Analytics workspace settings* -> *Access Control (IAM)* -> *Role Assignments*.

![](https://blog.nviso.eu/wp-content/uploads/2025/08/image-33-1024x358.png)

### Credential Material Management

Credential Material to access the target platform should be stored securely and encrypted. In Azure DevOps, you have several options for accessing credential material. Credentials can be stored directly in Azure DevOps as secret variables. Another option would be to use Azure Key Vault as a secure service for storing secrets, which also integrates well with Azure DevOps, allowing pipelines to fetch secrets dynamically. However, if you need to handle secrets in your pipelines, always follow the best practices [5] as advised by Microsoft.

In addition to that, instead of using a Key Vault, Azure DevOps offers the option to use service connections [6] and managed identities [7]. A service connection provides secure access to external services from your pipelines, while managed identities allow Azure resources to authenticate against Azure services without storing credentials in code.

### Pipeline Agents

Code that runs in Azure Pipelines requires at least one agent. In [Part 3](https://blog.nviso.eu/2025/08/05/detection-engineering-practicing-detection-as-code-validation-part-3/), we briefly went through the basic components of a pipeline, one of which was a Job. When a pipeline is executed, the system initiates one or more jobs. An agent is computing infrastructure with installed agent software that runs one job at a time [8]. Deploying more than one agents allows us to run Jobs in parallel.

![](https://blog.nviso.eu/wp-content/uploads/2025/08/image-35.png)

This is particularly useful from the standpoint of an MSSP, as it allows us to speed up the deployment by deploying in parallel to multiple tenants. We are going a bit more into depth on that topic on the section “Multitenant Deployments” below.

### Component Diagram

In [Part 1](https://blog.nviso.eu/2025/07/08/detection-engineering-practicing-detection-as-code-introduction-part-1/), we introduced a high-level workflow diagram outlining the approach for this seri...