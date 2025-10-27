---
title: Task state and Requirement State in SAP Cloud ALM
url: https://blogs.sap.com/2023/01/02/task-state-and-requirement-state-in-sap-cloud-alm/
source: SAP Blogs
date: 2023-01-03
fetch_date: 2025-10-04T02:54:54.870445
---

# Task state and Requirement State in SAP Cloud ALM

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Technology](/t5/technology/ct-p/technology)
* [Technology Blog Posts by SAP](/t5/technology-blog-posts-by-sap/bg-p/technology-blog-sap)
* Task state and Requirement State in SAP Cloud ALM

Technology Blog Posts by SAP

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/technology-blog-sap/article-id/161586&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [Task state and Requirement State in SAP Cloud ALM](/t5/technology-blog-posts-by-sap/task-state-and-requirement-state-in-sap-cloud-alm/ba-p/13561232)

![Jagmohan_Chawla](https://avatars.profile.sap.com/3/e/id3e02a32d24af6c810a7dca23644384a1930dc86567a9f0501bce6dfe6f6c6d25_small.jpeg "Jagmohan_Chawla")

![Product and Topic Expert](/html/@138D6F765B60D7FC0168643DE27D8A68/rank_icons/sap-logo-small-14px.png "Product and Topic Expert")
[Jagmohan\_Chawla](https://community.sap.com/t5/user/viewprofilepage/user-id/64810)

Product and Topic Expert

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=technology-blog-sap&message.id=161586)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/technology-blog-sap/article-id/161586)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13561232)

‎2023 Jan 02
12:35 PM

[6
Kudos](/t5/kudos/messagepage/board-id/technology-blog-sap/message-id/161586/tab/all-users "Click here to see who gave kudos to this post.")

5,007

* SAP Managed Tags
* [RISE with SAP](https://community.sap.com/t5/c-khhcw49343/RISE%2520with%2520SAP/pd-p/1e76886f-86ac-4839-9833-8bf95f5eb775)
* [SAP Activate](https://community.sap.com/t5/c-khhcw49343/SAP%2520Activate/pd-p/714d86bf-f0de-4038-81e4-25c791c15f0c)
* [SAP Cloud ALM](https://community.sap.com/t5/c-khhcw49343/SAP%2520Cloud%2520ALM/pd-p/73554900100800002513)
* [SAP S/4HANA](https://community.sap.com/t5/c-khhcw49343/SAP%2520S%252F4HANA/pd-p/73554900100800000266)
* [SAP S/4HANA Cloud Public Edition](https://community.sap.com/t5/c-khhcw49343/SAP%2520S%252F4HANA%2520Cloud%2520Public%2520Edition/pd-p/08e2a51b-1ce5-4367-8b33-4ae7e8b702e0)

* [SAP S/4HANA Cloud Public Edition

  SAP S/4HANA Cloud](/t5/c-khhcw49343/SAP%2BS%25252F4HANA%2BCloud%2BPublic%2BEdition/pd-p/08e2a51b-1ce5-4367-8b33-4ae7e8b702e0)
* [RISE with SAP

  Topic](/t5/c-khhcw49343/RISE%2Bwith%2BSAP/pd-p/1e76886f-86ac-4839-9833-8bf95f5eb775)
* [SAP Activate

  Services and Support](/t5/c-khhcw49343/SAP%2BActivate/pd-p/714d86bf-f0de-4038-81e4-25c791c15f0c)
* [SAP S/4HANA

  SAP S/4HANA](/t5/c-khhcw49343/SAP%2BS%25252F4HANA/pd-p/73554900100800000266)
* [SAP Cloud ALM

  Software Product](/t5/c-khhcw49343/SAP%2BCloud%2BALM/pd-p/73554900100800002513)

View products (5)

In this blog post, I would like to explain

* What is a state attribute for Tasks and Requirements

* How Obsolete task state is used

* How Task state is used in Deletion

# What is Task state

The Task state is an attribute of the Task. It denotes if the task is actively in use or not.

If it's not visible in your task list you can enable it using the filter options and column result settings

![](/legacyfs/online/storage/blog_attachments/2023/01/Taskstate.jpg)

# What are the values in the Task state

Task state can be Active or Obsolete

![](/legacyfs/online/storage/blog_attachments/2023/01/taskstatevalues.jpg)

by default, the Task list hides all the tasks in the state "Obsolete" but you can enable it using the filters to see the Obsolete tasks also

# How can a Task State be set to Obsolete?

There are many ways it can be done.  The most common are via SAP Activate content update or manually

###

### Via SAP Activate Content Update

In some situations, the instructions provided by the SAP Activate team may become out of date. As an example when SAP introduces automation, some of the previous procedures are deprecated. To ensure your tasks provided by SAP Activate methodology always remain up to date, such tasks are set to Obsolete by the system.

![](/legacyfs/online/storage/blog_attachments/2023/01/example_obs_task.jpg)

### Manually

If in a Project a certain Task is no longer meaningful but you want to maintain its existence, you can set this to Obsolete. You need to ensure you are in display mode to see this option.

![](/legacyfs/online/storage/blog_attachments/2023/01/set_to_obs.jpg)

Note that when a task is set to Obsolete, the status of the task is still preserved as the action can be reversed anytime by setting the Task to Active again

![](/legacyfs/online/storage/blog_attachments/2023/01/set_to_activ.jpg)

# How Obsolete Tasks behave

Obsolete tasks

* get a special prefix [Obsolete] in front of the Task Tile

* become read-only

# How Task state is important for deletion

Tasks and Requirements can not be deleted unless they are first set to the Obsolete state. This is to ensure accidental deletion is avoided. This is also explained in detail in this [Blog Post](https://blogs.sap.com/2022/01/26/sap-cloud-alm-important-change-set-tasks-requirements-to-obsolete-then-delete/)

# Next steps

As we publish more and more blog posts, it’s easy to get lost. Please visit the [Master Blog post](https://blogs.sap.com/2021/01/08/understanding-project-and-task-management-in-sap-cloud-alm/) and bookmark it.

To understand an end-to-end picture, please visit

[Expert Portal for Implementation](https://support.sap.com/en/alm/sap-cloud-alm/implementation/sap-cloud-alm-implementation-expert-portal.html) and staying connected. You can also Follow me to ensure you do not miss any updates.

Labels

* [Product Updates](/t5/technology-blog-posts-by-sap/bg-p/technology-blog-sap/label-name/product%20updates)

You must be a registered user to add a comment. If you've already registered, sign in. Otherwise, register and sign in.

* [Comment](/plugins/common/feature/oidcss/sso_login_redirect/providerid/sap_ids_prompt?redirectreason=permissiondenied&referer=https%3A%2F%2Fcommunity.sap.com%2Ft5%2Ftechnology-blog-posts-by-sap%2Ftask-state-and-requirement-state-in-sap-cloud-alm%2Fba-p%2F13561232%23comment-on-this)

Copy Link
![](https://community.sap.com/html/@EE5D5986E9F4E5657DCEACB7532B5C39/assets/bluesky-dark.svg)Bluesky
Linkedin

Related Content

* [S/4HANA transition for US Federal Agencies](/t5/technology-blog-posts-by-sap/s-4hana-transition-for-us-federal-agencies/ba-p/14234423)
  in [Technology Blog Posts by SAP](/t5/technology-blog-posts-by-sap/bg-p/technology-blog-sap)  3 hours ago
* [What’s new in Mobile development kit client 25.9](/t5/technology-blog-posts-by-sap/what-s-new-in-mobile-development-kit-client-25-9/ba-p/14227370)
  in [Technology Blog Posts by SAP](/t5/technology-blog-posts-by-sap/bg-p/technology-blog-sap)  yesterday
* [Secure Your Digital Journey with SAP CIAM](/t5/technology-blog-posts-by-sap/secure-your-digital-journey-with-sap-ciam/ba-p/14232983)
  in [Technology Blog Posts by SAP](/t5/technology-blog-posts-by-sap/bg-p/technology-blog-sap)  yesterday
* [Transforming Healthcare Procurement: Lessons from Our S/4HANA MM Implementation](/t5/technology-q-a/transforming-healthcare-procurement-lessons-from-our-s-4hana-mm/qaq-p/14233251)
  in [Technology Q&A](/t5/technology-q-a/qa-p/technology-questions)  yesterday
* [Document Grounding: A (hidden) gem in SAP Business AI’s portfolio for smaller companies.](/t5/technology-blog-posts-by-sap/document-grounding-a-hidden-gem-in-sap-business-ai-s-portfolio...