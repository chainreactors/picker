---
title: Migrate / Upload Vendor Opening Balances in Rise with SAP Cloud 2208
url: https://blogs.sap.com/2022/10/25/migrate-upload-vendor-opening-balances-in-rise-with-sap-cloud-2208/
source: SAP Blogs
date: 2022-10-26
fetch_date: 2025-10-03T20:53:25.314740
---

# Migrate / Upload Vendor Opening Balances in Rise with SAP Cloud 2208

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Enterprise Resource Planning](/t5/enterprise-resource-planning/ct-p/erp)
* [ERP Blog Posts by Members](/t5/enterprise-resource-planning-blog-posts-by-members/bg-p/erp-blog-members)
* Migrate / Upload Vendor Opening Balances in Rise w...

Enterprise Resource Planning Blog Posts by Members

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/erp-blog-members/article-id/67148&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [Migrate / Upload Vendor Opening Balances in Rise with SAP Cloud 2208](/t5/enterprise-resource-planning-blog-posts-by-members/migrate-upload-vendor-opening-balances-in-rise-with-sap-cloud-2208/ba-p/13551555)

![former_member825914](https://avatars.profile.sap.com/former_member_small.jpeg "former_member825914")

[former\_member825914](https://community.sap.com/t5/user/viewprofilepage/user-id/825914)

Explorer

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=erp-blog-members&message.id=67148)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/erp-blog-members/article-id/67148)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13551555)

‎2022 Oct 26
12:01 AM

[10
Kudos](/t5/kudos/messagepage/board-id/erp-blog-members/message-id/67148/tab/all-users "Click here to see who gave kudos to this post.")

4,132

* SAP Managed Tags
* [SAP S/4HANA migration cockpit](https://community.sap.com/t5/c-khhcw49343/SAP%2520S%252F4HANA%2520migration%2520cockpit/pd-p/791935194581077217831679640306539)

* [SAP S/4HANA migration cockpit

  Software Product Function](/t5/c-khhcw49343/SAP%2BS%25252F4HANA%2Bmigration%2Bcockpit/pd-p/791935194581077217831679640306539)

View products (1)

**Dear All,**

**Introduction:**

This blog will guide you with the steps required for migrating **“Vendor Opening Balances”** into the ***SAP* S/4HANA *Cloud 2208*.**

The **SAP S/4HANA migration cockpit****is a tool designed for customers who have just installed SAP S/4HANA (*new implementation scenarios*) and want *to*** *transfer* their *business data from SAP or non-SAP software systems*. The SAP S/4HANA migration cockpit has become an essential tool for SAP S/4HANA data migration, supporting customers during the transition to SAP S/4HANA. It is part of both SAP S/4HANA and SAP S/4HANA Cloud and can be launched using the “Migrate Your Data” app in the Fiori Launchpad (Data Migration Launchpad) or using transaction LTMC (to be retired by SAP S/4HANA 2021). With the migration Launchpad.

It uses migration objects to identify and transfer the relevant data and, facilitates the migration process by providing predefined migration content and mapping. The SAP S/4HANA migration cockpit is SAP’s recommended approach for the migration of business data to SAP S/4HANA Cloud.

* I am SAP S/4 HANA Finance Consultant. I am upload Vendor Opening Balance in SAP Cloud Environment.

* Previously we don’t have any SAP (ECC Version) Standard facilities to upload Vendor Opening Balance.

* Now in Rise with SAP Public Cloud 2208 SAP given the provision to upload Vendor Opening Balance One time activity through Migration Cockpit.

* This blog provides an overview of how to upload Vendor Opening Balance in SAP S4 HANA Cloud -2208

* After migration all Vendor Opening Balance (Debit / Credit) amount showing the Vendor Balance or FBL1N.

**Steps in Vendor Opening Balance Upload:**

1. Project Creation

2. Download Template ( XML File )

3. Upload Template

4. Prepare

5. Mapping Task

6. Simulate

7. Migrate

**Fiori Tile Name: Migrate Your Data**

**Step 1: Click the Tile**

![](/legacyfs/online/storage/blog_attachments/2022/10/1-73.png)

**Step 2: Create Project Name**

![](/legacyfs/online/storage/blog_attachments/2022/10/2-32.png)

**Step 3 : Create New Project**

![](/legacyfs/online/storage/blog_attachments/2022/10/3-24.png)

**Step 4 : Select the FI Accounts Payable Open Item**

![](/legacyfs/online/storage/blog_attachments/2022/10/4-20.png)

**Step 5: Select the FI Accounts Payable Open Item & Move the Right Side and Click Review**

![](/legacyfs/online/storage/blog_attachments/2022/10/5-25.png)

**Step 6: Add the Project / Do Not Add**

![](/legacyfs/online/storage/blog_attachments/2022/10/6-28.png)

**Step 7: Click the Create Project**

![](/legacyfs/online/storage/blog_attachments/2022/10/7-17.png)

**Step 8: Create Project is Display and Click the Side Arrow**

![](/legacyfs/online/storage/blog_attachments/2022/10/8-14.png)

**Step 9: Select and Download the Template**

![](/legacyfs/online/storage/blog_attachments/2022/10/9-13.png)

**Step 10: Check & fill the Mandatory Filed**

![](/legacyfs/online/storage/blog_attachments/2022/10/10-11.png)

**Step 10.1 Xml. file for SAP Format**

![](/legacyfs/online/storage/blog_attachments/2022/10/10.1.png)

**Step 11: Click the Upload File**

![](/legacyfs/online/storage/blog_attachments/2022/10/11-9.png)

**Step 12: Upload the xml file**

![](/legacyfs/online/storage/blog_attachments/2022/10/12-11.png)

**Step 13: Message Showing Data Successfully Transferred to Staging Tables**

![](/legacyfs/online/storage/blog_attachments/2022/10/13-8.png)

**Step 14: Click the Prepare**

![](/legacyfs/online/storage/blog_attachments/2022/10/14-11.png)

**Step 15: Select the Prepare Staging Tables**

![](/legacyfs/online/storage/blog_attachments/2022/10/15-7.png)

**Step 16: Select the Mapping Tasks**

![](/legacyfs/online/storage/blog_attachments/2022/10/16-9.png)

**Step 17: Mapping the all-Line Item**

![](/legacyfs/online/storage/blog_attachments/2022/10/17-9.png)

**Step 18: Do One by one Mapping Confirmed**

![](/legacyfs/online/storage/blog_attachments/2022/10/18-6.png)

**Step 19: Ones Mapping is Confirmed Profit Center**

![](/legacyfs/online/storage/blog_attachments/2022/10/19-6.png)

**Step 20: Select the Simulate**

![](/legacyfs/online/storage/blog_attachments/2022/10/20-6.png)

**Step 21: Start the Simulation**

![](/legacyfs/online/storage/blog_attachments/2022/10/21-16.png)

**Step 22: Click the Migrate & System Migrate is Successful**

![](/legacyfs/online/storage/blog_attachments/2022/10/22-4.png)

### **RESULT:**

Now, we have successfully migrated the **“Vendor Opening Balances”** to

the SAP S4/HANA Cloud system. In order to see the migrated data in the system ,select the Display Supplier Balances.

**Step 23: Balance Upload Check with Display Supplier Balances**

![](/legacyfs/online/storage/blog_attachments/2022/10/23-4.png)

**Step 24: Check the line Item is Successfully Balance Upload**

![](/legacyfs/online/storage/blog_attachments/2022/10/24-5.png)

**Step 25: Check the Balance Special G/L Line Item is Successfully Upload**

![](/legacyfs/online/storage/blog_attachments/2022/10/25-4.png)We have successfully upload to Vendor Opening Balances in Migration Cockpit Cloud Environment.

**Conclusion:**

From this blog, we have learned how to successfully migrate the **Vendor Opening Balances** to the SAP S4 HANA Cloud System using **Migrate Your Data tile**.

### **Thanks for reading this blog…**

Hope this blog will be useful. If you enjoyed this blog post please give it a like! If you have questions,

feel free to comment.

If you would like to keep up on the latest updates regarding SAP S4/HANA cloud, Kindly follow me…

**Best & Regards,**

**Chandramohan P R**

* [Vendor Opening Balances Upload](/t5/tag/Vendor%20Op...