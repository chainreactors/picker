---
title: How to preset the default Search Method in SAP MDG-F without ABAP knowledge (step-by-step guide)
url: https://blogs.sap.com/2023/01/05/how-to-preset-the-default-search-method-in-sap-mdg-f-without-abap-knowledge-step-by-step-guide/
source: SAP Blogs
date: 2023-01-06
fetch_date: 2025-10-04T03:09:25.808974
---

# How to preset the default Search Method in SAP MDG-F without ABAP knowledge (step-by-step guide)

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Technology](/t5/technology/ct-p/technology)
* [Technology Blog Posts by Members](/t5/technology-blog-posts-by-members/bg-p/technology-blog-members)
* How to preset the default Search Method in SAP MDG...

Technology Blog Posts by Members

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/technology-blog-members/article-id/162112&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [How to preset the default Search Method in SAP MDG-F without ABAP knowledge (step-by-step guide)](/t5/technology-blog-posts-by-members/how-to-preset-the-default-search-method-in-sap-mdg-f-without-abap-knowledge/ba-p/13561356)

![patrick_c](https://avatars.profile.sap.com/6/a/id6a927ae53d704c55114c0617a2965ef2037c830f37c686844f9dd96c4c5b1805_small.jpeg "patrick_c")

[patrick\_c](https://community.sap.com/t5/user/viewprofilepage/user-id/46016)

Explorer

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=technology-blog-members&message.id=162112)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/technology-blog-members/article-id/162112)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13561356)

‎2023 Jan 05
9:32 PM

[2
Kudos](/t5/kudos/messagepage/board-id/technology-blog-members/message-id/162112/tab/all-users "Click here to see who gave kudos to this post.")

5,278

* SAP Managed Tags
* [SAP Fiori](https://community.sap.com/t5/c-khhcw49343/SAP%2520Fiori/pd-p/73554900100700000977)
* [SAP Master Data Governance](https://community.sap.com/t5/c-khhcw49343/SAP%2520Master%2520Data%2520Governance/pd-p/67837800100800004488)
* [UI SAP Business Client (NWBC)](https://community.sap.com/t5/c-khhcw49343/UI%2520SAP%2520Business%2520Client%2520%28NWBC%29/pd-p/514184132407067932511783863172239)

* [SAP Master Data Governance

  SAP Master Data Governance](/t5/c-khhcw49343/SAP%2BMaster%2BData%2BGovernance/pd-p/67837800100800004488)
* [SAP Fiori

  Software Product](/t5/c-khhcw49343/SAP%2BFiori/pd-p/73554900100700000977)
* [UI SAP Business Client (NWBC)

  Software Product Function](/t5/c-khhcw49343/UI%2BSAP%2BBusiness%2BClient%2B%252528NWBC%252529/pd-p/514184132407067932511783863172239)

View products (3)

In this blog post you will learn how to easily change the Search Method in SAP MDG.

I have a Master Data Management background and train to master the MDG tool to make it usable for my customers.

When I first had to change the Search Method, I ran into some dead ends, and you, dear reader, should be spared that. That is why I have created this blog entry for those who have a basic knowledge of MDG customizing but have never made this kind of change.

**Let's start!**

In the following case I change the Search Method "Database Search" to "HANA Search".

The steps listed are similar for business partners and materials.

![](/legacyfs/online/storage/blog_attachments/2023/01/Screenshot-2023-01-02-151149.png)

Open "Technical Help".

![](/legacyfs/online/storage/blog_attachments/2023/01/Screenshot-2023-01-02-151402-3.png)

Now open Component Configuration.

![](/legacyfs/online/storage/blog_attachments/2023/01/Screenshot-2023-01-02-151716.png)

Click on "Where-Used list". The Application Configuration in the picture above shows you which Floorplan Configuration you need to choose.

![](/legacyfs/online/storage/blog_attachments/2023/01/Screenshot-2023-01-03-084259-1.png)

The next step begins in the "Main Page" area. The Search Method is located on the "Initial Page".

![](/legacyfs/online/storage/blog_attachments/2023/01/Screenshot-2023-01-02-152756.png)

Now click on the wrench of the Search UIBB.

![](/legacyfs/online/storage/blog_attachments/2023/01/Screenshot-2023-01-02-153125.png)

Now open Feeder Class Parameters.

![](/legacyfs/online/storage/blog_attachments/2023/01/Screenshot-2023-01-02-153508-1.png)

Change the Search Mode and the Incl.SearchHelp (below a short explanation how to insert the correct values) to the required one.

*Note - if you just enter a Search Mode HA and leave Incl.SearchHelp blank, you will get a blank entry in the Search Method field.*

![](/legacyfs/online/storage/blog_attachments/2023/01/Screenshot-2023-01-02-154224.png)

Press OK, test the changes and don't forget to save.

Now you have preset the Search Method to "HANA Search".

![](/legacyfs/online/storage/blog_attachments/2023/01/Screenshot-2023-01-02-155758.png)

**Where to find Search Mode and Incl.SearchHelp**

Start here:

MDGIMG/General Settings/Data Quality and Search/Define Search Applications

If you enter the section you have an overview of all available Search Modes

![](/legacyfs/online/storage/blog_attachments/2023/01/Screenshot-2023-01-02-154611.png)

Mark the required line and enter "Allocation of Search Help to Search Applications". Now you get an overview of all available Included search helps.

![](/legacyfs/online/storage/blog_attachments/2023/01/Screenshot-2023-01-02-155210.png)

![](/legacyfs/online/storage/blog_attachments/2023/01/Screenshot-2023-01-02-155601.png)

You can find the matching values for you Application Configuration here: [Set Up SAP HANA Search | SAP Help Portal](https://help.sap.com/docs/SAP_ERP_SPV/c20fcc49c3304d84bc462c8dcea1df6f/32fa01534849f41ee10000000a441470.html?locale=en-US&version=6.18.13)

**Conclusion**

It is very easy to change the search setting in the MDG.

Post your feedback and thoughts on the article!

Also I recommend to look at following resources:

Governance environment Topic page
<https://community.sap.com/topics/master-data-governance>

Post and answer questions
<https://answers.sap.com/tags/67837800100800004488>,

And read other posts on the topic <https://blogs.sap.com/tags/67837800100800004488/>

Don't forget to follow my profile for similar content ![:slightly_smiling_face:](/html/@4B6312D6275C37BF1932F8F25B21CD47/emoticons/1f642.png ":slightly_smiling_face:")

* [MDG](/t5/tag/MDG/tg-p/board-id/technology-blog-members)
* [mdg-f](/t5/tag/mdg-f/tg-p/board-id/technology-blog-members)
* [mdgbp](/t5/tag/mdgbp/tg-p/board-id/technology-blog-members)
* [mdgf](/t5/tag/mdgf/tg-p/board-id/technology-blog-members)
* [mdgm](/t5/tag/mdgm/tg-p/board-id/technology-blog-members)

4 Comments

You must be a registered user to add a comment. If you've already registered, sign in. Otherwise, register and sign in.

* [Comment](/plugins/common/feature/oidcss/sso_login_redirect/providerid/sap_ids_prompt?redirectreason=permissiondenied&referer=https%3A%2F%2Fcommunity.sap.com%2Ft5%2Ftechnology-blog-posts-by-members%2Fhow-to-preset-the-default-search-method-in-sap-mdg-f-without-abap-knowledge%2Fba-p%2F13561356%23comment-on-this)

Copy Link
![](https://community.sap.com/html/@EE5D5986E9F4E5657DCEACB7532B5C39/assets/bluesky-dark.svg)Bluesky
Linkedin

Related Content

* [Where can I get practice questions for SAP C\_TS4FI\_2023 prep?](/t5/technology-q-a/where-can-i-get-practice-questions-for-sap-c-ts4fi-2023-prep/qaq-p/14234268)
  in [Technology Q&A](/t5/technology-q-a/qa-p/technology-questions)  8 hours ago
* [What's New in SAP Analytics Cloud Modeling Extensions & Integration QRC4 2025 Release](/t5/technology-blog-posts-by-sap/what-s-new-in-sap-analytics-cloud-modeling-extensions-amp-integration-qrc4/ba-p/14208685)
  in [Technology Blog Posts by SAP](/t5/technology-blog-posts-by-sap/bg-p/technology-blog-sap)  yesterday
* [Document Grounding: A (h...