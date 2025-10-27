---
title: Employee Central Global Benefits Support for Affordable Care Act Reporting – Functionality & Configuration
url: https://blogs.sap.com/2023/03/14/employee-central-global-benefits-support-for-affordable-care-act-reporting-functionality-configuration/
source: SAP Blogs
date: 2023-03-15
fetch_date: 2025-10-04T09:35:21.008989
---

# Employee Central Global Benefits Support for Affordable Care Act Reporting – Functionality & Configuration

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Human Capital Management](/t5/human-capital-management/ct-p/hcm)
* [HCM Blog Posts by SAP](/t5/human-capital-management-blog-posts-by-sap/bg-p/hcm-blog-sap)
* Employee Central Global Benefits Support for Affor...

Human Capital Management Blog Posts by SAP

Learn directly from SAP experts through blogs that deliver practical guidance and opportunities to deepen your expertise.

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/hcm-blog-sap/article-id/6350&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [Employee Central Global Benefits Support for Affordable Care Act Reporting - Functionality & Configuration](/t5/human-capital-management-blog-posts-by-sap/employee-central-global-benefits-support-for-affordable-care-act-reporting/ba-p/13570348)

![nehasharma05](https://avatars.profile.sap.com/3/1/id313260fd4d87317148a8479b2d313c062646bceea707e76166f4aec9352fd67a_small.jpeg "nehasharma05")

![Associate](/html/@138D6F765B60D7FC0168643DE27D8A68/rank_icons/sap-logo-small-14px.png "Associate")
[nehasharma05](https://community.sap.com/t5/user/viewprofilepage/user-id/19781)

Associate

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=hcm-blog-sap&message.id=6350)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/hcm-blog-sap/article-id/6350)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13570348)

‎2023 Mar 14
9:22 PM

[3
Kudos](/t5/kudos/messagepage/board-id/hcm-blog-sap/message-id/6350/tab/all-users "Click here to see who gave kudos to this post.")

1,614

* SAP Managed Tags
* [SAP SuccessFactors Employee Central](https://community.sap.com/t5/c-khhcw49343/SAP%2520SuccessFactors%2520Employee%2520Central/pd-p/73555000100800000773)
* [SAP SuccessFactors Employee Central Global Benefits](https://community.sap.com/t5/c-khhcw49343/SAP%2520SuccessFactors%2520Employee%2520Central%2520Global%2520Benefits/pd-p/e85065bf-d10d-4f03-bdce-48b6dea5c230)

* [SAP SuccessFactors Employee Central

  SAP SuccessFactors HCM](/t5/c-khhcw49343/SAP%2BSuccessFactors%2BEmployee%2BCentral/pd-p/73555000100800000773)
* [SAP SuccessFactors Employee Central Global Benefits

  Additional Software Product](/t5/c-khhcw49343/SAP%2BSuccessFactors%2BEmployee%2BCentral%2BGlobal%2BBenefits/pd-p/e85065bf-d10d-4f03-bdce-48b6dea5c230)

View products (2)

As the Product Manager for Total Rewards - SAP SuccessFactors, I am excited to share that with the H2 2022 release, SAP SuccessFactors has introduced two enhancements to support United States Affordable Care Act Reporting.

The system will now be able to:

1. Store additional configurations regarding an insurance plan:
   Minimum Essential Coverage,
   Minimum Value,
   Plan Type (Fully Insured, Self-Insured)

2. Capture & Update the offer of Minimum Essential Coverage Plans for employees in various scenarios.

Let's first learn about the new elements of this enhancement and then delve into how each of these play together in various scenarios.

* #### **New Fields - Fields in Insurance Plan Object**

![](/legacyfs/online/storage/blog_attachments/2023/03/insurance-plan-setup.png)

New Fields in Insurance Plan Object

The above fields progressively appear when the Country/Region field is set as United States.

1. Minimum Essential Coverage: This is Yes/No field and can be set accordingly by the admin when a plan meets the MEC criteria as per the ACA guidelines.

2. Evaluate Offer of Coverage: This is a Yes/No field which shall be chosen to create offer records for the MEC plan. Only plans with a ‘yes’ value will be considered for offer record creation.

3. Coverage for Employee Required Contribution: This field needs to be set with the coverage name that is for the Enrollment For Option related to Employee only providing coverage to the employee only.

4. Enrolling for Employee Required Contribution: This field needs to be set with the Enrollment For option related to Employee only.

5. Plan Type: Configurability between Self-Insured & Fully Insured.

6. Minimum Value: This is a Yes/No field capturing whether a plan meets the standard insurance coverage requirement.

* **New Job - Evaluate Offer for Affordable Care Act Reporting**

This job can be configured in Admin Centre under Manage Data. This job creates offer records for the employees for the Insurance benefits with MEC plans. Admin needs to fill in the fields - Benefit, Insurance Plan (MEC Insurance Plan) and Job Owner.  On click of save, the job runs and can be monitored in Execution Manager Dashboard.

![](/legacyfs/online/storage/blog_attachments/2023/03/new-job.png)

Evaluate Offer for Affordable Care Act Reporting Job Setup

* **New Object - Benefit Offer Details for Employee**

This object captures the details of the MEC plan offer that is made to an employee. It gets updated in various scenarios which is detailed further.

![](/legacyfs/online/storage/blog_attachments/2023/03/offer-object.png)

Benefit Offer Details for Employee Object

The Date of Offer is the date when the MEC Insurance Plan is offered to the employee. Best practice to get this field captured correctly is to run the job the same day when the Open Enrollment Window Opens.
Employee Required Contribution is the minimum cost value which the employee contributes for a MEC plan that provides coverage only to the employee.

Now that the new elements are understood, let's look at the various situations of an employee cycle and the update in data captured in the ‘Benefit Offer Details for Employee’ object.

**Scenario 1: Open Enrollment Window**

Open enrollment is from 1 Jan 2023 to 28 Feb 2023. Benefits are effective from 1 March 2023 until 29 Feb 2024. To capture the offer details of the employees, admin should perform the below steps.

Step 1: Configure the fields for the MEC relevant insurance plan.
Step 2: Set up the ‘Evaluate Offer for Affordable Care Act Reporting’ job in the admin center for the required benefit & plan and monitor in Execution Manager Dashboard.
Step 3: Once the job is completed, you can see in Manage Data that ‘Benefit Offer Details for Employee’ record for the employees got created.

Below is a screenshot showing the offer record of Employee Oliver Perez.

![](/legacyfs/online/storage/blog_attachments/2023/03/OE.png)

Scenario - Open Enrollment

**Scenario 2: Enrollment**

Open enrollment is from 1 Jan 2023 to 28 Feb 2023. The Benefit Offer Details for Employee record is already in place in the ‘Offered’ status due to the job that was run by admin on 1 Jan 2023.  Employee Oliver Perez chooses to enroll into the Benefit and MEC Plan on 23 Jan 2023. The existing offer record gets updated with further details. In the below screenshot we can see that the details got updated – Status of Offer changed to Enrolled; Request date, Effective from date, Enrollment End Date got captured.

Evaluate Offer for Affordable Care Act Reporting job is not needed to be run as this is an automatic update.

![](/legacyfs/online/storage/blog_attachments/2023/03/enrollment.png)

Scenario - Employee Enrolls

**Scenario 3: Opt-Out**

1. Opt-out when OE window is open
   Open enrollment is from 1 Jan 2023 to 28 Feb 2023. Employee Oliver Perez chooses to enroll into the benefit Medical Insurance on 23 Jan 2023, but on 24 Jan 2023 he opt-outs of the benefit. The opt-out is effective from 1 March 2023....