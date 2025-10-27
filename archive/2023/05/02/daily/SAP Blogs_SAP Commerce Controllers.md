---
title: SAP Commerce Controllers
url: https://blogs.sap.com/2023/05/01/sap-commerce-controllers/
source: SAP Blogs
date: 2023-05-02
fetch_date: 2025-10-04T11:39:08.939120
---

# SAP Commerce Controllers

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [CRM and Customer Experience](/t5/crm-and-customer-experience/ct-p/crm)
* [CRM and CX Blog Posts by Members](/t5/crm-and-cx-blog-posts-by-members/bg-p/crm-blog-members)
* SAP Commerce Controllers

CRM and CX Blog Posts by Members

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/crm-blog-members/article-id/6345&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [SAP Commerce Controllers](/t5/crm-and-cx-blog-posts-by-members/sap-commerce-controllers/ba-p/13567114)

![Harish_Vatsa](https://avatars.profile.sap.com/0/6/id06e4f4268603321b4a03e85b47b0bfa7e89c04de1d2ba70adf8509e12ecec4ab_small.jpeg "Harish_Vatsa")

![SAP Champion](/html/@B3DACAC6163F980483AC32558EB69695/rank_icons/champion-rank-16x16.svg "SAP Champion")
[Harish\_Vatsa](https://community.sap.com/t5/user/viewprofilepage/user-id/124398)

SAP Champion

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=crm-blog-members&message.id=6345)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/crm-blog-members/article-id/6345)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13567114)

‎2023 May 01
2:35 PM

[11
Kudos](/t5/kudos/messagepage/board-id/crm-blog-members/message-id/6345/tab/all-users "Click here to see who gave kudos to this post.")

2,621

* SAP Managed Tags
* [SAP Commerce](https://community.sap.com/t5/c-khhcw49343/SAP%2520Commerce/pd-p/67837800100800007216)
* [SAP Commerce Cloud](https://community.sap.com/t5/c-khhcw49343/SAP%2520Commerce%2520Cloud/pd-p/73555000100800001224)

* [SAP Commerce

  SAP Commerce](/t5/c-khhcw49343/SAP%2BCommerce/pd-p/67837800100800007216)
* [SAP Commerce Cloud

  Software Product](/t5/c-khhcw49343/SAP%2BCommerce%2BCloud/pd-p/73555000100800001224)

View products (2)

SAP Commerce Controllers play a crucial role in managing the interactions between the frontend and backend of an SAP Commerce website. In simple terms, a controller is a Java class that handles a specific request from the frontend and provides the relevant data or actions to the user.

Let’s understand the concept of controllers in more detail.

What is a Controller and its Functionality?

In the MVC architecture (Model View Controller), a controller acts as an interface between the frontend and the backend. The controller takes in the user input from the frontend and processes it to fetch the necessary data from the database. The data is then transformed and returned to the user in a desired format.

In an SAP Commerce website, multiple controllers are created to handle different types of requests from the frontend like searching for a product, adding a product to cart, updating the cart, and so on. Each controller is associated with a specific URL pattern and handles the requests that match that pattern.

How are Controllers Managed in SAP Commerce?

In an SAP Commerce website, controllers are organized in packages that follow a specific naming convention. The controller package name must start with the prefix “controllers” and be followed by a dot-separated name that describes the functionality of the controllers.

Each controller class must extend the abstract class “AbstractController” and be annotated with the “@Controller” annotation. The “@RequestMapping” annotation is used to define the URL pattern that the controller will handle.

For example, if we want to create a controller that handles the request to view a product page, we will create a class named “ProductDetailsController” in the package “controllers.product”. The class will extend the abstract class “AbstractController” and be annotated with the “@Controller” annotation. The “@RequestMapping” annotation will define the URL pattern that the controller will map to, like “/product/{productCode}”.

What is the Role of Interceptors in Controllers?

Interceptors are another type of Java class in SAP Commerce that intercepts the requests and responses being passed between the frontend and the backend. Interceptors can be used to carry out common tasks like logging, validation, and authentication.

In SAP Commerce, interceptors can be associated with controllers to handle specific types of requests. For example, an authentication interceptor can be associated with a controller that requires the user to be logged in before accessing a particular page.

Conclusion

SAP Commerce controllers are the key to managing the interactions between the frontend and backend of a website. They provide a structured way of handling user input and fetching the necessary data from the database. When used in conjunction with interceptors, controllers provide a powerful tool for creating a robust and secure web application.

Please refer the below SAP link for more information on SAP Commerce Controllers:

[https://help.sap.com/docs/SAP\_COMMERCE\_CLOUD\_PUBLIC\_CLOUD/aa417173fe4a4ba5a473c93eb730a417/96ab213b1...](https://help.sap.com/docs/SAP_COMMERCE_CLOUD_PUBLIC_CLOUD/aa417173fe4a4ba5a473c93eb730a417/96ab213b15384646a96331bfdb4bf735.html?version=v2105)

* [controller](/t5/tag/controller/tg-p/board-id/crm-blog-members)
* [Hybris Controllers](/t5/tag/Hybris%20Controllers/tg-p/board-id/crm-blog-members)
* [SAP Commerce Controllers](/t5/tag/SAP%20Commerce%20Controllers/tg-p/board-id/crm-blog-members)

3 Comments

You must be a registered user to add a comment. If you've already registered, sign in. Otherwise, register and sign in.

* [Comment](/plugins/common/feature/oidcss/sso_login_redirect/providerid/sap_ids_prompt?redirectreason=permissiondenied&referer=https%3A%2F%2Fcommunity.sap.com%2Ft5%2Fcrm-and-cx-blog-posts-by-members%2Fsap-commerce-controllers%2Fba-p%2F13567114%23comment-on-this)

Copy Link
![](https://community.sap.com/html/@EE5D5986E9F4E5657DCEACB7532B5C39/assets/bluesky-dark.svg)Bluesky
Linkedin

Related Content

* [How to Reduce Cloud Storage usage on SAP Commerce Cloud](/t5/crm-and-cx-blog-posts-by-sap/how-to-reduce-cloud-storage-usage-on-sap-commerce-cloud/ba-p/14233898)
  in [CRM and CX Blog Posts by SAP](/t5/crm-and-cx-blog-posts-by-sap/bg-p/crm-blog-sap)  yesterday
* [Reducing Cart Abandonment with SAP Commerce Cloud](/t5/crm-and-cx-blog-posts-by-sap/reducing-cart-abandonment-with-sap-commerce-cloud/ba-p/14233819)
  in [CRM and CX Blog Posts by SAP](/t5/crm-and-cx-blog-posts-by-sap/bg-p/crm-blog-sap)  yesterday
* [SAP’s Commitment to Business Continuity that Protects what Matters](/t5/crm-and-cx-blog-posts-by-sap/sap-s-commitment-to-business-continuity-that-protects-what-matters/ba-p/14232343)
  in [CRM and CX Blog Posts by SAP](/t5/crm-and-cx-blog-posts-by-sap/bg-p/crm-blog-sap)  Wednesday
* [SAP Commerce Cloud Q3 ‘25 Release Highlights](/t5/crm-and-cx-blog-posts-by-sap/sap-commerce-cloud-q3-25-release-highlights/ba-p/14231991)
  in [CRM and CX Blog Posts by SAP](/t5/crm-and-cx-blog-posts-by-sap/bg-p/crm-blog-sap)  Wednesday
* [New course: Creating Promotions and Coupons in SAP Commerce Cloud](/t5/crm-and-cx-blog-posts-by-sap/new-course-creating-promotions-and-coupons-in-sap-commerce-cloud/ba-p/14226977)
  in [CRM and CX Blog Posts by SAP](/t5/crm-and-cx-blog-posts-by-sap/bg-p/crm-blog-sap)  a week ago

Top kudoed authors

| User | Count |
| --- | --- |
| [![pvsbprasad](https://avatars.profile.sap.com/d/6/idd68c4fbf62700ef39eecb5d35b7b10fd1065edee7ec60bda72a4bced895ca7c3_small.jpeg "pvsbprasad")  pvsbprasad](/t5/user/viewp...