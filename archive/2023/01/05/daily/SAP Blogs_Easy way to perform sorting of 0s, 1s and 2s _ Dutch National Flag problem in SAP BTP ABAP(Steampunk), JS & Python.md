---
title: Easy way to perform sorting of 0s, 1s and 2s | Dutch National Flag problem in SAP BTP ABAP(Steampunk), JS & Python
url: https://blogs.sap.com/2023/01/04/easy-way-to-perform-sorting-of-0s-1s-and-2s-dutch-national-flag-problem-in-sap-btp-abapsteampunk-js-python/
source: SAP Blogs
date: 2023-01-05
fetch_date: 2025-10-04T03:04:04.643009
---

# Easy way to perform sorting of 0s, 1s and 2s | Dutch National Flag problem in SAP BTP ABAP(Steampunk), JS & Python

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Technology](/t5/technology/ct-p/technology)
* [Technology Blog Posts by Members](/t5/technology-blog-posts-by-members/bg-p/technology-blog-members)
* Easy way to perform sorting of 0s, 1s and 2s | Dut...

Technology Blog Posts by Members

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/technology-blog-members/article-id/162312&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [Easy way to perform sorting of 0s, 1s and 2s | Dutch National Flag problem in SAP BTP ABAP(Steampunk), JS & Python](/t5/technology-blog-posts-by-members/easy-way-to-perform-sorting-of-0s-1s-and-2s-dutch-national-flag-problem-in/ba-p/13562859)

![kallolathome](https://avatars.profile.sap.com/8/d/id8dd1f1faeeb17582fb46ef15990b58394c58a7ec855824cb21f8cc8a8a158479_small.jpeg "kallolathome")

[kallolathome](https://community.sap.com/t5/user/viewprofilepage/user-id/14879)

Active Participant

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=technology-blog-members&message.id=162312)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/technology-blog-members/article-id/162312)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13562859)

‎2023 Jan 04
6:16 PM

[2
Kudos](/t5/kudos/messagepage/board-id/technology-blog-members/message-id/162312/tab/all-users "Click here to see who gave kudos to this post.")

1,366

* SAP Managed Tags
* [SAP BTP ABAP environment](https://community.sap.com/t5/c-khhcw49343/SAP%2520BTP%2520ABAP%2520environment/pd-p/73555000100800001164)
* [SAP S/4HANA Cloud ABAP Environment](https://community.sap.com/t5/c-khhcw49343/SAP%2520S%252F4HANA%2520Cloud%2520ABAP%2520Environment/pd-p/60907aa9-99e9-4d5d-9103-8b970e9bc0a4)
* [Python](https://community.sap.com/t5/c-khhcw49343/Python/pd-p/f220d74d-56e2-487e-8e6c-a8cb3def2378)
* [ABAP Development](https://community.sap.com/t5/c-khhcw49343/ABAP%2520Development/pd-p/833755570260738661924709785639136)
* [JavaScript](https://community.sap.com/t5/c-khhcw49343/JavaScript/pd-p/506421944534752500398156104608974)
* [SAP Business Technology Platform](https://community.sap.com/t5/c-khhcw49343/SAP%2520Business%2520Technology%2520Platform/pd-p/73555000100700000172)

* [ABAP Development

  Programming Tool](/t5/c-khhcw49343/ABAP%2BDevelopment/pd-p/833755570260738661924709785639136)
* [JavaScript

  Programming Tool](/t5/c-khhcw49343/JavaScript/pd-p/506421944534752500398156104608974)
* [SAP BTP ABAP environment

  SAP Business Technology Platform](/t5/c-khhcw49343/SAP%2BBTP%2BABAP%2Benvironment/pd-p/73555000100800001164)
* [Python

  Programming Tool](/t5/c-khhcw49343/Python/pd-p/f220d74d-56e2-487e-8e6c-a8cb3def2378)
* [SAP Business Technology Platform

  Software Product](/t5/c-khhcw49343/SAP%2BBusiness%2BTechnology%2BPlatform/pd-p/73555000100700000172)
* [SAP S/4HANA Cloud ABAP Environment

  Additional Software Product](/t5/c-khhcw49343/SAP%2BS%25252F4HANA%2BCloud%2BABAP%2BEnvironment/pd-p/60907aa9-99e9-4d5d-9103-8b970e9bc0a4)

View products (6)

## Introduction

This is part of the [**Easy way to write algorithms in ABAP: Series 01**](https://blogs.sap.com/2022/12/20/easy-way-to-write-algorithms-in-abap-series-01/). For more algorithms, please check the main blog-post.

## Problem

Given an array `nums` with `n` objects colored red, white, or blue, sort them **[in-place](https://en.wikipedia.org/wiki/In-place_algorithm)**so that objects of the same color are adjacent, with the colors in the order red, white, and blue.

We will use the integers `0`, `1`, and `2` to represent the color red, white, and blue, respectively.

You must solve this problem without using the library's sort function.

**Example 1:**

```
Input: nums = [2,0,2,1,1,0]

Output: [0,0,1,1,2,2]
```

**Example 2:**

```
Input: nums = [2,0,1]

Output: [0,1,2]
```

**Constraints:**

* `n == nums.length`

* `1 <= n <= 300`

* `nums[i]` is either `0`, `1`, or `2`.

**Follow up:** Could you come up with a one-pass algorithm using only constant extra space?

## Solution

Time Complexity: O(n)

Space Complexity: O(1)

### ABAP

```
CLASS zcl_algo_dnf DEFINITION

  PUBLIC

  FINAL

  CREATE PUBLIC .

  PUBLIC SECTION.

* Mandatory declaration

    INTERFACES if_oo_adt_classrun.

  PROTECTED SECTION.

  PRIVATE SECTION.

    TYPES ty_nums TYPE STANDARD TABLE OF i WITH EMPTY KEY.

    DATA lt_nums  TYPE STANDARD TABLE OF i WITH EMPTY KEY.

    METHODS sortNumbers

      CHANGING lt_nums TYPE STANDARD TABLE.

    METHODS swapNumbers

      CHANGING lt_nums TYPE STANDARD TABLE

               lv_i    TYPE i

               lv_j    TYPE i.

ENDCLASS.

CLASS zcl_algo_dnf IMPLEMENTATION.

  METHOD if_oo_adt_classrun~main.

    DATA(lo_obj) = NEW zcl_algo_dnf( ).

*   data

    lt_nums = VALUE ty_nums( ( 2 ) ( 0 ) ( 2 ) ( 1 ) ( 1 ) ( 0 ) ).

*   calling the method

    lo_obj->sortNumbers( CHANGING lt_nums = lt_nums ).

    out->write( |after sorting:------->| ).

    out->write( lt_nums ).

    FREE lt_nums.

  ENDMETHOD.

  METHOD sortNumbers.

*   indexes

    DATA(lv_low) = 1.

    DATA(lv_mid) = 1.

    DATA(lv_high) = lines( lt_nums ).

    WHILE lv_mid <= lv_high.

      CASE lt_nums[ lv_mid ].

        WHEN 0.

          swapNumbers( CHANGING lt_nums = lt_nums

                    lv_i = lv_low

                    lv_j = lv_mid ).

          lv_low += 1.

          lv_mid += 1.

        WHEN 1.

          lv_mid += 1.

        WHEN 2.

          swapNumbers( CHANGING lt_nums = lt_nums

                      lv_i = lv_mid

                      lv_j = lv_high ).

          lv_high -= 1.

      ENDCASE.

    ENDWHILE.

    FREE: lv_low, lv_mid, lv_high.

  ENDMETHOD.

  METHOD swapNumbers.

*   local variable

    DATA(lv_temp) = 0.

*   swapping

    lv_temp = lt_nums[ lv_i ].

    lt_nums[ lv_i ] =  lt_nums[ lv_j ].

    lt_nums[ lv_j ] = lv_temp.

    FREE lv_temp.

  ENDMETHOD.

ENDCLASS.
```

### JavaScript

```
/**

 * @param {number[]} nums

 * @return {void} Do not return anything, modify nums in-place instead.

 */

var sortColors = function (nums) {

    var lv_low = 0,

        lv_mid = 0,

        lv_high = nums.length - 1;

    while (lv_mid <= lv_high) {

        switch (nums[lv_mid]) {

            case 0:

                swapNumbers(nums, lv_low, lv_mid);

                lv_low += 1;

                lv_mid += 1;

                break;

            case 1:

                lv_mid += 1;

                break;

            case 2:

                swapNumbers(nums, lv_mid, lv_high);

                lv_high -= 1;

                break;

        }

    }

};

function swapNumbers(nums, i, j) {

    var temp = 0;

        temp = nums[i];

        nums[i] = nums[j];

        nums[j] = temp;

}
```

### Python

```
class Solution:

    def sortColors(self, nums: List[int]) -> None:

        """

        Do not return anything, modify nums in -place instead.

        """

        lv_low = lv_mid = 0

        lv_high = len(nums) - 1

        while lv_mid <= lv_high:

            if nums[lv_mid] == 0:

                swapNumbers(nums, lv_low, lv_mid)

                lv_low += 1

                lv_mid += 1

            elif nums[lv_mid] == 1:

                lv_mid += 1

            else:

                swapNumbers(nums, lv_mid, lv_high)

                lv_high -= 1

def swapNumbers(nums, i, j) -> None:

    lv_temp = 0

    lv_temp = nums...