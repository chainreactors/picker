---
title: Master Detail Binding using EventBus in SAP UI5
url: https://blogs.sap.com/2023/07/14/master-detail-binding-using-eventbus-in-sap-ui5/
source: SAP Blogs
date: 2023-07-15
fetch_date: 2025-10-04T11:52:59.471597
---

# Master Detail Binding using EventBus in SAP UI5

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Technology](/t5/technology/ct-p/technology)
* [Technology Blog Posts by Members](/t5/technology-blog-posts-by-members/bg-p/technology-blog-members)
* Master Detail Binding using EventBus in SAP UI5

Technology Blog Posts by Members

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/technology-blog-members/article-id/161586&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [Master Detail Binding using EventBus in SAP UI5](/t5/technology-blog-posts-by-members/master-detail-binding-using-eventbus-in-sap-ui5/ba-p/13559076)

![madhusudan007h](https://avatars.profile.sap.com/c/f/idcf3b80972404a9f54c6adec4beae09233d0bdd50438631ae99d01763c60c17e4_small.jpeg "madhusudan007h")

[madhusudan007h](https://community.sap.com/t5/user/viewprofilepage/user-id/137764)

Explorer

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=technology-blog-members&message.id=161586)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/technology-blog-members/article-id/161586)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13559076)

‎2023 Jul 14
6:58 PM

[3
Kudos](/t5/kudos/messagepage/board-id/technology-blog-members/message-id/161586/tab/all-users "Click here to see who gave kudos to this post.")

1,817

* SAP Managed Tags
* [SAP Business Application Studio](https://community.sap.com/t5/c-khhcw49343/SAP%2520Business%2520Application%2520Studio/pd-p/67837800100800007077)
* [SAPUI5](https://community.sap.com/t5/c-khhcw49343/SAPUI5/pd-p/500983881501772639608291559920477)

* [SAP Business Application Studio

  SAP Business Application Studio](/t5/c-khhcw49343/SAP%2BBusiness%2BApplication%2BStudio/pd-p/67837800100800007077)
* [SAPUI5

  Programming Tool](/t5/c-khhcw49343/SAPUI5/pd-p/500983881501772639608291559920477)

View products (2)

**Requirement:**

I had a requirement where on events of View1 I wanted to make some changes in View 2 in Master-Detail page with Nested Views.

**Advantage**

1. Multiple people can work on same project without facing any issue while merging.

2. Code is segregate which helps in reducing complexity of program.

3. Individual view can be used as a plugin.

**Note :**

Here I have created 3 Views one for SplitApp and remaining two views I made it as nested view inside the SplitApp as Master View and Detail View.

Step 1: Create one main view as SplitApp follow the as shown in the image

![](/legacyfs/online/storage/blog_attachments/2023/07/img1.png)

sample of nested view in SplitApp

**Master View**

![](/legacyfs/online/storage/blog_attachments/2023/07/img2.png)

Master View

**Detail View**

![](/legacyfs/online/storage/blog_attachments/2023/07/img3.png)

Detail View

**Invoking methods of Detail view controller for event occurring in Master View**

As per my Requirement this can be achieved by different ways but still will implement it by EventBus

Event Bus is publisher/subscriber design pattern. There will be 2 events one will be a publisher and another will be subscriber.Publisher : This is event which gets triggered on any event of same view.Subscriber: This is event which gets triggered on any event of another View.

**Code for Master controller  (Publish method)**

![](/legacyfs/online/storage/blog_attachments/2023/07/img4.png)

Publish Method

**Code for Detail controller (Subscribe method)**

![](/legacyfs/online/storage/blog_attachments/2023/07/img5.png)

Subscribe method

Once event is triggered in Master view (**publish**) an event will be published. All the subscriber (Detail view) events will be triggered (**subscribe**).

Step 2:

Create model with data and configure it in **manifest.json** file

**Data.json**

```
{

    "data":[

        {

            "name":"Madhusudan",

            "city":"Bangalore",

            "Gender":"Male",

            "Salary":"Rs.20000",

            "Designation":"Developer"

        },

        {

            "name":"Ayaz",

            "city":"Hassan",

            "Gender":"Male",

            "Salary":"Rs.30000",

            "Designation":"Developer"

        },

        {

            "name":"Monika",

            "city":"Yamaloka",

            "Gender":"Female",

            "Salary":"Rs.35000",

            "Designation":"Singing and Dancing"

        },

        {

            "name":"Faraz",

            "city":"Ramnagar",

            "Gender":"Male",

            "Salary":"Rs.40000",

            "Designation":"Test Engineer"

        },

        {

            "name":"Sachin",

            "city":"Gulbarga",

            "Gender":"Male",

            "Salary":"Rs.10000",

            "Designation":"System Engineer"

        },

        {

            "name":"Ganesh",

            "city":"Ranebennuru",

            "Gender":"Male",

            "Salary":"Rs.200000",

            "Designation":"Support"

        }

    ]

}
```

**Manifest.json**

![](/legacyfs/online/storage/blog_attachments/2023/07/img6.png)

Manifest.json

**Final Output**

![](/legacyfs/online/storage/blog_attachments/2023/07/img7.png)

output

**Conclusion**

Finally, we done. The same approach can be implement it by in different ways. nested views in master detail with EventBus is one more way. At the same time of event occurring you can pass multiple data as channels as user requirement.

Hope I find this helpful.

Thanks and Regards

**Madhusudan**

2 Comments

You must be a registered user to add a comment. If you've already registered, sign in. Otherwise, register and sign in.

* [Comment](/plugins/common/feature/oidcss/sso_login_redirect/providerid/sap_ids_prompt?redirectreason=permissiondenied&referer=https%3A%2F%2Fcommunity.sap.com%2Ft5%2Ftechnology-blog-posts-by-members%2Fmaster-detail-binding-using-eventbus-in-sap-ui5%2Fba-p%2F13559076%23comment-on-this)

Copy Link
![](https://community.sap.com/html/@EE5D5986E9F4E5657DCEACB7532B5C39/assets/bluesky-dark.svg)Bluesky
Linkedin

Related Content

* [RAP Using Custom Entity with load multiple data using Pagination and Preview using UI annotations](/t5/technology-q-a/rap-using-custom-entity-with-load-multiple-data-using-pagination-and/qaq-p/14233901)
  in [Technology Q&A](/t5/technology-q-a/qa-p/technology-questions)  yesterday
* [🚀 Remember the pioneering days of SAP ECC?](/t5/technology-blog-posts-by-members/remember-the-pioneering-days-of-sap-ecc/ba-p/14229517)
  in [Technology Blog Posts by Members](/t5/technology-blog-posts-by-members/bg-p/technology-blog-members)  Saturday
* [3rd level child in RAP managed scenario does not navigate to Identification facet](/t5/technology-q-a/3rd-level-child-in-rap-managed-scenario-does-not-navigate-to-identification/qaq-p/14219588)
  in [Technology Q&A](/t5/technology-q-a/qa-p/technology-questions)  2 weeks ago
* [Evaluating SAP’s new MCP servers: UI5, CAP, and Fiori tools in practice](/t5/technology-blog-posts-by-members/evaluating-sap-s-new-mcp-servers-ui5-cap-and-fiori-tools-in-practice/ba-p/14205611)
  in [Technology Blog Posts by Members](/t5/technology-blog-posts-by-members/bg-p/technology-blog-members)  a month ago
* [Applying 'Techncial User Propagation' to API Management](/t5/technology-blog-posts-by-sap/applying-techncial-user-propagation-to-api-management/ba-p/14191788)
  in [Technology Blog Posts by SAP](/t5/technology-blog-posts-by-sap/bg-p/technology-blog-sap)  2025 Aug 29

Top kudoed authors...