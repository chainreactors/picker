---
title: 若依及其二开系统的渗透测试指南
url: https://mp.weixin.qq.com/s/aq2lp-xKk5SoS0YRj3jWIA
source: Doonsec's feed
date: 2026-05-23
fetch_date: 2026-05-24T05:55:28.229439
---

# 若依及其二开系统的渗透测试指南

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/oQ0sWhcqsVmK5AlQoX29WbUJibjhyDIFtibga0brBFwauibiajXwoW315xHSFOnXicZCULumIiaL9ZvfqSJibrFT49cr561qDIe0ITb2Uhnc2vqFb8/0?wx_fmt=jpeg)

# 若依及其二开系统的渗透测试指南

原创

进击的HACK
进击的HACK

进击的HACK

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

> 字数 665，阅读大约需 4 分钟

## 前言

若依系统简单易上手，一些公司在生产环境会使用，也有不少的二开系统。

有时候，在渗透测试时会遇到基于若依进行二开的系统。本文聊一聊这些系统如何测试，有哪些通用技巧。

## 常见的若依及其二开系统

**官方版本**

* • RuoYi https://github.com/yangzongzhuan/RuoYi
* • ruoyi-vue 前后端分离版 https://gitee.com/y\_project/RuoYi-Vue

**常用二开版本**

* • tony2y/RuoYi-flowable https://github.com/tony2y/RuoYi-flowable
* • dromara/RuoYi-Vue-Plus https://github.com/dromara/RuoYi-Vue-Plus
* • YunaiV/ruoyi-vue-pro https://github.com/YunaiV/ruoyi-vue-pro

## 历史漏洞测试

### ruoyi

* • 针对若依系统 nday 的常见各种姿势 https://www.freebuf.com/articles/web/423254.html

### ruoyi-vue

基于 ruoyi-vue 的可以使用下面的工具测试：

* • 若依 Vue 漏洞检测工具 https://github.com/kk12-30/ruoyi-Vue-tools

该工具之前是 exe 的，最近更新了，有了 jar 版本的。
![0373116b0a08ff264b68006ae48478cf.png](https://mmbiz.qpic.cn/sz_mmbiz_png/oQ0sWhcqsVmCdJcibJl84daOuPPnSVRMHnBYyVDjwzXtBQAJz3uZlSLkyQYHIz9Tlrsh979lGQzIyDxyuV90JuuWsNsy2bWlTDKv5GgtEAM4/640?from=appmsg "null")

0373116b0a08ff264b68006ae48478cf.png

* • RuoYi-Vue 历史漏洞 https://blog.takake.com/posts/41565/

## 参考测试点

### 路由

* • 用 MaR 自动加载若依动态路由：从手动替换到一键通杀 [https://mp.weixin.qq.com/s/CrSDginjGrUS31By32PORA](https://mp.weixin.qq.com/s?__biz=Mzg4Njg3MDk5Ng==&mid=2247487157&idx=1&sn=da79fd7a7f8e0587cb23ffda2b73018f&scene=21#wechat_redirect)

### 若依 SSTI 模板注入

* • 某依最新版本稳定 4.8.1 RCE (Thymeleaf 模板注入绕过) [https://mp.weixin.qq.com/s/uxvGbO4biM87DVSXA\_ZlQw](https://mp.weixin.qq.com/s?__biz=MzYzNjAzOTY3Ng==&mid=2247484799&idx=1&sn=92d02ffee3888077c3c70e10ef0ff710&scene=21#wechat_redirect)
* • 若依最新版本 4.8.1 漏洞 SSTI 绕过获取 ShiroKey 至 RCE(全 JAVA 版本绕过，附带 POC) [https://mp.weixin.qq.com/s/4yi0UOTgBCsGK6J8qSz8tQ](https://mp.weixin.qq.com/s?__biz=MzkzMzk5MTM2NA==&mid=2247484433&idx=1&sn=7505842ab9a9e8e3babcd88be28dcf81&scene=21#wechat_redirect)

### 任意用户注册

若依有一个注册接口，默认是禁止注册，但如果开放了，我们能直接注册账号进入后台。
下面的文章便是找到了开发若依注册功能的系统

> 记一次对大型国企 Ruoyi 系统曲折的打点测试 But lucky [https://mp.weixin.qq.com/s/0qPBciOrN9-VLYXo6AahAg](https://mp.weixin.qq.com/s?__biz=MzkyODMxODUwNQ==&mid=2247493472&idx=1&sn=1bc0e9ff875e2d99334ac383ba2e07ad&scene=21#wechat_redirect)

接口

```
/register
```

![4b1831285167800ca61414c5af257f1f.png](https://mmbiz.qpic.cn/sz_mmbiz_png/oQ0sWhcqsVkh81rIVjzzWf81ib16FFwhX39Y109RcqwB7Dwuib5Aqawo8rgKhLqlCzZhaoSepNN9XVEZVDtzS8ud6ZKtpdIByHzujjE5l3IOU/640?from=appmsg "null")

4b1831285167800ca61414c5af257f1f.png

默认
![db97efbb16f3adaeb1a0eac76dc6e935.png](https://mmbiz.qpic.cn/mmbiz_png/oQ0sWhcqsVkepggTnwmfSubRZ4vMtpMML0CeSOvRlwK1oxktTuXD0Rkw9Vq8iavopgpt20E0upqXdib03yNvPkKOemqfZj2BFVPiaduZnBJR2k/640?from=appmsg "null")

db97efbb16f3adaeb1a0eac76dc6e935.png

### druid 弱密码

若依系统默认是开启 druid 的，且为弱密码

```
/prod-api/druid/login.html
ruoyi
123456
```

但是我们在测试的时候，可能会出现光有 druid 页面，但是没办法爆破密码的情况，排除 druid 密码修改为了强密码，有可能是更改了用户名。
而这种更改可能不是故意的，比如在二开的过程中将关键词`ruoyi`全局替换为`gold`，而这个过程中就把 druid 默认的用户名改了。

所以我们只要知道替换的关键词是什么，就有可能登录 druid。

那么如何寻找呢？
一个地方是**版权信息**，这个地方可能修改为关键词
![3e1a3bada9f633b59f3111406413a3e2.png](https://mmbiz.qpic.cn/sz_mmbiz_png/oQ0sWhcqsVkPIKJ1XCdsZRcbXLWPXmN0cHUibewEWib8ngMKmBkxyZwfwvvP0BdI2M5lz1QA7T0RodZ8dZTbLeqnvvIic7G7WEopa3u8QOIS4s/640?from=appmsg "null")

3e1a3bada9f633b59f3111406413a3e2.png

如果存在 api-docs 未授权，也可以在其中发现
若依一般包含下面的模块
![3f4b2b4d43da2f43aeb427703387b1b7.png](https://mmbiz.qpic.cn/sz_mmbiz_png/oQ0sWhcqsVnib58I5JsuA7Oa4ywfl6ddetYvxNicN0eL5cN7E7IqOxxWeK5JBzSEa3hY9BIibMZS5MCQ7ef7HiaLAWcxQlibFhicu9TDjRwaMDqzE/640?from=appmsg "null")

3f4b2b4d43da2f43aeb427703387b1b7.png

如果修改后
在`/prod-api/swagger-resources`中
![ab0fc5fccf5e6326e52a9d7c69682f06.png](https://mmbiz.qpic.cn/sz_mmbiz_png/oQ0sWhcqsVkLQA0AVLY621CprZmXriajK4MBZ6UiarSJfD4A7no410sAMvbRbywAOZt65TlKOIic6KRL3tzn61THpQG7vNqicRVfXrLEliaL49Fk/640?from=appmsg "null")

ab0fc5fccf5e6326e52a9d7c69682f06.png

那么 druid 用户名就可能是 gold

### API 批量分配导致的普通用户垂直越权到 admin

API 批量分配导致的普通用户垂直越权到 admin
[https://mp.weixin.qq.com/s/-4GuugChfBLFUXQVbS\_TpQ](https://mp.weixin.qq.com/s?__biz=MzkxNjMwNDUxNg==&mid=2247485820&idx=1&sn=d62c97c7f544683b31280e8412dc7ee1&scene=21#wechat_redirect)

### 其他

* • 若依常见漏洞一把梭（上） [https://mp.weixin.qq.com/s/lMss5FGUxjyIyIQ4aH-4Mw](https://mp.weixin.qq.com/s?__biz=Mzk1NzgzMjkxOQ==&mid=2247487289&idx=1&sn=743528ef3e4a15b397cd42c08a5b3ecb&scene=21#wechat_redirect)
* • 若依常见漏洞一把梭（下） [https://mp.weixin.qq.com/s/30ZqYZJP6zf1R\_BYIKkqzA](https://mp.weixin.qq.com/s?__biz=Mzk1NzgzMjkxOQ==&mid=2247487336&idx=1&sn=e110f44e7d47bf138735038afad695c8&scene=21#wechat_redirect)

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/a1BOUvqnbriaKQaulUawUmcqevsicgRXaDWWcgmsbG7iaTtKE89ZwJEkPHzibEzXwcibLn8PKu1hGoicqAEIW9uQjyBw/640?wx_fmt=jpeg)

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/a1BOUvqnbrhOdQiaFvupNflYqfzCq5nzdjQF1j9ib5wTPYG8g3txOmd7mu8icbHfWCHTLibYzSOMlRrlLD9EicEESzA/0?wx_fmt=png)

进击的HACK

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/a1BOUvqnbrhOdQiaFvupNflYqfzCq5nzdjQF1j9ib5wTPYG8g3txOmd7mu8icbHfWCHTLibYzSOMlRrlLD9EicEESzA/0?wx_fmt=png)

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