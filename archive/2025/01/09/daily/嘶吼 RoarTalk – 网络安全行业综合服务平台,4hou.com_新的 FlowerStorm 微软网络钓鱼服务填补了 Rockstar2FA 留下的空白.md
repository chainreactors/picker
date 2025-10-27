---
title: 新的 FlowerStorm 微软网络钓鱼服务填补了 Rockstar2FA 留下的空白
url: https://www.4hou.com/posts/2XJW
source: 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com
date: 2025-01-09
fetch_date: 2025-10-06T20:06:02.674637
---

# 新的 FlowerStorm 微软网络钓鱼服务填补了 Rockstar2FA 留下的空白

新的 FlowerStorm 微软网络钓鱼服务填补了 Rockstar2FA 留下的空白 - 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com

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

# 新的 FlowerStorm 微软网络钓鱼服务填补了 Rockstar2FA 留下的空白

胡金鱼
[新闻](https://www.4hou.com/category/news)
2025-01-08 12:00:00

![](https://img.4hou.com/article/%E6%B5%8F%E8%A7%88.png)94221

收藏

导语：无论 FlowerStorm 突然崛起背后的原因是什么，对于用户和企业来说，它是破坏性网络钓鱼攻击的又一推动因素，可能导致全面的网络攻击。

名为“FlowerStorm”的新 Microsoft 365 网络钓鱼即服务平台填补了 Rockstar2FA 网络犯罪服务突然关闭所留下的空白。

Trustwave 于 2024 年 11 月下旬首次记录，Rockstar2FA 作为 PhaaS 平台运行，促进针对 Microsoft 365 凭据的大规模中间对手 (AiTM) 攻击。该服务提供先进的规避机制、用户友好的面板和众多网络钓鱼选项，以每两周 200 美元的价格向网络犯罪分子出售访问权限。

Sophos 研究人员表示，Rockstar2FA 于 2024 年 11 月 11 日遭遇部分基础设施崩溃，导致该服务的许多页面无法访问，但这似乎不是针对网络犯罪平台的执法行动的结果，而是技术故障。几周后，FlowerStorm 首次出现在网上，并迅速获得关注。

![rockstar.webp.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20241226/1735181107108487.png "1735034481505260.png")

Rockstar2FA 检测

**Rockstar2FA 会重塑品牌吗**

1.这两个平台都使用模仿合法登录页面（例如 Microsoft）的网络钓鱼门户来获取凭据和 MFA 令牌，依赖于 .ru 和 .com 等域上托管的后端服务器。 Rockstar2FA 使用随机 PHP 脚本，而 FlowerStorm 使用 next.php 进行标准化。

2.他们的钓鱼页面的 HTML 结构非常相似，具有评论中的随机文本、Cloudflare“十字转门”安全功能以及“初始化浏览器安全协议”等提示。 Rockstar2FA 使用汽车主题，而 FlowerStorm 则转向植物主题，但底层设计保持一致。

3.凭据收集方法紧密结合，使用电子邮件、通行证和会话跟踪令牌等字段。这两个平台都通过其后端系统支持电子邮件验证和 MFA 身份验证。

4.域名注册和托管模式显著重叠，大量使用 .ru 和 .com 域名以及 Cloudflare 服务。到 2024 年底，它们的活动模式显示出同步上升和下降，表明出潜在的协调。

5.这两个平台都出现了操作错误，暴露了后端系统并表现出了高可扩展性。 Rockstar2FA 管理着 2000 多个域名，而 FlowerStorm 在 Rockstar2FA 崩溃后迅速扩张，这是一个共享框架。

![patterns.webp.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20241226/1735181108634543.png "1735035463540277.png")

活动模式

Sophos 总结道：“我们不能将 Rockstar2FA 和 FlowerStorm 联系起来，除非注意到由于部署的套件内容相似，这些套件至少反映了共同的系统。”

类似的域名注册模式可能反映了 FlowerStorm 和 Rockstar 的协调工作，尽管这些匹配模式也有可能更多地是由市场力量而非平台本身驱动。

**新的危险出现**

无论 FlowerStorm 突然崛起背后的原因是什么，对于用户和企业来说，它是破坏性网络钓鱼攻击的又一推动因素，可能导致全面的网络攻击。 Sophos 的遥测显示，FlowerStorm 所针对的大约 63% 的组织和 84% 的用户位于美国。

![targets.webp.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20241226/1735181110156471.png "1735035541149667.png")

FlowerStorm 目标

最受攻击的行业是服务业（33%）、制造业（21%）、零售业（12%）和金融服务业（8%）。为了防范网络钓鱼攻击，请使用具有 AiTM 抵抗 FIDO2 令牌的多重身份验证 (MFA)、部署电子邮件过滤解决方案，并使用 DNS 过滤来阻止对可疑域（如 .ru、.moscow 和 .dev）的访问。

文章翻译自：https://www.bleepingcomputer.com/news/security/new-flowerstorm-microsoft-phishing-service-fills-void-left-by-rockstar2fa/如若转载，请注明原文地址

* 分享至

![取消](https://www.4hou.com/sihou/images/close.jpg)
![嘶吼](https://www.4hou.com/sihou/images/logo.png)

感谢您的支持，我会继续努力的!

![扫码支持]( "扫一扫")

打开微信扫一扫后点击右上角即可分享哟

### 发表评论

评论

![](https://www.4hou.com/captcha/flat?iEjxBpNO)

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