---
title: Triggering a CPI process from SuccessFactors Intelligent Services
url: https://blogs.sap.com/2022/11/22/triggering-a-cpi-process-from-successfactors-intelligent-services/
source: SAP Blogs
date: 2022-11-23
fetch_date: 2025-10-03T23:29:23.067024
---

# Triggering a CPI process from SuccessFactors Intelligent Services

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Human Capital Management](/t5/human-capital-management/ct-p/hcm)
* [HCM Blog Posts by Members](/t5/human-capital-management-blog-posts-by-members/bg-p/hcm-blog-members)
* Triggering a CPI process from SuccessFactors Intel...

Human Capital Management Blog Posts by Members

Explore blogs from customers or SAP partners to gain best practices and fresh insights to succeed.

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/hcm-blog-members/article-id/4887&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [Triggering a CPI process from SuccessFactors Intelligent Services](/t5/human-capital-management-blog-posts-by-members/triggering-a-cpi-process-from-successfactors-intelligent-services/ba-p/13553402)

![NabarunKundu](https://avatars.profile.sap.com/b/1/idb195c02248e557089f9aa88080c8796a932c65df06526409ad119f29b8f2f242_small.jpeg "NabarunKundu")

[NabarunKundu](https://community.sap.com/t5/user/viewprofilepage/user-id/40735)

Explorer

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=hcm-blog-members&message.id=4887)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/hcm-blog-members/article-id/4887)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13553402)

‎2022 Nov 22
7:53 PM

[7
Kudos](/t5/kudos/messagepage/board-id/hcm-blog-members/message-id/4887/tab/all-users "Click here to see who gave kudos to this post.")

6,888

* SAP Managed Tags
* [SAP SuccessFactors Platform](https://community.sap.com/t5/c-khhcw49343/SAP%2520SuccessFactors%2520Platform/pd-p/73555000100800000775)
* [Cloud Integration](https://community.sap.com/t5/c-khhcw49343/Cloud%2520Integration/pd-p/67837800100800006801)

* [Cloud Integration

  SAP Integration Suite](/t5/c-khhcw49343/Cloud%2BIntegration/pd-p/67837800100800006801)
* [SAP SuccessFactors Platform

  SAP SuccessFactors HCM](/t5/c-khhcw49343/SAP%2BSuccessFactors%2BPlatform/pd-p/73555000100800000775)

View products (2)

**Background:** In Intelligent Service Center (ISC) we have a dedicated option to connect an Integration Center process from the events. But if we want to connect CPI processes from the Intelligent Service Center we don't have a straight forward option. In this blog I would like to explain how can we connect a CPI process based on the ISC events.

I am using the ISC event 'Change in Manager' to explain this scenario.

Now, if we click on this specific event from ISC this will take us to the detailed screen below. In this screen we have an option called 'Event Connector' and that can be used to connect CPI Process.

![](/legacyfs/online/storage/blog_attachments/2022/11/Event-Connector-1.jpg)

Event Connector in ISC Event

This will bring us to the next screen where we can enter the CPI process details using the 'New Event Connector' option. We need to enter a Name, the endpoint url of the CPI process and the authentication details. I have used the 'Basic Authentication' here. Please find the screen shot below for your reference.

![](/legacyfs/online/storage/blog_attachments/2022/11/Event-Connector-for-CPI-Process.png)

New Event Connector to maintain for a CPI process

Now the CPI process which we want to connect from ISC, should be a SOAP based process. You can use the WSDL provided by SAP in the Intelligence Service Center document to build this CPI process. You can find the sample WSDL in the [SAP Intelligent Service Center Document](https://help.sap.com/doc/e3eafa2654d84564a039e8bcb6218ea0/2205/en-US/SF_IS_SettingUp_Impl.pdf).

Once you deploy this process in CPI you should find the endpoint url in the CPI overview screen. That needs to be entered as the endpoint earlier stated above in the event connector.

As the setup is now completed you should be able to trigger the CPI process now from the event. We have changed the manager for an employee so the ISC event got triggered. This can be checked further from the event monitoring in ISC.

To check the next step if the CPI process is triggered, we need to check the transaction called 'Event Notification Audit Log' in SuccessFactors.

![](/legacyfs/online/storage/blog_attachments/2022/11/Event-Notification-1.png)

You should also look further and check your CPI process got triggered.

![](/legacyfs/online/storage/blog_attachments/2022/11/CPI-Process.png)

Check CPI Process

The inbound message should be as below. You can make further API call based on this message.

![](/legacyfs/online/storage/blog_attachments/2022/11/ISC-Payload.png)

Request Message from ISC

So, in this way we can intimate CPI with a change in manager scenario from SuccessFactors.

Here we have achieved the trigger from SF to CPI using Basic Authentication. But if you want to do this using Oauth please check the below blog.

[https://blogs.sap.com/2023/03/19/how-to-trigger-a-cpi-process-from-successfactors-intelligent-servic...](https://blogs.sap.com/2023/03/19/how-to-trigger-a-cpi-process-from-successfactors-intelligent-services-center-using-oauth2-client-credentials-grant/)

* [Cloud](/t5/tag/Cloud/tg-p/board-id/hcm-blog-members)
* [CPI Trigger](/t5/tag/CPI%20Trigger/tg-p/board-id/hcm-blog-members)
* [Event Notification Subscribers](/t5/tag/Event%20Notification%20Subscribers/tg-p/board-id/hcm-blog-members)
* [Intelligent Service Center](/t5/tag/Intelligent%20Service%20Center/tg-p/board-id/hcm-blog-members)

6 Comments

You must be a registered user to add a comment. If you've already registered, sign in. Otherwise, register and sign in.

* [Comment](/plugins/common/feature/oidcss/sso_login_redirect/providerid/sap_ids_prompt?redirectreason=permissiondenied&referer=https%3A%2F%2Fcommunity.sap.com%2Ft5%2Fhuman-capital-management-blog-posts-by-members%2Ftriggering-a-cpi-process-from-successfactors-intelligent-services%2Fba-p%2F13553402%23comment-on-this)

Copy Link
![](https://community.sap.com/html/@EE5D5986E9F4E5657DCEACB7532B5C39/assets/bluesky-dark.svg)Bluesky
Linkedin

Related Content

* [Difficulty Triggering Workflow in SuccessFactors When Data Is Auto-Posted from BTP](/t5/human-capital-management-q-a/difficulty-triggering-workflow-in-successfactors-when-data-is-auto-posted/qaq-p/14233952)
  in [Human Capital Management Q&A](/t5/human-capital-management-q-a/qa-p/hcm-questions)  10 hours ago
* [Enterprise Service Management in Action: AI-Driven Service Experiences at SAP Connect 2025](/t5/human-capital-management-blog-posts-by-sap/enterprise-service-management-in-action-ai-driven-service-experiences-at/ba-p/14229862)
  in [Human Capital Management Blog Posts by SAP](/t5/human-capital-management-blog-posts-by-sap/bg-p/hcm-blog-sap)  Monday
* [Seeing Skills Before They Matter: People Intelligence in SAP SuccessFactors](/t5/human-capital-management-blog-posts-by-members/seeing-skills-before-they-matter-people-intelligence-in-sap-successfactors/ba-p/14226130)
  in [Human Capital Management Blog Posts by Members](/t5/human-capital-management-blog-posts-by-members/bg-p/hcm-blog-members)  a week ago
* [EU Pay Transparency in SAP SuccessFactors — A Suite-Level Compliance Playbook](/t5/human-capital-management-blog-posts-by-members/eu-pay-transparency-in-sap-successfactors-a-suite-level-compliance-playbook/ba-p/14223230)
  in [Human Capital Management Blog Posts by Members](/t5/human-capital-management-blog-posts-by-members/bg-p/hcm-blog-members)  2 weeks ago
* [Hire and...