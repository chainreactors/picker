---
title: SAP PO B2B Add-On NRO (Number Range Object) Usage
url: https://blogs.sap.com/2023/01/06/sap-po-b2b-add-on-nro-number-range-object-usage/
source: SAP Blogs
date: 2023-01-07
fetch_date: 2025-10-04T03:15:20.856843
---

# SAP PO B2B Add-On NRO (Number Range Object) Usage

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Technology](/t5/technology/ct-p/technology)
* [Technology Blog Posts by Members](/t5/technology-blog-posts-by-members/bg-p/technology-blog-members)
* SAP PO B2B Add-On NRO (Number Range Object) Usage

Technology Blog Posts by Members

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/technology-blog-members/article-id/162116&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [SAP PO B2B Add-On NRO (Number Range Object) Usage](/t5/technology-blog-posts-by-members/sap-po-b2b-add-on-nro-number-range-object-usage/ba-p/13561382)

![amysh95](https://avatars.profile.sap.com/e/6/ide639a5e31c1a136c38d79395de21b27a8b83271e1383989ddfaaa0591c2460f9_small.jpeg "amysh95")

[amysh95](https://community.sap.com/t5/user/viewprofilepage/user-id/603339)

Participant

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=technology-blog-members&message.id=162116)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/technology-blog-members/article-id/162116)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13561382)

‎2023 Jan 06
5:50 PM

[1
Kudo](/t5/kudos/messagepage/board-id/technology-blog-members/message-id/162116/tab/all-users "Click here to see who gave kudos to this post.")

4,552

* SAP Managed Tags
* [SAP Process Integration](https://community.sap.com/t5/c-khhcw49343/SAP%2520Process%2520Integration/pd-p/01200615320800000719)
* [SAP Process Integration, business-to-business add-on](https://community.sap.com/t5/c-khhcw49343/SAP%2520Process%2520Integration%252C%2520business-to-business%2520add-on/pd-p/67837800100800004898)
* [SAP Process Orchestration](https://community.sap.com/t5/c-khhcw49343/SAP%2520Process%2520Orchestration/pd-p/477916618626075516391832082074785)

* [SAP Process Integration

  SAP NetWeaver](/t5/c-khhcw49343/SAP%2BProcess%2BIntegration/pd-p/01200615320800000719)
* [SAP Process Integration, business-to-business add-on

  SAP NetWeaver](/t5/c-khhcw49343/SAP%2BProcess%2BIntegration%25252C%2Bbusiness-to-business%2Badd-on/pd-p/67837800100800004898)
* [SAP Process Orchestration

  Software Product](/t5/c-khhcw49343/SAP%2BProcess%2BOrchestration/pd-p/477916618626075516391832082074785)

View products (3)

B2BIC NRO is generally used in EDI scenarios where the requirement is to send document numbers to customers in series which is not possible in the case of IDocs because IDocs are not created in sequence per customer.

Generally in B2B transactions, the flow is most likely IDoc to EDI via AS2/SFTP, etc. Where customers want the document number in series or shall I say in the order. This is not possible when sending the IDoc number as a document number.

In middleware (SAP PI/PO) we have NRO in b2bic which can be used to fulfill this requirement.

To set up the NRO in the system B2B Add-on needs to be installed on the PO server. I am assuming it is already installed on the server and the following steps need to perform to use range objects.

Go to B2B Integration cockpit by calling the below URL in the browser.

<http://<host><port>/b2bic>

![](/legacyfs/online/storage/blog_attachments/2023/01/B2B-Cockpit-1.png)

B2B Integration Cockpit Home Page

Click on NRO Maintenance then click on **Create** to-create Number range objects.

![](/legacyfs/online/storage/blog_attachments/2023/01/Create-range-object.png)

Create range objects

Below are the fields which need to be filled to me the NRO active.

|
 **Number range object name** |
 /B2B/<PARTNER\_NAME\_OBJ> |

|
 **Description** |
 Provide the description |

|
 **Minimum value** |
 Starting range of the document number for partner |

|
 **Maximum value** |
 Last range of the document number for the partner |

|
 **Formatted Value Length** |
 Same as format by number in graphical mapping just give how many leading 0’s need to be format |

|
 **Warn Level (%)** |
 Specify warning level in percentage in case the number range is about to reach its maximum |

|
 **Rotate** |
 Checked in case if number range is on its maximum value it will start from its minimum value again |

***Note:** when rotate is checked Warn Level will no longer be in operation because there is no significance in giving a warning on reaching NRO to its maximum range.*

![](/legacyfs/online/storage/blog_attachments/2023/01/create-rnage.png)

create range object

***Suggestion:** Whenever creating an NRO try to give the name of the partner in the name section and use value mapping/Fix Value to get this name. This will be helpful when you have a single common mapping in your PO landscape for all the customers. You can use these Objects in all the Outgoing EDI Messages as per the requirements.*

Once you create an object it will start reflecting some more fields which are also editable only after object creation. Here in case, a range object is created for an existing interface or partner you can edit the last document number for the partner which sent last.

![](/legacyfs/online/storage/blog_attachments/2023/01/edi-range-object.png)

EDI range objects

To use this NRO in mapping you need to use one constant and enter the following character sequence.

$B2B\_UEBNR***<Number\_Range\_Object\_Name>***$B2B\_END\_UEBNR

This will provide you the next number of a range object, in the same way, if you need to get the last/previous number of the range object you can write the following character sequence in the mapping with a constant.

$B2B\_UEBNR\_BEFORE**<*Number\_Range\_Object\_Name* >**$B2B\_END\_UEBNR

Example: In your NRO you have provided the name of your object as PARTNERDOCNUM

Then in Message mapping how it should be configured.

![](/legacyfs/online/storage/blog_attachments/2023/01/range-object-in-Message-mapping-1.png)

range object in message mapping

Also as per the design, it can be changed by fetching from ID by using value mapping or with Fix value depending freely on the design.

***Note:*** *This will not work if you are trying to test your MM/OM in a local run (ESR). This will be operational only in the end-to-end scenarios.*

To get the range objects values one module needs to be configured in the receiver channel

**Module name:** localejbs/TransmissionNumberModule

This module has several parameters that can be used as per the requirement:

|
 multipleNumbersPerMessage |
 If you want to insert multiple continuous numbers in a message, then use this parameter. |

|
 useLocalLock |
 If you want to acquire a lock on the individual NRO that is being used instead of a global lock, then use this parameter. Its default value is true. |

|
 sourceEncoding |
 Defines the encoding of the input message. If not specified the default value is ISO-8859-15. |

|
 destinationEncoding |
 Defines the encoding of the output file. If not specified the default value is ISO-8859-15. |

![](/legacyfs/online/storage/blog_attachments/2023/01/range-object-module-configuration-1.png)

range object module configuration

Once you run the scenario end-to-end this module will write the actual range number in place of your constant which you have written in message mapping.

***Note:** If you are verifying the range number value in the message monitor it will not be there you will see only the constant value in the payload. Because the module is not yet called in the message transformation it will call only when the payload is transferred to th...