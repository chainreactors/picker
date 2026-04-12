---
title: 构建自己的实时AI情报态势系统
url: https://mp.weixin.qq.com/s/KhOB5d6oj7wHOm-4_9d_TQ
source: Doonsec's feed
date: 2026-04-11
fetch_date: 2026-04-12T04:44:40.053377
---

# 构建自己的实时AI情报态势系统

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/TRfiawmTBsXY8pcWljUus2fMmuWLicZzN8QcEt9ezzgnQFxFGA7nLhmiarO3rzkdLlhrHgfd4CleYwlQpiaB6hCJbOibQxDyqZXKBFGgxAtdaXQg/0?wx_fmt=jpeg)

# 构建自己的实时AI情报态势系统

原创

少钧
少钧

OSINT情报世界

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

****![](https://mmbiz.qpic.cn/mmbiz_png/TRfiawmTBsXa3p1DR5vwbJUVpSuryx3ZZLN2ORN8BWhmo0jtAlGUichKWzic2jqcNnoI6nWcMzevef6bicljZstWbNhmfSquPfGI882ag1JnxzY/640?wx_fmt=png&from=appmsg)

账号调整通知：由于原公众号“开源情报俱乐部”无法使用，后续所有境外组织机构及OSINT相关内容改为此号分享。**

**培训通知：**2026年5月网络情报分析实战技能培训与CISAW认证时间为5月18-5月22日。需要系统化提升OSINT实战技能的朋友请添加微信号（osintclub007）咨询详细课程内容与安排。**

---

在开源情报（OSINT）领域，分析师面临的最大挑战不再是“缺乏数据”，而是“信息过载”与“信源碎片化”。SitDeck的出现，标志着情报工作模式从“被动检索”向“主动态势感知”的跨代跃升。

### **产品定位：情报流的“中央调度器”**

SitDeck不仅仅是一个数据查看器，它是一个集成了180+实时数据源、65+专业地理图层以及高度可定制AI逻辑的集成情报环境。

![](https://mmbiz.qpic.cn/mmbiz_jpg/TRfiawmTBsXbaiaUKdPko0QmjkLFS2mXx3o9QAtCkwOvergWbeq1HW0zT55QTCvxCYwJQwic1z7v5DsWCU1VHvvu3pJSQLXIFJMtLibB3BpXuIo/640?wx_fmt=jpeg&from=appmsg)

对于OSINT分析师而言，它的核心价值在于：将分散在Telegram、卫星监测、海事雷达、网络安全预警中的杂乱信号，聚合到一个具备逻辑关联的单一视图中。

### **核心功能特色：四大技术支柱**

**1.动态仪表盘架构**

SitDeck采用了类似“乐高”的组件化设计：

**55+智能组件：**涵盖了社交媒体流、新闻聚合、实时天气、地震波形、航班追踪、制裁名单等。

**一键式情报舱：**针对特定的垂直领域（如“乌俄冲突”、“红海航行安全”、“全球网络攻击监测”），提供专家级预设模版。分析师无需从零搭建，即可获得职业级的监控能力。

#### **2. 全球地理空间透视**

SitDeck的地图引擎集成了超过65个交互式图层，其颗粒度令人惊叹：

**军事与冲突图层：**实时显示交战区、导弹轨迹预测、临时禁飞区。

**基础设施监控：**全球电网、核电站状态、海底光缆节点及港口拥堵情况。

**自然灾害预警：**USGS地震监测、NOAA飓风路径、极光及空间天气影响。

#### **3.180+深度信源集成**

SitDeck解决了分析师维护数百个API密钥的痛苦。它内置了：

**冲突数据：**ACLED、Handala泄露点位、Liveuamap等。

**海事/航空：**AIS船只追踪、ADSB飞行数据、港口风险评级。

**安全与合规：**OFAC制裁名单、CISA漏洞预警、勒索软件受害者监控。

#### **4.AI情报大脑**

这是SitDeck区别于传统看板的“护城河”：

**AI分析师 (实时问答)：**分析师可以用自然语言提问（如：“对比过去48小时内伊朗境内的火情与泄露的GPS坐标是否重合”），AI会跨源检索并输出逻辑研判。

**自动生成情势报告：**AI定期对关注区域进行扫描，生成结构化的PDF简报，极大缩短了从搜集到分发的链路。

### **OSINT分析师如何构建自己的情报系统？**

以下为构建情报阵地的基本步骤：

**第一步：定义你的“情报任务”**

案例A：地缘政治监测。加载“冲突图层”+“社交媒体热词”+“卫星火情监测”。

案例B：企业风控与尽职调查。加载“制裁名单”+“网络泄露预警”+“全球新闻负面监测”。

**第二步：配置实时告警**

在SitDeck中设定阈值。例如：当特定港口的滞留船只超过平均值30%，或某个Telegram 频道出现特定“资产代号”时，系统通过Webhook或邮件即时推送。

**第三步：执行“信源对账”**

利用仪表盘的多维特性，当一个数据源（如X平台）爆出消息时，立即在同一界面的另一个组件（如海事雷达或卫星云图）中进行物理验证，实现交叉验证。

### **为什么OSINT分析师必须拥有它？**

**降本增效：**将原来需要3-4小时的例行搜集工作缩短至5分钟，让分析师专注于“研判”而非“搬运”。

**降低门槛：**无需编写代码，通过拖拽即可调用复杂的地理信息和数据API。

**实时反应：**在突发事件（如2026年美国对伊朗的“史诗狂怒”行动）中，秒级的态势更新是获取竞争优势的关键。

**隐私建议：**虽然SitDeck宣称隐私优先，但作为在线工具，在查询高度敏感的目标名称时，建议使用代号。

**免费vs付费：**Hobbyist计划（$0）已经开放了绝大部分组件和地图层，非常适合独立OSINT调查员作为常驻监控工具；对于需要高频、大批量AI任务的机构，才建议考虑付费版。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/TRfiawmTBsXYr051Ad5nxkGmvOR8IDBd0MeuxbvEvibO6GA2dz8etyqicPBE3LKWPlzZZISv8JicZQnonDALgtoMS3VdlhqibCNh9XiacI4pibHl9A/640?wx_fmt=png&from=appmsg)

SitDeck的核心并非取代分析师的思考，而是为分析师提供了一个‘认知增强外骨架’。它将地理坐标、时间线和语义信息在三维空间内完成解构，使得OSINT调查从‘碎片拼接’变成了‘逻辑拼图’。”

如果你正在寻找一个能承载你所有情报梦想的指挥中心，SitDeck或许是目前2026年最接近“科幻电影情报界面”的生产力工具。

网址：https://sitdeck.com/

**知识星球**

由于之前公众号及知识星球的许多深度调查文章无法查看，后续境外各种组织机构的详细内容报告都存放于知识星球**“OSINT世界”**

![](https://mmbiz.qpic.cn/mmbiz_jpg/TRfiawmTBsXY2iaqWIibUxxOXylcGibWh0LcANNUiaoBJwecVwR5EPgBAY7YsZTNqnicOutxqKfIKM1icnZEVOsDicPQ8QsbFOsSkdYTttMTutHTY0M/640?wx_fmt=jpeg&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/TRfiawmTBsXa3p1DR5vwbJUVpSuryx3ZZLN2ORN8BWhmo0jtAlGUichKWzic2jqcNnoI6nWcMzevef6bicljZstWbNhmfSquPfGI882ag1JnxzY/640?wx_fmt=png&from=appmsg)

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/sz_mmbiz_png/TRfiawmTBsXZ0IvlgnKW3s3up9hJnUrwLDtwr0Z4Vn5NL0rAW0Frcq9fzrJJdeEd6iaW2JQWLRYbGIZRYJ2b1x50icOcphd6p6Zaz9icb7dJyVI/0?wx_fmt=png)

OSINT情报世界

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/TRfiawmTBsXZ0IvlgnKW3s3up9hJnUrwLDtwr0Z4Vn5NL0rAW0Frcq9fzrJJdeEd6iaW2JQWLRYbGIZRYJ2b1x50icOcphd6p6Zaz9icb7dJyVI/0?wx_fmt=png)

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