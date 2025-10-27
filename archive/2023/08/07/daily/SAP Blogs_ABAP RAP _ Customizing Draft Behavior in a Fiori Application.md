---
title: ABAP RAP : Customizing Draft Behavior in a Fiori Application
url: https://blogs.sap.com/2023/08/06/abap-rap-customizing-draft-behavior-in-a-fiori-application/
source: SAP Blogs
date: 2023-08-07
fetch_date: 2025-10-04T11:59:30.049821
---

# ABAP RAP : Customizing Draft Behavior in a Fiori Application

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Technology](/t5/technology/ct-p/technology)
* [Technology Blog Posts by Members](/t5/technology-blog-posts-by-members/bg-p/technology-blog-members)
* ABAP RAP : Customizing Draft Behavior in a Fiori A...

Technology Blog Posts by Members

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/technology-blog-members/article-id/164449&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [ABAP RAP : Customizing Draft Behavior in a Fiori Application](/t5/technology-blog-posts-by-members/abap-rap-customizing-draft-behavior-in-a-fiori-application/ba-p/13575424)

![Ramjee_korada](https://avatars.profile.sap.com/a/6/ida68feb06dad0280b54c7e92a0996c1389c5cbe26af62aeffa035d47c94865194_small.jpeg "Ramjee_korada")

[Ramjee\_korada](https://community.sap.com/t5/user/viewprofilepage/user-id/10276)

Active Contributor

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=technology-blog-members&message.id=164449)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/technology-blog-members/article-id/164449)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13575424)

‎2023 Aug 06
10:35 PM

[7
Kudos](/t5/kudos/messagepage/board-id/technology-blog-members/message-id/164449/tab/all-users "Click here to see who gave kudos to this post.")

22,411

* SAP Managed Tags
* [SAP BTP ABAP environment](https://community.sap.com/t5/c-khhcw49343/SAP%2520BTP%2520ABAP%2520environment/pd-p/73555000100800001164)
* [SAP Fiori Elements](https://community.sap.com/t5/c-khhcw49343/SAP%2520Fiori%2520Elements/pd-p/ed5c1ef6-932f-4c19-b2ba-1be375109ff5)
* [SAP S/4HANA Cloud ABAP Environment](https://community.sap.com/t5/c-khhcw49343/SAP%2520S%252F4HANA%2520Cloud%2520ABAP%2520Environment/pd-p/60907aa9-99e9-4d5d-9103-8b970e9bc0a4)
* [ABAP Development](https://community.sap.com/t5/c-khhcw49343/ABAP%2520Development/pd-p/833755570260738661924709785639136)
* [SAP S/4HANA](https://community.sap.com/t5/c-khhcw49343/SAP%2520S%252F4HANA/pd-p/73554900100800000266)
* [ABAP RESTful Application Programming Model](https://community.sap.com/t5/c-khhcw49343/ABAP%2520RESTful%2520Application%2520Programming%2520Model/pd-p/7e44126e-7b27-471d-a379-df205a12b1ff)
* [SAP S/4HANA Cloud Public Edition](https://community.sap.com/t5/c-khhcw49343/SAP%2520S%252F4HANA%2520Cloud%2520Public%2520Edition/pd-p/08e2a51b-1ce5-4367-8b33-4ae7e8b702e0)

* [SAP S/4HANA Cloud Public Edition

  SAP S/4HANA Cloud](/t5/c-khhcw49343/SAP%2BS%25252F4HANA%2BCloud%2BPublic%2BEdition/pd-p/08e2a51b-1ce5-4367-8b33-4ae7e8b702e0)
* [SAP S/4HANA Cloud ABAP Environment

  Additional Software Product](/t5/c-khhcw49343/SAP%2BS%25252F4HANA%2BCloud%2BABAP%2BEnvironment/pd-p/60907aa9-99e9-4d5d-9103-8b970e9bc0a4)
* [SAP S/4HANA

  SAP S/4HANA](/t5/c-khhcw49343/SAP%2BS%25252F4HANA/pd-p/73554900100800000266)
* [SAP BTP ABAP environment

  SAP Business Technology Platform](/t5/c-khhcw49343/SAP%2BBTP%2BABAP%2Benvironment/pd-p/73555000100800001164)
* [ABAP RESTful Application Programming Model

  Software Product Function](/t5/c-khhcw49343/ABAP%2BRESTful%2BApplication%2BProgramming%2BModel/pd-p/7e44126e-7b27-471d-a379-df205a12b1ff)
* [ABAP Development

  Programming Tool](/t5/c-khhcw49343/ABAP%2BDevelopment/pd-p/833755570260738661924709785639136)
* [SAP Fiori Elements

  Software Product Function](/t5/c-khhcw49343/SAP%2BFiori%2BElements/pd-p/ed5c1ef6-932f-4c19-b2ba-1be375109ff5)

View products (7)

### Introduction:

The draft is a common feature in almost all applications, irrespective of whether it is an SAP or Non-SAP application. A draft is nothing but a temporary version of a business entity that has not yet been explicitly saved as an active version.

For more details in the context of

Fiori application, check out <https://experience.sap.com/fiori-design-web/draft-handling/>

ABAP RAP application, check out <https://help.sap.com/docs/btp/sap-abap-restful-application-programming-model/draft>

###

### Prerequisites:

This Blog Post explains Customizing Draft behavior in ABAP RAP Model with a business example and prerequisites are having knowledge of building fiori Applications using the RAP model. I strongly recommend visiting the [community page](https://community.sap.com/topics/abap/rap). It is a framework recently introduced to build cloud-ready Fiori applications using ABAP.

The RAP Model supports Managed, Unmanaged, and Mixed ( Managed with additional save, Managed with unmanaged save)  implementation scenarios. The draft feature can be enabled simply in all the implementation approaches and it is handled by the framework whether it is an unmanaged or a managed scenario. [See the documentation](https://help.sap.com/docs/btp/sap-abap-restful-application-programming-model/draft#draft-in-the-abap-restful-application-programming-model)

An application developer does not need to care about how draft data is written to the draft database table. As a default behavior, Framework copies the complete data from active persistence into a draft instance on which the user can continue working on it.

Of course, there will be some business requirements to tweak this default behavior and adjust the data on the UI for better visibility or control of the features on the UI. So the framework has some extension points to the application and it is the area of interest in this blogpost.

###

### Business Example:

In a purchase document application, There are three fields Status, Version, and Supplier along with other header information and its items, attachments, etc. The document can be switched into Edit mode in a few statuses like Saved, Rejected, Released/Approved.

As default behavior, the Active instance is copied into the draft instance with the same data. But the business requirement is

|
 Feature |
 Case when Status is SAVED |
 Case when Status is RELEASED/APPROVED |

|
 Field - Version Number |
 Not to be Incremented |
 Increment with 1 |

|
 Field - Supplier |
 Changeable |
 Not changeable |

### Implementation:

Let's see the implementation steps ( Detailed steps can be found in the documentation ) :

1. Enable the draft feature and provide draft persistence in Behavior Definition using quick-fix.

   ```
   unmanaged implementation in class zbp_rk_i_pur_con_ud unique;

   strict;

   with draft;

   define behavior for ZRK_I_PUR_CON_UD alias PurCon

   draft table zrk_dt_pur_con_u

   lock master

   total etag LoclLastChangedAt

   authorization master ( instance , global )

   etag master LoclLastChangedAt

   {

     field ( numbering : managed, readonly ) ConUuid;

     create ;

     update ;

     delete ;

   }​
   ```

2. Make sure the required fields are defined and projected in the entities.

   ```
   @AccessControl.authorizationCheck: #CHECK

   @EndUserText.label: 'ZRK_I_PUR_CON_UD'

   define root view entity ZRK_I_PUR_CON_UD as select from zrk_t_pur_con as PurCon

   composition [0..*] of ZRK_I_PUR_CON_I as _PurConItem

   composition [0..*] of zrk_i_pur_con_att as Attachments

   ...

   {

       key con_uuid as ConUuid,

       @Consumption.semanticObject: 'PurCon'

       object_id as ObjectId,

   ....

       version_no as VersionNo,

       '' as ReleasedAtLeastOnce,

       @Semantics.user.createdBy: true

       created_by as CreatedBy,

       @Semantics.systemDateTime.createdAt: true

       created_at as CreatedAt,

    ...