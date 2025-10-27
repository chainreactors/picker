---
title: Yet More ImageMagick Vulnerabilities
url: https://buaq.net/go-148166.html
source: unSafe.sh - 不安全
date: 2023-02-07
fetch_date: 2025-10-04T05:50:08.494578
---

# Yet More ImageMagick Vulnerabilities

* [unSafe.sh - 不安全](https://unsafe.sh)
* [我的收藏](/user/collects)
* [今日热榜](/?hot=true)
* [公众号文章](/?gzh=true)
* [导航](/nav/index)
* [Github CVE](/cve)
* [Github Tools](/tools)
* [编码/解码](/encode)
* [文件传输](/share/index)
* [Twitter Bot](https://twitter.com/buaqbot)
* [Telegram Bot](https://t.me/aqinfo)
* [Search](/search/search)

[Rss](/rss.xml)

[ ]
黑夜模式

![](https://8aqnet.cdn.bcebos.com/cdd53bbfd3f11c206575c533c6c17cf8.jpg)

Yet More ImageMagick Vulnerabilities

ImageMagick is a popular open-source image manipulation library used by many websites and sof
*2023-2-6 17:49:7
Author: [lab.wallarm.com(查看原文)](/jump-148166.htm)
阅读量:34
收藏*

---

ImageMagick is a popular open-source image manipulation library used by many websites and software applications to process and display images. A couple of vulnerabilities have recently been discovered in ImageMagick by [MetabaseQ](https://www.metabaseq.com/imagemagick-zero-days).

Two vulnerabilities CVE-2022-44267 and CVE-2022-44268 allow attackers to arbitrarily read files and cause DoS on the affected system. The payload to exploit this vulnerability is simple, which makes it easier for attackers to take advantage of the vulnerability.

![CVE-2022-44267 payload](https://i0.wp.com/lab.wallarm.com/wp-content/uploads/2023/02/Example-of-first-exploitation-payload.jpeg?resize=710%2C131&ssl=1)

Payload exploiting CVE-2022-44267 makes ImageMagick try to read the content from standard input, potentially leaving the process waiting forever.

![CVE-2022-44268 payload](https://i0.wp.com/lab.wallarm.com/wp-content/uploads/2023/02/Example-of-second-exploitation-payload.jpeg?resize=708%2C144&ssl=1)

Example of second exploitation payload

[ImageMagick](https://www.imagemagick.org/) is a widely used open-source image manipulation library because of its versatility and ease of use. It provides a suite of command-line tools and a library that can be used to perform a wide range of image-processing tasks, such as resizing, cropping, and converting images between different formats.

Many popular software applications and websites use ImageMagick to process and display images. For example, some content management systems (CMS), such as WordPress and Drupal, use ImageMagick to resize and crop images uploaded by users. ImageMagick has also been integrated into many software development tools, such as programming languages like PHP, Ruby, and Python, making it easier for developers to incorporate image-processing capabilities into their applications.

It is important for users and administrators to stay vigilant and keep their software updated to ensure that they are protected from potential security threats. Additionally, users and administrators should carefully evaluate the image sources they work with and limit the types of image formats that ImageMagick is configured to process.

[Wallarm End-to-End API Security](https://www.wallarm.com/product/api-security-platform) can protect against this type of attack. The [Wallarm Detection](https://docs.wallarm.com/about-wallarm/detecting-vulnerabilities/) Team has checked these new exploit vectors for Imagemagick and has definitively determined that our product will protect your applications.

文章来源: https://lab.wallarm.com/yet-more-imagemagick-vulnerabilities/
 如有侵权请联系:admin#unsafe.sh

© [unSafe.sh - 不安全](https://unsafe.sh) Powered By [PaperCache](https://github.com/code-scan/PaperCache)

* admin#unsafe.sh
* [安全马克](https://aq.mk)
* [星际黑客](https://xj.hk)
* [T00ls](https://t00ls.net)