---
title: SAP Build Process Automation – how to trigger process(es) from an automation
url: https://blogs.sap.com/2023/02/16/sap-build-process-automation-how-to-trigger-processes-from-an-automation/
source: SAP Blogs
date: 2023-02-17
fetch_date: 2025-10-04T06:52:16.109044
---

# SAP Build Process Automation – how to trigger process(es) from an automation

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Technology](/t5/technology/ct-p/technology)
* [Technology Blog Posts by SAP](/t5/technology-blog-posts-by-sap/bg-p/technology-blog-sap)
* SAP Build Process Automation - how to trigger proc...

Technology Blog Posts by SAP

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/technology-blog-sap/article-id/160465&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [SAP Build Process Automation - how to trigger process(es) from an automation](/t5/technology-blog-posts-by-sap/sap-build-process-automation-how-to-trigger-process-es-from-an-automation/ba-p/13557602)

![BojanDobranovic](https://avatars.profile.sap.com/6/c/id6c635891ac03fefb55e77345750fd0046367c37622dcdbc51b0533b8b8ca63c0_small.jpeg "BojanDobranovic")

![Product and Topic Expert](/html/@138D6F765B60D7FC0168643DE27D8A68/rank_icons/sap-logo-small-14px.png "Product and Topic Expert")
[BojanDobranovic](https://community.sap.com/t5/user/viewprofilepage/user-id/92190)

Product and Topic Expert

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=technology-blog-sap&message.id=160465)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/technology-blog-sap/article-id/160465)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13557602)

‎2023 Feb 16
11:28 PM

[13
Kudos](/t5/kudos/messagepage/board-id/technology-blog-sap/message-id/160465/tab/all-users "Click here to see who gave kudos to this post.")

10,838

* SAP Managed Tags
* [SAP Build](https://community.sap.com/t5/c-khhcw49343/SAP%2520Build/pd-p/73555000100700001491)
* [SAP Build Process Automation](https://community.sap.com/t5/c-khhcw49343/SAP%2520Build%2520Process%2520Automation/pd-p/73554900100800003832)

* [SAP Build

  Software Product](/t5/c-khhcw49343/SAP%2BBuild/pd-p/73555000100700001491)
* [SAP Build Process Automation

  SAP Build](/t5/c-khhcw49343/SAP%2BBuild%2BProcess%2BAutomation/pd-p/73554900100800003832)

View products (2)

***Update***: Among other great enhancements introduced in the April 2023 release of SAP Build Process Automation, we now have capability to trigger business process (workflow) directly from automation without a single line of code.

Please also check [this blog post](https://blogs.sap.com/2023/04/05/introducing-subprocesses-as-referenced-subflows-in-sap-build-process-automation/) to get familiar with new important topic of Subprocesses as Referenced Subflows.

This blog post can still be useful if you need to trigger some other service that requires token authentication. All you need to do to trigger a workflow is to select it from list of available business processes with API triggers and configure input parameters:

![](/legacyfs/online/storage/blog_attachments/2023/02/update_processes-scaled.jpg)

# Intro

Let's imagine a typical use case - your automation should fetch multiple invoice files from some source (file folder, Outlook, Gmail, FTP, etc.). Automation will loop through your file collection, extract data from those invoices using DOX and then analyze if everything is OK. Automation can post some of the invoices but what if PO is missing, or your 3-factor authentication found problems, or confidence level of recognition is low for some elements, or for larger total amount you must have a multi step approval?

There can be many different workflows that you will need to fire based on different conditions found in your invoices.

This blog post will show you how to do that - call SAP Build Process Automation [SBPA] Business Process  (workflow artifact) from an Automation (RPA artifact).

![](/legacyfs/online/storage/blog_attachments/2022/12/blog-main-2-scaled.jpg)

*Figure 1: Process example (click to enlarge)*

This was just one use case example but there are many situations and more complex scenarios where you will need to automate something and based on detected conditions trigger a different workflow for each condition.

![](/legacyfs/online/storage/blog_attachments/2022/12/automation-condition.jpg)

*Figure 2: Automation example (click to enlarge)*

Assumption is that all your processes are created and deployed in SAP Build Process Automation and each process is triggered by API call. *(To find out how to create a process workflow with API trigger check this [blog](https://blogs.sap.com/2022/12/02/start-your-business-process-through-an-api-trigger-in-sap-build-process-automation/).)*

![](/legacyfs/online/storage/blog_attachments/2022/12/process.jpg)

*Figure 3: Process' API trigger example (click to enlarge)*

In most cases your workflow will be part of the same project as your automation, but please note that you can call any SBPA workflow that is part of another project or even deployed on another tenant (as long as you have needed security credentials).

# Solution

In monitoring part of the SBPA check details of your deployed process API. It's important to know the expected JSON payload structure for this particular process (red rectangle). It's important to know exact field names as well as type of values (in this example 2 string inputs, one numeric and one boolean). On this screen you will find **URL** and **definitionID** values that we will need later (yellow rectangle).

![](/legacyfs/online/storage/blog_attachments/2022/12/api-definition-scaled.jpg)

In your project create a new custom data type called "Context". It's important that names and types are exactly the same as in your API definition.

![](/legacyfs/online/storage/blog_attachments/2022/12/context-data-type.jpg)

Now create an additional  custom data type called "WF API Trigger" that will hold all necessary (project/tenant specific) data to execute an API call.

![](/legacyfs/online/storage/blog_attachments/2022/12/datatype-for-api-variables.jpg)

Define 2 new variables in your automaton project. First is of type "WF API Trigger" and rename output to **myAPI**.

![](/legacyfs/online/storage/blog_attachments/2022/12/variable1.jpg)

For input values select custom data and add needed values. Before you saw where to find values for **api\_url** and **definition\_id**. To find other values you will need to go to your BTP Cockpit and click on service key of your SBPA instance and copy values from pop-up window:

![](/legacyfs/online/storage/blog_attachments/2022/12/credentials.jpg)

Values for **client\_id**, **client\_secret** and **token\_url** can be found here:

![](/legacyfs/online/storage/blog_attachments/2022/12/service_key.jpg)

Please note that **url** from service key MUST be appended with "**/oauth/token**" so the value of **token\_url** should look like this "<https://yourtenant.authentication.eu10.hana.ondemand.com>**/oauth/token**".

Now add any values you want for Context variable and rename it to **myContext**:

![](/legacyfs/online/storage/blog_attachments/2022/12/variable2.jpg)

Before calling the web service, you must prepare the JSON object with all the necessary data. There is a package in the Store called "Web services Best Practices". I encourage you to check those examples (as well as other packages from the store because they are great for learning and inspiration).

However, examples in this package don't cover cases where you need to authenticate using oAuth 2 (we first need to fetch the token and then execute POST call with payload)  so you will now add custom script to your project and define...