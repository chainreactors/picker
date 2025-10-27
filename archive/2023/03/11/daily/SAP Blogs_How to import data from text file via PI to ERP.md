---
title: How to import data from text file via PI to ERP
url: https://blogs.sap.com/2023/03/10/how-to-import-data-from-text-file-via-pi-to-erp/
source: SAP Blogs
date: 2023-03-11
fetch_date: 2025-10-04T09:15:59.895001
---

# How to import data from text file via PI to ERP

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Technology](/t5/technology/ct-p/technology)
* [Technology Blog Posts by Members](/t5/technology-blog-posts-by-members/bg-p/technology-blog-members)
* How to import data from text file via PI to ERP

Technology Blog Posts by Members

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/technology-blog-members/article-id/163004&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [How to import data from text file via PI to ERP](/t5/technology-blog-posts-by-members/how-to-import-data-from-text-file-via-pi-to-erp/ba-p/13566995)

![stradav](https://avatars.profile.sap.com/c/0/idc0eb8579600b8ea55d9335566a22a443ea65c97fbd9fb26915aee1ba245eb253_small.jpeg "stradav")

[stradav](https://community.sap.com/t5/user/viewprofilepage/user-id/127710)

Explorer

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=technology-blog-members&message.id=163004)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/technology-blog-members/article-id/163004)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13566995)

‎2023 Mar 10
8:34 PM

[1
Kudo](/t5/kudos/messagepage/board-id/technology-blog-members/message-id/163004/tab/all-users "Click here to see who gave kudos to this post.")

2,035

* SAP Managed Tags
* [SAP Process Integration](https://community.sap.com/t5/c-khhcw49343/SAP%2520Process%2520Integration/pd-p/01200615320800000719)

* [SAP Process Integration

  SAP NetWeaver](/t5/c-khhcw49343/SAP%2BProcess%2BIntegration/pd-p/01200615320800000719)

View products (1)

# Summary

Our initial situation is as follows: we do have text files with comma separated values which we want to import to our ERP system, automatically. This files are on a SFTP-server. So our PI-system should look every now and then if new files are available on the SFTP-server. If so, gonna catch them all and send them to our ERP system. One file can contain one to many entries, which should send to our ERP system in one call.

![](/legacyfs/online/storage/blog_attachments/2023/03/iFlow.png)

iFlow

# Precondition

To start over, we do need a PI-system (surprise!), in our case a SAP Netweaver Process Integration 7.50, a working ESR connection to our SAP ERP-system to configure the SPROXY and a SFTP-server we can use for testing the scenario.

# Let's Start

Let's start with a close look to our data file, and the data types we want to import.

```
1;Aragorn;Gondor

2;Boromir;Gondor

3;Galadriel;Valinor

4;Samweis;Hobbington
```

Our file has four entries and every entry consists of Id, name and lands. Quite simple so far. So let's start over and create the corresponding data-types. We define three data types, a DataEntry which represents one singe line of our data file, a DataList and a DataListExternal. DataListExternal is the data type we get from our data file from the SFTP-server, DataList is the data type we send to our ERP-system. We have two data types for the same thing, because they could potentially differ, if we do some message mapping and so on.

![](/legacyfs/online/storage/blog_attachments/2023/03/dt_dataentry.png)

DataEntry

![](/legacyfs/online/storage/blog_attachments/2023/03/dt_datalist.png)

DataList

![](/legacyfs/online/storage/blog_attachments/2023/03/dt_datalistexternal.png)

And because adding objects to our scenario is so much fun. We additionally create some Message Types. As you can see, XML namespace is empty. This is with full intention and conviction, because it caused some trouble with the message mapping later.

![](/legacyfs/online/storage/blog_attachments/2023/03/messagetypes-1.png)

Message Types

And of course we also need Service Interfaces. So let's go ahead and create some. And keep in mind, as always, we need one for inbound and one for outbound communication.

![](/legacyfs/online/storage/blog_attachments/2023/03/SI_ImportData.png)

Service Interface Inbound

![](/legacyfs/online/storage/blog_attachments/2023/03/SI_ImportData_Operation.png)

Service Interface Operation Inbound

![](/legacyfs/online/storage/blog_attachments/2023/03/SI_ImportDataExternal.png)

Service Interface Outbound

![](/legacyfs/online/storage/blog_attachments/2023/03/SI_ImportDataExternal_Operation.png)

Service Interface Operation Outbound

And just for completion we also add a simple Message Mapping and a Operational Mapping. We map our source DataListExternal to the target DataList.

![](/legacyfs/online/storage/blog_attachments/2023/03/MM_DataListExternalToDataList.png)

Message Mapping

![](/legacyfs/online/storage/blog_attachments/2023/03/MM_Definition.png)

Message Mapping Definition

![](/legacyfs/online/storage/blog_attachments/2023/03/OM_DataListExternalToDataList.png)

Operation Mapping ![](/legacyfs/online/storage/blog_attachments/2023/03/OM_Definition.png)

Operation Mapping Definition

At the end of the day, our namespace looks like this and is full of happy little design objects.

![](/legacyfs/online/storage/blog_attachments/2023/03/design_objects.png)

Now we do have all the necessary objects in our Enterprise Service Browser. We can now switch to our SAP ERP system and call transaction SPROXY. At Source -> ESR -> SWCs we find our namespace and the freshly created objects. With a right mouse click on our Service Interface SI\_ImportData, we can generate the Proxy Interface and the Implementing Class, which holds the method which is called when the PI system is sending data to the ERP system.

![](/legacyfs/online/storage/blog_attachments/2023/03/sproxy.png)

SPROXY

![](/legacyfs/online/storage/blog_attachments/2023/03/proxy_interface.png)

Proxy

![](/legacyfs/online/storage/blog_attachments/2023/03/class_method.png)

Class Method

We are almost there. So now we need a Communication Channel, a receiver adapter for sending messages to our ERP system. We use a SOAP adapter for sending HTTP messages.

![](/legacyfs/online/storage/blog_attachments/2023/03/cc_proxy_receiver.png)

Communication Channel Proxy Receiver

![](/legacyfs/online/storage/blog_attachments/2023/03/cc_proxy_receiver_general.png)

Communication Channel Proxy Receiver

And not to forget, we need a Communication Channel to fetch the data files from the SFTP-server. We use a SFTP adapter for this. But there is more. This little adapter has to do some serious magic to provide the right data for the subsequent processes. At first we create a Communication Channel called CC\_SFTP\_Sender and fill in all the stuff this little fellow needs for communication, like the server address, port, username, fingerprint and so on. We have to specify a filename and a directory. This is the place and file the adapter is looking for when connecting to the SFTP server. We can specify whether the file has to be deleted after processing or not and we can choose a polling interval. For testing purposes we set the polling interval to a few seconds, because time is money.

![](/legacyfs/online/storage/blog_attachments/2023/03/CC_SFTP_Sender.png)

Communication Channel SFTP Sender

![](/legacyfs/online/storage/blog_attachments/2023/03/CC_SFTP_Sender_settings.png)

Communication Channel SFTP Settings

Now this is the part where the magic happens. For the subsequent processing we do need a XML file. So we have to convert our comma separated data file to XML. For this task we can use the MessageTransformBean, which we can call as...