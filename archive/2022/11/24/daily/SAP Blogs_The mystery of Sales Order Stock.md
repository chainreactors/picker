---
title: The mystery of Sales Order Stock
url: https://blogs.sap.com/2022/11/23/the-mystery-of-sales-order-stock/
source: SAP Blogs
date: 2022-11-24
fetch_date: 2025-10-03T23:38:51.197590
---

# The mystery of Sales Order Stock

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Technology](/t5/technology/ct-p/technology)
* [Technology Blog Posts by SAP](/t5/technology-blog-posts-by-sap/bg-p/technology-blog-sap)
* The mystery of Sales Order Stock

Technology Blog Posts by SAP

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/technology-blog-sap/article-id/159854&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [The mystery of Sales Order Stock](/t5/technology-blog-posts-by-sap/the-mystery-of-sales-order-stock/ba-p/13555945)

![Andy456](https://avatars.profile.sap.com/c/5/idc50470931f6620ec2274ce882f7f356d4a9ffdb2595111f146c40e667e89a2ce_small.jpeg "Andy456")

![Product and Topic Expert](/html/@138D6F765B60D7FC0168643DE27D8A68/rank_icons/sap-logo-small-14px.png "Product and Topic Expert")
[Andy456](https://community.sap.com/t5/user/viewprofilepage/user-id/44251)

Product and Topic Expert

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=technology-blog-sap&message.id=159854)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/technology-blog-sap/article-id/159854)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13555945)

‎2022 Nov 23
7:19 PM

[12
Kudos](/t5/kudos/messagepage/board-id/technology-blog-sap/message-id/159854/tab/all-users "Click here to see who gave kudos to this post.")

1,526

* SAP Managed Tags
* [SAP Signavio](https://community.sap.com/t5/c-khhcw49343/SAP%2520Signavio/pd-p/088166be-6441-4660-9e5b-1a046de322bf)
* [SAP Signavio Process Insights](https://community.sap.com/t5/c-khhcw49343/SAP%2520Signavio%2520Process%2520Insights/pd-p/73555000100800003392)

* [SAP Signavio

  Additional Software Product](/t5/c-khhcw49343/SAP%2BSignavio/pd-p/088166be-6441-4660-9e5b-1a046de322bf)
* [SAP Signavio Process Insights

  business process transformation](/t5/c-khhcw49343/SAP%2BSignavio%2BProcess%2BInsights/pd-p/73555000100800003392)

View products (2)

**SAP SIGNAVIO Process Insights** holds many spectacular insights, some of which can be observed in many customer systems.

Today, let me talk about the mystery of Sales Order Stock : This can be observed at almost all customers that are running make to order processes. It can be described like this

![](/legacyfs/online/storage/blog_attachments/2022/11/Screenshot-2022-11-22-at-14.32.30.png)

Here comes the mystery : If companies run this process often enough, they will experience that while the sales order is completed, there is still Sales Order Stock.

**So what does that mean?**

The company produced something for a particular customer order, but did not sell it at the end.

We have seen occurrences where the stock value is in its millions of €. Hard to believe, isn't it?

How can you find out whether your company suffers from this mystery?

The answer is pretty straight forward: Connect to your SAP SIGNAVIO Process Insights tenant, and navigate to your Lead to Cash area, selecting the Performance Indicators.

![](/legacyfs/online/storage/blog_attachments/2022/11/Screenshot-2022-11-22-at-14.42.11.png)

This is a screen shot from a Demo System. If you select this Indicator, you are presented the size of the mystery.

![](/legacyfs/online/storage/blog_attachments/2022/11/Screenshot-2022-11-22-at-14.44.46.png)

**So what are possible root causes?**

Think of the following example scenario:

A customers orders 2 identical machines in one sales order, due to supply issues only one machine can be produced immediately. It is shipped and billed.

A second production order is in the system to produce the 2nd machine, but it takes time.

Now the customer contacts you, stating that they cannot wait that long and reject the 2nd machine.

The sales person accepts the cancelation, and reduces the order quantity to 1.

Now, the sales order is completed, with one production order remaining, with no more customer demand. Since production is typically decoupled from the sales, production builds the second machine, and posts it into customer stock, where it will remain ..... until you find out with SAP Process Insights.

Arguably, you can imaging many more scenarios which lead to this mystery.

So, if you want to run the analysis in your system, it takes you 3 clicks.

Make sure you exclude sales order stock that was created during the last days to cater for some delay between production end and delivery.

* **Recheck your Process Documentation**

* **Discuss with the Process Owner on what needs to be changed to prevent the problem from occuring in the future**

* **Setup a strategy to deal with the mystery stock ( case by case decision )**

* **Celebrate your process improvement**

Follow me in case you find such blogs helpful, and do not hesitate to reach out to me to discuss your thoughts.

**So, how large is your Sales Order Mystery Stock ?**

Labels

* [Life at SAP](/t5/technology-blog-posts-by-sap/bg-p/technology-blog-sap/label-name/life%20at%20sap)

4 Comments

You must be a registered user to add a comment. If you've already registered, sign in. Otherwise, register and sign in.

* [Comment](/plugins/common/feature/oidcss/sso_login_redirect/providerid/sap_ids_prompt?redirectreason=permissiondenied&referer=https%3A%2F%2Fcommunity.sap.com%2Ft5%2Ftechnology-blog-posts-by-sap%2Fthe-mystery-of-sales-order-stock%2Fba-p%2F13555945%23comment-on-this)

Copy Link
![](https://community.sap.com/html/@EE5D5986E9F4E5657DCEACB7532B5C39/assets/bluesky-dark.svg)Bluesky
Linkedin

Related Content

* [SAP S4HANA Plant Maintenance for dummies](/t5/technology-blog-posts-by-members/sap-s4hana-plant-maintenance-for-dummies/ba-p/14234304)
  in [Technology Blog Posts by Members](/t5/technology-blog-posts-by-members/bg-p/technology-blog-members)  3 hours ago
* [Transforming Healthcare Procurement: Lessons from Our S/4HANA MM Implementation](/t5/technology-q-a/transforming-healthcare-procurement-lessons-from-our-s-4hana-mm/qaq-p/14233251)
  in [Technology Q&A](/t5/technology-q-a/qa-p/technology-questions)  yesterday
* [🚀 Maîtrisez SAP S/4HANA : Les Fondamentaux de la Navigation !](/t5/technology-blog-posts-by-members/ma%C3%AEtrisez-sap-s-4hana-les-fondamentaux-de-la-navigation/ba-p/14229526)
  in [Technology Blog Posts by Members](/t5/technology-blog-posts-by-members/bg-p/technology-blog-members)  Saturday
* [🚀 Remember the pioneering days of SAP ECC?](/t5/technology-blog-posts-by-members/remember-the-pioneering-days-of-sap-ecc/ba-p/14229517)
  in [Technology Blog Posts by Members](/t5/technology-blog-posts-by-members/bg-p/technology-blog-members)  Saturday
* [SAP S/4HANA: Stop the 'Interapplication Spaghetti' 🍝 Start the Real-Time Transformation](/t5/technology-blog-posts-by-members/sap-s-4hana-stop-the-interapplication-spaghetti-start-the-real-time/ba-p/14229514)
  in [Technology Blog Posts by Members](/t5/technology-blog-posts-by-members/bg-p/technology-blog-members)  Saturday

Top kudoed authors

| User | Count |
| --- | --- |
| [![Ria4](https://avatars.profile.sap.com/4/1/id41f53dcfce78ad1c94edcd3a60b4666df8e3aac18a25c618793ae5b110c6aee0_small.jpeg "Ria4")  ![Associate](/html/@138D6F765B60D7FC0168643DE27D8A68/rank_icons/sap-logo-small-14px.png "Associate") Ria4](/t5/user/viewprofilepage/user-id/1478971) | 14 |
| [![jeet_kapase](https://avatars.profile.sap.com/0/0/id008b5bef5d6007221ab5d86367db67c9ec91895fa76b16aeddea0ed2fe268734_small.jpeg "jeet_kapase")  ![Product and Topic Expe...