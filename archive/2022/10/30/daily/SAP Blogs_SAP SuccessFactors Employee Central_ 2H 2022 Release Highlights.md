---
title: SAP SuccessFactors Employee Central: 2H 2022 Release Highlights
url: https://blogs.sap.com/2022/10/29/sap-successfactors-employee-central-2h-2022-release-highlights/
source: SAP Blogs
date: 2022-10-30
fetch_date: 2025-10-03T21:19:01.250096
---

# SAP SuccessFactors Employee Central: 2H 2022 Release Highlights

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Human Capital Management](/t5/human-capital-management/ct-p/hcm)
* [HCM Blog Posts by Members](/t5/human-capital-management-blog-posts-by-members/bg-p/hcm-blog-members)
* SAP SuccessFactors Employee Central: 2H 2022 Relea...

Human Capital Management Blog Posts by Members

Explore blogs from customers or SAP partners to gain best practices and fresh insights to succeed.

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/hcm-blog-members/article-id/4986&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [SAP SuccessFactors Employee Central: 2H 2022 Release Highlights](/t5/human-capital-management-blog-posts-by-members/sap-successfactors-employee-central-2h-2022-release-highlights/ba-p/13558550)

![nageshpolu](https://avatars.profile.sap.com/2/3/id23026426cb5d1932cfa7f01dbad9733599afa7882bd07df433a59e25fac28240_small.jpeg "nageshpolu")

[nageshpolu](https://community.sap.com/t5/user/viewprofilepage/user-id/751)

Contributor

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=hcm-blog-members&message.id=4986)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/hcm-blog-members/article-id/4986)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13558550)

‎2022 Oct 29
6:34 PM

[29
Kudos](/t5/kudos/messagepage/board-id/hcm-blog-members/message-id/4986/tab/all-users "Click here to see who gave kudos to this post.")

17,212

* SAP Managed Tags
* [SAP SuccessFactors Employee Central](https://community.sap.com/t5/c-khhcw49343/SAP%2520SuccessFactors%2520Employee%2520Central/pd-p/73555000100800000773)
* [SAP SuccessFactors HCM Suite](https://community.sap.com/t5/c-khhcw49343/SAP%2520SuccessFactors%2520HCM%2520Suite/pd-p/67838200100800004730)
* [SAP SuccessFactors Platform](https://community.sap.com/t5/c-khhcw49343/SAP%2520SuccessFactors%2520Platform/pd-p/73555000100800000775)

* [SAP SuccessFactors HCM Suite

  SAP SuccessFactors HCM](/t5/c-khhcw49343/SAP%2BSuccessFactors%2BHCM%2BSuite/pd-p/67838200100800004730)
* [SAP SuccessFactors Employee Central

  SAP SuccessFactors HCM](/t5/c-khhcw49343/SAP%2BSuccessFactors%2BEmployee%2BCentral/pd-p/73555000100800000773)
* [SAP SuccessFactors Platform

  SAP SuccessFactors HCM](/t5/c-khhcw49343/SAP%2BSuccessFactors%2BPlatform/pd-p/73555000100800000775)

View products (3)

Hi there,

Second half 2022 release is here!

This blog highlights key enhancements to SuccessFactors Employee Central (EC). This 2H release is more customer centric, lot of enhancements coming from customer community ideas, thumbs up!!

To celebrate 2H 2022 release, let’s look at some of the most interesting features and changes introduced since last time.

1. **UI Clean Up:** Long wait is over, team SAP removed all MDF-based foundation objects from the Manage Organization, Pay and Job Structures UI because you can't manage them here. You had to use the Manage Data UI instead. Finally, SAP decided to clean the interface. This enhancement is from a Customer Community idea

* Configuration Type: Universal

* ***Customer Community Idea***

![](/legacyfs/online/storage/blog_attachments/2022/10/Foundation-objects-1.png)

2. **Support for Additional Alternative Cost Centers**: Yes! You heard it right!! You now have the benefit of entering and assigning 30 alternative cost centers to an employee for a specified time period instead of the previous limitation of 12 alternative cost centers. This too is an enhancement from Customer Community idea.

* Configuration Type: Universal

* ***Customer Community Idea***

![](/legacyfs/online/storage/blog_attachments/2022/10/Cost-Center-1.png)

3. **Tooltip Added for HRIS Elements and Fields**: SAP added a tooltip for standard HRIS elements and fields on the Business Configuration UI. These tooltips provide meaningful information that helps administrators to use each field in the configuration. Again, an enhancement from Customer Community idea! Cheers!! Hope to see more coming.

* Configuration Type: Universal

* ***Customer Community Idea***

![](/legacyfs/online/storage/blog_attachments/2022/10/Tooltips-1.png)

4. **HRIS Actions from the Business Configuration UI is Deleted:** Clean up continues, most of the HRIS Actions from the section that isn't used in configuration of People Profile are removed from Manage Business Configuration > HRIS Actions. The actions under Business Configuration UI (BCUI) that are currently not used in configuration of the People Profile will be deleted on December 9, 2022.

* Configuration Type: Universal

![](/legacyfs/online/storage/blog_attachments/2022/10/HRIS-Actions-1.png)

5. **Manual Mass Change of Basic Rules to Application-Specific Scenarios:** One from my wish list and one more from customer community idea. Changing basic rules to application-specific rule scenarios for several rules at once is now a real thing. Yes, this is now possible for rules that can be converted to application-specific scenarios of the following modules:

   * **Employee Central Core & Time Off: Rules**

* All rules for workflows are assigned to an application-specific rule scenario. (WorkflowsNoBasicRules)

* All rules for event-reason derivation are assigned to an application-specific rule scenario. (EventReasonDerivationNoBasicRules)

* All rules that use the object Time Account Type are assigned to an application-specific rule scenario. (TimeAccountTypeNoBasicRules)

* All rules that use the object Time Type are assigned to an application-specific rule scenario. (TimeTypeNoBasicRule)

* Configuration Type: Universal

* ***Customer Community Idea***

**![](/legacyfs/online/storage/blog_attachments/2022/10/Business-Rules.png)**

6. **New Actions Available in Action Search**: A few new actions related to People Profile, Job Information, etc. are now available in the global header search box. Users can enter the exact text of an action or select from suggested actions to navigate to a desired product page.

Example:

* View my profile

* View my personal information

* View job Information for...

* View my job information

* View my organizational information

* View organizational information for....

* Configuration Type: Universal

![](/legacyfs/online/storage/blog_attachments/2022/10/Action-Search-2.png)

7. **New Replication Status in Data Replication Monitor**: SAP added a new status “*Awaiting Processing*” to the Employee Central Data Replication Monitor. The new status Awaiting Processing updates the Data Replication Monitor about employee replication requests that have been added to the staging area in the SAP S∕4HANA system but have yet to be processed. The status is also used when employee replication requests have been processed with temporary errors. This new status enables administrators to have a transparency in processing state of employees.

* Configuration Type: Universal

![](/legacyfs/online/storage/blog_attachments/2022/10/Replication.png)

8. **Last Updated by Source Information Added to Employee Central History UIs**: The "last updated" by source information is now provided on records created or changed using business processes or input channels running on Centralized services. For records saved using a process enabled on Centralized services, the system now shows through which business process the last change was made, for example, imports or transferring direct re...