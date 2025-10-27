---
title: 基于Dnspod的ddns
url: https://h4ck.org.cn/2024/05/16929
source: obaby@mars
date: 2024-05-09
fetch_date: 2025-10-06T17:13:39.951390
---

# 基于Dnspod的ddns

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

[后台开发『BackEnd』](https://h4ck.org.cn/cats/cxsj/backend)

# 基于Dnspod的ddns

2024年5月8日
[37 条评论](https://h4ck.org.cn/2024/05/16929#comments)

[![](https://h4ck.org.cn/wp-content/uploads/2024/05/cgi-bin_mmwebwx-bin_webwxgetmsgimg__MsgID7794979151019771527skey@crypt_b542c6c0_2a53c7990637fc8bc35c1a7e520b0f9ammweb_appidwx_webfilehelper-rotated.jpg)](https://h4ck.org.cn/wp-content/uploads/2024/05/cgi-bin_mmwebwx-bin_webwxgetmsgimg__MsgID7794979151019771527skey%40crypt_b542c6c0_2a53c7990637fc8bc35c1a7e520b0f9ammweb_appidwx_webfilehelper.jpg)

虽然，路由器提供了ddns功能，但是有个比较坑爹的问题就是修改路由器的dns服务器之后，路由器自动断开重新拨号了。重新拨号导致的问题就是ip地址变了，而路由器带的动态dns ttl有效期应该是6-10分钟左右。

也就意味着在这段时间内，cdn无法回源了，今天想着直接用dnspod的解析来动态修改。搜索了以下找到了这么个开源代码：

https://gitcode.com/strahe/dnspod-ddns/

跑了一下代码能用，但是在配置文件出错的情况下依然继续执行，这个就有点抑郁了。都出错了下次跑下去还是错的，有啥意义呢？

于是修改了一下代码，进行了部分调整：

```
调整配置文件路径为统一路径，不通系统分开意义不大
修复配置文件错误依然继续执行的问题
输出dnspod错误提示，根据错误提示可以大概知道自己是哪里配置错了
```

实际效果：

[![](https://h4ck.org.cn/wp-content/uploads/2024/05/Screenshot-2024-05-08-165632.png)](https://h4ck.org.cn/wp-content/uploads/2024/05/Screenshot-2024-05-08-165632.png)

在使用前先去dnspod后台添加解析，然后使用工具进行ip地址更新，否则可能会报错。

代码地址：

https://github.com/obaby/dnspod-ddns

☆版权☆

\* 网站名称：**[obaby@mars](https://h4ck.org.cn/)**
\* 网址：<https://h4ck.org.cn/>
\* 个性：<https://oba.by/>
\* 本文标题： [《基于Dnspod的ddns》](https://h4ck.org.cn/2024/05/16929)
\* 本文链接：<https://h4ck.org.cn/2024/05/16929>
\* 短链接：<https://oba.by/?p=16929>
\* 转载文章请标明文章来源，原文标题以及原文链接。请遵从 [《署名-非商业性使用-相同方式共享 2.5 中国大陆 (CC BY-NC-SA 2.5 CN) 》](https://creativecommons.org/licenses/by-nc-sa/2.5/cn/)许可协议。

---

[ddns](https://h4ck.org.cn/tags/ddns)[dnspod](https://h4ck.org.cn/tags/dnspod)

[Previous Post](https://h4ck.org.cn/2024/05/16937)
[Next Post](https://h4ck.org.cn/2024/05/16871)

![obaby](https://gg.lang.bi/avatar/d6ebc088df916bcc9e8b94a09f9b0f604e57be54b04bd520c6db2492740fc563?s=90&d=identicon&r=r)

#### obaby

爱好广泛的火星小妖精，有问题欢迎留言交流啊~(✪ω✪)
爬虫类工具请先点击这个链接查看用法https://oba.by/?p=12240
闺蜜圈APP下载 https://guimiquan.cn

#### 猜你喜欢：

2023年9月27日

#### [DAYI.MA（闺蜜圈）– 后台开发进度](https://h4ck.org.cn/2023/09/13453)

2021年3月18日

#### [html 播放rtsp 流rtsp2rtmp](https://h4ck.org.cn/2021/03/8026)

2024年3月12日

#### [Uni-id-co 外部系统联登](https://h4ck.org.cn/2024/03/15787)

### 37 comments

1. ![](https://gg.lang.bi/avatar/44c40589887c2a6c75aab996bc0a381fa3e3f60b168761754818a9ea10a9d728?s=64&d=identicon&r=r) **[刘郎](https://yjvc.cn/)**说道：

   [2024年5月8日 20:12](https://h4ck.org.cn/2024/05/16929#comment-115003)

   ![Level 4](https://badgen.net/badge/亲密度/Level 4/yellow?icon=codebeat)

   ![Safari 17](https://h4ck.org.cn/wp-content/plugins/wp-useragent/img/16/net/safari.png "Safari 17") Safari 17 ![Mac OS X 10.15](https://h4ck.org.cn/wp-content/plugins/wp-useragent/img/16/os/mac-3.png "Mac OS X 10.15") Mac OS X 10.15 ![cn](https://h4ck.org.cn/wp-content/plugins/wp-useragent/show-useragent/flags_svg/cn.svg "cn")

   固定 DNS ，或者换个更好的 DNS 服务，调调路由器设置，或者用 VPN，实在不行就找专业的人问问😌

   [回复](#comment-115003)

   1. ![](https://gg.lang.bi/avatar/d6ebc088df916bcc9e8b94a09f9b0f604e57be54b04bd520c6db2492740fc563?s=64&d=identicon&r=r)

      [2024年5月8日 20:15](https://h4ck.org.cn/2024/05/16929#comment-115005)

      ![公主](https://badgen.net/badge/管理员/小妖精/ff91a4?icon=terminal) ![Queen](https://badgen.net/badge/角色/女王/red?icon=matrix)

      ![Google Chrome 120](https://h4ck.org.cn/wp-content/plugins/wp-useragent/img/16/net/chrome.png "Google Chrome 120") Google Chrome 120 ![Windows 10](https://h4ck.org.cn/wp-content/plugins/wp-useragent/img/16/os/win-6.png "Windows 10") Windows 10 ![cn](https://h4ck.org.cn/wp-content/plugins/wp-useragent/show-useragent/flags_svg/cn.svg "cn")

      不是dns问题，是家里的ip地址老变。和dns服务关系不大。

      [回复](#comment-115005)

      1. ![](https://gg.lang.bi/avatar/44c40589887c2a6c75aab996bc0a381fa3e3f60b168761754818a9ea10a9d728?s=64&d=identicon&r=r)

         [2024年5月8日 20:17](https://h4ck.org.cn/2024/05/16929#comment-115007)

         ![Level 4](https://badgen.net/badge/亲密度/Level 4/yellow?icon=codebeat)

         ![Mozilla Compatible ](https://h4ck.org.cn/wp-content/plugins/wp-useragent/img/16/net/mozilla.png "Mozilla Compatible ") Mozilla Compatible ![iPhone iOS 17.4.1](https://h4ck.org.cn/wp-content/plugins/wp-useragent/img/16/device/iphone.png "iPhone iOS 17.4.1") iPhone iOS 17.4.1 ![cn](https://h4ck.org.cn/wp-content/plugins/wp-useragent/show-useragent/flags_svg/cn.svg "cn")

         家里 IP 地址常变，可以设静态 IP 或找智能切换的设备或软件

         [回复](#comment-115007)

         1. ![](https://gg.lang.bi/avatar/d6ebc088df916bcc9e8b94a09f9b0f604e57be54b04bd520c6db2492740fc563?s=64&d=identicon&r=r)

            [2024年5月8日 20:19](https://h4ck.org.cn/2024/05/16929#comment-115008)

            ![公主](https://badgen.net/badge/管理员/小妖精/ff91a4?icon=terminal) ![Queen](https://badgen.net/badge/角色/女王/red?icon=matrix)

            ![Google Chrome 120](https://h4ck.org.cn/wp-content/plugins/wp-useragent/img/16/net/chrome.png "Google Chrome 120") Google Chrome 120 ![Windows 10](https://h4ck.org.cn/wp-content/plugins/wp-useragent/img/16/os/win-6.png "Windows 10") Windows 10 ![cn](https://h4ck.org.cn/wp-content/plugins/wp-useragent/show-useragent/flags_svg/cn.svg "cn")

            纳尼？pppoe拨号，运营商分配的ip地址。哪里来的静态ip地址？

            [回复](#comment-115008)

            1. ![](https://gg.lang.bi/avatar/44c40589887c2a6c75aab996bc0a381fa3e3f60b168761754818a9ea10a9d728?s=64&d=identicon&r=r)

               [2024年5月8日 20:26](https://h4ck.org.cn/2024/05/16929#comment-115011)

               ![Level 4](https://badgen.net/badge/亲密度/Level 4/yellow?icon=codebeat)

               ![Mozilla Compatible ](https://h4ck.org.cn/wp-content/plugins/wp-useragent/img/16/net/mozilla.png "Mozilla Compatible ") Mozilla Compatible ![iPhone iOS 17.4.1](https://h4ck.org.cn/wp-content/plugins/wp-useragent/img/16/device/iphone.png "iPhone iOS 17.4.1") iPhone iOS 17.4.1 ![cn](https://h4ck.org.cn/wp-content/plugins/wp-useragent/show-useragent/flags_svg/cn.svg "cn")

               貌似没😂

               [回复](#comment-115011)
2. ![](https://gg.lang.bi/avatar/58a79d6c1371a10b17245e3121ec03aaebb1c4d40ee32b0e3fd717fc45d953d4?s=64&d=identicon&r=r)

   [2024年5月8日 21:09](https://h4ck.org.cn/2024/05/16929#comment-115013)

   ![](https://badgen.net/badge/友链/集美们/blue?icon=chrome) ![Level 3](https://badgen.net/badge/亲密度/Level 3/green?icon=codebeat)

   ![Microsoft Edge 124](https://h4ck.org.cn/wp-content/plugins/wp-useragent/img/16/net/edge-2.png "Microsoft Edge 124") Microsoft Edge 124 ![Windows 11](https://h4ck.org.cn/wp-content/plugins/wp-useragent/img/16/os/win-6.png "Windows 11") Windows 11 ![cn](https://h4ck.org.cn/wp-content/plugins/wp-useragent/show-useragent/flags_svg/cn.svg "cn")

   家里的网络也是，不定期更新的，有的时候分配的地址网速巨慢，千兆宽带的口号日趋无感了。

   [回复](#comment-115013)

   1. ![](https://gg.lang.bi/avatar/d6ebc088df916bcc9e8b94a09f9b0f604e57be54b04bd520c6db2492740fc563?s=64&d=identicon&r=r)

      [2024年5月8日 21:52](https://h4ck.org.cn/2024/05/16929#comment-115020)

      ![公主](https://badgen.net/badge/管理员/小妖精/ff91a4?icon=terminal) ![Queen](https://badgen.net/badge/角色/女王/red?icon=matrix)

      ![Google Chrome 120](https://h4ck.org.cn/wp-content/plugins/wp-useragent/img/16/net/chrome.png "Google Chrome 120") Google Chrome 120 ![Windows 10](https://h4ck.org.cn/wp-content/plugins/wp-useragent/img/16/os/win-6.png "Windows 10") Windows 10...