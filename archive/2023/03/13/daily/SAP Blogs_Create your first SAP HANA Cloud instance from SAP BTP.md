---
title: Create your first SAP HANA Cloud instance from SAP BTP
url: https://blogs.sap.com/2023/03/12/create-your-first-sap-hana-cloud-instance-from-sap-btp/
source: SAP Blogs
date: 2023-03-13
fetch_date: 2025-10-04T09:25:25.382922
---

# Create your first SAP HANA Cloud instance from SAP BTP

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Technology](/t5/technology/ct-p/technology)
* [Technology Blog Posts by Members](/t5/technology-blog-posts-by-members/bg-p/technology-blog-members)
* Create your first SAP HANA Cloud instance from SAP...

Technology Blog Posts by Members

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/technology-blog-members/article-id/163550&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [Create your first SAP HANA Cloud instance from SAP BTP](/t5/technology-blog-posts-by-members/create-your-first-sap-hana-cloud-instance-from-sap-btp/ba-p/13570350)

![azael_navarro](https://avatars.profile.sap.com/d/b/iddba124949f108f3a0cc5a831f7fd1d71c33dd160549d62c2bd0526e2f1af9b64_small.jpeg "azael_navarro")

[azael\_navarro](https://community.sap.com/t5/user/viewprofilepage/user-id/196968)

Active Participant

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=technology-blog-members&message.id=163550)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/technology-blog-members/article-id/163550)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13570350)

‎2023 Mar 12
11:27 AM

[6
Kudos](/t5/kudos/messagepage/board-id/technology-blog-members/message-id/163550/tab/all-users "Click here to see who gave kudos to this post.")

5,635

* SAP Managed Tags
* [SAP HANA Cloud](https://community.sap.com/t5/c-khhcw49343/SAP%2520HANA%2520Cloud/pd-p/73554900100800002881)

* [SAP HANA Cloud

  Software Product](/t5/c-khhcw49343/SAP%2BHANA%2BCloud/pd-p/73554900100800002881)

View products (1)

Dear experts,

After implementing the next tutorial [BTP Onboarding: SAP HANA Cloud](https://www.youtube.com/watch?v=h17LuFK4RHI), as the best step by step tutorial that i found, i would like to share my experience in what i really did in a quick way since i created the HANA instance until i opened my SQL console at first time, so you will win a lot of time trying to access with maybe not required steps that are documented in that great video (if in your case you need to follow all the steps, then feel free to do it in this case i had good luck to find a quick way):

* Search; SAP HANA Cloud and click

![](/legacyfs/online/storage/blog_attachments/2023/03/BTP-App.png)

* Create your instance with hana plan:

![](/legacyfs/online/storage/blog_attachments/2023/03/2-Create-instance.png)

* Dont forget your password, so you need to find the nex json node and then set your password:

"systempassword": "WAO\_Robotics\_HANA\_1",

![](/legacyfs/online/storage/blog_attachments/2023/03/3-JSON.png)

```
{

    "data": {

        "additionalWorkers": 0,

        "availabilityZonePlacement": {

            "highAvailabilityCrossMultiAZEnabled": false,

            "initialReplicaAvailabilityZone": "",

            "initialSourceAvailabilityZone": "",

            "primaryAvailabilityZone": "",

            "secondaryAvailabilityZone": ""

        },

        "edition": "cloud",

        "enabledservices": {

            "docstore": false,

            "scriptserver": false

        },

        "extensionservices": null,

        "memory": 30,

        "memoryScaleOut": 0,

        "productVersion": {

            "id": "",

            "releaseCycle": "",

            "track": ""

        },

        "project_name": "",

        "serviceStopped": false,

        "slaLevel": "standard",

        "storage": 120,

        "systempassword": "WAO_Robotics_HANA_1",

        "template_name": "",

        "update_strategy": "with_restart",

        "vcpu": 2,

        "versionIndicator": "",

        "whitelistIPs": []

    }

}
```

* Your BTP system will start creating your instance:

![](/legacyfs/online/storage/blog_attachments/2023/03/4-Creation.png)

* Once your instance is complete, you will see the status as Created:

![](/legacyfs/online/storage/blog_attachments/2023/03/5-CReated.png)

* Now you need to create a subscription called tools where i didnt configure any service or any complex steps (for me was very simple):

![](/legacyfs/online/storage/blog_attachments/2023/03/6-tools.png)

* Now you need to configure the role collection: SAP HANA Cloud Administrator

![](/legacyfs/online/storage/blog_attachments/2023/03/6-role-collection.png)

* Here there is an step that is not completelly explained in the video, when we can to see in the right menu the tool called: SAP HANA Cloud, you only needs to go to your subaccount for example and click then in "dev" sapce:

![](/legacyfs/online/storage/blog_attachments/2023/03/7-dev.png)

* Now you will find SAP HANA Cloud in the menu:

![](/legacyfs/online/storage/blog_attachments/2023/03/8-menu.png)

* Now if you click in SAP HANA Cloud, you will see your SAP HANA Database Instances:

![](/legacyfs/online/storage/blog_attachments/2023/03/9-instance.png)

* Now you will be able to open the SQL Console:

![](/legacyfs/online/storage/blog_attachments/2023/03/10-sql.png)

* Once you click then you will be requested to add your credentials with your same identity provider user that you gave the role collection:

![](/legacyfs/online/storage/blog_attachments/2023/03/11-sql.png)

* Sometime you will be requested to use an special user and password, so:

User is: DBADMIN

[https://help.sap.com/docs/HANA\_CLOUD\_DATABASE/c82f8d6a84c147f8b78bf6416dae7290/de4ee8bbbb5710148a04f...](https://help.sap.com/docs/HANA_CLOUD_DATABASE/c82f8d6a84c147f8b78bf6416dae7290/de4ee8bbbb5710148a04f023da147c8d.html)

Password: what you added when you created the instance WAO\_Robotics\_HANA\_1

* In the video we are requested to create an instance from SAP HANA Cloud Central, but it is important to say that i didnt create anything, for me was automatic:

![](/legacyfs/online/storage/blog_attachments/2023/03/14-central.png)

![](/legacyfs/online/storage/blog_attachments/2023/03/13-instance.png)

* Even as last configuration if you want to see technical configurations click in the next menu: Manage Configuration option and then even you will confirm the standard user that i explained steps above

![](/legacyfs/online/storage/blog_attachments/2023/03/14-manage.png)

![](/legacyfs/online/storage/blog_attachments/2023/03/15-config.png)

Enjoy it and success!

* [saphana](/t5/tag/saphana/tg-p/board-id/technology-blog-members)
* [SAPHANACLOUD](/t5/tag/SAPHANACLOUD/tg-p/board-id/technology-blog-members)

You must be a registered user to add a comment. If you've already registered, sign in. Otherwise, register and sign in.

* [Comment](/plugins/common/feature/oidcss/sso_login_redirect/providerid/sap_ids_prompt?redirectreason=permissiondenied&referer=https%3A%2F%2Fcommunity.sap.com%2Ft5%2Ftechnology-blog-posts-by-members%2Fcreate-your-first-sap-hana-cloud-instance-from-sap-btp%2Fba-p%2F13570350%23comment-on-this)

Copy Link
![](https://community.sap.com/html/@EE5D5986E9F4E5657DCEACB7532B5C39/assets/bluesky-dark.svg)Bluesky
Linkedin

Related Content

* [Extensibility in the Age of AI: Why ABCD Is Easier (and Smarter) Than You Think](/t5/technology-blog-posts-by-sap/extensibility-in-the-age-of-ai-why-abcd-is-easier-and-smarter-than-you/ba-p/14234516)
  in [Technology Blog Posts by SAP](/t5/technology-blog-posts-by-sap/bg-p/technology-blog-sap)  yesterday
* [S/4HANA transition for US Federal Agencies](/t5/technology-blog-posts-by-sap/s-4hana-transition-for-us-federal-agencies/ba-p/14234423)
  in ...