---
title: Use CPI AMQP adapter to test BTP Event Mesh
url: https://blogs.sap.com/2023/05/13/use-cpi-amqp-adapter-to-test-btp-event-mesh/
source: SAP Blogs
date: 2023-05-14
fetch_date: 2025-10-04T11:38:01.897246
---

# Use CPI AMQP adapter to test BTP Event Mesh

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Technology](/t5/technology/ct-p/technology)
* [Technology Blog Posts by SAP](/t5/technology-blog-posts-by-sap/bg-p/technology-blog-sap)
* Use CPI AMQP adapter to test BTP Event Mesh

Technology Blog Posts by SAP

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/technology-blog-sap/article-id/159307&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [Use CPI AMQP adapter to test BTP Event Mesh](/t5/technology-blog-posts-by-sap/use-cpi-amqp-adapter-to-test-btp-event-mesh/ba-p/13554455)

![Jacky_Liu1](https://avatars.profile.sap.com/0/c/id0c96fbc6ecfa4651eccd3b5e561d0848734220dc92c2198772bae6ac9168e7b7_small.jpeg "Jacky_Liu1")

![Product and Topic Expert](/html/@138D6F765B60D7FC0168643DE27D8A68/rank_icons/sap-logo-small-14px.png "Product and Topic Expert")
[Jacky\_Liu1](https://community.sap.com/t5/user/viewprofilepage/user-id/132085)

Product and Topic Expert

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=technology-blog-sap&message.id=159307)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/technology-blog-sap/article-id/159307)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13554455)

‎2023 May 13
1:33 PM

[5
Kudos](/t5/kudos/messagepage/board-id/technology-blog-sap/message-id/159307/tab/all-users "Click here to see who gave kudos to this post.")

5,823

* SAP Managed Tags
* [Cloud Integration](https://community.sap.com/t5/c-khhcw49343/Cloud%2520Integration/pd-p/67837800100800006801)
* [SAP Event Mesh](https://community.sap.com/t5/c-khhcw49343/SAP%2520Event%2520Mesh/pd-p/73554900100800000765)

* [Cloud Integration

  SAP Integration Suite](/t5/c-khhcw49343/Cloud%2BIntegration/pd-p/67837800100800006801)
* [SAP Event Mesh

  SAP Business Technology Platform](/t5/c-khhcw49343/SAP%2BEvent%2BMesh/pd-p/73554900100800000765)

View products (2)

In the situation of extesionsibility options determination like the following picture, to keep core system clean,for loose coupled application extension, we recommand to use side-by-side extensibility on BTP. In decoupled application, BTP Event Mesh play an important role.  We can realize some requirements with Integration instead of side by side extention.Today I will demo how use CPI AMQP adapter to test BTP event mesh.In my following blogs, I will introduce how to use CPI to realize  some logic triggered by  S/4 Hana Cloud event .

![](/legacyfs/online/storage/blog_attachments/2023/05/Screenshot-2023-05-13-at-17.13.25.png)

## Prerequisite:

* ### You have finished your [Initial Setup for you SAP Integration Suite](https://help.sap.com/docs/integration-suite/sap-integration-suite/initial-setup) .You will have CPI runtime service key information as the following:

![](/legacyfs/online/storage/blog_attachments/2023/05/1-59.png)

* ### For Event Mesh, you have finished the following 3  steps:

1. [Get Started with the Event Mesh User Interface](https://help.sap.com/docs/SAP_EM/bf82e6b26456494cbdd197057c09979f/83777b586ec54a01b5e807620f5c4660.html?locale=en-US)

2. [Setting Up SAP Event Mesh in BTP Cockpit](https://help.sap.com/docs/SAP_EM/bf82e6b26456494cbdd197057c09979f/3ef34ffcbbe94d3e8fff0f9ea2d5911d.html?locale=en-US)

3. [Creating an Event Mesh Instance Using the Default Plan,you will event mesh instance service key like...](https://help.sap.com/docs/SAP_EM/bf82e6b26456494cbdd197057c09979f/d0483a9e38434f23a4579d6fcc72654b.html?locale=en-US)

![](/legacyfs/online/storage/blog_attachments/2023/05/2-28.png)

## Testing Steps:

### 1, Create Event queue as [help .](https://help.sap.com/docs/SAP_EM/bf82e6b26456494cbdd197057c09979f/57af1bd4e8f54b0a9b36414a5ec6b800.html?locale=en-US)

![](/legacyfs/online/storage/blog_attachments/2023/05/3-32.png)

![](/legacyfs/online/storage/blog_attachments/2023/05/4-23.png)

![](/legacyfs/online/storage/blog_attachments/2023/05/5-23.png)

![](/legacyfs/online/storage/blog_attachments/2023/05/6-20.png)

### 2 Create oauth2 client credential in CPI

![](/legacyfs/online/storage/blog_attachments/2023/05/8-19.png)

![](/legacyfs/online/storage/blog_attachments/2023/05/9-15.png)

![](/legacyfs/online/storage/blog_attachments/2023/05/10-13.png)

### 3 Create and deploy iflow in CPI to consume event from event queqe in Event Mesh

![](/legacyfs/online/storage/blog_attachments/2023/05/7-17.png)

![](/legacyfs/online/storage/blog_attachments/2023/05/11-10.png)

![](/legacyfs/online/storage/blog_attachments/2023/05/12-9.png)

![](/legacyfs/online/storage/blog_attachments/2023/05/13-8.png)

![](/legacyfs/online/storage/blog_attachments/2023/05/14-7.png)

```
/* Refer the link below to learn more about the use cases of script.

https://help.sap.com/viewer/368c481cd6954bdfa5d0435479fd4eaf/Cloud/en-US/148851bf8192412cba1f9d2c17f...

If you want to know more about the SCRIPT APIs, refer the link below

https://help.sap.com/doc/a56f52e1a58e4e2bac7f7adbf45b2e26/Cloud/en-US/index.html */

import com.sap.gateway.ip.core.customdev.util.Message;

import java.util.HashMap;

def Message processData(Message message) {

    //Body

    def body = message.getBody(java.lang.String);

    def messageLog = messageLogFactory.getMessageLog(message)

        if (messageLog != null) {

        messageLog.addAttachmentAsString('Em content', body, 'text/plain')

    }

    return message;

}
```

![](/legacyfs/online/storage/blog_attachments/2023/05/15-7.png)

![](/legacyfs/online/storage/blog_attachments/2023/05/16-6.png)

![](/legacyfs/online/storage/blog_attachments/2023/05/17-9.png)

### 4 Create and deploy iflow in CPI to produce event to event queqe in Event Mesh

![](/legacyfs/online/storage/blog_attachments/2023/05/18-7.png)

![](/legacyfs/online/storage/blog_attachments/2023/05/19-5.png)

![](/legacyfs/online/storage/blog_attachments/2023/05/20-4.png)

![](/legacyfs/online/storage/blog_attachments/2023/05/21-5.png)

![](/legacyfs/online/storage/blog_attachments/2023/05/30-2.png)

![](/legacyfs/online/storage/blog_attachments/2023/05/23-3.png)

![](/legacyfs/online/storage/blog_attachments/2023/05/24-3.png)

### 5 Use postmen to send message  to eventissue iflow in step4

![](/legacyfs/online/storage/blog_attachments/2023/05/25-4.png)

![](/legacyfs/online/storage/blog_attachments/2023/05/26-2.png)

### 6 Check result in iflow of event consuption

![](/legacyfs/online/storage/blog_attachments/2023/05/27-2.png)

![](/legacyfs/online/storage/blog_attachments/2023/05/29-3.png)

The End!

Thanks for your time!

Best Regards!

Jacky Liu

Labels

* [Technology Updates](/t5/technology-blog-posts-by-sap/bg-p/technology-blog-sap/label-name/technology%20updates)

* [postman](/t5/tag/postman/tg-p/board-id/technology-blog-sap)

4 Comments

You must be a registered user to add a comment. If you've already registered, sign in. Otherwise, register and sign in.

* [Comment](/plugins/common/feature/oidcss/sso_login_redirect/providerid/sap_ids_prompt?redirectreason=permissiondenied&referer=https%3A%2F%2Fcommunity.sap.com%2Ft5%2Ftechnology-blog-posts-by-sap%2Fuse-cpi-amqp-adapter-to-test-btp-event-mesh%2Fba-p%2F13554455%23comment-on-this)

Copy Link
![](https://community.sap.com/html/@EE5D5986E9F4E5657DCEACB7532B5C39/assets/bluesky-dark.svg)Bluesky
Linkedin

Related Content

* [Extensibility in the Age of AI: Why ABCD Is Easier (and Smarter) Than You Think](/t5/technology-blog-posts-by-sap/extensib...