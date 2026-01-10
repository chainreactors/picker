---
title: GlassWorm恶意软件新变种来袭 植入后门加密钱包瞄准Mac设备
url: https://www.4hou.com/posts/pn4X
source: 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com
date: 2026-01-09
fetch_date: 2026-01-10T03:31:17.568002
---

# GlassWorm恶意软件新变种来袭 植入后门加密钱包瞄准Mac设备

GlassWorm恶意软件新变种来袭 植入后门加密钱包瞄准Mac设备 - 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com

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

# GlassWorm恶意软件新变种来袭 植入后门加密钱包瞄准Mac设备

胡金鱼
[新闻](https://www.4hou.com/category/news)
23小时 前发布

![](https://img.4hou.com/article/%E6%B5%8F%E8%A7%88.png)8882

收藏

导语：安全人员建议，已安装上述三款插件的开发者应立即卸载插件，重置GitHub账户密码，撤销NPM令牌，全面检查系统是否存在感染痕迹，必要时可重装系统。

GlassWorm恶意软件攻击活动近期发起第四波攻势，通过恶意VSCode/OpenVSX插件针对macOS开发者实施攻击，投放植入后门的加密货币钱包程序。

OpenVSX插件仓库与微软Visual Studio应用市场中的插件，均以开发工具、语言支持或主题皮肤的形式，为兼容VS Code的编辑器扩展功能、提升使用效率。

其中，微软应用市场是Visual Studio Code的官方插件商店；而OpenVSX作为一款开源、无厂商绑定的替代平台，主要被不支持或选择不依赖微软专有应用市场的编辑器所采用。

GlassWorm恶意软件最早于2025年10月侵入上述两大应用市场，藏身于恶意插件中，通过不可见的Unicode字符规避检测。

该恶意软件一旦安装，会窃取GitHub、npm及OpenVSX账户凭证，同时从多款插件中提取加密货币钱包数据。此外，它还支持通过虚拟网络计算（VNC）实现远程访问，并可借助SOCKS代理将流量路由至受害者设备。

尽管该攻击已被公开披露，各类防御措施也随之加强，但GlassWorm仍于2025年11月初卷土重来，侵入OpenVSX平台，随后又在12月初现身VS Code应用市场。

**GlassWorm再度入侵OpenVSX平台**

研究人员发现，新一轮GlassWorm攻击活动专门针对macOS系统，与此前仅针对Windows系统的攻击模式截然不同。

不同于前两波攻击使用的不可见Unicode字符，也不同于第三波攻击采用的编译型Rust二进制文件，最新攻击将经AES-256-CBC加密的载荷嵌入OpenVSX恶意插件的编译型JavaScript代码中，涉事恶意插件包括：

**·**studio-velte-distributor.pro-svelte-extension

**·**cudra-production.vsce-prettier-pro

**·**Puccin-development.full-access-catppuccin-pro-extension

恶意代码会在延迟15分钟后再执行，此举大概率是为了规避沙箱环境的动态分析。

在技术实现上，该恶意软件不再依赖PowerShell，转而使用AppleScript脚本；持久化机制也不再修改注册表，而是通过LaunchAgents实现。

不过，基于Solana区块链的命令与控制（C2）机制未发生变化，研究人员还指出，攻击所使用的基础设施也存在重叠。

除了继续针对50余款浏览器加密货币插件、开发者凭证（GitHub、NPM）及浏览器数据实施窃取外，新版GlassWorm还新增了窃取钥匙串（Keychain）密码的功能。

此外，其还搭载一项全新攻击功能：检测受感染主机上是否安装有Ledger Live、Trezor Suite等硬件加密货币钱包应用，并将这些应用替换为植入后门的恶意版本。

![1767511779128623.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20260109/1767923835153963.png "1767923798568877.png")

用于替换正版硬件钱包的恶意代码

据悉，该功能目前尚无法正常运行，原因是植入后门的钱包程序会返回空文件。这可能意味着攻击者仍在调试针对macOS系统的钱包木马，或是相关攻击基础设施正处于过渡期。目前，该功能的框架已搭建完成，只需等待载荷上传即可投入使用。其余恶意功能（凭证窃取、钥匙串访问、数据窃取、持久化驻留）均保持完全可用状态。

目前，其中两款插件已被OpenVSX平台平台标记警告，提示其发布者身份未经验证。

![1767511782731202.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20260109/1767923838123038.png "1767923820183960.png")

OpenVSX 平台上的GlassWorm恶意插件

下载量统计数据显示，这些恶意插件的安装量已超3.3万次，但这类数据往往会被威胁组织篡改，以此增加文件的可信度。

安全人员建议，已安装上述三款插件的开发者应立即卸载插件，重置GitHub账户密码，撤销NPM令牌，全面检查系统是否存在感染痕迹，必要时可重装系统。

文章来源自：https://www.bleepingcomputer.com/news/security/new-glassworm-malware-wave-targets-macs-with-trojanized-crypto-wallets/如若转载，请注明原文地址

* 分享至

![取消](https://www.4hou.com/sihou/images/close.jpg)
![嘶吼](https://www.4hou.com/sihou/images/logo.png)

感谢您的支持，我会继续努力的!

![扫码支持]( "扫一扫")

打开微信扫一扫后点击右上角即可分享哟

### 发表评论

评论

![](https://www.4hou.com/captcha/flat?KvWJdEzl)

#### 你可能感兴趣的

* [![]()

  GlassWorm恶意软件新变种来袭 植入后门加密钱包瞄准Mac设备](https://www.4hou.com/posts/pn4X)
* [![]()

  国家计算机病毒应急处理中心检测发现71款违法违规收集使用个人信息的移动应用](https://www.4hou.com/posts/wxog)
* [![]()

  2025 年度全球网络安全与网络攻击重大事件盘点](https://www.4hou.com/posts/W1Y4)
* [![]()

  2025年十大网络安全事件盘点：数字风险已闯入寻常生活](https://www.4hou.com/posts/jBXY)
* [![]()

  CSTIS：关于防范SleepyDck恶意软件的风险提示](https://www.4hou.com/posts/kgYr)
* [![]()

  仿冒微软激活工具域名暗藏恶意脚本致Windows设备感染](https://www.4hou.com/posts/NGMm)

![](https://img.4hou.com/images/微信图片_20231102150249.jpg)

# [胡金鱼](https://www.4hou.com/member/BVMN)

这个家伙很懒,什么也没说!

#### 最新文章

* [GlassWorm恶意软件新变种来袭 植入后门加密钱包瞄准Mac设备](https://www.4hou.com/posts/pn4X)
  2026-01-09 12:00:00
* [国家计算机病毒应急处理中心检测发现71款违法违规收集使用个人信息的移动应用](https://www.4hou.com/posts/wxog)
  2026-01-09 10:51:13
* [2025 年度全球网络安全与网络攻击重大事件盘点](https://www.4hou.com/posts/W1Y4)
  2026-01-08 15:18:41
* [2025年十大网络安全事件盘点：数字风险已闯入寻常生活](https://www.4hou.com/posts/jBXY)
  2026-01-07 12:00:00

[查看更多](https://www.4hou.com/member/BVMN)

# 相关热文

* [GlassWorm恶意软件新变种来袭 植入后门加密钱包瞄准Mac设备](https://www.4hou.com/posts/pn4X)

  胡金鱼
* [国家计算机病毒应急处理中心检测发现71款违法违规收集使用个人信息的移动应用](https://www.4hou.com/posts/wxog)

  胡金鱼
* [2025 年度全球网络安全与网络攻击重大事件盘点](https://www.4hou.com/posts/W1Y4)

  胡金鱼
* [2025年十大网络安全事件盘点：数字风险已闯入寻常生活](https://www.4hou.com/posts/jBXY)

  山卡拉
* [CSTIS：关于防范SleepyDck恶意软件的风险提示](https://www.4hou.com/posts/kgYr)

  胡金鱼
* [仿冒微软激活工具域名暗藏恶意脚本致Windows设备感染](https://www.4hou.com/posts/NGMm)

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