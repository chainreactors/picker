---
title: On-Prem Data to Cloud Data
url: https://blogs.sap.com/2022/11/06/on-prem-data-to-cloud-data/
source: SAP Blogs
date: 2022-11-07
fetch_date: 2025-10-03T21:52:09.928423
---

# On-Prem Data to Cloud Data

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [CRM and Customer Experience](/t5/crm-and-customer-experience/ct-p/crm)
* [CRM and CX Blog Posts by Members](/t5/crm-and-cx-blog-posts-by-members/bg-p/crm-blog-members)
* On-Prem Data to Cloud Data

CRM and CX Blog Posts by Members

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/crm-blog-members/article-id/6107&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [On-Prem Data to Cloud Data](/t5/crm-and-cx-blog-posts-by-members/on-prem-data-to-cloud-data/ba-p/13528421)

![vinod_singh](https://avatars.profile.sap.com/6/c/id6c52d54f9ccf9c25612bcab50a481487d0f050a3c502d49f1095e7641aa27cde_small.jpeg "vinod_singh")

[vinod\_singh](https://community.sap.com/t5/user/viewprofilepage/user-id/13924)

Participant

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=crm-blog-members&message.id=6107)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/crm-blog-members/article-id/6107)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13528421)

‎2022 Nov 06
8:15 PM

[7
Kudos](/t5/kudos/messagepage/board-id/crm-blog-members/message-id/6107/tab/all-users "Click here to see who gave kudos to this post.")

3,660

* SAP Managed Tags
* [SAP BTP, Kyma runtime](https://community.sap.com/t5/c-khhcw49343/SAP%2520BTP%252C%2520Kyma%2520runtime/pd-p/73554900100800003012)
* [Cloud Integration](https://community.sap.com/t5/c-khhcw49343/Cloud%2520Integration/pd-p/67837800100800006801)
* [SAP Commerce](https://community.sap.com/t5/c-khhcw49343/SAP%2520Commerce/pd-p/67837800100800007216)
* [SAP Commerce Cloud](https://community.sap.com/t5/c-khhcw49343/SAP%2520Commerce%2520Cloud/pd-p/73555000100800001224)
* [Cloud](https://community.sap.com/t5/c-khhcw49343/Cloud/pd-p/431932400353955532628433796433200)

* [SAP Commerce

  SAP Commerce](/t5/c-khhcw49343/SAP%2BCommerce/pd-p/67837800100800007216)
* [Cloud Integration

  SAP Integration Suite](/t5/c-khhcw49343/Cloud%2BIntegration/pd-p/67837800100800006801)
* [Cloud

  Topic](/t5/c-khhcw49343/Cloud/pd-p/431932400353955532628433796433200)
* [SAP Commerce Cloud

  Software Product](/t5/c-khhcw49343/SAP%2BCommerce%2BCloud/pd-p/73555000100800001224)
* [SAP BTP, Kyma runtime

  SAP Business Technology Platform](/t5/c-khhcw49343/SAP%2BBTP%25252C%2BKyma%2Bruntime/pd-p/73554900100800003012)

View products (5)

## Introduction

This blog would help you as an Architect to speed-up the migration process for your On-Prem / SAP Commerce from CCv1 (SAP Commerce Cloud on SAP Infrastructure) to CCv2 (SAP Commerce Cloud on Microsoft Azure Cloud). We will also see the difference between CCv1, On-Prem, and CCv2 and then look into detailed solutions for Data Compatibility and Data migration which is always the major concern of Architects and Project Management which will be the focus of this blog.

## Back to Basics

![](/legacyfs/online/storage/blog_attachments/2022/11/Screenshot-2022-11-06-at-15.12.08.png)

### CCV1:

This is also known as SAP Commerce cloud on SAP Infra since the Infrastructure and Data centers on which the environment runs are from SAP. Customers use to receive a detailed architectural diagram of the server configuration for each environment. Any deployment on STG and PROD required a service request ticket to SAP. The DB used here was HANA DB. We also use Splunk in many cases to check the server logs from QA/STG and PROD. The process to deploy any fix or troubleshooting issues was very complicated and had to go through a very slow process.

### On-Prem:

This is purely hosted on the customer location and managed by the customer alone without much involvement from SAP. The customer has their own choice to select any cloud providers (such as GCP / AWS ). The only support that SAP usually provides is those which is related to the Commerce Framework/Solution. The customer has the choice to select their own DB such as HANA, Oracle, or MySQL.

### CCv2:

This is based on a public cloud which is from Microsoft Azure. DB in the case of CCv2 is Microsoft Azure SQL Database which is provided from Azure Cloud. Here we use Kibana for checking server logs and Dynatrace for monitoring.

## Data Migration Architecture

![](/legacyfs/online/storage/blog_attachments/2022/11/SAP-Service.png)

Source : [https://www.sap.com/cxworks/article/2589632458/migrating\_to\_sap\_commerce\_cloud\_data\_and\_media\_migrat...](https://www.sap.com/cxworks/article/2589632458/migrating_to_sap_commerce_cloud_data_and_media_migration)

![](/legacyfs/online/storage/blog_attachments/2022/11/Self-Service-.png)

Source: [https://www.sap.com/cxworks/article/2589632458/migrating\_to\_sap\_commerce\_cloud\_data\_and\_media\_migrat...](https://www.sap.com/cxworks/article/2589632458/migrating_to_sap_commerce_cloud_data_and_media_migration)

##

## Data Model Compatibility for CCv2

Before you migrate it's very important that you check that your data model has been declared with Microsoft Azure SQL database-specific mapping.

|
 **Data Type** |
 **Database Mapping** | | | |

|
 **hsqldb** |
 **mysql** |
 **sap** |
 **sqlserver** |

|
 java.lang.String |
 VARCHAR(255) |
 varchar(255) |
 nvarchar(255) |
 nvarchar(255) |

|
 String |
 VARCHAR(255) |
 varchar(255) |
 nvarchar(255) |
 nvarchar(255) |

|
 java.lang.Float |
 float |
 float(20,5) |
 decimal(20,5) |
 float |

|
 java.lang.Double |
 double |
 double |
 decimal(30,8) |
 float |

|
 java.lang.Byte |
 smallint |
 smallint |
 smallint |
 integer |

|
 java.lang.Character |
 smallint |
 smallint |
 smallint |
 char(4) |

|
 java.lang.Short |
 smallint |
 integer |
 integer |
 integer |

|
 java.lang.Boolean |
 tinyint |
 tinyint(1) |
 decimal(1,0) |
 tinyint |

|
 java.lang.Long |
 bigint |
 bigint |
 bigint |
 bigint |

|
 java.lang.Integer |
 int |
 integer |
 bigint |
 integer |

|
 float |
 float default 0 |
 float(20,5)  DEFAULT 0 |
 decimal(20,5)  DEFAULT 0 |
 float default 0 |

|
 double |
 double default  0 |
 double DEFAULT 0 |
 decimal(30,8)  DEFAULT 0 |
 float default 0 |

|
 byte |
 smallint default  0 |
 smallint DEFAULT 0 |
 integer  DEFAULT 0 |
 integer default 0 |

|
 char |
 smallint default  0 |
 smallint DEFAULT 0 |
 integer DEFAULT '' |
 char(4) default '' |

|
 short |
 smallint default  0 |
 integer DEFAULT 0 |
 integer DEFAULT 0 |
 integer default 0 |

|
 boolean |
 tinyint default 0 |
 tinyint(1) DEFAULT  0 |
 decimal(1,0) DEFAULT  0 |
 tinyint default 0 |

|
 long |
 bigint default 0 |
 bigint DEFAULT 0 |
 bigint DEFAULT 0 |
 integer default 0 |

|
 int |
 int default 0 |
 integer DEFAULT 0 |
 bigint DEFAULT 0 |
 integer default 0 |

|
 java.util.Date |
 timestamp |
 datetime |
 timestamp |
 datetime2 |

|
 java.math.BigDecimal |
 decimal(30,8) |
 decimal(30,8) |
 decimal(30,8) |
 decimal(30,8) |

|
 java.io.Serializable |
 longvarbinary |
 longblob |
 blob |
 image |

|
 HYBRIS.LONG\_STRING |
 longvarchar |
 text |
 nvarchar(5000) |
 nvarchar(max) |

|
 HYBRIS.JSON |
 longvarchar |
 longtext |
 nclob |
 nvarchar(max) |

|
 HYBRIS.COMMA\_SEPARATED\_PKS |
 longvarchar |
 text |
 nvarchar(5000) |
 nvarchar(max) |

|
 HYBRIS.PK |
 BIGINT |
 bigint |
 bigint |
 bigint |

It's recommended that you also check the help page [Specifying a Deployment for Commerce Platform Types](https://help.sap.com/docs/SAP_COMMERCE/d0224eca81e249cb821f2cdf45a82ace/8c6254f086691014b095a08a61d1efed.html?locale=en-U...