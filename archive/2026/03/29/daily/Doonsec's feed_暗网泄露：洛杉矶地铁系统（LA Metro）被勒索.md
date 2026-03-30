---
title: 暗网泄露：洛杉矶地铁系统（LA Metro）被勒索
url: https://mp.weixin.qq.com/s/giN1Pv1KsvIndpTQT0Mt3g
source: Doonsec's feed
date: 2026-03-29
fetch_date: 2026-03-30T04:41:50.632876
---

# 暗网泄露：洛杉矶地铁系统（LA Metro）被勒索

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/A0R3tW9L7cea06ibsPEyDj3KkPmVZaUXtPjITQ3GFkWK8IUyzaUZLVtl0l0oCsOaPPCYlzQcGue3ricRMvTE9nRm3QMeTUmJEowf2X1Biafge4/0?wx_fmt=jpeg)

# 暗网泄露：洛杉矶地铁系统（LA Metro）被勒索

原创

c0nsen
c0nsen

开源情报技术研究院

![]()

在小说阅读器中沉浸阅读

事件是2026年3月20日左右由WorldLeaks勒索软件团伙发起的一起典型“数据勒索（Data Extortion）”攻击，针对美国加州洛杉矶市（City of Los Angeles，@LACity）及其下属的洛杉矶地铁系统（LA Metro）。

# 事件核心事实

攻击者：WorldLeaks（2025年由Hunters International重命名后的团伙）。他们已放弃传统加密文件，转而专注于“仅窃取数据+公开威胁”的勒索模式，已有数百起受害案例。

时间线：

3月20日：WorldLeaks在暗网将洛杉矶市列为受害者。

同时攻击LA Metro，导致地铁站显示屏、在线支付系统等部分服务中断，官方被迫限制员工对内部管理系统的访问。

3月27日：@Dail\*\*\*\*\*Web等账号转发截图并发布分析。

团伙宣称的数据规模：

初始X平台截图显示7.7TB / 337,377个文件，文件夹结构包含 /lacity/ 下多个内部目录（CONFIDENTIAL、案件相关数据、警察访谈记录样本等）。

团伙在暗网列出的样本为 159.9 GB / 779个文件（部分来源显示为160GB左右）。

![](https://mmbiz.qpic.cn/mmbiz_png/A0R3tW9L7cd4MPyIDe5csCsPl5yQeYXg0IDXf5dso2ywSeQchKLeOqFRU8OTEGTVju4b8icKxB9gbAcVU57PMW3eFj15IY827XLpMtoiaTdOU/640?wx_fmt=png&from=appmsg)

已公开的证据：仅文件夹截图和少量样本文件（例如警察访谈记录），尚未大规模公开发布完整数据集。团伙威胁“若不谈判/支付赎金，将很快全量泄露”。

# 关联影响与连锁反应

洛杉矶地铁：确认发现“未经授权活动”，主动切断内部系统访问，导致站台到站显示屏离线、部分服务受阻。

湾区其他城市：同一时期，Foster City等宣布进入紧急状态，暂停非紧急公共服务，怀疑同一团伙所为。

潜在数据类型（根据截图和报道推测）：员工记录、薪资/HR文件、财务预算、合同、GIS地图、建筑许可、公共服务数据库，甚至部分警方/案件相关资料。若属实，可能涉及大量居民个人信息。

LA Metro：已公开承认技术问题并采取限制措施，但未详细披露数据泄露细节。

# 风险评估

真实性：高度可信。运营中断+暗网截图+团伙历史记录表明存在真实入侵，但完整7.7TB数据的真实性和敏感度仍待验证（可能包含过时/部分数据，或被夸大）。

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/TEBBMzxzv79ibbJL0UiaZhowrpEOC2OQyZWpf8dPPNOxNib56qImcCo3DA2ickq5aBL0UuF0K1okVYrlS11lSwylibg/0?wx_fmt=png)

开源情报技术研究院

向上滑动看下一个

知道了

![]()
微信扫一扫
使用小程序

取消
允许

取消
允许

取消
允许

×
分析

![跳转二维码]()

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/TEBBMzxzv79ibbJL0UiaZhowrpEOC2OQyZWpf8dPPNOxNib56qImcCo3DA2ickq5aBL0UuF0K1okVYrlS11lSwylibg/0?wx_fmt=png)

微信扫一扫可打开此内容，
使用完整服务

：
，
，
，
，
，
，
，
，
，
，
，
，
。

视频
小程序
赞
，轻点两下取消赞
在看
，轻点两下取消在看
分享
留言
收藏
听过