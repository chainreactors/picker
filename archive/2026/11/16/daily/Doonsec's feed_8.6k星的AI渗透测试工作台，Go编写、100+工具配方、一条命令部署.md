---
title: 8.6k星的AI渗透测试工作台，Go编写、100+工具配方、一条命令部署
url: https://mp.weixin.qq.com/s/qLnixvhgzl7ayKpy8bBL5Q
source: Doonsec's feed
date: 2026-11-16
fetch_date: 2026-11-17T09:54:12.083607
---

# 8.6k星的AI渗透测试工作台，Go编写、100+工具配方、一条命令部署

# 8.6k星的AI渗透测试工作台，Go编写、100+工具配方、一条命令部署

原创

Violet Walker
Violet Walker

黑白之道

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

![](https://mmbiz.qpic.cn/sz_mmbiz_png/nGzNudUIJ6M0TFF3b36WXjbuKmHM7rTzvDUUnL9WD3prO2bFPoFPjmMYKbL9bZEAYEasY0lO5p5TL6NuZkNAxksgYBCRgdq6ognuJuRfROs/640?from=appmsg)
> **导语**：用一句话描述需求，AI就能拉起nmap、nuclei、sqlmap去干活——而且每一次工具调用都有人审批、有日志可查。CyberStrikeAI v1.8.0把渗透测试搬进了一个可审计的工作台。

![CyberStrikeAI v1.8.0 控制台](https://mmbiz.qpic.cn/mmbiz_png/nGzNudUIJ6PtAZeNefbqJFvnAAS8VHPYVNbpccibialbebdLPQNNZPaka13T8ib9gIe9fQc88bY0nL3ibZq3akxLCEyn1gxDfnR156Gr2G4E8cc/640?from=appmsg "CyberStrikeAI v1.8.0 控制台")

*配图：CyberStrikeAI v1.8.0 中文控制台仪表盘（图源：KitPloit 推文附图）*

## 一、先说清楚：这到底是什么

11月13日，安全工具博主KitPloit（@KitPloit，12万粉丝的“Hacker Tools”账号）转发了v1.8.0发布，配文只有一句自我定位：*The system of action for AI-native cybersecurity*——AI原生安全的“行动系统”。翻译过来就是：意图进来，受管控的执行出去，证据留下来，下次干得更好。

项目在GitHub上叫AIPentest/CyberStrikeAI（老地址`Ed1s0nZ/CyberStrikeAI`自动跳转），Go编写，Apache-2.0协议，**8610星、1924 fork**，2025年11月8日建仓，昨天刚推完v1.8.0。30个版本标签走的都是“源码+脚本”路线，Release页面不摆二进制包，部署靠`./run.sh`。

它不是一个扫描器，而是**平台**：左边是项目、资产、漏洞、任务，右边是聊天框，你说人话，它拆成工具调用。

![CyberStrikeAI Web 控制台对话界面](https://mmbiz.qpic.cn/sz_mmbiz_png/nGzNudUIJ6MuWZtMPwWZWcY83C21EPOFHia5P0MOKcvdibN7mBVyOWmibUhNuHiaXfAI2iasDUqSRBSZ3aTA6HL8nmvZ9glN9K9vDPoKEaMiccOfI/640?from=appmsg "CyberStrikeAI Web 控制台对话界面")

*配图：Web控制台，自然语言对话直接驱动安全工具（图源：CyberStrikeAI 官方仓库）*

## 二、把渗透测试拆成流水线

核心是**Pi编排**：支持单智能体，也有Deep、Plan-Execute、Supervisor三种多智能体模式，配合图形化工作流（Agent、工具、条件、审批自由组合成可复用流程）和14个预置角色。

工具层是第二根支柱。`tools/`目录里躺着90份YAML工具配方（官方称100+），覆盖侦察到利用的完整链路：网络扫描（nmap、masscan）、Web扫描（sqlmap、nikto、gobuster、ffuf）、漏洞扫描（nuclei、wpscan、dalfox）、子域名枚举、空间测绘（fofa、zoomeye、shodan）、API与容器安全（trivy、clair、kube-bench）、二进制分析（ghidra、radare2）、利用（metasploit、pwntools）、破解（hashcat）、后渗透（mimikatz、impacket）。MCP接入支持HTTP、stdio、SSE和动态工具发现，还带了Burp Suite插件与Chrome/Edge浏览器扩展，可把DevTools流量直接喂回平台。

第三根支柱是**知识库**：查询改写、向量检索、重排序、结果后处理一整套RAG，还挂了视觉模型处理截图、验证码和UI。官方截图里的知识管理界面正在给“SQL Injection”“Prompt Injection”这类条目建索引：

![CyberStrikeAI 知识库管理界面](https://mmbiz.qpic.cn/sz_mmbiz_png/nGzNudUIJ6P1xoFIdva7WMvrwQpCmwiaukC5oBzbo9zlD9ZXKa0yGRYoMvJDEz2c3j2f1IIWaop2sjHEYIoFaJXymugPyu1WHMFezDfdDnIY/640?from=appmsg "CyberStrikeAI 知识库管理界面")

*配图：知识库管理，RAG检索支撑攻击链推理（图源：CyberStrikeAI 官方仓库）*

## 三、治理与审计，才是它真正的重点

平台内置：人工审批模式、工具白名单、审计Agent复核、调用前正则拦截（默认保护政府域名）、多用户RBAC、SQLite持久化、审计日志与证据留存。还有“结果治理”——Agent看到的就是截断后的工具结果，历史输出过大时不会拖垮续跑。

配套还有资产台账（域名、IP、服务去重，支持CSV导入）、漏洞生命周期管理、批量任务队列，以及**攻击链建模**：把一次行动画成图，按风险着色，事后逐步回放。

![CyberStrikeAI 攻击链可视化](https://mmbiz.qpic.cn/mmbiz_png/nGzNudUIJ6N4Z9ic1DVJZ7AMPp812Vq98HP3v4YbSka4Smhsh2EwsIfRicQAhqMiaJ8AqUeO1LBbhWAlwP9OkpmRCg9icziaPeCxPZg4Da6QTpGE/640?from=appmsg "CyberStrikeAI 攻击链可视化")

*配图：攻击链可视化，节点按风险等级着色并支持导出（图源：CyberStrikeAI 官方仓库）*

需要说明白的是，高危能力它也有：WebShell管理（虚拟终端、文件操作）和内置C2（监听器、加密Beacon、任务队列）。README写得很清楚——**只在你自己拥有或获得明确授权的系统上使用**。

## 四、下载与部署

v1.8.0没有预编译二进制，只能拿源码跑脚本。以下地址均已实测可访问：

| 用途 | 地址 |
| --- | --- |
| 源码仓库（当前） | https://github.com/AIPentest/CyberStrikeAI |
| 源码仓库（旧地址，自动跳转） | https://github.com/Ed1s0nZ/CyberStrikeAI |
| v1.8.0 源码包（tar.gz） | https://github.com/AIPentest/CyberStrikeAI/archive/refs/tags/v1.8.0.tar.gz |
| v1.8.0 源码包（zip） | https://github.com/AIPentest/CyberStrikeAI/archive/refs/tags/v1.8.0.zip |
| v1.8.0 Release 页面 | https://github.com/AIPentest/CyberStrikeAI/releases/tag/v1.8.0 |
| 中文 README | https://github.com/AIPentest/CyberStrikeAI/blob/main/README\_CN.md |
| KitPloit 工具页 | https://kitploit.com/tools/github/ed1s0nz/cyberstrikeai |

前置条件只有两条：Go 1.25以上、Python 3.10以上。然后就是三条命令：

```
git clone https://github.com/AIPentest/CyberStrikeAI.git
cd CyberStrikeAI
chmod +x run.sh && ./run.sh
```

`run.sh`会自己检查环境、建虚拟环境、装依赖、编译并启动。默认HTTPS加本地自签证书，浏览器会报一次警告，认了就行，控制台在`https://127.0.0.1:8080/`。首次启动会打印一次性`admin`密码，登录后立刻改掉——这是最不能拖的一步。

接着去「系统设置 → AI通道配置」填上模型：provider、Base URL、API Key、模型名、token上限，OpenAI兼容、DeepSeek、Qwen都支持。nmap、sqlmap这些外部工具可选，缺了会跳过或用替代品顶上。升级有「一键更新」，命令行是`./cyberstrike-ai -update`，失败可`-update-rollback`回滚。

## 五、紫队怎么看这东西

红蓝都能用，但用法相反。

对红队来说，这是把“翻工具箱”变成“写需求”：以前一个完整流程要人记住nuclei怎么拼、sqlmap怎么调，现在交给编排器，图工作流还能固化复用。**迭代速度提升是实打实的**——过去一天的侦察，今天可能变成一小时。

对蓝队来说，账要反着算。它把“AI代理+命令行+上百个安全工具+WebShell+C2”打包到一台主机上，**这本身就是新的检测面**：终端里突然出现一串nmap和sqlmap参数、进程树里多出可疑二进制、外联出现陌生端口，都是现成的检测特征。作者自己配了“调用前正则拦截”和“人工审批”，说明风险边界他门儿清。

聪明的用法是当紫队：授权范围白纸黑字落到`config.yaml`里，代理按纸面配置跑，调用全部留证，报告和蓝队复测结果一对账。既验证防守扛不扛得住，也不用把代理机器丢进生产网乱试。

## 六、跑之前必须知道的三件事

第一，**授权**。没有书面授权的系统，一个字都不要动。工具箱里每样东西都能被用歪，这事儿不解释第二遍。

第二，**高危功能默认关着**。共享或生产环境，先读官方两份文档——安全模型`docs/en-US/security-model.md`和加固指南`docs/en-US/security-hardening.md`，再决定要不要开WebShell和C2。

第三，**凭据归属**。配进去的模型Key、平台RBAC账号、它自己生成的agent凭据都在你的主机上；这台机器的安全等级，就是全部测试资产的安全等级。

项目还是knownsec 404StarLink成员，拿过腾讯TCH智能渗透赛cha004代码。

---

**版权声明**：本文由华盟网原创发布，保留所有权利。配图由华盟网整理自项目官方仓库与公开推文，仅用于技术报道。

---

![](https://mmbiz.qpic.cn/mmbiz_jpg/nGzNudUIJ6P2fHJsuKpvvN4aia9DoAX4iaLUiasm5lRCQ4Yn07RO3iavzicfD9wjatj7Yrz7f66ntjUT3ia5nTOBiczBxABibmPcmGmoyNkLxLawAQQ/640?from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/nGzNudUIJ6P1ueFQLibxtM6WReeQH25Oj3DkSDrzRwzria9WZ7iaZiboHfxB3MKF5cNPvYzX0UhdIO57WdWUovFOZsZgyDJviatIlkQ2lLpCKmfc/640?from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_jpg/nGzNudUIJ6MFjlTYgUXiaZPYibCQY35qlqPJnuQJED931vPazDU3YH2Skrc9VUlyAIsIOJ4d8Lo9pYth5ylXFKrOdHtoVv5QtPwqQdzDTibMMM/640?from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/nGzNudUIJ6PTEOGaa1E2iaUr5kHdyylGB5lMZJDZG0pPgVRWcAU6XTp5YBe23fbXKYR2cSRT1WiaCA760mK24gztNr0OJ25Gk6UCNsjmXgYnQ/640?from=appmsg)

> 👇 点击**阅读原文**，访问我的网站

---

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/3xxicXNlTXLicpdp8GZxicJpcFIZglvakzYRZiaqt6W61hfgibjeymOgiaGqRsgNvgWIacMj7Gk4PIZ4o2NtW1zb9P6Q/0?wx_fmt=png)

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