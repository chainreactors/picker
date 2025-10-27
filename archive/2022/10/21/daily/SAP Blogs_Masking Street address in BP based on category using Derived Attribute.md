---
title: Masking Street address in BP based on category using Derived Attribute
url: https://blogs.sap.com/2022/10/20/masking-street-address-in-bp-based-on-category-using-derived-attribute/
source: SAP Blogs
date: 2022-10-21
fetch_date: 2025-10-03T20:29:09.898716
---

# Masking Street address in BP based on category using Derived Attribute

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Technology](/t5/technology/ct-p/technology)
* [Technology Blog Posts by Members](/t5/technology-blog-posts-by-members/bg-p/technology-blog-members)
* Masking Street address in BP based on category usi...

Technology Blog Posts by Members

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/technology-blog-members/article-id/160137&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [Masking Street address in BP based on category using Derived Attribute](/t5/technology-blog-posts-by-members/masking-street-address-in-bp-based-on-category-using-derived-attribute/ba-p/13550590)

![former_member822053](https://avatars.profile.sap.com/former_member_small.jpeg "former_member822053")

[former\_member822053](https://community.sap.com/t5/user/viewprofilepage/user-id/822053)

Explorer

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=technology-blog-members&message.id=160137)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/technology-blog-members/article-id/160137)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13550590)

‎2022 Oct 20
9:40 PM

[3
Kudos](/t5/kudos/messagepage/board-id/technology-blog-members/message-id/160137/tab/all-users "Click here to see who gave kudos to this post.")

3,179

* SAP Managed Tags
* [field masking for Web Client UI](https://community.sap.com/t5/c-khhcw49343/field%2520masking%2520for%2520Web%2520Client%2520UI/pd-p/73555000100800000427)
* [UI data protection logging for SAP S/4HANA](https://community.sap.com/t5/c-khhcw49343/UI%2520data%2520protection%2520logging%2520for%2520SAP%2520S%252F4HANA/pd-p/73554900100800002264)
* [CRM WebClient UI](https://community.sap.com/t5/c-khhcw49343/CRM%2520WebClient%2520UI/pd-p/216479123645680540588211456657763)

* [field masking for Web Client UI

  field masking](/t5/c-khhcw49343/field%2Bmasking%2Bfor%2BWeb%2BClient%2BUI/pd-p/73555000100800000427)
* [CRM WebClient UI

  Software Product Function](/t5/c-khhcw49343/CRM%2BWebClient%2BUI/pd-p/216479123645680540588211456657763)
* [UI data protection logging for SAP S/4HANA

  Software Product](/t5/c-khhcw49343/UI%2Bdata%2Bprotection%2Blogging%2Bfor%2BSAP%2BS%25252F4HANA/pd-p/73554900100800002264)

View products (3)

SAP UI Masking is a tool that sits between the database and GUI to protect the sensitive data. Basically the tool works at the presentation layer which can be used for making a field display only, mask using a pattern or completely hide the field itself without impacting the application layer that runs the business processes.

**Attribute Based Masking**: ABAC Policy cockpit is the feature in the product that offers many ways to protect the sensitive data like Hiding, disabling or masking the field as the per the requirement.

In below example, we will use Attribute Based Masking on field **STREET**with respect to transaction codes BP and BUP3 but masking will use derived attribute and value range for category US1 to implement the logic.

If the data in the field STCD1 is further categorized by type US1 (SSN) and US2 (General Data) then Attribute based masking will be the solution and it will mask only if the category is of type US1.

**Business Scenario**: Business Partner data is deemed as highly sensitive which is common in many organizatons. Users who have access to business partner data like transactions BP and BUP3 see much more than they are authorized to see. There is a growing concern among the organizations to protect the data of their employees, customers and suppliers. At the same time many departments need access to display BUP3/BP hence securing the data based on context is legitimate case for using UI Masking and data protection.

![](/legacyfs/online/storage/blog_attachments/2022/10/BP-Address-without-mask-2.png)

BP Address Without Masking

![](/legacyfs/online/storage/blog_attachments/2022/10/BP-Address-with-mask.png)

BP Address with Masking

**Prequisite**: Add-on UISM100 must be installed first in the system to achieve Field level Masking

**Configuration Steps**:

Configure Technical Information (*Table Name-Field Name*) of field in masking configuration.

The Technical Address of a GUI field can be find by pressing “*F1*” on the field.

![](/legacyfs/online/storage/blog_attachments/2022/10/F1-Technical-Information.png)

F1 Technical Information

SPRO -> SAP NetWeaver -> UI Data Protection Masking for SAP S/4HANA –> Maintain Metadata Configuration

* Maintain Logical Attributes

* Maintain Technical Address

Under Maintain Logical Attributes –> Click on New Entries

![](/legacyfs/online/storage/blog_attachments/2022/10/Logical-Attribute.png)

Logical Attribute

Click on Maintain Technical Address –> Click on new entries

![](/legacyfs/online/storage/blog_attachments/2022/10/Maintain-Technical-Attribute.png)

Maintain Technical Attribute

* Enter the table, field name, and Logical Attribute. C

* Select the row and click on Mass Configuration

* Select all and Generate Customizing

* Save

Click on Maintain Attributes and Ranges for Policy

![](/legacyfs/online/storage/blog_attachments/2022/10/Derived-Attribute-1.png)

Derived Attribute

![](/legacyfs/online/storage/blog_attachments/2022/10/Value-Range-2.png)

Value Range

Go to SE24 and create the class with following code changes that applies to tables and t-code fields based on context

![](/legacyfs/online/storage/blog_attachments/2022/10/Masking-Class.png)

Masking Class

Data Protection Configuration

Click on Maintain Policy Details for Attribute-Based Authorizations

![](/legacyfs/online/storage/blog_attachments/2022/10/ABAC-Policy.png)

ABAC Policy

Assign the above policy to the Logical Attribute which is tied to the fields where masking needs to be switched on.

**Conclusion**: Street address is masked based on derived attribute based on category of type US1 in BP and BUP3

Please share your thoughts and feedback in a comment.

Related topics – link from the text

Ask questions about field masking for SAP GUI and follow <https://answers.sap.com/tags/67838200100800005192>

Read other field masking for SAP GUI and follow blog posts <https://blogs.sap.com/tags/67838200100800005192>

* [Data Protection and Privacy](/t5/tag/Data%20Protection%20and%20Privacy/tg-p/board-id/technology-blog-members)
* [ui masking](/t5/tag/ui%20masking/tg-p/board-id/technology-blog-members)

2 Comments

You must be a registered user to add a comment. If you've already registered, sign in. Otherwise, register and sign in.

* [Comment](/plugins/common/feature/oidcss/sso_login_redirect/providerid/sap_ids_prompt?redirectreason=permissiondenied&referer=https%3A%2F%2Fcommunity.sap.com%2Ft5%2Ftechnology-blog-posts-by-members%2Fmasking-street-address-in-bp-based-on-category-using-derived-attribute%2Fba-p%2F13550590%23comment-on-this)

Copy Link
![](https://community.sap.com/html/@EE5D5986E9F4E5657DCEACB7532B5C39/assets/bluesky-dark.svg)Bluesky
Linkedin

Related Content

* [The Ultimate SAP S/4HANA Guide: From Master Data to End-to-End Processes](/t5/technology-blog-posts-by-members/the-ultimate-sap-s-4hana-guide-from-master-data-to-end-to-end-processes/ba-p/14228226)
  in [Technology Blog Posts by Members](/t5/technology-blog-posts-by-members/bg-p/technology-blog-members)  a week ago
* [Enabling AD -based Kerberos for Windows, MacBook, and Desktop Linux](/t5/technolog...