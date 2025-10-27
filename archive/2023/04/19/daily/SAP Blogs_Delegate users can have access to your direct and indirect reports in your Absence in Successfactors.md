---
title: Delegate users can have access to your direct and indirect reports in your Absence in Successfactors
url: https://blogs.sap.com/2023/04/18/delegate-users-can-have-access-to-your-direct-and-indirect-reports-in-your-absence-in-successfactors/
source: SAP Blogs
date: 2023-04-19
fetch_date: 2025-10-04T11:34:24.045017
---

# Delegate users can have access to your direct and indirect reports in your Absence in Successfactors

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Human Capital Management](/t5/human-capital-management/ct-p/hcm)
* [HCM Blog Posts by Members](/t5/human-capital-management-blog-posts-by-members/bg-p/hcm-blog-members)
* Delegate users can have access to your direct and ...

Human Capital Management Blog Posts by Members

Explore blogs from customers or SAP partners to gain best practices and fresh insights to succeed.

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/hcm-blog-members/article-id/4960&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [Delegate users can have access to your direct and indirect reports in your Absence in Successfactors](/t5/human-capital-management-blog-posts-by-members/delegate-users-can-have-access-to-your-direct-and-indirect-reports-in-your/ba-p/13555729)

![vpathangi](https://avatars.profile.sap.com/7/6/id7697ea3594d8b8f8a4281771cba17cc6d662ad7d39dbfdab4eff51ae68eaece8_small.jpeg "vpathangi")

[vpathangi](https://community.sap.com/t5/user/viewprofilepage/user-id/21727)

Participant

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=hcm-blog-members&message.id=4960)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/hcm-blog-members/article-id/4960)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13555729)

‎2023 Apr 18
4:07 PM

[7
Kudos](/t5/kudos/messagepage/board-id/hcm-blog-members/message-id/4960/tab/all-users "Click here to see who gave kudos to this post.")

6,940

* SAP Managed Tags
* [SAP SuccessFactors Employee Central](https://community.sap.com/t5/c-khhcw49343/SAP%2520SuccessFactors%2520Employee%2520Central/pd-p/73555000100800000773)
* [SAP SuccessFactors Employee Central - Employee Profile](https://community.sap.com/t5/c-khhcw49343/SAP%2520SuccessFactors%2520Employee%2520Central%2520-%2520Employee%2520Profile/pd-p/445702386321465023058666394389900)
* [SAP SuccessFactors Time Tracking](https://community.sap.com/t5/c-khhcw49343/SAP%2520SuccessFactors%2520Time%2520Tracking/pd-p/73555000100800002827)

* [SAP SuccessFactors Employee Central

  SAP SuccessFactors HCM](/t5/c-khhcw49343/SAP%2BSuccessFactors%2BEmployee%2BCentral/pd-p/73555000100800000773)
* [SAP SuccessFactors Employee Central - Employee Profile

  Software Product Function](/t5/c-khhcw49343/SAP%2BSuccessFactors%2BEmployee%2BCentral%2B-%2BEmployee%2BProfile/pd-p/445702386321465023058666394389900)
* [SAP SuccessFactors Time Tracking

  SAP SuccessFactors HCM](/t5/c-khhcw49343/SAP%2BSuccessFactors%2BTime%2BTracking/pd-p/73555000100800002827)

View products (3)

In Successfactors a Manager or HR in his absence can delegate any user his role to perform the task that Manager and HR was performing in actual role.

To achieve this, follow the below process.

**What are Delegates?**

The delegate users you assign will have access to your direct and indirect reports and can perform tasks that have been permissioned to you in the granted Permission Role, whilst acting as your delegate.

You can assign up to two delegates per delegator and each delegate can be given separate tasks or permissions to cover different functional areas. Please note, delegates will not have access to the delegators data.

Delegates are maintained in Job Relationships in Employee Central.

**Configuration - jobRelType picklist (the first letter should be lowercase in "jobRelType", otherwise, the system will not pick the changes inserted to a picklist that is labelled differently)**

Two new Job Relationships must be added to the "jobRelType" picklist in your instance. These are -:

* Delegate A

* Delegate B

***NOTE:*** When defining the External Code and Non-unique External Code of the picklist, make sure there is a space between the word and the number. i.e. "delegate 1" / "delegate 2"

**Configuration - Manage Permission Roles**

When defining the Target permissions of a Permission Role, you can now define "Delegate A" and "Delegate B" in the "Grant role to" pop-up. These options will only appear once the jobRelType picklist has been updated with the delegate values. Then you will be able to leverage the delegate roles the same as any other role (such as Manager).

).

![](/legacyfs/online/storage/blog_attachments/2023/04/Delegate-1-1.jpg)

![](/legacyfs/online/storage/blog_attachments/2023/04/Delegate-2.jpg)

If delegate relationship has been defined in Employee Central picklists, you can grant a permission role to delegates. When a manager delegates his or her tasks to two delegates, delegate A and delegate B, the manager’s direct reports will be the target population of delegate A and delegate B. If the manager, delegate A, and delegate B are in the same permission roles, delegate A and delegate B will have the same permissions. The manager’s direct reports will be the target populations of the delegate A and delegate B for the permissions which require a target. However, this delegate relationship cannot be used in non-user-based permissions. For example, even if delegate A and delegate B has the same “Miscellaneous Permissions > Position” permission as the manager, delegate A and delegate B cannot view the current state of the position or view its history because the “Position” permission is not user-based.

***What is user-based permission?***

* Permission to the data of a user. For example, the “Personal Information” permission controls access to the personal information data of a user.

* The target population of the permission can be grouped as a user list

* It can be RBP permissions or some of the MDF permissions

***What is non-user-based permission?***

User can distinguish those MDF objects if they are categorized in “Permission requiring MDF object target”. Those permissions will not be supported through delegate relationship.

![](/legacyfs/online/storage/blog_attachments/2023/04/Delegate-3.jpg)

Hope this blog was very useful for you in EC successfactors.

Thanks...will be back with one more new blog soon.

------ Venkata Subbarao Pathangi

* [delegate](/t5/tag/delegate/tg-p/board-id/hcm-blog-members)
* [delegate authentication](/t5/tag/delegate%20authentication/tg-p/board-id/hcm-blog-members)
* [delegated administration](/t5/tag/delegated%20administration/tg-p/board-id/hcm-blog-members)
* [SAP SF EC](/t5/tag/SAP%20SF%20EC/tg-p/board-id/hcm-blog-members)
* [SAPSuccessFactors](/t5/tag/SAPSuccessFactors/tg-p/board-id/hcm-blog-members)

5 Comments

You must be a registered user to add a comment. If you've already registered, sign in. Otherwise, register and sign in.

* [Comment](/plugins/common/feature/oidcss/sso_login_redirect/providerid/sap_ids_prompt?redirectreason=permissiondenied&referer=https%3A%2F%2Fcommunity.sap.com%2Ft5%2Fhuman-capital-management-blog-posts-by-members%2Fdelegate-users-can-have-access-to-your-direct-and-indirect-reports-in-your%2Fba-p%2F13555729%23comment-on-this)

Copy Link
![](https://community.sap.com/html/@EE5D5986E9F4E5657DCEACB7532B5C39/assets/bluesky-dark.svg)Bluesky
Linkedin

Related Content

* [HR Efficiency in Action: Automate and Streamline HR Processes](/t5/human-capital-management-blog-posts-by-sap/hr-efficiency-in-action-automate-and-streamline-hr-processes/ba-p/14233229)
  in [Human Capital Management Blog Posts by SAP](/t5/human-capital-management-blog-posts-by-sap/bg-p/hcm-blog-sap)  Thursday
* [Talent Intelligence Hub - Workflow for Proficiency Le...