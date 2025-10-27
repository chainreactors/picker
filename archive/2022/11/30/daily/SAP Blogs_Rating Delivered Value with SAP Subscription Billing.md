---
title: Rating Delivered Value with SAP Subscription Billing
url: https://blogs.sap.com/2022/11/29/rating-delivered-value-with-sap-subscription-billing/
source: SAP Blogs
date: 2022-11-30
fetch_date: 2025-10-04T00:04:27.417824
---

# Rating Delivered Value with SAP Subscription Billing

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Financial Management](/t5/financial-management/ct-p/financial-management)
* [Financial Management Blog Posts by SAP](/t5/financial-management-blog-posts-by-sap/bg-p/financial-management-blog-sap)
* Rating Delivered Value with SAP Subscription Billi...

Financial Management Blog Posts by SAP

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/financial-management-blog-sap/article-id/7947&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [Rating Delivered Value with SAP Subscription Billing](/t5/financial-management-blog-posts-by-sap/rating-delivered-value-with-sap-subscription-billing/ba-p/13560281)

![svenjamschnabel](https://avatars.profile.sap.com/f/0/idf09de47dd09e3d22a030e712b0cca026f880b7e4570f40cadc0ae023627b3fb0_small.jpeg "svenjamschnabel")

![Product and Topic Expert](/html/@138D6F765B60D7FC0168643DE27D8A68/rank_icons/sap-logo-small-14px.png "Product and Topic Expert")
[svenjamschnabel](https://community.sap.com/t5/user/viewprofilepage/user-id/44558)

Product and Topic Expert

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=financial-management-blog-sap&message.id=7947)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/financial-management-blog-sap/article-id/7947)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13560281)

‎2022 Nov 29
8:58 PM

[10
Kudos](/t5/kudos/messagepage/board-id/financial-management-blog-sap/message-id/7947/tab/all-users "Click here to see who gave kudos to this post.")

2,151

* SAP Managed Tags
* [SAP Subscription Billing](https://community.sap.com/t5/c-khhcw49343/SAP%2520Subscription%2520Billing/pd-p/73555000100800000472)

* [SAP Subscription Billing

  SAP Billing and Revenue Innovation Management](/t5/c-khhcw49343/SAP%2BSubscription%2BBilling/pd-p/73555000100800000472)

View products (1)

## Introduction

For usage-based business scenarios, the ability to charge your customers based on actual product and service consumption and delivered value rather than fixed numbers and cycles is key. In the end, your customers prefer to pay for what they get rather than sticking to an unchangeable, scheduled charge that is unassociated to what they actually consumed. And ultimately, you want your customers to be happy.

SAP Subscription Billing now offers you a feature that allows you to do exactly this: Rate usage records individually irrespective of the billing cycle of a subscription and thus rate actual consumption when it occurs. Moreover, you can now create complex usage records with items and item fields to reflect additional, price-relevant information. For each item of a usage record, a separate charge is then calculated and reflected on the resulting bill.

Let’s take a closer look at an example to see what this new feature is all about.

## Example Use Case: Charging an Electric Vehicle

To make this example as simple and easy to understand as possible, we are going to focus on usage-based charges and rate elements only, although you can of course combine different types of charges in your own pricing configurations.

We are going to go more or less step by step through the different apps in SAP Subscription Billing and the Price Calculation service for SAP Subscription Billing to see what is essential in setting up a pricing model with individual usage rating. We will first look at the field catalog, price element specifications, and pricing schemes in Price Calculation before jumping to SAP Subscription Billing. There, we will go through two configuration settings in Business Configuration, create a rate plan template, a product, and a subscription to then eventually configure a usage record with items and see the resulting bill.

For our example use case, an energy provider wants to offer a subscription model with individual usage rating for charging electric vehicles at public charging stations. When using a charging station, customers are then immediately charged based on the energy they consumed, the type of power connector they used, and the time the vehicle is parked at the charging point.

For this scenario, the provider has to charge usage records with two items:

+ Item 1 reflects the ID of the charge point operator, the energy consumed during the charging process, as well as the type of power connector used.
+ Item 2 reflects the time the electric vehicle is parked at the charging station.

![](/legacyfs/online/storage/blog_attachments/2022/11/ev_scenario.png)

### Defining a Pricing Model Using the Price Calculation Service for SAP Subscription Billing

In the **Manage Field Catalog** app in the user interface of Price Calculation, the provider creates the fields following in the table below. These fields are then later used to define lookup tables and input properties for the price element specifications.

|  |  |  |  |
| --- | --- | --- | --- |
| **Code** | **Description** | **Field Type** | **Source** |
| EV\_ChargedEnergy | Total amount of energy charged during a charging period, defined in kWh (KWH) | Quantity | External |
| EV\_PowerType | Type of connector Values: AC, DC | String | External |
| EV\_PartyId | Abstract ID of the charge point operator  Values: own, other | String | External |
| EV\_ParkingTime | Total parking time, defined in hours (H) | Quantity | External |

The provider then configures the rules for generating two price elements in the **Manage Price Element Specifications** app: One price element for consumed energy in relation to the power connector used and the operator of the charge point (*EV\_Energy*), and one price element for the parking fees for the time the vehicle was parked at the charge point (*EV\_Parking*).

![](/legacyfs/online/storage/blog_attachments/2022/11/ev_energy_price_element_specification.png)

Price element specification for EV\_Energy in Manage Price Element Specifications app

![](/legacyfs/online/storage/blog_attachments/2022/11/ev_parking_price_element_specification.png)

Price element specification for EV\_Parking in Manage Price Element Specifications app

In the price element specifications *EV\_Charging* and *EV\_Parking above*, you can see the pricing trees showing the steps performed to calculate the price elements as well as the input and output fields of the referenced lookup tables.

In the **Manage Pricing Schemes** app, the provider then creates a pricing scheme *EV\_Charging Session* which calculates the charges of the two price elements:

+ A charging fee for the consumed energy
+ A parking fee for the parking time

![](/legacyfs/online/storage/blog_attachments/2022/11/ev_pricing_scheme-1.png)

Pricing scheme EV\_Charging in the Manage Pricing Schemes app

Pricing schemes define the different price elements and their relationship in order to calculate charges and specify the procedure and sequence in which pricing is executed.

Once all this has been set up in Price Calculation, the provider can continue with the setup in the user interface of SAP Subscription Billing.

### Configuring Individual Usage Rating in SAP Subscription Billing

To enable individual rating of usage records, the provider performs several steps in SAP Subscription Billing.

In the **Business Configuration** app, the provider selects the pricing scheme created before and maps the fields created in Price Calculation to usage record items in ...