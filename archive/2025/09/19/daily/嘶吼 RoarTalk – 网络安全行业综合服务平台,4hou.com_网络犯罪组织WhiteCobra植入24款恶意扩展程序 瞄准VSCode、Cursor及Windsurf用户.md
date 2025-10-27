---
title: 网络犯罪组织WhiteCobra植入24款恶意扩展程序 瞄准VSCode、Cursor及Windsurf用户
url: https://www.4hou.com/posts/pn16
source: 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com
date: 2025-09-19
fetch_date: 2025-10-02T20:21:22.853612
---

# 网络犯罪组织WhiteCobra植入24款恶意扩展程序 瞄准VSCode、Cursor及Windsurf用户

网络犯罪组织WhiteCobra植入24款恶意扩展程序 瞄准VSCode、Cursor及Windsurf用户 - 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com

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

# 网络犯罪组织WhiteCobra植入24款恶意扩展程序 瞄准VSCode、Cursor及Windsurf用户

胡金鱼
[新闻](https://www.4hou.com/category/news)
2025-09-18 12:00:00

![](https://img.4hou.com/article/%E6%B5%8F%E8%A7%88.png)41247

收藏

导语：目前该攻击活动仍在持续——每当平台移除恶意扩展，攻击者就会立即上传新的恶意代码取而代之。

威胁组织WhiteCobra通过在Visual Studio应用商店和Open VSX注册表中植入24款恶意扩展程序，针对VSCode、Cursor和Windsurf代码编辑器用户发起攻击。

目前该攻击活动仍在持续——每当平台移除恶意扩展，攻击者就会立即上传新的恶意代码取而代之。

以太坊核心开发者Zak Cole在公开帖子中表示，他在使用一款看似合法的Cursor编辑器扩展程序（contractshark.solidity-lang）后，加密货币钱包遭到清空。 Cole指出，这款扩展程序具备所有“正常产品”的特征：专业设计的图标、详细的功能说明，且在Cursor官方注册表OpenVSX上的下载量达5.4万次。

终端安全服务商Koi的研究人员称，WhiteCobra正是今年7月通过伪造Cursor编辑器扩展程序窃取50万美元加密货币的同一组织。

**WhiteCobra攻击详情**

VSCode、Cursor和Windsurf均为支持VSIX格式扩展程序的代码编辑器——VSIX是VS Code应用商店和Open VSX平台上扩展程序的默认打包格式。

这种跨平台兼容性，加之上述平台对扩展程序提交缺乏严格的审核机制，使其成为攻击者理想的攻击载体，能够实现大范围影响。

据Koi安全团队分析，WhiteCobra打造的恶意VSIX扩展程序伪装性极强：不仅精心撰写功能描述，还伪造了高额下载量，以此骗取用户信任。

该团队发现，以下扩展程序属于WhiteCobra最新攻击活动的一部分：

**Open-VSX平台（适用于Cursor/Windsurf）**

1.ChainDevTools.solidity-pro

2.kilocode-ai.kilo-code

3.nomic-fdn.hardhat-solidity

4.oxc-vscode.oxc

5.juan-blanco.solidity

6.kineticsquid.solidity-ethereum-vsc

7.ETHFoundry.solidityethereum

8.JuanFBlanco.solidity-ai-ethereum

9.Ethereum.solidity-ethereum

10.juan-blanco.solidity

11.NomicFdn.hardhat-solidity

12.juan-blanco.vscode-solidity

13.nomic-foundation.hardhat-solidity

14.nomic-fdn.solidity-hardhat

15.Crypto-Extensions.solidity

16.Crypto-Extensions.SnowShsoNo

**VS Code应用商店**

1.JuanFBlanco.awswhh

2.ETHFoundry.etherfoundrys

3.EllisonBrett.givingblankies

4.MarcusLockwood.wgbk

5.VitalikButerin-EthFoundation.blan-co

6.ShowSnowcrypto.SnowShoNo

7.Crypto-Extensions.SnowShsoNo

8.Rojo.rojo-roblox-vscode

![marketplace.jpg](https://img.4hou.com/uploads/ueditor/php/upload/image/20250915/1757923630540698.jpg "1757923155105761.jpg")

冒充合法项目进行钓鱼下载

**恶意代码执行流程与危害**

研究人员表示，钱包被盗的攻击流程始于恶意扩展程序的主文件（extension.js）——该文件“与VSCode扩展模板自带的‘Hello World’基础代码几乎完全一致”，极具迷惑性。

但其中隐藏着一段简单的调用代码，会将执行权转移至次级脚本（prompt.js），随后从Cloudflare Pages下载下一阶段的恶意载荷。该载荷具备平台针对性，分别提供适用于Windows、ARM架构macOS和Intel架构macOS的版本：

Windows系统：通过PowerShell脚本执行Python脚本，再由Python脚本运行外壳代码（shellcode），最终植入LummaStealer恶意软件。

LummaStealer是一款信息窃取工具，专门针对加密货币钱包应用、浏览器扩展程序、浏览器中存储的凭据及即时通讯软件数据发起窃取。

macOS系统：恶意载荷为Mach-O格式的恶意二进制文件，本地执行后会加载一个未知家族的恶意软件。

**威胁组织运作模式与安全建议**

从WhiteCobra的内部操作手册可见，该犯罪组织会设定1万至50万美元的营收目标，提供命令与控制（C2）基础设施搭建指南，并详细规划社会工程学攻击与推广策略。

![leak.jpg](https://img.4hou.com/uploads/ueditor/php/upload/image/20250915/1757923631497204.jpg "1757923209264641.jpg")

泄露的WhiteCobra行动手册

这表明该组织运作高度有组织化，且不会因攻击曝光或扩展被下架而退缩。Koi安全团队指出，WhiteCobra仅需不到3小时就能部署新一轮攻击活动。

研究人员表示，当前扩展程序仓库亟需更完善的验证机制，以区分恶意扩展与合法扩展——因为评分、下载量和评论均可能被篡改，用于骗取用户信任。

针对代码编辑器扩展程序的下载，研究人员给出以下建议：

1. 仔细核查是否存在仿冒知名开发者或如相似名称混淆视听的情况；

2. 优先选择知名度高、信任记录良好的项目；

3. 对短期内突然获得大量下载量和正面评价的新项目保持警惕。

文章翻译自：https://www.bleepingcomputer.com/news/security/whitecobra-floods-vscode-market-with-crypto-stealing-extensions/如若转载，请注明原文地址

* 分享至

![取消](https://www.4hou.com/sihou/images/close.jpg)
![嘶吼](https://www.4hou.com/sihou/images/logo.png)

感谢您的支持，我会继续努力的!

![扫码支持]( "扫一扫")

打开微信扫一扫后点击右上角即可分享哟

### 发表评论

评论

![](https://www.4hou.com/captcha/flat?aLUkVHy6)

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

![](https://img.4hou.com/images/微信图片_20231102150249.jpg)

# [胡金鱼](https://www.4hou.com/member/BVMN)

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

[查看更多](https://www.4hou.com/member/BVMN)

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