---
title: Transport Iflows between different packages in the same SAP Cloud Integration tenant
url: https://blogs.sap.com/2022/12/25/transport-iflows-between-different-packages-in-the-same-sap-cloud-integration-tenant/
source: SAP Blogs
date: 2022-12-26
fetch_date: 2025-10-04T02:31:02.621198
---

# Transport Iflows between different packages in the same SAP Cloud Integration tenant

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Technology](/t5/technology/ct-p/technology)
* [Technology Blog Posts by Members](/t5/technology-blog-posts-by-members/bg-p/technology-blog-members)
* Transport Iflows between different packages in the...

Technology Blog Posts by Members

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/technology-blog-members/article-id/160171&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [Transport Iflows between different packages in the same SAP Cloud Integration tenant](/t5/technology-blog-posts-by-members/transport-iflows-between-different-packages-in-the-same-sap-cloud/ba-p/13550727)

![former_member9237](https://avatars.profile.sap.com/former_member_small.jpeg "former_member9237")

[former\_member9237](https://community.sap.com/t5/user/viewprofilepage/user-id/9237)

Explorer

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=technology-blog-members&message.id=160171)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/technology-blog-members/article-id/160171)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13550727)

‎2022 Dec 25
11:43 AM

[16
Kudos](/t5/kudos/messagepage/board-id/technology-blog-members/message-id/160171/tab/all-users "Click here to see who gave kudos to this post.")

8,684

* SAP Managed Tags
* [Cloud Integration](https://community.sap.com/t5/c-khhcw49343/Cloud%2520Integration/pd-p/67837800100800006801)

* [Cloud Integration

  SAP Integration Suite](/t5/c-khhcw49343/Cloud%2BIntegration/pd-p/67837800100800006801)

View products (1)

# **Introduction**

In this blog I am going to propose you a technical solution that I used on my last project to maintain “**transports**” between multiple environment packages in the same SAP Cloud Integration tenant.

The problem, often found in projects, comes when a SAP Cloud Integration tenant need to support multiple environments. There are situations when, customers usually host DEV and TEST environments in the same Cloud Integration tenant. The challenge comes from having all the environments packages on sync with minimal risks and effort. On this problem SAP tools cannot help us i.e. (File based transport, Transport via CTS+, Transport via SAP Cloud Transport Management).

![](/legacyfs/online/storage/blog_attachments/2022/12/landscape-2.png)Handling multiple environments in the same SAP Cloud Integration tenant

# **Define a procedure**

Before starting to talk about synchronizing packages in the same SAP Cloud Integration tenant, I think it is very important to underline the idea of having a procedure in place that you should follow throughout the entire project.

From my experience I find it very easy to be tempted on changing “small things”, especially on testing phases SIT and UAT, directly on the interest package and after the tests are unblocked to modify also on DEV. But this kind of approach on long term is translated on freezing the DEV package and testing packages to serve on development and testing at the same time.

Even if we have to maintain multiple environments in the same SAP Cloud Integration tenant or not, it is important to have in mind that the DEV package is used only for development and all the changes are done in this package and TEST packages (doesn`t matter how many test systems there are) will be used only for testing and not performing changes on these packages.

# **Manual approach**

Coming back to the packages synchronization in the same SAP Cloud Integration, an option could be downloading the integration flow locally, manually changing the IDs from manifest file and then importing the changes on the target package. This manual approach is not a feasible solution but is important to understand the process.

### Required steps

1. After you download the Integration flow from DEV package go on your computer and open the zip file. Go to the folder **META-INF** where is located the file ****MANIFEST.MF****. Open the file and change the following fields with the ID of the integration flow from TEST package:

* + Bundle-SymbolicName

  + Origin-Bundle-SymbolicName

  + Origin-Bundle-Name

  + Bundle-Name

![](/legacyfs/online/storage/blog_attachments/2022/12/manifest-2.png)Required changes on manifest file

2. Save changes and upload the new ZIP to target integration flow. Go to the Integration flow, under **Action** button select “**View metadata**” and upload the file that you changed at Step 1.

![](/legacyfs/online/storage/blog_attachments/2022/12/upload.png)

Upload changes on Test Integration

With this technique you will be 100% sure that all the changes made in DEV will go to TEST package. But as you probably think, this process is time consuming and of course requires maximum attention to prepare the file.

### Advantage

Ok, looks good, but why do I need this? Why not just delete the old TEST Integration Flow and copy the new version from DEV? The answer is because usually the Integration Flow has configurable parameters and once you make a new copy, it is necessary to change the DEV parameters to TEST. This is time consuming and requires, again maximum attention of checking all of them.

By using this approach, the Integration flow **is updated**, so the configurations remains the same and only thing that the end-user should do is pressing button "**Deploy**". So simple, right?

# **Automatic approach**

The manual process is an option, but still cannot be used in a real project where you have a lot of interfaces and the changes are frequently made in your landscape. In the end the developer will decide to make the changes directly in the environment where the team perform the tests, to save time. The versioning will be destroyed, and the changes will be performed manually in multiple Iflows.

After a short checking on API Business Hub, I have found **[Integration Content](https://api.sap.com/api/IntegrationContent/overview)** API collection. This collection has everything that I need to transform manual process in something that I could use on my project. Combining manual process with the API collection I decided to create a SAP Cloud Integration Iflow that will do the job. I used SAP Cloud Platform Integration to eliminate the hosting problem and the problem was reduced on building and an UI which receives some search keys from end-user, perform standard API calls and sending back a return message.

Bellow are the main steps that the integration flow should have:

1. Save from the request the key that will identify the source and target integration flows:![](/legacyfs/online/storage/blog_attachments/2022/12/parameterspng-1.png)

2. Download the source integration flow using following API call:

**GET https://<CPI\_HOST\_ADDRESS>/IntegrationDesigntimeArtifacts(Id='{Id}',Version='{Version}')/$value**

![](/legacyfs/online/storage/blog_attachments/2022/12/download.png)

Download Integration Flow -API structure

3. The ZIP file received from previous call, will be processed with a groovy script that needs to change from “**MANIFEST.MF**” file, the fields Only Bundle-SymbolicName, Origin-Bundle-SymbolicName, Origin-Bundle-Name, Bundle-Name with the ID of target integration flow. The rest of the ZIP content should remain unchanged.

```
Message replaceIflowID(Message message) {

    def input = message.getBody(java.io.InputStream);

    def S...