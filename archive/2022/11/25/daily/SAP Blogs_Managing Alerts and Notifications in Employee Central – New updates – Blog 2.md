---
title: Managing Alerts and Notifications in Employee Central – New updates – Blog 2
url: https://blogs.sap.com/2022/11/24/managing-alerts-and-notifications-in-employee-central-new-updates-blog-2/
source: SAP Blogs
date: 2022-11-25
fetch_date: 2025-10-03T23:43:51.754777
---

# Managing Alerts and Notifications in Employee Central – New updates – Blog 2

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Enterprise Resource Planning](/t5/enterprise-resource-planning/ct-p/erp)
* [ERP Blog Posts by SAP](/t5/enterprise-resource-planning-blog-posts-by-sap/bg-p/erp-blog-sap)
* Managing Alerts and Notifications in Employee Cent...

Enterprise Resource Planning Blog Posts by SAP

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/erp-blog-sap/article-id/51564&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [Managing Alerts and Notifications in Employee Central - New updates - Blog 2](/t5/enterprise-resource-planning-blog-posts-by-sap/managing-alerts-and-notifications-in-employee-central-new-updates-blog-2/ba-p/13558116)

![Sharath_T_N](https://avatars.profile.sap.com/0/9/id09c35c281ee96dafeadca68d7b6c2d9698f33eb3ee8f6ff07c909020ec2f8753_small.jpeg "Sharath_T_N")

![Product and Topic Expert](/html/@138D6F765B60D7FC0168643DE27D8A68/rank_icons/sap-logo-small-14px.png "Product and Topic Expert")
[Sharath\_T\_N](https://community.sap.com/t5/user/viewprofilepage/user-id/17618)

Product and Topic Expert

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=erp-blog-sap&message.id=51564)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/erp-blog-sap/article-id/51564)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13558116)

‎2022 Nov 24
6:27 PM

[14
Kudos](/t5/kudos/messagepage/board-id/erp-blog-sap/message-id/51564/tab/all-users "Click here to see who gave kudos to this post.")

7,554

* SAP Managed Tags
* [SAP SuccessFactors Employee Central](https://community.sap.com/t5/c-khhcw49343/SAP%2520SuccessFactors%2520Employee%2520Central/pd-p/73555000100800000773)
* [HCM (Human Capital Management)](https://community.sap.com/t5/c-khhcw49343/HCM%2520%28Human%2520Capital%2520Management%29/pd-p/26220882342286075781792349618930)

* [HCM (Human Capital Management)

  Software Product Function](/t5/c-khhcw49343/HCM%2B%252528Human%2BCapital%2BManagement%252529/pd-p/26220882342286075781792349618930)
* [SAP SuccessFactors Employee Central

  SAP SuccessFactors HCM](/t5/c-khhcw49343/SAP%2BSuccessFactors%2BEmployee%2BCentral/pd-p/73555000100800000773)

View products (2)

This blog post introduces you to the SuccessFactors Implementation Design Principle (SFIDP) document: ([Employee Central: Managing Alerts and Notification](https://d.dam.sap.com/a/WEbiYB2)) that was updated a few weeks back. The first blog was written a few years back. This was the [link](https://blogs.sap.com/2020/09/11/managing-alerts-and-notifications-in-employee-central/)

Implementation Design Principle documents are owned and managed by SAP SuccessFactors Product Management who engage and collaborate with select, interested partners along with SAP Professional Service to tap the rich implementation experience distilled in the document after a formalized product review process before broader publication.

![](/legacyfs/online/storage/blog_attachments/2022/11/NEWHP.png)

Major updates in the document are as follows

## Information about “Delete Old Pending alert flag”

The previous document demonstrated the on what is the effect of correcting an existing alert. The new update gives more information on when a new time slice is introduced on the HRIS element like Job information and the value of the field that determines the alert is changed in the new time slice and remains unaltered in the previous time slice.

Copying some parts from the documents.

**Scenario 1: An alert must be sent 1 month before the end of the contract.**

After the alerts job is run the records in the Alert object would be like this. Assume that the job runs on 16- Sep-2021.

|
 **Entity Type** |
 **Name** |
 **Entity Effective Date** |
 **Alert Rule Name** |
 **Alert Effective Date** |

|
 Job Info |
 Geoff Hill |
 15-Sep-2021 |
 ContractRuleEnd |
 15-Aug-2022 |

Now let us add a new time slice in the job information let us say the contract change as the event reasons on 1-Jan-2022 and the new contract end date is 20-Oct -2022. The job information records would look like the table shown below.

|
 **User ID** |
 **Name** |
 **Event Date** |
 **Event Reason** |
 **Contract End Date** |

|
 **88178** |
 Geoff Hill |
 15- Sep-2021 |
 New hire |
 15-Sep-2022 |

|
 **88178** |
 Geoff Hill |
 1-Jan-2022 |
 Contract Change |
 20-Oct-2022 |

After the alerts job is run the records in the Alert object would be like this. Assume that the job runs on 2-Jan-2022.

If “Delete Old Pending alert flag” is set to Yes in the Business Rule, then the row highlighted in yellow will be deleted and only one alert that is the second row will be sent.

|
 **Entity Type** |
 **Name** |
 **Entity Effective Date** |
 **Alert Rule Name** |
 **Alert Effective Date** |

|
 Job Info |
 Geoff Hill |
 15-Sep-2021 |
 ContractRuleEnd |
 15-Aug-2022 -> Deleted |

|
  |
  |
 1-Jan-2022 |
 Contract Change |
 20-Sep-2022 |

If “Delete Old Pending alert flag” is set to No in the Business Rule, then it will send 2 alerts one on 15-Aug and the other on 20-Sep-2022

**Scenario 2 – New time slice and correction.** **An alert must be sent 1 month before the end of the contract.**

|
 **User ID** |
 **Name** |
 **Event Date** |
 **Event Reason** |
 **Contract End Date** |

|
 **88178** |
 Geoff Hill |
 15- Sep-2021 |
 New hire |
 15-Sep-2022 |

After the alerts job is run the records in the Alert object would be like this. Assume that the job runs on 16- Sep-2021.

|
 **Entity Type** |
 **Name** |
 **Entity Effective Date** |
 **Alert Rule Name** |
 **Alert Effective Date** |

|
 Job Info |
 Geoff Hill |
 15-Sep-2021 |
 ContractRuleEnd |
 15-Aug-2022 |

Now the  same recorded is corrected (no time slice is added but the new hire record is corrected) on Dec 1st, 2021. The job runs after this change

|
 **User ID** |
 **Name** |
 **Event Date** |
 **Event Reason** |
 **Contract End Date** |

|
 **88178** |
 Geoff Hill |
 15- Sep-2021 |
 New hire |
 23-Nov-2022 |

The alert entry will look like the one below. This will be corrected (irrespective of the  “Delete Old Pending alert flag” is set to Yes or No)

|
 **Entity Type** |
 **Name** |
 **Entity Effective Date** |
 **Alert Rule Name** |
 **Alert Effective Date** |

|
 Job Info |
 Geoff Hill |
 15-Sep-2021 |
 ContractRuleEnd |
 23-Oct-2022 |

Now let us add a new time slice in the job information let us say the contract change as the event reasons on 1-Jan-2022 and the new contract end date is 1-Dec-2022. The job information records would look like the table shown below.

|
 **User ID** |
 **Name** |
 **Event Date** |
 **Event Reason** |
 **Contract End Date** |

|
 **88178** |
 Geoff Hill |
 15- Sep-2021 |
 New hire |
 23-Nov-2022 |

|
 **88178** |
 Geoff Hill |
 1-Jan-2022 |
 Contract Change |
 01-Dec-2022 |

If “Delete Old Pending alert flag” is set to Yes in the Business Rule, then the row highlighted in yellow will be deleted and only one alert that is in the second row will be sent.

|
 **Entity Type** |
 **Name** |
 **Entity Effective Date** |
 **Alert Rule Name** |
 **Alert Effective Date** |

|
 Job Info |
 Geoff Hill |
 15-Sep-2021 |
 ContractRuleEnd |
 23-Oct-2022 -> Deleted |

|
  |
  |
 1-Jan-2022 |
 Contract Change |
 01-Nov-2022 |

If “Delete Old Pending alert flag” is set to No in the Business Rule, then it will send 2 alerts one on 23-Oct and the other on 01-Nov-2022.

All the scenarios where the...