---
title: SAP CPI Exception Handling – Tips – Return to main flow
url: https://blogs.sap.com/2023/01/24/sap-cpi-exception-handling-tips-return-to-main-flow/
source: SAP Blogs
date: 2023-01-25
fetch_date: 2025-10-04T04:43:40.168748
---

# SAP CPI Exception Handling – Tips – Return to main flow

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Technology](/t5/technology/ct-p/technology)
* [Technology Blog Posts by Members](/t5/technology-blog-posts-by-members/bg-p/technology-blog-members)
* SAP CPI Exception Handling - Tips - Return to main...

Technology Blog Posts by Members

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/technology-blog-members/article-id/163656&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [SAP CPI Exception Handling - Tips - Return to main flow](/t5/technology-blog-posts-by-members/sap-cpi-exception-handling-tips-return-to-main-flow/ba-p/13571453)

![irvinrufus](https://avatars.profile.sap.com/e/9/ide985f40e0334ad34f799662d0bc9256d0c2f77802f2271cb6ae52c2f8c5b062e_small.jpeg "irvinrufus")

[irvinrufus](https://community.sap.com/t5/user/viewprofilepage/user-id/13558)

Explorer

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=technology-blog-members&message.id=163656)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/technology-blog-members/article-id/163656)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13571453)

‎2023 Jan 24
8:12 PM

[6
Kudos](/t5/kudos/messagepage/board-id/technology-blog-members/message-id/163656/tab/all-users "Click here to see who gave kudos to this post.")

19,249

* SAP Managed Tags
* [SAP Integration Suite](https://community.sap.com/t5/c-khhcw49343/SAP%2520Integration%2520Suite/pd-p/73554900100800003241)
* [Cloud Integration](https://community.sap.com/t5/c-khhcw49343/Cloud%2520Integration/pd-p/67837800100800006801)

* [Cloud Integration

  SAP Integration Suite](/t5/c-khhcw49343/Cloud%2BIntegration/pd-p/67837800100800006801)
* [SAP Integration Suite

  SAP Integration Suite](/t5/c-khhcw49343/SAP%2BIntegration%2BSuite/pd-p/73554900100800003241)

View products (2)

*Introduction*

CPI is a wonderful technology for B2B scenarios helping us connecting different systems, organize and transform data. As with connecting different systems, we may also at times need to process exceptions when things don't follow the way we expect them to.

This blog provides a beginner level insight into handling an exception in CPI.

CPI has the capability to handle exceptions. However, the way the exceptions are handled may be a little different than a beginner might expect. *It was definitely different than what I expected ![:slightly_smiling_face:](/html/@CB193FD929C1B3F628B5259D5B23C3AB/emoticons/1f642.png ":slightly_smiling_face:")*

As a traditional ABAP developer, I was expecting to catch the exception and route the control to the subsequent steps in the main iFlow. But, exception handling in CPI by design does NOT return to the main flow after an exception is raised.

For example, in the below flow, I'm expecting an exception at "Get gvCounter" step. But once the control proceeds to Exception process, the control does not return to the main integration flow  to process the rest of the steps.

![](/legacyfs/online/storage/blog_attachments/2023/01/SAP-CPI-Exception-01-01.png)

Exception Handling Issue

*Solution option*

How could the exception sub-process be routed back to the main flow?

One solution option is to group the subsequent processes in the main flow into a sub process and invoke the sub process within the Exception flow.

By granularizing the main process into sub processes, we can deviate the exception flow to process the remaining steps in the Integration flow.

Overview of the steps

1. **Define** the rest of the process flow as a local integration process as "**remainingFlow**"

2. **invoke** the "remainingFlow" from the exception handling flow

3. **Add** another step to invoke "remainingFlow" after the step that throws the exception. This is because we need the "remainingFlow" to be processed even when there is no exception.

**Step 01** - defining the "remainingFlow".

![](/legacyfs/online/storage/blog_attachments/2023/01/Define_remainingFlow.png)

**Step 02** - Define an exception process and invoke "remainingFlow" from the exception process.

In my example, I'm expecting an exception at the Get persist variable step "Get gvCounter". So, I'm defining an exception handling process to handle the error when the variable gvCounter is not persisted before.

![](/legacyfs/online/storage/blog_attachments/2023/01/SAP-CPI-Exception-03.png)

Define Exception Handling - Invoke remainingFlow

**Step 03** - I also need to make sure that the "reminingFlow" is processed even when there is no exceptions.

So, I'm invoking the "reminingFlow" in my main flow as well.

![](/legacyfs/online/storage/blog_attachments/2023/01/SAP-CPI-Exception-04.png)

Invoke remainingFlow from Main flow

After deploying, we can see the remainingFlow is invoked irrespective of whether there is an error or not.

*Concluding Thought*

The solution discussed here could be one among the many options. Any experienced developers are welcome to suggest any other methods you know to process the rest of the Integration steps after an exception is raised.

Also feel free to comment any SAP blogs or learning paths that would help learning Integration suite.

*Here are some helpful links that I follow to learn Integration Suite:*

[SAP Integration Suite](https://blogs.sap.com/tags/73554900100800003241/)

[Developing with SAP Integration Suite](https://learning.sap.com/learning-journey/developing-with-sap-integration-suite)

[SAP Integration Suite - Certification Path](https://help.sap.com/learning-journeys/500a46f27a261014ba6a9420b00213f1)

* [errorhandling](/t5/tag/errorhandling/tg-p/board-id/technology-blog-members)
* [exception](/t5/tag/exception/tg-p/board-id/technology-blog-members)
* [ExceptionSubProcess](/t5/tag/ExceptionSubProcess/tg-p/board-id/technology-blog-members)
* [sap cpi](/t5/tag/sap%20cpi/tg-p/board-id/technology-blog-members)

5 Comments

You must be a registered user to add a comment. If you've already registered, sign in. Otherwise, register and sign in.

* [Comment](/plugins/common/feature/oidcss/sso_login_redirect/providerid/sap_ids_prompt?redirectreason=permissiondenied&referer=https%3A%2F%2Fcommunity.sap.com%2Ft5%2Ftechnology-blog-posts-by-members%2Fsap-cpi-exception-handling-tips-return-to-main-flow%2Fba-p%2F13571453%23comment-on-this)

Copy Link
![](https://community.sap.com/html/@EE5D5986E9F4E5657DCEACB7532B5C39/assets/bluesky-dark.svg)Bluesky
Linkedin

Related Content

* [Flexible Workflows for Procurement in SAP S/4HANA](/t5/technology-blog-posts-by-members/flexible-workflows-for-procurement-in-sap-s-4hana/ba-p/14234315)
  in [Technology Blog Posts by Members](/t5/technology-blog-posts-by-members/bg-p/technology-blog-members)  8 hours ago
* [Replicating IT0006 to SAP ECP with a fixed address value, excluding address information in SF EC](/t5/technology-blog-posts-by-members/replicating-it0006-to-sap-ecp-with-a-fixed-address-value-excluding-address/ba-p/14234216)
  in [Technology Blog Posts by Members](/t5/technology-blog-posts-by-members/bg-p/technology-blog-members)  9 hours ago
* [Basic Configurations for SAP EWM Material Flow System: Part-1](/t5/technology-blog-posts-by-members/basic-configurations-for-sap-ewm-material-flow-system-part-1/ba-p/14233314)
  in [Technology Blog Posts by Members](/t5/technology-blog-posts-by-members/bg-p/technology-blog-members)  16 hours ago
* [RAP Using Custom Entity with load multiple data using ...