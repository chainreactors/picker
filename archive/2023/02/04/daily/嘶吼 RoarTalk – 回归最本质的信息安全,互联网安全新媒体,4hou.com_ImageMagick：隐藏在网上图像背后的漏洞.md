---
title: ImageMagick：隐藏在网上图像背后的漏洞
url: https://www.4hou.com/posts/GKpL
source: 嘶吼 RoarTalk – 回归最本质的信息安全,互联网安全新媒体,4hou.com
date: 2023-02-04
fetch_date: 2025-10-04T05:39:52.432582
---

# ImageMagick：隐藏在网上图像背后的漏洞

ImageMagick：隐藏在网上图像背后的漏洞 - 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com

[![](https://www.4hou.com/sihou/images/new4hou/newlogoss.png)](https://www.4hou.com)

* [首页](https://www.4hou.com)
* [企业中心](https://www.4hou.com/corp/newindex)
* [产业研究院](https://www.4hou.com/real-time)

![](https://www.4hou.com/sihou/images/new4hou/search-icon.png)

[投稿](https://www.4hou.com/contribute)

[登录](https://www.4hou.com/login)
  |
[注册](https://www.4hou.com/register)

* 导读 ▾
* [活动](https://www.4hou.com/newticket)
* [专题](https://www.4hou.com/category/special)
* [图谱](https://www.4hou.com/atlas/index)
* [报告](https://www.4hou.com/new-report-info)
* [嘶票](https://www.4hou.com/tickets)
* [嘶货](https://www.4hou.com/shop)
* [企业查询](https://www.4hou.com/corp/new-search-company)
* [招聘](https://www.4hou.com/recruit)![](https://www.4hou.com/sihou/images/1561626446625934.png)

* [新闻](https://www.4hou.com/category/news)
* [行业](https://www.4hou.com/category/industry)
* [趋势](https://www.4hou.com/category/observation)
* [访谈](https://www.4hou.com/category/people)
* [漏洞](https://www.4hou.com/category/vulnerable)
* [WEB安全](https://www.4hou.com/category/web)
* [业务安全](https://www.4hou.com/category/business)
* [系统安全](https://www.4hou.com/category/system)
* [内网渗透](https://www.4hou.com/category/penetration)
* [勒索软件](https://www.4hou.com/category/typ)
* [安全工具](https://www.4hou.com/category/tools)

# ImageMagick：隐藏在网上图像背后的漏洞

布加迪
[漏洞](https://www.4hou.com/category/vulnerable)
2023-02-03 12:00:00

![](https://img.4hou.com/article/%E6%B5%8F%E8%A7%88.png)137823

收藏

导语：研究人员在流行的ImageMagick图像处理实用工具中发现了新漏洞。

ImageMagick是一种免费开源软件套件，用于显示、转换和编辑图像文件。它可以对200多种格式的图像文件进行读写操作，因此它在全球网站上很常见，因为我们总是需要为用户的个人资料和目录等内容处理图片。

Ocelot团队在最近的一次高级持续性威胁（APT）模拟活动中发现，ImageMagick在一个基于Dupal的网站中被用于处理图像，因此该团队决定尝试找出该组件中的新漏洞，随后下载了最新版本的ImageMagick（当时是7.1.0-49）。结果发现了两个零日漏洞：

  CVE-2022-44267：ImageMagick 7.1.0-49很容易受到拒绝服务攻击。当它解析PNG图像（比如为了调整大小）时，转换进程可能会等待stdin输入。

  CVE-2022-44268：ImageMagick 7.1.0-49很容易受到信息泄露攻击。当它解析PNG图像（比如为了调整大小）时，生成的图像可能嵌入了任意远程文件的内容（如果ImageMagick二进制代码拥有读取权限）。

**如何触发漏洞利用？**

攻击者需要使用ImageMagick将恶意图像上传到网站，以便远程利用上述漏洞。

Ocelot团队非常感谢ImageMagick的志愿者团队，他们及时地验证并发布了所需的补丁：

https://github.com/ImageMagick/ImageMagick/commit/05673e63c919e61ffa1107804d1138c46547a475

这篇博文解释了这些漏洞的技术细节。

**CVE-2022-44267：拒绝服务**

ImageMagick：7.1.0-49

当ImageMagick解析PNG文件时，比如在收到图像后的调整大小操作中，转换进程可能会因无法处理其他图像而等待stdin输入，导致拒绝服务攻击。

不法分子可以制作PNG或使用现有的PNG，并添加文本块类型（比如tEXt）。这种类型有关键字和文本字符串。如果关键字是字符串“profile”（不带引号），那么ImageMagick将把该文本字符串解释为文件名，并将内容作为原始资料加载。如果指定的文件名是“-”，ImageMagick将尝试从标准输入读取内容，可能会让进程永远等待。

漏洞利用路径执行：

上传图像以触发ImageMagick命令，比如“convert”

ReadOnePNGImage（coders/ png.c: 2164）

![1.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230202/1675314507117839.png "1675314507117839.png")

图1

读取“tEXt”文本块：

![2.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230202/1675314514204578.png "1675314514204578.png")

图2

SetImageProfile（MagickCore / property.c: 4360）：

![3.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230202/1675314523152099.png "1675314523152099.png")

图3

检查关键字是否等于“profile”：

![4.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230202/1675314533132650.png "1675314533132650.png")

图4

在第4720行将文本字符串复制为文件名，在第4722行保存内容：

![5.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230202/1675314542504347.png "1675314542504347.png")

图5

FileToStringInfo将内容存储到string\_info->datum（MagickCore/string.c:1005）：

![6.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230202/1675314629208253.png "1675314629208253.png")

图6

FileToBlob（MagickCore/blob.c:1396）：将stdin分配给文件名作为“-”，导致进程永远等待输入：

![7.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230202/1675314639653417.png "1675314639653417.png")

图7

概念验证（PoC）：恶意PNG文件：

89504e470d0a1a0a0000000d49484452000000010000000108000000003a7e9b550000000b49444154789c63f8ff1f00030001fffc25dc510000000a7445587470726f66696c65002d00600c56a10000000049454e44ae426082

![8.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230202/1675314656271159.png "1675314656271159.png")

图8

证据：恶意图像文件：OCELOT\_output.png

![9.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230202/1675314665103550.png "1675314665103550.png")

图9

Stdin输入永远等待：

![10.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230202/1675314675183576.png "1675314675183576.png")

图10

**CVE-2022-44268：任意远程泄漏**

ImageMagick：7.1.0-49

当ImageMagick解析PNG文件时，比如在调整大小操作中，生成的图像可能嵌入了来自网站的任意远程文件的内容（如果magick二进制代码拥有读取权限）。

不法分子可以制作PNG或使用现有的PNG，并添加文本块类型（比如tEXt）。这种类型有关键字和文本字符串。如果关键字是字符串“profile”（不带引号），那么ImageMagick将把文本字符串解释为文件名，并将内容作为原始资料加载，然后攻击者可以下载大小调整后的图像，该图像随带远程文件的内容。

漏洞利用路径执行：

上传图像以触发ImageMagick命令，比如“convert”

ReadOnePNGImage（coders/ png.c: 2164）：

![11.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230202/1675314686320633.png "1675314686320633.png")

图11

读取tEXt文本块：

![12.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230202/1675314695210560.png "1675314695210560.png")

图12

SetImageProfile（MagickCore / property.c: 4360）

![13.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230202/1675314713979830.png "1675314713979830.png")

图13

检查关键字是否等于“profile”：

![14.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230202/1675314734119299.png "1675314734119299.png")

图14

在第4720行将文本字符串复制为文件名，在第4722行保存内容：

![15.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230202/1675314746188933.png "1675314746188933.png")

图15

FileToStringInfo将内容存储到string\_info->datum（MagickCore/string.c:1005）：

![16.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230202/1675314761970926.png "1675314761970926.png")

图16

如果提供了一个有效（且可以访问）的文件名，内容将返回给调用者函数（FileToStringInfo）， StringInfo对象将返回给SetImageProperty函数，将blob保存到生成的新图像中，这要感谢SetImageProfile函数：

![17.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230202/1675314776476648.png "1675314776476648.png")

图17

这个新图像可供攻击者下载，其中嵌入了任意网站文件内容。

PoC：恶意PNG内容泄露“/etc/passwd”文件：

89504e470d0a1a0a0000000d4948445200000001000000010100000000376ef9240000000a49444154789c636800000082008177cd72b6000000147445587470726f66696c65002f6574632f70617373776400b7f46d9c0000000049454e44ae426082

![18.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230202/1675314788363635.png "1675314788363635.png")

图18

证据：

通过profile->datum变量，/etc/passwd的内容存储在图像中：

![19.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230202/1675314798169364.png "1675314798169364.png")

图19

![20.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230202/1675314809459292.png "1675314809459292.png")

图20

/etc/passwd内容的十六进制表示，内容从图像中提取：

![21.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230202/1675314822182161.png "1675314822182161.png")

图21

来自网站中/etc/passwd的内容，在生成的图像中收到：

![22.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230202/1675314900192165.png "1675314900192165.png")图22

显示漏洞利用的视频：

![23.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230202/1675314921100564.png "1675314921100564.png")

图23

本文翻译自：https://www.metabaseq.com/imagemagick-zero-days/如若转载，请注明原文地址

* 分享至

![取消](https://www.4hou.com/sihou/images/close.jpg)
![嘶吼](https://www.4hou.com/sihou/images/logo.png)

感谢您的支持，我会继续努力的!

![扫码支持]( "扫一扫")

打开微信扫一扫后点击右上角即可分享哟

### 发表评论

评论

![](https://www.4hou.com/captcha/flat?XNpgiU8f)

#### 你可能感兴趣的

* [![]()

  Salesloft: GitHub账户遭入侵 导致Drift令牌被盗并引发大规模Salesforce数据窃取](https://www.4hou.com/posts/33NQ)
* [![]()

  TP-Link确认路由器存在未修复零日漏洞](https://www.4hou.com/posts/YZ8p)
* [![]()

  黑客借助HexStrike-AI工具可快速利用新型漏洞](https://www.4hou.com/posts/PGyn)
* [![]()

  黑客利用Sitecore零日漏洞部署WeepSteel侦察恶意软件](https://www.4hou.com/posts/RXAR)
* [![]()

  Docker Desktop严重漏洞可让攻击者劫持Windows主机](https://www.4hou.com/posts/omzK)
* [![]()

  WinRAR 零日漏洞被利用在解压档案时植入恶意软件](https://www.4hou.com/posts/vw4m)

![](https://img.4hou.com/portraits/10321ac81c30432685d31a710b4220de.jpg)

# [布加迪](https://www.4hou.com/member/VGrO)

IT英汉译匠，字典迷（尤爱英汉字典），酷爱羽毛球

#### 最新文章

* [Salesloft: GitHub账户遭入侵 导致Drift令牌被盗并引发大规模Salesforce数据窃取](h...