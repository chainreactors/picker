---
title: Catching up with WoofLocker, the most elaborate traffic redirection scheme to tech support scams
url: https://buaq.net/go-174731.html
source: unSafe.sh - 不安全
date: 2023-08-18
fetch_date: 2025-10-04T11:59:00.878699
---

# Catching up with WoofLocker, the most elaborate traffic redirection scheme to tech support scams

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

![](https://8aqnet.cdn.bcebos.com/d9de82ebe3abcd6aa4bbb19c524681b1.jpg)

Catching up with WoofLocker, the most elaborate traffic redirection scheme to tech support scams

Back in January 2020, we blogged about a tech support scam campaign dub
*2023-8-17 19:0:0
Author: [www.malwarebytes.com(查看原文)](/jump-174731.htm)
阅读量:15
收藏*

---

Back in January 2020, we blogged about a tech support scam campaign dubbed [WoofLocker](https://www.malwarebytes.com/blog/news/2020/01/woof-locker-stealthy-browser-locker-tech-support-scam) that was by far using the most complex traffic redirection scheme we had ever seen. In fact, the threat actor had started deploying infrastructure in earnest as early as 2017, about 3 years prior to our publication.

Fast forward to 2023, another 3 years have gone by and this campaign is still going as if nothing has happened. The tactics and techniques are very similar, but the infrastructure is now more robust than before to defeat potential takedown attempts. This change may have been in response to the work we did with web hosting companies and registrars, which only put this operation out of business temporarily.

It is just as difficult to reproduce and study the redirection mechanism now as it was then, especially in light of new fingerprinting checks. By connecting previous indicators of compromise we were able to expand our knowledge about the first iteration of WoofLocker and its new setup.

While we still do not know a lot about who is behind this scheme, we believe it may be the work of different threat actors that specialize in their area of expertise. WoofLocker may very well be a professional toolkit built specifically for advanced web traffic filtering and used exclusively by one customer. Victims that fall for the scam and call the phone number are then redirected to call centres presumably in South Asian countries.

This blog post summarizes our latest findings and provides indicators of compromise that may be helpful to the security community.

## Overview

Contrary to other tech support scam campaigns that often rely on malvertising as a delivery vector, we only observed WoofLocker being distributed via a limited number of compromised websites. The threat actor appears to have gained access to two categories: non adult traffic and adult traffic. That distinction can be seen in the unique redirection URL created for each victim with a parameter called "nad" and "ad" respectively.

Malicious JavaScript embedded in the compromised websites is used to retrieve the WoofLocker framework directly into the DOM from one of a handful of domain names. The code used by WoofLocker is highly obfuscated and makes use of steganography, a technique that embeds data inside of images.

Each victim that visits the compromised site is fingerprinted to determine if they are legitimate or not. Numerous checks are performed to detect the presence of virtual machines, certain browser extensions and security tools. Only genuine residential IP addresses are considered, provided they have not already been fingerprinted.

*![WoofLocker overview](https://www.malwarebytes.com/blog/threat-intelligence/2023/08/easset_upload_file87532_275989_e.png)**Figure 1: WoofLocker version 2 diagram*

The information from victims is sent back to the server as a PNG image (the data is hidden inside thanks to steganography) and followed by two possible outcomes. Users deemed not interesting will not see anything further, while potential victims will get redirected to another domain via a URL generated on the fly, with a unique ID only valid for this specific session.

This redirection shows the familiar browser locker screen with a fake warning about computer viruses. That part of the code is relatively straightforward and inspired by existing templates.

## Compromised sites

As mentioned earlier, the threat actor is using two different types of traffic: adult and non adult. The majority of websites loading WoofLocker are adult sites and this is not a coincidence as it plays into the scam's social engineering tactics.

Originally, the injected code was not obfuscated and contained the fingerprinting checks but in 2021 the threat actors changed it, to simply the injection and move some of the logic outside:

![Code compare](https://www.malwarebytes.com/blog/threat-intelligence/2023/08/easset_upload_file58241_275989_e.png)

*Figure 2: Code injected into compromised sites (comparison)*

In the image below, we are using Chrome's Developer Tools to see malicious code dynamically injected into the DOM. As a website administrator going directly to the raw HTML page, you might not see anything injected.

![](https://www.malwarebytes.com/blog/threat-intelligence/2023/08/easset_upload_file90778_275989_e.png)

*Figure 3: Code viewed in developer tools*

This code allows the threat actor to connect with their fingerprinting and redirection infrastructure, which in this case is located at cdncontentstorage[.]com.

## Fingerprinting

We previously described the fingerprinting mechanism in detail and it remains very similar. There were a few additions though, such as the check for specific Chrome extensions (GeoEdge, Kaspersky, McAfee). There also seems to be some kind of proxy detection, or perhaps detection specific to web debugging tools like Fiddler. This makes it much harder for security researchers to get a traffic capture as evidence of malfeasance.

![Extensions](https://www.malwarebytes.com/blog/threat-intelligence/2023/08/easset_upload_file54475_275989_e.png)

*Figure 4: Chrome extensions checks*

The following Python script can be used to decode the PNG image containing the fingerprinting JavaScript (thank you [Jason Reaves](https://medium.com/%40jason.reaves) for sharing):

```
from PIL import Image
import sys

# Driver Code
if __name__ == '__main__' :
	image = Image.open(sys.argv[1], 'r')
	data = ''
	imgdata = image.getdata()
	tt = []
	for i in range(len(imgdata)):
		tt.append(imgdata[i][0])
		tt.append(imgdata[i][1])
		tt.append(imgdata[i][2])
	for i in range(len(tt)):
		ar = 57 ^ tt[i]
		if ar >= 32:
			data += chr(ar)

	open(sys.argv[1]+'.decode', 'w').write(data)
```

![Decoded PNG](https://www.malwarebytes.com/blog/threat-intelligence/2023/08/easset_upload_file52991_275989_e.png)

*Figure 5: Decoded output from PNG image*

## URL redirection

We were able to identify the redirection URL this time, after numerous replays and debugging attempts:

![](https://www.malwarebytes.com/blog/threat-intelligence/2023/08/easset_upload_file47423_275989_e.png)

*Figure 6: Browser locker URL is sent hidden in PNG image*

Again, the threat actor uses steganography to include JavaScript code inside of an image. The browser reads that response via the getImageData function and executes it. Here, we can see the URL that is unique to this session (uid) and used for the redirect to the browser locker page.

## Web traffic

We were able to record a full traffic capture despite WoofLocker's evasion techniques. As mentioned previously, it appears that certain tools that involve proxying traffic may be detected. We had to use a different mechanism to get this traffic without being detected.

Sequentially, we see the fingerprinting checks being done with the use of steganography. The absence of the specific Chrome extensions the threat actor is looking for also generates some traffic. The final part is the user data validation and creation of a unique id (uid). The code once again uses steganography to load the malicious URL corresponding to the browser locker page.

![](https://www.malwarebytes.com/blog/threat-intelligence/2023/08/easset_...