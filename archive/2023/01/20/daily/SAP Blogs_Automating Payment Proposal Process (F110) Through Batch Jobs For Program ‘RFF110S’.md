---
title: Automating Payment Proposal Process (F110) Through Batch Jobs For Program ‘RFF110S’
url: https://blogs.sap.com/2023/01/19/automating-payment-proposal-process-f110-through-batch-jobs-for-program-rff110s/
source: SAP Blogs
date: 2023-01-20
fetch_date: 2025-10-04T04:22:43.614544
---

# Automating Payment Proposal Process (F110) Through Batch Jobs For Program ‘RFF110S’

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Enterprise Resource Planning](/t5/enterprise-resource-planning/ct-p/erp)
* [ERP Blog Posts by Members](/t5/enterprise-resource-planning-blog-posts-by-members/bg-p/erp-blog-members)
* Automating Payment Proposal Process (F110) Through...

Enterprise Resource Planning Blog Posts by Members

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/erp-blog-members/article-id/68520&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [Automating Payment Proposal Process (F110) Through Batch Jobs For Program 'RFF110S'](/t5/enterprise-resource-planning-blog-posts-by-members/automating-payment-proposal-process-f110-through-batch-jobs-for-program/ba-p/13569904)

![nimish_agarwal](https://avatars.profile.sap.com/8/3/id8381eefaf24ac1694f42be84cb1978320a458a1dfa49fd702880fe74a8266986_small.jpeg "nimish_agarwal")

[nimish\_agarwal](https://community.sap.com/t5/user/viewprofilepage/user-id/836948)

Explorer

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=erp-blog-members&message.id=68520)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/erp-blog-members/article-id/68520)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13569904)

‎2023 Jan 19
9:24 PM

[6
Kudos](/t5/kudos/messagepage/board-id/erp-blog-members/message-id/68520/tab/all-users "Click here to see who gave kudos to this post.")

17,156

* SAP Managed Tags
* [SAP Payment Engine](https://community.sap.com/t5/c-khhcw49343/SAP%2520Payment%2520Engine/pd-p/01200615320800001129)
* [FIN Accounts Receivable and Payable](https://community.sap.com/t5/c-khhcw49343/FIN%2520Accounts%2520Receivable%2520and%2520Payable/pd-p/173284387196962001652277559265438)

* [SAP Payment Engine

  SAP Payment Engine](/t5/c-khhcw49343/SAP%2BPayment%2BEngine/pd-p/01200615320800001129)
* [FIN Accounts Receivable and Payable

  Software Product Function](/t5/c-khhcw49343/FIN%2BAccounts%2BReceivable%2Band%2BPayable/pd-p/173284387196962001652277559265438)

View products (2)

Hello and welcome to my blog post on automating payment proposal process through batch jobs using program **RFF110S**.

**Introduction: -**

Client had a requirement to automate ONLY their proposal jobs whereas payment runs be executed manually by the AP team.

Daily, business executes 20 pay-cycles for multiple company codes with varied dataset based on the day of the week. For example, Checks are run on Tues & Thurs, ACHs & Wires daily, Outsourced Checks on Wed & Fri, and so on. Dates such as Posting date, Next post. date, etc. play a key role in defining your dataset for that specific day.

This looked quite monotonous even from a user perspective, entering same set of data every single day to get the process going.

**PS:** Requirement is ‘proposal job should ONLY trigger on business days.’

**Prerequisites: -**

Three-step settings required to achieve the aforesaid requirement -

Step 1 – Configuration Change - Create Factory Calendar, i.e., AP Team Working Days Calendar. (T.Code SCAL)

Step 2 – Create variants for program RFF110S for each working day (Program RFF110S)

Step 3 – Schedule batch jobs for program RFF110S with variants created in Step 2 (T.Code SM36)

**Step 1 – Configuration Change - Create Factory Calendar, i.e., ZZ - AP Team Working Days Calendar.**

T.Code  SCAL –

Usually, Factory calendar is quite a risky thing to configure, and it’s advisable to have inputs from PP (Production Planning) team before proceeding to setup the same. In case you don’t have PP team in the project, check who is responsible or owns the factory calendar part and align with them.

While creating a factory calendar be careful that SAP landscape is completely in sync with all the calendars available in production. The new transport request will include existing calendars as well as the one you will create for AP team working days schedule. Kindly take a note of that.

In my case, while creating factory calendar I had to tweak few days to reflect them as working day and few days as holiday. This can be achieved using Special rules in factory calendar and it's the sole criteria for your batch jobs to ONLY trigger on business days.

One important thing to remember, you must update the factory calendar every year based on the business days provided by your client.

![](/legacyfs/online/storage/blog_attachments/2023/01/Factory-Calendar-1.png)

![](/legacyfs/online/storage/blog_attachments/2023/01/Special-Rules-FC.png)

**Step 2 – Create variants for program RFF110S for each working day (Program RFF110S)**

This is the most critical step in the entire setup.

All my variants are DYNAMICALLY date updated and any change in the static field led to creation of new variant for the pay run.

For example,

ACHs (A) & Wires (W) ran daily

Checks (C) ran Tues & Thurs

Outsourced checks (O) ran Wed & Fri

To begin with parameters for program **RFF110S**, we need to create variants

**Variant 1 – CC\_MON**    (CC = Company Code & Mon = Monday)

Run date = Current date, Run id = Company code, Posting date = Current date +1, Docs Entered up to = current date, Company code, Payment Methods = **AW**, Next Post. Date = current date +2

Vendor range = to be provided by business. Rest of the fields can be selected on need basis.

**Variant 2 – CC\_TU\_TH**

Run date = Current date, Run id = Company code, Posting date = Current date +1, Docs Entered up to = current date, Company code, Payment Methods = **ACW,** Next Post. Date = current date +2

**Variant 3 – CC\_WED**

Run date = Current date, Run id = Company code, Posting date = Current date +1, Docs Entered up to = current date, Company code, Payment Methods = **AWO**, Next Post. Date = current date +2

**Variant 4 – CC\_FRI**

Run date = Current date, Run id = Company code, Posting date = Current date +1, Document entered up to = current date, Company code, Payment Methods = AWO, Next Post. Date = **current date +4**

Friday’s run required a new variant, solely because the next post. date is current date +4 days (since Sat & Sun are weekly off)

4 variants per company code were setup, reaching 80 variants in total for 20 company codes.

![](/legacyfs/online/storage/blog_attachments/2023/01/Variants-1.png)

![](/legacyfs/online/storage/blog_attachments/2023/01/Variants-2.png)

![](/legacyfs/online/storage/blog_attachments/2023/01/Variants-3.png)

**Step 3 – Schedule batch jobs for program RFF110S (T.Code SM36)**

The pay-cycles required to be run at 09:00 am daily. Jobs were scheduled as –

Job Name - **RFF110S\_MON\_CC** (MON = Monday & CC = Company Code)

Program – RFF110S

Variant – CC\_MON

Date and time – Enter upcoming Monday date and time as 09:00:00

Periodic Job – **Checked**, Period Values – **Weekly**

Restrictions – Factory calendar, Calendar ID:  **ZZ** and Select **Execute on Working Days** radio button.

Similarly schedule jobs for Tuesday, Wednesday, Thursday, and Friday with their respective variants.

When the scheduled batch job is executed, system will create an additional job for your proposal run with regular nomenclature **'F110-20230112-2000   -X'**. Please refer below screenshots for better understanding.

![](/legacyfs/online/storage/blog_attachments/2023/01/Batch-Job-1.png)

![](/legacyfs/online/storage/blog_attachments/2023/01/Batch-Job-2.png)

![](/legacyfs/online/storage/blog_attachments/2023/01/Ba...