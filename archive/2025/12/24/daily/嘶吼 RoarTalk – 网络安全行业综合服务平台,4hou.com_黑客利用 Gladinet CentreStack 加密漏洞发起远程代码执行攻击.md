---
title: 黑客利用 Gladinet CentreStack 加密漏洞发起远程代码执行攻击
url: https://www.4hou.com/posts/XPN8
source: 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com
date: 2025-12-24
fetch_date: 2025-12-25T03:25:46.695726
---

# 黑客利用 Gladinet CentreStack 加密漏洞发起远程代码执行攻击

黑客利用 Gladinet CentreStack 加密漏洞发起远程代码执行攻击 - 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com

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

# 黑客利用 Gladinet CentreStack 加密漏洞发起远程代码执行攻击

胡金鱼
[漏洞](https://www.4hou.com/category/vulnerable)
23小时 前发布

![](https://img.4hou.com/article/%E6%B5%8F%E8%A7%88.png)5438

收藏

导语：安全研究人员发出警告，攻击者可借助该漏洞获取硬编码加密密钥，进而实现远程代码执行。

黑客正针对两款远程文件安全访问共享产品——CentreStack与Triofox发起攻击，其所用的突破口，是这两款产品加密算法实现过程中一个此前未被公开披露的全新漏洞。

安全研究人员发出警告，攻击者可借助该漏洞获取硬编码加密密钥，进而实现远程代码执行。尽管该新型加密漏洞目前尚未获得官方漏洞编号，但Gladinet方面已向客户推送相关通知，建议用户将产品更新至11月29日发布的最新版本。该公司同时向客户提供了一套入侵指标，表明该漏洞已被用于野外攻击。

托管式网络安全平台Huntress的安全研究人员证实，目前至少有9家机构遭到攻击。攻击者在攻击中同时利用了上述新漏洞，以及一个编号为CVE-2025-30406的旧漏洞——这是一个本地文件包含漏洞，本地攻击者可利用该漏洞在无需身份验证的情况下访问系统文件。

**硬编码加密密钥漏洞原理**

借助Gladinet提供的入侵指标，Huntress的研究人员成功定位该漏洞的触发位置，并厘清了威胁者的利用方式。

研究发现，该漏洞根源在于Gladinet CentreStack与Triofox两款产品对AES加密算法的自定义实现环节——加密密钥与初始化向量（IV）被硬编码在GladCtrl64.dll文件中，攻击者可轻易提取。

具体而言，密钥值由两段固定的100字节中日文文本字符串生成，且所有产品安装实例中的该字符串完全一致。

漏洞的核心触发点在于对filesvr.dn处理器的处理逻辑：该处理器会使用上述静态密钥对t参数（即访问令牌）进行解密操作。

任何获取这些密钥的攻击者，都可解密包含文件路径、用户名、密码及时间戳等信息的访问令牌，甚至能伪造令牌冒充合法用户，向服务器发送指令以读取磁盘中的任意文件。

研究人员指出：“由于这些密钥永久固定不变，我们只需从内存中提取一次，就能用其解密服务器生成的所有令牌；更危险的是，攻击者还能利用密钥自行加密生成恶意令牌。”

Huntress观测到，攻击者会利用硬编码AES密钥伪造访问令牌，并将令牌的时间戳设置为9999年，以此实现令牌永久有效。

随后，攻击者会向服务器发起请求，获取web.config配置文件。该文件中包含machineKey密钥，攻击者可借助此密钥，通过视图状态反序列化漏洞触发远程代码执行。

![图片6.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20251215/1765789535850254.png "1765789535850254.png")

开发活动

目前，除已确认的攻击源IP地址147.124.216[.]205外，相关攻击的具体归属组织尚未明确。

在攻击目标方面，Huntress证实，截至12月10日，已有来自医疗、科技等多个行业的9家机构遭到攻击。研究人员建议，Gladinet CentreStack与Triofox的用户应尽快将产品升级至12月8日发布的16.12.10420.56791版本，同时更换系统的machineKey密钥。

此外，用户还应扫描系统日志，排查是否存在字符串vghpI7EToZUDIZDdprSubL3mTZ2——该字符串与加密后的文件路径相关联，是判定系统是否遭入侵的唯一可靠指标。

目前，Huntress已在其发布的报告中提供漏洞缓解指导方案，同时附上相关入侵指标，供安全防护人员用于加固防护体系，或排查自身系统是否已遭到入侵。

文章来源自：https://www.bleepingcomputer.com/news/security/hackers-exploit-gladinet-centrestack-cryptographic-flaw-in-rce-attacks/如若转载，请注明原文地址

* 分享至

![取消](https://www.4hou.com/sihou/images/close.jpg)
![嘶吼](https://www.4hou.com/sihou/images/logo.png)

感谢您的支持，我会继续努力的!

![扫码支持]( "扫一扫")

打开微信扫一扫后点击右上角即可分享哟

### 发表评论

评论

![](https://www.4hou.com/captcha/flat?afKsKk9c)

#### 你可能感兴趣的

* [![]()

  黑客利用 Gladinet CentreStack 加密漏洞发起远程代码执行攻击](https://www.4hou.com/posts/XPN8)
* [![]()

  新型UEFI漏洞曝光：技嘉、微星、华硕、华擎主板面临启动前攻击风险](https://www.4hou.com/posts/0MWV)
* [![]()

  黑客借 React2Shell 漏洞发起 EtherRAT 恶意软件攻击](https://www.4hou.com/posts/J1v9)
* [![]()

  漏洞预警 | React/Next.js组件RCE漏洞（CVE-2025-55182）详情分析-【附验证环境】](https://www.4hou.com/posts/NGzm)
* [![]()

  新型Mirai衍生僵尸网络ShadowV2现身 瞄准多品牌IoT设备漏洞发起攻击](https://www.4hou.com/posts/wxGm)
* [![]()

  漏洞预警 | React/Next.js组件存在RCE漏洞（CVE-2025-58360）](https://www.4hou.com/posts/mkrE)

![](https://img.4hou.com/images/微信图片_20231102150249.jpg)

# [胡金鱼](https://www.4hou.com/member/BVMN)

这个家伙很懒,什么也没说!

#### 最新文章

* [黑客利用 Gladinet CentreStack 加密漏洞发起远程代码执行攻击](https://www.4hou.com/posts/XPN8)
  2025-12-24 12:00:00
* [新型UEFI漏洞曝光：技嘉、微星、华硕、华擎主板面临启动前攻击风险](https://www.4hou.com/posts/0MWV)
  2025-12-23 10:36:23
* [黑客借 React2Shell 漏洞发起 EtherRAT 恶意软件攻击](https://www.4hou.com/posts/J1v9)
  2025-12-18 12:00:00
* [漏洞预警 | React/Next.js组件RCE漏洞（CVE-2025-55182）详情分析-【附验证环境】](https://www.4hou.com/posts/NGzm)
  2025-12-11 15:50:27

[查看更多](https://www.4hou.com/member/BVMN)

# 相关热文

* [黑客利用 Gladinet CentreStack 加密漏洞发起远程代码执行攻击](https://www.4hou.com/posts/XPN8)

  胡金鱼
* [新型UEFI漏洞曝光：技嘉、微星、华硕、华擎主板面临启动前攻击风险](https://www.4hou.com/posts/0MWV)

  胡金鱼
* [黑客借 React2Shell 漏洞发起 EtherRAT 恶意软件攻击](https://www.4hou.com/posts/J1v9)

  胡金鱼
* [漏洞预警 | React/Next.js组件RCE漏洞（CVE-2025-55182）详情分析-【附验证环境】](https://www.4hou.com/posts/NGzm)

  盛邦安全
* [新型Mirai衍生僵尸网络ShadowV2现身 瞄准多品牌IoT设备漏洞发起攻击](https://www.4hou.com/posts/wxGm)

  胡金鱼
* [漏洞预警 | React/Next.js组件存在RCE漏洞（CVE-2025-58360）](https://www.4hou.com/posts/mkrE)

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