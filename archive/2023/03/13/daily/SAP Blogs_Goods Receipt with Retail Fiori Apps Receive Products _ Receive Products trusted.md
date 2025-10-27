---
title: Goods Receipt with Retail Fiori Apps Receive Products / Receive Products trusted
url: https://blogs.sap.com/2023/03/12/goods-receipt-with-retail-fiori-apps-receive-products-receive-products-trusted/
source: SAP Blogs
date: 2023-03-13
fetch_date: 2025-10-04T09:25:17.550790
---

# Goods Receipt with Retail Fiori Apps Receive Products / Receive Products trusted

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Technology](/t5/technology/ct-p/technology)
* [Technology Blog Posts by Members](/t5/technology-blog-posts-by-members/bg-p/technology-blog-members)
* Goods Receipt with Retail Fiori Apps Receive Produ...

Technology Blog Posts by Members

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/technology-blog-members/article-id/162566&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [Goods Receipt with Retail Fiori Apps Receive Products / Receive Products trusted](/t5/technology-blog-posts-by-members/goods-receipt-with-retail-fiori-apps-receive-products-receive-products/ba-p/13564454)

![bop937](https://avatars.profile.sap.com/6/2/id6259410b3aa6752c16eaa16c7c485ae67df23cb7fd56cf4b1b4216f6082f347f_small.jpeg "bop937")

[bop937](https://community.sap.com/t5/user/viewprofilepage/user-id/127330)

Explorer

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=technology-blog-members&message.id=162566)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/technology-blog-members/article-id/162566)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13564454)

‎2023 Mar 12
1:06 PM

[4
Kudos](/t5/kudos/messagepage/board-id/technology-blog-members/message-id/162566/tab/all-users "Click here to see who gave kudos to this post.")

5,205

* SAP Managed Tags
* [Retail](https://community.sap.com/t5/c-khhcw49343/Retail/pd-p/99624789925257984685885)
* [SAPUI5](https://community.sap.com/t5/c-khhcw49343/SAPUI5/pd-p/500983881501772639608291559920477)
* [SAP Fiori for SAP S/4HANA](https://community.sap.com/t5/c-khhcw49343/SAP%2520Fiori%2520for%2520SAP%2520S%252F4HANA/pd-p/73555000100800000131)
* [MM (Materials Management)](https://community.sap.com/t5/c-khhcw49343/MM%2520%28Materials%2520Management%29/pd-p/477297786799213261950044802925335)

* [Retail

  Industry](/t5/c-khhcw49343/Retail/pd-p/99624789925257984685885)
* [SAP Fiori for SAP S/4HANA

  SAP Fiori](/t5/c-khhcw49343/SAP%2BFiori%2Bfor%2BSAP%2BS%25252F4HANA/pd-p/73555000100800000131)
* [MM (Materials Management)

  Software Product Function](/t5/c-khhcw49343/MM%2B%252528Materials%2BManagement%252529/pd-p/477297786799213261950044802925335)
* [SAPUI5

  Programming Tool](/t5/c-khhcw49343/SAPUI5/pd-p/500983881501772639608291559920477)

View products (4)

Receive Products is a SAP IS-R Retail standard application to post goods receipt. In my opinion it’s a great app that might seem profane at a first glance, but really shines after a deep dive ![:smiling_face_with_smiling_eyes:](/html/@41C5795FEF120B46F38A1F8D4435488E/emoticons/1f60a.png ":smiling_face_with_smiling_eyes:")

Since I couldn’t find much information online when I was looking into the app for our GR process, I thought it a bit underappreciated. Therefor I decided to point out the coolest features.

I won’t go into details with the basic  functionality like the multiple entry points (bar code scan, document or material number entry), GR posting and reversal, filters etc., since this is pretty obvious in the app itself, the information in the [Fiori Library](https://fioriappslibrary.hana.ondemand.com/sap/fix/externalViewer/#/detail/Apps('F1248')/W17) is solid and there are videos on youtube that cover this.

In this blog post I like to describe the (not that obvious) features I had to find out about myself (or at least find out by myself how the shortly mentioned feature in [SAP Help](https://help.sap.com/doc/79e0f54ff66d4cf0a3d21e87afb891c7/2.0%202016-08/en-US/frameset.htm?ef77f554b9b1b56ce10000000a44176d.html) actually works).

Ok, the start might be a bit basic, but if you are new to Fiori it might be helpful nonetheless and it caused a bit confusion in our project at first whether or not the app actually supports scanning.

1. (Really) Switch from desktop mode (in browser) to mobile mode and back

Hit F12 to enter development tools and switch mode:

![](/legacyfs/online/storage/blog_attachments/2023/03/1-9.png)

Right after clicking the visible window is switched and you can select the size of your actual device or create a custom one, but you are not yet in mobile mode! You need to reload (F5) first:

|
 ![](/legacyfs/online/storage/blog_attachments/2023/03/2-4.png) |
 ![](/legacyfs/online/storage/blog_attachments/2023/03/3-4.png) |
 ![](/legacyfs/online/storage/blog_attachments/2023/03/4-3.png) |

Now (when the scan symbol appears), you really are in mobile mode ![:smiling_face_with_smiling_eyes:](/html/@41C5795FEF120B46F38A1F8D4435488E/emoticons/1f60a.png ":smiling_face_with_smiling_eyes:")

2. Differences between “Receive Products” and “Receive Products trusted”

The first and pretty obvious functionality of the “trusted” version of this app is the additional option (the button in the upper right area) to select the complete document and post the GR either exactly like ordered (in case of reference to purchase order) or exactly like advised (in case of reference to inbound delivery document):

|
 ![](/legacyfs/online/storage/blog_attachments/2023/03/5-3.png) |
 ![](/legacyfs/online/storage/blog_attachments/2023/03/6-2.png) |

The normal (not trusted) “Receive Products” mode just doesn’t offer this menu button in the upper right area:

![](/legacyfs/online/storage/blog_attachments/2023/03/7-2.png)

Not that obvious is the second option to post a trusted GR.

2.1 Handling Units / SSCC18

If you received an inbound delivery with handling units and the handling units are identifiable by a scannable barcode (e.g. SSCC18) the scan of this number leads to direct posting in the background through “Receive Products trusted” while a scan in normal mode just opens the scanned document.

(sorry about the german screenshot, but it's just handling unit details from inbound delivery VL33n to show the connection)

![](/legacyfs/online/storage/blog_attachments/2023/03/9-1.png)

![](/legacyfs/online/storage/blog_attachments/2023/03/10-2.png)

Receive Products -> Scan opens document:

![](/legacyfs/online/storage/blog_attachments/2023/03/11-1.png)

Receive Products trusted -> Scan directly posts the GR in the background:

|
 ![](/legacyfs/online/storage/blog_attachments/2023/03/12-1.png) |
 ![](/legacyfs/online/storage/blog_attachments/2023/03/13-2.png) |

Btw. the HU description “pallets” on the screenshot stems from the description of the packaging material from customizing.

2.2 Other scannable identification (e.g. tracking number)

This works as well with other scannable data like e.g. a standard tracking number that logistic providers attach to deliveries.

If you can’t or do not want to use handling units the corresponding tracking number needs to be in LIKP-BOLNR:

![](/legacyfs/online/storage/blog_attachments/2023/03/14-1.png)

Frachtbr. = BOLNR

![](/legacyfs/online/storage/blog_attachments/2023/03/15-1.png)

3. BOL Number replaces internal delivery number

As you probably already could deduct from the screenshots above whatever is entered in LIKP-BOLNR will replace the SAP internal inbound delivery number on the "Receive Products" screens. So if you do not want to use it for the tracking number, you could/should store the suppliers delivery number in this field and directly see this number, which makes it much easier to verify that you are working on the right document.  (I mention this, because from my experience the suppliers delivery number will b...