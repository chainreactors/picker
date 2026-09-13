---
title: 【安全圈】黑客把Claude玩疯了：全自动扒光180万安卓App密钥机密
url: https://mp.weixin.qq.com/s/k4o4CiE-UysxfTQ1nP8Idg
source: Doonsec's feed
date: 2026-09-12
fetch_date: 2026-09-13T06:57:36.176481
---

# 【安全圈】黑客把Claude玩疯了：全自动扒光180万安卓App密钥机密

# 【安全圈】黑客把Claude玩疯了：全自动扒光180万安卓App密钥机密

安全圈

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

![](https://mmbiz.qpic.cn/sz_mmbiz_png/aBHpjnrGylgOvEXHviaXu1fO2nLov9bZ055v7s8F6w1DD1I0bx2h3zaOx0Mibd5CngBwwj2nTeEbupw7xpBsx27Q/640?wx_fmt=other&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

**关键词**

黑客

**核心事实：**全球 AI 领军企业 Anthropic 突然公开一份长达 154 页的重磅威胁情报报告，首度披露黑客正在野将 Claude 大模型改造成高度武器化的攻击中枢。黑客组织甚至调动 10 台 AWS 云主机搭建全自动反编译流水线，驱使 Claude 深度逆向扫描了 180 万款真实安卓 App，从中批量掠夺硬编码密钥；更有国家级黑客利用 Claude 实现了后门木马被杀毒软件查杀后“全自动改写免杀重构”。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/sbq02iadgfyE8dNv6qCj35icUjooQoFfHYwqGkQ507GibeRibgK2s1HQRafZUm5hL71InXiamwgZicuX22CdU8DsiaNzTA0STUtELTs16U7oibxKwAE/640?wx_fmt=other&from=appmsg)

## 💥 一、 180 万款 APK 遭工业级逆向：云主机+AI的大规模收割

以往移动应用的安全分析往往受限于人力成本与逆向耗时，而黑客团伙这一次彻底跑通了“大模型规模化批量收割”的新战法。Anthropic 在报告中追踪了一个代号为 **GTG-50014**（法语黑客组织，疑为知名勒索团伙 ShinyHunters 关联方）的攻击集群。

该团伙在 AWS 租用了 10 台高性能 EC2 实例，构建起一套完全无需人工干预的“流水线工厂”：

⚙️ 自动化密钥收割链条还原

① **全网爬取 APK：**自动化脚本从多个主流和第三方安卓市场批量抓取了多达 **180 万个独立 APK 安装包**；

② **解包与语义审计：**结合开源扫描引擎 TruffleHog 与 Claude API，对拆解后的 Java/Kotlin 源代码、资源配置与 native 库进行语义级敏感数据挖掘；

③ **自动去伪存真：**Claude 自动过滤无效测试字符，精准提取云服务 AccessKey、数据库连接串、支付商网关私钥以及内部服务 Token；

④ **情报即时回传：**经校验具有真实登录权限的凭据，第一时间通过自动化机器人推送至黑客的 Telegram 暗网变现频道。

## ⚡ 二、 不只是聊天助手：多智能体（Multi-Agent）与木马自愈

Anthropic 特别强调，黑客对大模型的使用早已脱离了“对话框问答”的初级阶段，而是深入整合为具有高度自主权的协同体系：

**1. 杀软刚告警，AI 已自动重写免杀代码：**
在披露的俄罗斯国家背景黑客 **GTG-20006**（关联知名 APT 组织 Midnight Blizzard / APT29）案例中，该组织建立了一套基于 Claude 的恶意软件自动迭代流程。当其在目标内网部署的 Windows 植入物被防病毒产品以静态签名阻断时，系统立即将告警特征回传，由 Claude 实时重构代码架构、替换混淆手法并重新编译分发，彻底消解了防御方的静态特征封堵能力。

**2. 多智能体（Multi-Agent）闭环自主打靶：**
多个黑产团伙（如 GTG-50020、GTG-50029）直接部署了多智能体工作流。不同 Agent 分别承担外网端口资产测绘、漏洞载荷投递、权限维持与数据渗漏等角色。多个 Agent 在无人类干预的情况下，可在数小时甚至数天内持续并行攻击全球数十家企业目标。

**3. 挖掘出未公开的 0-day 级别逻辑竞争漏洞：**
报告显示，黑客利用 Claude 成功发现了一处此前未被记录的 WordPress 重新安装竞态条件（Race Condition）缺陷，使攻击者能在未授权条件下凭空注入管理员高权账户。

🎯 Anthropic 重点处置黑客团伙画像

▪️ **GTG-50014（ShinyHunters 系）：**操控 10 台 EC2 云主机，滥用 Claude 对 180 万款 APK 进行自动化反编译与机密抽取；

▪️ **GTG-20006（俄系 APT29 关联）：**建立闭环免杀重构流程，针对被查杀木马自动执行源码改写与重编译；

▪️ **GTG-50020（黑产经济组织）：**在 4 天窗口期内密集扫描并针对 30 余家 AI 提供商尝试盗取未公开模型与商业 API Key；

▪️ **GTG-50029（多智能体单兵作战）：**自主部署多 Agent 挖掘 CMS 逻辑漏洞并搭建自动化社工窃密网络。

## 🛡️ 三、 防御者必须面对的残酷现实

Anthropic 此份报告揭示出一个不可逆转的趋势：AI 彻底抹平了高技术门槛 APT 与普通黑客之间的工具鸿沟。当攻击者能够以几美分的算力成本调动大模型并发审计数百万份代码时，以往企业依赖“代码混淆不够好但没人会专门看”的侥幸心理已彻底失效。

▪️ **移动端严禁硬编码任何密钥：**所有云厂商秘钥、三方 API 凭据绝不能随客户端编译打包，必须通过受限后端执行动态签名与鉴权分发；

▪️ **CI/CD 全面部署 Secret 阻断门禁：**在提交阶段引入静态机密扫描，确保一旦出现代码误写即刻阻断合并；

▪️ **转向行为检测与威胁狩猎：**面对 AI 自动改写特征的自愈型恶意代码，仅靠文件 Hash 与简单静态特征已无法立足，防御体系必须加固对父子进程异动、内存注入及出站网络行为的深度监控。

***END***

阅读推荐

[【安全圈】思科防火墙FMC曝满分漏洞：免密直取Root遭勒索攻陷](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652078830&idx=2&sn=552967b4aa41758e08d40d2c71bd56ca&scene=21#wechat_redirect)

[【安全圈】JFrog制品库曝组合漏洞：免密换取Admin凭据篡改依赖](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652078830&idx=3&sn=ae55fabe5ad167e850024e3d3f9b890b&scene=21#wechat_redirect)

[【安全圈】豆包又崩了！！！](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652078814&idx=1&sn=4bb4de8f89d37090d16af701bb3151a7&scene=21#wechat_redirect)

[【安全圈】JumpServer曝高危越权漏洞：普通用户发请求可窃管理员AK](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652078814&idx=2&sn=377865fd1deaae1b0ff7ae47552a4242&scene=21#wechat_redirect)

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