---
title: How to extract XSD from a WSDL with multiple Schema definitions
url: https://blogs.sap.com/2023/01/28/how-to-extract-xsd-from-a-wsdl-with-multiple-schema-definitions/
source: SAP Blogs
date: 2023-01-29
fetch_date: 2025-10-04T05:07:41.041973
---

# How to extract XSD from a WSDL with multiple Schema definitions

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Technology](/t5/technology/ct-p/technology)
* [Technology Blog Posts by Members](/t5/technology-blog-posts-by-members/bg-p/technology-blog-members)
* How to extract XSD from a WSDL with multiple Schem...

Technology Blog Posts by Members

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/technology-blog-members/article-id/161059&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [How to extract XSD from a WSDL with multiple Schema definitions](/t5/technology-blog-posts-by-members/how-to-extract-xsd-from-a-wsdl-with-multiple-schema-definitions/ba-p/13556307)

![vinaymittal](https://avatars.profile.sap.com/a/6/ida67175bb9d6c01d6452c9710944c8e53c095e40f6e2c7452c5170cc2ba4afb02_small.jpeg "vinaymittal")

[vinaymittal](https://community.sap.com/t5/user/viewprofilepage/user-id/187725)

Contributor

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=technology-blog-members&message.id=161059)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/technology-blog-members/article-id/161059)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13556307)

‎2023 Jan 28
4:39 PM

[9
Kudos](/t5/kudos/messagepage/board-id/technology-blog-members/message-id/161059/tab/all-users "Click here to see who gave kudos to this post.")

22,565

* SAP Managed Tags
* [SAP Integration Suite](https://community.sap.com/t5/c-khhcw49343/SAP%2520Integration%2520Suite/pd-p/73554900100800003241)

* [SAP Integration Suite

  SAP Integration Suite](/t5/c-khhcw49343/SAP%2BIntegration%2BSuite/pd-p/73554900100800003241)

View products (1)

## **This tool Is again Available Introduction**

As an Integration consultant I come across scenarios where I have a complex WSDL at hand with deeply nested structures and multiple schema definitions like the one below for Business Partner Replication.

![](/legacyfs/online/storage/blog_attachments/2023/01/Capture-16.png)

Working with WSDL's is all good and cool until you come across a requirement where you have to extract the XSD out of the WSDL and work on that. There might be several reasons why you may need to extract the XSD out of the WSDL a few of them which I faced are below.

+ * XSD needs to be shared with a third party as their system only accepts and works upon XSD's.

  * WSDL contains too much information and as SAP CI is interfacing between the third party and SAP this information is either not needed at their end or needs to be abstracted.

  * You need to do a XML validation in SAP CI which only works on a XSD schema and does not accept a WSDL!

  * You need to edit the schema in a way to perform multimapping on it for example
    <Messages>
    <Message1>
    <WSDL's Schema>
    </Message1>
    <Message2>
    <Schema2>
    </Message2>

In all of these cases working on a WSDL directly and updating it is a nightmare and so is trying to extract the schema's manually. Sometimes the WSDL files are easily over 10000 lines which makes it impossible to do it manually without comiting any mistakes.

Also what if you want a schema without any namespace prefixes? Stripping all the declarations and namespaces  and also ensuring that you handle complexType definitions where the name is same for different complexType definitions s a task in itself.

For example look at the two complexType "Text" definitions below they both are taken from the same WSDL but different Schema's

```
 <xsd:complexType name="Text">

    <xsd:sequence>

     <xsd:element name="BuyerTextElementID" minOccurs="0" type="TextElement"/>

     <xsd:element name="SupplierTextElementID" minOccurs="0" type="TextElement"/>

     <xsd:element name="TextElementLanguage" minOccurs="0" type="LanguageCode"/>

     <xsd:element name="TextElementText" minOccurs="0" type="TextElementText"/>

     <xsd:element name="TextElementTextFormat" minOccurs="0" type="TextElementTextFormat"/>

    </xsd:sequence>

    <xsd:attribute name="Type" type="TextType"/>

 </xsd:complexType>

And

<xsd:complexType name="Text">

    <xsd:annotation>

     <xsd:documentation xml:lang="EN">

      <ccts:RepresentationTerm>Text</ccts:RepresentationTerm>

     </xsd:documentation>

    </xsd:annotation>

    <xsd:simpleContent>

     <xsd:extension base="xsd:string">

      <xsd:attribute name="languageCode" type="LanguageCode"/>

     </xsd:extension>

    </xsd:simpleContent>

</xsd:complexType>
```

If you just copy paste all the schema nodes into a single file you will have conflicting namespace declarations, mirror duplicate types, and duplicate types with different definitions and whole lot of WSDL definitions to take care of. Working on a small WSDL is easy but when it comes to large WSDL's  like the one's from SAP its not an easy task.

## **Solution**

I developed a solution for this very problem and have deployed it for free use on [UtilityArena.](https://www.utilityarena.com/wsdlToXSDGeneratorController?initial)

Let me demonstrate how easy it is to extract a XSD out of a complex WSDL or repair a broken WSDL(a WSDL without any schema prefixes like the ones from salesforce , these are not accepted as is by SAP CI).

Go to the link above and upload your WSDL or paste the WSDL content in the text area.

![](/legacyfs/online/storage/blog_attachments/2023/01/Capture-17.png)

Click on Extract XSD and then you will have your extracted XSD ready for download.

![](/legacyfs/online/storage/blog_attachments/2023/01/Capture1.png)

And with just a few clicks you will have your XSD extracted from a WSDL in seconds.

* [wsdl](/t5/tag/wsdl/tg-p/board-id/technology-blog-members)
* [xsd](/t5/tag/xsd/tg-p/board-id/technology-blog-members)

11 Comments

You must be a registered user to add a comment. If you've already registered, sign in. Otherwise, register and sign in.

* [Comment](/plugins/common/feature/oidcss/sso_login_redirect/providerid/sap_ids_prompt?redirectreason=permissiondenied&referer=https%3A%2F%2Fcommunity.sap.com%2Ft5%2Ftechnology-blog-posts-by-members%2Fhow-to-extract-xsd-from-a-wsdl-with-multiple-schema-definitions%2Fba-p%2F13556307%23comment-on-this)

Copy Link
![](https://community.sap.com/html/@EE5D5986E9F4E5657DCEACB7532B5C39/assets/bluesky-dark.svg)Bluesky
Linkedin

Related Content

* [S/4HANA transition for US Federal Agencies](/t5/technology-blog-posts-by-sap/s-4hana-transition-for-us-federal-agencies/ba-p/14234423)
  in [Technology Blog Posts by SAP](/t5/technology-blog-posts-by-sap/bg-p/technology-blog-sap)  6 hours ago
* [Basic Configurations for SAP EWM Material Flow System: Part-1](/t5/technology-blog-posts-by-members/basic-configurations-for-sap-ewm-material-flow-system-part-1/ba-p/14233314)
  in [Technology Blog Posts by Members](/t5/technology-blog-posts-by-members/bg-p/technology-blog-members)  16 hours ago
* [SAP IQ to SAP HANA Cloud, Data Lake Migration Overview](/t5/technology-blog-posts-by-sap/sap-iq-to-sap-hana-cloud-data-lake-migration-overview/ba-p/14228663)
  in [Technology Blog Posts by SAP](/t5/technology-blog-posts-by-sap/bg-p/technology-blog-sap)  Wednesday
* [Artificial Intelligence and SAP Master Data Governance](/t5/technology-blog-posts-by-sap/artificial-intelligence-and-sap-master-data-governance/ba-p/14152960)
  in [Technology Blog Posts by SAP](/t5/technology-blog-posts-by-sap/bg-p/technology-blog-sap)  Tuesday
* [Quantifying Process Improvements: Creating Value...