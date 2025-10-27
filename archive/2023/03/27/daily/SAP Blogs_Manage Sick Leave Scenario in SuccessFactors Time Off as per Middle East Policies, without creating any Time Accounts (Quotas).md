---
title: Manage Sick Leave Scenario in SuccessFactors Time Off as per Middle East Policies, without creating any Time Accounts (Quotas)
url: https://blogs.sap.com/2023/03/26/manage-sick-leave-scenario-in-successfactors-time-off-as-per-middle-east-policies-without-creating-any-time-accounts-quotas/
source: SAP Blogs
date: 2023-03-27
fetch_date: 2025-10-04T10:45:56.979093
---

# Manage Sick Leave Scenario in SuccessFactors Time Off as per Middle East Policies, without creating any Time Accounts (Quotas)

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Human Capital Management](/t5/human-capital-management/ct-p/hcm)
* [HCM Blog Posts by Members](/t5/human-capital-management-blog-posts-by-members/bg-p/hcm-blog-members)
* Manage Sick Leave Scenario in SuccessFactors Time ...

Human Capital Management Blog Posts by Members

Explore blogs from customers or SAP partners to gain best practices and fresh insights to succeed.

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/hcm-blog-members/article-id/4916&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [Manage Sick Leave Scenario in SuccessFactors Time Off as per Middle East Policies, without creating any Time Accounts (Quotas)](/t5/human-capital-management-blog-posts-by-members/manage-sick-leave-scenario-in-successfactors-time-off-as-per-middle-east/ba-p/13554887)

![arrouth](https://avatars.profile.sap.com/5/a/id5a79b2f5e00c4b9857da29a824fcce7f81219e523c2ba6b31e1b8e40ef30cbbf_small.jpeg "arrouth")

[arrouth](https://community.sap.com/t5/user/viewprofilepage/user-id/37040)

Participant

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=hcm-blog-members&message.id=4916)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/hcm-blog-members/article-id/4916)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13554887)

‎2023 Mar 26
4:25 PM

[14
Kudos](/t5/kudos/messagepage/board-id/hcm-blog-members/message-id/4916/tab/all-users "Click here to see who gave kudos to this post.")

13,109

* SAP Managed Tags
* [SAP SuccessFactors Employee Central](https://community.sap.com/t5/c-khhcw49343/SAP%2520SuccessFactors%2520Employee%2520Central/pd-p/73555000100800000773)
* [SAP SuccessFactors HCM Core](https://community.sap.com/t5/c-khhcw49343/SAP%2520SuccessFactors%2520HCM%2520Core/pd-p/67837800100800006332)
* [HCM Time Management](https://community.sap.com/t5/c-khhcw49343/HCM%2520Time%2520Management/pd-p/666118459887932219928019980895838)

* [SAP SuccessFactors HCM Core

  SAP SuccessFactors HCM](/t5/c-khhcw49343/SAP%2BSuccessFactors%2BHCM%2BCore/pd-p/67837800100800006332)
* [HCM Time Management

  Software Product Function](/t5/c-khhcw49343/HCM%2BTime%2BManagement/pd-p/666118459887932219928019980895838)
* [SAP SuccessFactors Employee Central

  SAP SuccessFactors HCM](/t5/c-khhcw49343/SAP%2BSuccessFactors%2BEmployee%2BCentral/pd-p/73555000100800000773)

View products (3)

Dear Readers, In this blog we'll check a suitable solution for one of the very demanding scenarios for Middle East region-specific customers.

## **Business Requirement:**

Sick leave is granted for 120 days per annum, **where the year begins from the first date of the sick leave**, at the following rate. The sick leave period can either be continuous or intermittent.

* The first 30 days: entitled for Full Pay (100%)

* The following 60 days: entitled for three-quarters of the wage (75%)

* And the following 30 days without pay.

As per current features in SuccessFactors, this dynamic year detection based on the first sick leave application is not feasible by standard. So in this blog, we’ll check a suitable workaround solution, to meet this requirement.

**NOTE:** In this blog, **we have focused only on the specific part of the requirement (dynamic year detection)**. The salary proration based on the number of days applied in sick leave is not covered in this blog. This can be done in Payroll directly, rather in SuccessFactors EC Time Management.

**Disclaimer:** All pictures are taken from DEMO system.

## **Key Benefits of the Solution:**

1. No Time Accounts (Quotas) need to be created. The policy restriction can be managed through Take-Rules (Business Rules). So no burden of time accounts.

2. End User Experience wise also this solution will be stable and acceptable, as the end-user only will interact with Time-Off screen, just like other leaves.

3. Apart from the Leave application, no additional manual activity is required.

## **Overview of the Solution Design:**

![](/legacyfs/online/storage/blog_attachments/2023/03/Capture11-1.png)

Overview of the solution design

## **Configuration Steps in detail:**

### **Step 1: Time Type Creation and Assignment to Time Profile**

Go to '*Manage Data*' and create 'Sick Leave' Time Type as below:

![](/legacyfs/online/storage/blog_attachments/2023/03/Time-Type.png)

Sick Leave Time Type

Assign the sick leave to relevant Time profile.

![](/legacyfs/online/storage/blog_attachments/2023/03/Time-profile-assignment.png)

Example: Assign Time Type to Time Profile

### **Step 2: Create custom fields in 'Employee Time' Object.**

Go to '*Configure Object Definition -> Object = 'Employee Time''* and create two custom fields as below to capture Sick Leave Period Start Date and End Date.

![](/legacyfs/online/storage/blog_attachments/2023/03/Custom-field-in-Employee-Time.png)

Custom Fields in Employee Time

Apply the below field condition so that those fields only appear/applicable for '*Sick Leave*'. In the below example, the condition value is set as '1011' as we have created Sick Leave with external code '1011'.

NOTE: **'Visibility**' of those custom fields should be **'*Editable***', else in Integration Center Job, those fields will not be available.

![](/legacyfs/online/storage/blog_attachments/2023/03/Filter-Condition.png)

Field Condition on Custom Fields in Employee Time

Go to relevant permission role in '*Manage Permission Role*' admin tool and apply below permission setting for those custom fields in 'Employee Time' object, so that those fields should appear as read only in Time-Off Screen.

![](/legacyfs/online/storage/blog_attachments/2023/03/RBP.png)

Apply field level override permission for custom fields

### **Step 3: Create a custom MDF.**

Go to '*Configure Object Definition*' and create one Custom MDF as below. The purpose of this MDF is to store Sick Leave Period Start Date and Sick Leave Period End Date as per approved sick leaves.

![](/legacyfs/online/storage/blog_attachments/2023/03/Custom-MDF.png)

Custom MDF Definition to store Sick Leave period Start Date and End Date for individual Employees

### **Step 4: Business Rule to populate Custom fields 'Period Start Date' and 'Period End Date' in '*Employee Time*' object.**

Go to '*Configure Business Rule*' and create a business rule as below with base object 'Employee Time' and assign it to *'On Change*' event of below fields in 'Employee Time' MDF.

* Time type

* Start date

* End date

Purpose of this business rule is to populate '**Period Start Date**' and '**Period End Date**' while employee going to submit Sick Leave request.

Business Rule Logic:

If employee is applying first sick leave in that period, then 'Period Start Date' = Leave start date and 'Period End Date' = Leave start date + 12 Months.

If employee is applying further sick leave in that period, then 'Period Start Date' and 'Period End Date' is getting populated based on Custom MDF Table data.

![](/legacyfs/online/storage/blog_attachments/2023/03/Business-Rule-to-populate-custom-field1.png)

![](/legacyfs/online/storage/blog_attachments/2023/03/Business-Rule-to-populate-custom-field2.png)

Business Rule to Populate Sick Leave Period Start and End Date in Time Off Screen

### **Step 5: Build Integration Center Job**

Build one Integration Center Job as below.

The Purpose of this Job is to repl...