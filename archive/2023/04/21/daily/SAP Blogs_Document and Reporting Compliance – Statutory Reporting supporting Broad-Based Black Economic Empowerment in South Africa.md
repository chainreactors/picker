---
title: Document and Reporting Compliance – Statutory Reporting supporting Broad-Based Black Economic Empowerment in South Africa
url: https://blogs.sap.com/2023/04/20/document-and-reporting-compliance-statutory-reporting-supporting-broad-based-black-economic-empowerment-in-south-africa/
source: SAP Blogs
date: 2023-04-21
fetch_date: 2025-10-04T11:34:19.918039
---

# Document and Reporting Compliance – Statutory Reporting supporting Broad-Based Black Economic Empowerment in South Africa

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Technology](/t5/technology/ct-p/technology)
* [Technology Blog Posts by SAP](/t5/technology-blog-posts-by-sap/bg-p/technology-blog-sap)
* Document and Reporting Compliance – Statutory Repo...

Technology Blog Posts by SAP

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/technology-blog-sap/article-id/164962&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [Document and Reporting Compliance – Statutory Reporting supporting Broad-Based Black Economic Empowerment in South Africa](/t5/technology-blog-posts-by-sap/document-and-reporting-compliance-statutory-reporting-supporting-broad/ba-p/13571150)

![Alois](https://avatars.profile.sap.com/4/7/id4717ce4d05d6b7436bfcc4504141ccbc26b7f7235c0f404d62b8c43b78e4a854_small.jpeg "Alois")

![Product and Topic Expert](/html/@138D6F765B60D7FC0168643DE27D8A68/rank_icons/sap-logo-small-14px.png "Product and Topic Expert")
[Alois](https://community.sap.com/t5/user/viewprofilepage/user-id/13519)

Product and Topic Expert

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=technology-blog-sap&message.id=164962)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/technology-blog-sap/article-id/164962)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13571150)

‎2023 Apr 21
12:34 AM

[5
Kudos](/t5/kudos/messagepage/board-id/technology-blog-sap/message-id/164962/tab/all-users "Click here to see who gave kudos to this post.")

2,258

* SAP Managed Tags
* [SAP Document and Reporting Compliance](https://community.sap.com/t5/c-khhcw49343/SAP%2520Document%2520and%2520Reporting%2520Compliance/pd-p/73554900100700003181)

* [SAP Document and Reporting Compliance

  Software Product](/t5/c-khhcw49343/SAP%2BDocument%2Band%2BReporting%2BCompliance/pd-p/73554900100700003181)

View products (1)

### Why is there such kind of law?

Broad-Based Black Economic Empowerment (B-BBEE) got introduced in Government Gazette on 9th of January 2004 and amended with Codes of Good Practice in the course of time.

By introducing B-BBEE South African government took affirmative action to overcome economic legacy of apartheid and foster meaningful economic participation of all persons and communities across the country.

### How to measure black empowerment?

Simply speaking B-BBEE measures black empowerment by introducing a generic scorecard comprising of the following priority elements according to Codes of Good Practice.

* **Ownership** element measures effective ownership of entities by black people (with special focus on black women, cooperatives, workers, and communities).

* **Management** **Control** element measures effective control of entities by black people.

* **Skills** **Development** element measures the extent to which employers carry out initiatives designed to develop the competencies of black employees and black people.

* **Enterprise and Supplier Development** element measures the extent to which entities buy goods and services from empowering suppliers with strong B-BBEE recognition levels.

* **Socio-Economic Development** element measures the extent to which entities carry out initiatives that promote access to economy for black people.

It is important to mention the so-called B-BBEE recognition level here. The better an entity is measured against the before mentioned elements, the better the B-BBEE recognition level will be for the duration of 1 year.

B-BBEE recognition will be assessed in a verification process and the result will be a certificate.

There are several sector scorecards available in the meanwhile. Thus, get in contact with your customers or colleagues from business department to ask your company’s scorecard requirements and maybe certificate as reference.

First Code of Good Practice was published in Government Gazette / Staatskoerant No. 36928 from 11th of October 2013.
[36928\_11-10\_TradeInd\_Layout 1 (gazettes.africa)](https://gazettes.africa/archive/za/2013/za-government-gazette-dated-2013-10-11-no-36928.pdf)

### How does SAP help here?

Document and Reporting Compliance – Statutory Reporting (DRC) provides a report to support customers when measuring the Enterprise and Supplier Development.

To do so DRC combines vendor master data with classification representing the vendor’s scorecard certificate selecting supplier’s business volume accordingly.

Thus, there is business data-based evidence to which extend business has been done with empowering suppliers. The idea behind: The more companies do business with empowering suppliers the better will be their B-BBEE recognition level in next verification, which will motivate other companies to choose them as suppliers to increase their own B-BBEE recognition level.

Therefore, you would want to check on a regular basis which suppliers you can choose to improve or keep your scorecard recognition in next verification assessment.

![](/legacyfs/online/storage/blog_attachments/2023/04/Picture1-16.png)

Output of DRC report BBBEE Supplier Classification (RZA\_BBBEE\_CLFN)

### Where do data of this report come from?

You would want to check following settings in the system.

#### a) Vendor class with characteristics (App “Manage Classes” or transaction CL02)

Define a vendor class type 10 with characteristics representing the elements or criteria of Supplier and Enterprise Development scorecard as defined in Code of Good Practice.

![](/legacyfs/online/storage/blog_attachments/2023/04/Picture2-14.png)

Characteristics of class BBBEE (Best practice S/4HANA Cloud, public edition)

#### b) Characteristic values (App “Manage Characteristics" or transaction CT04)

Characteristics values represent the possible scorecard values as per Code of Good Practice. They are visible on vendor’s B-BBEE recognition level certificate.

![](/legacyfs/online/storage/blog_attachments/2023/04/Picture3-16.png)

Characteristic values of class BBBEE (Best practice S/4HANA Cloud, public edition)

#### c) Assignment of class to vendors (App “Manage Class Assignment” or transaction CL24N)

Vendors must be assigned to class representing B-BBEE.

![](/legacyfs/online/storage/blog_attachments/2023/04/Picture4-13.png)

Class assigned to vendors (Best Practice S/4HANA Cloud, public edition)

#### d) Assignment of characteristic values in vendor master data (App “Maintain Business Partner” or transaction BP)

Open business partner master data and choose role “Supplier (Fin. Accounting)”.
Choose Extras/Classification in menu bar.
Assign values as per vendor’s B-BBEE recognition level certificate.

![](/legacyfs/online/storage/blog_attachments/2023/04/Picture5-9.png)

Characteristic values assigned to vendor (Best Practice S/4HANA Cloud, public edition)

#### e) Run statutory reporting (App “Run Statutory Reports”)

Choose report RZA\_BBBEE\_CLFN “South Africa BBBEE Supplier Classification” and Reporting Period to launch a new report run.

![](/legacyfs/online/storage/blog_attachments/2023/04/Picture6-8.png)

Reporting periods of report RZA\_BBBEE\_CLFN (Best Practice S/4HANA Cloud, public edition)

Choose button “New Run”.
Choose button “Refresh” until Report Run Status changes into “Generated Successfully”.
Choose report run.

![](/legacyfs/online/storage/blog_attachments/2023/04/Picture7-8.png)

Run details of report RZA\_BBBEE\_CLFN (Best Practice S/4HANA Cloud, public edit...