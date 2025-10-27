---
title: 新型钓鱼即服务平台VoidProxy：瞄准微软365与谷歌账户 可绕过第三方SSO防护
url: https://www.4hou.com/posts/om1K
source: 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com
date: 2025-09-18
fetch_date: 2025-10-02T20:17:50.301797
---

# 新型钓鱼即服务平台VoidProxy：瞄准微软365与谷歌账户 可绕过第三方SSO防护

新型钓鱼即服务平台VoidProxy：瞄准微软365与谷歌账户 可绕过第三方SSO防护 - 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com

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

# 新型钓鱼即服务平台VoidProxy：瞄准微软365与谷歌账户 可绕过第三方SSO防护

胡金鱼
[技术](https://www.4hou.com/category/technology)
2025-09-17 12:00:00

![](https://img.4hou.com/article/%E6%B5%8F%E8%A7%88.png)40292

收藏

导语：该平台采用AitM攻击手段，可实时窃取用户凭据、多因素认证（MFA）验证码及会话Cookie。VoidProxy由Okta威胁情报团队发现，研究人员称其具备可扩展性强、规避性高且技术复杂的特点。

最近，一款名为VoidProxy的新型钓鱼即服务（PhaaS）平台被发现，其攻击目标包括微软365和谷歌账户，即便这些账户由Okta等第三方单点登录（SSO）服务商提供保护，也难以幸免。

该平台采用AitM攻击手段，可实时窃取用户凭据、多因素认证（MFA）验证码及会话Cookie。VoidProxy由Okta威胁情报团队发现，研究人员称其具备可扩展性强、规避性高且技术复杂的特点。

**VoidProxy攻击流程解析**

**1. 初始钓鱼邮件投递**：攻击始于从已攻陷账户（多来自Constant Contact、Active Campaign、NotifyVisitors等邮件服务提供商）发送的钓鱼邮件，邮件中包含短链接——用户点击后会经过多次重定向，最终跳转至钓鱼网站。

**2. 恶意网站伪装与防护**：钓鱼网站托管在.icu、.sbs、.cfd、.xyz、.top、.home等低成本临时域名上，并通过Cloudflare隐藏真实IP地址。访问者首先会遇到Cloudflare的验证码（CAPTCHA）验证，此举既能过滤机器人流量，又能增强网站“合法性”；同时，平台利用Cloudflare Worker环境过滤流量并加载页面。

![cloudflare.jpg](https://img.4hou.com/uploads/ueditor/php/upload/image/20250915/1757922258190492.jpg "1757922131988231.jpg")

在恶意网站上进行Cloudflare验证码步骤

**3. 目标定向与页面展示**：针对选定目标，平台会展示模仿微软或谷歌登录界面的钓鱼页面；其余非目标访问者则会被引导至无威胁的通用“欢迎”页面，以此降低被察觉的概率。

**4. 凭据窃取与SSO绕过**：若用户在钓鱼表单中输入凭据，请求会通过VoidProxy的AitM服务器代理至谷歌或微软的官方服务器；

![google-phish.jpg](https://img.4hou.com/uploads/ueditor/php/upload/image/20250915/1757922259631037.jpg "1757922205947409.jpg")

由VoidProxy提供的钓鱼页面

对于使用Okta等SSO服务的联合账户，用户会被重定向至第二阶段钓鱼页面——该页面模仿微软365或谷歌的Okta SSO登录流程，相关请求同样被代理至Okta官方服务器。

**5. 实时数据捕获与会话劫持**：VoidProxy的代理服务器在受害者与合法服务之间中转流量，同时捕获传输过程中的用户名、密码和MFA验证码；当合法服务生成会话Cookie时，平台会拦截该Cookie并创建副本，攻击者可直接在VoidProxy的管理面板中获取。

**防护措施与建议**

![admin-panel.jpg](https://img.4hou.com/uploads/ueditor/php/upload/image/20250915/1757922260944532.jpg "1757922254695108.jpg")

VoidProxy 的管理面板

Okta指出，已启用Okta FastPass等“防钓鱼认证”功能的用户可抵御VoidProxy攻击，并会收到账户正遭受攻击的警告。

研究人员提出以下防护建议：

**·**仅限受管理设备访问敏感应用；

**·**启用基于风险的访问控制；

**·**对管理类应用采用IP会话绑定；

**·**要求管理员执行敏感操作时重新进行身份验证。

文章翻译自：https://www.bleepingcomputer.com/news/security/new-voidproxy-phishing-service-targets-microsoft-365-google-accounts/如若转载，请注明原文地址

* 分享至

![取消](https://www.4hou.com/sihou/images/close.jpg)
![嘶吼](https://www.4hou.com/sihou/images/logo.png)

感谢您的支持，我会继续努力的!

![扫码支持]( "扫一扫")

打开微信扫一扫后点击右上角即可分享哟

### 发表评论

评论

![](https://www.4hou.com/captcha/flat?7Tj3dBYL)

#### 你可能感兴趣的

* [![]()

  新型钓鱼即服务平台VoidProxy：瞄准微软365与谷歌账户 可绕过第三方SSO防护](https://www.4hou.com/posts/om1K)
* [![]()

  ArmouryLoader加载器的全面分析——典型加载器家族系列分析五](https://www.4hou.com/posts/xyE9)
* [![]()

  Darka5恶意家族样本分析](https://www.4hou.com/posts/jBmR)
* [![]()

  NimDoor加密盗窃macOS恶意软件被删除后会自动恢复](https://www.4hou.com/posts/qoEG)
* [![]()

  前瞻对抗｜这大概是首次，AI挖出了Linux内核可利用0day](https://www.4hou.com/posts/6MAV)
* [![]()

  攻防速写｜一条微信消息，实现客户端持久化攻击](https://www.4hou.com/posts/5MzK)

![](https://img.4hou.com/images/微信图片_20231102150249.jpg)

# [胡金鱼](https://www.4hou.com/member/BVMN)

这个家伙很懒,什么也没说!

#### 最新文章

* [新型钓鱼即服务平台VoidProxy：瞄准微软365与谷歌账户 可绕过第三方SSO防护](https://www.4hou.com/posts/om1K)
  2025-09-17 12:00:00
* [ArmouryLoader加载器的全面分析——典型加载器家族系列分析五](https://www.4hou.com/posts/xyE9)
  2025-07-28 11:41:32
* [Darka5恶意家族样本分析](https://www.4hou.com/posts/jBmR)
  2025-07-24 14:04:33
* [NimDoor加密盗窃macOS恶意软件被删除后会自动恢复](https://www.4hou.com/posts/qoEG)
  2025-07-15 12:00:00

[查看更多](https://www.4hou.com/member/BVMN)

# 相关热文

* [新型钓鱼即服务平台VoidProxy：瞄准微软365与谷歌账户 可绕过第三方SSO防护](https://www.4hou.com/posts/om1K)

  胡金鱼
* [ArmouryLoader加载器的全面分析——典型加载器家族系列分析五](https://www.4hou.com/posts/xyE9)

  安天
* [Darka5恶意家族样本分析](https://www.4hou.com/posts/jBmR)

  企业资讯
* [NimDoor加密盗窃macOS恶意软件被删除后会自动恢复](https://www.4hou.com/posts/qoEG)

  胡金鱼
* [前瞻对抗｜这大概是首次，AI挖出了Linux内核可利用0day](https://www.4hou.com/posts/6MAV)

  企业资讯
* [攻防速写｜一条微信消息，实现客户端持久化攻击](https://www.4hou.com/posts/5MzK)

  企业资讯

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