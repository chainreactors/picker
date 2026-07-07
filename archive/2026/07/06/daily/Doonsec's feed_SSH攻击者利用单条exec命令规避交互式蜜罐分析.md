---
title: SSH攻击者利用单条exec命令规避交互式蜜罐分析
url: https://mp.weixin.qq.com/s/XfXKN41Ru4sV9tou8KHs_g
source: Doonsec's feed
date: 2026-07-06
fetch_date: 2026-07-07T06:02:29.913187
---

# SSH攻击者利用单条exec命令规避交互式蜜罐分析

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/WibvcdjxgJnuA578nKC8g4S2btJEIK86HJU6VDGP5GCib1Nk4vEdoyadtkhY8xfIN5bfO3mJ6AZ697Kaib6Lf5CePuDherxY11WDGAAKLzWnXk/0?wx_fmt=jpeg)

# SSH攻击者利用单条exec命令规避交互式蜜罐分析

网安百色

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

![](https://mmbiz.qpic.cn/mmbiz_png/WibvcdjxgJnvvQs5MibaBuXZdvEw1jGVnZED3wX2vYiabTWKibcMBkJwcPmyMiabEwAI1X4MqTfqwEUL5Iqnw7TDUA9EQ4xiasjqibJSCJKkBHCHtY/640?wx_fmt=png&from=appmsg)

SSH攻击者 increasingly 通过SSH滥用单个非交互式命令执行来绕过传统蜜罐分析，将认证后活动转化为简短的自动化探测，而非诱骗系统原本设计用于研究的交互式shell会话。

对十一个基于大语言模型（LLM）的SSH蜜罐的最新测量显示，99.23%的已认证会话仅包含单个非交互式命令请求，仅0.10%开启交互式shell，0.67%尝试文件传输。

| 模式 | 会话数 | 占比 |
| --- | --- | --- |
| 非交互式命令执行 | 176,256 | 99.23% |
| 交互式shell | 179 | 0.10% |
| 文件传输尝试 | 1,187 | 0.67% |
| 总计 | 177,622 | 100% |

此类攻击通常在1秒内完成，远超人类操作速度，明确指向自动化工具与僵尸网络基础设施。

独立Cowrie蜜罐即服务（HaaS）数据集（覆盖同期4,737个SSH蜜罐）证实了这一趋势：在包含至少一条命令的已登录会话中，92.67%恰好执行单条命令，与LLM蜜罐中观察到的非交互式主导现象一致。

HaaS档案库2017–2026年的纵向分析进一步表明，非交互式SSH会话自2018年起已普遍存在，2024年末占比骤升至97%以上（据Arxiv报告）。

这说明攻击者如今将SSH视为扫描与利用流程中的自动化检查点：完成认证后，以机器速度执行单条命令，快速收集信息或验证目标后立即转移。

单命令执行绕过蜜罐设计假设

多数SSH蜜罐及网络诱骗系统仍默认攻击者认证后会开启交互式shell并输入命令序列，以便记录、分析和"对话"。

基于LLM的SSH蜜罐（如AdvancedShelLM、HoneyLLM、HoneyGPT）明确针对终端对话真实性优化，其成功指标围绕交互时长与对话量构建。

部分框架（如VelLMes）甚至主动拒绝非交互式命令执行模式，直接丢弃当前互联网暴露环境中攻击者发送的约99%已认证流量。

在非交互模式下，攻击者通过exec请求发送单条命令，接收输出后立即关闭通道，不建立shell会话。这削弱了依赖命令序列的蜜罐有效性，迫使检测方法转向识别此类短时单次命令而非持续交互。

单命令exec会话的主导地位对SSH蜜罐设计及诱骗效果评估均产生直接影响：

数据偏差问题：仅支持交互式shell或忽略exec请求的蜜罐，系统性遗漏绝大多数攻击行为，导致数据集偏向罕见的人工操作，而非主流的自动化探测。

评估指标失效：当多数攻击在单条命令后1秒内终止时，依赖交互时长、命令数量或对话轮次的评估指标基本失去意义。

对LLM蜜罐而言，核心考验不再是攻击者"停留聊天时长"，而是能否通过验证探测：是否对常见命令返回真实Linux系统输出；能否在多次探测中维持状态一致性；以及多大程度符合野外观察到的探测模式。

研究人员在两组数据集中均未发现提示词注入字符串、明确AI/LLM提及或固定哈希探测，表明当前对LLM诱骗系统的压力主要来自执行正确性验证，而非对话操控。

本公众号所载文章为本公众号原创或根据网络搜索下载编辑整理，文章版权归原作者所有，仅供读者学习、参考，禁止用于商业用途。因转载众多，无法找到真正来源，如标错来源，或对于文中所使用的图片、文字、链接中所包含的软件/资料等，如有侵权，请跟我们联系删除，谢谢！

![图片](https://mmbiz.qpic.cn/mmbiz_jpg/1QIbxKfhZo5lNbibXUkeIxDGJmD2Md5vKicbNtIkdNvibicL87FjAOqGicuxcgBuRjjolLcGDOnfhMdykXibWuH6DV1g/640?wx_fmt=other&from=appmsg&wxfrom=5&wx_lazy=1&wx_co=1&randomid=p6hk1x4r&tp=webp#imgIndex=1)

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/1QIbxKfhZo6T5IuE1hib7qvAtbaaUZ8tt2fviaDoictibySdn9ibPOF34VZoLwMDYQWCnQGouyMttnhZib6G8fddDqNw/0?wx_fmt=png)

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