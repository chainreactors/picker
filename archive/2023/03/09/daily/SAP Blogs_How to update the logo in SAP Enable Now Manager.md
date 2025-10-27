---
title: How to update the logo in SAP Enable Now Manager
url: https://blogs.sap.com/2023/03/08/how-to-update-the-logo-in-sap-enable-now-manager/
source: SAP Blogs
date: 2023-03-09
fetch_date: 2025-10-04T09:01:26.126000
---

# How to update the logo in SAP Enable Now Manager

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Human Capital Management](/t5/human-capital-management/ct-p/hcm)
* [HCM Blog Posts by SAP](/t5/human-capital-management-blog-posts-by-sap/bg-p/hcm-blog-sap)
* How to update the logo in SAP Enable Now Manager

Human Capital Management Blog Posts by SAP

Learn directly from SAP experts through blogs that deliver practical guidance and opportunities to deepen your expertise.

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/hcm-blog-sap/article-id/6260&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [How to update the logo in SAP Enable Now Manager](/t5/human-capital-management-blog-posts-by-sap/how-to-update-the-logo-in-sap-enable-now-manager/ba-p/13566368)

![robert_way](https://avatars.profile.sap.com/f/0/idf034f623e59d20e1ad452a622e34fcf595bfcea46108701ff4fc73c588348be5_small.jpeg "robert_way")

![Product and Topic Expert](/html/@138D6F765B60D7FC0168643DE27D8A68/rank_icons/sap-logo-small-14px.png "Product and Topic Expert")
[robert\_way](https://community.sap.com/t5/user/viewprofilepage/user-id/817432)

Product and Topic Expert

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=hcm-blog-sap&message.id=6260)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/hcm-blog-sap/article-id/6260)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13566368)

‎2023 Mar 08
9:32 PM

[7
Kudos](/t5/kudos/messagepage/board-id/hcm-blog-sap/message-id/6260/tab/all-users "Click here to see who gave kudos to this post.")

1,919

* SAP Managed Tags
* [SAP Enable Now](https://community.sap.com/t5/c-khhcw49343/SAP%2520Enable%2520Now/pd-p/73554900100700001245)
* [SAP Enable Now, author option](https://community.sap.com/t5/c-khhcw49343/SAP%2520Enable%2520Now%252C%2520author%2520option/pd-p/73555000100800000429)
* [SAP Enable Now, cloud edition](https://community.sap.com/t5/c-khhcw49343/SAP%2520Enable%2520Now%252C%2520cloud%2520edition/pd-p/73554900100800000101)
* [Training](https://community.sap.com/t5/c-khhcw49343/Training/pd-p/676305042803066886656318788802663)

* [SAP Enable Now

  Software Product](/t5/c-khhcw49343/SAP%2BEnable%2BNow/pd-p/73554900100700001245)
* [SAP Enable Now, author option

  SAP Enable Now](/t5/c-khhcw49343/SAP%2BEnable%2BNow%25252C%2Bauthor%2Boption/pd-p/73555000100800000429)
* [SAP Enable Now, cloud edition

  SAP Enable Now](/t5/c-khhcw49343/SAP%2BEnable%2BNow%25252C%2Bcloud%2Bedition/pd-p/73554900100800000101)
* [Training

  Topic](/t5/c-khhcw49343/Training/pd-p/676305042803066886656318788802663)

View products (4)

## How do you update the logo in SAP Enable Now Manager?

I decided to write this blog today after someone asked me this same question and I didn't quite remember how to do it.  Lucky for us we have a vibrant Enable Now Community and I was able to find the answer through others' contributions in the Enable Now Community [Questions](https://community.sap.com/topics/enable-now?lng=en&tab=content).

This blog post is a way for me to aggregate the information I found while researching this and to document it in one place for future reference, along with some additional information from having just gone through this process.

This blog post was made possible by the answers provided to other people's very same question by the following Enable Now superstars: kristina.tanz, shanealipke and dirkmanuel2.  The original answers to the Community questions can be found [HERE](https://answers.sap.com/questions/13614708/changing-logo-of-the-manager.html) and [HERE](https://answers.sap.com/questions/13401466/logo-into-manager.html).

### Updating the logo

The logo that is displayed in Enable Now Manager lives in a special Workarea called "System".  This Workarea is created by default and is part of every instance of Enable Now cloud.  The System Workarea has Adaptable Resources, which include an object called "ui", and which is where the logo is located.

![](/legacyfs/online/storage/blog_attachments/2023/03/System_Workarea.jpg)

System Workarea

The first step, however, has to take place in another Workarea.  The overall process will consist of creating a new Manager Style in a different Workarea and then importing it into the System Workarea. The detailed steps are outlined below:

1. Open SEN Producer for a Workarea other than System.

2. Navigate to **Tools > Customization > Edit Style Resources**.

3. The Manager Style resource is not available 'out of the box' for Enable Now, so you will have to create a brand new Manager Style (use the **New..** button) in the **Edit Style Resources** area.  The new Manager Style **must be named "UI"**, which defaulted automatically for me.  This Manager Style will contain your new logo.

4. After creating the new Manager Style, it will appear in **Resources > Adaptable Resources**.  Update the SAP logo with your company's logo.  As Dirk mentions in his original answer, the image sizes for the logo are 600x96 for hi-res (recommended) or 300x48 original (default) size.  Anything larger than that will skew your Manager display.

5. Export the "UI" Manager Style as a .dkp file.

6. Open Manager and navigate to the System Workarea.  Open Producer for the System Workarea.

7. In Producer, start Editing the existing **Resources > Adaptable Resources > UI** object.

8. Import the new Manager Style (called "UI" from step 3) into the System Workarea.

9. Finish Editing the new ui object and Publish it.

10. Restart Manager

Here is a link to the SAP Enable Now [Customization Guide](https://help.sap.com/doc/db7bf2a163974c388b51317f58dc9cfb/2105/en-US/SAP_Enable_Now_Customization_en-US.pdf).  I hope this information is helpful - let me know in the comments if this was useful or if you have any additional tips and tricks to share!

Best,

* Robert

Labels

* [Technology Updates](/t5/human-capital-management-blog-posts-by-sap/bg-p/hcm-blog-sap/label-name/technology%20updates)

* [RobtWay](/t5/tag/RobtWay/tg-p/board-id/hcm-blog-sap)

4 Comments

You must be a registered user to add a comment. If you've already registered, sign in. Otherwise, register and sign in.

* [Comment](/plugins/common/feature/oidcss/sso_login_redirect/providerid/sap_ids_prompt?redirectreason=permissiondenied&referer=https%3A%2F%2Fcommunity.sap.com%2Ft5%2Fhuman-capital-management-blog-posts-by-sap%2Fhow-to-update-the-logo-in-sap-enable-now-manager%2Fba-p%2F13566368%23comment-on-this)

Copy Link
![](https://community.sap.com/html/@EE5D5986E9F4E5657DCEACB7532B5C39/assets/bluesky-dark.svg)Bluesky
Linkedin

Related Content

* [HR Efficiency in Action: Automate and Streamline HR Processes](/t5/human-capital-management-blog-posts-by-sap/hr-efficiency-in-action-automate-and-streamline-hr-processes/ba-p/14233229)
  in [Human Capital Management Blog Posts by SAP](/t5/human-capital-management-blog-posts-by-sap/bg-p/hcm-blog-sap)  Thursday
* [Automating Custom Performance Data Transfer to Employee Profiles](/t5/human-capital-management-blog-posts-by-members/automating-custom-performance-data-transfer-to-employee-profiles/ba-p/14217030)
  in [Human Capital Management Blog Posts by Members](/t5/human-capital-management-blog-posts-by-members/bg-p/hcm-blog-members)  Monday
* [Payroll Canada Year-End 2025](/t5/human-capital-management-blog-posts-by-sap/payroll-canada-year-end-2025/ba-p/14229443)
  in [Human Capital Management Blog Posts by SAP]...