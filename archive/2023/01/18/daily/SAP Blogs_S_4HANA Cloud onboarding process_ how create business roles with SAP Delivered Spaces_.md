---
title: S/4HANA Cloud onboarding process: how create business roles with SAP Delivered Spaces?
url: https://blogs.sap.com/2023/01/17/s-4hana-cloud-onboarding-process-how-create-business-roles-with-sap-delivered-spaces/
source: SAP Blogs
date: 2023-01-18
fetch_date: 2025-10-04T04:08:49.786451
---

# S/4HANA Cloud onboarding process: how create business roles with SAP Delivered Spaces?

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Enterprise Resource Planning](/t5/enterprise-resource-planning/ct-p/erp)
* [ERP Blog Posts by SAP](/t5/enterprise-resource-planning-blog-posts-by-sap/bg-p/erp-blog-sap)
* S/4HANA Cloud onboarding process: how create busin...

Enterprise Resource Planning Blog Posts by SAP

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/erp-blog-sap/article-id/53324&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [S/4HANA Cloud onboarding process: how create business roles with SAP Delivered Spaces?](/t5/enterprise-resource-planning-blog-posts-by-sap/s-4hana-cloud-onboarding-process-how-create-business-roles-with-sap/ba-p/13569930)

![wterceiro](https://avatars.profile.sap.com/4/1/id413a753f5dfd09d367b1937f5d78ef46010cf63d6910597dfce0c9575c5f2b24_small.jpeg "wterceiro")

![Product and Topic Expert](/html/@138D6F765B60D7FC0168643DE27D8A68/rank_icons/sap-logo-small-14px.png "Product and Topic Expert")
[wterceiro](https://community.sap.com/t5/user/viewprofilepage/user-id/10642)

Product and Topic Expert

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=erp-blog-sap&message.id=53324)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/erp-blog-sap/article-id/53324)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13569930)

‎2023 Jan 17
8:57 PM

[12
Kudos](/t5/kudos/messagepage/board-id/erp-blog-sap/message-id/53324/tab/all-users "Click here to see who gave kudos to this post.")

2,463

* SAP Managed Tags
* [SAP Fiori for SAP S/4HANA](https://community.sap.com/t5/c-khhcw49343/SAP%2520Fiori%2520for%2520SAP%2520S%252F4HANA/pd-p/73555000100800000131)
* [SAP Fiori Launchpad](https://community.sap.com/t5/c-khhcw49343/SAP%2520Fiori%2520Launchpad/pd-p/538710751289542466232554247536294)
* [SAP S/4HANA Cloud Public Edition](https://community.sap.com/t5/c-khhcw49343/SAP%2520S%252F4HANA%2520Cloud%2520Public%2520Edition/pd-p/08e2a51b-1ce5-4367-8b33-4ae7e8b702e0)

* [SAP S/4HANA Cloud Public Edition

  SAP S/4HANA Cloud](/t5/c-khhcw49343/SAP%2BS%25252F4HANA%2BCloud%2BPublic%2BEdition/pd-p/08e2a51b-1ce5-4367-8b33-4ae7e8b702e0)
* [SAP Fiori Launchpad

  SAP Fiori](/t5/c-khhcw49343/SAP%2BFiori%2BLaunchpad/pd-p/538710751289542466232554247536294)
* [SAP Fiori for SAP S/4HANA

  SAP Fiori](/t5/c-khhcw49343/SAP%2BFiori%2Bfor%2BSAP%2BS%25252F4HANA/pd-p/73555000100800000131)

View products (3)

Spaces and Page are the UI experience introduced with Fiori 3.0 and they are available in the S/4HANA Cloud since the release 2005 and in the S/4HANA since version 2020.

Now, with the new Horizon theme available in the S/4HANA Cloud, Spaces and Pages have a important role in these new Fiori UI visualization. Mainly in the "My Home" view in the Horizon Theme:

![](/legacyfs/online/storage/blog_attachments/2023/01/2023-01-14_15-02-48.jpg)

Together with Horizon Theme, Spaces and Pages increase the performance in the Fiori Screens and user navigability between the functions available for the user based on the roles assigned to him/her.

If you want to know more about Spaces and Pages, I suggest you to see this interesting blog wrote by Sylvya Strack : <https://blogs.sap.com/2020/07/> 29/structure-the-sap-fiori-launchpad-layout-with-spaces/

In this blog, she explain very well, how the Fiori applications is segregated in Spaces, Pages and Sections:

![](/legacyfs/online/storage/blog_attachments/2023/01/2023-01-14_13-53-59.jpg)

The Fiori Applications are grouped in Sections, that are grouped in Pages that finally are grouped in  Spaces. The Spaces are assigned to Business Roles.

The Fiori applications are included in the Catalogs that usually are delivered in the Scope Items available in the Best Practices.

In the case of S/4HANA Cloud, these Catalogs are maintained and delivered by SAP and installed during the Scope definition phase through the CBC (Central Business Configuration).

In S/4HANA on-premise or S/4HANA Cloud Private Edition, beside the Standard Catalogs delivered by SAP through Best Practice Implementation (in a Greenfield Scenario), is possible to create and customize Fiori Catalog. See this blog about that : [https://blogs.sap.com/2020/09/11/sap-fiori-for-sap-s-4hana-overview-of-tools-for-maintaining-custom-...](https://blogs.sap.com/2020/09/11/sap-fiori-for-sap-s-4hana-overview-of-tools-for-maintaining-custom-launchpad-content-and-layout/)

In S/4HANA Cloud, remember that no Role and Catalog will be available until the Scope and Organizational Structure are activated in the Deployment Tenant in the CBC :

![](/legacyfs/online/storage/blog_attachments/2023/01/2023-01-10_13-01-23-1.jpg)

Once the CBC Workspace Project is deployed in the S/4HANA Cloud Tenant, the next Step is create Role for the users in the Tenant System.

Before to create the Roles, one important step is configure the Space and Page feature in the Tenant.

To do that, you need to verify if the Administrator role is assigned to Administrator user created for you by the SAP operation team. Also verify if the Administrator Role already have the Catalog "SAP\_CORE\_BC\_UI\_FLD".

This catalog will allow you to use the Fiori apps called "Manage Launchpad Pages" and "Manage Launchpad Spaces" to create Custom Space and Pages, as well as configure Spaces for the Roles.

To verify if this Catalog is configured for the Administrator Role, use the Fiori app "Maintain Business Role":

![](/legacyfs/online/storage/blog_attachments/2023/01/2023-01-15_15-11-25.jpg)

![](/legacyfs/online/storage/blog_attachments/2023/01/2023-01-15_18-41-50.jpg)

In this Fiori app, search for the "Administrator" role and verify if the catalog "SAP\_CORE\_BC\_UI\_FLD" is assigned to it. If it is not assigned, edit the Role and assign the catalog to it.

After that, configure the system allowing the users works with Space and Pages. You do that using  the app "Manage Launchpad Settings". In this App, enter in the "Edit" mode clicking in the "Edit" Button. Turn on the flags for Space options :

![](/legacyfs/online/storage/blog_attachments/2023/01/2023-01-15_18-59-57.jpg)

Once done, press save.

As next step, log in the system as Administrator and create the Roles for this Tenant.

Remember that the S/4HANA Cloud Tenant, after CBC Scope activation, only Administrator role will be available in the System. Is part of the S/4HANA Cloud on boarding process to create the remaining roles and assign them to the users.

To do that, you need to enter in the Fiori app "Business Role Template". This app will show you all SAP Standard Roles delivered and assigned to this Tenant based on the Activation done through CBC. Click in all Roles and click in the button "Create Business Role" :

![](/legacyfs/online/storage/blog_attachments/2023/01/2023-01-13_20-20-32.jpg)

Next, the system will show you a popup with options to create the Roles massively  :

![](/legacyfs/online/storage/blog_attachments/2023/01/2023-02-15_12-47-51.jpg)

Now in the S/4HANA Cloud 2302, we have another feature called "Option for Spaces".

This popup bring us some important options :

* Option for Spaces :

  + ***Do Not Use Spaces***: in the case if this Business Role won't use Spaces and Pages.

  + ***Create and Assign Spaces Based on SAP-Delivered Spaces*** : this option create a custom Spaces based on the SAP-Delivered Space. If in the future, for a new release , if n...