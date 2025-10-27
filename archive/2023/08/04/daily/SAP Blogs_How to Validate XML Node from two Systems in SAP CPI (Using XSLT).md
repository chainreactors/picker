---
title: How to Validate XML Node from two Systems in SAP CPI (Using XSLT)
url: https://blogs.sap.com/2023/08/03/how-to-validate-xml-node-from-two-systems-in-sap-cpi-using-xslt/
source: SAP Blogs
date: 2023-08-04
fetch_date: 2025-10-04T12:01:31.746160
---

# How to Validate XML Node from two Systems in SAP CPI (Using XSLT)

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Technology](/t5/technology/ct-p/technology)
* [Technology Blog Posts by Members](/t5/technology-blog-posts-by-members/bg-p/technology-blog-members)
* How to Validate XML Node from two Systems in SAP C...

Technology Blog Posts by Members

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/technology-blog-members/article-id/164149&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [How to Validate XML Node from two Systems in SAP CPI (Using XSLT)](/t5/technology-blog-posts-by-members/how-to-validate-xml-node-from-two-systems-in-sap-cpi-using-xslt/ba-p/13573690)

![prathmesh009](https://avatars.profile.sap.com/f/7/idf71a13c1d12ac5a41b5c6dcda7aed8fc52a85efb63c69519efaa36f3a00bdd04_small.jpeg "prathmesh009")

[prathmesh009](https://community.sap.com/t5/user/viewprofilepage/user-id/810089)

Explorer

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=technology-blog-members&message.id=164149)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/technology-blog-members/article-id/164149)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13573690)

‎2023 Aug 03
7:45 PM

[3
Kudos](/t5/kudos/messagepage/board-id/technology-blog-members/message-id/164149/tab/all-users "Click here to see who gave kudos to this post.")

3,206

* SAP Managed Tags
* [SAP Integration Suite](https://community.sap.com/t5/c-khhcw49343/SAP%2520Integration%2520Suite/pd-p/73554900100800003241)
* [Cloud Integration](https://community.sap.com/t5/c-khhcw49343/Cloud%2520Integration/pd-p/67837800100800006801)

* [Cloud Integration

  SAP Integration Suite](/t5/c-khhcw49343/Cloud%2BIntegration/pd-p/67837800100800006801)
* [SAP Integration Suite

  SAP Integration Suite](/t5/c-khhcw49343/SAP%2BIntegration%2BSuite/pd-p/73554900100800003241)

View products (2)

**This blog post is intended to inform readers about a recent objective task I encountered while working on a project that involved two SAP systems. The purchase order number validation in both systems in the SAP CPI environment had to be done. If the two PO numbers were the same and confirmed, then inbound scenario has to be triggered.**

**System 1 : SAP S4 Hana (Note we will be using HTTPS considering it as SAP System)**

**System 2 : SAP ByD**

Below is the list of Contents :

1. Pre-requisites

2. Process Flow

3. iflow Development

4. Exception Handling

**————————————————————————————————————————————–**

### **1. Pre-requisites**

###

* In order to create this scenario work you will need access to SAP BTP (Integration Suite) with necessary roles and capabilities assigned. Or else you can refer this blog to [Set Up Integration Suite](https://developers.sap.com/tutorials/cp-starter-isuite-onboard-subscribe.html)

* Have knowledge about creating Integration flows (iflow) using SAP CPI.

* Knowledge of Adapters and other CPI Pallet options.

* OData API, Mail Credentials (for Exception).

* *Proxy, RFC, IDoc (As we are involving two system SAP & ByD therefore for posting data from SAP to CPI we can do it using the three given options)* ***\*Here we are using HTTPS considering it as a SAP System.***

'

### 2. Process Flow

![](/legacyfs/online/storage/blog_attachments/2023/08/Magenta-Step-Venn-Diagram.png)

Process Flow

### 3. iFlow Development

Create a Package and iflow

![](/legacyfs/online/storage/blog_attachments/2021/11/2-15.png)

Fill up Package Name of your choice, Technical Name and Description about the scenario.

Now Create new iflow and fill up details such as name, id and description.

![](/legacyfs/online/storage/blog_attachments/2023/08/4-10.png)

After Clicking on "Ok"

![](/legacyfs/online/storage/blog_attachments/2023/08/6-8.png)

As per our Flow Diagram first step is to **Fetch SAP Data into CPI (Content Modifier)**

![](/legacyfs/online/storage/blog_attachments/2023/08/adapter.png)

Postman As SAP System (System A)

Now we will use **"Content Enricher"**(To know functioning of <https://help.sap.com/docs/cloud-integration/sap-cloud-integration/define-content-enricher> )

In the 2nd Step we will connect another system (ByD) using OData to "Content Enricher" to merge the payloads from both systems.

![](/legacyfs/online/storage/blog_attachments/2023/08/snip2.png)

OData Configuration :

![](/legacyfs/online/storage/blog_attachments/2023/08/jkada.png)

In the Processing Tab select the fields you want in your payload structure.

![](/legacyfs/online/storage/blog_attachments/2023/08/adh.png)

Now till this step the message payload could look somewhat like this :

```
<?xml version='1.0' encoding='UTF-8'?>

<multimap:Messages xmlns:multimap="http://sap.com/xi/XI/SplitAndMerge">

  <multimap:Message1>       //Message from System A (Which is SAP in our Case)

    <DocNumber>100</DocNumber>

    <PurchaseOrderNumber>12345</PurchaseOrderNumber>  //This is the Purchase order number from SAP System

    <Item>Television</Item>

  </multimap:Message1>

  <multimap:Message2>   //Message from System B (Which is ByD in our Case)

     <rfc:ZHR_GET_EMP_BENEFIT_DETAILS.Response xmlns:rfc="urn:sap-com:document:sap:rfc:functions">

       <LT_0167>

   <PONum>12345</PONum>    //This is the Purchase order number from ByD System

        <item>

        <PERNR>00012345</PERNR></item>

        <DOB>01/01/2020</DOB>

        ....

       </LT_0167>

     </rfc:ZHR_GET_EMP_BENEFIT_DETAILS.Response>

  </multimap:Message2>

</multimap:Messages>
```

```
<multimap:Message1>   Payload from System A is captured in  </multimap:Message1>

<multimap:Message2> Payload from System B is captured in </multimap:Message2>

Now in the next step we will use XPATH in content modifier.

![](/legacyfs/online/storage/blog_attachments/2023/08/fhkfhka.png)

Source Value is captured from the XML Payload

Eg. <Parent>

     <Items>

        <material>101213</material>

        <price>100.00</price>

     </Items>

    </Parent>

If we want to pick only price then the source value would be.

//Parent/Items/price

In the same way select source values of both PO Numbers according to the combined payload.

![](/legacyfs/online/storage/blog_attachments/2023/08/hfffeq.png)

Now we will use XSLT Mapping Option from Pallets.

and write the below code to compare two nodes together. (Our Logic)
```

```
<?xml version="1.0" encoding="UTF-8" ?>

<xsl:transform xmlns:xsl="http://www.w3.org/1999/XSL/Transform" version="1.0">

 <xsl:output method="xml"  omit-xml-declaration="no" encoding="UTF-8" indent="yes" />

 <xsl:strip-space elements="*"/>

  <xsl:template match="/">

    <Output>

      <xsl:apply-templates select="/ParentNode/Child/PONum = /ParentNode_ByD/Child/ID"/>

    </Output>

  </xsl:template>

  <xsl:template match="@*|node()">

    <xsl:copy>

        <xsl:select-templates select="@*|node()"/>

    </xsl:copy>

  </xsl:template>

</xsl:transform>
```

You can notice in the <Output> </Output> Node i have compared the Xpaths which we have stored in Content Modifier in the previous step.

It will ultimately compare both nodes dynamically and give output in the form of Boolean (True or False)

Till this step our development is able to understand whether the XML Nodes are matching or not.

Now we will be using **"Router"**to bifurcate the flow.

![](/legacyfs/online/storage/blog_attachments/2023/08/jfkjfja.png)

* Router will have two branches (Matching...