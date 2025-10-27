---
title: SAP BTP Kyma/Kubernetes how-to: Pull from private repository
url: https://blogs.sap.com/2022/12/04/sap-btp-kyma-kubernetes-how-to-pull-from-private-repository/
source: SAP Blogs
date: 2022-12-05
fetch_date: 2025-10-04T00:30:53.691242
---

# SAP BTP Kyma/Kubernetes how-to: Pull from private repository

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Technology](/t5/technology/ct-p/technology)
* [Technology Blog Posts by SAP](/t5/technology-blog-posts-by-sap/bg-p/technology-blog-sap)
* SAP BTP Kyma/Kubernetes how-to: Pull from private ...

Technology Blog Posts by SAP

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/technology-blog-sap/article-id/163163&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [SAP BTP Kyma/Kubernetes how-to: Pull from private repository](/t5/technology-blog-posts-by-sap/sap-btp-kyma-kubernetes-how-to-pull-from-private-repository/ba-p/13566191)

![Gunter](https://avatars.profile.sap.com/a/4/ida479f2e0596469f30f8f256760af4a49349a092dbda1284ed2860522f6ceccd8_small.jpeg "Gunter")

![Product and Topic Expert](/html/@138D6F765B60D7FC0168643DE27D8A68/rank_icons/sap-logo-small-14px.png "Product and Topic Expert")
[Gunter](https://community.sap.com/t5/user/viewprofilepage/user-id/727)

Product and Topic Expert

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=technology-blog-sap&message.id=163163)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/technology-blog-sap/article-id/163163)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13566191)

‎2022 Dec 04
8:09 AM

[6
Kudos](/t5/kudos/messagepage/board-id/technology-blog-sap/message-id/163163/tab/all-users "Click here to see who gave kudos to this post.")

2,376

* SAP Managed Tags
* [SAP BTP, Kyma runtime](https://community.sap.com/t5/c-khhcw49343/SAP%2520BTP%252C%2520Kyma%2520runtime/pd-p/73554900100800003012)
* [Open Source](https://community.sap.com/t5/c-khhcw49343/Open%2520Source/pd-p/b2aac474-1581-4b1b-8932-de5f60b52558)

* [SAP BTP, Kyma runtime

  SAP Business Technology Platform](/t5/c-khhcw49343/SAP%2BBTP%25252C%2BKyma%2Bruntime/pd-p/73554900100800003012)
* [Open Source

  Programming Tool](/t5/c-khhcw49343/Open%2BSource/pd-p/b2aac474-1581-4b1b-8932-de5f60b52558)

View products (2)

## Blog content

**This information applies to both plain Kubernetes as it does to SAP BTP Kyma.** I wrote it because I found the information not in one piece and hope it saves you some time!

Pulling images into Kyma to run them as containers in pods is one of the wonderful things using Kubernetes. While we often leverage open-source software and configuration is in [ConfigMap](https://kubernetes.io/docs/concepts/configuration/configmap/)s it's often unavoidable to use a private repository for images. One that can only be accessed by your organization.

![](/legacyfs/online/storage/blog_attachments/2022/12/スクリーンショット-2022-12-04-163228.png)

Picture 1: Pull mechanisms to Kubernetes from an image repository.

There are two approaches to this:

1. Use your own private registry to store the images and pull them. My colleague Remy Astier wrote a [great blog](https://blogs.sap.com/2021/02/01/setting-up-a-private-docker-registry-in-sap-cloud-platform-kyma-kubernetes/) about it last year.

2. use the private repository option of commercial image registries like [Docker Hub](https://hub.docker.com/) or [Quay.io](https://quay.io/) and many others.

In this blog we'll look into option 2. Consider it a subset of option 1. Let's start!

## How-to

We use docker hub. The principle should be the same with other offerings on the web.

1. Push an image to the hub e.g. with
   > docker push <hub-id>/<imagename>:<tag>

2. On the docker hub set the image as private.
   ![](/legacyfs/online/storage/blog_attachments/2022/12/スクリーンショット-2022-12-04-164832.png)

3. Create a token in the security settings of your account as shown below. We'll only pull images, so read-only is sufficient.
   ![](/legacyfs/online/storage/blog_attachments/2022/12/スクリーンショット-2022-12-04-165045.png)Don't forget to keep the token secret somewhere, you need it later.

4. Now create a Kubernetes secret out of the token secret like so(below password needs to be exchanged completely with yours, just show it for easier understanding once you obtained it):
   > $: kubectl -n myKymaNamespace create secret docker-registry gunters-reg-credentials --docker-username='mydockerID' --docker-password=dckr\_pat\_XVe-9\_mySecret

5. Check the creation either on the CLI or look into the Kyma UI.
   ![](/legacyfs/online/storage/blog_attachments/2022/12/kyma-secret.png)You see the dockerconfigjson is created.

6. Finally we have to reference it in the deployment like so:
   ![](/legacyfs/online/storage/blog_attachments/2022/12/kyma-deployment-secret-1.png)

That's it.

## References

[SAP BTP Kyma - Help](https://help.sap.com/docs/BTP/65de2977205c403bbc107264b8eccf4b/468c2f3c3ca24c2c8497ef9f83154c44.html)

[Kyma - Open source project](https://kyma-project.io/docs/kyma/latest/)

Labels

* [Technology Updates](/t5/technology-blog-posts-by-sap/bg-p/technology-blog-sap/label-name/technology%20updates)

* [Docker](/t5/tag/Docker/tg-p/board-id/technology-blog-sap)
* [Kubernetes](/t5/tag/Kubernetes/tg-p/board-id/technology-blog-sap)

You must be a registered user to add a comment. If you've already registered, sign in. Otherwise, register and sign in.

* [Comment](/plugins/common/feature/oidcss/sso_login_redirect/providerid/sap_ids_prompt?redirectreason=permissiondenied&referer=https%3A%2F%2Fcommunity.sap.com%2Ft5%2Ftechnology-blog-posts-by-sap%2Fsap-btp-kyma-kubernetes-how-to-pull-from-private-repository%2Fba-p%2F13566191%23comment-on-this)

Copy Link
![](https://community.sap.com/html/@EE5D5986E9F4E5657DCEACB7532B5C39/assets/bluesky-dark.svg)Bluesky
Linkedin

Related Content

* [SAP Build FAQ: Commercials, Getting Started and More](/t5/technology-blog-posts-by-sap/sap-build-faq-commercials-getting-started-and-more/ba-p/14233744)
  in [Technology Blog Posts by SAP](/t5/technology-blog-posts-by-sap/bg-p/technology-blog-sap)  3 hours ago
* [RAP Using Custom Entity with load multiple data using Pagination and Preview using UI annotations](/t5/technology-q-a/rap-using-custom-entity-with-load-multiple-data-using-pagination-and/qaq-p/14233901)
  in [Technology Q&A](/t5/technology-q-a/qa-p/technology-questions)  12 hours ago
* [Creating a Hybrid CAP (Node.js) Profile with PostgreSQL on BTP from Business Application Studio](/t5/technology-blog-posts-by-members/creating-a-hybrid-cap-node-js-profile-with-postgresql-on-btp-from-business/ba-p/14233631)
  in [Technology Blog Posts by Members](/t5/technology-blog-posts-by-members/bg-p/technology-blog-members)  yesterday
* [What's New in SAP Analytics Cloud Modeling Extensions & Integration QRC4 2025 Release](/t5/technology-blog-posts-by-sap/what-s-new-in-sap-analytics-cloud-modeling-extensions-amp-integration-qrc4/ba-p/14208685)
  in [Technology Blog Posts by SAP](/t5/technology-blog-posts-by-sap/bg-p/technology-blog-sap)  yesterday
* [EDA with AEM and SAP Customer Activity Repository](/t5/technology-q-a/eda-with-aem-and-sap-customer-activity-repository/qaq-p/14232459)
  in [Technology Q&A](/t5/technology-q-a/qa-p/technology-questions)  Wednesday

Top kudoed authors

| User | Count |
| --- | --- |
| [![Ria4](https://avatars.profile.sap.com/4/1/id41f53dcfce78ad1c94edcd3a60b4666df8e3aac18a25c618793ae5b110c6aee0_small.jpeg "Ria4")  ![Associate](/html/@138D6F765B60D7FC0168643DE27D8A68/rank_icons/sap-logo-small-14px.png "Associate") Ria4](/t5/user/viewprofilepage/user-id/1478971) | 14 |
| [![jeet_kapase](https://avatars.profile.sap.com/0/0/id008b5bef5d6007221ab5...