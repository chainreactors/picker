---
title: 【安全圈】阿联酋国防部网络中心机密文件数据泄露
url: https://mp.weixin.qq.com/s/r7O8hKAzz6VMHH4_iER1Bg
source: Doonsec's feed
date: 2026-03-13
fetch_date: 2026-03-14T04:06:56.184178
---

# 【安全圈】阿联酋国防部网络中心机密文件数据泄露

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/sbq02iadgfyF9wkcXA7jFCZ40lIHRdPfVl5eedA4DvHsJ5G9A79mQrFicfrF3BbkGu4nRgj4kDfdO9t6V0icKIxqyYe2XKD26vZgHTzba9ogf4/0?wx_fmt=jpeg)

# 【安全圈】阿联酋国防部网络中心机密文件数据泄露

安全圈

![]()

在小说阅读器中沉浸阅读

![](https://mmbiz.qpic.cn/sz_mmbiz_png/aBHpjnrGylgOvEXHviaXu1fO2nLov9bZ055v7s8F6w1DD1I0bx2h3zaOx0Mibd5CngBwwj2nTeEbupw7xpBsx27Q/640?wx_fmt=other&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

**关键词**

数据泄露

2026年3月12日，【暗网威胁情报监测系统发现】 信息经纪人兼威胁行为者 **JRINTEL**（又称 jrintel / JR Intel）公开泄露 **[UAE] Classified MoD Cyber Center Defense Documents**。阿联酋国防部网络中心机密文件中的数据。

![20260312220547971-图片](https://mmbiz.qpic.cn/mmbiz_png/sbq02iadgfyE3kcJRZwv8icP7FnuPgpNUicGfRBM6KoWvAMFP5yxT4aDx93hJia8ricIPJz8GU1phHn1b5kFUOCDf6p6Omw3F82ItErfeyibibVEIw/640?wx_fmt=png&from=appmsg)

泄露文件为一压缩包 **UAE.rar**（68.6 MB），包含多份内部 PowerPoint 提案（文件名包括 *Cyber Enablement Proposal\_Adam Version.pptx*、*Cyber Proposal\_v2.0.pptx*、*Cyber Proposal\_v4.5.pptx*），时间跨度从 2021 年至 2026 年 3 月 12 日。

文件详细披露阿联酋国防部（MoD）网络中心构建“第五域”（网络空间）进攻性能力的完整路线图，包括埃米尔化（Emiratization）培训计划、零日漏洞培养、美国公司秘密收购策略及年度预算。

同时附带一张洛克希德·马丁（Lockheed Martin）与阿联酋官员的合影及相关新闻截图。

**威胁等级：高（Critical）**。本次泄露不仅暴露阿联酋网络战略核心，还为地区对手（尤其是伊朗支持的 APT 团体）提供可操作情报，可能引发针对性攻击或外交危机。

## 泄露内容分析

![20260312220629563-图片](https://mmbiz.qpic.cn/sz_mmbiz_png/sbq02iadgfyGXP9BicuHFjOMJzFL3v8onXzKDml8N796E506ecIsXPohMFXQjDI3OKubB0woeehU1cbhOhMsiaSiaa7spia8LiaBD94eicYVjaTiaoo/640?wx_fmt=png&from=appmsg)

**样本文件内容**：

* **Cyber Enablement Proposal\_Adam Version.pptx**（2024 年 7 月 21 日，作者 Joshua Knight）：

+ 核心目标：通过埃米尔化培养 60 名（5 年后 65 名）本土进攻性网络战士，取代外籍专家。
+ 36 个月三阶段培训（Crawl-Walk-Run）：虚拟靶场 + 真实任务（UAE 内部资产 + 第三方国家目标）。
+ 5 大专业领域：代码逆向、应用社工、网络协议、系统数据库、新兴技术（AI/OT/IoT）。
+ 每年预算约 650 万美元（含专家薪资、招聘、实验室、技术）。
+ 实验室三大支柱：训练、模拟真实环境、培养零日漏洞（重点软件、网络、数据库）。

* **Cyber Proposal\_v2.0.pptx**（2026 年 3 月 12 日）：最新版，强调“Global Cyber Defense and Intelligence”，提及中东威胁景观（数据泄露成本、驻留时间）。
* **Cyber Proposal\_v4.5.pptx**（2021 年 10 月 31 日）：早期框架，提出“隐藏在明处”（hide in plain sight）收购美国小型/中型/大型网络咨询与 AI 安全公司（目标：Herjavec、EWA、Cynet、Illumio、Zimperium 等），获取主权技术（XDR、Zero Trust、MTD、IAM）。
  **附加材料**：洛克希德·马丁与阿联酋官员合影（疑似网络合作项目现场）、UAE 建立“网络安全卓越中心”新闻截图。

### 泄露内容深度分析

**战略意图暴露**：

* 阿联酋明确将网络视为“第五域”，目标不仅是防御，还包括进攻性行动（“Engage in missions on 3rd party external targets”）。
* 计划到 2029 年形成 165 名本土专家梯队（35 名教官/专家 + 65 名高级），彻底摆脱对外籍专家依赖。
* “隐藏在明处”收购美国公司策略：通过美国壳公司转包、并购中小型企业（10-400 人）或大型企业（2000 人），实现全球能力快速部署，同时掩盖真实意图。
* 主权技术获取：收购 AI 安全软件公司，拥有知识产权，形成对地区对手的技术优势。

**技术与操作细节**：

* 详细列出所需技能矩阵（高级 Linux、网络协议、SQL、Python、云/OT 等）。
* 实验室重点培养零日漏洞（网络、系统、数据库、加密）。
* 真实任务训练：内部 UAE 资产 + 国家目标。

**财务细节**：

* 2025 年全年 G&A 预算约 656 万美元（含 5 名专家薪资、招聘、旅行、技术）。
* 12 个月启动预算约 300 万美元。

这些细节远超公开信息，属于典型的作战规划级机密。

### 地缘政治连锁

阿联酋近年来多次挫败伊朗支持的网络攻击，此次泄露可能被视为伊朗阵营的“情报胜利”，加剧海湾网络军备竞赛。

## 威胁行为者

**行为者**：JRINTEL（jrintel）
**类型**：财务驱动的“雇佣兵经纪人”（Mercenary Broker），非国家背景。
**活动平台**：Telegram 主频道、BreachForums、ReHub、BreachStars 等。
**历史活动**：

* 曾宣称拥有“所有阿联酋公民数据库”；
* 泄露美国 CIA/MI5/Mossad 特工数据、俄罗斯国防部文件、中国政府数据；
* 同时向中美俄以等多方出售情报，无固定效忠对象。
  **动机**：纯经济利益，通过 Telegram 频道兜售“免费样品”吸引付费订阅或私下交易。
  **本次操作特点**：以“FREE DATA V3”名义公开发布，配以阿联酋国旗照片与洛克希德·马丁合影，旨在最大化曝光与商业价值。
  **评估**：JRINTEL 具备持续获取高价值政府/军方文件的能力，本次泄露可能是其针对阿联酋系列行动的一部分（此前已有 UAEERF、Darb Portal 等泄露）。

***END***

阅读推荐

[【安全圈】首批付费卸载龙虾的用户已出现，专家回应：卸载也难永绝后患](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652074639&idx=1&sn=61b8b11214169b3c7accfb49dc75ce3b&scene=21#wechat_redirect)

[【安全圈】新型 “Zombie ZIP” 技术让恶意软件绕过安全工具](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652074639&idx=2&sn=a9136aab554468e0643fa955a64f6248&scene=21#wechat_redirect)

[【安全圈】研究人员在四分钟内就让 Comet AI 浏览器落入网络钓鱼陷阱](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652074639&idx=3&sn=480a307bc35df52882a0c81f57d63f10&scene=21#wechat_redirect)

[【安全圈】文言文击穿大模型安全防线，顶级模型的全线溃败](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652074602&idx=1&sn=71541cba8e88493809b1ead0467372e1&scene=21#wechat_redirect)

![](https://mmbiz.qpic.cn/mmbiz_gif/aBHpjnrGylgeVsVlL5y1RPJfUdozNyCEft6M27yliapIdNjlcdMaZ4UR4XxnQprGlCg8NH2Hz5Oib5aPIOiaqUicDQ/640?wx_fmt=gif)

![](https://mmbiz.qpic.cn/mmbiz_png/aBHpjnrGylgeVsVlL5y1RPJfUdozNyCEDQIyPYpjfp0XDaaKjeaU6YdFae1iagIvFmFb4djeiahnUy2jBnxkMbaw/640?wx_fmt=png)

**安全圈**

![](https://mmbiz.qpic.cn/mmbiz_gif/aBHpjnrGylgeVsVlL5y1RPJfUdozNyCEft6M27yliapIdNjlcdMaZ4UR4XxnQprGlCg8NH2Hz5Oib5aPIOiaqUicDQ/640?wx_fmt=gif)

←扫码关注我们

**网罗圈内热点 专注网络安全**

**实时资讯一手掌握！**

![](https://mmbiz.qpic.cn/mmbiz_gif/aBHpjnrGylgeVsVlL5y1RPJfUdozNyCE3vpzhuku5s1qibibQjHnY68iciaIGB4zYw1Zbl05GQ3H4hadeLdBpQ9wEA/640?wx_fmt=gif)

**好看你就分享 有用就点个赞**

**支持「****安全圈」就点个三连吧！**

![](https://mmbiz.qpic.cn/mmbiz_gif/aBHpjnrGylgeVsVlL5y1RPJfUdozNyCE3vpzhuku5s1qibibQjHnY68iciaIGB4zYw1Zbl05GQ3H4hadeLdBpQ9wEA/640?wx_fmt=gif)

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/aBHpjnrGylhgCQcCZBwQrSQRLABhjrXviafAj0avc5c69t69K1YymAruIaZWzXPqbGPourlnuu8pfibV0ebgqV9g/0?wx_fmt=png)

安全圈

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/aBHpjnrGylhgCQcCZBwQrSQRLABhjrXviafAj0avc5c69t69K1YymAruIaZWzXPqbGPourlnuu8pfibV0ebgqV9g/0?wx_fmt=png)

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