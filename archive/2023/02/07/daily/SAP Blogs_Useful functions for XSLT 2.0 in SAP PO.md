---
title: Useful functions for XSLT 2.0 in SAP PO
url: https://blogs.sap.com/2023/02/06/useful-functions-for-xslt-2.0-in-sap-po/
source: SAP Blogs
date: 2023-02-07
fetch_date: 2025-10-04T05:51:21.957306
---

# Useful functions for XSLT 2.0 in SAP PO

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Technology](/t5/technology/ct-p/technology)
* [Technology Blog Posts by Members](/t5/technology-blog-posts-by-members/bg-p/technology-blog-members)
* Useful functions for XSLT 2.0 in SAP PO

Technology Blog Posts by Members

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/technology-blog-members/article-id/162161&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [Useful functions for XSLT 2.0 in SAP PO](/t5/technology-blog-posts-by-members/useful-functions-for-xslt-2-0-in-sap-po/ba-p/13561824)

![jo_kr](https://avatars.profile.sap.com/d/c/iddc4ead11db01a60fd97c8c45705ad8084a4061baba9438c3dd05a02b42ccd39b_small.jpeg "jo_kr")

[jo\_kr](https://community.sap.com/t5/user/viewprofilepage/user-id/212163)

Explorer

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=technology-blog-members&message.id=162161)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/technology-blog-members/article-id/162161)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13561824)

‎2023 Feb 06
7:07 PM

[1
Kudo](/t5/kudos/messagepage/board-id/technology-blog-members/message-id/162161/tab/all-users "Click here to see who gave kudos to this post.")

3,168

* SAP Managed Tags
* [SAP Process Orchestration](https://community.sap.com/t5/c-khhcw49343/SAP%2520Process%2520Orchestration/pd-p/477916618626075516391832082074785)

* [SAP Process Orchestration

  Software Product](/t5/c-khhcw49343/SAP%2BProcess%2BOrchestration/pd-p/477916618626075516391832082074785)

View products (1)

Dear SAP PO community,

inspired by the blog post "[Useful XSLT mapping functions in SAP XI/PI](https://blogs.sap.com/2013/09/23/useful-xslt-mapping-functions-in-sap-xipi/)", I want to provide some more snippets.
Hint: In general Java function calls are often not required anymore with XSLT 2.0, but makes life easier for some SAP PO capabilites, like DynamicConfiguration or AuditLog-Access.

Prerequisite for xslt 2.0:

You must have implemented the following note in your SAP PO system:
[1893110 - Integrate external XSLT transformer in PI Mapping Runtime](https://launchpad.support.sap.com/#/notes/1893110) for [using XSLT 2.0](https://blogs.sap.com/2014/10/14/how-to-import-and-use-xslt-20-mappings-in-sap-pipo/)
[2221350 - Support for Java Extensions in the SaxonHE XSLT Transformer](https://launchpad.support.sap.com/#/notes/0002221350/E) for Java Function calls

Please see a working xslt 2.0, providing many aspects and SAP PO specials.
There is value mapping lookup, Java function call, custom xslt function, writing to MappingTrace, conditional Xpath 2.0, writing to AuditLog (Message Log), runtime details of xslt 2.0, date formatting and calculation without Java.

```
<?xml version="1.0" encoding="UTF-8"?>

<xsl:stylesheet version="2.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform" xmlns:atrace="java:com.sap.aii.mapping.api.AbstractTrace"

  xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:fn="urn:my:function" xmlns:xml="http://www.w3.org/XML/1998/namespace"

  xmlns:xslthelper="java:de.ho2.sappo.XsltMappingHelper"

  xmlns:vm="java:com.sap.aii.mapping.value.api.XIVMService" exclude-result-prefixes="vm atrace fn xsd xslthelper">

  <xsl:output method="xml" encoding="UTF-8" version="1.0" indent="yes"/>

  <!-- adding standard input parameters, also see https://help.sap.com/docs/SAP_NETWEAVER_750/0b9668e854374d8fa3fc8ec327ff3693/4bf40f2cc0c33de4e100000... -->

  <!-- Standard: HashMap of input Parameters -->

  <xsl:param name="inputparam"/>

  <!-- Standard: Runtime Constants -->

  <xsl:param name="MessageId"/>

  <xsl:param name="TimeSent"/>

  <xsl:param name="Interface"/>

  <xsl:param name="SenderParty"/>

  <xsl:param name="SenderService"/>

  <xsl:param name="ReceiverParty"/>

  <xsl:param name="ReceiverService"/>

  <!-- Standard: instance of AbstractTrace for MappingTrace -->

  <xsl:param name="MappingTrace"/>

  <!-- Stylesheet Name -->

  <xsl:variable name="xslName" select="replace(document-uri(document('')),'sapximapping:','')"/>

  <!-- Root of document (note the * which is required when using <xsl:template match="@*|node()">) -->

  <xsl:template match="/*">

    <!-- Stylesheet version -->

    <xsl:variable name="xslVersion" select="system-property('xsl:version')"/>

    <!-- Xslt processor name -->

    <xsl:variable name="product-name" select="system-property('xsl:product-name')"/>

    <!-- Xslt processor version -->

    <xsl:variable name="product-version" select="system-property('xsl:product-version')"/>

    <!-- writing runtime infos to the MappingTrace -->

    <xsl:sequence select="atrace:addInfo($MappingTrace,concat('XSLT processing stylesheet : ', $xslName,' (version: ',$xslVersion, ') on ', $product-name, ' ', $product-version ))"/>

    <!-- set DynamicConfiguration by using a Java extension call -->

    <!-- writing infos to the MappingTrace -->

    <xsl:sequence select="atrace:addInfo($MappingTrace, xslthelper:createDcEntry('https://sap/rest', 'operation', 'operation', $inputparam))"/>

    <!-- read DynamicConfiguration by using a Java extension call -->

    <!-- writing result to the MappingTrace -->

    <xsl:sequence select="atrace:addInfo($MappingTrace, xslthelper:getDcEntry('https://sap/rest', 'operation', $inputparam))"/>

    <!-- writing to Message Log (AuditLog) -->

    <xsl:sequence select="atrace:addInfo($MappingTrace, xslthelper:writeAuditLogMesage('Hello Audit Log (only written during runtime)', string($MessageId), 'success'))"/>

    <!-- current timestamp in xslt 2.0 method - more details about date functions and formatting can be found on the internet, no Java needed anymore -->

    <!-- No Java calls are required anymore for date stuff and even calculation, only a few examples: -->

    <xsl:sequence select="atrace:addInfo($MappingTrace, concat('Timestamp: ', string( current-dateTime()), '
Line-Feed: &amp;#xa; (hex) or &amp;#10; (dec)

    Date-Formatting: ', string(format-date(current-date(), '[Y0001]/[M01]/[D01]')),

    '
and one day later: ', string(format-date(current-date()+xsd:dayTimeDuration('P1D'), '[Y0001]/[M01]/[D01]')) ) )"/>

    <!-- Value-Mapping Lookup -->

    <!-- It's important for function calls to provide variable types with xsd:string, as alternative for using the string() function -->

    <!-- the ? will also work for empty sequences/results, which is similar to null in Java -->

    <xsl:variable name="vm-result" as="xsd:string?" select="vm:executeMapping('sourceAgency','sourceScheme', 'value','targetAgency','targetScheme')"/>

    <xsl:variable name="shouldTheMappingFail" select="yes|no"/>

    <!-- Cancel processing in case of "error"-->

    <!--xslt 2.0 conditional Xpath and xstl 2.0 error function-->

    <xsl:sequence select="if (string-length($vm-result) = 0 and $shouldTheMappingFail='yes')  then (error(  () , 'Lookup value is empty!')) else () "/>

    <xsl:sequence select="atrace:addInfo($MappingTrace,concat('Lookup Result: ', $vm-result ))"/>

    <!-- simply copy the source XML document

    <xsl:copy-of select="."/>-->

    <xsl:copy>

      <xsl:apply-templates select="@*|node()" />

    </xsl:copy>

  </xsl:template>

<!--simply copy all and use the custom function to print some comments-->

  <xsl:template match="@*|node()">

  <xsl:if test=". instance of element() ">

      <xsl:comment select="c...