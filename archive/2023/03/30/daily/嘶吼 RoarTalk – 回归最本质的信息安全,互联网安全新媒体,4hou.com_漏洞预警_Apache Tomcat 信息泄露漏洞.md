---
title: 漏洞预警|Apache Tomcat 信息泄露漏洞
url: https://www.4hou.com/posts/WBkg
source: 嘶吼 RoarTalk – 回归最本质的信息安全,互联网安全新媒体,4hou.com
date: 2023-03-30
fetch_date: 2025-10-04T11:06:03.323038
---

# 漏洞预警|Apache Tomcat 信息泄露漏洞

漏洞预警|Apache Tomcat 信息泄露漏洞 - 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com

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

# 漏洞预警|Apache Tomcat 信息泄露漏洞

棱镜七彩
[行业](https://www.4hou.com/category/industry)
2023-03-29 16:08:12

![](https://img.4hou.com/article/%E6%B5%8F%E8%A7%88.png)112879

收藏

导语：近日网上有关于开源项目Apache Tomcat 信息泄露漏洞，棱镜七彩威胁情报团队第一时间探测到，经分析研判，向全社会发起开源漏洞预警公告，提醒相关安全团队及时响应

**棱镜七彩安全预警**

近日网上有关于开源项目Apache Tomcat 信息泄露漏洞，棱镜七彩威胁情报团队第一时间探测到，经分析研判，向全社会发起开源漏洞预警公告，提醒相关安全团队及时响应。

**项目介绍**

Tomcat是Apache 软件基金会（Apache Software Foundation）的Jakarta 项目中的一个核心项目，由Apache、Sun 和其他一些公司及个人共同开发而成。由于有了Sun 的参与和支持，最新的Servlet 和JSP 规范总是能在Tomcat 中得到体现，Tomcat 5支持最新的Servlet 2.4 和JSP 2.0 规范。因为Tomcat 技术先进、性能稳定，而且免费。成为目前比较流行的Web 应用服务器。

**项目主页**

<https://tomcat.apache.org/>

**代码托管地址**

[https://github.com/apache/tomcat](https://github.com/apache/tomcat/commit/c64d496dda1560b5df113be55fbfaefec349b50f)

**CVE编号**

[CVE-2023-28708](https://nvd.nist.gov/vuln/detail/CVE-2023-28708)

**漏洞情况**

Apache Tomcat 是一款开源的 Web 应用服务器，RemoteIpFilter 是一个过滤器，用于将 HTTP 请求中代理服务器的 IP 地址替换为客户端的真实 IP 地址。

受影响版本中，当使用 RemoteIpFilter 处理通过 HTTP 从反向代理接收到的请求时，如果请求头中包含设置为 https 的 X-Forwarded-Proto 字段，Tomcat 创建的会话 cookie 将不包括 secure 属性，攻击者可能通过中间人攻击获取用户 cookie，从而使用受害者身份执行恶意操作。

**受影响的版本**

org.apache.tomcat:tomcat-catalina@[11.0.0, 11.0.0-M3)

org.apache.tomcat:tomcat-catalina@[10.0.0, 10.1.6)

org.apache.tomcat:tomcat-catalina@[9.0.0, 9.0.72)

org.apache.tomcat:tomcat-catalina@[8.0.0, 8.5.86)

**修复方案**

当前官方已发布最新版本，建议受影响的用户及时更新升级到最新版本。各个版本链接如下：

Apache Tomcat 11系列: https://tomcat.apache.org/download-11.cgi

Apache Tomcat 10系列: https://tomcat.apache.org/download-10.cgi

Apache Tomcat 9系列: https://tomcat.apache.org/download-90.cgi

Apache Tomcat 8系列: <https://tomcat.apache.org/download-80.cgi>

**链接地址**：

<https://nvd.nist.gov/vuln/detail/CVE-2023-28708>

<https://tomcat.apache.org/security-11.html>

<https://github.com/apache/tomcat/commit/c64d496dda1560b5df113be55fbfaefec349b50f>

查看更多安全漏洞：[快速查询安全漏洞 ｜ 柒巧板](https://weibo.cn/sinaurl?u=https%3A%2F%2Fspdx.cn%2Fsafety)

如若转载，请注明原文地址

* 分享至

![取消](https://www.4hou.com/sihou/images/close.jpg)
![嘶吼](https://www.4hou.com/sihou/images/logo.png)

### 发表评论

评论

![](https://www.4hou.com/captcha/flat?gaxf4MvP)

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