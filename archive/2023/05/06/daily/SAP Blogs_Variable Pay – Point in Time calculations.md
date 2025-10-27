---
title: Variable Pay – Point in Time calculations
url: https://blogs.sap.com/2023/05/05/variable-pay-point-in-time-calculations/
source: SAP Blogs
date: 2023-05-06
fetch_date: 2025-10-04T11:40:39.170615
---

# Variable Pay – Point in Time calculations

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Human Capital Management](/t5/human-capital-management/ct-p/hcm)
* [HCM Blog Posts by SAP](/t5/human-capital-management-blog-posts-by-sap/bg-p/hcm-blog-sap)
* Variable Pay - Point in Time calculations

Human Capital Management Blog Posts by SAP

Learn directly from SAP experts through blogs that deliver practical guidance and opportunities to deepen your expertise.

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/hcm-blog-sap/article-id/6392&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [Variable Pay - Point in Time calculations](/t5/human-capital-management-blog-posts-by-sap/variable-pay-point-in-time-calculations/ba-p/13570930)

![](/skins/images/E8A536C0D834652C9A43FCC2963C1D98/responsive_peak/images/icon_anonymous_profile.png)

Former Member

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=hcm-blog-sap&message.id=6392)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/hcm-blog-sap/article-id/6392)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13570930)

‎2023 May 05
12:47 PM

[12
Kudos](/t5/kudos/messagepage/board-id/hcm-blog-sap/message-id/6392/tab/all-users "Click here to see who gave kudos to this post.")

4,067

* SAP Managed Tags
* [SAP SuccessFactors Compensation](https://community.sap.com/t5/c-khhcw49343/SAP%2520SuccessFactors%2520Compensation/pd-p/73555000100800000771)
* [SAP SuccessFactors Employee Central](https://community.sap.com/t5/c-khhcw49343/SAP%2520SuccessFactors%2520Employee%2520Central/pd-p/73555000100800000773)

* [SAP SuccessFactors Compensation

  SAP SuccessFactors HCM](/t5/c-khhcw49343/SAP%2BSuccessFactors%2BCompensation/pd-p/73555000100800000771)
* [SAP SuccessFactors Employee Central

  SAP SuccessFactors HCM](/t5/c-khhcw49343/SAP%2BSuccessFactors%2BEmployee%2BCentral/pd-p/73555000100800000773)

View products (2)

## Introduction

A common Variable Pay request is to perform calculations based upon employees’ salaries as of a certain date, usually the end of the year. When integrating Variable Pay with Employee Central, this seemingly innocuous request becomes somewhat complex, as normally EC stores the employees’ “actual” salaries – that is, the salary of the job reduced for those who are on FTEs less than 1. When requesting the salary as of 31 December, for example, Variable Pay would get the part-time salary for part-time people and disregard the changes of FTE that may have happened in the year prior.

This means customers really don’t want to use the end of year salary - there is still proration involved. A better way to explain the requirement is to say they want to use the end of year FTE salary and prorate for changes in FTE and bonus target. For example, consider the following case:

An employee starts the year working full-time at a salary of £3,825 a month with a 20% bonus target. On the 1st of April, their salary is increased to £3,925 a month as part of the annual salary round. On the first of August, they change their working hours from 1 FTE to 0.75 FTE, so their salary in EC is changed from £3,925 to £2,943.75. Now imagine on 1 September they are promoted (but remain on 0.75 FTE) to a new monthly salary of £3,150 and bonus target of 25%.

The customer requirement is to have the bonus be based on the salary as of 31 December. If we go from the above, that would be an annual amount of £37,800. The pay component group for the bonus target is no better – it shows the bonus target as of that date and doesn’t consider the change in bonus target, let alone the change in FTE.

The bonus basis should be calculated as:

```
FTE Salary as of 31 December * FTE * bonus target percentage
```

For each change in FTE and bonus target percentage.

This should result in an employee history of the following:

|
 Start |
 End |
 Actual Annual Salary |
 FTE Annual Salary |
 Bonus Target % |
 FTE |
 Basis |

|
 01-Jan |
 31-Mar |
 45900 |
 45900 |
 20 |
 1 |
 10080 |

|
 01-Apr |
 31-Jul |
 47100 |
 47100 |
 20 |
 1 |
 10080 |

|
 01-Aug |
 31-Aug |
 35325 |
 47100 |
 20 |
 0.75 |
 7560 |

|
 01-Sep |
 31-Dec |
 37800 |
 50400 |
 25 |
 0.75 |
 9450 |

For row 1, the basis is calculated as 50400 (the FTE salary as of 31 Dec) \* 20% \* 1 = 10800. This is duplicated for row 2. For row 3, the basis is 50400 \* 20% \* 0.75 = 7560. For row 4, it is 50400 \* 25% \* 0.75 = 9450.

The question is, how do you configure this solution in EC and Variable Pay? I thought that this was impossible without something like a back-dated pay component or the like. I could think of no way to incorporate the FTE into the basis calculation – I wanted to multiply the FTE salary by the FTE:

```
(FTE Salary as of 31 December * FTE) * bonus target percentage
```

I then remembered the associative property of multiplication and shifted my thinking to:

```
FTE Salary as of 31 December * (FTE * bonus target percentage)
```

We don’t need to multiply the salary; we can multiply the bonus target! That opened things up – all it takes is some new fields in EC and a couple business rules and the job is done.

## Employee Central Configuration

Before proceeding on the details of the EC configuration, let’s revisit the Variable Pay point in time configuration options of the “Set Bonus Calculation” screen:

![](/legacyfs/online/storage/blog_attachments/2023/05/2023-05-04_16-47-43.jpg)

There are several options here, but specifically look at the first three check boxes. We have the following options:

* Salary and bonus target come from job (or comp, even though it isn’t mentioned) info

* Salary comes from a pay component group and bonus target comes from a field in job or comp info

* Basis comes from a pay component group

Of the three options, the second one is what we want and conforms most to best practices. Salary is stored in a pay component group and we get the bonus target percentage from a field. Let’s work with that.

|
 **NOTE:** I am basing the configuration of this blog on a very standard Essential Process Content (ex-Model Company) configuration. This has the following assumptions:    * Base Salary is stored in a single pay component and is the ‘actual’ salary (PC 1002)  * Bonus Target is stored in a single pay component and is a percentage (PC 1111)     It is highly likely your customer configuration will vary significantly. The basic concept presented above are transferable to other configurations, but the configuration steps below are specific to the starting configuration. I am unable to help with the configuration and requirements of your customers with out an official SAP Professional Services engagement. |

This means we will need a few things from EC:

* A custom field on Compensation Information to hold the “prorated” bonus target percentage

* A pay component group to hold the annualised FTE Salary

* A pay component to hold the periodic FTE Salary

* Business rules to populate the above

### Custom Bonus Target Percentage

I chose to add the custom field to Compensation Information. Navigate to Manage Business Configuration:

![](/legacyfs/online/storage/blog_attachments/2023/05/2023-05-04_17-06-11.jpg)

Add a custom field with the following properties:

![](/legacyfs/online/storage/blog_attachments/2023/05/2023-05-04_17-07-06.jpg)

Of course, the label is up to you. I chose “Bonusable Target Pct” because...