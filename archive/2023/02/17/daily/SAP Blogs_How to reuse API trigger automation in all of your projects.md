---
title: How to reuse API trigger automation in all of your projects
url: https://blogs.sap.com/2023/02/16/how-to-reuse-api-trigger-automation-in-all-of-your-projects/
source: SAP Blogs
date: 2023-02-17
fetch_date: 2025-10-04T06:52:11.241034
---

# How to reuse API trigger automation in all of your projects

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Technology](/t5/technology/ct-p/technology)
* [Technology Blog Posts by SAP](/t5/technology-blog-posts-by-sap/bg-p/technology-blog-sap)
* How to reuse API trigger automation in all of your...

Technology Blog Posts by SAP

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/technology-blog-sap/article-id/160540&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [How to reuse API trigger automation in all of your projects](/t5/technology-blog-posts-by-sap/how-to-reuse-api-trigger-automation-in-all-of-your-projects/ba-p/13557793)

![BojanDobranovic](https://avatars.profile.sap.com/6/c/id6c635891ac03fefb55e77345750fd0046367c37622dcdbc51b0533b8b8ca63c0_small.jpeg "BojanDobranovic")

![Product and Topic Expert](/html/@138D6F765B60D7FC0168643DE27D8A68/rank_icons/sap-logo-small-14px.png "Product and Topic Expert")
[BojanDobranovic](https://community.sap.com/t5/user/viewprofilepage/user-id/92190)

Product and Topic Expert

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=technology-blog-sap&message.id=160540)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/technology-blog-sap/article-id/160540)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13557793)

‎2023 Feb 16
11:32 PM

[11
Kudos](/t5/kudos/messagepage/board-id/technology-blog-sap/message-id/160540/tab/all-users "Click here to see who gave kudos to this post.")

1,531

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

This blog post can still be useful if you need to want to learn how to reuse your own automations.

All you need to do to trigger a workflow is to select it from list of available business processes with API triggers and configure input parameters:

![](/legacyfs/online/storage/blog_attachments/2023/02/update_processes-scaled.jpg)

# Intro

In my last blog post "[How to trigger process(es) from an automation](https://blogs.sap.com/2023/02/16/sap-build-process-automation-how-to-trigger-processes-from-an-automation/)" I showed you how to create the automation that will trigger the SBPA workflow. Now, I will show you how to turn this autmatomation into a generic solution that can be reused in your projects and shared with other citizen developers/builders on your tenant.

# Solution

## Creating generic reusable automation

Create a new project (or if you followed the last blog post and created a project you can just duplicate it and delete what is not needed). In our project with generic automation we will need only parts of the previous project. We will leave out context data type (that is specific for every single workflow) and create new inputs for our automation.

Data type "WF API trigger" is the same as described in previous blog post.

![](/legacyfs/online/storage/blog_attachments/2023/02/2023-02-15_20-32-23-scaled.jpg)

*FIGURE 1: Data Type (click on picture to enlarge it)*

Since our goal is to create a generic automation we will declare all elements that are workflow-dependent (context and workflow definition URL ) as inputs.

![](/legacyfs/online/storage/blog_attachments/2023/02/2023-02-15_21-00-07.jpg)

*FIGURE 2: Declaring inputs (click to enlarge)*

Instead of declaring our data type with hard coded values we will use environment variables so we can declare values during deployment. Please note that this approach will work in a typical scenario where you have one SBPA tenant for all your projects. If you need to trigger workflows from any tenant, check the subsection "Optional modification" at the end of this blog post.

![](/legacyfs/online/storage/blog_attachments/2023/02/2023-02-15_20-42-14.jpg)

*FIGURE 3: Creation of environment variables (click to enlarge)*

Make sure that your data type has no hardcoded values. We are using 4 environment variables and definition ID (workflow URL) from the input variable.

![](/legacyfs/online/storage/blog_attachments/2023/02/2023-02-15_20-49-05.jpg)

*FIGURE 4: Declare data type and set values (click to enlarge)*

Custom Script and activity "Call Web Service" are completely the same so you can just leave them as is (check previous blog post for details).

Now we finished our generic project. Save it. We must publish and deploy our project to be able to add it to the library and reuse.

![](/legacyfs/online/storage/blog_attachments/2023/02/2023-02-15_15-48-58-scaled.jpg)

*FIGURE 5: Deploying a project (click to enlarge)*

Make sure to enter proper values for all 4 runtime variables (environment variables) in deployment step #2.

After successful deployment, close your project and go back to SAP Build Lobby. You will see that your project is deployed and now you will see action "Publish to Library".

![](/legacyfs/online/storage/blog_attachments/2023/02/2023-02-15_16-06-45-scaled.jpg)

*FIGURE 6: Publish to Library (click to enlarge)*

Select the version you want to publish and leave blank Line Of Business and Product tags.
Your project is now published and available for reuse in every project by any builder/developer on your tenant.

##

## Using our generic automation

Let's now create our regular automation project and switch a view to dependencies. You can see that there are just 2 standard dependencies (core and excel).

![](/legacyfs/online/storage/blog_attachments/2023/02/2023-02-15_16-09-20-scaled.jpg)

*FIGURE 7: Dependencies view (click to enlarge)*

Now we will add a new dependency. Make sure to select "Add a Business Process project dependency".

![](/legacyfs/online/storage/blog_attachments/2023/02/2023-02-15_16-09-37-scaled.jpg)

*FIGURE 8: Adding new Dependency (click to enlarge)*

Select generic project (package) that you just published, select version (if there are more versions) and click add.

![](/legacyfs/online/storage/blog_attachments/2023/02/2023-02-15_16-09-58-scaled.jpg)

*FIGURE 9: Select your generic/reusable package (click to enlarge)*

Now you can switch to Artifact view and see that you still have your test automation but in the right side pane you will also see automation added as dependency. You can use it as any other element and add it to your project.

![](/legacyfs/online/storage/blog_attachments/2023/02/2023-02-15_16-11-11-scaled.jpg)

*FIGURE 10: generic automation is available (click to enlarge)*

Now you can add context data type for each workflow you will need to call, declare data type and add values and then add your API call automation. Populate inputs with context and definitio...