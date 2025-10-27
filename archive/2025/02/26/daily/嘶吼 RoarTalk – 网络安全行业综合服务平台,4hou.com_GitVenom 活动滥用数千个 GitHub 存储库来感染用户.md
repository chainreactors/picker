---
title: GitVenom 活动滥用数千个 GitHub 存储库来感染用户
url: https://www.4hou.com/posts/KGBG
source: 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com
date: 2025-02-26
fetch_date: 2025-10-06T20:33:25.249364
---

# GitVenom 活动滥用数千个 GitHub 存储库来感染用户

GitVenom 活动滥用数千个 GitHub 存储库来感染用户 - 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com

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

# GitVenom 活动滥用数千个 GitHub 存储库来感染用户

山卡拉
[新闻](https://www.4hou.com/category/news)
2025-02-25 10:19:22

![](https://img.4hou.com/article/%E6%B5%8F%E8%A7%88.png)63776

收藏

导语：GitVenom 活动是一种复杂的网络威胁

GitVenom 活动是一种复杂的网络威胁，利用 GitHub 存储库传播恶意软件并窃取加密货币。该活动通过创建数百个看似合法但包含恶意代码的虚假 GitHub 存储库来实施攻击，旨在诱骗开发人员下载和执行恶意代码，从而导致严重的财务损失。

**恶意代码部署**

GitVenom 背后的攻击者使用多种编程语言（如 Python、JavaScript、C、C++ 和 C#）制作虚假项目。这些项目通常声称提供社交媒体或加密货币管理的自动化工具等功能，但实际上隐藏了恶意代码，执行恶意操作。

![image.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20250225/1740449842213010.png "1740449842213010.png")

恶意存储库的示例结构

* Python 项目：攻击者使用一种技术，在一长行制表符后隐藏解密并执行恶意 Python 脚本的代码。
* JavaScript 项目：嵌入了恶意函数，用于解码并执行 Base64 编码的脚本。
* C、C++ 和 C# 项目：恶意批处理脚本被隐藏在 Visual Studio 项目文件中，以便在构建过程中执行。

这些虚假项目部署的恶意负载会从攻击者控制的 GitHub 存储库下载其他恶意组件。这些组件包括一个 Node.js 窃取程序，用于收集凭证和加密货币钱包数据等敏感信息，并通过 Telegram 将其上传给攻击者。此外，攻击者还使用了开源工具如 AsyncRAT 和 Quasar 后门。

根据 SecureList 的报告，攻击者还使用了剪贴板劫持程序，将加密货币钱包地址替换为攻击者控制的地址，从而导致严重的财务盗窃。值得注意的是，一个攻击者控制的比特币钱包在 2024 年 11 月收到了约 5 BTC（当时价值约 485,000 美元）。

**影响与缓解**

GitVenom 活动已经活跃多年，全球范围内都有感染尝试的报告，尤其是在俄罗斯、巴西和土耳其。这一活动凸显了盲目运行 GitHub 或其他开源平台代码所带来的风险。

为了降低风险，开发人员在执行或集成第三方代码之前必须彻底检查代码。这包括检查可疑的代码模式，并确保代码功能与描述一致。随着开源代码的广泛使用，类似攻击活动的可能性也在增加，这进一步强调了在处理第三方代码时保持警惕的必要性。

本文翻译自：https://gbhackers.com/gitvenom-campaign-abuses-thousands-of-github-repositories/如若转载，请注明原文地址

* 分享至

![取消](https://www.4hou.com/sihou/images/close.jpg)
![嘶吼](https://www.4hou.com/sihou/images/logo.png)

感谢您的支持，我会继续努力的!

![扫码支持]( "扫一扫")

打开微信扫一扫后点击右上角即可分享哟

### 发表评论

评论

![](https://www.4hou.com/captcha/flat?kbdamUXB)

#### 你可能感兴趣的

* [![]()

  ​LastPass提醒macOS用户：假冒热门软件的恶意程序通过虚假GitHub仓库传播](https://www.4hou.com/posts/LGqg)
* [![]()

  新型FileFix社工攻击诱导用户安装StealC信息窃取恶意软件](https://www.4hou.com/posts/nl14)
* [![]()

  新型NPM包利用 QR 码获取 cookie 的恶意软件](https://www.4hou.com/posts/VWE5)
* [![]()

  Cloudflare抵御创纪录DDoS攻击：峰值达22.2 Tbps、106亿PPS](https://www.4hou.com/posts/W1GW)
* [![]()

  npm供应链攻击“Shai-Hulud”持续发酵：187款npm包遭攻陷 含自传播恶意载荷](https://www.4hou.com/posts/mk5p)
* [![]()

  大规模Android广告欺诈团伙“SlopAds”被瓦解：利用224款恶意应用日均发起23亿次广告请求](https://www.4hou.com/posts/l01l)

![](https://img.4hou.com/FjC8MmzrcnfY_rzJyoXU2_G-O0i9)

# [山卡拉](https://www.4hou.com/member/azxO)

这个家伙很懒,什么也没说!

#### 最新文章

* [​LastPass提醒macOS用户：假冒热门软件的恶意程序通过虚假GitHub仓库传播](https://www.4hou.com/posts/LGqg)
  2025-09-30 12:01:00
* [新型FileFix社工攻击诱导用户安装StealC信息窃取恶意软件](https://www.4hou.com/posts/nl14)
  2025-09-29 12:00:00
* [新型NPM包利用 QR 码获取 cookie 的恶意软件](https://www.4hou.com/posts/VWE5)
  2025-09-28 12:00:00
* [Cloudflare抵御创纪录DDoS攻击：峰值达22.2 Tbps、106亿PPS](https://www.4hou.com/posts/W1GW)
  2025-09-26 12:01:00

[查看更多](https://www.4hou.com/member/azxO)

# 相关热文

* [​LastPass提醒macOS用户：假冒热门软件的恶意程序通过虚假GitHub仓库传播](https://www.4hou.com/posts/LGqg)

  胡金鱼
* [新型FileFix社工攻击诱导用户安装StealC信息窃取恶意软件](https://www.4hou.com/posts/nl14)

  胡金鱼
* [新型NPM包利用 QR 码获取 cookie 的恶意软件](https://www.4hou.com/posts/VWE5)

  胡金鱼
* [Cloudflare抵御创纪录DDoS攻击：峰值达22.2 Tbps、106亿PPS](https://www.4hou.com/posts/W1GW)

  胡金鱼
* [npm供应链攻击“Shai-Hulud”持续发酵：187款npm包遭攻陷 含自传播恶意载荷](https://www.4hou.com/posts/mk5p)

  胡金鱼
* [大规模Android广告欺诈团伙“SlopAds”被瓦解：利用224款恶意应用日均发起23亿次广告请求](https://www.4hou.com/posts/l01l)

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