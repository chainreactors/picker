---
title: Customizing Fonts in XDC file for Zebra and Honeywell Printer (Adobe Forms)
url: https://blogs.sap.com/2023/01/17/customizing-fonts-in-xdc-file-for-zebra-and-honeywell-printer-adobe-forms/
source: SAP Blogs
date: 2023-01-18
fetch_date: 2025-10-04T04:08:35.653635
---

# Customizing Fonts in XDC file for Zebra and Honeywell Printer (Adobe Forms)

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Technology](/t5/technology/ct-p/technology)
* [Technology Blog Posts by Members](/t5/technology-blog-posts-by-members/bg-p/technology-blog-members)
* Customizing Fonts in XDC file for Zebra and Honeyw...

Technology Blog Posts by Members

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/technology-blog-members/article-id/163401&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [Customizing Fonts in XDC file for Zebra and Honeywell Printer (Adobe Forms)](/t5/technology-blog-posts-by-members/customizing-fonts-in-xdc-file-for-zebra-and-honeywell-printer-adobe-forms/ba-p/13569549)

![former_member828182](https://avatars.profile.sap.com/former_member_small.jpeg "former_member828182")

[former\_member828182](https://community.sap.com/t5/user/viewprofilepage/user-id/828182)

Explorer

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=technology-blog-members&message.id=163401)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/technology-blog-members/article-id/163401)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13569549)

‎2023 Jan 17
10:58 PM

0
Kudos

2,831

* SAP Managed Tags
* [SAP Interactive Forms by Adobe](https://community.sap.com/t5/c-khhcw49343/SAP%2520Interactive%2520Forms%2520by%2520Adobe/pd-p/582573882271271216439685697820265)

* [SAP Interactive Forms by Adobe

  Software Product Function](/t5/c-khhcw49343/SAP%2BInteractive%2BForms%2Bby%2BAdobe/pd-p/582573882271271216439685697820265)

View products (1)

The ADS is using a so called XDC file as driver for its output.
The Zebra output is using zpl203.xdc or zpl300.xdc depending on what printer is in use and Honeywell is using ipl203.xdc.

**This post shows how to customize all the three files, to make the font look similar in all output cases.**

The default font in Zebra printer is “CG Triumvirate\_Normal\_Normal”
and in Honeywell printer is "Intermec Swiss 721\_Normal\_Normal".

This information can be found in the XDC file under the section “Raster Substitution Font”.

Due to the default setting in the File the output printed is always in these Font types.

**The Solution:**

To print the desired fonts in the output, the fonts need to be rasterized. The file must be changed to the following settings.

* Open the copied XDC file in a text editor and change the line:<xdc name="zpl300" id="zpl300" xmlns="[http://www.xfa.org/schema/xdc/1.0/|](http://www.xfa.org/schema/xdc/1.0/%7C)<http://www.xfa.org/schema/xdc/1.0/>">

  TO

  <xdc name="zpl300\_TQ" id="zpl300\_TQ" xmlns="[http://www.xfa.org/schema/xdc/1.0/|](http://www.xfa.org/schema/xdc/1.0/%7C)<http://www.xfa.org/schema/xdc/1.0/>">

**Rename the file with zpl300\_TQ and SAVE THE CHANGES.**
It is important to make sure you are not changing the original file.

* Now look for the following line:<rasterSubstitutionFont typeface="CG Triumvirate\_Normal\_Normal" unicodeRange="U+20-U+FF"/>

  change this to:

  <rasterSubstitutionFont typeface="CG Triumvirate\_Normal\_Normal" />

**Removing UnicodeRange allows the settings to set active for rasterizing.** **Save the changes.**

* You can now use whichever font you like for you Adobe forms, but One more important thing must be taken into consideration.
  The font you choose in Adobe Forms should be available in the ADS.

* If the font is not available in ADS server you need to upload the relevant “.ttf” file in the server.
  When the fonts are uploaded and available to use,  they are automatically rasterized with the above settings .

* The last step is to Upload this modified XDC file to the printer. It could be done with the following steps.

1. 1. Go to SE38.

   2. Start the report: RSPO002.

   3. Here select display XDC entries and look for which line is assigned to your printer.

   4. Once the new file is uploaded. Go back to the start of the RSPO0022 and change the XDC assigned to the printer in use to the file name you gave above “zpl300\_TQ.xdc”

   5. Save the Changes. The printer is ready to print with the new fonts.

* [fonts](/t5/tag/fonts/tg-p/board-id/technology-blog-members)
* [honeywell printer](/t5/tag/honeywell%20printer/tg-p/board-id/technology-blog-members)
* [zebra printer](/t5/tag/zebra%20printer/tg-p/board-id/technology-blog-members)

You must be a registered user to add a comment. If you've already registered, sign in. Otherwise, register and sign in.

* [Comment](/plugins/common/feature/oidcss/sso_login_redirect/providerid/sap_ids_prompt?redirectreason=permissiondenied&referer=https%3A%2F%2Fcommunity.sap.com%2Ft5%2Ftechnology-blog-posts-by-members%2Fcustomizing-fonts-in-xdc-file-for-zebra-and-honeywell-printer-adobe-forms%2Fba-p%2F13569549%23comment-on-this)

Copy Link
![](https://community.sap.com/html/@EE5D5986E9F4E5657DCEACB7532B5C39/assets/bluesky-dark.svg)Bluesky
Linkedin

Related Content

* [SAP S4HANA Plant Maintenance for dummies](/t5/technology-blog-posts-by-members/sap-s4hana-plant-maintenance-for-dummies/ba-p/14234304)
  in [Technology Blog Posts by Members](/t5/technology-blog-posts-by-members/bg-p/technology-blog-members)  8 hours ago
* [Going international - Caveats in custom ABAP programs](/t5/technology-blog-posts-by-members/going-international-caveats-in-custom-abap-programs/ba-p/13739006)
  in [Technology Blog Posts by Members](/t5/technology-blog-posts-by-members/bg-p/technology-blog-members)  2024 Jun 21
* [Crystal Reports 2020 for Eclipse - Java - Custom paper size for Zebra Label Printer](/t5/technology-q-a/crystal-reports-2020-for-eclipse-java-custom-paper-size-for-zebra-label/qaq-p/13628687)
  in [Technology Q&A](/t5/technology-q-a/qa-p/technology-questions)  2024 Mar 05
* [LSMW : How to Upload Master Data by using a Batch Input Recording IN SAP ECC](/t5/technology-blog-posts-by-members/lsmw-how-to-upload-master-data-by-using-a-batch-input-recording-in-sap-ecc/ba-p/13579625)
  in [Technology Blog Posts by Members](/t5/technology-blog-posts-by-members/bg-p/technology-blog-members)  2023 Oct 15
* [Smooth transition to ABAP for Cloud Development(Cheat sheet)](/t5/technology-blog-posts-by-members/smooth-transition-to-abap-for-cloud-development-cheat-sheet/ba-p/13571567)
  in [Technology Blog Posts by Members](/t5/technology-blog-posts-by-members/bg-p/technology-blog-members)  2023 Aug 15

Top kudoed authors

| User | Count |
| --- | --- |
| [![WouterLemaire](https://avatars.profile.sap.com/9/5/id95a688fa6b84e4186cabf39d7a83127ea90dd51dd190d355416d56f7d3a5be56_small.jpeg "WouterLemaire")  ![SAP Mentor](/html/@F4C200E47DAE3459A6BD3FBB7F9955B8/rank_icons/mentor-rank-16x16.svg "SAP Mentor") WouterLemaire](/t5/user/viewprofilepage/user-id/9863) | 6 |
| [![Sandra_Rossi](https://avatars.profile.sap.com/5/a/id5ade69af148fee003e69a3410fe4ea7d8d92f9f0535ff49f640e7d27e69efed1_small.jpeg "Sandra_Rossi")  Sandra\_Rossi](/t5/user/viewprofilepage/user-id/145194) | 4 |
| [![rajarajeswari_kaliyaperum](https://avatars.profile.sap.com/c/1/idc10d67889f40de37cfb340af4a802e39952419bdc3ee1ba9dd6000bf645e35b6_small.jpeg "rajarajeswari_kaliyaperum")  rajarajeswari\_kaliyaperum](/t5/user/viewprofilepage/user-id/654809) | 4 |
| [![kartheekkkota](https://avatars.profile.sap.com/2/d/id2d7e639322351b2b6b5a2b0a8d59075fd847a612a238bd7704e00c54f4a4e975_small.jpeg "kartheekkkota")  kartheekkkota](/t5/user/viewprofilepage/user-id/227849) | 4 |
| [![mickaelquesno...