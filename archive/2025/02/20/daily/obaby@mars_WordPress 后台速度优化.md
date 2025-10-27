---
title: WordPress 后台速度优化
url: https://h4ck.org.cn/2025/02/19381
source: obaby@mars
date: 2025-02-20
fetch_date: 2025-10-06T20:32:42.917207
---

# WordPress 后台速度优化

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

[博客相关『Blogger/WordPress』](https://h4ck.org.cn/cats/jyzj/wordp), [破解/汇编『Crack/Asm』](https://h4ck.org.cn/cats/crackasm)

# WordPress 后台速度优化

2025年2月19日
[55 条评论](https://h4ck.org.cn/2025/02/19381#comments)

[<https://video.h4ck.org.cn/wp-content/uploads/2025/02/1102_1739928913-1.mp4>](https://video.h4ck.org.cn/wp-content/uploads/2025/02/1102_1739928913-1.mp4?_=1)

昨天下午的时候，[![杜郎](https://g.h4ck.org.cn/avatar/1fbf51cf49f5c369ad2cd13d76c15c42?s=64&d=mm&r=g)杜郎](https://dujun.io)发消息，问有没有设么想干的事情，或者 wp 想要的插件。当时信誓旦旦的说没什么想写的东西呢。

等到了晚上的时候，发现wp 的后台加载速度变得贼慢，需要等待 N 秒才能打开，这就变得很奇怪，让自己一度以为是自己升级了 Envira Gellery 插件导致的，于是把插件版本回滚了。

但是，回滚之后速度并没有明显的改观，这就变得很恶心了。

还是老办法打开 query monitor，发现后台打开请求时间到了十几秒，主要问题在几个 http 请求上：

[![](https://h4ck.org.cn/wp-content/uploads/2025/02/Screenshot-2025-02-18-193702.png)](https://h4ck.org.cn/wp-content/uploads/2025/02/Screenshot-2025-02-18-193702.png)

[![](https://h4ck.org.cn/wp-content/uploads/2025/02/Screenshot-2025-02-18-193654.png)](https://h4ck.org.cn/wp-content/uploads/2025/02/Screenshot-2025-02-18-193654.png)

这几个 http 都超时了，访问的是 api.wordpress.org，直接在服务器上 curl 访问也有一定的概率会超时，即使修改 host 绑定 ip 之后改观依然不大。

[![](https://h4ck.org.cn/wp-content/uploads/2025/02/Screenshot-2025-02-18-193832.png)](https://h4ck.org.cn/wp-content/uploads/2025/02/Screenshot-2025-02-18-193832.png)

并且这个 ip 地址全球解析都是一样的，也就是说没法更换 ip 地址来访问别的服务器。当然，要解决这个问题最直接的办法是直接禁用 wp 的更新检查，但是这个方法我并不是十分喜欢，毕竟有时候更新修复的是一些严重的漏洞。那么除此之外就只能坐以待毙了？

这个 ip 访问不稳定应该还是大墙导致的，既然如此，那么用自己的服务器反代应该会好一些。直接分配一个二级域名，到服务器进行反代：

```
location / {

        proxy_pass https://198.143.164.251;
        proxy_http_version 1.1;
proxy_set_header Accept-Encoding "";
proxy_set_header Host api.wordpress.org;

}
```

需要注意的是需要将 Host 设置为Host api.wordpress.org，否则访问的时候会直接跳到 wp 的首页。

修改 wp 的 update.php 文件：

[![](https://h4ck.org.cn/wp-content/uploads/2025/02/Screenshot-2025-02-18-201949.png)](https://h4ck.org.cn/wp-content/uploads/2025/02/Screenshot-2025-02-18-201949.png)

将检查更新的地址替换掉，再次访问：

[![](https://h4ck.org.cn/wp-content/uploads/2025/02/Screenshot-2025-02-18-202558.png)](https://h4ck.org.cn/wp-content/uploads/2025/02/Screenshot-2025-02-18-202558.png)

此时请求的域名就变成自己的域名了，并且超时的问题基本解决掉。剩下的就是两个慢查询：

[![](https://h4ck.org.cn/wp-content/uploads/2025/02/Screenshot-2025-02-18-194350.png)](https://h4ck.org.cn/wp-content/uploads/2025/02/Screenshot-2025-02-18-194350.png)

这两个是 wp 后台登录的保护插件导致的，看下数据库已经记录了 28 万条：

[![](https://h4ck.org.cn/wp-content/uploads/2025/02/Jietu20250219-095256.jpg)](https://h4ck.org.cn/wp-content/uploads/2025/02/Jietu20250219-095256.jpg)

清空记录之后，一切就正常了。

[![](https://h4ck.org.cn/wp-content/uploads/2025/02/Screenshot-2025-02-18-194430.png)](https://h4ck.org.cn/wp-content/uploads/2025/02/Screenshot-2025-02-18-194430.png)

只剩下一个错误，这个目前影响不大，就先不管了。

然而，在看到有两个更新，在点更新的时候又崩了。

[![](https://h4ck.org.cn/wp-content/uploads/2025/02/WechatIMG110113-scaled.jpg)](https://h4ck.org.cn/wp-content/uploads/2025/02/WechatIMG110113.jpg)

提示的 object cache 导致的，这个插件用的版本还是比较老的，网上找个新版本，发现处理的并不彻底，各种提示信息以及按钮不能用，自己尝试修改了一下，去掉了一些验证。自己折腾到十一点多，有点困了，于是就找到了杜郎。

[![](https://h4ck.org.cn/wp-content/uploads/2025/02/WechatIMG1104-scaled.jpg)](https://h4ck.org.cn/wp-content/uploads/2025/02/WechatIMG1104.jpg)

然而，事情貌似没那么简单，早上看了一下，插件已经自己停止了：

[![](https://h4ck.org.cn/wp-content/uploads/2025/02/Jietu20250219-084706.jpg)](https://h4ck.org.cn/wp-content/uploads/2025/02/Jietu20250219-084706.jpg)

并且 enable cache 的按钮是灰的，还是授权校验没通过导致的。

至于这个怎么解决，只能仔细研究代码了，或者靠[![杜郎](https://g.h4ck.org.cn/avatar/1fbf51cf49f5c369ad2cd13d76c15c42?s=64&d=mm&r=g)杜郎](https://dujun.io)研究代码，嘻嘻。

不过得赞一下[![杜郎](https://g.h4ck.org.cn/avatar/1fbf51cf49f5c369ad2cd13d76c15c42?s=64&d=mm&r=g)杜郎](https://dujun.io)给提供的头图视频啊，还是蛮惊艳的。效果出奇的好呢。

最终在独狼的提示下，感觉还是修改license.php文件靠谱，object cache pro 1.22如果出现授权为 invalid，将文件替换为下面的内容即可：

温馨提示: 此处隐藏内容需要[发表评论](#respond "发表评论")，并且审核通过后才能查看。
（发表评论请勾选 **在此浏览器中保存我的显示名称、邮箱地址和网站地址，以便下次评论时使用。**）
（请仔细检查自己的昵称和评论内容，以免被识别为垃圾评论而导致无法正常审核。）

☆版权☆

\* 网站名称：**[obaby@mars](https://h4ck.org.cn/)**
\* 网址：<https://h4ck.org.cn/>
\* 个性：<https://oba.by/>
\* 本文标题： [《WordPress 后台速度优化》](https://h4ck.org.cn/2025/02/19381)
\* 本文链接：<https://h4ck.org.cn/2025/02/19381>
\* 短链接：<https://oba.by/?p=19381>
\* 转载文章请标明文章来源，原文标题以及原文链接。请遵从 [《署名-非商业性使用-相同方式共享 2.5 中国大陆 (CC BY-NC-SA 2.5 CN) 》](https://creativecommons.org/licenses/by-nc-sa/2.5/cn/)许可协议。

---

[Object Cache Pro](https://h4ck.org.cn/tags/object-cache-pro)[WordPress](https://h4ck.org.cn/tags/wordpress)

[Previous Post](https://h4ck.org.cn/2025/02/19419)
[Next Post](https://h4ck.org.cn/2025/02/19333)

![obaby](https://gg.lang.bi/avatar/d6ebc088df916bcc9e8b94a09f9b0f604e57be54b04bd520c6db2492740fc563?s=90&d=identicon&r=r)

#### obaby

爱好广泛的火星小妖精，有问题欢迎留言交流啊~(✪ω✪)
爬虫类工具请先点击这个链接查看用法https://oba.by/?p=12240
闺蜜圈APP下载 https://guimiquan.cn

#### 猜你喜欢：

2011年7月8日

#### [WinRar 4.01(64-bit) Cracked](https://h4ck.org.cn/2011/07/2940)

2022年9月20日

#### [GAY 免费域名](https://h4ck.org.cn/2022/09/10516)

2011年11月15日

#### [迅雷 7.2.3.3254 去广告补丁](https://h4ck.org.cn/2011/11/3390)

### 55 comments

1. ![](https://gg.lang.bi/avatar/c9b84eca89169750a7bb00740aea5786adbd48bcaaeed2393f4bef6a5adc1857?s=64&d=identicon&r=r) **[铃子](https://qq.md/)**说道：

   [2025年2月19日 10:57](https://h4ck.org.cn/2025/02/19381#comment-123899)

   ![Level 3](https://badgen.net/badge/亲密度/Level 3/green?icon=codebeat)

   ![Firefox 128](https://h4ck.org.cn/wp-content/plugins/wp-useragent/img/16/net/firefox.png "Firefox 128") Firefox 128 ![Windows 10](https://h4ck.org.cn/wp-content/plugins/wp-useragent/img/16/os/win-6.png "Windows 10") Windows 10 ![za](https://h4ck.org.cn/wp-content/plugins/wp-useragent/show-useragent/flags_svg/za.svg "za")

   我从ASP博客迁移时接触到的第一个PHP博客程序是WordPress，刚开始还不错，达到了日IP 200+，并且在搜索中排名前五。但后来由于网络或程序问题，网站变得非常卡顿，甚至后台都无法访问。最终无奈放弃，转而使用了Typecho，从此再也没用过WordPress。

   [回复](#comment-123899)

   1. ![](https://gg.lang.bi/avatar/d6ebc088df916bcc9e8b94a09f9b0f604e57be54b04bd520c6db2492740fc563?s=64&d=identicon&r=r)

      [2025年2月19日 13:28](https://h4ck.org.cn/2025/02/19381#comment-123909)

      ![公主](https://badgen.net/badge/管理员/小妖精/ff91a4?icon=terminal) ![Queen](https://badgen.net/badge/角色/女王/red?icon=matrix)

      ![Google Chrome 132](https://h4ck.org.cn/wp-content/plugins/wp-useragent/img/16/net/chrome.png "Google Chrome 132") Google Chrome 132 ![Mac OS X 10.15](https://h4ck.org.cn/wp-content/plugins/wp-useragent/img/16/os/mac-3.png "Mac OS X 10.15") Mac OS X 10.15 ![cn](https://h4ck.org.cn/wp-content/plugins/wp-useragent/show-useragent/flags_svg/cn.svg "cn")

      wp 这个东西后期的确会越来越重，但是数据量上来了之后就有点积重难返了。
      要想轻量化，wp 的确不是一个好的选择。

      [回复](#comment-123909)

      1. ![](https://gg.lang.bi/avatar/c9b84eca89169750a7bb00740aea5786adbd48bcaaeed2393f4bef6a5adc1857?s=64&d=identicon&r=r)

         [2025年2月19日 20:01](https://h4ck.org.cn/2025/02/19381#comment-123940)

         ![Level 3](https://badgen.net/badge/亲密度/Level 3/green?icon=codebeat)

         ![Firefox 128](https://h4ck.org.cn/wp-content/plugins/wp-useragent/img/16/net/firefox.png "Firefox 128") Firefox 128 ![Windows 10](https://h4ck.org.cn/wp-content/plugins/wp-useragent/img/16/os/win-6.png "Windows 10") Windows 10 ![cn](https://h4ck.org.cn/wp-content/plugins/wp-useragent/show-useragent/flags_svg/cn.svg "cn")

         确实，还是得看需求。WordPress的插件商业化方面做得非常好，开发者能通过插件盈利。而Typecho的生态则差距较大，很多开发者无法从中获利。毕竟，一开始面向的群体就不一样，这也是没办法的事。

 ...