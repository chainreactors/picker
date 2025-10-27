---
title: Delegated User Administration Using Attribute-Based Access Control in SAP Cloud Identity Services
url: https://blogs.sap.com/2023/07/17/delegated-user-administration-using-attribute-based-access-control-in-sap-cloud-identity-services/
source: SAP Blogs
date: 2023-07-18
fetch_date: 2025-10-04T11:54:34.555958
---

# Delegated User Administration Using Attribute-Based Access Control in SAP Cloud Identity Services

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Technology](/t5/technology/ct-p/technology)
* [Technology Blog Posts by SAP](/t5/technology-blog-posts-by-sap/bg-p/technology-blog-sap)
* Delegated User Administration Using Attribute-Base...

Technology Blog Posts by SAP

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/technology-blog-sap/article-id/159666&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [Delegated User Administration Using Attribute-Based Access Control in SAP Cloud Identity Services](/t5/technology-blog-posts-by-sap/delegated-user-administration-using-attribute-based-access-control-in-sap/ba-p/13555539)

![ValAtanassov](https://avatars.profile.sap.com/f/1/idf17934121f20a9bbb349c5727f41ae43728a4c44fd4640abecc568d5012a6b69_small.jpeg "ValAtanassov")

![Product and Topic Expert](/html/@138D6F765B60D7FC0168643DE27D8A68/rank_icons/sap-logo-small-14px.png "Product and Topic Expert")
[ValAtanassov](https://community.sap.com/t5/user/viewprofilepage/user-id/125402)

Product and Topic Expert

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=technology-blog-sap&message.id=159666)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/technology-blog-sap/article-id/159666)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13555539)

‎2023 Jul 17
4:49 PM

[15
Kudos](/t5/kudos/messagepage/board-id/technology-blog-sap/message-id/159666/tab/all-users "Click here to see who gave kudos to this post.")

4,400

* SAP Managed Tags
* [SAP Cloud Identity Services](https://community.sap.com/t5/c-khhcw49343/SAP%2520Cloud%2520Identity%2520Services/pd-p/67837800100800007337)

* [SAP Cloud Identity Services

  SAP Business Technology Platform](/t5/c-khhcw49343/SAP%2BCloud%2BIdentity%2BServices/pd-p/67837800100800007337)

View products (1)

## Why is this feature important for you?

You are an administrator at SAP Cloud Identity Services, but the standard predefined administrator roles that are offered to you, such as **Manage Users** or **Read Users**, are not flexible or fine granular enough for your user management needs and scenarios. If you are looking for a solution to that problem, then you are in the right place.

## Feature overview

Tenant administrators in SAP Cloud Identity Services are offered a predefined set of roles (authorizations) that provide a full set of permissions in a particular area. The administrators can get some roles assigned, but their scope (set of permissions) can’t be modified, and very often it’s too broad.

However, you may need to define authorization models with more complex restrictions for data access, like the so-called Attribute-Based Access Control (ABAC). So, with the need for finer granular separation of the administration work, the new feature of SAP Cloud Identity Services for admin authorizations based on policies (aka **delegated administration for user management)** comes as a solution for that need. In other words, administrators define custom authorization policies based on user attributes and assign these policies to other administrators or users, thus delegating them granular administrator rights. In this way, one administrator can have access to a subset of the users in the tenant and further to a subset of the attributes of these users.

So, this recently released feature offers the opportunity for delegating specific responsibilities for user management to different administrators by precisely limiting the user data an administrator can access and control. This helps to reduce manual administration efforts for user management and identity provisioning and avoid work disruption by leveraging the suite quality “[consistent security and identity management](https://www.sap.com/documents/2020/02/520ea921-847d-0010-87a3-c30de2ffd8ff.html)” for an intuitive login process within your intelligent sustainable enterprise.

This fine granular access control is based on a generic Authorization Management functionality provided by SAP Cloud Identity Services for which you can read more at [Configuring Authorization Policies](https://help.sap.com/docs/identity-authentication/identity-authentication/configuring-authorization-policies).

## The solution

So, let’s see how the user management admin access can be restricted to a subset of the whole user base.

Using the predefined Base Policies for users (CREATE\_USERS, READ\_USERS, UPDATE\_USERS, DELETE\_USERS, MANAGE\_USERS) you can define a custom one with restriction rules based on the values of some user attributes. In this way you limit the corresponding permission granted by the base policy, so it will be relevant only for the subset of users that match the specified rule.

You can restrict for which users the admin gets the corresponding access level (permission), based on the following user attributes:

|  |
| --- |
| **User Attributes** |
| **Attributes** | **Value** |
| user.userName | The **Login Name** attribute of the user as defined in the administration console. |
| user.addresses.country | The Country attribute part of the address in the personal user information. The value must match the predefined master data one. See [Countries.properties](https://help.sap.com/docs/IDENTITY_AUTHENTICATION/6d6d63354d1242d185ab4830fc04feb1/b10fc6a9a37c488a82ce7489b1fab64c.html?version=Cloud#loioe4e7e4c52cf04295bf94465eba7ceaaa).   **Tip**   Use the key from the key-value pair for the value of the user.country attribute. For example, you must use DE from the key-value pair DE=Germany. |
| user.costCenter | The **Cost Center** of the user, part of the employee information. |
| user.division | The **Division** of the user, part of the employee information. |
| user.department | The **Department** of the user, part of the employee information. The value must match the predefined master data one. See [Departments.properties](https://help.sap.com/docs/IDENTITY_AUTHENTICATION/6d6d63354d1242d185ab4830fc04feb1/b10fc6a9a37c488a82ce7489b1fab64c.html?version=Cloud#loiod13c638f0d5d4a8889debf278fcb0275). |
| user.organization | The **Company** of the user, part of the company information. |

You can also limit the attributes of the users that the admin can access by configuring one of the following attributes in your custom policy:

|  |
| --- |
| **User Attributes** |
| **Attributes** | **Value** |
| user.attributes | Allows you to define a subset of the user attributes (by listing them in the value field separated with commas) that the admin would be able to access.    User attributes that are not part of the SCIM Core Schema must be specified with their fully qualified name that includes the corresponding schema.      ***Note:***  *If the user.аttributes is used with the "=" operator, it supports only one attribute. For more attributes, use the "IN" operator adding each attribute separately.*  ***Note:***  *If you use the attribute ‘**password**’, you must also add the following two attributes: **‘****active**and **‘****urn:ietf:params:scim:schemas:extension:sap:2.0:User:status**’**.* |
| **Deprecated**  user.excludedAttributes | ***Note:***  *The user.excludedAttributes attribute is deprecated.*  *If you have a policy configured with the user.excludedAttributes attribute, exchange the user.excludedAttributes with the user.attributes attribute in combination with the "**NOT IN**" operator.*  *If the policy is co...