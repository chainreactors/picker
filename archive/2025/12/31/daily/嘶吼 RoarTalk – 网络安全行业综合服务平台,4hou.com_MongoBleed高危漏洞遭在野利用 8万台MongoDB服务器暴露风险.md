---
title: MongoBleed高危漏洞遭在野利用 8万台MongoDB服务器暴露风险
url: https://www.4hou.com/posts/OGNB
source: 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com
date: 2025-12-31
fetch_date: 2026-01-01T03:35:14.843458
---

# MongoBleed高危漏洞遭在野利用 8万台MongoDB服务器暴露风险

MongoBleed高危漏洞遭在野利用 8万台MongoDB服务器暴露风险 - 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com

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

# MongoBleed高危漏洞遭在野利用 8万台MongoDB服务器暴露风险

胡金鱼
[漏洞](https://www.4hou.com/category/vulnerable)
23小时 前发布

![](https://img.4hou.com/article/%E6%B5%8F%E8%A7%88.png)7364

收藏

导语：MongoBleed漏洞的根源在于MongoDB服务器对zlib库处理网络数据包（用于无损数据压缩）的逻辑缺陷。

一款影响多个MongoDB版本的高危漏洞——MongoBleed（CVE-2025-14847）正被黑客在野活跃利用，目前全球公网暴露的潜在易受攻击服务器已超8万台。

该漏洞的公开利用工具及相关技术细节已被披露，攻击者可借助此漏洞，从暴露的MongoDB服务器中远程窃取密钥、凭证及其他敏感数据。

该漏洞的CVSS评分达8.7分，被列为“紧急修复级别”。自12月19日起，自托管MongoDB实例的修复补丁已正式发布。

**漏洞利用原理：内存数据泄露**

MongoBleed漏洞的根源在于MongoDB服务器对zlib库处理网络数据包（用于无损数据压缩）的逻辑缺陷。

Ox Security的研究人员解释，该漏洞的核心问题是：MongoDB在处理网络消息时，返回的是“分配的内存大小”，而非“解压后的数据长度”。

攻击者可发送构造畸形的网络消息，谎报解压后的数据尺寸，诱使服务器分配更大的内存缓冲区。在此过程中，服务器会将包含敏感信息的内存数据泄露给攻击者。

通过这种方式泄露的敏感信息包括但不限于：账号凭证、API密钥/云服务密钥、会话令牌、个人身份信息（PII）、内部日志、配置文件、路径信息及客户端相关数据。

由于网络消息的解压过程发生在身份认证之前，攻击者利用MongoBleed漏洞无需提供有效的登录凭证，攻击门槛极低。

这款名为“MongoBleed”的公开PoC利用工具由Elastic安全研究员开发，其核心功能就是窃取内存中的敏感数据。该PoC工具有效且操作简单：“只需获取MongoDB实例的IP地址，就能开始挖掘内存中的数据库密码（明文存储）、AWS密钥等信息。”

![图片3.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20251229/1766993051164498.png "1766993051164498.png")

MongoBleed 漏洞利用程序致敏感信息泄露

据网络设备探测平台Censys数据，截至12月27日，全球公网暴露的潜在易受攻击MongoDB实例已达8.7万台。

**在野利用现状与检测方案**

云安全平台Wiz的遥测数据显示，该漏洞对云环境的影响同样严重——42%的可见系统中“至少存在一个受CVE-2025-14847漏洞影响的MongoDB实例”。

这些实例既包括内部资源，也涵盖公网暴露节点。目前已监测到MongoBleed（CVE-2025-14847）的在野利用行为，建议企业优先完成补丁更新。

另有未经证实的消息称，部分威胁者宣称在近期育碧《彩虹六号：围攻》在线平台入侵事件中，就利用了MongoBleed漏洞。

补丁更新仅为应对MongoBleed漏洞的一部分，企业还需排查是否已遭入侵。安全研究员提出一种检测方法：重点监控“发起数千次连接，但未产生任何元数据事件的源IP地址”。

不过研究员表示，该检测方法基于当前公开的PoC工具逻辑，攻击者可能通过伪造客户端元数据或降低攻击速度等方式规避检测。

MongoDB已针对MongoBleed漏洞发布修复公告，强烈建议管理员将服务器升级至安全版本：8.2.3、8.0.17、7.0.28、6.0.27、5.0.32或4.4.30。

官方提示，受该漏洞影响的MongoDB版本范围极广：既包括2017年底发布的部分旧版本，也涵盖2025年11月刚发布的新版本，具体如下：

**·**MongoDB 8.2.0 至 8.2.3

**·**MongoDB 8.0.0 至 8.0.16

**·**MongoDB 7.0.0 至 7.0.26

**·**MongoDB 6.0.0 至 6.0.26

**·**MongoDB 5.0.0 至 5.0.31

**·**MongoDB 4.4.0 至 4.4.29

**·**所有MongoDB Server v4.2版本

**·**所有MongoDB Server v4.0版本

**·**所有MongoDB Server v3.6版本

MongoDB Atlas（全托管多云数据库服务）的用户无需手动操作，官方已自动完成补丁更新。MongoDB表示，该漏洞暂无临时规避方案。若暂时无法升级版本，建议用户在服务器上禁用zlib压缩功能，官方已提供具体操作指南。

文章来源自：https://www.bleepingcomputer.com/news/security/exploited-mongobleed-flaw-leaks-mongodb-secrets-87k-servers-exposed/如若转载，请注明原文地址

* 分享至

![取消](https://www.4hou.com/sihou/images/close.jpg)
![嘶吼](https://www.4hou.com/sihou/images/logo.png)

感谢您的支持，我会继续努力的!

![扫码支持]( "扫一扫")

打开微信扫一扫后点击右上角即可分享哟

### 发表评论

评论

![](https://www.4hou.com/captcha/flat?or2sAQUa)

#### 你可能感兴趣的

* [![]()

  MongoBleed高危漏洞遭在野利用 8万台MongoDB服务器暴露风险](https://www.4hou.com/posts/OGNB)
* [![]()

  漏洞预警 | MongoDB 存在未授权内存泄露漏洞（CVE-2025-14847）](https://www.4hou.com/posts/QXPM)
* [![]()

  黑客利用 Gladinet CentreStack 加密漏洞发起远程代码执行攻击](https://www.4hou.com/posts/XPN8)
* [![]()

  新型UEFI漏洞曝光：技嘉、微星、华硕、华擎主板面临启动前攻击风险](https://www.4hou.com/posts/0MWV)
* [![]()

  黑客借 React2Shell 漏洞发起 EtherRAT 恶意软件攻击](https://www.4hou.com/posts/J1v9)
* [![]()

  漏洞预警 | React/Next.js组件RCE漏洞（CVE-2025-55182）详情分析-【附验证环境】](https://www.4hou.com/posts/NGzm)

![](https://img.4hou.com/images/微信图片_20231102150249.jpg)

# [胡金鱼](https://www.4hou.com/member/BVMN)

这个家伙很懒,什么也没说!

#### 最新文章

* [MongoBleed高危漏洞遭在野利用 8万台MongoDB服务器暴露风险](https://www.4hou.com/posts/OGNB)
  2025-12-31 12:00:00
* [漏洞预警 | MongoDB 存在未授权内存泄露漏洞（CVE-2025-14847）](https://www.4hou.com/posts/QXPM)
  2025-12-30 10:29:10
* [黑客利用 Gladinet CentreStack 加密漏洞发起远程代码执行攻击](https://www.4hou.com/posts/XPN8)
  2025-12-24 12:00:00
* [新型UEFI漏洞曝光：技嘉、微星、华硕、华擎主板面临启动前攻击风险](https://www.4hou.com/posts/0MWV)
  2025-12-23 10:36:23

[查看更多](https://www.4hou.com/member/BVMN)

# 相关热文

* [MongoBleed高危漏洞遭在野利用 8万台MongoDB服务器暴露风险](https://www.4hou.com/posts/OGNB)

  胡金鱼
* [漏洞预警 | MongoDB 存在未授权内存泄露漏洞（CVE-2025-14847）](https://www.4hou.com/posts/QXPM)

  盛邦安全
* [黑客利用 Gladinet CentreStack 加密漏洞发起远程代码执行攻击](https://www.4hou.com/posts/XPN8)

  胡金鱼
* [新型UEFI漏洞曝光：技嘉、微星、华硕、华擎主板面临启动前攻击风险](https://www.4hou.com/posts/0MWV)

  胡金鱼
* [黑客借 React2Shell 漏洞发起 EtherRAT 恶意软件攻击](https://www.4hou.com/posts/J1v9)

  胡金鱼
* [漏洞预警 | React/Next.js组件RCE漏洞（CVE-2025-55182）详情分析-【附验证环境】](https://www.4hou.com/posts/NGzm)

  盛邦安全

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