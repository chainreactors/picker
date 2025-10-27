---
title: SVG Steganography, (Mon, May 26th)
url: https://isc.sans.edu/diary/rss/31978
source: SANS Internet Storm Center, InfoCON: green
date: 2025-05-27
fetch_date: 2025-10-06T22:31:11.864280
---

# SVG Steganography, (Mon, May 26th)

# [Internet Storm Center](/)

[Sign In](/login.html)
[Sign Up](/register.html)

Handler on Duty: [Johannes Ullrich](/handler_list.html#johannes-ullrich "Johannes Ullrich")

Threat Level: [green](/infocon.html)

* [previous](/diary/31976)
* [next](/diary/31980)

My next class:

|  |  |  |
| --- | --- | --- |
| [Application Security: Securing Web Apps, APIs, and Microservices](https://www.sans.org/event/dallas-2025/course/application-security-securing-web-apps-api-microservices) | Dallas | Dec 1st - Dec 6th 2025 |

# [SVG Steganography](/forums/diary/SVG%2BSteganography/31978/)

**Published**: 2025-05-26. **Last Updated**: 2025-05-26 16:31:33 UTC
**by** [Johannes Ullrich](https://plus.google.com/101587262224166552564?rel=author) (Version: 1)

[0 comment(s)](/diary/SVG%2BSteganography/31978/#comments)

Didier recently published several diaries related to steganography. I have to admit that steganography isn't exactly my favorite topic. It is one of those "neat" infosec toys, but its applicability is limited. Data exfiltration usually does not require proper steganography, but just appending data to an image will usually work just fine.

On the other hand, it looks like the kids still like and enjoy diaries about steganography. For one of my recent podcasts, a viewer left a message asking about the use of SVG images for steganography, to avoid some of the loss issues with compressed image formats [1]. Image formats break down into two basic types: Bitmap and vector image formats. Most images you see are bitmap or pixel-based. These formats tend to be easier to create and display. However, they have the disadvantage of not being able to scale up, and the image size can become quite large, which in turn requires compression. While there are some commonly used lossless compression formats, many image formats accept some loss in detail to enhance compression. Steganography takes advantage of similar colors being indistinguishable from each other. However, the same issue is used by compression algorithms. Neighboring pixels with similar colors are often approximated by changing them all to the same color, simplifying compression.

The images below use JPEG compression. The "uncompressed" version on the left is 130kBytes, while the compressed version is around 23kBytes. For a quick glance, the images are identical, but if you zoom in a bit, you will probably see the "blockiness" of the compressed image caused by adjusting the colors. This compression would wipe out any steganography message

|  |  |
| --- | --- |
| ![](https://isc.sans.edu/diaryimages/images/IMG_2025.jpg) | ![](https://isc.sans.edu/diaryimages/images/IMG_2025_lowres.jpg) |
| uncompressed | compressed |

Vector-based images, on the other hand, describe pictures as vectors. This allows for arbitrary scaling of the images and can lead to smaller image formats, in particular for simple but large format images. On the web, "SVG" is particularly popular. SVG is based on XML, and can easily be embedded in HTML. For regular images, the "data:" URL would have to be used, which is quite clumsy for more complex images. For example, the menu icons on the left are embedded as SVG images. The little "house" for the link to "Homepage" is represented by this SVG snippet:

> `<svg style="width:20px;height:20px" viewBox="0 0 24 24">
>     <path fill="currentColor" d="M10,20V14H14V20H19V12H22L12,3L2,12H5V20H10Z"></path>
> </svg>`

The "path" describes the image shape. Even more complex images can be expressed as SVG, and bitmaps can be converted into SVG. For example, the dog above as an SVG using the Adobe SVG converter:

![](/diaryimages/images/LaiFu.svg)

You may notice that the image takes a moment to build, and it is 4 MB in size. But this, in turn, provides plenty of opportunity for steganography. Most SVG steganography tools I could find use pretty much the same method used for pixel-based images: They adjust the color of individual areas slightly [2][3]. For a complex SVG as the one shown above, this works pretty well.

But vector-based images offer another opportunity: You may add additional "vectors", without changing the look of the image. For example, a line can be split into two lines.

![](https://isc.sans.edu/diaryimages/images/Screenshot%202025-05-26%20at%2012_22_42%E2%80%AFPM.png)

A value can be encoded in the ratio of x and y. One advantage of SVG is that coordinates are expressed as floats, not integers. The image format is independent of its actual size. So it would be easy to encode a byte as (x+y)/y\*255 in each line. Or even increasing this to two bytes would be doable. Decoding the image would not require a special "key" like for most other steganography algorithms. Instead, the recipient just needs to know that all lines that continue each other are encoding data. For an observer, it would be noticeable if an image contains a lot of "continuing" lines. But the same is true for more steganography schemes: If an observer is aware of the steganography method, they will at least be able to detect that there is a message, and in some cases they will be able to extract it. To truly protect the message, it must first be encrypted before it is encoded into the image.

But even for SVG-encoded images, there is a change that later compression or optimization will remove the details encoded in the image, but it is less likely that a lossy compression is used on SVG.

Bevore implementing any of that... let me walk my dogs. Maybe there will be a follow-up diary later this week with a script.

[1] https://www.youtube.com/watch?v=QN4ecl9hQ80
[2] http://paper.ijcsns.org/07\_book/201910/20191016.pdf
[3] https://github.com/japplebaum/svgsteg

---
Johannes B. Ullrich, Ph.D. , Dean of Research, [SANS.edu](https://sans.edu)
[Twitter](https://jbu.me/164)|

Keywords: [steganography](/tag.html?tag=steganography) [svg](/tag.html?tag=svg)

[0 comment(s)](/diary/SVG%2BSteganography/31978/#comments)

My next class:

|  |  |  |
| --- | --- | --- |
| [Application Security: Securing Web Apps, APIs, and Microservices](https://www.sans.org/event/dallas-2025/course/application-security-securing-web-apps-api-microservices) | Dallas | Dec 1st - Dec 6th 2025 |

* [previous](/diary/31976)
* [next](/diary/31980)

### Comments

[Login here to join the discussion.](/login)

Top of page

×

![modal content]()

[Diary Archives](/diaryarchive.html)

* [![SANS.edu research journal](https://isc.sans.edu/images/researchjournal5.png)](/j/research)
* [Homepage](/index.html)
* [Diaries](/diaryarchive.html)
* [Podcasts](/podcast.html)
* [Jobs](/jobs)
* [Data](/data)
  + [TCP/UDP Port Activity](/data/port.html)
  + [Port Trends](/data/trends.html)
  + [SSH/Telnet Scanning Activity](/data/ssh.html)
  + [Weblogs](/weblogs)
  + [Domains](/data/domains.html)
  + [Threat Feeds Activity](/data/threatfeed.html)
  + [Threat Feeds Map](/data/threatmap.html)
  + [Useful InfoSec Links](/data/links.html)
  + [Presentations & Papers](/data/presentation.html)
  + [Research Papers](/data/researchpapers.html)
  + [API](/api)
* [Tools](/tools/)
  + [DShield Sensor](/howto.html)
  + [DNS Looking Glass](/tools/dnslookup)
  + [Honeypot (RPi/AWS)](/tools/honeypot)
  + [InfoSec Glossary](/tools/glossary)
* [Contact Us](/contact.html)
  + [Contact Us](/contact.html)
  + [About Us](/about.html)
  + [Handlers](/handler_list.html)* [About Us](/about.html)

[Slack Channel](/slack/index.html)

[Mastodon](https://infosec.exchange/%40sans_isc)

[Bluesky](https://bsky.app/profile/sansisc.bsky.social)

[X](https://twitter.com/sans_isc)

![](/adimg.html?id=)

© 2025 SANS™ Internet Storm Center
Developers: We have an [API](/api/) for you!   [![Creative Commons License](/images/cc.png)](https://creativecommons.org/licenses/by-nc-sa/4.0/)

* [Link To Us](/linkback.html)
* [About Us](/about.html)
* [Handlers](/handler_list.html)
* [Privacy Policy](/privacy.html)