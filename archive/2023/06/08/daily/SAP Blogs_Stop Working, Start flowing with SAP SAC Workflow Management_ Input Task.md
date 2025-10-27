---
title: Stop Working, Start flowing with SAP SAC Workflow Management: Input Task
url: https://blogs.sap.com/2023/06/07/stop-working-start-flowing-with-sap-sac-workflow-management-input-task/
source: SAP Blogs
date: 2023-06-08
fetch_date: 2025-10-04T11:47:11.484357
---

# Stop Working, Start flowing with SAP SAC Workflow Management: Input Task

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Technology](/t5/technology/ct-p/technology)
* [Technology Blog Posts by Members](/t5/technology-blog-posts-by-members/bg-p/technology-blog-members)
* Stop Working, Start flowing with SAP SAC Workflow ...

Technology Blog Posts by Members

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/technology-blog-members/article-id/160879&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [Stop Working, Start flowing with SAP SAC Workflow Management: Input Task](/t5/technology-blog-posts-by-members/stop-working-start-flowing-with-sap-sac-workflow-management-input-task/ba-p/13555161)

![monica_sugeth](https://avatars.profile.sap.com/7/6/id76276346aec60c56b6e7abf51f1bd5cb89534b86d1f0c7979e04d0385d04f3f6_small.jpeg "monica_sugeth")

[monica\_sugeth](https://community.sap.com/t5/user/viewprofilepage/user-id/852059)

Explorer

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=technology-blog-members&message.id=160879)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/technology-blog-members/article-id/160879)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13555161)

‎2023 Jun 07
11:03 PM

[3
Kudos](/t5/kudos/messagepage/board-id/technology-blog-members/message-id/160879/tab/all-users "Click here to see who gave kudos to this post.")

2,325

* SAP Managed Tags
* [SAP Analytics Cloud](https://community.sap.com/t5/c-khhcw49343/SAP%2520Analytics%2520Cloud/pd-p/67838200100800006884)
* [SAP Analytics Cloud for planning](https://community.sap.com/t5/c-khhcw49343/SAP%2520Analytics%2520Cloud%2520for%2520planning/pd-p/819703369010316911100650199149950)
* [SAP Analytics Hub](https://community.sap.com/t5/c-khhcw49343/SAP%2520Analytics%2520Hub/pd-p/73555000100800000638)

* [SAP Analytics Cloud

  SAP Analytics Cloud](/t5/c-khhcw49343/SAP%2BAnalytics%2BCloud/pd-p/67838200100800006884)
* [SAP Analytics Hub

  SAP Analytics Hub](/t5/c-khhcw49343/SAP%2BAnalytics%2BHub/pd-p/73555000100800000638)
* [SAP Analytics Cloud for planning

  Software Product](/t5/c-khhcw49343/SAP%2BAnalytics%2BCloud%2Bfor%2Bplanning/pd-p/819703369010316911100650199149950)

View products (3)

I am Monica Elam Parithi, a Senior SAP Consultant working in SAC and ByD.

In this article, I would like to provide comprehensive insights into the “Input Task” in SAC.

We will generate an Input Task rather than share the version with each responsible member and risk getting out of track.

In most cases, we share the version with responsible members and don’t know which task is performed by which member. This is where the Input task plays the key role.

**What is an Input task?**

* Input Task is used to obtain feedback or value changes or other additional information from colleagues.

* It can be assigned to one or more colleagues and can be used to work iteratively on different assignments.

* Here each Assignee works individually on the assigned task in a private version so it will not disturb the actual values (Original Story remains unchanged) and will also not be visible to any other users.

* Once the task is completed and after it is reviewed by the owner of the input task it will be published from the private to the public version.

**What are the Prerequisites to Perform Input Task?**

* You need to start by creating a Story using the Planning Model

* The model must have at least one dimension by which the responsible users (Assigner/Assignee) can be identified.

* There must be an active Private Version to create a task.

* To perform this process, the Story must have the Actual values for the data which has to be updated.

**Process Flow of Input Task**

Assign the responsible person in the dimension of the Data Model.![](/legacyfs/online/storage/blog_attachments/2023/06/Input-Task1.png)

A brief example for the Input Task: Let us consider that the owner of the model needs to assign the task to “NJACOB” (the Assignee). In this case, it is the Sales Head and he wants to update the sales team’s working hours and cost and it is for that reason that he is using the “Input Task.”

**Step-1:**

* Open the Story where the Input Task is to be created.

* The Story must have the Private version for task allocation, here I have used the private version named “Input Task.”

* Choose the “More” icon and select the “Create Input Task.”

![](/legacyfs/online/storage/blog_attachments/2023/06/Input-Task2.png)

**Step-2***:* The summary page tab will be created on the left side of the story page

* Specify the due date.

* Enable “Cancel task on the due date automatically.” This is needed if you wish to cancel the task on the due date upon completion.

* You can also add a reminder to inform the Assignee about the task.

* Enable the “Models” Check box.

* In “Versions,” select the private version against which we are going to assign the task.

* Under “Distribution” select the Dimension against which the Person responsible is assigned in the data model.

![](/legacyfs/online/storage/blog_attachments/2023/06/Input-Task3.png)

* Enable the checkbox against which the assignee is going to work. I have assigned for “Refining” and “Corporate” members.

* Before clicking on “Send” make sure there are no other Versions in edit mode.

* Click on “Send” (The task will be sent as mail and notified in the SAC).

![](/legacyfs/online/storage/blog_attachments/2023/06/Input-Task4.png)

**Step-3***:* Action to be performed by the Assignee NJACOB:

* The Assignee receives the task in the notification and selects the task.

![](/legacyfs/online/storage/blog_attachments/2023/06/Input-Task5.png)

* Assignee will be able to see the Task for active members. Initially, the status of the task will show “In Process.”

* Choose one of the “Active Members” to switch to the active Story where you wish to edit.

* On selecting the member “Sales,” we will be navigated to the Sales Cost center on the Story page.

![](/legacyfs/online/storage/blog_attachments/2023/06/Input-Task6.png)

* Initially the value of Sales is “0.”

![](/legacyfs/online/storage/blog_attachments/2023/06/Input-Task7.png)

* The value is specified by the owner of the Cost Center “Sales”

![](/legacyfs/online/storage/blog_attachments/2023/06/Input-Task8.png)

* After completing the task, click on “Submit.” Add the comment if needed and then Submit.

![](/legacyfs/online/storage/blog_attachments/2023/06/Input-Task9.png)

**Step-4***:* The Owner of the task gets the notification in both mail and SAC. The owner opens the Input Task and that changes the Task Status to “Submitted.”

![](/legacyfs/online/storage/blog_attachments/2023/06/Input-Task10.png)

* Check the values updated by the Assignee; the Assigner can either Approve or Cancel the submitted task.

* Once the task is approved or cancelled by the owner of the task, the Assignee will be intimated through mail and SAC tenant.

* Now the Status is changed to “Successful.”

![](/legacyfs/online/storage/blog_attachments/2023/06/Input-Task11.png)

* In this case, the task is approved, and after the approval, the updated values are available in the Original Story. Now you can convert the Private Version to the Public Version, which makes it visible for all the users.

![](/legacyfs/online/storage/blog_attachments/2023/06/Input-Task12.png)

In conclusion, we can easily assign the task and track the work by the ow...