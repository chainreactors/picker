---
title: [Golang]Nps二开魔改版(Debug版)
url: https://www.nctry.com/2776.html
source: TRY博客
date: 2025-08-06
fetch_date: 2025-10-07T00:17:42.465652
---

# [Golang]Nps二开魔改版(Debug版)

[![TRY博客](https://www.nctry.com/wp-content/uploads/2018/11/20181120_091128_42.png)](https://www.nctry.com)

* [随手记](https://www.nctry.com/xjb)
* [渗透学习](https://www.nctry.com/category/hacker)
* [本站友好作者](https://www.nctry.com/%E6%9C%AC%E7%AB%99%E5%8F%8B%E5%A5%BD%E4%BD%9C%E8%80%85)
* [隐私政策](https://www.nctry.com/privacy)
* [关于站长](https://www.nctry.com/about)
* [友链](https://www.nctry.com/link)

# [Golang]Nps二开魔改版(Debug版)

[TRY](https://www.nctry.com/2776.html)

2025-08-05

407

[0](https://www.nctry.com/2776.html#respond)

# 至少我们曾经在一起过。

来自：一言

# 同样也是几年前的项目了，可配合一键debug开启使用。

项目地址:[https://github.com/TryGOTry/Debug-Nps](https://www.nctry.com/go/?url=https://github.com/TryGOTry/Debug-Nps)

# nps魔改Debug版

## 介绍

几年前的项目了，现在开源。在原版nps的基础上，增加了nps探测，以及对应的利用方式（如获取cookie，页面等），进行一些简单的二开。未经过大量测试，可能存在bug。 详细用法：可看nps官方

# 二开说明

```
1.流量重新加密
2.参数加密(AES加解密，可以自行修改aes的key，默认是是:12367dsadwqe890x)
3.debug调试模式探测和利用
4.ui修改等
5.更加人性化:socks5代理设置备注等
6.增加401认证,避免被全网扫描(在nps的conf中的good.conf里配置) 401_user_name,401_user_pass
```

# 部分截图

1.和nps一样，只是多了个debug端口设置

![](https://www.nctry.com/wp-content/uploads/2025/08/1.png)

2.如果目标开启debug后会自动返回ua头，可点击Debug按钮获取详细

![](https://www.nctry.com/wp-content/uploads/2025/08/2.png)

3.获取的cookie都是js语句，直接可以一键设置cookie

![](https://www.nctry.com/wp-content/uploads/2025/08/3.png)

4.也可开启socks5代理,密码不设置的话就是随机

![](https://www.nctry.com/wp-content/uploads/2025/08/4.png)

## 如何开启debug

可配合另外一个项目使用：[https://github.com/TryGOTry/ChromeDebugLnk](https://www.nctry.com/go/?url=https://github.com/TryGOTry/ChromeDebugLnk)

本文作者为[TRY](https://www.nctry.com/2776.html)，转载请注明。

[debug](https://www.nctry.com/tag/debug) [nps](https://www.nctry.com/tag/nps)

0人点赞

发表评论
取消回复

昵称（必填）

邮箱（必填）

网址

表情
 图片
 链接
 代码

[x] 接收回复邮件通知
 提交评论

分享

微信

微博

QQ

by:TRY

蜀ICP备18037281号-2| TRY博客 |
Copyright © nctry.com

夜间模式
[ ]

---

100