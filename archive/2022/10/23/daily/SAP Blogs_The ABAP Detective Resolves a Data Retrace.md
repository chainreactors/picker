---
title: The ABAP Detective Resolves a Data Retrace
url: https://blogs.sap.com/2022/10/22/the-abap-detective-resolves-a-data-retrace/
source: SAP Blogs
date: 2022-10-23
fetch_date: 2025-10-03T20:41:14.969746
---

# The ABAP Detective Resolves a Data Retrace

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Additional Blog Posts by Members](/t5/additional-blog-posts-by-members/bg-p/additional-blog-members)
* The ABAP Detective Resolves a Data Retrace

Additional Blog Posts by Members

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/additional-blog-members/article-id/63286&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [The ABAP Detective Resolves a Data Retrace](/t5/additional-blog-posts-by-members/the-abap-detective-resolves-a-data-retrace/ba-p/13551153)

![JimSpath](https://avatars.profile.sap.com/1/9/id19e0902ffb151e54856445a6cc9bb1df4e8202ab913d64c6e2e2d8625cd7bf0a_small.jpeg "JimSpath")

![SAP Champion](/html/@B3DACAC6163F980483AC32558EB69695/rank_icons/champion-rank-16x16.svg "SAP Champion")
[JimSpath](https://community.sap.com/t5/user/viewprofilepage/user-id/184)

SAP Champion

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=additional-blog-members&message.id=63286)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/additional-blog-members/article-id/63286)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13551153)

‎2022 Oct 22
2:51 PM

[1
Kudo](/t5/kudos/messagepage/board-id/additional-blog-members/message-id/63286/tab/all-users "Click here to see who gave kudos to this post.")

774

* SAP Managed Tags
* [User Experience](https://community.sap.com/t5/c-khhcw49343/User%2520Experience/pd-p/4616d815-f39e-45c8-b13b-5a2d6679778f)

* [User Experience

  Topic](/t5/c-khhcw49343/User%2BExperience/pd-p/4616d815-f39e-45c8-b13b-5a2d6679778f)

View products (1)

This case is about data more than code. In the cold case files are stacks of evidence, observations for possible future use. Could be environmental or climate data, could be traffic or road conditions, could be inventory information. Digging through archives can be rewarding as long as there is some type of index or metadata, and the current technology allows for review of previously collected digital bits. Think floppy drives, magnetic tape, or even optical storage. The content on those media is useless if you can't read them.

What happens when the "cloud" storage repository goes away? That is the crux of this current case: geotagged data that was uploaded to a site that <*big cloud provider*> decided to shut down. When I learned hundreds of images I contributed were to be inaccessible, I made a withdrawal, intending to move the content to a new repository.

Here's where the metadata, the data dictionary, and sizing requirements come in. In my case, I recorded many ground-level images, doing field survey/service work. Over 10 years ago, the ability to capture GPS data was more limited (and expensive) than it it now, so the primary data had no location information. On upload, locations were manually tagged on a map. Doing so added metadata. However, because of site rules, the images were degraded (reduced in resolution). Meaning my original data was better in some ways, and worse in others.

Why crowd source data collection? The easiest example is traffic; hundreds (or billions) of GPS-enabled location records allow sites to produce real-time condition maps, offer alternate routes, and capture evolving trends. Even if you don't realize you're contributing you are, for which we thank you. For voluntary projects like bio-diversity analyses, having people collect data on forms can be burdensome, so the easier the set-up is, the more data to be gathered. Sites can offer incentives, whether basic recognition ("Four Star Reviewer!") or some swag ("Oooh, T shirts!"), or future dividends such as data retrieval. See below under "also".

### Field Survey

[![](/legacyfs/online/storage/blog_attachments/2022/10/earth-yellow-trail-frog-hollow.jpg)](https://web.archive.org/web/20161014101121/http%3A//www.panoramio.com/photo/24364336)

Frog Hollow and the Yellow Trail

Here is one example of a field data capture. On the left side of the inset image is a walking trail; on the right side is a stream. A primary use of these data is quality control on path suggestions; should a stream crossing be hazardous due to increased flow exacerbated by upstream "development".

The saved online file is missing metadata, and was shrunk from the original capture. The "jhead" utility program tells us:

```
File name    : panoramio-24364336.jpg

File size    : 139933 bytes

File date    : 2022:10:07 15:32:29

Resolution   : 800 x 600

JPEG Quality : 75
```

Not to mention, the date shows when it was downloaded, not when it was captured or uploaded. The "takeout" process where you can preserve your original contributions show metadata in a separate related file:

```
 139823 Nov  8  2018 2018-09-05/panoramio-24364336.jpg

    874 Nov  8  2018 2018-09-05/panoramio-24364336.jpg.json
```

The image size is the reduced quality (*drat*), but there are lat/lon points, and the original capture date:

```
 "formatted": "Jul 11, 2009, 6:49:30 PM UTC"
```

Some data reconstitution could be done from these parts, but the higher resolution imagery could not. Long digging steps skipped here for brevity.

Ah, one of these may be the original:

```
 1302599 Jul 11  2009 DSCN7671.JPG

 1308378 Jul 11  2009 DSCN7672.JPG

 1297094 Jul 11  2009 DSCN7673.JPG

File name    : DSCN7671.JPG

File size    : 1302599 bytes

File date    : 2009:07:11 13:22:50

Date/Time    : 2009:07:11 09:22:51

Resolution   : 2560 x 1920

...

JPEG Quality : 84
```

JPEG quality higher, image size larger, only problem is which image was preserved online, and what to do about the remainder? Turned out to be #7675. My search used timestamps though these were not entirely helpful for 2 reasons: one being the camera not having accurate time and date (less of an issue if the sequence stays in order), the other being the file transfer date was recorded rather than the capture moment. The latter cause headaches resulting in fewer good archive retrievals.

A side by side resolution comparison indicates the value of recovering the clearer images. If not apparent in the default post rendering, click/zoom to verify.

|
 ![](/legacyfs/online/storage/blog_attachments/2022/10/DSCN7675-crop.jpg)    High resolution |
 ![](/legacyfs/online/storage/blog_attachments/2022/10/panoramio-24364336-crop.jpg)    Low resolution |

Another issue is the quantity of original data points compared to those sent to the cloud repository. Perhaps some sites take (slurp) all your data, but curated sites might either reject some portion, or create barriers like transfer speed or content size limits (e.g. "< 10 megapixels"). As these geotags were done manually, the leftover images had no recorded locations other than my sparse field notes (or blog posts done at the time); recreating that level of detail after an appreciable time was tough. Some records were captured at obvious places with visible landmarks, some not so much. Think of field data capture such as valve or joint condition by physical inspection, maybe bridge piers or safety rails. More frequent image capture, even by non-professional structural engineers, can assist in safety reviews.

From a set of 5 dates, my archives had roughly 500 still images (and a few movies) in the time period from 2009-2010. Recently, with a 128GB data card, I took 700 images in an hour or two, just to show the potential explosive growth of base...