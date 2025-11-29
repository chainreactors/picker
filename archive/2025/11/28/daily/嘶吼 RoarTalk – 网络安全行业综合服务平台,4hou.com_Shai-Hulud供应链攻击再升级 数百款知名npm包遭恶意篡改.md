---
title: Shai-Hulud供应链攻击再升级 数百款知名npm包遭恶意篡改
url: https://www.4hou.com/posts/VW39
source: 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com
date: 2025-11-28
fetch_date: 2025-11-29T03:11:09.958910
---

# Shai-Hulud供应链攻击再升级 数百款知名npm包遭恶意篡改

Shai-Hulud供应链攻击再升级 数百款知名npm包遭恶意篡改 - 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com

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

# Shai-Hulud供应链攻击再升级 数百款知名npm包遭恶意篡改

胡金鱼
[新闻](https://www.4hou.com/category/news)
23小时 前发布

![](https://img.4hou.com/article/%E6%B5%8F%E8%A7%88.png)8675

收藏

导语：目前所有遭篡改的包仍可在npm上下载，但在部分情况下，npm平台会弹出“最新版本未经授权发布”的警告信息，这表明平台的自动审查机制已检测到异常。

在新一轮Shai-Hulud供应链攻击中，攻击者在npm仓库（Node Package Manager）植入了数百款经过恶意篡改的知名软件包，涉及Zapier、ENS Domains、PostHog、Postman等热门项目。

这些恶意软件包被上传至npm平台，核心目的是窃取开发者凭证及持续集成/持续部署（CI/CD）密钥，窃取到的数据会以编码形式自动上传至GitHub。截至本文发布时，GitHub上已检索到27600条与此次攻击相关的记录条目。

![Shai-Hulud_npm_27k.jpg](https://img.4hou.com/uploads/ueditor/php/upload/image/20251125/1764042609582857.jpg "1764042143118737.jpg")

在新Shai-Hulud行动中被窃取秘密的GitHub仓库

Shai-Hulud恶意软件最早于9月中旬现身npm生态，当时它通过自我传播型载荷感染了187个软件包，并利用TruffleHog工具窃取开发者密钥。其攻击手法为：自动下载合法软件包，修改package.json文件以注入恶意脚本，再通过被盗的维护者账号将篡改后的包重新发布到npm。

专注于开发者安全的平台Aikido Security的恶意软件研究员Charlie Eriksen较早发现了这轮新攻击——起初检测到105个带有Shai-Hulud特征的恶意篡改包，此后仅按包名统计，数量已增至492个。随后该研究员发出预警，指出此次供应链攻击窃取的密钥已泄露至GitHub。

然而攻击规模仍在呈指数级扩张，目前恶意包数量已突破2.7万个。云安全平台Wiz的研究人员发现，攻击者共使用了约350个独立的维护者账号，并透露“过去几小时内，每30分钟就有1000个新仓库被创建”。

GitHub上出现的这些仓库，实则表明使用了恶意npm包且环境中存储有GitHub凭证的开发者设备已遭入侵。

CI/CD安全公司Step Security对新版Shai-Hulud恶意软件的技术分析显示，其恶意载荷主要存在于两个文件中：一个是setup\_bun.js，这是一个伪装成Bun安装程序的恶意投放器；另一个是bun\_environment.js，文件大小达10MB。

Step Security指出，该文件采用“极致的代码混淆技术”，例如包含数千条记录的大型十六进制编码字符串、反分析循环，以及用于提取代码中所有字符串的混淆函数。

该恶意软件的攻击流程分为五个阶段，包括窃取密钥（GitHub与npm令牌、AWS、GCP、Azure等云平台的凭证），以及一个破坏性步骤——覆盖受害者的整个主目录。

为自部署软件提供防护解决方案的公司Koi Security统计显示，若计入同一软件包的所有受感染版本，Shai-Hulud已影响超800个npm包。

研究人员确认，新版Shai-Hulud变体的破坏性步骤仅在满足四个特定条件时才会触发：当恶意软件无法通过GitHub认证、无法在GitHub创建仓库、无法获取GitHub令牌，或无法找到npm令牌时，便会删除用户的主目录。

据Wiz透露，恶意代码会收集开发者及CI/CD密钥，并将其上传至“名称包含Shai-Hulud标识”的GitHub仓库。该恶意代码仅在软件包预安装阶段执行，并会创建以下四个文件：cloud.json、contents.json、environment.json、truffleSecrets.json。窃取的密钥会被上传至自动生成的GitHub仓库，这些仓库的描述统一为“Shai-Hulud: The Second Coming”。

![Shai-Hulud_compromised-GitHub.jpg](https://img.4hou.com/uploads/ueditor/php/upload/image/20251125/1764042612114127.jpg "1764042276184316.jpg")

GitHub账户托管来自沙丘行动的仓库

此外，攻击者似乎还获取了部分GitHub账号的控制权，目前正利用这些账号创建包含上述四个文件的仓库。

尽管GitHub会在攻击者创建仓库后立即进行删除，但攻击者创建新仓库的速度极快，难以彻底拦截。

在Aikido Security发现的186个感染新版Shai-Hulud恶意软件的包中，包含多个来自Zapier、ENS Domains、PostHog和AsyncAPI的软件包。其中，遭篡改的Zapier包是构建Zapier集成功能的官方工具包，对Zapier开发者至关重要；而ENS Domains相关包则是钱包、去中心化应用（DApps）、交易所及ENS Manager应用广泛使用的工具库，主要用于处理.eth域名（如将域名解析为以太坊地址、关联IPFS内容、验证域名有效性，以及与官方ENS智能合约交互）。

目前所有遭篡改的包仍可在npm上下载，但在部分情况下，npm平台会弹出“最新版本未经授权发布”的警告信息，这表明平台的自动审查机制已检测到异常。

![npm.jpg](https://img.4hou.com/uploads/ueditor/php/upload/image/20251125/1764042616133917.png "1764042311724022.png")

npm上的警告信息

研究人员建议开发者：获取完整的受感染包列表，将所用包降级至安全版本，并立即更换密钥及CI/CD令牌。

Wiz的研究人员则建议安全团队：首先识别出受感染的包并替换为合法版本，同时督促企业更换所有与npm、GitHub及云服务商相关的凭证。

Aikido Security还建议开发者，若条件允许，在持续集成过程中禁用npm的postinstall（安装后）脚本。

值得注意的是，Shai-Hulud此次卷土重来的背景是在npm平台遭遇多起高影响供应链攻击后。GitHub已推出额外的安全措施以防范此类攻击，但这些措施目前仍在逐步落地中。

文章来源自：https://www.bleepingcomputer.com/news/security/shai-hulud-malware-infects-500-npm-packages-leaks-secrets-on-github/如若转载，请注明原文地址

* 分享至

![取消](https://www.4hou.com/sihou/images/close.jpg)
![嘶吼](https://www.4hou.com/sihou/images/logo.png)

感谢您的支持，我会继续努力的!

![扫码支持]( "扫一扫")

打开微信扫一扫后点击右上角即可分享哟

### 发表评论

评论

![](https://www.4hou.com/captcha/flat?89VuwnzV)

#### 你可能感兴趣的

* [![]()

  Shai-Hulud供应链攻击再升级 数百款知名npm包遭恶意篡改](https://www.4hou.com/posts/VW39)
* [![]()

  年访问量 2600 万的电视盗版流媒体平台Photocall遭联合查处后停运](https://www.4hou.com/posts/OG3G)
* [![]()

  ClickFix 攻击借仿冒 Windows 更新界面推送恶意软件](https://www.4hou.com/posts/RX30)
* [![]()

  九国联合行动摧毁千余台恶意软件服务器](https://www.4hou.com/posts/xyKn)
* [![]()

  “ShadowRay 2.0”全球攻击活动：利用旧漏洞劫持Ray集群构建自传播挖矿僵尸网络](https://www.4hou.com/posts/J13l)
* [![]()

  Cloudflare将本周大规模服务中断事件归咎于数据库问题](https://www.4hou.com/posts/MX3B)

![](https://img.4hou.com/images/微信图片_20231102150249.jpg)

# [胡金鱼](https://www.4hou.com/member/BVMN)

这个家伙很懒,什么也没说!

#### 最新文章

* [Shai-Hulud供应链攻击再升级 数百款知名npm包遭恶意篡改](https://www.4hou.com/posts/VW39)
  2025-11-28 12:01:00
* [年访问量 2600 万的电视盗版流媒体平台Photocall遭联合查处后停运](https://www.4hou.com/posts/OG3G)
  2025-11-28 12:00:00
* [ClickFix 攻击借仿冒 Windows 更新界面推送恶意软件](https://www.4hou.com/posts/RX30)
  2025-11-27 12:00:00
* [九国联合行动摧毁千余台恶意软件服务器](https://www.4hou.com/posts/xyKn)
  2025-11-25 12:00:00

[查看更多](https://www.4hou.com/member/BVMN)

# 相关热文

* [Shai-Hulud供应链攻击再升级 数百款知名npm包遭恶意篡改](https://www.4hou.com/posts/VW39)

  胡金鱼
* [年访问量 2600 万的电视盗版流媒体平台Photocall遭联合查处后停运](https://www.4hou.com/posts/OG3G)

  胡金鱼
* [ClickFix 攻击借仿冒 Windows 更新界面推送恶意软件](https://www.4hou.com/posts/RX30)

  胡金鱼
* [九国联合行动摧毁千余台恶意软件服务器](https://www.4hou.com/posts/xyKn)

  胡金鱼
* [“ShadowRay 2.0”全球攻击活动：利用旧漏洞劫持Ray集群构建自传播挖矿僵尸网络](https://www.4hou.com/posts/J13l)

  胡金鱼
* [Cloudflare将本周大规模服务中断事件归咎于数据库问题](https://www.4hou.com/posts/MX3B)

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