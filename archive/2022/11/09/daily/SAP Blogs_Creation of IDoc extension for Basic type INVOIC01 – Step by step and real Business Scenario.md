---
title: Creation of IDoc extension for Basic type INVOIC01 – Step by step and real Business Scenario
url: https://blogs.sap.com/2022/11/08/creation-of-idoc-extension-for-basic-type-invoic01-step-by-step-and-real-business-scenario/
source: SAP Blogs
date: 2022-11-09
fetch_date: 2025-10-03T22:05:19.562129
---

# Creation of IDoc extension for Basic type INVOIC01 – Step by step and real Business Scenario

* [SAP Community](/)
* [Groups](/t5/groups/ct-p/groups)
* [Interest Groups](/t5/interest-groups/ct-p/interests)
* [Application Development and Automation](/t5/application-development-and-automation/gh-p/application-development)
* [Blog Posts](/t5/application-development-and-automation-blog-posts/bg-p/application-developmentblog-board)
* Creation of IDoc extension for Basic type INVOIC01...

Application Development and Automation Blog Posts

Learn and share on deeper, cross technology development topics such as integration and connectivity, automation, cloud extensibility, developing at scale, and security.

All communityThis groupBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/application-developmentblog-board/article-id/46820&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

#### We have launched new [Developer forums/groups](https://community.sap.com/t5/developers/ct-p/developers) in the SAP Community. If you are here to publish developer- or SAP-technology related blog posts, please check out our new groups instead. You can find more information about the developer forums in this [What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147).

Read only

## [Creation of IDoc extension for Basic type INVOIC01 - Step by step and real Business Scenario](/t5/application-development-and-automation-blog-posts/creation-of-idoc-extension-for-basic-type-invoic01-step-by-step-and-real/ba-p/13555297)

![elson_meco](https://avatars.profile.sap.com/d/c/iddcc24474adb8fae737ca772d461e120ac09c096204840dea8d2ef1fc17bbcf27_small.jpeg "elson_meco")

[elson\_meco](https://community.sap.com/t5/user/viewprofilepage/user-id/17285)

Explorer

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=application-developmentblog-board&message.id=46820)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/application-developmentblog-board/article-id/46820)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13555297)

‎2022 Nov 08
8:20 PM

[8
Kudos](/t5/kudos/messagepage/board-id/application-developmentblog-board/message-id/46820/tab/all-users "Click here to see who gave kudos to this post.")

32,466

* SAP Managed Tags
* [ABAP Development](https://community.sap.com/t5/c-khhcw49343/ABAP%2520Development/pd-p/833755570260738661924709785639136)

* [ABAP Development

  Programming Tool](/t5/c-khhcw49343/ABAP%2BDevelopment/pd-p/833755570260738661924709785639136)

View products (1)

In this blog post, I will describe the steps I have followed to create an extension for the basic type INVOIC01. I will also illustrate the actual business requirement and what was requested.

First, I know that there are a lot of materials out there for how to create an IDoc extension and I won't get into very tiny details and will focus more on my problem.

So, to give a general background in transaction NACE we have done the configuration for Application V3 (Billing), OutputType (ZRDO), and Processing routines: Medium - EDI, Program - RSNASTED, FORM routine - EDI\_PROCESSING. But surely you know this part well. Anyway here is a print screen:

![](/legacyfs/online/storage/blog_attachments/2022/10/NACE.png)

Now the Basic type INVOIC01 can be configured in transaction VF03 where we create billing documents for a customer. In the images to follow I will show the output configuration in VF03 and the IDoc from transaction WE02

![](/legacyfs/online/storage/blog_attachments/2022/10/2.VF03-1.png)

![](/legacyfs/online/storage/blog_attachments/2022/10/3.WE02.png)

You can see that above I have highlighted the value of field BELNR = '0090072614' for one of the segments E1EDK02 and more exactly the one where QUALF = '087' (you can check it for yourself what that means, but to avoid you the pain it is 'Reference Document Number Billing Doc.'). The above image is important because there lies the problem.

The document I have shown in transaction VF03 that generates this IDoc is a Credit Memo and is generated following the Invoice '0090072614'. Yes, you are right: "The one in the segment E1EDK02", but this image will help you get a more clear idea:

![](/legacyfs/online/storage/blog_attachments/2022/10/4.Document-Flow.png)

The customer requested two additional fields (a document number and its date), except the number of the invoice and this information, was to be added to a child segment under E1EDK02. The value of the fields had to be retrieved following this rule:

* If in a custom tab "Additional fields" the values were entered use those, otherwise use the number and date of the accounting document.

![](/legacyfs/online/storage/blog_attachments/2022/10/5.Ref-doc..png)

And again the image shows that the first check is true and so the values are taken directly from the invoice without needing the accounting document.

Now, the steps to create this extension, without going very much into detail as the material out there is plenty to help you. So, I will just list the list of steps. In the end the most interesting part for the ABAP enthusiasts and the end result.

1. Creation of the custom segment Z1EDK02 in WE31

2. Creation of extension IDoc ZINVOIC1 in WE30 from the basic type INVOIC01

3. Creation of the Logical Message Type ZINVOIC in WE81

4. Assigning Logical Message Type ZINVOIC to Extension IDoc Type ZINVOIC1 in WE82

5. Assigning the Logical Message Typer to the Partner Profile in WE20

6. Finding and implementing the Customer Exit to write the logic to add the new segment

Now, for the last two points, I will make an exception and go into more detail as it helps to find where to implement our custom logic.

In WE20 we have done this configuration for our partner profile:

![](/legacyfs/online/storage/blog_attachments/2022/10/6.WE20-1.png)

If you double-click on the Process code we can find the Function Module to generate the IDoc and where we should insert our code, but don't worry as I have provided below all the screens from one step to the other:

![](/legacyfs/online/storage/blog_attachments/2022/10/7.Code1_.png)

![](/legacyfs/online/storage/blog_attachments/2022/10/8.Code2_.png)

As we are the INCLUDE I have implemented the code to add this new segment and I think that the logic is quite simple. First we check for the additional data in the invoice and if they aren't there to be found we check in BKPF. Only if found in any of them is the segment added.

```
* Extension of IDoc INVOIC01 - Logic to populate the new segment 'Z1EDK02'

DATA: lv_nr_fapiao   TYPE zznr_fapiao,

      lv_dt_fapiao   TYPE zzdt_fapiao.

DATA: ls_edidd TYPE edidd,

      ls_z1edk03 TYPE z1edk02.

IF int_edidd-segnam = 'E1EDK02'.

  CLEAR: e1edk02, bkpf.

  MOVE int_edidd-sdata TO e1edk02.

  IF e1edk02-qualf = '087'.

    ls_edidd-segnam = 'Z1EDK02'.

*   Invoice data for new additional custom tab

    CLEAR: lv_nr_fapiao, lv_dt_fapiao.

    SELECT SINGLE zznr_fapiao zzdt_fapiao

      INTO ( lv_nr_fapiao, lv_dt_fapiao )

      FROM vbrk WHERE vbeln = e1edk02-belnr.

    IF lv_nr_fapiao IS NOT INITIAL AND lv_dt_fapiao IS NOT INITIAL.

      ls_z1edk03-belnr = lv_nr_fapiao.

      ls_z1edk03-bldat = lv_dt_fapiao.

      MOVE ls_z1edk03 TO ls_edidd-sdata.

      APPEND ls_edidd TO int_edidd[]. "Addition of a new segment under 'E1EDK02'

    ELSE.

      "Read from BKPF to find the accounting document

      SELECT SINGLE * FROM bkpf

        WHERE awtyp = 'VBRK' AND awkey = e1edk02-belnr.

      IF sy-subrc = 0.

        ls_z1edk03-belnr = bkpf-belnr.

        ls_z1edk03-bldat = bkpf-bldat.

        MOVE ls_z1edk03 TO ls_edidd-sdata.

        APPEND ls_edidd TO int_edidd[]. "Addition of a new segment under '...