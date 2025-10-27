---
title: SAP SuccessFactors Employee Central – Facts about Pay Range derivation on Position and Employee objects
url: https://blogs.sap.com/2022/12/04/sap-successfactors-employee-central-facts-about-pay-range-derivation-on-position-and-employee-objects/
source: SAP Blogs
date: 2022-12-05
fetch_date: 2025-10-04T00:31:02.742718
---

# SAP SuccessFactors Employee Central – Facts about Pay Range derivation on Position and Employee objects

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Human Capital Management](/t5/human-capital-management/ct-p/hcm)
* [HCM Blog Posts by Members](/t5/human-capital-management-blog-posts-by-members/bg-p/hcm-blog-members)
* SAP SuccessFactors Employee Central - Facts about ...

Human Capital Management Blog Posts by Members

Explore blogs from customers or SAP partners to gain best practices and fresh insights to succeed.

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/hcm-blog-members/article-id/4512&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [SAP SuccessFactors Employee Central - Facts about Pay Range derivation on Position and Employee objects](/t5/human-capital-management-blog-posts-by-members/sap-successfactors-employee-central-facts-about-pay-range-derivation-on/ba-p/13533921)

![manubhutani](https://avatars.profile.sap.com/c/8/idc8752275f085319c2c3f492d9bd37e9905171603dccbc4482b751bb14bb3cca8_small.jpeg "manubhutani")

[manubhutani](https://community.sap.com/t5/user/viewprofilepage/user-id/17674)

Active Contributor

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=hcm-blog-members&message.id=4512)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/hcm-blog-members/article-id/4512)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13533921)

‎2022 Dec 04
1:51 AM

[5
Kudos](/t5/kudos/messagepage/board-id/hcm-blog-members/message-id/4512/tab/all-users "Click here to see who gave kudos to this post.")

9,227

* SAP Managed Tags
* [SAP SuccessFactors Employee Central](https://community.sap.com/t5/c-khhcw49343/SAP%2520SuccessFactors%2520Employee%2520Central/pd-p/73555000100800000773)
* [SAP SuccessFactors Employee Central Payroll](https://community.sap.com/t5/c-khhcw49343/SAP%2520SuccessFactors%2520Employee%2520Central%2520Payroll/pd-p/67837800100800006744)
* [SAP SuccessFactors Employee Central Payroll, third-party data integration tool](https://community.sap.com/t5/c-khhcw49343/SAP%2520SuccessFactors%2520Employee%2520Central%2520Payroll%252C%2520third-party%2520data%2520integration%2520tool/pd-p/67837800100800007325)
* [HCM Payroll](https://community.sap.com/t5/c-khhcw49343/HCM%2520Payroll/pd-p/372556673030062693282256213775139)

* [SAP SuccessFactors Employee Central Payroll

  SAP SuccessFactors HCM](/t5/c-khhcw49343/SAP%2BSuccessFactors%2BEmployee%2BCentral%2BPayroll/pd-p/67837800100800006744)
* [SAP SuccessFactors Employee Central Payroll, third-party data integration tool

  SAP SuccessFactors HCM](/t5/c-khhcw49343/SAP%2BSuccessFactors%2BEmployee%2BCentral%2BPayroll%25252C%2Bthird-party%2Bdata%2Bintegration%2Btool/pd-p/67837800100800007325)
* [HCM Payroll

  Software Product Function](/t5/c-khhcw49343/HCM%2BPayroll/pd-p/372556673030062693282256213775139)
* [SAP SuccessFactors Employee Central

  SAP SuccessFactors HCM](/t5/c-khhcw49343/SAP%2BSuccessFactors%2BEmployee%2BCentral/pd-p/73555000100800000773)

View products (4)

This article has been written assuming the reader has fair amount of HCM knowledge about Pay ranges. I will not focus on Pay range as an object but will talk more about scenarios around it in SuccessFactors (SF) Employee central (EC). I realized that some information related to this topic is available in bits and pieces at various places, so I planned to write one with detailed insights for the community.

Organizations pay different compensation amounts to employees within same job grade or same job function, hence they establish a range based on market pay rates and set up minimum pay, mid-point pay and the maximum pay for each pay range. Depending upon various factors including employee performance, employee experience etc. the employee compensation is adjusted within the pay range.

SF has inbuilt functions to derive the Pay range depending upon the pay range object configuration in the system. It is very important to understand how Pay range is derived in SF EC so that you follow the correct config steps and then standard functions can do the magic for you. It is suggested to use those functions instead of configuring a custom solution to derive pay range.

As per customer's requirements and scenarios you can create associations of pay range with other objects ex. Legal Entity, Pay grade etc. Since every client is different, hence the requirements are different too. Some derive pay range based upon the Company, Pay grade and Location.

Some clients have complex requirements where pay range is derived based upon not only these standard attributes but other custom attributes as well. Firstly, you have to configure those custom attributes as MDF and then create associations on pay range object.

For each attribute that is required to derive pay range, you must create an association between it and pay range. Since for association you need an object so for custom attributes you must create a custom MDF before creating the association. Let's say you have a requirement to derive pay range based on 5 attributes, out of which 2 are custom. So association in corporate data model will look something like this.

![](/legacyfs/online/storage/blog_attachments/2022/08/PR-association.png)

For standard functions to derive pay range, you must have all these attributes on Position MDF as well as Job Information object. We will discuss more about this later in this article.

* **Let's talk about deriving pay range on the Position object.**

**Step 1**: If your customer has a requirement to derive pay range based on custom attributes also, then create a custom MDF object for each of them.

**Step 2**: Configure these attributes on Position object. Make sure the custom attributes are not of type 'STRING' but 'Generic object' and Valid values source has correct technical name of the custom MDF object.

**Step 3**: Create a Basic business rule with base object "Position' and set the Pay range and its attributes using function *'Get Pay Range by Position'* and *'Get Pay Range attributes'.*Below screenshot can be referred. ![](/legacyfs/online/storage/blog_attachments/2022/08/PR-rule.png)

**Step 4**: Assign this business rule on all attributes (including pay range) associated with pay range.

**Step 5**: Make the visibility of Pay range of Pay range mid, min and max as 'View' on the Position object. As you are deriving these values through a business rule, it makes sense to keep these fields as read only.

**Step 6:**This step is very important if you have configured UI for the position object. In that case you must assign the business rule (from step 3) in the position configuration UI.

![](/legacyfs/online/storage/blog_attachments/2022/12/unit.png)

Now, you are ready to test it on Position object. You can create a new position and update all the attributes. As business rule is assigned on all the attributes so you may see pay range getting derived before populating all the attributes that are required to derive the pay range. This is because the system looks for a pay range which matches all of the configured objects associated with pay range. If some attributes are optional and blank, then system will derive the pay range accordingly. Hence, it is very important that you configure and sequence these attributes (based on which pay range should be derived) on pay range object correctly. For ex. if pay range is derived based on 4 attributes and only first is po...