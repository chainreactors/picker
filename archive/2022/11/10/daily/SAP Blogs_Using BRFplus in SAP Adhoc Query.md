---
title: Using BRFplus in SAP Adhoc Query
url: https://blogs.sap.com/2022/11/09/using-brfplus-in-sap-adhoc-query/
source: SAP Blogs
date: 2022-11-10
fetch_date: 2025-10-03T22:15:06.678854
---

# Using BRFplus in SAP Adhoc Query

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Technology](/t5/technology/ct-p/technology)
* [Technology Blog Posts by Members](/t5/technology-blog-posts-by-members/bg-p/technology-blog-members)
* Using BRFplus in SAP Adhoc Query

Technology Blog Posts by Members

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/technology-blog-members/article-id/162512&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [Using BRFplus in SAP Adhoc Query](/t5/technology-blog-posts-by-members/using-brfplus-in-sap-adhoc-query/ba-p/13564084)

![Binu_Jacob1](https://avatars.profile.sap.com/f/b/idfb8a635f05d60c0a249e8f69c2fac8b59fe8aa52e9b960178edfced237780e4e_small.jpeg "Binu_Jacob1")

[Binu\_Jacob1](https://community.sap.com/t5/user/viewprofilepage/user-id/56336)

Explorer

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=technology-blog-members&message.id=162512)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/technology-blog-members/article-id/162512)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13564084)

‎2022 Nov 09
6:45 PM

[4
Kudos](/t5/kudos/messagepage/board-id/technology-blog-members/message-id/162512/tab/all-users "Click here to see who gave kudos to this post.")

1,314

* SAP Managed Tags
* [NW ABAP Business Rule Framework (BRFplus)](https://community.sap.com/t5/c-khhcw49343/NW%2520ABAP%2520Business%2520Rule%2520Framework%2520%28BRFplus%29/pd-p/133205901943786179366163043997549)

* [NW ABAP Business Rule Framework (BRFplus)

  Software Product Function](/t5/c-khhcw49343/NW%2BABAP%2BBusiness%2BRule%2BFramework%2B%252528BRFplus%252529/pd-p/133205901943786179366163043997549)

View products (1)

SAP has two powerful frameworks to support a functional consultant. These are:

* BRFplus

* SAP Adhoc query.

In this blog I would like to share my experience in calling a BRFplus function within an SAP Adhoc query. This I hope with help in extending the reach that BRFplus and SAP Adhoc query can provide for your requirements.

**Scenario:**

I am using an Adhoc query based on a simple table based infoset to display a set of fields. The query reads data from a custom table used in a custom application developed with ABAP. Now in the underlying infoset used by the adhoc query, I have created an 'additional field' called 'staff' which is populated by a call to a BRFplus function.

Of course, there are other means to populate this additional field but the use of BRFplus is just to illustrate the power in using the combination of SAP Adhoc query with BRFplus.

**A: Create a simple BRFplus application:**

While this blog is focused mainly to show the use of both the above frameworks in tandem, I will not be going through in detail to create the brfplus artifacts. So only the high-level steps are shown.

**This involves:**

1. Creating an application in BRFplus (the transaction code is brfplus)

![](/legacyfs/online/storage/blog_attachments/2022/11/2022-11-07_140205.jpg)

2. Create the Function:

This function has the input of 'User' (based on field UserID) and outputs 'PERNR' (based on fied PERNR). The ruleset used (ZJB01RS) consists of a 'Rule' that reads table 'PA0105' (standard table in HCM) passing User (UserID) and Subtype and fetching PERNR from table PA0105.

![](/legacyfs/online/storage/blog_attachments/2022/11/2-3.jpg)

The RULESET called ZJB01RS.

![](/legacyfs/online/storage/blog_attachments/2022/11/3-1.jpg)

The Database lookup "FETCHPERNR" used in rule above.

![](/legacyfs/online/storage/blog_attachments/2022/11/4-2.jpg)

Once the BRFplus artifacts are saved and activated the 'simulation' to check the application is below.

![](/legacyfs/online/storage/blog_attachments/2022/11/5-2.jpg)

![](/legacyfs/online/storage/blog_attachments/2022/11/6-3.jpg)

Now that the BRFplus application works, the 'Class' to be generated as below. Use the "Generate Function" to do this under the "Code Generation' tab

![](/legacyfs/online/storage/blog_attachments/2022/11/7-2.jpg)

Now to display the "code template' to be used in our infoset in the SAP Adhoc query. Click on the "Create Code Template' button (see the above image).

The code template is as shown below. Copy this code to be later used in our 'INFOSET'.

![](/legacyfs/online/storage/blog_attachments/2022/11/8-2.jpg)

**B: The SAP ADHOC Query:**

The adhoc query creation has 2 steps:

**1.Create the Infoset**:

The infoset created using transaction 'SQ02' is based on a simple table as shown below.

![](/legacyfs/online/storage/blog_attachments/2022/11/9-1.jpg)

I have added the required fields from the table and also create an 'Additional field' called 'staff'.

![](/legacyfs/online/storage/blog_attachments/2022/11/10-2.jpg)

I will populate this field called 'Staff' using the brfplus function created earlier. Right click on the field "staff" and go to "field code".

Copy and paste the 'Code Template"" that we created in the brfplus to the below and make minor modifications in the code.

![](/legacyfs/online/storage/blog_attachments/2022/11/11-1.jpg)

The modifications needed to read the data from the brfplus is below:

1. There is a field in the infoset called "Name of the person who changed the object". This field is of the type "UserID'. Use the technical name of the field and assign to the input parameter of the code.![](/legacyfs/online/storage/blog_attachments/2022/11/12-1.jpg)

2. Similarly assign the output parameter as below. Field 'Staff' is assigned to the importing field 'ea\_result".

```
  TRY.

      cl_fdt_function_process=>process( EXPORTING iv_function_id = lv_function_id

                                                  iv_timestamp   = lv_timestamp

                                        IMPORTING ea_result      = staff

                                        CHANGING  ct_name_value  = lt_name_value ).

      CATCH cx_fdt into lx_fdt.
```

Save and Generate the infoset and assign to the appropriate 'User Group".

**2. Create the query based on the above infoset.**

Create the Query based on the above infoset

![](/legacyfs/online/storage/blog_attachments/2022/11/13-1.jpg)

The fields used

![](/legacyfs/online/storage/blog_attachments/2022/11/14-1.jpg)

Now execute the query. You will see the field "Staff" getting populated from the brfplus as below.

![](/legacyfs/online/storage/blog_attachments/2022/11/15-1.jpg)

This blog post only provides a high-level overview of the creation of the BRFplus application and SAP Query since the idea was to only provide how BRFplus can be used in SAP Query and expand the reach of these two frameworks. Should you need details on the creation of the above artifacts, I am happy to provide.

If you have any questions, you can comment below. I would love to hear from you on how you were able to use this option to provide more value to your business.

* [SAP Adhoc Query](/t5/tag/SAP%20Adhoc%20Query/tg-p/board-id/technology-blog-members)

2 Comments

You must be a registered user to add a comment. If you've already registered, sign in. Otherwise, register and sign in.

* [Comment](/plugins/common/feature/oidcss/sso_login_redirect/providerid/sap_ids_prompt?redirectreason=permissiondenied&referer=https%3A%2F%2Fcommunity.sap.com%2Ft5%2Ftechnology-blog-posts-by-members%2Fusing-brfplus-in-sap-adhoc-query%2Fba-p%2F13564084%23comment-on-this)

Copy Link
![](https://community.sap.com/html/@EE5D598...