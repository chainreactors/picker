---
title: Reward and Recognition – Spot Award Auto Budget Calculation
url: https://blogs.sap.com/2022/12/05/reward-and-recognition-spot-award-auto-budget-calculation/
source: SAP Blogs
date: 2022-12-06
fetch_date: 2025-10-04T00:34:20.043543
---

# Reward and Recognition – Spot Award Auto Budget Calculation

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Human Capital Management](/t5/human-capital-management/ct-p/hcm)
* [HCM Blog Posts by Members](/t5/human-capital-management-blog-posts-by-members/bg-p/hcm-blog-members)
* SuccessFactors Reward and Recognition - Spot Award...

Human Capital Management Blog Posts by Members

Explore blogs from customers or SAP partners to gain best practices and fresh insights to succeed.

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/hcm-blog-members/article-id/5096&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [SuccessFactors Reward and Recognition - Spot Award Auto Budget Calculation](/t5/human-capital-management-blog-posts-by-members/successfactors-reward-and-recognition-spot-award-auto-budget-calculation/ba-p/13564743)

![murat_alcal](https://avatars.profile.sap.com/2/2/id22aa59dcc5b67663fe4f96b9a4d75eaa4202a73fefe71a9875a7f6703fe76400_small.jpeg "murat_alcal")

[murat\_alcal](https://community.sap.com/t5/user/viewprofilepage/user-id/174722)

Participant

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=hcm-blog-members&message.id=5096)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/hcm-blog-members/article-id/5096)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13564743)

‎2022 Dec 05
8:46 PM

[10
Kudos](/t5/kudos/messagepage/board-id/hcm-blog-members/message-id/5096/tab/all-users "Click here to see who gave kudos to this post.")

4,857

* SAP Managed Tags
* [SAP SuccessFactors Compensation](https://community.sap.com/t5/c-khhcw49343/SAP%2520SuccessFactors%2520Compensation/pd-p/73555000100800000771)
* [SAP SuccessFactors HCM Suite](https://community.sap.com/t5/c-khhcw49343/SAP%2520SuccessFactors%2520HCM%2520Suite/pd-p/67838200100800004730)
* [SAP SuccessFactors Platform](https://community.sap.com/t5/c-khhcw49343/SAP%2520SuccessFactors%2520Platform/pd-p/73555000100800000775)

* [SAP SuccessFactors HCM Suite

  SAP SuccessFactors HCM](/t5/c-khhcw49343/SAP%2BSuccessFactors%2BHCM%2BSuite/pd-p/67838200100800004730)
* [SAP SuccessFactors Compensation

  SAP SuccessFactors HCM](/t5/c-khhcw49343/SAP%2BSuccessFactors%2BCompensation/pd-p/73555000100800000771)
* [SAP SuccessFactors Platform

  SAP SuccessFactors HCM](/t5/c-khhcw49343/SAP%2BSuccessFactors%2BPlatform/pd-p/73555000100800000775)

View products (3)

**Introduction**

In this blog post, I will be sharing an automated design concept for Spot Award Budget calculation and how to configure it.

---

**About Spot Awards**

A Spot Award is a non-recurring, compensation event that is based on a specific contribution or performance. It can be cash or stock and is generally subject to budget and guidelines. It can be peer-to-peer or delivered within a manager hierarchy.

Our key word here is budget.

**So, how do we manage the budgets?**

As per the system standard, the only way to maintain or manage the budget is to import the values via an admin tool by choosing any of the below methods and utilizing a data template;

1. Overwrite existing budget: If you want to perform a full data replacement

2. Add to existing budget: If you want to add to the existing budget data

The above methods do give you flexible management, there aren't any restrictions other than the used values that need to be lower than the imported budget amounts which is an obvious one but the existing methods do not provide a dynamic way to calculate the budget automatically through time.

I will share an automated solution to calculate, simulate and distribute spot award budgets to the budget holders.

**Scenario:** When the employee becomes eligible to hold a budget (becoming a manager for the first time, being promoted to a specific title, having new direct reports, etc.) to nominate people within their organization, the system will calculate the respective amount as per the company policy and assign it to the holder.

**Solution:** There are multiple ways to calculate and approach this scenario but for this blog, I will be choosing the below method;

![](/legacyfs/online/storage/blog_attachments/2022/12/Data-Flow.png)

Data Flow

1. Create a Spot Award Program. As a pre-requisite, you will need to have the necessary technical knowledge of the Reward & Recognition implementation. You can refer to the [implementation document](https://help.sap.com/docs/SAP_SUCCESSFACTORS_COMPENSATION/70b6f618048540f0847db586847bc14d/f1d3ed14e6e449a9b44b0fa93dd35747.html?locale=en-US).

2. Create the necessary custom MDF objects as per your policy requirements. As a pre-requisite, you will need to have the necessary technical knowledge of the Metadata Framework (MDF) implementation. You can refer to the [implementation document](https://help.sap.com/docs/SAP_SUCCESSFACTORS_PLATFORM/e4a4ce68589841709a8202928c23803a/44d64fea23df4544b6ce7e91587bf1af.html?locale=en-US&q=sap%20successfactors%20metadata%20framework).

   1. (Mandatory) Create a custom MDF object to calculate the budget as a simulated value, later on, this will be integrated with the standard "Spot Award Budget" object.

   2. (Optional) Create a custom MDF object to store the budget amount index to look up.

   3. (Optional) Create a custom MDF object (both a parent and a child object) to store the team member sizes per manager.

      1. If your policy dictates counting certain direct reports, you will need the child custom object.

      2. If your policy considers counting all of the direct reports, the parent object will suffice.

   4. (Optional) Create a custom MDF object to store additional budget values to input the values inside that calculations as exceptions to your generic calculation.

3. Create the business rules based on your calculation scenarios. As a pre-requisite, you will need to have the necessary technical knowledge of the Business Rules implementation. You can refer to the [implementation document](https://help.sap.com/docs/SAP_SUCCESSFACTORS_PLATFORM/b37699fa8054409787a8321c9428aeca/3edea1972e6a452bb740940d404b2845.html?locale=en-US).

4. Create the necessary integrations via the integration center. As a pre-requisite, you will need to have the necessary technical knowledge of the Integration Center usage. You can refer to the [implementation document](https://help.sap.com/docs/SAP_SUCCESSFACTORS_PLATFORM/60ba370328e0485797adde67aee846a0/6182c69afefc4fa9a800d7c79931b01b.html?locale=en-US).

---

**Solution Step-by-Step Guide**

**Step 1:** Create a Spot Award Program.

* Create the Spot Award Program as per your requirements. For the sake of this example budget hierarchy is "Nominator":

![](/legacyfs/online/storage/blog_attachments/2022/12/Spot-Award-Program.png)

Spot Award Program

---

**Step 2:** Create all of the custom MDF objects and data records. Sub-sections labelled as "Optional" are not mandatory to implement this solution.

* (Optional) Create a custom MDF object (both a parent and a child object) to store the team member sizes per manager.

![](/legacyfs/online/storage/blog_attachments/2022/12/Spot-Award-Budget-Calculation-Team-Member-Size-Settings.png)

Spot Award Budget Calculation Team Member Size - Settings

![](/legacyfs/online/storage/blog_attachments/2022/12/Spot-Award-Budget-Calculation-Team-Member-Size-Fields-and-Associations.png)

Spot Award Budget Calculation Team Member Size - Fields and Associations

![](/legacyfs/online/st...