---
title: Using SAP Build Apps, create a Web app that simulates a lead generation page for C4C
url: https://blogs.sap.com/2023/03/20/using-sap-build-apps-create-a-web-app-that-simulates-a-lead-generation-page-for-c4c/
source: SAP Blogs
date: 2023-03-21
fetch_date: 2025-10-04T10:08:40.203520
---

# Using SAP Build Apps, create a Web app that simulates a lead generation page for C4C

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [CRM and Customer Experience](/t5/crm-and-customer-experience/ct-p/crm)
* [CRM and CX Blog Posts by Members](/t5/crm-and-cx-blog-posts-by-members/bg-p/crm-blog-members)
* Using SAP Build Apps, create a Web app that simula...

CRM and CX Blog Posts by Members

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/crm-blog-members/article-id/6255&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [Using SAP Build Apps, create a Web app that simulates a lead generation page for C4C](/t5/crm-and-cx-blog-posts-by-members/using-sap-build-apps-create-a-web-app-that-simulates-a-lead-generation-page/ba-p/13551756)

![adeya](https://avatars.profile.sap.com/b/d/idbd984ebaa3c065597c47ed5fa4f7835a735518fe217d47d034078edf1975b930_small.jpeg "adeya")

[adeya](https://community.sap.com/t5/user/viewprofilepage/user-id/649409)

Explorer

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=crm-blog-members&message.id=6255)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/crm-blog-members/article-id/6255)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13551756)

‎2023 Mar 20
8:23 PM

[4
Kudos](/t5/kudos/messagepage/board-id/crm-blog-members/message-id/6255/tab/all-users "Click here to see who gave kudos to this post.")

2,542

* SAP Managed Tags
* [C4C Sales](https://community.sap.com/t5/c-khhcw49343/C4C%2520Sales/pd-p/825493229490678079515430289276035)
* [SAP Build Apps](https://community.sap.com/t5/c-khhcw49343/SAP%2520Build%2520Apps/pd-p/6cfd8176-04ae-4548-8f38-158456e1a47a)

* [C4C Sales

  Software Product Function](/t5/c-khhcw49343/C4C%2BSales/pd-p/825493229490678079515430289276035)
* [SAP Build Apps

  Additional Software Product](/t5/c-khhcw49343/SAP%2BBuild%2BApps/pd-p/6cfd8176-04ae-4548-8f38-158456e1a47a)

View products (2)

**Use Case**: Suppose a Utility company wants to provide you an offer with a quote on electricity. You go to their website; enter how much electricity you usually consume and click “request more information” after providing name and email address. Afterwards automatically a C4C lead will be created in sales cloud and a sales rep will contact you.

**Business Requirement**: The purpose of this demonstration is to show that a web form with required fields can be used to send data directly to the C4C (Sales cloud).

**How-to-Approach**: Send an automatic message ID for lead creation from SAP Build App to C4C, and search for the same lead with synchronized fields.

**Landscape used:**

SAP Build Apps: Source system
SAP BTP: Middleware
SAP C4C: Target system

![](/legacyfs/online/storage/blog_attachments/2023/03/1-45.png)

**Steps:**

1. **How to Create web Application with SAP Build App:**

1.1.  Access the SAP Build App link and login using credentials under **Email** and **PW**.

![](/legacyfs/online/storage/blog_attachments/2023/03/2-25.png)

**Note**: Please follow the steps below to register and raise access if you do not have an SAP Build App link:

[SAP Build request steps](https://blogs.sap.com/2023/02/28/learning-sap-build-apps-from-basics-sap-build-apps-sandbox/)

1.2.  Please Click on **Create-->**Select **Build an application** tile under **SAP Build page**.

![](/legacyfs/online/storage/blog_attachments/2023/03/3-28.png)

        1.3. Select **Web & mobile application.**

![](/legacyfs/online/storage/blog_attachments/2023/03/4-20.png)

**Note**: Appgyver Classic is the older version of SAP Build App (Appgyver)that will migrate any project created under this version to an application that runs on mobile devices and the web.

1.4. Please enter **Project name** and **Description** and click on **Create button**.

![](/legacyfs/online/storage/blog_attachments/2023/03/5-21.png)

       1.5. Go to **Lobby** you can manually type or **Filter** with My project and check your newly created project available in the list. Check application type as well.

![](/legacyfs/online/storage/blog_attachments/2023/03/6-16.png)

      1.6. Click on add new page from landing page to create **template**.

![](/legacyfs/online/storage/blog_attachments/2023/03/7-14.png)

      1.7. Go to **Auth**--> **Enable Authentication**--> **SAP BTP Authentication** and select **Ok** for pop-up.

![](/legacyfs/online/storage/blog_attachments/2023/03/8-9.png)

![](/legacyfs/online/storage/blog_attachments/2023/03/9-11.png)

1.8. To design the layout, select the layout type in **Full Screen mode**.

![](/legacyfs/online/storage/blog_attachments/2023/03/10-13.png)

      1.9.Create the required fields and buttons using **drag-and-drop** functionality.

![](/legacyfs/online/storage/blog_attachments/2023/03/11-13.png)

      1.10. Go-to **Variables** and create the **App variable** manually, **rename** and **save** it.

![](/legacyfs/online/storage/blog_attachments/2023/03/12-11.png)

      1.11.Go to **Data-->** Click **Enable more data entities-->** Select the Data Entity -->**Add Integration**.

![](/legacyfs/online/storage/blog_attachments/2023/03/13-13.png)

    1.12. Select **Data** -->Under **Data Entities** -->Search **Lead Collection** -->Select **Enable more data entities**-->Add the **Lead collection**.

![](/legacyfs/online/storage/blog_attachments/2023/03/14-10.png)

     1.13. Under **UI canvas** -->Select **Variable** -->**Data Variables-->** **Add data Variables-->** Select the **data entity (Lead Collection)** which was enabled in previous step

![](/legacyfs/online/storage/blog_attachments/2023/03/15-9.png)

     1.14. Click on the **field** and try to do **data binding** for Vorname field under value with **app variable** (which you have defined in Check Step 1.10)

![](/legacyfs/online/storage/blog_attachments/2023/03/1.14-1.png)

* Click **Value** select **Data and Variables**.

![](/legacyfs/online/storage/blog_attachments/2023/03/17-10.png)

* Select **App Variable**.

![](/legacyfs/online/storage/blog_attachments/2023/03/18-7.png)

* Click on Vorname from the list to do the binding.

![](/legacyfs/online/storage/blog_attachments/2023/03/19-7.png)

**Note**: Please follow the same steps for each field and complete the value mapping

1.15. Click and **expand** the **button** (**Generate Lead**) to map all the fields in the template to C4C.

![](/legacyfs/online/storage/blog_attachments/2023/03/Picture20-5.png)

     1.16. From the left-hand side of the screen, select **Data** and drag and drop the **Create Record**.

![](/legacyfs/online/storage/blog_attachments/2023/03/Picture21-4.png)

     1.17. Click on the **Data record** and on right hand side under:

* **Resource name**: Select Lead Collection(App Variable).

![](/legacyfs/online/storage/blog_attachments/2023/03/Picture22-4.png)

* **Record**: From the SAP Build App Template map the relevant fields to C4C you want to display.

![](/legacyfs/online/storage/blog_attachments/2023/03/Picture23-4.png)

* **Authentication**: Enter Your C4C OData communication user Details and select authentication type as Basic, Save.

![](/legacyfs/online/storage/blog_attachments/2023/03/Picture24-4.png)

     1.18. Under **Dialog-->** select **Toast** -->Drag and drop and -->select **Toast Message** to write expression:

![](/legacyfs/online/storage/blog_attachments/2023/03/Picture25-3.png)

* Output Record (Success message):

![](/legacyfs/online/storage/blog_attachments/2023/03/Picture26-3.png)

...