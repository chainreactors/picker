---
title: 快速搭建个人博客，1Panel让Halo博客部署变得如此简单
url: https://mp.weixin.qq.com/s/U9bmX3Votky5WCLRh-g3jw
source: Doonsec's feed
date: 2026-06-23
fetch_date: 2026-06-24T06:01:00.313190
---

# 快速搭建个人博客，1Panel让Halo博客部署变得如此简单

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/OsuOF7sibMYsicrLqkSm7usibmS1oy4b0hj4ne9feVZ0U6MM9J9JiahdEsdZDCwFpkexGym3WIlYx9iaxzrPJ7iagt1A/0?wx_fmt=jpeg)

# 快速搭建个人博客，1Panel让Halo博客部署变得如此简单

原创

didiplus
didiplus

攻城狮成长日记

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

![](https://mmbiz.qpic.cn/mmbiz_gif/f5u8u3lDeLchGaIcFTOuEzUYJyA2UibBrCNnQdjVEpYaZthELRW8oaiaUPXweZu61lAcOx0bWAPzhgJMibtaLaHVA/640?wx_fmt=gif&wxfrom=13&tp=wxpic)

> ❝
>
> 大家好！我是一个热衷于分享IT技术的up主。在这个公众号里，我将为大家带来最新、最实用的技术干货，从编程语言到前沿科技，从软件开发到网络安全。希望通过我的分享，能够帮助更多的小伙伴提升技术水平，共同成长！欢迎关注，一起探索科技的魅力吧！

在这个信息化的时代，拥有一个个人博客是记录生活、分享知识、展示作品的好方法。对于技术爱好者和开发者来说，使用Halo[1]这样的轻量级博客框架能够让你轻松搭建一个功能强大且美观的博客。而通过1Panel[2]的帮助，这一过程将变得更加简单和直观。本文将指导你如何使用1Panel快速部署Halo博客，让你的个人博客迅速上线。

## 环境准备

### 1panel简介

1Panel 是一个现代化、开源的 Linux 服务器运维管理面板。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/OsuOF7sibMYsicrLqkSm7usibmS1oy4b0hjYaJvfd9InPYYX6mTR29orqJ0IdqJR2AC25oZhhzuugmICUGWaW11WA/640?wx_fmt=png&from=appmsg)

具有以下功能：

* **快速建站**：深度集成 `WordPress` 和 `Halo`，域名绑定、`SSL`证书配置等一键搞定。
* **高效管理**：通过`Web`端轻松管理 `Linux`服务器，包括应用管理、主机监控、文件管理、数据库管理、容器管理等。
* **安全可靠**：最小漏洞暴露面，提供防火墙和安全审计等功能。
* **一键备份**：支持一键备份和恢复，备份数据云端存储，永不丢失。

### 安装

首先，你需要准备一台云服务器，可以参考以下步骤：

1. **获取云服务器**：选择适合自己需求的云服务器，例如阿里云或腾讯云。可以[参考这篇文章](https://mp.weixin.qq.com/s?__biz=MjM5OTc5MjM4Nw==&mid=2457381248&idx=1&sn=b8c540d1437f0df119c3c6571559f028&chksm=b0ba13ec87cd9afa61e3496b3a82b537ad338d85724e1b0dfd46daec489f03ae05300287fa49&token=47270989&lang=zh_CN&scene=21#wechat_redirect)。
2. **安装1Panel**：登录你的服务器，通过SSH连接，执行以下命令安装1Panel：

```
curl -sSL https://resource.fit2cloud.com/1panel/package/quick_start.sh -o quick_start.sh && sudo bash quick_start.sh
```

3. **访问1Panel**：安装完成后，1Panel会提供一个Web地址和登录凭证。使用浏览器访问该地址并登录。

### 安装基础软件

在安装`Halo`之前，需要先在`1Panel`上配置必要的软件环境，包括 `OpenResty` 和 `MySQL`。在接下来的教程中，我们将默认这些软件已经安装完毕，因此不会再详细说明相关步骤。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/OsuOF7sibMYsicrLqkSm7usibmS1oy4b0hjZ0tiagIMibaPoxUwA0MPu63d8R95ySNbc4jzhYicgOicicZZWsXayPINElg/640?wx_fmt=png&from=appmsg)

## 安装Halo应用

进入应用商店，浏览可用的应用列表，找到并选择Halo应用进行安装。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/OsuOF7sibMYsicrLqkSm7usibmS1oy4b0hjx1GRWFPRCMVprJic8XsfDbCjJ0ic8WtibJddJB4wlNL0z87b53myBdsPg/640?wx_fmt=png&from=appmsg)

在应用详情页选择最新的 Halo 版本进行安装。![](https://mmbiz.qpic.cn/sz_mmbiz_png/OsuOF7sibMYsicrLqkSm7usibmS1oy4b0hjwibjNxoa7iaQelEW4mTRK2Ow7FuR5gPVBicv8poSoiaDRCEVk7pdMNTWIg/640?wx_fmt=png&from=appmsg)

> ❝
>
> 参数说明：
>
> * **名称**：要创建的 Halo 应用的名称。
> * **数据库服务**：Halo 应用使用的数据库应用，支持下拉选择已安装的数据库应用，1Panel 会自动配置 Halo 使用该数据库。
> * **数据库名**：Halo 应用使用的数据库名称，1Panel 会在选中的数据库中自动创建这个数据库。
> * **数据库用户**：Halo 应用使用的数据库用户名，1Panel 会在选中的数据库中自动创建这个用户，并添加对应的数据库授权。
> * **数据库用户密码**：Halo 应用使用的数据库用户密码，1Panel 会在选中的数据库中自动为上一步创建的用户配置该密码。
> * **超级管理员用户名**：Halo 应用初始化创建的超级管理员用户名。
> * **超级管理员密码**：Halo 应用初始化创建的超级管理员密码。
> * **外部访问地址**：Halo 应用的最终访问地址，如果有为 Halo 规划域名，需要配置为域名格式，例如 `http://halo.example.com`。否则配置为 `http://服务器IP:PORT`，例如 `http://192.168.1.1:8090`。
> * **端口**：Halo 应用的服务端口。

开始安装后页面自动跳转到已安装应用列表，等待刚刚安装的 Halo 应用变为已启动状态。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/OsuOF7sibMYsicrLqkSm7usibmS1oy4b0hjPKdLRphzXwqBKCPEEkBHicicTgPl4PIvzkibrrMTpsUHryK5P7z4cicmRw/640?wx_fmt=png&from=appmsg)

此时便可以通过配置的外部访问地址来访问 Halo 了。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/OsuOF7sibMYsicrLqkSm7usibmS1oy4b0hjfSzvWd53qwbohZWxvbiaQ6LVkSoEDMgQADibJwkOZkNXrsQLLicjHtMJg/640?wx_fmt=png&from=appmsg)

## 创建网站

完成 Halo 应用的安装后，网站不会自动创建。我们需要手动添加一个新网站，并将 Halo 应用绑定到该网站上，这样才能通过域名进行访问。

在 1Panel 中，点击菜单中的“网站”选项，进入网站列表页面，然后点击“创建网站”按钮。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/OsuOF7sibMYsicrLqkSm7usibmS1oy4b0hjp2wR4KnGddTJZN0POAibpkFdnnzas0uen2FKdBq20kTHtCxItYRozCw/640?wx_fmt=png&from=appmsg "创建网站")

创建网站

> ❝
>
> 1. 在已装应用中选择我们刚刚新建的 Halo 应用。
> 2. 正确填写主域名，需要注意的是需要提前解析好域名到服务器 IP。

最后，点击确认按钮，等待网站创建完成。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/OsuOF7sibMYsicrLqkSm7usibmS1oy4b0hjHia5hCJgMJqfziaQUxYdPN6xz6hvHzv83JyAmUFughib9fYUSDJkAq9Dg/640?wx_fmt=png&from=appmsg)

## 申请证书

1Panel 的证书功能涵盖了与证书管理相关的多种操作，包括申请证书、自动续约、ACME 账户管理，以及 DNS 账户管理等。通过使用 1Panel 的证书功能，你可以轻松完成证书的申请和管理。

1. 创建Acme账号，如下图所示：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/OsuOF7sibMYsicrLqkSm7usibmS1oy4b0hjrYfYwkKkVib63WyCPLapicWiarj6ZsVhGvMcV4VxOhicqepka5ZtCGnx9g/640?wx_fmt=png&from=appmsg)

2. 创建DSN账号，如下图所示：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/OsuOF7sibMYsicrLqkSm7usibmS1oy4b0hjEuBxrnTqkJ6ASZiamhkmOy6EBnJzPu4tU5nDicMggQG1LcIDdt6nicTpA/640?wx_fmt=png&from=appmsg)
> ❝
>
> 由于我的域名是托管到`cloudflare`中，所以，类型我这里选择`cloudflare`。还有值得注意的是`API Token`不是用`Global API Key`。

3. 申请证书

完成了上述账号的创建，即可开始申请证书了，按照如下图的表单正确填写，即完成证书的申请。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/OsuOF7sibMYsicrLqkSm7usibmS1oy4b0hjeYNX2asFV9eOyf8wR7fyPrPf3QSsv3kO613icz95wDefhtpeetq5djA/640?wx_fmt=png&from=appmsg)

可以通过日志文件查看证书的申请情况。如下图所示：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/OsuOF7sibMYsicrLqkSm7usibmS1oy4b0hj5jOAcRhyibUd2wKmyRbuBBicD3DwaCko6WSjxJwhW2MqMpndwWPBuicIw/640?wx_fmt=png&from=appmsg)

## 为网站开启SSL

为网站开启SSL能够加密客户端与服务器之间的数据传输，保障用户信息的安全，防止数据被第三方窃取或篡改。启用SSL还可以提升网站的信誉度，增加用户信任感，并在搜索引擎排名中获得更好的表现。可以通过1panel轻松完成。

* 打开`网站`，点击`配置`，如下图所示：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/OsuOF7sibMYsicrLqkSm7usibmS1oy4b0hj9ibK2M5LVYuicL3TdjuM4gggicUN1ia9tPmxVVC75kw9poRA1NALVRXYKw/640?wx_fmt=png&from=appmsg)

* 在左侧菜单选择**HTTPS**，然后，HTTP 选项**选择访问HTTP自动跳转到HTTPS**，接着选**启用HTTPS**按钮，导入刚才申请好的证书。如下图所示：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/OsuOF7sibMYsicrLqkSm7usibmS1oy4b0hjEn44kIXBQ1mooOnPSdzCjuia07yHFRup0XrTU3qVCKtbSoKibnYyGic0A/640?wx_fmt=png&from=appmsg)

## 验证结果

完成以上配置后，你的Halo博客已经成功部署并运行起来了。打开浏览器，输入你配置的域名，即可访问你的个人博客。你可以在管理后台中进一步定制博客的主题、插件和其他设置，使其更符合你的个性化需求。 如下图所示：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/OsuOF7sibMYsicrLqkSm7usibmS1oy4b0hjzrePAVCOsPialKjUVP88QcBzN7KNvo8erRfe38zibAdfDQyxqtne8uYg/640?wx_fmt=png&from=appmsg "didiplus.kwpmp.cn")

didiplus.kwpmp.cn

> ❝
>
> `https://didiplus.kwpmp.cn`:这是我的博客地址欢迎大家参观，如果大家在部署上遇到什么问题也可以留言。

## 总结

通过1Panel，部署Halo博客变得前所未有的简单。你不需要复杂的命令行操作或深入的技术背景，只需几步操作，便可拥有一个属于自己的个人博客。现在就行动起来，记录下你生活中的点点滴滴，分享你的知识与见解吧！

## 推荐阅读

---

* [当你拥有一台云服务器，你最想做的事情是啥？](https://mp.weixin.qq.com/s?__biz=MjM5OTc5MjM4Nw==&mid=2457381248&idx=1&sn=b8c540d1437f0df119c3c6571559f028&chksm=b0ba13ec87cd9afa61e3496b3a82b537ad338d85724e1b0dfd46daec489f03ae05300287fa49&token=47270989&lang=zh_CN&scene=21#wechat_redirect)

---

**参考文档**

[1]

Halo: *https://www.halo.run/*

[2]

1Panel: *https://1panel.cn/*

![](https://mmbiz.qpic.cn/sz_mmbiz_png/OsuOF7sibMYtjIRLBwxQ3nQAtibnbGmeREia8PHfBB1qiaEZDIib84s63TuUw7tYyAiblDUox95cdCpm3DCAuOyfXwwA/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/OsuOF7sibMYtjIRLBwxQ3nQAtibnbGmeRE3HXia8ibthbJ659ibYic1HuwJanGY1PxibiaVnSDhd9KdtBw60Y1AVC1yU8Q/640?wx_fmt=jpeg&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/OsuOF7sibMYtjIRLBwxQ3nQAtibnbGmeRExXEZs9nlXezWLGzib674NkVCWRdIN544QLRte2qwGnCZpxgYlhBmb5Q/640?wx_fmt=png&from=appmsg)

预览时标签不可点

![]()

微信扫一扫
关注该公众号

知道了

![]()
微信扫一扫
使用小程序

取消
允许

取消
允许

取消
允许

×
分析

![跳转二维码]()

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/OsuOF7sibMYtLPfoEoNn5zJQjy6nMKW0GVf41zsKNsIVKdWJsxm2gSyIToAJOFI8x2wryVm4GqQib0ibno9KzEa9A/0?wx_fmt=png)

微信扫一扫可打开此内容，
使用完整服务

：
，
，
，
，
，
，
，
，
，
，
，
，
。

视频
小程序
赞
，轻点两下取消赞
在看
，轻点两下取消在看
分享
留言
收藏
听过