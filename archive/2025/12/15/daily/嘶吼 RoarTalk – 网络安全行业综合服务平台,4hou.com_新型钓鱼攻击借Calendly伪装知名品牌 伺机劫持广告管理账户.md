---
title: 新型钓鱼攻击借Calendly伪装知名品牌 伺机劫持广告管理账户
url: https://www.4hou.com/posts/jBoY
source: 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com
date: 2025-12-15
fetch_date: 2025-12-16T03:21:45.886297
---

# 新型钓鱼攻击借Calendly伪装知名品牌 伺机劫持广告管理账户

新型钓鱼攻击借Calendly伪装知名品牌 伺机劫持广告管理账户 - 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com

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

# 新型钓鱼攻击借Calendly伪装知名品牌 伺机劫持广告管理账户

胡金鱼
[新闻](https://www.4hou.com/category/news)
23小时 前发布

![](https://img.4hou.com/article/%E6%B5%8F%E8%A7%88.png)8168

收藏

导语：此次攻击的特殊之处在于，攻击者借助大众熟知的知名品牌建立信任，显著提升了诱骗效果。

一场持续进行的钓鱼攻击活动正以Calendly为诱饵载体，仿冒联合利华、迪士尼、万事达卡、路威酩轩、优步等知名品牌，伺机窃取目标用户的谷歌工作区及脸书商业账户凭证。

尽管针对商业广告管理账户的攻击并非新鲜事，但这一攻击活动具备极强的定向性，其精心打造的钓鱼诱饵大幅提升了攻击成功率。

一旦攻击者获取营销账户权限，便可将其作为跳板，发起各类恶意广告活动，用于中间人钓鱼、恶意软件分发及点击劫持攻击。此外，广告平台支持地域定向、域名过滤及设备精准定位等功能，攻击者可借此实施“水坑式”攻击。

从收益角度看，被攻陷的营销账户还可转售给网络犯罪分子，实现直接变现。而谷歌工作区账户往往关联企业内网环境与核心业务数据，尤其是在单点登录及宽松身份提供商配置下，其被窃取的危害会进一步扩大。

**基于Calendly的钓鱼攻击流程**

Calendly是一款正规的在线日程预约平台，会议组织者可向参会方发送链接，供对方自主选择空闲时段。该平台此前曾被用于钓鱼攻击，而此次攻击的特殊之处在于，攻击者借助大众熟知的知名品牌建立信任，显著提升了诱骗效果。

**攻击的具体流程如下****：**

1. 诱饵投放：攻击者先伪装成知名品牌的招聘人员，向目标用户发送伪造的会议邀约，且钓鱼落地页还会仿冒企业真实员工身份，增强可信度。据悉，这些钓鱼邮件由AI工具生成，累计仿冒品牌超75个，涵盖路威酩轩、乐高、万事达卡、优步等。

![图片4.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20251203/1764751329121022.png "1764751086138016.png")

钓鱼邮件启动攻击

2. 链路跳转：受害者点击邮件链接后，会进入伪造的Calendly页面，页面首先会弹出人机验证（CAPTCHA），验证通过后随即跳转至AiTM钓鱼页面，尝试窃取用户的谷歌工作区登录会话。

3. 多平台适配：Push Security在与某受害机构核实后确认，该活动核心目标为谷歌多客户账户广告管理账户。

![图片5.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20251203/1764751333210742.png "1764751135135053.png")

假的Calendly页面

研究人员最初发现31个支撑该攻击的独立URL，后续又排查出多个变种版本：其一仿冒联合利华、迪士尼、乐高、Artisan等品牌，专门窃取脸书商业账户凭证；另一较新版本则采用浏览器嵌套攻击技术，通过显示含正规URL的伪造弹窗，同时窃取谷歌与脸书两类账户凭证。

![图片6.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20251203/1764751336410884.png "1764751205180051.png")

针对脸书账户的页面

4. 反检测机制：钓鱼页面还内置反分析防护，包括拦截VPN及代理流量、禁止访客在页面内打开开发者工具等，以此规避安全检测。

![图片7.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20251203/1764751340185126.png "1764751257194732.png")

变体针对两种账户类型

**并行的恶意广告钓鱼活动**

与此同时，Push Security还监测到另一项针对谷歌广告管理账户的恶意广告攻击：用户在谷歌搜索中查询“Google Ads”时，可能点击到恶意赞助广告，进而被导向谷歌广告主题的钓鱼页面，最终跳转至仿冒谷歌登录界面的AiTM钓鱼站点。

![图片8.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20251203/1764751336203234.png "1764751336203234.png")

恶意搜索结果排名第一

研究发现，此类攻击的恶意页面多部署在Odoo平台，部分还会经Kartra平台跳转。

![图片9.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20251203/1764751371162343.png "1764751371162343.png")

虚假Google广告着陆页

尽管针对广告管理账户的同类攻击早有记载，但对攻击者而言，其仍具备极高的牟利价值。鉴于AiTM技术可绕过双重认证防护，安全机构建议高价值账户持有者采取以下防护措施：使用硬件安全密钥、输入凭证前仔细核验URL、将登录弹窗拖动至浏览器边缘以验证其合法性。

文章来源自：https://www.bleepingcomputer.com/news/security/fake-calendly-invites-spoof-top-brands-to-hijack-ad-manager-accounts/如若转载，请注明原文地址

* 分享至

![取消](https://www.4hou.com/sihou/images/close.jpg)
![嘶吼](https://www.4hou.com/sihou/images/logo.png)

感谢您的支持，我会继续努力的!

![扫码支持]( "扫一扫")

打开微信扫一扫后点击右上角即可分享哟

### 发表评论

评论

![](https://www.4hou.com/captcha/flat?1xu2TEYL)

#### 你可能感兴趣的

* [![]()

  新型钓鱼攻击借Calendly伪装知名品牌 伺机劫持广告管理账户](https://www.4hou.com/posts/jBoY)
* [![]()

  Predator间谍软件采用新型攻击载体实施零点击攻击](https://www.4hou.com/posts/yzKz)
* [![]()

  AI安全元年 | 盘点2025年AI与安全的“相爱相杀”](https://www.4hou.com/posts/Eynm)
* [![]()

  勒索软件利用EDR工具隐秘执行恶意代码](https://www.4hou.com/posts/KGwl)
* [![]()

  Shai-Hulud第二轮攻击波及NPM生态 40万条敏感凭证遭泄露](https://www.4hou.com/posts/gylZ)
* [![]()

  安卓电视 YouTube 客户端 SmartTube 遭入侵 恶意更新强制推送](https://www.4hou.com/posts/rpzk)

![](https://img.4hou.com/images/微信图片_20231102150249.jpg)

# [胡金鱼](https://www.4hou.com/member/BVMN)

这个家伙很懒,什么也没说!

#### 最新文章

* [新型钓鱼攻击借Calendly伪装知名品牌 伺机劫持广告管理账户](https://www.4hou.com/posts/jBoY)
  2025-12-15 12:00:00
* [Predator间谍软件采用新型攻击载体实施零点击攻击](https://www.4hou.com/posts/yzKz)
  2025-12-12 12:00:00
* [AI安全元年 | 盘点2025年AI与安全的“相爱相杀”](https://www.4hou.com/posts/Eynm)
  2025-12-11 14:17:49
* [勒索软件利用EDR工具隐秘执行恶意代码](https://www.4hou.com/posts/KGwl)
  2025-12-11 12:00:00

[查看更多](https://www.4hou.com/member/BVMN)

# 相关热文

* [新型钓鱼攻击借Calendly伪装知名品牌 伺机劫持广告管理账户](https://www.4hou.com/posts/jBoY)

  胡金鱼
* [Predator间谍软件采用新型攻击载体实施零点击攻击](https://www.4hou.com/posts/yzKz)

  胡金鱼
* [AI安全元年 | 盘点2025年AI与安全的“相爱相杀”](https://www.4hou.com/posts/Eynm)

  山卡拉
* [勒索软件利用EDR工具隐秘执行恶意代码](https://www.4hou.com/posts/KGwl)

  胡金鱼
* [Shai-Hulud第二轮攻击波及NPM生态 40万条敏感凭证遭泄露](https://www.4hou.com/posts/gylZ)

  胡金鱼
* [安卓电视 YouTube 客户端 SmartTube 遭入侵 恶意更新强制推送](https://www.4hou.com/posts/rpzk)

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