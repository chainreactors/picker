---
title: Misp-Extractor - Tool That Connects To A MISP Instance And Retrieves Attributes Of Specific Types (Such As IP Addresses, URLs, And Hashes)
url: https://buaq.net/go-149687.html
source: unSafe.sh - 不安全
date: 2023-02-17
fetch_date: 2025-10-04T06:50:32.988202
---

# Misp-Extractor - Tool That Connects To A MISP Instance And Retrieves Attributes Of Specific Types (Such As IP Addresses, URLs, And Hashes)

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

![](https://8aqnet.cdn.bcebos.com/9874352e5bbd19ad7ac55fce2f105b87.jpg)

Misp-Extractor - Tool That Connects To A MISP Instance And Retrieves Attributes Of Specific Types (Such As IP Addresses, URLs, And Hashes)

This code connects to a given MISP (Malware Information Sharing Platform) server and parses
*2023-2-16 19:30:0
Author: [www.kitploit.com(查看原文)](/jump-149687.htm)
阅读量:25
收藏*

---

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEirkuUXFuFisOj31sHr6yUODLiit7jImL8i0JbgePkHWCW1kGILGhqQ5ObMloMllQvbFHCiHhvGa6FtlXj2CvHTAm8dMxJgBqUHXK8nYDwz2qRjhNwyJ-CyuPHgOj1WDJnUjydrd_HlHd03LsyXgRzyhLqUc0wRbslHazfIETdtp_1KrbWrKXJxSXkLyg/w400-h400/misp-extractor.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEirkuUXFuFisOj31sHr6yUODLiit7jImL8i0JbgePkHWCW1kGILGhqQ5ObMloMllQvbFHCiHhvGa6FtlXj2CvHTAm8dMxJgBqUHXK8nYDwz2qRjhNwyJ-CyuPHgOj1WDJnUjydrd_HlHd03LsyXgRzyhLqUc0wRbslHazfIETdtp_1KrbWrKXJxSXkLyg/s1024/misp-extractor.png)

This code connects to a given [MISP](https://www.kitploit.com/search/label/MISP "MISP") (Malware [Information Sharing](https://www.kitploit.com/search/label/Information%20Sharing "Information Sharing") Platform) server and parses a given number of events, writing the IP addresses, URLs, and MD5 [hashes](https://www.kitploit.com/search/label/Hashes "hashes") found in the events to three separate files.

To use this script, you will need to provide the URL of your MISP instance and a [valid](https://www.kitploit.com/search/label/Valid "valid") API key. You can then call the MISPConnector.run() method to retrieve the attributes and save them to files.

To use the code, run the following command:

```
python3 misp_connector.py --misp-url <MISP_URL> --misp-key <MISP_API_KEY> --limit <EVENT_LIMIT>
```

## Supported attribute types

The MISPConnector class currently supports the following attribute types:

* ip-src
* ip-dst
* md5
* url
* domain

If an attribute of one of these types is found in an event, it will be added to the appropriate set (for example, IP addresses will be added to the network\_set) and written to the corresponding file (network.txt, hash.txt, or url.txt).

The code can be configured by passing arguments to the command-line script. The available arguments are:

* misp-url: The URL of the MISP server. This argument is required.
* misp-key: The API key for the MISP server. This argument is required.
* limit: The maximum number of events to parse. The default is 2000.

This script has the following limitations:

* It only retrieves attributes of specific types (as listed above).
* It only writes the retrieved attributes to files, without any further processing or analysis.
* It only retrieves a maximum of 2000 events, as specified by the limit parameter in the misp.search() method.

This code is provided under the MIT License. See the LICENSE file for more details.

Misp-Extractor - Tool That Connects To A MISP Instance And Retrieves Attributes Of Specific Types (Such As IP Addresses, URLs, And Hashes)
![Misp-Extractor - Tool That Connects To A MISP Instance And Retrieves Attributes Of Specific Types (Such As IP Addresses, URLs, And Hashes)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEirkuUXFuFisOj31sHr6yUODLiit7jImL8i0JbgePkHWCW1kGILGhqQ5ObMloMllQvbFHCiHhvGa6FtlXj2CvHTAm8dMxJgBqUHXK8nYDwz2qRjhNwyJ-CyuPHgOj1WDJnUjydrd_HlHd03LsyXgRzyhLqUc0wRbslHazfIETdtp_1KrbWrKXJxSXkLyg/s72-w400-c-h400/misp-extractor.png)
Reviewed by Zion3R
on
8:30 AM
Rating: 5

文章来源: http://www.kitploit.com/2023/02/misp-extractor-tool-that-connects-to.html
 如有侵权请联系:admin#unsafe.sh

© [unSafe.sh - 不安全](https://unsafe.sh) Powered By [PaperCache](https://github.com/code-scan/PaperCache)

* admin#unsafe.sh
* [安全马克](https://aq.mk)
* [星际黑客](https://xj.hk)
* [T00ls](https://t00ls.net)