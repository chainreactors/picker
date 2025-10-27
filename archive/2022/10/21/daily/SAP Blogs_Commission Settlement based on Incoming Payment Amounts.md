---
title: Commission Settlement based on Incoming Payment Amounts
url: https://blogs.sap.com/2022/10/20/commission-settlement-based-on-incoming-payment-amounts/
source: SAP Blogs
date: 2022-10-21
fetch_date: 2025-10-03T20:29:32.366504
---

# Commission Settlement based on Incoming Payment Amounts

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Enterprise Resource Planning](/t5/enterprise-resource-planning/ct-p/erp)
* [ERP Blog Posts by Members](/t5/enterprise-resource-planning-blog-posts-by-members/bg-p/erp-blog-members)
* Commission Settlement based on Incoming Payment Am...

Enterprise Resource Planning Blog Posts by Members

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/erp-blog-members/article-id/66382&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [Commission Settlement based on Incoming Payment Amounts](/t5/enterprise-resource-planning-blog-posts-by-members/commission-settlement-based-on-incoming-payment-amounts/ba-p/13542333)

![thiagorigo](https://avatars.profile.sap.com/a/b/idabb319ce52b04b628a1a688ced9ed63922b59575d7444e523b0829192d4d19f8_small.jpeg "thiagorigo")

[thiagorigo](https://community.sap.com/t5/user/viewprofilepage/user-id/122164)

Explorer

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=erp-blog-members&message.id=66382)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/erp-blog-members/article-id/66382)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13542333)

‎2022 Oct 20
5:48 PM

[9
Kudos](/t5/kudos/messagepage/board-id/erp-blog-members/message-id/66382/tab/all-users "Click here to see who gave kudos to this post.")

4,722

* SAP Managed Tags
* [SAP SuccessFactors Incentive Management](https://community.sap.com/t5/c-khhcw49343/SAP%2520SuccessFactors%2520Incentive%2520Management/pd-p/73555000100800001602)
* [SAP S/4HANA](https://community.sap.com/t5/c-khhcw49343/SAP%2520S%252F4HANA/pd-p/73554900100800000266)
* [SD (Sales and Distribution)](https://community.sap.com/t5/c-khhcw49343/SD%2520%28Sales%2520and%2520Distribution%29/pd-p/209057551571413566377230676804921)
* [SD Sales](https://community.sap.com/t5/c-khhcw49343/SD%2520Sales/pd-p/167431589774684563301227734202839)
* [Settlement Management](https://community.sap.com/t5/c-khhcw49343/Settlement%2520Management/pd-p/9400b307-81e0-4db8-9487-df04dac62aeb)

* [SAP S/4HANA

  SAP S/4HANA](/t5/c-khhcw49343/SAP%2BS%25252F4HANA/pd-p/73554900100800000266)
* [SD (Sales and Distribution)

  Software Product Function](/t5/c-khhcw49343/SD%2B%252528Sales%2Band%2BDistribution%252529/pd-p/209057551571413566377230676804921)
* [SD Sales

  Software Product Function](/t5/c-khhcw49343/SD%2BSales/pd-p/167431589774684563301227734202839)
* [Settlement Management

  Software Product Function](/t5/c-khhcw49343/Settlement%2BManagement/pd-p/9400b307-81e0-4db8-9487-df04dac62aeb)
* [SAP SuccessFactors Incentive Management

  SAP SuccessFactors HCM](/t5/c-khhcw49343/SAP%2BSuccessFactors%2BIncentive%2BManagement/pd-p/73555000100800001602)

View products (5)

Hi there, my name is Thiago Rigo (or just Rigo), I'm SAP S/4HANA OTC & Logistics Solution Architect and I want to share my experience about a requriement related to Commissions setltlement.

The main objective of this post is to share my findings and how I solved the requirement.

**First of all, a little bit about commission process and SAP S/4HANA:**

Commissioning is the process of paying a portion of the sold amount to the sales representative. The company agrees with the sales representative the rules for comission as well as the commission percentage and/or commission method.

In SAP S/4AHANA the solution for commissions is delivered in best practices trough scope item *2TT - Sales Commissions - External Sales Representative* which uses Condition Contract Management (CCM) as solution.

If you are not familiar with the solution I recommend you check the scope item process before going foward this post.

Basically, there are two ways to calculate commission amount:

1. Based on billed amount.

2. Based on fully paid billed amount.

**Here is about what I was challenged:**

In the customer where I'm working for, the business explained that depending on the agreements with the external sales representative, the commission amount must be paid over partial payments, in this case Installment payments.

For example, a SD billing of 300 USD is created on Oct 10, with payment terms of 3 instalments of 100 USD as following:

1. 100 USD on Oct 10;

2. 100 USD on Nov 10;

3. 100,USD on Dec 10.

According to example above and the standard option of commission based on fully paid billed amount, the commission amount would be relevant only after last payment on December.

![](/legacyfs/online/storage/blog_attachments/2022/10/Picture1-60.png)

Figure 1: Standard Process

The requirement is: once any payment is done, the respective paid amount (eg. 100 USD) should be relevant to be commissioned to external sales representative.

![](/legacyfs/online/storage/blog_attachments/2022/10/Picture2-42.png)

Figure 2: Business Requirement

**How to achieve that?**

The condition contract management solution has several configurations, in my investigation and researches, I learned that base amount relevant for commision payment is called “Business Volume” and basically there is a CDS View assigned to commission contract which is responsible for searching data which is base for the business volume.

The business volume profile is assigned to the condition contract type in in the following path:

|
 *IMG > Logistics – General > Settlement Management > Condition Contract Management > Condition Contract Settlement > Specify Settlement Settings for Condition Contract Types* |

![](/legacyfs/online/storage/blog_attachments/2022/10/Picture3-26.png)

Figure 3: Business Volume Profile assignment to Condition Contract Type

And the assignment of the business profile with the CDS View is available on the following SPRO path:

|
 I*MG > Logistics – General > Settlement Management > Condition Contract Management > Condition Contract Settlement > Define and Configure Profiles for Business Volume Determination* |

![](/legacyfs/online/storage/blog_attachments/2022/10/Picture4-28.png)

Figure 4: CDS View assignment to BV

Now checking the CDS view VWB2\_VBRKVBRP\_7 in tcode SE11 we found its respective data definition:

![](/legacyfs/online/storage/blog_attachments/2022/10/Picture5-19.png)

Figure 5: CDS View Data Definition

**Here is the trick:**

It’s possible to create your own CDS View selecting from V\_WB2\_VBRK\_VBRP\_5 and enhance selection with relevant fields to filter only incoming payment amounts by joining fields from CDS View I\_OperationalAcctgDocItem or any other CDS view which has incoming payment data.

In this case I joined fields of Clearing Document and Clearing Date + Posting Key = '15' to find the correponding incoming payment amount.

Ask to your ABAP Developer for developing the CDS View according to business needs.

![](/legacyfs/online/storage/blog_attachments/2022/10/Screenshot_3-1.png)

Figure 6: Creating custom CDS View

Once the new CDS view is done you can assign it to the business volume profile (as mentioned before).

From now, the company will be able settle commissions based on incoming payment amounts which could be partial or fully payments.

**Considerations:**

This solution may works for any other requirement which are not covered by the standard, the CDS View assignment can be changed to another one which solves the issue only by configuration or you may do a small development of new CDS View instead of developing a huge custom report or Fiori app to do ...