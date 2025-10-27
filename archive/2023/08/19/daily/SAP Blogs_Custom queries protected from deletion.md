---
title: Custom queries protected from deletion
url: https://blogs.sap.com/2023/08/18/custom-queries-protected-from-deletion/
source: SAP Blogs
date: 2023-08-19
fetch_date: 2025-10-04T11:59:53.153379
---

# Custom queries protected from deletion

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [CRM and Customer Experience](/t5/crm-and-customer-experience/ct-p/crm)
* [CRM and CX Blog Posts by Members](/t5/crm-and-cx-blog-posts-by-members/bg-p/crm-blog-members)
* Custom queries protected from deletion

CRM and CX Blog Posts by Members

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/crm-blog-members/article-id/6442&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [Custom queries protected from deletion](/t5/crm-and-cx-blog-posts-by-members/custom-queries-protected-from-deletion/ba-p/13578720)

![Amita1](https://avatars.profile.sap.com/3/1/id31f40c07a1c0b9c32f3c3d57e555f1e075ca7a5ae7f828226099f16455bb25e6_small.jpeg "Amita1")

[Amita1](https://community.sap.com/t5/user/viewprofilepage/user-id/130308)

Participant

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=crm-blog-members&message.id=6442)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/crm-blog-members/article-id/6442)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13578720)

‎2023 Aug 18
9:57 PM

[2
Kudos](/t5/kudos/messagepage/board-id/crm-blog-members/message-id/6442/tab/all-users "Click here to see who gave kudos to this post.")

759

* SAP Managed Tags
* [SAP Sales Cloud](https://community.sap.com/t5/c-khhcw49343/SAP%2520Sales%2520Cloud/pd-p/73554900100700002221)
* [SAP Service Cloud](https://community.sap.com/t5/c-khhcw49343/SAP%2520Service%2520Cloud/pd-p/73555000100700000801)
* [C4C Extensibility](https://community.sap.com/t5/c-khhcw49343/C4C%2520Extensibility/pd-p/522899869556788325823974243317861)
* [C4C Sales](https://community.sap.com/t5/c-khhcw49343/C4C%2520Sales/pd-p/825493229490678079515430289276035)

* [C4C Sales

  Software Product Function](/t5/c-khhcw49343/C4C%2BSales/pd-p/825493229490678079515430289276035)
* [C4C Extensibility

  Software Product Function](/t5/c-khhcw49343/C4C%2BExtensibility/pd-p/522899869556788325823974243317861)
* [SAP Sales Cloud

  Software Product](/t5/c-khhcw49343/SAP%2BSales%2BCloud/pd-p/73554900100700002221)
* [SAP Service Cloud

  Software Product](/t5/c-khhcw49343/SAP%2BService%2BCloud/pd-p/73555000100700000801)

View products (4)

With SAP Sales & Service Cloud 2305 release briefing, SAP had come up with a great extensibility feature in Cloud for Customer.

As an administrator, it is now possible to protect the custom queries across all the objects such as Accounts, Leads, Opportunities and many more from getting renamed or deleted by the end users.

With this, we can now create multiple custom queries and can protect any individual or all the queries at once.

**Note**: We can protect the new custom queries as well as the custom queries which were created before this 2305 release briefing.

**PROCEDURE TO PROTECT THE CUSTOM QUERIES:**

1. Navigate to any respected object say “Leads” Object and click on “Start Adaptation” option.

![](/legacyfs/online/storage/blog_attachments/2023/08/1-36.png)

2. Click on the “Advance Search” icon à click on “Organize Queries” option.

![](/legacyfs/online/storage/blog_attachments/2023/08/2-37.png)

3. For the custom Queries say “Lead\_Test”, protect option is available and we can enable it.

4. Click on save and then end the adaptation.

![](/legacyfs/online/storage/blog_attachments/2023/08/3-32.png)

**TESTING:**

**Scenario 1**: Before enabling the protect option for the custom query in adaptation:

* In adaptation, before enabling the protect option for the custom query “Lead\_Test”:

![](/legacyfs/online/storage/blog_attachments/2023/08/Test_1.png)

* Hence, as a user in OWL screen, we can observe that the custom query “Lead\_Test” is editable i.e., it can be renamed or also can be removed it from the queries list.

![](/legacyfs/online/storage/blog_attachments/2023/08/Test_2.png)

* And, if the user is trying to delete it from Personalization mode, it will allow to do so.

![](/legacyfs/online/storage/blog_attachments/2023/08/Test_3.png)

![](/legacyfs/online/storage/blog_attachments/2023/08/Test_4.png)

**Scenario 2:** After enabling the protect option for the custom query in adaptation:

* In adaptation, after enabling the protect option for the custom query “Lead\_Test”:

![](/legacyfs/online/storage/blog_attachments/2023/08/Test-2_1.png)

* Hence, as a user we can notice that the custom query “Lead\_Test” is not editable i.e., the user will not be able to rename it or can delete/remove it from the OWL screen.

![](/legacyfs/online/storage/blog_attachments/2023/08/Test-2_2.png)

* And, if the user is trying to delete it from Personalization mode, it will not allow to do so.

![](/legacyfs/online/storage/blog_attachments/2023/08/Test-2_3.png)

![](/legacyfs/online/storage/blog_attachments/2023/08/Test-2_4.png)

Please let me know if you have any queries on the same.

Thank you!!

Warm Regards,

Amita Biradar

* [SAP 2305 Release](/t5/tag/SAP%202305%20Release/tg-p/board-id/crm-blog-members)

You must be a registered user to add a comment. If you've already registered, sign in. Otherwise, register and sign in.

* [Comment](/plugins/common/feature/oidcss/sso_login_redirect/providerid/sap_ids_prompt?redirectreason=permissiondenied&referer=https%3A%2F%2Fcommunity.sap.com%2Ft5%2Fcrm-and-cx-blog-posts-by-members%2Fcustom-queries-protected-from-deletion%2Fba-p%2F13578720%23comment-on-this)

Copy Link
![](https://community.sap.com/html/@EE5D5986E9F4E5657DCEACB7532B5C39/assets/bluesky-dark.svg)Bluesky
Linkedin

Related Content

* [How to improve performance of SAP Commerce Cloud populators](/t5/crm-and-cx-blog-posts-by-sap/how-to-improve-performance-of-sap-commerce-cloud-populators/ba-p/14113435)
  in [CRM and CX Blog Posts by SAP](/t5/crm-and-cx-blog-posts-by-sap/bg-p/crm-blog-sap)  2025 May 28
* [SAP Commerce Cloud Updates in 2024: A Not-So-Brief Summary for Technical Users](/t5/crm-and-cx-blog-posts-by-sap/sap-commerce-cloud-updates-in-2024-a-not-so-brief-summary-for-technical/ba-p/13946014)
  in [CRM and CX Blog Posts by SAP](/t5/crm-and-cx-blog-posts-by-sap/bg-p/crm-blog-sap)  2024 Nov 24
* [What's New in SAP Commerce Cloud: Key Feature Updates for Business Users in 2024](/t5/crm-and-cx-blog-posts-by-sap/what-s-new-in-sap-commerce-cloud-key-feature-updates-for-business-users-in/ba-p/13932624)
  in [CRM and CX Blog Posts by SAP](/t5/crm-and-cx-blog-posts-by-sap/bg-p/crm-blog-sap)  2024 Nov 09
* [When and How to contact the SAP ID Service team?](/t5/crm-and-cx-blog-posts-by-sap/when-and-how-to-contact-the-sap-id-service-team/ba-p/13812455)
  in [CRM and CX Blog Posts by SAP](/t5/crm-and-cx-blog-posts-by-sap/bg-p/crm-blog-sap)  2024 Aug 31
* [Audit Data and Audit Logging in SAP Commerce](/t5/crm-and-cx-blog-posts-by-members/audit-data-and-audit-logging-in-sap-commerce/ba-p/13738362)
  in [CRM and CX Blog Posts by Members](/t5/crm-and-cx-blog-posts-by-members/bg-p/crm-blog-members)  2024 Jul 01

Top kudoed authors

| User | Count |
| --- | --- |
| [![pvsbprasad](https://avatars.profile.sap.com/d/6/idd68c4fbf62700ef39eecb5d35b7b10fd1065edee7ec60bda72a4bced895ca7c3_small.jpeg "pvsbprasad")  pvsbprasad](/t5/user/viewprofilepage/user-id/7820) | 6 |
| [![nikhilwalsetwar](https://avatars.profile.sap.com/b/d/idbd6ba15cea60dda1124d1d2a600f3f07633f911411928898ec0745b28c8b5ac2_small.jpeg "nikhilwalsetwar")  nikhilwalsetwar](/t5/user/viewprofilepage/user-id/42514) | 1 |
| [![ravi_crm1508...