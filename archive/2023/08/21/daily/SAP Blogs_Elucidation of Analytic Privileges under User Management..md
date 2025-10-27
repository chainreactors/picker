---
title: Elucidation of Analytic Privileges under User Management.
url: https://blogs.sap.com/2023/08/20/elucidation-of-analytic-privileges-under-user-management./
source: SAP Blogs
date: 2023-08-21
fetch_date: 2025-10-04T11:59:49.873170
---

# Elucidation of Analytic Privileges under User Management.

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Technology](/t5/technology/ct-p/technology)
* [Technology Blog Posts by Members](/t5/technology-blog-posts-by-members/bg-p/technology-blog-members)
* Elucidation of Analytic Privileges under User Mana...

Technology Blog Posts by Members

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/technology-blog-members/article-id/165453&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [Elucidation of Analytic Privileges under User Management.](/t5/technology-blog-posts-by-members/elucidation-of-analytic-privileges-under-user-management/ba-p/13580609)

![akashkannan22](https://avatars.profile.sap.com/3/d/id3d61c73bff526eb7a004a12e48fc11e5f970071eb1f04b5545806dd6a291ecd2_small.jpeg "akashkannan22")

[akashkannan22](https://community.sap.com/t5/user/viewprofilepage/user-id/847958)

Explorer

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=technology-blog-members&message.id=165453)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/technology-blog-members/article-id/165453)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13580609)

‎2023 Aug 20
11:57 AM

[3
Kudos](/t5/kudos/messagepage/board-id/technology-blog-members/message-id/165453/tab/all-users "Click here to see who gave kudos to this post.")

800

* SAP Managed Tags
* [SAP Analytics Cloud, data modeling](https://community.sap.com/t5/c-khhcw49343/SAP%2520Analytics%2520Cloud%252C%2520data%2520modeling/pd-p/3ecbe2ed-7fe9-4831-924a-77987d1a4259)
* [SAP HANA](https://community.sap.com/t5/c-khhcw49343/SAP%2520HANA/pd-p/73554900100700000996)
* [BW SAP HANA Modeling Tools (Eclipse)](https://community.sap.com/t5/c-khhcw49343/BW%2520SAP%2520HANA%2520Modeling%2520Tools%2520%28Eclipse%29/pd-p/362090813548382577915604715460332)
* [SAP HANA multi-model processing](https://community.sap.com/t5/c-khhcw49343/SAP%2520HANA%2520multi-model%2520processing/pd-p/ca0132d1-ba23-4d3c-a7ef-5bcbd1cf01a3)

* [SAP HANA

  Software Product](/t5/c-khhcw49343/SAP%2BHANA/pd-p/73554900100700000996)
* [BW SAP HANA Modeling Tools (Eclipse)

  Software Product Function](/t5/c-khhcw49343/BW%2BSAP%2BHANA%2BModeling%2BTools%2B%252528Eclipse%252529/pd-p/362090813548382577915604715460332)
* [SAP HANA multi-model processing

  Software Product Function](/t5/c-khhcw49343/SAP%2BHANA%2Bmulti-model%2Bprocessing/pd-p/ca0132d1-ba23-4d3c-a7ef-5bcbd1cf01a3)
* [SAP Analytics Cloud, data modeling

  Software Product Function](/t5/c-khhcw49343/SAP%2BAnalytics%2BCloud%25252C%2Bdata%2Bmodeling/pd-p/3ecbe2ed-7fe9-4831-924a-77987d1a4259)

View products (4)

Hello all,

I'll elucidate the analytic privileges in this documentation by creating a graphical view(Calculation view).

let us start...

First, what is Analytic privilege?

**Analytic Privileges:**

Analytic privileges grant different users access to different portions of data in the same view based on their business role. Within the definition of an analytic privilege, the conditions that control which data users see are either contained in an XML document or defined using SQL.

In this document, I'm not going to use SQL statements. So it's the XML-based Analytic privilege.

**Note:** Analytic Privileges can be used only activated once. If you need to change the Analytic Privilege after it has been successfully activated, you will have to delete it and re-create it from scratch.

In the following we are going to grant Analytic Privileges to user K2885 which will finally allow reporting off the Analytic and Calculation Views. We are restricting access to only Company Code ‘1000’.

**Procedure:**

1. Create a Calculation view under the “Material” package.

* Right Click on Calculation View > New

![](/legacyfs/online/storage/blog_attachments/2023/08/f2-2.png)

Figure1

2. Enter “ZCV\_MARA” for the name of the view

* Select EKKO as a table and choose some field.

* Because it's a Calculation View, any measure field is mandatory.

* In this, I'm using Classic Analytic Privilege.

3. Save and Activate the Analytical View.

![](/legacyfs/online/storage/blog_attachments/2023/08/f2-3.png)

Figure2

4. Create an Analytic Privilege under the same package “Material”

* Right Click on Analytic Privilege > New

![](/legacyfs/online/storage/blog_attachments/2023/08/f3-2.png)

Figure 3

5. Enter name ZAN\_EKKO\_1000

* Enter a description

* Click “Next”

![](/legacyfs/online/storage/blog_attachments/2023/08/f4-2.png)

Figure 4

6. Select the ZCV\_MARA Views

* Click Add

* Click Finish

7. Implementing the privilege is now done in three steps:

1) Select further views for which this privilege should be valid (optional).

2) Select the validity from and to date.

3) Select attributes on which a restriction shall be defined.

4) Define value restrictions for the attributes selected in 3.

![](/legacyfs/online/storage/blog_attachments/2023/08/f5-3.png)

Figure 5

8. Add the field “BUKRS” to the list of “Associated Attributes Restrictions”.

* Click the corresponding “Add” button

* Select field “BUKRS” from the presented field list

* Click “OK”.

![](/legacyfs/online/storage/blog_attachments/2023/08/figure-6.png)

Figure 6

9. Define the value restriction for field “BUKRS”

* Click the “Add” button for “Assign Restrictions” (this increases the counter for the number of restrictions for BUKRS)

* Click into the “Value” field in “Assign Restrictions”. Click the “…”-icon.

* In the search window, search for Company Code 1000

* Select the Company Code from  the search list

* Click OK

![](/legacyfs/online/storage/blog_attachments/2023/08/f7-2.png)

Figure 7

10. Save and Activate Analytic Privilege.

That's all guys, we have successfully completed an analytic privilege.

***Assign Analytic Privilege ZAN\_EKKO\_1000 to user K2885.***

11. Open the User Editor for user USER01 under Security > Users

* In that Editor, switch to tab “Analytic Privileges”

![](/legacyfs/online/storage/blog_attachments/2023/08/f8-3.png)

Figure 8

12. Click the green “+”-icon

* From the list of “Matching items”, select privilege “Material/ZAN\_EKKO\_1000”

* Click “OK”

![](/legacyfs/online/storage/blog_attachments/2023/08/f9-2.png)

Figure 9

Regards,

Akash Kannan K

Reference:

[Analytic Privilege](https://help.sap.com/docs/SAP_HANA_ONE/1c837b3899834ddcbae140cc3e7c7bdd/db08ea0cbb571014a386f851122958b2.html)

* [AnalayticPrivileges](/t5/tag/AnalayticPrivileges/tg-p/board-id/technology-blog-members)
* [authorization](/t5/tag/authorization/tg-p/board-id/technology-blog-members)
* [s4hana saphana intelligententerprise](/t5/tag/s4hana%20saphana%20intelligententerprise/tg-p/board-id/technology-blog-members)
* [usermanagement](/t5/tag/usermanagement/tg-p/board-id/technology-blog-members)

You must be a registered user to add a comment. If you've already registered, sign in. Otherwise, register and sign in.

* [Comment](/plugins/common/feature/oidcss/sso_login_redirect/providerid/sap_ids_prompt?redirectreason=permissiondenied&referer=https%3A%2F%2Fcommunity.sap.com%2Ft5%2Ftechnology-blog-posts-by-members%2Felucidation-of-analytic-privileges-under-user-management%2Fba-p%2F13580609%23comment-on-this)

Copy Link
![](https://community.sap.com/html/@EE5D5986E9F4E5657DCEACB7532B5C39/assets/bluesky-dark.svg)Bluesky
Linkedin

Related Content

* [SAP IQ to SAP HANA Cloud, Data Lake Migration Overview](/t5/technology-blog-posts-by-sap/...