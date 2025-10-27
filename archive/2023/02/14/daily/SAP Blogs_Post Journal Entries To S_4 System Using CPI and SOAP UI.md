---
title: Post Journal Entries To S/4 System Using CPI and SOAP UI
url: https://blogs.sap.com/2023/02/13/post-journal-entries-to-s-4-system-using-cpi-and-soap-ui/
source: SAP Blogs
date: 2023-02-14
fetch_date: 2025-10-04T06:31:43.507329
---

# Post Journal Entries To S/4 System Using CPI and SOAP UI

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Technology](/t5/technology/ct-p/technology)
* [Technology Blog Posts by Members](/t5/technology-blog-posts-by-members/bg-p/technology-blog-members)
* Post Journal Entries To S/4 System Using CPI and S...

Technology Blog Posts by Members

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/technology-blog-members/article-id/163182&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [Post Journal Entries To S/4 System Using CPI and SOAP UI](/t5/technology-blog-posts-by-members/post-journal-entries-to-s-4-system-using-cpi-and-soap-ui/ba-p/13568098)

![kvrsaicharan1152](https://avatars.profile.sap.com/f/2/idf2c3795251c4f615a2ce84b540ad02afea3746de9fb64c85f07f77cc586fb542_small.jpeg "kvrsaicharan1152")

[kvrsaicharan1152](https://community.sap.com/t5/user/viewprofilepage/user-id/716309)

Explorer

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=technology-blog-members&message.id=163182)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/technology-blog-members/article-id/163182)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13568098)

‎2023 Feb 13
9:11 PM

[2
Kudos](/t5/kudos/messagepage/board-id/technology-blog-members/message-id/163182/tab/all-users "Click here to see who gave kudos to this post.")

7,182

* SAP Managed Tags
* [SAP Integration Suite](https://community.sap.com/t5/c-khhcw49343/SAP%2520Integration%2520Suite/pd-p/73554900100800003241)
* [Cloud Integration](https://community.sap.com/t5/c-khhcw49343/Cloud%2520Integration/pd-p/67837800100800006801)
* [SAP S/4HANA](https://community.sap.com/t5/c-khhcw49343/SAP%2520S%252F4HANA/pd-p/73554900100800000266)

* [SAP S/4HANA

  SAP S/4HANA](/t5/c-khhcw49343/SAP%2BS%25252F4HANA/pd-p/73554900100800000266)
* [Cloud Integration

  SAP Integration Suite](/t5/c-khhcw49343/Cloud%2BIntegration/pd-p/67837800100800006801)
* [SAP Integration Suite

  SAP Integration Suite](/t5/c-khhcw49343/SAP%2BIntegration%2BSuite/pd-p/73554900100800003241)

View products (3)

# Introduction

This blog post describes how to post GL Account Documents from CPI and also how to test Async API from SOAP UI.

### Prerequisite:

* Object JOURNALENTRYBULKCREATIONREQUES should be activated in SOAMANGER webservice configuration.

* SOAP UI application should be downloaded in local system.

* To Post Journal entries to S/4 System. Technical User should be created and have sufficient authorization.

## Journal Entry - POST Asynchronous

First To test Asynchronous API, Go to Tcode SOAMANAGER in S/4 System. Click on Web service configuration and later on search with Object Name i.e JOURNALENTRYBULKCREATIONREQUES

![](/legacyfs/online/storage/blog_attachments/2023/02/soapservices4.jpg)

Go through the object and Open service WSDL generation and save WSDL file in system with .wsdl extension.

## Post JE From SOAP UI:

Now Open SOAP UI and create New SOAP Project by providing the WSDL file and now you will find two URL's  of having soap envelope versions SOAP 1.1 and SOAP 1.2

Here when you are trying to post journal entries through SOAP UI or Postman, you should provide Message ID in query parameters ex: 988C6E5C-2CC1-11CA-A044-08002B1BC518.

Now provide Technical User name and Password in SOAP UI and provide valid data in request body and then execute. For Asynchronous you will receive 202 Accepted as status code. I observed that sometimes even for bad data you will get 202 Accepted. So to check errors go to srt\_log Tcode and if you want to know whether it is delivered or not you can check in srt\_moni Tcode by providing the message ID that you have given while calling.

Journal Entries are posted in ACDOCA and BSEG Tables.

To check Document is created or not. Go to  Tcode SE16 -> ACDOCA/BSEG Table and Search by providing cost center ,year and currency Code

### Structure of Request Payload:

<soapenv:Envelope xmlns:soapenv="<http://www.w3.org/2003/05/soap-envelope>">
<soapenv:Header/>
<soapenv:Body>
<sfin:JournalEntryBulkCreateRequest xmlns:sfin="<http://sap.com/xi/SAPSCORE/SFIN>">
<MessageHeader>
<ID>MSG\_2023-02-08</ID>
<!--<ReferenceID></ReferenceID>-->
<CreationDateTime>2023-02-08T00:00:00Z</CreationDateTime>
</MessageHeader>
<!--1 or more repetitions:-->
<JournalEntryCreateRequest>
<MessageHeader>
<ID>SUB\_MSG\_2023-02-08</ID>
<!--<ReferenceID></ReferenceID>-->
<CreationDateTime>2023-02-08T00:00:00Z</CreationDateTime>
</MessageHeader>
<JournalEntry>
<OriginalReferenceDocumentType>BKPFF</OriginalReferenceDocumentType>
<OriginalReferenceDocument/>
<OriginalReferenceDocumentLogicalSystem/>
<BusinessTransactionType>RFBU</BusinessTransactionType>
<AccountingDocumentType>   </AccountingDocumentType>
<DocumentHeaderText>Test JE Posting</DocumentHeaderText>
<CreatedByUser>     </CreatedByUser>
<CompanyCode>     </CompanyCode>
<DocumentDate>2023-02-08</DocumentDate>
<PostingDate>2023-02-08</PostingDate>
<Item>
<!--Optional:-->
<GLAccount>    </GLAccount>
<AmountInTransactionCurrency currencyCode="">1000</AmountInTransactionCurrency>
<DebitCreditCode>S</DebitCreditCode>
<DocumentItemText>Testing 0442</DocumentItemText>
<AccountAssignment>
<!--Optional:-->
<CostCenter>    </CostCenter>
</AccountAssignment>
</Item>
<Item>
<!--Optional:-->
<GLAccount>   </GLAccount>
<AmountInTransactionCurrency currencyCode="">-1000</AmountInTransactionCurrency>
<DebitCreditCode>H</DebitCreditCode>
<DocumentItemText>Testing 0442</DocumentItemText>
<AccountAssignment>
<CostCenter></CostCenter>
</AccountAssignment>
</Item>
</JournalEntry>
</JournalEntryCreateRequest>
</sfin:JournalEntryBulkCreateRequest>
</soapenv:Body>
</soapenv:Envelope>

**Note:**

Debit and Credit Line Items should always be balanced. If Debit Line Item Amount is 100 then Credit Line Item Amount Should be -100.

You have to provide valid cost center , GL Account and Document Type to post journal entries in s/4 system

## Post Journal Entries From CPI:

To Post Journal Entries from CPI, We have to use SOAP RM Receiver Adapter. Store Technical User Name and Password in Security Store and Provide that Credential Name, URL, Location ID in SOAP RM Adapter Configuration. In Soap RM Message ID determination, you can select Generate or Reuse.

While Posting, You have to Use XSLT Mapping to provide prefix sfin: and xmlns namespace i.e xmlns:sfin="<http://sap.com/xi/SAPSCORE/SFIN>". You have to use after Message Mapping.

![](/legacyfs/online/storage/blog_attachments/2023/02/cpiflow.jpg)

Below XSLT Code will add Prefix sfin: and xmlns Namespace to the Request Payload. SOAP RM adapter will add soap envelope automatically.

**XSLT Code:**

<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<xsl:stylesheet version="1.0" xmlns:xsl="<http://www.w3.org/1999/XSL/Transform>" xmlns:soapenv="<http://schemas.xmlsoap.org/soap/envelope/>"
xmlns:sfin="<http://sap.com/xi/SAPSCORE/SFIN>">
<xsl:output omit-xml-declaration="yes" indent="yes"/>

<xsl:template match="node()|@\*">
<xsl:copy>
<xsl:apply-templates select="node()|@\*"/>
</xsl:copy>
</xsl:template>

<xsl:template match="JournalEntryBulkCreateRequest">
<xsl:element name="sfin:{name()}">
<xsl:apply-templates select="node()|@\*"/>
</xsl:element>
</xsl:template>
</xsl:stylesheet>

### Conclusion

This is how we can post journal entries using Asynchronous API from CPI and SOAP UI Application

Follow my profile to be notified for the next b...