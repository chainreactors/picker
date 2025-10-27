---
title: 死鸭子事件簿之二
url: https://h4ck.org.cn/2024/07/17568
source: obaby@mars
date: 2024-07-17
fetch_date: 2025-10-06T17:41:13.118454
---

# 死鸭子事件簿之二

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

[个人日记『Diary』](https://h4ck.org.cn/cats/dddd/grrj)

# 死鸭子事件簿之二

2024年7月16日
[48 条评论](https://h4ck.org.cn/2024/07/17568#comments)

[![](https://h4ck.org.cn/wp-content/uploads/2024/07/WechatIMG945.jpg)](https://h4ck.org.cn/wp-content/uploads/2024/07/WechatIMG945.jpg)

周日的时候，收到反馈，说公司对接的一批设备数据批量失效了。所有人的权限在所有设备上都被取消掉了，这并不是第一次出现用户权限莫名奇妙失效的情况，之前的时候局限于个别人，个别设备。解决方案也很简单粗暴，直接重新下发权限。然鹅，这种大面积失效，用户直接炸锅了。

联系设备厂商，厂商问，有那么着急吗？ 用户都炸了，你说能不着急吗？终于中午的时候派了技术过来。下午开始查看设备日志，进行一系列的测试工作。

为了保证用户暂时能用，让研发把所有的设备重新下发了用户权限数据。但是，保留了两台，让他们进行调试以及现场故障排查。在折腾了一下午之后，没有得出神马有用的结论，给其中一台测试设备进行升级固件之后，表示要运行测试一段时间看看效果。看他们暂时也拿不出什么更有建设性意义的方案，暂时于其他人合计先这么处理。跟领导汇报后，领导不认可，要求必须给出问题原因。于是只好带着他们的研发继续去现场进行问题排查。终于，在经历了 4 个小时之后，在十点左右，给出了问题的答案，于下午的结论区别不大：

1.我们删除数据，导致数据出现错乱

2.他们的系统于我们的系统共用出现了数据冲突

3.数据下发过快，导致存储过程出现问题。

对于 1 跟 3 我是极度不认可的，也在群里跟他们据理力争。数据删除是经过确认的单个用户权限删除，并且是通过设备方提供的 mqtt 主题进行数据删除，并没有直接修改设备数据。怎么回导致所有设备六十多台，所有用户的权限集体失效？

数据下发也是通过 mqtt 进行主题发布，设备方订阅消息进行权限处理，有哪里存在速度快慢问题？

至于 2，不知道设备上的数据存储逻辑，不好判断。

终于，又过了一个小时，设备方给回了个可能的原因。平台数据于我们的数据可能存在目录一致性问题，导致数据可能出现加载问题。这个结论相对来说比 13 就靠谱了很多，最起码是可能的诱因，但是依然无法解释在一个时间段所有设备全部失效的问题。

跟各种设备方打交道多了，永远不知道对面的水平到底是如何的。如果不懂技术，那么这几个闪烁其词的理由也就搪塞过去了。但是解决不了问题，在自己要求下，设备方今天安排研发过来进行现场调试。

有时候觉得挺离谱的，到底是哪里来的自信，给出这些不着边际的答案。不由得又让我想到了之前另外一个设备方给的算法，

> [哥哥，不会写文档就 tm 别写，老老实实写代码行吗？](https://h4ck.org.cn/2024/03/16050)

这些莫名奇妙的自信，真的让人很上火。当然，我也没想到这个死鸭子事件薄能写第二件。当然，以后还有第三件，第四件。

于是，人生就让这些死鸭子给浪费掉了！折腾到 11 点，连《2077》都没来得及玩！艹！

☆版权☆

\* 网站名称：**[obaby@mars](https://h4ck.org.cn/)**
\* 网址：<https://h4ck.org.cn/>
\* 个性：<https://oba.by/>
\* 本文标题： [《死鸭子事件簿之二》](https://h4ck.org.cn/2024/07/17568)
\* 本文链接：<https://h4ck.org.cn/2024/07/17568>
\* 短链接：<https://oba.by/?p=17568>
\* 转载文章请标明文章来源，原文标题以及原文链接。请遵从 [《署名-非商业性使用-相同方式共享 2.5 中国大陆 (CC BY-NC-SA 2.5 CN) 》](https://creativecommons.org/licenses/by-nc-sa/2.5/cn/)许可协议。

---

[bug](https://h4ck.org.cn/tags/bug)[程序员](https://h4ck.org.cn/tags/%E7%A8%8B%E5%BA%8F%E5%91%98)

[Previous Post](https://h4ck.org.cn/2024/07/17576)
[Next Post](https://h4ck.org.cn/2024/07/17545)

![obaby](https://gg.lang.bi/avatar/d6ebc088df916bcc9e8b94a09f9b0f604e57be54b04bd520c6db2492740fc563?s=90&d=identicon&r=r)

#### obaby

爱好广泛的火星小妖精，有问题欢迎留言交流啊~(✪ω✪)
爬虫类工具请先点击这个链接查看用法https://oba.by/?p=12240
闺蜜圈APP下载 https://guimiquan.cn

#### 猜你喜欢：

2013年5月20日

#### [骚货速成手册，专业骚货解剖骚货 【转载】](https://h4ck.org.cn/2013/05/5154)

2024年8月27日

#### [秋风起](https://h4ck.org.cn/2024/08/17926)

2025年1月22日

#### [小年 — 这真的就要过年了？](https://h4ck.org.cn/2025/01/19030)

### 48 comments

1. ![](https://gg.lang.bi/avatar/d838166f05390e17979f10c8e0fcc3b1d719369e6450e9eb30f218d8579263ee?s=64&d=identicon&r=r) **[dujun](https://dujun.io/)**说道：

   [2024年7月16日 10:48](https://h4ck.org.cn/2024/07/17568#comment-117365)

   ![](https://badgen.net/badge/用户/已认证/CCFF33?icon=rss) ![](https://badgen.net/badge/友链/集美们/blue?icon=chrome) ![Level 7](https://badgen.net/badge/亲密度/Level 7/pink?icon=codebeat)

   ![Google Chrome 126](https://h4ck.org.cn/wp-content/plugins/wp-useragent/img/16/net/chrome.png "Google Chrome 126") Google Chrome 126 ![Mac OS X 10.15](https://h4ck.org.cn/wp-content/plugins/wp-useragent/img/16/os/mac-3.png "Mac OS X 10.15") Mac OS X 10.15 ![cn](https://h4ck.org.cn/wp-content/plugins/wp-useragent/show-useragent/flags_svg/cn.svg "cn")

   甩锅现场

   [回复](#comment-117365)

   1. ![](https://gg.lang.bi/avatar/d6ebc088df916bcc9e8b94a09f9b0f604e57be54b04bd520c6db2492740fc563?s=64&d=identicon&r=r)

      [2024年7月16日 13:20](https://h4ck.org.cn/2024/07/17568#comment-117371)

      ![公主](https://badgen.net/badge/管理员/小妖精/ff91a4?icon=terminal) ![Queen](https://badgen.net/badge/角色/女王/red?icon=matrix)

      ![Google Chrome 118](https://h4ck.org.cn/wp-content/plugins/wp-useragent/img/16/net/chrome.png "Google Chrome 118") Google Chrome 118 ![Mac OS X 10.15](https://h4ck.org.cn/wp-content/plugins/wp-useragent/img/16/os/mac-3.png "Mac OS X 10.15") Mac OS X 10.15 ![cn](https://h4ck.org.cn/wp-content/plugins/wp-useragent/show-useragent/flags_svg/cn.svg "cn")

      真就死活不认

      [回复](#comment-117371)
2. ![](https://gg.lang.bi/avatar/fccc0a7a91070d2458de2d7275a721769c0b47e5087199512c691e09d55f1ca4?s=64&d=identicon&r=r)

   [2024年7月16日 10:50](https://h4ck.org.cn/2024/07/17568#comment-117366)

   ![](https://badgen.net/badge/友链/集美们/blue?icon=chrome) ![Level 6](https://badgen.net/badge/亲密度/Level 6/red?icon=codebeat)

   ![Google Chrome 107](https://h4ck.org.cn/wp-content/plugins/wp-useragent/img/16/net/chrome.png "Google Chrome 107") Google Chrome 107 ![Android 14](https://h4ck.org.cn/wp-content/plugins/wp-useragent/img/16/os/android.png "Android 14") Android 14 ![cn](https://h4ck.org.cn/wp-content/plugins/wp-useragent/show-useragent/flags_svg/cn.svg "cn")

   计算器验算这个梗，我印象深刻，一直忘不了，这种逻辑运算能力羡慕死了。我要是会岂不是，什么编程语言我都可以学会了。

   [回复](#comment-117366)

   1. ![](https://gg.lang.bi/avatar/d6ebc088df916bcc9e8b94a09f9b0f604e57be54b04bd520c6db2492740fc563?s=64&d=identicon&r=r)

      [2024年7月16日 13:21](https://h4ck.org.cn/2024/07/17568#comment-117372)

      ![公主](https://badgen.net/badge/管理员/小妖精/ff91a4?icon=terminal) ![Queen](https://badgen.net/badge/角色/女王/red?icon=matrix)

      ![Google Chrome 118](https://h4ck.org.cn/wp-content/plugins/wp-useragent/img/16/net/chrome.png "Google Chrome 118") Google Chrome 118 ![Mac OS X 10.15](https://h4ck.org.cn/wp-content/plugins/wp-useragent/img/16/os/mac-3.png "Mac OS X 10.15") Mac OS X 10.15 ![cn](https://h4ck.org.cn/wp-content/plugins/wp-useragent/show-useragent/flags_svg/cn.svg "cn")

      计算器好评啊，跟我算的一样哒

      [回复](#comment-117372)
3. ![](https://gg.lang.bi/avatar/c8b1c4e066955840427abd9f454b9fb9569d4480ec1b84bb78c8b210d91893d8?s=64&d=identicon&r=r)

   [2024年7月16日 11:07](https://h4ck.org.cn/2024/07/17568#comment-117368)

   ![Level 6](https://badgen.net/badge/亲密度/Level 6/red?icon=codebeat)

   ![Microsoft Edge 126](https://h4ck.org.cn/wp-content/plugins/wp-useragent/img/16/net/edge-2.png "Microsoft Edge 126") Microsoft Edge 126 ![Windows 10](https://h4ck.org.cn/wp-content/plugins/wp-useragent/img/16/os/win-6.png "Windows 10") Windows 10 ![us](https://h4ck.org.cn/wp-content/plugins/wp-useragent/show-useragent/flags_svg/us.svg "us")

   都没日志吗？这些设备做得可真low

   [回复](#comment-117368)

   1. ![](https://gg.lang.bi/avatar/d6ebc088df916bcc9e8b94a09f9b0f604e57be54b04bd520c6db2492740fc563?s=64&d=identicon&r=r)

      [2024年7月16日 13:21](https://h4ck.org.cn/2024/07/17568#comment-117373)

      ![公主](https://badgen.net/badge/管理员/小妖精/ff91a4?icon=terminal) ![Queen](https://badgen.net/badge/角色/女王/red?icon=matrix)

      ![Google Chrome 118](https://h4ck.org.cn/wp-content/plugins/wp-useragent/img/16/net/chrome.png "Google Chrome 118") Google Chrome 118 ![Mac OS X 10.15](https://h4ck.org.cn/wp-content/plugins/wp-useragent/img/16/os/mac-3.png "Mac OS X 10.15") Mac OS X 10.15 ![cn](https://h4ck.org.cn/wp-content/plugins/wp-useragent/show-useragent/flags_svg/cn.svg "cn")

      有日志，查了半天查了个寂寞

      [回复](#comment-117373)
4. ![](https://gg.lang.bi/avatar/7b909a52d63c104feb8ec19c7581480aa1c0ae0be29120160ef7735cf431ff49?s=64&d=identicon&r=r)

   [2024年7月16日 13:08](https://h4ck.org.cn/2024/07/17568#comment-117369)

   ![Level 3](https://badgen.net/badge/亲密度/Level 3/green?icon=codebeat)

   ![Google Chrome 126](https://h4ck.org.cn/wp-content/plugins/wp-useragent/img/16/net/chrome.png "Google Chrome 126") Google Chrome 126 ![Android 10](https...