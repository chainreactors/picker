---
title: CPI Message Processing Report
url: https://blogs.sap.com/2023/08/03/cpi-message-processing-report/
source: SAP Blogs
date: 2023-08-04
fetch_date: 2025-10-04T12:01:49.518706
---

# CPI Message Processing Report

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Technology](/t5/technology/ct-p/technology)
* [Technology Blog Posts by Members](/t5/technology-blog-posts-by-members/bg-p/technology-blog-members)
* CPI Message Processing Report

Technology Blog Posts by Members

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/technology-blog-members/article-id/162250&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [CPI Message Processing Report](/t5/technology-blog-posts-by-members/cpi-message-processing-report/ba-p/13562348)

![Jayesh8909](https://avatars.profile.sap.com/5/4/id54422bf727f25ce08b7559a7f4808eccbf9ef6e14b782680d5daa0fb2f06a87c_small.jpeg "Jayesh8909")

[Jayesh8909](https://community.sap.com/t5/user/viewprofilepage/user-id/152626)

Explorer

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=technology-blog-members&message.id=162250)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/technology-blog-members/article-id/162250)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13562348)

‎2023 Aug 03
7:17 PM

[5
Kudos](/t5/kudos/messagepage/board-id/technology-blog-members/message-id/162250/tab/all-users "Click here to see who gave kudos to this post.")

7,952

* SAP Managed Tags
* [SAP Integration Suite](https://community.sap.com/t5/c-khhcw49343/SAP%2520Integration%2520Suite/pd-p/73554900100800003241)
* [Cloud Integration](https://community.sap.com/t5/c-khhcw49343/Cloud%2520Integration/pd-p/67837800100800006801)

* [Cloud Integration

  SAP Integration Suite](/t5/c-khhcw49343/Cloud%2BIntegration/pd-p/67837800100800006801)
* [SAP Integration Suite

  SAP Integration Suite](/t5/c-khhcw49343/SAP%2BIntegration%2BSuite/pd-p/73554900100800003241)

View products (2)

## Introduction:

SAP is widely used ERP solution in the world, and it provides number of solutions for a smooth business process, I have been part of many project assignments and one concern I have faced during all my assignments is clients or user requesting **CPI message processing data** so that they don't have to rely on a CPI resource.

## Solution:

In CPI, usually business or client wants to check what message has been processed and which one failed but unfortunately CPI monitoring cannot provide them a tabular view of all the messages and their respective status.

Since we had faced this issue, we have created a simple solution to generate a excel report which contains interface name, status and failure reason.

There are other blogs available on **message processing report**, but they are only displaying count of success and failure message, while **this blog helps you to create a report with detailed information**.

## Relevance:

This article is helpful for people who are supporting SAP CPI projects as it reduces manual monitoring effort and also creating a simple sheet that clients and businesses can also understand and hence reduces the effort.

## Background:

SAP has provided APIs to fetch CPI message processing data, to generate our report we have to call multiple APIs, we need to pass value from one API response to another API call and then we will convert the data into CSV or excel format and send it out as an email attachment.

## Integration Scenario Details

Receiver Adapter Configuration:

|
 Protocol |
 OData |

|
 Address |
 Tenant URL/api/v1/ |

|
 Authentication |
 Basic |

|
 Protocol |
 HTTP |

|
 Address |
 Tenant URL/api/v1/MessageProcessingLogs('${property.GUID}')/ErrorInformation/$value |

|
 Authentication |
 Basic |

|
 Protocol |
 Mail |

|
 Address |
 SMTP address |

|
 Authentication |
 Basic/None |

|
  |
  |

## IFLOW Design

![](/legacyfs/online/storage/blog_attachments/2023/07/img1-1.png)

**Steps to be performed in Main Iflow**

1. **Start Timer:** It can be scheduled for the time you want to generate the report.

2. **Content Modifier:** to create property “**to and from date** “for Odata query.

**![](/legacyfs/online/storage/blog_attachments/2023/07/img2-2.png)**

3. **Request Reply:** To handle response from OData call

4. **OData Adapter:** To fetch CPI logs for respective tenant based on filter query

Query: $select=LogStart,LogEnd,MessageGuid,IntegrationFlowName,Status,IntegrationArtifact&$filter=LogStart ge datetime'${property.FromDate}' and LogEnd le datetime'${property.ToDate}' and Status ne 'DISCARDED'

![](/legacyfs/online/storage/blog_attachments/2023/07/img3-1.png)

![](/legacyfs/online/storage/blog_attachments/2023/07/img4-1.png)

5. **General splitter:** To split Records into individual record.

**![](/legacyfs/online/storage/blog_attachments/2023/07/img5-1.png)**

6. **Router:** Two paths created in router, 1 for CPI message with failed status and 2 for all the other statuses

**![](/legacyfs/online/storage/blog_attachments/2023/07/img6-1.png)**

**Steps for failed route path**

* **Content modifier:** to add all the required field for report added as a property

**![](/legacyfs/online/storage/blog_attachments/2023/07/img7-1.png)**

* **Request Reply:** To handle response from HTTP Call

* **HTTP Adapter:** To fetch error detail of a failed message using Message GUID

**![](/legacyfs/online/storage/blog_attachments/2023/07/img8-1.png)**

* **Groovy Script:** To create a CSV file with Iflow name, Message ID, Start time, End time, status and error details

**![](/legacyfs/online/storage/blog_attachments/2023/07/img9.png)**

**Steps for Default Route**

* **Content modifier:** to add all the required field for report added as a property

**![](/legacyfs/online/storage/blog_attachments/2023/07/img10.png)**

* **Groovy Script:** To create a CSV file with Iflow name, Message ID, Start time, End time, status

**![](/legacyfs/online/storage/blog_attachments/2023/07/img11.png)**

7. **Gather:** To gather all records from both failed and default route to create a single CSV file![](/legacyfs/online/storage/blog_attachments/2023/07/img12.png)

8. **Content Modifier:** To add custom CSV header

**![](/legacyfs/online/storage/blog_attachments/2023/07/img13.png)**

9. **Send:** To be use for mail adapter to send the mail.

10. **Mail Adapter:** To trigger a mail to respective people with Body as an attachment.![](/legacyfs/online/storage/blog_attachments/2023/07/img14.png)

11. **Write Variable:** To create a local variable which will hold last execution date, so that when iflow runs next time it will only fetch details after last run.![](/legacyfs/online/storage/blog_attachments/2023/07/img15.png)

**Excel:**

![](/legacyfs/online/storage/blog_attachments/2023/07/img16.png)

Hope this blog helps you to understand the use of SAP CPI APIs and to create a proper report.

4 Comments

You must be a registered user to add a comment. If you've already registered, sign in. Otherwise, register and sign in.

* [Comment](/plugins/common/feature/oidcss/sso_login_redirect/providerid/sap_ids_prompt?redirectreason=permissiondenied&referer=https%3A%2F%2Fcommunity.sap.com%2Ft5%2Ftechnology-blog-posts-by-members%2Fcpi-message-processing-report%2Fba-p%2F13562348%23comment-on-this)

Copy Link
![](https://community.sap.com/html/@EE5D5986E9F4E5657DCEACB7532B5C39/assets/bluesky-dark.svg)Bluesky
Linkedin

Related Content

* [SAP S4HANA Plant Maintenance for dummies](/t5/technology-blog-posts-by-members/sap-s4hana-plant-maintenance-for-dummies/ba-p/14234304)
  in [Technology Blog Posts by Members](/t5...