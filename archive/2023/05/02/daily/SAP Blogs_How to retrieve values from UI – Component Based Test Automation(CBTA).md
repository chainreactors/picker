---
title: How to retrieve values from UI – Component Based Test Automation(CBTA)
url: https://blogs.sap.com/2023/05/01/how-to-retrieve-values-from-ui-cbta-test-automation/
source: SAP Blogs
date: 2023-05-02
fetch_date: 2025-10-04T11:39:18.920385
---

# How to retrieve values from UI – Component Based Test Automation(CBTA)

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Technology](/t5/technology/ct-p/technology)
* [Technology Blog Posts by Members](/t5/technology-blog-posts-by-members/bg-p/technology-blog-members)
* How to retrieve values from UI – Component Based T...

Technology Blog Posts by Members

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/technology-blog-members/article-id/163007&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [How to retrieve values from UI – Component Based Test Automation(CBTA)](/t5/technology-blog-posts-by-members/how-to-retrieve-values-from-ui-component-based-test-automation-cbta/ba-p/13567098)

![Rittika](https://avatars.profile.sap.com/f/8/idf8d5e07c6934feb2c0729c869457727c7e7a4626c05733c3e1b1566820e1a5f6_small.jpeg "Rittika")

[Rittika](https://community.sap.com/t5/user/viewprofilepage/user-id/123061)

Participant

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=technology-blog-members&message.id=163007)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/technology-blog-members/article-id/163007)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13567098)

‎2023 May 01
9:10 AM

[2
Kudos](/t5/kudos/messagepage/board-id/technology-blog-members/message-id/163007/tab/all-users "Click here to see who gave kudos to this post.")

1,628

* SAP Managed Tags
* [SAP Solution Manager](https://community.sap.com/t5/c-khhcw49343/SAP%2520Solution%2520Manager/pd-p/01200615320800000636)
* [SOLMAN Test Suite](https://community.sap.com/t5/c-khhcw49343/SOLMAN%2520Test%2520Suite/pd-p/132949817163443344955330185779754)

* [SAP Solution Manager

  SAP Solution Manager](/t5/c-khhcw49343/SAP%2BSolution%2BManager/pd-p/01200615320800000636)
* [SOLMAN Test Suite

  Software Product Function](/t5/c-khhcw49343/SOLMAN%2BTest%2BSuite/pd-p/132949817163443344955330185779754)

View products (2)

**Solution Manager 7.2 SP 16**

**CBTA 3.0 SP 19.2**

**SAP GUI 800**

CBTA test scripts are not built by writing any coding. They are built by aggregating components. A common need in test script recording/execution is to retrieve the value of screen components from UI. It is required to map the value of output parameters from one test script to other test script to test end-to-end business scenarios. In this blog post we will discuss about various techniques of retrieving information from SAP GUI so that values can be mapped to other child scripts.

**Scenario 1 – Retrieving information from status bar**

In this scenario, we want to retrieve the information from the success message in status bar. This can be easily accomplished via execution context. The execution context can be seen as a shared memory where information is stored to make it available to the subsequent steps of the test script.

With CBTA, the execution context can be populated with computed values. The typical use case is to dynamically create a variable, in which the result of a step is stored and reused by the next ones.

For example, the business scenario could be to use the VA01 transaction to create a Sales Order and use the ID of the newly created sales order in the YME59 transaction to create a PO.

Sales order creation will generate a success message in status bar. This example can be automated using the CBTA\_GUI\_SB\_GETMESSAGEPARAMS component. This component retrieves the parameter values of the status bar and stores them in variables that are prefixed by the transaction code.

![](/legacyfs/online/storage/blog_attachments/2023/05/Pic1.jpg)

The status bar of the VA01 transaction creates the following variables:

* VA01\_MessageStatus

* VA01\_MessageParameter0

* VA01\_MessageParameter1

The information retrieved from the status bar (of type GuiStatusbar) is visible in the execution report, as shown below:

![](/legacyfs/online/storage/blog_attachments/2023/05/Pic2.jpg)

The runtime library resolves the value of each component parameter by replacing each token with the value of the corresponding variable. This value can be easily mapped to subsequent scripts.

**Scenario 2 – Retrieving information embedded in SAP GUI screen**

In this scenario, we want to retrieve the information embedded in SAP GUI screen. CBTA relies on the concept of components. Most of the components are used to simulate user interactions. Some others are used to verify the application consistency; they get information from the UI and provide the ability to perform checkpoints

For example, retrieving the value of Purchase Requisition from below SAP GUI screen.

![](/legacyfs/online/storage/blog_attachments/2023/05/Pic3.jpg)

Another example could be retrieving the value of Purchase order from below SAP GUI screen.

![](/legacyfs/online/storage/blog_attachments/2023/05/Pic4.jpg)

To achieve this, the Test Engineer can define checkpoints while recording the scenario in CBTA Test recording Wizard. Each checkpoint will be converted into a step in the generated test script. The component used to perform the check may vary depending on the UI technology used by the application being tested.

We may press the “*Add Checkpoint*” button while recording the script to start the *Check Picker* mode.

![](/legacyfs/online/storage/blog_attachments/2023/05/Pic5.jpg)

The test engineer can define checkpoints to verify the consistency of the application or to simply retrieve information from the UI.

* **Check Data** must be selected to define a checkpoint

* **Get Data** must be selected to retrieve information

![](/legacyfs/online/storage/blog_attachments/2023/05/Pic6.jpg)

*Check data details*

The default components used to perform the checks for SAP GUI transactions are:

* CBTA\_GUI\_GETPROPERTY

* CBTA\_GUI\_CHECKPROPERTY

While recording the script, press “Add checkpoint” button to start the check picker mode.

![](/legacyfs/online/storage/blog_attachments/2023/05/Pic7.jpg)

Select the component from SAP GUI screen whose value needs to be captured.

![](/legacyfs/online/storage/blog_attachments/2023/05/Pic8.jpg)

The wizard creates the checkpoint and adds it to the list of steps with some default settings.

![](/legacyfs/online/storage/blog_attachments/2023/05/Pic9.jpg)

In this example, the checkpoint checks the Purchase order number, but we only want to retrieve the information. Convert the checkpoint to a simple *Get Data* step by selecting the radio button ‘Get Data’. The corresponding step is updated and the component, which the test will use at runtime, is shown in Step Details section.

![](/legacyfs/online/storage/blog_attachments/2023/05/Pic10.jpg)

![](/legacyfs/online/storage/blog_attachments/2023/05/Pic11.jpg)

![](/legacyfs/online/storage/blog_attachments/2023/05/Pic12.jpg)

This value in CBTA\_GUI\_GETPROPERTY component can be easily passed to subsequent script.

**Scenario 3 – Retrieving information from Strings**

In this scenario, we want to retrieve the information from SAP GUI screen pop-up screen.

![](/legacyfs/online/storage/blog_attachments/2023/05/Pic13.jpg)

We can easily retrieve the value using ‘Add checkpoint’ and ‘Get Data’. But the only challenge is that ‘Get data’ will retrieve full sentence i.e., Inbound delivery 190090339 has been saved. Our objective is to map the value of Inbound delivery ‘190090339’ to subsequent script.

There are many ways to achieve this using VBScript functions. Here, I am using a simple split fu...