---
title: Connecting On Premise Mail Destination Using SAP Cloud SDK JavaScript Version 3 on SAP CAP
url: https://blogs.sap.com/2023/02/14/connecting-on-premise-mail-destination-using-sap-cloud-sdk-javascript-version-3-on-sap-cap/
source: SAP Blogs
date: 2023-02-15
fetch_date: 2025-10-04T06:37:10.108818
---

# Connecting On Premise Mail Destination Using SAP Cloud SDK JavaScript Version 3 on SAP CAP

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Technology](/t5/technology/ct-p/technology)
* [Technology Blog Posts by Members](/t5/technology-blog-posts-by-members/bg-p/technology-blog-members)
* Connecting On Premise Mail Destination and Sending...

Technology Blog Posts by Members

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/technology-blog-members/article-id/161994&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [Connecting On Premise Mail Destination and Sending Email Using SAP Cloud SDK JavaScript Version 3 on SAP CAP](/t5/technology-blog-posts-by-members/connecting-on-premise-mail-destination-and-sending-email-using-sap-cloud/ba-p/13560956)

![codebrokerad](https://avatars.profile.sap.com/d/7/idd70ade26fcafaa38338b15b141073a763811e3486b6b6adbbb1d4c0873628ee3_small.jpeg "codebrokerad")

[codebrokerad](https://community.sap.com/t5/user/viewprofilepage/user-id/121863)

Participant

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=technology-blog-members&message.id=161994)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/technology-blog-members/article-id/161994)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13560956)

‎2023 Feb 14
11:01 PM

[9
Kudos](/t5/kudos/messagepage/board-id/technology-blog-members/message-id/161994/tab/all-users "Click here to see who gave kudos to this post.")

9,860

* SAP Managed Tags
* [SAP Cloud Application Programming Model](https://community.sap.com/t5/c-khhcw49343/SAP%2520Cloud%2520Application%2520Programming%2520Model/pd-p/9f13aee1-834c-4105-8e43-ee442775e5ce)
* [SAP Cloud SDK](https://community.sap.com/t5/c-khhcw49343/SAP%2520Cloud%2520SDK/pd-p/73555000100800000895)
* [SAP Connectivity service](https://community.sap.com/t5/c-khhcw49343/SAP%2520Connectivity%2520service/pd-p/67837800100800004901)
* [SAP Business Technology Platform](https://community.sap.com/t5/c-khhcw49343/SAP%2520Business%2520Technology%2520Platform/pd-p/73555000100700000172)

* [SAP Connectivity service

  SAP Business Technology Platform](/t5/c-khhcw49343/SAP%2BConnectivity%2Bservice/pd-p/67837800100800004901)
* [SAP Cloud SDK

  SAP Cloud SDK](/t5/c-khhcw49343/SAP%2BCloud%2BSDK/pd-p/73555000100800000895)
* [SAP Cloud Application Programming Model

  Software Product Function](/t5/c-khhcw49343/SAP%2BCloud%2BApplication%2BProgramming%2BModel/pd-p/9f13aee1-834c-4105-8e43-ee442775e5ce)
* [SAP Business Technology Platform

  Software Product](/t5/c-khhcw49343/SAP%2BBusiness%2BTechnology%2BPlatform/pd-p/73555000100700000172)

View products (4)

Hello SAP Community.

This blog post will provide a solution for many faced when developing their business application.
> ***How to connect On-premise SAP BTP destination through a NodeJS application to send email using Cloud Application Programming CAP?***

Solutions to these problem were successful for scenarios by joachim.vanpraet either creating our [own destination in BTP using SMTP providers like Mailtrap](https://blogs.sap.com/2019/11/28/send-an-email-from-a-nodejs-application/), which was not suitable for our use case because it is not on-premise solution.

Other solution provided by miroll is tackling the scenario through [BTP Cloud Foundry](https://blogs.sap.com/2021/05/07/connect-to-an-on-premise-mail-server-from-sap-btp-cloud-foundry/) using Java successfuly, but our tech stack was Javascript / NodeJS.

To find a solution, I have checked out the announcement from marika.marszalkowski and this section of [the post](http://SAP Cloud SDK for JavaScript Version 3) about newest updates fascinated me.

> ### Sending Emails
>
>
>
> We recently released experimental functionality to send e-mails against SAP BTP destinations of type “MAIL”.
> In version 3 we will make it available for productive use.
> You can find more details in the [mail documentation](https://sap.github.io/cloud-sdk/docs/js/features/mail-client).

After I read the documentation and understand it, I have created a new project to test this feature. And with a simple configuration, you can now connect your on premise mail servers successfully thanks to the wonderful developers of SAP Cloud SDK Team.

**Let's move step by step to show how to perform it in a simple CAP application from scratch.**

## 1.Requirements - BTP Services Necessary In Setup Account

These are free services on BTP, so it means everyone can test what we perform with a Trial account:

* **Authorization and Trust Management Service**

* **Destination Service**

* **Connectivity Service**

IDE to make our app work is running in **SAP Business Application Studio.**

We also need to generate **service instance keys** for each of those services to test our application. Check image below how to create service instance key aft

I have generated those services and service keys with a naming convention as follows. First parameter is service instance name, second parameter is service instance key. I have created those in BTP as you can see Authorization and Trust Management service below, and complete the rest.

> mail-xsuaa , mail-xsuaa-key
>
>
>
> mail-destination , mail-destination-key
>
>
>
> mail-connectivity, mail-connectivity-key

![](/legacyfs/online/storage/blog_attachments/2023/02/ss7-1.png)

Figure 1 : [Setting up BTP Service Instance and Service Key in BTP Cockpit - Click to Enlarge](https://blogs.sap.com/wp-content/uploads/2023/02/ss7-1.png)

Destination configuration is very important to handle, in this example we are using SMTP server for Gmail and its configuration is as below in our BTP Destination.

With the 'New Property' Tab, you can add more properties or delete the extra ones that are not necessary for your configuration.The destination you are calling should be type 'MAIL' and must be [configured](https://help.sap.com/docs/CP_CONNECTIVITY/cca91383641e40ffbe03bdc78f00f681/6442cb4f8b0f41178abce14c35f5def4.html?locale=en-US) correctly.

Here is an example for you:

![](/legacyfs/online/storage/blog_attachments/2023/02/ss5.png)

Figure 2 : [SMTP Destination Configuration in BTP Subaccount - Click to Enlarge](https://blogs.sap.com/wp-content/uploads/2023/02/ss5.png)

Additional properties we set up in the image that are not clearly visible is as below for this usecase is as below. Please note the configuration may change for different SMTP Server Providers:

```
mail.smtp.from=<enter e-mail address to send email from here>

mail.smtp.ssl.checkserveridentity=true

mail.smtp.starttls.enable=true

mail.smtp.starttls.required=true

mail.transport.protocol=smtp9

tokenServiceURLType=Dedicated (optional field)
```

##

## 2. Create a New Project

Open Business Application Studio. Click the top left pane red highlighted>File>New Project From Template.

![](/legacyfs/online/storage/blog_attachments/2023/02/Inkedss1.jpg)

Figure 3 : [Initial Project Setup in SAP Business Application Studio - Click to Enlarge](https://blogs.sap.com/wp-content/uploads/2023/02/Inkedss1.jpg)

Then choose CAP Project and click Start.

![](/legacyfs/online/storage/blog_attachments/2023/02/ss2.png)

Figure 4 : [Choosing CAP Project will Provide Necessary Development Runtime](https://blogs.sap.com/wp-content/uploads/2023/02/ss2.png)

Set your project configuration as below image and click Finish.

![](/legacyfs/online/storage/blog_attachments/2023/02/ss3.png)

Figure 5 :[Minimal Features Addition to Run Pr...