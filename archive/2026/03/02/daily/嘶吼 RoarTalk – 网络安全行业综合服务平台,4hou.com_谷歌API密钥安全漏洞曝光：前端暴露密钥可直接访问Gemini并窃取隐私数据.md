---
title: 谷歌API密钥安全漏洞曝光：前端暴露密钥可直接访问Gemini并窃取隐私数据
url: https://www.4hou.com/posts/kgyv
source: 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com
date: 2026-03-02
fetch_date: 2026-03-03T04:11:31.935936
---

# 谷歌API密钥安全漏洞曝光：前端暴露密钥可直接访问Gemini并窃取隐私数据

谷歌API密钥安全漏洞曝光：前端暴露密钥可直接访问Gemini并窃取隐私数据 - 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com

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

# 谷歌API密钥安全漏洞曝光：前端暴露密钥可直接访问Gemini并窃取隐私数据

胡金鱼
[漏洞](https://www.4hou.com/category/vulnerable)
2026-03-02 11:49:21

![](https://img.4hou.com/article/%E6%B5%8F%E8%A7%88.png)6273

收藏

导语：攻击者可从网页源代码中复制API密钥，通过Gemini API服务访问私密数据。

安全研究人员最新发现，嵌入在可访问前端代码中、用于地图等服务的谷歌API密钥，可被用于向Gemini AI助手进行身份认证，并访问私密数据。研究人员在扫描来自多个行业机构（甚至包括谷歌自身）的公开网页时，发现了近3000个此类密钥。

该问题源于谷歌推出Gemini助手、开发者开始在项目中启用大语言模型API之后。在此之前，谷歌云API密钥不被视为敏感数据，即使公开暴露也普遍认为无安全风险。

开发者通常使用API密钥为项目扩展功能，例如在网站中加载地图、嵌入YouTube视频、使用统计服务或Firebase相关功能。而随着Gemini的推出，谷歌云API密钥同时具备了谷歌AI助手的身份凭证权限。

研究人员表示：攻击者可从网页源代码中复制API密钥，通过Gemini API服务访问私密数据。

由于Gemini API并非免费使用，攻击者还可滥用该权限调用接口，为自身牟利。根据模型与上下文窗口不同，恶意攻击者若将API调用量刷满，单个受害者账户每天可能产生数千美元的费用。这些API密钥已在公开JavaScript代码中暴露多年，如今却在无人察觉的情况下突然获得了更高危的权限。

![图片5.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20260227/1772180757185909.png "1772180757185909.png")

研究人员对2025年11月的Common Crawl数据集进行分析，在代码中发现超过2800个正在使用、且公开暴露的谷歌API密钥。

研究人员称，其中部分密钥被大型金融机构、安全公司和招聘公司使用。他们已向谷歌报告该问题，并提供了来自谷歌自身基础设施的相关样本。

其中一个案例显示，某枚仅用作标识符的API密钥至少从2023年2月起就已部署，并嵌入在谷歌某产品的公开网站页面源代码中。

![图片6.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20260227/1772180834547054.png "1772180834547054.png")

Google的暴露密钥

安全研究人员使用该密钥调用Gemini API的/models接口，成功列出了可用模型。并于2025年11月21日向谷歌通报该问题。经过多轮沟通，谷歌在2026年1月13日将该漏洞归类为“单服务权限提升”。

谷歌表示，目前已实施主动检测机制，拦截试图访问Gemini API的泄露API密钥。宣布将采取以下措施：

-新的AI Studio密钥默认仅开放Gemini权限范围

-泄露的API密钥将被禁止访问Gemini

-检测到密钥泄露时将主动发送通知

谷歌建议开发者检查项目中是否启用了Gemini（生成式语言API），审计环境中所有API密钥是否存在公开暴露，并立即轮换存在风险的密钥。

文章来源自：https://www.bleepingcomputer.com/news/security/previously-harmless-google-api-keys-now-expose-gemini-ai-data/如若转载，请注明原文地址

* 分享至

![取消](https://www.4hou.com/sihou/images/close.jpg)
![嘶吼](https://www.4hou.com/sihou/images/logo.png)

感谢您的支持，我会继续努力的!

![扫码支持]( "扫一扫")

打开微信扫一扫后点击右上角即可分享哟

### 发表评论

评论

![](https://www.4hou.com/captcha/flat?vX9fp3Al)

#### 你可能感兴趣的

* [![]()

  谷歌API密钥安全漏洞曝光：前端暴露密钥可直接访问Gemini并窃取隐私数据](https://www.4hou.com/posts/kgyv)
* [![]()

  思科Catalyst SD-WAN严重认证绕过漏洞遭长期入侵，可植入恶意节点控制网络](https://www.4hou.com/posts/vwNM)
* [![]()

  多款谷歌应用商店心理健康App曝安全漏洞 超千万用户敏感医疗信息面临泄露风险](https://www.4hou.com/posts/mkAn)
* [![]()

  黑客利用 React Native Metro 高危漏洞入侵开发者系统](https://www.4hou.com/posts/DxG5)
* [![]()

  vm2 Node.js沙箱库曝高危漏洞 可突破沙箱执行任意代码](https://www.4hou.com/posts/qoOk)
* [![]()

  黑客反被黑客黑：研究人员劫持 StealC 控制面板，窃取攻击者情报](https://www.4hou.com/posts/XPgo)

![](https://img.4hou.com/images/微信图片_20231102150249.jpg)

# [胡金鱼](https://www.4hou.com/member/BVMN)

这个家伙很懒,什么也没说!

#### 最新文章

* [谷歌API密钥安全漏洞曝光：前端暴露密钥可直接访问Gemini并窃取隐私数据](https://www.4hou.com/posts/kgyv)
  2026-03-02 11:49:21
* [思科Catalyst SD-WAN严重认证绕过漏洞遭长期入侵，可植入恶意节点控制网络](https://www.4hou.com/posts/vwNM)
  2026-02-28 12:00:00
* [多款谷歌应用商店心理健康App曝安全漏洞 超千万用户敏感医疗信息面临泄露风险](https://www.4hou.com/posts/mkAn)
  2026-02-27 11:59:00
* [黑客利用 React Native Metro 高危漏洞入侵开发者系统](https://www.4hou.com/posts/DxG5)
  2026-02-13 12:00:00

[查看更多](https://www.4hou.com/member/BVMN)

# 相关热文

* [谷歌API密钥安全漏洞曝光：前端暴露密钥可直接访问Gemini并窃取隐私数据](https://www.4hou.com/posts/kgyv)

  胡金鱼
* [思科Catalyst SD-WAN严重认证绕过漏洞遭长期入侵，可植入恶意节点控制网络](https://www.4hou.com/posts/vwNM)

  胡金鱼
* [多款谷歌应用商店心理健康App曝安全漏洞 超千万用户敏感医疗信息面临泄露风险](https://www.4hou.com/posts/mkAn)

  胡金鱼
* [黑客利用 React Native Metro 高危漏洞入侵开发者系统](https://www.4hou.com/posts/DxG5)

  胡金鱼
* [vm2 Node.js沙箱库曝高危漏洞 可突破沙箱执行任意代码](https://www.4hou.com/posts/qoOk)

  胡金鱼
* [黑客反被黑客黑：研究人员劫持 StealC 控制面板，窃取攻击者情报](https://www.4hou.com/posts/XPgo)

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