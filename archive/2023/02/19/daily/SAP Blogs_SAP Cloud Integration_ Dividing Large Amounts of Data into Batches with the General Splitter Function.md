---
title: SAP Cloud Integration: Dividing Large Amounts of Data into Batches with the General Splitter Function
url: https://blogs.sap.com/2023/02/18/sap-cloud-integration-dividing-large-amounts-of-data-into-batches-with-the-general-splitter-function/
source: SAP Blogs
date: 2023-02-19
fetch_date: 2025-10-04T07:29:41.542281
---

# SAP Cloud Integration: Dividing Large Amounts of Data into Batches with the General Splitter Function

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Technology](/t5/technology/ct-p/technology)
* [Technology Blog Posts by Members](/t5/technology-blog-posts-by-members/bg-p/technology-blog-members)
* SAP Cloud Integration: Dividing Large Amounts of D...

Technology Blog Posts by Members

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/technology-blog-members/article-id/160462&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [SAP Cloud Integration: Dividing Large Amounts of Data into Batches with the General Splitter Function](/t5/technology-blog-posts-by-members/sap-cloud-integration-dividing-large-amounts-of-data-into-batches-with-the/ba-p/13552440)

![vbalko-claimate](https://avatars.profile.sap.com/d/3/idd32011e98e1bd427091598b43b2a6bb9efd322bdb126f709a83f8f89204fa9e3_small.jpeg "vbalko-claimate")

[vbalko-claimate](https://community.sap.com/t5/user/viewprofilepage/user-id/178477)

Contributor

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=technology-blog-members&message.id=160462)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/technology-blog-members/article-id/160462)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13552440)

‎2023 Feb 18
8:06 PM

[3
Kudos](/t5/kudos/messagepage/board-id/technology-blog-members/message-id/160462/tab/all-users "Click here to see who gave kudos to this post.")

12,513

* SAP Managed Tags
* [Cloud Integration](https://community.sap.com/t5/c-khhcw49343/Cloud%2520Integration/pd-p/67837800100800006801)
* [SAP Business Technology Platform](https://community.sap.com/t5/c-khhcw49343/SAP%2520Business%2520Technology%2520Platform/pd-p/73555000100700000172)

* [Cloud Integration

  SAP Integration Suite](/t5/c-khhcw49343/Cloud%2BIntegration/pd-p/67837800100800006801)
* [SAP Business Technology Platform

  Software Product](/t5/c-khhcw49343/SAP%2BBusiness%2BTechnology%2BPlatform/pd-p/73555000100700000172)

View products (2)

## Chapter 1: Introduction

If you are working with SAP Cloud Integration and need to process a large amount of messages, dividing them into batches can help improve performance and avoid errors. In this blog post, we will discuss how to use the General splitter function and its group attribute to split messages into batches.

## Chapter 2: Example iFlow

To use the General splitter function, you can create an iFlow in SAP Cloud Integration that includes a Splitter component. Here is an example iFlow that demonstrates how to use the General splitter function to split messages into batches.

![](/legacyfs/online/storage/blog_attachments/2023/02/2023-02-18-20_40_34-Cloud-Integration.png)

## Chapter 3: Setting Parameters and Input and Output XML

To use the General splitter function, you need to set the following parameters:

**XPath Expression:** This is the parameter, which contains xpath expression to the element on which, should be batch created..

**group:** This is the parameter, which contains maximum number of messages, that should be included in each batch.

Because it is general splitter, the surrounding elements are taken over to the each batch. In case of iterating splitter, the containing elements are lost.

Here is an example input XML:

```
  <Orders>

    <Order>

      <ID>1</ID>

      <Name>Order 1</Name>

      <Partner>Partner 1</Partner>

      <Amount>100</Amount>

    </Order>

    <Order>

      <ID>2</ID>

      <Name>Order 2</Name>

      <Partner>Partner 2</Partner>

      <Amount>200</Amount>

    </Order>

    <Order>

      <ID>3</ID>

      <Name>Order 3</Name>

      <Partner>Partner 3</Partner>

      <Amount>300</Amount>

    </Order>

  </Orders>
```

And here is an example output XML after splitting the messages into batches of 2 messages (group = 2):

```
  <Orders>

    <Order>

      <ID>1</ID>

      <Name>Order 1</Name>

      <Partner>Partner 1</Partner>

      <Amount>100</Amount>

    </Order>

    <Order>

      <ID>2</ID>

      <Name>Order 2</Name>

      <Partner>Partner 2</Partner>

      <Amount>200</Amount>

    </Order>

  </Orders>
```

## Chapter 4: Summary

Dividing a large amount of messages into batches can help improve performance and avoid errors when working with SAP Cloud Integration. The General splitter function and its group attribute make it easy to split messages into batches. By setting the group name and batch size parameters, you can divide your messages into batches and process them efficiently.

In this blog post, we provided an example iFlow that demonstrates how to use the General splitter function, as well as example XML that you can use to test the function with purchase orders.

This concludes our discussion on using the General splitter function in SAP Cloud Integration.

## Chapter 5: Final Thoughts

If you work with SAP Cloud Integration and deal with a high volume of messages, using the General splitter function can be a valuable tool to help optimize your processes. It can help to prevent errors and make your workflows more efficient.

In addition to the General splitter function, there are other components and tools available in SAP Cloud Integration that can help you to work with large amounts of data. These include data mapping and data transformation tools, as well as integration with other SAP and non-SAP systems.

By familiarizing yourself with these tools, you can make the most of your SAP Cloud Integration platform and streamline your workflows.

Disclaimer: This blog post can be also found on my other blog page: <https://vbalko.blogspot.com/2023/02/sap-cpi-tips-split-messages-to-batches.html>

General Splitter

* [general splitter](/t5/tag/general%20splitter/tg-p/board-id/technology-blog-members)
* [SAPTipsandTricks](/t5/tag/SAPTipsandTricks/tg-p/board-id/technology-blog-members)

1 Comment

You must be a registered user to add a comment. If you've already registered, sign in. Otherwise, register and sign in.

* [Comment](/plugins/common/feature/oidcss/sso_login_redirect/providerid/sap_ids_prompt?redirectreason=permissiondenied&referer=https%3A%2F%2Fcommunity.sap.com%2Ft5%2Ftechnology-blog-posts-by-members%2Fsap-cloud-integration-dividing-large-amounts-of-data-into-batches-with-the%2Fba-p%2F13552440%23comment-on-this)

Copy Link
![](https://community.sap.com/html/@EE5D5986E9F4E5657DCEACB7532B5C39/assets/bluesky-dark.svg)Bluesky
Linkedin

Related Content

* [Organizational Management in SAP S/4HANA HCM](/t5/technology-blog-posts-by-members/organizational-management-in-sap-s-4hana-hcm/ba-p/14234285)
  in [Technology Blog Posts by Members](/t5/technology-blog-posts-by-members/bg-p/technology-blog-members)  yesterday
* [Driving AI Adoption with BTP: Highlights](/t5/technology-blog-posts-by-sap/driving-ai-adoption-with-btp-highlights/ba-p/14233554)
  in [Technology Blog Posts by SAP](/t5/technology-blog-posts-by-sap/bg-p/technology-blog-sap)  yesterday
* [Transforming Healthcare Procurement: Lessons from Our S/4HANA MM Implementation](/t5/technology-q-a/transforming-healthcare-procurement-lessons-from-our-s-4hana-mm/qaq-p/14233251)
  in [Technology Q&A](/t5/technology-q-a/qa-p/technology-questions)  Thursday
* [SAP Service and Asset Manager 2405 - MDK Metadata Deployment Error in SAP BAS Environment](/t5/technology-q-a/sap-service-and-asset-manager-2405-mdk-metadata-deployment-error-in-sap-bas/qaq-p/14231957)
  in [Technology Q&A](/t5/tech...