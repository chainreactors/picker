---
title: SAP Information Steward Email Notification Utility
url: https://blogs.sap.com/2023/04/07/sap-information-steward-email-notification-utility/
source: SAP Blogs
date: 2023-04-08
fetch_date: 2025-10-04T11:30:10.840014
---

# SAP Information Steward Email Notification Utility

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Technology](/t5/technology/ct-p/technology)
* [Technology Blog Posts by SAP](/t5/technology-blog-posts-by-sap/bg-p/technology-blog-sap)
* SAP Information Steward Email Notification Utility

Technology Blog Posts by SAP

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/technology-blog-sap/article-id/162067&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [SAP Information Steward Email Notification Utility](/t5/technology-blog-posts-by-sap/sap-information-steward-email-notification-utility/ba-p/13562556)

![rachitapatel](https://avatars.profile.sap.com/d/a/idda2601740f64c8f5242a95b806e8cbb4753dd64b1dc2ee888bce1e1130e754bb_small.jpeg "rachitapatel")

![Product and Topic Expert](/html/@138D6F765B60D7FC0168643DE27D8A68/rank_icons/sap-logo-small-14px.png "Product and Topic Expert")
[rachitapatel](https://community.sap.com/t5/user/viewprofilepage/user-id/128746)

Product and Topic Expert

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=technology-blog-sap&message.id=162067)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/technology-blog-sap/article-id/162067)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13562556)

‎2023 Apr 07
9:25 PM

[1
Kudo](/t5/kudos/messagepage/board-id/technology-blog-sap/message-id/162067/tab/all-users "Click here to see who gave kudos to this post.")

1,527

* SAP Managed Tags
* [SAP Information Steward](https://community.sap.com/t5/c-khhcw49343/SAP%2520Information%2520Steward/pd-p/01200314690800001657)

* [SAP Information Steward

  SAP Information Steward](/t5/c-khhcw49343/SAP%2BInformation%2BSteward/pd-p/01200314690800001657)

View products (1)

## **Overview**

**How to activate e-mail alerts for utility service monitor?**

## **Usage**

E-mail notifications are preferred for the following processes:

* Match review tasks

* Rule tasks

* Rules approval process

* Terms

* Policy sets

* Policy statements

* Scorecards

## **General Steps**

Appropriate permissions are required to perform this task (For example: Administrator rights to CMC).

There are three steps which needs to be performed in CMC:

*(Configuration of e-mail notifications)*
(i) CMC Users and Groups: User e-mail address for notifications set-up.
(ii) CMC Servers: E-mail notification configuration set-up.

*(Adding applicable e-mail addresses)*
(iii) CMC Information Steward Application: Activating e-mail alerts for utilities.

(Optional) The final step has to be performed in SAP IS, if the default settings are not being changed.
- By default, the email notification is being enabled in SAP IS.
- SAP IS Manage: Set-up general e-mail notification preferences.

## Part 1: Setting up user's e-mail address for notification (CMC Users and Groups)

***Pre-requisite:*** An administrator rights of CMC is required to add user's e-mail information.

***Steps:***

**1.** Log in to the **CMC** with Administrator privileges.

![](/legacyfs/online/storage/blog_attachments/2023/04/2023-04-04_11-21-40.png)

Fig.1. SAP BusinessObjects CMC (Source: CMC Homepage)

**2.** From the Organize section (or dropdown menu) in the **CMC homepage**, select **Users and Groups**.

![](/legacyfs/online/storage/blog_attachments/2023/04/2023-04-04_11-28-39.png)

Fig.2. Users and Groups (Source: CMC Homepage)

**3.** **Add** a new user, provide all the details here.

![](/legacyfs/online/storage/blog_attachments/2023/04/2023-04-04_11-36-02.png)

Fig.3. Adding a New User (Source: CMC Homepage (Users and Groups))

Or go to the appropriate user name (from the User List) or group (from the group list) and click **Manage**. Now, go to the *Properties* option.

![](/legacyfs/online/storage/blog_attachments/2023/04/2023-04-05_11-29-34.png)

Fig.4. Selecting appropriate user or group (Source: CMC Users and Groups)

**4.** In the **E-mail textbox**, fill in the appropriate contact information.

![](/legacyfs/online/storage/blog_attachments/2023/04/2023-04-04_11-37-52.png)

Fig.5. Adding User's E-mail Details (Source: CMC Users and Groups)

**5.** Finally, click on **Save & Close.**

***Next Steps:*** Recipient user's e-mail address has been successfully added for notifications. Once this step is completed, now the next step is about configuring the e-mail notification.

## **Part 2: Setting up e-mail notification configuration (EIM Adaptive Job Server Destination e-mail: CMC Servers)**

***Pre-requisites:** The recipient user's email address must be added in the Users and Groups configuration from CMC. Ensure the appropriate permissions to CMC are present.*

***Steps:***

**1.** Log in to the **CMC** with Administrator privileges.

![](/legacyfs/online/storage/blog_attachments/2023/04/2023-04-04_11-21-40-1.png)

Fig.6. SAP BusinessObjects CMC (Source: CMC Homepage)

**2.** From the *Organize* section (or dropdown menu) in the **CMC homepage**, select **Servers**.

![](/legacyfs/online/storage/blog_attachments/2023/04/2023-04-04_11-28-39_1.png)

Fig.7. Servers (Source: CMC Homepage)

**3.** On the left side, click on the **Servers list**. This will display a list of all the existing servers.

![](/legacyfs/online/storage/blog_attachments/2023/04/Fig8.png)

Fig.8. Servers Selection (Source: CMC Servers)

**4.** Now, from this *Servers list*, select the **Adaptive Job Server**.

![](/legacyfs/online/storage/blog_attachments/2023/04/Fig9.png)

Fig.9. Servers List (Source: CMC Servers)

**5.** Click **Manage**. Now, go to the *Properties* option and the respective dialog box will open.

![](/legacyfs/online/storage/blog_attachments/2023/04/Fig10-1.png)

Fig.10. Adaptive Job Server Selection - Properties (Source: CMC Servers)

**6.** From the left side, select **Destination**.

![](/legacyfs/online/storage/blog_attachments/2023/04/Fig11-1.png)

Fig.11. Adaptive Job Server Properties - Destination (Source: CMC Servers)

**7.** Here, a list of e-mail options will appear. Select the **respective E-mail** and click on **Add**.

![](/legacyfs/online/storage/blog_attachments/2023/04/Fig12-1.png)

Fig.12. Email Selection (Source: CMC Servers)

**8.** Add the **E-mail related details** here.

![](/legacyfs/online/storage/blog_attachments/2023/04/Fig14-1.png)

Fig.13. E-mail details (Source: CMC Servers)

**9.** Click on **Save & Close.**

***Next Steps:*** Once the EIM Adaptive Job Server Destination Email has been configured with all the details (like SMTP domain, host, port, message content, etc) then the next step is about activating e-mail alerts.

## **Part 3: Activating e-mail alerts for Utilities (CMC Information Steward Application)**

***Prerequisites:*** Setting up recipient user's e-mail and configuring the EIM Adaptive Job Server destination e-mail.

**Steps:**

**1.** Log in to the **CMC** with Administrator privileges.

![](/legacyfs/online/storage/blog_attachments/2023/04/2023-04-04_11-21-40-2.png)

Fig.14. SAP BusinessObjects CMC (Source: CMC Homepage)

**2.** From the *Manage* section (or dropdown menu) in the **CMC homepage**, select **Applications.**

![](/legacyfs/online/storage/blog_attachments/2023/04/Fig15-1.png)

Fig.15. CMC Applications (Source: CMC Homepage)

**3.** From the Applications menu, double-click on Information Steward Application.

![](/legacyfs/online/storage/blog_attachments/2023/04/Fig16-1.png)

Fig.16. CMC Information Steward Application (Source: CMC...