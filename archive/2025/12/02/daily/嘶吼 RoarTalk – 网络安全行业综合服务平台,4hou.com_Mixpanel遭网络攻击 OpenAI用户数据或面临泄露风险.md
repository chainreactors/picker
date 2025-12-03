---
title: Mixpanel遭网络攻击 OpenAI用户数据或面临泄露风险
url: https://www.4hou.com/posts/l0rJ
source: 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com
date: 2025-12-02
fetch_date: 2025-12-03T03:15:38.791662
---

# Mixpanel遭网络攻击 OpenAI用户数据或面临泄露风险

Mixpanel遭网络攻击 OpenAI用户数据或面临泄露风险 - 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com

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

# Mixpanel遭网络攻击 OpenAI用户数据或面临泄露风险

胡金鱼
[新闻](https://www.4hou.com/category/news)
23小时 前发布

![](https://img.4hou.com/article/%E6%B5%8F%E8%A7%88.png)12677

收藏

导语：目前，OpenAI 已启动调查以明确事件的完整影响范围。

OpenAI 正向部分 ChatGPT API 客户发送通知，告知其部分身份信息因第三方分析服务商 Mixpanel 遭遇数据泄露而面临暴露风险。

Mixpanel 提供事件分析服务，OpenAI 借助该服务追踪 API 产品前端界面上的用户交互行为。据了解，这并非 OpenAI 自身系统遭入侵。OpenAI 表示，此次网络安全事件仅影响“与部分 API 用户相关的有限分析数据”，ChatGPT 及其他产品的用户未受波及。

据 Mixpanel 通报，此次攻击“仅影响少量客户”，攻击源于该公司 11 月 8 日检测到的一起短信钓鱼活动。OpenAI 在获悉 Mixpanel 正在开展调查后，于 11 月 25 日收到了受影响数据集的详细信息。

OpenAI 指出，聊天记录、API 请求内容、API 使用数据、密码、凭证信息、API 密钥、支付详情及政府签发身份证件等敏感数据均未被泄露或暴露。此次可能暴露的信息包括：

**·**API 账户注册时提供的姓名

**·**与 API 账户关联的电子邮箱地址

**·**基于 API 用户浏览器获取的大致位置信息（城市、州/省、国家/地区）

**·**用于访问 API 账户的操作系统及浏览器类型

**·**引荐网站（即引导用户访问 API 的来源网站）

**·**与 API 账户关联的组织 ID 或用户 ID

由于未涉及敏感凭证泄露，OpenAI 表示用户无需重置密码或重新生成 API 密钥。

另有部分用户反馈，加密货币投资组合追踪与税务平台 CoinTracker 也受到此次事件影响，泄露数据还包括设备元数据及有限的交易次数信息。

目前，OpenAI 已启动调查以明确事件的完整影响范围。作为预防措施，该公司已将 Mixpanel 从生产服务中移除，并正直接通知相关组织、管理员及个人用户。尽管 OpenAI 着重说明仅 API 用户受影响，但仍向所有订阅用户发送了通知。

OpenAI 警示，泄露的数据可能被用于钓鱼攻击或社会工程学攻击，建议用户警惕与此次事件相关、看似可信的恶意信息。对于包含链接或附件的信息，用户需核实其是否来自 OpenAI 官方域名。同时，该公司敦促用户启用双重认证，切勿通过电子邮件、短信或聊天工具发送密码、API 密钥、验证码等敏感信息。

针对此次攻击，Mixpanel 已采取多项应对措施：保障受影响账户安全、撤销活跃会话及登录权限、更换泄露的凭证信息、封禁攻击者的 IP 地址，并要求所有员工重置密码。此外，该公司还部署了新的安全管控措施，以防范未来发生类似事件。

文章来源自：https://www.bleepingcomputer.com/news/security/openai-discloses-api-customer-data-breach-via-mixpanel-vendor-hack/如若转载，请注明原文地址

* 分享至

![取消](https://www.4hou.com/sihou/images/close.jpg)
![嘶吼](https://www.4hou.com/sihou/images/logo.png)

### 发表评论

评论

![](https://www.4hou.com/captcha/flat?u1rgPkIm)

#### 你可能感兴趣的

* [![]()

  恶意大模型持续升级：WormGPT 4与KawaiiGPT可生成勒索软件代码与钓鱼脚本](https://www.4hou.com/posts/kgqY)
* [![]()

  Mixpanel遭网络攻击 OpenAI用户数据或面临泄露风险](https://www.4hou.com/posts/l0rJ)
* [![]()

  Shai-Hulud供应链攻击再升级 数百款知名npm包遭恶意篡改](https://www.4hou.com/posts/VW39)
* [![]()

  年访问量 2600 万的电视盗版流媒体平台Photocall遭联合查处后停运](https://www.4hou.com/posts/OG3G)
* [![]()

  ClickFix 攻击借仿冒 Windows 更新界面推送恶意软件](https://www.4hou.com/posts/RX30)
* [![]()

  九国联合行动摧毁千余台恶意软件服务器](https://www.4hou.com/posts/xyKn)

![](https://img.4hou.com/images/微信图片_20231102150249.jpg)

# [胡金鱼](https://www.4hou.com/member/BVMN)

这个家伙很懒,什么也没说!

#### 最新文章

* [恶意大模型持续升级：WormGPT 4与KawaiiGPT可生成勒索软件代码与钓鱼脚本](https://www.4hou.com/posts/kgqY)
  2025-12-02 12:00:00
* [Mixpanel遭网络攻击 OpenAI用户数据或面临泄露风险](https://www.4hou.com/posts/l0rJ)
  2025-12-02 11:59:00
* [Shai-Hulud供应链攻击再升级 数百款知名npm包遭恶意篡改](https://www.4hou.com/posts/VW39)
  2025-11-28 12:01:00
* [年访问量 2600 万的电视盗版流媒体平台Photocall遭联合查处后停运](https://www.4hou.com/posts/OG3G)
  2025-11-28 12:00:00

[查看更多](https://www.4hou.com/member/BVMN)

# 相关热文

* [恶意大模型持续升级：WormGPT 4与KawaiiGPT可生成勒索软件代码与钓鱼脚本](https://www.4hou.com/posts/kgqY)

  胡金鱼
* [Mixpanel遭网络攻击 OpenAI用户数据或面临泄露风险](https://www.4hou.com/posts/l0rJ)

  胡金鱼
* [Shai-Hulud供应链攻击再升级 数百款知名npm包遭恶意篡改](https://www.4hou.com/posts/VW39)

  胡金鱼
* [年访问量 2600 万的电视盗版流媒体平台Photocall遭联合查处后停运](https://www.4hou.com/posts/OG3G)

  胡金鱼
* [ClickFix 攻击借仿冒 Windows 更新界面推送恶意软件](https://www.4hou.com/posts/RX30)

  胡金鱼
* [九国联合行动摧毁千余台恶意软件服务器](https://www.4hou.com/posts/xyKn)

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