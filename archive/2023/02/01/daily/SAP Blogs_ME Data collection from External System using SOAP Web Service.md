---
title: ME Data collection from External System using SOAP Web Service
url: https://blogs.sap.com/2023/01/31/me-data-collection-from-external-system-using-soap-web-service/
source: SAP Blogs
date: 2023-02-01
fetch_date: 2025-10-04T05:20:12.432150
---

# ME Data collection from External System using SOAP Web Service

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Product Lifecycle Management](/t5/product-lifecycle-management/ct-p/plm)
* [PLM Blog Posts by Members](/t5/product-lifecycle-management-blog-posts-by-members/bg-p/plm-blog-members)
* ME Data collection from External System using SOAP...

Product Lifecycle Management Blog Posts by Members

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/plm-blog-members/article-id/1445&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [ME Data collection from External System using SOAP Web Service](/t5/product-lifecycle-management-blog-posts-by-members/me-data-collection-from-external-system-using-soap-web-service/ba-p/13555664)

![Venkatesan1997](https://avatars.profile.sap.com/6/b/id6b0debec8cb62f04d116e1001d4620925ab595f6c6b635e45baedf9979215564_small.jpeg "Venkatesan1997")

[Venkatesan1997](https://community.sap.com/t5/user/viewprofilepage/user-id/121365)

Explorer

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=plm-blog-members&message.id=1445)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/plm-blog-members/article-id/1445)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13555664)

‎2023 Jan 31
3:57 PM

[11
Kudos](/t5/kudos/messagepage/board-id/plm-blog-members/message-id/1445/tab/all-users "Click here to see who gave kudos to this post.")

2,211

* SAP Managed Tags
* [SAP Manufacturing Execution](https://community.sap.com/t5/c-khhcw49343/SAP%2520Manufacturing%2520Execution/pd-p/01200615320800000731)
* [SAP Manufacturing Integration and Intelligence](https://community.sap.com/t5/c-khhcw49343/SAP%2520Manufacturing%2520Integration%2520and%2520Intelligence/pd-p/01200314690800000151)

* [SAP Manufacturing Execution

  SAP Digital Manufacturing](/t5/c-khhcw49343/SAP%2BManufacturing%2BExecution/pd-p/01200615320800000731)
* [SAP Manufacturing Integration and Intelligence

  SAP Digital Manufacturing](/t5/c-khhcw49343/SAP%2BManufacturing%2BIntegration%2Band%2BIntelligence/pd-p/01200314690800000151)

View products (2)

### **Hello Everyone,**

SAP ME (Manufacturing Execution) and MII (Manufacturing Integration and Intelligence) are niche tools given by SAP to connect shop floor systems like PLCs, / SCADA / Historians / Third-party systems to ERP (SAP ECC / SAP S/4 HANA).

Here, in this article, I am describing the steps involved in connecting such a third-party shop floor system with SAP MII using SOAP Web service methods instead of the traditional OPC integration methods.

### **Prerequisites:**

1. ME data collection parameters setup completed as required

2. To make the Web service call, create a ME/MII UME service user.

### **High-Level Overview:**

1. Expose the MII BLS transaction as a WSDL service to send Machine parameter values.

2. Create a Custom workflow.

3. Built BLS transaction to receive Machine values and record them in ME data collection.

#### **1.** **MII BLS transaction as WSDL service**

* Developed a BLS transaction in the MII workbench with an input XML parameter.

* XML structure should be enveloped by the message name and enlist required parameter names as nodes containing respective values, as shown below.

  ```
  <Message_Name>

  <Param_Name1>Value</Param_Name1>

  :

  </Message_Name>
  ```

* Validate and assign the input XML parameter to the Message Enqueuer action block to call the Custom Workflow configurations.

* Provide the MII WSDL URL for the third-party system to call and pass external system Machine parameter values.![](/legacyfs/online/storage/blog_attachments/2023/01/image-16-1.png)

#### **2.   Create a Custom Workflow**

* Create a Custom workflow for Message type processing, as shown below.

* Message name should start with Z to identify as Custom Workflow.

* Map a new MII BLS transaction as a service transaction to receive the input XML and proceed further.![](/legacyfs/online/storage/blog_attachments/2023/01/image-18-1.png)

**Note:** Using a custom MII Workflow Configuration, the triggered messages can be traced for any failure and can be re-run from the SAP MII Queue monitor.

#### **3.** **BLS Service transaction to receive and record ME data collection values.**

* Within the mapped MII BLS service transaction, repeat through the XML nodes to validate the required conditions for the DC data type and value received.![](/legacyfs/online/storage/blog_attachments/2023/01/image-17-2.png)

* Then call the PAPI (logDCGroup) to initiate the ME Data collection. Catch and handle any exceptions thrown from PAPI as needed.

Frame the MII BLS transaction WSDL path with parameter name(s) for the Third-party system developer to call and pass the ME Data collection parameters & values.

### **Syntax options:**

1. For SOAP Webservice call, MII WSDLGen shall be used as shown below after assigning proper reference documents,

[http://<Hostname>:<Port>/XMII/WSDLGen/<TransactionPath>?wsdl](http://<Hostname>:<Port>/XMII/WSDLGen/%3CTransactionPath%3E?wsdl)

2. Or you can encapsulate the MII transaction into a XACUTE query to have session parameters properly binded and expose the web service call URL as below,

<http://<Hostname>:<Port>/XMII/Illuminator?QueryTemplate=<XacutePath>&<InputParams>>

3. Directly use the Runner based URL to call the transaction,

<http://<Hostname>:<Port>/XMII/Runner?Transaction=<TransactionPath>&<InputParam>=<<InputXML>>>

### **Conclusion & Merits:**

Usually, for shop floor integration scenarios, where Machine data is captured from PLC / SCADA / Other Third-party systems, MII will use PCo (Plant Connectivity) based OPC or ODBC connections to drive the interface.

In cases like this where a Third-party system doesn’t expose data through OPC or ODBC frameworks but can call a simple web service to pass data over for further SAP processing above demonstrated the interface works seamlessly.

This also eliminates an additional integration point/software i.e., PCo which needs to be maintained.

I believe, this article will help you how to set up the Machine Integration and use the MII transactions to improve the application development in SAP MII. I encourage you to post your comment and I will try to answer them as soon as possible. Please follow me for more useful content.

* [custom workflow](/t5/tag/custom%20workflow/tg-p/board-id/plm-blog-members)
* [data collection](/t5/tag/data%20collection/tg-p/board-id/plm-blog-members)
* [Machine Integration](/t5/tag/Machine%20Integration/tg-p/board-id/plm-blog-members)
* [plant connectivity](/t5/tag/plant%20connectivity/tg-p/board-id/plm-blog-members)
* [sap manufacturing execution](/t5/tag/sap%20manufacturing%20execution/tg-p/board-id/plm-blog-members)
* [sap manufacturing integration and intelligence](/t5/tag/sap%20manufacturing%20integration%20and%20intelligence/tg-p/board-id/plm-blog-members)
* [wsdl](/t5/tag/wsdl/tg-p/board-id/plm-blog-members)

3 Comments

You must be a registered user to add a comment. If you've already registered, sign in. Otherwise, register and sign in.

* [Comment](/plugins/common/feature/oidcss/sso_login_redirect/providerid/sap_ids_prompt?redirectreason=permissiondenied&referer=https%3A%2F%2Fcommunity.sap.com%2Ft5%2Fproduct-lifecycle-management-blog-posts-by-members%2Fme-data-collection-from-external-system-using-soap-web-service%2Fba-p%2F13555664%23comment-on-this)

Copy Link
![](https://community.sap.com/html/@E...