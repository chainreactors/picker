---
title: Six Million Pictures
url: https://www.hackerfactor.com/blog/index.php?%2Farchives%2F979-Six-Million-Pictures.html=
source: Instapaper: Unread
date: 2023-01-21
fetch_date: 2025-10-04T04:31:21.637926
---

# Six Million Pictures

![Hacker Factor Logo](/images/hf-lock-banner.png)

[The Hacker Factor Blog](/blog/)

**Science-based transgender diversity for vulnerable evidence-based fetus entitlement**

[Home](/)
[Blog](/blog/)
[Swag](https://www.zazzle.com/hackerfactor/?rf=238307745558769988)

### About

[Dr. Neal Krawetz](/about.php) writes The Hacker Factor Blog. Follow him on [Mastodon](https://noc.social/%40hackerfactor).

### Tools

• [FotoForensics](https://fotoforensics.com/): Test your own photos.

### Links

**Security**

### Calendar

|  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- |
| [«](https://hackerfactor.com/blog/index.php?/archives/2025/09.html "View posts for previous month") | October '25 | | | | |  |
| S | M | T | W | T | F | S |
|  |  |  | 1 | 2 | 3 | 4 |
| 5 | 6 | 7 | 8 | 9 | 10 | 11 |
| 12 | 13 | 14 | 15 | 16 | 17 | 18 |
| 19 | 20 | 21 | 22 | 23 | 24 | 25 |
| 26 | 27 | 28 | 29 | 30 | 31 |  |

### Archives

* [October 2025](/blog/index.php?/archives/2025/10.html "October 2025")
* [September 2025](/blog/index.php?/archives/2025/09.html "September 2025")
* [August 2025](/blog/index.php?/archives/2025/08.html "August 2025")
* [Recent...](/blog/index.php?frontpage)
* [Older...](https://hackerfactor.com/blog/index.php?/archive)

### Feeds

* [![XML](/blog/templates/nealk/img/xml.gif)](/blog/index.php?/feeds/index.rss1)
  [RSS 1.0 feed](/blog/index.php?/feeds/index.rss1)
* [![XML](/blog/templates/nealk/img/xml.gif)](/blog/index.php?/feeds/index.rss2)
  [RSS 2.0 feed](/blog/index.php?/feeds/index.rss2)

### Categories

* [Conferences](/blog/index.php?/categories/7-Conferences "Been there, done that, took notes")
* [Copyright](/blog/index.php?/categories/16-Copyright "Copyrights, Patents, and Concerns")
* [Financial](/blog/index.php?/categories/8-Financial "Money Matters")
* [Forensics](/blog/index.php?/categories/14-Forensics "Computer and Digital Forensics")
* [Authentication](/blog/index.php?/categories/23-Authentication)
* [FotoForensics](/blog/index.php?/categories/17-FotoForensics "http://fotoforensics.com/")
* [Image Analysis](/blog/index.php?/categories/1-Image-Analysis "A Picture's Worth")
* [IoT](/blog/index.php?/categories/22-IoT "Internet of Things")
* [Mass Media](/blog/index.php?/categories/6-Mass-Media "Volume Does Not Imply Brightness")
* [Music](/blog/index.php?/categories/24-Music)
* [Network](/blog/index.php?/categories/3-Network "A Series of Tubes")
* [Honeypot](/blog/index.php?/categories/21-Honeypot "This is my other computer")
* [Tor](/blog/index.php?/categories/19-Tor "The Onion Router")
* [Phones](/blog/index.php?/categories/18-Phones "Telemarketers, Cold Calls, and Scams")
* [Politics](/blog/index.php?/categories/13-Politics "Fear, Uncertaity, Doubt, and that bad aftertaste")
* [Privacy](/blog/index.php?/categories/9-Privacy "You Have The Right")
* [Programming](/blog/index.php?/categories/5-Programming "Code Monkey's Unite!")
* [AI](/blog/index.php?/categories/20-AI "AI and Machine Learning")
* [Security](/blog/index.php?/categories/4-Security "Attack and Defend")
* [Terrorists](/blog/index.php?/categories/2-Terrorists "Terrorism Research")
* [Travel](/blog/index.php?/categories/15-Travel "Enjoy life! Eat out more often!")
* [Unfiction](/blog/index.php?/categories/12-Unfiction "I can't make this up...")
* [[Other]](/blog/index.php?/categories/11-Other "Catch-all category")

[All categories](/blog/index.php?frontpage "All categories")

# [Six Million Pictures](/blog/index.php?/archives/979-Six-Million-Pictures.html)

## Thursday, 19 January 2023

Last Saturday we hit a milestone at [FotoForensics](https://fotoforensics.com/): 6 million unique pictures! I was really hoping that this achievement wouldn't be marred by porn so I could do a deep dive into it. (SPOILER ALERT: Not porn! Woo hoo!)

Here's the picture! It arrived on 2023-01-14 at 11:50:55 GMT:

[![](https://fotoforensics.com/analysis.php?id=fc5f07ba4c6a65d140a653eb44ecec766ccb15df.143628&fmt=orig&size=600)](https://fotoforensics.com/analysis.php?id=fc5f07ba4c6a65d140a653eb44ecec766ccb15df.143628)

I'm not big on following sports, celebrities, or pop culture, so I approached this picture with zero knowledge. The picture shows two women and a guy at some kind of club or restaurant. However, I don't know the people or the situation. This sounds like a great opportunity to do some image sleuthing. (Click on the picture to view it at FotoForensics.)

Side note: I'm writing this as a streaming flow of consciousness. I didn't gather the pictures or complete this investigation before I started writing.

### Where to start? Metadata!

When evaluating a picture, it's always good to check the metadata. A camera-original picture will often include date, time, camera settings, and other information that can help track down the source. For example, an embedded time zone or region-specific device can provide a good guess about where the photo was taken. Similarly, many photo editors leave details in the metadata.

On the downside, many applications re-encode the image and strip out the source metadata. If the metadata was stripped, then there may be no camera or location information.

Unfortunately with this picture, there is no informative metadata. At minimum, this means that the picture has been resaved from some other photo.

The only interesting thing in the metadata is the ICC Profile. This specific profile is from Google and indicates that the picture was processed by an app -- either through an Android application or a Google service.

### Hidden Pixels and Quality

JPEG encodes pixels using an 8x8 grid. If the image doesn't align with the grid, then there are [hidden pixel](/blog/index.php?/archives/794-Six-and-Hidden-Pixels.html) along the right and bottom edges that pad out the image. This image size is 940x788 -- neither dimension is divisible by 8, so there are 4x4 hidden pixels. (940+4 = 944, which is divisible by 8. Similarly, 788+4 = 792 which is also dibisible by 8.) The encoded image is 944x792 pixels, but automatically cropped to 940x788 before being displayed.

Different applications use different approaches for filling the JPEG padding. Adobe uses a mirrored pattern than often produces a butterfly-wing shape on high-contrast curves. In contrast, libjpeg just repeats the last pixel value, creating a stretched effect. However, a lossless crop often leaves the original uncropped pixels. With this picture, there is a stretched pattern used for the padding. That's consistent with libjpeg and not an Adobe product.

![](https://fotoforensics.com/analysis.php?id=fc5f07ba4c6a65d140a653eb44ecec766ccb15df.143628&fmt=hidden&size=600)

Similarly, different applications use different encoding tables. The 'JPEG %' analyzer shows that this image was encoded as a JPEG at 92% using the JPEG Standard.

While this doesn't tell us who these people are, the results from the metadata, hidden pixels, and JPEG % are consistent: this was re-encoded using a standard JPEG library. (Google uses standard libraries.) This was *not* last saved using an Adobe product.

The final quality test is the error level analysis (ELA). ELA evaluates the compression quality. Bright colors indicates the areas that will change more during a JPEG re-encoding. You should compare similar surfaces, similar textures, and similar edges. Any inconsistencies, such as a flat surface that is at a different intensity from other flat surfaces, denotes an alteration.

![](https://fotoforensics.com/analysis.php?id=fc5f07ba4c6a65d140a653eb44ecec766ccb15df.143628&fmt=ela&size=600)

With this picture, there are a couple of things that stand out:

* All of the flat, smooth surfaces are equally dark. The dark clothing, dark ceiling, and even the smooth skin. (No comment about any potential plastic surgery to remove wrinkles.) An image that is this dark -- and yet last encoded at a high quality like 92% -- means that it has been re-encoded multiple times.

* The areas with fine details (high frequencies), such as the lac...