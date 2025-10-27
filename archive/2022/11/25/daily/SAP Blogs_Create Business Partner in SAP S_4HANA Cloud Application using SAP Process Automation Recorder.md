---
title: Create Business Partner in SAP S/4HANA Cloud Application using SAP Process Automation Recorder
url: https://blogs.sap.com/2022/11/24/create-business-partner-in-sap-s-4hana-cloud-application-using-sap-process-automation-recorder/
source: SAP Blogs
date: 2022-11-25
fetch_date: 2025-10-03T23:43:47.098674
---

# Create Business Partner in SAP S/4HANA Cloud Application using SAP Process Automation Recorder

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Technology](/t5/technology/ct-p/technology)
* [Technology Blog Posts by SAP](/t5/technology-blog-posts-by-sap/bg-p/technology-blog-sap)
* Create Business Partner in SAP S/4HANA Cloud using...

Technology Blog Posts by SAP

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/technology-blog-sap/article-id/160016&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [Create Business Partner in SAP S/4HANA Cloud using Recorder capability of SAP Build Process Automation](/t5/technology-blog-posts-by-sap/create-business-partner-in-sap-s-4hana-cloud-using-recorder-capability-of/ba-p/13556298)

![former_member766716](https://avatars.profile.sap.com/former_member_small.jpeg "former_member766716")

[former\_member766716](https://community.sap.com/t5/user/viewprofilepage/user-id/766716)

Explorer

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=technology-blog-sap&message.id=160016)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/technology-blog-sap/article-id/160016)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13556298)

‎2022 Nov 24
7:12 PM

[10
Kudos](/t5/kudos/messagepage/board-id/technology-blog-sap/message-id/160016/tab/all-users "Click here to see who gave kudos to this post.")

3,724

* SAP Managed Tags
* [SAP Intelligent Robotic Process Automation](https://community.sap.com/t5/c-khhcw49343/SAP%2520Intelligent%2520Robotic%2520Process%2520Automation/pd-p/73554900100800002142)
* [SAP Cloud Platform, industry edition, client libraries](https://community.sap.com/t5/c-khhcw49343/SAP%2520Cloud%2520Platform%252C%2520industry%2520edition%252C%2520client%2520libraries/pd-p/73555000100800000218)
* [SAP S/4HANA Cloud Public Edition](https://community.sap.com/t5/c-khhcw49343/SAP%2520S%252F4HANA%2520Cloud%2520Public%2520Edition/pd-p/08e2a51b-1ce5-4367-8b33-4ae7e8b702e0)
* [SAP Build Process Automation](https://community.sap.com/t5/c-khhcw49343/SAP%2520Build%2520Process%2520Automation/pd-p/73554900100800003832)
* [SAP Business Technology Platform](https://community.sap.com/t5/c-khhcw49343/SAP%2520Business%2520Technology%2520Platform/pd-p/73555000100700000172)

* [SAP S/4HANA Cloud Public Edition

  SAP S/4HANA Cloud](/t5/c-khhcw49343/SAP%2BS%25252F4HANA%2BCloud%2BPublic%2BEdition/pd-p/08e2a51b-1ce5-4367-8b33-4ae7e8b702e0)
* [SAP Intelligent Robotic Process Automation

  Software Product](/t5/c-khhcw49343/SAP%2BIntelligent%2BRobotic%2BProcess%2BAutomation/pd-p/73554900100800002142)
* [SAP Build Process Automation

  SAP Build](/t5/c-khhcw49343/SAP%2BBuild%2BProcess%2BAutomation/pd-p/73554900100800003832)
* [SAP Business Technology Platform

  Software Product](/t5/c-khhcw49343/SAP%2BBusiness%2BTechnology%2BPlatform/pd-p/73555000100700000172)
* [SAP Cloud Platform, industry edition, client libraries

  SAP Business Technology Platform](/t5/c-khhcw49343/SAP%2BCloud%2BPlatform%25252C%2Bindustry%2Bedition%25252C%2Bclient%2Blibraries/pd-p/73555000100800000218)

View products (5)

Hi Folks,
In this blog, we are going to create business partner in SAP S/4HANA Cloud Application using SAP Process Automation Recorder.

**Pre-requisites**The minimum version required to automate SAP S/4HANA Cloud Application is mentioned below:

* **Agent/MSI version** – 2.0.25.75

* **Extension version** - **V2**– 2.0.25.31

* **Extension version** – **V3**– 3.0.3.3

* **SDK version** – 1.25.57

To start with, lets create a new project in Cloud Studio and open SAP S/4HANA Cloud Application in a new browser window.

![](/legacyfs/online/storage/blog_attachments/2022/11/1-84.png)

**Step 1** - Create a new application. Now all the applications running in our machine would be listed down. We need to select SAP S/4HANA Cloud Application cloud from the list.

![](/legacyfs/online/storage/blog_attachments/2022/11/2-47.png)

**Step 2**. When SAP S/4HANA Cloud Application is selected, two options are available in the Cloud Studio – Recorder and Manual Capture.

We will move on with the Recorder option in this blog. So, let us click on Record button.

![](/legacyfs/online/storage/blog_attachments/2022/11/3-41.png)

**Step 3**: We can see the recording widget is launched on top of the SAP S/4HANA Cloud Application.
To start the recording, click on the red button.

![](/legacyfs/online/storage/blog_attachments/2022/11/4-33.png)

**Step 4:** Once the page is captured, enter username, password and then click on login button.

![](/legacyfs/online/storage/blog_attachments/2022/11/5-25.png)

**Step 5**: Now that we have logged into the application, we can see there are different tiles listed on the UI.

**Since there is a change in the UI and we are in automatic capture mode, the recording widget automatically captures the new screen without any user intervention**.

**To utilize the Auto Capture feature of the SAP Process Automation Recorder, the minimum version required is  -**

* **Agent/MSI version** – 2.0.31.47

* **Extension version** - **V2**– 2.0.31.46

* **Extension version** – **V3**– 3.0.3.3

* **SDK version** – 1.31.49

*Else we need to capture the screen by clicking on the camera button every time we get the Capture Hint in the recording widget or if there is a change in UI.*

Once the new screen is automatically captured by the recording widget. Click on arrow and select Business Partner Master from the list.

![](/legacyfs/online/storage/blog_attachments/2022/11/6-22.png)

**Step 6**: Click Maintain Business Partner tile.

![](/legacyfs/online/storage/blog_attachments/2022/11/7-27.png)

**Step 7**: Then after click Organization and wait until the recording widget is finished capturing the new screen.

![](/legacyfs/online/storage/blog_attachments/2022/11/8-24.png)

**Step 8**: Select the grouping as per your choice. Here I have selected Ext. alphanumeric numbering.

![](/legacyfs/online/storage/blog_attachments/2022/11/9-38.png)

**Step 9**: Enter the value for Business Partner as per the grouping.

I have entered BP001.

![](/legacyfs/online/storage/blog_attachments/2022/11/10-16.png)

**Step 10**: Now fill in the Name and Address.

![](/legacyfs/online/storage/blog_attachments/2022/11/11-17.png)

**Step 11**: Once the details are filled in, click on Save to create a new business partner with the given details.

![](/legacyfs/online/storage/blog_attachments/2022/11/12-16.png)

**Step 12**: Since we have successfully recorded a scenario to create business partner in Cloud Studio. Now click on stop recording and export the artifacts.

![](/legacyfs/online/storage/blog_attachments/2022/11/13-15.png)

After the artifacts are downloaded, an application and an automation are saved in Cloud Studio.

![](/legacyfs/online/storage/blog_attachments/2022/11/14-14.png)

Any changes to the business partner data can be made in Cloud Studio even after exporting the artifacts. Select the activity and then update the input parameter.

![](/legacyfs/online/storage/blog_attachments/2022/11/15-13.png)

We can also provide the business partner data from an excel.

To create the business partner from the excel data, the above automation needs to be enhanced. We will create an automation that will read and process the data from excel and then pass the business partner data to the current automation.

Let us create a new automation to read the business partner data from excel.

The excel that ...