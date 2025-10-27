---
title: Amazon CloudFront 免费 CDN 初体验
url: https://h4ck.org.cn/2024/11/18486
source: obaby@mars
date: 2024-11-11
fetch_date: 2025-10-06T19:14:01.593124
---

# Amazon CloudFront 免费 CDN 初体验

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

# Amazon CloudFront 免费 CDN 初体验

2024年11月10日
[45 条评论](https://h4ck.org.cn/2024/11/18486#comments)

[![](https://h4ck.org.cn/wp-content/uploads/2024/11/2024_04_18_08_39_IMG_2767-tuya.jpg)](https://h4ck.org.cn/wp-content/uploads/2024/11/2024_04_18_08_39_IMG_2767-tuya.jpg)

前几天在[呆哥](https://dai.ge/146.html)的博客看到了为网站添加cloudfront的文章，于是昨天把一个没套cdn的域名尝试给加上了cdn。

具体添加的步骤按照呆哥的文章操作就可以啦，然而，在添加完cdn之后，却一直出现问题，报502错误。

按照之前的配置方式，直接添加的http的回源，很可能是这个回源问题，尝试添加http回源，发现http是能访问的。但是https的不行，猜测可能是aws的回源校验证书了，本地服务器用的都是同一个证书（h4ck.org.cn），如果校验证书有效性，那肯定是无法创建链接的。重新申请免费证书之后，这个问题算是解决了。

然而还有另外一个诡异的问题，那就是https://www.obaby.org.cn可以访问，但是https://obaby.org.cn无法访问,报403错误。参考官方的文档，提示是cname问题，域名是dnspod解析的直接给@添加的cname记录。不过这个做法按照dns的国际做法其实是不受支持的，不能直接给@添加cname解析的。只好将域名解析切换到he.net重新创建alias解析。

[![](https://h4ck.org.cn/wp-content/uploads/2024/11/Screenshot-2024-11-10-084314.png)](https://h4ck.org.cn/wp-content/uploads/2024/11/Screenshot-2024-11-10-084314.png)

然而问题依旧，猜测还是配置问题。后来才发现这个东西的异常之处，按照理解添加域名之后，不在需要添加额外的cname了。

[![](https://h4ck.org.cn/wp-content/uploads/2024/11/Screenshot-2024-11-10-084858.png)](https://h4ck.org.cn/wp-content/uploads/2024/11/Screenshot-2024-11-10-084858.png)

然而事实上却是，这个东西不管添加的的时候创建的域名是什么，在这里都需要把添加的时候的域名加进去才能正常匹配到这个cname。

[![](https://h4ck.org.cn/wp-content/uploads/2024/11/Screenshot-2024-11-10-085134.png)](https://h4ck.org.cn/wp-content/uploads/2024/11/Screenshot-2024-11-10-085134.png)

另外一个就是这个源里面的，源域的问题，最外侧的这个名称其实无关紧要。

[![](https://h4ck.org.cn/wp-content/uploads/2024/11/Screenshot-2024-11-10-085328.png)](https://h4ck.org.cn/wp-content/uploads/2024/11/Screenshot-2024-11-10-085328.png)

需要设置的是内部的original domain:

[![](https://h4ck.org.cn/wp-content/uploads/2024/11/Screenshot-2024-11-10-085306.png)](https://h4ck.org.cn/wp-content/uploads/2024/11/Screenshot-2024-11-10-085306.png)

这个对应的才是回源的配置。经过上面的设置之后，终于两个域名都能用了，并且，顺便把ipv6也给开启了。

测速效果，V4:

[![](https://h4ck.org.cn/wp-content/uploads/2024/11/Screenshot-2024-11-09-214446.png)](https://h4ck.org.cn/wp-content/uploads/2024/11/Screenshot-2024-11-09-214446.png) [![](https://h4ck.org.cn/wp-content/uploads/2024/11/Screenshot-2024-11-09-214256.png)](https://h4ck.org.cn/wp-content/uploads/2024/11/Screenshot-2024-11-09-214256.png)

v6速度：

[![](https://h4ck.org.cn/wp-content/uploads/2024/11/Screenshot-2024-11-09-213926.png)](https://h4ck.org.cn/wp-content/uploads/2024/11/Screenshot-2024-11-09-213926.png)

后台地址：

<https://console.aws.amazon.com>

☆版权☆

\* 网站名称：**[obaby@mars](https://h4ck.org.cn/)**
\* 网址：<https://h4ck.org.cn/>
\* 个性：<https://oba.by/>
\* 本文标题： [《Amazon CloudFront 免费 CDN 初体验》](https://h4ck.org.cn/2024/11/18486)
\* 本文链接：<https://h4ck.org.cn/2024/11/18486>
\* 短链接：<https://oba.by/?p=18486>
\* 转载文章请标明文章来源，原文标题以及原文链接。请遵从 [《署名-非商业性使用-相同方式共享 2.5 中国大陆 (CC BY-NC-SA 2.5 CN) 》](https://creativecommons.org/licenses/by-nc-sa/2.5/cn/)许可协议。

---

[aws](https://h4ck.org.cn/tags/aws)[CDN](https://h4ck.org.cn/tags/cdn)[CloudFront](https://h4ck.org.cn/tags/cloudfront)

[Previous Post](https://h4ck.org.cn/2024/11/18501)
[Next Post](https://h4ck.org.cn/2024/11/18473)

![obaby](https://gg.lang.bi/avatar/d6ebc088df916bcc9e8b94a09f9b0f604e57be54b04bd520c6db2492740fc563?s=90&d=identicon&r=r)

#### obaby

爱好广泛的火星小妖精，有问题欢迎留言交流啊~(✪ω✪)
爬虫类工具请先点击这个链接查看用法https://oba.by/?p=12240
闺蜜圈APP下载 https://guimiquan.cn

#### 猜你喜欢：

2020年8月21日

#### [Porn Data Anaylize — Hadoop安装](https://h4ck.org.cn/2020/08/7357)

2023年1月10日

#### [诱惑](https://h4ck.org.cn/2023/01/10971)

2022年8月21日

#### [微图坊爬虫 [Chrome Support]【22.08.21】【Windows】](https://h4ck.org.cn/2022/08/10397)

### 45 comments

1. ![](https://gg.lang.bi/avatar/f708fe332792fb965837fec42b58154ece68b3d2d608dfb006b39535a2a901ba?s=64&d=identicon&r=r) **[段先森](https://www.duanxiansen.com/)**说道：

   [2024年11月10日 09:38](https://h4ck.org.cn/2024/11/18486#comment-120844)

   ![Level 4](https://badgen.net/badge/亲密度/Level 4/yellow?icon=codebeat)

   ![Microsoft Edge 119](https://h4ck.org.cn/wp-content/plugins/wp-useragent/img/16/net/edge-2.png "Microsoft Edge 119") Microsoft Edge 119 ![Windows 10](https://h4ck.org.cn/wp-content/plugins/wp-useragent/img/16/os/win-6.png "Windows 10") Windows 10 ![cn](https://h4ck.org.cn/wp-content/plugins/wp-useragent/show-useragent/flags_svg/cn.svg "cn")

   有免费的不白嫖岂不可惜

   [回复](#comment-120844)

   1. ![](https://gg.lang.bi/avatar/d6ebc088df916bcc9e8b94a09f9b0f604e57be54b04bd520c6db2492740fc563?s=64&d=identicon&r=r)

      [2024年11月10日 09:58](https://h4ck.org.cn/2024/11/18486#comment-120845)

      ![公主](https://badgen.net/badge/管理员/小妖精/ff91a4?icon=terminal) ![Queen](https://badgen.net/badge/角色/女王/red?icon=matrix)

      ![Google Chrome 126](https://h4ck.org.cn/wp-content/plugins/wp-useragent/img/16/net/chrome.png "Google Chrome 126") Google Chrome 126 ![Android 10](https://h4ck.org.cn/wp-content/plugins/wp-useragent/img/16/os/android.png "Android 10") Android 10 ![cn](https://h4ck.org.cn/wp-content/plugins/wp-useragent/show-useragent/flags_svg/cn.svg "cn")

      果断嫖啊

      [回复](#comment-120845)
   2. ![](https://gg.lang.bi/avatar/518463de57aced5daaa0d49e288c7dae67b8eb9f40233a1e8880804ebee704d2?s=64&d=identicon&r=r)

      [2024年11月10日 17:06](https://h4ck.org.cn/2024/11/18486#comment-120871)

      ![](https://badgen.net/badge/友链/集美们/blue?icon=chrome) ![Level 3](https://badgen.net/badge/亲密度/Level 3/green?icon=codebeat)

      ![Google Chrome 109](https://h4ck.org.cn/wp-content/plugins/wp-useragent/img/16/net/chrome.png "Google Chrome 109") Google Chrome 109 ![Windows 10](https://h4ck.org.cn/wp-content/plugins/wp-useragent/img/16/os/win-6.png "Windows 10") Windows 10 ![cn](https://h4ck.org.cn/wp-content/plugins/wp-useragent/show-useragent/flags_svg/cn.svg "cn")

      小段说的对 ![cool](https://h4ck.org.cn/wp-content/plugins/kama-wp-smile/packs/qip/cool.gif)

      [回复](#comment-120871)
2. ![](https://gg.lang.bi/avatar/35f5b036116cd9e4772887e32f5505296b5286160160fc3bbfd6263465f856c4?s=64&d=identicon&r=r)

   [2024年11月10日 09:58](https://h4ck.org.cn/2024/11/18486#comment-120846)

   ![Level 4](https://badgen.net/badge/亲密度/Level 4/yellow?icon=codebeat)

   ![Google Chrome 118](https://h4ck.org.cn/wp-content/plugins/wp-useragent/img/16/net/chrome.png "Google Chrome 118") Google Chrome 118 ![Windows 11](https://h4ck.org.cn/wp-content/plugins/wp-useragent/img/16/os/win-6.png "Windows 11") Windows 11 ![cn](https://h4ck.org.cn/wp-content/plugins/wp-useragent/show-useragent/flags_svg/cn.svg "cn")

   全站切换cdn还有各种邮箱解析也要改呀，太麻烦了。

   [回复](#comment-120846)

   1. ![](https://gg.lang.bi/avatar/d6ebc088df916bcc9e8b94a09f9b0f604e57be54b04bd520c6db2492740fc563?s=64&d=identicon&r=r)

      [2024年11月10日 10:00](https://h4ck.org.cn/2024/11/18486#comment-120848)

      ![公主](https://badgen.net/badge/管理员/小妖精/ff91a4?icon=terminal) ![Queen](https://badgen.net/badge/角色/女王/red?icon=matrix)

      ![Google Chrome 126](https://h4ck.org.cn/wp-content/plugins/wp-useragent/img/16/net/chrome.png "Google Chrome 126") Google Chrome 126 ![Android 10](https://h4ck.org.cn/wp-content/plugins/wp-useragent/img/16/os/android.png "Android 10") Android 10 ![cn](https://h4ck.org.cn/wp-content/plugins/wp-useragent/show-useragent/flags_svg/cn.svg "cn")

      我这个是切了ns 所以有些麻烦 一般是不需要哒

      [回复](#comment-120848...