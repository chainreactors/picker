---
title: How to Mass Update Business Roles
url: https://blogs.sap.com/2023/07/05/how-to-mass-update-business-roles/
source: SAP Blogs
date: 2023-07-06
fetch_date: 2025-10-04T11:53:29.991358
---

# How to Mass Update Business Roles

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Enterprise Resource Planning](/t5/enterprise-resource-planning/ct-p/erp)
* [ERP Blog Posts by SAP](/t5/enterprise-resource-planning-blog-posts-by-sap/bg-p/erp-blog-sap)
* How to Mass Update Business Roles

Enterprise Resource Planning Blog Posts by SAP

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/erp-blog-sap/article-id/50826&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [How to Mass Update Business Roles](/t5/enterprise-resource-planning-blog-posts-by-sap/how-to-mass-update-business-roles/ba-p/13553396)

![Tayane](https://avatars.profile.sap.com/4/d/id4d2d58bc40b1d37b5ee1cb7b23f537eb72d39ac3b3946114f66c9b4b52cf47de_small.jpeg "Tayane")

![Product and Topic Expert](/html/@138D6F765B60D7FC0168643DE27D8A68/rank_icons/sap-logo-small-14px.png "Product and Topic Expert")
[Tayane](https://community.sap.com/t5/user/viewprofilepage/user-id/143549)

Product and Topic Expert

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=erp-blog-sap&message.id=50826)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/erp-blog-sap/article-id/50826)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13553396)

‎2023 Jul 05
7:43 PM

[4
Kudos](/t5/kudos/messagepage/board-id/erp-blog-sap/message-id/50826/tab/all-users "Click here to see who gave kudos to this post.")

5,867

* SAP Managed Tags
* [SAP S/4HANA Cloud Public Edition Human Resources](https://community.sap.com/t5/c-khhcw49343/SAP%2520S%252F4HANA%2520Cloud%2520Public%2520Edition%2520Human%2520Resources/pd-p/a8945cb2-dac7-490c-a6b6-7d8629f65668)
* [SAP Fiori Launchpad](https://community.sap.com/t5/c-khhcw49343/SAP%2520Fiori%2520Launchpad/pd-p/538710751289542466232554247536294)
* [SAP S/4HANA Cloud Public Edition](https://community.sap.com/t5/c-khhcw49343/SAP%2520S%252F4HANA%2520Cloud%2520Public%2520Edition/pd-p/08e2a51b-1ce5-4367-8b33-4ae7e8b702e0)

* [SAP S/4HANA Cloud Public Edition

  SAP S/4HANA Cloud](/t5/c-khhcw49343/SAP%2BS%25252F4HANA%2BCloud%2BPublic%2BEdition/pd-p/08e2a51b-1ce5-4367-8b33-4ae7e8b702e0)
* [SAP Fiori Launchpad

  SAP Fiori](/t5/c-khhcw49343/SAP%2BFiori%2BLaunchpad/pd-p/538710751289542466232554247536294)
* [SAP S/4HANA Cloud Public Edition Human Resources

  Additional Software Product](/t5/c-khhcw49343/SAP%2BS%25252F4HANA%2BCloud%2BPublic%2BEdition%2BHuman%2BResources/pd-p/a8945cb2-dac7-490c-a6b6-7d8629f65668)

View products (3)

Hello Community,

Creating Business Roles is a process that requires attention, as it is directly related to authorizations in the system. Thus, it is common in a system to have several Business Roles with different specifications. However, some Business Role configurations can be similar, and at some times it can be very useful to be able to mass update them.

Now, in SAP S/4HANA Cloud, it is possible to make mass changes to a Business Roles using the Mass Change Wizard.This is helpful, for example, if you have switched from using custom spaces to SAP-delivered spaces or if you start using spaces. In that case, you can select all affected business roles and click Assign SAP-Delivered Spaces. The system then automatically assigns SAP-delivered spaces to all of the business roles in question. If you click Remove Launchpad Spaces Already Assigned, the custom spaces that were assigned to the business roles previously are automatically removed.

## Procedure

1. Go to Maintain Business Roles app

2. Select the Business Roles that you want to change and click on "Mass Change" button
   ![](/legacyfs/online/storage/blog_attachments/2023/07/Untitled.png)

3. The Mass Change Wizard appears with the allowed changes

4. Select the Area and Attribute that you want to change

5. Click on "Next Step"

6. Proceed with the Changes in the attributed

7. Click on "Next Step" again

8. Review and Confirm the changes

All the allowed changes are described below:

**Business Role Data -** With this attribute, you'll be able to change the Role Group, Expose to SAP BTP and Inherit Spaces in Derived Business Roles.

**Business User Assignment** - With this attribute, you'll be able to add and remove Business Users.

**Business Catalog Assignment** - With this attribute, you'll be able to add and remove Business Catalogs.

**Launchpad Space Assignment** - With this attribute, you'll be able to add and remove Launchpad Spaces.

**Assign SAP-Delivered Spaces** - With this attribute, you'll be able to assign SAP-Delivered Spaces to your Business Roles.

**Access Categories** - With this attribute, you'll be able to change access categories as required.

**Restrictions (AVAILABLE ONLY AFTER THE 2308 S/4HANA CLOUD RELEASE)** - With this attribute, you'll be able to change General Restriction Values, add Restrictions, remove Restricions and change Restriction Values.

Please note that depending of the Business Role, specially the ones predefined by SAP, some attributes might not be modifiable.

Hope I could help you understand better the mass update.

For more information on SAP S/4HANA Cloud, check out the following links:

* SAP S/4HANA cloud release information: <http://www.sap.com/s4-cloudrelease>

* Best practices for SAP S/4HANA Cloud [here](https://rapid.sap.com/bp/#/browse/categories/sap_s%254hana/areas/cloud)

* DMS : [Document Management in SAP S/4HANA Cloud](https://help.sap.com/viewer/f369b2eff700401494ba6e7c9a573288/1905.500/en-US/70414d95dcfe4f588032ddca36f5d7ec.html)

Best regards,

Tayane.

Labels

* [Technology Updates](/t5/enterprise-resource-planning-blog-posts-by-sap/bg-p/erp-blog-sap/label-name/technology%20updates)

1 Comment

You must be a registered user to add a comment. If you've already registered, sign in. Otherwise, register and sign in.

* [Comment](/plugins/common/feature/oidcss/sso_login_redirect/providerid/sap_ids_prompt?redirectreason=permissiondenied&referer=https%3A%2F%2Fcommunity.sap.com%2Ft5%2Fenterprise-resource-planning-blog-posts-by-sap%2Fhow-to-mass-update-business-roles%2Fba-p%2F13553396%23comment-on-this)

Copy Link
![](https://community.sap.com/html/@EE5D5986E9F4E5657DCEACB7532B5C39/assets/bluesky-dark.svg)Bluesky
Linkedin

Related Content

* [GRC, Trade and Tax with SAP S/4HANA Cloud Public Edition 2508](/t5/enterprise-resource-planning-blog-posts-by-sap/grc-trade-and-tax-with-sap-s-4hana-cloud-public-edition-2508/ba-p/14229204)
  in [Enterprise Resource Planning Blog Posts by SAP](/t5/enterprise-resource-planning-blog-posts-by-sap/bg-p/erp-blog-sap)  Thursday
* [SAP Business Suite - Q4 Global Partner Update](/t5/enterprise-resource-planning-blog-posts-by-sap/sap-business-suite-q4-global-partner-update/ba-p/14232752)
  in [Enterprise Resource Planning Blog Posts by SAP](/t5/enterprise-resource-planning-blog-posts-by-sap/bg-p/erp-blog-sap)  Wednesday
* [SAP Enterprise Support Academy Newsletter October 2025](/t5/enterprise-resource-planning-blog-posts-by-sap/sap-enterprise-support-academy-newsletter-october-2025/ba-p/14232476)
  in [Enterprise Resource Planning Blog Posts by SAP](/t5/enterprise-resource-planning-blog-posts-by-sap/bg-p/erp-blog-sap)  Wednesday
* [SAP Sustainability Footprint Management: Q3-25 Updates & Highlights](/t5/enterprise-resource-planning-blog-posts-by-sap/sap-sustainability-footprint-management-q3-25-updates-amp-highlights/ba-p/14230327)
  in [Enterprise Resource Planning Blog Posts by SAP](/t5/enterp...