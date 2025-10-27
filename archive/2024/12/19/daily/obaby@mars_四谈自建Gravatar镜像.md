---
title: 四谈自建Gravatar镜像
url: https://h4ck.org.cn/2024/12/18819
source: obaby@mars
date: 2024-12-19
fetch_date: 2025-10-06T19:35:30.547386
---

# 四谈自建Gravatar镜像

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

# 四谈自建Gravatar镜像

2024年12月18日
[55 条评论](https://h4ck.org.cn/2024/12/18819#comments)

[![](https://h4ck.org.cn/wp-content/uploads/2024/12/default-10.jpg)](https://h4ck.org.cn/wp-content/uploads/2024/12/default-10.jpg)

至于为什么是四谈，之前的谈，参考这里：<https://h4ck.org.cn/?s=gravatar>。前几天收到[![杜郎](https://g.h4ck.org.cn/avatar/1fbf51cf49f5c369ad2cd13d76c15c42?s=64&d=mm&r=g)杜郎](https://dujun.io)的消息，说我搭建的gravatar代理失效了。之前有段时间因为cf的流量问题，一度放弃了那个代理。

[![](https://h4ck.org.cn/wp-content/uploads/2024/12/default-11-scaled.jpg)](https://h4ck.org.cn/wp-content/uploads/2024/12/default-11.jpg)

看来是改了规定了，不过现在貌似还能用。然而国内的这些代理，却一个一个的都比较诡异，诡异之处在于缓存刷新时间是个迷，换了头像几百年都不更新，这也的确是让人无语。昨天在[杜老师的聊天室](https://chat.dusays.com/dusays/channels/town-square)吐槽，有知情网友告知更新时间是一个月：

[![](https://h4ck.org.cn/wp-content/uploads/2024/12/Screenshot-2024-12-18-160953.png)](https://h4ck.org.cn/wp-content/uploads/2024/12/Screenshot-2024-12-18-160953.png)

这一个月都够自己换好几次头像了。最后很有爱心的给了个自建方案，这种自建是个方法，但是还是想着直接套cdn来搞一个。把盾云的服务整合了一下，正好空出来一个域名就用来干这个了，要代理也简单，不要用国内的cdn，选择亚太或者欧美，添加回源地址：

[![](https://h4ck.org.cn/wp-content/uploads/2024/12/Screenshot-2024-12-18-161345.png)](https://h4ck.org.cn/wp-content/uploads/2024/12/Screenshot-2024-12-18-161345.png)

直接ip地址回源：192.0.80.241 Host填写gravatar.com这样，一个自建的gravatar代理就ok了。

☆版权☆

\* 网站名称：**[obaby@mars](https://h4ck.org.cn/)**
\* 网址：<https://h4ck.org.cn/>
\* 个性：<https://oba.by/>
\* 本文标题： [《四谈自建Gravatar镜像》](https://h4ck.org.cn/2024/12/18819)
\* 本文链接：<https://h4ck.org.cn/2024/12/18819>
\* 短链接：<https://oba.by/?p=18819>
\* 转载文章请标明文章来源，原文标题以及原文链接。请遵从 [《署名-非商业性使用-相同方式共享 2.5 中国大陆 (CC BY-NC-SA 2.5 CN) 》](https://creativecommons.org/licenses/by-nc-sa/2.5/cn/)许可协议。

---

[Cravatar](https://h4ck.org.cn/tags/cravatar)[Gravatar](https://h4ck.org.cn/tags/gravatar)[weavatar](https://h4ck.org.cn/tags/weavatar)

[Previous Post](https://h4ck.org.cn/2024/12/18831)
[Next Post](https://h4ck.org.cn/2024/12/18797)

![obaby](https://gg.lang.bi/avatar/d6ebc088df916bcc9e8b94a09f9b0f604e57be54b04bd520c6db2492740fc563?s=90&d=identicon&r=r)

#### obaby

爱好广泛的火星小妖精，有问题欢迎留言交流啊~(✪ω✪)
爬虫类工具请先点击这个链接查看用法https://oba.by/?p=12240
闺蜜圈APP下载 https://guimiquan.cn

#### 猜你喜欢：

2023年5月3日

#### [给blog添加一个live2d小姐姐](https://h4ck.org.cn/2023/05/11920)

2022年11月5日

#### [也谈自建Gravatar镜像](https://h4ck.org.cn/2022/11/10659)

2025年2月19日

#### [WordPress 后台速度优化](https://h4ck.org.cn/2025/02/19381)

### 55 comments

1. ![](https://gg.lang.bi/avatar/316d22991de81658a564317696ccbd48fea4f9d7c49212e0e50cccddcde6c9bf?s=64&d=identicon&r=r) **[刘郎](https://vjo.cc/)**说道：

   [2024年12月18日 17:18](https://h4ck.org.cn/2024/12/18819#comment-122259)

   ![](https://badgen.net/badge/用户/已认证/CCFF33?icon=rss) ![](https://badgen.net/badge/友链/集美们/blue?icon=chrome) ![Level 5](https://badgen.net/badge/亲密度/Level 5/orange?icon=codebeat)

   ![Google Chrome 127](https://h4ck.org.cn/wp-content/plugins/wp-useragent/img/16/net/chrome.png "Google Chrome 127") Google Chrome 127 ![GNU/Linux](https://h4ck.org.cn/wp-content/plugins/wp-useragent/img/16/os/linux.png "GNU/Linux") GNU/Linux ![cn](https://h4ck.org.cn/wp-content/plugins/wp-useragent/show-useragent/flags_svg/cn.svg "cn")

   不自己弄 头像时不时的会挂掉😂

   [回复](#comment-122259)

   1. ![](https://gg.lang.bi/avatar/d6ebc088df916bcc9e8b94a09f9b0f604e57be54b04bd520c6db2492740fc563?s=64&d=identicon&r=r)

      [2024年12月18日 20:16](https://h4ck.org.cn/2024/12/18819#comment-122274)

      ![公主](https://badgen.net/badge/管理员/小妖精/ff91a4?icon=terminal) ![Queen](https://badgen.net/badge/角色/女王/red?icon=matrix)

      ![Google Chrome 130](https://h4ck.org.cn/wp-content/plugins/wp-useragent/img/16/net/chrome.png "Google Chrome 130") Google Chrome 130 ![Windows 10](https://h4ck.org.cn/wp-content/plugins/wp-useragent/img/16/os/win-6.png "Windows 10") Windows 10 ![cn](https://h4ck.org.cn/wp-content/plugins/wp-useragent/show-useragent/flags_svg/cn.svg "cn")

      关键是那些第三方的，感觉也智障。

      [回复](#comment-122274)
2. ![](https://gg.lang.bi/avatar/c44d885e47f3366e1926898246ecc70fc950b80314f34861521a7bad7b7af49c?s=64&d=identicon&r=r)

   [2024年12月18日 18:10](https://h4ck.org.cn/2024/12/18819#comment-122260)

   ![Level 4](https://badgen.net/badge/亲密度/Level 4/yellow?icon=codebeat)

   ![Microsoft Edge 131](https://h4ck.org.cn/wp-content/plugins/wp-useragent/img/16/net/edge-2.png "Microsoft Edge 131") Microsoft Edge 131 ![Windows 10](https://h4ck.org.cn/wp-content/plugins/wp-useragent/img/16/os/win-6.png "Windows 10") Windows 10 ![cn](https://h4ck.org.cn/wp-content/plugins/wp-useragent/show-useragent/flags_svg/cn.svg "cn")

   除了从jsd引入一些资源所以我反代了jsd之外，其它的基本就是有公益的就用公益的了。自从geekzu好像常常失效后，我又换成了 cravatar

   [回复](#comment-122260)

   1. ![](https://gg.lang.bi/avatar/d6ebc088df916bcc9e8b94a09f9b0f604e57be54b04bd520c6db2492740fc563?s=64&d=identicon&r=r)

      [2024年12月18日 20:17](https://h4ck.org.cn/2024/12/18819#comment-122276)

      ![公主](https://badgen.net/badge/管理员/小妖精/ff91a4?icon=terminal) ![Queen](https://badgen.net/badge/角色/女王/red?icon=matrix)

      ![Google Chrome 130](https://h4ck.org.cn/wp-content/plugins/wp-useragent/img/16/net/chrome.png "Google Chrome 130") Google Chrome 130 ![Windows 10](https://h4ck.org.cn/wp-content/plugins/wp-useragent/img/16/os/win-6.png "Windows 10") Windows 10 ![cn](https://h4ck.org.cn/wp-content/plugins/wp-useragent/show-useragent/flags_svg/cn.svg "cn")

      c we 都是同一群人建立的貌似，不过这个更新逻辑就贼蛋疼，用着不爽。

      [回复](#comment-122276)
3. ![](https://gg.lang.bi/avatar/35f5b036116cd9e4772887e32f5505296b5286160160fc3bbfd6263465f856c4?s=64&d=identicon&r=r)

   [2024年12月18日 18:15](https://h4ck.org.cn/2024/12/18819#comment-122261)

   ![Level 4](https://badgen.net/badge/亲密度/Level 4/yellow?icon=codebeat)

   ![Google Chrome 118](https://h4ck.org.cn/wp-content/plugins/wp-useragent/img/16/net/chrome.png "Google Chrome 118") Google Chrome 118 ![Windows 11](https://h4ck.org.cn/wp-content/plugins/wp-useragent/img/16/os/win-6.png "Windows 11") Windows 11 ![cn](https://h4ck.org.cn/wp-content/plugins/wp-useragent/show-useragent/flags_svg/cn.svg "cn")

   NB，都自己弄了。

   [回复](#comment-122261)

   1. ![](https://gg.lang.bi/avatar/d6ebc088df916bcc9e8b94a09f9b0f604e57be54b04bd520c6db2492740fc563?s=64&d=identicon&r=r)

      [2024年12月18日 20:17](https://h4ck.org.cn/2024/12/18819#comment-122277)

      ![公主](https://badgen.net/badge/管理员/小妖精/ff91a4?icon=terminal) ![Queen](https://badgen.net/badge/角色/女王/red?icon=matrix)

      ![Google Chrome 130](https://h4ck.org.cn/wp-content/plugins/wp-useragent/img/16/net/chrome.png "Google Chrome 130") Google Chrome 130 ![Windows 10](https://h4ck.org.cn/wp-content/plugins/wp-useragent/img/16/os/win-6.png "Windows 10") Windows 10 ![cn](https://h4ck.org.cn/wp-content/plugins/wp-useragent/show-useragent/flags_svg/cn.svg "cn")

      第三方的，都各种槽点。

      [回复](#comment-122277)
4. ![](https://gg.lang.bi/avatar/d838166f05390e17979f10c8e0fcc3b1d719369e6450e9eb30f218d8579263ee?s=64&d=identicon&r=r)

   [2024年12月18日 18:15](https://h4ck.org.cn/2024/12/18819#comment-122262)

   ![](https://badgen.net/badge/用户/已认证/CCFF33?icon=rss) ![](https://badgen.net/badge/友链/集美们/blue?icon=chrome) ![Level 7](https://badgen.net/badge/亲密度/Level 7/pink?icon=codebeat)

   ![Google Chrome 131](https://h4ck.org.cn/wp-content/plugins/wp-useragent/img/16/net/chrome.png "Google Chrome ...