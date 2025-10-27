---
title: How to handle repair production order in SAP Digital Manufacturing Cloud(DMC)
url: https://blogs.sap.com/2023/02/05/how-to-handle-repair-production-order-in-sap-digital-manufacturing-clouddmc/
source: SAP Blogs
date: 2023-02-06
fetch_date: 2025-10-04T05:47:29.670817
---

# How to handle repair production order in SAP Digital Manufacturing Cloud(DMC)

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Product Lifecycle Management](/t5/product-lifecycle-management/ct-p/plm)
* [PLM Blog Posts by Members](/t5/product-lifecycle-management-blog-posts-by-members/bg-p/plm-blog-members)
* How to handle repair production order in SAP Digit...

Product Lifecycle Management Blog Posts by Members

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/plm-blog-members/article-id/1428&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [How to handle repair production order in SAP Digital Manufacturing Cloud(DMC)](/t5/product-lifecycle-management-blog-posts-by-members/how-to-handle-repair-production-order-in-sap-digital-manufacturing-cloud/ba-p/13552922)

![pooja_yadav](https://avatars.profile.sap.com/d/9/idd9a6194e1eda6e0519a2f38c99cb5e2fb6a801affe6507c07f78efd5e7224e1e_small.jpeg "pooja_yadav")

[pooja\_yadav](https://community.sap.com/t5/user/viewprofilepage/user-id/47171)

Explorer

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=plm-blog-members&message.id=1428)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/plm-blog-members/article-id/1428)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13552922)

‎2023 Feb 05
9:20 AM

[9
Kudos](/t5/kudos/messagepage/board-id/plm-blog-members/message-id/1428/tab/all-users "Click here to see who gave kudos to this post.")

3,127

* SAP Managed Tags
* [SAP Digital Manufacturing](https://community.sap.com/t5/c-khhcw49343/SAP%2520Digital%2520Manufacturing/pd-p/73555000100800001492)

* [SAP Digital Manufacturing

  SAP Digital Manufacturing](/t5/c-khhcw49343/SAP%2BDigital%2BManufacturing/pd-p/73555000100800001492)

View products (1)

In this blog, I would like to show how to handle repair production orders in SAP Digital Manufacturing Cloud(DMC).

                                                                  Repair production orders are created to correct the defects. Such orders will be without the reference to material so that labor cost will capture only. Currently DMC, supports the order with valid material number but to capture labor hours on repair Order, material may not be needed. So, such order without the material will get failed in DMC. In this blog, you will see a way to handle repair orders in DMC.

**Prerequisites-**

1. Create a dummy material in DMC.

2. Modify the Production Orders (LIOPRO05 V2) custom XSLT to accept the order without material in Manage Integration Workflows app in DMC.

**Creating a dummy Material in DMC**

1. Go to Manage material app.

2. Click “+” to create new material.

3. ![](/legacyfs/online/storage/blog_attachments/2023/01/material_manage.jpg)Under Main section, filled all the mandatory fields.![](/legacyfs/online/storage/blog_attachments/2023/01/material_main.jpg)

4. Under Alternate UOM section, add UOM![](/legacyfs/online/storage/blog_attachments/2023/01/material_uom.jpg)

5. Under Build section, make sure Order Processing Mode field have “**Use ERP and Routing (Default value)**” value.![](/legacyfs/online/storage/blog_attachments/2023/01/material_build.jpg)

6. Click save.

7. Dummy material is created.

**Modifying Production Order Custom XSLT to accept the production order without material**

We must modify in the below nodes in XSLT, so that DMC accept the order without material-

1. Node : ManufacturingOrder => Material

   ```
   <Material>

       <!---Added for rework order|Header Material-->

       <xsl:choose>

           <xsl:when test="MATNR">

               <xsl:value-of select="MATNR"/>

           </xsl:when>

           <xsl:otherwise>

               <xsl:variable name="material" select="'NULL_ECC'"/>

               <xsl:value-of select="$material"/>

           </xsl:otherwise>

       </xsl:choose>

   </Material>

   ​
   ```

2. Node : ManufacturingOrder ==> BillOfMaterial

   ```
   <BillOfMaterial>

   <!-- Added for Rework Order | Bill of material Number-->

   <xsl:choose>

       <xsl:when test="MATNR">

           <xsl:value-of select="STLNR"/>

       </xsl:when>

       <xsl:otherwise>

           <xsl:variable name="BillofMaterial" select="'02110817'"/>

           <xsl:value-of select="$BillofMaterial"/>

       </xsl:otherwise>

   </xsl:choose>

   </BillOfMaterial>

   ​
   ```

3. Node : ManufacturingOrder ==> BillOfMaterialVariant

   ```
   <BillOfMaterialVariant>

       <!-- Added for Rework Order | Bill of material Variant-->

       <xsl:choose>

           <xsl:when test="MATNR">

               <xsl:value-of select="STLAL"/>

           </xsl:when>

           <xsl:otherwise>

               <xsl:variable name="BillofMaterial" select="'1'"/>

               <xsl:value-of select="$BillofMaterial"/>

           </xsl:otherwise>

       </xsl:choose>

   </BillOfMaterialVariant>

   ​
   ```

4. Node : ManufacturingOrder ==> BillOfMaterialVariantUsage

   ```
   <BillOfMaterialVariantUsage>

       <!-- Added for Rework Order | Bill of material Variant usage-->

       <xsl:choose>

           <xsl:when test="MATNR">

               <xsl:value-of select="STLAN"/>

           </xsl:when>

           <xsl:otherwise>

               <xsl:variable name="BillofMaterial" select="'1'"/>

               <xsl:value-of select="$BillofMaterial"/>

           </xsl:otherwise>

       </xsl:choose>

   </BillOfMaterialVariantUsage>

   ​
   ```

5. Node : ManufacturingOrder ==> MfgOrdPlndTotQtyInBaseUnit (if missed this, you will not able to release the order).

   ```
   <MfgOrdPlndTotQtyInBaseUnit pp:unitCode="{BMEINS}">

       <!-- Added for Rework Order | Planned Quantity-->

       <xsl:choose>

           <xsl:when test="MATNR">

               <xsl:value-of select="BMENGE"/>

           </xsl:when>

           <xsl:otherwise>

               <xsl:value-of select="GAMNG"/>

           </xsl:otherwise>

       </xsl:choose>

   </MfgOrdPlndTotQtyInBaseUnit>

   ​
   ```

6. Create new </pp:ManufacturingOrderComponent> node for when order doesn’t have material.

   ```
   <!--Added for Rework Order | Generating Bill of material payload with hardcoded values -->

   <xsl:if test="not(E1RESBL) and not(string(/LOIPRO05/IDOC/E1AFKOL/MATNR))">

       <pp:ManufacturingOrderComponent>

           <RequirementType>AR</RequirementType>

           <Material>NULL_ECC</Material>

           <Reservation>0102637848</Reservation>

           <ReservationItem>10</ReservationItem>

           <GoodsMovementType>261</GoodsMovementType>

           <BillOfMaterialItemNumber>10</BillOfMaterialItemNumber>

           <BillOfMaterialItemCategory>L</BillOfMaterialItemCategory>

           <ManufacturingOrderItem>0000</ManufacturingOrderItem>

           <BillOfMaterial>02038353</BillOfMaterial>

           <SupplyArea>

               <xsl:value-of select="PRVBE"/>

           </SupplyArea>

           <StorageLocation>0001</StorageLocation>

           <RequiredQuantityInBaseUnit pp:unitCode="GLL">1</RequiredQuantityInBaseUnit>

           <Warehouse>

               <xsl:value-of select="LGNUM"/>

           </Warehouse>

           <MatlCompIsMarkedForBackflush>

               <xsl:call-template name="convertToBool">

                   <xsl:with-param name="bool" select="BACKFLUSH"/>

               </xsl:call-template>

           </MatlCompIsMarkedForBackflush>

           <MaterialIsCoProduct>

               <xsl:call-template name...