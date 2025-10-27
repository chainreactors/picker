---
title: BTP Workflow Management service task using RAP rest WEB API in S4 Cloud
url: https://blogs.sap.com/2022/11/07/btp-workflow-management-service-task-using-rap-rest-web-api-in-s4-cloud/
source: SAP Blogs
date: 2022-11-08
fetch_date: 2025-10-03T21:56:15.954424
---

# BTP Workflow Management service task using RAP rest WEB API in S4 Cloud

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Technology](/t5/technology/ct-p/technology)
* [Technology Blog Posts by SAP](/t5/technology-blog-posts-by-sap/bg-p/technology-blog-sap)
* BTP Workflow Management service task using RAP res...

Technology Blog Posts by SAP

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/technology-blog-sap/article-id/161432&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [BTP Workflow Management service task using RAP rest WEB API in S4 Cloud](/t5/technology-blog-posts-by-sap/btp-workflow-management-service-task-using-rap-rest-web-api-in-s4-cloud/ba-p/13560819)

![ravish_ranka](https://avatars.profile.sap.com/1/3/id13e12dbf01027c72d12c935abe0ddb8223a5acee7f5ce23a27f9af21e2f3962f_small.jpeg "ravish_ranka")

![Product and Topic Expert](/html/@138D6F765B60D7FC0168643DE27D8A68/rank_icons/sap-logo-small-14px.png "Product and Topic Expert")
[ravish\_ranka](https://community.sap.com/t5/user/viewprofilepage/user-id/157771)

Product and Topic Expert

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=technology-blog-sap&message.id=161432)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/technology-blog-sap/article-id/161432)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13560819)

‎2022 Nov 07
5:20 PM

[3
Kudos](/t5/kudos/messagepage/board-id/technology-blog-sap/message-id/161432/tab/all-users "Click here to see who gave kudos to this post.")

2,045

* SAP Managed Tags
* [SAP Workflow Management, workflow capability](https://community.sap.com/t5/c-khhcw49343/SAP%2520Workflow%2520Management%252C%2520workflow%2520capability/pd-p/73554900100800000555)
* [ABAP RESTful Application Programming Model](https://community.sap.com/t5/c-khhcw49343/ABAP%2520RESTful%2520Application%2520Programming%2520Model/pd-p/7e44126e-7b27-471d-a379-df205a12b1ff)
* [SAP S/4HANA Cloud Public Edition](https://community.sap.com/t5/c-khhcw49343/SAP%2520S%252F4HANA%2520Cloud%2520Public%2520Edition/pd-p/08e2a51b-1ce5-4367-8b33-4ae7e8b702e0)

* [SAP S/4HANA Cloud Public Edition

  SAP S/4HANA Cloud](/t5/c-khhcw49343/SAP%2BS%25252F4HANA%2BCloud%2BPublic%2BEdition/pd-p/08e2a51b-1ce5-4367-8b33-4ae7e8b702e0)
* [SAP Workflow Management, workflow capability

  SAP Business Technology Platform](/t5/c-khhcw49343/SAP%2BWorkflow%2BManagement%25252C%2Bworkflow%2Bcapability/pd-p/73554900100800000555)
* [ABAP RESTful Application Programming Model

  Software Product Function](/t5/c-khhcw49343/ABAP%2BRESTful%2BApplication%2BProgramming%2BModel/pd-p/7e44126e-7b27-471d-a379-df205a12b1ff)

View products (3)

Hello Everyone,

I wanted to user RAP based API in sap cloud in my workflow service task to get/update the data from BTP Workflow to S4 public cloud. When I was trying with service URL with direct basic authentication as destination in BTP, it wasn’t giving me the result as authentication which comes when we try from eclipse will not allow us to get the data. Instead, I was getting response as HTML data.

I have explored few of the blog to connect service from RAP, but none of them was giving solution to connection RAP API directly from Workflow. After several reads, some YouTube videos, hit and trial I was able to trigger service from workflow.

Here I am illustrating how we can use RAP rest API in workflow service task. Following are the steps covered.

1. Create XSUAA service instance and service key to enable trust from workflow user to RAP based web API in cloud.![](/legacyfs/online/storage/blog_attachments/2022/11/XSUAA_diagram-1.png)

2. Create destination to consume REST API in workflow service task with XSUAA trust service token and default identity provider credentials.

3. Using Workflow service task to call API

When we want to do GET or POST request through BTP workflow management, we need to create destination in our BTP subaccount. When we try to connect BTP workflow service to our SAP S4 Public cloud API it needs to be authenticated using default identity provider. We need to authenticate this workflow service user XSUAA to get initial token

Go to BTP subaccount's and create instance for Authorization and Trust Management Service and this will create XSUAA service instance.

![](/legacyfs/online/storage/blog_attachments/2022/11/XSUAA.png)

Provide the details for Plan as apiaccess and name for instance and click on create.

![](/legacyfs/online/storage/blog_attachments/2022/11/XSUAA1.png)

It will take few seconds and now you can go to instance with name you created and create a service key. Below is the service key which I already created.

![](/legacyfs/online/storage/blog_attachments/2022/11/XSUAA2.png)

Open the service key data and copy URL, Client Id, Client Secret. These will be used in to create new destination.

![](/legacyfs/online/storage/blog_attachments/2022/11/XSUAA3.png)

Go to destination tab and create new destination. Before that just get the URL of your RAP based web API created in eclipse. Go to service binding and select your web API and click on service URL.

![](/legacyfs/online/storage/blog_attachments/2022/11/WebAPI1-1.png)

Copy the URL and replace and remove '-web' from URL

[https://1e40e2cb-b1df-4e5e.abap-web.eu10.hana.ondemand.com/sap/opu/odata/sap/ZRET\_C\_COMPWFSTATUS\_API...](https://1e40e2cb-b1df-4e5e.abap-web.eu10.hana.ondemand.com/sap/opu/odata/sap/ZRET_C_COMPWFSTATUS_API/?sap-client=100)

Target URL will look like this.

[https://1e40e2cb-b1df-4e5e.abap.eu10.hana.ondemand.com/sap/opu/odata/sap/ZRET\_C\_COMPWFSTATUS\_API/?sa...](https://1e40e2cb-b1df-4e5e.abap.eu10.hana.ondemand.com/sap/opu/odata/sap/ZRET_C_COMPWFSTATUS_API/?sap-client=100)

![](/legacyfs/online/storage/blog_attachments/2022/11/WebAPI2.png)

Now go to destination and click on create destination with below parameters

![](/legacyfs/online/storage/blog_attachments/2022/11/dest1.png)

Take URL from service URL

User and password are of your BTP account credential

Client id , Client secret and Token service URL below are from XSUAA service key created earlier.

Please note don't forget to add '/oauth/token' in the Token service URL taken from XSUAA service key URL.

![](/legacyfs/online/storage/blog_attachments/2022/11/dest2.png)

![](/legacyfs/online/storage/blog_attachments/2022/11/dest3.png)

Until now we are good with destination creation , please check connection as well.

![](/legacyfs/online/storage/blog_attachments/2022/11/dest4.png)

Now goto workflow in BAS and add destination in service task and service URL as well.

GET call in service task

Here Path would be the url to your service along with the entityset.This part will be added in the destination path. I have created a variable for same. Path along with destination should build your complete URL to service.

![](/legacyfs/online/storage/blog_attachments/2022/11/WFGet1.png)

PUT/POST call in service task will be as below

![](/legacyfs/online/storage/blog_attachments/2022/11/WFPut1-1.png)

Token URL will be same as service path, no addition '/oauth/token' required here. Workflow service will take care of adding 'XSRF-TOKEN = 'FETCH' in header of the get service call before doing put/post call to get the token and use the same in put/post call to authenticate.

![](/legacyfs/online/storage/blog_attachments/2022/11/WFPut2.png)

**Summerry**

We learned how we can connect a REST API in SAP cloud to connect to SAP Wor...