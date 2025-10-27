---
title: 新型物联网僵尸网络现身，疯狂劫持设备发动大规模 DDoS 攻击
url: https://www.4hou.com/posts/0MoN
source: 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com
date: 2025-01-22
fetch_date: 2025-10-06T20:04:49.499136
---

# 新型物联网僵尸网络现身，疯狂劫持设备发动大规模 DDoS 攻击

新型物联网僵尸网络现身，疯狂劫持设备发动大规模 DDoS 攻击 - 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com

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

# 新型物联网僵尸网络现身，疯狂劫持设备发动大规模 DDoS 攻击

山卡拉
[行业](https://www.4hou.com/category/industry)
2025-01-21 10:33:42

![](https://img.4hou.com/article/%E6%B5%8F%E8%A7%88.png)75450

收藏

导语：自 2024 年底起，IoT 僵尸网络的 C＆C 服务器便开始向日本及其他国家和地区发送大规模 DDoS 攻击命令。

自 2024 年底起，IoT 僵尸网络的 C＆C 服务器便开始向日本及其他国家和地区发送大规模 DDoS 攻击命令。这些命令的目标涵盖了多家公司，其中不乏日本的大型企业与银行。

尽管目前无法确认直接联系，但一些目标组织反馈，在此期间出现了临时连接异常和网络中断的情况，而这些状况与观察到的攻击命令高度吻合。

**物联网僵尸网络的新威胁聚焦日本**

这个基于 Mirai/Bashlite 的僵尸网络利用 RCE 漏洞或弱密码来感染物联网设备。感染阶段包括下载一个脚本，该脚本会从分发服务器获取加载程序可执行文件。

之后，加载程序使用专门的 User-Agent 标头从服务器成功检索实际的恶意软件负载，然后在内存中执行它。

该恶意软件与 C＆C 服务器通信，以获取发起 DDoS 攻击（SYN Flood、TCP ACK Flood、UDP Flood 等）或将设备转变为代理服务器的命令。

![image.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20250121/1737426715933842.png "1737425854164666.png")

使用自定义 User-Agent 标头从分发服务器下载二进制文件的代码

它采用了多种规避技术，并通过镜像过去的 Mirai 僵尸网络行为来 停用阻止[DDoS 攻击](https://gbhackers.com/ddos-attack-size-increased/)期间由高负载触发的系统重启的看门狗计时器。

它还操纵 iptables 规则来阻碍感染检测和 DDoS 攻击可见性。通过阻止 WAN 端 TCP 连接，它旨在防止交叉感染，同时保持内部管理访问。

通过使用动态配置的 iptables 规则，恶意软件能够接收来自外界的 UDP 数据包，并通过隐藏其活动来抑制 TCP RST 数据包。

![image.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20250121/1737426716274462.png "1737425890106630.png")

用于禁用看门狗定时器的恶意软件代码

2024 年 12 月 27 日至 2025 年 1 月 4 日期间观察到的 DDoS 攻击针对的是北美、欧洲和亚洲的组织，主要集中在美国、巴林和波兰。

趋势科技的分析显示，不同目标地区的命令模式有所不同。针对日本目标的攻击经常使用“stomp”命令，而针对国际目标的攻击则更常使用“gre”命令。

攻击主要集中在交通运输、信息通信、金融保险等领域。而国际攻击也主要集中在信息通信、金融保险行业，针对交通运输领域的攻击明显较少。

![image.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20250121/1737426718657211.png "1737425933171192.png")

目标行业

这些攻击背后的实施者表现出了适应性，并在实施初步防御措施后针对日本组织测试了“套接字”和“握手”等新命令。

![image.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20250121/1737426718147523.png "1737425958159445.png")

恶意软件在初始化阶段设置的 iptables 规则

僵尸网络分析结果显示，共有 348 台设备遭到感染。受感染设备中，80% 主要是 TP-Link 和 Zyxel 等供应商生产的无线路由器，此外，来自海康威视的 IP 摄像机在受感染设备中也占了相当比例。

导致其被利用的因素包括默认设置的持久性、过时的固件和安全功能不充分，这些因素使攻击者能够轻易破坏这些设备并利用它们进行 DDoS 攻击和网络入侵等恶意活动。

**针对 DDoS 攻击和物联网漏洞的缓解策略**

为了减轻僵尸网络感染和 DDoS 攻击，请实施强大的安全措施。通过更改默认凭据、定期更新固件和分段物联网网络来保护物联网设备。

同时，要严格限制设备的远程访问权限，对设备进行行之有效的管理，密切监控网络流量，一旦发现异常即刻响应处理。

针对 UDP 洪水攻击，可通过阻止特定的 IP 地址和协议来进行防范；还可以积极与服务提供商展开深度合作，共同应对风险；另外，加强路由器硬件的防护能力，也是减轻 UDP 洪水攻击影响的重要举措 。

本文翻译自：https://gbhackers.com/new-iot-botnet-launches-large-scale-ddos-attacks/如若转载，请注明原文地址

* 分享至

![取消](https://www.4hou.com/sihou/images/close.jpg)
![嘶吼](https://www.4hou.com/sihou/images/logo.png)

感谢您的支持，我会继续努力的!

![扫码支持]( "扫一扫")

打开微信扫一扫后点击右上角即可分享哟

### 发表评论

评论

![](https://www.4hou.com/captcha/flat?o82nKyKM)

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

![](https://img.4hou.com/FjC8MmzrcnfY_rzJyoXU2_G-O0i9)

# [山卡拉](https://www.4hou.com/member/azxO)

这个家伙很懒,什么也没说!

#### 最新文章

* [Exchange/M365最新防范攻略！CACTER三步补齐原生防护短板](https://www.4hou.com/posts/l03l)
  2025-09-29 17:48:04
* [【附下载】2025我们身边的 网信安全 典型案例等 官方视频汇编](https://www.4hou.com/posts/kg3x)
  2025-09-29 14:55:37
* [蝉联荣誉！梆梆安全再度获选 “北京市委网信办第二届网络安全技术支撑单位”](https://www.4hou.com/posts/9jKP)
  2025-09-29 14:23:50
* [聚焦可信AI安全！SDC2025 议题重磅揭晓](https://www.4hou.com/posts/gy39)
  2025-09-28 17:20:40

[查看更多](https://www.4hou.com/member/azxO)

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