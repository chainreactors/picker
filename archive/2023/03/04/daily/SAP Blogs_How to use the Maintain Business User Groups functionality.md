---
title: How to use the Maintain Business User Groups functionality
url: https://blogs.sap.com/2023/03/03/how-to-use-the-maintain-business-user-groups-functionality/
source: SAP Blogs
date: 2023-03-04
fetch_date: 2025-10-04T08:37:57.476587
---

# How to use the Maintain Business User Groups functionality

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Enterprise Resource Planning](/t5/enterprise-resource-planning/ct-p/erp)
* [ERP Blog Posts by SAP](/t5/enterprise-resource-planning-blog-posts-by-sap/bg-p/erp-blog-sap)
* How to use the Maintain Business User Groups funct...

Enterprise Resource Planning Blog Posts by SAP

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/erp-blog-sap/article-id/52247&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [How to use the Maintain Business User Groups functionality](/t5/enterprise-resource-planning-blog-posts-by-sap/how-to-use-the-maintain-business-user-groups-functionality/ba-p/13562815)

![Tayane](https://avatars.profile.sap.com/4/d/id4d2d58bc40b1d37b5ee1cb7b23f537eb72d39ac3b3946114f66c9b4b52cf47de_small.jpeg "Tayane")

![Product and Topic Expert](/html/@138D6F765B60D7FC0168643DE27D8A68/rank_icons/sap-logo-small-14px.png "Product and Topic Expert")
[Tayane](https://community.sap.com/t5/user/viewprofilepage/user-id/143549)

Product and Topic Expert

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=erp-blog-sap&message.id=52247)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/erp-blog-sap/article-id/52247)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13562815)

‎2023 Mar 03
7:03 PM

[1
Kudo](/t5/kudos/messagepage/board-id/erp-blog-sap/message-id/52247/tab/all-users "Click here to see who gave kudos to this post.")

2,426

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

With the SAP S/4HANA Cloud 2302 release a new feature is now available: Business User Groups. With this feature you can create business user groups and assign multiple business users to them. This helps you to organize your area and easily search for all business users of a certain category.

In this Blog Post I will show you how you can easily create a Business User Group and assign it to your users.

### **Prerequisites:**

Ensure that you have the Business Catalog SAP\_CORE\_BC\_IAM\_GRP\_PC assigned to your user. This Business Catalog is also added as default into the Business Role Template SAP\_BR\_ADMINISTRATOR.

Also, the following restriction types (in the following business catalogs) are required for maintaining business role groups and business user groups:

|
 Business Catalogs |
 Restriction Types |

|
 SAP\_CORE\_BC\_IAM\_RM |
 Business Role (S\_BRL) |

|
 SAP\_CORE\_BC\_IAM\_UM |
 Business User (CLASS) |

|
 SAP\_CORE\_BC\_IAM\_RA |
 Business Role (S\_BRL)   Business User (CLASS) |

|
 SAP\_CORE\_BC\_IAM\_RM\_DISP\_PC |
 Business Role (ROLE\_GROUP) |

|
 SAP\_CORE\_BC\_IAM\_UM\_DISP\_PC |
 Business User (CLASS) |

### **Creating a Business User Group:**

1. Go to "Maintain Business User Groups" app and click on "Create" button
   ![](/legacyfs/online/storage/blog_attachments/2023/03/BusinessUser-1.png)

2. Choose the Group Description and click on "Create" button again
   *\*Please note that the name of business user group is created automatically in namespace ZCB.*
   ![](/legacyfs/online/storage/blog_attachments/2023/03/BusinessUser-2.png)

3. The Business User Group is now created

### **Assigning users to a Business User Group:**

1. In the Maintain Business User Groups app, click on the group that you want to add a user

2. Once the group details appear, click on "Add" button
   ![](/legacyfs/online/storage/blog_attachments/2023/03/BusinessUser-3.png)

3. A pop-up window will open with the Business Users. Select the Business Users that you want to add to the Business Group and click on "Add" button
   ![](/legacyfs/online/storage/blog_attachments/2023/03/BusinessUser-4.png)

4. Now the Business Users were added to the Business Group.

*Kindly note that it's also possible to add a Business User Group to a specific Business User inside Maintain Business User app inside the Business User details.*

### **Removing users of a Business User Group:**

1. In the Maintain Business User Groups app, click on the group that you want to remove the user

2. Once the group details appear, select the Business User that you want to remove and click on "Remove" button

### **Deleting a Business User Group:**

It's only possible to delete a Business User Group if it has no Business User assigned to it. Ensure that you have removed all the Business Users assignments before deleting a Business User group.

For more details regarding this new functionality, please check the [SAP Help Portal Documentation - Maintain Business User Groups](https://help.sap.com/docs/SAP_S4HANA_CLOUD/a630d57fc5004c6383e7a81efee7a8bb/24f5b79256f64990af35b22ea87ea020.html?locale=en-US).

Hope this information is useful for you! I would greatly appreciate if you could share your feedbacks and thoughts in the comments.

Also, I encourage you to browse for other [Community Topics](https://community.sap.com/topics) that may be useful for you.

Best regards,

Tayane.

Labels

* [Technology Updates](/t5/enterprise-resource-planning-blog-posts-by-sap/bg-p/erp-blog-sap/label-name/technology%20updates)

You must be a registered user to add a comment. If you've already registered, sign in. Otherwise, register and sign in.

* [Comment](/plugins/common/feature/oidcss/sso_login_redirect/providerid/sap_ids_prompt?redirectreason=permissiondenied&referer=https%3A%2F%2Fcommunity.sap.com%2Ft5%2Fenterprise-resource-planning-blog-posts-by-sap%2Fhow-to-use-the-maintain-business-user-groups-functionality%2Fba-p%2F13562815%23comment-on-this)

Copy Link
![](https://community.sap.com/html/@EE5D5986E9F4E5657DCEACB7532B5C39/assets/bluesky-dark.svg)Bluesky
Linkedin

Related Content

* [Int4 Suite Agents Empowers Functional Consultants To Test Integrated SAP S/4HANA Business Processes](/t5/enterprise-resource-planning-blog-posts-by-members/int4-suite-agents-empowers-functional-consultants-to-test-integrated-sap-s/ba-p/14234100)
  in [Enterprise Resource Planning Blog Posts by Members](/t5/enterprise-resource-planning-blog-posts-by-members/bg-p/erp-blog-members)  yesterday
* [How to trigger HU label print in S/4HANA Cloud Public Edition (API\_FORM\_PRINT\_SRV not available)](/t5/enterprise-resource-planning-q-a/how-to-trigger-hu-label-print-in-s-4hana-cloud-public-edition-api-form/qaq-p/14233989)
  in [Enterprise Resource Planning Q&A](/t5/enterprise-resource-planning-q-a/qa-p/erp-questions)  yesterday
* [Busin...