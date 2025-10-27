---
title: AFE (Authorization for Expenditure) process with offline Adobe Forms Scenario
url: https://blogs.sap.com/2023/03/04/afe-authorization-for-expenditure-process-with-offline-adobe-forms-scenario/
source: SAP Blogs
date: 2023-03-05
fetch_date: 2025-10-04T08:43:47.971606
---

# AFE (Authorization for Expenditure) process with offline Adobe Forms Scenario

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Technology](/t5/technology/ct-p/technology)
* [Technology Blog Posts by Members](/t5/technology-blog-posts-by-members/bg-p/technology-blog-members)
* AFE (Authorization for Expenditure) process with o...

Technology Blog Posts by Members

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/technology-blog-members/article-id/162317&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [AFE (Authorization for Expenditure) process with offline Adobe Forms Scenario](/t5/technology-blog-posts-by-members/afe-authorization-for-expenditure-process-with-offline-adobe-forms-scenario/ba-p/13562948)

![kasralikarpratik](https://avatars.profile.sap.com/5/b/id5bbff3f9d10f048202c0c0b73d56590b785951fa8fa4ac4a9c73a791b54d0cca_small.jpeg "kasralikarpratik")

[kasralikarpratik](https://community.sap.com/t5/user/viewprofilepage/user-id/541785)

Explorer

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=technology-blog-members&message.id=162317)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/technology-blog-members/article-id/162317)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13562948)

‎2023 Mar 04
6:42 AM

[1
Kudo](/t5/kudos/messagepage/board-id/technology-blog-members/message-id/162317/tab/all-users "Click here to see who gave kudos to this post.")

15,250

* SAP Managed Tags
* [Oil, Gas, and Energy](https://community.sap.com/t5/c-khhcw49343/Oil%252C%2520Gas%252C%2520and%2520Energy/pd-p/156805312755941004032364)
* [Utilities](https://community.sap.com/t5/c-khhcw49343/Utilities/pd-p/48826897347003784259801)
* [ABAP Development](https://community.sap.com/t5/c-khhcw49343/ABAP%2520Development/pd-p/833755570260738661924709785639136)
* [SAP Business Workflow](https://community.sap.com/t5/c-khhcw49343/SAP%2520Business%2520Workflow/pd-p/271076705480744283548543960420215)
* [SAP Interactive Forms by Adobe](https://community.sap.com/t5/c-khhcw49343/SAP%2520Interactive%2520Forms%2520by%2520Adobe/pd-p/582573882271271216439685697820265)

* [Oil, Gas, and Energy

  Industry](/t5/c-khhcw49343/Oil%25252C%2BGas%25252C%2Band%2BEnergy/pd-p/156805312755941004032364)
* [Utilities

  Industry](/t5/c-khhcw49343/Utilities/pd-p/48826897347003784259801)
* [SAP Business Workflow

  Software Product Function](/t5/c-khhcw49343/SAP%2BBusiness%2BWorkflow/pd-p/271076705480744283548543960420215)
* [SAP Interactive Forms by Adobe

  Software Product Function](/t5/c-khhcw49343/SAP%2BInteractive%2BForms%2Bby%2BAdobe/pd-p/582573882271271216439685697820265)
* [ABAP Development

  Programming Tool](/t5/c-khhcw49343/ABAP%2BDevelopment/pd-p/833755570260738661924709785639136)

View products (5)

Hello Everyone,

Today I am going to explain how to achieve AFE process which is used in oil and gas industries for both Upstream and Downstream.

The term AFE stands for Authorization for Expenditure. This term is used for drilling and completion costs. AFE is used for approval of large Capital expenditure related to exploration, development and production. Also it is getting used for approval of expenditure related to Drilling, Pre drilling.

So how to design this AFE process in SAP. This process is most commonly done by using Project and WBS level where you can add cost of each materials used for upstream / downstream activities.

And using workflow (either standard / custom ) the approval process takes place.

In this blog I am going to explain how to achieve this process when trigger / Initiation of this AFE process happens offline or you can say at the site level where its not in network.

This will be achieved using offline adobe forms scenario. I am not going to explain it with the exact technical details as it is more depends upon the process you are trying to design. Also this is little complex design because of lot of back and forth involved with the approvals.

Step 1:

Create offline form where you can ask user to enter the exact project details like what are different steps needs to performed and when user click on submit, it will come to SAP and create work orders for all the different steps. This will be achieved using data connection in the Adobe forms. You can create data connection for the service created. You can also trigger the workflow using RFC's.

Step 2:

Create custom workflow. After step 1, It will go for the first level of approval. This step you can either use your own DOA process ( Delegation of authorities) to identify the first level of approver who will give approval to create work orders for each steps and approval to perform this project.

Step 3:

After work orders are created, Another set of adobe forms will gets created and it will be sent in email to all the different managers who will be representatives of each activities and they will maintain all details and cost for it. for ex drilling manager will maintain drilling activities that needs to be performed & cost associated with it.

Step 4:

Once all the manager's maintain it and click submit, it will again comes to SAP and goes for the approvals based on DOA. After all approvals it will update those activities in work order and change the status of the work order. Remaining process you can design it in SAP to handle the AFE.

There are many different ways to design the AFE but this process was designed specifically for the offline scenario.

You can also design this AFE in SAP itself as I mentioned before using project systems.

I thought to share this because i didn't find many blog explaining how to achieve this process in SAP.

There is no design documentation to be followed however based on my experience, if the business requirement is not complex and can be done with internal approvals, the standard workflow solution can be followed.

If you came across with any AFE process please share it.

Thank you.

You must be a registered user to add a comment. If you've already registered, sign in. Otherwise, register and sign in.

* [Comment](/plugins/common/feature/oidcss/sso_login_redirect/providerid/sap_ids_prompt?redirectreason=permissiondenied&referer=https%3A%2F%2Fcommunity.sap.com%2Ft5%2Ftechnology-blog-posts-by-members%2Fafe-authorization-for-expenditure-process-with-offline-adobe-forms-scenario%2Fba-p%2F13562948%23comment-on-this)

Copy Link
![](https://community.sap.com/html/@EE5D5986E9F4E5657DCEACB7532B5C39/assets/bluesky-dark.svg)Bluesky
Linkedin

Related Content

* [Event enabling SAP Data Replication Framework with Advanced Event Mesh & RAP Business Events](/t5/technology-blog-posts-by-sap/event-enabling-sap-data-replication-framework-with-advanced-event-mesh-amp/ba-p/14224298)
  in [Technology Blog Posts by SAP](/t5/technology-blog-posts-by-sap/bg-p/technology-blog-sap)  a week ago
* [SAP Datasphere Integration with SAP S/4HANA: SAP Cloud Connector Setup Guide](/t5/technology-blog-posts-by-sap/sap-datasphere-integration-with-sap-s-4hana-sap-cloud-connector-setup-guide/ba-p/14224459)
  in [Technology Blog Posts by SAP](/t5/technology-blog-posts-by-sap/bg-p/technology-blog-sap)  a week ago
* [A Comprehensive Guide to Data Migration with the SAP S/4HANA Migration Cockpit](/t5/technology-blog-posts-by-members/a-comprehensive-guide-to-data-migration-with-the-sap-s-4hana-migration/ba-p/14224541)
  in [Technology Blog Posts by Members](/t5/technology-blog-posts-by-members/bg-p/technology-blog-mem...