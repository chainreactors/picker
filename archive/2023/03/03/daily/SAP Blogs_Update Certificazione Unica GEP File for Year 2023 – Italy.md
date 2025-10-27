---
title: Update Certificazione Unica GEP File for Year 2023 – Italy
url: https://blogs.sap.com/2023/03/02/update-certificazione-unica-gep-file-for-year-2023-italy/
source: SAP Blogs
date: 2023-03-03
fetch_date: 2025-10-04T08:31:52.408682
---

# Update Certificazione Unica GEP File for Year 2023 – Italy

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Enterprise Resource Planning](/t5/enterprise-resource-planning/ct-p/erp)
* [ERP Blog Posts by SAP](/t5/enterprise-resource-planning-blog-posts-by-sap/bg-p/erp-blog-sap)
* Update Certificazione Unica GEP File for Year 2023...

Enterprise Resource Planning Blog Posts by SAP

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/erp-blog-sap/article-id/51793&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [Update Certificazione Unica GEP File for Year 2023 - Italy](/t5/enterprise-resource-planning-blog-posts-by-sap/update-certificazione-unica-gep-file-for-year-2023-italy/ba-p/13559860)

![MayaSchnabel](https://avatars.profile.sap.com/3/1/id31609a242fa13c8b9ffbe3f9c23ebdcf7391b9af4b9197a5060440894aa30d6f_small.jpeg "MayaSchnabel")

![Advisor](/html/@138D6F765B60D7FC0168643DE27D8A68/rank_icons/sap-logo-small-14px.png "Advisor")
[MayaSchnabel](https://community.sap.com/t5/user/viewprofilepage/user-id/11260)

Advisor

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=erp-blog-sap&message.id=51793)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/erp-blog-sap/article-id/51793)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13559860)

‎2023 Mar 02
10:49 PM

[4
Kudos](/t5/kudos/messagepage/board-id/erp-blog-sap/message-id/51793/tab/all-users "Click here to see who gave kudos to this post.")

1,989

* SAP Managed Tags
* [SAP Business One](https://community.sap.com/t5/c-khhcw49343/SAP%2520Business%2520One/pd-p/01200615320800000816)
* [SAP Business One, version for SAP HANA](https://community.sap.com/t5/c-khhcw49343/SAP%2520Business%2520One%252C%2520version%2520for%2520SAP%2520HANA/pd-p/67838200100800004775)

* [SAP Business One

  SAP Business One](/t5/c-khhcw49343/SAP%2BBusiness%2BOne/pd-p/01200615320800000816)
* [SAP Business One, version for SAP HANA

  SAP Business One](/t5/c-khhcw49343/SAP%2BBusiness%2BOne%25252C%2Bversion%2Bfor%2BSAP%2BHANA/pd-p/67838200100800004775)

View products (2)

An amended layout of the withholding tax **single certification** (*Certificazione Unica*) is required by the Ministry of Finance of Italy for declarations made for the year 2023.

If you currently not intend to upgrade to version 10 FP 2208 HF01 or higher of SAP Business One and SAP Business One, version for SAP HANA, you can update the previous layout of the withholding tax single certification to a new one for year 2023 using the steps described in this blog, including the update of header and tax date indicators.

**Let's start**

There are two GEP files for different databases: MS SQL and SAP HANA. The following procedure takes MS SQL as an example, and you will get a new GEP file for year 2023 for the database of MS SQL.

1. **Download the official report template** (PDF file) from the tax authority site (e.g. [Modello sintetico CU 2023 - pdf](https://www.agenziaentrate.gov.it/portale/documents/20143/4913767/CU_modSIN_2023.pdf/555f8704-fe5f-5dd6-616e-8b2103e610c7)). From this file you can find the header and tax date indicators for year 2023. Use your tool to capture them and save them as image files. It is recommended to save them in PNG format.![](/legacyfs/online/storage/blog_attachments/2023/03/1_report-template.png)

2. **Download the 2022 GEP file** in the *Electronic File Manager - Setup* window (*Administration*→ *Setup*→ *General*→ *Electronic File Manager*). Right-click row *Italy Single Certification Report 2.8 (System)* and choose *Download*. You now have the GEP file of version 2.8.

   ![](/legacyfs/online/storage/blog_attachments/2023/03/2_EFM.png)

3. **Extract RPT files** - Start the electronic file manager to open the 2022 GEP file downloaded in step 2. In the format explorer, you can see two RPT files: *Report\_Ordinario\_2022* and *Report\_Sintetico\_2022*. Right-click each RPT file and choose *Save As...*to save them as the files to which you will make the changes.![](/legacyfs/online/storage/blog_attachments/2023/03/3_Save-as.png)

4. **Replace with new header of year 2023** – start SAP Crystal Reports to update the two files saved in step 3.

* Open the file saved from *Report\_Ordinario\_2022.rpt*, insert the images saved in step 1, and use them to cover the 2022 header on pages 1 and 2, and the 2022 tax date indicators on page 2. Save this RPT file as a new file *Report\_Ordinario\_2023.rpt* and close it.

* Open the file saved from *Report\_Sintetico\_2022.rpt*, insert the images saved in step 1, and use them to cover the 2022 header and tax date indicators on page 1. Save this RPT file as a new file *Report\_Sintetico\_2023.rpt* and close it.![](/legacyfs/online/storage/blog_attachments/2023/03/4_Picture.png)

5. **Package RPT into GEP** - Return to the electronic file manager with the 2022 GEP file.

* Right-click *Report\_Ordinario\_2022*, choose *Update*, and select the new file *Report\_Ordinario\_2023.rpt* in step 4. A message appears when it is updated successfully. Delete the old file *Report\_Ordinario\_2022*.

* Right-click *Report\_Sintetico\_2022*, choose *Update*, and select the new file *Report\_Sintetico\_2023.rpt* in step 4. A message appears when it is updated successfully. Delete the old file *Report\_Sintetico\_2022*. **NOTE**: in the format explorer, the ordinary report (*Report\_Ordinario\_2023.rpt*) must be above the simplified report (*Report\_Sintetico\_2023.rpt*). You can always use *Move Up* or *Move Down* in the right-click menu to change their order.

6. **Increase version** - In the format explorer, select the root node (*Italy Single Certification Report 2.80 (SYSTEM, MSSQL)*), and update the version number to a new one, e.g., 2.9, in three properties: *Version*, *Name*, and *Description*. **NOTE**: you can also add new entries in the supported version list, such as 10.00.200, 10. 00.210. However, this is not mandatory.![](/legacyfs/online/storage/blog_attachments/2023/03/6_Increas-version.png)

7. **Save new GEP file** - Save the updated format as follows as a new GEP file, e.g. *Italy Single Certification Report 2.9 (System).GEP*. Upload this new GEP file to SAP Business One, and you can run the withholding tax single certification for year 2023 with this new format.![](/legacyfs/online/storage/blog_attachments/2023/03/7_last.png)

This solution can serve you next year as well if no other major changes will be required, and if you do not intend to go for immediate version upgrade.

More information can be found in SAP Notes:  **[3301826](https://launchpad.support.sap.com/#/notes/3301826)** and  [**3303978**](https://launchpad.support.sap.com/#/notes/3303978)

and in the tax authorities site: [https://www.agenziaentrate.gov.it/portale/web/guest/certificazione-unica-2023/infogen-certificazione...](https://www.agenziaentrate.gov.it/portale/web/guest/certificazione-unica-2023/infogen-certificazione-unica-2023)

Credits to: libin.yan

Labels

* [Product Updates](/t5/enterprise-resource-planning-blog-posts-by-sap/bg-p/erp-blog-sap/label-name/product%20updates)

* [b1pminsights](/t5/tag/b1pminsights/tg-p/board-id/erp-blog-sap)
* [italy](/t5/tag/italy/tg-p/board-id/erp-blog-sap)
* [Unica](/t5/tag/Unica/tg-p/board-id/erp-blog-sap)

You must be a registered user to add a comment. If you've already registered, sign in. Otherwise, register and sign in.

* [Comment](/plugins/common/feature/oidcss/sso_...