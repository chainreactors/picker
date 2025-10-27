---
title: SAP Datasphere – SAP Data Provisioning Agent Upgrade
url: https://blogs.sap.com/2023/04/07/sap-datasphere-sap-data-provisioning-agent-upgrade/
source: SAP Blogs
date: 2023-04-08
fetch_date: 2025-10-04T11:30:26.339095
---

# SAP Datasphere – SAP Data Provisioning Agent Upgrade

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Technology](/t5/technology/ct-p/technology)
* [Technology Blog Posts by Members](/t5/technology-blog-posts-by-members/bg-p/technology-blog-members)
* SAP Datasphere – SAP Data Provisioning Agent Upgra...

Technology Blog Posts by Members

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/technology-blog-members/article-id/163430&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [SAP Datasphere – SAP Data Provisioning Agent Upgrade](/t5/technology-blog-posts-by-members/sap-datasphere-sap-data-provisioning-agent-upgrade/ba-p/13569884)

![akhilesh_pandey](https://avatars.profile.sap.com/1/9/id1985a01c09d5a0265cb652d86b08c78136e17ccdb8c1788fcddbb1a217e84f32_small.jpeg "akhilesh_pandey")

[akhilesh\_pandey](https://community.sap.com/t5/user/viewprofilepage/user-id/135401)

Explorer

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=technology-blog-members&message.id=163430)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/technology-blog-members/article-id/163430)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13569884)

‎2023 Apr 07
8:18 PM

[10
Kudos](/t5/kudos/messagepage/board-id/technology-blog-members/message-id/163430/tab/all-users "Click here to see who gave kudos to this post.")

14,412

* SAP Managed Tags
* [SAP Datasphere](https://community.sap.com/t5/c-khhcw49343/SAP%2520Datasphere/pd-p/73555000100800002141)
* [SAP HANA smart data integration](https://community.sap.com/t5/c-khhcw49343/SAP%2520HANA%2520smart%2520data%2520integration/pd-p/73554900100800000033)

* [SAP HANA smart data integration

  SAP HANA](/t5/c-khhcw49343/SAP%2BHANA%2Bsmart%2Bdata%2Bintegration/pd-p/73554900100800000033)
* [SAP Datasphere

  Software Product](/t5/c-khhcw49343/SAP%2BDatasphere/pd-p/73555000100800002141)

View products (2)

**Introduction:**

This blog is about updating the SAP Data Provisioning agent which is also known as “DP Agent” (On windows). The Data Provisioning Agent provides secure connectivity between the SAP HANA database and you’re on premise, adapter-based sources. The DP Agent control all SAP HANA smart data integration (SDI)  Adapters and connections to HANA database. It acts as the communication interface between HANA and the Adapter.

SAP Datasphere allows you to use SAP HANA smart data integration (SDI) and its Data Provisioning Agent to enable on-premise connections. To do this, you first have to download and install the SDI Data Provisioning agent to a network location from which it can establish HTTPS connections to SAP HANA on Cloud.

With latest update of SAP Datasphere, it offers more Adapters – ABAP Adapter, HANA Adapter, MssqlLogReaderAdapter, OracleLogReader Adapter, CloudDataIntergation Adapter, CamelJdbc Adapter.

![](/legacyfs/online/storage/blog_attachments/2023/04/Image1.jpg)

We will cover the upgrading the Data Provisioning Agent installed on windows box by running the installation program in update mode.

**Pre-requisite:**

As per SAP recommendation, before upgrading the Data Provisioning Agent, make sure that your SAP HANA server has already been updated to the same version of your target version of DP agent.

To check your current version (On windows): -

* Open the versions.txt file. The default path to the file on windows is drive:\*\*\*\*\dataprovagent\versions.txt and look for dpagent.version to confirm the Data Provisioning agent version. Example : dpagent.version=2.6.1.1

OR

Open windows command prompt and navigate to <DPAgent\_root>/bin directory and enter the command to <DPAgent\_root>/bin/\agentcli.bat –configAgent,

![](/legacyfs/online/storage/blog_attachments/2023/04/Image2.jpg)

* To view the version of DP agent, select Enter Option 11 and that’s shows your current version

![](/legacyfs/online/storage/blog_attachments/2023/04/Image3.jpg)

**Execution Steps as below:**

Step1. Login to SAP portal - <https://launchpad.support.sap.com/> and download the latest available DP Agent version (to download the software follow the patch shared in below screenshot) and extract this to an empty directory.

![](/legacyfs/online/storage/blog_attachments/2023/04/Image4.jpg)

Step2. Stop the running SAP HANA Data Provisioning Agent service, in windows you can do it by using Option1- Services manager in Control Panel and other Option2 by command prompt using DP Agent Configuration Tool. Below screen show for Option 2.

Open cmd and enter the command to *<DPAgent\_root>/bin/\agentcli.bat –configAgent*

![](/legacyfs/online/storage/blog_attachments/2023/04/Image5.jpg)

further you can validate the services from services.msc

Step3. Now go to the directory where software is extracted & click on hdbinst.exe  and run as  administrator, there you will get list of all selection for existing DP agents installed and new installation option with detailed of there versions, here we are going with existing one and select the option accordingly-

![](/legacyfs/online/storage/blog_attachments/2023/04/Image6.jpg)

Step4. So here I took option 1 to upgrade the version & further it will ask you to manually enter the Domain\username for agent service  & Password for Agent Service

![](/legacyfs/online/storage/blog_attachments/2023/04/Image7.jpg)

Here, your upgarde completed and you can check the logs under path –                       C:\Users\\*\*\*\*\*\* \AppData\Local\Temp\hdb\_dataprovagent\_\*\*\*\*

Step5. Validation – to check the version and Agent status, you can check with DPAgent Configuration tool - Open cmd and enter the command to *<DPAgent\_root>/bin/\agentcli.bat –configAgent*

![](/legacyfs/online/storage/blog_attachments/2023/04/Image8.jpg)

![](/legacyfs/online/storage/blog_attachments/2023/04/Image9.jpg)

\*\*you can check service in windows from servcies.msc as well and perform start/stop of servcies from DP agent configuration tool. Also in windows the agent service is re-created and started automatically

Since, the Agent is already registerd on your SAP Datasphere- you can validate the status by login to SAP Datasphere -> System->Configuration-> Data Integartion -> On premise Agents ->Adapters Tab

![](/legacyfs/online/storage/blog_attachments/2023/04/Image10.jpg)

You will find the status must be green and showing the current updated version i.e *2.6.3.4* from *2.6.1.1*

**Conclusion:**

This concludes the DP Agent upgrade to latest available version installed on windows box.

*In Linux – steps will be same just below command will be different*

*Start/stop services - navigate to <DPAgent\_root>/bin, and run ./dpagent\_servicedaemon.sh stop or start  & To start the installation manager run ./hdbsetup*

Thanks for reading this article, Looking forward for your valuable feedback and comments !!

**Reference:**

[https://help.sap.com/docs/HANA\_SMART\_DATA\_INTEGRATION/7952ef28a6914997abc01745fef1b607/23b6324923dc4...](https://help.sap.com/docs/HANA_SMART_DATA_INTEGRATION/7952ef28a6914997abc01745fef1b607/23b6324923dc4f499425931311bad5ae.html)

1 Comment

You must be a registered user to add a comment. If you've already registered, sign in. Otherwise, register and sign in.

* [Comment](/plugins/common/feature/oidcss/sso_login_redirect/providerid/sap_ids_prompt?redirectreason=permissiondenied&referer=https%3A%2F%2Fcommunity.sap.com%2Ft5%2Ftechnology-blog-posts-by-members%2Fsap-datasphere-sap-data-pr...