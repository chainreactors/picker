---
title: Grafana ：最高级别漏洞可实现管理员身份冒充
url: https://www.4hou.com/posts/W13X
source: 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com
date: 2025-11-26
fetch_date: 2025-11-27T03:10:30.145706
---

# Grafana ：最高级别漏洞可实现管理员身份冒充

Grafana ：最高级别漏洞可实现管理员身份冒充 - 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com

[![](https://www.4hou.com/sihou/images/new4hou/newlogoss.png)](https://www.4hou.com)

* [首页](https://www.4hou.com)
* [企业中心](https://www.4hou.com/corp/newindex)
* [产业研究院](https://www.4hou.com/real-time)

![](https://www.4hou.com/sihou/images/new4hou/search-icon.png)

[投稿](https://www.4hou.com/contribute)

[登录](https://www.4hou.com/loginIng)
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

# Grafana ：最高级别漏洞可实现管理员身份冒充

胡金鱼
[漏洞](https://www.4hou.com/category/vulnerable)
23小时 前发布

![](https://img.4hou.com/article/%E6%B5%8F%E8%A7%88.png)7122

收藏

导语：在特定场景下，该漏洞可能导致新配置的用户被识别为已存在的内部账号（如管理员账号），进而引发账号冒充或权限提升风险。

Grafana Labs 发布安全预警，其企业版产品中存在一处最高严重级别漏洞（CVE-2025-41115）。攻击者可利用该漏洞将新创建用户伪装成管理员，或实现权限提升操作。

需注意的是，该漏洞仅在跨域身份管理系统配置并启用的场景下可被利用。具体而言，只有当“enableSCIM”功能开关与“user\_sync\_enabled”选项均设置为“true”时，恶意或已被劫持的 SCIM 客户端才能通过配置“数字格式 externalId”的方式，将新用户关联到包括管理员在内的内部账号。其中，externalId 是身份提供商用于追踪用户的 SCIM 记账属性。

由于 Grafana 会将该属性值直接映射到内部用户的“user.uid”字段，像“1”这样的数字格式 externalId 可能被系统识别为已存在的内部账号，进而导致账号冒充或权限提升风险。

根据 Grafana 官方文档，SCIM 配置功能目前处于“公开预览”阶段，支持力度有限，因此该功能的实际应用范围可能并不广泛。

Grafana 作为一款数据可视化与监控平台，用户群体覆盖各类组织——从小型初创企业到知名大型企业均在使用。其核心功能是将指标数据、日志及其他运维数据转化为可视化仪表盘、告警通知与分析报告。

Grafana Labs 表示：“在特定场景下，该漏洞可能导致新配置的用户被识别为已存在的内部账号（如管理员账号），进而引发账号冒充或权限提升风险。”

**漏洞影响范围与修复方案**

CVE-2025-41115 漏洞影响 Grafana 企业版 12.0.0 至 12.2.1 版本（需满足 SCIM 已启用的条件）。其中，Grafana 开源版（OSS）用户不受影响；Grafana 云服务（包括亚马逊托管 Grafana、Azure 托管 Grafana）已完成补丁部署。

对于自托管部署的管理员，可通过安装以下任一更新版本修复漏洞：

**·**Grafana 企业版 12.3.0

**·**Grafana 企业版 12.2.1

**·**Grafana 企业版 12.1.3

**·**Grafana 企业版 12.0.6

**漏洞发现与处置时间线**

该漏洞于 11 月 4 日在内部审计过程中被发现，约 24 小时后 Grafana 团队便推出了安全更新。在此期间，Grafana Labs 经调查确认，该漏洞未在 Grafana 云服务中被实际利用。11 月 19 日，官方正式发布安全更新及配套公告。官方建议 Grafana 用户尽快安装可用补丁，或通过修改配置（禁用 SCIM 功能）阻断潜在攻击路径。

上月，实时情报公司 GreyNoise 曾报告针对 Grafana 旧版路径遍历漏洞的扫描活动异常增多。研究人员此前指出，这类扫描活动可能是为探测暴露的 Grafana 实例，为后续新漏洞披露后的攻击做准备。目前，Grafana Labs 已向客户推送补丁版本，并完成相关防护配置部署，且Grafana 开源版用户不受此漏洞影响。

文章来源自：https://www.bleepingcomputer.com/news/security/grafana-warns-of-max-severity-admin-spoofing-vulnerability/如若转载，请注明原文地址

* 分享至

![取消](https://www.4hou.com/sihou/images/close.jpg)
![嘶吼](https://www.4hou.com/sihou/images/logo.png)

### 发表评论

评论

![](https://www.4hou.com/captcha/flat?kvy6EsPM)

#### 你可能感兴趣的

* [![]()

  微软：Windows 11 24H2 高危漏洞导致文件资源管理器等核心组件崩溃](https://www.4hou.com/posts/QX9q)
* [![]()

  Grafana ：最高级别漏洞可实现管理员身份冒充](https://www.4hou.com/posts/W13X)
* [![]()

  ImunifyAV曝远程代码执行漏洞 数百万Linux托管网站面临风险](https://www.4hou.com/posts/rpAk)
* [![]()

  高危runC漏洞曝光 黑客可突破Docker容器逃逸](https://www.4hou.com/posts/XP4l)
* [![]()

  Windows Server WSUS高危漏洞遭在野利用 微软紧急发布补丁](https://www.4hou.com/posts/nlpD)
* [![]()

  Windows SMB高危提权漏洞遭活跃利用 未打补丁设备恐被获取SYSTEM权限](https://www.4hou.com/posts/8g5l)

![](https://img.4hou.com/images/微信图片_20231102150249.jpg)

# [胡金鱼](https://www.4hou.com/member/BVMN)

这个家伙很懒,什么也没说!

#### 最新文章

* [微软：Windows 11 24H2 高危漏洞导致文件资源管理器等核心组件崩溃](https://www.4hou.com/posts/QX9q)
  2025-11-26 12:01:00
* [Grafana ：最高级别漏洞可实现管理员身份冒充](https://www.4hou.com/posts/W13X)
  2025-11-26 12:00:00
* [ImunifyAV曝远程代码执行漏洞 数百万Linux托管网站面临风险](https://www.4hou.com/posts/rpAk)
  2025-11-21 12:00:00
* [高危runC漏洞曝光 黑客可突破Docker容器逃逸](https://www.4hou.com/posts/XP4l)
  2025-11-19 11:10:33

[查看更多](https://www.4hou.com/member/BVMN)

# 相关热文

* [微软：Windows 11 24H2 高危漏洞导致文件资源管理器等核心组件崩溃](https://www.4hou.com/posts/QX9q)

  胡金鱼
* [Grafana ：最高级别漏洞可实现管理员身份冒充](https://www.4hou.com/posts/W13X)

  胡金鱼
* [ImunifyAV曝远程代码执行漏洞 数百万Linux托管网站面临风险](https://www.4hou.com/posts/rpAk)

  胡金鱼
* [高危runC漏洞曝光 黑客可突破Docker容器逃逸](https://www.4hou.com/posts/XP4l)

  胡金鱼
* [Windows Server WSUS高危漏洞遭在野利用 微软紧急发布补丁](https://www.4hou.com/posts/nlpD)

  胡金鱼
* [Windows SMB高危提权漏洞遭活跃利用 未打补丁设备恐被获取SYSTEM权限](https://www.4hou.com/posts/8g5l)

  胡金鱼

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