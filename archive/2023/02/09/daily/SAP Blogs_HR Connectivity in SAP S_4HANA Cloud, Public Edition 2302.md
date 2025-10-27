---
title: HR Connectivity in SAP S/4HANA Cloud, Public Edition 2302
url: https://blogs.sap.com/2023/02/08/hr-connectivity-in-sap-s-4hana-cloud-public-edition-2302/
source: SAP Blogs
date: 2023-02-09
fetch_date: 2025-10-04T06:07:13.375427
---

# HR Connectivity in SAP S/4HANA Cloud, Public Edition 2302

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Enterprise Resource Planning](/t5/enterprise-resource-planning/ct-p/erp)
* [ERP Blog Posts by SAP](/t5/enterprise-resource-planning-blog-posts-by-sap/bg-p/erp-blog-sap)
* HR Connectivity in SAP S/4HANA Cloud, Public Editi...

Enterprise Resource Planning Blog Posts by SAP

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/erp-blog-sap/article-id/52742&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [HR Connectivity in SAP S/4HANA Cloud, Public Edition 2302](/t5/enterprise-resource-planning-blog-posts-by-sap/hr-connectivity-in-sap-s-4hana-cloud-public-edition-2302/ba-p/13565572)

![former_member57128](https://avatars.profile.sap.com/former_member_small.jpeg "former_member57128")

[former\_member57128](https://community.sap.com/t5/user/viewprofilepage/user-id/57128)

Explorer

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=erp-blog-sap&message.id=52742)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/erp-blog-sap/article-id/52742)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13565572)

‎2023 Feb 08
8:04 PM

[2
Kudos](/t5/kudos/messagepage/board-id/erp-blog-sap/message-id/52742/tab/all-users "Click here to see who gave kudos to this post.")

2,297

* SAP Managed Tags
* [RISE with SAP](https://community.sap.com/t5/c-khhcw49343/RISE%2520with%2520SAP/pd-p/1e76886f-86ac-4839-9833-8bf95f5eb775)
* [SAP S/4HANA Cloud Public Edition Human Resources](https://community.sap.com/t5/c-khhcw49343/SAP%2520S%252F4HANA%2520Cloud%2520Public%2520Edition%2520Human%2520Resources/pd-p/a8945cb2-dac7-490c-a6b6-7d8629f65668)
* [SAP S/4HANA](https://community.sap.com/t5/c-khhcw49343/SAP%2520S%252F4HANA/pd-p/73554900100800000266)
* [SAP S/4HANA Cloud Public Edition](https://community.sap.com/t5/c-khhcw49343/SAP%2520S%252F4HANA%2520Cloud%2520Public%2520Edition/pd-p/08e2a51b-1ce5-4367-8b33-4ae7e8b702e0)

* [SAP S/4HANA Cloud Public Edition

  SAP S/4HANA Cloud](/t5/c-khhcw49343/SAP%2BS%25252F4HANA%2BCloud%2BPublic%2BEdition/pd-p/08e2a51b-1ce5-4367-8b33-4ae7e8b702e0)
* [RISE with SAP

  Topic](/t5/c-khhcw49343/RISE%2Bwith%2BSAP/pd-p/1e76886f-86ac-4839-9833-8bf95f5eb775)
* [SAP S/4HANA

  SAP S/4HANA](/t5/c-khhcw49343/SAP%2BS%25252F4HANA/pd-p/73554900100800000266)
* [SAP S/4HANA Cloud Public Edition Human Resources

  Additional Software Product](/t5/c-khhcw49343/SAP%2BS%25252F4HANA%2BCloud%2BPublic%2BEdition%2BHuman%2BResources/pd-p/a8945cb2-dac7-490c-a6b6-7d8629f65668)

View products (4)

Hi SAP S/4HANA Cloud, public edition community,

welcome to this blog post which will cover the release of SAP S/4HANA Cloud, public edition 2302 focusing on HR Connectivity. Watch the video below to get a crisp overview of the highlight for this release:

### “Worker Overview” App

With the new “Worker Overview” app you benefit from improved performance and search functionality, as it is a complete redesign of how workforce data is displayed in SAP S/4HANA Cloud, public edition. The new “Worker Overview” app replaces the “Employee Fact Sheet” and delivers the same look and feel as the SAP Fiori “Manage Workforce” app.

The SAP Help Portal: [Worker Overview | SAP Help Portal](https://help.sap.com/docs/SAP_S4HANA_CLOUD/a630d57fc5004c6383e7a81efee7a8bb/352f5e4c5dd74be8b2cfb6f372c3390c.html?q=Worker%20Overview) offers you detailed information about the “Worker Overview” app, such as:

* A complete description of the “Worker Overview” app, including a video: [SAP S/4HANA Cloud - Worker Overview (kaltura.com)](https://cdnapisec.kaltura.com/html5/html5lib/v2.98/mwEmbedFrame.php/p/1921661/uiconf_id/37285991/entry_id/1_jvmb7j7a?wid=_1921661&iframeembed=true&playerId=kaltura_player&entry_id=1_jvmb7j7a) that shows you what you can display and view in the “Worker Overview” app.

* Authorizations for the “Worker Overview” app, as you can view different worker data depending on the assigned business catalogs.

* A feature comparison for the “Worker Overview” app and the “Employee Fact Sheet”.

Besides the new “Worker Overview” app, there are three enhanced functionalities around the “Manage Workforce” app that I’d like to introduce you to:

### “Entry Source” Field

The new “Entry Source” field is from now on available in the “Manage Workforce” and the new “Worker Overview” app.

With the help of the “Entry Source” field you can find out where the data was initially entered.

Worker data which has been entered via SAP SuccessFactors can't be changed in the “Manage Workforce” app, it can only be edited in the source system itself to avoid inconsistencies.

Here, you find the different options:

![](/legacyfs/online/storage/blog_attachments/2023/02/entry-field.png)

Please note that from now on data can be imported and maintained in the “Manage Workforce” app even if the SAP S/4HANA Cloud, public edition system is integrated with external HR system.

### “Rehire” Process

With the second enhancement, the new “Rehire” process, it is possible to rehire a worker who has previously worked at the company. The existing work agreement is kept as a record. A new work agreement with a new ID is created.

You can either rehire a worker with the same worker type, for example, rehire an employee as an employee or rehire with a different worker type, for example, rehire an employee as a contingent worker.

There are two “Rehire” scenarios to mention:

* Scenario1: Change in Country/Company Code:

In case of transfer it is recommended that existing workforce assignment is terminated and the workforce person is rehired with a new employment. If this is not done then the available filter options such as company, country, worker type to exclude data from the replication are not supported.

* Scenario 2: Conversion from Contingent Worker to Workforce Person or Vice Versa:

In case of conversion scenario, it is mandatory to rehire the workforce person with new employment. The rehiring of same employment is not supported.

### “Outbound Integration of locally maintained Workforce Data”

The third innovation, the "Outbound Integration of locally maintained Workforce Data", enables customers to distribute the Workforce data, that is locally maintained in SAP S/4HANA Cloud, public edition (for example via the 'Manage Workforce' app) across their landscape utilizing SAP Master Data Integration and by using SAP One Domain Model.

Finally I'd like to make you aware that we have a brand new microlearning in place:

### [Manage Workforce App – SAP **S/4HANA** Cloud, Public Edition](https://microlearning.opensap.com/media/Manage%2BWorkforce%2BApp%2B-%2BSAP%2BS%2B4HANA%2BCloud%2C%2BPublic%2BEdition/1_wyobx4l8)

It is designed specifically for user administrators and those involved in user management. The video provides an overview and system demo of the Manage Workforce app’s functions, including navigation, worker creation, and worker maintenance. You can learn about the essential prerequisites and how to create workers directly in the app, edit employment data, and assign the necessary business catalog to your business role.

**For more information on SAP S/4HANA Cloud, public edition check out the following links:**

* SAP S/4HANA Cloud, Public Edition Release Info [Here](https://community.sap.com/topics/s4hana-cloud/product-releases)

* SAP S/4HANA Cloud, Public Edition for Human Resources [Topic Page](ht...