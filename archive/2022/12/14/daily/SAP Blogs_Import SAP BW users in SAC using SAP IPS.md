---
title: Import SAP BW users in SAC using SAP IPS
url: https://blogs.sap.com/2022/12/13/import-sap-bw-users-in-sac-using-sap-ips/
source: SAP Blogs
date: 2022-12-14
fetch_date: 2025-10-04T01:24:02.115365
---

# Import SAP BW users in SAC using SAP IPS

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Technology](/t5/technology/ct-p/technology)
* [Technology Blog Posts by Members](/t5/technology-blog-posts-by-members/bg-p/technology-blog-members)
* Import SAP BW users in SAC using SAP IPS

Technology Blog Posts by Members

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/technology-blog-members/article-id/159779&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [Import SAP BW users in SAC using SAP IPS](/t5/technology-blog-posts-by-members/import-sap-bw-users-in-sac-using-sap-ips/ba-p/13548122)

![gaurav_234](https://avatars.profile.sap.com/0/c/id0cd8c20f5487abb58a9b5798bbbaf6be2c421a972caaaa3edcdb993dc963a99e_small.jpeg "gaurav_234")

[gaurav\_234](https://community.sap.com/t5/user/viewprofilepage/user-id/44987)

Participant

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=technology-blog-members&message.id=159779)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/technology-blog-members/article-id/159779)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13548122)

‎2022 Dec 13
5:56 PM

[5
Kudos](/t5/kudos/messagepage/board-id/technology-blog-members/message-id/159779/tab/all-users "Click here to see who gave kudos to this post.")

3,192

* SAP Managed Tags
* [SAP Analytics Cloud](https://community.sap.com/t5/c-khhcw49343/SAP%2520Analytics%2520Cloud/pd-p/67838200100800006884)
* [SAP BTP Security](https://community.sap.com/t5/c-khhcw49343/SAP%2520BTP%2520Security/pd-p/842ea649-eeef-464c-b80c-a64b03e40158)
* [Identity Provisioning](https://community.sap.com/t5/c-khhcw49343/Identity%2520Provisioning/pd-p/73555000100800000425)

* [SAP Analytics Cloud

  SAP Analytics Cloud](/t5/c-khhcw49343/SAP%2BAnalytics%2BCloud/pd-p/67838200100800006884)
* [Identity Provisioning

  SAP Business Technology Platform](/t5/c-khhcw49343/Identity%2BProvisioning/pd-p/73555000100800000425)
* [SAP BTP Security

  Software Product Function](/t5/c-khhcw49343/SAP%2BBTP%2BSecurity/pd-p/842ea649-eeef-464c-b80c-a64b03e40158)

View products (3)

**Introduction**

We got a requirement to import SAP BW roles/users in SAC to enable folder restrictions based on sites. In this blog, I will provide the steps to import SAP BW roles/users in SAC **using SAP IPS**.

Some excellent blogs provide similar automated solutions using SCIM APIs, CSVs etc. Refer:

<https://blogs.sap.com/2021/05/28/sap-analytics-cloud-scim-api-best-practices-and-sample-scripts/>

[https://blogs.sap.com/2021/12/02/sap-analytics-cloud-replicating-bw-analysis-authorizations-into-dim...](https://blogs.sap.com/2021/12/02/sap-analytics-cloud-replicating-bw-analysis-authorizations-into-dimension-read-write-property/)

![](/legacyfs/online/storage/blog_attachments/2022/12/Requirement.jpg)

The Identity Provisioning service automates identity lifecycle processes. It helps you provision identities and their authorizations to various cloud and on-premises business applications. For more information, you can refer to a very nice blog

<https://blogs.sap.com/2019/11/20/sap-identity-provisioning-ips-is-now-bundled-with-s-4hana-cloud/>

**Step-by-step guide**

1. Ensure you are subscribed to an active IPS account and have minimum cloud admin access to this subaccount in BTP. The technical name should match![](/legacyfs/online/storage/blog_attachments/2022/12/IPS.png)

2. Ensure in IPS you have access to ‘Manage Identity Provisioning’, Manage on-premise and Manage Destinations access.

3. Onboard the IPS subaccount on your cloud connector![](/legacyfs/online/storage/blog_attachments/2022/12/IPS-SCC.png)

4. Navigate to Cloud to on-premise->Access control and create a RFC destination with the below resource. Ref: <https://help.sap.com/doc/c30747989e33466e8e4f789dd9c3c81c/Cloud/en-US/Provisioning_Service.pdf>![](/legacyfs/online/storage/blog_attachments/2022/12/IPS-resource.png)

5. Login in BTP and in the IPS subaccount create RFC destination of your BW system![](/legacyfs/online/storage/blog_attachments/2022/12/IPS-BTP.png)

6. Select SAP Application Server ABAP and create your ABAP source system in IPS account

7. In transformation Tab, put a similar condition as below to import users with specific role/pattern e.g. Import all users with role ZSAC\*

*{*

*"user": {*

*"ignore": false,*

*"condition": "($.ACTIVITYGROUPS[?(@.AGR\_NAME contains 'ZSAC\_')] EMPTY false)",*

*"mappings": [*

*{*

*"sourcePath": "$.USERNAME",*

*"targetVariable": "entityIdSourceSystem"*

*},*

8. In the properties tab put a filter ‘abap.role.filter’ to create Teams. E.g. ^ZSAC\_.\* will import all the roles which start with ZSAC as Teams in SAC

9. Create a Target system as Type ‘SAP analytics cloud’, in the transformation tab ensure that the source username and target username are mapped. By default, email Id without a domain name is created as a user Id in SAC. For additional properties, please refer: <https://help.sap.com/doc/c30747989e33466e8e4f789dd9c3c81c/Cloud/en-US/Provisioning_Service.pdf>

*{*

*"sourcePath": "$.userName",*

*"targetPath": "$.userName"*

*},*

10. Schedule the import job in IPS from the source system

![](/legacyfs/online/storage/blog_attachments/2022/12/SCC-Jobs.png)

11. Check the job logs

12. Verify the results in the SAC tenant![](/legacyfs/online/storage/blog_attachments/2022/12/SCC-RESULT.png)

Thank you for your time reading this, I hope you found this useful and informative. Hopefully with this solution you will be able to connect your ABAP system with SAC for different use cases

Looking forward to hearing your thoughts!

4 Comments

You must be a registered user to add a comment. If you've already registered, sign in. Otherwise, register and sign in.

* [Comment](/plugins/common/feature/oidcss/sso_login_redirect/providerid/sap_ids_prompt?redirectreason=permissiondenied&referer=https%3A%2F%2Fcommunity.sap.com%2Ft5%2Ftechnology-blog-posts-by-members%2Fimport-sap-bw-users-in-sac-using-sap-ips%2Fba-p%2F13548122%23comment-on-this)

Copy Link
![](https://community.sap.com/html/@EE5D5986E9F4E5657DCEACB7532B5C39/assets/bluesky-dark.svg)Bluesky
Linkedin

Related Content

* [SAP Build FAQ: Commercials, Getting Started and More](/t5/technology-blog-posts-by-sap/sap-build-faq-commercials-getting-started-and-more/ba-p/14233744)
  in [Technology Blog Posts by SAP](/t5/technology-blog-posts-by-sap/bg-p/technology-blog-sap)  4 hours ago
* [Flexible Workflows for Procurement in SAP S/4HANA](/t5/technology-blog-posts-by-members/flexible-workflows-for-procurement-in-sap-s-4hana/ba-p/14234315)
  in [Technology Blog Posts by Members](/t5/technology-blog-posts-by-members/bg-p/technology-blog-members)  4 hours ago
* [SAP S4HANA Plant Maintenance for dummies](/t5/technology-blog-posts-by-members/sap-s4hana-plant-maintenance-for-dummies/ba-p/14234304)
  in [Technology Blog Posts by Members](/t5/technology-blog-posts-by-members/bg-p/technology-blog-members)  5 hours ago
* [Project-Based Services in SAP S/4HANA](/t5/technology-blog-posts-by-members/project-based-services-in-sap-s-4hana/ba-p/14234290)
  in [Technology Blog Posts by Members](/t5/technology-blog-posts-by-members/bg-p/technology-blog-members)  5 hours ago
* [Organizational Management in SAP S/4HANA HCM](/t5/technology-blog-posts-by-members/organizational-management-in-sap-s-4hana-hcm/ba-p/14234285)
  in [Technology Blog Posts by Members](/t5/technology-...