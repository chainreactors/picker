---
title: Establishing SAC Connection with SFDC
url: https://blogs.sap.com/2023/01/06/establishing-sac-connection-with-sfdc/
source: SAP Blogs
date: 2023-01-07
fetch_date: 2025-10-04T03:15:23.360834
---

# Establishing SAC Connection with SFDC

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Technology](/t5/technology/ct-p/technology)
* [Technology Blog Posts by Members](/t5/technology-blog-posts-by-members/bg-p/technology-blog-members)
* Establishing SAC Connection with SFDC

Technology Blog Posts by Members

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/technology-blog-members/article-id/162574&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [Establishing SAC Connection with SFDC](/t5/technology-blog-posts-by-members/establishing-sac-connection-with-sfdc/ba-p/13564504)

![Sujit](https://avatars.profile.sap.com/2/8/id2828308dd10fbcf33ea5e12388152477acb453d87b8da732dd47fcfa54d47f0a_small.jpeg "Sujit")

[Sujit](https://community.sap.com/t5/user/viewprofilepage/user-id/730)

Active Participant

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=technology-blog-members&message.id=162574)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/technology-blog-members/article-id/162574)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13564504)

‎2023 Jan 06
5:18 PM

[2
Kudos](/t5/kudos/messagepage/board-id/technology-blog-members/message-id/162574/tab/all-users "Click here to see who gave kudos to this post.")

2,759

* SAP Managed Tags
* [SAP Analytics Cloud](https://community.sap.com/t5/c-khhcw49343/SAP%2520Analytics%2520Cloud/pd-p/67838200100800006884)

* [SAP Analytics Cloud

  SAP Analytics Cloud](/t5/c-khhcw49343/SAP%2BAnalytics%2BCloud/pd-p/67838200100800006884)

View products (1)

Recently, I was exploring SAC on SFDC for one of my clients.

While exploring I felt that the SAC – SFDC combination is not used much, as during my exploration I encountered multiple issues, which I had not faced when using SAC with other sources like BW4HANA or SQL Server or Standalone Excel upload.

Some of these were bugs, some by design, but as I mentioned I had not faced similar issue with other data sources, it was difficult to identify if the product was behaving wrong or I was not doing it the correct way. As a result, I had to turn to google to check if others have faced similar issues and to learn from their experience of resolving it, but even on Google or on SCN I could not find much…hence the above assumption that SAC – SFDC combination is not used much.

Therefore, I plan to share the same with all here as this might help others and/or hopefully give them some direction, if they encounter similar issue…this can turn out to be a multi-part blog series, as there were multiple issues we encountered, I will try to pen down the same as time permits.

Part 1 – Establishing SAC Connection with SFDC

1. SAC connects with SFDC using the acquired connection also commonly known as Import connection ![](/legacyfs/online/storage/blog_attachments/2023/01/Salesforce-Acquired-Connection.png)

2. The connection interface is common like for all other acquired connection. ![](/legacyfs/online/storage/blog_attachments/2023/01/Salesforce-Connector-Window.png)

3. We selected Authentication type as ‘Basic Authentication’

4. And entered the required details like Authorization URL, Username, Password and expected the connection to work…simple

5. However, the connection did not work and gave out an error

6. We cross-checked the details entered with relevant teams, but still the connection refused to work.

7. However, the SFDC team, while sharing the connection details & credentials, had also shared one more detail and that was Secret key, but the SAC connection interface does not provide any field to enter secret key, nor does the help documentation mention it. Maybe SFDC’s local login interface provides a separate field to add the Secret key, but SAC’s does not. So there is no way to know If this piece of data is to be used at all, as none of us had earlier worked on SFDC

8. As we were doing the trial and error, the basis team decided to use this piece of data somehow…but how was that data to be used, there was no field provided for it. Where were we to enter it, so the system can pick it up, if it really required it to establish the connection.

9. In one such trial and error attempt, the basis team entered the password & secret key combination in the password field in a concatenated format i.e. Passwordsecretkey

10. Success..It worked.

This is a minor issue, but when you are working on the new technology combination, with no help around in person or documentation and add to that a unclear interface with missing field, Minor issues become frustrating and time-consuming to resolve.

Hope this will save someone some time.

Thanks for Reading !!!

Sujit Honrao

* [Acquired Connection](/t5/tag/Acquired%20Connection/tg-p/board-id/technology-blog-members)
* [connection](/t5/tag/connection/tg-p/board-id/technology-blog-members)
* [salesforce](/t5/tag/salesforce/tg-p/board-id/technology-blog-members)
* [secret key](/t5/tag/secret%20key/tg-p/board-id/technology-blog-members)

3 Comments

You must be a registered user to add a comment. If you've already registered, sign in. Otherwise, register and sign in.

* [Comment](/plugins/common/feature/oidcss/sso_login_redirect/providerid/sap_ids_prompt?redirectreason=permissiondenied&referer=https%3A%2F%2Fcommunity.sap.com%2Ft5%2Ftechnology-blog-posts-by-members%2Festablishing-sac-connection-with-sfdc%2Fba-p%2F13564504%23comment-on-this)

Copy Link
![](https://community.sap.com/html/@EE5D5986E9F4E5657DCEACB7532B5C39/assets/bluesky-dark.svg)Bluesky
Linkedin

Related Content

* [🚀 Remember the pioneering days of SAP ECC?](/t5/technology-blog-posts-by-members/remember-the-pioneering-days-of-sap-ecc/ba-p/14229517)
  in [Technology Blog Posts by Members](/t5/technology-blog-posts-by-members/bg-p/technology-blog-members)  Saturday
* [Migrating Integration Flows with JDBC on Cloud Foundry While Using SAP HANA on Neo](/t5/technology-blog-posts-by-sap/migrating-integration-flows-with-jdbc-on-cloud-foundry-while-using-sap-hana/ba-p/14223891)
  in [Technology Blog Posts by SAP](/t5/technology-blog-posts-by-sap/bg-p/technology-blog-sap)  2 weeks ago
* [Deployed Objects not getting saved in SAP BODS](/t5/technology-q-a/deployed-objects-not-getting-saved-in-sap-bods/qaq-p/14222485)
  in [Technology Q&A](/t5/technology-q-a/qa-p/technology-questions)  2 weeks ago
* [Migrating from SAP PO to SAP Integration Suite (CPI): A Practical Guide](/t5/technology-blog-posts-by-members/migrating-from-sap-po-to-sap-integration-suite-cpi-a-practical-guide/ba-p/14219938)
  in [Technology Blog Posts by Members](/t5/technology-blog-posts-by-members/bg-p/technology-blog-members)  2 weeks ago
* [Enhancing Security in SAP Cloud Transport Management in SAP BTP - 2](/t5/technology-blog-posts-by-members/enhancing-security-in-sap-cloud-transport-management-in-sap-btp-2/ba-p/14180681)
  in [Technology Blog Posts by Members](/t5/technology-blog-posts-by-members/bg-p/technology-blog-members)  2025 Aug 16

Top kudoed authors

| User | Count |
| --- | --- |
| [![WouterLemaire](https://avatars.profile.sap.com/9/5/id95a688fa6b84e4186cabf39d7a83127ea90dd51dd190d355416d56f7d3a5be56_small.jpeg "WouterLemaire")  ![SAP Mentor](/html/@F4C200E47DAE3459A6BD3FBB7F9955B8/rank_icons/mentor-rank-16x16.svg "SAP Mentor") WouterLemaire](/t5/user/viewprofilepage/user-id/9863) | 6 |
| [![Sandra_Rossi](https://avatars.profile.sap.com/5/a/id5ade69af148fee003e69a3410fe4ea7...