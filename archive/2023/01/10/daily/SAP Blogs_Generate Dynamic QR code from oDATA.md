---
title: Generate Dynamic QR code from oDATA
url: https://blogs.sap.com/2023/01/09/generate-dynamic-qr-code-from-odata/
source: SAP Blogs
date: 2023-01-10
fetch_date: 2025-10-04T03:24:50.652807
---

# Generate Dynamic QR code from oDATA

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Technology](/t5/technology/ct-p/technology)
* [Technology Blog Posts by Members](/t5/technology-blog-posts-by-members/bg-p/technology-blog-members)
* Generate Dynamic QR code from oDATA

Technology Blog Posts by Members

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/technology-blog-members/article-id/162632&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [Generate Dynamic QR code from oDATA](/t5/technology-blog-posts-by-members/generate-dynamic-qr-code-from-odata/ba-p/13564848)

![nitinksh1](https://avatars.profile.sap.com/a/c/idacef170ce1e7f2f7c7ed45f61d80f3b3b4fa1466fcc18c01a0505b6b26d85535_small.jpeg "nitinksh1")

[nitinksh1](https://community.sap.com/t5/user/viewprofilepage/user-id/45127)

Participant

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=technology-blog-members&message.id=162632)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/technology-blog-members/article-id/162632)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13564848)

‎2023 Jan 09
7:05 PM

[6
Kudos](/t5/kudos/messagepage/board-id/technology-blog-members/message-id/162632/tab/all-users "Click here to see who gave kudos to this post.")

19,302

* SAP Managed Tags
* [ABAP Development](https://community.sap.com/t5/c-khhcw49343/ABAP%2520Development/pd-p/833755570260738661924709785639136)
* [NW ABAP Gateway (OData)](https://community.sap.com/t5/c-khhcw49343/NW%2520ABAP%2520Gateway%2520%28OData%29/pd-p/181161894649260056016734803547327)
* [NW ABAP Web Services](https://community.sap.com/t5/c-khhcw49343/NW%2520ABAP%2520Web%2520Services/pd-p/99891761267046184358097136821575)

* [NW ABAP Gateway (OData)

  Software Product Function](/t5/c-khhcw49343/NW%2BABAP%2BGateway%2B%252528OData%252529/pd-p/181161894649260056016734803547327)
* [NW ABAP Web Services

  Software Product Function](/t5/c-khhcw49343/NW%2BABAP%2BWeb%2BServices/pd-p/99891761267046184358097136821575)
* [ABAP Development

  Programming Tool](/t5/c-khhcw49343/ABAP%2BDevelopment/pd-p/833755570260738661924709785639136)

View products (3)

## **Introduction**

QR (Quick Response) codes are two-dimensional barcodes that are widely used for storing and sharing information. They are particularly useful because they can be read quickly and easily by a smartphone or other device equipped with a camera and a QR code reader app.

If we can add a QR code to our app/oData call, it can open a wide area of fields for implementation.

### **Step-by-Step Procedure:**

1. Create a page format as of QR size: If we do not create a page format then the QR will be shown in the whole A4 size page and a lot of space will be left empty. Use tcode SPAD for creating.

2. Create a Barcode: We will use SE73 to create a barcode.

3. Create a smartstyle: To create a character format for QR.

4. Create a smartform: To display the

5. Create a class: To convert text to xstring. This xstring will be passed to the oData call.

6. Table Creation: Create a table to store the data to be displayed in form of a QR code via oData.

7. Create oData Service: Finally, we will be creating an oData service.

8. Publish and test the Odata service.

Let's start the development now in the steps mentioned above.

### **STEP 1:** Create a page format: Go to tcode SPAD.

1.1 Click on the full administrator and go to the tab Device Types and click on display.

![](/legacyfs/online/storage/blog_attachments/2023/01/Image-1-SPAD-landing-screen-1.jpg)

Image 1- SPAD landing screen

![](/legacyfs/online/storage/blog_attachments/2023/01/Image-2-SPAD-Page-Format-2.jpg)

Image 2- SPAD Page Format

1.2 Click on the pencil button to come to change mode and then click Create to create a new page format.

![](/legacyfs/online/storage/blog_attachments/2023/01/Image-3-Create-Page-Format-1.jpg)

Image 3- Create Page Format

1.3 Save the page format with the below settings. One thing to notice is that depending on the data, the QR code can increase its size a bit as it has to hold more data in it. Play and change these settings as required.

![](/legacyfs/online/storage/blog_attachments/2023/01/Image-4-Save-Page-Format-1.jpg)

Image 4- Save Page Format

1.4 Our first step completes here.

### **STEP 2:** Create a barcode.

2.1 Go to tcode SE73 and create a new Barcode.

![](/legacyfs/online/storage/blog_attachments/2023/01/Image-5-SE73-2.png)

Image 5 - SE73

2.2 Create a new barcode.

![](/legacyfs/online/storage/blog_attachments/2023/01/Image-6-New-Barcode-1.png)

Image 6 - New Barcode

2.3 Use the below setting to create the barcode.

![](/legacyfs/online/storage/blog_attachments/2023/01/Image-7-New-Barcode-Setting-1.png)

Image 7 - New Barcode Setting

![](/legacyfs/online/storage/blog_attachments/2023/01/Image-8-New-Barcode-Setting-1.png)

Image 8 - New Barcode Setting

![](/legacyfs/online/storage/blog_attachments/2023/01/Image-9-New-Barcode-Setting-2.png)

Image 9 - New Barcode Setting

![](/legacyfs/online/storage/blog_attachments/2023/01/Image-10-New-Barcode-Setting-1.png)

Image 10 - New Barcode Setting

2.4 QR Code is created. Now it's time to test the QR code. Place your cursor on the new barcode, in our case it is ZQRDISP, and hit F6 (execute barcode). I guess we all are excited to see the QR code in this development for the first time.

![](/legacyfs/online/storage/blog_attachments/2023/01/Image-11-Test-Barcode-From-SE73-1.png)

Image 11 - Test Barcode From SE73

2.5 Execute the report with any text.

![](/legacyfs/online/storage/blog_attachments/2023/01/Image-12-Execute-Report-2.png)

Image 12 - Execute Report

2.6 Tada! Our QR code is ready.

![](/legacyfs/online/storage/blog_attachments/2023/01/Image-13-QR-Code-from-SE73-1.png)

Image 13 - QR Code from SE73

### **STEP 3 : Create Smartstyle**

Let's create a smartstyle on the top of created barcode.

3.1 Create a smartstyle with character format as the created barcode. Also, create a default paragraph to add to the header data.

![](/legacyfs/online/storage/blog_attachments/2023/01/Image-14-Smartsyles.png)

Image 14 - Smartsyles

### **STEP 4: Create Smartform**

Let's move on to create a smartform.

4.1 This smartform will have an input parameter of type string and we will pass this parameter to the text element so that it can be displayed as a QR code. Add recently created smartsytle via the output options tab of the text element.

![](/legacyfs/online/storage/blog_attachments/2023/01/Image-15-Smartform.png)

Image 15 - Smartform

4.2 Save and activate it.

4.3 It's time to execute the smartform, let's see what the output looks like. Pass any text to input field. Voila, we got a QR code!![:man_dancing:](/html/@7F7B61D4FB6468E01D38BC7CE6AA4097/emoticons/1f57a.png ":man_dancing:")![:man_dancing:](/html/@7F7B61D4FB6468E01D38BC7CE6AA4097/emoticons/1f57a.png ":man_dancing:")![:man_dancing:](/html/@7F7B61D4FB6468E01D38BC7CE6AA4097/emoticons/1f57a.png ":man_dancing:")

![](/legacyfs/online/storage/blog_attachments/2023/01/Image-16-Smartform-Output.png)

Image 16 - Smartform Output

4.4 Do scan the QR code and it will take you to like to read another oData blog.

### **STEP 5: Create Class**

5.1 Create a class that will take a string as an input. It will take that string and pass it to smartform, generate the QR from it, and then finally the QR will be converted to pdf xstring. As oData can not p...