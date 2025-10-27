---
title: Efficient Employee Grouping in SAP SuccessFactors: Custom Attribute-based Identity Provisioning
url: https://blogs.sap.com/2023/04/21/efficient-employee-grouping-in-sap-successfactors-custom-attribute-based-identity-provisioning/
source: SAP Blogs
date: 2023-04-22
fetch_date: 2025-10-04T11:33:32.790027
---

# Efficient Employee Grouping in SAP SuccessFactors: Custom Attribute-based Identity Provisioning

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Human Capital Management](/t5/human-capital-management/ct-p/hcm)
* [HCM Blog Posts by Members](/t5/human-capital-management-blog-posts-by-members/bg-p/hcm-blog-members)
* Efficient Employee Grouping in SAP SuccessFactors:...

Human Capital Management Blog Posts by Members

Explore blogs from customers or SAP partners to gain best practices and fresh insights to succeed.

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/hcm-blog-members/article-id/4891&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [Efficient Employee Grouping in SAP SuccessFactors: Custom Attribute-based Identity Provisioning](/t5/human-capital-management-blog-posts-by-members/efficient-employee-grouping-in-sap-successfactors-custom-attribute-based/ba-p/13553479)

![shrutithakkar](https://avatars.profile.sap.com/9/c/id9c42a89ebb4a664e84b6e25cb4b2369b4074fd5d51b1faddcd003364f75d7702_small.jpeg "shrutithakkar")

[shrutithakkar](https://community.sap.com/t5/user/viewprofilepage/user-id/35141)

Active Participant

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=hcm-blog-members&message.id=4891)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/hcm-blog-members/article-id/4891)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13553479)

‎2023 Apr 21
9:17 PM

[12
Kudos](/t5/kudos/messagepage/board-id/hcm-blog-members/message-id/4891/tab/all-users "Click here to see who gave kudos to this post.")

5,756

* SAP Managed Tags
* [SAP Cloud Identity Services](https://community.sap.com/t5/c-khhcw49343/SAP%2520Cloud%2520Identity%2520Services/pd-p/67837800100800007337)
* [Identity Provisioning](https://community.sap.com/t5/c-khhcw49343/Identity%2520Provisioning/pd-p/73555000100800000425)
* [SAP SuccessFactors Employee Central](https://community.sap.com/t5/c-khhcw49343/SAP%2520SuccessFactors%2520Employee%2520Central/pd-p/73555000100800000773)
* [SAP SuccessFactors HCM Suite](https://community.sap.com/t5/c-khhcw49343/SAP%2520SuccessFactors%2520HCM%2520Suite/pd-p/67838200100800004730)
* [SAP Identity Management](https://community.sap.com/t5/c-khhcw49343/SAP%2520Identity%2520Management/pd-p/01200615320800000721)

* [SAP SuccessFactors HCM Suite

  SAP SuccessFactors HCM](/t5/c-khhcw49343/SAP%2BSuccessFactors%2BHCM%2BSuite/pd-p/67838200100800004730)
* [SAP Cloud Identity Services

  SAP Business Technology Platform](/t5/c-khhcw49343/SAP%2BCloud%2BIdentity%2BServices/pd-p/67837800100800007337)
* [SAP Identity Management

  SAP NetWeaver](/t5/c-khhcw49343/SAP%2BIdentity%2BManagement/pd-p/01200615320800000721)
* [Identity Provisioning

  SAP Business Technology Platform](/t5/c-khhcw49343/Identity%2BProvisioning/pd-p/73555000100800000425)
* [SAP SuccessFactors Employee Central

  SAP SuccessFactors HCM](/t5/c-khhcw49343/SAP%2BSuccessFactors%2BEmployee%2BCentral/pd-p/73555000100800000773)

View products (5)

Streamlining Employee Grouping in SAP SuccessFactors: Leveraging Custom Attributes from SAP SuccessFactors via Identity Provisioning for Identity Authentication User Store Management.

In this blog, the focus is on streamlining employee grouping in SAP SuccessFactors using custom attributes. For an example we are using custom15 from the User Data file is utilized to determine the appropriate group for employees in the Identity Authentication user store.

There could be different conditions that can be used to check a particular field value and update the employee in a specific group.

The custom attribute (custom15) is utilized as a key factor for grouping employees in SAP SuccessFactors. By checking the value of this field, employees are dynamically assigned to different groups. If the value is set to "Yes", they are directed to the 'MFAGROUP' group in Identity Authentication. On the other hand, if the value is set to anything other than "Yes" (e.g. "No" or left blank), the employees are directed to the 'NO\_MFA' group.

By utilizing the "Is MFA?" (Custom15) field, employee grouping in Identity Authentication is streamlined, ensuring that employees are accurately placed in the appropriate groups based on the value of this custom attribute. This approach simplifies user store management and enhances the overall identity and access management process in SAP SuccessFactors.

**Step 1- Identity Provisioning Source System - SAP SuccessFactors**

The Custom15 value can be added to the sf.user.attributes property in the Identity Provisioning configuration. This allows Identity Provisioning to read and load this user attribute from SAP SuccessFactors during the provisioning process. It is important to ensure that the extra attribute, in this case Custom15, is appropriately separated by a comma to ensure accurate data processing.

![](/legacyfs/online/storage/blog_attachments/2023/04/SF-Attribute.png)

sf.user.attributes

**Step 2 - Mapping the data in Source System**

Add the following code to the source system transformation into the User mapping section. I am updating the value of Custom15 from SF into CustomAttribute2 in IAS:

###### *{* *"sourcePath": "$['urn:sap:cloud:scim:schemas:extension:sfsf:2.0:User']['custom15']",* *"optional": true,* *"targetPath": "$['urn:sap:cloud:scim:schemas:extension:custom:2.0:User']['attributes'][1]['value']"* *},* *{* *"condition": "$['urn:sap:cloud:scim:schemas:extension:sfsf:2.0:User']['custom15'] EMPTY false",* *"constant": "customAttribute2",* *"targetPath": "$['urn:sap:cloud:scim:schemas:extension:custom:2.0:User']['attributes'][1]['name']"* *},* *{* *"sourcePath": "$.custom15",* *"targetPath": "$.custom15"* *}*

###### ![](/legacyfs/online/storage/blog_attachments/2023/04/Source-Code_UserMapping.png)

Transformation - Source Code - UserMapping

**Step 3 - Identity Provisioning Target System - Identity Authentication**

Add the following code to the Identity Authentication target system transformation into the User mapping Section:

###### *{* *"sourcePath": "$['urn:sap:cloud:scim:schemas:extension:sfsf:2.0:User']['custom15']",* *"optional": true,* *"targetPath": "$['urn:sap:cloud:scim:schemas:extension:custom:2.0:User']['attributes'][1]['value']"* *},* *{* *"constant": "customAttribute2",* *"targetPath": "$['urn:sap:cloud:scim:schemas:extension:custom:2.0:User']['attributes'][1]['name']"* *},*

![](/legacyfs/online/storage/blog_attachments/2023/04/Target-Transformation_Code.png)

Transformation - Target Code - UserMapping

**Step 4 - Create the two User Groups**

In Identity Authentication Administration Console, create the two user groups to update the employees:

* MFAGROUP

* NO\_MFA

![](/legacyfs/online/storage/blog_attachments/2023/04/Groups.png)

User Groups

**Step 5 - Add Condition for employees to get auto updated in User groups created in Identity Authentication**

These mappings will assign the user groups to the users who are fits with the given condition.

###### *{* *"condition": "($.custom15 == 'Yes')",* *"constant": "MFAGROUP",* *"targetPath": "$.groups[0].value"* *},* *{* *"condition": "($.custom15 != 'Yes')",* *"constant": "NO\_MFA",* *"targetPath": "$.groups[0].value"* *},*

![](/legacyfs/online/storage/blog_attachments/2023/04/Groupingcode.png)

Transformation - Target Code - UserMapping - Groupingcode

**Step 6- Run Read Job Identity Provisioning**

Run a new Read job from Identity Provisioning from SAP SuccessFactors s...