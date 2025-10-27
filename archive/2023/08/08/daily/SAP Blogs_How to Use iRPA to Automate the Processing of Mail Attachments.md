---
title: How to Use iRPA to Automate the Processing of Mail Attachments
url: https://blogs.sap.com/2023/08/07/how-to-use-irpa-to-automate-the-processing-of-mail-attachments/
source: SAP Blogs
date: 2023-08-08
fetch_date: 2025-10-04T12:01:26.515874
---

# How to Use iRPA to Automate the Processing of Mail Attachments

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Technology](/t5/technology/ct-p/technology)
* [Technology Blog Posts by Members](/t5/technology-blog-posts-by-members/bg-p/technology-blog-members)
* How to Use iRPA to Automate the Processing of Mail...

Technology Blog Posts by Members

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/technology-blog-members/article-id/164337&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [How to Use iRPA to Automate the Processing of Mail Attachments](/t5/technology-blog-posts-by-members/how-to-use-irpa-to-automate-the-processing-of-mail-attachments/ba-p/13574862)

![siva_nagireddy](https://avatars.profile.sap.com/8/d/id8dbee40016e3ab8c3eacad7903f72162018bda86a625eec300edfb71890539c1_small.jpeg "siva_nagireddy")

[siva\_nagireddy](https://community.sap.com/t5/user/viewprofilepage/user-id/155522)

Explorer

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=technology-blog-members&message.id=164337)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/technology-blog-members/article-id/164337)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13574862)

‎2023 Aug 07
6:57 PM

[3
Kudos](/t5/kudos/messagepage/board-id/technology-blog-members/message-id/164337/tab/all-users "Click here to see who gave kudos to this post.")

2,781

* SAP Managed Tags
* [SAP Intelligent Robotic Process Automation](https://community.sap.com/t5/c-khhcw49343/SAP%2520Intelligent%2520Robotic%2520Process%2520Automation/pd-p/73554900100800002142)
* [SAP Build Process Automation](https://community.sap.com/t5/c-khhcw49343/SAP%2520Build%2520Process%2520Automation/pd-p/73554900100800003832)

* [SAP Intelligent Robotic Process Automation

  Software Product](/t5/c-khhcw49343/SAP%2BIntelligent%2BRobotic%2BProcess%2BAutomation/pd-p/73554900100800002142)
* [SAP Build Process Automation

  SAP Build](/t5/c-khhcw49343/SAP%2BBuild%2BProcess%2BAutomation/pd-p/73554900100800003832)

View products (2)

**Intelligent Robotic Process Automation (iRPA)** offers a powerful solution for automating mundane and repetitive tasks, allowing organizations to optimize their processes and improve overall efficiency. One such area where iRPA can be highly beneficial is the automation of mail attachment processing. In this context, **iRPA** can be employed to seamlessly extract, analyse, and act upon attachments received via emails.

**Step 1 :**

**Adding Dependencies**

The characteristics and content of a package can be reused by another project through the structure of a dependency. The Dependencies used here are :

Choose add a Business Process Project Dependency.

**irpa\_core**
**irpa\_excel**
**irpa\_outlook**
**irpa\_pdf**
**irpa\_web**
**irpa\_sapui5**

After Successfully adding dependencies,

![](/legacyfs/online/storage/blog_attachments/2023/08/MicrosoftTeams-image-2-1.png)

*Image 1*

**Step 2 :**

**Saving Attachments using Outlook Activity**

Open the outlook instance activity.

![](/legacyfs/online/storage/blog_attachments/2023/08/MicrosoftTeams-image-3-1.png)

*Image 2*

Utilise the search email activity to locate the specific email you are looking for and save the attachment and choose create custom data and provide folder, folder type and store domain.

![](/legacyfs/online/storage/blog_attachments/2023/08/MicrosoftTeams-image-5-1.png)

*Image 3*

Open the is there no context action in an forever loop to verify whether the email contains the correct subject and document to be stored.

![](/legacyfs/online/storage/blog_attachments/2023/08/MicrosoftTeams-image-7-2.png)

*Image 4*

Use the Get Mail subject(Outlook) option under Default section to get the mail's Subject.

Use Get Mail Body(Outlook) activity to access the mail's body, including any data and stored documents.

Use the Save All Mail Attachment activity to store every attachment, including any word, pdf, or other files that is contained in the email.

Get the context of the following email using the Get Next Email Context activity.

Exit the Forever Loop and close the outlook instance using Close Outlook Instance activity.

![](/legacyfs/online/storage/blog_attachments/2023/08/Screenshot-2023-07-31-at-12.15.41-AM.png)

*Image 5*

**Step 3 :**

**Retrieve Data from the Downloaded PDF Attachment**

Using the get file collection activity, find the location of the downloaded file.

![](/legacyfs/online/storage/blog_attachments/2023/08/MicrosoftTeams-image-13-1.png)

*Image 6*

Open the PDF using the open PDF activity, and then use the get text, get text after, Get total pages and get text before activities to obtain the data from the PDF.

![](/legacyfs/online/storage/blog_attachments/2023/08/MicrosoftTeams-image-9-1.png)

*Image 7*

Use log message to print the information that was obtained from the extracted PDF on the console.

![](/legacyfs/online/storage/blog_attachments/2023/08/MicrosoftTeams-image-10-1.png)

*Image 8*

close and release the pdf Using the close and release PDF activity.

![](/legacyfs/online/storage/blog_attachments/2023/08/MicrosoftTeams-image-12-1.png)

*Image 9*

Here you can find some learning content:

[https://learning.sap.com/learning-journey/create-processes-and-automations-with-sap-build-process-au...](https://learning.sap.com/learning-journey/create-processes-and-automations-with-sap-build-process-automation)

This short blog can help you to understand basic knowledge about How to Use iRPA to Automate the Processing of Mail Attachments.

Since i am also new to writing blogs, Expert suggestions & feedbacks are much appreciated.

If you like this blog post you can follow me for more blogs i will try to make in coming future specifically related to SAP BTP Technologies.

Thank you,
Mekapothu Siva Nagireddy.

1 Comment

You must be a registered user to add a comment. If you've already registered, sign in. Otherwise, register and sign in.

* [Comment](/plugins/common/feature/oidcss/sso_login_redirect/providerid/sap_ids_prompt?redirectreason=permissiondenied&referer=https%3A%2F%2Fcommunity.sap.com%2Ft5%2Ftechnology-blog-posts-by-members%2Fhow-to-use-irpa-to-automate-the-processing-of-mail-attachments%2Fba-p%2F13574862%23comment-on-this)

Copy Link
![](https://community.sap.com/html/@EE5D5986E9F4E5657DCEACB7532B5C39/assets/bluesky-dark.svg)Bluesky
Linkedin

Related Content

* [Build process automation : Error adding MDG approval and visualization from trial account](/t5/technology-q-a/build-process-automation-error-adding-mdg-approval-and-visualization-from/qaq-p/14234371)
  in [Technology Q&A](/t5/technology-q-a/qa-p/technology-questions)  yesterday
* [SAP S4HANA Plant Maintenance for dummies](/t5/technology-blog-posts-by-members/sap-s4hana-plant-maintenance-for-dummies/ba-p/14234304)
  in [Technology Blog Posts by Members](/t5/technology-blog-posts-by-members/bg-p/technology-blog-members)  yesterday
* [SAP GUI Automation within SAP BPA Workflow Process](/t5/technology-q-a/sap-gui-automation-within-sap-bpa-workflow-process/qaq-p/14234302)
  in [Technology Q&A](/t5/technology-q-a/qa-p/technology-questions)  yesterday
* [Subscription to SAP Build process automation is consistantly failing in BTP trial account](/t5/technology-q-a/subscription-to-sap-build-process-automation-is-consistantly-failing-in-btp/qaq-p/14231598)
  in [Technology Q&A](/t5/technology-q-a/qa-p/technology-questions)  Tuesday
* [Basic ...