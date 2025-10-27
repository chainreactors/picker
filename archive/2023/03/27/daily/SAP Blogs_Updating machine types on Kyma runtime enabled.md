---
title: Updating machine types on Kyma runtime enabled
url: https://blogs.sap.com/2023/03/26/updating-machine-types-on-kyma-runtime-enabled/
source: SAP Blogs
date: 2023-03-27
fetch_date: 2025-10-04T10:45:59.216964
---

# Updating machine types on Kyma runtime enabled

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Technology](/t5/technology/ct-p/technology)
* [Technology Blog Posts by SAP](/t5/technology-blog-posts-by-sap/bg-p/technology-blog-sap)
* Updating machine types on Kyma runtime enabled

Technology Blog Posts by SAP

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/technology-blog-sap/article-id/160368&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [Updating machine types on Kyma runtime enabled](/t5/technology-blog-posts-by-sap/updating-machine-types-on-kyma-runtime-enabled/ba-p/13557393)

![gabbi](https://avatars.profile.sap.com/5/d/id5d1ce96e6a7e45a001f65f5b22a5a2c470d6531e3abc3447464e89db6620a57b_small.jpeg "gabbi")

![Product and Topic Expert](/html/@138D6F765B60D7FC0168643DE27D8A68/rank_icons/sap-logo-small-14px.png "Product and Topic Expert")
[gabbi](https://community.sap.com/t5/user/viewprofilepage/user-id/13919)

Product and Topic Expert

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=technology-blog-sap&message.id=160368)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/technology-blog-sap/article-id/160368)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13557393)

‎2023 Mar 26
4:10 PM

[5
Kudos](/t5/kudos/messagepage/board-id/technology-blog-sap/message-id/160368/tab/all-users "Click here to see who gave kudos to this post.")

1,618

* SAP Managed Tags
* [SAP BTP, Kyma runtime](https://community.sap.com/t5/c-khhcw49343/SAP%2520BTP%252C%2520Kyma%2520runtime/pd-p/73554900100800003012)
* [DevOps](https://community.sap.com/t5/c-khhcw49343/DevOps/pd-p/51112e3c-4b78-4058-a637-67f453c196c9)
* [SAP Business Technology Platform](https://community.sap.com/t5/c-khhcw49343/SAP%2520Business%2520Technology%2520Platform/pd-p/73555000100700000172)

* [DevOps

  Programming Tool](/t5/c-khhcw49343/DevOps/pd-p/51112e3c-4b78-4058-a637-67f453c196c9)
* [SAP BTP, Kyma runtime

  SAP Business Technology Platform](/t5/c-khhcw49343/SAP%2BBTP%25252C%2BKyma%2Bruntime/pd-p/73554900100800003012)
* [SAP Business Technology Platform

  Software Product](/t5/c-khhcw49343/SAP%2BBusiness%2BTechnology%2BPlatform/pd-p/73555000100700000172)

View products (3)

To improve customer experience and provide more flexibility, we have recently enabled changing machine types for Kyma clusters.

## What does it mean?

When you provision a Kyma cluster from the BTP cockpit, you decide on the machine types and min and max values. These are your Kubernetes worker nodes on which your custom workloads and Kyma components will run.

The default configuration of the Kyma runtime provides the following:

*3 Virtual machines of 4 CPU and 16 GB each*

![](/legacyfs/online/storage/blog_attachments/2023/03/Screenshot-2023-03-23-at-14.09.58.png)

You have always been able to change the default machine type while provisioning a cluster from the BTP.

However, whatever machine type you decided on during the provisioning, you could not change it without deleting the existing cluster.

## What is new?

The latest improvements in the Kyma runtime enable updating the machine type even after provisioning the cluster, which previously was impossible.

*Now, you can simply do it by updating the environment from the BTP cockpit.*

Navigate to Instance & Subscriptions in your subaccount where Kyma is provisioned.

* Go to Environments

* Update

![](/legacyfs/online/storage/blog_attachments/2023/03/Screenshot-2023-03-23-at-14.20.03.png)

**Note**: *In case, you decide to change to a lower machine type, ensure the number of virtual machines are adjusted accordingly. This is to ensure that your workloads should have enough resources (memory and CPU) available to run properly.*

So far, so good, but ...

## You may wonder why you need to do that

You started with a certain size of workloads to be deployed.

As your usage, workloads, and business scenarios deployed on Kyma have grown, you realize that having a different machine type might meet your requirements better.

Many customers have wanted to do that for a while, and now they can go ahead and update their Kyma runtime to use the machine types that fit their needs best. ![:slightly_smiling_face:](/html/@91D3E334D8D95BECA16E36EA295E2455/emoticons/1f642.png ":slightly_smiling_face:")

Labels

* [Product Updates](/t5/technology-blog-posts-by-sap/bg-p/technology-blog-sap/label-name/product%20updates)

* [cloud-native](/t5/tag/cloud-native/tg-p/board-id/technology-blog-sap)
* [Kubernetes](/t5/tag/Kubernetes/tg-p/board-id/technology-blog-sap)
* [Kyma](/t5/tag/Kyma/tg-p/board-id/technology-blog-sap)

1 Comment

You must be a registered user to add a comment. If you've already registered, sign in. Otherwise, register and sign in.

* [Comment](/plugins/common/feature/oidcss/sso_login_redirect/providerid/sap_ids_prompt?redirectreason=permissiondenied&referer=https%3A%2F%2Fcommunity.sap.com%2Ft5%2Ftechnology-blog-posts-by-sap%2Fupdating-machine-types-on-kyma-runtime-enabled%2Fba-p%2F13557393%23comment-on-this)

Copy Link
![](https://community.sap.com/html/@EE5D5986E9F4E5657DCEACB7532B5C39/assets/bluesky-dark.svg)Bluesky
Linkedin

Related Content

* [SAP Build FAQ: Commercials, Getting Started and More](/t5/technology-blog-posts-by-sap/sap-build-faq-commercials-getting-started-and-more/ba-p/14233744)
  in [Technology Blog Posts by SAP](/t5/technology-blog-posts-by-sap/bg-p/technology-blog-sap)  yesterday
* [Unlocking SAP Fiori and other business content on Mobile: A Practical Guide](/t5/technology-blog-posts-by-sap/unlocking-sap-fiori-and-other-business-content-on-mobile-a-practical-guide/ba-p/14230532)
  in [Technology Blog Posts by SAP](/t5/technology-blog-posts-by-sap/bg-p/technology-blog-sap)  Wednesday
* [SAP IQ to SAP HANA Cloud, Data Lake Migration Overview](/t5/technology-blog-posts-by-sap/sap-iq-to-sap-hana-cloud-data-lake-migration-overview/ba-p/14228663)
  in [Technology Blog Posts by SAP](/t5/technology-blog-posts-by-sap/bg-p/technology-blog-sap)  Wednesday
* [Artificial Intelligence and SAP Master Data Governance](/t5/technology-blog-posts-by-sap/artificial-intelligence-and-sap-master-data-governance/ba-p/14152960)
  in [Technology Blog Posts by SAP](/t5/technology-blog-posts-by-sap/bg-p/technology-blog-sap)  Tuesday
* [SAP S/4HANA: Stop the 'Interapplication Spaghetti' 🍝 Start the Real-Time Transformation](/t5/technology-blog-posts-by-members/sap-s-4hana-stop-the-interapplication-spaghetti-start-the-real-time/ba-p/14229514)
  in [Technology Blog Posts by Members](/t5/technology-blog-posts-by-members/bg-p/technology-blog-members)  Saturday

Top kudoed authors

| User | Count |
| --- | --- |
| [![Ria4](https://avatars.profile.sap.com/4/1/id41f53dcfce78ad1c94edcd3a60b4666df8e3aac18a25c618793ae5b110c6aee0_small.jpeg "Ria4")  ![Associate](/html/@138D6F765B60D7FC0168643DE27D8A68/rank_icons/sap-logo-small-14px.png "Associate") Ria4](/t5/user/viewprofilepage/user-id/1478971) | 14 |
| [![jeet_kapase](https://avatars.profile.sap.com/0/0/id008b5bef5d6007221ab5d86367db67c9ec91895fa76b16aeddea0ed2fe268734_small.jpeg "jeet_kapase")  ![Product and Topic Expert](/html/@138D6F765B60D7FC0168643DE27D8A68/rank_icons/sap-logo-small-14px.png "Product and Topic Expert") jeet\_kapase](/t5/user/viewprofilepage/user-id/16635) | 11 |
| [![FranciscoHurtado](https://avatars.profile.sap.com/c/7/idc7445eb9fe40fe17679b80e46c92d9e3f68656d9bae139d019c063457d...