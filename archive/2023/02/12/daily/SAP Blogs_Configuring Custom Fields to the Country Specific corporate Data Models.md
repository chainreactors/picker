---
title: Configuring Custom Fields to the Country Specific corporate Data Models
url: https://blogs.sap.com/2023/02/11/configuring-custom-fields-to-the-country-specific-corporate-data-models/
source: SAP Blogs
date: 2023-02-12
fetch_date: 2025-10-04T06:25:45.439785
---

# Configuring Custom Fields to the Country Specific corporate Data Models

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Human Capital Management](/t5/human-capital-management/ct-p/hcm)
* [HCM Blog Posts by Members](/t5/human-capital-management-blog-posts-by-members/bg-p/hcm-blog-members)
* Configuring Custom Fields to the Country Specific ...

Human Capital Management Blog Posts by Members

Explore blogs from customers or SAP partners to gain best practices and fresh insights to succeed.

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/hcm-blog-members/article-id/5115&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [Configuring Custom Fields to the Country Specific corporate Data Models](/t5/human-capital-management-blog-posts-by-members/configuring-custom-fields-to-the-country-specific-corporate-data-models/ba-p/13566794)

![Haridha_Ponnusamy](https://avatars.profile.sap.com/4/7/id47d2662c0ea52124500baac0bee1936f19966c6c3aa97a99a1269e038f04157d_small.jpeg "Haridha_Ponnusamy")

[Haridha\_Ponnusamy](https://community.sap.com/t5/user/viewprofilepage/user-id/118171)

Participant

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=hcm-blog-members&message.id=5115)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/hcm-blog-members/article-id/5115)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13566794)

‎2023 Feb 11
5:03 PM

[4
Kudos](/t5/kudos/messagepage/board-id/hcm-blog-members/message-id/5115/tab/all-users "Click here to see who gave kudos to this post.")

7,216

* SAP Managed Tags
* [SAP SuccessFactors Employee Central](https://community.sap.com/t5/c-khhcw49343/SAP%2520SuccessFactors%2520Employee%2520Central/pd-p/73555000100800000773)
* [SAP SuccessFactors HCM Core](https://community.sap.com/t5/c-khhcw49343/SAP%2520SuccessFactors%2520HCM%2520Core/pd-p/67837800100800006332)

* [SAP SuccessFactors HCM Core

  SAP SuccessFactors HCM](/t5/c-khhcw49343/SAP%2BSuccessFactors%2BHCM%2BCore/pd-p/67837800100800006332)
* [SAP SuccessFactors Employee Central

  SAP SuccessFactors HCM](/t5/c-khhcw49343/SAP%2BSuccessFactors%2BEmployee%2BCentral/pd-p/73555000100800000773)

View products (2)

## Introduction

Configuring Custom Fields to the Country Specific corporate Data Models. Currently there are 7 fields listed below with hard-coded sync-mappings delivered with the corporate Address element.

1. addressLine1

2. addressLine2

3. addressLine3

4. city

5. state

6. zip-code

7. country

![](/legacyfs/online/storage/blog_attachments/2023/02/Business-address.png)

For example: If there if a requirement to customize the corporate address format of India to have an additional field like Floor, Street name, Number etc... based on organizational needs, follow the below configuration steps.

## Country/Region Specific Corporate Data Model

The foundation objects from Corporate Data Model that need to be localized based on the country/region are configured in Country Specific corporate data model. In case the configuration for a particular country/region is missing, the definition in the Corporate Data Model is used.

## Steps to add a custom Fields.

The following steps are used in adding a custom field to the Country Specific corporate data model.

### Export Country Specific Corporate Data Models

* Navigate to Provisioning >> Succession Management >> Import/Export Country/Region Specific XML for Corporate Data Model >> Select *Export*.

Save the file in the folder containing the DTD files from the course files.

* ![](/legacyfs/online/storage/blog_attachments/2023/02/Country-specific-corporate-data-model-Provisioning-1.png)

Country specific corporate data model-Provisioning

* To download from Instance, Go to: Admin Center > Import/Export Country/Region-Specific XML for Corporate Data Model.

  *Verify the below permission is enabled in RBP:*

  *Administrator Permissions > Manage Foundation Objects > Import/Export Corporate Data Model and Import/Export Country/Region-Specific XML for Corporate Data Model.*

  ![](/legacyfs/online/storage/blog_attachments/2023/02/Country-specific-corporate-data-model-Instance-2.png)*Country specific corporate data model-Instance*

### Updating custom fields using XML

1. Open the CSF for the Corporate data model in your XML editor.

2. Go to the country "IND".

   ![](/legacyfs/online/storage/blog_attachments/2023/02/Corporate-data-model-India.png)

   Country specific corporate data model

3. Add the below XML example wherever required in the Corporate Address HRIS Element, to configure your corporate address for India.

   *<hris-field max-length="256" id="custom-string1" visibility="both">*
   *<label>Floor</label>* *</hris-field>*

   *<hris-field max-length="256" id="custom-string2" visibility="both">
   <label>Street Name</label>*
   *</hris-field>*

   *![](/legacyfs/online/storage/blog_attachments/2023/02/Corporate-data-model-Updated.png)*

   Corporate data model-Updated

4. Save a new version of the CSF Corporate Data Model.

5. Use the Action Search in instance or provisioning to navigate to the Import/Export Country/Region-Specific XML.

6. Upload the CSF Corporate Data Model.

7. Navigate to ***Manage Organization, Pay and Job Structures***.

8. Go to *Create New → Location,* the Country to India to verify that the Foundation Object meets the requirements and updated with custom fields.

   1. ![](/legacyfs/online/storage/blog_attachments/2023/02/Updated-CS-Corporate-Data-Model.png) *Updated CS Corporate Data Model*

## Conclusion

Hope this article clarifies how you add custom Fields to the Country Specific corporate Data Models. Hope the above approach helps with your business requirements.

Please visit the below resources to learn more about SAP Core HR solutions.

* [SAP SuccessFactors Employee Central Main Website](https://www.sap.com/products/human-resources-hcm.html)

* [SAP SuccessFactors Employee Central SAP Help](https://help.sap.com/viewer/product/SAP_SUCCESSFACTORS_EMPLOYEE_CENTRAL/latest/en-US)

* [SAP SuccessFactors Community – Employee Central](https://community.successfactors.com/t5/Employee-Central/ct-p/EmployeeCentral)

*Note: The images in the blog are taken from internal Demo Instances and owned by me.*

Please feel free to share thoughts & suggestions in the comments. If you have any questions, please let me know.

* [EmployeeCentral](/t5/tag/EmployeeCentral/tg-p/board-id/hcm-blog-members)
* [successfactors](/t5/tag/successfactors/tg-p/board-id/hcm-blog-members)

You must be a registered user to add a comment. If you've already registered, sign in. Otherwise, register and sign in.

* [Comment](/plugins/common/feature/oidcss/sso_login_redirect/providerid/sap_ids_prompt?redirectreason=permissiondenied&referer=https%3A%2F%2Fcommunity.sap.com%2Ft5%2Fhuman-capital-management-blog-posts-by-members%2Fconfiguring-custom-fields-to-the-country-specific-corporate-data-models%2Fba-p%2F13566794%23comment-on-this)

Copy Link
![](https://community.sap.com/html/@EE5D5986E9F4E5657DCEACB7532B5C39/assets/bluesky-dark.svg)Bluesky
Linkedin

Related Content

* [SAP BTP for HR at SAP Connect and Success Connect 2025 summary - bigger and better than ever](/t5/human-capital-management-blog-posts-by-sap/sap-btp-for-hr-at-sap-connect-and-success-connect-2025-summary-bigger-and/ba-p/14209124)
  in [Human Capital Management Blog Posts by SAP](/t5/human-capital-management-blog-posts-by-sap/bg-p/hcm-blog-sap)  a month...