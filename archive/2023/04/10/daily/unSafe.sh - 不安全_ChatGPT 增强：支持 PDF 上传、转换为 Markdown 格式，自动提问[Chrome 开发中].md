---
title: ChatGPT 增强：支持 PDF 上传、转换为 Markdown 格式，自动提问[Chrome 开发中]
url: https://buaq.net/go-157759.html
source: unSafe.sh - 不安全
date: 2023-04-10
fetch_date: 2025-10-04T11:29:30.956935
---

# ChatGPT 增强：支持 PDF 上传、转换为 Markdown 格式，自动提问[Chrome 开发中]

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

![](https://8aqnet.cdn.bcebos.com/ee94400ec106d3003de088168fb05bca.jpg)

ChatGPT 增强：支持 PDF 上传、转换为 Markdown 格式，自动提问[Chrome 开发中]

HomeAIChatGPT 增强：支持 PDF 上传、转换为 Markdown 格式，自动提问[Chrome 开发中]
*2023-4-9 11:11:0
Author: [www.appinn.com(查看原文)](/jump-157759.htm)
阅读量:57
收藏*

---

[Home](https://www.appinn.com)

[AI](https://www.appinn.com/category/ai/)

ChatGPT 增强：支持 PDF 上传、转换为 Markdown 格式，自动提问[Chrome 开发中]

青小蛙在偶然间发现了一个正在开发中的 ChatGPT 增强插件 **chatgpt-markdown-and-pdf-extension**，还没有正式命名，也未上架商店。但非常有意思，它能够将 ChatGPT 回复转换为 Markdown 格式，支持上传 PDF 文档让机器人回复，还能根据正则表达式自动提问。@[Appinn](https://www.appinn.com/chatgpt-markdown-and-pdf-extension/)

![ChatGPT 增强：支持 PDF 上传、转换为 Markdown 格式，自动提问[Chrome 开发中] 1](https://static1.appinn.com/images/202304/chatgpt-markdown-and-pdf-extension.jpg!o "ChatGPT 增强：支持 PDF 上传、转换为 Markdown 格式，自动提问[Chrome 开发中] 1")

## sailist/chatgpt-enhancement-extension

先来说上传 PDF 这件事。

### 为 ChatGPT 添加上传 PDF 功能

由于 ChatGPT 不支持上传 PDF，所以这款插件的解决方案是提前设置问题，逐页载入 PDF，自动回答的方式：

![ChatGPT 增强：支持 PDF 上传、转换为 Markdown 格式，自动提问[Chrome 开发中] 2](https://static1.appinn.com/images/202304/pdf_preview.jpg!o "ChatGPT 增强：支持 PDF 上传、转换为 Markdown 格式，自动提问[Chrome 开发中] 2")

青小蛙翻出藏在 macOS 里的比特币白皮书，传给了 ChatGPT。由于字数限制，插件读取 PDF 内容之后，**一页一页的自动发给 ChatGPT**，然后通过预设的提问（右边栏有个小按钮可以展开，如下图），可以使用正则表达式自动提问：

![ChatGPT 增强：支持 PDF 上传、转换为 Markdown 格式，自动提问[Chrome 开发中] 3](https://static1.appinn.com/images/202304/screen-appinn2023-04-08-21-38-53.jpg!o "ChatGPT 增强：支持 PDF 上传、转换为 Markdown 格式，自动提问[Chrome 开发中] 3")

整个处理过程根据 PDF 大小需要一阵子，最后就得到了三问。如果文档里有图表，也会得到一个答案。当然这种针对 PDF 的处理方式，还是有些粗糙，不过比没有强呀 😂

另外，还记得这个嘛：

* [ChatPDF – 让 ChatGPT 帮你读 PDF 文档。不，它说它就是一个 PDF 文件](https://www.appinn.com/chatpdf/)

### 为 ChatGPT 添加 Markdown 格式

针对 ChatGPT 的每一条回复，在顶部都有一个 Markdown 按钮，并且可以方便的复制：

![ChatGPT 增强：支持 PDF 上传、转换为 Markdown 格式，自动提问[Chrome 开发中] 4](https://static1.appinn.com/images/202304/screen-appinn2023-04-08_22_09_16.jpg!o "ChatGPT 增强：支持 PDF 上传、转换为 Markdown 格式，自动提问[Chrome 开发中] 4")

## 获取

* [Github](https://github.com/sailist/chatgpt-enhancement-extension)

并未上架商店，可以直接下载 dist.crx 文件，然后解压缩，再通过开发者模式加载就可以使用了。

---

文章来源: https://www.appinn.com/chatgpt-markdown-and-pdf-extension/
 如有侵权请联系:admin#unsafe.sh

© [unSafe.sh - 不安全](https://unsafe.sh) Powered By [PaperCache](https://github.com/code-scan/PaperCache)

* admin#unsafe.sh
* [安全马克](https://aq.mk)
* [星际黑客](https://xj.hk)
* [T00ls](https://t00ls.net)