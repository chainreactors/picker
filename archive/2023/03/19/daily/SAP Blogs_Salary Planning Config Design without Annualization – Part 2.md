---
title: Salary Planning Config Design without Annualization – Part 2
url: https://blogs.sap.com/2023/03/18/salary-planning-config-design-without-annualization-part-2/
source: SAP Blogs
date: 2023-03-19
fetch_date: 2025-10-04T10:02:23.935237
---

# Salary Planning Config Design without Annualization – Part 2

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Human Capital Management](/t5/human-capital-management/ct-p/hcm)
* [HCM Blog Posts by Members](/t5/human-capital-management-blog-posts-by-members/bg-p/hcm-blog-members)
* Salary Planning Config Design without Annualizatio...

Human Capital Management Blog Posts by Members

Explore blogs from customers or SAP partners to gain best practices and fresh insights to succeed.

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/hcm-blog-members/article-id/4866&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [Salary Planning Config Design without Annualization - Part 2](/t5/human-capital-management-blog-posts-by-members/salary-planning-config-design-without-annualization-part-2/ba-p/13552498)

![Venkatesh_M](https://avatars.profile.sap.com/3/5/id35b0127b0929631ab3b5072196696f9ba842fbb5072c4c0288669ba556193e5d_small.jpeg "Venkatesh_M")

[Venkatesh\_M](https://community.sap.com/t5/user/viewprofilepage/user-id/116410)

Participant

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=hcm-blog-members&message.id=4866)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/hcm-blog-members/article-id/4866)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13552498)

‎2023 Mar 18
8:01 AM

0
Kudos

1,033

* SAP Managed Tags
* [SAP SuccessFactors Compensation](https://community.sap.com/t5/c-khhcw49343/SAP%2520SuccessFactors%2520Compensation/pd-p/73555000100800000771)
* [SAP SuccessFactors Employee Central](https://community.sap.com/t5/c-khhcw49343/SAP%2520SuccessFactors%2520Employee%2520Central/pd-p/73555000100800000773)
* [SAP SuccessFactors Employee Central - Employee Profile](https://community.sap.com/t5/c-khhcw49343/SAP%2520SuccessFactors%2520Employee%2520Central%2520-%2520Employee%2520Profile/pd-p/445702386321465023058666394389900)
* [SAP SuccessFactors HCM Suite](https://community.sap.com/t5/c-khhcw49343/SAP%2520SuccessFactors%2520HCM%2520Suite/pd-p/67838200100800004730)

* [SAP SuccessFactors HCM Suite

  SAP SuccessFactors HCM](/t5/c-khhcw49343/SAP%2BSuccessFactors%2BHCM%2BSuite/pd-p/67838200100800004730)
* [SAP SuccessFactors Compensation

  SAP SuccessFactors HCM](/t5/c-khhcw49343/SAP%2BSuccessFactors%2BCompensation/pd-p/73555000100800000771)
* [SAP SuccessFactors Employee Central

  SAP SuccessFactors HCM](/t5/c-khhcw49343/SAP%2BSuccessFactors%2BEmployee%2BCentral/pd-p/73555000100800000773)
* [SAP SuccessFactors Employee Central - Employee Profile

  Software Product Function](/t5/c-khhcw49343/SAP%2BSuccessFactors%2BEmployee%2BCentral%2B-%2BEmployee%2BProfile/pd-p/445702386321465023058666394389900)

View products (4)

This is the second part of the topic “Salary planning without Annualization”. In this blog, we are going to discuss the EC approach for performing salary review on monthly income. I would encourage you to go through the first part <https://blogs.sap.com/2023/03/17/salary-planning-config-design-without-annualization-part-1/>to get the context in more detail.

The annualization concept is not specific to the compensation module, it happens across the SF suite including EC. Our plan is not to stop annualization in EC unlike in the Comp approach, being the source to all talent modules, doing that can derail the processes. We’ll create a parallel setup in EC which would be in sync with EC but without hindering EC’s annualization.

It might sound confusing until you see the result. Just to confirm again, here we are not doing any changes that we have done in the Comp approach and the status of the solution is the same as in the background of the issue section of part 1 and now we are going to resolve that issue by doing required changes in EC.

Let's divide the EC approach into two activities, creating a parallel pay component and creating parallel pay ranges and each activity is further divided into steps. Like in the comp approach, at the end of each activity, we’ll see the output to know the status. Without further due, let's dive right into the design process

### **Creating Parallel pay component:**

**Step 1: Create a new frequency instance**

Go to “Manage organization, pay and job structures” to create the new frequency instance with annualization factor 1

![](/legacyfs/online/storage/blog_attachments/2023/03/Picture1-31.png)

**Step 2: Update the existing pay component of the monthly pay**

Use the same tool to update the “Used for Comp Planning” field to “None” for the existing monthly income pay component

![](/legacyfs/online/storage/blog_attachments/2023/03/Picture2-25.png)

**Step 3: Create a new pay component for monthly pay**

Then within the same tool, you can create the new pay component by using the newly created frequency along with updating the “Used for Comp Planning” field to “Comp”

![](/legacyfs/online/storage/blog_attachments/2023/03/Picture3-20.png)

**Step 4: Create a business rule to default the new pay component**

Go to “Configure business rules” to create the business rule which automatically creates the new pay component for the employees based on EC’s existing monthly pay by copying the amount and currency from existing pay competent but with the new frequency which we created earlier

![](/legacyfs/online/storage/blog_attachments/2023/03/Screenshot-2023-03-17-195923.png)

**Step 5: Assign the business rule to comp info portlet**

Go to “Manage business configuration” to assign the newly created business rule to the comp info portlet with event type OnSave which means it would be triggered while saving the comp info for an employee

![](/legacyfs/online/storage/blog_attachments/2023/03/Picture5-18.png)

**Step 6: Grant view permission for the new pay component**

Go to “Manage permission roles” to grant the view permission for the newly created pay component for the concerned roles

![](/legacyfs/online/storage/blog_attachments/2023/03/Picture6-16.png)

**Step 7: Assign the new pay component to the employees**

If you want to assign this new pay component for a few employees, you can go to their employee profile and re-save their comp info portlet to have this pay component automatically created which you can’t edit. If you want to do it for multiple employees you can use the “Import employee data” functionality

![](/legacyfs/online/storage/blog_attachments/2023/03/Picture7-18.png)

**Output:**

Except for the pay ranges, it seems everything is correct including merit and budget.

![](/legacyfs/online/storage/blog_attachments/2023/03/Picture8-15.png)

Click to enlarge

![](/legacyfs/online/storage/blog_attachments/2023/03/Picture9-10.png)

### **Creating parallel pay ranges:**

As the system couldn't find the pay ranges with the comp frequency instance “CM”, pay ranges are blank. Now we'll create the parallel pay ranges for comp**.**

**Step 1: Export the pay ranges from the system**

As you can’t export the foundation object data directly from the system, create a table report to export the data as follows.

![](/legacyfs/online/storage/blog_attachments/2023/03/Screenshot-2023-03-17-193711.png)

**Step 2: Create a duplicate file from an exported file**

Once you have exported the file, you can just create a duplicate copy of the file using the save-as option and then update the columns “Pay Range ID” and “Frequency”

You can just add the prefix “Comp” to the existing ids to serve the purpose and r...