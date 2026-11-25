---
title: 【安全圈】OpenAI与思科推Shirudo：AI写eBPF实现零停机热阻断
url: https://mp.weixin.qq.com/s/ZA33GrfkXNARGU8LJ4EtLA
source: Doonsec's feed
date: 2026-11-24
fetch_date: 2026-11-25T10:39:52.545514
---

# 【安全圈】OpenAI与思科推Shirudo：AI写eBPF实现零停机热阻断

# 【安全圈】OpenAI与思科推Shirudo：AI写eBPF实现零停机热阻断

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

AI

**核心事实**：OpenAI 与思科（Cisco）宣布联合开源 Linux 运行时自卫防御项目 **Shirudo**（日文“盾”之意）。该项目专为应对 AI 时代“负漏洞窗口期”而设计，允许 AI 智能体在操作系统内核层动态编写专用的 eBPF 过滤逻辑，在无需重启应用进程、不中断对外业务的前提下，实现高危漏洞利用的毫秒级热阻断。

![](https://mmbiz.qpic.cn/mmbiz_jpg/sbq02iadgfyGJLY5Y6qicKubNCt17tJRWaP8A4GzRGzH7SA7G7CiartMZlCyzM5HOk1xjiaaEq4QJM3jwq4L1y3wX93t6eHclytz9ZpORKhxtKA/640?wx_fmt=other&from=appmsg)

在传统漏洞处置链条中，一个基础库或内核漏洞从被发现到上游发布修复补丁、下游发行版集成、运维团队排期测试再到最终重启服务上线，通常需要数周甚至数月。而当前大语言模型具备极强的代码逆向与漏洞挖掘能力，使得新漏洞从公开到出现自动化在野利用的耗时甚至短于补丁发布时间。Shirudo 的核心目标，是在官方二进制补丁就绪前，为生产系统插入一道可热插拔的安全防护垫。

## 🔍 技术架构：基于 Tetragon 与 eBPF 的无损内核拦截

Shirudo 构建在思科 Isovalent 旗下的开源内核安全平台 Tetragon 之上，深度利用了 Linux eBPF（扩展伯克利数据包过滤器）的高性能沙箱虚拟机机制：

* **免重启代码注入**

  ：eBPF 允许在不重新编译内核、不加载外部专有驱动模块且无需重启宿主机的情况下，直接挂载内核探测点（kprobe、tracepoint）或安全模块勾子（LSM）。
* **针对性微型护盾（Shield）**

  ：防御智能体接收到漏洞信息或威胁情报后，定位易受攻击的底层函数路径，生成专一微型的 eBPF 过滤规则，仅阻断符合特定异常调用模式的载荷，正常业务请求不受任何阻滞。
* **OCI 制品与硬件签名分发**

  ：生成的防御规则被打包为标准化的 `.bee` 制品包，通过兼容 OCI 标准的容器镜像仓库统一发布。目标服务器的 Shirudo Agent 拉取该包后，利用 TPM（可信平台模块）硬件根校验数字签名，严防防护程序本身被恶意投毒。

## 💥 实测验证：拦截 Elasticsearch 在线攻防漏洞

OpenAI 与思科在对照实验环境中演示了真实业务防护效果：

* **攻击场景设定**

  ：针对持续对外提供查询服务的 Elasticsearch 生产集群，模拟发起远程代码执行（RCE）渗透利用。
* **智能体动态响应**

  ：Codex 驱动的防御 Agent 分析漏洞签名与利用链条后，在操作机自动生成了一段针对性的 eBPF Shield 代码。
* **无损热阻断结果**

  ：Shield 被热加载到运行节点后，成功截断所有非法的类加载与子进程派生尝试，同时 Elasticsearch 进程的 PID 未发生改变，TCP 现有长连接未被重置，客户端检索吞吐量维持正常基准。

## 🛡️ 闭环风控流程：从只读观察到自动退场

为了防止 AI 编写的防御逻辑产生业务副作用或误杀关键交易，Shirudo 规定了严格的状态晋升生命周期：

**阶段一：静态合规与隔离验证**
编写的 eBPF 规则必须先通过 Linux 内核内置 Verifier 验证，确保没有无限循环、非法内存越界及死锁风险。

**阶段二：影子观察（Dry Run）**
规则初始加载时不直接执行拦截（DROP），而是仅记录告警日志，与生产真实业务请求流量做特征比对，评估误报率。

**阶段三：管理员审批转入强制阻断**
指标核验通过后，经安全运维团队确认或根据策略自动升级为 Active Blocking 状态，开始在内核入口掐断恶意 Payload。

**阶段四：正式补丁到达后自动卸载**
当底层应用在后续例行维护窗口完成二进制补丁更新后，Shirudo 自动识别对应漏洞修复状态，静默卸载对应的临时 eBPF 挂钩，消除任何多余的内核开销。

***END***

阅读推荐

[【安全圈】英伟达热修复驱动翻车：闲置9小时仍偷写36GB日志](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652080032&idx=1&sn=763967cc27dfc41b9938316226fa2d69&scene=21#wechat_redirect)

[【安全圈】AI Agent自主挖掘零日漏洞：11分钟拿下医疗服务器](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652080032&idx=2&sn=0979762f073753e029a45dc071f89129&scene=21#wechat_redirect)

[【安全圈】CISA紧急预警：VMware与Cisco等四枚高危遭在野利用](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652080032&idx=3&sn=cd19a06b8fed5919a4de9fec4b756e3a&scene=21#wechat_redirect)

[【安全圈】单月1130起勒索，3.11亿条数据被挂牌](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652080017&idx=1&sn=70d92ae03f620a7ace3b8888d687816a&scene=21#wechat_redirect)

[【安全圈】UAC被曝蠢到离谱的绕过，微软不分配CVE](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652080017&idx=2&sn=c4ef9c02feb49f867d9b5e707a06405a&scene=21#wechat_redirect)

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