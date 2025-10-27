---
title: [SAP BTP Onboarding Series] – Step-by-Step guide to activate your SAP Build Work Zone, Advanced Edition
url: https://blogs.sap.com/2023/01/02/sap-btp-onboarding-series-step-by-step-guide-to-activate-your-sap-build-work-zone-advanced-edition/
source: SAP Blogs
date: 2023-01-03
fetch_date: 2025-10-04T02:54:49.859389
---

# [SAP BTP Onboarding Series] – Step-by-Step guide to activate your SAP Build Work Zone, Advanced Edition

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Technology](/t5/technology/ct-p/technology)
* [Technology Blog Posts by SAP](/t5/technology-blog-posts-by-sap/bg-p/technology-blog-sap)
* [SAP BTP Onboarding Series] - Step-by-Step guide t...

Technology Blog Posts by SAP

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/technology-blog-sap/article-id/159509&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [[SAP BTP Onboarding Series] - Step-by-Step guide to activate your SAP Build Work Zone, Advanced Edition](/t5/technology-blog-posts-by-sap/sap-btp-onboarding-series-step-by-step-guide-to-activate-your-sap-build/ba-p/13555072)

![nageshcaparthy](https://avatars.profile.sap.com/b/1/idb1d57d2f98163d09352377bdfd277236518048e3408ee1e7a6c0b272ba218ffc_small.jpeg "nageshcaparthy")

![Product and Topic Expert](/html/@138D6F765B60D7FC0168643DE27D8A68/rank_icons/sap-logo-small-14px.png "Product and Topic Expert")
[nageshcaparthy](https://community.sap.com/t5/user/viewprofilepage/user-id/2099)

Product and Topic Expert

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=technology-blog-sap&message.id=159509)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/technology-blog-sap/article-id/159509)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13555072)

‎2023 Jan 02
2:23 PM

[32
Kudos](/t5/kudos/messagepage/board-id/technology-blog-sap/message-id/159509/tab/all-users "Click here to see who gave kudos to this post.")

38,705

* SAP Managed Tags
* [SAP Build Work Zone, advanced edition](https://community.sap.com/t5/c-khhcw49343/SAP%2520Build%2520Work%2520Zone%252C%2520advanced%2520edition/pd-p/73555000100800002781)
* [SAP Build Apps](https://community.sap.com/t5/c-khhcw49343/SAP%2520Build%2520Apps/pd-p/6cfd8176-04ae-4548-8f38-158456e1a47a)
* [SAP Business Technology Platform](https://community.sap.com/t5/c-khhcw49343/SAP%2520Business%2520Technology%2520Platform/pd-p/73555000100700000172)
* [Customer Onboarding Services](https://community.sap.com/t5/c-khhcw49343/Customer%2520Onboarding%2520Services/pd-p/e12c0b6a-edb1-4ea6-b2d5-19b365e41a61)

* [SAP Build Work Zone, advanced edition

  Software Product](/t5/c-khhcw49343/SAP%2BBuild%2BWork%2BZone%25252C%2Badvanced%2Bedition/pd-p/73555000100800002781)
* [SAP Build Apps

  Additional Software Product](/t5/c-khhcw49343/SAP%2BBuild%2BApps/pd-p/6cfd8176-04ae-4548-8f38-158456e1a47a)
* [SAP Business Technology Platform

  Software Product](/t5/c-khhcw49343/SAP%2BBusiness%2BTechnology%2BPlatform/pd-p/73555000100700000172)
* [Customer Onboarding Services

  Services and Support](/t5/c-khhcw49343/Customer%2BOnboarding%2BServices/pd-p/e12c0b6a-edb1-4ea6-b2d5-19b365e41a61)

View products (4)

This blog is a part of the [SAP BTP Customer Onboarding](https://support.sap.com/en/product/onboarding-resource-center/business-technology-platform.html) Series, and we aim to keep the onboarding series of blogs up to date with any changes in the product setup activities. We look forward to your feedback and continuous support to keep these onboarding documents updated.

With the new announcements from SAP TechEd on SAP Build Work Zone, we found it exciting to get our customers, IT Professionals, and line of business experts to easily build and design engaging business sites for your employees, partners, and customers to increase productivity. In short, SAP Build Work Zone offers the following benefits:

* Increase efficiency and productivity of individual users and teams working with SAP apps, processes & self-services

* Empower lines of business to easily build business sites (create content & publish information without IT)

* Boost people's engagement and establish interactive communities

* Foster active knowledge sharing across the enterprise

* Provide a great onboarding and learning experience

The benefits are huge, now the next question is how do you activate these services, and what prerequisites/services are required for you to get started?? Well, from the point of onboarding you to a new service, let us look at how to activate SAP Build Work Zone, advanced edition:

1. You are assigned the Global Admin Role in your SAP Business Technology Platform

2. Create a Sub-Account and Activate SAP Cloud Identity Service

3. Setup Trust between SAP Identity Service - Identity Authentication, and BTP Subaccount

4. Run the booster “SAP Build Work Zone Advanced Edition”

5. Post Booster Configuration

6. Run the configurator, pre-requisite Configure IAS and IPS

7. Common Issues/Troubleshooting

While we explain each of the points in detail, please pay close attention to the service configurations specifically on **Booster activation, IAS, & IPS Configurations, and Run Configurator** steps.

Caution: Scenarios not considered in this blog are, an existing JAM migration, and SAP SuccessFactors WorkZone setup.

Before we get started, here is the official documentation on the [SAP Build Work Zone setup](https://help.sap.com/docs/WZ/b03c84105ff74f809631e494bd612e83/5c0103b130de411fb2a4b5416e36d767.html). We understand the various needs of our customers, partner, and community and we will explore this in more detail including step-by-step instructions with screenshots & background information.

1. **You are assigned the Global Admin Role in your SAP Business Technology Platform**

As a part of the setup process, you need to have the **SAP BTP Global Administrator** role to perform the next task. In case you do not have a global admin role, please reach your internal team.

2. **Create a Sub-Account and, Activate SAP Cloud Identity Service**

In this blog, we are considering the setup with a new Global Account, and are therefore going to create a **New Sub-account** and activate the **SAP** **Cloud Identity Services**. In case you have an existing sub-account or an active SAP Cloud Identity Service you may skip the creating/activating steps (**a and b**).

**a.** Log in to the **SAP BTP Cockpit** to **create a new sub-account**, from the BTP Account Explorer page -> click on Create -> select Subaccount.

![](/legacyfs/online/storage/blog_attachments/2022/12/Image-1-3.png)

Image 1

Now enter the details to create your subaccount, as displayed below. While selecting your data center, you may select the one nearest to your location to avoid latency or you may pick and choose the data center where SAP Work Zone is supported, the table on the [SAP Help page](https://help.sap.com/docs/WZ/b03c84105ff74f809631e494bd612e83/9e78b62e8d2a4e1b928d85d22fe957a7.html) can help to clarify the implications of this selection. I have selected Europe Frankfurt in this demo and I have kept the subdomain with auto-populated value. In case you need to modify it, please do so now as it cannot be edited once the subaccount is created.

![](/legacyfs/online/storage/blog_attachments/2022/12/Image-2-2.png)

Image 2

The new subaccount is created. Since you have created the new subaccount, by default you will be assigned as the subaccount administrator. Click on the subaccount to open it.

![](/legacyfs/online/storage/blog_attachments/2022/12/Image-3-4.png)

Image 3

b. Now let us activate the **SAP Cloud Identity Service**, and as said before if you have an active SAP Cloud Identity service you may skip this activation step. For the purpose of this blog, I’m using a Cloud Identity Service that ha...