---
title: Things to consider  –  Migration to SAP Commerce Cloud 2211
url: https://blogs.sap.com/2023/02/17/things-to-consider-migration-to-sap-commerce-cloud-2211/
source: SAP Blogs
date: 2023-02-18
fetch_date: 2025-10-04T07:21:59.603878
---

# Things to consider  –  Migration to SAP Commerce Cloud 2211

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [CRM and Customer Experience](/t5/crm-and-customer-experience/ct-p/crm)
* [CRM and CX Blog Posts by Members](/t5/crm-and-cx-blog-posts-by-members/bg-p/crm-blog-members)
* Things to consider - Migration to SAP Commerce C...

CRM and CX Blog Posts by Members

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/crm-blog-members/article-id/6231&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [Things to consider - Migration to SAP Commerce Cloud 2211](/t5/crm-and-cx-blog-posts-by-members/things-to-consider-migration-to-sap-commerce-cloud-2211/ba-p/13549871)

![phy_abhijit](https://avatars.profile.sap.com/f/8/idf8e7562738b4ed987363196fe9c80711ddb1ad8698eef427f09d552efd858572_small.jpeg "phy_abhijit")

[phy\_abhijit](https://community.sap.com/t5/user/viewprofilepage/user-id/737412)

Explorer

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=crm-blog-members&message.id=6231)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/crm-blog-members/article-id/6231)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13549871)

‎2023 Feb 17
6:32 PM

[12
Kudos](/t5/kudos/messagepage/board-id/crm-blog-members/message-id/6231/tab/all-users "Click here to see who gave kudos to this post.")

10,803

* SAP Managed Tags
* [SAP Commerce](https://community.sap.com/t5/c-khhcw49343/SAP%2520Commerce/pd-p/67837800100800007216)
* [SAP Commerce Cloud](https://community.sap.com/t5/c-khhcw49343/SAP%2520Commerce%2520Cloud/pd-p/73555000100800001224)
* [PORTAL Migration and Upgrade](https://community.sap.com/t5/c-khhcw49343/PORTAL%2520Migration%2520and%2520Upgrade/pd-p/439208526315459272242491809978043)

* [SAP Commerce

  SAP Commerce](/t5/c-khhcw49343/SAP%2BCommerce/pd-p/67837800100800007216)
* [PORTAL Migration and Upgrade

  Software Product Function](/t5/c-khhcw49343/PORTAL%2BMigration%2Band%2BUpgrade/pd-p/439208526315459272242491809978043)
* [SAP Commerce Cloud

  Software Product](/t5/c-khhcw49343/SAP%2BCommerce%2BCloud/pd-p/73555000100800001224)

View products (3)

SAP Commerce Cloud 2211 got release November,2022 and still under Continuous innovation. There are already patches on (so far 3rd patch 2211.3 as of today). I would like to share simple steps to migrate to Commerce 2211 with our experience of migration and challenges we faced.

The very first thing to note that Commerce cloud 2211 version is cloud only version. If there is any customer in On-prem with prior version but would like to upgrade commerce to 2211, the commerce cloud needs to be upgraded to Cloud first, then only the commerce engine could be upgraded to 2211 version else, customer can upgrade till the last On-prem version 2205 (till date announced by SAP) considering the EMM is May 31, 2024. You can refer the [Supported releases here](https://help.sap.com/docs/SAP_COMMERCE_CLOUD_PUBLIC_CLOUD/12be4ac419604b01aabb1adeb2c4c8a2/1c6c687ad0ed4964bb43d409818d23a2.html?version=latest).

**You can find all defined steps to upgrade Commerce cloud platform from 2205 to 2211 [here](https://help.sap.com/docs/SAP_COMMERCE_CLOUD_PUBLIC_CLOUD/bbcd2978537e4ae298479557c0b8fdbd/71ce7fccfb3242c09690e8000e6e681f.html?version=latest) [at SAP support portal](https://help.sap.com/docs/SAP_COMMERCE_CLOUD_PUBLIC_CLOUD/bbcd2978537e4ae298479557c0b8fdbd/71ce7fccfb3242c09690e8000e6e681f.html?version=latest)**

**A. Software required / Software compatibility**:

* Search Engines:

|
 SAP Commerce Cloud Version |
 Current Update Releases |
 Supported Solr Versions |

|
 2211 |
 2211.2 |
 8.11.2 |

|
 2211.1 |
 8.11.2 |

|
 2211.0 |
 8.11.2 |

\*SAP Commerce Cloud supports the latest patch version of SAP Commerce cloud and the Solr version that is shipped with it. But you want to be with specific solr version, you can do the same through manifest.json file

* Node.js : SAP Commerce Cloud supports 14, 16 & 18 Node.js versions

* SAP Commerce Cloud 2211 requires JDK 17 or later. It is fully compatible with [SAP Machine 17](https://sap.github.io/SapMachine/)

**B. tomcat.generaloptions:**

We often update tomcat general properties, if you have prior version tomcat.general properties overridden in your local.properties, please make sure, you get the same OOTB from platform/project.properties and append as needed. There was a large drop in JDK 14 with the removal of the Concurrent Mark Sweep (CMS) garbage collector. All those CMS collectors\* (CMSInitiatingOccupancyFraction, CMSClassUnloadingEnabled, UseCMSInitiatingOccupancyOnly etc.) was deprecated in JDK 9 and was removed in JDK 14. As SAP Commerce cloud is on JDK 17, you need to remove all of those from your local.properties on tomcat.generaloptions.

  It’s recommended to get the tomcat.generaloptions property details as OOTB under platform/project.properties and append properties as needed \*\*.

\*You can find those CMS collector removal details

\*\* You can find more details on garbage collection [here](https://help.sap.com/docs/SAP_COMMERCE_CLOUD_PUBLIC_CLOUD/51e73d14aedc487384e4518b60a1f5fd/13b02a10be4f406f960280eafddbdcff.html?version=latest)

**C. OpenAPI 3.0 upgrade**:

SAP Commerce cloud 2211 supports OpenAPI 3.0 and you need to consider compatibilities associated with it. You need to migrate your webservices and occ/occaddon extensions. Please be remembered, you need to update each webservice and occ services considering OpenApi changes as well as swagger-annotations to newer version 2.2.2\*\*\*.

\*\*\*You can find all those OpenApi, swagger  [compatible annotations here](https://help.sap.com/docs/SAP_COMMERCE_CLOUD_PUBLIC_CLOUD/bbcd2978537e4ae298479557c0b8fdbd/277f145325a4409b975f6e2af91b7401.html?version=latest)

**D. XML Schema validator issue accessExternalSchema' is not recognized**

Property '<http://javax.xml.XMLConstants/property/accessExternalSchema>' is not recognized

You can find a KBA on SAP site on the same at [3292249](https://me.sap.com/notes/0003292249) but it shares areas to look to resolve the issue.

The issue occurs due to external jar( xerces) dependency. The **accessExternalSchema** is defined in JAXP 1.5  but Apache xerces does not support it anymore.

We did the follow things to resolve the issue

1. Removeall direct and indirect dependencies on the Xerces library**(**xerces\*\*.jar) dependency so that default Xerces implementation bundled with the JRE 17 will be in effect

2. Modifyfew codes base as we were using xerces for Base64 encrytion and decryption for SSO

\*There is another option to set system properties javax.xml.parsers.DocumentBuilderFactory to use the internal JAXP DocumentBuilder but we couldn’t make it well

**E. Missing CatalogVersion \_boconfig': CatalogVersion with catalogId '\_boconfig' and version 'hidden' not found**

You can resolve this issue by running following.

ant importImpex -Dresource=(Absolute path like C:\\*\*\\*\*\}\hybris\bin\modules\backoffice-framework\backoffice\resources\impex\essentialdataMediaCatalog.impex

Updated on 10th April, 2023

**F: Disable console log in local for Slf4jAuditableActionHandler DB\_AUDIT**

I would like to share another important point on local set up. You might see there will be lot of log regarding "**Slf4jAuditableActionHandler DB\_AUDIT**" and it may cause issue while debugging your local changes as this log will be all over the console.

![](/legacyfs/online/storage/...