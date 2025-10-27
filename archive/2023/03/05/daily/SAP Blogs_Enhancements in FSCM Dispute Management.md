---
title: Enhancements in FSCM Dispute Management
url: https://blogs.sap.com/2023/03/04/enhancements-in-fscm-dispute-management/
source: SAP Blogs
date: 2023-03-05
fetch_date: 2025-10-04T08:43:38.693168
---

# Enhancements in FSCM Dispute Management

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Supply Chain Management](/t5/supply-chain-management/ct-p/scm)
* [SCM Blog Posts by Members](/t5/supply-chain-management-blog-posts-by-members/bg-p/scm-blog-members)
* Enhancements in FSCM Dispute Management

Supply Chain Management Blog Posts by Members

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/scm-blog-members/article-id/4769&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [Enhancements in FSCM Dispute Management](/t5/supply-chain-management-blog-posts-by-members/enhancements-in-fscm-dispute-management/ba-p/13563019)

![Bohdan](https://avatars.profile.sap.com/7/3/id734646801e0751f4793baef6e38a5f65d7a31dc8216c06989ee6328558476ad9_small.jpeg "Bohdan")

[Bohdan](https://community.sap.com/t5/user/viewprofilepage/user-id/180051)

Active Contributor

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=scm-blog-members&message.id=4769)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/scm-blog-members/article-id/4769)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13563019)

‎2023 Mar 04
4:43 PM

[8
Kudos](/t5/kudos/messagepage/board-id/scm-blog-members/message-id/4769/tab/all-users "Click here to see who gave kudos to this post.")

9,016

* SAP Managed Tags
* [ABAP Development](https://community.sap.com/t5/c-khhcw49343/ABAP%2520Development/pd-p/833755570260738661924709785639136)
* [SAP Financial Supply Chain Management](https://community.sap.com/t5/c-khhcw49343/SAP%2520Financial%2520Supply%2520Chain%2520Management/pd-p/01200615320800000553)

* [SAP Financial Supply Chain Management

  SAP Financial Supply Chain Management](/t5/c-khhcw49343/SAP%2BFinancial%2BSupply%2BChain%2BManagement/pd-p/01200615320800000553)
* [ABAP Development

  Programming Tool](/t5/c-khhcw49343/ABAP%2BDevelopment/pd-p/833755570260738661924709785639136)

View products (2)

Dear SAPers,

SAP delivered a dedicated component called **Dispute Management** within FSCM module to manage the differences (i.e., *disputes*) that arise during clearing of incoming payments & customer invoices. Dispute Management uses the component **Case Management** as a technical basis to process the dispute cases. The purpose of this post is to explore the enhancement options behind the BADI **SCMG\_CHNG\_BFR\_STR\_C**. This post will focus mainly on the use of this BAdI for management of dispute cases. I’ll provide some recommendations on the architecture of the enhancements and some useful tips how to use the interface of this BAdI efficiently.

## Overview of the BAdI interface

This BAdI uses the interface IF\_EX\_SCMG\_CHNG\_BFR\_STR\_C with one method CHANGE. The screenshot below shows the method’s signature:

![](/legacyfs/online/storage/blog_attachments/2023/03/01_00_BADI_interface.jpg)

This BAdI is a generic BAdI within case management framework and it is used in many processes. However, this BAdI can be implemented only once i.e., only one active implementation can exist at a time. The interface uses an importing parameter FLT\_VAL to distinguish between various processes that call this BAdI. Typical filter values are:

* F\_DM – for dispute cases.

* FDCD – for documented credit decision.

Screenshot below shows the implementation of this BAdI:

![](/legacyfs/online/storage/blog_attachments/2023/03/01_BADI_implementation.jpg)

## High-level architecture of the BAdI implementation

If you want to use this BAdI for implementation of custom logic, I’d recommend using the implementing class for this BAdI only as a *controller*, whereas the main logic should be implemented in separate global classes. Let me clarify what I mean.

BAdI implementing class ZCL\_IM\_SCMG\_CHNG\_BFR\_ST as is shown below serves only one purpose: it checks the value of the filter and routes the execution to two other global classes: ZCL\_IM\_SCMG\_CHNG\_BFR\_ST\_DC & ZCL\_IM\_SCMG\_CHNG\_BFR\_ST\_DCD. The first class implements custom logic for dispute cases, the second one for documented credit decisions.

What are the benefits of this approach? Main benefit in my opinion is that the enhancement logic is split into separate classes. Each class follows the *single responsibility principle* and knows how to handle the objects of one type only. This architecture ensures smaller regression impact and means lower maintenance cost in the long run: if you need to adjust the logic for one component (e.g., dispute cases), you can be sure that other functionalities will not be impacted by these changes.

```
class zcl_im_scmg_chng_bfr_st definition

  public

  final

  create public .

  public section.

    interfaces if_ex_scmg_chng_bfr_str_c .

  protected section.

  private section.

endclass.

class zcl_im_scmg_chng_bfr_st implementation.

* <SIGNATURE>---------------------------------------------------------------------------------------+

* | Instance Public Method ZCL_IM_SCMG_CHNG_BFR_ST->IF_EX_SCMG_CHNG_BFR_STR_C~CHANGE

* +-------------------------------------------------------------------------------------------------+

* | [--->] IM_CASE                        TYPE REF TO IF_SCMG_CASE

* | [--->] FLT_VAL                        TYPE        SCMGPROCESS

* | [!CX!] CX_SCMG_CASE_BADI

* +--------------------------------------------------------------------------------------</SIGNATURE>

  method if_ex_scmg_chng_bfr_str_c~change.

    constants:

      begin of lc_filter,

        dispute_case      type scmgprocess value 'F_DM',

        doc_cred_decision type scmgprocess value 'FDCD',

      end of lc_filter.

    case flt_val.

      when lc_filter-dispute_case.

        zcl_im_scmg_chng_bfr_st_dc=>change_dc( im_case ).

      when lc_filter-doc_cred_decision.

        zcl_im_scmg_chng_bfr_st_dcd=>change_dcd( im_case ).

      when others.

        return.

    endcase.

  endmethod.

endclass.
```

Screenshots below show how new class for dispute cases was implemented:

![](/legacyfs/online/storage/blog_attachments/2023/03/01_dc_method_interface.jpg)

![](/legacyfs/online/storage/blog_attachments/2023/03/02_dc_method_parameters.jpg)

## Instance of the case as method parameter

If you’re a functional consultant and you analyze the interface of this BAdI for the first time, you might be confused a bit: the method has only one importing parameter IM\_CASE and normally you cannot change the parameters of this type. Besides, even if you put a breakpoint in the code and will check the variable IM\_CASE in debug mode, you’ll not find a lot of useful details. Screenshot below shows how this parameter looks like during debugging.

![](/legacyfs/online/storage/blog_attachments/2023/03/03_im_case_in_debug.jpg)

The explanation is simple: this method receives an instance of the dispute case. Each dispute case as an instance has certain ***attributes*** (i.e., values associated with it) and ***methods*** (i.e., actions you can perform in relation to the instance). Let’s see how to access these attributes and what are some useful methods you can use to get / set the values of certain attributes.

### Overview of Getter Methods

If you want to check a value of some attribute, you can use the method GET\_SINGLE\_ATTRIBUTE\_VALUE. It will retrieve the current value of the attribute e.g., who is coordinator of the dispute case. Similarly, you can use another method GET\_SINGLE\_OLD\_ATTR\_VALUE to retrieve...