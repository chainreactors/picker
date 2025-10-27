---
title: Automatic Idoc Generation while Creating Purchase Order
url: https://blogs.sap.com/2023/03/20/automatic-idoc-generation-while-creating-purchase-order/
source: SAP Blogs
date: 2023-03-21
fetch_date: 2025-10-04T10:08:29.931711
---

# Automatic Idoc Generation while Creating Purchase Order

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Enterprise Resource Planning](/t5/enterprise-resource-planning/ct-p/erp)
* [ERP Blog Posts by Members](/t5/enterprise-resource-planning-blog-posts-by-members/bg-p/erp-blog-members)
* Automatic Idoc Generation while Creating Purchase ...

Enterprise Resource Planning Blog Posts by Members

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/erp-blog-members/article-id/67330&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [Automatic Idoc Generation while Creating Purchase Order, Nace/Output type, Partner Profile, IDOC Extension](/t5/enterprise-resource-planning-blog-posts-by-members/automatic-idoc-generation-while-creating-purchase-order-nace-output-type/ba-p/13554090)

![zunaid_hingora2](https://avatars.profile.sap.com/4/f/id4fd83b9d607850a6a2fa35e1ca2bf76e17e320d8521fa0a69c170997a5ad8111_small.jpeg "zunaid_hingora2")

[zunaid\_hingora2](https://community.sap.com/t5/user/viewprofilepage/user-id/200731)

Active Contributor

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=erp-blog-members&message.id=67330)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/erp-blog-members/article-id/67330)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13554090)

‎2023 Mar 20
9:41 PM

[1
Kudo](/t5/kudos/messagepage/board-id/erp-blog-members/message-id/67330/tab/all-users "Click here to see who gave kudos to this post.")

8,778

* SAP Managed Tags
* [MM (Materials Management)](https://community.sap.com/t5/c-khhcw49343/MM%2520%28Materials%2520Management%29/pd-p/477297786799213261950044802925335)
* [User Interface](https://community.sap.com/t5/c-khhcw49343/User%2520Interface/pd-p/378427990965467211484671270864901)

* [MM (Materials Management)

  Software Product Function](/t5/c-khhcw49343/MM%2B%252528Materials%2BManagement%252529/pd-p/477297786799213261950044802925335)
* [User Interface

  Topic](/t5/c-khhcw49343/User%2BInterface/pd-p/378427990965467211484671270864901)

View products (2)

Hi Friends,

Recently i got a chance to work on one interface where PO is required to be sent to Third Party System. This transmission was done through IDOC. In this blog, i will show you the manual steps to generate IDOC for PO and also Automatic settings.

***Note** - In this blog i have shown example for specific vendor 1234. But in Partner profile setup i have used LogitechSYS. Difference is explained in detail in later steps.*

For videos of all my blogs, please click on below link.

<https://www.youtube.com/channel/UCx5F7mhmIYye8ETY3cM5zQQ>

Below is the scope of this blog.

1. Manual Steps for IDOC generation for PO

2. Automatic IDOC generation for PO.

3. NACE Configuration.

4. Partner Profile Configuration - WE20

5. IDOC Extension

**IDOC Generation**

1. Manual IDOC Generation

Go to ME23N. Open purchase order. You can see Messages Tab. Click on that button.![](/legacyfs/online/storage/blog_attachments/2023/03/Picture1-34.png)

If you see below IDOC is already Created. Status is green. It means IDOC generation is completed. But how is this done. First, I will explain you manual process from PO. Then I will take you to MN05 to make settings for automatic generation![](/legacyfs/online/storage/blog_attachments/2023/03/Picture2-29.png)

Make PO in Change mode and come to below screen. Enter fields for yellow line as shown below. Click on Further Data. If you see the Function it is VN. Why VN is selected and what is the difference between VN and LS?

* VN is selected when PO is to be sent to specific vendors. For e.g. you have 1000 plus vendors and only 10 vendors to be provided PO through IDOC than Use VN.

* LS is selected when PO is transmitted to third party System. For e.g. your organization is using third party software to create POs, than configure system under LS. POs for all vendor will be created through this setting.

![](/legacyfs/online/storage/blog_attachments/2023/03/Picture3-22.png)

Select the option as shown below and come back.![](/legacyfs/online/storage/blog_attachments/2023/03/Picture4-16.png)

Click on Save button.![](/legacyfs/online/storage/blog_attachments/2023/03/Picture5-19.png)

After saving, click on Messages and see below line. Its green. Click on processing log.![](/legacyfs/online/storage/blog_attachments/2023/03/Picture6-17.png)

Idoc number is displayed. Copy that idoc number and go to WE02. It will be generated.![](/legacyfs/online/storage/blog_attachments/2023/03/Picture7-19.png)

2. Automatic Generation

Go to MN05. Provide output type and Press Enter. Now question is where this output type is comes from? It comes from NACE transaction code. MM consultants can guide you through this process.![](/legacyfs/online/storage/blog_attachments/2023/03/Picture8-16.png)

You will have multiple option. I have created for 1st option but prefer 2nd one. Keep it very simpler.![](/legacyfs/online/storage/blog_attachments/2023/03/Picture9-11.png)

Provide details as below and execute.![](/legacyfs/online/storage/blog_attachments/2023/03/Picture10-9.png)

Provide below inputs and save. Now you will be able to generate IDOC automatically when PO is saved.![](/legacyfs/online/storage/blog_attachments/2023/03/Picture11-13.png)

Below screenshot is for LS Function![](/legacyfs/online/storage/blog_attachments/2023/03/Picture12-11.png)

**Nace Configuration**

Now let us understand from where values in below screenshots are coming. There are 3 values you can see

* ZPO

* VN or LS (Not in screenshot, but in above screenshot)

* Partner

![](/legacyfs/online/storage/blog_attachments/2023/03/Picture1-39.png)

Go to Transaction code NACE. Click on EF as shown below screenshot. Click on Output types.

![](/legacyfs/online/storage/blog_attachments/2023/03/Picture2-36.png)

Click on Output types and click on New Entries. This is already configured so ‘New Entries’ Won’t Appear.![](/legacyfs/online/storage/blog_attachments/2023/03/Picture3-28.png)

Click as shown in screenshot and select your languages. Just do F4 and select. Its standard![](/legacyfs/online/storage/blog_attachments/2023/03/Picture4-22.png)

Click on Processing Routines and select the entries.![](/legacyfs/online/storage/blog_attachments/2023/03/Picture5-24.png)

Click on Partner function. And maintain the entries. You can select your own entries. ￼![](/legacyfs/online/storage/blog_attachments/2023/03/Picture6-22.png)

Click on Procedures. You will see below screen. Select the line as shown below. ￼![](/legacyfs/online/storage/blog_attachments/2023/03/Picture7-23.png)

Click on Control. Click on New Entries and Select EDI Purchase order. Give the Step number.![](/legacyfs/online/storage/blog_attachments/2023/03/Picture8-20.png)

Note – After this configuration you will be able to see the ZPO entry in MN05.

**Partner Profile Configuration**

Go to WE20. See below screen. We have created the Partner profile. This is must for Idoc Configuration. If this is not done, idoc will fail.

* If you see on left, there is Partner LogitecSYS. There are multiples but we have created Partner LogitecSYS. This is the 3rd party system

* Partner number = LogitechSYS. This comes from BD54.

* Partner type = LS. Means it is sent to third party system instead of specific Vendor. It is System specific.

* Type = is nothing but in case of error in idoc, who will be notified. We have selected S means ...