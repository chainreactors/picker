---
title: Alternative to BDC for Transactions F-30 or FB05 in RAP/Fiori Apps for Posting with Clearing
url: https://blogs.sap.com/2023/01/07/alternative-to-bdc-for-transactions-f-30-or-fb05-in-rap-fiori-apps-for-posting-with-clearing/
source: SAP Blogs
date: 2023-01-08
fetch_date: 2025-10-04T03:19:07.643813
---

# Alternative to BDC for Transactions F-30 or FB05 in RAP/Fiori Apps for Posting with Clearing

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Technology](/t5/technology/ct-p/technology)
* [Technology Blog Posts by Members](/t5/technology-blog-posts-by-members/bg-p/technology-blog-members)
* Alternative to BDC for Transactions F-30 or FB05 i...

Technology Blog Posts by Members

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/technology-blog-members/article-id/162593&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [Alternative to BDC for Transactions F-30 or FB05 in RAP/Fiori Apps for Posting with Clearing](/t5/technology-blog-posts-by-members/alternative-to-bdc-for-transactions-f-30-or-fb05-in-rap-fiori-apps-for/ba-p/13564585)

![VijayCR](https://avatars.profile.sap.com/5/d/id5dec9917d1d4a6afdb1c924dc1f0d19cccdfabf28cb31d70a37ff6e8b182bcc2_small.jpeg "VijayCR")

[VijayCR](https://community.sap.com/t5/user/viewprofilepage/user-id/38084)

Active Contributor

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=technology-blog-members&message.id=162593)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/technology-blog-members/article-id/162593)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13564585)

‎2023 Jan 07
5:05 PM

[13
Kudos](/t5/kudos/messagepage/board-id/technology-blog-members/message-id/162593/tab/all-users "Click here to see who gave kudos to this post.")

13,796

* SAP Managed Tags
* [SAP BTP ABAP environment](https://community.sap.com/t5/c-khhcw49343/SAP%2520BTP%2520ABAP%2520environment/pd-p/73555000100800001164)
* [ABAP Development](https://community.sap.com/t5/c-khhcw49343/ABAP%2520Development/pd-p/833755570260738661924709785639136)
* [ABAP RESTful Application Programming Model](https://community.sap.com/t5/c-khhcw49343/ABAP%2520RESTful%2520Application%2520Programming%2520Model/pd-p/7e44126e-7b27-471d-a379-df205a12b1ff)

* [ABAP Development

  Programming Tool](/t5/c-khhcw49343/ABAP%2BDevelopment/pd-p/833755570260738661924709785639136)
* [SAP BTP ABAP environment

  SAP Business Technology Platform](/t5/c-khhcw49343/SAP%2BBTP%2BABAP%2Benvironment/pd-p/73555000100800001164)
* [ABAP RESTful Application Programming Model

  Software Product Function](/t5/c-khhcw49343/ABAP%2BRESTful%2BApplication%2BProgramming%2BModel/pd-p/7e44126e-7b27-471d-a379-df205a12b1ff)

View products (3)

Hello Experts,

Posting the documents with Clearing open items and doing the transfer postings is a very common requirements in most of the SAP implementation FICO based projects.

Clearing can done in multiple ways

* G/L posting with clearing

* Customer - Customer  Posting with clearing

* Vendor- vendor Posting with Clearing

Till today for the custom based requirements we are using either BDC on the transactions F-30 or FB05 with Transfer posting with clearing options or using the below three function modules which is detailed out in the below blog .

* POSTING\_INTERFACE\_START

* POSTING\_INTERFACE\_CLEARING

* POSTING\_INTERFACE\_END

<https://blogs.sap.com/2016/10/04/fb05-or-f-30-using-a-standard-sap-fm/>

However with the ABAP cloud and Fiori apps are coming into picture there was an alternative approach required to perform the transfer postings.

**New Approach for the Transfer postings :**

During the analysis to find a new class or function module to avoid the BDC coding and perform the above activity the below applications Upload Journal Entry app  F2548 <https://fioriappslibrary.hana.ondemand.com/sap/fix/externalViewer/#/detail/Apps('F2548')/S24OPand> the SOAP based Interface <https://api.sap.com/api/OP_JOURNALENTRYBULKCLEARINGREQUEST_IN/overview> which is posting the Journal Entries is evaluated and realized the class CL\_FDC\_ACCDOC\_POST=> ACCDOC\_POST is used in the same.

Before Moving into the technical solution let us understand what is the Transfer posting with Clearing :

Lets say customer 1  has total open items of 2000 Eur and out of that he wants to transfer 1500 to another customer and clear the original posting we can use any of the transaction FB05 or F-30 to do the same using the options

* Open Transaction F-30 provide the customer1 details to be cleared and posted

![](/legacyfs/online/storage/blog_attachments/2023/01/MicrosoftTeams-image-11.png)

F-30 Transaction

Enter the amount to be transferred from Customer 1

![](/legacyfs/online/storage/blog_attachments/2023/01/MicrosoftTeams-image-10.png)

Transfer Amount

Now click on the Process Open Items buttons and check the list of open items

![](/legacyfs/online/storage/blog_attachments/2023/01/MicrosoftTeams-image-14.png)

Now click on the Charge Off Difference to charge the remaining amounts to Customer 2 for Clearing as shown below enter amount as \*

![](/legacyfs/online/storage/blog_attachments/2023/01/MicrosoftTeams-image-13.png)

On Click of back button the posting will be seen as below with the customer line items and the amounts to be transferred,

![](/legacyfs/online/storage/blog_attachments/2023/01/MicrosoftTeams-image-101.png)

Thus you can do the postings and clear the Customer 1. When you open the Open items again for the Customer 1 1500 will be cleared.

Find the below reference code for the reference for Customer - Customer Transfer posting scenario .

* Fill the Header structure

* Fill the Item Table with the line items for the Customer 1 to be transferred

* Fill the Item table to be cleared structure with the Customer 2 number

* Simulate using the class method cl\_fdc\_accdoc\_post=>accdoc\_simulate  to check for any errors

* In case of no errors use the class cl\_fdc\_accdoc\_post=>accdoc\_post  or wrap the class inside a RFC Function module for RAP based scenarios and call the function module with Destination 'NONE' to avoid the commit dumps .

**NOTE : The below code will help to start with the postings with clearing but it might non work 1-1 in practical scenarios .**

```
*&---------------------------------------------------------------------*

*& Report Z_POST_CLEAR

*&---------------------------------------------------------------------*

*&

*&---------------------------------------------------------------------*

REPORT z_post_clear.

DATA: fdc_accdoc_tax              TYPE fdc_t_accdoc_tax,

      fdc_accdoc_whtax            TYPE fdc_t_accdoc_whtax,

      fdc_accdoc_itm_to_be_clrd   TYPE fdc_t_accdoc_itm_to_be_clrd,

      fdc_accdoc_pay_diff         TYPE fdc_t_accdoc_pay_diff,

      accdoc_itm_copa             TYPE fdc_t_accdoc_itm_copa,

      fdc_accdoc_itm              TYPE fdc_t_accdoc_itm,

      accdoc_dispute              TYPE fdc_t_accdoc_dispute,

      accdoc_one_time_account     TYPE fdc_t_accdoc_one_time_account,

      itm_payment_only            TYPE fdc_s_accdoc_with_item,

      fdc_accdoc_warning_messages TYPE fdc_t_accdoc_warning_messages,

      warning                     TYPE fdc_t_accdoc_warning_messages.

** Fill header info

DATA(headerinfo) = VALUE fdc_s_accdoc_hdr( bukrs = '0001'

                                 blart = cl_abap_context_info=>get_system_date( )

                                 budat = cl_abap_context_info=>get_system_date( )

                                 waers = 'EUR'

                                 hwaer = 'EUR' " Get the currencies from CDS View p_ldcmpcurr

                                 hwae2 = 'EUR' " Get the currencies from CDS View p_ldcmpcurr

                                 xblnr = 'Test13'

          ...