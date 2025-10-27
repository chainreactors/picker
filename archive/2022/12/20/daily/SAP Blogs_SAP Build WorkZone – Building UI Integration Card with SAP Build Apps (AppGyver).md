---
title: SAP Build WorkZone – Building UI Integration Card with SAP Build Apps (AppGyver)
url: https://blogs.sap.com/2022/12/19/sap-build-workzone-building-ui-integration-card-with-sap-build-apps-appgyver/
source: SAP Blogs
date: 2022-12-20
fetch_date: 2025-10-04T01:58:51.405066
---

# SAP Build WorkZone – Building UI Integration Card with SAP Build Apps (AppGyver)

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Technology](/t5/technology/ct-p/technology)
* [Technology Blog Posts by SAP](/t5/technology-blog-posts-by-sap/bg-p/technology-blog-sap)
* SAP Build WorkZone - Building UI Integration Card ...

Technology Blog Posts by SAP

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/technology-blog-sap/article-id/159239&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [SAP Build WorkZone - Building UI Integration Card with SAP Build Apps (AppGyver)](/t5/technology-blog-posts-by-sap/sap-build-workzone-building-ui-integration-card-with-sap-build-apps/ba-p/13554194)

![Jay2](https://avatars.profile.sap.com/c/7/idc787c1b7169d28a783ce3ee14f5c41f026c662674bb7517b98343205f22bc0f4_small.jpeg "Jay2")

![Product and Topic Expert](/html/@138D6F765B60D7FC0168643DE27D8A68/rank_icons/sap-logo-small-14px.png "Product and Topic Expert")
[Jay2](https://community.sap.com/t5/user/viewprofilepage/user-id/40000)

Product and Topic Expert

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=technology-blog-sap&message.id=159239)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/technology-blog-sap/article-id/159239)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13554194)

‎2022 Dec 19
5:42 PM

[16
Kudos](/t5/kudos/messagepage/board-id/technology-blog-sap/message-id/159239/tab/all-users "Click here to see who gave kudos to this post.")

6,864

* SAP Managed Tags
* [SAP S/4HANA](https://community.sap.com/t5/c-khhcw49343/SAP%2520S%252F4HANA/pd-p/73554900100800000266)
* [SAP Build Work Zone, advanced edition](https://community.sap.com/t5/c-khhcw49343/SAP%2520Build%2520Work%2520Zone%252C%2520advanced%2520edition/pd-p/73555000100800002781)
* [SAP Build Apps](https://community.sap.com/t5/c-khhcw49343/SAP%2520Build%2520Apps/pd-p/6cfd8176-04ae-4548-8f38-158456e1a47a)
* [SAP Build](https://community.sap.com/t5/c-khhcw49343/SAP%2520Build/pd-p/73555000100700001491)

* [SAP S/4HANA

  SAP S/4HANA](/t5/c-khhcw49343/SAP%2BS%25252F4HANA/pd-p/73554900100800000266)
* [SAP Build Work Zone, advanced edition

  Software Product](/t5/c-khhcw49343/SAP%2BBuild%2BWork%2BZone%25252C%2Badvanced%2Bedition/pd-p/73555000100800002781)
* [SAP Build Apps

  Additional Software Product](/t5/c-khhcw49343/SAP%2BBuild%2BApps/pd-p/6cfd8176-04ae-4548-8f38-158456e1a47a)
* [SAP Build

  Software Product](/t5/c-khhcw49343/SAP%2BBuild/pd-p/73555000100700001491)

View products (4)

**What is SAP Build?**

SAP build is a combination of different intelligent tools such as SAP Build Apps, SAP Build Process Automation, and SAP Build Work Zone advanced edition which helps organizations to create/roll out enterprise applications in no time.

[**SAP Build Work Zone**](https://www.sap.com/products/technology-platform/workzone.html) which helps to create business sites is combined as a package with other tools.  SAP Work Zone enables you to build digital workplace solutions to increase user productivity and engagement. It centralizes access to relevant business applications, processes, information, and communication in a unified entry point that your users can access from any device.

**What you will learn?**

In this blog, we will explore how can we use SAP Build Apps (Formerly known as **AppGyver**) to create an application and render it into a UI Integration card of SAP Work Zone. UI Integration Cards allow displaying of business content from various SAP and third-party applications.

**Pre-Requisites -**

1. Subscription to SAP Build Apps - [SAP Build Apps Free Tier Individual Access](https://blogs.sap.com/2022/11/25/sap-build-apps-free-tier-individual-access/)

2. SAP S/4HANA oData API access (e.g Purchase requisition) / any oData api of your choice which fits your business needs.

**Architecture -**

![](/legacyfs/online/storage/blog_attachments/2022/12/Screenshot-2022-12-19-at-6.15.05-PM.png)

**Steps to create a Web application in SAP Build Apps -**

1. Open the SAP BUILD lobby and create a web application as shown below -

   |
    ![](/legacyfs/online/storage/blog_attachments/2022/12/0-3.png) |
    ![](/legacyfs/online/storage/blog_attachments/2022/12/1-83.png) |
    ![](/legacyfs/online/storage/blog_attachments/2022/12/2-56.png) |

2. Configure oData service under the data section.![](/legacyfs/online/storage/blog_attachments/2022/12/Screenshot-2022-12-19-at-10.14.43-PM.png)

3. All data dependencies are set, and we are good to start the UI development and bind the data to the respective components. Before we do, that, let's disable the navigation and menu option for the application. This will be a full-screen application and will be part of a UI integration card, so doesn't make sense to have it.

   |
    ![](/legacyfs/online/storage/blog_attachments/2022/12/Screenshot-2022-12-19-at-7.20.03-PM.png) |
    ![](/legacyfs/online/storage/blog_attachments/2022/12/Screenshot-2022-12-19-at-2.31.32-PM.png) |

4. Create a UI with a List view showing a list of items (e.g. purchase requisitions).

   |
    ![](/legacyfs/online/storage/blog_attachments/2022/12/10-21.png) |
    ![](/legacyfs/online/storage/blog_attachments/2022/12/Screenshot-2022-12-19-at-10.16.12-PM-1.png) |

5. We are all set to create the build and host it on SAP BTP. Creating a build will take a while as it will be lined up in a queue on the build server, so be patient and have a cup of coffee while it gets ready.

   |
    ![](/legacyfs/online/storage/blog_attachments/2022/12/12-13.png) |
    ![](/legacyfs/online/storage/blog_attachments/2022/12/13-13.png) |

6. Once the build is ready you can download the zip file and unzip it, in the next section we will be deploying this application on cloud foundry runtime.

**Steps to deploy SAP Build apps on BTP Cloud Foundry -**

Unzip the build file and create a manifest file that will include the deployment details. An example is shared below.

```
---

applications:

- name: appgyvercard

  routes:

    - route: appgyvercard.cfapps.euXX.hana.ondemand.com

  path: ./

  memory: 128M

  buildpack: staticfile_buildpack
```

Open the terminal and log in to your CF account and set the correct org and space and deploy the application.

```
sudo cf login -a https://api.cf.euXX.hana.ondemand.com

cf push appgyvercard
```

On the successful deployment of the application, you will be prompted with the application URL, which you have to note as we will be needing it in the next step.

**Steps to integrate UI Integration card in SAP Build Work Zone -**

1. You should be the owner of the workspace or create a new workspace to add a UI integration card widget.![](/legacyfs/online/storage/blog_attachments/2022/12/Screenshot-2022-12-19-at-2.25.52-PM-1.png)

2. Add a widget of type web content and enter the web application details. You have to enter the application URL, which we noted before after deploying the application on BTP CF. After this step, you have successfully added a UI Integration card.

   |
    ![](/legacyfs/online/storage/blog_attachments/2022/12/Screenshot-2022-12-19-at-2.26.02-PM.png) |
    ![](/legacyfs/online/storage/blog_attachments/2022/12/Screenshot-2022-12-19-at-2.26.14-PM.png) |
    ![](/legacyfs/online/storage/blog_attachments/2022/12/Screenshot-2022-12-19-at-2.27.19-PM.png) |

3. Final SAP Build apps in UI integration card in the workspace -![](/legacyfs/online/storage/blog_attachments/...