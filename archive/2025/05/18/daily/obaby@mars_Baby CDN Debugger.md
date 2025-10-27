---
title: Baby CDN Debugger
url: https://h4ck.org.cn/2025/05/20746
source: obaby@mars
date: 2025-05-18
fetch_date: 2025-10-06T22:26:30.293653
---

# Baby CDN Debugger

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

[业余爱好『Favourite』](https://h4ck.org.cn/cats/cxsj/%E4%B8%9A%E4%BD%99%E7%88%B1%E5%A5%BD%E3%80%8Efavourite%E3%80%8F), [前端开发『FrontEnd』](https://h4ck.org.cn/cats/cxsj/%E5%89%8D%E7%AB%AF%E5%BC%80%E5%8F%91%E3%80%8Efrontend%E3%80%8F), [后台开发『BackEnd』](https://h4ck.org.cn/cats/cxsj/backend)

# Baby CDN Debugger

2025年5月17日
[39 条评论](https://h4ck.org.cn/2025/05/20746#comments)

[![](https://h4ck.org.cn/wp-content/uploads/2025/05/微信图片_20250517181308.jpg)](https://h4ck.org.cn/wp-content/uploads/2025/05/%E5%BE%AE%E4%BF%A1%E5%9B%BE%E7%89%87_20250517181308.jpg)

昨天晚上打完球往家走的时候，看了下手机，收到[杜郎](https://dujun.io)的消息说网站挂了。

[![](https://h4ck.org.cn/wp-content/uploads/2025/05/微信图片_20250517185046-scaled.jpg)](https://h4ck.org.cn/wp-content/uploads/2025/05/%E5%BE%AE%E4%BF%A1%E5%9B%BE%E7%89%87_20250517185046.jpg)

这种情况一般就是cdn的问题了。因为自己手机能获取到v6的地址，晚上还回复了几条评论。现在看来基本可以确认还是cdn出问题了。

后来[倦意](https://jyblog.cn)也@说证书变成自签名了。

[![](https://h4ck.org.cn/wp-content/uploads/2025/05/微信图片_20250517185051-scaled.jpg)](https://h4ck.org.cn/wp-content/uploads/2025/05/%E5%BE%AE%E4%BF%A1%E5%9B%BE%E7%89%87_20250517185051.jpg)

到家看了下果然是cdn的问题，昨天的时候cdn域名9offibrx.cnvip.akdns.top解析的地址有下面几个：

```
111.180.205.158
111.180.205.154
117.50.201.110
57.180.25.103
61.136.162.23
```

后来在群里也看到有人说站点挂了，挂在了同一个节点上111.180.205.158。

[![](https://h4ck.org.cn/wp-content/uploads/2025/05/微信图片_20250517185648-scaled.jpg)](https://h4ck.org.cn/wp-content/uploads/2025/05/%E5%BE%AE%E4%BF%A1%E5%9B%BE%E7%89%87_20250517185648.jpg)

如果要解决cdn节点问题，最简单的办法就是自建解析，排除掉有问题的节点。

新建A记录，选几个可用的ip地址添加上：

[![](https://h4ck.org.cn/wp-content/uploads/2025/05/Screenshot-2025-05-17-185927.png)](https://h4ck.org.cn/wp-content/uploads/2025/05/Screenshot-2025-05-17-185927.png)

新建cname记录，将www和@解析到上面的域名即可：

[![](https://h4ck.org.cn/wp-content/uploads/2025/05/Screenshot-2025-05-17-190049.png)](https://h4ck.org.cn/wp-content/uploads/2025/05/Screenshot-2025-05-17-190049.png)

之后等解析生效就可以了，生效之后那些失效的节点就被排除掉了。

不过要排除到底是节点问题还是什么问题，其实最简单的就是直接通过postman之类的工具测试。在进行节点测试的时候需要再header中取消原来的host，添加新的host才能自定义host。

[![](https://h4ck.org.cn/wp-content/uploads/2025/05/Screenshot-2025-05-17-190256.png)](https://h4ck.org.cn/wp-content/uploads/2025/05/Screenshot-2025-05-17-190256.png)

这个测试通过postman的确可以，但是如果要再手机上测试就麻烦了。于是，我自己做了一个工具<http://cd.h4ck.org.cn>，可以简单的认为是个postman网页版。

[![](https://h4ck.org.cn/wp-content/uploads/2025/05/Screenshot-2025-05-17-190540.png)](https://h4ck.org.cn/wp-content/uploads/2025/05/Screenshot-2025-05-17-190540.png)

上面的错误是因为直接访问节点，服务器的证书是自签名证书，关闭证书校验就能获取数据了。如下：

[![](https://h4ck.org.cn/wp-content/uploads/2025/05/Screenshot-2025-05-17-211729.png)](https://h4ck.org.cn/wp-content/uploads/2025/05/Screenshot-2025-05-17-211729.png)

预览页面可以看到具体页面信息：

[![](https://h4ck.org.cn/wp-content/uploads/2025/05/Screenshot-2025-05-17-211736.png)](https://h4ck.org.cn/wp-content/uploads/2025/05/Screenshot-2025-05-17-211736.png)

证书信息：

[![](https://h4ck.org.cn/wp-content/uploads/2025/05/Screenshot-2025-05-17-211744.png)](https://h4ck.org.cn/wp-content/uploads/2025/05/Screenshot-2025-05-17-211744.png)

可以看到是lecdn的自签名证书，那么现在该怎么通过这个节点测试博客呢？

直接添加自定义host：

[![](https://h4ck.org.cn/wp-content/uploads/2025/05/Screenshot-2025-05-17-212051.png)](https://h4ck.org.cn/wp-content/uploads/2025/05/Screenshot-2025-05-17-212051.png) [![](https://h4ck.org.cn/wp-content/uploads/2025/05/Screenshot-2025-05-17-212058.png)](https://h4ck.org.cn/wp-content/uploads/2025/05/Screenshot-2025-05-17-212058.png) [![](https://h4ck.org.cn/wp-content/uploads/2025/05/Screenshot-2025-05-17-212105.png)](https://h4ck.org.cn/wp-content/uploads/2025/05/Screenshot-2025-05-17-212105.png)

这样一切就正常了是不是？所以，如果要测试cdn的某个节点就可以通过上面的方式测试了。

同样，对于ipv6的节点也是支持的，默认访问上面的域名会根据当前网络状态返回v4或者v6地址，如果没有切换到v6，可以通过访问<https://cd6.h4ck.org.cn>，直接访问v6的地址。

还是一博客的v6ip为例：

[![](https://h4ck.org.cn/wp-content/uploads/2025/05/Screenshot-2025-05-17-212817.png)](https://h4ck.org.cn/wp-content/uploads/2025/05/Screenshot-2025-05-17-212817.png)

其实被waf系统拦截了：

[![](https://h4ck.org.cn/wp-content/uploads/2025/05/Screenshot-2025-05-17-212828.png)](https://h4ck.org.cn/wp-content/uploads/2025/05/Screenshot-2025-05-17-212828.png)

需要注意v6的ip地址拼接采用后面的形式：https://[2408:8214:e10:7210:2e2:69ff:fe39:d706]:443 知名端口号无需添加，可以省略80 443，会自动根据协议处理。

添加域名之后就可以了：

[![](https://h4ck.org.cn/wp-content/uploads/2025/05/Screenshot-2025-05-17-213451.png)](https://h4ck.org.cn/wp-content/uploads/2025/05/Screenshot-2025-05-17-213451.png)

对于cdn以及waf可以通过同样的方式测试，测试文件也是可以的。

[![](https://h4ck.org.cn/wp-content/uploads/2025/05/Screenshot-2025-05-17-214533.png)](https://h4ck.org.cn/wp-content/uploads/2025/05/Screenshot-2025-05-17-214533.png)

查看资源缓存状态：

[![](https://h4ck.org.cn/wp-content/uploads/2025/05/Screenshot-2025-05-17-214544.png)](https://h4ck.org.cn/wp-content/uploads/2025/05/Screenshot-2025-05-17-214544.png)

以及其他类型的错误排查也是可以的：

[![](https://h4ck.org.cn/wp-content/uploads/2025/05/Screenshot-2025-05-17-215944.png)](https://h4ck.org.cn/wp-content/uploads/2025/05/Screenshot-2025-05-17-215944.png)

**工具地址：**

IPv4 & IPv6访问

<http://cd.h4ck.org.cn>

IPv6 访问Only

<https://cd6.h4ck.org.cn>

*注意：cd地址不支持v6服务器的探测，cd6地址支持v4以及v6服务器探测。*

☆版权☆

\* 网站名称：**[obaby@mars](https://h4ck.org.cn/)**
\* 网址：<https://h4ck.org.cn/>
\* 个性：<https://oba.by/>
\* 本文标题： [《Baby CDN Debugger》](https://h4ck.org.cn/2025/05/20746)
\* 本文链接：<https://h4ck.org.cn/2025/05/20746>
\* 短链接：<https://oba.by/?p=20746>
\* 转载文章请标明文章来源，原文标题以及原文链接。请遵从 [《署名-非商业性使用-相同方式共享 2.5 中国大陆 (CC BY-NC-SA 2.5 CN) 》](https://creativecommons.org/licenses/by-nc-sa/2.5/cn/)许可协议。

---

[CDN](https://h4ck.org.cn/tags/cdn)[Python3](https://h4ck.org.cn/tags/python3)[waf](https://h4ck.org.cn/tags/waf)[WEB调试](https://h4ck.org.cn/tags/web%E8%B0%83%E8%AF%95)[南墙](https://h4ck.org.cn/tags/%E5%8D%97%E5%A2%99)[雷池](https://h4ck.org.cn/tags/%E9%9B%B7%E6%B1%A0)

[Previous Post](https://h4ck.org.cn/2025/05/20774)
[Next Post](https://h4ck.org.cn/2025/05/20733)

![obaby](https://gg.lang.bi/avatar/d6ebc088df916bcc9e8b94a09f9b0f604e57be54b04bd520c6db2492740fc563?s=90&d=identicon&r=r)

#### obaby

爱好广泛的火星小妖精，有问题欢迎留言交流啊~(✪ω✪)
爬虫类工具请先点击这个链接查看用法https://oba.by/?p=12240
闺蜜圈APP下载 https://guimiquan.cn

#### 猜你喜欢：

2024年5月12日

#### [Google & Bing 爬虫IP列表](https://h4ck.org.cn/2024/05/16956)

2021年6月16日

#### [BeautifulSoup4 中文乱码](https://h4ck.org.cn/2021/06/8318)

2023年11月17日

#### [退路](https://h4ck.org.cn/2023/11/14296)

### 39 comments

1. ![](https://gg.lang.bi/avatar/d838166f05390e17979f10c8e0fcc3b1d719369e6450e9eb30f218d8579263ee?s=64&d=identicon&r=r) **[dujun](https://dujun.io/)**说道：

   [2025年5月17日 22:34](https://h4ck.org.cn/2025/05/20746#comment-126488)

   ![](https://badgen.net/badge/用户/已认证/CCFF33?icon=rss) ![](https://badgen.net/badge/友链/集美们/blue?icon=chrome) ![Level 7](https://badgen.net/badge/亲密度/Level 7/pink?icon=codebeat)

   ![Google Chrome 136](https://h4ck.org.cn/wp-content/plugins/wp-useragent/img/16/net/chrome.png "Google Chrome 136") Google Chrome 136 ![Mac OS X 10.15](https://h4ck.org.cn/wp-content/plugins/wp-useragent/img/16/os/mac-3.png "Mac OS X 10.15") Mac OS X 10.15 ![cn](https://h4ck.org.cn/wp-content/plugins/wp-useragent/show-useragent/flags_svg/cn.svg "cn")

   甚至感觉不如云盾？虽然云盾被攻击会罢工，但是你这个遇到的问题是不是更频繁。

   [回复](#comment-126488)

   1. ![](https://gg.lang.bi/avatar/d6ebc088df916bcc9e8b94a09f9b0f604e57be54b04bd520c6db2492740fc563?s=64&d=identico...