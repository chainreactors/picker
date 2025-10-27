---
title: Transporting BPC Security profiles, teams for BPC4HANA. DoNotUse PFCG. Guide to transport BPC security Profiles, teams.
url: https://blogs.sap.com/2023/03/26/transporting-bpc-security-profiles-teams-for-bpc4hana.-donotuse-pfcg./
source: SAP Blogs
date: 2023-03-27
fetch_date: 2025-10-04T10:45:54.198807
---

# Transporting BPC Security profiles, teams for BPC4HANA. DoNotUse PFCG. Guide to transport BPC security Profiles, teams.

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Financial Management](/t5/financial-management/ct-p/financial-management)
* [Financial Management Blog Posts by Members](/t5/financial-management-blog-posts-by-members/bg-p/financial-management-blog-members)
* Transporting BPC Security profiles, teams for BPC4...

Financial Management Blog Posts by Members

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/financial-management-blog-members/article-id/5377&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [Transporting BPC Security profiles, teams for BPC4HANA. DoNotUse PFCG. Guide to transport BPC security Profiles, teams.](/t5/financial-management-blog-posts-by-members/transporting-bpc-security-profiles-teams-for-bpc4hana-donotuse-pfcg-guide/ba-p/13560079)

![SahilTaneja](https://avatars.profile.sap.com/1/9/id191a4929460b85f2bded0488be11e85d5e9a171b71d0c87e93883d40204aba38_small.jpeg "SahilTaneja")

[SahilTaneja](https://community.sap.com/t5/user/viewprofilepage/user-id/606691)

Participant

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=financial-management-blog-members&message.id=5377)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/financial-management-blog-members/article-id/5377)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13560079)

‎2023 Mar 26
7:49 PM

[3
Kudos](/t5/kudos/messagepage/board-id/financial-management-blog-members/message-id/5377/tab/all-users "Click here to see who gave kudos to this post.")

2,154

* SAP Managed Tags
* [SAP Business Planning and Consolidation, version for SAP NetWeaver](https://community.sap.com/t5/c-khhcw49343/SAP%2520Business%2520Planning%2520and%2520Consolidation%252C%2520version%2520for%2520SAP%2520NetWeaver/pd-p/01200615320800001016)
* [Security](https://community.sap.com/t5/c-khhcw49343/Security/pd-p/49511061904067247446167091106425)

* [SAP Business Planning and Consolidation, version for SAP NetWeaver

  Software Product](/t5/c-khhcw49343/SAP%2BBusiness%2BPlanning%2Band%2BConsolidation%25252C%2Bversion%2Bfor%2BSAP%2BNetWeaver/pd-p/01200615320800001016)
* [Security

  Topic](/t5/c-khhcw49343/Security/pd-p/49511061904067247446167091106425)

View products (2)

Transporting BPC profiles is a tedious process than the one we usually follow for FIORI and PFCG roles.

\*Never transport BPC profiles through PFCG.

\*\* BPC auto generated role for Teams or profiles can differ in name in different environments in same landscape. For example, you created a BPC profile directly in test system, which got name ZBPC\_\*\*\*\*\*\*06. And in dev system, there is one profile which needs to be transported to Production with name ZBPC\_\*\*\*\*\*\*06, if moved through PFCG will replace the existing profile. SO its always a better idea to move profiles through RSA1.

Steps to transport.

1. Create a new Customizing TR through charm or directly.

2. Go to RSA1 tcode.

3. You might see below warning, just press continue, another topic for another day ![:winking_face:](/html/@04D3FD3B132035083B4AC3194BC6AF8A/emoticons/1f609.png ":winking_face:") :

![](/legacyfs/online/storage/blog_attachments/2023/03/1-65.png)

Warning when opened RSA1

4.    The RSA1 tcode starts in Administration tab by default. Click on Transport Connection.

![](/legacyfs/online/storage/blog_attachments/2023/03/2-45.png)

5.      Before you select the objects, first set the Collection Mode to Collect Automatically:

![](/legacyfs/online/storage/blog_attachments/2023/03/3-42.png)

Collect Automatically to enable Checkbox option

6.     Then navigate to the More Types -> Environment and Click on Select Objects. The pop up will appear with all the environments available. Select the one, for which you want to transport the profiles, teams.

![](/legacyfs/online/storage/blog_attachments/2023/03/4-29.png)

Select the Environment

7.     By default, all the objects (profiles, teams, models, dimensions) in that environment will be selected:

![](/legacyfs/online/storage/blog_attachments/2023/03/5-30.png)

All options are selected by default

FYI – I am trying to hide all the custom objects with Blue pen, which I have created. So please ignore that.

8.     We don’t want to transport any functional objects for sure. So, please click on “Do not Transport Any Below” by right clicking on the environment.

![](/legacyfs/online/storage/blog_attachments/2023/03/6-21.png)

Select Do no transport any below option to uncheck all objects

9.

1. Everything will be unchecked, now navigate to Teams, Data Access profiles and Task profiles. And click the ones you want to transport.

\*\*\*Please note that in case you are transporting Team, please make sure you select the relevant Data Access profile and Task Profile too, else the TR will be moved with RC = 0 but the objects won’t move.

After selecting the objects, please click on mini truck button, we are familiar with and have been doing all our life:

![](/legacyfs/online/storage/blog_attachments/2023/03/6.1.png)

Usual truck button for transport

10.    While releasing the TR, you will see the warning about dependent objects in your data access profiles, i.e., Environment, Model, Dimensions and Dimension members referenced:

![](/legacyfs/online/storage/blog_attachments/2023/03/7-22.png)

Warning on the dependent Objects such as Env, Model, Dimensions and Dimension Members

\*\*\*\*Since we are referencing Models and dimensions in our data access profiles, it makes us dependent on Functional teams. So please make sure model and dimension including dimension members are transported before you transport security profile, else the TR will end up in RC 8.

\*\*\*\*\*make sure you Make the environment status Offline before you move your TR, else the TR will again end up in RC = 8.

So essentially, all the BPC transports cause a Downtime unless you enable users with task “Use System When Offline” which is definitely not a good idea.

\*\*\*\*\*\* Once you move your objects successfully, refer to UJE\_\*\_AGR tables accordingly to map your composites to BPC roles. Its always a good practice to map task and data profiles to a team and assign the team specific role to user referring from table UJE\_TEAM\_AGR.

I am sure, there must be other ways to transport BPC security profiles and teams, but I find this one relatively easier than others. But still open to suggestions. Thanks for reading this. Let me know, in case of any questions.

* [bpc data access profile](/t5/tag/bpc%20data%20access%20profile/tg-p/board-id/financial-management-blog-members)
* [bpc security](/t5/tag/bpc%20security/tg-p/board-id/financial-management-blog-members)
* [BPC task profile](/t5/tag/BPC%20task%20profile/tg-p/board-id/financial-management-blog-members)
* [bpc teams](/t5/tag/bpc%20teams/tg-p/board-id/financial-management-blog-members)
* [bpc transport guide](/t5/tag/bpc%20transport%20guide/tg-p/board-id/financial-management-blog-members)
* [transport](/t5/tag/transport/tg-p/board-id/financial-management-blog-members)

You must be a registered user to add a comment. If you've already registered, sign in. Otherwise, register and sign in.

* [Comment](/plugins/common/feature/oidcss/sso_login_redirect/providerid/sap_ids_prompt?redirectreason=permissiondenied&referer=https%3A%2F%2Fcommunity.sap.com%2Ft5%2Ffinancial-management-blog-posts-by-members%2Ftransporting-bpc-security-pro...