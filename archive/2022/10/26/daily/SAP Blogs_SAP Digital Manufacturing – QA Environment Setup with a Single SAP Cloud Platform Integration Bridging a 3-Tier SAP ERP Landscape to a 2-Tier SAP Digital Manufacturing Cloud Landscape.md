---
title: SAP Digital Manufacturing – QA Environment Setup with a Single SAP Cloud Platform Integration Bridging a 3-Tier SAP ERP Landscape to a 2-Tier SAP Digital Manufacturing Cloud Landscape
url: https://blogs.sap.com/2022/10/25/sap-digital-manufacturing-qa-environment-setup-with-a-single-sap-cloud-platform-integration-bridging-a-3-tier-sap-erp-landscape-to-a-2-tier-sap-digital-manufacturing-cloud-landscape/
source: SAP Blogs
date: 2022-10-26
fetch_date: 2025-10-03T20:53:27.488164
---

# SAP Digital Manufacturing – QA Environment Setup with a Single SAP Cloud Platform Integration Bridging a 3-Tier SAP ERP Landscape to a 2-Tier SAP Digital Manufacturing Cloud Landscape

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Supply Chain Management](/t5/supply-chain-management/ct-p/scm)
* [SCM Blog Posts by SAP](/t5/supply-chain-management-blog-posts-by-sap/bg-p/scm-blog-sap)
* SAP Digital Manufacturing (DMC) – QA Environment S...

Supply Chain Management Blog Posts by SAP

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/scm-blog-sap/article-id/6129&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [SAP Digital Manufacturing (DMC) – QA Environment Setup with a Single SAP Cloud Platform Integration Bridging a 3-Tier SAP ERP Landscape to a 2-Tier SAP Digital Manufacturing Cloud Landscape](/t5/supply-chain-management-blog-posts-by-sap/sap-digital-manufacturing-dmc-qa-environment-setup-with-a-single-sap-cloud/ba-p/13553806)

![KatjaHuschle](https://avatars.profile.sap.com/a/6/ida62b986c7382bcfc39bf455599bda6089bf27dc1dc0c901b278ace94cb9124ac_small.jpeg "KatjaHuschle")

![Product and Topic Expert](/html/@138D6F765B60D7FC0168643DE27D8A68/rank_icons/sap-logo-small-14px.png "Product and Topic Expert")
[KatjaHuschle](https://community.sap.com/t5/user/viewprofilepage/user-id/147705)

Product and Topic Expert

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=scm-blog-sap&message.id=6129)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/scm-blog-sap/article-id/6129)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13553806)

‎2022 Oct 25
9:44 PM

[12
Kudos](/t5/kudos/messagepage/board-id/scm-blog-sap/message-id/6129/tab/all-users "Click here to see who gave kudos to this post.")

4,813

* SAP Managed Tags
* [SAP Digital Manufacturing](https://community.sap.com/t5/c-khhcw49343/SAP%2520Digital%2520Manufacturing/pd-p/73555000100800001492)

* [SAP Digital Manufacturing

  SAP Digital Manufacturing](/t5/c-khhcw49343/SAP%2BDigital%2BManufacturing/pd-p/73555000100800001492)

View products (1)

In this blog, I would like to summarize and share the learnings of my colleagues Felix Stingel and Tobias Spaegele who have set up this type of landscape in multiple customer projects using standard content provided by SAP Digital Manufacturing Cloud for SAP Cloud Integration.

So, the applause is due to them ![:smiling_face_with_smiling_eyes:](/html/@7A6CB440EDFA84191C7C515B95E65344/emoticons/1f60a.png ":smiling_face_with_smiling_eyes:")

# Business Context

Depending on the role of your organization (customer or partner), the license purchased, and the purpose of the subscription, different entitlements (SaaS (Software as a Service) applications) for SAP Digital Manufacturing Cloud are available.

By default, each customer is eligible to subscribe to two tenants: one for production and one for testing (quality).
That means that for **SAP Digital Manufacturing Cloud we foresee a 2-tier landscap**e:

**Quality (Q) - Production (P)**

Most customers, however, have a **3-tier landscape for their SAP ERP on-premise systems**. In these systems, plants are configured with the same plant identifier, which is possible as they are different systems.

For instance, ***Plant 7000*** exists in all three systems:

**Development (DEV) – Quality (Q) – Production (P)**

In many implementation projects, the question is how to design the solution landscape. The aim is to preserve the 3-tier ERP landscape without changing the plant identifiers, as the plant identifiers are already used in a wider context. Instead, the aim is to match the ERP landscape to the 2-tier SAP Digital Manufacturing Cloud landscape that only allows unique plant identifiers in an SAP Digital Manufacturing Cloud tenant.

# Integration of SAP Digital Manufacturing Cloud with SAP S/4HANA or SAP ERP - short recap

The technical integration between SAP Digital Manufacturing Cloud and SAP S/4HANA or SAP ERP is achieved using SAP Cloud Integration (CPI) and Cloud Connector (CC) as illustrated below.
I will not describe the steps needed to enable the integration in this blog. For more information, you can refer to the detailed description in the [Integration Guide](https://help.sap.com/docs/SAP_DIGITAL_MANUFACTURING_CLOUD/c86ca4026fae4cb3ba66ed751866175b/9895ed8f0a8e41828418937d0a43d38b.html) on the SAP Help Portal.

In the next chapter, I will simply highlight additional steps needed to be performed to achieve mapping between systems and plants.

# Target Landscape

The diagram below illustrates the target solution landscape. The three-tier SAP ERP system is integrated with the two-tier SAP Digital Manufacturing Cloud environment via SAP CPI.

To facilitate this integration, CPI artifacts are provided to enable the mapping of plants. Additional information is available in the [Integration Guide](https://help.sap.com/docs/SAP_DIGITAL_MANUFACTURING_CLOUD/c86ca4026fae4cb3ba66ed751866175b/9895ed8f0a8e41828418937d0a43d38b.html) on the SAP Help Portal, under the section Mapping Plants (Plant Conversion).

For details regarding any known limitations, please refer to the [SAP Digital Manufacturing: Restrictions and Limitations Note](https://me.sap.com/notes/3379404)

In the example below, only one instance of SAP CPI is used for the DEV and Q systems.

![](/legacyfs/online/storage/blog_attachments/2022/10/Target-Landscape.png)Example Target Landscape

# **Set up procedure**

### Unique Destination

For each on-premise system, you need to set up a unique destination in your SAP CPI subaccount. You can use one Cloud Connector to integrate multiple on-premise systems with the cloud.

### Define Plant in SAP Digital Manufacturing Cloud

Define a unique plant name that you want to use in SAP Digital Manufacturing Cloud. Configure the plant including the required integration settings such as the ***ERP Destination*** using the [Manage Plants](https://help.sap.com/docs/SAP_DIGITAL_MANUFACTURING_CLOUD/97c9e9b9fac74be2a023638cd1700b46/3ed7eb36b33f41ae8b6e42c2e1dc37bf.html) app in SAP Digital Manufacturing Cloud.![](/legacyfs/online/storage/blog_attachments/2022/10/managePlant-1.png)

### Enable ***Plant Conversion*** in SAP CPI

Prerequisite: You have downloaded the SAP S/4HANA Integration with SAP Digital Manufacturing Cloud CPI content package. For more information, see [SAP HELP](https://help.sap.com/docs/SAP_DIGITAL_MANUFACTURING_CLOUD/c86ca4026fae4cb3ba66ed751866175b/53eae9c442d24864ae517ab96624a85b.html).

1. Go to your SAP CPI application.
2. Choose ***Build and Develop Integration Content.*** Select the *SAP S/4HANA Integration with SAP Digital Manufacturing Cloud*
3. Search for *Initial Parameters*
4. Under ***Actions*** choose ***Configure***.![CPI_EnablePlantConversion-3.png](/t5/image/serverpage/image-id/313198iD299579E36F5F66A/image-size/medium?v=v2&px=400 "CPI_EnablePlantConversion-3.png")
5. Set ***ENABLE\_PLANT\_CONVERSION*** to *****TRUE*****![](/legacyfs/online/storage/blog_attachments/2022/10/CPI_EnablePlantConversion-2-2.png)
6. Save and deploy your changes.

### Configure plant value mapping in SAP CPI.

1. Go to your SAP CPI application.
2. Choose ***Build and Develop Integration Content.*** Select the *SAP S/4HANA Integration with SAP Digital Manufacturing Cloud*
3. Search for **Plant Value Mapping** ![PlantValueMapping.png](/t5/image/serverpage/image-id/313201iF79A53D11DB33885/image-size/medium?v=v2&px=400 "PlantValueMapping.png")
4. Under ***Actions*** choose ***Configure***.
5. Create two entries for each ERP system ...