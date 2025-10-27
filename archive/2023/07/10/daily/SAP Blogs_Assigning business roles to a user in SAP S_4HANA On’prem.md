---
title: Assigning business roles to a user in SAP S/4HANA On’prem
url: https://blogs.sap.com/2023/07/09/assigning-business-roles-to-a-user-in-sap-s-4hana-onprem/
source: SAP Blogs
date: 2023-07-10
fetch_date: 2025-10-04T11:52:27.103092
---

# Assigning business roles to a user in SAP S/4HANA On’prem

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Technology](/t5/technology/ct-p/technology)
* [Technology Blog Posts by Members](/t5/technology-blog-posts-by-members/bg-p/technology-blog-members)
* Assigning business roles to a user in SAP S/4HANA ...

Technology Blog Posts by Members

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/technology-blog-members/article-id/160981&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [Assigning business roles to a user in SAP S/4HANA On'prem](/t5/technology-blog-posts-by-members/assigning-business-roles-to-a-user-in-sap-s-4hana-on-prem/ba-p/13555545)

![mickaelquesnot](https://avatars.profile.sap.com/5/9/id592e9cc97ec986f0d6ae5e9db725546658112960aaef6e03a2a7680bb1496070_small.jpeg "mickaelquesnot")

[mickaelquesnot](https://community.sap.com/t5/user/viewprofilepage/user-id/150004)

Active Participant

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=technology-blog-members&message.id=160981)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/technology-blog-members/article-id/160981)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13555545)

‎2023 Jul 09
9:02 AM

[3
Kudos](/t5/kudos/messagepage/board-id/technology-blog-members/message-id/160981/tab/all-users "Click here to see who gave kudos to this post.")

6,621

* SAP Managed Tags
* [SAP Fiori](https://community.sap.com/t5/c-khhcw49343/SAP%2520Fiori/pd-p/73554900100700000977)
* [SAP ERP](https://community.sap.com/t5/c-khhcw49343/SAP%2520ERP/pd-p/01200615320800000659)
* [SAP ERP Central Component](https://community.sap.com/t5/c-khhcw49343/SAP%2520ERP%2520Central%2520Component/pd-p/01200314690800000122)
* [SAP Fiori for SAP S/4HANA](https://community.sap.com/t5/c-khhcw49343/SAP%2520Fiori%2520for%2520SAP%2520S%252F4HANA/pd-p/73555000100800000131)
* [SAP S/4HANA](https://community.sap.com/t5/c-khhcw49343/SAP%2520S%252F4HANA/pd-p/73554900100800000266)

* [SAP ERP

  SAP ERP](/t5/c-khhcw49343/SAP%2BERP/pd-p/01200615320800000659)
* [SAP ERP Central Component

  SAP ERP](/t5/c-khhcw49343/SAP%2BERP%2BCentral%2BComponent/pd-p/01200314690800000122)
* [SAP S/4HANA

  SAP S/4HANA](/t5/c-khhcw49343/SAP%2BS%25252F4HANA/pd-p/73554900100800000266)
* [SAP Fiori

  Software Product](/t5/c-khhcw49343/SAP%2BFiori/pd-p/73554900100700000977)
* [SAP Fiori for SAP S/4HANA

  SAP Fiori](/t5/c-khhcw49343/SAP%2BFiori%2Bfor%2BSAP%2BS%25252F4HANA/pd-p/73555000100800000131)

View products (5)

Creating basic settings for using SAP Fiori launchpad (back-end system)

<https://youtu.be/6M-5D5JZmDw>

Context

If you use the SAP Fiori launchpad as user interface, a prerequisite is that you have roles assigned to your Fiori user in the NetWeaver Gateway system.

SAP delivers a bundle of business roles as templates for customers. You must copy all \*BR\* roles for SAP Best Practices for SAP S/4HANA from the Gateway Server to your namespace.

Note

SAP\_BR\* roles are not designed to be used as productive roles. They are demo roles which enable system users to make use of the SAP Fiori launchpad and try out the predefined scope items of SAP Best Practices for SAP S/4HANA.

For productive use, you should always copy the delivered roles and adapt them as required. In addition, you define and implement an appropriate authorization concept.

For a summary of all roles used in this edition sorted by scope item, refer to the Process steps, business roles, and apps .

You have the following options for assigning business roles:

 You assign only roles needed for a specific scope item. In this case, check the related test script for the required roles in the Roles section. You can find the test scripts in the SAP Best Practices documentation package.

 You assign all roles needed for SAP Best Practices for SAP S/4HANA. In this case, assign all business roles to your user.

Procedure

1. In the SAP NetWeaver Gateway system, choose one of the following navigation options:

Transaction Code/app SU01

SAP Menu Tools Administration User Maintenance Users

2. In the User Maintenance screen, enter the user ID of the user who you want to assign a role to.

3. Choose Change.

4. In the Maintain User view, choose the Roles tab.

5. In the Role field, enter the role name. Use the wildcard \*BR\* to search for all relevant roles. You can assign several roles to a user at this stage if necessary.

6. Choose Enter, save, and go back to the SAP Easy Access view.

Results

The roles are now assigned to the user. These roles are referred to in the test script.

[https://fioriappslibrary.hana.ondemand.com/sap/fix/externalViewer/#](https://fioriappslibrary.hana.ondemand.com/sap/fix/externalViewer/)

Download PDF :

[https://www.linkedin.com/posts/mickaelquesnot\_abrtau-activity-7083681636822720512-7Dln?utm\_source=sh...](https://www.linkedin.com/posts/mickaelquesnot_abrtau-activity-7083681636822720512-7Dln?utm_source=share&utm_medium=member_desktop)

* [business role](/t5/tag/business%20role/tg-p/board-id/technology-blog-members)

You must be a registered user to add a comment. If you've already registered, sign in. Otherwise, register and sign in.

* [Comment](/plugins/common/feature/oidcss/sso_login_redirect/providerid/sap_ids_prompt?redirectreason=permissiondenied&referer=https%3A%2F%2Fcommunity.sap.com%2Ft5%2Ftechnology-blog-posts-by-members%2Fassigning-business-roles-to-a-user-in-sap-s-4hana-on-prem%2Fba-p%2F13555545%23comment-on-this)

Copy Link
![](https://community.sap.com/html/@EE5D5986E9F4E5657DCEACB7532B5C39/assets/bluesky-dark.svg)Bluesky
Linkedin

Related Content

* [SAP S4HANA Plant Maintenance for dummies](/t5/technology-blog-posts-by-members/sap-s4hana-plant-maintenance-for-dummies/ba-p/14234304)
  in [Technology Blog Posts by Members](/t5/technology-blog-posts-by-members/bg-p/technology-blog-members)  yesterday
* [Project-Based Services in SAP S/4HANA](/t5/technology-blog-posts-by-members/project-based-services-in-sap-s-4hana/ba-p/14234290)
  in [Technology Blog Posts by Members](/t5/technology-blog-posts-by-members/bg-p/technology-blog-members)  yesterday
* [Organizational Management in SAP S/4HANA HCM](/t5/technology-blog-posts-by-members/organizational-management-in-sap-s-4hana-hcm/ba-p/14234285)
  in [Technology Blog Posts by Members](/t5/technology-blog-posts-by-members/bg-p/technology-blog-members)  yesterday
* [🚀 The Universal Journal is Calling: Master the Evolution to S/4HANA Intelligence](/t5/technology-blog-posts-by-members/the-universal-journal-is-calling-master-the-evolution-to-s-4hana/ba-p/14229512)
  in [Technology Blog Posts by Members](/t5/technology-blog-posts-by-members/bg-p/technology-blog-members)  Saturday
* [The Power of the Batch: Why Traceability is Non-Negotiable in Supply Chain 🧪📦](/t5/technology-blog-posts-by-members/the-power-of-the-batch-why-traceability-is-non-negotiable-in-supply-chain/ba-p/14229432)
  in [Technology Blog Posts by Members](/t5/technology-blog-posts-by-members/bg-p/technology-blog-members)  a week ago

Top kudoed authors

| User | Count |
| --- | --- |
| [![WouterLemaire](https://avatars.profile.sap.com/9/5/id95a688fa6b84e4186cabf39d7a83127ea90dd51dd190d355416d56f7d3a5be56_small.jpeg "WouterLemaire")  ![SAP Mentor](/html/@F4C200E47DAE3459A6BD3FBB7F9955B8/rank_icons/mentor-rank-16x16.svg "SAP Mentor") WouterLemaire](/t5/user/viewprofilepage/user-id/9863) | 6 |
| [![rajarajeswari_k...