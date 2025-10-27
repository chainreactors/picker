---
title: SAP Cloud ALM : Next Generation -Data Collection Infrastructure
url: https://blogs.sap.com/2023/05/05/sap-cloud-alm-next-generation-data-collection-infrastructure/
source: SAP Blogs
date: 2023-05-06
fetch_date: 2025-10-04T11:40:26.497670
---

# SAP Cloud ALM : Next Generation -Data Collection Infrastructure

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Technology](/t5/technology/ct-p/technology)
* [Technology Blog Posts by SAP](/t5/technology-blog-posts-by-sap/bg-p/technology-blog-sap)
* SAP Cloud ALM : Next Generation -Data Collection I...

Technology Blog Posts by SAP

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/technology-blog-sap/article-id/160472&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [SAP Cloud ALM : Next Generation -Data Collection Infrastructure](/t5/technology-blog-posts-by-sap/sap-cloud-alm-next-generation-data-collection-infrastructure/ba-p/13557627)

![former_member513362](https://avatars.profile.sap.com/former_member_small.jpeg "former_member513362")

[former\_member513362](https://community.sap.com/t5/user/viewprofilepage/user-id/513362)

Explorer

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=technology-blog-sap&message.id=160472)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/technology-blog-sap/article-id/160472)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13557627)

‎2023 May 05
3:53 PM

[9
Kudos](/t5/kudos/messagepage/board-id/technology-blog-sap/message-id/160472/tab/all-users "Click here to see who gave kudos to this post.")

3,664

* SAP Managed Tags
* [SAP Cloud ALM](https://community.sap.com/t5/c-khhcw49343/SAP%2520Cloud%2520ALM/pd-p/73554900100800002513)

* [SAP Cloud ALM

  Software Product](/t5/c-khhcw49343/SAP%2BCloud%2BALM/pd-p/73554900100800002513)

View products (1)

# **Introduction**

The **Next Generation - Data Collection Infrastructure** available with SAP Cloud ALM provides a standardized way to collect monitoring data using the **OpenTelemetry** instrumentation approach and protocol. With this approach, we reduce the instrumentation and operations efforts for the Cloud LoBs to the minimum. The observability data can be sent in a fire-and-forget manner, without the need for any persistence and with minimal integration efforts in SAP Cloud ALM. Currently, this approach is supported for Performance Monitoring, Integration Monitoring, Job Monitoring and Health Monitoring apps in SAP Cloud ALM.

# **Motivation**

SAP Cloud ALM Run (CRUN) collects monitoring data for various use cases like Performance Monitoring, Integration Monitoring, Exception Monitoring etc., from Managed-Cloud services. This needs considerable instrumentation effort from the LoB applications and requires connectivity to be established by the customer.

At this juncture, Next Generation – Data Collection Infrastructure (NG-DCI) intervenes with an aim to:

* Reduce the Cloud LoB effort to integrate with CRUN

* Relieve customers from the task of establishing connectivity between the Managed-Cloud tenant and Cloud ALM tenant.

* Relieve Managed-Cloud (LoB) applications from having to maintain the configurations of tenant-specific connectivity between Cloud applications microservices and CALM instances

* Relieve multi-tenant applications and services from keeping up a state and using an unforeseeable number of resources (memory, CPU usage etc.)

# **Why use OpenTelemetry?**

* OpenTelemetry (also referred to as OTel) is an open-source observability framework with a collection of tools, APIs, and SDKs.

* OTel is the new industry standard for adding observable instrumentation to cloud-native applications both inside and outside SAP.

* OTel enables us to instrument, generate, collect, and export telemetry data for analysis and to understand the application’s performance and behavior.

* OTel is vendor-agnostic instrumentation library (available per language) with support for both automatic and manual instrumentation.

* OTel makes observability effortless, inexpensive, and insightful.

* OTel is aligned with Cross Product Architecture vision for Logging & Monitoring and Technology Guidelines at SAP.

# Concept and **Architecture**

NG-DCI has three core components, described along with their goals below:

1. **Data Collection Instrumentation -** Provide **sufficient instrumentation support**

   * Minimize instrumentation efforts for the customer and SAP

   * Use standard OpenTelemetry, whenever possible

   * Support all use cases in a standardized manner as much as possible. For example, connectivity handling and configuration exchange.

   * Enable end-to-end correlation by hybrid approach of SAP Passport and OpenTelemetry based correlation.

2. **Data Collector Runtime -**Provide **unified data collection runtime** approach

   * Unify runtime for push-based and pull-based data collection

   * Provide unified approach for customer’s and SAP internal use cases

   * Replace customer-managed connectivity with SAP-managed connectivity for SaaS scenarios.

   * Improve quality of data delivery by efficient queuing

3. **Data Routing infrastructure** in CALM - Provide **unified approach for data routing**

   * Enable dynamic routing of data to corresponding SAP Cloud ALM tenant across data centers.

   * Embrace openness regarding data exchange

   * Import data from third-party services or systems based on the APIs that are inbound to OpenTelemetry

   * Export data to third-party services or systems based on the APIs that are outbound from OpenTelemetry

   * Forward data to SAP Focused Run (FRUN)

   * Improve quality of data delivery by efficient queuing

# ![](/legacyfs/online/storage/blog_attachments/2023/04/NG-DCI-concept-and-architecture.png)

# **Why NG-DCI?**

|
 **Before NG-DCI** |
 **With NG-DCI** |

|
 Tenant to tenant connectivity |
 Application to application connectivity |

|
 Customer managed connectivity and the need to manage multiple credentials. |
 Connectivity and authentication are managed by NG-DCI. No customer interaction required. |

|
 Multiple calls to SAP Cloud ALM (per use case) |
 Cross tenant calls managed by DCI (Data Collection Instrumentation). |

|
 Less efficient |
 Increased efficiency and scalability |

|
 High integration efforts |
 Reduced instrumentation and operations efforts |

|
 Multiple integration APIs exposed by SAP Cloud ALM use cases which result in various integration activities. |
 Standardized integration approach using OpenTelemetry |

# References

[Next Generation – Data Collection Infrastructure (cloud.sap)](https://support.sap.com/en/alm/sap-cloud-alm/operations/expert-portal/data-collection-infrastructure.html)

[OpenTelemetry](https://opentelemetry.io/docs/)

Labels

* [Product Updates](/t5/technology-blog-posts-by-sap/bg-p/technology-blog-sap/label-name/product%20updates)

* [Logging and Monitoring](/t5/tag/Logging%20and%20Monitoring/tg-p/board-id/technology-blog-sap)
* [NG-DCI](/t5/tag/NG-DCI/tg-p/board-id/technology-blog-sap)
* [sap cloud alm for operations](/t5/tag/sap%20cloud%20alm%20for%20operations/tg-p/board-id/technology-blog-sap)

You must be a registered user to add a comment. If you've already registered, sign in. Otherwise, register and sign in.

* [Comment](/plugins/common/feature/oidcss/sso_login_redirect/providerid/sap_ids_prompt?redirectreason=permissiondenied&referer=https%3A%2F%2Fcommunity.sap.com%2Ft5%2Ftechnology-blog-posts-by-sap%2Fsap-cloud-alm-next-generation-data-collection-infrastructure%2Fba-p%2F13557627%23comment-on-this)

Copy Link
![](https://community.sap.com/html/@EE5D5986E9F4E5657DCEACB7532B5C39/assets/bluesky-dark.svg)Bluesky
Linkedin

Related Content

*...