---
title: Account Team Member Integration – SAP Sales Cloud (C4C) to SAP Marketing Cloud (SMC)
url: https://blogs.sap.com/2023/08/17/account-team-member-integration-sap-sales-cloud-c4c-to-sap-marketing-cloud-smc/
source: SAP Blogs
date: 2023-08-18
fetch_date: 2025-10-04T11:59:26.881580
---

# Account Team Member Integration – SAP Sales Cloud (C4C) to SAP Marketing Cloud (SMC)

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [CRM and Customer Experience](/t5/crm-and-customer-experience/ct-p/crm)
* [CRM and CX Blog Posts by SAP](/t5/crm-and-cx-blog-posts-by-sap/bg-p/crm-blog-sap)
* Account Team Member Integration - SAP Sales Cloud ...

CRM and CX Blog Posts by SAP

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/crm-blog-sap/article-id/13081&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [Account Team Member Integration - SAP Sales Cloud (C4C) to SAP Marketing Cloud (SMC)](/t5/crm-and-cx-blog-posts-by-sap/account-team-member-integration-sap-sales-cloud-c4c-to-sap-marketing-cloud/ba-p/13558556)

![jan_kaemmerle](https://avatars.profile.sap.com/f/5/idf5f06919f02818f5209720a32a65612276d5a138f988b13759300f93687789ae_small.jpeg "jan_kaemmerle")

![Product and Topic Expert](/html/@138D6F765B60D7FC0168643DE27D8A68/rank_icons/sap-logo-small-14px.png "Product and Topic Expert")
[jan\_kaemmerle](https://community.sap.com/t5/user/viewprofilepage/user-id/239184)

Product and Topic Expert

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=crm-blog-sap&message.id=13081)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/crm-blog-sap/article-id/13081)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13558556)

‎2023 Aug 18
12:48 AM

[6
Kudos](/t5/kudos/messagepage/board-id/crm-blog-sap/message-id/13081/tab/all-users "Click here to see who gave kudos to this post.")

3,046

* SAP Managed Tags
* [SAP Marketing Cloud](https://community.sap.com/t5/c-khhcw49343/SAP%2520Marketing%2520Cloud/pd-p/73555000100700000751)
* [SAP Sales Cloud](https://community.sap.com/t5/c-khhcw49343/SAP%2520Sales%2520Cloud/pd-p/73554900100700002221)

* [SAP Marketing Cloud

  Software Product](/t5/c-khhcw49343/SAP%2BMarketing%2BCloud/pd-p/73555000100700000751)
* [SAP Sales Cloud

  Software Product](/t5/c-khhcw49343/SAP%2BSales%2BCloud/pd-p/73554900100700002221)

View products (2)

# Introduction

The SAP standard package "**SAP Cloud for Customer Integration with SAP Marketing**" ([Integration Flow | SAP Cloud for Customer Integration with SAP Marketing | SAP Business Accelerator ...](https://api.sap.com/package/SAPHybrisCloudforCustomerIntegrationwithSAPHybrisMarketing/integrationflow)) for the integration between SAP Sales Cloud (C4C) and SAP Marketing Cloud (SMC) provides several iFlows for the replication of account/contact and transactional (lead, activity, etc.) data.

With release 2308, the feature "**Segmentation Attributes for Account Team Members"** ([Interaction Contact Attributes | SAP Help Portal](https://help.sap.com/docs/SAP_MARKETING_CLOUD/ac1eab4c66bc490da7ac2c378c46b0e7/0286789a85544ca9a570d4aaaff1e4ac.html?locale=en-US)) will be available in SMC. To make use of the new segmentation attributes, the Account Team Member entity needs to be filled properly by C4C.

However, in the above mentioned SAP standard package, there is no iFlow for the Account Team Member replication included. Therefore, a custom approach needs to be implemented in SAP Cloud Integration (CI) to fulfil the usage in segmentation and also in the email personalization scenario.

## Architecture

To replicate the Account Team Members from C4C to SMC, an iFlow needs to be created in CI. The iFlow needs to pull the data on a frequent base (e.g. scheduling: each hour) from C4C.

The OData Adapter in CI can be used to access the C4C OData Service "**CorporateAccountCollection**" for replication of the "**Account Team Members - Account Relationship**".

Then the mapping (see section "CI Configuration - Mapping") to the OData service "**API\_MKT\_CORPORATE\_ACCOUNT\_SRV;v=0003/AccountTeamMembers**" needs to be done, to send the data to SMC.

![](/legacyfs/online/storage/blog_attachments/2023/07/architecture-3.png)

**Please notice:**

In the above illustration, also the "**Account Team Members**", so the Employee master data, is included. The C4C OData service "**EmployeeBasicDataCollection**" can be used in addition, to load further employee data (needs to be stored in custom fields or customer business objects in SMC).

However, within SMC, the employee master data is already provided in the app "**Maintain Employees**". The attributes "First Name", "Last Name" and "Email Address" are provided in the standard. The replication of further employee data is in most customer scenarios not needed.

Therefore, this blog focuses on the integration of the "**Account Team Members Account Relationship**" only.

# C4C Configuration

## Create Communication System for OData communication

A communication system needs to be created, to fetch the Account Team Members from C4C.

![](/legacyfs/online/storage/blog_attachments/2023/07/c4c_comm_system-1.png)

|
 **ID** |
 e.g. SMC\_AEI (Account Employee Integration) |

|
 **SAP Business Suite** |
 No |

|
 **Host Name** |
 AEI |

|
 **System Access Type** |
 Internet |

In the technical information under system instances the following entry needs to be created:

|
 **System Instance ID** |
 SMC\_AEI |

|
 **Preferred Application Protocol** |
 6 - Http |

## Create Communication Arrangement for OData communication

A communication arrangement with communication scenario "**OData Services for Business Objects**" needs to created.

![](/legacyfs/online/storage/blog_attachments/2023/07/c4c_comm_arrangement-1.png)

In the communication arrangement the following OData services have to be assigned:

* businessuser

* customer

* employeeanduser

* employeebasicdata

## C4C Payload example

When fetching the "**CorporateAccountTeamCollection**" from C4C, the JSON payload looks like below.

*GET:    <https://<host>/sap/c4c/odata/v1/c4codataapi/CorporateAccountTeamCollection>*

```
{

    "d": {

        "results": [

            {

                "__metadata": {

                    "uri": "https://<host>:443/sap/c4c/odata/v1/c4codataapi

                            /CorporateAccountTeamCollection('00163E04B6021ED2B7C1BAE7533304F2')",

                    "type": "c4codata.CorporateAccountTeam",

                    "etag": "W/\"datetimeoffset'2015-07-06T08%3A45%3A26.6721490Z'\""

                },

                "ObjectID": "00163E04B6021ED2B7C1BAE7533304F2",

                "ParentObjectID": "00163E04B6021ED2B7C1B5AF23E884C7",

                "AccountID": "1000001",

                "EmployeeUUID": "00163E03-A070-1EE2-88BA-37FB8F5F50A9",

                "EmployeeID": "E1000",

                "PartyRoleCode": "142",

                "PartyRoleCodeText": "Account Owner",

                "StartDate": "/Date(-62135769600000)/",

                "EndDate": "/Date(253402214400000)/",

                "MainIndicator": true,

                "SalesOrganisationID": "",

                "DistributionChannelCode": "",

                "DistributionChannelCodeText": "",

                "DivisionCode": "",

                "DivisionCodeText": "",

                "ETag": "/Date(1436172326672)/"

                }

            }

        ]

    }

}
```

# CI Configuration

The iFlow is executed periodically to fetch the Account Team Members from C4C.
Then the mapping to the OData service is done and the data needs to be replicated to SMC.

![](/legacyfs/online/storage/blog_attachments/2023/07/cpi_iflow.png)

## Mapping

In the iFlow, the mapping of the C4C OData service to the SMC service ...