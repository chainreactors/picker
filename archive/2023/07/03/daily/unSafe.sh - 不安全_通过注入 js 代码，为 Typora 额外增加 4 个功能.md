---
title: 通过注入 js 代码，为 Typora 额外增加 4 个功能
url: https://buaq.net/go-170989.html
source: unSafe.sh - 不安全
date: 2023-07-03
fetch_date: 2025-10-04T11:52:23.590579
---

# 通过注入 js 代码，为 Typora 额外增加 4 个功能

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

![](https://8aqnet.cdn.bcebos.com/296f1804f454bc4e63ebbd0be8b87f18.jpg)

通过注入 js 代码，为 Typora 额外增加 4 个功能

*2023-7-2 15:35:2
Author: [www.appinn.com(查看原文)](/jump-170989.htm)
阅读量:45
收藏*

---

[Typora](https://www.appinn.com/tag/typora/) 是一款非常优秀的跨平台 [Markdown](https://www.appinn.com/tag/markdown/) 编辑器，原开发者一直在做的，就是一个简单的编辑器。但用户需求是不断增加的，论坛的 @tempUserName 同学就通过注入 js 代码，为 Typora 增加了几个新功能：标签页管理、多关键字搜索、调整表格、只读模式。@Appinn

![通过注入 js 代码，为 Typora 额外增加 4 个功能 1](https://static1.appinn.com/images/202306/appinn-feature-images-2023-07-02t151327-364.png!o "通过注入 js 代码，为 Typora 额外增加 4 个功能 1")

来自[**发现频道**](https://meta.appinn.net/c/faxian/10)，临时用户的分享 <https://meta.appinn.net/t/topic/44934>

## 分享一下我给 Typora 整的标签页管理和多关键字搜索脚本

这位大佬的用户名叫 tempUserName，真临时用户 😂

## Typora 痛点

没有标签页，多开几个文档就找不到北了，只能狂按 alt+Tab。我搜了一下，好多人都在吐槽这点。

第二点是我个人不满：都说笔记是第二大脑，但是几乎所有的笔记软件都不支持多关键字搜索。

> 最常见的场景就是：某个文件存了一个文字片段，要用的时候只能想起`AAA` 、`BBB`、`CCC` 三个关键字，如果使用自带的单关键字搜索`AAA`，搜索结果有几百条。真的很难从上千个文件中找出来目标文件。

存了但是检索不出来，这不就是新时代《诗云》么。

## 脚本效果

### 多关键字搜索

* ctrl+shift+P：打开搜索框
* esc：关闭搜索框
* enter：搜索
* ArrowUp，ArrowDown：方向键上下选中
* click、ctrl+enter：当前窗口打开
* ctrl+click、ctrl+shift+enter：新窗口打开
* drag：拖动输入框可移动搜索框

![通过注入 js 代码，为 Typora 额外增加 4 个功能 2](https://meta-cdn1.appinn.com/uploads/default/original/3X/6/3/63b6270e4601a40e9c71c9c6f72a432914951e07.gif "通过注入 js 代码，为 Typora 额外增加 4 个功能 2")

### 标签页管理

ctrl+鼠标拖动，修改表格的行高列宽。

![通过注入 js 代码，为 Typora 额外增加 4 个功能 3](https://meta-cdn1.appinn.com/uploads/default/original/3X/3/b/3bdb2e3763e80b54fcf243a0f4c6f87a702925c3.gif "通过注入 js 代码，为 Typora 额外增加 4 个功能 3")

### 拖动调整表格大小

[](https://img.appinn.com/wp-content/uploads/2023/07/ezgif.com-resize-6.mp4)

### read\_only.js：只读模式

只读模式下文档不可编辑。快捷键：ctrl+shift+R。

### truncate\_text.js：隐藏前面内容，提高大文件渲染性能

大文件在 Typora 的渲染性能很糟糕，用此脚本隐藏掉前面的内容（只是隐藏显示，不修改文件），提高渲染性能。

* ctrl+shift+B：隐藏最前面的文本段
* ctrl+shift+U：重新显示所有文本段
* ctrl+shift+Y：根据当前可视范围显示上下段

## 安装方式

下载脚本后：

1. 找到 Typora 安装路径，包含 `window.html` 的文件夹 A。（不同版本的 Typora 的文件夹结构可能不同，在我这是 `Typora/resources/app`，推荐使用 everything 找一下）
2. 打开文件夹 A，将源码的 plugin 文件夹粘贴进该文件夹下。
3. 打开文件 `A/window.html`。搜索文件内容 `<script src="./app/window/frame.js" defer="defer"></script>`，并在后面加入 `<script src="./plugin/index.js" defer="defer"></script>`。保存。（不同版本的 Typora 查找的内容可能不同，其实就是查找导入 frame.js 的 script 标签）
4. 重启 Typora。

更多原理、下载及细节参考 [GitHub](https://github.com/obgnail/typora_plugin) 页面。

---

文章来源: https://www.appinn.com/typora-4-plugin/
 如有侵权请联系:admin#unsafe.sh

© [unSafe.sh - 不安全](https://unsafe.sh) Powered By [PaperCache](https://github.com/code-scan/PaperCache)

* admin#unsafe.sh
* [安全马克](https://aq.mk)
* [星际黑客](https://xj.hk)
* [T00ls](https://t00ls.net)