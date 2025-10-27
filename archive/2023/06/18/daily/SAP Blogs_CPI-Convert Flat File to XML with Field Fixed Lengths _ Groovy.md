---
title: CPI-Convert Flat File to XML with Field Fixed Lengths | Groovy
url: https://blogs.sap.com/2023/06/17/cpi-convert-flat-file-to-xml-with-field-fixed-lengths-groovy/
source: SAP Blogs
date: 2023-06-18
fetch_date: 2025-10-04T11:45:52.318217
---

# CPI-Convert Flat File to XML with Field Fixed Lengths | Groovy

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Technology](/t5/technology/ct-p/technology)
* [Technology Blog Posts by Members](/t5/technology-blog-posts-by-members/bg-p/technology-blog-members)
* CPI-Convert Flat File to XML with Field Fixed Leng...

Technology Blog Posts by Members

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/technology-blog-members/article-id/162309&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [CPI-Convert Flat File to XML with Field Fixed Lengths | Groovy](/t5/technology-blog-posts-by-members/cpi-convert-flat-file-to-xml-with-field-fixed-lengths-groovy/ba-p/13562845)

![pkaushiksrinivas](https://avatars.profile.sap.com/5/7/id57a83de789d7907bf663211edaadebb140c94ed9efe1af6f8ff52d51ec4f2d85_small.jpeg "pkaushiksrinivas")

[pkaushiksrinivas](https://community.sap.com/t5/user/viewprofilepage/user-id/721484)

Explorer

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=technology-blog-members&message.id=162309)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/technology-blog-members/article-id/162309)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13562845)

‎2023 Jun 17
4:41 PM

[5
Kudos](/t5/kudos/messagepage/board-id/technology-blog-members/message-id/162309/tab/all-users "Click here to see who gave kudos to this post.")

12,104

* SAP Managed Tags
* [Cloud Integration](https://community.sap.com/t5/c-khhcw49343/Cloud%2520Integration/pd-p/67837800100800006801)

* [Cloud Integration

  SAP Integration Suite](/t5/c-khhcw49343/Cloud%2BIntegration/pd-p/67837800100800006801)

View products (1)

# Introduction

This blog covers an idea on how we can convert a Flat File to dynamic XML structure with Field Fixed Lengths in CPI using groovy script.

### Input Flat File Sample :

```
202310FABCDX    01TEST123 4530450801000100000002825999010152023

202310FABCDF    01TEST456 3530150801000100000014582444010152023

202310FABCDA    01TEST789 5530250801000100000023264182710152023
```

### Expected Output XML :

```
<?xml version="1.0" encoding="UTF-8"?>

<Root>

   <Record>

      <Date>202310</Date>

      <Mat>FABCDX</Mat>

      <PO>01TEST123</PO>

      <GRP1>453</GRP1>

      <GRP2>045</GRP2>

      <GRP3>0801</GRP3>

      <GRP4>0001</GRP4>

      <AMT>000000028259990</AMT>

      <CRDT>10152023</CRDT>

   </Record>

   <Record>

      <Date>202310</Date>

      <Mat>FABCDF</Mat>

      <PO>01TEST456</PO>

      <GRP1>353</GRP1>

      <GRP2>015</GRP2>

      <GRP3>0801</GRP3>

      <GRP4>0001</GRP4>

      <AMT>000000145824440</AMT>

      <CRDT>10152023</CRDT>

   </Record>

   <Record>

      <Date>202310</Date>

      <Mat>FABCDA</Mat>

      <PO>01TEST789</PO>

      <GRP1>553</GRP1>

      <GRP2>025</GRP2>

      <GRP3>0801</GRP3>

      <GRP4>0001</GRP4>

      <AMT>000000232641827</AMT>

      <CRDT>10152023</CRDT>

   </Record>

</Root>
```

### Groovy Script

```
import com.sap.gateway.ip.core.customdev.util.Message;

import java.util.HashMap;

import groovy.xml.*

import com.sap.it.api.ITApiFactory;

import com.sap.gateway.ip.core.customdev.util.Message;

import java.util.HashMap;

def Message processData(Message message)

{

  //Body

  def body = message.getBody(java.lang.String) as String;

  def lines = body.split("\n");

  //root node

  def body1 = "<Root>";

  //Get the XML segments name and Field fixed lengths

  def prop = message.getProperties();

  def Segments = prop.get("xmlSegments").split(",") as String[]

  def FieldFixedLengths = prop.get("FieldFixedLengths").split(",") as String[]

  //looping to read the lines and form a XML

  for (i = 0; i < lines.length; i++)

   {

    def sum = 0

    body1 += "<Record>";

    //looping through externalized parameters to create XML tag with fixed lengths

    for (k = 0; k < FieldFixedLengths.length; k++)

    {

      def l2 = Integer.valueOf(FieldFixedLengths[k]);

      println("Start" + sum + "End" + l2)

body1 += "<" + Segments[k] + ">" + lines[i].substring(sum, sum + Integer.valueOf(FieldFixedLengths[k])) + "</" + Segments[k] + ">";

      sum += Integer.valueOf(FieldFixedLengths[k]);

    }

    body1 += "</Record>";

  }

  //closing root note

  body1 += "</Root>";

//storing the converted XML to body

message.setBody(body1);

return message;

}
```

## Simulation results on online Groovy IDE :

![](/legacyfs/online/storage/blog_attachments/2023/06/Simulation-on-Online-Groovy-IDE.jpg)

Simulation Results for Flat File to XML with Field Fixed Length conversion

**NOTE** : Please pass xmlSegments and Field Fixed Lengths (with comma separated values) as Message Property through a Content Modifier

**Pros :**

* Dynamic names for XML segments can be generated as we are externalizing the XMLSegment names and their fixed field lengths.

**Cons :**

* This groovy may be suitable when the data load and no of lines in the flat file is less. If the no of Line items is comparatively more, then chances are there that we may observe a performance issue (in terms of processing times of this script). By referring the link [Handling text files in Groovy script of CPI (SAP Cloud Platform Integration). | SAP Blogs](https://blogs.sap.com/2019/07/15/handling-text-files-in-groovy-script-of-cpi-sap-cloud-platform-integration./) , the above groovy can be modified to read data as Input Stream instead of reading body as String for an optimal memory footprint.

## Summary

Groovy script to convert Flat file to XML (with dynamic xml segment names) was illustrated above.

Comments or feedback/suggestions, pros/cons with respect to the above are welcome from fellow Integration folks.

## References

* [SAP HCI/CPI - Cloud Platform Integration: Converting the File from field fixed length file to XML Su...](http://sapcpidesign.blogspot.com/2019/06/converting-file-from-field-fixed-length.html)

* [Convert flat file into XML | SAP Blogs](https://blogs.sap.com/2019/02/14/convert-flat-file-into-xml/)

* [Handling text files in Groovy script of CPI (SAP Cloud Platform Integration). | SAP Blogs](https://blogs.sap.com/2019/07/15/handling-text-files-in-groovy-script-of-cpi-sap-cloud-platform-integration./)

* [CPI](/t5/tag/CPI/tg-p/board-id/technology-blog-members)
* [flatfile](/t5/tag/flatfile/tg-p/board-id/technology-blog-members)
* [groovy](/t5/tag/groovy/tg-p/board-id/technology-blog-members)
* [xml](/t5/tag/xml/tg-p/board-id/technology-blog-members)

2 Comments

You must be a registered user to add a comment. If you've already registered, sign in. Otherwise, register and sign in.

* [Comment](/plugins/common/feature/oidcss/sso_login_redirect/providerid/sap_ids_prompt?redirectreason=permissiondenied&referer=https%3A%2F%2Fcommunity.sap.com%2Ft5%2Ftechnology-blog-posts-by-members%2Fcpi-convert-flat-file-to-xml-with-field-fixed-lengths-groovy%2Fba-p%2F13562845%23comment-on-this)

Copy Link
![](https://community.sap.com/html/@EE5D5986E9F4E5657DCEACB7532B5C39/assets/bluesky-dark.svg)Bluesky
Linkedin

Related Content

* [A Smarter Move from Boomi and MuleSoft to SAP Integration Suite - Assessed, Automated, Validated](/t5/technology-blog-posts-by-members/a-smarter-move-from-boomi-and-mulesoft-to-sap-integration-suite-assessed/ba-p/14233647)
  in [Technology Blog Posts by Members](/t5/technology-blog-posts-by-members/bg-p/technology-blog-members)  Thursday
* [How to Send Custom Headers (e.g., Transaction-Id) in HTTP PA...