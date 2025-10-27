---
title: Integrate SAP Cloud Identity Provisioning Service with SAP Build Work Zone, standard edition for federation of business content
url: https://blogs.sap.com/2023/05/26/integrate-sap-cloud-identity-provisioning-service-with-sap-build-work-zone-standard-edition-for-federation-of-business-content/
source: SAP Blogs
date: 2023-05-27
fetch_date: 2025-10-04T11:39:33.282710
---

# Integrate SAP Cloud Identity Provisioning Service with SAP Build Work Zone, standard edition for federation of business content

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Technology](/t5/technology/ct-p/technology)
* [Technology Blog Posts by SAP](/t5/technology-blog-posts-by-sap/bg-p/technology-blog-sap)
* Integrate SAP Cloud Identity Provisioning Service ...

Technology Blog Posts by SAP

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/technology-blog-sap/article-id/163297&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [Integrate SAP Cloud Identity Provisioning Service with SAP Build Work Zone, standard edition for federation of business content](/t5/technology-blog-posts-by-sap/integrate-sap-cloud-identity-provisioning-service-with-sap-build-work-zone/ba-p/13566691)

![harjeetjudge](https://avatars.profile.sap.com/5/a/id5a542fc0521696be11cdefe87b02c1bb6510a5cc86ceee9a8a357cd3c4191122_small.jpeg "harjeetjudge")

![Product and Topic Expert](/html/@138D6F765B60D7FC0168643DE27D8A68/rank_icons/sap-logo-small-14px.png "Product and Topic Expert")
[harjeetjudge](https://community.sap.com/t5/user/viewprofilepage/user-id/107963)

Product and Topic Expert

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=technology-blog-sap&message.id=163297)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/technology-blog-sap/article-id/163297)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13566691)

‎2023 May 26
10:23 PM

[9
Kudos](/t5/kudos/messagepage/board-id/technology-blog-sap/message-id/163297/tab/all-users "Click here to see who gave kudos to this post.")

8,854

* SAP Managed Tags
* [SAP Cloud Identity Services](https://community.sap.com/t5/c-khhcw49343/SAP%2520Cloud%2520Identity%2520Services/pd-p/67837800100800007337)
* [SAP Build Work Zone, standard edition](https://community.sap.com/t5/c-khhcw49343/SAP%2520Build%2520Work%2520Zone%252C%2520standard%2520edition/pd-p/73554900100800003081)

* [SAP Cloud Identity Services

  SAP Business Technology Platform](/t5/c-khhcw49343/SAP%2BCloud%2BIdentity%2BServices/pd-p/67837800100800007337)
* [SAP Build Work Zone, standard edition

  Software Product](/t5/c-khhcw49343/SAP%2BBuild%2BWork%2BZone%25252C%2Bstandard%2Bedition/pd-p/73554900100800003081)

View products (2)

You may have seen an option in SAP Build Work Zone, standard edition to connect Work Zone to SAP Cloud Identity Provisioning Service (IPS).  Did you ever wonder what this option was for and how it can be used when federating content from remote content providers into SAP Build Work Zone, standard edition?

![](/legacyfs/online/storage/blog_attachments/2023/05/1-95.png)

When you click the Connect button it does couple things:

1. It will provision an SAP Cloud Identity Provisioning tenant if you don't already have one.

2. Add target connectors in SAP Cloud Identity Provisioning Service to allow provisioning to SAP Build Work Zone standard edition.

Clicking the **Connect** button should show a **Connected** status on the screen.

![](/legacyfs/online/storage/blog_attachments/2023/05/2-58.png)

If you see an error or are stuck in the connecting state, check to make sure prerequisites required for this integration are met.  The prerequisites are documented in the [help guide](https://help.sap.com/docs/build-work-zone-standard-edition/sap-build-work-zone-standard-edition/configure-integration-with-identity-provisioning-service?q=content%20provider).  Furthermore, it may still be possible to proceed even if the screen above shows an error message.  The main thing we require is access to SAP Cloud Identity Provisioning tenant that has SAP Build Work Zone, standard edition available as a target system for provisioning.  If either of these is not true for your case, log a support ticket under EP-WZ-PRV component.

![](/legacyfs/online/storage/blog_attachments/2023/05/11-23.png)

To see how this integration can be used we need to setup a remote content provider for SAP Build Work Zone, standard edition.  For this blog, I am using SAP BTP ABAP Environment as the content provider and setup the integration using the steps documented in [this](https://developers.sap.com/tutorials/abap-environment-lp-service-content-provider.html) tutorial.  When adding the content provider in Work Zone make sure "**Use the Identity Provisioning service to provision user authorizations"** option is enabled.  This is not covered in the tutorial but is required for the scenario I am covering in this blog.  Make note of the ID (eg. Tutorial) specified for your content provider as it's also required later on when setting up SAP Build Work Zone as a target system in SAP Cloud Identity Provisioning Service.

![](/legacyfs/online/storage/blog_attachments/2023/05/10-27.png)

In my SAP BTP ABAP environment, I've exposed a few business roles to the BTP environment.  For eg, the TRAINWORKZONE role is marked **Exposed to SAP BTP**.![](/legacyfs/online/storage/blog_attachments/2023/05/12-21.png)

The TRAINWORKZONE roles has access to **Communication Management** application.

![](/legacyfs/online/storage/blog_attachments/2023/05/16-15.png)

The exposed roles show up in SAP Build Work Zone standard edition and can be assigned to site to provide access to users.  As you can see in the screenshot, besides the TRAINWORKZONE role I've exposed few additional roles as well.  Each back-end role provides access to certain business apps to users that are assigned those roles in the back-end system.

![](/legacyfs/online/storage/blog_attachments/2023/05/13-22.png)

What you will notice is that these roles will not be visible as role collections in your SAP BTP subaccount so there won't be an option to assign them to users through the BTP Cockpit.  This is expected since we enabled the "**Use the Identity Provisioning service to provision user authorizations"** option when adding SAP BTP ABAP environment as a content provider in SAP Build Work Zone.  You may be wondering than **how do I control what applications users can see SAP Build Work Zone site?**

To accomplish this we will need to setup Identity Provisioning service to read users and their roles from SAP BTP ABAP environment and provision to SAP Build Work Zone Standard Edition.  This process will ensure that users that access the Work Zone site can only see applications that they are authorized to use in the BTP ABAP environment.

Let's look at the process to do just that.

**Prepare SAP BTP ABAP Environment for use with SAP Cloud Identity Provisioning Service**

1. Log into your SAP BTP ABAP Environment and search for **Maintain Communication Users** and access the application**.![](/legacyfs/online/storage/blog_attachments/2023/05/4-47.png)**

2. Click **New** and create a new communication user.  Specify a **User Name**, **Description,** and **Password**.  Click **Create.**

3. Access **Communication Systems.**

4. Click New and specify a **System ID** and **System Name**and click**Create.**

5. Specify a value for **Host Name**to match your IAS tenant hostname**.**For eg. xxxxxxx.accounts.ondemand.com

6. Click + under **Users for Inbound Communication**.

7. Select the Communication user created earlier and click **OK**.

8. Save your Communication System.

9. Access **Communication Arrangements.**

10. Click New and choose the value help icon to open up the list of available communication scenarios.

11. Search for **SAP\_COM\_0193**and select it from the list**.**This communication s...