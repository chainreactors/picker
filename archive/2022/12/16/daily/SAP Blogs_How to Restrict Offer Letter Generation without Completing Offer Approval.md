---
title: How to Restrict Offer Letter Generation without Completing Offer Approval
url: https://blogs.sap.com/2022/12/15/how-to-restrict-offer-letter-generation-without-completing-offer-approval/
source: SAP Blogs
date: 2022-12-16
fetch_date: 2025-10-04T01:40:09.765469
---

# How to Restrict Offer Letter Generation without Completing Offer Approval

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Human Capital Management](/t5/human-capital-management/ct-p/hcm)
* [HCM Blog Posts by Members](/t5/human-capital-management-blog-posts-by-members/bg-p/hcm-blog-members)
* How to Restrict Offer Letter Generation without Co...

Human Capital Management Blog Posts by Members

Explore blogs from customers or SAP partners to gain best practices and fresh insights to succeed.

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/hcm-blog-members/article-id/5091&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [How to Restrict Offer Letter Generation without Completing Offer Approval](/t5/human-capital-management-blog-posts-by-members/how-to-restrict-offer-letter-generation-without-completing-offer-approval/ba-p/13564309)

![anan_jayghosh](https://avatars.profile.sap.com/a/7/ida71234e52bce635a349bf8cf808b54b413dcae4f2fbbfac3b7f78d7da9210858_small.jpeg "anan_jayghosh")

![Product and Topic Expert](/html/@138D6F765B60D7FC0168643DE27D8A68/rank_icons/sap-logo-small-14px.png "Product and Topic Expert")
[anan\_jayghosh](https://community.sap.com/t5/user/viewprofilepage/user-id/8664)

Product and Topic Expert

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=hcm-blog-members&message.id=5091)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/hcm-blog-members/article-id/5091)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13564309)

‎2022 Dec 15
7:17 PM

[15
Kudos](/t5/kudos/messagepage/board-id/hcm-blog-members/message-id/5091/tab/all-users "Click here to see who gave kudos to this post.")

4,209

* SAP Managed Tags
* [SAP SuccessFactors Platform](https://community.sap.com/t5/c-khhcw49343/SAP%2520SuccessFactors%2520Platform/pd-p/73555000100800000775)
* [SAP SuccessFactors Recruiting](https://community.sap.com/t5/c-khhcw49343/SAP%2520SuccessFactors%2520Recruiting/pd-p/67837800100800006356)
* [SAP Workflow Management, business rules capability](https://community.sap.com/t5/c-khhcw49343/SAP%2520Workflow%2520Management%252C%2520business%2520rules%2520capability/pd-p/73554900100800000842)

* [SAP SuccessFactors Recruiting

  SAP SuccessFactors HCM](/t5/c-khhcw49343/SAP%2BSuccessFactors%2BRecruiting/pd-p/67837800100800006356)
* [SAP SuccessFactors Platform

  SAP SuccessFactors HCM](/t5/c-khhcw49343/SAP%2BSuccessFactors%2BPlatform/pd-p/73555000100800000775)
* [SAP Workflow Management, business rules capability

  SAP Business Technology Platform](/t5/c-khhcw49343/SAP%2BWorkflow%2BManagement%25252C%2Bbusiness%2Brules%2Bcapability/pd-p/73554900100800000842)

View products (3)

# Introduction

The offer management process allows recruiting users to send offers for approval before they are extended to the candidate.

The **O****ffer Approval** process consists of assembling the details of the offer intended for the candidate and routing it for approval from key stakeholders. Once the offer approval form is generated, it can be routed for approval to designated users

Once the offer is approved and ready to be extended to the candidate, users with proper permissions can generate **Offer Letters**. Offer letter data is populated into the selected template. The recruiting user may modify the letter and attach documents to be completed by the Candidate

*However, there are scenarios where the Recruiters forget/skip the Offer Approval step and they will directly generate the Offer Letter without the Offer Approval which will result in creating a lot of confusion and waste of time*.

To overcome this scenario, we have come up with a solution in such a way that we can **restrict the Offer Letter generation by the Recruiter if the Offer Approval is not completed**.

# Solution

The Solution is pretty much simple as follows,

1. Create a ***Custom picklist field*** in the ***Application*** for this and define it in the *****Offer Approval*****

2. Create an ***Error Message*** definition in *******Manage Data.*******

3. Write a ***Business rule*** based on the Offer Approval status and tag to the ***Custom picklist field*** that we have created.

#### 1 : Create a ***Custom picklist field*** in the ***Application*** for this and define it in the ***Offer Approval*** stage.

1. Create the ***Custom Picklist field*** with the name as “***Offer Approved***” values “**Yes**” & “***No***”.

![](/legacyfs/online/storage/blog_attachments/2022/12/MicrosoftTeams-image-2.png)

Fig-1: Screenshot of Job Application XML template.

2. Define the “***Write***” Permission to the “***Recruiter***” in the Job Requisition template for the filed “***cust\_offerApproved***” in the “***Offer Approval***” Status*.*

![](/legacyfs/online/storage/blog_attachments/2022/12/MicrosoftTeams-image-3-1.png)

Fig-2: Screenshot of Job Requisition xml template

3. Once you give the permission the same will be visible in the UI as below.

![](/legacyfs/online/storage/blog_attachments/2022/12/MicrosoftTeams-image-7-1.png)

Fig-3: Screenshot of the Application page in the Talent Pipeline

### 2 : Create an ***Error Message*** definition in ***Manage Data.***

1. Navigate to the “***Manage Data”*** and click on the “***Create New”*** section and select “***Message Definition***” to create an “***Error Message***”.You can configure the error message which is to be displayed with the required Translations. As of now, we are giving the following message as “***Text***” “ ***Please Initiate the Offer Approval***” After that provide the “***External Code & Name”*** and *“**Save”*** the Message Definition*.*

![](/legacyfs/online/storage/blog_attachments/2022/12/4-2.png)

Fig-4: Screenshot of Message Definition

#### 3: Write a ***Business rule*** based on the ***Offer Approval status*** and tag it to the ***Custom picklist field*** that we have created.

1. Navigate to “***Manage Rules in Recruiting”*** and create a new “***Job Application Business Rule***” Provide the “***Basic Information***” and provide the Below conditions in the Business Rule. Then select the “ Error Message” that we have created in Step -2. and also set one more condition to make the values in the “***Offer Approved”*** field to “***Null***”

![](/legacyfs/online/storage/blog_attachments/2022/12/MicrosoftTeams-image-4.png)

Fig-5: Screenshot of Business rule conditions

2. Now provide the “Else If” Condition as mentioned below and “***Save”*** the Business Rule.

![](/legacyfs/online/storage/blog_attachments/2022/12/MicrosoftTeams-image-5.png)

Fig-6: Screenshot of Business rule condition

3. Now we need to assign this Business Rule to the “***Job Application***” in “***Manage Rules in Recruiting***” and we need to assign the trigger point as “***Offer Approved***” field as Field Change Rule.

![](/legacyfs/online/storage/blog_attachments/2022/12/MicrosoftTeams-image-6.png)

Fig-7: Screenshot of Manage rules in Recruiting

4. We have defined the condition in such a way that, The system will automatically set the value of the “***Offer Approved***” field to “***Yes***” based on only if the status of “***Offer Approval***” is “***Completed***” and if the Recruiter tries to change the value manually, the system will automatically set the value to “***Null***”.

*Now we can navigate to the **Offer Approval** status and see how effectively our solution is working!!!*

**Condition-1**

If the Recruiter tries to Move the Candidate from “...