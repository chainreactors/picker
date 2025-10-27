---
title: SAP CPI: CI/CD from zero to hero – Code inspection and quality control
url: https://blogs.sap.com/2023/02/10/sap-cpi-ci-cd-from-zero-to-hero-code-inspection-and-quality-control/
source: SAP Blogs
date: 2023-02-11
fetch_date: 2025-10-04T06:19:37.419871
---

# SAP CPI: CI/CD from zero to hero – Code inspection and quality control

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Technology](/t5/technology/ct-p/technology)
* [Technology Blog Posts by Members](/t5/technology-blog-posts-by-members/bg-p/technology-blog-members)
* SAP CPI: CI/CD from zero to hero – Code inspection...

Technology Blog Posts by Members

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/technology-blog-members/article-id/159031&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [SAP CPI: CI/CD from zero to hero – Code inspection and quality control](/t5/technology-blog-posts-by-members/sap-cpi-ci-cd-from-zero-to-hero-code-inspection-and-quality-control/ba-p/13543918)

![nunomcpereira](https://avatars.profile.sap.com/7/5/id75d18a481fc978dd268c41afbd23ef5bae60153e3b85cdbe9f34fb1ec47af74b_small.jpeg "nunomcpereira")

[nunomcpereira](https://community.sap.com/t5/user/viewprofilepage/user-id/147300)

Explorer

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=technology-blog-members&message.id=159031)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/technology-blog-members/article-id/159031)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13543918)

‎2023 Feb 10
8:03 PM

[13
Kudos](/t5/kudos/messagepage/board-id/technology-blog-members/message-id/159031/tab/all-users "Click here to see who gave kudos to this post.")

6,230

* SAP Managed Tags
* [SAP Integration Suite](https://community.sap.com/t5/c-khhcw49343/SAP%2520Integration%2520Suite/pd-p/73554900100800003241)
* [Cloud Integration](https://community.sap.com/t5/c-khhcw49343/Cloud%2520Integration/pd-p/67837800100800006801)
* [SAP BTP, Cloud Foundry runtime and environment](https://community.sap.com/t5/c-khhcw49343/SAP%2520BTP%252C%2520Cloud%2520Foundry%2520runtime%2520and%2520environment/pd-p/73555000100800000287)

* [Cloud Integration

  SAP Integration Suite](/t5/c-khhcw49343/Cloud%2BIntegration/pd-p/67837800100800006801)
* [SAP BTP, Cloud Foundry runtime and environment

  SAP Business Technology Platform](/t5/c-khhcw49343/SAP%2BBTP%25252C%2BCloud%2BFoundry%2Bruntime%2Band%2Benvironment/pd-p/73555000100800000287)
* [SAP Integration Suite

  SAP Integration Suite](/t5/c-khhcw49343/SAP%2BIntegration%2BSuite/pd-p/73554900100800003241)

View products (3)

This blog is part of a blog series, so you can find the first page here (<https://blogs.sap.com/2023/02/02/sap-cpi-ci-cd-from-from-zero-to-hero/>). This is the agenda we're following:

* [Backup Binaries and Source Code](https://blogs.sap.com/2023/02/02/sap-cpi-ci-cd-from-from-zero-to-hero/)

* **Code inspection and quality control (explained in this page)**

* [Release management](https://blogs.sap.com/2023/02/15/sap-cpi-ci-cd-from-zero-to-hero-release-management/)

* [Certificates expiration](https://blogs.sap.com/2023/02/23/sap-cpi-ci-cd-from-zero-to-hero-certificates-expiration/)

* [Automated Testing](https://blogs.sap.com/2023/02/28/sap-cpi-ci-cd-from-zero-to-hero-automated-testing/)

* [Documentation](https://blogs.sap.com/2023/03/03/sap-cpi-ci-cd-from-zero-to-hero-documentation/)

* [Code Review](https://blogs.sap.com/2023/03/10/sap-cpi-ci-cd-from-zero-to-hero-code-review/)

# Code inspection and quality control

One of the key aspects of our interfaces is code quality and consistency. Since we have a lot of interfaces we need to make sure that all of them follow our development guidelines framework. After some investigation, I found CPI Lint, an open source github to bring lint into CPI from 7a519509aed84a2c9e6f627841825b5a

![](/legacyfs/online/storage/blog_attachments/2023/02/cpilint-1.png)

CPILint checking code compliance with development guidelines

I think the code is great so a special thanks to Morten for providing such tool. More details about CPI Lint on his github <https://github.com/mwittrock/cpilint> and also on this sap blog <https://blogs.sap.com/2019/02/01/meet-cpilint/>

Despite Morten released version 1.0.4, we're currently using version 1.0.3, and I'm in the process of migrating it to 1.0.4. In summary, the current tool is capable to read the code of an integration flow and check it against the rules defined on a xml file.

Unfortunately, our company has specific guidelines/rules that the "standard" tool does not cover, so I forked Morten repository to allow it to register extension rules by providing these extra rules on a separate project. The forked code (<https://github.com/nunomcpereira/cpilint>) is now able to search for extension jars on the classpath containing extra rules. I also had to make some of the methods public here and there to make it available to use on these extra rules.

CPILint custom (<https://github.com/nunomcpereira/cpilint_custom>) was then born to provide our custom rules only used at our company. Follows the extension rules created and what they do:

* **default-names-not-allowed-rule:** Since CPI has no concept of comments for each component, we want to make sure that we have meaningful names on components that describe the logic of the iflow, so we check that for all possible CPI components we don't have default names such as "*Content Modifier 1*", "*Content Modifier 2*", "*Request Reply 1*" naming or "*groovy1*" for filenames. I heard from Morten that this is now supported on his version 1.0.4, so I'll follow up on that (example below).![](/legacyfs/online/storage/blog_attachments/2023/02/default_names.png)

* **unused-parameters-rule:** How many times have you defined some external parameters that in the end were not used? CPI provides the "*Remove unused parameters*" button which would work in a similar fashion as this rule. This rule just asserts that all your defined parameters are being used (example of the externalized parameters screen below).![](/legacyfs/online/storage/blog_attachments/2023/02/externalized_parameters.png)

* **allowed-headers-empty:** We have main iflows (reached from outside) and internal iflows communicating via process direct. In both scenarios, the "*Allowed headers*" setting being empty might be a problem because the headers would get lost between process direct calls if so. In case of main iflows, there are some headers that we allow to receive like the SapAuthenticatedUserName for instance. Right now according to our rule configuration we're only validating on purpose the communications via process direct, not making it mandatory to receive headers on the main iflow but this is configurable on the rule (example of allowed headers empty below).![](/legacyfs/online/storage/blog_attachments/2023/02/allowed_headers_empty.png)

* **response-headers-allowed:** During developments, we were faced with an issue where a target system was called and returned an invalid header for CPI. I don't remember the details but if I recall it was because the header exceeds the maximum size that CPI can handle. With this error, we learn not to accept \* by default on the response headers of our http calls. This rule is enforcing that (example of usage of response header on http adapter below).![](/legacyfs/online/storage/blog_attachments/2023/02/response_headers_wildcard.png)

* **undeclared-data-type:** During developments we realized that we had a property defined on a content modifier without a type specified and for that particular scenario this resulted on a runtime error since CPI assumed that the property was somehow a complex object when we wanted it t...