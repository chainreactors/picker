---
title: HPE Aruba漏洞致敏感信息遭未授权访问
url: https://www.4hou.com/posts/DxX5
source: 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com
date: 2026-01-16
fetch_date: 2026-01-17T03:26:45.677140
---

# HPE Aruba漏洞致敏感信息遭未授权访问

HPE Aruba漏洞致敏感信息遭未授权访问 - 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com

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

# HPE Aruba漏洞致敏感信息遭未授权访问

山卡拉
[漏洞](https://www.4hou.com/category/vulnerable)
2026-01-16 10:52:54

![](https://img.4hou.com/article/%E6%B5%8F%E8%A7%88.png)6168

收藏

导语：HPE已发布安全补丁，修复其Networking Instant On设备中存在的多个高危漏洞。

HPE已发布安全补丁，修复其Networking Instant On设备中存在的多个高危漏洞。这些漏洞可能泄露内部VLAN配置数据，允许远程攻击者破坏无线网络或未授权获取敏感网络信息。

![Silent Aruba Data Ex..._imresizer.jpg](https://img.4hou.com/uploads/ueditor/php/upload/image/20260116/1768531754135544.jpg "1768531754135544.jpg")

上述缺陷影响运行3.3.1.0及以下版本软件的Instant On接入点和1930交换机，3.3.2.0及更高版本已包含对应修复程序。

根据HPE安全公告HPESBNW04988，最严重的漏洞（编号CVE-2025-37165）存在于HPE Networking Instant On接入点的路由器模式配置中，会导致VLAN信息在非预期网络接口上泄露。

当设备以路由器模式运行时，精心构造的流量会使内部网络配置细节（如VLAN标识符及分段设计）通过数据包外泄，而此类数据包本不应包含此类信息。

**HPE Aruba Instant On缺陷泄露网络细节**

该漏洞无需身份验证或用户交互，可通过网络远程利用，严重等级为高，CVSS v3.1评分为7.5，对数据机密性影响极大，但不直接影响数据完整性或系统可用性。

HPE警告称，能够监控或注入受影响接口流量的恶意攻击者，可利用泄露的VLAN及拓扑数据绘制内部网段地图，进而策划进一步横向渗透或针对网络敏感区域的定向攻击。

目前该漏洞无临时解决方案，由Quora.org的丹尼尔·J·布鲁曼（Daniel J Blueman）发现并报告，其CVSS向量为CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:N/A:N，属于网络型低复杂度漏洞，无需任何权限即可利用。

第二个高危漏洞（编号CVE-2025-37166）同样影响HPE Networking Instant On接入点，当设备处理特制网络数据包时可能被触发。

成功利用该漏洞可导致接入点陷入无响应状态，部分情况下需硬重置才能恢复服务，使攻击者得以对Wi-Fi基础设施实施远程拒绝服务攻击。

该漏洞由GreyCortex的彼得·切尔马尔（Petr Chelmar）发现，同样被评定为“高危”，CVSS v3.1评分为7.5，向量为CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:N/I:N/A:H，凸显其对系统可用性的影响，而非数据安全性或完整性。

此外，HPE Instant On设备还受底层操作系统内核中多个数据包处理漏洞影响，对应编号为CVE-2023-52340和CVE-2022-48839。

这些内核级漏洞源于IPv4和IPv6数据包处理机制缺陷，可能导致设备运行期间出现拒绝服务故障及内存损坏，严重等级均为高，CVSS评分最高可达7.5，具体分值视漏洞编号及攻击向量而定。

HPE表示，内核开发人员已在 upstream 层面修复这些漏洞，HPE Instant On工程团队也已完成集成，除升级软件外，无其他针对性临时解决方案。

截至发稿，HPE尚未发现针对这些漏洞的公开利用代码或活跃攻击行为。

HPE建议受影响的Aruba Instant On 1930交换机系列及Instant On接入点，尽快升级至3.3.2.0及更高版本软件。升级可通过2025年12月10日当周推送的自动更新完成，也可通过Instant On应用程序或Web门户手动操作。

本文翻译自：https://gbhackers.com/nissan-motor-breach/如若转载，请注明原文地址

* 分享至

![取消](https://www.4hou.com/sihou/images/close.jpg)
![嘶吼](https://www.4hou.com/sihou/images/logo.png)

感谢您的支持，我会继续努力的!

![扫码支持]( "扫一扫")

打开微信扫一扫后点击右上角即可分享哟

### 发表评论

评论

![](https://www.4hou.com/captcha/flat?lnVlnSxv)

#### 你可能感兴趣的

* [![]()

  CVE-2026-20824漏洞：Windows远程协助存在安全功能绕过风险](https://www.4hou.com/posts/EyY4)
* [![]()

  HPE Aruba漏洞致敏感信息遭未授权访问](https://www.4hou.com/posts/DxX5)
* [![]()

  Ni8mare高危漏洞来袭 黑客可远程劫持n8n服务器](https://www.4hou.com/posts/om3A)
* [![]()

  WebRAT恶意软件借GitHub伪造漏洞利用程序传播](https://www.4hou.com/posts/Bvw2)
* [![]()

  MongoBleed高危漏洞遭在野利用 8万台MongoDB服务器暴露风险](https://www.4hou.com/posts/OGNB)
* [![]()

  漏洞预警 | MongoDB 存在未授权内存泄露漏洞（CVE-2025-14847）](https://www.4hou.com/posts/QXPM)

![](https://img.4hou.com/FjC8MmzrcnfY_rzJyoXU2_G-O0i9)

# [山卡拉](https://www.4hou.com/member/azxO)

这个家伙很懒,什么也没说!

#### 最新文章

* [CVE-2026-20824漏洞：Windows远程协助存在安全功能绕过风险](https://www.4hou.com/posts/EyY4)
  2026-01-16 11:17:10
* [HPE Aruba漏洞致敏感信息遭未授权访问](https://www.4hou.com/posts/DxX5)
  2026-01-16 10:52:54
* [Ni8mare高危漏洞来袭 黑客可远程劫持n8n服务器](https://www.4hou.com/posts/om3A)
  2026-01-12 12:00:00
* [WebRAT恶意软件借GitHub伪造漏洞利用程序传播](https://www.4hou.com/posts/Bvw2)
  2026-01-04 12:00:00

[查看更多](https://www.4hou.com/member/azxO)

# 相关热文

* [CVE-2026-20824漏洞：Windows远程协助存在安全功能绕过风险](https://www.4hou.com/posts/EyY4)

  山卡拉
* [HPE Aruba漏洞致敏感信息遭未授权访问](https://www.4hou.com/posts/DxX5)

  山卡拉
* [Ni8mare高危漏洞来袭 黑客可远程劫持n8n服务器](https://www.4hou.com/posts/om3A)

  胡金鱼
* [WebRAT恶意软件借GitHub伪造漏洞利用程序传播](https://www.4hou.com/posts/Bvw2)

  胡金鱼
* [MongoBleed高危漏洞遭在野利用 8万台MongoDB服务器暴露风险](https://www.4hou.com/posts/OGNB)

  胡金鱼
* [漏洞预警 | MongoDB 存在未授权内存泄露漏洞（CVE-2025-14847）](https://www.4hou.com/posts/QXPM)

  盛邦安全

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