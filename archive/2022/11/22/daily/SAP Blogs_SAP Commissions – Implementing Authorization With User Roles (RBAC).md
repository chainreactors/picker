---
title: SAP Commissions – Implementing Authorization With User Roles (RBAC)
url: https://blogs.sap.com/2022/11/21/sap-commissions-implementing-authorization-with-user-roles-rbac/
source: SAP Blogs
date: 2022-11-22
fetch_date: 2025-10-03T23:23:37.624007
---

# SAP Commissions – Implementing Authorization With User Roles (RBAC)

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Human Capital Management](/t5/human-capital-management/ct-p/hcm)
* [HCM Blog Posts by SAP](/t5/human-capital-management-blog-posts-by-sap/bg-p/hcm-blog-sap)
* SAP Commissions - Implementing Authorization With ...

Human Capital Management Blog Posts by SAP

Learn directly from SAP experts through blogs that deliver practical guidance and opportunities to deepen your expertise.

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/hcm-blog-sap/article-id/5882&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [SAP Commissions - Implementing Authorization With User Roles (RBAC)](/t5/human-capital-management-blog-posts-by-sap/sap-commissions-implementing-authorization-with-user-roles-rbac/ba-p/13554527)

![Yogananda](https://avatars.profile.sap.com/5/9/id59e1da3a3dca34a1bd12f9d987d3cdb668e528e343194e20fc715b0bc28cc49b_small.jpeg "Yogananda")

![Product and Topic Expert](/html/@138D6F765B60D7FC0168643DE27D8A68/rank_icons/sap-logo-small-14px.png "Product and Topic Expert")
[Yogananda](https://community.sap.com/t5/user/viewprofilepage/user-id/75)

Product and Topic Expert

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=hcm-blog-sap&message.id=5882)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/hcm-blog-sap/article-id/5882)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13554527)

‎2022 Nov 21
7:10 PM

[4
Kudos](/t5/kudos/messagepage/board-id/hcm-blog-sap/message-id/5882/tab/all-users "Click here to see who gave kudos to this post.")

7,075

* SAP Managed Tags
* [SAP Cloud Identity Services](https://community.sap.com/t5/c-khhcw49343/SAP%2520Cloud%2520Identity%2520Services/pd-p/67837800100800007337)
* [SAP SuccessFactors Incentive Management](https://community.sap.com/t5/c-khhcw49343/SAP%2520SuccessFactors%2520Incentive%2520Management/pd-p/73555000100800001602)

* [SAP Cloud Identity Services

  SAP Business Technology Platform](/t5/c-khhcw49343/SAP%2BCloud%2BIdentity%2BServices/pd-p/67837800100800007337)
* [SAP SuccessFactors Incentive Management

  SAP SuccessFactors HCM](/t5/c-khhcw49343/SAP%2BSuccessFactors%2BIncentive%2BManagement/pd-p/73555000100800001602)

View products (2)

### This article goes through the SAP Best practice for authentication flow to identify who the user is and then goes through authorization flows if the user has permission for the roles assigned at a Group level.

In this blog, we are also covering **Top-Down User Sync Best Practice** as well when users are assigned with appropriate group from your HR System or IDM and syncs to different SAP Applications for authorization.![](/legacyfs/online/storage/blog_attachments/2022/11/b058d672f63f4c39120e0eaf938c88fe.png)

## What Is RBAC ?

Role-based access control (RBAC) is a security approach that uses roles to define what a user is and isn’t allowed to do. In an SAP Commissions application, users are assigned roles with varying permissions for different resources, including workflow, territory & quote, and embedded analytic applications

So, when a user tries to access a application, the system will first find the roles associated with the user and then check if any of the roles have the appropriate permission. If so, the user is allowed to access the application. If not, the user is denied access

**Let's see the High Level Understanding flow**

![](/legacyfs/online/storage/blog_attachments/2022/11/2022-11-22_00-35-45.gif)

### What Is Authorization?

Authorization is about answering the question, *“Is this user allowed to do a certain operation?”*. This is different from Authentication, in which we answer the question, *“Which user is this request coming from?”*

Both are essential to most applications, and as such, we first go through authentication flows to identify who the user is. Then we go through authorization flows in which we decide if the user has permission to do certain operations.

**Example** : SAP Identity Authentication Service(IAS) is maintaining all the users with groups which is received from Successfactors, Azure, Sailpoint, Workday or any other systems for users Authorization access while going through Authentication process. ![](/legacyfs/online/storage/blog_attachments/2022/11/2022-11-22_00-23-36.png)Follow step by step to have RBAC Process in place for SAP Commissions Application

---

### How to Assign Permissions to a particular Role ?

Go to **User Administration >** Select **Roles >** Expand **Callidus Portal >** Select **Role to assign Permissions**![](/legacyfs/online/storage/blog_attachments/2022/11/2022-11-21_23-11-29.png)
Select anyone of the **Role** to see Permissions are added correctly according to the role defined.![](/legacyfs/online/storage/blog_attachments/2022/11/2022-11-21_23-38-11.png)

### How to Create a Group ?

Go to Groups and Click + and New Dialog box will be displayed![](/legacyfs/online/storage/blog_attachments/2022/11/2022-11-21_23-18-26.png)

### How to assign a role at a Group Level ?

From the previous step, you have created a **Group**, so you can select the Group and Click **Add** in Assigned Roles and pick the roles displayed in your dialog screen and assign it.![](/legacyfs/online/storage/blog_attachments/2022/11/2022-11-21_23-31-01.png)
Another example for **Administrator** role to assign it to Group Level![](/legacyfs/online/storage/blog_attachments/2022/11/2022-11-21_23-28-10.png)
Now, we can see **Users are synced with appropriate User Groups** which is as per your IDM or HR System according to the Authorization process.![](/legacyfs/online/storage/blog_attachments/2022/11/2022-11-22_00-19-35.png)

Exact User Groups are matching from above step in both systems (from the Identity Management system maintained by your HR System or from Azure, Okta, SailPoint or any other systems)![](/legacyfs/online/storage/blog_attachments/2022/11/2022-11-22_00-23-36-1.png)

---

### Advantages of RBAC

+ **Easy to understand**: The structure of roles and permissions is very intuitive. It can be understood by new employees fairly quickly.

+ **Easy changes**: As the org structure changes, assigning new roles to employees automatically gives them all the right access - there is no extra coding required, and the change can be made via a dashboard in minutes.

+ **Improving compliance**: RBAC forces executives to think about and organize access control. This information can then be used by compliance officers during an audit.

+ **Decrease risk of data breaches/leakage**: Due to its ease of use, developers can easily implement the right access control policies in their APIs, reducing the chances of data leaks.

---

### References

#### [SAP Commissions – Must to know about IAS/IPS Process](https://blogs.sap.com/2020/10/26/sap-commissions-must-know-about-ias-ips-other-apps/)

#### [**Top-Down Documentation**](https://help.sap.com/viewer/85ce2a3717a644afa2bbd21f70387549/2111/en-US/72589dca7c231014a804993ce4041860.html)

#### [**User Groups Documentation**](https://help.sap.com/viewer/7b28ab814143467db8f7af8cc6fe541c/2012/en-US/5d1aadddcde1455caf7b207f244177a7.html)

#### [**KB Article for Bottom-up & Top-Down Approach (2999357)**](https://launchpad.support.sap.com/#/notes/2999357)

Labels

* [Technology Updates](/t5/human-capital-management-blog-posts-by-sap/bg-p/hcm-blog-sap/label-name/technology%20updates)

* [ac...