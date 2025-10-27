---
title: Using Custom MDF objects for Employee Class and Employment Type
url: https://blogs.sap.com/2023/06/07/using-custom-mdf-objects-for-employee-class-and-employment-type/
source: SAP Blogs
date: 2023-06-08
fetch_date: 2025-10-04T11:47:20.692261
---

# Using Custom MDF objects for Employee Class and Employment Type

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Human Capital Management](/t5/human-capital-management/ct-p/hcm)
* [HCM Blog Posts by Members](/t5/human-capital-management-blog-posts-by-members/bg-p/hcm-blog-members)
* Using Custom MDF objects for Employee Class and Em...

Human Capital Management Blog Posts by Members

Explore blogs from customers or SAP partners to gain best practices and fresh insights to succeed.

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/hcm-blog-members/article-id/4909&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [Using Custom MDF objects for Employee Class and Employment Type](/t5/human-capital-management-blog-posts-by-members/using-custom-mdf-objects-for-employee-class-and-employment-type/ba-p/13553880)

![juliamaisch](https://avatars.profile.sap.com/3/6/id3686c080a5268f29b59fd86b44968845d026f52e843db7b16c0b1490de3a1e4f_small.jpeg "juliamaisch")

[juliamaisch](https://community.sap.com/t5/user/viewprofilepage/user-id/24460)

Discoverer

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=hcm-blog-members&message.id=4909)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/hcm-blog-members/article-id/4909)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13553880)

‎2023 Jun 07
10:57 PM

[9
Kudos](/t5/kudos/messagepage/board-id/hcm-blog-members/message-id/4909/tab/all-users "Click here to see who gave kudos to this post.")

7,200

* SAP Managed Tags
* [SAP SuccessFactors Employee Central](https://community.sap.com/t5/c-khhcw49343/SAP%2520SuccessFactors%2520Employee%2520Central/pd-p/73555000100800000773)
* [SAP SuccessFactors HCM Suite](https://community.sap.com/t5/c-khhcw49343/SAP%2520SuccessFactors%2520HCM%2520Suite/pd-p/67838200100800004730)
* [Cloud Integration](https://community.sap.com/t5/c-khhcw49343/Cloud%2520Integration/pd-p/67837800100800006801)

* [SAP SuccessFactors HCM Suite

  SAP SuccessFactors HCM](/t5/c-khhcw49343/SAP%2BSuccessFactors%2BHCM%2BSuite/pd-p/67838200100800004730)
* [Cloud Integration

  SAP Integration Suite](/t5/c-khhcw49343/Cloud%2BIntegration/pd-p/67837800100800006801)
* [SAP SuccessFactors Employee Central

  SAP SuccessFactors HCM](/t5/c-khhcw49343/SAP%2BSuccessFactors%2BEmployee%2BCentral/pd-p/73555000100800000773)

View products (3)

I have seen requirements where Employee Class and Employment Type picklist functionalities were not meeting customer requirements.

This blog describes the solution to set up complex validation combinations between Employee Class and Employment Type. While SAP standard configuration provides these fields as picklists, due to which different combinations of validations cannot be used for e.g., some Employee Class values can only be used in certain Legal Entities, or some Employment Types can only be used in combination with certain Employee Class values as well as within certain Legal Entities.

The fields Employee Class and Employment Type in Job Information are usually used to be able to classify employees. If Employee Central is integrated with SAP HCM, fields used are IT0001-PERSG and IT0001-PERSK.

Below is the configuration to achieve these requirements in Employee Central as well as to make sure, that the integration to SAP HCM is working as expected.

To meet these requirements, configure two custom MDF objects for Employee Class and Employment Type, including needed associations.

Create a custom MDF object for Employee Class in “Configure Object Definition”:

![](/legacyfs/online/storage/blog_attachments/2023/06/PIC-1-Configure-Object-Definition-Employee-Class.png)

Configure Object Definition Employee Class

Including the following association and security permissions:

![](/legacyfs/online/storage/blog_attachments/2023/06/PIC-2-Object-Settings-Employee-Class.png)

Object Settings Employee Class

View in "Manage Data":

![](/legacyfs/online/storage/blog_attachments/2023/06/PIC-3-Manage-Data-Employee-Class.png)

Manage Data Employee Class

Create a custom MDF object for Employment Type in “Configure Object Definition”:

![](/legacyfs/online/storage/blog_attachments/2023/06/PIC-4-Configure-Object-Definition-Employment-Type-1.png)

Configure Object Definition Employment Type

Including the following associations and security permissions:

![](/legacyfs/online/storage/blog_attachments/2023/06/PIC-5-Object-Settings-Employment-Type.png)

Object Settings Employment Type

View in "Manage Data":

![](/legacyfs/online/storage/blog_attachments/2023/06/PIC-6-Manage-Data-Employment-Type.png)

Manage Data Employment Type

If you are wondering how to configure a custom MDF object, please refer to [this link](https://userapps.support.sap.com/sap/support/knowledge/en/2285199).

Create two custom fields in job information to add the fields in “Manage Business Configuration":

![](/legacyfs/online/storage/blog_attachments/2023/06/PIC-7-Manage-Business-Configuration-Job-Information.png)

Manage Business Configuration - Job Information

Including the association configuration:

![](/legacyfs/online/storage/blog_attachments/2023/06/PIC-8-Field-Settings-Employee-Class.png)

Field Settings Employee Class

![](/legacyfs/online/storage/blog_attachments/2023/06/PIC-9-Field-Settings-Employment-Type.png)

Field Settings Employment Type

From an HCM integration point of view, using custom MDF objects for Employee Class (Employee Group/Mitarbeitergruppe) and Employment Type (Employee Sub-Group/Mitarbeiterkreis) in SuccessFactors ensures that only valid combinations are replicated into SAP HCM. So e.g., a certain Employment Type can only be chosen in combination with defined Employee Class as well as e.g., with defined country (or Legal Entity). The mapping of the objects can be done analog to the mapping of picklist values. There is no additional effort in the standard BIB mapping.

![](/legacyfs/online/storage/blog_attachments/2023/06/PIC-10-HCM.png)

HCM

For further information about Business Integration Builder (BIB), please refer to [this link](https://blogs.sap.com/2018/10/03/business-integration-builder-bib-knowledge/) or [the Replicating Employee Master Data from Employee Central to SAP ERP HCM Guide](https://help.sap.com/doc/3786491995e945fdb3c8ebfcfdbed626/2205/en-US/SF_EC_ERP_EE_Data_HCI_en-US.pdf).

Please be aware, that standard Employee Class SuccessFactors picklist field can be used as filter in HCM replication. To ensure, that this functionality can still be used, configure a picklist field on Employee Class object with Employee Class standard picklist.

![](/legacyfs/online/storage/blog_attachments/2023/06/PIC-11-Employee-Class-Picklist.png)

Employee Class Picklist

Additionally, enable standard Employee Class picklist field in Job Info and use a business rule to set the value automatically depending on object field, e.g., like this:

![](/legacyfs/online/storage/blog_attachments/2023/06/PIC-12-Business-Rule.png)

Business Rule

With this configuration, you can choose Employee Class and Employment Type flexibly and at the same time make sure, that only allowed combinations can be chosen. Other benefits are e.g., the simplification of reporting on Employee Class and Employment Type as well as using both fields as permission group filters.

Hope this gave a nice information, and you enjoyed this blog! Please feel free to leave a comment or question below.

1 Comment

You must be a reg...