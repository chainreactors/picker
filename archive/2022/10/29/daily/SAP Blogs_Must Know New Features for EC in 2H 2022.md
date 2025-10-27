---
title: Must Know New Features for EC in 2H 2022
url: https://blogs.sap.com/2022/10/28/must-know-new-features-for-ec-in-2h-2022/
source: SAP Blogs
date: 2022-10-29
fetch_date: 2025-10-03T21:13:30.929358
---

# Must Know New Features for EC in 2H 2022

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Human Capital Management](/t5/human-capital-management/ct-p/hcm)
* [HCM Blog Posts by SAP](/t5/human-capital-management-blog-posts-by-sap/bg-p/hcm-blog-sap)
* Must Know New Features for EC in 2H 2022

Human Capital Management Blog Posts by SAP

Learn directly from SAP experts through blogs that deliver practical guidance and opportunities to deepen your expertise.

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/hcm-blog-sap/article-id/5923&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [Must Know New Features for EC in 2H 2022](/t5/human-capital-management-blog-posts-by-sap/must-know-new-features-for-ec-in-2h-2022/ba-p/13555589)

![AndrewK](https://avatars.profile.sap.com/2/f/id2ffc4e26c5b84747d09eebfacc07cdf5c70e22a5d2cec67a3d55f00da7dea171_small.jpeg "AndrewK")

![Product and Topic Expert](/html/@138D6F765B60D7FC0168643DE27D8A68/rank_icons/sap-logo-small-14px.png "Product and Topic Expert")
[AndrewK](https://community.sap.com/t5/user/viewprofilepage/user-id/18345)

Product and Topic Expert

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=hcm-blog-sap&message.id=5923)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/hcm-blog-sap/article-id/5923)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13555589)

‎2022 Oct 28
4:12 PM

[16
Kudos](/t5/kudos/messagepage/board-id/hcm-blog-sap/message-id/5923/tab/all-users "Click here to see who gave kudos to this post.")

5,158

* SAP Managed Tags
* [SAP SuccessFactors Employee Central](https://community.sap.com/t5/c-khhcw49343/SAP%2520SuccessFactors%2520Employee%2520Central/pd-p/73555000100800000773)
* [SAP SuccessFactors HCM Core](https://community.sap.com/t5/c-khhcw49343/SAP%2520SuccessFactors%2520HCM%2520Core/pd-p/67837800100800006332)

* [SAP SuccessFactors HCM Core

  SAP SuccessFactors HCM](/t5/c-khhcw49343/SAP%2BSuccessFactors%2BHCM%2BCore/pd-p/67837800100800006332)
* [SAP SuccessFactors Employee Central

  SAP SuccessFactors HCM](/t5/c-khhcw49343/SAP%2BSuccessFactors%2BEmployee%2BCentral/pd-p/73555000100800000773)

View products (2)

With every release, there are important features and changes to the user experience that both Employee Central administrators and employees will need to be aware of. For the 2H 2022 release, we have consolidated a list of features that are “Must Know” items for Employee Central Core, Time Off, and Global Benefits. All of the features listed below will also include links to related information that will provide additional details regarding that specific feature.

Please also review other release related information at [SAP SuccessFactors Release Information](https://help.sap.com/viewer/product/SAP_SUCCESSFACTORS_RELEASE_INFORMATION/cloud/en-US) as well as specific features coming in the 2H 2022 Release in the [What’s New Viewer](https://help.sap.com/whats-new/8fcf4960eea24f78b1d7613da406a885?locale=en-US).

A compiled [list of guide changes for Employee Central in 2H 2022](https://community.successfactors.com/t5/Employee-Central-Resources-Blog/List-of-guide-changes-for-Employee-Central-in-2H-2022/ba-p/297957) is also available for review.

|
 **Centralized Services** | | |

|
 **Feature Name** |
 **Reference Number** |
 **Configuration Type** |

|
 Universal Support for Centralized Services Entities |
 ECT-197772 |
 Universal |

We have introduced universal support for some of the Centralized Services entities. These entities are no longer governed by the configuration option:

|
 **Universal Entities** |
 **Description** |

|
 Global Assignment Imports |
 Centralized services now universally support Global Assignments data imports in Incremental Load mode and in Full Purge mode. |

|
 Global Information Editing UI Save |
 Centralized services now universally support saving changes on the Editing UI for Global Information. |

|
 Personal Information Editing UI Save |
 Centralized services now universally support saving changes on the Editing UI for Personal Information. |

|
 Job Relationship History UI Save |
 Centralized services now universally support saving changes on the History UI of Job Relationships. |

|
 Job Information History UI Save |
 Centralized services now universally support saving changes on the History UI of Job Information. |

|
 Address Editing UI Save |
 Centralized services now universally support saving changes on the Editing UI for Address. |

|
 National ID Editing UI Save |
 Centralized services now universally support saving changes on the Editing UI for National ID. |

With this enhancement, you have access to the supported Centralized Services entities by default.

We would like to highlight the following key points regarding Universal features in this release:

* **Job Information History UI Save:**

  + Updating the Hire Date is no longer possible in the Job History UI, however we have enhanced the Hire Date Correction tool to allow for more flexibility (see Hire Date Correction section further down in this blog for more details)

  + The data validation check for the Job History's oldest record should always be a Hire Event record, otherwise no further changes can be made to an employee's Job History.

* **Job Information Imports:** This feature was made Universal in 1H 2022, however now we've added an enhancement in this release to allow custom entry date values.

* **Job Information History UI & Job Information Imports:** From this release, we do not support the creation of Leave of Absence (LOA) and Return to Work record Events. Customers will need to use Employee Central Time Off for LOA instead. Please review KBAs [3228287](https://launchpad.support.sap.com/#/notes/3228287) & [3205591](https://launchpad.support.sap.com/#/notes/3205591) for more details.

**Related Information:**

* Blog: [Employee Central Centralized Services in Second Half 2022 (2H 2022) Release – Innovation Alert](https://community.successfactors.com/t5/Employee-Central-Resources-Blog/Employee-Central-Centralized-Services-in-Second-Half-2022-2H/ba-p/276294)

* Handbook: [Implementing Employee Central Core – Centralized Services in Employee Central](https://help.sap.com/docs/SAP_SUCCESSFACTORS_EMPLOYEE_CENTRAL/b14dd15ca58f43e0856184a740a4b212/3d1f814fe6e64adcb7a8253f161ff5f8.html)

* Handbook: [Managing Mass Changes in Employee Central – Centralized Services for Employee Data Imports](https://help.sap.com/docs/SAP_SUCCESSFACTORS_EMPLOYEE_CENTRAL/6b8f2827f40642f3aa95dc4ac65055dc/d5e493915fd140108e25b115e8c16acd.html)

* [What’s New Viewer Link](https://help.sap.com/docs/SAP_SUCCESSFACTORS_RELEASE_INFORMATION/8e0d540f96474717bbf18df51e54e522/20739137634b4800a5efc7c9007237fa.html?parentHref=%2Fwhats-new%2F8fcf4960eea24f78b1d7613da406a885%3FArea%3DEmployee%252520Central%26Component%3DPersonal%252520Information%26Version%3D2H%2525202022%26locale%3Den-US&parentName=SAP%20SuccessFactors%20What%27s%20New)

|
 **Centralized Services** | | | |

|
 **Feature Name** |
 **Reference Number** |
 **Configuration Type** |
 **Related Information** |

|
 Centralized Services Support Integrations with Employee Central Compensation |
 ECT-194595 |
 Admin Opt-out (Preview)    **Update:**Admin Opt-in (Production) |
 [What’s New Viewer Link](https://help.sap.com/docs/SAP_SUCCESSFACTORS_RELEASE_INFORMATION/8e0d540f96474717bbf18df51e54e522/64b3a04b8d4948c28c77f28...