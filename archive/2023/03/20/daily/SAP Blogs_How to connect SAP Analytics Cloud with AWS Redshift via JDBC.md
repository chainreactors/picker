---
title: How to connect SAP Analytics Cloud with AWS Redshift via JDBC
url: https://blogs.sap.com/2023/03/19/how-to-connect-sap-analytics-cloud-with-aws-redshift-via-jdbc/
source: SAP Blogs
date: 2023-03-20
fetch_date: 2025-10-04T10:05:00.669766
---

# How to connect SAP Analytics Cloud with AWS Redshift via JDBC

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Technology](/t5/technology/ct-p/technology)
* [Technology Blog Posts by Members](/t5/technology-blog-posts-by-members/bg-p/technology-blog-members)
* How to create an imported connection between SAP A...

Technology Blog Posts by Members

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/technology-blog-members/article-id/160622&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [How to create an imported connection between SAP Analytics Cloud and AWS Redshift](/t5/technology-blog-posts-by-members/how-to-create-an-imported-connection-between-sap-analytics-cloud-and-aws/ba-p/13553285)

![carlospinto](https://avatars.profile.sap.com/6/c/id6c614dc6094e62e2119ab9e41fec49abe5ce9030a4bf8bd4d3c76974185f1e33_small.jpeg "carlospinto")

[carlospinto](https://community.sap.com/t5/user/viewprofilepage/user-id/14727)

Active Participant

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=technology-blog-members&message.id=160622)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/technology-blog-members/article-id/160622)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13553285)

‎2023 Mar 19
6:15 PM

[9
Kudos](/t5/kudos/messagepage/board-id/technology-blog-members/message-id/160622/tab/all-users "Click here to see who gave kudos to this post.")

5,994

* SAP Managed Tags
* [SAP Analytics Cloud](https://community.sap.com/t5/c-khhcw49343/SAP%2520Analytics%2520Cloud/pd-p/67838200100800006884)
* [SAP Java Virtual Machine](https://community.sap.com/t5/c-khhcw49343/SAP%2520Java%2520Virtual%2520Machine/pd-p/01200615320800003576)
* [Cloud Connector](https://community.sap.com/t5/c-khhcw49343/Cloud%2520Connector/pd-p/0f95abc4-29f3-477d-874c-7c758b81f779)
* [SAP HANA Cloud](https://community.sap.com/t5/c-khhcw49343/SAP%2520HANA%2520Cloud/pd-p/73554900100800002881)
* [SAP HANA Cloud, SAP HANA database](https://community.sap.com/t5/c-khhcw49343/SAP%2520HANA%2520Cloud%252C%2520SAP%2520HANA%2520database/pd-p/ada66f4e-5d7f-4e6d-a599-6b9a78023d84)
* [SAP Business Technology Platform](https://community.sap.com/t5/c-khhcw49343/SAP%2520Business%2520Technology%2520Platform/pd-p/73555000100700000172)

* [SAP Analytics Cloud

  SAP Analytics Cloud](/t5/c-khhcw49343/SAP%2BAnalytics%2BCloud/pd-p/67838200100800006884)
* [SAP Java Virtual Machine

  SAP Java Virtual Machine](/t5/c-khhcw49343/SAP%2BJava%2BVirtual%2BMachine/pd-p/01200615320800003576)
* [Cloud Connector

  Additional Software Product](/t5/c-khhcw49343/Cloud%2BConnector/pd-p/0f95abc4-29f3-477d-874c-7c758b81f779)
* [SAP HANA Cloud

  Software Product](/t5/c-khhcw49343/SAP%2BHANA%2BCloud/pd-p/73554900100800002881)
* [SAP HANA Cloud, SAP HANA database

  Additional Software Product](/t5/c-khhcw49343/SAP%2BHANA%2BCloud%25252C%2BSAP%2BHANA%2Bdatabase/pd-p/ada66f4e-5d7f-4e6d-a599-6b9a78023d84)
* [SAP Business Technology Platform

  Software Product](/t5/c-khhcw49343/SAP%2BBusiness%2BTechnology%2BPlatform/pd-p/73555000100700000172)

View products (6)

In this blog post, I will explain how to connect SAP Analytics Cloud with AWS Redshift using SAP Cloud Connector and Cloud Agent. I have ordered and completed the information found on the [SAP Help Portal](http://help.sap.com) based on my personal experience to clarify the doubts raised in this [question](https://answers.sap.com/questions/12897059/sap-analytics-cloud-integration-with-aws-redshift.html).

This is an **Imported Data connection** that extracts the data from the source system and upload it to the cloud. If you need a Live Data connection, you can use a HANA Cloud instance on BTP or a third-party software. Please check my blog post for a step-by-step guide: [How to create a live connection between SAP Analytics Cloud and AWS Redshift](https://community.sap.com/t5/technology-blogs-by-members/how-to-create-a-live-connection-between-sap-analytics-cloud-and-aws/ba-p/13916903).

I had some issues with the SAC Agent Simple Deployment Kit, so I decided to install the components separately: Cloud Connector, Cloud Agent, Apache Tomcat, JVM (Java Virtual Machine), JDK (Java Development Kit) and JDBC driver.

It is recommended to install them together on a dedicated server to avoid slowness or downtime. Once all the components are up and running, we will be able to create a connection from SAC to Redshift.

Here is the [link](https://help.sap.com/docs/SAP_ANALYTICS_CLOUD/00f68c2e08b941f081002fd3691d86a7/0d5ffbb6951b45778c1a90ffd0114f04.html?locale=en-US) I mainly used and these are the steps to follow. If you are struggling with some point, please leave a comment, and I will try to help.

1. Install JVM
2. Install Cloud Connector
3. Install JDK
4. Install Apache Tomcat
5. Deploy Cloud Agent on Apache Tomcat
6. Configure Cloud Connector
7. Configure Cloud Agent in SAC
8. Install JDBC driver
9. Create connection in SAC

![](/legacyfs/online/storage/blog_attachments/2023/03/Integration-architecture.jpg)

*Integration architecture*

**Step 1 - Install JVM**

1.1.- Download the JVM [here](https://tools.hana.ondemand.com/#cloud). I chose sapjvm-8.1.090-windows-x64.zip

1.2.- Extract it to *C:\1\_JVM\sapjvm\_8*

**Step 2 - Install Cloud Connector**

This step is explained [here](https://help.sap.com/docs/connectivity/sap-btp-connectivity-cf/installation). Please find below the steps to follow:

2.1.- Download the Cloud Connector [here](https://tools.hana.ondemand.com/#cloud). I chose sapcc-2.14.2-windows-x64.msi

2.2.- Extract it to *C:\2\_SCC*

2.3.- Install it following this [link](https://help.sap.com/docs/connectivity/sap-btp-connectivity-cf/installation). I installed it on Microsoft Windows OS. I selected the JVM folder (*C:\1\_JVM\sapjvm\_8*) for the JDK during the installation

2.4.- After installation, you can start and stop it via shortcuts on the desktop, or by using the Windows Services manager

**Step 3 - Install JDK**

3.1.- Download the JDK [here](https://www.oracle.com/java/technologies/downloads/#jdk19-windows). I chose jdk-19\_windows-x64\_bin.msi

3.2.- Extract it to *C:\3\_JDK*

**Step 4 - Install Apache Tomcat**

4.1.- Download the Apache Tomcat [here](https://tomcat.apache.org/download-90.cgi). I chose 64-bit Windows zip (apache-tomcat-9.0.67.exe)

4.2.- Double-click the .exe file to start the installation

4.3.- During the installation, enter the Administrator login credentials, select *C:\3\_JDK* folder for the JDK, and *C:\4\_Tomcat* folder as destination

4.4.- Start your Web browser and open <http://localhost:8080> to verify the installation

**Step 5 - Deploy Cloud Agent on Apache Tomcat**

This step is explained [here](https://help.sap.com/doc/00f68c2e08b941f081002fd3691d86a7/2023.2/en-US/7c35129451f5432194773adac7f89598.html). Please find below the steps to follow:

5.1.- Download the Cloud agent [here](https://launchpad.support.sap.com/#/softwarecenter)

5.2.- Extract the package and copy the file C4A\_AGENT.war to *C:\4\_Tomcat\webapps*

5.3.- Create a user with the Services role in tomcat-users.xml file. This user will be needed when creating the connection in SAC

5.4.- Restart the Tomcat service and test if the deployment was successful by opening <http://localhost:8080/C4A_AGENT/deploymentInfo>. The version of the Cloud agent should be displayed.

**Step 6 - Configure Cloud Connector**

Access the Cloud Connector administration at <https...