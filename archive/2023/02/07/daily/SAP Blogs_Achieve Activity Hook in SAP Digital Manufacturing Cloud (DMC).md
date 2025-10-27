---
title: Achieve Activity Hook in SAP Digital Manufacturing Cloud (DMC)
url: https://blogs.sap.com/2023/02/06/achieve-activity-hook-in-sap-digital-manufacturing-cloud-dmc/
source: SAP Blogs
date: 2023-02-07
fetch_date: 2025-10-04T05:51:19.501014
---

# Achieve Activity Hook in SAP Digital Manufacturing Cloud (DMC)

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Product Lifecycle Management](/t5/product-lifecycle-management/ct-p/plm)
* [PLM Blog Posts by Members](/t5/product-lifecycle-management-blog-posts-by-members/bg-p/plm-blog-members)
* How to achieve an Activity Hook in SAP Digital Man...

Product Lifecycle Management Blog Posts by Members

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/plm-blog-members/article-id/1487&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [How to achieve an Activity Hook in SAP Digital Manufacturing Cloud (DMC)](/t5/product-lifecycle-management-blog-posts-by-members/how-to-achieve-an-activity-hook-in-sap-digital-manufacturing-cloud-dmc/ba-p/13560760)

![abolik97](https://avatars.profile.sap.com/2/2/id22cd120268407c4dbb32e09b7f281505d8870b121aa62cdea96338b884d3c88b_small.jpeg "abolik97")

[abolik97](https://community.sap.com/t5/user/viewprofilepage/user-id/123097)

Explorer

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=plm-blog-members&message.id=1487)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/plm-blog-members/article-id/1487)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13560760)

‎2023 Feb 06
7:16 PM

[11
Kudos](/t5/kudos/messagepage/board-id/plm-blog-members/message-id/1487/tab/all-users "Click here to see who gave kudos to this post.")

2,420

* SAP Managed Tags
* [SAP Digital Manufacturing](https://community.sap.com/t5/c-khhcw49343/SAP%2520Digital%2520Manufacturing/pd-p/73555000100800001492)
* [SAP Manufacturing Execution](https://community.sap.com/t5/c-khhcw49343/SAP%2520Manufacturing%2520Execution/pd-p/01200615320800000731)

* [SAP Manufacturing Execution

  SAP Digital Manufacturing](/t5/c-khhcw49343/SAP%2BManufacturing%2BExecution/pd-p/01200615320800000731)
* [SAP Digital Manufacturing

  SAP Digital Manufacturing](/t5/c-khhcw49343/SAP%2BDigital%2BManufacturing/pd-p/73555000100800001492)

View products (2)

> **Business Concept:**

Activity Hook in SAP ME: An Activity hook is a Hookable Activity assigned to a hook point.

In SAP ME we have functionality to assign activities at some hook points so that system will automatically trigger that in manufacturing process.

In this blog you will get to know how we can achieve this functionality in SAP DMC.

**Business Scenario:**

**Example:** Let us consider there is requirement to auto start and auto complete one of the operations in routing without operator intervention.

**Solution in SAP ME:** we will create a customized activity and assign it to the hook point (POST\_COMPLETE) of previous operation on routing level.

(i.e., on completion of the current operation next operation will auto start and auto complete.)

**Solution in SAP DMC:** To achieve the same functionality in DMC we can create Production Process.  More Information about Production Process you can find in here [Design Production Process SAP Help](https://help.sap.com/docs/SAP_DIGITAL_MANUFACTURING_CLOUD/f1949e1d1fd24d7e998e5f70fecc1835/c93b358ef5b5454384a3f412b589f899.html).

We can assign production process to POD buttons however in our example we don't want any operator intervention. So, we should use the Manage Automatic Triggers App. There we can create business rule providing the triggering condition and attaching the production process that needs to be triggered.

**Steps to create Production Process:**

1. Search for Manage Production Process App in SAP DMC. Click on create. Provide Name, Description. Version will auto populate however we can change version as well.

2. Click on ‘+’ to create the production process. Provide Name, Description, select Runtime type as Cloud and Runtime Environment will auto populate as Cloud. Click on create.

3. Now start designing the production process. First drag and drop start control then select services Start SFCs and Complete SFCs under SFC Production Activities.

4. Next step is to manage input parameters of the production process. Need to create input parameters to PP so that autostart & autocomplete process can be used for any operation, any resource, and any SFC. Select first control (Start) and click on Manage Parameters to add inputs to production process. Check the inputs which are mandatory for SFC Start and SFC Complete Services accordingly add the inputs to production process. Provide Name to input, select data type from drop down if its mandatory filed for production process then select checkbox 'Required' and click on Save.

5. Now assign the created variables to the inputs of start and complete services. Click on Save All to save the production process.  Now Production process to automatically start and complete the SFC at given operation is developed. Next step is to deploy the PP.

6. To deploy the production process click on Quick Deploy. Click on Deploy and Activate.

7. To make the created production process visible in the service registry (To be able to use in another apps) Choose more, click on edit header and set Publish to Service Registry to ON.

Now we need to create a business rule using Manage Automatic App to trigger the production process on given conditions.

**Steps to create business rule using Manage Automatic App:**

1. Search for Manage Automatic Triggers App in SAP DMC. Click on Business Rule to create a new business rule and click on Create.

2. Provide Name, Description to business rule. Select Trigger Type as: Event. Select Event Type as ‘SFC Operation Activity Completed’ on which you want to trigger production process. Considering our example:

   On completion of the current operation, we want to automatically start the next operation. So, select Event Type as ‘SFC Operation Activity Completed’.

3. Next step is to configure the Conditions on which business rule should trigger:

   In SAP ME we can add hook point activity on operation, routing, or resource level. Similarly, we can provide here conditions for which plant, operation, routing, or resource we want to trigger business rule.

4. Now we need to assign the production process that we want to trigger. Under Action Item browse for Production Process created.

5. Now configure input parameters of production process. We created business rule to auto start and auto complete SFC at XYZ operation.  Thus, providing operation, resource as constant values and SFC will be passed dynamically. Click on create to save created business rule.

6. Last step is to deploy created business rule. Click on Quick Deploy.

**Summary:** Using business rule we have successfully achieved calling a production process on an event.

**Conclusion:**Please, let me know your comments/observations. If you have any questions, I encourage you to post in the comment section [here](https://answers.sap.com/tags/01200615320800000731) and I will try to answer them as soon as possible.

To know more about SAP DMC follow [here](https://www.sap.com/products/scm/digital-manufacturing-cloud.html).

2 Comments

You must be a registered user to add a comment. If you've already registered, sign in. Otherwise, register and sign in.

* [Comment](/plugins/common/feature/oidcss/sso_login_redirect/providerid/sap_ids_prompt?redirectreason=permissiondenied&referer=https%3A%2F%2Fcommunity.sap.com%2Ft5%2Fproduct-lifecycle-management-blog-posts-by-members%2Fhow-to-achieve-an-activity-hook-in-sap-digital-manufacturing-cloud-dmc%...