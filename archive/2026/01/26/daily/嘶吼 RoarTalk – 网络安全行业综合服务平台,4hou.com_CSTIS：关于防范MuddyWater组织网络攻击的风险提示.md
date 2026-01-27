---
title: CSTIS：关于防范MuddyWater组织网络攻击的风险提示
url: https://www.4hou.com/posts/8gpW
source: 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com
date: 2026-01-26
fetch_date: 2026-01-27T03:37:18.513777
---

# CSTIS：关于防范MuddyWater组织网络攻击的风险提示

CSTIS：关于防范MuddyWater组织网络攻击的风险提示 - 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com

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

# CSTIS：关于防范MuddyWater组织网络攻击的风险提示

胡金鱼
[漏洞](https://www.4hou.com/category/vulnerable)
23小时 前发布

![](https://img.4hou.com/article/%E6%B5%8F%E8%A7%88.png)11567

收藏

导语：MuddyWater组织近期针对政府、军事、电信、能源等机构实施网络攻击，窃取系统凭证、机密文件等敏感数据。

近日，工业和信息化部网络安全威胁和漏洞信息共享平台（CSTIS）监测发现，MuddyWater组织近期针对政府、军事、电信、能源等机构实施网络攻击，窃取系统凭证、机密文件等敏感数据。

攻击者通过鱼叉邮件投递双重伪装载荷，一类是伪装成PDF文档的可执行文件（如“xxx.pdf.exe”），另一类则在DOC文档中嵌入恶意宏代码。一旦受害者误启PDF文档，伪装文档将立即释放UDPGangster后门（MuddyWater组织的UDP后门，支持远程控制、窃密等）到本地。对于嵌入恶意宏代码的DOC文档，一旦打开，宏代码将会被静默执行并从自身解密释放后续载荷，将其保存为txt文件后重命名为装载UDPGangster的novaservice.exe可执行文件。攻击载荷成功在内存部署后门后，UDPGangster会将自身复制为SystemProc.exe，并通过写入注册表HKCU\...\UserShellFolders\Startup实现自动启动。同时，MuddyWater组织采用动态C2连接策略，优先读取本地配置文件，失败则回退至硬编码C2地址。后门程序会收集主机名、工作组、系统版本及用户名等数据，加密回传至服务端，最终建立对目标主机的远程控制。

建议相关单位及用户立即禁用Office宏执行策略，阻断恶意文档释放攻击载荷；部署邮件网关动态沙箱，深度检测伪装PDF的可执行文件及带宏文档；实时监控注册表路径HKCU\Software\...\UserShellFolders\Startup异常写入，清除SystemProc.exe后门持久化项。

**相关IOC信息**

**MD5：**

07502104c6884e6151f6e0a53966e199

409d02d6153af220e527fd72256ee3a5

561b2983d558283c446ff674ff6138c3

7bfbc76c7eeb652d73b85c99ee83b339

9e06b36f4da737b8d699a6846c2540e9

a39f74247367e0891f18b7662c8e69b5

a546d2363a4b94e361d0874b690c853b

a9235540208fa6a25614c24a59e19199

aa75a0baebc93d4ca7498453ef64128a

bed77abc7e12230439c0b53dd68ffaf7

d84812961fc7cd8340031efd7b5508a8

dd6af28d1a03193fc76001b04d5827cc

de14abbda6a649d9ec90a816847f95db

e09a720574a6594b1444ebc1d6cca969

e5dd608292b6f421b0c108816d25fc5e

**SHA256：**

7ea4b307e84c8b32c0220eca13155a4cf66617241f96b8af26ce2db8115e3d53

aea51eaafacd03ade98875b107481d46a8f79ea9d903172b2ed8458c785a8273

d766a8ff123449a8c87fb3570c885439ccfd7d6151847d6d1f44ee7a59c4845c

ff62c294a2bcfee0d291b15ff1fd1733d08ab901281acf9c089f4662b4002a69

**SHA1：**

0543e6c36ca89e5d3e13656af0d1b4af0b7585c9

7bb0d162bbaa462c516502d1db56818d24ad825f

903e97ee731796fde34153c71eb718a1015ba358

d00280f07f2159adb16d8f76b7838e3e86773a7e

**关联域名：**

157[.]20[.]182[.]75[:]1269

64[.]7[.]198[.]12[:]1259

**关联IP地址：**

157[.]20[.]182[.]75

64[.]7[.]198[.]12

文章来源自：网络安全威胁和漏洞信息共享平台

如若转载，请注明原文地址

* 分享至

![取消](https://www.4hou.com/sihou/images/close.jpg)
![嘶吼](https://www.4hou.com/sihou/images/logo.png)

### 发表评论

评论

![](https://www.4hou.com/captcha/flat?OhKlQ0MO)

#### 你可能感兴趣的

* [![]()

  CSTIS：关于防范MuddyWater组织网络攻击的风险提示](https://www.4hou.com/posts/8gpW)
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

![](https://img.4hou.com/images/微信图片_20231102150249.jpg)

# [胡金鱼](https://www.4hou.com/member/BVMN)

这个家伙很懒,什么也没说!

#### 最新文章

* [CSTIS：关于防范MuddyWater组织网络攻击的风险提示](https://www.4hou.com/posts/8gpW)
  2026-01-26 11:42:29
* [严重漏洞WhisperPair曝光：黑客可通过蓝牙音频设备实施追踪与窃听](https://www.4hou.com/posts/J14v)
  2026-01-22 12:00:00
* [GoBruteforcer 僵尸网络新攻势：利用AI生成配置漏洞 瞄准加密货币数据库](https://www.4hou.com/posts/nl2Y)
  2026-01-19 12:00:00
* [CVE-2026-20824漏洞：Windows远程协助存在安全功能绕过风险](https://www.4hou.com/posts/EyY4)
  2026-01-16 11:17:10

[查看更多](https://www.4hou.com/member/BVMN)

# 相关热文

* [CSTIS：关于防范MuddyWater组织网络攻击的风险提示](https://www.4hou.com/posts/8gpW)

  胡金鱼
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