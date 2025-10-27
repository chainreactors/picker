---
title: SAP BusinessObjects WebIntelligence : Send Scheduled Report to users only in case “Scheduled Report Contains Data” else do NOT send  the blank report.
url: https://blogs.sap.com/2023/03/16/sap-businessobjects-webintelligence-send-scheduled-report-to-users-only-in-case-scheduled-report-contains-data-else-do-not-send-the-blank-report./
source: SAP Blogs
date: 2023-03-17
fetch_date: 2025-10-04T09:50:59.848668
---

# SAP BusinessObjects WebIntelligence : Send Scheduled Report to users only in case “Scheduled Report Contains Data” else do NOT send  the blank report.

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Technology](/t5/technology/ct-p/technology)
* [Technology Blog Posts by Members](/t5/technology-blog-posts-by-members/bg-p/technology-blog-members)
* SAP BusinessObjects WebIntelligence : Send Schedul...

Technology Blog Posts by Members

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/technology-blog-members/article-id/160098&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [SAP BusinessObjects WebIntelligence : Send Scheduled Report to users only in case "Scheduled Report Contains Data" else do NOT send the blank report.](/t5/technology-blog-posts-by-members/sap-businessobjects-webintelligence-send-scheduled-report-to-users-only-in/ba-p/13550268)

![Ashish_Farkya](https://avatars.profile.sap.com/8/c/id8c1cc330b829628c70bceffa73dea8424e2226e0284ab1dc6684325d330f94d2_small.jpeg "Ashish_Farkya")

[Ashish\_Farkya](https://community.sap.com/t5/user/viewprofilepage/user-id/585271)

Participant

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=technology-blog-members&message.id=160098)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/technology-blog-members/article-id/160098)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13550268)

‎2023 Mar 16
3:34 PM

[2
Kudos](/t5/kudos/messagepage/board-id/technology-blog-members/message-id/160098/tab/all-users "Click here to see who gave kudos to this post.")

2,443

* SAP Managed Tags
* [SAP BusinessObjects Business Intelligence platform](https://community.sap.com/t5/c-khhcw49343/SAP%2520BusinessObjects%2520Business%2520Intelligence%2520platform/pd-p/01200314690800000337)
* [SAP BusinessObjects - Web Intelligence (WebI)](https://community.sap.com/t5/c-khhcw49343/SAP%2520BusinessObjects%2520-%2520Web%2520Intelligence%2520%28WebI%29/pd-p/907900296036854683333078008146613)

* [SAP BusinessObjects Business Intelligence platform

  SAP BusinessObjects Business Intelligence](/t5/c-khhcw49343/SAP%2BBusinessObjects%2BBusiness%2BIntelligence%2Bplatform/pd-p/01200314690800000337)
* [SAP BusinessObjects - Web Intelligence (WebI)

  Software Product Function](/t5/c-khhcw49343/SAP%2BBusinessObjects%2B-%2BWeb%2BIntelligence%2B%252528WebI%252529/pd-p/907900296036854683333078008146613)

View products (2)

In this blog post, I would like to share a business scenario ( primarily used for "Reconciliation Reports" ) and one of the solution to it.

**Business Scenario :**

For a WebI Report ( may be a Reconciliation report between two systems) which is scheduled to run on daily basis, users would like to -

1. Send a copy of the report to users only if the reconciliation has issues ( i.e. the Recon report has variances identified)

2. However, if there were no variances ( reconciliation was successful) then don't send the report with NO data (blank report) to users.

3. Additionally, In case "Schedule" fails to execute for any technical reasons, notify Business Users about the failure and automatically, SAP BusinessObjects WebI scheduler should try to re-run the schedule ( for 5 times at the interval of 1 minute before it gives up).

Sounds interesting yet complicated??

If you have been using WebI scheduling for quite sometime then I think you would find requirement mentioned in point #1 as simple, may be the requirement in point # 3 a bit new but however still simple, but  the requirement in point #2 is something that makes this business case a complex one.

**Solution :**

Part 1 : Create a WebI Report on two sources -

1. Create a WebI report, with two data providers. Merge the data set on common dimensions. Calculate variance/difference in the WebI report.

2. Set the report /block level filter as show only the records having (variance<>0)

Part 2 : Schedule the Report ( with few settings) -

1. Schedule the report to run daily, Set the options to deliver the report via "email" and with excel attachment of the report.   *-- takes care of requirement in point #1*

2. Use the " **Delivery Rules**" property to set the Schedule Status as "**Warning**" when ***Scheduled Report contains NO data.***

![](/legacyfs/online/storage/blog_attachments/2023/03/WebI-Report-Schedule-Delivery-Rules-1.png)

Schedule - Delivery Rules Options

The trick here is that If the report contains data then the status of the scheduled Report would be set to "**Success**". Due to the success status, the output of the report in excel format via email will be sent to users.

But if, the Scheduled Output of the report doesn't pull any data then the schedule status would be marked as "**Warning**".

The moment SAP BusinessObjects scheduler finds the status as "**Warning**", it doesn't trigger the email with excel attachment -*-- This takes care of the second requirement*

3. Now, the only requirement left to address is - What if the Schedule failed to run due to any system failures/ technical issues?

Let's look at the solution for this as follows :

To notify users that the Report Schedule **failed** to run, we can set "Notification" emails as follows -

![](/legacyfs/online/storage/blog_attachments/2023/03/Email-when-job-failed-to-run.png)

Email Notification when job failed to run

now, lets configure re-try ( 5 times; 1 minute apart) , as follows :

![](/legacyfs/online/storage/blog_attachments/2023/03/Reattempt-Schedule-in-case-of-failure.png)

Re-try Schedule

Hope, you found this blog interesting!

Cheers!

~ Ashish

* [SAP BusinessObjects - Web Intelligence (WebI)](/t5/tag/SAP%20BusinessObjects%20-%20Web%20Intelligence%20%28WebI%29/tg-p/board-id/technology-blog-members)

3 Comments

You must be a registered user to add a comment. If you've already registered, sign in. Otherwise, register and sign in.

* [Comment](/plugins/common/feature/oidcss/sso_login_redirect/providerid/sap_ids_prompt?redirectreason=permissiondenied&referer=https%3A%2F%2Fcommunity.sap.com%2Ft5%2Ftechnology-blog-posts-by-members%2Fsap-businessobjects-webintelligence-send-scheduled-report-to-users-only-in%2Fba-p%2F13550268%23comment-on-this)

Copy Link
![](https://community.sap.com/html/@EE5D5986E9F4E5657DCEACB7532B5C39/assets/bluesky-dark.svg)Bluesky
Linkedin

Related Content

* [how to mitigate "web.xml configuration file disclosure" for SAP crystal BO server BI Platform 4.2 SP](/t5/technology-q-a/how-to-mitigate-quot-web-xml-configuration-file-disclosure-quot-for-sap/qaq-p/14233378)
  in [Technology Q&A](/t5/technology-q-a/qa-p/technology-questions)  Thursday
* [A New Home for SAP Enterprise Support Value Maps on SAP Community](/t5/technology-blog-posts-by-sap/a-new-home-for-sap-enterprise-support-value-maps-on-sap-community/ba-p/14222693)
  in [Technology Blog Posts by SAP](/t5/technology-blog-posts-by-sap/bg-p/technology-blog-sap)  a week ago
* [NDC Converter 2.0: Automating Your Journey from BusinessObjects to Cloud Analytics](/t5/technology-q-a/ndc-converter-2-0-automating-your-journey-from-businessobjects-to-cloud/qaq-p/14226676)
  in [Technology Q&A](/t5/technology-q-a/qa-p/technology-questions)  a week ago
* [SAP Business Intelligence - Statement of Direction Update](/t5/technology-blog-posts-by-members/sap-business-intelligence-statement-of-direction-update/ba-p/14226077)
  in [Technology Blog Posts by Members](/t5/technology-blog-posts-by-members/bg-p/technology-blog-members)  a week ago
* [How to size and support the new Crystal Reports DSL Engine...