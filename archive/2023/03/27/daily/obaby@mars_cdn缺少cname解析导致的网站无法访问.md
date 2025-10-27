---
title: cdn缺少cname解析导致的网站无法访问
url: https://h4ck.org.cn/2023/03/cdn%e7%bc%ba%e5%b0%91cname%e8%a7%a3%e6%9e%90%e5%af%bc%e8%87%b4%e7%9a%84%e7%bd%91%e7%ab%99%e6%97%a0%e6%b3%95%e8%ae%bf%e9%97%ae/
source: obaby@mars
date: 2023-03-27
fetch_date: 2025-10-04T10:45:19.062227
---

# cdn缺少cname解析导致的网站无法访问

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

[博客相关『Blogger/WordPress』](https://h4ck.org.cn/cats/jyzj/wordp)

# cdn缺少cname解析导致的网站无法访问

2023年3月26日
[4 条评论](https://h4ck.org.cn/2023/03/11639#comments)

[![](https://image.h4ck.org.cn/wp-content/uploads/2023/03/cdd4b34c8c7540f1fbe9246efdf442bc.jpg)](https://image.h4ck.org.cn/wp-content/uploads/2023/03/cdd4b34c8c7540f1fbe9246efdf442bc.jpg)

这个问题其实应该是一直存在的，不过由于访问博客用的没有带www的网址，所以一直没发现问题。上周末的时候用手机打开带www前缀的域名提示网站未备案无法坊问，当时还以为是cdn节点问题。今天把个人信息的网址链接修改了一下，鼠标放上去加载的时候直接提示404了，这个就很奇怪。

[![](https://image.h4ck.org.cn/wp-content/uploads/2023/03/搜狗截图20230326203353.png)](https://image.h4ck.org.cn/wp-content/uploads/2023/03/%E6%90%9C%E7%8B%97%E6%88%AA%E5%9B%BE20230326203353.png)

直接访问链接，又出现上周末看到的错误：

[![](https://image.h4ck.org.cn/wp-content/uploads/2023/03/搜狗截图20230326202749.png)](https://image.h4ck.org.cn/wp-content/uploads/2023/03/%E6%90%9C%E7%8B%97%E6%88%AA%E5%9B%BE20230326202749.png)

这才想起来可能是没有添加www的CNAME记录，于是登录后台重新添加了带www前缀的CNAME域名，然後一切问题就都解决了。

☆版权☆

\* 网站名称：**[obaby@mars](https://h4ck.org.cn/)**
\* 网址：<https://h4ck.org.cn/>
\* 个性：<https://oba.by/>
\* 本文标题： [《cdn缺少cname解析导致的网站无法访问》](https://h4ck.org.cn/2023/03/11639)
\* 本文链接：<https://h4ck.org.cn/2023/03/11639>
\* 短链接：<https://oba.by/?p=11639>
\* 转载文章请标明文章来源，原文标题以及原文链接。请遵从 [《署名-非商业性使用-相同方式共享 2.5 中国大陆 (CC BY-NC-SA 2.5 CN) 》](https://creativecommons.org/licenses/by-nc-sa/2.5/cn/)许可协议。

---

[CDN](https://h4ck.org.cn/tags/cdn)[cname](https://h4ck.org.cn/tags/cname)[WordPress](https://h4ck.org.cn/tags/wordpress)

[Previous Post](https://h4ck.org.cn/2023/03/11659)
[Next Post](https://h4ck.org.cn/2023/03/11620)

![obaby](https://gg.lang.bi/avatar/d6ebc088df916bcc9e8b94a09f9b0f604e57be54b04bd520c6db2492740fc563?s=90&d=identicon&r=r)

#### obaby

爱好广泛的火星小妖精，有问题欢迎留言交流啊~(✪ω✪)
爬虫类工具请先点击这个链接查看用法https://oba.by/?p=12240
闺蜜圈APP下载 https://guimiquan.cn

#### 猜你喜欢：

2012年5月10日

#### [WordPress jQuery隐藏侧边栏](https://h4ck.org.cn/2012/05/4061)

2023年2月26日

#### [忙碌的周末吖](https://h4ck.org.cn/2023/02/11292)

2010年11月12日

#### [诡异的“可疑恶意站点”](https://h4ck.org.cn/2010/11/2136)

### 4 comments

1. ![](https://gg.lang.bi/avatar/a3187abab7f61b0c43efc6d88384d1c643d359defed5874a2a3b60e979effc83?s=64&d=identicon&r=r) **[梦](http://www.mzyq.com)**说道：

   [2023年3月27日 16:49](https://h4ck.org.cn/2023/03/11639#comment-93832)

   ![](https://badgen.net/badge/友链/集美们/blue?icon=chrome) ![Level 5](https://badgen.net/badge/亲密度/Level 5/orange?icon=codebeat)

   ![Google Chrome 109](https://h4ck.org.cn/wp-content/plugins/wp-useragent/img/16/net/chrome.png "Google Chrome 109") Google Chrome 109 ![Windows 10](https://h4ck.org.cn/wp-content/plugins/wp-useragent/img/16/os/win-6.png "Windows 10") Windows 10 ![cn](https://h4ck.org.cn/wp-content/plugins/wp-useragent/show-useragent/flags_svg/cn.svg "cn")

   这……
   大佬疏忽了啊？

   [回复](#comment-93832)

   1. ![](https://gg.lang.bi/avatar/d6ebc088df916bcc9e8b94a09f9b0f604e57be54b04bd520c6db2492740fc563?s=64&d=identicon&r=r)

      [2023年3月27日 18:38](https://h4ck.org.cn/2023/03/11639#comment-93834)

      ![公主](https://badgen.net/badge/管理员/小妖精/ff91a4?icon=terminal) ![Queen](https://badgen.net/badge/角色/女王/red?icon=matrix)

      ![Google Chrome 102](https://h4ck.org.cn/wp-content/plugins/wp-useragent/img/16/net/chrome.png "Google Chrome 102") Google Chrome 102 ![Mac OS X 10.15](https://h4ck.org.cn/wp-content/plugins/wp-useragent/img/16/os/mac-3.png "Mac OS X 10.15") Mac OS X 10.15 ![cn](https://h4ck.org.cn/wp-content/plugins/wp-useragent/show-useragent/flags_svg/cn.svg "cn")

      确实是大意了~~~忘了www这茬啦~~ ![wacko](https://h4ck.org.cn/wp-content/plugins/kama-wp-smile/packs/qip/wacko.gif)

      [回复](#comment-93834)
2. ![](https://gg.lang.bi/avatar/1c03767b0691f80231895255661bcf42eceab95dc8b493ee80c835b07f577f49?s=64&d=identicon&r=r)

   [2023年3月29日 01:33](https://h4ck.org.cn/2023/03/11639#comment-93893)

   ![](https://badgen.net/badge/友链/集美们/blue?icon=chrome) ![Level 6](https://badgen.net/badge/亲密度/Level 6/red?icon=codebeat)

   ![Microsoft Edge 111](https://h4ck.org.cn/wp-content/plugins/wp-useragent/img/16/net/edge-2.png "Microsoft Edge 111") Microsoft Edge 111 ![Windows 10](https://h4ck.org.cn/wp-content/plugins/wp-useragent/img/16/os/win-6.png "Windows 10") Windows 10 ![cn](https://h4ck.org.cn/wp-content/plugins/wp-useragent/show-useragent/flags_svg/cn.svg "cn")

   出现碎图了哦！

   [回复](#comment-93893)

   1. ![](https://gg.lang.bi/avatar/d6ebc088df916bcc9e8b94a09f9b0f604e57be54b04bd520c6db2492740fc563?s=64&d=identicon&r=r)

      [2023年3月29日 08:41](https://h4ck.org.cn/2023/03/11639#comment-93908)

      ![公主](https://badgen.net/badge/管理员/小妖精/ff91a4?icon=terminal) ![Queen](https://badgen.net/badge/角色/女王/red?icon=matrix)

      ![Google Chrome 102](https://h4ck.org.cn/wp-content/plugins/wp-useragent/img/16/net/chrome.png "Google Chrome 102") Google Chrome 102 ![Mac OS X 10.15](https://h4ck.org.cn/wp-content/plugins/wp-useragent/img/16/os/mac-3.png "Mac OS X 10.15") Mac OS X 10.15 ![cn](https://h4ck.org.cn/wp-content/plugins/wp-useragent/show-useragent/flags_svg/cn.svg "cn")

      嗯嗯，百度云加速挂了，现在他们官网能访问，我的图片域名还是挂着的。

      [回复](#comment-93908)

### 发表回复 [取消回复](/2023/03/11639#respond)

您的邮箱地址不会被公开。 必填项已用 \* 标注

评论 \*

显示名称 \*

邮箱 \*

网站

[ ]  在此浏览器中保存我的显示名称、邮箱地址和网站地址，以便下次评论时使用。

[x] 如果有人回复我的评论，请通过电子邮件通知我。

[x]

Δ

### 标签云[Tag Cloud]

Your browser doesn't support the HTML5 CANVAS tag.

* [ASM](https://h4ck.org.cn/tags/asm)
* [PETools](https://h4ck.org.cn/tags/petools)
* [OD](https://h4ck.org.cn/tags/od)
* [爬虫](https://h4ck.org.cn/tags/%E7%88%AC%E8%99%AB)
* [Debugger](https://h4ck.org.cn/tags/debugger)
* [iOS](https://h4ck.org.cn/tags/ios)
* [心情](https://h4ck.org.cn/tags/myfeeling)
* [秀人集](https://h4ck.org.cn/tags/%E7%A7%80%E4%BA%BA%E9%9B%86)
* [yolov5](https://h4ck.org.cn/tags/yolov5)
* [系统美化](https://h4ck.org.cn/tags/os-diy)
* [驱动开发](https://h4ck.org.cn/tags/driver-develop)
* [CentOS](https://h4ck.org.cn/tags/centos)
* [PE](https://h4ck.org.cn/tags/pe)
* [php](https://h4ck.org.cn/tags/php)
* [月经](https://h4ck.org.cn/tags/%E6%9C%88%E7%BB%8F)
* [Delphi](https://h4ck.org.cn/tags/delphi)
* [Python](https://h4ck.org.cn/tags/python)
* [妹子图](https://h4ck.org.cn/tags/%E5%A6%B9%E5%AD%90%E5%9B%BE)
* [UniApp](https://h4ck.org.cn/tags/uniapp)
* [Android](https://h4ck.org.cn/tags/android)
* [Windows](https://h4ck.org.cn/tags/windows)
* [QQ](https://h4ck.org.cn/tags/qq)
* [Google](https://h4ck.org.cn/tags/google)
* [C/C++](https://h4ck.org.cn/tags/cc)
* [ubuntu](https://h4ck.org.cn/tags/ubuntu)
* [Unpack](https://h4ck.org.cn/tags/tuoke)
* [Crack](https://h4ck.org.cn/tags/crack)
* [Linux](https://h4ck.org.cn/tags/linux)
* [OSX](https://h4ck.org.cn/tags/osx)
* [闺蜜圈](https://h4ck.org.cn/tags/%E9%97%BA%E8%9C%9C%E5%9C%88)
* [spider](https://h4ck.org.cn/tags/spider)
* [远程控制](https://h4ck.org.cn/tags/remot-control)
* [文本编辑](https://h4ck.org.cn/tags/texteditor)
* [Virus Analysit](https://h4ck.org.cn/tags/virus-analysit)
* [WordPress](https://h4ck.org.cn/tags/wordpress)
* [无题](https://h4ck.org.cn/tags/nomean)
* [美女](https://h4ck.org.cn/tags/beauty)
* [CDN](https://h4ck.org.cn/tags/cdn)
* [大姨妈](https://h4ck.org.cn/tags/%E5%A4%A7%E5%A7%A8%E5%A6%88)
* [杂谈](https://h4ck.org.cn/tags/zatan)
* [IDA](https://h4ck.org.cn/tags/ida)
* [Django](https://h4ck.org.cn/tags/django)
* [jeb](https://h4ck.org.cn/tags/jeb)
* [Plugin](https://h4ck.org.cn/tags/plugi...