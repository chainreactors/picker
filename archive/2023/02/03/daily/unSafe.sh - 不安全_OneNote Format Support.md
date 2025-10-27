---
title: OneNote Format Support
url: https://buaq.net/go-147711.html
source: unSafe.sh - 不安全
date: 2023-02-03
fetch_date: 2025-10-04T05:34:02.453507
---

# OneNote Format Support

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

![](https://8aqnet.cdn.bcebos.com/9d293557be4fcbe0d5b784fdcbe7677f.jpg)

OneNote Format Support

Skip to contentMicrosoft OneNote is rising in popularity as a vector for ma
*2023-2-2 19:14:42
Author: [blog.cerbero.io(查看原文)](/jump-147711.htm)
阅读量:20
收藏*

---

[Skip to content](#content)

Microsoft OneNote is rising in popularity as a vector for malware. Therefore, all commercial licenses of Cerbero Suite can now download our “OneNote Format” package from Cerbero Store which parses the OneNote format and extracts embedded files.

Installing the package from Cerbero Store takes only a few mouse clicks.

[![](https://blog.cerbero.io/wp-content/uploads/2023/02/onenote/install.png)](https://blog.cerbero.io/wp-content/uploads/2023/02/onenote/install.png)

Once the package is installed, you can directly inspect OneNote documents in Cerbero Suite and all embedded files are automatically extracted and ready to be inspected

[![](https://blog.cerbero.io/wp-content/uploads/2023/02/onenote/extract.png)](https://blog.cerbero.io/wp-content/uploads/2023/02/onenote/extract.png)

In this image an executable is extracted from the OneNote malware. The executable contains a CAB archive in a resource entry. The CAB archive contains a VBS script which can directly be inspected.

The OneNote package can also be used programmatically.

```
from Pro.Core import *
from Pkg.OneNote.Core import OneNoteObject

def parseOneNoteDocument(fname):
    c = createContainerFromFile(fname)
    if c.isNull():
        return
    obj = OneNoteObject()
    if not obj.Load(c):
        return
    files = obj.GetEmbeddedFiles()
    for file in files:
        print("offset:", hex(file[0]), "size:", hex(file[1]))
```

## Post navigation

文章来源: https://blog.cerbero.io/?p=2516
 如有侵权请联系:admin#unsafe.sh

© [unSafe.sh - 不安全](https://unsafe.sh) Powered By [PaperCache](https://github.com/code-scan/PaperCache)

* admin#unsafe.sh
* [安全马克](https://aq.mk)
* [星际黑客](https://xj.hk)
* [T00ls](https://t00ls.net)