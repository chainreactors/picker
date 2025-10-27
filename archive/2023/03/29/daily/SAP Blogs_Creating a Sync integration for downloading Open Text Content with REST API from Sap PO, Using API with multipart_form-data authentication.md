---
title: Creating a Sync integration for downloading Open Text Content with REST API from Sap PO, Using API with multipart/form-data authentication
url: https://blogs.sap.com/2023/03/28/creating-a-sync-integration-for-downloading-open-text-content-with-rest-api-from-sap-po-using-api-with-multipart-form-data-authentication/
source: SAP Blogs
date: 2023-03-29
fetch_date: 2025-10-04T11:01:01.315245
---

# Creating a Sync integration for downloading Open Text Content with REST API from Sap PO, Using API with multipart/form-data authentication

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Technology](/t5/technology/ct-p/technology)
* [Technology Blog Posts by Members](/t5/technology-blog-posts-by-members/bg-p/technology-blog-members)
* Creating a Sync integration for downloading Open T...

Technology Blog Posts by Members

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/technology-blog-members/article-id/159757&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [Creating a Sync integration for downloading Open Text Content with REST API from Sap PO, Using API with multipart/form-data authentication](/t5/technology-blog-posts-by-members/creating-a-sync-integration-for-downloading-open-text-content-with-rest-api/ba-p/13548004)

![anoop-jose](https://avatars.profile.sap.com/3/a/id3a9cf2190cbfeee8b87d2c1208a2aae31ec84c2334b5fa25ead6eadb12021ab8_small.jpeg "anoop-jose")

[anoop-jose](https://community.sap.com/t5/user/viewprofilepage/user-id/45780)

Participant

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=technology-blog-members&message.id=159757)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/technology-blog-members/article-id/159757)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13548004)

‎2023 Mar 28
10:57 PM

[1
Kudo](/t5/kudos/messagepage/board-id/technology-blog-members/message-id/159757/tab/all-users "Click here to see who gave kudos to this post.")

3,437

* SAP Managed Tags
* [SAP Process Orchestration](https://community.sap.com/t5/c-khhcw49343/SAP%2520Process%2520Orchestration/pd-p/477916618626075516391832082074785)

* [SAP Process Orchestration

  Software Product](/t5/c-khhcw49343/SAP%2BProcess%2BOrchestration/pd-p/477916618626075516391832082074785)

View products (1)

### **Introduction**:

The purpose of this document is to develop a synchronous interface to download content from Open Text Content Server (OTCS) using REST API. I have tried to cover the overall design with code snippets for reference.

### **Scope**:

* Rest OTCS authentication using Content-Type: multipart/form-data (Credentials as a header of the multipart body) for the token (otcsticket) generation.

* Parameterized Mapping for accessing the OTCS credentials from ICO.

* Calling OTCS authentication lookup, accessing parameters from java mapping.

* Creating DynamicConfigurationKey for rest channel Parameter from java mapping.

* *OTCS session token management is out of scope.*

### **Overall Design**:

![](/legacyfs/online/storage/blog_attachments/2023/03/PO-OTCS-Digrm.jpg)

Sync Interface to get the Document from OpenText via PO 7.5

### **Solution Flow**:

1. SAP ECC calls a proxy to send the Document ID of the document in OTCS.

2. PO Request java mapping receives Document ID.

   1. Calls OTCS - *Authentication* API for a token (otcsticket) via REST lookup

   2. Post ID and token to OTCS - *Content* API

3. PO Response Java Mapping receives Document as an inputstream and maps it to the content field.

4. Base64 content Field is sent to SAP for further processing.

### **Rest API consumed from Open Text Content Server (OTCS):**

* **Authentication API - /otcs/cs.exe/api/v1/auth:** API needs to be called with credentials in Content-Type: multipart/form-data section to generate a token, which is called otcsticket. Otcsticket needs to be present in the header for *content* API to be called.![](/legacyfs/online/storage/blog_attachments/2023/03/AuthAPI-2.jpg)In Content-Type: multipart/form-data, credentials need to be present, separated by a boundary.

* **Content API - /otcs/cs.exe/api/v1/nodes/{ID}/content:** API would return the document as a byte stream, when called with the token and ID of the document in the header.![](/legacyfs/online/storage/blog_attachments/2023/03/GetDocAPI.jpg)otcsticket and ID of the document in the http header

### **PO Objects and code snippets**:

**Data Structure**

Document ID for OTCS comes as DataID from SAP. The document is returned to SAP as Content.![](/legacyfs/online/storage/blog_attachments/2023/03/REQ-RES-DS.jpg)

**ICO**![](/legacyfs/online/storage/blog_attachments/2023/03/ICO-1.jpg)

**Mapping (MM) & Operational mapping (OM)**

Please take care of the above ICO parameter in

* OM-> Parameters section and Request Mapping Binding section

* MM -> Signature tab

Request Mapping with java mapping in the Attributes and Methods Section![](/legacyfs/online/storage/blog_attachments/2023/03/MM-Req-1.jpg)

```
public void transform(TransformationInput in, TransformationOutput out) throws StreamTransformationException {

		try {

			getTrace().addDebugMessage("***OTCS-Request-JavaMapping-Start");

			//Get the mapping parameter from ICO

			String paramChannel = in.getInputParameters().getString("lookupChannel");

			String paramUserName = in.getInputParameters().getString("username");

			String paramPassword = in.getInputParameters().getString("password");

			String paramBoundary = in.getInputParameters().getString("boundary");

			getTrace().addDebugMessage("***OTCS-Step1-LogPramFromICO-lookupChannel:" + paramChannel + "-username:"

				+ paramUserName + "-password:" + paramPassword +"-boundary:" +  paramBoundary);

			//Creating multipart/form-data for OTCS authentication

			String LINE_FEED = "\r\n";

			String ContentDisposition = "Content-Disposition: form-data; name=\"";

			String authReqFormData ="";

			authReqFormData =  LINE_FEED + paramBoundary + LINE_FEED + ContentDisposition + "username\"" + LINE_FEED

				+ LINE_FEED + paramUserName + LINE_FEED + paramBoundary +  LINE_FEED +ContentDisposition

				+ "password\"" + LINE_FEED + LINE_FEED + paramPassword + LINE_FEED + paramBoundary + "–-" + LINE_FEED;

			getTrace().addDebugMessage("***OTCS-Step2-multipart/form-data:" + authReqFormData);

			//Read message header value for Receiver

			String paramReceiver = in.getInputHeader().getReceiverService();

			getTrace().addDebugMessage("***OTCS-Step3-ReceiverService:" + paramReceiver);

			//Get the OTCS rest lookup Channel Object for authentication

			Channel lookup_channel = LookupService.getChannel(paramReceiver, paramChannel);

			//Call rest lookup channel, with multipart/form-data payload

			SystemAccessor accessor = null;

			accessor = LookupService.getSystemAccessor(lookup_channel);

			InputStream authInputStream = new ByteArrayInputStream(authReqFormData.getBytes("UTF-8"));

			Payload authPayload = LookupService.getXmlPayload(authInputStream);

			Payload tokenOutPayload = null;

			//Call lookup

			getTrace().addDebugMessage("***OTCS-Step4-CallLookupChannel");

			tokenOutPayload = accessor.call(authPayload);

			//Parse for Lookup response for token

			InputStream authOutputStream = tokenOutPayload.getContent();

			DocumentBuilderFactory authfactory = DocumentBuilderFactory.newInstance();

			DocumentBuilder authbuilder = authfactory.newDocumentBuilder();

			Document authdocument = authbuilder.parse(authOutputStream);

			NodeList nlticket = authdocument.getElementsByTagName("ticket");

			String tokenTicket = "Empty";

			Node node = nlticket.item(0);

			if (node != null){

				node = node.getFirstChild();

				if (node != null){

					tokenTicket = node.getNodeValue();

				}

			}

			getTrace().addDebugMessage("***OTCS-Step5-TokenFromLookup:" + tokenTicket);

			//Parse input stream and get DataID from SAP

			DocumentBuilderFactory dbFactory = DocumentBui...