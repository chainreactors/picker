---
title: 新型Mirai衍生僵尸网络ShadowV2现身 瞄准多品牌IoT设备漏洞发起攻击
url: https://www.4hou.com/posts/wxGm
source: 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com
date: 2025-12-09
fetch_date: 2025-12-10T03:20:53.772676
---

# 新型Mirai衍生僵尸网络ShadowV2现身 瞄准多品牌IoT设备漏洞发起攻击

新型Mirai衍生僵尸网络ShadowV2现身 瞄准多品牌IoT设备漏洞发起攻击 - 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com

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

# 新型Mirai衍生僵尸网络ShadowV2现身 瞄准多品牌IoT设备漏洞发起攻击

胡金鱼
[漏洞](https://www.4hou.com/category/vulnerable)
23小时 前发布

![](https://img.4hou.com/article/%E6%B5%8F%E8%A7%88.png)6828

收藏

导语：尽管两起事件并无关联，但该僵尸网络仅在宕机期间活跃，这一特征或表明此次活动为一次测试性攻击。

一款名为“ShadowV2”的新型Mirai衍生僵尸网络恶意软件已被发现，其利用已知漏洞针对D-Link、TP-Link等厂商的物联网设备发起攻击。

FortiGuard Labs研究人员在10月亚马逊云服务大规模宕机期间监测到该攻击活动。尽管两起事件并无关联，但该僵尸网络仅在宕机期间活跃，这一特征或表明此次活动为一次测试性攻击。

**攻击载体：8个跨厂商IoT设备漏洞**

ShadowV2通过利用多款IoT产品的至少8个已知漏洞进行传播，涉及设备及对应漏洞如下：

- DD-WRT路由器：CVE-2009-2765

- D-Link设备：CVE-2020-25506、CVE-2022-37055、CVE-2024-10914、CVE-2024-10915

- DigiEver设备：CVE-2023-52163

- TBK设备：CVE-2024-3721

- TP-Link设备：CVE-2024-53375

其中，CVE-2024-10914是已被公开利用的命令注入漏洞，影响D-Link多款已停产（EoL）设备，厂商已明确表示不会为该漏洞提供修复补丁。

经与厂商核实后确认，受影响设备型号同样不会获得该漏洞的修复支持。D-Link方面已更新旧版公告并添加该漏洞的CVE编号，同时发布新公告提及ShadowV2攻击活动表示已停产或终止支持的设备将不再进行开发维护，也不会收到固件更新。

另一漏洞CVE-2024-53375于2024年11月被详细披露，据悉厂商已通过测试版（beta）固件更新修复该漏洞。

**攻击范围与技术特征**

![图片7.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20251202/1764666357101252.png "1764666121194464.png")

ShadowV2 使用的各种漏洞利用

FortiGuard Labs研究人员表示，ShadowV2的攻击流量源自IP地址198[.]199[.]72[.]27，目标涵盖路由器、网络附加存储（NAS）设备及数字视频录像机（DVR），涉及政府、科技、制造、托管安全服务提供商（MSSP）、电信、教育等七大行业，攻击范围遍布全球，包括美洲、欧洲、非洲、亚洲及大洋洲。

技术层面，该恶意软件自称为“ShadowV2 Build v1.0.0 IoT version”，与Mirai僵尸网络的LZRD变种存在相似性。其传播流程为：通过下载器脚本（binary.sh）从81[.]88[.]18[.]108服务器获取恶意程序，完成初始植入。

![图片8.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20251202/1764666360664133.png "1764666154205785.png")

下载脚本

在配置加密方面，ShadowV2采用XOR编码对文件系统路径、用户代理（User-Agent）字符串、HTTP头及Mirai风格特征字符串进行加密处理。

功能上，该僵尸网络支持对UDP、TCP及HTTP协议发起分布式拒绝服务攻击，且每种协议均包含多种洪水攻击类型，控制服务器通过向受控设备（僵尸机）发送指令触发攻击。

![图片9.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20251202/1764666363127706.png "1764666201185502.png")

DDoS攻击触发

通常情况下，DDoS僵尸网络的盈利模式包括向网络犯罪分子出租攻击算力，或直接勒索攻击目标（要求支付赎金以停止攻击）。但截至目前，ShadowV2的幕后操控者身份及其盈利策略尚未明确。

文章来源自：https://www.bleepingcomputer.com/news/security/new-shadowv2-botnet-malware-used-aws-outage-as-a-test-opportunity/如若转载，请注明原文地址

* 分享至

![取消](https://www.4hou.com/sihou/images/close.jpg)
![嘶吼](https://www.4hou.com/sihou/images/logo.png)

感谢您的支持，我会继续努力的!

![扫码支持]( "扫一扫")

打开微信扫一扫后点击右上角即可分享哟

### 发表评论

评论

![](https://www.4hou.com/captcha/flat?8vtQW8i4)

#### 你可能感兴趣的

* [![]()

  新型Mirai衍生僵尸网络ShadowV2现身 瞄准多品牌IoT设备漏洞发起攻击](https://www.4hou.com/posts/wxGm)
* [![]()

  漏洞预警 | React/Next.js组件存在RCE漏洞（CVE-2025-58360）](https://www.4hou.com/posts/mkrE)
* [![]()

  微软：Windows 11 24H2 高危漏洞导致文件资源管理器等核心组件崩溃](https://www.4hou.com/posts/QX9q)
* [![]()

  Grafana ：最高级别漏洞可实现管理员身份冒充](https://www.4hou.com/posts/W13X)
* [![]()

  ImunifyAV曝远程代码执行漏洞 数百万Linux托管网站面临风险](https://www.4hou.com/posts/rpAk)
* [![]()

  高危runC漏洞曝光 黑客可突破Docker容器逃逸](https://www.4hou.com/posts/XP4l)

![](https://img.4hou.com/images/微信图片_20231102150249.jpg)

# [胡金鱼](https://www.4hou.com/member/BVMN)

这个家伙很懒,什么也没说!

#### 最新文章

* [新型Mirai衍生僵尸网络ShadowV2现身 瞄准多品牌IoT设备漏洞发起攻击](https://www.4hou.com/posts/wxGm)
  2025-12-09 12:00:00
* [漏洞预警 | React/Next.js组件存在RCE漏洞（CVE-2025-58360）](https://www.4hou.com/posts/mkrE)
  2025-12-04 16:57:08
* [微软：Windows 11 24H2 高危漏洞导致文件资源管理器等核心组件崩溃](https://www.4hou.com/posts/QX9q)
  2025-11-26 12:01:00
* [Grafana ：最高级别漏洞可实现管理员身份冒充](https://www.4hou.com/posts/W13X)
  2025-11-26 12:00:00

[查看更多](https://www.4hou.com/member/BVMN)

# 相关热文

* [新型Mirai衍生僵尸网络ShadowV2现身 瞄准多品牌IoT设备漏洞发起攻击](https://www.4hou.com/posts/wxGm)

  胡金鱼
* [漏洞预警 | React/Next.js组件存在RCE漏洞（CVE-2025-58360）](https://www.4hou.com/posts/mkrE)

  盛邦安全
* [微软：Windows 11 24H2 高危漏洞导致文件资源管理器等核心组件崩溃](https://www.4hou.com/posts/QX9q)

  胡金鱼
* [Grafana ：最高级别漏洞可实现管理员身份冒充](https://www.4hou.com/posts/W13X)

  胡金鱼
* [ImunifyAV曝远程代码执行漏洞 数百万Linux托管网站面临风险](https://www.4hou.com/posts/rpAk)

  胡金鱼
* [高危runC漏洞曝光 黑客可突破Docker容器逃逸](https://www.4hou.com/posts/XP4l)

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