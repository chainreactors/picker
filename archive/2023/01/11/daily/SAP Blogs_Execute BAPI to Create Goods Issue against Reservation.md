---
title: Execute BAPI to Create Goods Issue against Reservation
url: https://blogs.sap.com/2023/01/10/execute-bapi-to-create-goods-issue-against-reservation/
source: SAP Blogs
date: 2023-01-11
fetch_date: 2025-10-04T03:31:33.794570
---

# Execute BAPI to Create Goods Issue against Reservation

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Enterprise Resource Planning](/t5/enterprise-resource-planning/ct-p/erp)
* [ERP Blog Posts by Members](/t5/enterprise-resource-planning-blog-posts-by-members/bg-p/erp-blog-members)
* Execute BAPI to Create Goods Issue against Reserva...

Enterprise Resource Planning Blog Posts by Members

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/erp-blog-members/article-id/68247&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [Execute BAPI to Create Goods Issue against Reservation](/t5/enterprise-resource-planning-blog-posts-by-members/execute-bapi-to-create-goods-issue-against-reservation/ba-p/13565254)

![sumantk24x7](https://avatars.profile.sap.com/0/3/id030b8673027be48f29c4570ff677db5a1f2b540032b520db5c329af1e79c9ddb_small.jpeg "sumantk24x7")

[sumantk24x7](https://community.sap.com/t5/user/viewprofilepage/user-id/135647)

Explorer

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=erp-blog-members&message.id=68247)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/erp-blog-members/article-id/68247)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13565254)

‎2023 Jan 10
11:30 PM

[4
Kudos](/t5/kudos/messagepage/board-id/erp-blog-members/message-id/68247/tab/all-users "Click here to see who gave kudos to this post.")

5,644

* SAP Managed Tags
* [MM Inventory Management](https://community.sap.com/t5/c-khhcw49343/MM%2520Inventory%2520Management/pd-p/402489426158095572469338199787586)

* [MM Inventory Management

  Software Product Function](/t5/c-khhcw49343/MM%2BInventory%2BManagement/pd-p/402489426158095572469338199787586)

View products (1)

**Purpose:**

In this blog, the user will learn how to use Execute BAPI to create goods issue against a reservation.

**Contents:**

* Overview about "Create and Execute Goods Issue against Reservation using BAPI"

* Prerequisite

* BAPI

* Steps to execute

* Conclusion

**Overview:**

The majority of the professional time is spent by functional and technical consultants, who are responsible for enhancement and interface (i.e., SAP to non-SAP and vice versa). So this blog is useful for testing and executing BAPI, and the purpose of this blog post is to create awareness among functional and technical consultants who are new and want to explore it.

**Prerequisite :**

* Reservation Number or

* Reservation number created through workorder

**BAPI :**

* BAPI\_GOODSMVT\_CREATE

* BAPI\_TRANSACTION\_COMMIT

**Steps : Goto T-Code - SE37**

1. Click on “Function Module”

2. Click on “Execute”

3. Click on “Test Sequences”

![](/legacyfs/online/storage/blog_attachments/2023/01/1-6.png)

Enter BAPI in below test sequences:

![](/legacyfs/online/storage/blog_attachments/2023/01/2-6.png)

Then click on Execute.

Now, Below screen appears:

![](/legacyfs/online/storage/blog_attachments/2023/01/3-3.png)

passed all the required parameters as per the below Documentation into the BAPI:

**<Import Parameters>**

**GOODSMVT\_HEADER**

|
 **Parameters** |
 **Value** |

|
 **PSTNG\_DATE** |
 09.01.2023 |

|
 **DOC\_DATE** |
 09.01.2023 |

|
 **REF\_DOC\_NO** |
 789 |

**GOODSMVT\_CODE**

|
 **Parameters** |
 **Value** |

|
 **GM\_CODE** |
 03 |

**<Tables>**

**GOODSMVT\_ITEM**

|
 **Parameters** |
 **Value** |

|
 **MATERIAL** |
 15 |

|
 **PLANT** |
 1710 |

|
 **STGE\_LOC** |
 171A |

|
 **MOVE\_TYPE** |
 261 |

|
 **ENTRY\_QNT** |
 1 |

|
 **ENTRY\_UOM** |
 PC |

|
 **ENTRY\_UOM\_ISO** |
 PC |

|
 **RESERV\_NO** |
 789 |

|
 **RES\_ITEM** |
 0003 |

Under Export Parameter you can check “Material Document Number” created.

![](/legacyfs/online/storage/blog_attachments/2023/01/4-2.png)

Then click on “Back”

Now, Below Screen Appear:

![](/legacyfs/online/storage/blog_attachments/2023/01/5-2.png)

Pass “X” value under parameter WAIT.

Then click on Execute.

Again, click on Back.

Now, Below screen appears:

![](/legacyfs/online/storage/blog_attachments/2023/01/6-2.png)

Then Click on “Copy”

Back & Exit.

**Conclusion**

Now we have successfully executed the BAPI and created goods issue against Reservation Number.

* Use Movement type 201 for Reservation Number which are created against cost center or

* Use Movement type 261 for Reservation number created through workorder

###

### **Thanks for reading this blog…**

Hope this blog will be useful. If you enjoyed this blog post please give it a like! If you have questions,

feel free to comment.

If you would like to keep up on the latest updates regarding SAP S4/HANA cloud, Kindly follow me…

**Thanks & Regards,**

**Sumant Kumar Modi**

Kindly provide the feedback

1 Comment

You must be a registered user to add a comment. If you've already registered, sign in. Otherwise, register and sign in.

* [Comment](/plugins/common/feature/oidcss/sso_login_redirect/providerid/sap_ids_prompt?redirectreason=permissiondenied&referer=https%3A%2F%2Fcommunity.sap.com%2Ft5%2Fenterprise-resource-planning-blog-posts-by-members%2Fexecute-bapi-to-create-goods-issue-against-reservation%2Fba-p%2F13565254%23comment-on-this)

Copy Link
![](https://community.sap.com/html/@EE5D5986E9F4E5657DCEACB7532B5C39/assets/bluesky-dark.svg)Bluesky
Linkedin

Related Content

* [Japan Bank Charges in Payment Run](/t5/enterprise-resource-planning-blog-posts-by-sap/japan-bank-charges-in-payment-run/ba-p/14231441)
  in [Enterprise Resource Planning Blog Posts by SAP](/t5/enterprise-resource-planning-blog-posts-by-sap/bg-p/erp-blog-sap)  Tuesday
* [Int4 Suite — your SAP Joule testbed and skills builder](/t5/enterprise-resource-planning-blog-posts-by-members/int4-suite-your-sap-joule-testbed-and-skills-builder/ba-p/14229790)
  in [Enterprise Resource Planning Blog Posts by Members](/t5/enterprise-resource-planning-blog-posts-by-members/bg-p/erp-blog-members)  Sunday
* [App "Overall Cost planning (Enhanced)" not visible in Fiori Library](/t5/enterprise-resource-planning-q-a/app-quot-overall-cost-planning-enhanced-quot-not-visible-in-fiori-library/qaq-p/14228535)
  in [Enterprise Resource Planning Q&A](/t5/enterprise-resource-planning-q-a/qa-p/erp-questions)  a week ago
* [My Learning Journal on BTP (5) - Build A Small Finance Agent: CAP + Generative AI Hub + LangChain](/t5/enterprise-resource-planning-blog-posts-by-sap/my-learning-journal-on-btp-5-build-a-small-finance-agent-cap-generative-ai/ba-p/14222295)
  in [Enterprise Resource Planning Blog Posts by SAP](/t5/enterprise-resource-planning-blog-posts-by-sap/bg-p/erp-blog-sap)  2 weeks ago
* [Restriction of Access to Executive Payroll Data in SAP HR](/t5/enterprise-resource-planning-q-a/restriction-of-access-to-executive-payroll-data-in-sap-hr/qaq-p/14222348)
  in [Enterprise Resource Planning Q&A](/t5/enterprise-resource-planning-q-a/qa-p/erp-questions)  2 weeks ago

Top kudoed authors

| User | Count |
| --- | --- |
| [![MichalKrawczyk](https://avatars.profile.sap.com/6/7/id677f624df4f67fa55aef9b803484fd38cfa389573f663b9623d9dc410597c931_small.jpeg "MichalKrawczyk")  MichalKrawczyk](/t5/user/viewprofilepage/user-id/45785) | 11 |
| [![Amin_Omidy](https://avatars.profile.sap.com/3/e/id3ec1fabb5feddc26ec180cef8c60f7c62692cc423031b6be3bab024c75e2c7d3_small.jpeg "Amin_Omidy")  ![SAP Champion](/html/@B3DACAC6163F980483AC32558EB69695/rank_icons/champion-rank-16x16.svg "SAP Champion") Amin\_Omidy](/t5/user/viewprofilepage/user-id/40654) | 3 |
| [![form...