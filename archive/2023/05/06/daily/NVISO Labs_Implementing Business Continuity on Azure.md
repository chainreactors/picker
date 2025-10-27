---
title: Implementing Business Continuity on Azure
url: https://blog.nviso.eu/2023/05/05/implementing-business-continuity-on-azure/
source: NVISO Labs
date: 2023-05-06
fetch_date: 2025-10-04T11:39:34.702527
---

# Implementing Business Continuity on Azure

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

# Implementing Business Continuity on Azure

[Elpida Rouka](https://blog.nviso.eu/author/elpida-rouka/ "Posts by Elpida Rouka")

[Azure](https://blog.nviso.eu/category/cloud-security/azure/), [Cloud Security](https://blog.nviso.eu/category/cloud-security/), [Cyber Strategy](https://blog.nviso.eu/category/cyber-strategy/), [Business Continuity](https://blog.nviso.eu/category/cybersecurity/business-continuity/)

May 5, 2023May 5, 2023
12 Minutes

There is a general misconception among cloud consumers that the availability of their resources in the cloud is always guaranteed. This is not true since all cloud providers, including Microsoft, offer specific SLAs for their products that almost never reach an availability target of 100%. For the consumers who have deployed critical resources and applications to the cloud, reaching the company-defined targets for Business Continuity can be technically challenging and confusing. The purpose of this blog post is to provide practical guidance on how Business Continuity is expressed on the cloud, how it can be implemented for many Azure IaaS and PaaS services and what real-world problems each solution attempts to solve.

## Introduction

Before we dive into the technical Azure-specific details, let’s explain what Business Continuity is and what it involves.

*Business Continuity* is the capability of the organization to continue the delivery of products or services at acceptable predefined levels following a disruptive incident. According to ISO 22301, business continuity is not limited only to IT and it involves many enterprise aspects.

In this blog post, we will focus on the business continuity aspects related to IT. Each of them corresponds to a specific type of SLA that you may have internally or with your customers, so there are multiple aspects of Business Continuity that may be applicable to you.

If it’s important for you to keep your services always up and running, you should focus on *High Availability*. This is the ability of a system to be continuously operational, or, in other words, have an uptime percentage of near 100%. It is generally achieved by implementing redundant, mirrored copies of the hardware and data, so that if one component fails, another one takes over.

If fluctuating demand and bottlenecks cause your systems to struggle, then you may need to focus on *Scalability*. This is the ability of a system to scale up or scale down cloud resources as needed to meet fluctuating demand. It can be considered as an aspect of Business Continuity, since peaks in demand can be the result or the cause of an incident.

Finally, to protect data that are critical to your company’s functionality and need to be always available and recoverable, you should implement *Backup.* This is the duplication of data to a secondary location, so that if the primary copy is harmed or becomes unavailable, data from the other location can be retrieved and the system can be rolled back to a specific point in time.

The following diagram shows an analogy between the aforementioned terms and the problems they tackle.

![](https://blog.nviso.eu/wp-content/uploads/2023/01/image-20-1024x445.png)

*Business Continuity: Mapping of problems and solutions*

It is important to note that the implementation of any of the controls described in this blogpost should be based on a structured business continuity assessment/plan, and should be selected based on the requirements of your environment or application. Improvident implementation of controls could result in undue costs or in inefficient protection.

## Implementing High Availability

Depending on the required uptime of your application or system and the scale of disaster you need to be able to recover from, there are many ways to implement high availability in Azure. When choosing the controls that will be implemented in your environment, you should always consider that the availability in a chain of resources is determined by the weakest link in the chain. For example, in the case of an application composed by a front-end server and a database, if the web server is spread across multiple availability zones but the database is single-instance, the whole application will not be available anymore if the availability zone of the database goes down. Having the above in mind, we present below the different options provided by Azure, sorted by increasing complexity and costs.

### Protection against hardware failures

Small-scale technical or hardware issues may affect single-instance components. To avoid this, the component should be mirrored to a secondary hardware volume. On Azure, depending on your cloud computing state, this can be implemented as follows:

#### IaaS

When the component is a Virtual Machine (VM), this can be achieved by using **availability sets**. An availability set is a logical grouping of VMs that allows Azure to understand how your application is built to provide for redundancy and availability. While for single-instance VMs Azure guarantees a 99,9% uptime SLA, by using availability sets the uptime is increased to 99,95%. To use availability sets on Azure VMs, you need to perform the following steps:

1. Create an availability set;
2. Create new VMs; in the creation wizard, under “Availability options” choose “Availability set” and then select the previously created set.

*Note: It is not possible to add existing VMs to an availability set after their creation.*

#### PaaS

Azure PaaS components are protected against local hardware failures by design, guaranteeing higher uptime SLAs than IaaS. Specifically:

* Storage Accounts: Microsoft ensures 3 instances of the service when using the default redundancy option (Locally redundant Storage – LRS). This offers an SLA of 99.999999999% (11 nines) uptime.
* SQL Databases: By default, Microsoft ensures at least two instances of the service within the same data center, reaching 99,99% uptime.
* Cosmos DB: By default, Microsoft provides three replicas (individual nodes) within a cluster, ensuring an SLA of 99,99% uptime.
* App Service: Microsoft guarantees an SLA of 99.95% uptime for App Services, for tiers other than Free or Shared.

### Protection against datacenter failures

To provide the option of protecting against failures that affect the whole datacenter, such as fire, power and cooling disruptions or flood, Microsoft has introduced th...