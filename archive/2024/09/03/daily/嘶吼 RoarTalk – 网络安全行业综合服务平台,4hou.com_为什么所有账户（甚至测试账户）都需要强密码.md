---
title: 为什么所有账户（甚至测试账户）都需要强密码
url: https://www.4hou.com/posts/rpkK
source: 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com
date: 2024-09-03
fetch_date: 2025-10-06T18:24:05.836680
---

# 为什么所有账户（甚至测试账户）都需要强密码

为什么所有账户（甚至测试账户）都需要强密码 - 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com

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

# 为什么所有账户（甚至测试账户）都需要强密码

胡金鱼
[新闻](https://www.4hou.com/category/news)
2024-09-02 12:01:00

![](https://img.4hou.com/article/%E6%B5%8F%E8%A7%88.png)85500

收藏

导语：这些犯罪分子往往采用新技术来实施密码喷洒攻击和其他暴力破解方法。

强密码是保护用户帐户的关键——即使是已经忘记的帐户。黑客也会寻找任何方法来访问用户的环境或窃取数据，甚至利用早已被遗忘的陈旧或不活跃的帐户。

旧账户很容易被忽视，但它们仍然可以为黑客提供初始访问路线，并为他们提供扩大活动的平台。每个有权访问用户基础设施的账户都很重要。

**保护测试账户**

测试环境（例如在创建新软件或网站功能时生成的环境）是黑客的首要目标。犯罪分子可以利用这些帐户轻松访问数据：例如，用于开发测试环境的真实客户信息。他们甚至可以利用这些环境作为跳板，访问其他更具特权的帐户。黑客可以利用管理员或特权帐户造成更大的破坏。

当熟练的攻击者获得具有登录凭据的任何用户帐户的访问权限（即使是具有非常低访问权限的旧测试帐户）时，他们可以将其用作扩展访问权限和提升权限的平台。

例如，他们可以在具有相似权限级别的帐户之间水平移动，或者垂直跳转到具有更多权限的帐户，例如 IT 团队帐户或管理员帐户。

**微软漏洞利用测试账户**

今年 1 月，微软表示其公司网络遭到俄罗斯黑客的攻击。名为 Midnight Blizzard 的攻击者窃取了电子邮件和附加文件。

微软表示，只有“极小一部分”公司电子邮件账户遭到入侵，但其中确实包括高层领导以及网络安全和法律团队的员工。

攻击者使用“密码喷洒攻击”入侵，这是一种暴力破解技术，涉及对多个账户尝试相同的密码。这次攻击没有利用微软系统或产品的漏洞。

相反，这就像猜测未使用的测试帐户上的弱密码或已知被破解的密码一样简单。用该软件巨头的话来说，攻击者“使用密码喷洒攻击来破坏传统的非生产测试租户帐户并获得立足点”。

这就强调了确保所有帐户（而不仅仅是管理员或特权帐户）获得最高级别保护的重要性。

至关重要的是，企业应避免在测试账户上使用弱凭据或默认凭据；在 PoC 之后，应停用测试账户/环境；并且应正确隔离测试账户和类似环境。

**如何使用强密码确保所有账户安全**

那么用户可以采取什么措施来保护自己的所有帐户——即使是在非活动环境中时。

**·**Active Directory 审计：保持对未使用和不活跃帐户以及其他与密码相关的漏洞的可见性至关重要。

**·**多因素身份验证：MFA 是抵御黑客的重要防御措施，即使密码被泄露，也能为您提供额外的防御层。

防御措施越多越好，可以从双因素身份验证开始。例如，输入密码后通过一次性密码确认。然而，最强大的 MFA 不止两个步骤，可能还包括生物识别方法，例如面部扫描或指纹。

如果用户在账户（甚至是测试账户）中建立了 MFA，安全性将大大提高。但是，请注意 MFA 仍然可以被规避，密码泄露仍然是最常见的起点。

**·**加强密码策略：有效的密码是抵御黑客的重要第一道防线。用户·的密码策略应阻止最终用户创建包含常见基本术语或键盘行列（如“qwerty”或“123456”）的弱密码。

最好的方法是强制使用长而独特的密码或密码短语，同时使用自定义词典来阻止与特定组织和行业相关的任何术语。

**升级所有帐户的密码安全性**

毫无疑问，人们面对的是一群非常老练的网络犯罪分子，他们会利用任何弱点来破坏用户的系统、窃取用户的数据、造成经济损失甚至毁掉声誉。这些犯罪分子往往采用新技术来实施密码喷洒攻击和其他暴力破解方法。

然而，尽管这些技术为黑客提供了新的攻击途径，但它也是建立防御的关键。借助密码策略和密码审计器等工具，用户可以检测帐户中的漏洞，甚至是不知道的漏洞。所以，建议所有人都应该勤加利用相关安全工具以保护自己的账户。

文章翻译自：https://www.bleepingcomputer.com/news/security/why-all-accounts-even-test-accounts-need-strong-passwords/如若转载，请注明原文地址

* 分享至

![取消](https://www.4hou.com/sihou/images/close.jpg)
![嘶吼](https://www.4hou.com/sihou/images/logo.png)

### 发表评论

评论

![](https://www.4hou.com/captcha/flat?WOhHgeFy)

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