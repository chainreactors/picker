---
title: Send SAPscript form PDF from output type message to Business Network
url: https://blogs.sap.com/2023/08/18/send-sapscript-form-pdf-from-output-type-message-to-business-network/
source: SAP Blogs
date: 2023-08-19
fetch_date: 2025-10-04T11:59:42.892119
---

# Send SAPscript form PDF from output type message to Business Network

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Spend Management](/t5/spend-management/ct-p/spend-management)
* [Spend Management Blog Posts by Members](/t5/spend-management-blog-posts-by-members/bg-p/spend-management-blog-members)
* Send SAPscript form PDF from output type message t...

Spend Management Blog Posts by Members

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/spend-management-blog-members/article-id/1880&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [Send SAPscript form PDF from output type message to Business Network](/t5/spend-management-blog-posts-by-members/send-sapscript-form-pdf-from-output-type-message-to-business-network/ba-p/13579642)

![gellper](https://avatars.profile.sap.com/c/e/idce8e680f3364702f17df575649f3aab802fc3858da584bcaf390a5440f4e1857_small.jpeg "gellper")

[gellper](https://community.sap.com/t5/user/viewprofilepage/user-id/150771)

Participant

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=spend-management-blog-members&message.id=1880)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/spend-management-blog-members/article-id/1880)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13579642)

‎2023 Aug 18
10:13 PM

[7
Kudos](/t5/kudos/messagepage/board-id/spend-management-blog-members/message-id/1880/tab/all-users "Click here to see who gave kudos to this post.")

4,847

* SAP Managed Tags
* [SAP Integration Suite, managed gateway](https://community.sap.com/t5/c-khhcw49343/SAP%2520Integration%2520Suite%252C%2520managed%2520gateway/pd-p/73554900100800000194)
* [SAP Integration Suite, managed gateway for spend management and SAP Business Network](https://community.sap.com/t5/c-khhcw49343/SAP%2520Integration%2520Suite%252C%2520managed%2520gateway%2520for%2520spend%2520management%2520and%2520SAP%2520Business%2520Network/pd-p/73554900100800000872)
* [SAP Ariba solution integration for SAP Business Suite](https://community.sap.com/t5/c-khhcw49343/SAP%2520Ariba%2520solution%2520integration%2520for%2520SAP%2520Business%2520Suite/pd-p/67838200100800006082)
* [SAP Business Network for Procurement and SAP Business Network for Supply Chain](https://community.sap.com/t5/c-khhcw49343/SAP%2520Business%2520Network%2520for%2520Procurement%2520and%2520SAP%2520Business%2520Network%2520for%2520Supply%2520Chain/pd-p/67838200100800005701)

* [SAP Integration Suite, managed gateway

  SAP Integration Suite](/t5/c-khhcw49343/SAP%2BIntegration%2BSuite%25252C%2Bmanaged%2Bgateway/pd-p/73554900100800000194)
* [SAP Ariba solution integration for SAP Business Suite

  SAP Business Network for Procurement and SAP Business Network for Supply Chain](/t5/c-khhcw49343/SAP%2BAriba%2Bsolution%2Bintegration%2Bfor%2BSAP%2BBusiness%2BSuite/pd-p/67838200100800006082)
* [SAP Integration Suite, managed gateway for spend management and SAP Business Network

  SAP Integration Suite](/t5/c-khhcw49343/SAP%2BIntegration%2BSuite%25252C%2Bmanaged%2Bgateway%2Bfor%2Bspend%2Bmanagement%2Band%2BSAP%2BBusiness%2BNetwork/pd-p/73554900100800000872)
* [SAP Business Network for Procurement and SAP Business Network for Supply Chain

  SAP Business Network for Procurement and SAP Business Network for Supply Chain](/t5/c-khhcw49343/SAP%2BBusiness%2BNetwork%2Bfor%2BProcurement%2Band%2BSAP%2BBusiness%2BNetwork%2Bfor%2BSupply%2BChain/pd-p/67838200100800005701)

View products (4)

One of the common requirements when we are implementing SAP Ariba Commerce Automation or Digital Supplier Network, is to send attachments inside the purchase order to Ariba Business Network, but this functionality is already included implementing the next Include in the User Exit EXIT\_SAPLEINM\_002:
> ```
>  INCLUDE ARBCIG_ORDER_REQUEST_002 IF FOUND.
> ```

But...what happens when you want to send the PDF of the purchase order, and this PDF is generated in a SAPScript form, that is executed inside the output type message:

![](/legacyfs/online/storage/blog_attachments/2023/08/print1.jpg)

Message Output

This Output type is configured in NACE transaction where you enter the form name of the SAPScript that will be triggered:

![](/legacyfs/online/storage/blog_attachments/2023/08/print2.jpg)

NACE Output Type

The complication of this functionality is that this printout of the purchase order, is triggered when the output message is already processed and the purchase order is already approved, but when you are sending the purchase order to Ariba Business Network, this steps are not finished yet, so you must implement a logic to print the PDF of the purchase order, executing manually the SAPScript in real time when the PO is sent to Business Network.

We can do that implementing the BADI ARBCIG\_BADI\_ATTACHMENT\_UTIL where we process the attachments of the PO.

![](/legacyfs/online/storage/blog_attachments/2023/08/print3.jpg)

BADI ARBCIG\_BADI\_ATTACHMENT\_UTIL

We only need the method PRE\_ATTACHMENT\_PROCESS:

![](/legacyfs/online/storage/blog_attachments/2023/08/print4.jpg)

METHOD PRE\_ATTACHMENT\_PROCESS

Inside this method, we will implement the next logic:

1. Search in NAST table with the PO ID if exists the message you are configured in NACE transaction for the purchase order you are approving.

2. Read the data of the PO from MF ME\_READ\_PO\_FOR\_PRINTING.

3. Execute the MF ECP\_PRINT\_PO with the form ID.

4. Read the OTF data of the form with MF READ\_OTF\_FROM\_MEMORY.

5. Convert OTF data to PDF with MF CONVERT\_OTF.

6. Encrypt the PDF from Hexadecimal to Base64 with MF SCMS\_BASE64\_ENCODE\_STR.

7. Complete the E1ARBCIG\_ATTACH\_HDR\_DET segment with header data of attachment.

8. Complete the E1ARBCIG\_ATTACH\_CONTENT\_DET segment with the content of Base64 string.

All this steps are detailed in the next code:
> ```
>   method IF_ARBCIG_ATTACHMENT_UTIL~PRE_ATTACHMENT_PROCESS.
>
>
>
>
>
>     DATA: gint_nast      TYPE nast,
>
>           lv_count       TYPE i,
>
>           lv_ebeln       TYPE ebeln,
>
>           ent_screen     TYPE c,
>
>           ent_retco      TYPE i,
>
>           l_nast         TYPE nast,
>
>           l_druvo        TYPE t166k-druvo,
>
>           l_from_memory,
>
>           toa_dara       TYPE toa_dara,
>
>           arc_params     TYPE arc_params,
>
>           aux_form       TYPE tnapr-fonam VALUE 'ZMMSS_PEDCOMPRAS',
>
>           lv_message     TYPE tnapr-fonam VALUE 'ZPC',
>
>           lt_docs        TYPE TABLE OF docs,
>
>           l_doc          TYPE meein_purchase_doc_print,
>
>           otf            TYPE TABLE OF itcoo,
>
>           pdf_bytecount  TYPE i,
>
>           nom_archivo    TYPE string,
>
>           pdfout         TYPE TABLE OF tline,
>
>           lv_debug       TYPE char1,
>
>           pdf            TYPE XSTRING,
>
>           ls_e1edk01     TYPE e1edk01,
>
>           ls_hdr_det     TYPE E1ARBCIG_ATTACH_HDR_DET,
>
>           ls_hdr_content TYPE E1ARBCIG_ATTACH_CONTENT_DET,
>
>           idoc_data      TYPE edidd,
>
>           lv_base64      TYPE string,
>
>           len            TYPE i,
>
>           lv_offset_mx   TYPE i,
>
>           lv_offset_mn   TYPE i,
>
>           div            TYPE i,
>
>           temp           TYPE i.
>
>
>
> *"---------------------------------------------------------------------
>
> *" NOTES:
>
> *"  1) Control display of PO in GUI window
>
> *"       ENT_SCREEN = 'X'   => PO is displayed in GUI window
>
> *"...