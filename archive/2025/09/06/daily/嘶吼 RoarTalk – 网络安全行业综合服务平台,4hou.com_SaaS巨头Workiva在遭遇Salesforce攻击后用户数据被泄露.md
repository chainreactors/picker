---
title: SaaS巨头Workiva在遭遇Salesforce攻击后用户数据被泄露
url: https://www.4hou.com/posts/QXzY
source: 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com
date: 2025-09-06
fetch_date: 2025-10-02T19:43:50.246268
---

# SaaS巨头Workiva在遭遇Salesforce攻击后用户数据被泄露

SaaS巨头Workiva在遭遇Salesforce攻击后用户数据被泄露 - 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com

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

# SaaS巨头Workiva在遭遇Salesforce攻击后用户数据被泄露

胡金鱼
[新闻](https://www.4hou.com/category/news)
2025-09-05 12:00:01

![](https://img.4hou.com/article/%E6%B5%8F%E8%A7%88.png)56813

收藏

导语：据Workiva发送给受影响客户的私人邮件通知显示，攻击者窃取了少量商业联系信息，包括姓名、电子邮箱地址、电话号码以及支持工单内容。

知名云基SaaS（软件即服务）提供商Workiva已通知其客户，攻击者通过入侵第三方客户关系管理（CRM）系统，窃取了部分用户数据。

Workiva的云软件主要用于为财务报告、合规审查和审计工作收集、关联及共享数据。截至去年年底，该公司拥有6305家客户，2024年营收达7.39亿美元。

其客户名单涵盖85%的《财富》500强企业，以及谷歌、T-Mobile、达美航空、Wayfair、好时、Slack、高知特、桑坦德银行、诺基亚、卡夫亨氏、温迪快餐、派拉蒙、梅赛德斯-奔驰等知名企业。

**数据泄露细节与平台安全性说明**

据Workiva上周发送给受影响客户的私人邮件通知显示，攻击者窃取了少量商业联系信息，包括姓名、电子邮箱地址、电话号码以及支持工单内容。

该公司解释称：“此类事件与近期多起针对大型机构的攻击类似。重要的是，Workiva平台本身及其中的所有数据均未被访问或破坏。CRM供应商已通知我们，攻击者是通过一个关联的第三方应用程序非法入侵的。”

Workiva还提醒受影响客户保持警惕，因为被盗信息可能被用于鱼叉式钓鱼攻击。

**关联Salesforce数据泄露事件**

尽管Workiva未披露此次攻击的更多细节，但据了解，该事件是近期Salesforce数据泄露潮的一部分——这一系列攻击与勒索团伙ShinyHunters有关，已影响多家知名企业。

就在不久前，Cloudflare披露称，其被迫轮换了104个由Cloudflare平台签发的令牌，这些令牌被ShinyHunters团伙窃取。该团伙于8月中旬入侵了Cloudflare用于客户支持和内部客户案例管理的Salesforce实例。

自今年年初以来，ShinyHunters就通过语音钓鱼（vishing）针对Salesforce客户实施数据盗窃攻击，受影响企业包括谷歌、Cisco、Allianz Life、、Workday、Qantas、Adidas以及LVMH旗下子公司（包括迪奥、路易威登和蒂芙尼等）。

近期，该勒索团伙的攻击手段有所转变：他们开始利用窃取的OAuth令牌（用于Salesloft的Drift AI聊天工具与Salesforce的集成功能）入侵客户的Salesforce实例，并从客户消息和支持工单中提取敏感信息，如密码、AWS访问密钥和Snowflake令牌。

通过这种方式，ShinyHunters除了窃取Salesforce CRM数据外，还入侵了少量谷歌Workspace账户，并攻陷了网络安全公司Zscaler和Palo Alto Networks的Salesforce。

文章翻译自：https://www.bleepingcomputer.com/news/security/saas-giant-workiva-discloses-data-breach-after-salesforce-attack/如若转载，请注明原文地址

* 分享至

![取消](https://www.4hou.com/sihou/images/close.jpg)
![嘶吼](https://www.4hou.com/sihou/images/logo.png)

### 发表评论

评论

![](https://www.4hou.com/captcha/flat?56IPgCFK)

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