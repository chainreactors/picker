---
title: 严重漏洞WhisperPair曝光：黑客可通过蓝牙音频设备实施追踪与窃听
url: https://www.4hou.com/posts/J14v
source: 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com
date: 2026-01-22
fetch_date: 2026-01-23T03:31:27.746276
---

# 严重漏洞WhisperPair曝光：黑客可通过蓝牙音频设备实施追踪与窃听

严重漏洞WhisperPair曝光：黑客可通过蓝牙音频设备实施追踪与窃听 - 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com

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

# 严重漏洞WhisperPair曝光：黑客可通过蓝牙音频设备实施追踪与窃听

胡金鱼
[漏洞](https://www.4hou.com/category/vulnerable)
23小时 前发布

![](https://img.4hou.com/article/%E6%B5%8F%E8%A7%88.png)7818

收藏

导语：攻击者可利用该漏洞劫持蓝牙音频配件、追踪用户位置并窃听对话。

安全研究人员在 Google 的Fast Pair（快速配对）协议中发现了一个严重漏洞，攻击者可利用该漏洞劫持蓝牙音频配件、追踪用户位置并窃听对话。

该漏洞编号为 CVE-2025-36911，被命名为WhisperPair，影响数亿支持 Google Fast Pair 功能的无线耳机、耳塞和音箱。由于漏洞存在于配件本身，无论用户使用何种智能手机操作系统均会受到影响，这意味着使用易受攻击蓝牙设备的 iPhone 用户也面临同等风险。

发现该漏洞的研究人员解释称，该漏洞源于许多旗舰音频配件对 Fast Pair 协议的不当实现。

尽管 Fast Pair 规范规定蓝牙设备在非配对模式下应忽略配对请求，但许多厂商并未在产品中强制实施此检查，从而允许未授权设备在用户不知情或未同意的情况下发起配对。

为启动 Fast Pair 流程，搜索者（手机）会向提供者（配件）发送一条表示想要配对的消息。Fast Pair 规范指出，如果配件未处于配对模式，则应忽略此类消息。 然而，许多设备在实际操作中并未强制实施此检查，允许未授权设备启动配对流程。在收到易受攻击设备的回复后，攻击者可以通过建立常规蓝牙配对来完成 Fast Pair 过程。

攻击者可利用任何具备蓝牙功能的设备，在14米范围内，于数秒内强制与受影响的音频配件配对，且无需用户交互或物理接触。

受影响的品牌包括 Google、Jabra、JBL、Logitech、Marshall、Nothing、OnePlus、Sony、Soundcore 等。

配对成功后，攻击者将获得对音频设备的完全控制权，能够以高音量播放音频，或通过设备的麦克风窃听用户对话。

如果该配件从未与 Android 设备配对过，攻击者还可通过将其添加到自己的 Google 账户中，利用 Google 的 查找设备网络来追踪受害者的位置。

“受害者可能会在数小时或数天后看到一条不想要的追踪通知，但该通知显示的是他们自己的设备，”研究人员说道。“这可能导致用户将该警告误认为是系统 Bug 而忽略，从而使攻击者能够在较长一段时间内持续追踪受害者。”

随后，Google 向研究人员颁发了最高额度15,000 美元的赏金，并在 150 天的披露期内与厂商合作发布了安全补丁。不过，他们指出，针对所有受影响设备的安全更新可能尚未全部推送。

特别提醒，防御此类攻击的唯一方法是安装设备厂商提供的固件更新。在 Android 手机上禁用 Fast Pair 无法防止攻击，因为该功能无法在配件端被关闭。

文章来源自：https://www.bleepingcomputer.com/news/security/critical-whisperpair-flaw-lets-hackers-track-eavesdrop-via-bluetooth-audio-devices/如若转载，请注明原文地址

* 分享至

![取消](https://www.4hou.com/sihou/images/close.jpg)
![嘶吼](https://www.4hou.com/sihou/images/logo.png)

### 发表评论

评论

![](https://www.4hou.com/captcha/flat?8Dua9axF)

#### 你可能感兴趣的

* [![]()

  严重漏洞WhisperPair曝光：黑客可通过蓝牙音频设备实施追踪与窃听](https://www.4hou.com/posts/J14v)
* [![]()

  GoBruteforcer 僵尸网络新攻势：利用AI生成配置漏洞 瞄准加密货币数据库](https://www.4hou.com/posts/nl2Y)
* [![]()

  CVE-2026-20824漏洞：Windows远程协助存在安全功能绕过风险](https://www.4hou.com/posts/EyY4)
* [![]()

  HPE Aruba漏洞致敏感信息遭未授权访问](https://www.4hou.com/posts/DxX5)
* [![]()

  Ni8mare高危漏洞来袭 黑客可远程劫持n8n服务器](https://www.4hou.com/posts/om3A)
* [![]()

  WebRAT恶意软件借GitHub伪造漏洞利用程序传播](https://www.4hou.com/posts/Bvw2)

![](https://img.4hou.com/images/微信图片_20231102150249.jpg)

# [胡金鱼](https://www.4hou.com/member/BVMN)

这个家伙很懒,什么也没说!

#### 最新文章

* [严重漏洞WhisperPair曝光：黑客可通过蓝牙音频设备实施追踪与窃听](https://www.4hou.com/posts/J14v)
  2026-01-22 12:00:00
* [GoBruteforcer 僵尸网络新攻势：利用AI生成配置漏洞 瞄准加密货币数据库](https://www.4hou.com/posts/nl2Y)
  2026-01-19 12:00:00
* [CVE-2026-20824漏洞：Windows远程协助存在安全功能绕过风险](https://www.4hou.com/posts/EyY4)
  2026-01-16 11:17:10
* [HPE Aruba漏洞致敏感信息遭未授权访问](https://www.4hou.com/posts/DxX5)
  2026-01-16 10:52:54

[查看更多](https://www.4hou.com/member/BVMN)

# 相关热文

* [严重漏洞WhisperPair曝光：黑客可通过蓝牙音频设备实施追踪与窃听](https://www.4hou.com/posts/J14v)

  胡金鱼
* [GoBruteforcer 僵尸网络新攻势：利用AI生成配置漏洞 瞄准加密货币数据库](https://www.4hou.com/posts/nl2Y)

  胡金鱼
* [CVE-2026-20824漏洞：Windows远程协助存在安全功能绕过风险](https://www.4hou.com/posts/EyY4)

  山卡拉
* [HPE Aruba漏洞致敏感信息遭未授权访问](https://www.4hou.com/posts/DxX5)

  山卡拉
* [Ni8mare高危漏洞来袭 黑客可远程劫持n8n服务器](https://www.4hou.com/posts/om3A)

  胡金鱼
* [WebRAT恶意软件借GitHub伪造漏洞利用程序传播](https://www.4hou.com/posts/Bvw2)

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