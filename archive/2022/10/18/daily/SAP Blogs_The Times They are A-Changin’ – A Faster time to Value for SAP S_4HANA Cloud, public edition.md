---
title: The Times They are A-Changin’ – A Faster time to Value for SAP S/4HANA Cloud, public edition
url: https://blogs.sap.com/2022/10/17/the-times-they-are-a-changin-a-faster-time-to-value-for-sap-s-4hana-cloud-public-edition/
source: SAP Blogs
date: 2022-10-18
fetch_date: 2025-10-03T20:06:50.593938
---

# The Times They are A-Changin’ – A Faster time to Value for SAP S/4HANA Cloud, public edition

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Enterprise Resource Planning](/t5/enterprise-resource-planning/ct-p/erp)
* [ERP Blog Posts by SAP](/t5/enterprise-resource-planning-blog-posts-by-sap/bg-p/erp-blog-sap)
* The Times They are A-Changin' - A Faster time to V...

Enterprise Resource Planning Blog Posts by SAP

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/erp-blog-sap/article-id/49728&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [The Times They are A-Changin' - A Faster time to Value for SAP S/4HANA Cloud, public edition](/t5/enterprise-resource-planning-blog-posts-by-sap/the-times-they-are-a-changin-a-faster-time-to-value-for-sap-s-4hana-cloud/ba-p/13545411)

![Bert_Laws_SAP](https://avatars.profile.sap.com/7/e/id7e914ba069ec3a93ff3aa81f3b477da9f7b0dd797f521cc62522531775af1157_small.jpeg "Bert_Laws_SAP")

![Advisor](/html/@138D6F765B60D7FC0168643DE27D8A68/rank_icons/sap-logo-small-14px.png "Advisor")
[Bert\_Laws\_SAP](https://community.sap.com/t5/user/viewprofilepage/user-id/132301)

Advisor

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=erp-blog-sap&message.id=49728)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/erp-blog-sap/article-id/49728)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13545411)

‎2022 Oct 18
12:24 AM

[4
Kudos](/t5/kudos/messagepage/board-id/erp-blog-sap/message-id/49728/tab/all-users "Click here to see who gave kudos to this post.")

1,000

* SAP Managed Tags
* [SAP TechEd](https://community.sap.com/t5/c-khhcw49343/SAP%2520TechEd/pd-p/755421404636447943131706525840948)
* [SAP S/4HANA Cloud Public Edition](https://community.sap.com/t5/c-khhcw49343/SAP%2520S%252F4HANA%2520Cloud%2520Public%2520Edition/pd-p/08e2a51b-1ce5-4367-8b33-4ae7e8b702e0)

* [SAP S/4HANA Cloud Public Edition

  SAP S/4HANA Cloud](/t5/c-khhcw49343/SAP%2BS%25252F4HANA%2BCloud%2BPublic%2BEdition/pd-p/08e2a51b-1ce5-4367-8b33-4ae7e8b702e0)
* [SAP TechEd

  Event](/t5/c-khhcw49343/SAP%2BTechEd/pd-p/755421404636447943131706525840948)

View products (2)

Bob Dylan’s famous song “*The Times they are A-Changin*’” rings as true today as it did in 1963 when it was first recorded.  It was a song of protest and an anthem for a generation.   I could argue that this theme also cuts through the years and rings true today when we look at what the real emergence of the cloud is doing to enterprise software in general and to SAP ERP specifically.   For years, we have looked at local infrastructure and architecture as unchangeable.  But the times they are indeed “a-Changin'” and if you are interested in deploying a baseline of scope for S/4HANA Cloud, public edition in 30 days – or less – welcome to the world of Baseline Activation Service and the Activation Accelerators.  This is what I’ll talk about in today’s blog.

At its core, SAP has a robust set of tools to help you implement S/4HANA Cloud, public edition.   While you can vary a lot of your configuration master data (org units, currencies, etc. ), a lot of the initial implementation activities can boil down to doing a few key things – multiple times. First, you want to be sure that you understand the scope that you will be deploying – we have the digital demand assessment (the DDA) for that.  Next, SAP Central Business Configuration (CBC) will help you to activate the scope that you identify that you need via the DDA.  Next, SAP Cloud ALM will help you to configure what you have activated.  Next, you can use the Migration Cockpit to migrate your data into S/4HANA Cloud, public edition and finally you can automate many of your testing activities using the Automated Testing Tool.  What is challenging – and let’s be honest – is that it can become a bit tedious is the discipline required to do the same things and the repetition to do these things over and over.  Enter Baseline Activation and the Activation Accelerators.

Newly released in June of this year, Baseline Activation & in August, activation accelerators were released that do a couple of really important things.  First, it defines a baseline of 60-70 common scope items that almost 80-90% of S/4HANA customers almost always deploy.  This becomes the scope of your baseline.   Standardized templates can be used to collect configuration information and then can be deployed to bring in pre- defined configuration info in a manual or automated batch upload into S/4.  We have pre-built automation accelerators (currently only available through Partners) that help you to automate the deployment and configuration of certain scope items:

|
 **Line of Business** |
 **Scope  Item** |
 **In-App Configuration Features** |

|
 Finance |
 J59 |
 BRF+ Settings for Customer Balance Confirmation, Item Interest Calculation |

|
 Finance |
 J58 |
 Workflows, Teams and Responsibility for Journal Entry Verification |

|
 Finance |
 J60,1NT |
 BRF+ Settings for Payment Advice, Printed Checks, Supplier Balance Confirmation, Item Interest Calculation, Payment List Teams & Responsibility |

|
 Finance |
 1LQ |
 Print Queues, Email Templates, Logos, Output Items, Output Parameter Determination, Form Templates |

|
 Sale, Finance |
 2LH,2LH,2V7,BD9 |
 Purchasing Info Records ,Teams & Responsibility, Pricing Condition, Custom Logic |

|
 Procurement |
 J45,18J |
 Workflows for Purchase Orders, Purchase Requisitions , Supplier Invoices, Teams and Responsibilities and Supplier Invoice Settings |

(To learn more about uploading configuration data directly into S/4HANA Cloud, follow [this link](https://help.sap.com/docs/SAP_S4HANA_CLOUD/b249d650b15e4b3d9fc2077ee921abd0/f92cd2bd253c4ee287f91695147089ab.html) in help.sap.com).  Pre-built data migration templates are also available that identify specific data related to the baseline scope using the migration cockpit.  Finally, pre-defined test data containers with related automation accelerators can be used to automate your testing procedures.

So how can you learn more about the activation accelerators and baseline activation?  Currently, access to the activation accelerators is addressed in [SAP note 3246861](https://launchpad.support.sap.com/#/notes/3246861). But if we look at deployment methodology, we first have [SAP Activate](https://community.sap.com/topics/activate) and now in SAP Activate we have the [Activate roadmap Viewer for S/4HANA Cloud, public edition](https://go.support.sap.com/roadmapviewer/#/group/658F507A-D6F5-4B78-9EE1-0300C5F1E40F/roadmapOverviewPage/d9ffcd6438ab4ee9a02bfcf682502892).

There is a lot more to learn about the accelerators and baseline and we invite you to stop by our booth as Tech Ed later this month!!

Labels

* [Product Updates](/t5/enterprise-resource-planning-blog-posts-by-sap/bg-p/erp-blog-sap/label-name/product%20updates)

You must be a registered user to add a comment. If you've already registered, sign in. Otherwise, register and sign in.

* [Comment](/plugins/common/feature/oidcss/sso_login_redirect/providerid/sap_ids_prompt?redirectreason=permissiondenied&referer=https%3A%2F%2Fcommunity.sap.com%2Ft5%2Fenterprise-resource-planning-blog-posts-by-sap%2Fthe-times-they-are-a-changin-a-faster-time-to-value-for-sap-s-4hana-cloud%2Fba-p%2F13545411%23comment-on-this)

Copy Link
![](https://community.sap.com/html/@EE5D5986E9F4E5657DCEACB7532B5C39/assets/bluesky-dark.svg)Bluesky
Linkedin

Related Content

* [Enabling...