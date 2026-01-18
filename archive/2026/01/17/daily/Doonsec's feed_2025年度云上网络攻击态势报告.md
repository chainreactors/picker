---
title: 2025年度云上网络攻击态势报告
url: https://mp.weixin.qq.com/s/uZyLXvQy19huvb2_IdmJ_Q
source: Doonsec's feed
date: 2026-01-17
fetch_date: 2026-01-18T03:37:18.349235
---

# 2025年度云上网络攻击态势报告

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/VcRPEU1K2ofZibdBG9zeAqhC4uHlHdIzUBnfBssoOaniaPMAOFV3P8Rq39d23BUREcbvibI0fdYicJDydRVX5OnzvA/0?wx_fmt=jpeg)

# 2025年度云上网络攻击态势报告

计算机与网络安全

![]()

在小说阅读器中沉浸阅读

**云上攻击早已进入"后漏洞利用"时代。**

攻击者不再满足于"能打进去"，而是追求"打进去能赚钱"。当我们分析这些入侵记录时，一个残酷的现实浮出水面：**近六成成功入侵目的是挖矿，其它被肉鸡而导致的安全事件、甚至数据被加密勒索也层出不穷**，AI基础设施正进入攻击者的视野。

本报告基于主机侧大量的入侵记录进行深度分析，涵盖 **3万+**个独立攻击源IP，涉及 **137** 个CVE漏洞。

**重要说明：**本报告数据来源于**主机侧入侵检测系统**，记录的是**攻击者命令在目标主机上实际执行**的事件，而非网络安全设备拦截日志或扫描器探测记录。

***年度关键发现：***

***针对AI的攻击工具集***

***正在快速扩张***

从LLM编排到AI Agent，12款AI产品被纳入攻击目标，这是AI安全需要被重视的信号。

![图片1.png](https://mmbiz.qpic.cn/mmbiz_png/OJbMFMZkdelSOSa4kgRRm89jU44nqCZYibsicicnZEZeicqU5sw7rctLHBiaibwPXbibnhD5E5bUk8jxuyRx9kEScfvGg/640?wx_fmt=png&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=0)

其他重要发现：

![图片2.png](https://mmbiz.qpic.cn/mmbiz_png/OJbMFMZkdelSOSa4kgRRm89jU44nqCZYqgCVP0ZTBb168X75NiaXXUc3RTzSicdw2A7wq4OwOHUicYUp0QRo8muUQ/640?wx_fmt=png&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=1)

**0****1**

***漏洞利用态势：谁在“躺枪”？***

### **1.1 年度“最受黑客青睐”的 CVE 漏洞 Top 10**

![图片3.png](https://mmbiz.qpic.cn/mmbiz_png/OJbMFMZkdelSOSa4kgRRm89jU44nqCZYRvZvGm29mGxs1YmUGic0m2FSjUgTDAkovVCaHlYEMeI6CmtgstgFHCQ/640?wx_fmt=png&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=2)

**深度洞察：**

**React Server Components****漏洞的“****屠榜”****现象值得深思。**这个2025年新披露的漏洞，单枪匹马贡献了超过54%的成功入侵。这揭示了一个危险趋势：**现代前端框架的服务端渲染能力，正在成为新的攻击面****。** 当开发者享受SSR带来的性能红利时，攻击者也在享受RCE带来的"入侵红利"。

**老旧漏洞的"****长尾效应"****同样值得警惕****。**数据显示，2019年甚至更早披露的漏洞至今仍被持续利用。漏洞一旦被武器化，就会长期存在于攻击者的工具库中，成为自动化扫描的"标配"——修复窗口不是几个月，而是永远。

### **1.2 漏洞新旧程度分析：新旧漏洞的"双杀"**

下图展示的是**被利用漏洞的****CVE****披露年份**分布，反映攻击者对新旧漏洞的利用偏好。

![图片4.png](https://mmbiz.qpic.cn/mmbiz_png/OJbMFMZkdelSOSa4kgRRm89jU44nqCZYLHNcHAIPh5kWibh2FHZJphl5cXWyGltr1AFyenWU5tC2UXjibSU4ucFA/640?wx_fmt=png&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=3)

![图片5.png](https://mmbiz.qpic.cn/mmbiz_png/OJbMFMZkdelSOSa4kgRRm89jU44nqCZYpwpgRrbxNm3Rm46KNjSVSC1FZn3dkIic9MF5WDqU34J2sz23MfBnjFA/640?wx_fmt=png&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=4)

**深度洞察：**

**2025****年新漏洞占据56%****以上的入侵量，这是一个危险信号****。** 它意味着：

* **攻击者的武器化速度已经超过了企业的修复速度。**

* “**等等看”****的补丁策略已经彻底失效。**

* **漏洞披露后的24-48****小时，就是生死时速。**

但同时，**老旧漏洞的“****长尾效应”****同样不容忽视**，2019年甚至更早披露的漏洞至今仍被持续利用，揭示了另一个问题：“**僵尸资产”****正在成为企业安全的最大盲区**。这些系统可能早已被遗忘，但攻击者没有忘记它们。

**0****2**

## ***攻击来源分析：谁在攻击你？***

**2.1 应重点关注的攻击源IP**

**![图片6.png](https://mmbiz.qpic.cn/mmbiz_png/OJbMFMZkdelSOSa4kgRRm89jU44nqCZYxiaD8ckdsdiaaZLW6oqY4k2EoRLjbhVmxNQibZmUpylib5a5EFwuKuvfRw/640?wx_fmt=png&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=5)**

**深度洞察：**

**荷兰、波兰、芬兰的高排名更值得关注****。** 这些国家的VPS服务商是攻击者搭建C2基础设施的热门选择。

**内网攻击占1.7%****，这是横向移动的信号****。** 一旦攻击者突破边界，内网就是“自助餐厅”。

**0****3**

***攻击类型分析：攻击者想要什么？***

### **3.1 攻击目的分布**

**![图片7.png](https://mmbiz.qpic.cn/mmbiz_png/OJbMFMZkdelSOSa4kgRRm89jU44nqCZYNF5lgyukUDmAQyxibiahIjNO3VPck7ObN3EAZZRwQP9ibEkFszWicYricVg/640?wx_fmt=png&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=6)**

**数据说明**：为更清晰地洞察攻击者的核心动机，本章节聚焦于意图明确的攻击记录进行分析。

![图片8.png](https://mmbiz.qpic.cn/mmbiz_png/OJbMFMZkdelSOSa4kgRRm89jU44nqCZY3u77asFcOtiafc1a4BTs5cGgV362PuhiaOXpZbrY8nGlAicZnjrcYpNbQ/640?wx_fmt=png&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=7)

**深度洞察：**

**挖矿攻击占据近六成，这是“****后漏洞利用”****时代的标志性特征。**

为什么是挖矿？因为它是**最稳定的变现方式**：

* **低风险**：不需要窃取数据，不触发数据泄露告警

* **高收益**：7x24小时挖矿，算力即金钱

* **可规模化**：一套脚本打天下，批量部署

* **难追踪**：加密货币的匿名性提供天然保护

**33%****的“****验证”****类攻击同样值得警惕****。** 这意味着攻击者在"踩点"——今天的验证，就是明天的入侵。

### **3.2 挖矿攻击深度分析**

挖矿攻击是2025年云上最主要的威胁类型，占意图明确攻击的 **58.1%**。

**挖矿攻击利用的主要漏洞：**

![图片9.png](https://mmbiz.qpic.cn/mmbiz_png/OJbMFMZkdelSOSa4kgRRm89jU44nqCZYLhm8JkfHUhMhrUa0J6Ja6bmeCBOk5rWTA1rA4H7XwGXI3EQAKqRhJA/640?wx_fmt=png&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=8)

**深度洞察：**

**XXL-JOB****的高排名揭示了一个被忽视的风险：任务调度系统****。** 这类系统通常：

* 部署在内网，安全意识薄弱；

* 使用默认配置，accessToken形同虚设；

* 拥有执行任意代码的“合法”能力。

**Langflow****的出现则预示着新的攻击趋势：AI****工具链正在成为攻击目标****。** 随着企业大规模部署AI应用，这类漏洞的影响只会越来越大。

**0****4**

***攻击工具分析：攻击者的“武器库”***

### **4.1 挖矿工具生态**

**深度洞察：**

**挖矿攻击的“****平民化”****趋势****。**开源挖矿工具（如 XMRig）和公开的漏洞利用代码大幅降低了攻击门槛。攻击者的逻辑很简单：

* 下载开源 XMRig；

* 配置矿池地址；

* 部署到被控主机；

* 坐等收益。

这意味着：

* **低技术门槛**：不需要恶意软件开发能力，下载即用；

* **攻击者群体扩大**：从专业黑产团伙扩展到“脚本小子”；

* **攻击量级上升**：工具易得导致攻击频次大幅增加。

**云原生环境面临定向威胁****。**我们观察到 Kinsing 等专门针对云原生环境的攻击工具，它们擅长：

* 利用容器逃逸；

* 攻击 Kubernetes 集群；

* 横向移动到其他容器。

**0****5**

***时间趋势分析：攻击的******“******节奏******”***

### **5.1 月度攻击趋势**

![图片10.png](https://mmbiz.qpic.cn/mmbiz_png/OJbMFMZkdelSOSa4kgRRm89jU44nqCZYG9SxDWVticpicM4Aj8TOiaMic4ZbG72f16vS4EYrlYd0AVpUFDBF5KK08w/640?wx_fmt=png&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=9)

**深度洞察：**

**12****月的3177%****增长不是异常，是“****必然”****。** 这个数字背后是多重因素的叠加：

* **React Server Components****漏洞的闪电武器化：**这个漏洞在12月初被披露后，攻击者在极短时间内完成了武器化和大规模利用；

* **漏洞利用的“****窗口期效应”****：**新漏洞披露后的头几周是攻击者的黄金窗口，大量未修复系统成为目标

**“平静”****的月份也不平静。** 7-11月看似攻击量较低（月均约12,000次），但每月上万次的成功入侵，意味着**每天都有****300-400****次恶意命令在云上系统被实际执行**。

### **5.2 星期分布**

![图片11.png](https://mmbiz.qpic.cn/mmbiz_png/OJbMFMZkdelSOSa4kgRRm89jU44nqCZYAhicDMibh9r8GBWlB0ACiaV72bvaGLUqg9aALY2o3wayL2MBDaxHmcnoA/640?wx_fmt=png&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=10)

**深度洞察：**

**攻击在工作日和周末分布相对均匀，这是自动化攻击的典型特征****。**攻击者不需要"上班"，脚本7x24小时运行。

**周二的峰值可能与工作周期有关****。**周二是工作周的第二天，企业系统活跃度高，新部署的应用和服务较多，暴露面相应增加，为自动化扫描提供了更多目标。

**0****6**

***攻击技术分析：攻击者的******“工具箱”***

### **6.1 常见攻击命令模式**

**黑吃黑：服务器沦为攻击者的“****修罗场”**

![图片12.png](https://mmbiz.qpic.cn/mmbiz_png/OJbMFMZkdelSOSa4kgRRm89jU44nqCZYnVgxpicdGduMv4VpxIry7bhSnCtoMQyTXcXcSHDzh6WciatRrSEJvSFA/640?wx_fmt=png&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=11)

![更新2.png](https://mmbiz.qpic.cn/mmbiz_png/OJbMFMZkdelSOSa4kgRRm89jU44nqCZYKfpMBhsXkRXkyx8jaVt9J3kMtXs5PkYQ1lSfkZTLI8F0j1QjPUHA1g/640?wx_fmt=png&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=12)

**深度洞察：**

**pipe\_chain****（管道链）的高频使用揭示了攻击者的“****反检测”****意识****。** 通过管道将多个命令串联，可以：

* 避免在命令历史中留下完整记录；

* 绕过基于单一命令的检测规则；

* 实现“无文件”攻击。

**rm\_files****和pkill\_process****的高频出现说明了一个有趣的现象：攻击者之间的“****内卷”****。** 当一台服务器被多个攻击者盯上时，后来者会：

* 杀死前任的挖矿进程；

* 删除前任的恶意文件；

* 部署自己的挖矿程序。

**这是一场“****矿工”****之间的战争，而受害者的服务器就是战场。**

### **6.2 下载基础设施**

**Top 6****恶意下载域名：**

⚠️ **关于合法平台滥用的说明**

下表中出现的**github.com**、**gist.githubusercontent.com**、**raw.githubusercontent.com**是合法的代码托管平台，被攻击者滥用来分发恶意载荷。这些域名本身不是恶意的，**不建议直接封禁**，应采用URL级别的精细过滤策略。

![图片](https://mmbiz.qpic.cn/mmbiz_png/OJbMFMZkdel5ql9XpXzYya4PgsYXKjV1icDRYPSSC7CDAq4z3djS3ibpgayGoPXNRwlDAxODSKSsaZ5TUiam73tfg/640?wx_fmt=png&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=13)

**深度洞察：**

**攻击者正在大规模滥用合法平台****。** GitHub、Gist这些“白名单”域名成为恶意载荷的“避风港”：

* 企业防火墙通常不会拦截GitHub

* CDN加速让下载更快

* 即使被举报，换个账号继续

**download.c3pool.org****的高排名说明攻击者甚至不需要自建基础设施****。**直接从矿池官网下载挖矿程序，简单粗暴但有效。

**0****7**

***IOC 威胁情报***

### **7.1 高危IP地址 (部分)**

以下IP在2025年度攻击中高频出现，建议加入黑名单：

```
103.43.8.198
185.191.127.110
13.229.128.172
154.16.112.232
95.214.55.47
其它 （联系腾讯云安全团队，获取更全信息）
```

**7.2 恶意域名 (部分)**

以下域名用于恶意载荷分发，建议加入DNS黑名单：

```
ellison.st
download.c3pool.org
repositorylinux.xyz
oceanic-node.su
niggabin.net
其它 （联系腾讯云安全团队，获取更全信息）
```

**注意：**gist.githubusercontent.com、github.com、raw.githubusercontent.com虽然被滥用，但不建议直接封禁，应采用更精细的URL级别过滤。

**0****8**

***AI基础设施：攻击者的新战场***

在过去的2025年，AI迎来了大爆发，大模型开始在各行各业中落地生根，构建AI-SPM（AI  Security Posture Management‌ 人工智能安全态势管理系统），持续监控和评估人工智能系统的安全风险变得尤为重要。

### **8.1 Top5 检测漏洞的AI组件**

|  |
| --- |
| **组件** |
| mlflow |
| gradio |
| langchain |
| clickhouse |
| Chuanhugpt |
| …. |

**深度洞察：**

* MLflow 等模型管理工具的风险暴露度极高，这直接威胁着云上 AI 资产的完整性。

* MLflow、Gradio 与 LangChain分别卡位了 AI 的模型管理（MLflow）、交互入口（Gradio）与应用编排（LangChain）。在实际攻防中，这三类组件一旦失守，意味着攻击者可以直接窃取模型资产、篡改交互逻辑或通过编排层穿透内网。

### **8.2 Top5 漏洞的类型**

|  |
| --- |
| 漏洞类型 |
| 代码执行 (Code Execution) |
| 目录遍历 (Directory Traversal) |
| 服务器端请求伪造 (SSRF) |
| 跨站脚本 (XSS) |
| 信息泄漏 (Information Leakage) |
| …. |

* 在AI环境中，不仅要关注数量，更要关注漏洞的破坏力。相比于传统Web的轻微漏洞，AI场景下的RCE（代码执行）和目录遍历往往能造成毁灭性后果（如 GPU 挖矿、训练集泄露），这意味着攻击者一旦得手，即可直接获取容器宿主机权限，实现容器逃逸。

* SSRF漏洞的高发，表明黑客正在利用AI代理作为跳板，扫描和攻击企业云环境内部的隔离区。

### **8.3 攻击面持续扩张**...