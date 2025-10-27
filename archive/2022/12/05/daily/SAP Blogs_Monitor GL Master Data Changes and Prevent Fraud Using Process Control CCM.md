---
title: Monitor GL Master Data Changes and Prevent Fraud Using Process Control CCM
url: https://blogs.sap.com/2022/12/04/monitor-gl-master-data-changes-and-prevent-fraud-using-process-control-ccm/
source: SAP Blogs
date: 2022-12-05
fetch_date: 2025-10-04T00:31:00.586030
---

# Monitor GL Master Data Changes and Prevent Fraud Using Process Control CCM

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Financial Management](/t5/financial-management/ct-p/financial-management)
* [Financial Management Blog Posts by Members](/t5/financial-management-blog-posts-by-members/bg-p/financial-management-blog-members)
* Monitor GL Master Data Changes and Prevent Fraud U...

Financial Management Blog Posts by Members

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/financial-management-blog-members/article-id/5404&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [Monitor GL Master Data Changes and Prevent Fraud Using Process Control CCM](/t5/financial-management-blog-posts-by-members/monitor-gl-master-data-changes-and-prevent-fraud-using-process-control-ccm/ba-p/13565809)

![former_member822053](https://avatars.profile.sap.com/former_member_small.jpeg "former_member822053")

[former\_member822053](https://community.sap.com/t5/user/viewprofilepage/user-id/822053)

Explorer

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=financial-management-blog-members&message.id=5404)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/financial-management-blog-members/article-id/5404)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13565809)

‎2022 Dec 04
2:00 AM

[1
Kudo](/t5/kudos/messagepage/board-id/financial-management-blog-members/message-id/5404/tab/all-users "Click here to see who gave kudos to this post.")

2,229

* SAP Managed Tags
* [SAP Process Control](https://community.sap.com/t5/c-khhcw49343/SAP%2520Process%2520Control/pd-p/01200314690800000209)

* [SAP Process Control

  SAP Process Control](/t5/c-khhcw49343/SAP%2BProcess%2BControl/pd-p/01200314690800000209)

View products (1)

Process Controls as a concept is about providing a centralized controls and compliance management solution. It is designed to assess, document, evaluate, monitor and report the effectiveness of internal controls.

One of the core component of Process Control is Continuous Control Monitoring (CCM). This component monitors the ERP systems based on Business Rule logic and sends exception alerts to the control owners based on the deficieny criteria defined in the Business Rule.

**Note: Process Control does not block any business transaction in the ERP system.**

For more details how to configure Business Rule for configurable scenario, please refer below wiki.

[Business Rule Functionality – Governance, Risk and Compliance – SCN Wiki](https://wiki.scn.sap.com/wiki/display/GRC/Business%2BRule%2BFunctionality)

**Business Scenario**: GL account is a master data entity in SAP and it is the heart of financial statements where accounting data is posted from journals and aggregated from subledgers, such as accounts payable, accounts receivable, cash management, fixed assets, purchasing and projects hence monitoring the GL Master Changes settings like blocked for posting in company code is critical to prevent manipulations in the Financial Statements.

T-code FS00 can be used to maintain GL Account and add or remove the block for posting in company code or chart of accounts.

In below example, we will use configurable data source type and business rule in GRC Process Controls to identify the execptions and send alert to the control owner based on a particular company code deemed as sensitive in the enterprise.

![](/legacyfs/online/storage/blog_attachments/2022/12/FS00.png)

Transaction Code FS00

As we are using configurable sub scenario with analysis type as changes, it is mandatory to ensure table logging is active in the ERP system. The table SKB1stores GL Account Master Data Changes.

Go to T-code SE11 then Technical Settings and ensure Log Changes field is selected as shown in below screenshot

![](/legacyfs/online/storage/blog_attachments/2022/12/SKB1.png)

Log Changes Active

Once above steps are validated, please setup the GRC Process Control Master Data

1. Organization

2. Business Process

3. Sub process

4. Risk

5. Control

6. Assign a control owner in the roles tab of control

7. Create a Data Source

8. Create Business Rule by using the data source created in step 7

9. Assign Business Rule to the Control

10. Go to Scheduling then Automated Monitoring and schedule a job by selecting the control

Create Data Source like shown in the below screenshots

![](/legacyfs/online/storage/blog_attachments/2022/12/DS.png)

Data Source

![](/legacyfs/online/storage/blog_attachments/2022/12/DS1.png)

Data Source

![](/legacyfs/online/storage/blog_attachments/2022/12/DS3png.png)

Data Source data received from ERP system

Now let's see the setup of Business Rule

![](/legacyfs/online/storage/blog_attachments/2022/12/BR.png)

Business Rule

![](/legacyfs/online/storage/blog_attachments/2022/12/BR1-1.png)

Business Rule

![](/legacyfs/online/storage/blog_attachments/2022/12/BR2.png)

Business Rule

![](/legacyfs/online/storage/blog_attachments/2022/12/BR3.png)

Business Rule

![](/legacyfs/online/storage/blog_attachments/2022/12/BR4.png)

Business Rule

![](/legacyfs/online/storage/blog_attachments/2022/12/BR5.png)

Business Rule

![](/legacyfs/online/storage/blog_attachments/2022/12/BR6.png)

Business Rule

Now let's see the control performance of the automated monitoring

![](/legacyfs/online/storage/blog_attachments/2022/12/Control.png)

Control Monitoring

![](/legacyfs/online/storage/blog_attachments/2022/12/Control1.png)

Control Result

![](/legacyfs/online/storage/blog_attachments/2022/12/Control2.png)

Control Result

Finally, lets validate the GL account block for posting changed

![](/legacyfs/online/storage/blog_attachments/2022/12/Compared-with-FS00-result.png)

Compared with FS00 Result

Conclusion: Continuous Control Monitoring can help organizations in enhancing their cybersecurity program. It can reduce the damage before it is too late and management can proactively monitor the critical financial risks and remediate issues.

* [grcpc](/t5/tag/grcpc/tg-p/board-id/financial-management-blog-members)
* [process controls](/t5/tag/process%20controls/tg-p/board-id/financial-management-blog-members)

4 Comments

You must be a registered user to add a comment. If you've already registered, sign in. Otherwise, register and sign in.

* [Comment](/plugins/common/feature/oidcss/sso_login_redirect/providerid/sap_ids_prompt?redirectreason=permissiondenied&referer=https%3A%2F%2Fcommunity.sap.com%2Ft5%2Ffinancial-management-blog-posts-by-members%2Fmonitor-gl-master-data-changes-and-prevent-fraud-using-process-control-ccm%2Fba-p%2F13565809%23comment-on-this)

Copy Link
![](https://community.sap.com/html/@EE5D5986E9F4E5657DCEACB7532B5C39/assets/bluesky-dark.svg)Bluesky
Linkedin

Related Content

* [SAP GRC for SAP HANA - Early Adopter Care Program is Open!](/t5/financial-management-blog-posts-by-sap/sap-grc-for-sap-hana-early-adopter-care-program-is-open/ba-p/14233031)
  in [Financial Management Blog Posts by SAP](/t5/financial-management-blog-posts-by-sap/bg-p/financial-management-blog-sap)  Wednesday
* [Finance Connect: Strategic Transformation, Not Just Applications](/t5/financial-management-blog-posts-by-sap/finance-connect-strategic-transformation-not-just-applications/ba-p/14230913)
  in [Financial Management Blog Posts by SAP](/t5/financial-management-blog-posts-by-sap/bg-p/financial-management-blog-sap)  Monday
* [How to handle the auto. creation of costing views...