---
title: Value Mapping usage in XSLT Mappings with CPI
url: https://blogs.sap.com/2023/01/18/value-mapping-usage-in-xslt-mappings-with-cpi/
source: SAP Blogs
date: 2023-01-19
fetch_date: 2025-10-04T04:16:37.895527
---

# Value Mapping usage in XSLT Mappings with CPI

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Technology](/t5/technology/ct-p/technology)
* [Technology Blog Posts by Members](/t5/technology-blog-posts-by-members/bg-p/technology-blog-members)
* Value Mapping usage in XSLT Mappings with CPI

Technology Blog Posts by Members

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/technology-blog-members/article-id/163541&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [Value Mapping usage in XSLT Mappings with CPI](/t5/technology-blog-posts-by-members/value-mapping-usage-in-xslt-mappings-with-cpi/ba-p/13570311)

![RobertQ](https://avatars.profile.sap.com/4/0/id403ff67f0c95beecefe426d1fc8bec2c2c8650a47f14267dfcef9a0340d2ffdb_small.jpeg "RobertQ")

[RobertQ](https://community.sap.com/t5/user/viewprofilepage/user-id/121246)

Explorer

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=technology-blog-members&message.id=163541)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/technology-blog-members/article-id/163541)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13570311)

‎2023 Jan 18
9:41 PM

[3
Kudos](/t5/kudos/messagepage/board-id/technology-blog-members/message-id/163541/tab/all-users "Click here to see who gave kudos to this post.")

10,110

* SAP Managed Tags
* [Cloud Integration](https://community.sap.com/t5/c-khhcw49343/Cloud%2520Integration/pd-p/67837800100800006801)

* [Cloud Integration

  SAP Integration Suite](/t5/c-khhcw49343/Cloud%2BIntegration/pd-p/67837800100800006801)

View products (1)

# Introduction:

I recently got asked by a collegue how to add information to an xslt mapping from a value mapping in SAP Integration Suite/ Cloud Integration for a migration project from SAP PI/PO to SAP Integration Suite. In the specific case he needed a solution to change the IDOC EDI\_DC40 field RCVPRN based on the SNDPRN/RCVPRN provided in the input ducument for several sender/ receiver systems and different IDOC Basic types.

I created a xslt mapping to edit the required target field and to add the information dynamicly based on extracted values from the input xml through a value mapping call.

This solution can be reused for all requirements there a xslt mapping is used and information from a value mapping needs to be included in the transformation.

To use this solution you should have basic value mapping, basic groovy script / java and basic xslt knowledge.

# Implementation:

## Solution overview:

Use the adapter of your choise to send input data to your IFlow. For this blog post I use the HTTPS adapter to post a sample xml via postman to the SAP Integration Suite.

![](/legacyfs/online/storage/blog_attachments/2023/01/Iflow.png)

Overview

## Content Modifier:

I use a content modifier to read the input information from the input xml as xpath parameters. This can also be achieved directly in the Groovy script by analysing the input xml. For simplicity and if you are not so experienced in Java/ Groovy I recomend the usage of the Content Modifier.

![](/legacyfs/online/storage/blog_attachments/2023/01/ContentModifier-1.png)

Content Modifier

## Groovy Script:

In the Groovy script I define variables to hold the information from the Content Modifier.

The variables are then used to call the ValueMapping API for mapping an input value to an output value. This mapped value is then stored as an exchange parameter that can be acces in the xslt mapping afterwards.

```
import com.sap.gateway.ip.core.customdev.util.Message;

import java.util.HashMap;

import com.sap.it.api.ITApiFactory

import com.sap.it.api.mapping.ValueMappingApi

def Message processData(Message message) {

    def map = message.getProperties();

    sAgency = map.get("inputSAgency");

    sIdentifier = map.get("inputSIdentifier");

    inputValue = map.get("inputValue");

    rAgency = map.get("inputRAgency");

    rIdentifier = map.get("inputRIdentifier");

    def VMservice = ITApiFactory.getService(ValueMappingApi.class, null);

    if( VMservice != null)

    {

        def mappedValue = VMservice.getMappedValue(sAgency, sIdentifier, inputValue, rAgency, rIdentifier)

        message.setProperty("outputValue", mappedValue);

    }

    return message;

}
```

# XSLT Mapping:

In the XSLT Mapping I access the exchange parameters via a xslt param, which are automaticly linked to the corresponding exchange parameters or header of the IFlow. I use the mapped outputValue in the mapping. If no value mapping is found and the value is null or empty, I copy the input value as a fallback.

```
<?xml version="1.0" encoding="utf-8"?>

<xsl:stylesheet xmlns:xsl="http://www.w3.org/1999/XSL/Transform" version="3.0" xmlns:xs="http://www.w3.org/2001/XMLSchema" exclude-result-prefixes="#all">

	<xsl:output method="xml" indent="yes" encoding="UTF-8"/>

	<xsl:mode on-no-match="shallow-copy"/>

	<xsl:param name="outputValue"/>

	<xsl:template match="/" name="xsl:initial-template">

		<xsl:next-match/>

	</xsl:template>

	<xsl:template match="//IDOC/EDI_DC40/RCVPRN">

		<xsl:element name="RCVPRN">

			<xsl:choose>

				<xsl:when test="string-length($outputValue)>0">

					<xsl:value-of select="$outputValue"/>

				</xsl:when>

				<xsl:otherwise>

					<xsl:value-of select="."/>

				</xsl:otherwise>

			</xsl:choose>

		</xsl:element>

	</xsl:template>

</xsl:stylesheet>
```

## Value Mapping:

In the Value Mapping I added a value map for a Source agency "SAgency", Source identifier "SIdentifier", Target agency "RAgency", Target identifier "RIdentifier". I added a value mapping for a source value "SValue" to a target value "RValue".

For your purpose you can modifie the corresponding values.

![](/legacyfs/online/storage/blog_attachments/2023/01/ValueMapping.png)

ValueMapping

## Test the solution:

For testing this solution I use postman. You can use a tool of your choise to the send data to the SAP Integration Suite.

I send a part of an IDOC xml via postman with the SNDPRN as "SAgency" and the RCVRPN as "SValue". This fields are then extracted in the Content Modifier. The Groovy Script that uses the information for the Value Mapping and in the XSLT Mapping I map the mapped Value "RValue" to the RCVPRN field. In the picture below you can see the input xml and the output xml with the mapped value in the RCVPRN fiel.

![](/legacyfs/online/storage/blog_attachments/2023/01/Test.png)

Test

# Conclusion and further Enhancements:

In this blog post I wanted to show you the usage of a XSLT mapping with a Value Mapping.

Further enhancements to this solutions could be the use of XSLT to access the Value Mapping API directly from the script without the need of a Content Modifier or a Groovy script. For such an aproch you would need to create a seperate Java Class to provide a methode that do the work describet in the Groovy script or to find out, how the  ITApiFactory class can be used in XSLT to get the VMService and exceute the getMappendValue function.

Another useful scenario would be to use this aproach with the combination of an XSLT Mapping created in the Integration Advisor and access the mapped value as a global parameter.

I hope this post is helpful to you and thank you for reading this blog post. Please feel free to share your feedback or thoughts in the comments section.

Best regards

Robert Quindt

* [cloud integration](/t5/tag/cloud%20integration/tg-p/board-...