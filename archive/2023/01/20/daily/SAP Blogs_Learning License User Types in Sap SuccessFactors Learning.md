---
title: Learning License User Types in Sap SuccessFactors Learning
url: https://blogs.sap.com/2023/01/19/learning-license-user-types-in-sap-successfactors-learning/
source: SAP Blogs
date: 2023-01-20
fetch_date: 2025-10-04T04:22:36.216947
---

# Learning License User Types in Sap SuccessFactors Learning

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Human Capital Management](/t5/human-capital-management/ct-p/hcm)
* [HCM Blog Posts by Members](/t5/human-capital-management-blog-posts-by-members/bg-p/hcm-blog-members)
* Learning License User Types in SAP SuccessFactors ...

Human Capital Management Blog Posts by Members

Explore blogs from customers or SAP partners to gain best practices and fresh insights to succeed.

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/hcm-blog-members/article-id/5267&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [Learning License User Types in SAP SuccessFactors Learning](/t5/human-capital-management-blog-posts-by-members/learning-license-user-types-in-sap-successfactors-learning/ba-p/13571296)

![kchamarthy](https://avatars.profile.sap.com/b/d/idbd8182f484e9fa8e92aca5f2fd1fb535eeca7dad0d5c8affc4ffa004bf62a422_small.jpeg "kchamarthy")

[kchamarthy](https://community.sap.com/t5/user/viewprofilepage/user-id/33909)

Explorer

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=hcm-blog-members&message.id=5267)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/hcm-blog-members/article-id/5267)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13571296)

‎2023 Jan 19
11:27 PM

[13
Kudos](/t5/kudos/messagepage/board-id/hcm-blog-members/message-id/5267/tab/all-users "Click here to see who gave kudos to this post.")

14,245

* SAP Managed Tags
* [SAP SuccessFactors HCM Suite](https://community.sap.com/t5/c-khhcw49343/SAP%2520SuccessFactors%2520HCM%2520Suite/pd-p/67838200100800004730)
* [SAP SuccessFactors Learning](https://community.sap.com/t5/c-khhcw49343/SAP%2520SuccessFactors%2520Learning/pd-p/67837800100800006334)
* [SAP SuccessFactors Platform](https://community.sap.com/t5/c-khhcw49343/SAP%2520SuccessFactors%2520Platform/pd-p/73555000100800000775)

* [SAP SuccessFactors HCM Suite

  SAP SuccessFactors HCM](/t5/c-khhcw49343/SAP%2BSuccessFactors%2BHCM%2BSuite/pd-p/67838200100800004730)
* [SAP SuccessFactors Learning

  SAP SuccessFactors HCM](/t5/c-khhcw49343/SAP%2BSuccessFactors%2BLearning/pd-p/67837800100800006334)
* [SAP SuccessFactors Platform

  SAP SuccessFactors HCM](/t5/c-khhcw49343/SAP%2BSuccessFactors%2BPlatform/pd-p/73555000100800000775)

View products (3)

SAP SuccessFactors licenses for Learning classify the users into two License user types, “Active” or “Functional”. It is important to classify the users into right type for compliance with the licenses purchased by the customer.

**Difference between Functional user and Active user:**

The Learning management system does not differentiate between an Active and Functional User. The License type classification is only used for licensing and reporting reasons.

**Who is an Active Learning User?**

Employees with active profiles in the system that are not classified as functional are classified as **ACTIVE**

**Who is a Functional Learning User?**

Employees and non-employees whose learning history records are recorded within Learning but are not given access to the Learning management system are classified as **FUNCTIONAL**

Below are few examples of how customers can categorize the users under the two License types.

* Functional User: Users who are Seasonal, Mastered in SAP HCM, Contractor, Retirees, Former employees with access

* Active Users: Users who are Full time, Part time, Leave of Absence

A customer can categorize any user as Functional user only if they have purchased the Functional licenses.

**How are the Active/Functional users measured?**

The License User type is measured by SAP as below:

**Active User –**

Active user count includes the below criteria :

* All the users who have ACTIVE status and are not classified as Functional user and  not using Learning market place in the LMS

* ALL users who have one learning history recorded in the Learning system for an external or internal course or have a course enrolled or launched a course on their learning plan

**Functional User –**

Functional user count includes the below criteria :

* All the users who have ACTIVE status and are classified as Functional user and not using Learning market place in the LMS

* All users who have one learning history recorded in the Learning system for an external or internal course or have a course enrolled or launched a course on their learning plan

**Methods of updating the License user type**

The License User type field on the User record can be updated using any of these methods:

1. Manual update of License User Types in Learning Administration

2. Importing License User Types in Learning Administration (Batch Import)

3. Importing License User Types in Learning Administration (using User Connector)

4. Updating the Succession data model with Standard element-“LearningLicenseUserType” for sending the License information from Bizx to Learning

**1.Manual update of License User Types in Learning Administration**

If customers have purchased SAP SuccessFactors Learning external or functional licenses and are using shopping account type or any other custom field in the system to classify the users as external, the user license types must be assigned to the External users as Functional.

Procedure to set License user type:

* Go to Learning Administration> People> Users

* Search for the user to find the user with the incorrect license user type and edit the record.

* In License User Type, select the license type of the user:

  + Active

  + Functional

**Search for users and their status**

![](/legacyfs/online/storage/blog_attachments/2023/01/Search-User-type-by-License-user-type-1.png)

*Search Users by Learning License User Type*

**2.Importing License User Types in Learning Administration (Batch Import)**

To update multiple user license types in learning, you may import the user records with the license types .

**Procedure:**

* In Learning Administration> System Administration >Tools> Import Data.

* Select the Record type of **User** and then select **Download Template** to download the latest import template.

* Add the users in the User ID column and add the correct License User Type for the users and save your changes.

* Select Import Data to import the file updated with records

* You may import as a background job or choose to run the job immediately or to schedule to run the job.

* Select Finish.

Note: When adding new users, if license user type value is left blank, the system will default the type to Active.

**Import User Data**

Download the Import data Template for User import

![](/legacyfs/online/storage/blog_attachments/2023/01/Import-User-data-1.png)

*Import User Data*

3. **Importing License User Types in Learning Administration (using User Connector)**

If the license user type is not maintained in your HRIS, and you would like to update it directly in LMS, you may use the User connector to update the license user type in LMS

For updating license user type of users using User Connector, follow the below steps:

1. Update the Connector configuration here -System administration > Configuration > System Configuration > Connectors = user.field.mapping.data. LICENSE\_USER\_TYPE=FUNCTIONAL

2. Identify User records - Identify the user records to update the Correct License user type

3. Download the User connector template here-System administration > Connecto...