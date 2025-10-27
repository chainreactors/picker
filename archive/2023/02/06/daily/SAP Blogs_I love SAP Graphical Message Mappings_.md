---
title: I love SAP Graphical Message Mappings?
url: https://blogs.sap.com/2023/02/05/i-love-sap-graphical-message-mappings/
source: SAP Blogs
date: 2023-02-06
fetch_date: 2025-10-04T05:47:32.096507
---

# I love SAP Graphical Message Mappings?

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Technology](/t5/technology/ct-p/technology)
* [Technology Blog Posts by Members](/t5/technology-blog-posts-by-members/bg-p/technology-blog-members)
* I love SAP Graphical Message Mappings?

Technology Blog Posts by Members

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/technology-blog-members/article-id/161195&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [I love SAP Graphical Message Mappings?](/t5/technology-blog-posts-by-members/i-love-sap-graphical-message-mappings/ba-p/13556837)

![BrunoKon](https://avatars.profile.sap.com/f/8/idf87e6fdb46f5f07a43cec5bae59ba842b57ce318067eb13dbdac535c2e0a9fad_small.jpeg "BrunoKon")

[BrunoKon](https://community.sap.com/t5/user/viewprofilepage/user-id/45002)

Explorer

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=technology-blog-members&message.id=161195)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/technology-blog-members/article-id/161195)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13556837)

‎2023 Feb 05
9:14 AM

[1
Kudo](/t5/kudos/messagepage/board-id/technology-blog-members/message-id/161195/tab/all-users "Click here to see who gave kudos to this post.")

3,167

* SAP Managed Tags
* [SAP Process Integration](https://community.sap.com/t5/c-khhcw49343/SAP%2520Process%2520Integration/pd-p/01200615320800000719)
* [SAP Process Orchestration](https://community.sap.com/t5/c-khhcw49343/SAP%2520Process%2520Orchestration/pd-p/477916618626075516391832082074785)

* [SAP Process Integration

  SAP NetWeaver](/t5/c-khhcw49343/SAP%2BProcess%2BIntegration/pd-p/01200615320800000719)
* [SAP Process Orchestration

  Software Product](/t5/c-khhcw49343/SAP%2BProcess%2BOrchestration/pd-p/477916618626075516391832082074785)

View products (2)

![](/legacyfs/online/storage/blog_attachments/2023/01/Graphical-Message-Mapping-1.jpg)

Message Mapping rule for target message field D\_1154

One constant throughout all of SAP's successful integration journey from XI to PI, and then to PO, has been their ***Graphical Message Mapping Editor***.

I'm not sure everyone loves their Graphical Message Mappings - but like it or not, it has also made the leap to the cloud as well. As 7a519509aed84a2c9e6f627841825b5a points out in his blog *"**[Cloud Integration mapping: Your options explained and compared](https://blogs.sap.com/2018/06/18/cloud-integration-mapping-your-options-explained-and-compared/)**"*

* it allows you to "drag and drop" source fields to target fields

* it does not require any coding (well ... we will get to that)

* it comes available with lots of built functions

* and you can build your own functions as well (ok ... there is some coding)

The great advantage of the Message Mapping Editor is it's ease of use, and it's graphical nature, and my 'gut feel' tells me it is used in something like 80% of all PI/PO mappings. But you need to be careful - as soon as the requirements get somewhat complicated, you end up with a message mapping that is really really ugly, and ***difficult to understand, support and maintain***. And that is where Java and XSLT (and now Groovy and JavaScript) really get to shine.

Even with the ≈ 80% of mappings that the graphical mapping editor is suitable for, it is still sometimes difficult to understand how the mapping works, without a certain level of technical expertise. Just try to make sense of the mapping rule for target message field **D\_1154** from the image above.

SAP have not offered any sort of message mapping documentation solution, and so there is a great dependency on SAP PI/PO, and now SAP CI technical experts (especially now where there is a lot of activity to migrate away from PI/PO and to potentially redesign interfaces). There are some basic methods available to extract the information, and load it into Excel, where comparison of the mappings is also possible - but it's not ideal.

### SAP PI/PO Message Mapping Documentation

There is a better solution - we've created a ***Message Mapping Documentation*** feature that enables the easy review of message mappings. Non-technical people can now make some sense of message mappings, and SAP PI/PO and SAP CI technical experts do not need to waste their time creating documentation (I know I hated doing this years ago).

The message mapping rule for target message field **D\_1154** shown above is transcribed into the following documentation - which is clearly much ***easier to understand***.

![](/legacyfs/online/storage/blog_attachments/2023/01/UDO-mapping-rule-1.jpg)

Message Mapping rule for target message field D\_1154

The overall message mapping documentation created includes the meta data, information about Function Libraries, and also any local UDF code. Elements, such as standard SAP functions and function calls, are colour-coded to improve readability.

![](/legacyfs/online/storage/blog_attachments/2023/01/UDO-mapping-documentation.jpg)

Message Mapping Documentation

### SAP PI/PO Message Mapping Comparison

Some years later we built on the Message Mapping Documentation with a ***Message Mapping Comparison*** feature, to enable the quick determination of differences in message mappings - even across different PI/PO systems.

Comparing two message mappings is simple and clear, with any differences highlighted in yellow.

![](/legacyfs/online/storage/blog_attachments/2023/01/UDO-Message-Mapping-Comparison.jpg)

Message Mapping Comparison

### SAP PI/PO Message Mapping Similarity Analysis

And, in 2022, we developed the unique ***Message Mapping Similarity Analysis***, so you can easily compare all your message mappings against all your other message mappings - to identify your message mappings that are say, "***90% or more similar***" (similarity % is configurable, from 50% to 100%).

The result of the analysis is shown in a window like the one below - by selecting the primary mapping on the left you can see all of its similar mappings on the right. And from here you can easily determine exactly how the mappings differ by clicking on '**Compare'**.

![](/legacyfs/online/storage/blog_attachments/2023/01/UDO-Similarity-Analysis.jpg)

Message Mapping Similarity Analysis

### Conclusion

We hope this has opened up your eyes about what is possible when working with SAP Graphical Message Mappings.

Understanding how your Message mappings are working is important. In the absence of clear documentation, support and maintenance will be more problematic. And a migration away from SAP PI/PO will also benefit from improved transparency.

Let me know if you have any feedback or questions, and I will respond as soon as I can.

### Finding out more

These mapping features are just a small part of our ***UDO for SAP PI/PO*** software, which is easily installed and configured on your client - you can be reviewing your interfaces and mappings in as little as 20 mins.

If you're interested in finding out more you can find us at our Arianim page on the [SAP Store](https://store.sap.com/dcp/en/product/display-0000060320_live_v1/UDO%2520for%2520SAP%2520PI%252FPO). If you like, we can give you a short demo and an evaluation version - you can then try it out in your own environment, on your own PI/PO mappings.

The content in this post is based on our Arianim blog "[*Does anyone love their SAP Graphical Message ...