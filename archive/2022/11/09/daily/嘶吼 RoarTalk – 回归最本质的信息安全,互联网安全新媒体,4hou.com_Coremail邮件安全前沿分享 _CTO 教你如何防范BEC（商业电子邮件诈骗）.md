---
title: Coremail邮件安全前沿分享 |CTO 教你如何防范BEC（商业电子邮件诈骗）
url: https://www.4hou.com/posts/WBrn
source: 嘶吼 RoarTalk – 回归最本质的信息安全,互联网安全新媒体,4hou.com
date: 2022-11-09
fetch_date: 2025-10-03T22:01:37.026375
---

# Coremail邮件安全前沿分享 |CTO 教你如何防范BEC（商业电子邮件诈骗）

Coremail邮件安全前沿分享 |CTO 教你如何防范BEC（商业电子邮件诈骗） - 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com

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

# Coremail邮件安全前沿分享 |CTO 教你如何防范BEC（商业电子邮件诈骗）

CACTER
[行业](https://www.4hou.com/category/industry)
2022-11-08 17:38:39

![](https://img.4hou.com/article/%E6%B5%8F%E8%A7%88.png)136469

收藏

导语：如何防范BEC攻击？Coremail CTO近期在邮件安全热点问题探讨交流会中强调账号监测和邮件监测是关键防护重点。

10月27日，Coremail举办聚焦邮件安全热点问题探讨交流会，Coremail CTO林延中莅临直播间，为观众详解Coremail对商业电子邮件诈骗(简称：BEC)的最新研究成果，并分享了应对建议。

![](https://pic2.zhimg.com/80/v2-c9d1fa7ee747027118a87d0c43133681_1440w.webp)

商业电子邮件犯罪(Business Email Compromise，简称BEC)是一种高级的电子邮件攻击，其本质是构造假身份欺骗受害者，尽量使用最少的、隐蔽性高的有效载荷(如URL或附件)来躲避检测。

通常情况下，黑客会伪装成目标受害者的同事或目标受害组织的供应商，要求他们进行付款或发送一些敏感数据。

BEC作为当今常见的邮件诈骗手段，从美国硅谷著名风险投资公司，再到中国外贸行业，均频繁遭遇BEC导致损失巨额财产，使得邮件安全从业者面临更艰巨的考验。

**一、BEC攻击过程全解密**

![](https://pic1.zhimg.com/80/v2-76e9b942961dd3dd3acc7dbb136ca7ec_1440w.webp)

上图为Coremail根据实际案例还原的BEC原理图，黑客不仅冒充了CEO的姓名，也仿冒了该外贸客户的域名，具有很强的欺骗性，结合黑客要求供应商、财务对指定账户进行打款的话术，一旦上当受骗就会遭受较大的财产损失。

**二、什么是域名仿冒？**

Coremail CTO林延中举了个例子，假设域名为http://yourdomain.com的情况下，黑客可能采用大小写、数字进行替换，不仔细甄别很难发现是假冒域名。

![](https://pic4.zhimg.com/80/v2-c252f9549f4ec0ba158474ef0ed9cd5f_1440w.webp)

大小写、数字进行替换的域名仿冒

根据还原案例不难发现，BEC常见攻击过程分为盗号-侦查-潜伏-发起攻击-重复等五个步骤。

![](https://pic1.zhimg.com/80/v2-401b650660817aac53fa734012a0edf0_1440w.webp)

这也说明盗号过程（账号监测） 和 攻击过程（邮件监测）是两个BEC的关键防护重点。

“从全网来看，被盗账号是海量的，可能发生在每一个企业。那么对于Coremail而言，我们的管理难点在于尽可能的减少盗号漏判，同时使用精准的算法识别最后攻击环节的BEC邮件流量，并提供高效预警，通知对应企业的安全人员、管理人员，制止正在发生的BEC诈骗。”
——Coremail CTO　林延中

**BEC防护措施一：CAC 2.0账号监测与处置**

为什么处置被盗账号如此重要？

这是因为黑客在实施BEC前期需要做大量信息收集工作，通过盗号获取员工-公司的历史邮件往来信息。
Coremail作为防守方，能够通过大数据分析和行为习惯分析识别出被盗账号。
黑客通过钓鱼或暴力破解成功盗号后，其行为与正常用户完全一致的概率微乎其微，所以当账号出现的行为与日常习惯偏离较大时，Coremail就能通过这部分异常特征识别可疑账号并处置。
——Coremail CTO　林延中

Coremail账号安全防护产品以防暴卫士为核心、威胁情报为辅，通过对邮箱账号状态进行检测，查看是否有外部的暴力破解、异常登录与内部的疑似被盗账号，有效降低邮箱账号被盗风险。

![](https://pic1.zhimg.com/80/v2-feabb9963bc7995afcd9375b1413b828_1440w.webp)

在过去的8月~10月，Coremail通过对全网检测到的异常账号进行了锁定处置，使得全网异常账号数量骤降。

由于异常账号常常被黑客当做“肉鸡”发送BEC邮件，处置异常账号也意味着BEC邮件、垃圾广告的发送量大幅减少。

**BEC防护措施二：监测仿冒域名：降低BEC攻击影响**

除了处置异常账号，减少BEC邮件的发送量，Coremail每个月也会检测到10~15个正在发生的BEC攻击。

![](https://pic2.zhimg.com/80/v2-edea237773db2f9852a2465addc5f571_1440w.webp)

攻击集中于制造业与海外贸易行业，为了减少BEC攻击带来的不良影响，Coremail通过大数据筛选+人工审核的方式，对管理员及最终用户进行告警，提醒用户可能正在遭受域名仿冒类型的商业诈骗攻击。

![](https://pic2.zhimg.com/80/v2-0f2e11421d0f1913efdaa60457253b05_1440w.webp)

**提醒示例**

Coremail的举措也得到了客户的一致好评，满意度高达100%。

在过去的5月~9月，Coremail主动对39个客户做了BEC诈骗风险提示，降低了客户潜在的商业诈骗风险，挽回潜在金钱损失超千万元。

邮件安全自动化处置也将成为趋势，通过账号安全+邮件威胁监测拦截，构建综合安全体系，进而提升安全作用范围，降低安全人员投入也将成为Coremail未来努力的方向。

Coremail始终倡导以“一站式解决所有邮件安全问题”为基础理念，从现有客户痛点出发，减少客户的运维压力，同时将自身的安全能力赋能给服务客户，提升客户综合防护能力，共同建设良好的邮件安全生态。

以上就是本次交流会的部分内容，更多精彩欢迎登录Coremail管理员社区查看完整回放。

**精华查看**

![](https://pic4.zhimg.com/80/v2-c0c2efecdc4a1383b94a409ce2f153d7_1440w.webp)

了解Coremail CTO

![](https://pic3.zhimg.com/80/v2-56c37647c75900fbe42e3e4b81fcba2a_1440w.webp)

如若转载，请注明原文地址

* 分享至

![取消](https://www.4hou.com/sihou/images/close.jpg)
![嘶吼](https://www.4hou.com/sihou/images/logo.png)

感谢您的支持，我会继续努力的!

![扫码支持]( "扫一扫")

打开微信扫一扫后点击右上角即可分享哟

### 发表评论

评论

![](https://www.4hou.com/captcha/flat?w7dqZplD)

#### 你可能感兴趣的

* [![]()

  Exchange/M365最新防范攻略！CACTER三步补齐原生防护短板](https://www.4hou.com/posts/l03l)
* [![]()

  【附下载】2025我们身边的 网信安全 典型案例等 官方视频汇编](https://www.4hou.com/posts/kg3x)
* [![]()

  蝉联荣誉！梆梆安全再度获选 “北京市委网信办第二届网络安全技术支撑单位”](https://www.4hou.com/posts/9jKP)
* [![]()

  聚焦可信AI安全！SDC2025 议题重磅揭晓](https://www.4hou.com/posts/gy39)
* [![]()

  2025第五届太原网络安全高峰论坛成功举办](https://www.4hou.com/posts/8gJl)
* [![]()

  特勤局手册 | 监听办公室](https://www.4hou.com/posts/42B2)

![](https://img.4hou.com/portraits/789873803bbe1d5cf9b06a0859e2af0b.png)

# [CACTER](https://www.4hou.com/member/64Y9)

国内领先企业级邮件安全解决方案提供商，提供一站式防护。

#### 最新文章

* [Exchange/M365最新防范攻略！CACTER三步补齐原生防护短板](https://www.4hou.com/posts/l03l)
  2025-09-29 17:48:04
* [【附下载】2025我们身边的 网信安全 典型案例等 官方视频汇编](https://www.4hou.com/posts/kg3x)
  2025-09-29 14:55:37
* [蝉联荣誉！梆梆安全再度获选 “北京市委网信办第二届网络安全技术支撑单位”](https://www.4hou.com/posts/9jKP)
  2025-09-29 14:23:50
* [聚焦可信AI安全！SDC2025 议题重磅揭晓](https://www.4hou.com/posts/gy39)
  2025-09-28 17:20:40

[查看更多](https://www.4hou.com/member/64Y9)

# 相关热文

* [Exchange/M365最新防范攻略！CACTER三步补齐原生防护短板](https://www.4hou.com/posts/l03l)

  CACTER
* [【附下载】2025我们身边的 网信安全 典型案例等 官方视频汇编](https://www.4hou.com/posts/kg3x)

  网络伍豪
* [蝉联荣誉！梆梆安全再度获选 “北京市委网信办第二届网络安全技术支撑单位”](https://www.4hou.com/posts/9jKP)

  梆梆安全
* [聚焦可信AI安全！SDC2025 议题重磅揭晓](https://www.4hou.com/posts/gy39)

  企业资讯
* [2025第五届太原网络安全高峰论坛成功举办](https://www.4hou.com/posts/8gJl)

  企业资讯
* [特勤局手册 | 监听办公室](https://www.4hou.com/posts/42B2)

  RC2反窃密实验室

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