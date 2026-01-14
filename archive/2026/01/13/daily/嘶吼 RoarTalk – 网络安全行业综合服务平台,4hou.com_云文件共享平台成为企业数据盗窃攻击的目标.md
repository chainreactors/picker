---
title: 云文件共享平台成为企业数据盗窃攻击的目标
url: https://www.4hou.com/posts/0MwV
source: 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com
date: 2026-01-13
fetch_date: 2026-01-14T03:34:20.900815
---

# 云文件共享平台成为企业数据盗窃攻击的目标

云文件共享平台成为企业数据盗窃攻击的目标 - 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com

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

# 云文件共享平台成为企业数据盗窃攻击的目标

胡金鱼
[新闻](https://www.4hou.com/category/news)
23小时 前发布

![](https://img.4hou.com/article/%E6%B5%8F%E8%A7%88.png)14878

收藏

导语：其攻击目标主要是浏览器存储数据（账户凭证、信用卡信息、个人资料）、即时通讯软件数据及加密货币钱包信息。

网络犯罪团伙Zestix正对外兜售从数十家企业窃取的核心数据，其入侵途径疑似为攻破这些企业的ShareFile、Nextcloud及OwnCloud云存储实例。

据分析，攻击者的初始访问权限，可能是通过在员工设备上部署RedLine、Lumma、Vidar等信息窃取器，获取相关账户凭证后实现的。

这三款信息窃取器通常通过恶意广告投放或ClickFix社会工程攻击进行传播，其攻击目标主要是浏览器存储数据（账户凭证、信用卡信息、个人资料）、即时通讯软件数据及加密货币钱包信息。

![图片1.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20260106/1767681014146761.png "1767680977203896.png")

Zestix 在地下论坛的兜售内容示例

当云存储平台未启用多因素认证防护时，掌握有效凭证的威胁组织即可未经授权访问文件共享平台等服务。

报告指出，部分被分析的被盗凭证已在犯罪数据库中存在多年，这表明受害企业长期未更换凭证，甚至在时隔许久后仍未失效相关活跃会话。

**多起入侵事件被公开兜售**

据了解，Zestix以初始访问代理（IAB）的身份活跃于地下黑客论坛，专门售卖高价值企业云平台的访问权限。 目前已攻破多个行业组织的ShareFile、Nextcloud及OwnCloud云存储环境，涉及领域包括航空、国防、医疗健康、公用事业、公共交通、电信、法律、房地产及政府机构。

Zestix的攻击流程如下：先解析信息窃取器获取的日志，专门筛选企业云存储平台的访问链接（ShareFile、Nextcloud）；随后利用未启用多因素认证的有效账号密码，登录目标文件共享服务。

安全研究人员通过将其平台监测到的信息窃取器数据，与公开可用的镜像文件、元数据及开源情报进行关联分析，最终锁定了潜在的入侵切入点。

在已分析的案例中，至少有15起事件可确认：企业云存储服务的员工凭证，是被信息窃取器成功窃取的。

需要强调的是，此项验证仅为研究员的单方研判，名单中涉及的企业均未公开确认发生数据泄露事件。唯一的例外或为西班牙国家航空（Iberia），但该公司近期披露的安全事件，并不一定与调查结果相关。

Zestix对外宣称，其兜售的被盗数据量从数十吉字节到数太字节不等，内容涵盖飞机维修手册与机队数据、国防工程文件、客户数据库、医疗健康档案、公共交通系统结构图、公用事业激光雷达测绘图、互联网服务提供商网络配置、卫星项目资料、企业资源规划（ERP）系统源代码、政府合同文件及法律文书等。

这些据称被盗的文件，大多会使企业面临安全漏洞泄露、用户隐私曝光及工业间谍活动等多重风险；而政府合同文件的外泄，更可能引发国家安全层面的担忧。

![图片2.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20260106/1767681024211779.png "1767681024211779.png")

暴露数据的大小和类型

另外，Zestix以Sentap为别名，额外兜售涉及30个受害目标的数据，但研究人员未采用相同方法对这批数据进行验证。

研究人员指出，除已列出的受害企业外，其威胁情报数据显示，云存储凭证泄露是一个更广泛的系统性安全问题，根源在于相关组织未能落实良好的安全防护实践。

目前已监测到数千台受感染的计算机，其中不乏Deloitte、KPMG、三星、Honeywell、Walmart等知名企业的设备。

安全研究人员目前已就此次验证的凭证泄露事件通知了ShareFile，同时也将向Nextcloud和OwnCloud发出了安全预警，以便这些平台能够及时采取相应应对措施。

文章来源自：https://www.bleepingcomputer.com/news/security/cloud-file-sharing-sites-targeted-for-corporate-data-theft-attacks/如若转载，请注明原文地址

* 分享至

![取消](https://www.4hou.com/sihou/images/close.jpg)
![嘶吼](https://www.4hou.com/sihou/images/logo.png)

感谢您的支持，我会继续努力的!

![扫码支持]( "扫一扫")

打开微信扫一扫后点击右上角即可分享哟

### 发表评论

评论

![](https://www.4hou.com/captcha/flat?u7ClyQdn)

#### 你可能感兴趣的

* [![]()

  云文件共享平台成为企业数据盗窃攻击的目标](https://www.4hou.com/posts/0MwV)
* [![]()

  新型网络犯罪工具ErrTraffic实现ClickFix攻击自动化 伪造网站故障诱骗用户中招](https://www.4hou.com/posts/YZ1O)
* [![]()

  GlassWorm恶意软件新变种来袭 植入后门加密钱包瞄准Mac设备](https://www.4hou.com/posts/pn4X)
* [![]()

  国家计算机病毒应急处理中心检测发现71款违法违规收集使用个人信息的移动应用](https://www.4hou.com/posts/wxog)
* [![]()

  2025 年度全球网络安全与网络攻击重大事件盘点](https://www.4hou.com/posts/W1Y4)
* [![]()

  2025年十大网络安全事件盘点：数字风险已闯入寻常生活](https://www.4hou.com/posts/jBXY)

![](https://img.4hou.com/images/微信图片_20231102150249.jpg)

# [胡金鱼](https://www.4hou.com/member/BVMN)

这个家伙很懒,什么也没说!

#### 最新文章

* [云文件共享平台成为企业数据盗窃攻击的目标](https://www.4hou.com/posts/0MwV)
  2026-01-13 12:00:00
* [新型网络犯罪工具ErrTraffic实现ClickFix攻击自动化 伪造网站故障诱骗用户中招](https://www.4hou.com/posts/YZ1O)
  2026-01-12 12:00:00
* [GlassWorm恶意软件新变种来袭 植入后门加密钱包瞄准Mac设备](https://www.4hou.com/posts/pn4X)
  2026-01-09 12:00:00
* [国家计算机病毒应急处理中心检测发现71款违法违规收集使用个人信息的移动应用](https://www.4hou.com/posts/wxog)
  2026-01-09 10:51:13

[查看更多](https://www.4hou.com/member/BVMN)

# 相关热文

* [云文件共享平台成为企业数据盗窃攻击的目标](https://www.4hou.com/posts/0MwV)

  胡金鱼
* [新型网络犯罪工具ErrTraffic实现ClickFix攻击自动化 伪造网站故障诱骗用户中招](https://www.4hou.com/posts/YZ1O)

  胡金鱼
* [GlassWorm恶意软件新变种来袭 植入后门加密钱包瞄准Mac设备](https://www.4hou.com/posts/pn4X)

  胡金鱼
* [国家计算机病毒应急处理中心检测发现71款违法违规收集使用个人信息的移动应用](https://www.4hou.com/posts/wxog)

  胡金鱼
* [2025 年度全球网络安全与网络攻击重大事件盘点](https://www.4hou.com/posts/W1Y4)

  胡金鱼
* [2025年十大网络安全事件盘点：数字风险已闯入寻常生活](https://www.4hou.com/posts/jBXY)

  山卡拉

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