---
title: Multiple address handling for sales documents in SAP S/4HANA Cloud
url: https://blogs.sap.com/2023/03/12/multiple-address-handling-for-sales-documents-in-sap-s-4hana-cloud/
source: SAP Blogs
date: 2023-03-13
fetch_date: 2025-10-04T09:25:22.422582
---

# Multiple address handling for sales documents in SAP S/4HANA Cloud

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Enterprise Resource Planning](/t5/enterprise-resource-planning/ct-p/erp)
* [ERP Blog Posts by SAP](/t5/enterprise-resource-planning-blog-posts-by-sap/bg-p/erp-blog-sap)
* Multiple address handling for sales documents in S...

Enterprise Resource Planning Blog Posts by SAP

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/erp-blog-sap/article-id/52404&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [Multiple address handling for sales documents in SAP S/4HANA Cloud](/t5/enterprise-resource-planning-blog-posts-by-sap/multiple-address-handling-for-sales-documents-in-sap-s-4hana-cloud/ba-p/13563712)

![varunvenkat](https://avatars.profile.sap.com/6/d/id6d9836d543f88d438477c8e54903aa6ba4a079c87ec08d808dc512a637a4c55f_small.jpeg "varunvenkat")

![Product and Topic Expert](/html/@138D6F765B60D7FC0168643DE27D8A68/rank_icons/sap-logo-small-14px.png "Product and Topic Expert")
[varunvenkat](https://community.sap.com/t5/user/viewprofilepage/user-id/83606)

Product and Topic Expert

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=erp-blog-sap&message.id=52404)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/erp-blog-sap/article-id/52404)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13563712)

‎2023 Mar 12
12:07 PM

[10
Kudos](/t5/kudos/messagepage/board-id/erp-blog-sap/message-id/52404/tab/all-users "Click here to see who gave kudos to this post.")

6,685

* SAP Managed Tags
* [SAP S/4HANA business partner](https://community.sap.com/t5/c-khhcw49343/SAP%2520S%252F4HANA%2520business%2520partner/pd-p/e5aee8fa-b65f-4af6-9f57-9d0a05b033bc)
* [SD Sales](https://community.sap.com/t5/c-khhcw49343/SD%2520Sales/pd-p/167431589774684563301227734202839)
* [SAP S/4HANA Cloud Public Edition](https://community.sap.com/t5/c-khhcw49343/SAP%2520S%252F4HANA%2520Cloud%2520Public%2520Edition/pd-p/08e2a51b-1ce5-4367-8b33-4ae7e8b702e0)

* [SAP S/4HANA Cloud Public Edition

  SAP S/4HANA Cloud](/t5/c-khhcw49343/SAP%2BS%25252F4HANA%2BCloud%2BPublic%2BEdition/pd-p/08e2a51b-1ce5-4367-8b33-4ae7e8b702e0)
* [SD Sales

  Software Product Function](/t5/c-khhcw49343/SD%2BSales/pd-p/167431589774684563301227734202839)
* [SAP S/4HANA business partner

  Additional Software Product](/t5/c-khhcw49343/SAP%2BS%25252F4HANA%2Bbusiness%2Bpartner/pd-p/e5aee8fa-b65f-4af6-9f57-9d0a05b033bc)

View products (3)

As an S/4HANA Cloud consultant, you might come across a scenario where sales documents need to contain varying data for the different partner functions of a certain business partner. In SAP S/4HANA Cloud, multiple address handling allows you to maintain different addresses for a single business partner, depending on the partner function. Some of the commonly used partner functions in sales documents are:

* Sold-to Party

* Ship-to Party

* Bill-to Party

To illustrate a common business example, a business partner that manages multiple production/storage locations can have shipping addresses that differ from the standard sold-to address of the business partner. In this blog, we will look at the steps to set up multiple address handling for the different partner functions mentioned above in SAP S/4HANA Cloud.

**Prerequisite:** **Enable Multiple Address Handling in Customizing**

The prerequisite to use the multiple address handling capability is to enable this in the customizing of your system. For this, open the app “Configure Your Solution” and type in “Address handling” into the search field. Navigate into the entries highlighted in Figure 1. (In case you are using CBC, you can directly search for the SSCUI IDs shown in the screenshots below)

![](/legacyfs/online/storage/blog_attachments/2023/02/conigure_solution_search_result.png)

Figure 1

After clicking into the *Business Partner* item, activate the configuration step 17 ‘Activate Multiple Address Handling for Customer Master Data in SAP BP’ as shown in Figure 2.

![](/legacyfs/online/storage/blog_attachments/2023/02/activate_MAH_part1.png)

Figure 2

After activation multiple address handling for master data, customers can now prepare/consolidate their business partner (customer) records accordingly. The SD processes will continue to work as before. Once the customer master data is streamlined, customers can then activate multiple address handling in SD documents (Figure 3) as well. Refer to guides in the [Central note](https://me.sap.com/notes/3119364) for further details.

![](/legacyfs/online/storage/blog_attachments/2023/02/activate_MAH_part2.png)

Figure 3

Now that the configuration is out of the way, let’s dive into how to actually assign multiple addresses to the various partner functions.

**Select a business partner**

Open the “Manage Business Partner” app and search for a business partner that you want to use for test purposes. For this blog, I will be using the BP **10100009** (Inlandskunde DE 9). Navigate into the Business Partner view.

**Create** **a new address**

In the Address header under the section ‘Address Details’, click the “Create” Button to create a new address entry. Make sure you are in Edit mode to be able to do this.

![](/legacyfs/online/storage/blog_attachments/2023/02/Manage_BP_address_details.png)

Create new address

Now click on the newly created blank row to go into the item level. Fill out the address fields such as ‘Country’, ‘City’, ‘Street’ etc.

**Add a usage type for the new address**

Now scroll down to the ‘Address Usage’ section. This is the crucial step in the whole process. Click on the “Create” button here to add a new address usage line. Pick values for the ‘Valid From’ and ‘Valid To’ fields and for Address Type, choose **Delivery Address (SHIP\_TO).** This will indicate to the system that the newly created address in the previous step will be used for the Ship-To party partner function.

![](/legacyfs/online/storage/blog_attachments/2023/02/Manage_BP_ship_to_address_address_usage.png)

Add usage type

Apply the changes and save the draft to persist your changes. You can repeat this process (creating a new address and assigning an address usage) for the partner function Bill-to party as well. Choose the address type "Billing Address (BILL-TO) in that case. Furthermore, there is also the possibility to have multiple addresses with the same usage type (multiple delivery addresses for example). In that case, one of these multiple addresses per usage type has to be defined as the standard address.

Please note that the partner function Payer is currently not supported for multiple address handling.

**Use the multiple address handling in your sales documents**

Having completed the setup, we can now run a test to see how the multiple address handling comes into effect. Open the “Create Sales Orders – VA01” app. Choose the Order type “OR” (Standard Order) and the sales organization (1010 in my case) of the BP you are testing with. Hit Enter.

In the Sold-to Party field, enter your BP ID and hit enter. You will now see one or multiple popups, where you can select the address value to be used for the respective partner function. After this step, fill out values for the fields Customer reference and Customer reference date. After hitting enter, you will notice that the correct address for the Ship-to Party has automatically been determined based on the address usage th...