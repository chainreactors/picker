---
title: kaf-cli – 将 txt 小说转换为电子书（EPub、Mobi、azw3），带封面、目录[Win/macOS/Linux/Android]
url: https://buaq.net/go-140486.html
source: unSafe.sh - 不安全
date: 2022-12-19
fetch_date: 2025-10-04T01:53:14.603867
---

# kaf-cli – 将 txt 小说转换为电子书（EPub、Mobi、azw3），带封面、目录[Win/macOS/Linux/Android]

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

![](https://8aqnet.cdn.bcebos.com/7cd4b14cea7763d644b4410265fe5659.jpg)

kaf-cli – 将 txt 小说转换为电子书（EPub、Mobi、azw3），带封面、目录[Win/macOS/Linux/Android]

HomeAndroidkaf-cli – 将 txt 小说转换为电子书（EPub、Mobi、azw3），带封面、目录[Win/macOS/Linux/Android]
*2022-12-18 17:44:5
Author: [www.appinn.com(查看原文)](/jump-140486.htm)
阅读量:43
收藏*

---

[Home](https://www.appinn.com)

[Android](https://www.appinn.com/category/android/)

kaf-cli – 将 txt 小说转换为电子书（EPub、Mobi、azw3），带封面、目录[Win/macOS/Linux/Android]

**kaf-cli** 是一个开源项目，用来自动将 .txt 格式的电子小说转换为 EPub、Mobi、azw3 电子书格式，并且能够自动识别目录、标题，以及添加封面图片。支持 Windows、macOS、Linux，还拥有 Android 版本。@[Appinn](https://www.appinn.com/kaf-cli/)

![kaf-cli - 将 txt 小说转换为电子书（EPub、Mobi、azw3），带封面、目录[Win/macOS/Linux/Android]](https://static1.appinn.com/images/202212/kaf-cli.jpg!o "kaf-cli - 将 txt 小说转换为电子书（EPub、Mobi、azw3），带封面、目录[Win/macOS/Linux/Android] 1")

## kaf-cli

提到 cli（command-line interface），就可以知道这是一款命令行工具，不过不要害怕，使用非常简单。

### 功能

kaf-cli 的功能主要是将 txt 文件转换为 EPub、Mobi、azw3 格式，支持：

* 自定义封面
* 自动识别书名和章节(示例中所有用法都会自动识别)
* 自动识别字符编码(自动解决中文乱码)
* 自定义章节标题识别规则
* 自动给章节正文生成加粗居中的标题
* 自定义标题对齐方式
* 段落自动识别
* 段落自动缩进
* 自定义段落缩进字数
* 自定义段落间距
* 自定义书籍语言
* 知轩藏书格式文件名会自动提取书名和作者, 例: `《希灵帝国》（校对版全本）作者：远瞳.txt`
* 超快速(130章/s以上速度, 4000章30s不到)

实际上，以青小蛙的使用体验来看，对于整理的比较好的 .txt 电子小说，只需要用到自定义封面功能，其他的 kaf-cli 完成的很赞。

### 傻瓜操作模式

虽然是命令行工具，但 kaf-cli 提供了傻瓜式操作模式：

**把 .txt 文件拖到 `kaf-cli.exe` 上面就能完成自动转换**

所以，完全不需要使用命令提示符、终端，也完全不需要使用命令行。

### 自定义封面功能

在傻瓜操作模式下, 如果目录下有 `cover.png` 文件会自动添加为封面、支持 jpg、png 格式。

所以，用起来还是非常容易的。

—-

### 命令行模式

```
Usage of kaf-cli.exe:
  -align string
        标题对齐方式: left、center、righ (default "center")
  -author string
        作者 (default "YSTYLE")
  -bookname string
        书名: 默认为txt文件名
  -bottom string
        段落间距(单位可以为em、px) (default "1em")
  -cover string
        封面图片 (default "cover.png")
  -filename string
        txt 文件名
  -format string
        书籍格式: all、epub、mobi、azw3 (default "all")
  -indent uint
        段落缩进字数 (default 2)
  -lang string
        设置语言: en,de,fr,it,es,zh,ja,pt,ru,nl。 环境变量KAF_CLI_LANG可修改默认值 (default "zh")
  -match string
        匹配标题的正则表达式, 不写可以自动识别, 如果没生成章节就参考教程。例: -match 第.{1,8}章 表示第和章字之间可以有1-8个任意文字 (default "自动匹配,可自定义")
  -max uint
        标题最大字数 (default 35)
  -out string
        输出文件名，不需要包含格式后缀
  -tips
        添加本软件教程 (default true)
```

比如，下面这一句命令行，可以转换 小说.txt 文件，并且设置作者 小众软件，封面 appinn.png，匹配章节 第x节。

```
./kaf-cli -author 小众软件 -filename ./小说.txt -cover appinn.png -match "第.{1,8}节"
```

关于章节，还有几个例子：

* Section 1 ~ Section 100 `-match "Section \d+"`
* Chapter xxx `-match "Chapter .{1,8}"`

还是那句话，自动识别挺好的，先自动，不成功再自定义就好了。

## 获取

* [官网](https://ystyle.top/2019/12/31/txt-converto-epub-and-mobi/)
* [GitHub](https://github.com/ystyle/kaf-cli)
* [Android](https://github.com/ystyle/kaf-cli/releases/tag/android)
* [百度盘](https://kutt.appinn.com/PnOeak)（开发者提供）

百度盘中还有Wi-Fi传书、漫画转换等几个工具

### Android 版本

这个就更方便了，可以直接在 Android 里转换：

![kaf-cli - 将 txt 小说转换为电子书（EPub、Mobi、azw3），带封面、目录[Win/macOS/Linux/Android] 1](https://static1.appinn.com/images/202212/kaf2.jpg!o "kaf-cli - 将 txt 小说转换为电子书（EPub、Mobi、azw3），带封面、目录[Win/macOS/Linux/Android] 2")

---

文章来源: https://www.appinn.com/kaf-cli/
 如有侵权请联系:admin#unsafe.sh

© [unSafe.sh - 不安全](https://unsafe.sh) Powered By [PaperCache](https://github.com/code-scan/PaperCache)

* admin#unsafe.sh
* [安全马克](https://aq.mk)
* [星际黑客](https://xj.hk)
* [T00ls](https://t00ls.net)