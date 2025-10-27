---
title: API trigger failed? Here’s why you got 422 error
url: https://blogs.sap.com/2023/07/23/api-trigger-failed-heres-why-you-got-422-error/
source: SAP Blogs
date: 2023-07-24
fetch_date: 2025-10-04T11:52:24.198751
---

# API trigger failed? Here’s why you got 422 error

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Technology](/t5/technology/ct-p/technology)
* [Technology Blog Posts by SAP](/t5/technology-blog-posts-by-sap/bg-p/technology-blog-sap)
* API trigger fail? Here's why you got 422 error

Technology Blog Posts by SAP

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/technology-blog-sap/article-id/162788&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [API trigger fail? Here's why you got 422 error](/t5/technology-blog-posts-by-sap/api-trigger-fail-here-s-why-you-got-422-error/ba-p/13564931)

![Dan_Wroblewski](https://avatars.profile.sap.com/d/6/idd630780f059388c9e8e8fa9d85021d5fbf6d51e34b585117ee5e4425f1998531_small.jpeg "Dan_Wroblewski")

![Developer Advocate](/html/@138D6F765B60D7FC0168643DE27D8A68/rank_icons/sap-logo-small-14px.png "Developer Advocate")
[Dan\_Wroblewski](https://community.sap.com/t5/user/viewprofilepage/user-id/72)

Developer Advocate

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=technology-blog-sap&message.id=162788)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/technology-blog-sap/article-id/162788)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13564931)

‎2023 Jul 23
7:53 AM

[10
Kudos](/t5/kudos/messagepage/board-id/technology-blog-sap/message-id/162788/tab/all-users "Click here to see who gave kudos to this post.")

4,451

* SAP Managed Tags
* [SAP Build Apps](https://community.sap.com/t5/c-khhcw49343/SAP%2520Build%2520Apps/pd-p/6cfd8176-04ae-4548-8f38-158456e1a47a)
* [SAP Build](https://community.sap.com/t5/c-khhcw49343/SAP%2520Build/pd-p/73555000100700001491)
* [SAP Build Process Automation](https://community.sap.com/t5/c-khhcw49343/SAP%2520Build%2520Process%2520Automation/pd-p/73554900100800003832)

* [SAP Build Apps

  Additional Software Product](/t5/c-khhcw49343/SAP%2BBuild%2BApps/pd-p/6cfd8176-04ae-4548-8f38-158456e1a47a)
* [SAP Build

  Software Product](/t5/c-khhcw49343/SAP%2BBuild/pd-p/73555000100700001491)
* [SAP Build Process Automation

  SAP Build](/t5/c-khhcw49343/SAP%2BBuild%2BProcess%2BAutomation/pd-p/73554900100800003832)

View products (3)

Just yesterday, I got an email from a participant in one of my recent SAP Build CodeJams in the Netherlands, who was having trouble calling the SAP Build Process Automation API to trigger his process. I get these questions all the time.

![](/legacyfs/online/storage/blog_attachments/2023/07/2023-07-23_08-20-45-scaled.jpg)

Well, I have documented (almost) all of the reasons why your API call could fail (except for the fact that you have no internet connection), and I mapped them to the status code you would receive.

I am really proud of this documentation – I try to anticipate what problems you might face and, through a lot of trial and error, I try to determine what each status code means. But the documentation is buried in my [tutorial](https://developers.sap.com/tutorials/build-apps-workflow-trigger.html) for the CodeJam, so I'd thought I give it it's own blog post.

---

So here's what could go wrong with your API call:

* **403:** The destination to the SAP Build Process Automation API is not configured properly. Make sure the client ID, secret, service URL and authentication URL (with `/oath/token` path) are set correctly. Do not add user/password for the authentication URL.

* **404:** The API did not recognize the name of your process (i.e., `definitionId` in the request body mapper) or the path to the service is wrong – both in the **create** tab. A wrong path, of course, could be caused by a problem in either the base URL or the path of the **create** action.

* **415:** You did not send the `Content-Type` request header.

* **422:** This basically means that the API heard your call but it didn’t like something in the request body. This is probably the most common and vexing problem. More on this error below.

* **500:** This may mean that your URLs are wrong, especially, you may have the wrong URL for OAuth authentication, such as you forget to add the path `/oauth/token`.

## Debugging 422 Error

Getting 422 when calling your trigger is the most common problem. There are essentially 2 reasons for this:

* The names of the trigger/input parameters that you sent do not match the parameters you defined (case sensitive).

* The values you sent are not of the right data types. For example, you sent text for a number field or an invalid date format (dates must be in this format: `2023-01-31`).

![](/legacyfs/online/storage/blog_attachments/2023/07/2023-07-23_08-59-19.jpg)

It only takes a few minutes to debug such an error. It helps to do the following:

* Check the trigger in your deployed process to see what the process is expecting. ![](/legacyfs/online/storage/blog_attachments/2023/07/2023-07-23_09-44-55-scaled.jpg)

* Use the browser's Developer Tools (and then select the **Network** tab) to check what values were sent. For example, from SAP Build Apps, run a test of the trigger from the **Data** tab, and you will get a call labeled with the name of the destination. Then look at the payload for what request body was sent. ![](/legacyfs/online/storage/blog_attachments/2023/07/2023-07-23_09-40-21-scaled.jpg)

Now match them up and see what values are mislabeled or missing.

### Startling discovery

But while experimenting for this blog, I found out something interesting: **the API call does NOT care what parameters you send**.

That's right.

You can send whatever parameters you want, or you can even not send the `context` part of the payload at all. You can send parameters with the wrong name, or extra parameters.

The **422** error occurs only when you use the parameters in your workflow, for example, displaying them in a form, and they are of the wrong data type. More specifically, it can occur when you define a date field in a form and you map it to a trigger parameter that is not formatted as a date or to a parameter that has not been sent at all.

I am not sure how you catch such bad input inside your process – comment below if you know.

|
 You still need to send some valid JSON, or you will get a **400** error. And you must send a **definitionId** or you will get a **404** error. |

## Documentation on SAP Business Accelerator Hub

I never took notice of it, but there is helpful [documentation](https://api.sap.com/api/SPA_Workflow_Runtime/path/post_v1_workflow_instances) about the error messages in the API documentation. For example, it explains that 404 is thrown when the `definitionId` is missing or the specified process instance does not exist, so it can be quite helpful.

![](/legacyfs/online/storage/blog_attachments/2023/07/2023-07-23_09-23-48.jpg)

But not all the messages are fully explained, and that is what I tried to do above.

Labels

* [Technology Updates](/t5/technology-blog-posts-by-sap/bg-p/technology-blog-sap/label-name/technology%20updates)

5 Comments

You must be a registered user to add a comment. If you've already registered, sign in. Otherwise, register and sign in.

* [Comment](/plugins/common/feature/oidcss/sso_login_redirect/providerid/sap_ids_prompt?redirectreason=permissiondenied&referer=https%3A%2F%2Fcommunity.sap.com%2Ft5%2Ftechnology-blog-posts-by-sap%2Fapi-trigger-fail-here-s-why-you-got-422-error%2Fba-p%2F13564931%23comment-on-this)

Copy Link
![](https://community.sap.com/html/@EE5D5986...