---
title: npm供应链攻击“Shai-Hulud”持续发酵：187款npm包遭攻陷 含自传播恶意载荷
url: https://www.4hou.com/posts/mk5p
source: 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com
date: 2025-09-27
fetch_date: 2025-10-02T20:46:26.044286
---

# npm供应链攻击“Shai-Hulud”持续发酵：187款npm包遭攻陷 含自传播恶意载荷

npm供应链攻击“Shai-Hulud”持续发酵：187款npm包遭攻陷 含自传播恶意载荷 - 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com

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

# npm供应链攻击“Shai-Hulud”持续发酵：187款npm包遭攻陷 含自传播恶意载荷

胡金鱼
[新闻](https://www.4hou.com/category/news)
2025-09-26 12:00:00

![](https://img.4hou.com/article/%E6%B5%8F%E8%A7%88.png)32181

收藏

导语：该供应链攻击已导致至少187款npm包被攻陷，这些包中植入了具备自传播能力的恶意载荷，可进一步感染其他npm包。

网络安全研究人员发现，一场持续进行的供应链攻击已导致至少187款npm包被攻陷，这些包中植入了具备自传播能力的恶意载荷，可进一步感染其他npm包。

这场被命名为“Shai-Hulud”的协同式蠕虫攻击于近日启动，最初攻陷的是周下载量超200万次的@ctrl/tinycolor npm包。此后攻击范围大幅扩大，目前已波及CrowdStrike公司npm命名空间下的多个包。

**从tinycolor到CrowdStrike：攻击范围逐步扩大**

目前，高级后端软件工程师Daniel Pereira向社区发出警示，称全球最大的JavaScript包仓库npmjs.com正遭受大规模软件供应链攻击，并提醒所有人避免安装@ctrl/tinycolor项目的最新版本。

![dan-p-post.jpg](https://img.4hou.com/uploads/ueditor/php/upload/image/20250917/1758094221113067.jpg "1758093674511804.jpg")

Pereira提醒大家注意持续的npm供应链攻击

过去24小时内，Pereira曾试图通过更隐秘的渠道联系GitHub，告知其这场持续的攻击——“已有大量代码仓库成为目标”，若公开披露可能会让更多人面临风险。

软件供应链安全公司Socket随即对此次攻击展开调查，初步确认至少40款npm包遭攻陷。如今，Socket与Aikido的研究人员均发现了更多受影响的包，使得受攻陷包的总数达到至少187款。

安全公司StepSecurity也发布了技术分析报告，包含反混淆后的代码片段与攻击流程图，基本印证了Socket的初步调查结果。

受影响的包中，包括多个由CrowdStrike的npmjs账号“crowdstrike-publisher”发布的包。

随后，CrowdStrike发言人回应称：在第三方开源仓库（即公共npm仓库）中检测到多款恶意Node包后，已迅速将其移除，并主动轮换了公共仓库中的密钥。这些包并未用于Falcon传感器（CrowdStrike的核心产品），因此该平台未受影响，客户安全仍有保障。

**自传播蠕虫利用TruffleHog窃取密钥**

遭攻陷的npm包版本中，包含一套针对“同一维护者名下其他包”的自传播机制。Socket研究人员解释称，恶意软件会先下载该维护者发布的所有包，修改包内的package.json文件，植入名为bundle.js的脚本（代码片段如下），重新打包后再发布，从而“实现对下游包的自动木马化感染”。

![socket-bundle_js-file.jpg](https://img.4hou.com/uploads/ueditor/php/upload/image/20250917/1758094221900795.jpg "1758093739161744.jpg")

bundle.js 文件下载 TruffleHog 以提取密钥

bundle.js脚本会调用TruffleHog——这是一款合法的密钥扫描工具，开发者与安全人员常用来检测代码仓库或其他数据源中意外泄露的敏感信息（如API密钥、密码、令牌等）。

但该恶意脚本滥用了这款工具，在主机中搜索令牌与云服务凭证。脚本会验证并利用开发者凭证与持续集成（CI）凭证，在代码仓库中创建GitHub Actions工作流，再将窃取到的信息通过硬编码的Webhook（链接为hxxps://webhook[.]site/bb8ca5f6-4175-45d2-b042-fc9ebb8170b7）外传。

攻击名称“Shai-Hulud”源自遭攻陷包中恶意软件使用的工作流文件“shai-hulud.yaml”，其灵感来自科幻小说《沙丘》系列中的巨型沙虫。

在已发现的其他受攻陷包中，恶意软件与此前版本完全一致，均通过bundle.js执行以下操作：

1. 下载并运行合法密钥扫描工具TruffleHog；

2. 在主机中搜索令牌、云凭证等敏感密钥；

3. 验证发现的开发者凭证与CI凭证是否有效；

4. 在代码仓库中创建未授权的GitHub Actions工作流；

5. 将敏感数据通过硬编码的Webhook端点外传。

**攻击背景：近期大规模供应链攻击频发**

除了攻击目标包含热门npm包外，此次供应链攻击的“时间节点”也尤为特殊——它发生在同一月份的两起高关注度供应链攻击之后。

9月第一周，一场名为“s1ngularity”的攻击中，AI驱动的恶意软件攻陷了2180个GitHub账户。尽管目前仍在调查此次攻击的根本原因，但包括Pereira在内的业内人士推测，此次攻击的幕后黑手可能与“s1ngularity”的攻击者为同一伙人。

本月早些时候，热门npm包chalk与debug的维护者也在另一场独立攻击中遭遇钓鱼，导致其管理的项目被攻陷。

这些攻击产生的连锁反应已深入软件依赖链，可能影响到广泛使用的项目，例如谷歌Gemini CLI。

**安全建议**

这些持续发生的攻击，暴露了现代软件供应链的脆弱性——一个恶意拉取请求或一个遭攻陷的维护者账户，就可能引发连锁反应，影响数百个项目。

尽管谷歌、CrowdStrike等厂商强调其核心平台未受影响，但此次事件仍凸显出一个迫切需求：开发者必须加强对软件构建流程与流水线的安全防护。

针对受影响的用户，建议采取以下措施：

1. 审计自身环境与日志，排查是否存在攻陷痕迹；

2. 轮换所有敏感密钥与CI/CD令牌；

3. 检查依赖树，移除包含恶意版本的包；

4. 将依赖包版本锁定到可信发布版本；

5. 限制发布凭证的权限范围。

文章翻译自：https://www.bleepingcomputer.com/news/security/self-propagating-supply-chain-attack-hits-187-npm-packages/如若转载，请注明原文地址

* 分享至

![取消](https://www.4hou.com/sihou/images/close.jpg)
![嘶吼](https://www.4hou.com/sihou/images/logo.png)

感谢您的支持，我会继续努力的!

![扫码支持]( "扫一扫")

打开微信扫一扫后点击右上角即可分享哟

### 发表评论

评论

![](https://www.4hou.com/captcha/flat?20TyGLED)

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