---
title: 面对域名过期漏洞，PyPI阻断了账户劫持与攻击风险
url: https://www.4hou.com/posts/RXGR
source: 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com
date: 2025-08-22
fetch_date: 2025-10-07T00:17:00.677005
---

# 面对域名过期漏洞，PyPI阻断了账户劫持与攻击风险

面对域名过期漏洞，PyPI阻断了账户劫持与攻击风险 - 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com

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

# 面对域名过期漏洞，PyPI阻断了账户劫持与攻击风险

胡金鱼
[新闻](https://www.4hou.com/category/news)
2025-08-21 12:00:00

![](https://img.4hou.com/article/%E6%B5%8F%E8%A7%88.png)51091

收藏

导语：PyPI 建议用户在账户中添加一个来自非自定义域名的备用邮箱，以避免服务中断；同时，应开启 PyPI 账户的双因素认证，从而增强账户抵御劫持的保护能力。

最新消息，Python 包索引 (PyPI) 目前已引入了新的保护措施，以防止通过密码重置劫持账户的域名复活攻击。

PyPI 是 Python 开源包的官方仓库，为软件开发人员、产品维护者以及使用 Python 库、工具和框架的企业所广泛使用。

项目维护者在PyPI上发布软件的账户与电子邮件地址相关联。对于部分项目而言，其关联的电子邮箱地址还与特定域名绑定。若该域名过期，攻击者便可注册此域名，随后通过搭建邮件服务器并发起账户密码重置请求，进而掌控 PyPI 上的对应项目。

此类攻击的风险在于可能引发供应链攻击：遭劫持的项目会推送恶意版本的热门 Python 包，而在多数情况下，这些恶意包会通过 pip 自动安装。2022 年 5 月“ctx”包遭入侵便是典型案例——攻击者在该包中植入代码，专门针对亚马逊 AWS 密钥及账户凭证。

为解决这一问题，PyPI 如今会对平台上已验证电子邮箱地址所对应的域名进行检查，若发现域名已过期或即将进入过期阶段，便会将相关邮箱地址标记为未验证状态。

从技术层面来看，PyPI 借助 Domainr 的 Status API 确定域名的生命周期阶段（活跃、宽限期、赎回期、待删除），以此判断是否需要对相应账户采取措施。

![diagram(1).jpg](https://img.4hou.com/uploads/ueditor/php/upload/image/20250820/1755671477174803.jpg "1755671032131198.jpg")

域生命周期

一旦电子邮箱地址对应的域名进入上述状态，该邮箱便无法用于密码重置或其他账户恢复操作，即便攻击者注册了该域名，也难以找到可乘之机。

实际上，这些新措施的开发工作于 4 月启动，当时已通过初步扫描对相关情况进行评估。最终，新措施于 2025 年 6 月正式推出，且平台会每日进行扫描。自实施以来，在新系统下已有超过 1800 个电子邮箱地址被标记为未验证。

尽管新措施并非无懈可击，也无法应对所有攻击场景，但它显著降低了攻击者通过利用过期域名劫持 PyPI 账户的风险。PyPI 建议用户在账户中添加一个来自非自定义域名的备用邮箱，以避免服务中断；同时，应开启 PyPI 账户的双因素认证，从而增强账户抵御劫持的保护能力。

文章翻译自：https://www.bleepingcomputer.com/news/security/pypi-now-blocks-domain-resurrection-attacks-used-for-hijacking-accounts/如若转载，请注明原文地址

* 分享至

![取消](https://www.4hou.com/sihou/images/close.jpg)
![嘶吼](https://www.4hou.com/sihou/images/logo.png)

感谢您的支持，我会继续努力的!

![扫码支持]( "扫一扫")

打开微信扫一扫后点击右上角即可分享哟

### 发表评论

评论

![](https://www.4hou.com/captcha/flat?lW1RwC7U)

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