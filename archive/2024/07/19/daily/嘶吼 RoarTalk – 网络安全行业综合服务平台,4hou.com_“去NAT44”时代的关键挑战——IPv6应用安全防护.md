---
title: “去NAT44”时代的关键挑战——IPv6应用安全防护
url: https://www.4hou.com/posts/ArnO
source: 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com
date: 2024-07-19
fetch_date: 2025-10-06T17:40:40.825519
---

# “去NAT44”时代的关键挑战——IPv6应用安全防护

“去NAT44”时代的关键挑战——IPv6应用安全防护 - 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com

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

# “去NAT44”时代的关键挑战——IPv6应用安全防护

盛邦安全
[行业](https://www.4hou.com/category/industry)
2024-07-18 17:56:09

![](https://img.4hou.com/article/%E6%B5%8F%E8%A7%88.png)74049

收藏

导语：近日，工业和信息化部办公厅、中央网信办秘书局联合印发《关于开展“网络去NAT”专项工作 进一步深化IPv6部署应用》的通知。

近日，工业和信息化部办公厅、中央网信办秘书局联合印发《关于开展“网络去NAT”专项工作 进一步深化IPv6部署应用》的通知。该通知指出，IPv4到IPv4网络地址转换（NAT44）设备在一定程度上阻碍了IPv6规模部署和应用水平的进一步提升，为加快IPv6规模部署和流量提升，需要开展“网络去NAT”专项工作。在应用方面，通知要求，互联网企业要深化应用服务IPv6升级改造，优化放量引流策略，实现注册、登录、使用全链条支持IPv6，提升固网环境下IPv6流量占比。

IPv6时代的来临为网络带来了更高效和透明的运行模式，同时也伴随着IPv6业务、应用、服务器等网络资产的安全防护面临更为严峻的挑战。

**“去NAT44”时代，资产暴露面风险增加**

以往，NAT44技术在一定程度上掩盖了设备的真实地址，减少了直接攻击的可能性。然而，随着IPv6地址的直接暴露，设备如同置身于“光天化日”之下，虽然提升了网络效率和透明度，但也显著增加了被攻击的风险。攻击者能更直接地访问服务器，尝试各种恶意手段，如DDoS攻击、SQL注入及跨站脚本攻击等。此外，许多安全设备虽然具备处理IPv6流量的能力，但却常因默认仅开启对IPv4的防护策略，也使得网络暴露于风险之中。

**安全威胁多元化，IPv6面临新挑战**

**地址空间扩大带来的扫描风险：**IPv6巨大的地址空间使得攻击者更容易进行随机地址扫描，寻找潜在的攻击目标。

**新协议特性引发的漏洞：**IPv6的新协议头和扩展头可能存在未知的安全漏洞，容易被攻击者利用。

**自动化配置带来的安全风险：**IPv6支持无状态和有状态的地址自动配置方式，这可能被攻击者利用来实施地址冲突和拒绝服务攻击。

**邻居发现协议（NDP）的脆弱性：**NDP可能面临欺骗报文攻击和拒绝服务攻击，攻击者可能利用NDP的缺陷来截取数据或发起其他攻击。

**IPv6应用安全防护建议**

**全面评估IPv6网络环境：**对现有网络架构进行评估，确保全面支持IPv6，并识别潜在的安全风险点。

**部署RayWAF加固安全防线：**在关键Web应用前部署RayWAF，作为防御第一线，抵御外部攻击。

**制定IPv6安全策略：**根据业务需求，制定IPv6环境下的安全策略，包括精细化的访问控制和数据加密措施等。

**强化网络安全监控：**利用RayWAF的监控功能，实时监测IPv6流量，及时发现漏洞并进行响应，确保Web应用的安全性。

**定期安全审计与培训：**定期对网络安全进行审计，及时安装系统更新和安全补丁，加强员工的安全意识培训，提高整体安全防护能力。

**RayWAF在IPv6应用安全防护中的作用**

**全面兼容IPv6：**无缝接入IPv6网络环境，为IPv6网络下的Web应用提供同等级别的安全防护。目前，盛邦安全全线产品均可无缝对接IPv6网络环境，为客户提供安全可靠的解决方案。

**精细访问控制：**基于IPv6地址的精细化访问控制策略，有效限制恶意访问和数据泄露风险。

**智能威胁识别：**利用大数据分析、机器学习和人工智能技术，智能识别和防御新型Web攻击和未知威胁。

**高效性能保障：**优化的数据处理流程，确保在处理IPv6流量时保持高性能，不影响用户体验。

**全面日志审计：**详尽记录IPv6环境下的访问和攻击日志，有助于事后分析和溯源。

2024年4月，中央网信办、国家发展改革委、工业和信息化部联合印发《深入推进IPv6规模部署和应用2024年工作安排》，旨在全面推进IPv6技术创新与融合应用，为建设网络强国、数字中国提供有力支撑。此次两部门联合开展“网络去NAT”专项工作，再次加速了我国IPv6演进升级的步伐。在此过程中，我们应高度重视IPv6应用安全防护工作，在提升IPv6连通率与流量占比的同时，保障网络安全稳定运行，才能更好地释放IPv6的价值，使其发挥更大的赋能效应，共建一个安全、可信、高效、全面互联的数字世界。

[原文链接](https://www.webray.com.cn/skippath/blog/blog_2241.html)

如若转载，请注明原文地址

* 分享至

![取消](https://www.4hou.com/sihou/images/close.jpg)
![嘶吼](https://www.4hou.com/sihou/images/logo.png)

### 发表评论

评论

![](https://www.4hou.com/captcha/flat?Zrh3PKWo)

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

![](https://img.4hou.com/portraits/3c8d3af7c49c95c16dd14518142759d6.png)

# [盛邦安全](https://www.4hou.com/member/9ZO4)

让网络空间更有序

#### 最新文章

* [Exchange/M365最新防范攻略！CACTER三步补齐原生防护短板](https://www.4hou.com/posts/l03l)
  2025-09-29 17:48:04
* [【附下载】2025我们身边的 网信安全 典型案例等 官方视频汇编](https://www.4hou.com/posts/kg3x)
  2025-09-29 14:55:37
* [蝉联荣誉！梆梆安全再度获选 “北京市委网信办第二届网络安全技术支撑单位”](https://www.4hou.com/posts/9jKP)
  2025-09-29 14:23:50
* [聚焦可信AI安全！SDC2025 议题重磅揭晓](https://www.4hou.com/posts/gy39)
  2025-09-28 17:20:40

[查看更多](https://www.4hou.com/member/9ZO4)

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