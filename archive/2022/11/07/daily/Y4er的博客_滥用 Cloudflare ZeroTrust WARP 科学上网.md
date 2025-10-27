---
title: 滥用 Cloudflare ZeroTrust WARP 科学上网
url: https://y4er.com/posts/cloudflare-zerotrust-proxy/
source: Y4er的博客
date: 2022-11-07
fetch_date: 2025-10-03T21:51:13.644074
---

# 滥用 Cloudflare ZeroTrust WARP 科学上网

[Y4er的博客](/ "Y4er的博客")

[归档](/posts/) [专栏](/series/) [分类](/categories/) [标签](/tags/) [笔记](/note/) [朋友](/friends/) [作品](/showcase/)

浅色深色跟随系统

[Y4er的博客](/ "Y4er的博客")

取消

[归档](/posts/)[专栏](/series/)[分类](/categories/)[标签](/tags/)[笔记](/note/)[朋友](/friends/)[作品](/showcase/)

浅色深色跟随系统

## 目录

* [前言](#前言)
* [原理](#原理)
* [全局代理配置](#全局代理配置)
* [单端口Proxy模式](#单端口proxy模式)
* [优缺点](#优缺点)
* [抛弃官方客户端](#抛弃官方客户端)
* [真实IP和地理位置](#真实ip和地理位置)

## 目录

* [前言](#前言)
* [原理](#原理)
* [全局代理配置](#全局代理配置)
* [单端口Proxy模式](#单端口proxy模式)
* [优缺点](#优缺点)
* [抛弃官方客户端](#抛弃官方客户端)
* [真实IP和地理位置](#真实ip和地理位置)

# 滥用 Cloudflare ZeroTrust WARP 科学上网

![Y4er avatar](/img/avatar.jpg)[Y4er](https://github.com/Y4er "Author")
 收录于  类别 [瞎折腾](/categories/%E7%9E%8E%E6%8A%98%E8%85%BE/)

2022-11-06  2022-11-06  约 1193 字
 预计阅读 6 分钟

目录

* [前言](#前言)
* [原理](#原理)
* [全局代理配置](#全局代理配置)
* [单端口Proxy模式](#单端口proxy模式)
* [优缺点](#优缺点)
* [抛弃官方客户端](#抛弃官方客户端)
* [真实IP和地理位置](#真实ip和地理位置)

警告

本文最后更新于 2022-11-06，文中内容可能已过时。

折腾了一下cf的零信任，发现了很多好玩的。虽然hostloc的mjj们应该都玩过了，我还是在这里记录一下。

关键字：cloudflare、warp、vpn。

# # 前言

之前写过用cloudflare零信任功能的tunnel功能做内网穿透。然后这几天又看了看文档，发现cf的零信任需要装一个warp的客户端。

# # 原理

和tunnel的原理差不多，都是cf用自己的cdn节点做代理访问。

# # 全局代理配置

客户端直接从https://1.1.1.1/ 这里下载对应平台的软件即可。

需要一个cloudflare账号，最好不要用自己的域名邮箱，用gmail，不然会让验证付款方式。

[![image.png](https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/593424/dcdce0e7-a881-3451-83d7-9e738bea8640.png)](https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/593424/dcdce0e7-a881-3451-83d7-9e738bea8640.png "image.png")

image.png

登陆进去点零信任的按钮。进去后会让你填你的组织名，随便填记住就行。然后填信用卡的地方跳过（这个地方有风控，最好用老账号）。

然后setting-authentication

[![image.png](https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/593424/a337d663-c4dd-0683-e990-565254c84959.png)](https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/593424/a337d663-c4dd-0683-e990-565254c84959.png "image.png")

image.png

如下配置

[![image.png](https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/593424/8b7f5fa0-5d00-813d-6329-579169658054.png)](https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/593424/8b7f5fa0-5d00-813d-6329-579169658054.png "image.png")

image.png

App Launcher中是配置谁可以访问主页的地方，点击Rule-Add Rule

[![image.png](https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/593424/13a987fa-5c52-7f6d-a007-f10ba7a2c7ad.png)](https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/593424/13a987fa-5c52-7f6d-a007-f10ba7a2c7ad.png "image.png")

image.png

然后点击warp client 配置客户端 `settings/devices/edit`

[![image.png](https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/593424/8a0bde22-9861-0ba5-f896-96d77087876a.png)](https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/593424/8a0bde22-9861-0ba5-f896-96d77087876a.png "image.png")

image.png

配置谁可以登陆零信任客户端

[![image.png](https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/593424/df079569-c216-bc47-7ad7-af6d85106ddf.png)](https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/593424/df079569-c216-bc47-7ad7-af6d85106ddf.png "image.png")

image.png

[![image.png](https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/593424/4d162318-c0e8-91ee-d637-0a6a2e739245.png)](https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/593424/4d162318-c0e8-91ee-d637-0a6a2e739245.png "image.png")

image.png

然后warp客户端中登陆零信任账户

[![image.png](https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/593424/70518ac5-72d1-af1f-6d35-61fc94b81b01.png)](https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/593424/70518ac5-72d1-af1f-6d35-61fc94b81b01.png "image.png")

image.png

输入你的组织名后会弹一个链接在浏览器

[![image.png](https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/593424/6cc2bcd2-aa99-329f-b449-2b0b6f6e6d81.png)](https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/593424/6cc2bcd2-aa99-329f-b449-2b0b6f6e6d81.png "image.png")

image.png

这里要输入和你上面warp client规则匹配的邮箱，输入验证码登陆即可。

[![image.png](https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/593424/5ce29674-7a10-42f1-31e3-1a39ea8a4cb6.png)](https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/593424/5ce29674-7a10-42f1-31e3-1a39ea8a4cb6.png "image.png")

image.png

验证成功后让你打开warp客户端，此时warp变成了这个样子

[![image.png](https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/593424/2e96569c-a3ef-cef0-5dfe-b5fd2d2d9293.png)](https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/593424/2e96569c-a3ef-cef0-5dfe-b5fd2d2d9293.png "image.png")

image.png

直接点链接就可以了。

测速

[![image.png](https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/593424/bf7043e2-9e05-69c9-3f89-2e808896c49f.png)](https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/593424/bf7043e2-9e05-69c9-3f89-2e808896c49f.png "image.png")

image.png

# # 单端口Proxy模式

settings/devices 这个地方设置单端口监听。

[![image.png](https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/593424/0dceab6f-6cd8-e360-cdb5-2ec84279767f.png)](https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/593424/0dceab6f-6cd8-e360-cdb5-2ec84279767f.png "image.png")

image.png

因为是零信任team模式，这个监听策略会下发到客户端。

浏览器这个插件得配socks4

[![image.png](https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/593424/557bb9ed-7286-e597-01d3-4ac5e13155ec.png)](https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/593424/557bb9ed-7286-e597-01d3-4ac5e13155ec.png "image.png")

image.png

其他配socks5也可以，玄学。

# # 优缺点

优点不用说，快就是优点，而且cf节点可能会被一些厂商认为是原生IP，懂得都懂。

缺点有一些网站可能会屏蔽cf的cdn节点，比如奈飞。

还有就是这个东西是可以换IP的，有cf的IP池在，不过需要折腾一下咯，关键词：`cloudflare warp 解锁`。

# # 抛弃官方客户端

warp原理就是wireguard协议

所以用 <https://github.com/ViRb3/wgcf> 导出wireguard配置用wireGuard客户端链接就行了。

# # 真实IP和地理位置

根据官方文档 <https://developers.cloudflare.com/warp-client/known-issues-and-faq/> 说的是，warp不会泄露用户IP地址，实测也确实没有泄露用户地址。

在社区讨论中 <https://community.cloudflare.com/t/beware-cloudflare-warp-does-not-always-hide-your-ip/425348/14> 提到，泄露IP地址应该是个BUG，在最新版已经修复了。

但是最重要的一点就是，虽然不会泄露真实IP，但是会泄露你的地理位置。这个原意是为了你在北京点外卖不给你定位到美国去，文档翻译回来如图

[![image.png](https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/593424/5276341f-d99e-4683-e9b4-8bd6d0154991.png)](https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/593424/5276341f-d99e-4683-e9b4-8bd6d0154991.png "image.png")

image.png

因为cf会给你路由到离你最近的cf节点上，比如我是北京市的IP，那么访问baidu.com时，baidu虽然不会收到我的真实IP，但是他会收到同为北京市的cf节点的IP，而这个IP是离你最近的CF节点的IP。所以这东西不适合用来日站。

并且节点发送给目标服务器的http请求中，有cf的特征，如图。

[![image.png](https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/593424/f058dcf6-3f62-424f-3ca3-d3d7bbe87cda.png)](https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/593424/f058dcf6-3f62-424f-3ca3-d3d7bbe87cda.png "image.png")

image.png

全是特征啊….

文笔垃圾，措辞轻浮，内容浅显，操作生疏。不足之处欢迎大师傅们指点和纠正，感激不尽。

![](/img/avatar.jpg)

*如果你觉得这篇文章对你有所帮助，欢迎赞赏或关注微信公众号～*

![](/img/reward/wechat.png)![](/img/reward/alipay.png)![](/img/reward/weixin_mp.jpg)

更新于 2022-11-06

LINE

[Cloudflare](/tags/cloudflare/)

返回 | [主页](/)

[CVE-2022-41828 Amazon Redshift JDBC Driver RCE](/posts/cve-2022-41828-amazon-redshift-jdbc-driver-rce/ "CVE-2022-41828 Amazon Redshift JDBC Driver RCE")
[对ZDI公布的InfraSuite Device Master一揽子漏洞的分析](/posts/infrasuite-device-master-cves/ "对ZDI公布的InfraSuite Device Master一揽子漏洞的分析")

Please enable JavaScript to view the comments powered by [Utterances](https://utteranc.es/).

由 [Hugo](https://gohugo.io/ "Hugo 0.148.2") 强力驱动 | 托管在 [Cloudflare Pages](https://pages.cloudflare.com/ "Cloudflare Pages") 上 | 主题 -  [DoIt](https://github.com/HEIGE-PCloud/DoIt "DoIt 0.4.2")

2018 - 2025 [Y4er](https://github.com/Y4er) | [CC BY-NC 4.0](https://creativecommons.org/licenses/by-nc/4.0/)