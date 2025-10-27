---
title: Transport and Deployment of Artifacts in WEB IDE : HANA XSA
url: https://blogs.sap.com/2022/12/17/transport-and-deployment-of-artifacts-in-web-ide-hana-xsa/
source: SAP Blogs
date: 2022-12-18
fetch_date: 2025-10-04T01:51:50.020161
---

# Transport and Deployment of Artifacts in WEB IDE : HANA XSA

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Technology](/t5/technology/ct-p/technology)
* [Technology Blog Posts by Members](/t5/technology-blog-posts-by-members/bg-p/technology-blog-members)
* Transport and Deployment of Artifacts in WEB IDE :...

Technology Blog Posts by Members

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/technology-blog-members/article-id/160507&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [Transport and Deployment of Artifacts in WEB IDE : HANA XSA](/t5/technology-blog-posts-by-members/transport-and-deployment-of-artifacts-in-web-ide-hana-xsa/ba-p/13552642)

![pallab_haldar](https://avatars.profile.sap.com/4/2/id42d0a352096e2fd071fe39e7ec5b73f1f20abf1d7ce6542aa72c8246918879b7_small.jpeg "pallab_haldar")

[pallab\_haldar](https://community.sap.com/t5/user/viewprofilepage/user-id/594699)

Active Participant

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=technology-blog-members&message.id=160507)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/technology-blog-members/article-id/160507)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13552642)

‎2022 Dec 17
1:36 AM

0
Kudos

2,377

* SAP Managed Tags
* [SAP HANA](https://community.sap.com/t5/c-khhcw49343/SAP%2520HANA/pd-p/73554900100700000996)

* [SAP HANA

  Software Product](/t5/c-khhcw49343/SAP%2BHANA/pd-p/73554900100700000996)

View products (1)

Today I am going to discuss about the Transport and Deployment of Artifacts in WEB IDE : HANA XSA. In the below diagram I am going to discuss about the different deployment option for MTA  Application.

![](/legacyfs/online/storage/blog_attachments/2022/12/Deployment-Architecture.png)

Now describe each and every Application Artifact's deployment process in Details :

**1. Artifact Deployment using SAP ChaRM (**SAP Change Request Management**) :**

A. First Configure **CTS+** for SAP HANA in SAP Solution manager.

Related SAP Link -

[https://wiki.scn.sap.com/wiki/pages/viewpage.action?pageId=447468169#ConfiguringCTS+inSAPSolutionMan...](https://wiki.scn.sap.com/wiki/pages/viewpage.action?pageId=447468169#ConfiguringCTS+inSAPSolutionManager7.1and7.2-1.1.CTS+forSAPHANA)

B. Configure an HTTP Destination .

C. Configure the Transport Organizer  UI.

D. Configure the XSA Transport Landscape .

Reference SAP link -

<https://www.sap.com/documents/2015/07/6ac162e3-527c-0010-82c7-eda71af511fa.html>

E. Configure HANA systems to CHARM as Non SAP system(TMS System Landscape Configuration).
F. Configure source and Target systems.

1. STMS configuration.

2. Define transport routes between the systems in system landscape.

3. Activate extended transport control in TMS

G. Create a CTS Transport using STMS and attach the **.MTAR** archive to the transport and moved to the configured target.

E. Import Manually in Tcode **STMS\_IMPORT** view or

The overall dataflows will look like below for the SAP ChaRM with **CTS+** :

![](/legacyfs/online/storage/blog_attachments/2022/12/cts.png)

<https://assets.cdn.sap.com/sapcom/docs/2016/12/98ccd65a-9c7c-0010-82c7-eda71af511fa.pdf>

**2. Deployment Using GitHub and CI/CD implementation :**

How to integrate GitHub in web IDE and do push and pop operation to put and fetch data from Git and available in the below link -

[https://blogs.sap.com/2022/12/15/mta-project-integration-with-git-in-business-application-studio-han...](https://blogs.sap.com/2022/12/15/mta-project-integration-with-git-in-business-application-studio-hana-xsa/)

Now we will discuss about the Git interaction with CI/CD to automate the code integration -

The configuration steps is given in the GitHub with the below reference link -

<https://github.blog/2022-02-02-build-ci-cd-pipeline-github-actions-four-steps/>

A CI/CD pipeline for SAP HANA extended application services, advanced model comprises the following steps:

* Push your code changes to a source code management (SCM) tool of your choice. In our case it is GIT. The push event to the SCM system triggers the CI process.

* In the CI build, the Cloud MTA Build Tool (MBT) triggers the technology-specific compilers for the respective modules contained in the MTA. For more information, see [Cloud MTA Build Tool![Information published on non-SAP site](https://help.sap.com/doc/3324745951b44b578bd65221d2ff8f9a/Cloud/en-US/themes/sap-light/img/3rd_link.png "Information published on non-SAP site")](https://help.sap.com/docs/link-disclaimer?site=https%3A%2F%2Fsap.github.io%2Fcloud-mta-build-tool%2F "https://sap.github.io/cloud-mta-build-tool/")

* The Cloud MTA Build Tool packages the artifacts from each module into one archive file with the extension `.mtar`.

* The build result is automatically deployed into an environment for automated testing during the CI build. The CI build may contain different tests, such as static code checks for the JavaScript sources  and automated user interface tests .

* The MTA archive is deployed to the production environment.

![](/legacyfs/online/storage/blog_attachments/2022/12/cicd.png)

Reference URL :

[https://help.sap.com/docs/CICD\_OVERVIEW/3324745951b44b578bd65221d2ff8f9a/55242ddaa08d4f3190fd06171b5...](https://help.sap.com/docs/CICD_OVERVIEW/3324745951b44b578bd65221d2ff8f9a/55242ddaa08d4f3190fd06171b5f85f5.html)

**3. Deploy with  XS Deploy using command line or Using Web IDE Interface :**

This deployment of MTAR file is limited within same server instance and between same or different space.

XS advanced runtime is installed in HANA XSA server. But if you want to deploy using command line  from your local machine you follow the below steps :

1. Install XS CLI client tools locally.

2. Configure command-line tools to use the NPM Registry to resolve package dependencies if required.

3. Execute below command to deploy your .mtar file -

A. xs deploy  student.mtar

4.  to check the application use this two command -

A. xs services and xs app.

Reference URL -

[https://help.sap.com/docs/SAP\_HANA\_PLATFORM/400066065a1b46cf91df0ab436404ddc/0919e1cbd20646aead930a5...](https://help.sap.com/docs/SAP_HANA_PLATFORM/400066065a1b46cf91df0ab436404ddc/0919e1cbd20646aead930a5743cfa7e1.html)

You can also deploy the mtar file from Web IDE graphical interfaces  after building the MTAR files-

![](/legacyfs/online/storage/blog_attachments/2022/12/Daploy-Internally-1.png)

4. Deployment by ABAP Transport using SCTS\_HTA\_TOOLS :

To use this deployment ABAP stack should be setup on the SAM SID on top of HANA server.

ABAP transport user to transport the attached MTAR files to the corresponding system and import them to the equivalent XSA space.

The configuration is available in the below link -

<https://launchpad.support.sap.com/#/notes/2569651>

This is all about HANA XSA deployment. Hop it will help.

You must be a registered user to add a comment. If you've already registered, sign in. Otherwise, register and sign in.

* [Comment](/plugins/common/feature/oidcss/sso_login_redirect/providerid/sap_ids_prompt?redirectreason=permissiondenied&referer=https%3A%2F%2Fcommunity.sap.com%2Ft5%2Ftechnology-blog-posts-by-members%2Ftransport-and-deployment-of-artifacts-in-web-ide-hana-xsa%2Fba-p%2F13552642%23comment-on-this)

Copy Link
![](https://community.sap.com/html/@EE5D5986E9F4E5657DCEACB7532B5C39/assets/bluesky-dark.svg)Bluesky
Linkedin

Related Content

* [Building SaaS...