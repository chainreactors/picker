---
title: SAP PI/PO – Download Dowjones quotation rates – JavaMapping solution
url: https://blogs.sap.com/2022/10/19/sap-pi-po-download-downjones-quotation-rates-javamapping-solution/
source: SAP Blogs
date: 2022-10-20
fetch_date: 2025-10-03T20:22:50.698262
---

# SAP PI/PO – Download Dowjones quotation rates – JavaMapping solution

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Technology](/t5/technology/ct-p/technology)
* [Technology Blog Posts by Members](/t5/technology-blog-posts-by-members/bg-p/technology-blog-members)
* SAP PI/PO – Download Dowjones quotation rates - Ja...

Technology Blog Posts by Members

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/technology-blog-members/article-id/160038&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [SAP PI/PO – Download Dowjones quotation rates - JavaMapping solution](/t5/technology-blog-posts-by-members/sap-pi-po-download-dowjones-quotation-rates-javamapping-solution/ba-p/13549915)

![rhviana](https://avatars.profile.sap.com/1/2/id1293610da630b8bdcc225f1ffcef912b628a41620563b195ef4f9c2c9d4de7b6_small.jpeg "rhviana")

[rhviana](https://community.sap.com/t5/user/viewprofilepage/user-id/160570)

Active Contributor

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=technology-blog-members&message.id=160038)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/technology-blog-members/article-id/160038)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13549915)

‎2022 Oct 19
8:12 PM

[1
Kudo](/t5/kudos/messagepage/board-id/technology-blog-members/message-id/160038/tab/all-users "Click here to see who gave kudos to this post.")

949

* SAP Managed Tags
* [SAP Process Integration](https://community.sap.com/t5/c-khhcw49343/SAP%2520Process%2520Integration/pd-p/01200615320800000719)
* [SAP Process Orchestration](https://community.sap.com/t5/c-khhcw49343/SAP%2520Process%2520Orchestration/pd-p/477916618626075516391832082074785)

* [SAP Process Integration

  SAP NetWeaver](/t5/c-khhcw49343/SAP%2BProcess%2BIntegration/pd-p/01200615320800000719)
* [SAP Process Orchestration

  Software Product](/t5/c-khhcw49343/SAP%2BProcess%2BOrchestration/pd-p/477916618626075516391832082074785)

View products (2)

Hello Folks on-premise,

Everything is good here or it’s time to fly (cloud) - SAP CPI !!!! ? ![:grinning_face:](/html/@4736AE9D443582E0D4797EA7008B31CA/emoticons/1f600.png ":grinning_face:")

I just would like to post one solution for a project that the requirement to download the list from DowJones in general used for quotation process and others related with financial aspects.

\*IMPORTANT, you should require user and password to access the DowJones API with DowJones team.\*

---

### **Agenda:**

---

1. #### Introduction

2. #### Integration Diagram

3. **Integration Development Steps**

   1. #### Process steps – Repository

      1. #### DJSPListResponse java - Outbound - First interface

      2. #### StreamToZipAttachment java - Inbound - Second interface

   2. #### Process steps – Directory

4. #### SAP PI Testing first interface

5. #### SAP PI Testing second interface

6. #### Conclusion

---

## Introduction

---

Basically the integration is using API Rest ( HTTPS ) to download the list of files that can be used for financial aspects.

There are two API's, one to download the list and another to download the ZIP file valid for that specific filename.

---

## Integration Diagram:

---

I decide design the integration in SAP PI breaking in two times, first time download the list and add via java mapping inside one tag in the XML custom payload generated via java mapping and add those values as string.

The abaper should separate the values using the parameter " ; " for each file, stored and trigger the second time of integration, where a proxy generate will stimulate SAP PI with name of file that should download go for the second API to download the ZIP file.

The second interface is responsable to read the input stream and create the main documento payload as XML and the attachment of ZIP downloaded from the API and response to backend system.

The abap program should recive the data, extract the attachment from the second proxy and open zip file to be processed the details inside the file.

---

![](/legacyfs/online/storage/blog_attachments/2022/10/Diagram.png)

---

## **Clear for you?**

## Let’s rock!

---

## **Integration Development Steps:**

---

I will just high light with the picture and mention the steps of java mapping import.

1. ### **Repository:**

   * **Imported Archives – JavaMapping**

2. ### **Directory:**

   * **ICO Receiver Interface**

   * **ICO Outbound Processing SFTP Channels**

---

## Process steps – Repository:

---

![](/legacyfs/online/storage/blog_attachments/2022/10/Blog.png)

* **Repository: Imported Archives – JavaMapping**

---

## DJSPListResponse java - Outbound - First interface:

---

This first java mapping is responsable in the response of the first API, to push the list of files available, use the inputstream and add inside one XML tag <String>.

From this list the abap program will store, split and many table entry to call the second interface to download the zip files.

```
package com.sap.DJSPLListResponse;

import java.io.InputStream;

import java.io.OutputStream;

import com.sap.aii.mapping.api.AbstractTransformation;

import com.sap.aii.mapping.api.StreamTransformationException;

import com.sap.aii.mapping.api.TransformationInput;

import com.sap.aii.mapping.api.TransformationOutput;

public class DJSPLListResponse extends AbstractTransformation {

	public void transform(TransformationInput transformationInput, TransformationOutput transformationOutput) throws StreamTransformationException

	{

		try {

			//Info message is added to trace.

			getTrace().addInfo("JAVA Mapping Called");

			InputStream inputstream = transformationInput.getInputPayload().getInputStream();

            OutputStream outputstream = transformationOutput.getOutputPayload().getOutputStream();

          //Getting input payload into strInContent.

            byte[] b = new byte[inputstream.available()];

            inputstream.read(b);

            String strInContent = new String(b);

            String tagdiv = strInContent.substring(strInContent.indexOf("<div>") + 5, strInContent.indexOf("</div>")).trim();

            String prefix = "<?xml version=\"1.0\" encoding=\"UTF-8\"?><ns0:MT_Dowjones_SplListResponse xmlns:ns0=\"http://oerlikon.com/Dowjones/IF_0056_SplList\">";

            String suffix = "</ns0:MT_Dowjones_SplListResponse>";

            String xmlPayload= "";

            xmlPayload = prefix + "<SPL><String>" + tagdiv + "</String></SPL>" + suffix;

            outputstream.write(xmlPayload.getBytes());

		}

		catch(Exception exception)

		{

			//If exception occurs it is written to mapping trace.

			getTrace().addDebugMessage(exception.getMessage());

			//stopping the mapping by throwing exception.

			throw new StreamTransformationException(exception.getMessage());

		}

	}

}
```

---

## StreamToZipAttachment java - Inbound - Second interface:

---

This java mapping also you can use the generate a local files in your machine, so a completly generic code that you should adapt for your case but you can test locally before upload in the SAP PI via SAP Netweaver developer studio.

Another point, if you use local, there is no possibility to see the attachment but only the output Main Document payload.

```
package <your_package>;

import java.io.FileInputStream;

import java.io.FileOutputStream;

import java.io.IOException;

import java.io.InputStream;

import java.io.OutputStream;

import java.io.StringReader;
...