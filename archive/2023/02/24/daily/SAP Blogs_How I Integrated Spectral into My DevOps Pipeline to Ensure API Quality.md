---
title: How I Integrated Spectral into My DevOps Pipeline to Ensure API Quality
url: https://blogs.sap.com/2023/02/23/how-i-integrated-spectral-into-my-devops-pipeline-to-ensure-api-quality/
source: SAP Blogs
date: 2023-02-24
fetch_date: 2025-10-04T07:57:57.664186
---

# How I Integrated Spectral into My DevOps Pipeline to Ensure API Quality

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Technology](/t5/technology/ct-p/technology)
* [Technology Blog Posts by Members](/t5/technology-blog-posts-by-members/bg-p/technology-blog-members)
* How I Integrated Spectral into My DevOps Pipeline ...

Technology Blog Posts by Members

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/technology-blog-members/article-id/161055&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [How I Integrated Spectral into My DevOps Pipeline to Ensure API Quality](/t5/technology-blog-posts-by-members/how-i-integrated-spectral-into-my-devops-pipeline-to-ensure-api-quality/ba-p/13556280)

![SirtiB](https://avatars.profile.sap.com/d/3/idd35fed74069fd910ddc4ad3ce9a31c489883c321b9aaf7ce54cd18d2d9984c54_small.jpeg "SirtiB")

[SirtiB](https://community.sap.com/t5/user/viewprofilepage/user-id/125434)

Explorer

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=technology-blog-members&message.id=161055)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/technology-blog-members/article-id/161055)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13556280)

‎2023 Feb 23
10:30 PM

[4
Kudos](/t5/kudos/messagepage/board-id/technology-blog-members/message-id/161055/tab/all-users "Click here to see who gave kudos to this post.")

1,799

* SAP Managed Tags
* [SAP Integration Suite](https://community.sap.com/t5/c-khhcw49343/SAP%2520Integration%2520Suite/pd-p/73554900100800003241)
* [API Management](https://community.sap.com/t5/c-khhcw49343/API%2520Management/pd-p/67838200100800006828)

* [API Management

  SAP Business Technology Platform](/t5/c-khhcw49343/API%2BManagement/pd-p/67838200100800006828)
* [SAP Integration Suite

  SAP Integration Suite](/t5/c-khhcw49343/SAP%2BIntegration%2BSuite/pd-p/73554900100800003241)

View products (2)

Currently, I am focusing extensively on Continuous Integration and Deployment (CI/CD) within the context of integration. My ultimate objective is to not only guarantee the safety of my integration processes during development and deployment but also to automate the process using a suitable set of rules.

In this context, I came across Vadim Klimov's blog post titled "Enforcement of Compliance with a Style Guide," which has inspired me to delve deeper into the topic of API linting.

<https://blogs.sap.com/2022/10/18/api-contract-enforcement-of-compliance-with-a-style-guide/>

I came to recognize the importance of using API linting tools and adhering to style guides. Consequently, I decided to incorporate Spectral into my DevOps pipeline to ensure that my APIs adhere to the required standards.

Spectral is a valuable tool for maintaining APIs, as it performs API linting by checking specifications against a custom set of rules and ensuring they adhere to defined structures. It provides a range of built-in lint rules, which cover a wide range of potential issues with your API specification. It also allows you to write your own custom rules, which makes it highly customizable. By integrating Spectral into my build and deployment process, I was able to analyze the results and make improvements to my APIs to ensure they met the desired standards. To test this integration, I created a simple example YAML file to establish a pipeline. The code for this YAML file is as follows:

```
trigger:

- master

variables:

  CONFIG_PATH: '$(Build.SourcesDirectory)/spectral.yaml'

steps:

- script: |

    npx @stoplight/spectral-cli lint "$(Build.SourcesDirectory)/SBU/spectral.yml" -r $CONFIG_PATH -o "$(Build.SourcesDirectory)/test-results/spectral-results.xml" -f junit

  displayName: 'Spectral Linting'

  continueOnError: false

- task: PublishTestResults@2

  inputs:

    testResultsFormat: 'JUnit'

    testResultsFiles: '$(Build.SourcesDirectory)/test-results/spectral-results.xml'

    failTaskOnFailedTests: true

    testRunTitle: 'Spectral Linting Results'

  displayName: 'Publish Spectral Test Results'
```

The trigger "master" indicates that the pipeline is triggered when changes are made to the master branch of the repository. The pipeline contains a variable CONFIG\_PATH that contains the path to the Spectral configuration file. In the first step, the script npx @stoplight/spectral-cli lint is executed to check the API specification. The configuration file is referenced via the variable CONFIG\_PATH, and the results of the check are saved in the JUnit format in the spectral-results.xml file. If errors occur during the check, the task will mark the pipeline as failed.

Once my pipeline has successfully completed, the following output will be displayed:

![](/legacyfs/online/storage/blog_attachments/2023/02/Unbenanntes-Bild.png)

The image depicts a pipeline run that was successful.

The pipeline has run successfully and a subsequent process could now deploy the API.

In case of an error, the following would be displayed:

![](/legacyfs/online/storage/blog_attachments/2023/02/Unbenanntes-Bild-1.png)

The image shows a pipeline run that encountered errors.

![](/legacyfs/online/storage/blog_attachments/2023/02/Unbenanntes-Bild-2.png)

This image displays the linting results along with an XML attachment.

My pipeline has failed and is recorded in my test run report. Spectral has determined the exact cause for me and saved it in a separate file. In addition to being able to monitor the quality of development, I can also ensure that the APIs are deployed only if they comply with my defined ruleset.

The integration of Spectral into my DevOps pipeline has enhanced the quality and standards compliance of my APIs. Encouraging the adoption of API linting tools like Spectral in DevOps practices is crucial to ensure high-quality and standardized APIs. Additionally, it alleviates the need to ensure that every developer has set up the required prerequisites locally and allows me to safely enforce my ruleset through the pipeline.

What measures have you taken so far to ensure the quality of your API development?

* [cicd](/t5/tag/cicd/tg-p/board-id/technology-blog-members)
* [linter](/t5/tag/linter/tg-p/board-id/technology-blog-members)
* [Spectral](/t5/tag/Spectral/tg-p/board-id/technology-blog-members)

You must be a registered user to add a comment. If you've already registered, sign in. Otherwise, register and sign in.

* [Comment](/plugins/common/feature/oidcss/sso_login_redirect/providerid/sap_ids_prompt?redirectreason=permissiondenied&referer=https%3A%2F%2Fcommunity.sap.com%2Ft5%2Ftechnology-blog-posts-by-members%2Fhow-i-integrated-spectral-into-my-devops-pipeline-to-ensure-api-quality%2Fba-p%2F13556280%23comment-on-this)

Copy Link
![](https://community.sap.com/html/@EE5D5986E9F4E5657DCEACB7532B5C39/assets/bluesky-dark.svg)Bluesky
Linkedin

Related Content

* [A GitHub action to update tenant subscriptions for multitenant SaaS applications on BTP](/t5/technology-blog-posts-by-members/a-github-action-to-update-tenant-subscriptions-for-multitenant-saas/ba-p/14181456)
  in [Technology Blog Posts by Members](/t5/technology-blog-posts-by-members/bg-p/technology-blog-members)  2025 Sep 02
* [Migration SAP PI/PO to SAP Cloud Integration using Pipeline concepts](/t5/technology-blog-posts-by-members/migration-sap-pi-po-to-sap-cloud-integration-using-pipeline-concepts/ba-p/14189135)
  in [Technology Blog Posts by Members](/t5/technology-blog-posts-by-memb...