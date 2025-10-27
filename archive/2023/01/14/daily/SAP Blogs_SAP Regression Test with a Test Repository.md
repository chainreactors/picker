---
title: SAP Regression Test with a Test Repository
url: https://blogs.sap.com/2023/01/13/sap-regression-test-with-a-test-repository/
source: SAP Blogs
date: 2023-01-14
fetch_date: 2025-10-04T03:52:48.991209
---

# SAP Regression Test with a Test Repository

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Technology](/t5/technology/ct-p/technology)
* [Technology Blog Posts by SAP](/t5/technology-blog-posts-by-sap/bg-p/technology-blog-sap)
* SAP Regression Test with a Test Repository

Technology Blog Posts by SAP

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/technology-blog-sap/article-id/163543&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [SAP Regression Test with a Test Repository](/t5/technology-blog-posts-by-sap/sap-regression-test-with-a-test-repository/ba-p/13567263)

![frankschwalb](https://avatars.profile.sap.com/e/a/idea83561e63f64cc1a94eb55fe1fa2950c98aaf280f5e1c265233d1ced11e9368_small.jpeg "frankschwalb")

![Product and Topic Expert](/html/@138D6F765B60D7FC0168643DE27D8A68/rank_icons/sap-logo-small-14px.png "Product and Topic Expert")
[frankschwalb](https://community.sap.com/t5/user/viewprofilepage/user-id/45071)

Product and Topic Expert

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=technology-blog-sap&message.id=163543)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/technology-blog-sap/article-id/163543)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13567263)

‎2023 Jan 13
7:40 PM

[9
Kudos](/t5/kudos/messagepage/board-id/technology-blog-sap/message-id/163543/tab/all-users "Click here to see who gave kudos to this post.")

3,351

* SAP Managed Tags
* [SAP Solution Manager](https://community.sap.com/t5/c-khhcw49343/SAP%2520Solution%2520Manager/pd-p/01200615320800000636)
* [Focused Build for SAP Solution Manager](https://community.sap.com/t5/c-khhcw49343/Focused%2520Build%2520for%2520SAP%2520Solution%2520Manager/pd-p/bd524d9b-1ee4-452d-a5b4-c25520976179)
* [SOLMAN Test Suite](https://community.sap.com/t5/c-khhcw49343/SOLMAN%2520Test%2520Suite/pd-p/132949817163443344955330185779754)

* [SAP Solution Manager

  SAP Solution Manager](/t5/c-khhcw49343/SAP%2BSolution%2BManager/pd-p/01200615320800000636)
* [SOLMAN Test Suite

  Software Product Function](/t5/c-khhcw49343/SOLMAN%2BTest%2BSuite/pd-p/132949817163443344955330185779754)
* [Focused Build for SAP Solution Manager

  Software Product Function](/t5/c-khhcw49343/Focused%2BBuild%2Bfor%2BSAP%2BSolution%2BManager/pd-p/bd524d9b-1ee4-452d-a5b4-c25520976179)

View products (3)

A regression test is intended to ensure, that changes in one part of an existing system do not lead to unwanted effects on other areas. It usually consists of repeating existing test cases that retest the entire system or processes and should be performed after changes have been successfully tested. Typically, regressive testing takes place quite late in the test cycle.

Due to the repetitive nature and frequency of these repetitions, it makes sense to use a formalized or automated procedure for regression testing.

For this purpose, we set up and maintain a "global" test case repository, i.e., a central administration and storage of reusable test cases. Optimally, all parties involved have access.

This repository is the basis for manual as well as automated tests.

### **Objective**

A test repository is a collection of test cases for all processes in the system landscape to be regressively tested. Can be used as a scope for all test types and phases. It therefore initially only contains processes that are already used productively.

* Complete: Mapping of all business processes

* Standardised: used as a basis for all test phases in release and rollout projects

* Up-to-date: Changes to and new processes are adopted

![](/legacyfs/online/storage/blog_attachments/2023/01/Picture1-15.png)

### **Advantages**

* High reusability in the context of a wide variety of project types and phases

* Reduction of effort in preparing individual test phases

* Reduction of effort in testing

* Strong standardization of test phases

### **Realization**

Depending on the tools used in a company, all test cases are collected in a test case catalog, e.g. in Excel.

Structured according to the requirements:

* starting with the area, core process and processes

* Priority, test efforts, test relevance for different tests or country

* additional info like Test user, hardware, requirements etc.

are useful information and can be stored in the catalog or test cases. The structure and catalog can be extended at any time depending on new requirements.

A reasonable and flexible numbering makes it easier to find, assign and later test the test cases.

![](/legacyfs/online/storage/blog_attachments/2023/01/2023-01-12_09-51-55.png)

The test cases themselves can be stored in a share or/and in the SAP Solution Manager Solution Documentation (test cases or test steps). All test cases should be maintained with the same template or with test case type test steps. This simplifies the maintenance as well as testing.

If you want to plan a regressive test, you can simply collect the test cases from the defined catalogue as required by business, and the same scope can also be used for recurring tests.

#### **Priority**

* Prio1 (very high) Business core processes (max. 5-7 test cases per WS) -

Assessment by risk: which processes cause the highest costs and/or the highest number of employees unable to work in case of failure? Regressive tests:  test scope for reality testing and are tested in all project types for assurance before handover to the country

* Prio 2 (high): Business-critical processes

Required for daily warehouse operations, i.e. responsible for regularly used physical processes Relevant for error-free inventory management Prio 1 + 2 test cases covers the test scope for comprehensive assurance of system functions, e.g. when commissioning new warehouses in an existing country

* Prio 3 (medium): All other processes

For rollouts in new countries, a 100% test of the system is required, for which Prio 1-3 as well as specific new developments are tested. When new warehouses are commissioned, these test cases are to be tested optionally to increase safety.

* Prio 4 (low):

ggf. special cases, if applicable

For a release, for example, only prio 1&2 test cases can be selected, for a rollout or upgrade project also prio 3&4 test cases. Additional test cases can be easily added as needed. For recurring testing tasks, predefined and coordinated test scopes can be easily created, tested and reported.

The test plans and packages are then created as usual.

### **Versioning & Updating**

With each change introduced into the system, a regressive test may also change, or new ones have to be added, old ones deleted. Time-consuming and unpopular review of test cases should be planned and monitored as an integral part of  the test procedure**.**

During each project/release the business checks whether the existing test cases catalog is still up to date and correspond to the current productive and the changes planned for the project/release (or changes introduced in the meantime) of the processes.

* For deltas, existing test cases are supplemented, or new ones created and, if necessary, stored separately, e.g., proposals for releases or projects.

* Changes are implemented by the business themselves directly in the Excel and test cases/test steps or will be communicated to the test management.

* New test cases can be created by the business to test developments and changes to a release or project.

* At the ...