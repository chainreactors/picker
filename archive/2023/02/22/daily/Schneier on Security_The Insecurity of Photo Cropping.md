---
title: The Insecurity of Photo Cropping
url: https://www.schneier.com/blog/archives/2023/02/the-insecurity-of-photo-cropping.html
source: Schneier on Security
date: 2023-02-22
fetch_date: 2025-10-04T07:47:54.192529
---

# The Insecurity of Photo Cropping

# [Schneier on Security](https://www.schneier.com/)

Menu

* [Blog](https://www.schneier.com)
* [Newsletter](https://www.schneier.com/crypto-gram/)
* [Books](https://www.schneier.com/books/)
* [Essays](https://www.schneier.com/essays/)
* [News](https://www.schneier.com/news/)
* [Talks](https://www.schneier.com/talks/)
* [Academic](https://www.schneier.com/academic/)
* [About Me](https://www.schneier.com/blog/about/)

### Search

*Powered by [DuckDuckGo](https://duckduckgo.com/)*

Blog

Essays

Whole site

### Subscribe

[![Atom](https://www.schneier.com/wp-content/uploads/2019/10/rss-32px.png)](https://www.schneier.com/feed/atom/)[![Facebook](https://www.schneier.com/wp-content/uploads/2019/10/facebook-32px.png)](https://www.facebook.com/bruce.schneier)[![Twitter](https://www.schneier.com/wp-content/uploads/2019/10/twitter-32px.png)](https://twitter.com/schneierblog)[![Email](https://www.schneier.com/wp-content/uploads/2019/10/email-32px.png)](https://www.schneier.com/crypto-gram)

[Home](https://www.schneier.com)[Blog](https://www.schneier.com/blog/archives/)

## The Insecurity of Photo Cropping

The *Intercept* has a [long article](https://theintercept.com/2023/02/14/whistleblower-image-crop-document/) on the insecurity of photo cropping:

> One of the hazards lies in the fact that, for some of the programs, downstream crop reversals are possible for viewers or readers of the document, not just the file’s creators or editors. Official instruction manuals, help pages, and promotional materials may mention that cropping is reversible, but this documentation at times fails to note that these operations are reversible by any viewers of a given image or document.
>
> […]
>
> Uncropped versions of images can be preserved not just in Office apps, but also in a file’s own metadata. A photograph taken with a modern digital camera contains all types of metadata. Many image files record text-based metadata such as the camera make and model or the GPS coordinates at which the image was captured. Some photos also include binary data such as a thumbnail version of the original photo that may persist in the file’s metadata even after the photo has been edited in an image editor.

Tags: [forensics](https://www.schneier.com/tag/forensics/), [metadata](https://www.schneier.com/tag/metadata/), [photos](https://www.schneier.com/tag/photos/), [whistleblowers](https://www.schneier.com/tag/whistleblowers/)

[Posted on February 21, 2023 at 7:14 AM](https://www.schneier.com/blog/archives/2023/02/the-insecurity-of-photo-cropping.html) •
[23 Comments](https://www.schneier.com/blog/archives/2023/02/the-insecurity-of-photo-cropping.html#comments)

### Comments

Winter •
[February 21, 2023 7:48 AM](https://www.schneier.com/blog/archives/2023/02/the-insecurity-of-photo-cropping.html/#comment-418127)

I try to solve these problems by converting (exporting) “cropped” photographs to .PNG. But I must admit that I do not know how, or even if, this would affect the metadata.

Peter A. •
[February 21, 2023 7:55 AM](https://www.schneier.com/blog/archives/2023/02/the-insecurity-of-photo-cropping.html/#comment-418128)

It’s not the insecurity of photo cropping per se, it’s the insecurity of photo cropping *apps* – and the fact that the version of the image before cropping may make its way to unintended audience. One needs to be careful when erasing Mr. Jezhov from a photo…

Uthor •
[February 21, 2023 8:28 AM](https://www.schneier.com/blog/archives/2023/02/the-insecurity-of-photo-cropping.html/#comment-418130)

I was wondering if exporting a Word document to PDF gets rid of this data. But I also assume that it would add some metadata that you wouldn’t want in there.

David Rudling •
[February 21, 2023 8:51 AM](https://www.schneier.com/blog/archives/2023/02/the-insecurity-of-photo-cropping.html/#comment-418131)

There are products such as exiferaser which claim to strip this unwanted data from a digital camera image but I don’t know how effective they are.

TimH •
[February 21, 2023 10:42 AM](https://www.schneier.com/blog/archives/2023/02/the-insecurity-of-photo-cropping.html/#comment-418132)

PNGs save creation time. Save the file as a Windows type BMP.

JonKnowsNothing •
[February 21, 2023 11:43 AM](https://www.schneier.com/blog/archives/2023/02/the-insecurity-of-photo-cropping.html/#comment-418140)

@ALL

iirc(badly) iPhone edits also create a shadow file. When you DL to Windows you can see them and delete them. They contain the sequence of edits.

iirc(badly) There was some info that Screen Shot tools also contain some traceable elements of the original besides the selected image. It was not safe to rely on Screen Shots to remove the EXIF data information.

iirc(badly) Marcy Wheeler (emptywheel. net) has had some experience deciphering pdfs of legal documents. That is not a safe conversion either.

Even if you manage to crop the image and remove the tracks, there is the subject of the image. There are now more reports of using the image itself to determine the original.

The NSA+Google have a massive full web scrap project to replace Exif data and add geotags on any image that does not have them.

Canadian Wild Life Rangers used terrain ID and GPS extrapolation to determine the precise spot where a US Hunter poached a trophy animal inside Canada shooting across the US-Canadian border. The US Hunter tried to hide his poaching by doing a tight crop of the Trophy Pose image. (1)

A curious aspect:

* The US hunter shooting across the border and killing a trophy animal was fined and given a No Hunt In Canada sentence.
* The USA Border Patrol gets no penalties at all for shooting across the border into Mexico and killing people there. The US Border Patrol doesn’t hide anything at all. It’s on video and celebrated by the department.

===

1) There are specialty field cameras called Trail Cameras. Very popular with wild life scientists as well as hunters. The cameras can be placed anywhere and record still or video both in Daylight and Nighttime, No Flash (red eye). They run on batteries and can last in the field a long time. The upper end models have built in uploading to the cloud, on demand, RT. Some of the apps analyze the hundreds of images pulling out specified ones of interest: deer, wolf, bear, bumblebee etc. They use the data to ID time of day, path of travel, seasonal migration. Lots more.

You do not have to upload the data, it can be stored on a SD card and you can parse the data yourself. The main difficulty in self parsing is: you get thousands of images of waving leaves, grass and branches and a few snaps of something worth looking at like a skunk.

It’s like a RING camera in concept except portable.

april •
[February 21, 2023 11:50 AM](https://www.schneier.com/blog/archives/2023/02/the-insecurity-of-photo-cropping.html/#comment-418141)

Winter,

> I try to solve these problems by converting (exporting) “cropped” photographs to .PNG. But I must admit that I do not know how, or even if, this would affect the metadata.

It depends on the program. PNG supports metadata, and a program may try to be “helpful” and copy it from the original image. Be sure to review the available settings of the export process. Or just take a screenshot of the original image (preferably with the viewer and “saver” being separate programs) and export that; it’s unlikely many programmers would go to the trouble of writing code to grab metadata from the program(s) being screenshotted.

If you’re really concerned, make a specific effort to clean the metadata. Programs including pngcrush, jpegtran, and exiftran can do it, but there are also dedicated programs such as “Metadata anonymisation toolkit v2” (packaged as “mat2” in Debian and pre-installed in TAILS) that don’t require you to know anything about the format.

(And when removing metadata from JPEGs, make sure the final image opens with correct orientation. It might not if you’ve stripped the rotation metadata; but then again, an unprocessed direct-...