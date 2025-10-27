---
title: Validation Policy in Ariba Guided Buying
url: https://blogs.sap.com/2023/03/04/validation-policy-in-ariba-guided-buying/
source: SAP Blogs
date: 2023-03-05
fetch_date: 2025-10-04T08:43:40.849617
---

# Validation Policy in Ariba Guided Buying

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Spend Management](/t5/spend-management/ct-p/spend-management)
* [Spend Management Blog Posts by Members](/t5/spend-management-blog-posts-by-members/bg-p/spend-management-blog-members)
* Validation Policy in Ariba Guided Buying

Spend Management Blog Posts by Members

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/spend-management-blog-members/article-id/1863&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [Validation Policy in Ariba Guided Buying](/t5/spend-management-blog-posts-by-members/validation-policy-in-ariba-guided-buying/ba-p/13562985)

![Chhetan1](https://avatars.profile.sap.com/d/3/idd35a10cb1334547512e63e16f648267bf6ed163abca1e3b31a32e8fb0ee05204_small.jpeg "Chhetan1")

[Chhetan1](https://community.sap.com/t5/user/viewprofilepage/user-id/46979)

Participant

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=spend-management-blog-members&message.id=1863)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/spend-management-blog-members/article-id/1863)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13562985)

‎2023 Mar 04
11:51 AM

[6
Kudos](/t5/kudos/messagepage/board-id/spend-management-blog-members/message-id/1863/tab/all-users "Click here to see who gave kudos to this post.")

6,434

* SAP Managed Tags
* [SAP Ariba Buying and Invoicing](https://community.sap.com/t5/c-khhcw49343/SAP%2520Ariba%2520Buying%2520and%2520Invoicing/pd-p/088a2ce1-412b-458b-becb-2311c968d328)

* [SAP Ariba Buying and Invoicing

  Software Product](/t5/c-khhcw49343/SAP%2BAriba%2BBuying%2Band%2BInvoicing/pd-p/088a2ce1-412b-458b-becb-2311c968d328)

View products (1)

**Hello, welcome to my blog post!** It’s a complete guide for Ariba consultants and administrators who configures and manages validation policies in Ariba guided buying

**Introduction**

Validation policy guides user to follow the right procedures while creating requisition. When user submits a requisition, guided buying validates the fields of it against policies.

Validation policies can be setup by using header level or line-item level fields of requisition. It displays an informational message, an error message or request for justification on requisition page.

**Note:** Error message doesn’t allow users to submit requisition until they correct the error on it

Let’s discuss how to configure validation policy in Ariba guided buying

Login to Guided buying->click on Admin->Click Manage Policies->Download a sample policy from Validation Policy section

An excel template consists of four sheets a description, a key definition, an expression and a message

**Description:**![](/legacyfs/online/storage/blog_attachments/2023/03/Picture1-5.png)

**Policy Name:** Enter the name of the purchasing policy.

**Policy Description:** let’s administrator to know what the requirement is.

**Policy Applicable Type:** It can be requisition, non-catalog request, line item form or tile

**Key Definition:**![](/legacyfs/online/storage/blog_attachments/2023/03/Picture2-5.png)

**Policy Name:** Copy it from ‘Description’ tab

**Lookup Key:** It should be ProcurementUnit or PurchasingUnit

**Lookup Kay Value:** It can be a user purchasing unit or defaulted to “ALL”

**Expression:**![](/legacyfs/online/storage/blog_attachments/2023/03/Picture3-5.png)

**Policy Name:** Copy it from ‘Key Definition’ tab

**Left hand side Type:** Enter value “Field” to evaluate

**Left hand side Field:** Enter the value of field to evaluate. For example: CompanyCode.UniqueName

**Right hand side Type:** It should always be “constant”

**Right hand side Field:** Enter the associated value or details of fields mentioned in the Left-hand side Field (Column C). For example: company code 1234

**Operator:** <, >, ==, !=, <=, >=, contains, hasAllValues, or hasAnyValues operators decides whether to apply policy or not

**Logical Operator:** && and || operators are applicable, if there are more than 1 line in the policy. && operator triggers policy if conditions of all the lines are met. || operator triggers policy if condition of first line or the next line is met.

**Message:**![](/legacyfs/online/storage/blog_attachments/2023/03/Picture4-3.png)

**Policy Name:** Copy it from ‘Expression’ tab

**Severity:** When users violate a policy, guided buying displays either of the messages to them

* **Info->** Displays a text message that set in the policy. Allows users to submit requisition

* **Justification->** Displays a message requesting user to provide justification for raising a requisition

* **Error->** Displays an error message on requisition. It doesn’t allow users to submit requisition until they correct the error on it

**Message:** A text message that requests users to understand and follow purchasing policies of company and justify their purchasing requests

**Justification Options:** customer can have a predefined justification for the policy or else leave this column blank and allow users to enter their justification in comment box.

**Configuration:**

Let’s configure validation policies for some real time scenarios

**Scenario 1:** Display an **error** message; if the total amount of requisition is equal to “0”![](/legacyfs/online/storage/blog_attachments/2023/03/Picture5-5.png)![](/legacyfs/online/storage/blog_attachments/2023/03/Picture6-4.png)![](/legacyfs/online/storage/blog_attachments/2023/03/Picture7-3.png)![](/legacyfs/online/storage/blog_attachments/2023/03/Picture8-3.png)

**Scenario 2:** Display an **error** message; Do not allow user to raise PR against company code “1234”![](/legacyfs/online/storage/blog_attachments/2023/03/Picture9-3.png)![](/legacyfs/online/storage/blog_attachments/2023/03/Picture10-2.png)![](/legacyfs/online/storage/blog_attachments/2023/03/Picture11-3.png)![](/legacyfs/online/storage/blog_attachments/2023/03/Picture12-3.png)

**Scenario 3:** Display an **error** message; a quote is mandatory from supplier “1234567000”![](/legacyfs/online/storage/blog_attachments/2023/03/Picture13-3.png)![](/legacyfs/online/storage/blog_attachments/2023/03/Picture14-2.png)![](/legacyfs/online/storage/blog_attachments/2023/03/Picture15-3.png)![](/legacyfs/online/storage/blog_attachments/2023/03/Picture16-2.png)

**Scenario 4:** Display an **informational** message; if user orders a non-catalog item for commodity code “12345678 and 87654321”![](/legacyfs/online/storage/blog_attachments/2023/03/Picture17-1.png)![](/legacyfs/online/storage/blog_attachments/2023/03/Picture18.png)![](/legacyfs/online/storage/blog_attachments/2023/03/Picture19.png)![](/legacyfs/online/storage/blog_attachments/2023/03/Picture20.png)

**Scenario 5:** Request for **justification**; if user orders a non-catalog item with supplier “0001234567”![](/legacyfs/online/storage/blog_attachments/2023/03/Picture21.png)![](/legacyfs/online/storage/blog_attachments/2023/03/Picture22.png)![](/legacyfs/online/storage/blog_attachments/2023/03/Picture23.png)![](/legacyfs/online/storage/blog_attachments/2023/03/Picture24.png)

**Note:**

* When preparing the file, copy and paste the Policy Name which is referenced in the next few sheets. Do not use the same policy name to create other policies. Do not include colon ‘:’ in the policy name. The characters of Policy name and description is limited to 256

* When creating policy for multiple c...