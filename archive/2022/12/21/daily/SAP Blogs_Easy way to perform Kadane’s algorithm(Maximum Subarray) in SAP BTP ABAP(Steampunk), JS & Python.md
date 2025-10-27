---
title: Easy way to perform Kadane’s algorithm(Maximum Subarray) in SAP BTP ABAP(Steampunk), JS & Python
url: https://blogs.sap.com/2022/12/20/easy-way-to-perform-kadanes-algorithmmaximum-subarray-in-sap-btp-abapsteampunk-js-python/
source: SAP Blogs
date: 2022-12-21
fetch_date: 2025-10-04T02:04:45.035761
---

# Easy way to perform Kadane’s algorithm(Maximum Subarray) in SAP BTP ABAP(Steampunk), JS & Python

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Enterprise Resource Planning](/t5/enterprise-resource-planning/ct-p/erp)
* [ERP Blog Posts by Members](/t5/enterprise-resource-planning-blog-posts-by-members/bg-p/erp-blog-members)
* Easy way to perform Kadane's algorithm(Maximum Sub...

Enterprise Resource Planning Blog Posts by Members

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/erp-blog-members/article-id/66907&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [Easy way to perform Kadane's algorithm(Maximum Subarray) in SAP BTP ABAP(Steampunk), JS & Python](/t5/enterprise-resource-planning-blog-posts-by-members/easy-way-to-perform-kadane-s-algorithm-maximum-subarray-in-sap-btp-abap/ba-p/13548546)

![kallolathome](https://avatars.profile.sap.com/8/d/id8dd1f1faeeb17582fb46ef15990b58394c58a7ec855824cb21f8cc8a8a158479_small.jpeg "kallolathome")

[kallolathome](https://community.sap.com/t5/user/viewprofilepage/user-id/14879)

Active Participant

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=erp-blog-members&message.id=66907)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/erp-blog-members/article-id/66907)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13548546)

‎2022 Dec 20
6:35 PM

[8
Kudos](/t5/kudos/messagepage/board-id/erp-blog-members/message-id/66907/tab/all-users "Click here to see who gave kudos to this post.")

3,799

* SAP Managed Tags
* [SAP BTP ABAP environment](https://community.sap.com/t5/c-khhcw49343/SAP%2520BTP%2520ABAP%2520environment/pd-p/73555000100800001164)
* [SAP S/4HANA Cloud ABAP Environment](https://community.sap.com/t5/c-khhcw49343/SAP%2520S%252F4HANA%2520Cloud%2520ABAP%2520Environment/pd-p/60907aa9-99e9-4d5d-9103-8b970e9bc0a4)
* [Python](https://community.sap.com/t5/c-khhcw49343/Python/pd-p/f220d74d-56e2-487e-8e6c-a8cb3def2378)
* [ABAP Development](https://community.sap.com/t5/c-khhcw49343/ABAP%2520Development/pd-p/833755570260738661924709785639136)
* [JavaScript](https://community.sap.com/t5/c-khhcw49343/JavaScript/pd-p/506421944534752500398156104608974)

* [ABAP Development

  Programming Tool](/t5/c-khhcw49343/ABAP%2BDevelopment/pd-p/833755570260738661924709785639136)
* [JavaScript

  Programming Tool](/t5/c-khhcw49343/JavaScript/pd-p/506421944534752500398156104608974)
* [SAP BTP ABAP environment

  SAP Business Technology Platform](/t5/c-khhcw49343/SAP%2BBTP%2BABAP%2Benvironment/pd-p/73555000100800001164)
* [Python

  Programming Tool](/t5/c-khhcw49343/Python/pd-p/f220d74d-56e2-487e-8e6c-a8cb3def2378)
* [SAP S/4HANA Cloud ABAP Environment

  Additional Software Product](/t5/c-khhcw49343/SAP%2BS%25252F4HANA%2BCloud%2BABAP%2BEnvironment/pd-p/60907aa9-99e9-4d5d-9103-8b970e9bc0a4)

View products (5)

## Introduction

This is part of the [**Easy way to write algorithms in ABAP: Series 01**](https://blogs.sap.com/2022/12/20/easy-way-to-write-algorithms-in-abap-series-01/). For more algorithms, please check the main blog-post.

## Problem

Given an integer array **`nums`**, find the subarray which has the **`largest sum and return its sum`**.

**Example 1:**

```
Input: nums = [-2,1,-3,4,-1,2,1,-5,4]

Output: 6

Explanation: [4,-1,2,1] has the largest sum = 6.
```

**Example 2:**

```
Input: nums = [1]

Output: 1
```

**Example 3:**

```
Input: nums = [5,4,-1,7,8]

Output: 23
```

**Constraints:**

* `1 <= nums.length <= 105`

* `-104 <= nums[i] <= 104`

## Solution

Time Complexity: O(n)

Space Complexity: O(1)

### ABAP

```
CLASS zcl_algo_kadane DEFINITION

  PUBLIC

  FINAL

  CREATE PUBLIC .

  PUBLIC SECTION.

* Mandatory declaration

    INTERFACES if_oo_adt_classrun.

  PROTECTED SECTION.

  PRIVATE SECTION.

    TYPES ty_nums TYPE STANDARD TABLE OF i WITH EMPTY KEY.

    METHODS kadaneAlgorithm

      IMPORTING lt_nums       TYPE STANDARD TABLE

      RETURNING VALUE(rv_msf) TYPE i.

ENDCLASS.

CLASS zcl_algo_kadane IMPLEMENTATION.

  METHOD if_oo_adt_classrun~main.

    out->write( |{ kadaneAlgorithm( VALUE ty_nums( ( 5 ) ( 4 ) ( -1 ) ( 7 ) ( 8 ) ) ) }| ).

  ENDMETHOD.

  METHOD kadaneAlgorithm.

* local variables

    DATA : lv_meh   TYPE i VALUE 0, "max ending here

           lv_temp  TYPE i VALUE 0, "sum

           lv_start TYPE i VALUE 0, "start

           lv_end   TYPE i VALUE 0. "end

    rv_msf = VALUE #( lt_nums[ 1 ] OPTIONAL ).

    LOOP AT lt_nums ASSIGNING FIELD-SYMBOL(<lf_wa>).

      lv_meh += <lf_wa>.

      IF ( rv_msf < lv_meh ).

        rv_msf = lv_meh.

        lv_start = lv_temp.

        lv_end = ( sy-tabix -  1 ).

      ENDIF.

      IF ( lv_meh < 0 ).

        lv_meh = 0.

        lv_temp = sy-tabix.

      ENDIF.

    ENDLOOP.

    UNASSIGN <lf_wa>.

    FREE : lv_meh, lv_temp, lv_start, lv_end.

  ENDMETHOD.

ENDCLASS.
```

### JavaScript

```
/**

 * @param {number[]} nums

 * @return {number}

 */

var maxSubArray = function (nums) {

    /** lv_msf should start at -Infinity (or at the value of the first item of the array),

     * otherwise an array containing all negative numbers won't give a proper result */

    var lv_msf = -Infinity,

        lv_meh = 0,

        lv_start = 0,

        lv_end = 0,

        lv_temp = 0;

    for (let i = 0; i < nums.length; i++) {

        lv_meh += nums[i];

        if (lv_msf < lv_meh) {

            lv_msf = lv_meh;

            lv_start = lv_temp;

            lv_end = i;

        }

        if (lv_meh < 0) {

            lv_meh = 0;

            lv_temp = i + 1;

        }

    }

    return lv_msf;

};
```

### Python

```
class Solution:

    def maxSubArray(self, nums: List[int]) -> int:

        # local variables

        lv_msf = nums[0]

        lv_meh = 0

        lv_start = 0

        lv_end = 0

        lv_temp = 0

        # running the loop

        for i in range(0, len(nums)):

            lv_meh += nums[i]

            if (lv_msf < lv_meh):

                lv_msf = lv_meh

                lv_start = lv_temp

                lv_end = i

            if(lv_meh < 0):

                lv_meh = 0

                lv_temp = i + 1

        return lv_msf
```

N.B: For ABAP, I am using SAP BTP ABAP Environment 2211 Release.

Happy Coding! ![:slightly_smiling_face:](/html/@CB4E4CB9DC3C08A3AD56D3C681CE34D1/emoticons/1f642.png ":slightly_smiling_face:")

* [algorithms](/t5/tag/algorithms/tg-p/board-id/erp-blog-members)
* [JavaScript](/t5/tag/JavaScript/tg-p/board-id/erp-blog-members)
* [kadane](/t5/tag/kadane/tg-p/board-id/erp-blog-members)
* [maxsubarray](/t5/tag/maxsubarray/tg-p/board-id/erp-blog-members)
* [Python](/t5/tag/Python/tg-p/board-id/erp-blog-members)
* [Steampunk](/t5/tag/Steampunk/tg-p/board-id/erp-blog-members)

7 Comments

You must be a registered user to add a comment. If you've already registered, sign in. Otherwise, register and sign in.

* [Comment](/plugins/common/feature/oidcss/sso_login_redirect/providerid/sap_ids_prompt?redirectreason=permissiondenied&referer=https%3A%2F%2Fcommunity.sap.com%2Ft5%2Fenterprise-resource-planning-blog-posts-by-members%2Feasy-way-to-perform-kadane-s-algorithm-maximum-subarray-in-sap-btp-abap%2Fba-p%2F13548546%23comment-on-this)

Copy Link
![](https://community.sap.com/html/@EE5D5986E9F4E5657DCEACB7532B5C39/assets/bluesky-dark.svg)Bluesky
Linkedin

Related Content

* [Create subarray in SAP HANA Calculation View](/t5/enterprise-resource-planning-q-a/create-subarray-in-sap-hana-calculation-view/qaq-p/11...