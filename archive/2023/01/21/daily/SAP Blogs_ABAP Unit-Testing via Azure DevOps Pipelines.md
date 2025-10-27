---
title: ABAP Unit-Testing via Azure DevOps Pipelines
url: https://blogs.sap.com/2023/01/20/abap-unit-testing-via-azure-devops-pipelines/
source: SAP Blogs
date: 2023-01-21
fetch_date: 2025-10-04T04:28:31.491099
---

# ABAP Unit-Testing via Azure DevOps Pipelines

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Technology](/t5/technology/ct-p/technology)
* [Technology Blog Posts by Members](/t5/technology-blog-posts-by-members/bg-p/technology-blog-members)
* ABAP Unit-Testing via Azure DevOps Pipelines

Technology Blog Posts by Members

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/technology-blog-members/article-id/159811&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [ABAP Unit-Testing via Azure DevOps Pipelines](/t5/technology-blog-posts-by-members/abap-unit-testing-via-azure-devops-pipelines/ba-p/13548331)

![felix_fjm](https://avatars.profile.sap.com/3/e/id3e9d41b191f5b8c5f4ed1cba4622a5cfe6d2df409b1572634d1111301f5b0640_small.jpeg "felix_fjm")

[felix\_fjm](https://community.sap.com/t5/user/viewprofilepage/user-id/818549)

Explorer

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=technology-blog-members&message.id=159811)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/technology-blog-members/article-id/159811)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13548331)

‎2023 Jan 20
10:31 PM

[10
Kudos](/t5/kudos/messagepage/board-id/technology-blog-members/message-id/159811/tab/all-users "Click here to see who gave kudos to this post.")

2,947

* SAP Managed Tags
* [ABAP Development](https://community.sap.com/t5/c-khhcw49343/ABAP%2520Development/pd-p/833755570260738661924709785639136)
* [ABAP Testing and Analysis](https://community.sap.com/t5/c-khhcw49343/ABAP%2520Testing%2520and%2520Analysis/pd-p/808952988084195139233186926963168)
* [DevOps](https://community.sap.com/t5/c-khhcw49343/DevOps/pd-p/51112e3c-4b78-4058-a637-67f453c196c9)
* [SAP Continuous Integration and Delivery](https://community.sap.com/t5/c-khhcw49343/SAP%2520Continuous%2520Integration%2520and%2520Delivery/pd-p/73554900100800001771)

* [ABAP Development

  Programming Tool](/t5/c-khhcw49343/ABAP%2BDevelopment/pd-p/833755570260738661924709785639136)
* [ABAP Testing and Analysis

  Programming Tool](/t5/c-khhcw49343/ABAP%2BTesting%2Band%2BAnalysis/pd-p/808952988084195139233186926963168)
* [DevOps

  Programming Tool](/t5/c-khhcw49343/DevOps/pd-p/51112e3c-4b78-4058-a637-67f453c196c9)
* [SAP Continuous Integration and Delivery

  SAP Business Technology Platform](/t5/c-khhcw49343/SAP%2BContinuous%2BIntegration%2Band%2BDelivery/pd-p/73554900100800001771)

View products (4)

## Motivation and Functionality

In this blog we want to show how **ABAP Unit-Tests** can be run from a **CI/CD pipeline**. This is relevant for all applications where automated deployment shall be achieved. We run the respective ABAP Unit-Tests through automatically triggered Azure DevOps pipelines. Graphically **displayed test results** are also desired to be obtained. In the following, I will start by explaining the rough procedure and architecture. A graphical delineation can be viewed in *figure 1*.

ABAP Unit-Tests belonging to an ABAP class are called by an HTTP POST-request in a Node.js-App that executes JavaScript code. The respective ABAP package, which contains the tested ABAP classes, is pushed into a GitHub repository on which we place an Azure DevOps pipeline. Consequently, our Azure DevOps pipeline can be triggered by commits of its underlying GitHub repository, respectively by changes of our ABAP package objects to which belong the tested ABAP classes.

Meanwhile, the respective Node.js-App is pushed into another GitHub repository. This Node.js-App repository is then cloned in our pipeline, so that we are able to run the Node.js-App through running our triggered Azure DevOps pipeline. In doing so we use a different repository than the one in which we store the ABAP package. Otherwise it would be necessary that all the GitHub repositories of all the ABAP packages that shall be tested, and upon which we place Azure DevOps pipelines, contain our Node.js-App. This would be inconvenient and could eventually cause additional maintenance efforts. By cloning a particular Node.js-App repository, we avoid these issues and potential referencing complications.

Altogether, if an ABAP class to be tested is changed and committed into its ABAP package’s GitHub repository, a connected Azure DevOps pipeline will be triggered to run, which starts a Node.js-App that calls Unit-Tests on the ABAP class and delivers JUnit-formatted test results.

Finally, a ready-to-use task in our pipeline enables us to display test results in a JUnit format as expressive graphics in Azure DevOps.

![](/legacyfs/online/storage/blog_attachments/2023/01/figure_1-scaled.jpg)

Figure 1

## Tutorial and Guidance

Initially, we tried to take advantage of the [abap\_test\_runner\_cli](https://www.npmjs.com/package/abap_test_runner_cli), which promised to run Unit-Tests through command line inputs. This nevertheless failed to be integrated in our Azure DevOps pipeline. For further information regarding the abap\_test\_runner\_cli, see [Jakob Marius Kjær’s  blog article](https://blogs.sap.com/2021/09/08/run-your-abap-unit-test-in-ci-pipelines/).

We then switched to Mattias Johansson’s [Node.js-App](https://github.com/trr-official/abapunit2junit), to which we aligned when implementing our Unit-Test-running [Node.js-App](https://github.com/Q-PERIOR/QP_ABAP_Unit-Testing). Detailed explanations of the code and of the functionality of the Node.js-App can be found in [Mattias Johansson’s respective blog article](https://blogs.sap.com/2018/12/17/abap-continuous-integration-with-azure-devops-abap-unit-in-the-cloud/).

Essentially, [our Node.js-App](https://github.com/Q-PERIOR/QP_ABAP_Unit-Testing) first calls an HTTP GET-request to fetch a CSRF-Token needed to run ABAP Unit-Tests. This CSRF-Token is then included in the HTTP POST-request to run the ABAP Unit-Tests. Thereby, a XML-file that contains a call to run ABAP Unit-Tests is used as body. The ABAP Unit-Testing results are then transformed from AUnit to JUnit format by using a XSL-file.

When starting the Node.js-App, SAP-username, SAP-password, the ABAP-Package containing the ABAP classes to be tested, and the path of the file for test-results have to be specified by the user - for example as follows:

*npm start -- --username=<SAP-User> --password=<SAP-Password> --package=<Z2607\_AZURE\_UNIT\_TEST> --file=<result/abapResultFile.xml>*

The target file is optional. If not specified, a default file will be chosen. This target file contains the XML-formatted test results of our ABAP Unit-Tests.

Now, the Unit-Testing Node.js-App and the ABAP package which contains the ABAP classes to be tested should be integrated into an Azure DevOps pipeline. Therefore, we first push the respective ABAP package in a GitHub repository. This GitHub repository is then used to build an Azure DevOps pipeline, so that a commit in this ABAP package repository can be used as pipeline trigger.

*Figure 2* shows in *line* 6 that our pipeline is triggered by commits of the underlying GitHub repository’s main branch. Further on, Node.js has to be installed.

![](/legacyfs/online/storage/blog_attachments/2023/01/figure_2-3.jpg)

Figure 2

As seen in *figure 3*, we then clone a second GitHub repository, which consists of our Node.js-App.

![](/legacyfs/online/storage/blog_attachments/2023/01/figure_3.jpg)

Figure 3

The cloned GitHub repository is stored in a working dictionary which has the same name...