---
title: 安卓逆向 -- 某DB去开屏广告+本地vip（ProxyPin重写）
url: https://mp.weixin.qq.com/s/vy6hs23MDSQjyepkSdCCkQ
source: Doonsec's feed
date: 2026-04-07
fetch_date: 2026-04-08T04:30:52.916445
---

# 安卓逆向 -- 某DB去开屏广告+本地vip（ProxyPin重写）

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/Gv6JExJQjUUWHA8dnpEXj2EhlXwqIQKs1icQk9C8JBCbdLr9s1ibZgTvG7b6F6Ogt6WxVdYMf2ReOoMfR7ib6tNnWU1PjxO2rGemW1MIND6QPE/0?wx_fmt=jpeg)

# 安卓逆向 -- 某DB去开屏广告+本地vip（ProxyPin重写）

Barih
Barih

逆向有你

![]()

在小说阅读器中沉浸阅读

## 一、准备工具

1.mumu模拟器或真机（我用的是魔改的模拟器https://www.bilibili.com/video/BV178tbzYEXh/?spm\_id\_from=333.337.search-card.all.click
2.ProxyPin  模拟器开启ROOT 将proxypin根证书安装到指定位置，这里不再详细介绍，参考网上教程

## 二、开始修改

打开要抓包的软件，开始抓包。发现接口响应都是以明文展示的.
**关键字段分析：**

```
 复制代码 隐藏代码
enabled： 是否开启，true改为false
overtime： 广告倒计时，原本是5秒，改为0
ad： {}  广告来源，直接赋值NUlL
promotion_days:  推广天数
vip_expired_at： vip到期时间
is_vip： 是否vip
```

有了以上参数，开始重写

![](https://mmbiz.qpic.cn/mmbiz_png/Gv6JExJQjUX5yzL9vjDhAu6EgHWWZtnwcAjMzDXVGX1p5I1yptbjuChsiaSSlPjRbM4rvPSt40PcOE1XEJZcgK2gwZ1Wfjb2FTjd7an8Qg4c/640?wx_fmt=png&from=appmsg)

找到
\*/api/v1/startup
类似的接口，鼠标长按接口选择请求重写，选择替换响应
1.去开屏广告

将消息体Body中splash\_ad{ }替换为以下内容：其余不变

```
 复制代码 隐藏代码
    "splash_ad": {
      "enabled": false,
      "overtime": 0,
      "ad": null
    },
   UPDATE_DESCRIPTION = "";
   NOTICE = "";
   placeholder = "";
```

2.去广告
\*/api/v1/ads

```
 复制代码 隐藏代码
    enabled = false;
    ads = {};
```

3.本地VIP
\*/api/v1/users

```
 复制代码 隐藏代码
{
      "promotion_days":9999,
      "vip_expired_at":"2099-09-09T09:09:09.000+09:00",
      "is_vip":true
    }
```

这里注意，要在重写里面新增一个Hearder

因为接口默认开启缓存，导致请求304，重写不生效
这个重写要把状态码、请求头、请求体开关全部打开，保证vip重写能够生效
最终重写列表：

![](https://mmbiz.qpic.cn/mmbiz_png/Gv6JExJQjUWhHUONK9xvcqAZGwIRHeCmI4DNn2TJrLLXlbUic5bsrZWKe8ia9Kjbyrw3ibDsVr9T1GhP7YBHkib6xeIDFU0Eutw06bskoAV70RE/640?wx_fmt=png&from=appmsg)

不出意外，清除缓存并重启APP就可以实现无广告，本地VIP

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Gv6JExJQjUUbKK9mBy5QicrhpicZA4wwUL7mWGxTA4icJMNiaCicuNkGX8HxchIgMiaUusSkadlIicTRpkkIxwIDosoQQGef0g8ibEftahhMyyjYPOM/640?wx_fmt=png&from=appmsg)

**·****今 日 推 荐****·**

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/Gv6JExJQjUVUSCX4NR7lu9ssq39VEHktnhxOLMWoczv02NjichcnNQqFcmt4N2TaCT9eOULUZRmpHggecEbbib8WdUGrvAWTXpn2MkSSm70QA/640?wx_fmt=jpeg&from=appmsg)

本文内容来自网络，如有侵权请联系删除

预览时标签不可点

阅读原文

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/WJRHqUiaud0ouQQFouib41PSeoKKZO7mHSXDQ01XdAqPlLVKZD1yyPlfnErolowiaaDic5GDnU7B2GNhkou8PGqaCQ/0?wx_fmt=png)

逆向有你

向上滑动看下一个

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/WJRHqUiaud0ouQQFouib41PSeoKKZO7mHSXDQ01XdAqPlLVKZD1yyPlfnErolowiaaDic5GDnU7B2GNhkou8PGqaCQ/0?wx_fmt=png)

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