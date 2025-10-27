---
title: SAP Cloud Identity Access Governance (IAG) integration with Identity Authentication Service (IAS)
url: https://blogs.sap.com/2023/06/17/sap-cloud-identity-access-governance-iag-integration-with-identity-authentication-service-ias/
source: SAP Blogs
date: 2023-06-18
fetch_date: 2025-10-04T11:45:55.354825
---

# SAP Cloud Identity Access Governance (IAG) integration with Identity Authentication Service (IAS)

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Technology](/t5/technology/ct-p/technology)
* [Technology Blog Posts by SAP](/t5/technology-blog-posts-by-sap/bg-p/technology-blog-sap)
* SAP Cloud Identity Access Governance (IAG) integra...

Technology Blog Posts by SAP

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/technology-blog-sap/article-id/162140&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [SAP Cloud Identity Access Governance (IAG) integration with Identity Authentication Service (IAS)](/t5/technology-blog-posts-by-sap/sap-cloud-identity-access-governance-iag-integration-with-identity/ba-p/13562764)

![muthu_kumar](https://avatars.profile.sap.com/6/2/id62af18a1b83f7cee0ccd3d1b22c111a9002768e9f1f3cf2bb77facebaffd8b8f_small.jpeg "muthu_kumar")

![Product and Topic Expert](/html/@138D6F765B60D7FC0168643DE27D8A68/rank_icons/sap-logo-small-14px.png "Product and Topic Expert")
[muthu\_kumar](https://community.sap.com/t5/user/viewprofilepage/user-id/137199)

Product and Topic Expert

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=technology-blog-sap&message.id=162140)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/technology-blog-sap/article-id/162140)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13562764)

‎2023 Jun 17
3:48 PM

[4
Kudos](/t5/kudos/messagepage/board-id/technology-blog-sap/message-id/162140/tab/all-users "Click here to see who gave kudos to this post.")

17,837

* SAP Managed Tags
* [Governance, Risk, Compliance (GRC) and Cybersecurity](https://community.sap.com/t5/c-khhcw49343/Governance%252C%2520Risk%252C%2520Compliance%2520%28GRC%29%2520and%2520Cybersecurity/pd-p/237150e2-6555-4a16-b49e-e93dbf1891da)
* [SAP Access Control](https://community.sap.com/t5/c-khhcw49343/SAP%2520Access%2520Control/pd-p/01200615320800000796)
* [SAP Cloud Identity Access Governance](https://community.sap.com/t5/c-khhcw49343/SAP%2520Cloud%2520Identity%2520Access%2520Governance/pd-p/73555000100800000334)

* [SAP Access Control

  SAP Access Control](/t5/c-khhcw49343/SAP%2BAccess%2BControl/pd-p/01200615320800000796)
* [SAP Cloud Identity Access Governance

  SAP Cloud Identity Access Governance](/t5/c-khhcw49343/SAP%2BCloud%2BIdentity%2BAccess%2BGovernance/pd-p/73555000100800000334)
* [Governance, Risk, Compliance (GRC) and Cybersecurity

  Product Category](/t5/c-khhcw49343/Governance%25252C%2BRisk%25252C%2BCompliance%2B%252528GRC%252529%2Band%2BCybersecurity/pd-p/237150e2-6555-4a16-b49e-e93dbf1891da)

View products (3)

In this blog I will go through the steps to Integrate IAG with IAS.

SAP Cloud Identity Access Governance is a cloud-based service for creating self-service requests to applications for on-premise and cloud source applications and systems. By connecting to the SAP Cloud Identity Access Governance solution, it enables Identity Authentication users to initiate access requests, which are then provisioned to target applications.

**Prerequisite**: IAG Administrator, IAS & IPS administrator or knowledge in IAS & IPS is preferred to do this setup.

**Make sure you completed initial setup for IAG (IAS and IPS enablement) in IAG before following the below steps.**

## Process Overview

There are four overall steps to enable integration between Identity Authentication Service (SAP IAS) and the SAP Cloud Identity Access Governance solution and its services:

1. Connect Identity Provisioning with IAG

2. Create Proxy System for IAS In the IPS

3. Create an instance for Cloud Foundry in the IAG

4. Run the repository synch job to sync user data and provision access requests.

### 1.Connect Identity Provisioning with IAG

The following step is applicable for an Identity Provisioning bundle tenant was created or updated on the SAP Cloud Identity (SCI) platform for use with SAP Cloud Identity Access Governance.

The URL for Identity Provisioning is as follows:

<https://UNIQUEID.accounts.ondemand.com/ips>

1. Login to the IAS > User & Authorizations > Administrators > Add System user and provide the Access Proxy System API access. Note down the Client ID and Secret ( Once Secret is generated, you cannot retrieve or change it.)

2. Login to the IAG BTP Subaccount and create a destination with the name IPS\_PROXY as shown in the table below.

3. Enter the Properties listed in the table below for the destination. All properties must be entered. Some properties must be added as Additional Properties. **Copy the names of all properties as displayed. Property names and values are case sensitive.**

4. Check the Use default JDK truststore checkbox.

5. Save your entries.You can test the destination in the BTP Cockpit. However, the URL does not point to a valid API for Identity Provisioning, and shows green status, but HTTP 301 or similar.

|
 Name |
 IPS\_PROXY |

|
 Type |
 HTTP |

|
 Description |
 IPS Destination |

|
 URL |
 <https://<<YOUR_IPS_URL_BUT_WITHOUT_THE__ips>>>; (For example: <https://UNIQUEID.accounts.ondemand.com> |

|
 Proxy Type |
 Internet |

|
 Authentication |
 BasicAuthentication |

|
 User |
 <<CLIENT\_ID\_FROM\_STEP\_1\_ABOVE>> |

|
 Password |
 << SECRET\_FROM\_STEP 1\_ABOVE>> |

|
 Accept |
 application/scim+json |

|
 GROUPSURL |
 /Groups |

|
 serviceURL |
 /ipsproxy/service/api/v1/scim/ |

|
 USERSURL |
 /Users |

### 2.Create Proxy System for IAS In the IPS

Need to create a proxy system to enable Identity authentication service to connect with the IAG Subaccount. Before creating proxy system, please set up the technical user (of type System) in Identity Authentication and assign this user the necessary authorizations.

#### **2.1) How to create a technical user in IAS?**

* In SAP Cloud Identity Services admin console, navigate to Users & Authorizations > Administrators.

* Add an administrator user of type System and configure the basic authentication method for this user.

**Please note down the Client Id, Secret from the system user once it created.**

#### 2.2) Create**a Proxy System**

1. Open your Identity Provisioning Launchpad.

2. Copy the external system ID and use it to set up the Cloud Foundry instance in the Systems app.

3. Add a proxy system for IAS and choose Save. The Type should be Identity Authentication

   |
     |
     |

   |
    Type |
    Identity Authentication |

   |
    System Name |
    <Free text> |

   |
    Destination Name |
     |

   |
    Description |
    <Free text> |

4. Enter the Properties as shown in below table

   |
    Type=HTTP   Authentication=BasicAuthentication   ProxyType=Internet   URL= Specify the URL of the Identity Authentication tenant of your company.             For example: <https://mytenant.accounts.ondemand.com>   User=<<CLIENT\_ID\_FROM\_STEP\_2.1\_ABOVE>>   Password=<< SECRET\_FROM\_STEP 2.1\_ABOVE>>   ias.api.version=2    ias.support.patch.operation=true    ips.trace.failed.entity.content=false |

### 3.Create an instance for IAS in the IAG

1. Log into the SAP Cloud Identity Access Governance launchpad and open the Application app.

2. Create a system for IAS. For System Type, select IAS.

3. Enter the external system ID mentioned in step 2.2 in the section Create Proxy system and Save.

### 4.Run the repository synch job to sync user data and provision access requests.

In the SAP Cloud Identity Access Governance launchpad, open the Job Scheduler app. In the Job Category dr...