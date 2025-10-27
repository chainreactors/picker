---
title: Amazon CloudFront 免费 CDN 配置教程
url: https://h4ck.org.cn/2024/11/18501
source: obaby@mars
date: 2024-11-11
fetch_date: 2025-10-06T19:14:00.531451
---

# Amazon CloudFront 免费 CDN 配置教程

[![obaby@mars](/wp-content/uploads/2023/08/logo-pink-small.png)](https://h4ck.org.cn)

Artificial Intelligence / Reverse Engineering / Internet of Things / Full Stack Developer

* [※说说/Talk※](https://h4ck.org.cn/talk)
* [※留言/Msg※](https://h4ck.org.cn/guestbook)
* [※归档/File※](https://h4ck.org.cn/myarchive)
* [※资源/Res※](https://h4ck.org.cn/res-page)
* [※我是谁/Me※](https://h4ck.org.cn/whoami)
* [※集美们/Besties※](https://h4ck.org.cn/besties)

 [Menu](#mobilemenu)

* [※说说/Talk※](https://h4ck.org.cn/talk)
* [※留言/Msg※](https://h4ck.org.cn/guestbook)
* [※归档/File※](https://h4ck.org.cn/myarchive)
* [※资源/Res※](https://h4ck.org.cn/res-page)
* [※我是谁/Me※](https://h4ck.org.cn/whoami)
* [※集美们/Besties※](https://h4ck.org.cn/besties)

[业余爱好『Favourite』](https://h4ck.org.cn/cats/cxsj/%E4%B8%9A%E4%BD%99%E7%88%B1%E5%A5%BD%E3%80%8Efavourite%E3%80%8F)

# Amazon CloudFront 免费 CDN 配置教程

2024年11月10日
[18 条评论](https://h4ck.org.cn/2024/11/18501#comments)

[![](https://h4ck.org.cn/wp-content/uploads/2024/11/微信图片_20241110193501.jpg)](https://h4ck.org.cn/wp-content/uploads/2024/11/%E5%BE%AE%E4%BF%A1%E5%9B%BE%E7%89%87_20241110193501.jpg)

[三十海河](https://h4ck.org.cn/2024/11/18486/comment-page-1#comment-120855) 留言文能不能出个教程，下午看了下正好之前给宝子做的博客挂掉了。正好迁移过来，不过不得不说，这个体验的确比较奇怪，cname解析，有的域名能加，有的不能加，这就很离谱。

视频分两段录的，主要是第一段失败了，但是实在不想重新录了。直接看这两段吧。第一段有些问题，第二段也提到了。

整体用起来的感觉就是，很多翻译有些奇怪，包括文档看的也莫名其妙，这个就很蛋疼。

不过好在最后还是成功了，折腾半天，哼唧唧

☆版权☆

\* 网站名称：**[obaby@mars](https://h4ck.org.cn/)**
\* 网址：<https://h4ck.org.cn/>
\* 个性：<https://oba.by/>
\* 本文标题： [《Amazon CloudFront 免费 CDN 配置教程》](https://h4ck.org.cn/2024/11/18501)
\* 本文链接：<https://h4ck.org.cn/2024/11/18501>
\* 短链接：<https://oba.by/?p=18501>
\* 转载文章请标明文章来源，原文标题以及原文链接。请遵从 [《署名-非商业性使用-相同方式共享 2.5 中国大陆 (CC BY-NC-SA 2.5 CN) 》](https://creativecommons.org/licenses/by-nc-sa/2.5/cn/)许可协议。

---

[CDN](https://h4ck.org.cn/tags/cdn)[教程](https://h4ck.org.cn/tags/videos)

[Previous Post](https://h4ck.org.cn/2024/11/18508)
[Next Post](https://h4ck.org.cn/2024/11/18486)

![obaby](https://gg.lang.bi/avatar/d6ebc088df916bcc9e8b94a09f9b0f604e57be54b04bd520c6db2492740fc563?s=90&d=identicon&r=r)

#### obaby

爱好广泛的火星小妖精，有问题欢迎留言交流啊~(✪ω✪)
爬虫类工具请先点击这个链接查看用法https://oba.by/?p=12240
闺蜜圈APP下载 https://guimiquan.cn

#### 猜你喜欢：

2023年7月4日

#### [随机小姐姐测试版](https://h4ck.org.cn/2023/07/12430)

2021年6月21日

#### [秀人集爬虫](https://h4ck.org.cn/2021/06/8353)

2023年9月9日

#### [爱美女网爬虫[预览版] [23.09.09] [Windows]](https://h4ck.org.cn/2023/09/13292)

### 18 comments

1. ![](https://gg.lang.bi/avatar/40c46b2a6ef05464946a7e3f5230bdfa16b5d4e861c7b69977ef77efde66638a?s=64&d=identicon&r=r) **[三十海河](http://ihaihe.cn)**说道：

   [2024年11月10日 20:06](https://h4ck.org.cn/2024/11/18501#comment-120878)

   ![Level 4](https://badgen.net/badge/亲密度/Level 4/yellow?icon=codebeat)

   ![Chrome 130](https://h4ck.org.cn/wp-content/plugins/wp-useragent/img/16/net/chrome.png "Chrome 130") Chrome 130 ![iPhone iOS 18.0](https://h4ck.org.cn/wp-content/plugins/wp-useragent/img/16/device/iphone.png "iPhone iOS 18.0") iPhone iOS 18.0 ![cn](https://h4ck.org.cn/wp-content/plugins/wp-useragent/show-useragent/flags_svg/cn.svg "cn")

   太感谢了，我研究研究，确实需要cdn给图片加速了

   [回复](#comment-120878)
2. ![](https://gg.lang.bi/avatar/378b36848f972f331d59acb5104e9fb96758c96bf0689be3911351c5ad12134a?s=64&d=identicon&r=r)

   [2024年11月10日 20:18](https://h4ck.org.cn/2024/11/18501#comment-120879)

   ![Level 3](https://badgen.net/badge/亲密度/Level 3/green?icon=codebeat)

   ![Microsoft Edge 129](https://h4ck.org.cn/wp-content/plugins/wp-useragent/img/16/net/edge-2.png "Microsoft Edge 129") Microsoft Edge 129 ![Windows 10](https://h4ck.org.cn/wp-content/plugins/wp-useragent/img/16/os/win-6.png "Windows 10") Windows 10 ![cn](https://h4ck.org.cn/wp-content/plugins/wp-useragent/show-useragent/flags_svg/cn.svg "cn")

   亚马逊的免费CDN服务给了多少流量和带宽呢？
   现自己站点用的是国内的CDN服务，速度还不错。
   不明白为何哔哩哔哩这么讨厌，非得要到其站点下才能看清晰版本，无语。

   [回复](#comment-120879)

   1. ![](https://gg.lang.bi/avatar/d6ebc088df916bcc9e8b94a09f9b0f604e57be54b04bd520c6db2492740fc563?s=64&d=identicon&r=r)

      [2024年11月10日 20:44](https://h4ck.org.cn/2024/11/18501#comment-120881)

      ![公主](https://badgen.net/badge/管理员/小妖精/ff91a4?icon=terminal) ![Queen](https://badgen.net/badge/角色/女王/red?icon=matrix)

      ![Google Chrome 126](https://h4ck.org.cn/wp-content/plugins/wp-useragent/img/16/net/chrome.png "Google Chrome 126") Google Chrome 126 ![Windows 10](https://h4ck.org.cn/wp-content/plugins/wp-useragent/img/16/os/win-6.png "Windows 10") Windows 10 ![cn](https://h4ck.org.cn/wp-content/plugins/wp-useragent/show-useragent/flags_svg/cn.svg "cn")

      每月传出 1TB 数据至互联网
      每月 10000000 个 HTTP 或 HTTPS 请求
      每月 200 万次 CloudFront 函数调用
      每月 200 万次 CloudFront KeyValueStore 读取
      免费 SSL 证书

      bilibili的确是这样的

      [回复](#comment-120881)

      1. ![](https://gg.lang.bi/avatar/378b36848f972f331d59acb5104e9fb96758c96bf0689be3911351c5ad12134a?s=64&d=identicon&r=r)

         [2024年11月10日 20:55](https://h4ck.org.cn/2024/11/18501#comment-120883)

         ![Level 3](https://badgen.net/badge/亲密度/Level 3/green?icon=codebeat)

         ![Microsoft Edge 129](https://h4ck.org.cn/wp-content/plugins/wp-useragent/img/16/net/edge-2.png "Microsoft Edge 129") Microsoft Edge 129 ![Windows 10](https://h4ck.org.cn/wp-content/plugins/wp-useragent/img/16/os/win-6.png "Windows 10") Windows 10 ![cn](https://h4ck.org.cn/wp-content/plugins/wp-useragent/show-useragent/flags_svg/cn.svg "cn")

         嗯，那对于个人的博客站点来说是够用啦

         顺便好奇一下，为何`10000000 `不用100万直接表示更加直观，哈。

         [回复](#comment-120883)

         1. ![](https://gg.lang.bi/avatar/d6ebc088df916bcc9e8b94a09f9b0f604e57be54b04bd520c6db2492740fc563?s=64&d=identicon&r=r)

            [2024年11月10日 21:11](https://h4ck.org.cn/2024/11/18501#comment-120884)

            ![公主](https://badgen.net/badge/管理员/小妖精/ff91a4?icon=terminal) ![Queen](https://badgen.net/badge/角色/女王/red?icon=matrix)

            ![Google Chrome 126](https://h4ck.org.cn/wp-content/plugins/wp-useragent/img/16/net/chrome.png "Google Chrome 126") Google Chrome 126 ![Windows 10](https://h4ck.org.cn/wp-content/plugins/wp-useragent/img/16/os/win-6.png "Windows 10") Windows 10 ![cn](https://h4ck.org.cn/wp-content/plugins/wp-useragent/show-useragent/flags_svg/cn.svg "cn")

            因为我是抄来的，哈哈哈

            [回复](#comment-120884)
3. ![](https://gg.lang.bi/avatar/7ca2eb6a07de78fd08989205bc741ef66a4746b1f518fa164f8e71b016366c75?s=64&d=identicon&r=r)

   [2024年11月11日 00:05](https://h4ck.org.cn/2024/11/18501#comment-120887)

   ![Level 6](https://badgen.net/badge/亲密度/Level 6/red?icon=codebeat)

   ![Microsoft Edge 129](https://h4ck.org.cn/wp-content/plugins/wp-useragent/img/16/net/edge-2.png "Microsoft Edge 129") Microsoft Edge 129 ![Windows 11](https://h4ck.org.cn/wp-content/plugins/wp-useragent/img/16/os/win-6.png "Windows 11") Windows 11 ![cn](https://h4ck.org.cn/wp-content/plugins/wp-useragent/show-useragent/flags_svg/cn.svg "cn")

   每月传出 1TB 数据至互联网
   每月 10000000 个 HTTP 或 HTTPS 请求
   每月 200 万次 CloudFront 函数调用
   每月 200 万次 CloudFront KeyValueStore 读取
   免费 SSL 证书

   这个也可以哈！

   [回复](#comment-120887)

   1. ![](https://gg.lang.bi/avatar/d6ebc088df916bcc9e8b94a09f9b0f604e57be54b04bd520c6db2492740fc563?s=64&d=identicon&r=r)

      [2024年11月11日 08:09](https://h4ck.org.cn/2024/11/18501#comment-120892)

      ![公主](https://badgen.net/badge/管理员/小妖精/ff91a4?icon=terminal) ![Queen](https://badgen.net/badge/角色/女王/red?icon=matrix)

      ![Google Chrome 126](https://h4ck.org.cn/wp-content/plugins/wp-useragent/img/16/net/chrome.png "Google Chrome 126") Google Chrome 126 ![Mac OS X 10.15](https://h4ck.org.cn/wp-content/plugins/wp-useragent/img/16/os/mac-3.png "Mac OS X 10.15") Mac OS X 10.15 ![cn](https://h4ck.org.cn/wp-content/plugins/wp-useragent/show-useragent/flags_svg/cn.svg "cn")

      是的，这个量还是非常不错的。

      [回复](#comment-120892)
4. ![](https://gg.lang.bi/avatar/65cd1f408c1cc0949b34d3cd2acad0cb5a2b8c362ebf31ca9ee0dc9edcc63e81?s=64&d=identicon&r=r)

   [2024年11月11日 03:27](https://h4ck.org.cn/2024/11/18501#comment-120889)

   ![](https://bad...