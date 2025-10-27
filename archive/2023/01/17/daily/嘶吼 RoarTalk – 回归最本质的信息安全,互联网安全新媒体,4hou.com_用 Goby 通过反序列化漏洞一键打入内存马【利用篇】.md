---
title: 用 Goby 通过反序列化漏洞一键打入内存马【利用篇】
url: https://www.4hou.com/posts/xjK3
source: 嘶吼 RoarTalk – 回归最本质的信息安全,互联网安全新媒体,4hou.com
date: 2023-01-17
fetch_date: 2025-10-04T04:02:13.256849
---

# 用 Goby 通过反序列化漏洞一键打入内存马【利用篇】

用 Goby 通过反序列化漏洞一键打入内存马【利用篇】 - 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com

[![](https://www.4hou.com/sihou/images/new4hou/newlogoss.png)](https://www.4hou.com)

* [首页](https://www.4hou.com)
* [企业中心](https://www.4hou.com/corp/newindex)
* [产业研究院](https://www.4hou.com/real-time)

![](https://www.4hou.com/sihou/images/new4hou/search-icon.png)

[投稿](https://www.4hou.com/contribute)

[登录](https://www.4hou.com/login)
  |
[注册](https://www.4hou.com/register)

* 导读 ▾
* [活动](https://www.4hou.com/newticket)
* [专题](https://www.4hou.com/category/special)
* [图谱](https://www.4hou.com/atlas/index)
* [报告](https://www.4hou.com/new-report-info)
* [嘶票](https://www.4hou.com/tickets)
* [嘶货](https://www.4hou.com/shop)
* [企业查询](https://www.4hou.com/corp/new-search-company)
* [招聘](https://www.4hou.com/recruit)![](https://www.4hou.com/sihou/images/1561626446625934.png)

* [新闻](https://www.4hou.com/category/news)
* [行业](https://www.4hou.com/category/industry)
* [趋势](https://www.4hou.com/category/observation)
* [访谈](https://www.4hou.com/category/people)
* [漏洞](https://www.4hou.com/category/vulnerable)
* [WEB安全](https://www.4hou.com/category/web)
* [业务安全](https://www.4hou.com/category/business)
* [系统安全](https://www.4hou.com/category/system)
* [内网渗透](https://www.4hou.com/category/penetration)
* [勒索软件](https://www.4hou.com/category/typ)
* [安全工具](https://www.4hou.com/category/tools)

# 用 Goby 通过反序列化漏洞一键打入内存马【利用篇】

Goby
[行业](https://www.4hou.com/category/industry)
2023-01-16 16:06:36

![](https://img.4hou.com/article/%E6%B5%8F%E8%A7%88.png)266683

收藏

导语：Goby 使用者无需任何配置，就可以一键打入内存马。

![ncm.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230116/1673855318247232.png "1673854864108475.png")

Goby 社区第 22 篇技术分享文章

全文共：3734 字 预计阅读时间：10 分钟

---

## 0×01 前言

##

在上一篇[《Shell中的幽灵王者—JAVAWEB 内存马 【认知篇】》](https://mp.weixin.qq.com/s/44vf7fZv-O0yGMA6sVezKA)中，我从概念上介绍了很多内存马的东西，并给出了我的观点：“大势所趋下，内存马技术将会像 SQL 注入、文件上传一样，是以后每位安全研究员都必须掌握的安全技术”。

内存马技术很好，很棒，大人小孩都爱用，但实际上，一个不可避免的问题是，能熟练修改、调试、使用内存马的技术门槛，相对较高，除了漏洞利用所需要的安全知识，还需要对框架、中间件的设计模式、源码实现相当了解，并且面对不同版本、不同环境、不同 JDK 等情况进行多种兼容，仅针对一个目标进行攻击，可能需要大量的研究与调试，编写代码，这对项目通常时间比较紧的大多数漏洞利用者来讲，不是性价比最高的方式。

试想一下，如果遇到一个反序列化漏洞，你需要测试 Gadget，生成反序列化 payload，原版的 ysoserial 提供的 payload 一般就执行命令，而命令执行后也无法看到结果，在环境不出网的情况下更加无法知道怎么继续利用。在情况允许的情况下，攻击者可以打入内存马，但是面对中间件的版本不同，内核使用的技术可能不同，如果没有提前准备或根据指定环境调试相关的代码，很难一次利用成功。

那该怎么解决呢？我认为，针对某种漏洞类型，能提供一个通用的利用框架，可以覆盖绝大多数的情况，**让攻击者可以无视中间的技术，直接能够使用**，才是最好的办法，如果针对每个漏洞，还能够**提供最佳实践，让使用者点点点就可以了**，岂不美哉？

所以，请观看如下视频：

[【用 Goby 通过反序列化漏洞一键打入内存马【利用篇】](https://www.bilibili.com/video/BV1vR4y1Y7G8/?share_source=copy_web&vd_source=4784d8435f8ee3b6f6fa5b032a0ba2ea)

**感受到"点点点"的快乐了吗？我是脚本小子，我爱点点点，我喂自己袋盐**。接下来简单介绍一下插件的使用。

## 0×02 介绍

反序列化漏洞是什么、ysoserial 项目是什么在这里就不在赘述了，这里主要介绍的是这次融合在 Goby 中的插件的使用方式。

### 2.1 Gadget

说到反序列化漏洞，最重要的就是 Gadget，目标环境中，必须包含带有漏洞利用链的依赖，但是即使有了依赖，还可能因为依赖不全、版本不同等等各种原因，导致利用失败。

Goby 通过动态修改类字节码、反序列化流等手段，提供了不同依赖版本、不同利用方式等共计 65 条反序列化 Gadget，可以覆盖绝大多数的漏洞利用场景。

使用者可以按需选择自己想使用的 Gadget。

![1.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230116/1673855319849960.png "1673854930194134.png")

如若转载，请注明原文地址

* 分享至

![取消](https://www.4hou.com/sihou/images/close.jpg)
![嘶吼](https://www.4hou.com/sihou/images/logo.png)

感谢您的支持，我会继续努力的!

![扫码支持]( "扫一扫")

打开微信扫一扫后点击右上角即可分享哟

### 发表评论

评论

![](https://www.4hou.com/captcha/flat?QmFvPO1D)

#### 你可能感兴趣的

* [![]()

  Exchange/M365最新防范攻略！CACTER三步补齐原生防护短板](https://www.4hou.com/posts/l03l)
* [![]()

  【附下载】2025我们身边的 网信安全 典型案例等 官方视频汇编](https://www.4hou.com/posts/kg3x)
* [![]()

  蝉联荣誉！梆梆安全再度获选 “北京市委网信办第二届网络安全技术支撑单位”](https://www.4hou.com/posts/9jKP)
* [![]()

  聚焦可信AI安全！SDC2025 议题重磅揭晓](https://www.4hou.com/posts/gy39)
* [![]()

  2025第五届太原网络安全高峰论坛成功举办](https://www.4hou.com/posts/8gJl)
* [![]()

  特勤局手册 | 监听办公室](https://www.4hou.com/posts/42B2)

![](https://img.4hou.com/portraits/f8c7a9e0093d81eb59309a8fcf2cd326.png)

# [Goby](https://www.4hou.com/member/6V1N)

Attack surface mapping

#### 最新文章

* [Exchange/M365最新防范攻略！CACTER三步补齐原生防护短板](https://www.4hou.com/posts/l03l)
  2025-09-29 17:48:04
* [【附下载】2025我们身边的 网信安全 典型案例等 官方视频汇编](https://www.4hou.com/posts/kg3x)
  2025-09-29 14:55:37
* [蝉联荣誉！梆梆安全再度获选 “北京市委网信办第二届网络安全技术支撑单位”](https://www.4hou.com/posts/9jKP)
  2025-09-29 14:23:50
* [聚焦可信AI安全！SDC2025 议题重磅揭晓](https://www.4hou.com/posts/gy39)
  2025-09-28 17:20:40

[查看更多](https://www.4hou.com/member/6V1N)

# 相关热文

* [Exchange/M365最新防范攻略！CACTER三步补齐原生防护短板](https://www.4hou.com/posts/l03l)

  CACTER
* [【附下载】2025我们身边的 网信安全 典型案例等 官方视频汇编](https://www.4hou.com/posts/kg3x)

  网络伍豪
* [蝉联荣誉！梆梆安全再度获选 “北京市委网信办第二届网络安全技术支撑单位”](https://www.4hou.com/posts/9jKP)

  梆梆安全
* [聚焦可信AI安全！SDC2025 议题重磅揭晓](https://www.4hou.com/posts/gy39)

  企业资讯
* [2025第五届太原网络安全高峰论坛成功举办](https://www.4hou.com/posts/8gJl)

  企业资讯
* [特勤局手册 | 监听办公室](https://www.4hou.com/posts/42B2)

  RC2反窃密实验室

![]()

[公司简介](https://www.4hou.com/about?title=公司简介)
|
[我要投稿](https://www.4hou.com/about?title=我要投稿)
|
[更新日志](https://www.4hou.com/about?title=更新日志)
|
[友情链接](https://www.4hou.com/about?title=友情链接)
|
[隐私政策](https://www.4hou.com/about?title=隐私政策)
|

[![](https://www.4hou.com/sihou/images/new4hou/weibo.png)](http://weibo.com/u/6069423878)
![](https://www.4hou.com/sihou/images/new4hou/wechat.png)

本站4hou.com，所使用的字体和图片文字等素材部分来源于原作者或互联网共享平台。如使用任何字体和图片文字有侵犯其版权所有方的，嘶吼将配合联系原作者核实，并做出删除处理。

[©2024 北京嘶吼文化传媒有限公司 京ICP备16063439号-1](https://beian.miit.gov.cn/)
本站由 ![](https://www.4hou.com/sihou/images/new4hou/txcloud.png) ![](https://www.4hou.com/sihou/images/new4hou/bdcloud.png) ![](https://www.4hou.com/sihou/images/new4hou/ucloud.png) 提供云计算服务

微信

[微博](http://weibo.com/u/6069423878)
[RSS](https://www.4hou.com/feed)
[知乎](https://zhuanlan.zhihu.com/roartalk)