---
title: Scenario: Data Extraction via the Custom CDS View application
url: https://blogs.sap.com/2023/03/10/scenario-data-extraction-via-the-custom-cds-view-application/
source: SAP Blogs
date: 2023-03-11
fetch_date: 2025-10-04T09:15:57.465873
---

# Scenario: Data Extraction via the Custom CDS View application

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Technology](/t5/technology/ct-p/technology)
* [Technology Blog Posts by Members](/t5/technology-blog-posts-by-members/bg-p/technology-blog-members)
* Scenario: Data Extraction via the Custom CDS View ...

Technology Blog Posts by Members

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/technology-blog-members/article-id/162995&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [Scenario: Data Extraction via the Custom CDS View application](/t5/technology-blog-posts-by-members/scenario-data-extraction-via-the-custom-cds-view-application/ba-p/13566942)

![guruL](https://avatars.profile.sap.com/9/7/id973ee8727e929bb72eb3ef2e73d603e8f6586830fef5eb83c3eefa788a8e617b_small.jpeg "guruL")

![Product and Topic Expert](/html/@138D6F765B60D7FC0168643DE27D8A68/rank_icons/sap-logo-small-14px.png "Product and Topic Expert")
[guruL](https://community.sap.com/t5/user/viewprofilepage/user-id/125249)

Product and Topic Expert

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=technology-blog-members&message.id=162995)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/technology-blog-members/article-id/162995)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13566942)

‎2023 Mar 10
8:38 PM

[3
Kudos](/t5/kudos/messagepage/board-id/technology-blog-members/message-id/162995/tab/all-users "Click here to see who gave kudos to this post.")

8,180

* SAP Managed Tags
* [SAP HANA Cloud](https://community.sap.com/t5/c-khhcw49343/SAP%2520HANA%2520Cloud/pd-p/73554900100800002881)

* [SAP HANA Cloud

  Software Product](/t5/c-khhcw49343/SAP%2BHANA%2BCloud/pd-p/73554900100800002881)

View products (1)

**Introduction section: -**

Extracting data in mass from SAP S/4HANA using custom CDS view has multiple use cases. In this blog, let’s look at the steps for creating a custom CDS (Core Data Service) view that is enabled for data extraction with associations, using the **Custom CDS Views** application.

**Prerequisite: -**

* To open the Custom CDS View app, the key user has to be assigned to a business role being part of business catalog “Extensibility – Custom CDS Views” (ID:SAP\_CORE\_BC\_EXT\_CCV).

The role “Analytics Specialist” (ID: SAP\_BR\_ANALYTICS\_SPECIALIST) is one example.

**Steps: -**

1. Open the **Custom CDS Views**

![](/legacyfs/online/storage/blog_attachments/2023/03/Picture1-16.png)

Custom CDS View tile

2. Choose **Create** to create the custom CDS view.

![](/legacyfs/online/storage/blog_attachments/2023/03/Picture2-12.png)

3. In the dialog box, enter the required details. Select **Data Extraction** from the **Scenario** drop down list and then choose **Create**.

![](/legacyfs/online/storage/blog_attachments/2023/03/Picture3-12.png)

Now the custom CDS view is enabled as a data extraction custom CDS view.

4. On the **Select Primary Data Source** screen, select the primary data source. For example, I\_AcademicTitle.

![](/legacyfs/online/storage/blog_attachments/2023/03/Picture4-6.png)

5. Choose **Check** to check for any errors.

![](/legacyfs/online/storage/blog_attachments/2023/03/Picture5-10.png)

      Once the check is completed, a message is displayed stating that the check is now complete.

![](/legacyfs/online/storage/blog_attachments/2023/03/Picture6-9.png)

Primary data source is now added to the custom CDS view.

6. If you don’t need associated data source, then proceed with step number 9. Otherwise, choose the **Add** button and select **Associated Data Sources** from the dropdown list.

.

![](/legacyfs/online/storage/blog_attachments/2023/03/Picture7-10.png)

Select the associated data source as per your requirement. For example, I\_AcademicTitleText, and then choose **OK**.

![](/legacyfs/online/storage/blog_attachments/2023/03/Picture8-9.png)

7. Choose the **Join Condition** icon to maintain the join conditions between primary data source and associated data source.

![](/legacyfs/online/storage/blog_attachments/2023/03/Picture9-6.png)

8. Check for errors in the custom CDS view as shown in step 5

9. If there are no errors, choose Publish to publish the custom CDS view.

![](/legacyfs/online/storage/blog_attachments/2023/03/Picture10-5.png)

The custom CDS view is now ready for data extraction.

![](/legacyfs/online/storage/blog_attachments/2023/03/Picture11-7.png)

**Note: -**

* Only full-load extraction is supported for the custom CDS views created using the Data Extraction scenario. Delta extraction isn't supported.

**Summary: -**

With the Data Extraction scenario option in Custom CDS View application, Data extraction from SAP S/4HANA cloud system to other (BW) systems is possible using communication channel for custom CDS view.

**Further references and related blogs: -**

* [[SAP Help] Data Extraction](https://help.sap.com/docs/SAP_S4HANA_CLOUD/0f69f8fb28ac4bf48d2b57b9637e81fa/2f8f8f549ab4472b97b7f90a0ee28291.html?locale=en-US&q=data%20extraction)

* [[Blog] CDS based data extraction – Part I Overview](https://blogs.sap.com/2019/12/13/cds-based-data-extraction-part-i-overview/)

* [[Blog] CDS based data extraction – Part II Delta Handling](https://blogs.sap.com/2019/12/16/cds-based-data-extraction-part-ii-delta-handling/)

* [[Blog] CDS based data extraction – Part III Miscellaneous](https://blogs.sap.com/2019/12/20/cds-based-data-extraction-part-iii-miscellaneous/)

* [custom cds views](/t5/tag/custom%20cds%20views/tg-p/board-id/technology-blog-members)
* [data extraction](/t5/tag/data%20extraction/tg-p/board-id/technology-blog-members)

1 Comment

You must be a registered user to add a comment. If you've already registered, sign in. Otherwise, register and sign in.

* [Comment](/plugins/common/feature/oidcss/sso_login_redirect/providerid/sap_ids_prompt?redirectreason=permissiondenied&referer=https%3A%2F%2Fcommunity.sap.com%2Ft5%2Ftechnology-blog-posts-by-members%2Fscenario-data-extraction-via-the-custom-cds-view-application%2Fba-p%2F13566942%23comment-on-this)

Copy Link
![](https://community.sap.com/html/@EE5D5986E9F4E5657DCEACB7532B5C39/assets/bluesky-dark.svg)Bluesky
Linkedin

Related Content

* [Project-Based Services in SAP S/4HANA](/t5/technology-blog-posts-by-members/project-based-services-in-sap-s-4hana/ba-p/14234290)
  in [Technology Blog Posts by Members](/t5/technology-blog-posts-by-members/bg-p/technology-blog-members)  yesterday
* [Using Joule’s Async Feature to Communicate with a Custom BTP App](/t5/technology-blog-posts-by-sap/using-joule-s-async-feature-to-communicate-with-a-custom-btp-app/ba-p/14231021)
  in [Technology Blog Posts by SAP](/t5/technology-blog-posts-by-sap/bg-p/technology-blog-sap)  Tuesday
* [Adobe Form preview in S4 Cloud](/t5/technology-q-a/adobe-form-preview-in-s4-cloud/qaq-p/14230965)
  in [Technology Q&A](/t5/technology-q-a/qa-p/technology-questions)  Monday
* [A Hitchhiker's Guide to SAP Fiori User Experience and its Technologies – 2025 edition](/t5/technology-blog-posts-by-sap/a-hitchhiker-s-guide-to-sap-fiori-user-experience-and-its-technologies-2025/ba-p/14230556)
  in [Technology Blog Posts by SAP](/t5/technology-blog-posts-by-sap/bg-p/technology-blog-sap)  Monday
* [🚀 Remember the pioneering days of SAP ECC?](/t5/technology-blog-posts-by-members/remember-the-pioneering-days-of-sap-ecc/ba-p/14229517)
  in [Technology Blog Posts by Members](/t5/technology-blog-po...