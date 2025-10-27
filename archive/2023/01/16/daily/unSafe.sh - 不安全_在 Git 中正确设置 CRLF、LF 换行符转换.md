---
title: 在 Git 中正确设置 CRLF、LF 换行符转换
url: https://buaq.net/go-145613.html
source: unSafe.sh - 不安全
date: 2023-01-16
fetch_date: 2025-10-04T03:58:49.160335
---

# 在 Git 中正确设置 CRLF、LF 换行符转换

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

![]()

在 Git 中正确设置 CRLF、LF 换行符转换

前言CRLF、LF 是用来表示文本换行的方式。CR (Car­riage Re­turn) 代表回车，对应字符 \r，LF (Line Feed) 代表
*2023-1-15 14:38:0
Author: [blog.upx8.com(查看原文)](/jump-145613.htm)
阅读量:20
收藏*

---

## 前言

CRLF、LF 是用来表示文本换行的方式。CR (Car­riage Re­turn) 代表回车，对应字符 `\r`，LF (Line Feed) 代表换行，对应字符 `\n`。由于历史原因，不同的操作系统文本使用的换行符各不相同。主流的操作系统一般使用 CRLF 或者 LF 作为其文本的换行符。其中，Win­dows 系统使用的是 CRLF, Unix 系统 (包括 Linux、Ma­cOS 近些年的版本) 使用的是 LF。

## 修改 Git 配置

### core.autocrlf

Git 提供了一个名为 `core.autocrlf` 的配置，可以自动完成标准化与转换。它的设置方式如下：

```
git config --global core.autocrlf  [true | input | false]  # 全局设置
git config --local core.autocrlf  [true | input | false] # 针对本项目设置
```

* `true` 提交时转换为LF，检出时转换为CRLF
* `input` 提交时转换为LF，检出时不转换
* `false` 提交与检出的代码都保持文件原有的换行符不变（不转换）

> CRLF 与 LF 混合的文本文件不受此配置控制。

在文本编辑器可选换行符，且知道如何正确选择的情况下，其实无需进行任何设置。但为了防止在开发非 Win­dows 项目时不小心使用了 CRLF ，可以进行如下设置，这样在提交 (com­mit) 时换行符会转换为 LF。

```
git config --global core.autocrlf input
```

对于偶尔会开发 Win­dows 项目的开发者，可以单独对 Win­dows 项目进行设置，来保留 CRLF 。

```
git config --local core.autocrlf false
```

### core.safecrlf

由于没有一个绝对有效的算法来判断一个文件是否为文本，所以 Git 提供了一项禁止 / 警告不可逆转换的配置来防止错误的标准化与转换。它主要是影响到多种换行符混合的文件，我们可以手动将其转换为同一种换行符：

```
git config --global core.safecrlf [true | false | warn]
```

* `true` 禁止提交混合换行符的文本文件(git add 的时候会被拦截，提示异常)
* `warn` 提交混合换行符的文本文件的时候发出警告，但是不会阻止 git add 操作
* `false` 不禁止提交混合换行符的文本文件（默认配置）

## 参考资料

[理解 CRLF，LF](https://www.jianshu.com/p/ec9564fe1c2b)

[自定义 Git - 配置 Git](https://www.freesion.com/article/12301224348/)

文章来源: https://blog.upx8.com/3184
 如有侵权请联系:admin#unsafe.sh

© [unSafe.sh - 不安全](https://unsafe.sh) Powered By [PaperCache](https://github.com/code-scan/PaperCache)

* admin#unsafe.sh
* [安全马克](https://aq.mk)
* [星际黑客](https://xj.hk)
* [T00ls](https://t00ls.net)