---
title: Cross-Line stock put away with EWM
url: https://blogs.sap.com/2023/01/13/cross-line-stock-put-away-with-ewm/
source: SAP Blogs
date: 2023-01-14
fetch_date: 2025-10-04T03:52:51.512963
---

# Cross-Line stock put away with EWM

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Supply Chain Management](/t5/supply-chain-management/ct-p/scm)
* [SCM Blog Posts by Members](/t5/supply-chain-management-blog-posts-by-members/bg-p/scm-blog-members)
* Cross-Line stock put away with EWM

Supply Chain Management Blog Posts by Members

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/scm-blog-members/article-id/4920&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [Cross-Line stock put away with EWM](/t5/supply-chain-management-blog-posts-by-members/cross-line-stock-put-away-with-ewm/ba-p/13567925)

![narsimha_namburi](https://avatars.profile.sap.com/9/d/id9d5557d6c55837dfd912b0099ec21a90b449299047adb5988fdedbd1346f46e1_small.jpeg "narsimha_namburi")

[narsimha\_namburi](https://community.sap.com/t5/user/viewprofilepage/user-id/559130)

Participant

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=scm-blog-members&message.id=4920)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/scm-blog-members/article-id/4920)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13567925)

‎2023 Jan 13
7:02 PM

[13
Kudos](/t5/kudos/messagepage/board-id/scm-blog-members/message-id/4920/tab/all-users "Click here to see who gave kudos to this post.")

9,235

* SAP Managed Tags
* [SAP Extended Warehouse Management](https://community.sap.com/t5/c-khhcw49343/SAP%2520Extended%2520Warehouse%2520Management/pd-p/01200615320800000705)
* [EWM - Delivery Processing](https://community.sap.com/t5/c-khhcw49343/EWM%2520-%2520Delivery%2520Processing/pd-p/674879738150278190016884561790060)

* [SAP Extended Warehouse Management

  SAP Extended Warehouse Management](/t5/c-khhcw49343/SAP%2BExtended%2BWarehouse%2BManagement/pd-p/01200615320800000705)
* [EWM - Delivery Processing

  Software Product Function](/t5/c-khhcw49343/EWM%2B-%2BDelivery%2BProcessing/pd-p/674879738150278190016884561790060)

View products (2)

**Cross Line put away with EWM**

Ever got from business that system should determine bins in specific sequence rather than just determining with bin name in ascending order? Cross-Line stock put away is the solution.

Let’s understand how it works.

In this example, I created 20 bins under 1 storage type in a sequence as shown below.

01-01-01, 01-01-02 ….........01-01-20.

![](/legacyfs/online/storage/blog_attachments/2023/01/Picture1-19.png)

When the put away task is created, the system will determine bins in a sequence as shown below.

![](/legacyfs/online/storage/blog_attachments/2023/01/Picture2-11.png)

The system is determining bins in a sequence in the ascending order of naming convention.

How to achieve bin determination in a specific sequence number?

Let’s configure activity area and maintain sort sequence for CLSP – Cross line Put away

![](/legacyfs/online/storage/blog_attachments/2023/01/Picture3-8.png)

Perform bin sorting with specific sequence numbers for bins. (In this case I’ve used sorting upload template)

![](/legacyfs/online/storage/blog_attachments/2023/01/Picture4-11.png)

Sorting number updated for all bins.

After sorting with CLSP, if we try to create a warehouse task for the same delivery, the system will propose bins based on the sort sequence number.

![](/legacyfs/online/storage/blog_attachments/2023/01/Picture5-7.png)

If a new delivery is created, the system will again search bins based on the sort sequence number

![](/legacyfs/online/storage/blog_attachments/2023/01/Picture6-5.png)

In these cases, even though PTWY activity area not assigned to bins, we can still create put away tasks and combine tasks into warehouse order with predefined rules.

Sorting bins with PTWY activity will only be useful for travel path optimization but not determining the destination bin. The reason being activity area will come into place only after the bin determination.

Thus Cross-Line put away can help to optimize the bin determination in the put away.

PS: This is my personal observation based on requirements and this blog is based on S4 HANA 2022 version sandbox. Functionality available in older versions also.

Thank you for reading the post, please share thoughts and feedback.

Follw <https://community.sap.com/topics/extended-warehouse-management> for more content.

Follow Narsimha Namburi for more updates.

References

<https://help.sap.com>

2 Comments

You must be a registered user to add a comment. If you've already registered, sign in. Otherwise, register and sign in.

* [Comment](/plugins/common/feature/oidcss/sso_login_redirect/providerid/sap_ids_prompt?redirectreason=permissiondenied&referer=https%3A%2F%2Fcommunity.sap.com%2Ft5%2Fsupply-chain-management-blog-posts-by-members%2Fcross-line-stock-put-away-with-ewm%2Fba-p%2F13567925%23comment-on-this)

Copy Link
![](https://community.sap.com/html/@EE5D5986E9F4E5657DCEACB7532B5C39/assets/bluesky-dark.svg)Bluesky
Linkedin

Related Content

* [How to have unified HU in EWM?](/t5/supply-chain-management-q-a/how-to-have-unified-hu-in-ewm/qaq-p/14234542)
  in [Supply Chain Management Q&A](/t5/supply-chain-management-q-a/qa-p/scm-questions)  2 hours ago
* [Advanced Intercompany Sales in SAP S/4HANA](/t5/supply-chain-management-blog-posts-by-members/advanced-intercompany-sales-in-sap-s-4hana/ba-p/14234227)
  in [Supply Chain Management Blog Posts by Members](/t5/supply-chain-management-blog-posts-by-members/bg-p/scm-blog-members)  9 hours ago
* [Material & Quality Management in SAP S/4HANA](/t5/supply-chain-management-blog-posts-by-members/material-amp-quality-management-in-sap-s-4hana/ba-p/14234018)
  in [Supply Chain Management Blog Posts by Members](/t5/supply-chain-management-blog-posts-by-members/bg-p/scm-blog-members)  12 hours ago
* [Variant Configuration (LO-VC) in SAP S/4HANA](/t5/supply-chain-management-blog-posts-by-members/variant-configuration-lo-vc-in-sap-s-4hana/ba-p/14234012)
  in [Supply Chain Management Blog Posts by Members](/t5/supply-chain-management-blog-posts-by-members/bg-p/scm-blog-members)  13 hours ago
* [Master Data and Core Logistics Processes in SAP S/4HANA](/t5/supply-chain-management-blog-posts-by-members/master-data-and-core-logistics-processes-in-sap-s-4hana/ba-p/14233991)
  in [Supply Chain Management Blog Posts by Members](/t5/supply-chain-management-blog-posts-by-members/bg-p/scm-blog-members)  13 hours ago

Top kudoed authors

| User | Count |
| --- | --- |
| [![former_member8860](https://avatars.profile.sap.com/former_member_small.jpeg "former_member8860")  former\_member8860](/t5/user/viewprofilepage/user-id/8860) | 1 |
| [![Omar_Ossama](https://avatars.profile.sap.com/6/0/id60770dc14b33e6d35123a7bd2eaa3d06dbba849d4621ca8fc61220b1d4cbdcc7_small.jpeg "Omar_Ossama")  Omar\_Ossama](/t5/user/viewprofilepage/user-id/145202) | 1 |
| [![former_member788724](https://avatars.profile.sap.com/former_member_small.jpeg "former_member788724")  former\_member788724](/t5/user/viewprofilepage/user-id/788724) | 1 |
| [![Rahul_Gandi1](https://avatars.profile.sap.com/8/8/id88f3b6bb61a7ae49c61dc9fe258f8832a55ef6620c927ff171b95b71a8d75933_small.jpeg "Rahul_Gandi1")  Rahul\_Gandi1](/t5/user/viewprofilepage/user-id/1877178) | 1 |
| [![Sumit_Holey](https://avatars.profile.sap.com/6/4/id642b6f7f0a2309c97ee5c73483a3639ad95efdee106b06c21d76239272afc5d5_small.jpeg "Sumit_Holey")  Sumit\_Holey](/t5/user/viewprofilepage/user-id/11624) | 1 |
| [![vamshikrishna_sr...