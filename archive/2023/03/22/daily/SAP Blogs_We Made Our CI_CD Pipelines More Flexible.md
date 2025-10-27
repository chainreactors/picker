---
title: We Made Our CI/CD Pipelines More Flexible
url: https://blogs.sap.com/2023/03/21/we-made-our-ci-cd-pipelines-more-flexible/
source: SAP Blogs
date: 2023-03-22
fetch_date: 2025-10-04T10:14:59.903694
---

# We Made Our CI/CD Pipelines More Flexible

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Technology](/t5/technology/ct-p/technology)
* [Technology Blog Posts by SAP](/t5/technology-blog-posts-by-sap/bg-p/technology-blog-sap)
* We Made Our CI/CD Pipelines More Flexible

Technology Blog Posts by SAP

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/technology-blog-sap/article-id/159269&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [We Made Our CI/CD Pipelines More Flexible](/t5/technology-blog-posts-by-sap/we-made-our-ci-cd-pipelines-more-flexible/ba-p/13554294)

![SarahLendle](https://avatars.profile.sap.com/b/b/idbbce1dc4f8c5bb81416e8b8a5f1b236dabdd4f97045b3adf982f30b59dc2e547_small.jpeg "SarahLendle")

![Advisor](/html/@138D6F765B60D7FC0168643DE27D8A68/rank_icons/sap-logo-small-14px.png "Advisor")
[SarahLendle](https://community.sap.com/t5/user/viewprofilepage/user-id/535766)

Advisor

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=technology-blog-sap&message.id=159269)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/technology-blog-sap/article-id/159269)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13554294)

‎2023 Mar 21
8:47 PM

[8
Kudos](/t5/kudos/messagepage/board-id/technology-blog-sap/message-id/159269/tab/all-users "Click here to see who gave kudos to this post.")

1,562

* SAP Managed Tags
* [DevOps](https://community.sap.com/t5/c-khhcw49343/DevOps/pd-p/51112e3c-4b78-4058-a637-67f453c196c9)
* [SAP Continuous Integration and Delivery](https://community.sap.com/t5/c-khhcw49343/SAP%2520Continuous%2520Integration%2520and%2520Delivery/pd-p/73554900100800001771)

* [DevOps

  Programming Tool](/t5/c-khhcw49343/DevOps/pd-p/51112e3c-4b78-4058-a637-67f453c196c9)
* [SAP Continuous Integration and Delivery

  SAP Business Technology Platform](/t5/c-khhcw49343/SAP%2BContinuous%2BIntegration%2Band%2BDelivery/pd-p/73554900100800001771)

View products (2)

With SAP Continuous Integration and Delivery, we strive for simplicity: Our service on SAP BTP offers ready-made pipelines for various SAP-specific development scenarios. With them, we want to help you implement CI/CD quickly and without having to care about the underlying infrastructure. Simplicity, however, shouldn’t mean inflexibility. That’s why we’ve added additional configuration options to our pipelines to make sure they work for your purposes.

In different stages of your CI/CD pipelines, you can now add additional credentials and variables. This lets you, for example, access a private repository when building your application or set a DEBUG flag when running your tests.

Have a look at the following example to see how our new feature works:

# Use Private npm Packages in Your CI/CD Job

Add an access token to the **Build** stage of your SAP Continuous Integration and Delivery job to access private npm packages during its execution.

## Procedure

1. In your source code repository, create a custom .npmrc file with the following content:

   ```
   //registry.npmjs.org/:_authToken=${NPM_TOKEN}​
   ```

   **Note:**You specify a literal value of ${NPM\_TOKEN}. The npm CLI will replace this value with the contents of the NPM\_TOKEN environment variable. Do not put a token in this file.

2. Check in your .npmrc file.

3. In SAP Continuous Integration and Delivery, create a new or edit an existing SAP Cloud Application Programming Model job.

4. In the **Build** stage, choose **+** *(Add credentials variable)* next to **Additional Credentials**.
   As a result, the **Add Credentials Variable** pop-up window opens.

5. For **Name**, enter NPM\_TOKEN.

6. Open the **Credentials Name** drop-down list and choose **Create Credentials**.
   As a result, the **Create Credentials** pop-up window opens.

7. For **Credentials Name**, enter mynpmtoken.

8. From the **Type** drop-down list, choose **Secret Text**.

9. In the **Secret** text field, enter your token.

10. Choose **Create**.
    As a result, your newly created credential is used for **Credentials Name**.

11. Choose **OK**.

12. Create and run your job.

## Result

You can now use private npm packages with your SAP Continuous Integration and Delivery job.

That’s cool, isn’t it? Have a look at our documentation and try it out yourself: [Adding Environment Variables to Stages | SAP Help Portal](https://help.sap.com/docs/CONTINUOUS_DELIVERY/99c72101f7ee40d0b2deb4df72ba1ad3/c8314b6c8e564f42925e9d10453bd541.html?version=Cloud&language=en-US)

We’re also working on adding even more flexibility to our pipelines. Stay tuned!

Labels

* [Technology Updates](/t5/technology-blog-posts-by-sap/bg-p/technology-blog-sap/label-name/technology%20updates)

* [BTPDevOps](/t5/tag/BTPDevOps/tg-p/board-id/technology-blog-sap)
* [cicd](/t5/tag/cicd/tg-p/board-id/technology-blog-sap)
* [CICD for SAP BTP](/t5/tag/CICD%20for%20SAP%20BTP/tg-p/board-id/technology-blog-sap)
* [DevOps](/t5/tag/DevOps/tg-p/board-id/technology-blog-sap)
* [SAPCICD](/t5/tag/SAPCICD/tg-p/board-id/technology-blog-sap)

You must be a registered user to add a comment. If you've already registered, sign in. Otherwise, register and sign in.

* [Comment](/plugins/common/feature/oidcss/sso_login_redirect/providerid/sap_ids_prompt?redirectreason=permissiondenied&referer=https%3A%2F%2Fcommunity.sap.com%2Ft5%2Ftechnology-blog-posts-by-sap%2Fwe-made-our-ci-cd-pipelines-more-flexible%2Fba-p%2F13554294%23comment-on-this)

Copy Link
![](https://community.sap.com/html/@EE5D5986E9F4E5657DCEACB7532B5C39/assets/bluesky-dark.svg)Bluesky
Linkedin

Related Content

* [Optimizing Accessibility for Visual Impairment](/t5/technology-blog-posts-by-sap/optimizing-accessibility-for-visual-impairment/ba-p/14234652)
  in [Technology Blog Posts by SAP](/t5/technology-blog-posts-by-sap/bg-p/technology-blog-sap)  yesterday
* [SAP BTP CI CD service for on premise S4 HANA systems RICEFW applications](/t5/technology-q-a/sap-btp-ci-cd-service-for-on-premise-s4-hana-systems-ricefw-applications/qaq-p/14234519)
  in [Technology Q&A](/t5/technology-q-a/qa-p/technology-questions)  yesterday
* [Flexible Workflows for Procurement in SAP S/4HANA](/t5/technology-blog-posts-by-members/flexible-workflows-for-procurement-in-sap-s-4hana/ba-p/14234315)
  in [Technology Blog Posts by Members](/t5/technology-blog-posts-by-members/bg-p/technology-blog-members)  yesterday
* [SAP S4HANA Plant Maintenance for dummies](/t5/technology-blog-posts-by-members/sap-s4hana-plant-maintenance-for-dummies/ba-p/14234304)
  in [Technology Blog Posts by Members](/t5/technology-blog-posts-by-members/bg-p/technology-blog-members)  yesterday
* [Organizational Management in SAP S/4HANA HCM](/t5/technology-blog-posts-by-members/organizational-management-in-sap-s-4hana-hcm/ba-p/14234285)
  in [Technology Blog Posts by Members](/t5/technology-blog-posts-by-members/bg-p/technology-blog-members)  yesterday

Top kudoed authors

| User | Count |
| --- | --- |
| [![Ria4](https://avatars.profile.sap.com/4/1/id41f53dcfce78ad1c94edcd3a60b4666df8e3aac18a25c618793ae5b110c6aee0_small.jpeg "Ria4")  ![Associate](/html/@138D6F765B60D7FC0168643DE27D8A68/rank_icons/sap-logo-small-14px.png "Associate") Ria4](/t5/user/viewprofilepage/user-id/1478971) | 14 |
| [![jeet_kapase](https://avatars.profile.sap.com/0/0/id008b5bef5d6007221ab5d86367db67c9ec91895fa76b16aeddea0ed2fe268734_small.jpeg "jeet_kapase")  ![Product and Topic Expert](/html/@138D6...