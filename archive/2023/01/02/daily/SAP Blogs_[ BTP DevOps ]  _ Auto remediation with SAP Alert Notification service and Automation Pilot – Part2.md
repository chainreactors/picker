---
title: [ BTP DevOps ]  : Auto remediation with SAP Alert Notification service and Automation Pilot – Part2
url: https://blogs.sap.com/2023/01/01/btp-devops-auto-remediation-with-sap-alert-notification-service-and-automation-pilot-part2/
source: SAP Blogs
date: 2023-01-02
fetch_date: 2025-10-04T02:52:05.160921
---

# [ BTP DevOps ]  : Auto remediation with SAP Alert Notification service and Automation Pilot – Part2

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Technology](/t5/technology/ct-p/technology)
* [Technology Blog Posts by SAP](/t5/technology-blog-posts-by-sap/bg-p/technology-blog-sap)
* [ BTP DevOps ] : Auto remediation with SAP Alert ...

Technology Blog Posts by SAP

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/technology-blog-sap/article-id/161551&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [[ BTP DevOps ] : Auto remediation with SAP Alert Notification service and Automation Pilot - Part2](/t5/technology-blog-posts-by-sap/btp-devops-auto-remediation-with-sap-alert-notification-service-and/ba-p/13561110)

![showkath_naseem](https://avatars.profile.sap.com/b/3/idb31430339dce394fae56e5099a002a181ef4cf21068545b19463517d3280ac9b_small.jpeg "showkath_naseem")

![Product and Topic Expert](/html/@138D6F765B60D7FC0168643DE27D8A68/rank_icons/sap-logo-small-14px.png "Product and Topic Expert")
[showkath\_naseem](https://community.sap.com/t5/user/viewprofilepage/user-id/1529)

Product and Topic Expert

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=technology-blog-sap&message.id=161551)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/technology-blog-sap/article-id/161551)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13561110)

‎2023 Jan 01
6:11 PM

[9
Kudos](/t5/kudos/messagepage/board-id/technology-blog-sap/message-id/161551/tab/all-users "Click here to see who gave kudos to this post.")

1,928

* SAP Managed Tags
* [SAP Alert Notification service for SAP BTP](https://community.sap.com/t5/c-khhcw49343/SAP%2520Alert%2520Notification%2520service%2520for%2520SAP%2520BTP/pd-p/73555000100800001401)
* [SAP Automation Pilot](https://community.sap.com/t5/c-khhcw49343/SAP%2520Automation%2520Pilot/pd-p/73554900100800002433)
* [SAP BTP, Cloud Foundry runtime and environment](https://community.sap.com/t5/c-khhcw49343/SAP%2520BTP%252C%2520Cloud%2520Foundry%2520runtime%2520and%2520environment/pd-p/73555000100800000287)

* [SAP BTP, Cloud Foundry runtime and environment

  SAP Business Technology Platform](/t5/c-khhcw49343/SAP%2BBTP%25252C%2BCloud%2BFoundry%2Bruntime%2Band%2Benvironment/pd-p/73555000100800000287)
* [SAP Alert Notification service for SAP BTP

  SAP Business Technology Platform](/t5/c-khhcw49343/SAP%2BAlert%2BNotification%2Bservice%2Bfor%2BSAP%2BBTP/pd-p/73555000100800001401)
* [SAP Automation Pilot

  SAP Business Technology Platform](/t5/c-khhcw49343/SAP%2BAutomation%2BPilot/pd-p/73554900100800002433)

View products (3)

### New Year , New Blog Post  ![:party_popper:](/html/@40A2E70E9EEFCF8DC7E4089129B7C173/emoticons/1f389.png ":party_popper:")

𝐿𝑒𝓉’𝓈 𝓌𝑒𝓁𝒸𝑜𝓂𝑒 𝓉𝒽𝒾𝓈 n𝑒𝓌 c𝒶𝓁𝑒𝓃𝒹𝒶𝓇 y𝑒𝒶𝓇 𝟤𝟢𝟤𝟥 w𝒾𝓉𝒽 𝑔𝓇𝑒𝒶𝓉 𝑒𝓃𝓉𝒽𝓊𝓈𝒾𝒶𝓈𝓂 and 𝓃𝑒𝓌 𝑒𝓃𝑒𝓇𝑔𝒾𝑒𝓈, accompanied by𝓉𝒽𝑒𝓌𝒶𝓇𝓂𝑒𝓈𝓉 𝒶𝓈𝓅𝒾𝓇𝒶𝓉𝒾𝑜𝓃𝓈. 𝑀𝒶𝓎 𝓉𝒽𝒾𝓈 𝓎𝑒𝒶𝓇 𝒷𝓇𝒾𝓃𝑔 𝓃𝑒𝓌 𝒽𝒶𝓅𝓅𝒾𝓃𝑒𝓈𝓈, 𝓃𝑒𝓌 𝑔𝑜𝒶𝓁𝓈, 𝓃𝑒𝓌 𝒶𝒸𝒽𝒾𝑒𝓋𝑒𝓂𝑒𝓃𝓉𝓈, 𝓁𝑜𝓉𝓈 𝑜𝒻 𝑒𝓍𝒸𝒾𝓉𝒾𝓃𝑔 𝑜𝓅𝓅𝑜𝓇𝓉𝓊𝓃𝒾𝓉𝒾𝑒𝓈 𝒶𝓃𝒹 𝓂𝒶𝓃𝓎 𝓃𝑒𝓌 𝒾𝓃𝓈𝓅𝒾𝓇𝒶𝓉𝒾𝑜𝓃𝓈 𝓉𝑜 𝓎𝑜𝓊𝓇 𝓁𝒾𝒻𝑒. Let’s all 𝑒𝓍𝓅𝑒𝓇𝒾𝑒𝓃𝒸𝑒 𝓃𝑒𝓌 𝓉𝒽𝒾𝓃𝑔𝓈 𝒶𝓃𝒹 𝓁𝑒𝒶𝓇𝓃 𝓃𝑒𝓌 𝓉𝒽𝒾𝓃𝑔𝓈in 𝓉𝒽𝒾𝓈 𝓃𝑒𝓌 𝓎𝑒𝒶𝓇 ![:chocolate_bar:](/html/@430D05534B35A4F4451B9C8DFE17BE92/emoticons/1f36b.png ":chocolate_bar:") ![:candy:](/html/@E86FE371A5FDDA22BE9C15385EC0DE5E/emoticons/1f36c.png ":candy:")![:soft_ice_cream:](/html/@21A19FAA023C4EEFBD1498717B16A7E6/emoticons/1f366.png ":soft_ice_cream:")

This blog post is part of [a series of blog posts](https://blogs.sap.com/2019/06/05/sap-cloud-platform-alert-notification-is-now-generally-available/)related to SAP BTP  Alert Notification service.
In [Part 1](https://blogs.sap.com/2022/01/19/detect-application-crashes-in-sap-btp-cloud-foundry-with-sap-alert-notification-service-part-1/) Use case was " how to catch application crashes in SAP BTP by utilizing Alert Notification" . The idea of **Part 2** is  to “React Proactively & automatically remediate application instance crashes by using out-of-the-box [integration](https://help.sap.com/docs/AUTOMATION_PILOT/de3900c419f5492a8802274c17e07049/2a9e5dc555154371a534ea2a7987c977.html) of a state-of-the-art DevOps tools, such as [SAP Automation Pilot](https://help.sap.com/docs/AUTOMATION_PILOT/de3900c419f5492a8802274c17e07049/4536e41c57aa442095ccbac977965f26.html) ,  [SAP BTP Alert Notification](https://help.sap.com/docs/ALERT_NOTIFICATION/5967a369d4b74f7a9c2b91f5df8e6ab6/086361cb02fb467993acd6f9515607d4.html?locale=en-US&state=DRAFT)

*Document  Reference*  : **[SAP Automation Pilot Integrate with SAP Alert Notification Service for SAP BTP](https://help.sap.com/docs/AUTOMATION_PILOT/de3900c419f5492a8802274c17e07049/2a9e5dc555154371a534ea2a7987c977.html)**

As you know , the primary goal of [SAP Automation Pilot](https://help.sap.com/docs/AUTOMATION_PILOT/de3900c419f5492a8802274c17e07049/4536e41c57aa442095ccbac977965f26.html?locale=en-US) is to **simplify and automate complex manual processes** , **automate** multiple **DevOps tasks** in order to minimize the cloud operational effort behind any cloud solution in the SAP Business Technology Platform

# Use-case 1 : Simple Scenario

In this blog post , we would like to illustrate Auto remediation With simple use case

"Auto Start Application instance when Application Crashed/Stopped"

![](/legacyfs/online/storage/blog_attachments/2023/01/Usecase-BlogPost.png)

# **Configurations in** **SAP Automation Pilot**

**Step1 ) Create Service Account** with **Execute** privileges.This Technical Service Account you will use in Alert Notification service. As of now Service Account Supports two types of Authentication

1. [Basic Authentication](https://help.sap.com/docs/AUTOMATION_PILOT/de3900c419f5492a8802274c17e07049/acf58b69e1484f8595e6b398687b08b3.html?locale=en-US#basic-authentication)

2. [SAP Cloud PKI Client Certificate](https://help.sap.com/docs/AUTOMATION_PILOT/de3900c419f5492a8802274c17e07049/acf58b69e1484f8595e6b398687b08b3.html?locale=en-US#basic-authentication)

**Reference** : [Service Account in SAP Automation Pilot](https://help.sap.com/docs/AUTOMATION_PILOT/de3900c419f5492a8802274c17e07049/acf58b69e1484f8595e6b398687b08b3.html?locale=en-US)

**Step2 )** **Build Trigger URL**

1. Go to the **Executions** section in the Automation Pilot’s UI and choose the **Build Event Trigger**

2. Choose **Alert****Notifications** a trigger type.

3. Select your desired [command](https://help.sap.com/docs/AUTOMATION_PILOT/de3900c419f5492a8802274c17e07049/5bbe7dba99d24caeafddf7fa62dc63b9.html) by specifying the catalog, command and version fields.

* For Restarting and re-staging applications: You have below commands

  ```
  RestartCfApp, RestageCfApp, StartCfApp, StopCfApp

  TriggerStartCfApp,TriggerStopCfApp​
  ```

  4. After all fields are set in the desired way, you can scroll back to the top and copy the automatically generated URL (To any notepad).

  ![](/legacyfs/online/storage/blog_attachments/2023/01/2-BuildEvent-Trigger-URL-2-Old-CopyURL.png)

# **Configurations in Alert Notification**

Let’s start by creating a SAP Automation Pilot action for the Alert Notification.

1. Navigate to Alert Notification’s service instance UI in your Cloud Cockpit, tab **Actions**, click the **Create.**

2. Choose SAP Automation Pilot action type.

![](/legacyfs/online/storage/blog_attachments/2023/01/6-Alert-SubScription-Actions-Select-Automation-1.png)

         3. In the displayed form, enter the name of the target table in Automation Pilot.

![](/legacyfs/online/storage/blog_attachments/2023/01/6...