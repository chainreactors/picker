---
title: WebRAT恶意软件借GitHub伪造漏洞利用程序传播
url: https://www.4hou.com/posts/Bvw2
source: 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com
date: 2026-01-04
fetch_date: 2026-01-05T03:51:08.310755
---

# WebRAT恶意软件借GitHub伪造漏洞利用程序传播

WebRAT恶意软件借GitHub伪造漏洞利用程序传播 - 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com

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

# WebRAT恶意软件借GitHub伪造漏洞利用程序传播

胡金鱼
[漏洞](https://www.4hou.com/category/vulnerable)
23小时 前发布

![](https://img.4hou.com/article/%E6%B5%8F%E8%A7%88.png)10286

收藏

导语：至少从今年9月起，该恶意软件的运营者开始借助精心构造的GitHub代码仓库投放病毒，这些仓库宣称提供多款曾被媒体报道的漏洞利用程序。

WebRAT恶意软件目前正通过GitHub代码仓库进行传播，这些仓库谎称存放着近期披露漏洞的概念验证（PoC）利用程序。

这款兼具后门功能与信息窃取能力的恶意软件于2025年年初出现，此前的传播渠道为盗版软件，以及《罗布乐思》《反恐精英》《腐蚀》等游戏的作弊程序。

据报告显示，WebRAT能够窃取Steam、Discord、Telegram等平台的账户凭证，以及加密货币钱包数据，同时还可通过摄像头监视受害者，并截取设备屏幕画面。

至少从去年9月起，该恶意软件的运营者开始借助精心构造的GitHub代码仓库投放病毒，这些仓库宣称提供多款曾被媒体报道的漏洞利用程序，涉及的漏洞包括：

-CVE-2025-59295：Windows系统MSHTML/IE组件中存在的堆缓冲区溢出漏洞，攻击者可通过网络发送特制数据，实现任意代码执行。

-CVE-2025-10294：WordPress无密码登录插件OwnID中的高危身份认证绕过漏洞。由于对共享密钥的验证机制存在缺陷，未授权攻击者无需凭证即可登录任意用户账户，包括管理员账户。

-CVE-2025-59230：Windows远程访问连接管理器（RasMan）服务中的权限提升漏洞。本地已认证攻击者可利用该服务的访问控制缺陷，在受影响的Windows设备上将自身权限提升至系统权限（SYSTEM）。

卡巴斯基实验室的安全研究人员共发现15个传播WebRAT的恶意代码仓库，这些仓库均包含漏洞相关说明、所谓利用程序的功能介绍，以及对应的缓解措施。

从内容的行文结构判断，卡巴斯基认为这些文本由人工智能模型生成。

![图片1.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20251224/1766561667123421.png "1766561582137368.png")

恶意仓库中的漏洞描述

该恶意软件具备多种持久化驻留手段，包括修改Windows注册表、创建计划任务，以及将自身注入随机的系统目录中。

研究人员指出，这些伪造的漏洞利用程序以加密压缩包形式分发，压缩包内包含四类文件：文件名即为解压密码的空文件、用作伪装的损坏诱饵动态链接库文件、攻击执行链中所需的批处理文件，以及名rasmanesc.exe的主投放器程序。

![图片2.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20251224/1766561670891585.png "1766561628179939.png")

档案内容

分析显示，这款投放器会先提升自身权限、禁用Windows Defender杀毒软件，再从硬编码的网络地址下载并执行WebRAT恶意软件。

卡巴斯基强调，此次攻击活动中使用的WebRAT变种，与此前已被记录的样本并无差异，具备的功能也与过往报告描述一致。

![图片3.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20251224/1766561678610405.png "1766561678610405.png")

WebRAT的运营概述

利用GitHub上的伪造漏洞利用程序诱骗不明真相的用户安装恶意软件，并非新出现的攻击手段，相关案例在过去已有大量记载。就在近期，威胁者还曾通过在GitHub上推广伪造的LDAPNightmare漏洞利用程序，传播信息窃取类恶意软件。

目前，卡巴斯基发现的所有与本次WebRAT攻击活动相关的恶意GitHub代码仓库均已被移除。但开发者及网络安全爱好者仍需警惕所使用资源的来源，因为威胁者可能会更换发布者名称，再次上传新的诱饵仓库。因此人们在测试来自非可信来源的漏洞利用程序或代码时，务必在可控的隔离环境中运行。

文章来源自：https://www.bleepingcomputer.com/news/security/webrat-malware-spread-via-fake-vulnerability-exploits-on-github/如若转载，请注明原文地址

* 分享至

![取消](https://www.4hou.com/sihou/images/close.jpg)
![嘶吼](https://www.4hou.com/sihou/images/logo.png)

感谢您的支持，我会继续努力的!

![扫码支持]( "扫一扫")

打开微信扫一扫后点击右上角即可分享哟

### 发表评论

评论

![](https://www.4hou.com/captcha/flat?RHpnfZZO)

#### 你可能感兴趣的

* [![]()

  WebRAT恶意软件借GitHub伪造漏洞利用程序传播](https://www.4hou.com/posts/Bvw2)
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

![](https://img.4hou.com/images/微信图片_20231102150249.jpg)

# [胡金鱼](https://www.4hou.com/member/BVMN)

这个家伙很懒,什么也没说!

#### 最新文章

* [WebRAT恶意软件借GitHub伪造漏洞利用程序传播](https://www.4hou.com/posts/Bvw2)
  2026-01-04 12:00:00
* [MongoBleed高危漏洞遭在野利用 8万台MongoDB服务器暴露风险](https://www.4hou.com/posts/OGNB)
  2025-12-31 12:00:00
* [漏洞预警 | MongoDB 存在未授权内存泄露漏洞（CVE-2025-14847）](https://www.4hou.com/posts/QXPM)
  2025-12-30 10:29:10
* [黑客利用 Gladinet CentreStack 加密漏洞发起远程代码执行攻击](https://www.4hou.com/posts/XPN8)
  2025-12-24 12:00:00

[查看更多](https://www.4hou.com/member/BVMN)

# 相关热文

* [WebRAT恶意软件借GitHub伪造漏洞利用程序传播](https://www.4hou.com/posts/Bvw2)

  胡金鱼
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