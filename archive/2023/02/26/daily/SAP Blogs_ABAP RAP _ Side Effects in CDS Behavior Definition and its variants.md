---
title: ABAP RAP : Side Effects in CDS Behavior Definition and its variants
url: https://blogs.sap.com/2023/02/25/abap-rap-side-effects-in-in-cds-behavior-definition-and-its-variants/
source: SAP Blogs
date: 2023-02-26
fetch_date: 2025-10-04T08:08:27.429812
---

# ABAP RAP : Side Effects in CDS Behavior Definition and its variants

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Technology](/t5/technology/ct-p/technology)
* [Technology Blog Posts by Members](/t5/technology-blog-posts-by-members/bg-p/technology-blog-members)
* ABAP RAP : Side Effects in CDS Behavior Definition...

Technology Blog Posts by Members

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/technology-blog-members/article-id/161363&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [ABAP RAP : Side Effects in CDS Behavior Definition and its variants](/t5/technology-blog-posts-by-members/abap-rap-side-effects-in-cds-behavior-definition-and-its-variants/ba-p/13557872)

![Ramjee_korada](https://avatars.profile.sap.com/a/6/ida68feb06dad0280b54c7e92a0996c1389c5cbe26af62aeffa035d47c94865194_small.jpeg "Ramjee_korada")

[Ramjee\_korada](https://community.sap.com/t5/user/viewprofilepage/user-id/10276)

Active Contributor

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=technology-blog-members&message.id=161363)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/technology-blog-members/article-id/161363)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13557872)

‎2023 Feb 25
12:53 PM

[7
Kudos](/t5/kudos/messagepage/board-id/technology-blog-members/message-id/161363/tab/all-users "Click here to see who gave kudos to this post.")

10,781

* SAP Managed Tags
* [SAP BTP ABAP environment](https://community.sap.com/t5/c-khhcw49343/SAP%2520BTP%2520ABAP%2520environment/pd-p/73555000100800001164)
* [SAP Fiori Elements](https://community.sap.com/t5/c-khhcw49343/SAP%2520Fiori%2520Elements/pd-p/ed5c1ef6-932f-4c19-b2ba-1be375109ff5)
* [SAP S/4HANA Cloud ABAP Environment](https://community.sap.com/t5/c-khhcw49343/SAP%2520S%252F4HANA%2520Cloud%2520ABAP%2520Environment/pd-p/60907aa9-99e9-4d5d-9103-8b970e9bc0a4)
* [ABAP Development](https://community.sap.com/t5/c-khhcw49343/ABAP%2520Development/pd-p/833755570260738661924709785639136)
* [ABAP RESTful Application Programming Model](https://community.sap.com/t5/c-khhcw49343/ABAP%2520RESTful%2520Application%2520Programming%2520Model/pd-p/7e44126e-7b27-471d-a379-df205a12b1ff)

* [ABAP Development

  Programming Tool](/t5/c-khhcw49343/ABAP%2BDevelopment/pd-p/833755570260738661924709785639136)
* [SAP BTP ABAP environment

  SAP Business Technology Platform](/t5/c-khhcw49343/SAP%2BBTP%2BABAP%2Benvironment/pd-p/73555000100800001164)
* [ABAP RESTful Application Programming Model

  Software Product Function](/t5/c-khhcw49343/ABAP%2BRESTful%2BApplication%2BProgramming%2BModel/pd-p/7e44126e-7b27-471d-a379-df205a12b1ff)
* [SAP Fiori Elements

  Software Product Function](/t5/c-khhcw49343/SAP%2BFiori%2BElements/pd-p/ed5c1ef6-932f-4c19-b2ba-1be375109ff5)
* [SAP S/4HANA Cloud ABAP Environment

  Additional Software Product](/t5/c-khhcw49343/SAP%2BS%25252F4HANA%2BCloud%2BABAP%2BEnvironment/pd-p/60907aa9-99e9-4d5d-9103-8b970e9bc0a4)

View products (5)

​​​

**Introduction:**

​The most awaited feature was released for SAP BTP - ABAPEnvironment in 2302. It is none other than 'Side effects in CDS Behavior Definition'.

I have been waiting for this feature and can't stop myself from trying it. I thought the syntax would be complicated and was surprised when I realized they were so simple and readable.

​​​Side effects are useful in UI scenarios based on draft-enabled BOs to notify a Fiori Elements UI that data changes of defined fields require the recalculation of other data values, permissions or messages  .​

Earlier we had to use annotations in Fiori Application to refresh the target elements on the UI automatically. Th​is​ new features reduce the dependency on UI development and help backend developers to test functions in ADT preview itself. ​

Multiple variants are already available and t​his blog post describes most used cases and other features are yet to be explored.

1. Side effects in the same entity on field change

2. Side effects in different entities on a field change

3. Side effects in different entities on a custom action.

T​o demonstrate and focus on this feature, a well-known travel data model with booking as a composition child and OData v4 + Draft is considered .

**Use case:**

In this example, Travel is the root entity and Booking as a composition ​child. Total price on travel entity is a read only field and it is the summation of Booking-fee on ​Travel entity and Flight-Price from each Booking entity.

That means Total-Price needs to be updated whenever

* booking-fee is changed or

* new booking is created or

* Flight price is changed.

To complicate things a little, let us introduce a custom action to apply discounts on selective flight bookings. So that flight prices are recalculated and also Total price on Travel is also calculated and reflected on UI.

**Implementation approach:**

1. ​Develop the Fiori elements application using RAP-CDS-Modeling. ​

2. ​Define the required determinations and actions on the specified entities.

3. ​​Implement the business logic in ​respective Behavior Pool classes

4. Identify the source properties and target properties/entities for side effects

5. Define the side effects in Behavior definition ( note: Only once side effects can be defined in a behavior definition )

6. ​Expose the side​ effects in Projection level behavior definition so that they are available UI consumption.

**​**​**I****​mp​lementation steps:**

1. ​Develop the fiori elements application using RAP-CDS-Modeling.

   * ​Travel ZRK\_SDE\_I\_TRAVEL and Booking zrk\_sde\_i\_booking entities have been generated and ​defined its Behavior definition  ZRK\_SDE\_I\_TRAVEL .

   * As the focus of the blog post is not about data model and to keep the blog post simple, Source code is published in [git repository](https://github.com/koradaramjee789/ZRK_SIDE_EFFECTS_RAP.git).

2. Define the required determinations and actions on the specified entities.

   1. ​Determination Calculate\_Total\_price in Travel entity.

      ```
       determination Calculate_Total_price on modify { field BookingFee; }
      ```

   2. ​Determination Calculate\_Total\_price in Booking entity.

      ```
      determination calculate_Total_Price on modify { create;  field flightprice; }
      ```

   3. Internal action ReCalcTotalPrice​ in Travel entity which is in turn executed in above 2 steps so that business logic is implemented once and consistent. ​

      ```
      internal action ReCalcTotalPrice;
      ```

   4. Custom action Apply\_Discount​ in Booking entity​

      ```
       action Apply_Discount parameter zrk_sde_a_apply_disc result [1] $self;
      ```

3. Implement the business logic in ​respective Behavior Pool classes.

   ```
   *************** calculate_Total_Price at Travel Entity

     METHOD Calculate_Total_price.

       "update involved instances

       MODIFY ENTITIES OF zrk_sde_i_travel IN LOCAL MODE

         ENTITY Travel

           EXECUTE recalctotalprice

           FROM CORRESPONDING #( keys ).

     ENDMETHOD.

   *************** calculate_Total_Price at Booking Entity

    METHOD calculate_Total_Price.

       READ ENTITIES OF zrk_sde_i_travel IN LOCAL MODE

           ENTITY Booking

           BY \_Travel

           FIELDS ( TravelUUID )

            WITH CORRESPONDING #( keys )

            RESULT DATA(lt_travels).

       "update involved instances

       MODIFY ENTITIES OF zrk_sde...