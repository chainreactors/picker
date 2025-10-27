---
title: Creating a New Lead from an Email and attaching the customer request in C4C – Overview and Steps
url: https://blogs.sap.com/2023/03/31/creating-a-new-lead-from-an-email-and-attaching-the-customer-request-in-c4c-overview-and-steps/
source: SAP Blogs
date: 2023-04-01
fetch_date: 2025-10-04T11:20:46.682985
---

# Creating a New Lead from an Email and attaching the customer request in C4C – Overview and Steps

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [CRM and Customer Experience](/t5/crm-and-customer-experience/ct-p/crm)
* [CRM and CX Blog Posts by Members](/t5/crm-and-cx-blog-posts-by-members/bg-p/crm-blog-members)
* Creating a New Lead from an Email and attaching th...

CRM and CX Blog Posts by Members

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/crm-blog-members/article-id/6320&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [Creating a New Lead from an Email and attaching the customer request in C4C - Overview and Steps](/t5/crm-and-cx-blog-posts-by-members/creating-a-new-lead-from-an-email-and-attaching-the-customer-request-in-c4c/ba-p/13565896)

![sudarshanmc89](https://avatars.profile.sap.com/3/e/id3e52bd94f9e1ab71a38cd41b4bdc71e1f46111ed462745aa26309a671362d034_small.jpeg "sudarshanmc89")

[sudarshanmc89](https://community.sap.com/t5/user/viewprofilepage/user-id/833103)

Explorer

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=crm-blog-members&message.id=6320)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/crm-blog-members/article-id/6320)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13565896)

‎2023 Mar 31
9:44 PM

[8
Kudos](/t5/kudos/messagepage/board-id/crm-blog-members/message-id/6320/tab/all-users "Click here to see who gave kudos to this post.")

4,256

* SAP Managed Tags
* [SAP Cloud for Customer add-ins](https://community.sap.com/t5/c-khhcw49343/SAP%2520Cloud%2520for%2520Customer%2520add-ins/pd-p/01200615320800003136)
* [C4C Sales](https://community.sap.com/t5/c-khhcw49343/C4C%2520Sales/pd-p/825493229490678079515430289276035)

* [SAP Cloud for Customer add-ins

  SAP Cloud for Customer](/t5/c-khhcw49343/SAP%2BCloud%2Bfor%2BCustomer%2Badd-ins/pd-p/01200615320800003136)
* [C4C Sales

  Software Product Function](/t5/c-khhcw49343/C4C%2BSales/pd-p/825493229490678079515430289276035)

View products (2)

Hey All,

I am writing this blog to serve as central information on How to save the email from outlook directly to a new lead in C4C. Here you will find the steps to achieve in your system and get to know about how they work technically.

**Key Capabilities**-Add Possibility to save email just at creating lead for better usability.

**Note:** SAP C4C Server-side Integration with Microsoft Outlook is a must to achieve the end goal. Please follow below mentioned blog post for more information.

[C4C Server-side Integration with Microsoft Outlook | SAP Blogs](https://blogs.sap.com/2018/04/19/c4c-server-side-integration-with-microsoft-outlook/).

**Getting Started**

**Step 1****]** Go to Email Integration Work Center and then select Groupware Settings WC View.

![](/legacyfs/online/storage/blog_attachments/2023/03/Groupware-Settings-1.png)

**Fig *1.* *Email**Integration WC - Groupware Settings WC View***

**Step 2****]** Go to the **PROFILES** Tab as shown below and click on pencil icon next to the respective profile to make the changes.

[Profile is a collection of configuration settings and parameters. When administrators provision users, a profile is assigned to each user. To be provisioned, users must be assigned to a profile.]

![](/legacyfs/online/storage/blog_attachments/2023/03/Groupware-Settings-Profiles-Tab.png)

**Fig 2**. Groupware Settings - Profiles Tab

**Step 3]** Click on **ADD-IN SETTINGS** tab and then check the "Lead" Checkbox on the top.

Note: -Please make sure that this checkbox is checked otherwise Lead card will not be visible to you.

![](/legacyfs/online/storage/blog_attachments/2023/03/Groupware-Settings-Profiles-ADD-IN-Settings.png)

**Fig 3.** Groupware Settings - Profiles - ADD-IN Settings

**Step 4]** Go to Lead Card, here you can be able to see the three important Tabs.

1. 1. **Detailed View![](/legacyfs/online/storage/blog_attachments/2023/03/Lead-Card-Detail-View-3.png)**                                                   **Fig 4.** Lead Card - Detail View

      * The main purpose of the tab is to Add/remove the fields that you want while creating the lead from outlook.

      * If you want the field to be displayed in outlook while creating the lead, then "Display on create" should be checked.

      * Click on the Pencil icon to apply the properties of the fields such as Read Only/Required by selecting the respective checkboxes.

      * **Please note****that,** the Setting the default value for the field is applicable only for fields visible in the Add-In (i.e., on the "Create Object" form).The default values should be set in the String format. No other format is supported.For example, to set a default value for a picklist, use the picklist item’s code; for a reference field, use a GUID in the G format; for date/time, use the YYYY-MM-DDTHH:mm:ss format; for a checkbox, use "true" or "false".

   2. **Basic** **View**: You can select the fields to be displayed in groupware for the basic view of Lead.![](/legacyfs/online/storage/blog_attachments/2023/03/Lead-Card-Basic-View.png)                                              **Fig 5**. Lead Card - Basic View

   3. **Settings: -**You can select sort method, days in past to display, and filter status (e.g., open, canceled etc.).

      1. Allow Create: -If this is checked then you can be able create Lead from Outlook

      2. Allow Update: -If this is checked then you can be able update Lead from Outlook![](/legacyfs/online/storage/blog_attachments/2023/03/Lead-Card-Settings-View.png)                      **Fig 6**. Lead Card - Settings View

**Step 5]** The fields shown below will be displayed to the user in outlook while creating the lead.

![](/legacyfs/online/storage/blog_attachments/2023/03/Above-Fields-will-be-Available-in-Outlook-to-User-while-creating-Lead.png)

**Fig 7.** Above Fields will be Available in Outlook to User while creating Lead

**Note**: -Status field will not be displayed to the user while creating the lead (You can't control the status value)

![](/legacyfs/online/storage/blog_attachments/2023/03/Status-Read-Only-1.png)

**Fig 8.** Non-Availability of the Status field while creating the Lead

**Step 6]** Go to the Outlook and select the email and then click on **View Context of SAP Cloud for Customer** to open the groupware add-in.

![](/legacyfs/online/storage/blog_attachments/2023/03/C4C-Addin-in-Outlook.png)

**Fig 9.** C4C - ADD-IN in Outlook

**Step 7]** Click on the + button to create the Lead and then select **Lead** as shown below.

![](/legacyfs/online/storage/blog_attachments/2023/03/Lead-Create-1-3.png)

                             **Fig 10.** Selecting the Lead Object to create the Lead from Outlook

**Step 8]** You can create the lead with existing account or with the new account and the fields will be displayed accordingly (Please check **Step 4** on How to add/remove fields).

Enter all the necessary details to the fields displayed.

![](/legacyfs/online/storage/blog_attachments/2023/03/Lead-Data-1-1.png)

**Fig 11**. Filling the Data in the Lead Creation screen of outlook - Part 1

![](/legacyfs/online/storage/blog_attachments/2023/03/Lead-Data-2-1.png)

**Fig 12**. Filling the Data in the Lead Creation screen of Outlook - Part 2

**Step 9]** After entering all the data,

If you click on the action "**Save with this item"**, The new lead will be created, and e-mail message will be saved to SAP C4C system as an e-mail object.
...