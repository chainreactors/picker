---
title: tips and tricks around BAdI IDOC_DATA_MAPPER
url: https://blogs.sap.com/2023/01/10/tips-and-tricks-around-badi-idoc_data_mapper/
source: SAP Blogs
date: 2023-01-11
fetch_date: 2025-10-04T03:31:53.411297
---

# tips and tricks around BAdI IDOC_DATA_MAPPER

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Technology](/t5/technology/ct-p/technology)
* [Technology Blog Posts by Members](/t5/technology-blog-posts-by-members/bg-p/technology-blog-members)
* tips and tricks around BAdI IDOC\_DATA\_MAPPER

Technology Blog Posts by Members

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/technology-blog-members/article-id/160757&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [tips and tricks around BAdI IDOC\_DATA\_MAPPER](/t5/technology-blog-posts-by-members/tips-and-tricks-around-badi-idoc-data-mapper/ba-p/13554232)

![Michael_Keller1](https://avatars.profile.sap.com/9/a/id9aaad6f005486fc219c51d653ce468eabe7e7a07b9448a444e077c8bc88f5ab2_small.jpeg "Michael_Keller1")

![SAP Champion](/html/@B3DACAC6163F980483AC32558EB69695/rank_icons/champion-rank-16x16.svg "SAP Champion")
[Michael\_Keller1](https://community.sap.com/t5/user/viewprofilepage/user-id/4750)

SAP Champion

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=technology-blog-members&message.id=160757)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/technology-blog-members/article-id/160757)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13554232)

‎2023 Jan 10
8:37 PM

[20
Kudos](/t5/kudos/messagepage/board-id/technology-blog-members/message-id/160757/tab/all-users "Click here to see who gave kudos to this post.")

14,462

* SAP Managed Tags
* [ABAP Development](https://community.sap.com/t5/c-khhcw49343/ABAP%2520Development/pd-p/833755570260738661924709785639136)
* [SAP NetWeaver Application Server for ABAP](https://community.sap.com/t5/c-khhcw49343/SAP%2520NetWeaver%2520Application%2520Server%2520for%2520ABAP/pd-p/01200314690800000234)
* [SAP Process Integration](https://community.sap.com/t5/c-khhcw49343/SAP%2520Process%2520Integration/pd-p/01200615320800000719)

* [ABAP Development

  Programming Tool](/t5/c-khhcw49343/ABAP%2BDevelopment/pd-p/833755570260738661924709785639136)
* [SAP NetWeaver Application Server for ABAP

  SAP NetWeaver](/t5/c-khhcw49343/SAP%2BNetWeaver%2BApplication%2BServer%2Bfor%2BABAP/pd-p/01200314690800000234)
* [SAP Process Integration

  SAP NetWeaver](/t5/c-khhcw49343/SAP%2BProcess%2BIntegration/pd-p/01200615320800000719)

View products (3)

Dear Community, [IDoc](https://help.sap.com/docs/SAP_NETWEAVER_AS_ABAP_751_IP/8f3819b0c24149b5959ab31070b64058/4ab074b6aa3a1997e10000000a421937.html?locale=en-US) is the abbreviation for "Intermediate Document", a widley used SAP standard to exchange business data between systems (mostly SAP software based).

With an implementation of the classic Business Add-in (BAdI) IDOC\_DATA\_MAPPER, you can change values in outbound and inbound IDocs via ABAP programming. Here are some tips and tricks around implementing this BAdI.

### Check use of IDoc Conversion Rules first

Before you implement BAdI IDOC\_DATA\_MAPPER, check if the SAP standard of "IDoc Conversion Rules" solves your problem as well (transaction BD62, BD55 and BD79. The major advantage is that you easily configure different mapping rules withouth programming, even with mapping in error cases to one "fallback" value.

### Check whether your BAdI implementation is actually called

Read the discussion in the comments to this blog. An implementation of the BAdI IDOC\_DATA\_MAPPER is apparently only executed when an inbound or outbound IDoc is written. This also excludes execution in transaction BD87. Look for alternative enhancement technologies for such use cases.

### Think about your architecture

Don't write the complete source code to fullfill all your requirements into the BAdI implementation. This has various disadvantages. For example, you cannot proof the BAdI implementation with unit tests. As a proposal, think about different classes with a clear scope ([Separation of Concerns](https://en.wikipedia.org/wiki/Separation_of_concerns)![:disappointed_face:](/html/@51317F7935B06825B21C40F70A87A8E5/emoticons/1f61e.png ":disappointed_face:")

1. Class ZCL\_<..>\_IDOC\_DATA\_MAPPER: For tasks like extracting values from IDoc, calling business logic to map values, publish changed IDoc values and more.

1. Class ZCX\_<..>: Exception class to handle technical IDOC\_DATA\_MAPPER problems.

1. Class ZCL\_<..>\_MAPPING: To fullfill the original business requirements.

1. Class ZCX\_<..>: Exception class to handle business logic (mapping) problems.

### Run only when necessary

Check at least IDOC\_CONTROL-DIRECT and IDOC\_CONTROL-MESTYP if the IDoc actually being processed fits to your implementation. Background is that BAdI IDOC\_DATA\_MAPPER can be implemented multiple times for different scopes. Every implementation is executed when an IDoc is received or sent. So don't interfere with other IDoc processes.

### Get data from IDoc

You find the IDoc data in table IDOC\_DATA - surprise ![:winking_face:](/html/@3DE12A51D4EA9511721B4713FD383281/emoticons/1f609.png ":winking_face:") Read the wanted table line with IDOC\_CONTROL-DOCNUM and SEGNAM. Move the value in SDATA to a corresponding structure of the right data type. Maybe there's some function module that do that step for you but unfortunately I can't remember right now ![:disappointed_face:](/html/@51317F7935B06825B21C40F70A87A8E5/emoticons/1f61e.png ":disappointed_face:")

### Publish your changes

Set CHANGING parameter HAVE\_TO\_CHANGE to 'X' (abap\_true).

Publish your changes via entries in table MAPPING. You get the right SEGNUM value from reading the IDOC\_DATA table.

If you set the SAVE\_TYPE to 'V' you won't see the original unmapped value in IDoc status message.

Always fill structure PROTOCOL-STAMID and PROTOCOL-STAMNO. So you will get your own IDOC status messages instead of a SAP standard message. Please note that if you change an IDoc value there will always be an additional IDoc status message.

### Publish error situation

Surprisingly, set HAVE\_TO\_CHANGE to value 'E' in error situation. This is the indicator for IDoc processing that something went wrong (compare documentation of interface IF\_EX\_IDOC\_DATA\_MAPPER).

### Test with IDocs

Use transaction WE19 to do some IDoc test processing in save environment. If your implementation is active, it will be processed.

### Debug into SAP standard

Set a breakpoint in your BAdI implementation. When using transaction WE19, ABAP debugger will be executed. Now you can debug into the SAP standard that calls your BAdI implementation. That's really helpfull if your changes to the IDoc are not processed as expected.

That's all for now. As a little extra I made a [GitHub repository](https://github.com/Keller-Michael/BAdI_IDOC_DATA_MAPPER_example) with some example code. Not more than a reminder. Please do not forget to add your experiences with this BAdI and IDocs via comments ![:slightly_smiling_face:](/html/@687C2AE1C2A8C4A650D152CC454D53AE/emoticons/1f642.png ":slightly_smiling_face:")

Many thanks for reading and stay healthy

Michael

* [badi](/t5/tag/badi/tg-p/board-id/technology-blog-members)
* [idoc](/t5/tag/idoc/tg-p/board-id/technology-blog-members)
* [idoc\_data\_mapper](/t5/tag/idoc_data_mapper/tg-p/board-id/technology-blog-members)
* [inbound](/t5/tag/inbound/tg-p/board-id/technology-blog-members)
* [mapping](/t5/tag/mapping/tg-p/board-id/technology-blog-members)
* [outbound](/t5/tag/outbound/tg-p/board-id/technology-blog-mem...