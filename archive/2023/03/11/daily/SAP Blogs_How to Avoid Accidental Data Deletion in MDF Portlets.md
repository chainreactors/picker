---
title: How to Avoid Accidental Data Deletion in MDF Portlets
url: https://blogs.sap.com/2023/03/10/how-to-avoid-accidental-data-deletion-in-mdf-portlets/
source: SAP Blogs
date: 2023-03-11
fetch_date: 2025-10-04T09:15:54.770599
---

# How to Avoid Accidental Data Deletion in MDF Portlets

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Human Capital Management](/t5/human-capital-management/ct-p/hcm)
* [HCM Blog Posts by Members](/t5/human-capital-management-blog-posts-by-members/bg-p/hcm-blog-members)
* How to Avoid Accidental Data Deletion in MDF Portl...

Human Capital Management Blog Posts by Members

Explore blogs from customers or SAP partners to gain best practices and fresh insights to succeed.

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/hcm-blog-members/article-id/5102&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [How to Avoid Accidental Data Deletion in MDF Portlets](/t5/human-capital-management-blog-posts-by-members/how-to-avoid-accidental-data-deletion-in-mdf-portlets/ba-p/13565947)

![Venkatesh_M](https://avatars.profile.sap.com/3/5/id35b0127b0929631ab3b5072196696f9ba842fbb5072c4c0288669ba556193e5d_small.jpeg "Venkatesh_M")

[Venkatesh\_M](https://community.sap.com/t5/user/viewprofilepage/user-id/116410)

Participant

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=hcm-blog-members&message.id=5102)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/hcm-blog-members/article-id/5102)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13565947)

‎2023 Mar 10
8:40 PM

[9
Kudos](/t5/kudos/messagepage/board-id/hcm-blog-members/message-id/5102/tab/all-users "Click here to see who gave kudos to this post.")

2,428

* SAP Managed Tags
* [SAP SuccessFactors Employee Central](https://community.sap.com/t5/c-khhcw49343/SAP%2520SuccessFactors%2520Employee%2520Central/pd-p/73555000100800000773)
* [SAP SuccessFactors Employee Central - Employee Profile](https://community.sap.com/t5/c-khhcw49343/SAP%2520SuccessFactors%2520Employee%2520Central%2520-%2520Employee%2520Profile/pd-p/445702386321465023058666394389900)
* [SAP SuccessFactors HCM Suite](https://community.sap.com/t5/c-khhcw49343/SAP%2520SuccessFactors%2520HCM%2520Suite/pd-p/67838200100800004730)
* [SAP SuccessFactors Platform](https://community.sap.com/t5/c-khhcw49343/SAP%2520SuccessFactors%2520Platform/pd-p/73555000100800000775)

* [SAP SuccessFactors Employee Central

  SAP SuccessFactors HCM](/t5/c-khhcw49343/SAP%2BSuccessFactors%2BEmployee%2BCentral/pd-p/73555000100800000773)
* [SAP SuccessFactors Employee Central - Employee Profile

  Software Product Function](/t5/c-khhcw49343/SAP%2BSuccessFactors%2BEmployee%2BCentral%2B-%2BEmployee%2BProfile/pd-p/445702386321465023058666394389900)
* [SAP SuccessFactors HCM Suite

  SAP SuccessFactors HCM](/t5/c-khhcw49343/SAP%2BSuccessFactors%2BHCM%2BSuite/pd-p/67838200100800004730)
* [SAP SuccessFactors Platform

  SAP SuccessFactors HCM](/t5/c-khhcw49343/SAP%2BSuccessFactors%2BPlatform/pd-p/73555000100800000775)

View products (4)

The frequent occurrence of accidental data deletion is largely attributed to human error and can result in the loss of critical employee or system data which may cause dominoes effect across the system landscape, and other consequences. While there are remedial measures such as running audit reports and data retrieval to address such incidents, it is essential to acknowledge that prevention is preferable to cure.

Therefore, organizations should take a proactive approach to prevent such incidents from occurring. Both technical and non-technical measures can be employed, but this article focuses on a technical solution that can prevent accidental data deletion

In this blog post, we’ll discuss how to remove delete option for any MDF portlet to avoid accidental data deletion

Let’s delve into two scenarios under each of the options - RBP and Configuration UI - to help you find the best fit for your needs.

### **Role Based Permissions (RBP):**

Let's start with the RBP option. This option is perfect if you want to grant different permissions for different roles, allowing you to keep the delete option for a few roles and remove it for others. However, keep in mind that this option can be time-consuming as you'll need to update all the concerned roles with the required permission for the concerned objects.

#### **Scenario 1:** **Portlet with base object which has effective dating**

Lets go through the steps to remove the "Delete" button of the portlet highlighted below

![](/legacyfs/online/storage/blog_attachments/2023/03/Picture1-14.png)

First, make sure to secure your MDF object, head to "Configure Object Definitions," choose the required object, and update the security section's fields as highlighted in the screenshot and save the object

![](/legacyfs/online/storage/blog_attachments/2023/03/Picture2-10.png)

![](/legacyfs/online/storage/blog_attachments/2023/03/Picture3-10.png)

Once you've secured the object, go to "Manager Permission Roles" to remove the delete option for the concerned role. Open the required role, click on the permission button to see permission settings, and uncheck the delete option in the selected permission category before saving the role.

![](/legacyfs/online/storage/blog_attachments/2023/03/Picture5-9.png)

You’ll no longer see the “Delete” button for the people who have that role.

![](/legacyfs/online/storage/blog_attachments/2023/03/Picture6-8.png)

#### **In scenario 2: Portlet which has a base object with no effective dating**

For the portlet which has composite association you can see “Trash” icon for each child record along with the “Delete” button at the bottom portlet as in scenario one

![](/legacyfs/online/storage/blog_attachments/2023/03/Picture7-9.png)

You'll need to secure both the parent and child objects using “Configure Object Definitions” as in scenario 1

Following parent object has effective date as none and has composite association with child object

![](/legacyfs/online/storage/blog_attachments/2023/03/Picture8-8.png)

![](/legacyfs/online/storage/blog_attachments/2023/03/Picture9-5.png)

Child object has effective dating from parent

![](/legacyfs/online/storage/blog_attachments/2023/03/Picture10-4.png)

Update the security section of both objects as below

![](/legacyfs/online/storage/blog_attachments/2023/03/Picture11-6.png)

Once securing the object go to “Manager Permission Roles” to remove the delete option for concerned role as in scenario 1

As you can see there is no delete option for parent object as it has no effective dating ,its only available for child object. Uncheck delete option for child object and save the role

![](/legacyfs/online/storage/blog_attachments/2023/03/Picture12-8.png)

Unfortunately, the delete permission of the child object only works for the "Trash" icon and not for the "Delete" button of the portlet, as it's one of the limitations under RBP option for objects without effective dating.

![](/legacyfs/online/storage/blog_attachments/2023/03/Picture13-7.png)

### **Configuration UI:**

If you're looking for an easier option, the Configuration UI option is the way to go. This option removes the delete option for all roles, saving you the time and effort of updating individual roles. Here we don’t need to perform any of the two steps which performed under RBP option

#### **Scenario 1:** **Portlet with base object which has effective dating**

Go to "Manage Configuration UI," search for the UI ID created for the base object, click on edit properties and set the delete record field to “No” under control options section and save

![](/legacyfs/...