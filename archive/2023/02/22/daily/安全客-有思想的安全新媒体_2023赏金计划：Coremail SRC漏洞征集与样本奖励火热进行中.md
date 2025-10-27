---
title: 2023赏金计划：Coremail SRC漏洞征集与样本奖励火热进行中
url: https://www.anquanke.com/post/id/286526
source: 安全客-有思想的安全新媒体
date: 2023-02-22
fetch_date: 2025-10-04T07:41:28.945181
---

# 2023赏金计划：Coremail SRC漏洞征集与样本奖励火热进行中

首页

阅读

* [安全资讯](https://www.anquanke.com/news)
* [安全知识](https://www.anquanke.com/knowledge)
* [安全工具](https://www.anquanke.com/tool)

活动

社区

学院

安全导航

内容精选

* [专栏](/column/index.html)
* [精选专题](https://www.anquanke.com/subject-list)
* [安全KER季刊](https://www.anquanke.com/discovery)
* [360网络安全周报](https://www.anquanke.com/week-list)

# 2023赏金计划：Coremail SRC漏洞征集与样本奖励火热进行中

阅读量**253860**

|评论**1**

发布时间 : 2023-02-21 16:00:05

**x**

##### 译文声明

本文是翻译文章

译文仅供参考，具体内容表达以及含义原文为准。

![]()

## 赏金活动一：Coremail SRC漏洞奖励计划

### **01活动背景**

2023年1月，**Coremail安全应急响应中心（Coremail SRC）正式上线启用**，面向公众收集安全漏洞信息与安全情报。Coremail SRC旨在联合众多安全专家、白帽子研究员共同发现潜在的安全威胁，为用户提供全方位的安全保护。

**参与者可在Coremail SRC测试平台进行漏洞挖掘，然后将漏洞报告发送至src@coremail.cn**

### **02漏洞接收范围与要求**

**Coremail SRC接收的漏洞范围**包括

1. Coremail官网（[http://www.](https://link.zhihu.com/?target=http%3A//www.coremail.cn)[coremail.cn](https://link.zhihu.com/?target=http%3A//www.coremail.cn)）
2. Coremail邮件系统试用demo环境（[https://](https://link.zhihu.com/?target=https%3A//sdemo.icoremail.net)[sdemo.icoremail.net](https://link.zhihu.com/?target=https%3A//sdemo.icoremail.net)）
3. cacter官网（[http://www.](https://link.zhihu.com/?target=http%3A//www.cacter.com)[cacter.com](https://link.zhihu.com/?target=http%3A//www.cacter.com)）
4. Coremail邮箱客户端（Air版）【[https://](https://link.zhihu.com/?target=https%3A//lunkr.cn/dl%3Fp%3Dmail%26arch_type%3Dwin64.exe)[lunkr.cn/dl?](https://link.zhihu.com/?target=https%3A//lunkr.cn/dl%3Fp%3Dmail%26arch_type%3Dwin64.exe)[p=mail&arch\_type=win64.exe](https://link.zhihu.com/?target=https%3A//lunkr.cn/dl%3Fp%3Dmail%26arch_type%3Dwin64.exe)】

**暂不接受子域名漏洞和其他系统漏洞**

### **03注意事项**

1、Coremail SRC注重漏洞的可利用性，不接收shelf-XSS、无法获取数据的注入漏洞、仅能探测端口的SSRF、密码明文传输、未设置http安全属性、无法利用的开源依赖库版本漏洞、单纯的暴力破解、拒绝服务类漏洞等。

2、针对Coremail邮件系统的漏洞挖掘请统一在SRC测试平台中进行，请勿在Coremail及用户的生产环境进行漏洞，请勿进行拒绝服务类漏洞测试以免影响其他用户的使用。

### **04奖金安排**

**Coremail SRC为参与者准备了丰厚的现金奖励。只要符合漏洞相关条件，无论是严重漏洞，还是高低危漏洞，都能获得相应的奖励。**

### **严重漏洞奖励：￥**10000-50000元

**高危漏洞奖励：**￥3000-8000元

**中危漏洞奖励：**￥500-3000元

### **低危漏洞奖励：**￥100-300元

### **03获奖公布与奖励领取方式**

参与者请将漏洞报告，管理员会进行审核，审核通过判定级别后将进行邮件回复，告知漏洞等级与奖金金额，奖金将由Coremail工作人员进行联系发放。

### SRC奖励发放约定白帽子需要对漏洞详情进行保密，请勿通过其他平台重复提交

欢迎各位白帽子积极参与！感谢大家共同维护邮件安全生态环境！

## 赏金活动二：恶意样本提交激励计划

“恶意样本提交激励计划”是由CACTER邮件安全发起的一项提高服务客户邮件安全系统保护的活动，主要目的是更好地帮助客户排查潜在风险问题，同时丰富CAC邮件安全大数据中心威胁邮件云端特征库，共同提升CAC大数据中心的识别能力，共同建造良好的邮件安全环境。

注**：“恶意样本提交激励计划”最新活动规则从2022年3月正式开始**

### **01活动内容**

**【参与方式】**

邮件提交可疑/明显的电子邮件（含木马病毒）给**cac-team@coremail.cn**

**【满足条件】**

**1、提交的样本为有效样本**

有效样本是指cac-team评定为漏判的钓鱼邮件、BEC诈骗邮件或病毒邮件（垃圾邮件不在此范畴内）

**2、在规定时间内提交样本**

时效性：收到恶意邮件需在72小时内反馈至cac-team

**【评选标准】**

1、对提交有效样本的客户发放奖励

2、对提交有效样本的价值性和影响面积较大的客户发放奖励

### **02结果公布**

【专家判定】提交样本的1~2天内会通过cac-team邮件反馈您提交的样本结果，请及时查看

【奖励发放】经我司邮件安全专家评定为有效样本的客户，将会在1周内收到领取奖励的邮件，请您及时登录管理员社区留下联系地址

【积分发放】对应的积分奖励将会在每月月末进行核算，可在Coremail管理员社区主页内查询

![]()

**【有奖榜单】**

1. 有奖榜单——会公布每周、每月的恶意样本排行榜

![]()

### **03奖励等级欢迎提交有效恶意样本**

### **钱兔似锦奖：**奖金500元&社区积分奖励100分

**大展宏兔奖：**应季时令水果1箱/鸭鸭家族2只&社区积分奖励10分

### **扬眉兔气奖：**应季时令水果1箱/鸭鸭家族2只&社区积分奖励10分

积分不仅可以用作社区互动答疑、发帖咨询、征集活动，还可以参与社区积分兑换活动

![]()

本文翻译自 原文链接。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**CACTER**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/286526](/post/id/286526)

安全KER - 有思想的安全新媒体

本文转载自:

如若转载,请注明出处：

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [诈骗](/tag/%E8%AF%88%E9%AA%97)
* [邮件安全](/tag/%E9%82%AE%E4%BB%B6%E5%AE%89%E5%85%A8)
* [钓鱼攻击](/tag/%E9%92%93%E9%B1%BC%E6%94%BB%E5%87%BB)

**+1**0赞

收藏

![](https://p0.ssl.qhimg.com/t0155a5d5b8f6dc52a4.png)CACTER

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p0.ssl.qhimg.com/t01ec60109ca3059a09.png)

[![](https://p0.ssl.qhimg.com/t0155a5d5b8f6dc52a4.png)](/member.html?memberId=158115)

[CACTER](/member.html?memberId=158115)

致力于一站式解决所有邮件安全问题

* 文章
* **5**

* 粉丝
* **0**

### TA的文章

* ##### [2023赏金计划：Coremail SRC漏洞征集与样本奖励火热进行中](/post/id/286526)

  2023-02-21 16:00:05
* ##### [活动 | Coremail有奖活动：2022全新发布恶意样本提交激励计划](/post/id/270955)

  2022-03-25 17:30:16
* ##### [活动 | 保卫邮件安全大作战,丰富大奖等你来！](/post/id/257036)

  2021-10-27 10:52:37
* ##### [活动 | Coremail2021邮件安全竞赛正式开幕！快来报名吧！](/post/id/253843)

  2021-09-23 17:30:11
* ##### [活动 | CoremailSRC邀你来找茬，提交漏洞、恶意样本有奖励！](/post/id/237071)

  2021-04-06 17:30:23

### 相关文章

* ##### [2022年移动网络钓鱼攻击数量创历史新高](/post/id/286973)

  2023-03-03 11:00:48
* ##### [社交网站Reddit遭高针对性钓鱼攻击](/post/id/286335)

  2023-02-14 10:15:04
* ##### [域名注册商Namecheap的邮件账户被黑客发送大量钓鱼邮件](/post/id/286312)

  2023-02-13 12:00:17
* ##### [欧洲执法机构捣毁一跨境加密欺诈网络，诈骗金额高达数千万欧元](/post/id/285555)

  2023-01-17 12:00:34
* ##### [记货拉拉信息安全月钓鱼体验活动](/post/id/276741)

  2022-07-22 10:30:15
* ##### [活动 | Coremail有奖活动：2022全新发布恶意样本提交激励计划](/post/id/270955)

  2022-03-25 17:30:16
* ##### [钓鱼小技巧-XLM](/post/id/261493)

  2021-12-06 17:30:43

### 热门推荐

文章目录

* [赏金活动一：Coremail SRC漏洞奖励计划](#h2-0)
  + [01活动背景](#h3-1)
  + [02漏洞接收范围与要求](#h3-2)
  + [03注意事项](#h3-3)
  + [04奖金安排](#h3-4)
  + [严重漏洞奖励：￥10000-50000元](#h3-5)
  + [低危漏洞奖励：￥100-300元](#h3-6)
  + [03获奖公布与奖励领取方式](#h3-7)
  + [SRC奖励发放约定白帽子需要对漏洞详情进行保密，请勿通过其他平台重复提交](#h3-8)
* [赏金活动二：恶意样本提交激励计划](#h2-9)
  + [01活动内容](#h3-10)
  + [02结果公布](#h3-11)
  + [03奖励等级欢迎提交有效恶意样本](#h3-12)
  + [钱兔似锦奖：奖金500元&社区积分奖励100分](#h3-13)
  + [扬眉兔气奖：应季时令水果1箱/鸭鸭家族2只&社区积分奖励10分](#h3-14)

![](https://p0.qhimg.com/t11098f6bcd5614af4bf21ef9b5.png)

安全KER

* [关于我们](/about)
* [联系我们](/note/contact)
* [用户协议](/note/protocol)
* [隐私协议](/note/privacy)

商务合作

* [合作内容](/note/business)
* [联系方式](/note/contact)
* [友情链接](/link)

内容需知

* [投稿须知](https://www.anquanke.com/contribute/tips)
* [转载须知](/note/repost)
* 官网QQ群：568681302

合作单位

* [![安全KER](https://p0.ssl.qhimg.com/t01592a959354157bc0.png)](http://www.cert.org.cn/)
* [![安全KER](https://p0.ssl.qhimg.com/t014f76fcea94035e47.png)](http://www.cnnvd.org.cn/)

Copyright © 北京奇虎科技有限公司 三六零数字安全科技集团有限公司 安全KER All Rights Reserved [京ICP备08010314号-66](https://beian.miit.gov.cn/)[![](https://icon.cnzz.com/img/pic.gif)](https://www.cnzz.com/stat/website.php?web_id=1271278035 "站长统计")

微信二维码

**X**![安全KER](https://p0.ssl.qhimg.com/t0151209205b47f2270.jpg)