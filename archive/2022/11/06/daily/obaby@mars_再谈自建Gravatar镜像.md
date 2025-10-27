---
title: 再谈自建Gravatar镜像
url: https://h4ck.org.cn/2022/11/%e5%86%8d%e8%b0%88%e8%87%aa%e5%bb%bagravatar%e9%95%9c%e5%83%8f/
source: obaby@mars
date: 2022-11-06
fetch_date: 2025-10-03T21:49:04.359207
---

# 再谈自建Gravatar镜像

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

# 再谈自建Gravatar镜像

2022年11月5日
[19 条评论](https://h4ck.org.cn/2022/11/10671#comments)

![](https://image.h4ck.org.cn/wp-content/uploads/2022/10/0eecd1b654d916102a60e76deee87016.jpg)

今天上午建了一个gravatar镜像服务，下午看了一下oss里面的文件，乱七八糟什么东西都有。dujun说的很对，一旦公开服务了可能会发生各种事情。

刚才登录看了一下，倒是不出意料，什么东西都有，连gravatar的js css文件都缓存过来了：

![](https://image.h4ck.org.cn/wp-content/uploads/2022/11/搜狗截图20221105201708.jpg)

这就有点超出预期了，于是重新改了缓存规则，至于怎么改的就不写了。同时弄了个静态页：

![](https://image.h4ck.org.cn/wp-content/uploads/2022/11/搜狗截图20221105201817.jpg)

重新定义了404页面：

![](https://image.h4ck.org.cn/wp-content/uploads/2022/11/搜狗截图20221105201835.jpg)

☆版权☆

\* 网站名称：**[obaby@mars](https://h4ck.org.cn/)**
\* 网址：<https://h4ck.org.cn/>
\* 个性：<https://oba.by/>
\* 本文标题： [《再谈自建Gravatar镜像》](https://h4ck.org.cn/2022/11/10671)
\* 本文链接：<https://h4ck.org.cn/2022/11/10671>
\* 短链接：<https://oba.by/?p=10671>
\* 转载文章请标明文章来源，原文标题以及原文链接。请遵从 [《署名-非商业性使用-相同方式共享 2.5 中国大陆 (CC BY-NC-SA 2.5 CN) 》](https://creativecommons.org/licenses/by-nc-sa/2.5/cn/)许可协议。

---

[Cravatar](https://h4ck.org.cn/tags/cravatar)[Gravatar](https://h4ck.org.cn/tags/gravatar)[WordPress](https://h4ck.org.cn/tags/wordpress)

[Previous Post](https://h4ck.org.cn/2022/11/10677)
[Next Post](https://h4ck.org.cn/2022/11/10659)

![obaby](https://gg.lang.bi/avatar/d6ebc088df916bcc9e8b94a09f9b0f604e57be54b04bd520c6db2492740fc563?s=90&d=identicon&r=r)

#### obaby

爱好广泛的火星小妖精，有问题欢迎留言交流啊~(✪ω✪)
爬虫类工具请先点击这个链接查看用法https://oba.by/?p=12240
闺蜜圈APP下载 https://guimiquan.cn

#### 猜你喜欢：

2023年11月16日

#### [去掉 jetpack 给 wp admin bar 添加的通知模块](https://h4ck.org.cn/2023/11/14285)

2022年9月15日

#### [WordPress 评论显示IP归属地插件–WP-UserAgent[增强版]](https://h4ck.org.cn/2022/09/10469)

2009年9月25日

#### [WordPress 正文添加标签选项](https://h4ck.org.cn/2009/09/264)

### 19 comments

1. ![](https://gg.lang.bi/avatar/ffe079586b4cbcb80e308ac87712f9d5c8d4918b4e6c5f00d68a0be009891cae?s=64&d=identicon&r=r) **[胡一派](https://yipai.me)**说道：

   [2022年11月5日 20:43](https://h4ck.org.cn/2022/11/10671#comment-88585)

   ![Level 3](https://badgen.net/badge/亲密度/Level 3/green?icon=codebeat)

   ![Firefox 108](https://h4ck.org.cn/wp-content/plugins/wp-useragent/img/16/net/firefox.png "Firefox 108") Firefox 108 ![Mac OS X 10.10](https://h4ck.org.cn/wp-content/plugins/wp-useragent/img/16/os/mac-3.png "Mac OS X 10.10") Mac OS X 10.10 ![cn](https://h4ck.org.cn/wp-content/plugins/wp-useragent/show-useragent/flags_svg/cn.svg "cn")

   用cloudflare workers做省事儿多了。

   [回复](#comment-88585)

   1. ![](https://gg.lang.bi/avatar/d6ebc088df916bcc9e8b94a09f9b0f604e57be54b04bd520c6db2492740fc563?s=64&d=identicon&r=r)

      [2022年11月5日 20:45](https://h4ck.org.cn/2022/11/10671#comment-88586)

      ![公主](https://badgen.net/badge/管理员/小妖精/ff91a4?icon=terminal) ![Queen](https://badgen.net/badge/角色/女王/red?icon=matrix)

      ![Google Chrome 104](https://h4ck.org.cn/wp-content/plugins/wp-useragent/img/16/net/chrome.png "Google Chrome 104") Google Chrome 104 ![Windows 10](https://h4ck.org.cn/wp-content/plugins/wp-useragent/img/16/os/win-6.png "Windows 10") Windows 10 ![cn](https://h4ck.org.cn/wp-content/plugins/wp-useragent/show-useragent/flags_svg/cn.svg "cn")

      用这个怎么做？没试过

      [回复](#comment-88586)

      1. ![](https://gg.lang.bi/avatar/ffe079586b4cbcb80e308ac87712f9d5c8d4918b4e6c5f00d68a0be009891cae?s=64&d=identicon&r=r)

         [2022年11月5日 20:50](https://h4ck.org.cn/2022/11/10671#comment-88587)

         ![Level 3](https://badgen.net/badge/亲密度/Level 3/green?icon=codebeat)

         ![Firefox 117](https://h4ck.org.cn/wp-content/plugins/wp-useragent/img/16/net/firefox.png "Firefox 117") Firefox 117 ![GNU/Linux](https://h4ck.org.cn/wp-content/plugins/wp-useragent/img/16/os/linux.png "GNU/Linux") GNU/Linux ![cn](https://h4ck.org.cn/wp-content/plugins/wp-useragent/show-useragent/flags_svg/cn.svg "cn")

         谷歌搜索：cloudflare 反代 gravatar

         [回复](#comment-88587)

         1. ![](https://gg.lang.bi/avatar/d6ebc088df916bcc9e8b94a09f9b0f604e57be54b04bd520c6db2492740fc563?s=64&d=identicon&r=r)

            [2022年11月5日 21:04](https://h4ck.org.cn/2022/11/10671#comment-88589)

            ![公主](https://badgen.net/badge/管理员/小妖精/ff91a4?icon=terminal) ![Queen](https://badgen.net/badge/角色/女王/red?icon=matrix)

            ![Google Chrome 104](https://h4ck.org.cn/wp-content/plugins/wp-useragent/img/16/net/chrome.png "Google Chrome 104") Google Chrome 104 ![Windows 10](https://h4ck.org.cn/wp-content/plugins/wp-useragent/img/16/os/win-6.png "Windows 10") Windows 10 ![cn](https://h4ck.org.cn/wp-content/plugins/wp-useragent/show-useragent/flags_svg/cn.svg "cn")

            试了一下，连系统部署完了之后的域名都访问不通。workers.dev直接就挂了。

            [回复](#comment-88589)

            1. ![](https://gg.lang.bi/avatar/ffe079586b4cbcb80e308ac87712f9d5c8d4918b4e6c5f00d68a0be009891cae?s=64&d=identicon&r=r)

               [2022年11月5日 21:09](https://h4ck.org.cn/2022/11/10671#comment-88590)

               ![Level 3](https://badgen.net/badge/亲密度/Level 3/green?icon=codebeat)

               ![Google Chrome 105](https://h4ck.org.cn/wp-content/plugins/wp-useragent/img/16/net/chrome.png "Google Chrome 105") Google Chrome 105 ![Windows 11](https://h4ck.org.cn/wp-content/plugins/wp-useragent/img/16/os/win-6.png "Windows 11") Windows 11 ![cn](https://h4ck.org.cn/wp-content/plugins/wp-useragent/show-useragent/flags_svg/cn.svg "cn")

               不可能吧，你肯定哪里没做对。我博客就是用cloudflare反代的gravatar。绑定的域名要先随便添加一个A记录（ip随便填，只是用来添加A记录），这样才会被转发。

               [回复](#comment-88590)

               1. ![](https://gg.lang.bi/avatar/d6ebc088df916bcc9e8b94a09f9b0f604e57be54b04bd520c6db2492740fc563?s=64&d=identicon&r=r)

                  [2022年11月5日 21:21](https://h4ck.org.cn/2022/11/10671#comment-88593)

                  ![公主](https://badgen.net/badge/管理员/小妖精/ff91a4?icon=terminal) ![Queen](https://badgen.net/badge/角色/女王/red?icon=matrix)

                  ![Google Chrome 104](https://h4ck.org.cn/wp-content/plugins/wp-useragent/img/16/net/chrome.png "Google Chrome 104") Google Chrome 104 ![Windows 10](https://h4ck.org.cn/wp-content/plugins/wp-useragent/img/16/os/win-6.png "Windows 10") Windows 10 ![cn](https://h4ck.org.cn/wp-content/plugins/wp-useragent/show-useragent/flags_svg/cn.svg "cn")

                  ok了。跑通了~~~~

                  [回复](#comment-88593)
2. ![](https://gg.lang.bi/avatar/d838166f05390e17979f10c8e0fcc3b1d719369e6450e9eb30f218d8579263ee?s=64&d=identicon&r=r)

   [2022年11月5日 21:23](https://h4ck.org.cn/2022/11/10671#comment-88595)

   ![](https://badgen.net/badge/用户/已认证/CCFF33?icon=rss) ![](https://badgen.net/badge/友链/集美们/blue?icon=chrome) ![Level 7](https://badgen.net/badge/亲密度/Level 7/pink?icon=codebeat)

   ![Safari 16](https://h4ck.org.cn/wp-content/plugins/wp-useragent/img/16/net/safari.png "Safari 16") Safari 16 ![iPhone iOS 16.1](https://h4ck.org.cn/wp-content/plugins/wp-useragent/img/16/device/iphone.png "iPhone iOS 16.1") iPhone iOS 16.1 ![cn](https://h4ck.org.cn/wp-content/plugins/wp-useragent/show-useragent/flags_svg/cn.svg "cn")

   “ 不惮以最坏的恶意揣测别人”是至理名言

   [回复](#comment-88595)

   1. ![](https://gg.lang.bi/avatar/d6ebc088df916bcc9e8b94a09f9b0f604e57be54b04bd520c6db2492740fc563?s=64&d=identicon&r=r)

      [2022年11月5日 21:24](https://h4ck.org.cn/2022/11/10671#comment-88596)

      ![公主](https://badgen...