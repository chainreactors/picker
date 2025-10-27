---
title: Migrating from Workflow Management to SAP Build Process Automation
url: https://blogs.sap.com/2023/07/19/migrating-from-workflow-management-to-sap-build-process-automation/
source: SAP Blogs
date: 2023-07-20
fetch_date: 2025-10-04T11:54:37.243141
---

# Migrating from Workflow Management to SAP Build Process Automation

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Technology](/t5/technology/ct-p/technology)
* [Technology Blog Posts by Members](/t5/technology-blog-posts-by-members/bg-p/technology-blog-members)
* Migrating from Workflow Management to SAP Build Pr...

Technology Blog Posts by Members

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/technology-blog-members/article-id/163534&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [Migrating from Workflow Management to SAP Build Process Automation](/t5/technology-blog-posts-by-members/migrating-from-workflow-management-to-sap-build-process-automation/ba-p/13570296)

![Jana_dK](https://avatars.profile.sap.com/2/6/id26f5d8c4f37bccae5ae0df71cb57a26c4d75a69206db9f89dd59cb463c08122e_small.jpeg "Jana_dK")

![SAP Mentor](/html/@F4C200E47DAE3459A6BD3FBB7F9955B8/rank_icons/mentor-rank-16x16.svg "SAP Mentor")
[Jana\_dK](https://community.sap.com/t5/user/viewprofilepage/user-id/4610)

SAP Mentor

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=technology-blog-members&message.id=163534)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/technology-blog-members/article-id/163534)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13570296)

‎2023 Jul 19
9:47 PM

[10
Kudos](/t5/kudos/messagepage/board-id/technology-blog-members/message-id/163534/tab/all-users "Click here to see who gave kudos to this post.")

6,550

* SAP Managed Tags
* [SAP Workflow Management](https://community.sap.com/t5/c-khhcw49343/SAP%2520Workflow%2520Management/pd-p/73554900100800003239)
* [SAP Build Process Automation](https://community.sap.com/t5/c-khhcw49343/SAP%2520Build%2520Process%2520Automation/pd-p/73554900100800003832)

* [SAP Workflow Management

  SAP Business Technology Platform](/t5/c-khhcw49343/SAP%2BWorkflow%2BManagement/pd-p/73554900100800003239)
* [SAP Build Process Automation

  SAP Build](/t5/c-khhcw49343/SAP%2BBuild%2BProcess%2BAutomation/pd-p/73554900100800003832)

View products (2)

## Introduction

More than a year ago, I started developing a workflow in the Business Application Studio. The workflow itself is started from an automation that monitors an outlook inbox. For every received mail with an attachment, the workflow starts. It’s rather a very complex workflow, which exists of more than 20 possible user tasks (Divided over 4 forms and 6 Custom UI tasks), uses 7 different business rules, has the possibility to call 5 other automations depending on the flow.
Now that Workflow Management and iRPA became deprecated as of June 2023, the time was there to migrate this solution. Here are some thoughts about when to choose how you’re migrating!

## 2 options

There are 2 options to consider when changing to SAP Build Process Automation. You can recreate your workflow in a business process or you can deploy your workflow directly to your SAP Build Process Automation environment after some small changes.

* Recreate the workflow into a business process

* Deploy your workflow to SAP Build Process Automation

I’m going to give you some advantages and disadvantages per option.

## Recreate the workflow in a business process

This is the most timeconsuming option of both. If it’s a more complex workflow, it might take you a lot of time to reproduce the whole flow in a business process.
More importantly is that you’ll have to consider wether the missing features are important for your use case or not.

To start with, you cannot create Custom UI5 tasks and use them in your business process the same way you easily could in a workflow created in the Business Application Studio. The forms embedded now do not have all the options.

That brings me to the next disadvantage for me: no possibility to have more than 2 buttons: an accept and reject button. I have some tasks with 4 to 5 possible options to choose: re-read the business rules if no entry was found, retry the checks in S4 if some (master)data had to be changed in the meantime, forward the task (we recreated our own forwarding possibility), put the task on hold,…

The “condition” possibility. Using a custom script and/or exclusive gateway in a workflow, you can easily use a case and go through all the options. The condition possibility in a business process is not foreseen to handle several outcomes at once.

Also, the intermediate message event is a very important one in my case. I really do want to wait for the outcome and response of an automation.

Iterative flow logic should be coming in Q3, which is also a very handy one. I use it a lot to go through some steps again, but eventually with changed context and different outcomes.

Disadvantages:

* Time consuming

* Not every feature is available yet

  + Custom UI5 Tasks

  + Intermediate message events

  + Only 2 buttons possible

  + No complex expressions

  + Iterative flow logic

Advantages

* All in one project

* Future proof

## Deploy the workflow to SAP Build Process Automation

This is the second, less time consuming, option. There is a possiblity to change some things in your worklow that has been created for the SAP Workflow Management, to make it work on a SAP Build Process Automation environment.
There are three possible things you’d need to change, if used in your workflow:

* Xs-app.json files of your start and task UIs

* API calls to iRPA, workflow or business rules

* yaml file of your workflow

Every exact step you have to take is described here : [https://help.sap.com/docs/workflow-capability/workflow-cloud-foundry/migrate-to-sap-build-process-au...](https://help.sap.com/docs/workflow-capability/workflow-cloud-foundry/migrate-to-sap-build-process-automation)

The biggest advantage here is that you already have a working workflow, you know exactly what it can and cannot and you don’t have to rethink the whole process again. But it is probably not the most future proof option, especially if your workflow is not to complex. You still have to maintain your automations and your workflow seperatly, it’s case-sensitive and a typing error for the payloads is quickly made.

And more important to mention: the versioning problem that has been existing for a while now between workflow and automations. Whenever you have a running instance and you change one of your automations and add a new input parameter, all your running instances will fail. Quite a big disadvantage if you have a new release planned and about 2-3-400 or more running instances.

Advantages

* You know exactly what you’re migrating

* All the options still exist

Disadvantages

* Not future proof

* Seperated environments and code

* Case sensitive

* Versioning

## Conclusion

As my workflow was complicated and using some features that are not able to reproduce in a business process yet, it was a very easy decision to make which option I was going to take.

Having the same options was more important, since they’re really necessary through the whole flow and to have everything working the same way it did before. I’m looking forward to see the whole business process capability evolving into a more major part of the SAP Build Process Automation.

Nevertheless, I hope you all have an idea now about when to choose what option!

Want to know more about my journey in migrating everything from iRPA and Workflow to SAP Build Process Automation? Follow me!

**Questions, thoughts or co...