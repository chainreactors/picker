---
title: 【安全圈】单月1130起勒索，3.11亿条数据被挂牌
url: https://mp.weixin.qq.com/s/FsGcKbXLdUXcvqx7LfIq3w
source: Doonsec's feed
date: 2026-11-22
fetch_date: 2026-11-23T10:02:21.201533
---

# 【安全圈】单月1130起勒索，3.11亿条数据被挂牌

# 【安全圈】单月1130起勒索，3.11亿条数据被挂牌

安全圈
安全圈

安全圈

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

![](https://mmbiz.qpic.cn/sz_mmbiz_png/aBHpjnrGylgOvEXHviaXu1fO2nLov9bZ055v7s8F6w1DD1I0bx2h3zaOx0Mibd5CngBwwj2nTeEbupw7xpBsx27Q/640?wx_fmt=other&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

**关键词**

数据泄露·暗网交易

数世咨询联合零零信安发布的《全球数据泄露态势月度报告（2026年10月）》给出了一个不太舒服的结论：**数据泄露已经不再是"某家公司出了事"，而是一条稳定运转的产业链。**

这份报告基于 0.zone 安全开源情报系统，监控范围覆盖明网、深网、暗网与匿名社群，合计约 10 万个威胁源。换句话说，下面的数字不是抽样推测，而是从暗网交易平台和匿名社群里直接扒下来的"挂牌信息"。

先看总量。

* 10 月监控到的**高价值买卖情报 11,834 份**
* 美国是泄露第一大国，**1,899 份**，其后是法国、印度、中国、意大利
* 有明确行业属性的数据约占 **97%**，集中在金融、信息与互联网、党政军与社会、制造、电商
* 体量维度更夸张：包含数份**数十亿级三要素日志**、数十份**数十亿级二要素数据**、**十亿条个人邮箱与电话**；全球整体泄露量在**数百亿行以上**

需要说明的是，报告明确标注：所有数据均为暗网卖家**宣称**内容，真实性与实际泄露范围未经权威核实，不构成事实认定。这一点很重要——卖家夸大是常态。但即便打个对折，量级依然惊人。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/sbq02iadgfyFibia2vXxHbts4NWCdVWdz3Ws6IbMWLlMPRYRhQ8IpWr002JGxOHryianME3KNsa7CH5bbAP7bAdKzGG38Kh3SibuRQqbWvZC9icdU/640?from=appmsg)

## 十起抽样事件，五起指向中国

报告抽取了 10 起典型事件做细节分析，其中 5 起涉及中国主体，且**字段颗粒度值得警惕**。

**中国某酒店集团，约 3.11 亿条记录。** 字段包含 user\_id、姓名、联系电话、街道地址、城市、注册状态、最近预订号、最近酒店代码与品牌、最近入住与离店时间、预订次数、完成入住次数、完成间夜数。

**中国某旅行服务公司。** 字段包含行程数量、酒店预订数、火车票数、机票数，以及常用出发城市。

**中国某智能电动汽车公司。** 字段包含车辆 ID、车型、电池容量（kWh）、充电次数、换电次数、累计电量（Wh）。

**中国某防务 AI 公司。** 约 2.85GB 压缩数据，字段包含**源代码**与 **special government projects**。

**\*国**外国人管理后端。**26 万余条住宿登记记录（涉及约 21.6 万个唯一证件号）、27,254 张扫描件（约 1.47GB），字段含护照资料页、签证、人像，以及**带密码哈希的运营账号\*\*。

这五条放在一起看，能读出一个共性：**字段命名呈现出典型的业务库直出特征**。`last_reservation_id`、`primary_battery_capacity_kwh`、`swap_session_count`、`operator accounts with password hashes`——这些不是撞库拼凑出来的"二要素"，而是从生产库导出的整表。这意味着泄露源头大概率是**数据库权限失守、备份文件外流或供应链环节**，而不是外围被拖库。

对防守方来说，这个区别决定了排查方向完全不同。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/sbq02iadgfyHKncSwf3DslG7Bc81rCOyomayzkHD8kMKgGjMTofudhwKIYx67viae49eRicGDicicKNUiaWYdcbJnsFPD396udqBAnqGPopxT8kYk/640?from=appmsg)

## 勒索侧：84 个组织，1130 起事件

10 月全球有勒索发布行为的商业黑客组织共 **84 个**，公开勒索事件 **1,130 件**。TOP 30 组织发布了其中的 **77.01%**，集中度相当高。

拉长看趋势：虽然月度波动明显，10 月较 9 月有所回落，但整体活跃度趋于稳定，**10 月的活跃度已达到 2025 年 11 月的 156.3%**。报告将此归因于 TI+AI（开源情报 + 人工智能自动化）攻击方式成熟——自 WormGPT、FraudGPT 出现后，黑客组织持续向**精英化、小型化、自动化**演进，组织数量随之分裂增长。

本期重点介绍的 **n0n** 是典型样本。该组织 2026 年 9 月中旬才公开现身，运营方式封闭、团队规模小，初期以纯数据窃取与公开泄露为主，后续出现加密器开发迹象，加密文件追加 `.n0n` 扩展名，并在 Tor 泄露站点按受害者定制勒索说明与倒计时。

其初始访问手法值得单独划线：**大量依赖窃取或弱凭证**——凭证填充、会话令牌、邮箱与一次性验证码，**未见明确的大规模漏洞利用**。公开情报还显示其使用 AI 编程辅助工具生成与调试攻击脚本。

截至 11 月中旬，n0n 声称的受害者约 120 至 220 个（各平台口径不一），覆盖 40 余国，中国在列。2026 年 10 月 12 日，该组织一次性点名约 38 家全球港口、码头与航运企业，跨 18 个国家。

![](https://mmbiz.qpic.cn/mmbiz_jpg/sbq02iadgfyH11vSutZ63QP3TexMiauutq4YGJgh6iaO4FCoMicVkGpusaCiaUokXzDpsPEjNkO46TqSqdskjQJhyhldRprcicmL3CQMv8cYMNRbM/640?from=appmsg)

## 匿名社群：每月约 10 万条我国样例数据

10 月监控到匿名社交社群情报 **49,751,229 条**，提供有效泄露样例下载 **7,127 份**。涉及我国的内容覆盖快递、银行、学生、就医、打车、退休人员、医护、车主、网贷、投资等信息。

报告给出了一个估算：每份样例提供数十至数百条不等，**仅匿名社群每月发布的我国样例数据就有约 10 万条，全数据量估算在 1000 万条以上**。

另一个细节：10 月匿名社交软件活跃用户中，以"86"开头的手机号共发信 **5,858 条**。这类软件不受实名监管，发信主体的目的性需要单独评估。

## 运维视角：这份报告该怎么用

把报告当"新闻"看，价值有限；当"自查清单"看，能直接产出动作。

1. **先做字段级盘点，而不是表级盘点。**

   报告里最有价值的信息是字段名。请核对自家核心库是否存在"最近一次入住/消费/充电"这类冗余字段——它们把用户行为时间线完整暴露，一旦整表外流，等于交出一份行为画像。
2. **把"带密码哈希的运营账号"当高危项。**

   外国人管理后端那条里，`operator accounts with password hashes` 与业务数据同库同表，这是权限设计问题。运营账号应独立库、独立认证域。
3. **按"凭证优先"重排防御权重。**

   n0n 没有用 0day 就打进去了，靠的是凭证填充、会话令牌与邮箱验证码。检查三件事：会话令牌是否有失效策略、邮箱验证码是否可被转发、是否存在跨系统的密码复用。
4. **第三方与供应链清单要落到"数据流向"。**

   3.11 亿条酒店记录、38 家港口同时被点名，共同指向供应商/中介环节的集中泄露。清单不止要列供应商名字，还要列"他们把数据放在哪、谁能导全表"。
5. **暗网监控关键词至少覆盖三类：**

   企业域名、品牌中英文名、高管与 DBA 邮箱。报告中的 10 万威胁源口径可以作为选型参照。
6. **对已公开的行业性泄露，做"假设已泄露"演练。**

   酒店、出行、车企这三类数据有强关联性（手机号 + 行程 + 车辆），撞库风险远高于单一数据源，应评估账号体系的异地/异设备登录策略。

最后提醒一句：报告中的数据均为卖家宣称，**不要直接引用为事实向外通报**。但它指出的字段结构、攻击路径与组织行为模式，是可以直接用于加固的。

***END***

阅读推荐

[【安全圈】Linux KVM曝高危逃逸漏洞：虚机跨租户直读宿主机127GB内存](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652079967&idx=1&sn=38dfa6a339d62a690035a68d6f9dad4c&scene=21#wechat_redirect)

[【安全圈】黑客部署自主AI智能体：11分钟自挖0day攻陷服务器夺Root](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652079967&idx=2&sn=85167f3d14ddd041423b52b5fed14503&scene=21#wechat_redirect)

[【安全圈】安卓恶意框架Bazuka曝光：截屏假锁屏掩护盗窃集成AI评分](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652079967&idx=3&sn=97d432e3da143b3dec3677290d6a03eb&scene=21#wechat_redirect)

[【安全圈】群晖DSM曝9.8分严重漏洞](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652079944&idx=1&sn=5b3509c80b236854f9a85bd7dcd0cd3e&scene=21#wechat_redirect)

[【安全圈】VMware曝9.8分零日漏洞](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652079944&idx=2&sn=169d2011f57187ae08f15408372fdc78&scene=21#wechat_redirect)

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

阅读原文

不喜欢

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
推荐
，轻点两下取消推荐
分享
留言
收藏
听过