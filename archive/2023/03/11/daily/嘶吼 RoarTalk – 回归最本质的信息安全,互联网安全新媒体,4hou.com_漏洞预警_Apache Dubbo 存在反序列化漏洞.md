---
title: 漏洞预警|Apache Dubbo 存在反序列化漏洞
url: https://www.4hou.com/posts/DEBx
source: 嘶吼 RoarTalk – 回归最本质的信息安全,互联网安全新媒体,4hou.com
date: 2023-03-11
fetch_date: 2025-10-04T09:12:44.361861
---

# 漏洞预警|Apache Dubbo 存在反序列化漏洞

漏洞预警|Apache Dubbo 存在反序列化漏洞 - 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com

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

# 漏洞预警|Apache Dubbo 存在反序列化漏洞

棱镜七彩
[行业](https://www.4hou.com/category/industry)
2023-03-10 09:57:12

![](https://img.4hou.com/article/%E6%B5%8F%E8%A7%88.png)119863

收藏

导语：近日网上有关于开源项目Apache Dubbo 存在反序列化漏洞，棱镜七彩威胁情报团队第一时间探测到，经分析研判，向全社会发起开源漏洞预警公告，提醒相关安全团队及时响应

**棱镜七彩安全预警**

近日网上有关于开源项目Apache Dubbo 存在反序列化漏洞，棱镜七彩威胁情报团队第一时间探测到，经分析研判，向全社会发起开源漏洞预警公告，提醒相关安全团队及时响应。

**项目介绍**

Apache Dubbo 是一款 RPC 服务开发框架，用于解决微服务架构下的服务治理与通信问题，官方提供了 Java、Golang 等多语言 SDK 实现。使用 Dubbo 开发的微服务原生具备相互之间的远程地址发现与通信能力， 利用 Dubbo 提供的丰富服务治理特性，可以实现诸如服务发现、负载均衡、流量调度等服务治理诉求。Dubbo 被设计为高度可扩展，用户可以方便的实现流量拦截、选址的各种定制逻辑。

**项目主页**

https://cn.dubbo.apache.org/

**代码托管地址**

https://github.com/apache/dubbo

**CVE编号**

[CVE-2023-23638](https://nvd.nist.gov/vuln/detail/CVE-2023-23638)

**漏洞情况**

Apache Dubbo 是一款 RPC 服务开发框架，用于解决微服务架构下的服务治理与通信问题，官方提供了 Java、Golang 等多语言 SDK 实现。该项目受影响版本存在反序列化漏洞，由于Dubbo在序列化时检查不够全面，当攻击者可访问到dubbo服务时，可通过构造恶意请求绕过检查触发反序列化，执行恶意代码

**受影响的版本**

org.apache.dubbo:dubbo-common@[3.0.0, 3.0.14)

org.apache.dubbo:dubbo-qos@[3.1.0, 3.1.6)

org.apache.dubbo:dubbo-common@[2.7.0, 2.7.22)

**修复方案**

将组件 org.apache.dubbo:dubbo-common 升级至 3.0.14 及以上版本

将组件 org.apache.dubbo:dubbo-qos 升级至 3.1.6 及以上版本

将组件 org.apache.dubbo:dubbo-common 升级至 2.7.22 及以上版本

**链接地址：**

<https://nvd.nist.gov/vuln/detail/CVE-2023-23638>

<https://cn.dubbo.apache.org/zh-cn/overview/mannual/java-sdk/advanced-features-and-usage/security/class-check/>

<https://github.com/apache/dubbo/commit/6e5c1f8665216ccda4b2eb8c0465882efe62dd61>

<https://github.com/apache/dubbo/commit/ce3b0e285a463b566a9d685049201bfaf526c8ac#diff-fa4e0fb5d923710d8f070b478addd5e3638e101fdf9a3e32a855f429f90eed09>

<https://github.com/apache/dubbo/commit/4f664f0a3d338673f4b554230345b89c580bccbb>

查看更多安全漏洞：[快速查询安全漏洞 ｜ 柒巧板](https://spdx.cn/safety)

如若转载，请注明原文地址

* 分享至

![取消](https://www.4hou.com/sihou/images/close.jpg)
![嘶吼](https://www.4hou.com/sihou/images/logo.png)

### 发表评论

评论

![](https://www.4hou.com/captcha/flat?xpTw190o)

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

![](https://img.4hou.com/portraits/4fb31b21420c34b053939ec1fc0a9646.png)

# [棱镜七彩](https://www.4hou.com/member/VGo9)

专注开源安全合规，专注供应链安全

#### 最新文章

* [Exchange/M365最新防范攻略！CACTER三步补齐原生防护短板](https://www.4hou.com/posts/l03l)
  2025-09-29 17:48:04
* [【附下载】2025我们身边的 网信安全 典型案例等 官方视频汇编](https://www.4hou.com/posts/kg3x)
  2025-09-29 14:55:37
* [蝉联荣誉！梆梆安全再度获选 “北京市委网信办第二届网络安全技术支撑单位”](https://www.4hou.com/posts/9jKP)
  2025-09-29 14:23:50
* [聚焦可信AI安全！SDC2025 议题重磅揭晓](https://www.4hou.com/posts/gy39)
  2025-09-28 17:20:40

[查看更多](https://www.4hou.com/member/VGo9)

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