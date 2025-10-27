---
title: 滥用 Cloudflare ZeroTrust WARP 科学上网
url: https://buaq.net/go-134425.html
source: unSafe.sh - 不安全
date: 2022-11-07
fetch_date: 2025-10-03T21:51:24.153625
---

# 滥用 Cloudflare ZeroTrust WARP 科学上网

* [unSafe.sh - 不安全](https://unsafe.sh)
* [我的收藏](/user/collects)
* [今日热榜](/?hot=true)
* [公众号文章](/?gzh=true)
* [导航](/nav/index)
* [Github CVE](/cve)
* [Github Tools](/tools)
* [编码/解码](/encode)
* [文件传输](/share/index)
* [Twitter Bot](https://twitter.com/buaqbot)
* [Telegram Bot](https://t.me/aqinfo)
* [Search](/search/search)

[Rss](/rss.xml)

[ ]
黑夜模式

![](https://8aqnet.cdn.bcebos.com/0f1a779543a715585400705587c039c0.jpg)

滥用 Cloudflare ZeroTrust WARP 科学上网

折腾了一下cf的零信任，发现了很多好玩的。虽然hostloc的mjj们应该都玩过了，我还是在这里记录一下。关键字：cloudflare、warp、vpn。之前写过用cloudflare零信任功能的tu
*2022-11-6 22:42:45
Author: [y4er.com(查看原文)](/jump-134425.htm)
阅读量:170
收藏*

---

折腾了一下cf的零信任，发现了很多好玩的。虽然hostloc的mjj们应该都玩过了，我还是在这里记录一下。

关键字：cloudflare、warp、vpn。

之前写过用cloudflare零信任功能的tunnel功能做内网穿透。然后这几天又看了看文档，发现cf的零信任需要装一个warp的客户端。

和tunnel的原理差不多，都是cf用自己的cdn节点做代理访问。

客户端直接从https://1.1.1.1/ 这里下载对应平台的软件即可。

需要一个cloudflare账号，最好不要用自己的域名邮箱，用gmail，不然会让验证付款方式。

[![https://y4er.com/img/uploads/cloudflare-zerotrust-proxy/1.png](https://y4er.com/img/uploads/cloudflare-zerotrust-proxy/1.png)](https://y4er.com/img/uploads/cloudflare-zerotrust-proxy/1.png "1.png")

登陆进去点零信任的按钮。进去后会让你填你的组织名，随便填记住就行。然后填信用卡的地方跳过（这个地方有风控，最好用老账号）。

然后setting-authentication

[![https://y4er.com/img/uploads/cloudflare-zerotrust-proxy/2.png](https://y4er.com/img/uploads/cloudflare-zerotrust-proxy/2.png)](https://y4er.com/img/uploads/cloudflare-zerotrust-proxy/2.png "2.png")

如下配置

[![https://y4er.com/img/uploads/cloudflare-zerotrust-proxy/3.png](https://y4er.com/img/uploads/cloudflare-zerotrust-proxy/3.png)](https://y4er.com/img/uploads/cloudflare-zerotrust-proxy/3.png "3.png")

App Launcher中是配置谁可以访问主页的地方，点击Rule-Add Rule

[![https://y4er.com/img/uploads/cloudflare-zerotrust-proxy/4.png](https://y4er.com/img/uploads/cloudflare-zerotrust-proxy/4.png)](https://y4er.com/img/uploads/cloudflare-zerotrust-proxy/4.png "4.png")

然后点击warp client 配置客户端 `settings/devices/edit`

[![https://y4er.com/img/uploads/cloudflare-zerotrust-proxy/5.png](https://y4er.com/img/uploads/cloudflare-zerotrust-proxy/5.png)](https://y4er.com/img/uploads/cloudflare-zerotrust-proxy/5.png "5.png")

配置谁可以登陆零信任客户端

[![https://y4er.com/img/uploads/cloudflare-zerotrust-proxy/6.png](https://y4er.com/img/uploads/cloudflare-zerotrust-proxy/6.png)](https://y4er.com/img/uploads/cloudflare-zerotrust-proxy/6.png "6.png")

[![https://y4er.com/img/uploads/cloudflare-zerotrust-proxy/7.png](https://y4er.com/img/uploads/cloudflare-zerotrust-proxy/7.png)](https://y4er.com/img/uploads/cloudflare-zerotrust-proxy/7.png "7.png")

然后warp客户端中登陆零信任账户

[![https://y4er.com/img/uploads/cloudflare-zerotrust-proxy/8.png](https://y4er.com/img/uploads/cloudflare-zerotrust-proxy/8.png)](https://y4er.com/img/uploads/cloudflare-zerotrust-proxy/8.png "8.png")

输入你的组织名后会弹一个链接在浏览器

[![https://y4er.com/img/uploads/cloudflare-zerotrust-proxy/9.png](https://y4er.com/img/uploads/cloudflare-zerotrust-proxy/9.png)](https://y4er.com/img/uploads/cloudflare-zerotrust-proxy/9.png "9.png")

这里要输入和你上面warp client规则匹配的邮箱，输入验证码登陆即可。

[![https://y4er.com/img/uploads/cloudflare-zerotrust-proxy/10.png](https://y4er.com/img/uploads/cloudflare-zerotrust-proxy/10.png)](https://y4er.com/img/uploads/cloudflare-zerotrust-proxy/10.png "10.png")

验证成功后让你打开warp客户端，此时warp变成了这个样子

[![https://y4er.com/img/uploads/cloudflare-zerotrust-proxy/11.png](https://y4er.com/img/uploads/cloudflare-zerotrust-proxy/11.png)](https://y4er.com/img/uploads/cloudflare-zerotrust-proxy/11.png "11.png")

直接点链接就可以了。

测速

[![https://y4er.com/img/uploads/cloudflare-zerotrust-proxy/12.png](https://y4er.com/img/uploads/cloudflare-zerotrust-proxy/12.png)](https://y4er.com/img/uploads/cloudflare-zerotrust-proxy/12.png "12.png")

settings/devices 这个地方设置单端口监听。

[![https://y4er.com/img/uploads/cloudflare-zerotrust-proxy/13.png](https://y4er.com/img/uploads/cloudflare-zerotrust-proxy/13.png)](https://y4er.com/img/uploads/cloudflare-zerotrust-proxy/13.png "13.png")

因为是零信任team模式，这个监听策略会下发到客户端。

浏览器这个插件得配socks4

[![https://y4er.com/img/uploads/cloudflare-zerotrust-proxy/14.png](https://y4er.com/img/uploads/cloudflare-zerotrust-proxy/14.png)](https://y4er.com/img/uploads/cloudflare-zerotrust-proxy/14.png "14.png")

其他配socks5也可以，玄学。

优点不用说，快就是优点，而且cf节点可能会被一些厂商认为是原生IP，懂得都懂。

缺点有一些网站可能会屏蔽cf的cdn节点，比如奈飞。

还有就是这个东西是可以换IP的，有cf的IP池在，不过需要折腾一下咯，关键词：`cloudflare warp 解锁`。

warp原理就是wireguard协议

所以用 <https://github.com/ViRb3/wgcf> 导出wireguard配置用wireGuard客户端链接就行了。

根据官方文档 <https://developers.cloudflare.com/warp-client/known-issues-and-faq/> 说的是，warp不会泄露用户IP地址，实测也确实没有泄露用户地址。

在社区讨论中 <https://community.cloudflare.com/t/beware-cloudflare-warp-does-not-always-hide-your-ip/425348/14> 提到，泄露IP地址应该是个BUG，在最新版已经修复了。

但是最重要的一点就是，虽然不会泄露真实IP，但是会泄露你的地理位置。这个原意是为了你在北京点外卖不给你定位到美国去，文档翻译回来如图

[![https://y4er.com/img/uploads/cloudflare-zerotrust-proxy/15.png](https://y4er.com/img/uploads/cloudflare-zerotrust-proxy/15.png)](https://y4er.com/img/uploads/cloudflare-zerotrust-proxy/15.png "15.png")

因为cf会给你路由到离你最近的cf节点上，比如我是北京市的IP，那么访问baidu.com时，baidu虽然不会收到我的真实IP，但是他会收到同为北京市的cf节点的IP，而这个IP是离你最近的CF节点的IP。所以这东西不适合用来日站。

并且节点发送给目标服务器的http请求中，有cf的特征，如图。

[![https://y4er.com/img/uploads/cloudflare-zerotrust-proxy/16.png](https://y4er.com/img/uploads/cloudflare-zerotrust-proxy/16.png)](https://y4er.com/img/uploads/cloudflare-zerotrust-proxy/16.png "16.png")

全是特征啊….

文笔垃圾，措辞轻浮，内容浅显，操作生疏。不足之处欢迎大师傅们指点和纠正，感激不尽。

文章来源: https://y4er.com/posts/cloudflare-zerotrust-proxy/
 如有侵权请联系:admin#unsafe.sh

© [unSafe.sh - 不安全](https://unsafe.sh) Powered By [PaperCache](https://github.com/code-scan/PaperCache)

* admin#unsafe.sh
* [安全马克](https://aq.mk)
* [星际黑客](https://xj.hk)
* [T00ls](https://t00ls.net)