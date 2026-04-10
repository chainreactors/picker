---
title: 朝鲜黑客组织的分布式运作架构、安全漏洞与加密货币洗钱链路
url: https://mp.weixin.qq.com/s/fbQ0WINl2pb-zkOd9UDb6g
source: Doonsec's feed
date: 2026-04-09
fetch_date: 2026-04-10T04:41:13.662520
---

# 朝鲜黑客组织的分布式运作架构、安全漏洞与加密货币洗钱链路

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/ft6csZH0gNXEPrs8hU7oLHc5AlVV49j0rde6B5W70buqakgRPxsf4DibRA8Qrb1nTJiaJcvt0u6vpibUlQeSfzA7p5o2UOG6p8b9pZrY6tDPl4/0?wx_fmt=jpeg)

# 朝鲜黑客组织的分布式运作架构、安全漏洞与加密货币洗钱链路

原创

助力行业的
助力行业的

李白你好

![]()

在小说阅读器中沉浸阅读

## 事件背景与数据来源

**DPRK IT Workers内部支付服务器泄露事件技术分析：朝鲜黑客组织的分布式运作架构、安全漏洞与加密货币洗钱链路。**

事件核心源于一名DPRK IT工人的设备被**infostealer恶意软件**感染。攻击者（匿名来源）从中提取了大量内部数据，包括：

* IPMsg聊天记录（局域网即时通讯工具，常用于DPRK分布式团队内部协调）；
* 浏览器历史与虚假身份文档；
* 390个账户信息、214条有效聊天记录；
* 加密货币交易流水及支付凭证。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ft6csZH0gNU9edJ6MTFQX1IbyAlKKvRBP4ynmV1dVESj0qYMry12E4WdHuxatA0Q4MusIAroBZv7lN1cSicKnD9opTNHfXqVDlR7uSXicfF14/640?wx_fmt=png&from=appmsg)![](https://mmbiz.qpic.cn/mmbiz_png/ft6csZH0gNWbJiaRlhDlWq4AoHdEyq03raSZKAs5iaY93esPxkfEOlGojOP5yLcMPUotDy0WddpDXialjH4ONYWJefEKSg0zUvickRbuSg9Tb9k/640?wx_fmt=png&from=appmsg)

数据时间跨度为2025年12月至2026年2月（部分延伸至4月）。ZachXBT通过链上追踪与聊天日志交叉验证，构建了完整的组织架构图（交互式可视化已于泄露后下线，但数据已被归档）。该集群每月收入约100万美元，与Chainalysis此前报告的DPRK IT工人整体年收入规模（2024年近8亿美元）高度吻合，但属于“低阶”团伙， sophistication低于AppleJeus或TraderTraitor等高级持久化威胁（APT）组。

**技术要点**：infostealer通常通过钓鱼邮件或供应链攻击植入，窃取浏览器cookie、聊天历史及凭证。本案再次证明，远程办公设备安全是DPRK IT工人体系的薄弱环节——他们依赖Astrill VPN等工具隐藏位置，却未能防范端点威胁。

## 通信与协作基础设施

DPRK IT工人采用典型的“分布式公司”模式，核心通信平台包括：

* **IPMsg**：局域网级即时通讯工具，支持文件传输与群聊。日志显示33名DPRK IT工人在同一网络内实时沟通，讨论任务分配、假身份申请及项目渗透。
* **luckyguys[.]site（WebMsg平台）**：内部“支付汇报平台”，功能类似Discord + 内部CRM。工人上报收入、提交转账凭证，管理员统一确认。平台默认密码为**123456**，且10个用户未修改。该域名在聊天中被反复提及，是整个资金汇报的“大本营”。
* **Slack-like内部群**：用于分享外部情报（如深假求职新闻），并严禁外部链接分享以防泄露。

**技术分析**：默认弱口令+未启用多因素认证（MFA），暴露了典型的“内部系统安全意识缺失”。平台角色字段包含朝鲜姓名、城市编码及分组代号（如710 Command Department指挥部），便于层级管理，却也为情报分析提供了结构化线索。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/ft6csZH0gNXNzWt1j4D4f7DV7DZukQHInr0pj1EMnTVCYtFzaDbWrReQjt0pzlIRBEZfpybiaE2dFholYq89Kxrl1fGfe72envqC3icvHibeDE/640?wx_fmt=jpeg&from=appmsg)

## 组织架构与分工

ZachXBT基于完整数据集绘制了交互式组织架构图（数据范围2025.12–2026.2）：

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/ft6csZH0gNXgU3mkc8mCouBFc4OZVbAsdZQ4v5OaYicHsuNzCNicmqPgcWuyzWkTV8cG3I5tYJxibUzRzR5jYeAtylze3V6dM07wJ2mgfK8VDM/640?wx_fmt=jpeg&from=appmsg)

* **顶层**：PC-1234（Admin）统一管理所有支付账户、凭证发放及确认。
* **指挥部**：710 Command Department负责全局调度。
* **三大分支**（共48个组）：

+ Operational Units（作战单元）：20个组，专注具体任务，最大Unit 1020单组收款92万美元。
+ Regional Groups（地区组）：8个组，按朝鲜国内/海外地区划分。
+ Sector & Industry Groups（行业组）：20个组，渗透不同领域。

已知渗透行业包括：

* Web3/Crypto（核心，因为匿名性高）；
* 传统科技（后端开发、软件工程）；
* 金融科技；
* 国防承包商（高风险）；
* 医疗健康IT、游戏开发。

三个关联公司（Sobaeksu、Saenal、Songkwang）已被OFAC制裁。支付总额按用户/组精确统计，体现高度结构化的“绩效考核”机制。

## 支付与洗钱技术链路

资金流呈现高度一致的模式（2025年11月底起累计超350万美元）：

1. **收入端**：工人以假身份远程接IT项目，薪资以稳定币或加密货币支付。
2. **上报**：通过luckyguys.site向PC-1234汇报，转账至指定钱包（示例：0xb51DA55047Fd899aD08Ab5CE349823664d311998、TSxYS91qoXrJUoMhWaQfMz9p2b7FTw57L3）。

![](https://mmbiz.qpic.cn/mmbiz_jpg/ft6csZH0gNV0CjVxx5koVbA2oHtSQrN83qP0YyckHXdKtX6ibwIDETksZRnSSNwlfet2obYFpGQ2WkRYS5SeJCNqKUiaHMQAbUWag9EqDOeyY/640?wx_fmt=jpeg&from=appmsg)

3. **洗钱端**：

* 加密货币 → 交易所/服务商提现；
* 或通过Payoneer等 fintech平台 → 中国银行账户；
* 部分直接转账至香港地址（真实性待核实）。

4. **出金**：管理员确认后发放凭证，资金最终流入朝鲜（疑似支持核/导弹项目）。

**链上特征**：

* 支付地址与已知DPRK IT工人集群高度关联；
* Tron地址于2025年12月被Tether冻结；
* 转账模式固定，体现“流水线”操作。

**技术亮点**：该体系充分利用加密货币的跨境匿名性与OTC（场外交易）便利性，同时借助中国银行与Payoneer实现法币落地，形成闭环。OFAC 2026年3月制裁记录显示，类似网络2024年已产生近8亿美元收入，本案是其低阶分支的缩影。

### 技能培训与攻击能力

聊天记录显示，管理员于2025年11月至2026年2月向群组分享43份Hex-Rays/IDA Pro培训模块，涵盖：

* 反汇编与反编译；
* 本地/远程调试；
* PE可执行文件解包（示例：“using-ida-debugger-to-unpack-an-hostile-pe-executable”）；
* 其他网络安全主题。

**技术意义**：表明该团伙具备一定逆向工程能力，可用于植入恶意软件或分析目标项目代码。一名成员“Jerry”曾讨论针对GalaChain游戏项目Arcano的攻击（是否执行未知），凸显Web3项目仍是高价值目标。

## 安全漏洞与运营风险

本案暴露多处低阶错误：

* **默认密码123456**：10个账户未改，ZachXBT调查站点故意使用相同密码作为“彩蛋”。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ft6csZH0gNXAe1jRYic7rkDO2lSP1lv3vJDd3jfHLQYJsibQU6hXsTTJV6vx8yOPQqPrOkq8csYQPcC82rOQv8Q0eRg6vzgzD3KiccRruzqatQ/640?wx_fmt=png&from=appmsg)![](https://mmbiz.qpic.cn/sz_mmbiz_png/ft6csZH0gNXenbg9yhPvwOtrUyzQXCnqWh86kDdvibAUcicWpgC5AWLARcNpjfyVzaUKnSMdvRZ3CMs8gvcS5ArsOo9TCHQJ6t4qIhp34ibXmE/640?wx_fmt=png&from=appmsg)

* **内部平台暴露**：luckyguys.site在IPMsg中被直接讨论，未做外部访问控制。
* **端点安全缺失**：依赖infostealer易感染的远程设备。
* **身份伪造**：使用深假、假证件申请职位，但Slack聊天中已讨论相关风险新闻。

ZachXBT指出，该集群 sophistication低于顶级DPRK APT组，留下了“低风险、高回报”的攻击窗口。

## 对加密货币行业的启示

1. **KYC/AML强化**：项目方招聘远程开发者时需加强身份验证（视频面试、设备指纹、背景调查），防范深假与假身份。
2. **链上监控**：定期追踪可疑稳定币流向已知DPRK集群地址，结合Tether等冻结机制。
3. **端点防护**：推广EDR（Endpoint Detection and Response）工具，防范infostealer。
4. **情报共享**：ZachXBT的开源调查模式（含交互式架构图）为行业提供可复制模板。未来可扩展至更多低阶团伙。
5. **政策层面**：OFAC与Chainalysis报告强调，该网络直接资助DPRK武器计划，加密行业需与监管机构加强协作。

## 结论

本次泄露事件以低成本infostealer攻击，完整揭露了一个每月百万美元级的DPRK IT工人支付闭环，展现了“国家支持 + 分布式远程办公 + 加密货币洗钱”的成熟模式。尽管技术 sophistication较低（弱口令、未加密内部平台），但其规模化与隐蔽性仍构成现实威胁。ZachXBT的深度链上+日志分析再次证明，公开情报与社区调查是对抗此类威胁的关键武器。

加密货币行业应以此为鉴：技术创新的同时，必须同步提升安全意识与合规能力。未来ZachXBT计划持续更新investigation.io站点，更多低阶团伙或将被曝光——正如他所言，“威胁行为者正错过一个低风险、高回报的机会”。

相关文章

[朝鲜黑客真牛逼！潜伏六个月，盗走2.85亿，缔造史上最精密的DeFi猎杀行动](https://mp.weixin.qq.com/s?__biz=MzkwMzMwODg2Mw==&mid=2247516360&idx=1&sn=88b1ccb4aa568ecf187589b359edd44a&scene=21#wechat_redirect)

[再次盗取15亿美元加密货币，朝鲜如何培养出世界一流黑客的？](https://mp.weixin.qq.com/s?__biz=MzkwMzMwODg2Mw==&mid=2247510753&idx=1&sn=cf5a2e481c47d3b09ce169b34bbdfaf2&scene=21#wechat_redirect)

## 网络安全情报攻防站

**www.libaisec.com**

综合性的技术交流与资源共享社区

专注于红蓝对抗、攻防渗透、威胁情报、数据泄露

![](https://mmbiz.qpic.cn/mmbiz_jpg/ft6csZH0gNVa5e6f9f04DyDGRKF5uDEcWcxHlcuVVt5WtlibLQCiaFYsvic5sCHGyvSBiaJLdPRKWEHBeUK6iaRQTgdM02MV614NnicQnlL0ibjZzQ/640?wx_fmt=jpeg&from=appmsg)

预览时标签不可点

阅读原文

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/XoIcX2HtlUAuS65pf9u98YWJSdI6kWZ64ziasaVXOFXiabEV2AuCY8yGygtKHicEFVvHnw3bzhsDXBB3DQIiaNhOiaQ/0?wx_fmt=png)

李白你好

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/XoIcX2HtlUAuS65pf9u98YWJSdI6kWZ64ziasaVXOFXiabEV2AuCY8yGygtKHicEFVvHnw3bzhsDXBB3DQIiaNhOiaQ/0?wx_fmt=png)

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