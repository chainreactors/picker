---
title: S/4HANA Business Partner BDT configuration comparison between clients
url: https://blogs.sap.com/2022/12/02/s-4hana-business-partner-bdt-configuration-comparison-between-clients/
source: SAP Blogs
date: 2022-12-03
fetch_date: 2025-10-04T00:23:44.985081
---

# S/4HANA Business Partner BDT configuration comparison between clients

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Enterprise Resource Planning](/t5/enterprise-resource-planning/ct-p/erp)
* [ERP Blog Posts by SAP](/t5/enterprise-resource-planning-blog-posts-by-sap/bg-p/erp-blog-sap)
* S/4HANA Business Partner BDT configuration compari...

Enterprise Resource Planning Blog Posts by SAP

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/erp-blog-sap/article-id/52379&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [S/4HANA Business Partner BDT configuration comparison between clients](/t5/enterprise-resource-planning-blog-posts-by-sap/s-4hana-business-partner-bdt-configuration-comparison-between-clients/ba-p/13563488)

![Andi_M](https://avatars.profile.sap.com/3/a/id3a5d140ec7baa422d46629af5881b8299f397cf27a68241232baf1edaa302e7d_small.jpeg "Andi_M")

![Product and Topic Expert](/html/@138D6F765B60D7FC0168643DE27D8A68/rank_icons/sap-logo-small-14px.png "Product and Topic Expert")
[Andi\_M](https://community.sap.com/t5/user/viewprofilepage/user-id/181182)

Product and Topic Expert

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=erp-blog-sap&message.id=52379)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/erp-blog-sap/article-id/52379)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13563488)

‎2022 Dec 02
6:49 PM

[4
Kudos](/t5/kudos/messagepage/board-id/erp-blog-sap/message-id/52379/tab/all-users "Click here to see who gave kudos to this post.")

2,618

* SAP Managed Tags
* [SAP S/4HANA](https://community.sap.com/t5/c-khhcw49343/SAP%2520S%252F4HANA/pd-p/73554900100800000266)
* [APP PLATFORM Business Partner](https://community.sap.com/t5/c-khhcw49343/APP%2520PLATFORM%2520Business%2520Partner/pd-p/397511424400755828374365287279243)
* [SAP S/4HANA Cloud Private Edition](https://community.sap.com/t5/c-khhcw49343/SAP%2520S%252F4HANA%2520Cloud%2520Private%2520Edition/pd-p/5c26062a-9855-4f39-8205-272938b6882f)

* [SAP S/4HANA

  SAP S/4HANA](/t5/c-khhcw49343/SAP%2BS%25252F4HANA/pd-p/73554900100800000266)
* [APP PLATFORM Business Partner

  Software Product Function](/t5/c-khhcw49343/APP%2BPLATFORM%2BBusiness%2BPartner/pd-p/397511424400755828374365287279243)
* [SAP S/4HANA Cloud Private Edition

  SAP S/4HANA Cloud](/t5/c-khhcw49343/SAP%2BS%25252F4HANA%2BCloud%2BPrivate%2BEdition/pd-p/5c26062a-9855-4f39-8205-272938b6882f)

View products (3)

At BP transaction in your S/4HANA system you might notice that some descriptions of tabs, sections etc. are not correct or missing. That could happen in some cases where you convert your ECC system into a S/4HANA system. Another case could be after setting up a new client.

SAP offers a comparison tool to compare 2 clients in regards of BDT settings and offers the user the opportunity to include the differences in a transport that can then be sent to the new client.

This blog is relevant for all releases working with Business Partner, meaning ECC 6.0 onwards. Main focus is SAP S/4HANA on-premise and private cloud edition, which is the most relevant working with Business Partner.

# Starting Point

Screenshot below shows wrong descriptions at a screen (tab) and a screen section. Target at this example is to compare the BDT setup of screenshot client (target client) with BDT setup of standard delivery client 000 (source client) to correct wrong descriptions. Source or target client could be any client in your system.

![](/legacyfs/online/storage/blog_attachments/2022/12/01.png)

# Run comparison tool

## Requirements

An RFC connection must be established between the two desired clients.

## Selection screen

Run Transaction BDT\_COMPARE or execute program BDT\_COMPARE at **source** client.

![](/legacyfs/online/storage/blog_attachments/2022/12/02.png)

|
 **Field Name** |
 **Description** |
 **Comment/Action** |

|
 RFC Destination |
 Name of RFC Connection |
 Type in the name of the RFC connection or use the drop down to receive a list of all RFC connections. |

|
 Application Object |
 The Object you wish to do a comparison on. |
 Type in the Application object for which you want to produce a comparison of BDT customizing tables.    most relevant objects:    * BUPA - SAP Business Partner  * BUPR - SAP Business Partner: Partner Relationships |

|
 Applications |
 These fields limit the applications within an application object that will be check. |
 If you do not want a full comparison of the Application object, use these field to limit the comparison to only those applications you would like checked. |

|
 Cross-Application Settings |
 Check box to include BDT customizing that covers Cross-Application settings. |
 Check Cross-Application Settings. |

|
 Customizing Tables |
 Check Box to include customizing tables |
 Check Customizing tables |

|
 Language |
 Language for description texts |
 leave blank to compare all languages |

|
 Display the Same |
 Check Box to include customizing settings that are identical in both clients |
 Check if you would like to view those items that are the same in both clients. This box or one of the 4 that follows it must be checked, that is why this is listed as conditional.    I would not recommend checking this box. It is likely to produce a very long list. Since  this program is usually used to detect differences, there will not usually be any added value to checking this box. |

|
 Display Different |
 Check Box to include customizing settings that are different between the two clients being compared. |
 Since you are usually running this program to identify differences, you would usually check this box.    Check if you would like to view those items that are the difference between the two clients being compared. This box or one of the 4 other boxes it is group with must be checked, that is why this is listed as conditional. |

|
 Display existing fr source sys |
 Check Box to display table entries that only exit in the Source System. |
 Since you are usually running this program to identify differences, you would usually check this box    Check this box if you would like to see entries that only exits only in the source system. This box or one of the 4 other boxes it is group with must be check, that is why this is listed as conditional. |

|
 Display existing fr target sys |
 Check Box to display table entries that only exit in the Target System |
 Check this box if you would like to see entries that only exits only in the target system. This box or one of the 4 other boxes in it's group with must be check, that is why this is listed as conditional. |

After execution you will see the result list.

## Comparison result

![](/legacyfs/online/storage/blog_attachments/2022/12/03.png)

Result list is splitted into 3 areas - only two are shown at my example.

### Red entries

There are the same key entries in customizing tables at both clients but with different configuration.

### Yellow entries

There are key entries in customizing tables in target system only.

At target client there is one custom field at BP transaction (KNA1-ZCUST) which is not implemented at source client (000). The reason for many lines just for one custom field implementation is caused by BDT configuration settings of Field Group and View configuration and assignment.

Custom field implementation is described at this [blog post](https://blogs.sap.com/2019/11/07/sap-s-4hana-business-partner-fie...