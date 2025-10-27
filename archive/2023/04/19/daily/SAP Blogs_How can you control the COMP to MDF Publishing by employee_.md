---
title: How can you control the COMP to MDF Publishing by employee?
url: https://blogs.sap.com/2023/04/18/how-can-you-control-the-comp-to-mdf-publishing-by-employee/
source: SAP Blogs
date: 2023-04-19
fetch_date: 2025-10-04T11:34:16.436558
---

# How can you control the COMP to MDF Publishing by employee?

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Human Capital Management](/t5/human-capital-management/ct-p/hcm)
* [HCM Blog Posts by Members](/t5/human-capital-management-blog-posts-by-members/bg-p/hcm-blog-members)
* How can you control the COMP to MDF Publishing by ...

Human Capital Management Blog Posts by Members

Explore blogs from customers or SAP partners to gain best practices and fresh insights to succeed.

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/hcm-blog-members/article-id/4914&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [How can you control the COMP to MDF Publishing by employee?](/t5/human-capital-management-blog-posts-by-members/how-can-you-control-the-comp-to-mdf-publishing-by-employee/ba-p/13554278)

![NicolasC67](https://avatars.profile.sap.com/6/0/id604a8de1734c857efdde6e6849a5671d5014127b61d28175a7dc00ef11708536_small.jpeg "NicolasC67")

[NicolasC67](https://community.sap.com/t5/user/viewprofilepage/user-id/120441)

Participant

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=hcm-blog-members&message.id=4914)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/hcm-blog-members/article-id/4914)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13554278)

‎2023 Apr 18
9:55 PM

[6
Kudos](/t5/kudos/messagepage/board-id/hcm-blog-members/message-id/4914/tab/all-users "Click here to see who gave kudos to this post.")

1,637

* SAP Managed Tags
* [SAP SuccessFactors Compensation](https://community.sap.com/t5/c-khhcw49343/SAP%2520SuccessFactors%2520Compensation/pd-p/73555000100800000771)

* [SAP SuccessFactors Compensation

  SAP SuccessFactors HCM](/t5/c-khhcw49343/SAP%2BSuccessFactors%2BCompensation/pd-p/73555000100800000771)

View products (1)

Hi everyone,

if you are working on SAP SuccessFactors Compensation, you certainly know already how to publish information from Compensation Worksheets to Employee Central. The module lets us define some fields to control the publishing (e.g. by Country, Legal Entity, etc.).

But what about the publishing towards a custom MDF portlet?

Publishing compensation data to a custom MDF table is pretty recent (at the time I write this blog post) and there is certainly room for improvement but if there is one thing that is missing compared to a publishing to Employee Central, that is the ability to "filter" or we should rather say "control" which employee we want to push/publish versus some others we must not or do not want.

There is no standard feature available so here under are few steps to guide you through implementing something simple to better control who is going to get published versus not.

1. Create a **Mandatory String Field** in your custom MDF object (e.g. Published from Compensation?)

2. Add a **Custom String Field** in your **Form Template** and play with its formula to describe the conditions upon which one employee should be published at the end of your campaign or not. (e.g. for an LTI process, you can set this custom field equal to **blank** if nothing has been granted to the employee and **YES** if otherwise)

3. In your XML, map your **Custom String Compensation Field** with you **Mandatory String Custom MDF Field**

Make sure the custom field either displays **YES** or **blank**. This way, during the publishing, sending blank towards your **Custom MDF Object** on that mandatory field will simply make the publishing fail for that particular employee. All the other employees having a **YES** would be published as expected.

![](/legacyfs/online/storage/blog_attachments/2023/04/2023-04-14_09-19-27.png)

Publishing log file

I will surely check in the Influence SAP Compensation campaign there is already an enhancement request to add a filter like we do have for EC publishing, but in the meantime, you can definitely go with the above solution to quickly control your MDF publishing.

If you want to go further, you can even add an **Editable YES/NO dropdown** field in your worksheet to let some C&B Admin or HRBP users choose who should get published or not, and ask them to provide a **rationale** maybe. Then based on that additional field, you take this dropdown field into consideration inside your formula which is controlling the publishing and you shall have something pretty handy for your compensation campaigns.

Should you have any questions or feedback, thanks for posting feedback here below, I'd love to hear back from you if that helped you or if you find any improvements to it!

Thanks for reading till the end ;)!

* [Compensation](/t5/tag/Compensation/tg-p/board-id/hcm-blog-members)
* [custom mdf](/t5/tag/custom%20mdf/tg-p/board-id/hcm-blog-members)
* [lti](/t5/tag/lti/tg-p/board-id/hcm-blog-members)
* [publishing](/t5/tag/publishing/tg-p/board-id/hcm-blog-members)

You must be a registered user to add a comment. If you've already registered, sign in. Otherwise, register and sign in.

* [Comment](/plugins/common/feature/oidcss/sso_login_redirect/providerid/sap_ids_prompt?redirectreason=permissiondenied&referer=https%3A%2F%2Fcommunity.sap.com%2Ft5%2Fhuman-capital-management-blog-posts-by-members%2Fhow-can-you-control-the-comp-to-mdf-publishing-by-employee%2Fba-p%2F13554278%23comment-on-this)

Copy Link
![](https://community.sap.com/html/@EE5D5986E9F4E5657DCEACB7532B5C39/assets/bluesky-dark.svg)Bluesky
Linkedin

Related Content

* [HR Efficiency in Action: Automate and Streamline HR Processes](/t5/human-capital-management-blog-posts-by-sap/hr-efficiency-in-action-automate-and-streamline-hr-processes/ba-p/14233229)
  in [Human Capital Management Blog Posts by SAP](/t5/human-capital-management-blog-posts-by-sap/bg-p/hcm-blog-sap)  Thursday
* [List of Employee Central & Employee Central Payroll Guide Updates for the 2H 2025 Release](/t5/human-capital-management-blog-posts-by-sap/list-of-employee-central-amp-employee-central-payroll-guide-updates-for-the/ba-p/14228406)
  in [Human Capital Management Blog Posts by SAP](/t5/human-capital-management-blog-posts-by-sap/bg-p/hcm-blog-sap)  a week ago
* [Publishing multiple event reason for same employee from compensation to EC](/t5/human-capital-management-q-a/publishing-multiple-event-reason-for-same-employee-from-compensation-to-ec/qaq-p/14221817)
  in [Human Capital Management Q&A](/t5/human-capital-management-q-a/qa-p/hcm-questions)  2 weeks ago
* [Managing Misconduct in SAP Successfactors : An MDF-Driven Approach](/t5/human-capital-management-blog-posts-by-members/managing-misconduct-in-sap-successfactors-an-mdf-driven-approach/ba-p/14216116)
  in [Human Capital Management Blog Posts by Members](/t5/human-capital-management-blog-posts-by-members/bg-p/hcm-blog-members)  2 weeks ago
* [Can we either hide or default the event and event reason in promotion through compensation worksheet](/t5/human-capital-management-q-a/can-we-either-hide-or-default-the-event-and-event-reason-in-promotion/qaq-p/14203115)
  in [Human Capital Management Q&A](/t5/human-capital-management-q-a/qa-p/hcm-questions)  2025 Sep 01

Top kudoed authors

| User | Count |
| --- | --- |
| [![StephanieBM01](https://avatars.profile.sap.com/c/c/idccc84e6bff2c414fae1b3ec977ab5e84ee0ad729b03db91e7b5124b190a9fbcd_small.jpeg "StephanieBM01")  StephanieBM01](/t5/user/viewprofilepage/user-id/24844) | 4 |
| [![nageshpolu](https://avatars.profile.sap.com/2/3/id23026426cb5d1932cfa7f01dbad97335...