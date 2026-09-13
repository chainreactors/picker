---
title: 【安全圈】黑客操纵数百个AI Agent：26秒破11家企业，夜袭440台服务器
url: https://mp.weixin.qq.com/s/5CV1XcAtZXSiCRKDzpTxoQ
source: Doonsec's feed
date: 2026-09-12
fetch_date: 2026-09-13T06:57:33.710365
---

# 【安全圈】黑客操纵数百个AI Agent：26秒破11家企业，夜袭440台服务器

# 【安全圈】黑客操纵数百个AI Agent：26秒破11家企业，夜袭440台服务器

安全圈

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

![](https://mmbiz.qpic.cn/sz_mmbiz_png/aBHpjnrGylgOvEXHviaXu1fO2nLov9bZ055v7s8F6w1DD1I0bx2h3zaOx0Mibd5CngBwwj2nTeEbupw7xpBsx27Q/640?wx_fmt=other&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

**关键词**

黑客

**核心事实：**全球网络安全界见证了首场被完整记录的多智能体（Multi-Agent）集团化在野闪电战。一名操纵数百个自主 AI Agent 的攻击者，针对全球企业与教育机构广泛部署的 PaperCut 打印服务器漏洞链（`CVE-2026-81578` 与 `CVE-2026-82078`）发起自主渗透。战役爆发时，AI 军团在短短 **26 秒内连续打穿 11 家组织**，仅用 **7 分钟就攻破内网直取域管权限**，全网至少 440 台主机在无人类干预下被自动化收割。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/sbq02iadgfyFDRsALdTRLzX6cwE0TUSreYOzvFWfxp5dZfCf4SR7tVSdOsptPb09FA5gaKPic4EA9rhEHDoicMeUlV0ibJZTTibiciaxdDb1Lib679c/640?wx_fmt=other&from=appmsg)

## ⚡ 一、 令人胆寒的作战时效：从零研发到全域接管仅需数分钟

由 GreyNoise、Blackpoint Cyber 以及 Arctic Wolf 三家国际威胁情报团队联合起底的溯源取证显示，整个攻击展现出前所未有的“机器速度”：

⏱️ AI 闪电战时间线复盘

▪️ **不到 4 小时：**攻击者从完全空白的工作空间起步，通过让 AI 对比补丁差异、编写验证脚本，在 4 小时内即完成了针对真实受害者的首发远程代码执行（RCE）；

▪️ **26 秒打穿 11 家组织：**在集中攻击波次启动后，多智能体并发调度，仅 26 秒便在 11 家异地独立机构内成功落地并执行载荷；

▪️ **7 分钟横向斩获域管：**在美国一所受害高中的真实案例中，AI Agent 从最初突破外网打印系统，到搜集主机凭据、探测内网活动目录，直至夺得 Domain Administrator（域管理员）特权，**全链路耗时仅 7 分钟**。

## 🧠 二、 揭秘幕后架构：黑客如何把 AI 组装成全自动打工人

安全专家发现，攻击者并非只让 AI 写写脚本，而是依托两项核心开源基础设施，构建了一个具有**自我排错与持久记忆**能力的智能体流水线：

**1. 持久记忆（Hindsight）与多智能体并发工作区（AionUi）：**
黑客使用开源记忆服务 `Hindsight` 保持跨任务的持久上下文，使 Agent 绝不会在长流程任务中“失忆”；通过 `AionUi` 同步调度基于 OpenAI Codex 与 DeepSeek 模型的数百个智能体进程。

**2. 自动化失败分析与代码自愈闭环：**
遇到防御阻断或网络超时时，系统不作简单放弃，而是由专用 Agent 抓取错误堆栈，自动改写 PoC 交互逻辑，重新生成变形载荷进行针对性重试。

**3. 武器化内网工具链自主下发：**
Agent 突破边界后，自动化推送 Mimikatz、SharpHound、Certipy、Rubeus、Impacket 等经典黑客工具，全流程由 Python 编排脚本监视进度，自主推进 AD 域信息抓取与内网代理穿透。

📊 本次多智能体战役关键作战指标

▪️ **受害规模：**波及全球 48 个国家、395 家已知机构、440+ 台自建服务器；

▪️ **核心漏洞：**组合利用 PaperCut NG/MF 认证绕过与远程代码执行（CVE-2026-81578 / 82078）；

▪️ **受影响重灾区：**欧美教育系统、大型企业分支机构；

▪️ **核心攻击源 IP：**`45.142.193[.]132`。

## 🛡️ 三、 紧急止血与防御响应行动指南

针对该起恶性在野利用，软件厂商 PaperCut 官方已正式废弃此前发布的紧急临时热补丁，推出了经过完整回归测试的正规维护发行版：

**1. 检索与封禁高危攻击源与内网异常痕迹：**

```
# 1. 检查网络连接中是否存在指向已被曝光的恶意控制源
netstat -antp | grep "45.142.193.132"

# 2. 检查日志目录中是否存在自动化探针与 Java 反序列化报错
grep -Ei "CVE-2026-81578|Meterpreter|mimikatz" /opt/papercut/server/logs/*
```

**2. 彻底止血升级与架构防护建议：**

① **全量升级到正规修复版本：**立即部署 PaperCut NG/MF **26.0.5**、**25.0.13** 或 **24.1.10**，替代此前的临时紧急补丁；

② **严防边缘设备直连公网：**打印管理服务绝无任何理由直接向公网暴露 9191/9192 端口，必须将其下沉至独立内网管理 VLAN 并限制访问控制列表；

③ **阻断横向提权路径：**限制打印服务主机的域账号权限，严禁将域管特权账号登录到该类边缘设备，彻底切断 AI Agent 窃取内存凭证借机跃迁的通道。

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