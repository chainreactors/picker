---
title: Activating Standard Fiori Applications
url: https://blogs.sap.com/2022/12/22/activating-standard-fiori-applications/
source: SAP Blogs
date: 2022-12-23
fetch_date: 2025-10-04T02:19:51.205507
---

# Activating Standard Fiori Applications

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Technology](/t5/technology/ct-p/technology)
* [Technology Blog Posts by Members](/t5/technology-blog-posts-by-members/bg-p/technology-blog-members)
* Activating Standard Fiori Applications

Technology Blog Posts by Members

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/technology-blog-members/article-id/160245&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [Activating Standard Fiori Applications](/t5/technology-blog-posts-by-members/activating-standard-fiori-applications/ba-p/13551283)

![ChiranjeeviAppapogu_123456789](https://avatars.profile.sap.com/2/5/id2510403e9323cf4150c1970c891200e5d54dbc5ee839bb128cb93a5dd99ee5bb_small.jpeg "ChiranjeeviAppapogu_123456789")

[ChiranjeeviAppapogu\_123456789](https://community.sap.com/t5/user/viewprofilepage/user-id/17415)

Participant

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=technology-blog-members&message.id=160245)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/technology-blog-members/article-id/160245)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13551283)

‎2022 Dec 22
1:59 PM

[7
Kudos](/t5/kudos/messagepage/board-id/technology-blog-members/message-id/160245/tab/all-users "Click here to see who gave kudos to this post.")

32,680

* SAP Managed Tags
* [SAPUI5](https://community.sap.com/t5/c-khhcw49343/SAPUI5/pd-p/500983881501772639608291559920477)
* [SAP Fiori Launchpad](https://community.sap.com/t5/c-khhcw49343/SAP%2520Fiori%2520Launchpad/pd-p/538710751289542466232554247536294)

* [SAPUI5

  Programming Tool](/t5/c-khhcw49343/SAPUI5/pd-p/500983881501772639608291559920477)
* [SAP Fiori Launchpad

  SAP Fiori](/t5/c-khhcw49343/SAP%2BFiori%2BLaunchpad/pd-p/538710751289542466232554247536294)

View products (2)

This Blog post is regarding Activating Standard Fiori Application process.

## **Introduction:**

In this blog post, I would like to work on the process of activating standard fiori application and show that application in fiori launchpad after it got activated. For that we have to follow the process which includes steps as follows....

**Step1:** We should be ready active with our fiori launchpad home page.

**Step2:** In this step, we need to go to the central fiori apps library, here is the link

[https://fioriappslibrary.hana.ondemand.com/sap/fix/externalViewer/#](https://fioriappslibrary.hana.ondemand.com/sap/fix/externalViewer/).

![](/legacyfs/online/storage/blog_attachments/2022/12/Screenshot-400.png)

Fig:1

Here we need to select the fiori standard app based on role or any other app available in app reference library to setup and activate. After selecting standard fiori app, check the configurations of the app which are suitable for on premises S/4 HANA systems.

![](/legacyfs/online/storage/blog_attachments/2022/12/Screenshot-401.png)

                                                                     Fig:2

**Step3:** Now we have to go into Implementation information, here we have to check Front-End components, Back-End components.

![](/legacyfs/online/storage/blog_attachments/2022/12/Screenshot-417.png)

                                                                    Fig:3

In SAP GUI we need to check these Front-End and Back-End components are available or not by using T-Code(SPAM).

![](/legacyfs/online/storage/blog_attachments/2022/12/Screenshot-402.png)

                                                              Fig:4

If those components related info available in GUI, we can proceed to check SAP NOTES in GUI by using T-Code(SNOTE).

![](/legacyfs/online/storage/blog_attachments/2022/12/Screenshot-403.png)

                                                              Fig:5

Click on execute button it will show related info about SAP NOTE for the app.

**Step4:** Within the configuration section the next step is to activate our application by using technical name/ path in the GUI by using SICF/ICF service in T-Code(SICF).

![](/legacyfs/online/storage/blog_attachments/2022/12/Screenshot-418.png)

                                                                       Fig:6

![](/legacyfs/online/storage/blog_attachments/2022/12/Screenshot-404.png)

                                                                  Fig:7

![](/legacyfs/online/storage/blog_attachments/2022/12/Screenshot-405.png)

                                                                        Fig:8

**Step5:** Now we need to use our username to appropriate SAP ROLE in T-Code(PFCG) as detailed on the fiori apps library.

![](/legacyfs/online/storage/blog_attachments/2022/12/Screenshot-419.png)

                                                                     Fig:9

![](/legacyfs/online/storage/blog_attachments/2022/12/Screenshot-421.png)

                                                                 Fig:10

Once created enter the Z version of the required role i.e. Z\_SAP\_BR\_MANAGER. Save it.

![](/legacyfs/online/storage/blog_attachments/2022/12/Screenshot-422.png)

                                                                  Fig:11

**Step6:** After assigning username as role, now we need to setup back-end OData service in the T-Code(/IWND/MAINT\_SERVICE). Here we need to Add Service which is available in the fiori app library for the selected app.

![](/legacyfs/online/storage/blog_attachments/2022/12/Screenshot-420.png)

                                                              Fig:12

![](/legacyfs/online/storage/blog_attachments/2022/12/Screenshot-424.png)

                                                                      Fig:13

After that once again go to PFCG role, change the role with starting **Z**\_**SAP\_BR\_MANAGER** like this and give the authorizations for the role and save. That’s it all done.

Now go to fiori launchpad, refresh and find the standard fiori application activated. Click on “ My Inbox” app to test it works.

![](/legacyfs/online/storage/blog_attachments/2022/12/10-27.png)

                                                                     Fig:14

**Conclusion:**

We have seen complete process of Activating Standard Fiori Application, by using this process we can activate standard fiori application from fiori apps central library to on premise launchpad. If any of the components of standard fiori application (version, software, hardware components, OData service and Role) are not suitable with our on-premises we cannot activate standard fiori applications.

Note\*: all the screenshots attached to the blog post are from my PC only.

Kindly leave any doubts or questions in the comments below.

Thanks & Regards,

Chiranjeevi Appapogu.

* [activating standard fiori apps](/t5/tag/activating%20standard%20fiori%20apps/tg-p/board-id/technology-blog-members)

3 Comments

You must be a registered user to add a comment. If you've already registered, sign in. Otherwise, register and sign in.

* [Comment](/plugins/common/feature/oidcss/sso_login_redirect/providerid/sap_ids_prompt?redirectreason=permissiondenied&referer=https%3A%2F%2Fcommunity.sap.com%2Ft5%2Ftechnology-blog-posts-by-members%2Factivating-standard-fiori-applications%2Fba-p%2F13551283%23comment-on-this)

Copy Link
![](https://community.sap.com/html/@EE5D5986E9F4E5657DCEACB7532B5C39/assets/bluesky-dark.svg)Bluesky
Linkedin

Related Content

* [Flexible Workflows...