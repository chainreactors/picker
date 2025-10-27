---
title: [BRF+ New Output Management]: Use DDIC Interface based Regular Custom Adobe Form – Handle ‘Spool request could not be found APOC_OR_MESSAGES 145’
url: https://blogs.sap.com/2023/03/10/brf-new-output-management-use-ddic-interface-based-regular-custom-adobe-form-handle-spool-request-could-not-be-found-apoc_or_messages-145/
source: SAP Blogs
date: 2023-03-11
fetch_date: 2025-10-04T09:15:49.773509
---

# [BRF+ New Output Management]: Use DDIC Interface based Regular Custom Adobe Form – Handle ‘Spool request could not be found APOC_OR_MESSAGES 145’

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Supply Chain Management](/t5/supply-chain-management/ct-p/scm)
* [SCM Blog Posts by SAP](/t5/supply-chain-management-blog-posts-by-sap/bg-p/scm-blog-sap)
* [BRF+ New Output Management]: Use DDIC Interface b...

Supply Chain Management Blog Posts by SAP

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/scm-blog-sap/article-id/5103&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [[BRF+ New Output Management]: Use DDIC Interface based Regular Custom Adobe Form – Handle ‘Spool request could not be found APOC\_OR\_MESSAGES 145’](/t5/supply-chain-management-blog-posts-by-sap/brf-new-output-management-use-ddic-interface-based-regular-custom-adobe/ba-p/13568423)

![robinthakral](https://avatars.profile.sap.com/3/6/id3654955412c011d53783b63324229824495876fc2d595e22e94298d69a18ea3d_small.jpeg "robinthakral")

[robinthakral](https://community.sap.com/t5/user/viewprofilepage/user-id/801057)

Participant

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=scm-blog-sap&message.id=5103)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/scm-blog-sap/article-id/5103)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13568423)

‎2023 Mar 10
9:34 PM

0
Kudos

9,113

* SAP Managed Tags
* [ABAP Development](https://community.sap.com/t5/c-khhcw49343/ABAP%2520Development/pd-p/833755570260738661924709785639136)
* [SAP Forms service by Adobe](https://community.sap.com/t5/c-khhcw49343/SAP%2520Forms%2520service%2520by%2520Adobe/pd-p/73555000100800000066)
* [SAP Invoice and Goods Receipt Reconciliation](https://community.sap.com/t5/c-khhcw49343/SAP%2520Invoice%2520and%2520Goods%2520Receipt%2520Reconciliation/pd-p/67837800100800005970)
* [EWM - Goods Movement](https://community.sap.com/t5/c-khhcw49343/EWM%2520-%2520Goods%2520Movement/pd-p/866234868597946653151414257432264)
* [NW ABAP Business Rule Framework (BRFplus)](https://community.sap.com/t5/c-khhcw49343/NW%2520ABAP%2520Business%2520Rule%2520Framework%2520%28BRFplus%29/pd-p/133205901943786179366163043997549)

* [ABAP Development

  Programming Tool](/t5/c-khhcw49343/ABAP%2BDevelopment/pd-p/833755570260738661924709785639136)
* [SAP Forms service by Adobe

  SAP Business Technology Platform](/t5/c-khhcw49343/SAP%2BForms%2Bservice%2Bby%2BAdobe/pd-p/73555000100800000066)
* [SAP Invoice and Goods Receipt Reconciliation

  SAP Invoice and Goods Receipt Reconciliation](/t5/c-khhcw49343/SAP%2BInvoice%2Band%2BGoods%2BReceipt%2BReconciliation/pd-p/67837800100800005970)
* [EWM - Goods Movement

  Software Product Function](/t5/c-khhcw49343/EWM%2B-%2BGoods%2BMovement/pd-p/866234868597946653151414257432264)
* [NW ABAP Business Rule Framework (BRFplus)

  Software Product Function](/t5/c-khhcw49343/NW%2BABAP%2BBusiness%2BRule%2BFramework%2B%252528BRFplus%252529/pd-p/133205901943786179366163043997549)

View products (5)

## **INTRODUCTION****:**

For the last few weeks, I have been working on a requirement that required a custom Adobe form for a standard **GR label** through NACE but later, we had to opt for new BRF+ O/P management. The ideal approach is to use fragmented Adobe form, but the number of fields was not there in the standard service interface. So, we opted for the **DDIC interface option available in ‘Assign Form Templates’**.

Challenge: To achieve this requirement, I had faced a couple of challenges:

1. Spool request could not be found - APOC\_OR\_MESSAGES (145): Discussed in this blog.
2. Dump - /BOBF/CX\_FRW\_FATAL – CLASS CL\_APOC\_OR\_A\_ITEM\_GET\_DOCUMENT: Create a Z\* Driver program for the form individually and check the issue there – for my case, [ADS Configuration](https://help.sap.com/saphelp_nwmobile71/helpdata/en/43/f0638873b56bede10000000a11466f/frameset.htm) was the issue, handled by me and basis tech guy
3. Bar code center alignment: [Centre Alignment of BARCODE](https://blogs.sap.com/2023/03/16/adobe-form-centre-alignment-of-barcode-128-with-xml-schema/) blog.

In this blog post we will cover the steps to print GR Label and handle **Spool request could not be found - APOC\_OR\_MESSAGES (145)**.

## **MAIN CONTENT****:**

1. Firstly, get the name of the standard program – subroutine (Form routine) that you would be triggered in the back-end from the business process. You can later, choose any other sub-routine as well, if that one has better parameters as per your requirement. Make sure the sub-routine you are choosing has \*PDF or ADOBE\* naming pattern to have the FP\_JOB\_OPEN/CLOSE else you must manually change the printout subroutine.

\*\* In my case, I have used Program – SAPM07DR, Routine - ENTRY\_WE03\_PDF.

2. Create an executable report ZAB\_IM\_SAPM07DR replicating subroutine-pool SAPM07DR, Includes ZIN\_IM\_M07DRTOP, ZIN\_IM\_M07DRSON\_PDF from M07DRTOP, M07DRSON\_PDF resp. and replace the std. includes with them in program ZAB\_IM\_SAPM07DR.

3. Go to SFP, create a DDIC interface as per the parameters exported in the sub-routine, handle the required processing logic, and create the required layout in ADOBE form to the interface.

**4. Point of solution**: In the subroutine, FORM\_OPEN\_PDF, just before FP\_JOB\_OPEN – handle the output parameters as below, as per [SAP KBA 3016791 - Error 'Spool request could not be found.'](https://me.sap.com/notes/0003016791):

```
  gs_outputparams-getpdf   = abap_false.
  gs_outputparams-reqnew   = abap_true.
  gs_outputparams-covtitle = nast-tdcovtitle.
  gs_outputparams-nodialog = abap_true.
  gs_outputparams-preview  = abap_false.​
```

Activate the program.

5. Share the name to functional or manage it in SPRO.

+ Application Area: 'Cross-Application Components'

+ Sub Application Area: 'Output Control'

+ Select the configuration step 'Assign Form Templates' (SSCUI 102313)

+ Maintain

  * Application Object Type - GOODS\_MOVEMENT

  * Output Type - GOODS\_RECEIPT\_LABEL

  * Form type – 2 – Output Forms (DDIC Interface)

  * Form Template ID - ZAF\_IM\_GR\_LABEL

  * Program – ZAB\_IM\_SAPM07DR

  * Routine - ENTRY\_WE03\_PDF![](/legacyfs/online/storage/blog_attachments/2023/03/assign-form-templates.png)

*(Don’t forget to transport the config data with customizing transport in testing client – Tcode SCC1).*

1. Now functional will go to transaction OPD or below process, that will trigger Fiori launchpad. ![](/legacyfs/online/storage/blog_attachments/2023/03/OPD.png)

And edit the entry for the configured form under ‘Form Template’ for Rules for ‘GOODS\_MOVEMENT’ replacing the standard form and activate it.

## **Outcome****:**

Now create a document in the test client for Material document and go to MIGO, enter MBLNR -> output-> Display Outputs.

Enter a row with Preparation status & and details as per configuration.

![](/legacyfs/online/storage/blog_attachments/2023/03/MIGO-1.png)

Select the row and click Display document (pdf icon)

![](/legacyfs/online/storage/blog_attachments/2023/03/output-1.png)

GR\_LABEL - Z\*FORM\*

**Reference links**:

[2736938 - Settings for processing program and form templates in billing document in new output manag...](https://userapps.support.sap.com/sap/support/notes/2736938)

[2294198 - SAP S/4HANA output control - customized forms](https://me.sap.com/notes/2294198)

[2608890 - Standard S/4HANA Output Control settings for Purchasing (output forms and processing progr...](https://userapps.sup...