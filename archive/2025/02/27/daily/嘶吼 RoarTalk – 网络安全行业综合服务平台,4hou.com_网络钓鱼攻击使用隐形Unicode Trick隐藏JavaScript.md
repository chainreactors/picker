---
title: 网络钓鱼攻击使用隐形Unicode Trick隐藏JavaScript
url: https://www.4hou.com/posts/zA5q
source: 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com
date: 2025-02-27
fetch_date: 2025-10-06T20:32:56.323203
---

# 网络钓鱼攻击使用隐形Unicode Trick隐藏JavaScript

网络钓鱼攻击使用隐形Unicode Trick隐藏JavaScript - 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com

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

# 网络钓鱼攻击使用隐形Unicode Trick隐藏JavaScript

胡金鱼
[技术](https://www.4hou.com/category/technology)
2025-02-26 12:01:00

![](https://img.4hou.com/article/%E6%B5%8F%E8%A7%88.png)267164

收藏

导语：这种攻击很难检测，因为空白减少了安全扫描仪将其标记为恶意的可能性。

一种新的JavaScript混淆方法利用不可见的Unicode字符来表示二进制值，在针对美国政治行动委员会（PAC）附属机构的网络钓鱼攻击中被积极滥用。

发现此次攻击的网络威胁实验室报告称，该攻击发生在2025年1月初，并带有复杂的迹象，例如使用了：

**·**针对受害者提供个性化的非公开信息；

**·**调试器断点和定时检查以逃避检测；

**·**递归包装邮戳跟踪链接到模糊的最终网络钓鱼目的地。

JavaScript开发人员在2024年10月首次披露了这种混淆技术，它在实际攻击中的迅速采用凸显了新研究被武器化的速度。

**使JS有效负载“不可见”**

新的混淆技术利用不可见的Unicode字符，特别是韩文半宽（U+FFA0）和韩文全宽（U+3164）。

JavaScript负载中的每个ASCII字符被转换为8位二进制表示，其中的二进制值（1和0）被不可见的韩文字符替换。

混淆后的代码作为属性存储在JavaScript对象中，由于韩文填充字符呈现为空白，因此脚本中的有效负载看起来为空，如下图末尾的空白所示。

![white-space.webp.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20250220/1740023014119615.png "1740022915298839.png")

隐藏恶意代码的空白

一个简短的引导脚本使用JavaScript代理的“get（）陷阱”检索隐藏的有效负载。当访问hidden属性时，Proxy将不可见的韩文填充字符转换回二进制并重建原始JavaScript代码。

Juniper分析师报告称，攻击者除了上述步骤之外，还使用了额外的隐藏步骤，比如用base64编码脚本，并使用反调试检查来逃避分析。

![base64.jpg](https://img.4hou.com/uploads/ueditor/php/upload/image/20250220/1740023015108965.jpg "1740022980814088.jpg")

韩文填充字符序列的Base64编码

Juniper解释说：“攻击是高度个性化的，包括非公开信息，最初的JavaScript会在被分析时试图调用调试器断点，检测到延迟，然后通过重定向到一个正常的网站来中止攻击。”

这种攻击很难检测，因为空白减少了安全扫描仪将其标记为恶意的可能性。

由于有效负载只是对象中的一个属性，因此可以将其注入合法脚本而不会引起怀疑；另外，整个编码过程很容易实现，不需要高级知识。

Juniper表示，此次活动中使用的两个域名先前与Tycoon 2FA网络钓鱼工具包有关。如果是这样，我们很可能会看到这种不可见的混淆方法在未来被更广泛的攻击者采用。

文章翻译自：https://www.bleepingcomputer.com/news/security/phishing-attack-hides-javascript-using-invisible-unicode-trick/如若转载，请注明原文地址

* 分享至

![取消](https://www.4hou.com/sihou/images/close.jpg)
![嘶吼](https://www.4hou.com/sihou/images/logo.png)

感谢您的支持，我会继续努力的!

![扫码支持]( "扫一扫")

打开微信扫一扫后点击右上角即可分享哟

### 发表评论

评论

![](https://www.4hou.com/captcha/flat?myWsvPQN)

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