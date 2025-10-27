---
title: Empowering business users to create new workflows with S/4HANA Cloud, public edition and SAP BTP – Part 2
url: https://blogs.sap.com/2023/05/05/empowering-business-users-to-create-new-workflows-with-s-4hana-cloud-public-edition-and-sap-btp-part-2/
source: SAP Blogs
date: 2023-05-06
fetch_date: 2025-10-04T11:40:18.423774
---

# Empowering business users to create new workflows with S/4HANA Cloud, public edition and SAP BTP – Part 2

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Technology](/t5/technology/ct-p/technology)
* [Technology Blog Posts by SAP](/t5/technology-blog-posts-by-sap/bg-p/technology-blog-sap)
* Empowering business users to create new workflows ...

Technology Blog Posts by SAP

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/technology-blog-sap/article-id/164453&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [Empowering business users to create new workflows with S/4HANA Cloud, public edition and SAP BTP – Part 2](/t5/technology-blog-posts-by-sap/empowering-business-users-to-create-new-workflows-with-s-4hana-cloud-public/ba-p/13570157)

![MartyMcCormick](https://avatars.profile.sap.com/9/c/id9cd5c2c92e4347d2b5972256b5ec172ca03c51fb7e41c0b6b5ef5a93a4362e47_small.jpeg "MartyMcCormick")

![Product and Topic Expert](/html/@138D6F765B60D7FC0168643DE27D8A68/rank_icons/sap-logo-small-14px.png "Product and Topic Expert")
[MartyMcCormick](https://community.sap.com/t5/user/viewprofilepage/user-id/132272)

Product and Topic Expert

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=technology-blog-sap&message.id=164453)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/technology-blog-sap/article-id/164453)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13570157)

‎2023 May 05
9:22 PM

[6
Kudos](/t5/kudos/messagepage/board-id/technology-blog-sap/message-id/164453/tab/all-users "Click here to see who gave kudos to this post.")

2,979

* SAP Managed Tags
* [SAP Build](https://community.sap.com/t5/c-khhcw49343/SAP%2520Build/pd-p/73555000100700001491)
* [SAP S/4HANA Cloud Public Edition](https://community.sap.com/t5/c-khhcw49343/SAP%2520S%252F4HANA%2520Cloud%2520Public%2520Edition/pd-p/08e2a51b-1ce5-4367-8b33-4ae7e8b702e0)
* [SAP Build Process Automation](https://community.sap.com/t5/c-khhcw49343/SAP%2520Build%2520Process%2520Automation/pd-p/73554900100800003832)

* [SAP S/4HANA Cloud Public Edition

  SAP S/4HANA Cloud](/t5/c-khhcw49343/SAP%2BS%25252F4HANA%2BCloud%2BPublic%2BEdition/pd-p/08e2a51b-1ce5-4367-8b33-4ae7e8b702e0)
* [SAP Build Process Automation

  SAP Build](/t5/c-khhcw49343/SAP%2BBuild%2BProcess%2BAutomation/pd-p/73554900100800003832)
* [SAP Build

  Software Product](/t5/c-khhcw49343/SAP%2BBuild/pd-p/73555000100700001491)

View products (3)

This is the second blog in a three part series demoing SAP Build Process Automation (SBPA) along with SAP Build app to call an API in SAP S/4HANA Cloud, public edition (S/4HC).  To recap, the app allows end users to enter basic information about a new project and submission triggers an approval workflow on SBPA.  After approval, a call to S/4HC is made to create the project with the data submitted and a default set of work packages.  In [part 1](https://blogs.sap.com/2023/05/03/creating-projects-in-sap-s-4hana-cloud-based-on-approval-in-sap-build-process-automation-via-sap-btp-cloud-integration/) of this series, I covered how to create a REST API integration flow on BTP Cloud Integration to handle the API for SBPA and subsequent API mapping for S/4HC.  In this blog, I’ll cover the SBPA setup to handle the approval workflow and call to the REST API on BTP CI via an Action.

There are 3 main steps required for SBPA.

1. Create BTP Destination for BTP CI REST Endpoint

2. Create an Action to handle the API call to BTP CI.

3. Create the Business Process to handle call from SAP Build app, approval workflow forms, and incorporate action call.

Note: There are also other blogs/tutorials that can be referenced for more information on adding actions to process automations including this [one](https://blogs.sap.com/2022/10/21/sap-process-automation-your-first-simple-action-project-end-to-end/).

## Create BTP Destination for SAP BTP Cloud Integration

A BTP destination is needed in order for SBPA to connect to our REST API.  An example outlining the process to create a destination is documented [here](https://developers.sap.com/tutorials/cp-cf-create-destination.html).

The Client ID, Client Secret and Token Service URL are found in the service instance key of your BTP CI subaccount.

You can find the REST endpoint when you deploy your integration under the Operations View->Manage Integration Content.  You can remove the */clientproject* from the end of the URL which then produces a value: <https://<subaccount>-rt.cfapps.sap.hana.ondemand.com/http/>

The following additional properties should be added to use the destination in SAP Build:

* sap.processautomation.enabled = true

* sap.applicationdevelopment.actions.enabled = true

![](/legacyfs/online/storage/blog_attachments/2023/05/redo1.png)

BTP Destination for BTP Cloud Integration

## Create Action for REST API

Note: an end to end tutorial for Action creation can be found [here](https://developers.sap.com/tutorials/spa-process-action-create.html).

An OpenAPI Specification is needed in order to create the action based on the REST endpoint created in the first blog.  I created this file by using chatGPT to generate the specification based on the JSON payload that was used to build the iFlow.  To keep things simple, I used all String datatypes but if you wanted to perform validations you could correctly set the datatypes.

![](/legacyfs/online/storage/blog_attachments/2023/05/api1-2.png)

Using chatGPT to generate OpenAPI 3.0 file

Navigate to the SAP Business Process Automation app on BTP and select *Build an Automated Process*.

![](/legacyfs/online/storage/blog_attachments/2023/05/api2.png)

Build an Automated Process

Next click on *Actions* to create a new Actions project.

![](/legacyfs/online/storage/blog_attachments/2023/05/api3.png)

API Action

Give your project a name and description and provide the OpenAPI file created in the previous step.

![](/legacyfs/online/storage/blog_attachments/2023/05/api4.png)

Add the POST action

![](/legacyfs/online/storage/blog_attachments/2023/05/api5a.png)

API Action

Next, you'll want to enable CSRF for the action via Settings in the upper left.

![](/legacyfs/online/storage/blog_attachments/2023/05/api6-1.png)

Enable CSRF for Action

You can modify any API fields that you need to in the Action or default fields.

![](/legacyfs/online/storage/blog_attachments/2023/05/api7.png)

Action API Fields

In order to verify that our Action works correctly, we can test it right from the project by clicking on Test and inputting some test data.  A successful test should result in a HTTP 201 response, which it does in this case.

![](/legacyfs/online/storage/blog_attachments/2023/05/api8.png)

Testing API in Action

Verifying that the call worked end to end, I can see the newly created project in S/4HC by querying the projects API in S/4HC directly from Postman.

![](/legacyfs/online/storage/blog_attachments/2023/05/api9.png)

Project in S/4HC

Once testing is complete, the Action can be released and published.

![](/legacyfs/online/storage/blog_attachments/2023/05/api9a.png)

Release the Action

![](/legacyfs/online/storage/blog_attachments/2023/05/api9b.png)

Publish the Action

![](/legacyfs/online/storage/blog_attachments/2023/05/api9c.png)

Published Action

## Create Business Process

The destination needs to be added to SBPA before creating the Business Process.  In the Build lobby, navigate to settings and you should see a popup to add the destination...