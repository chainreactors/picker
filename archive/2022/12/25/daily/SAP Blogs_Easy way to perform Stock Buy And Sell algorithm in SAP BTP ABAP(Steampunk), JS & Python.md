---
title: Easy way to perform Stock Buy And Sell algorithm in SAP BTP ABAP(Steampunk), JS & Python
url: https://blogs.sap.com/2022/12/24/easy-way-to-perform-stock-buy-and-sell-algorithm-in-sap-btp-abapsteampunk-js-python/
source: SAP Blogs
date: 2022-12-25
fetch_date: 2025-10-04T02:29:27.039904
---

# Easy way to perform Stock Buy And Sell algorithm in SAP BTP ABAP(Steampunk), JS & Python

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Enterprise Resource Planning](/t5/enterprise-resource-planning/ct-p/erp)
* [ERP Blog Posts by Members](/t5/enterprise-resource-planning-blog-posts-by-members/bg-p/erp-blog-members)
* Easy way to perform Stock Buy And Sell algorithm i...

Enterprise Resource Planning Blog Posts by Members

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/erp-blog-members/article-id/67666&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [Easy way to perform Stock Buy And Sell algorithm in SAP BTP ABAP(Steampunk), JS & Python](/t5/enterprise-resource-planning-blog-posts-by-members/easy-way-to-perform-stock-buy-and-sell-algorithm-in-sap-btp-abap-steampunk/ba-p/13558368)

![kallolathome](https://avatars.profile.sap.com/8/d/id8dd1f1faeeb17582fb46ef15990b58394c58a7ec855824cb21f8cc8a8a158479_small.jpeg "kallolathome")

[kallolathome](https://community.sap.com/t5/user/viewprofilepage/user-id/14879)

Active Participant

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=erp-blog-members&message.id=67666)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/erp-blog-members/article-id/67666)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13558368)

‎2022 Dec 24
1:40 PM

[3
Kudos](/t5/kudos/messagepage/board-id/erp-blog-members/message-id/67666/tab/all-users "Click here to see who gave kudos to this post.")

2,078

* SAP Managed Tags
* [SAP BTP ABAP environment](https://community.sap.com/t5/c-khhcw49343/SAP%2520BTP%2520ABAP%2520environment/pd-p/73555000100800001164)
* [SAP S/4HANA Cloud ABAP Environment](https://community.sap.com/t5/c-khhcw49343/SAP%2520S%252F4HANA%2520Cloud%2520ABAP%2520Environment/pd-p/60907aa9-99e9-4d5d-9103-8b970e9bc0a4)
* [ABAP Development](https://community.sap.com/t5/c-khhcw49343/ABAP%2520Development/pd-p/833755570260738661924709785639136)
* [JavaScript](https://community.sap.com/t5/c-khhcw49343/JavaScript/pd-p/506421944534752500398156104608974)

* [ABAP Development

  Programming Tool](/t5/c-khhcw49343/ABAP%2BDevelopment/pd-p/833755570260738661924709785639136)
* [JavaScript

  Programming Tool](/t5/c-khhcw49343/JavaScript/pd-p/506421944534752500398156104608974)
* [SAP BTP ABAP environment

  SAP Business Technology Platform](/t5/c-khhcw49343/SAP%2BBTP%2BABAP%2Benvironment/pd-p/73555000100800001164)
* [SAP S/4HANA Cloud ABAP Environment

  Additional Software Product](/t5/c-khhcw49343/SAP%2BS%25252F4HANA%2BCloud%2BABAP%2BEnvironment/pd-p/60907aa9-99e9-4d5d-9103-8b970e9bc0a4)

View products (4)

## Introduction

This is part of the [**Easy way to write algorithms in ABAP: Series 01**](https://blogs.sap.com/2022/12/20/easy-way-to-write-algorithms-in-abap-series-01/). For more algorithms, please check the main blog-post.

## Problem

You are given an array **`prices`** where **`prices[i]`** is the price of a given stock on the **`ith`** day.

You want to maximize your profit by choosing a **single day** to buy one stock and choosing a **different day in the future** to sell that stock.

Return *the maximum profit you can achieve from this transaction*. If you cannot achieve any profit, return **`0`**.

**Example 1:**

```
Input: prices = [7,1,5,3,6,4]

Output: 5

Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.

Note that buying on day 2 and selling on day 1 is not allowed because you must buy

before you sell.
```

**Example 2:**

```
Input: prices = [7,6,4,3,1]

Output: 0

Explanation: In this case, no transactions are done and the max profit = 0.
```

**Constraints:**

* `1 <= prices.length <= 105`

* `0 <= prices[i] <= 104`

## Solution

Time Complexity: O(n)

Space Complexity: O(1)

### ABAP

```
CLASS zcl_stock DEFINITION

  PUBLIC

  FINAL

  CREATE PUBLIC .

  PUBLIC SECTION.

* Mandatory declaration

    INTERFACES if_oo_adt_classrun.

  PROTECTED SECTION.

  PRIVATE SECTION.

    TYPES ty_prices TYPE STANDARD TABLE OF i WITH DEFAULT KEY.

    METHODS StockBuySell

      IMPORTING lt_prices            TYPE ty_prices

      RETURNING VALUE(rv_max_profit) TYPE i.

ENDCLASS.

CLASS zcl_stock IMPLEMENTATION.

  METHOD if_oo_adt_classrun~main.

    out->write( |{ StockBuySell( VALUE #( ( 7 ) ( 1 ) ( 5 ) ( 3 ) ( 6 ) ( 4 ) ) ) }| ).

  ENDMETHOD.

  METHOD StockBuySell.

    DATA(lv_min_price) = lt_prices[ 1 ].

    LOOP AT lt_prices ASSIGNING FIELD-SYMBOL(<lfs_wa>).

      lv_min_price = nmin( val1 = lv_min_price

                           val2 = <lfs_wa> ).

      rv_max_profit = nmax( val1 = rv_max_profit

                            val2 = ( <lfs_wa> - lv_min_price ) ).

    ENDLOOP.

    UNASSIGN <lfs_wa>.

    FREE lv_min_price.

  ENDMETHOD.

ENDCLASS.
```

### JavaScript

```
var maxProfit = function(prices) {

    var lv_min_price = prices[0],

        lv_max_profit = 0;

    for(let i = 0; i < prices.length; i++){

        lv_min_price = Math.min(lv_min_price, prices[i]);

        lv_max_profit = Math.max(lv_max_profit, (prices[i] - lv_min_price));

    }

    return lv_max_profit;

};
```

### Python

```
class Solution:

    def maxProfit(self, prices: List[int]) -> int:

        lv_min_price = prices[0]

        lv_max_profit = 0

        for i in range(0, len(prices)):

            lv_min_price = min(lv_min_price, prices[i])

            lv_max_profit = max(lv_max_profit, (prices[i] - lv_min_price))

        return lv_max_profit
```

N.B: For ABAP, I am using SAP BTP ABAP Environment 2211 Release.

Happy Coding! ![:slightly_smiling_face:](/html/@AB1AFF728742E596A69993DB64EECECF/emoticons/1f642.png ":slightly_smiling_face:")

* [algorithms](/t5/tag/algorithms/tg-p/board-id/erp-blog-members)
* [JavaScript](/t5/tag/JavaScript/tg-p/board-id/erp-blog-members)
* [Python](/t5/tag/Python/tg-p/board-id/erp-blog-members)
* [Steampunk](/t5/tag/Steampunk/tg-p/board-id/erp-blog-members)

1 Comment

You must be a registered user to add a comment. If you've already registered, sign in. Otherwise, register and sign in.

* [Comment](/plugins/common/feature/oidcss/sso_login_redirect/providerid/sap_ids_prompt?redirectreason=permissiondenied&referer=https%3A%2F%2Fcommunity.sap.com%2Ft5%2Fenterprise-resource-planning-blog-posts-by-members%2Feasy-way-to-perform-stock-buy-and-sell-algorithm-in-sap-btp-abap-steampunk%2Fba-p%2F13558368%23comment-on-this)

Copy Link
![](https://community.sap.com/html/@EE5D5986E9F4E5657DCEACB7532B5C39/assets/bluesky-dark.svg)Bluesky
Linkedin

Related Content

* [New Custom Heuristic for Campaign Planning in PP/DS based on Order Quantity Thresholds](/t5/enterprise-resource-planning-blog-posts-by-sap/new-custom-heuristic-for-campaign-planning-in-pp-ds-based-on-order-quantity/ba-p/14139421)
  in [Enterprise Resource Planning Blog Posts by SAP](/t5/enterprise-resource-planning-blog-posts-by-sap/bg-p/erp-blog-sap)  2025 Jul 01
* [Asset Management in SAP S/4HANA Cloud Private Edition | 2023 FPS02 Release](/t5/enterprise-resource-planning-blog-posts-by-sap/asset-management-in-sap-s-4hana-cloud-private-edition-2023-fps02-release/ba-p/13894290)
  in [Enterprise Resource Planning Blog Posts by SAP](/t5/enterprise-resource-planning-blog-posts-by-sap/bg-p/erp-blog-sap)  2024 Dec 03
* [SAP S/4HANA Cloud Private Edition | 2023 FPS02 Release – Part 1](/t5/enterprise-resource-planning-blog-posts-by-sap/sap-s-4hana-cloud-private-edition-2023-fps02-release-part-1/ba-p/13875865)
  in [Enterpris...