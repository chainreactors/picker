---
title: 【安全圈】供水设施遭入侵，Claude AI 助力黑客锁定 OT 资产
url: https://mp.weixin.qq.com/s/VQ__D66eY8CuAv4rV_NPAA
source: Doonsec's feed
date: 2026-05-07
fetch_date: 2026-05-08T04:52:45.240932
---

# 【安全圈】供水设施遭入侵，Claude AI 助力黑客锁定 OT 资产

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/sbq02iadgfyGHVIOvPw8vUXe80bl7ibkpWibN7SqNAVLWvaqd3ns7av87KsIiaYOpvXibjePicHwrrJ1NsibNeQPL2xrYbIvyREIYWhHLgxLPD3jGo/0?wx_fmt=jpeg)

# 【安全圈】供水设施遭入侵，Claude AI 助力黑客锁定 OT 资产

安全圈

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

![](https://mmbiz.qpic.cn/sz_mmbiz_png/aBHpjnrGylgOvEXHviaXu1fO2nLov9bZ055v7s8F6w1DD1I0bx2h3zaOx0Mibd5CngBwwj2nTeEbupw7xpBsx27Q/640?wx_fmt=other&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

**关键词**

黑客

网络安全公司 Dragos 发布了一份威胁情报报告，详细描述了对墨西哥蒙特雷一家市政供水排水公司的入侵事件。**在此次事件中，身份不明的威胁行为者大量使用人工智能工具辅助攻击。**

对这家供水公司的黑客攻击发生在 2026 年 1 月，但它是 2025 年 12 月至 2026 年 2 月期间针对多个墨西哥政府组织的更广泛攻击活动的一部分。此次活动最初由 Gambit Security 的研究人员发现，随后他们邀请 Dragos 专门评估该供水公司工业控制系统（ICS）面临的威胁。

此次入侵与典型网络攻击的不同之处在于，Anthropic 的 Claude 和 OpenAI 的 GPT 模型在其中扮演核心角色，共同构成了一个人工智能辅助的行动引擎。

Claude 是主要的技术主力，负责入侵规划、工具开发和问题解决，而 GPT 则处理受害者数据并生成结构化报告。

研究人员发现的最引人注目的成果之一，是 Claude 编写的一个长达 1.7 万行的 Python 框架，它根据攻击者的反馈不断优化。Claude 将这个脚本命名为 “BACKUPOSINT v9.0 APEX PREDATOR”，其中包含 49 个模块，运用了公开的攻击安全技术，涵盖从凭证收集、活动目录侦察到数据库访问和权限提升等各个方面。

Dragos 指出，虽然这套工具集并非特别复杂或新颖，但 Claude 组装、测试和迭代的速度在行动上意义重大，它将原本可能需要数天或数周开发的工作压缩到了几个小时。

从工业安全角度来看，人工智能辅助行动产生最重大影响的时刻，是 Claude 自主识别出一台内部服务器上运行的 vNode 监控与数据采集（SCADA）及工业物联网（IIoT）管理界面。

关键的是，攻击者并未特意要求人工智能寻找运营技术（OT）系统。Claude 在广泛的内部网络侦察过程中自行识别出该平台，由于其与关键国家基础设施相关，将其归类为高价值目标，并建议作为优先攻击对象。

Dragos 认为，通用人工智能模型这种未经提示就识别出与 OT 相关资产的情况，对工业安全领域来说是一个尤为重要的新动向。

随后，Claude 对 vNode 界面进行分析，确定它依赖单一密码认证机制，并建议采用密码喷洒攻击作为最可行的切入点。

接着，人工智能自行研究供应商文档和公共资源，整理凭证列表，并针对该界面进行了两轮自动密码喷洒攻击。

所有尝试最终均告失败，攻击者随后将重点转移到其他地方进行数据窃取。Dragos 未发现任何控制系统被访问或攻击者获得该公司工业环境运营可见性的证据。

尽管对 OT 系统的入侵尝试失败，但 Dragos 指出，此次事件意义重大，像 Claude 这样的人工智能工具，让那些并非专门寻找此类系统的攻击者更容易发现 OT 系统。

不过，Dragos 谨慎表示，公众高度警惕的人工智能自主执行攻击的场景，目前并不符合 ICS/OT 威胁领域中对手能力的实际情况。

此次攻击活动背后的攻击者身份仍未查明，尚未发现与任何已知国家或犯罪组织的关联，不过攻击者持续使用西班牙语这一行为特征值得关注。Dragos 将该活动追踪为 TAT26 - 12（TAT 代表临时活动线程）。

***END***

阅读推荐

[【安全圈】安卓高危0Day漏洞可远程获取Shell访问权限](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652076197&idx=1&sn=f04ddcae84cf9ff13b2696de01ec65eb&scene=21#wechat_redirect)

[【安全圈】上古软件DaemonTools被投毒埋下木马：直接卸载吧 已经没啥用](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652076197&idx=2&sn=d5866e3f0b1ae35fa7de7fc57defec1d&scene=21#wechat_redirect)

[【安全圈】PHP 结束 30 多年定制许可历史，正式采用 BSD 3-Clause 许可证](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652076197&idx=3&sn=9d052ec11e89d8715f365258c5a457f8&scene=21#wechat_redirect)

[【安全圈】Apache HTTP Server 漏洞致数百万服务器面临远程代码执行攻击风险](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652076183&idx=1&sn=9d34b2fc14abfd37f943b2df7423829c&scene=21#wechat_redirect)

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

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/aBHpjnrGylhgCQcCZBwQrSQRLABhjrXviafAj0avc5c69t69K1YymAruIaZWzXPqbGPourlnuu8pfibV0ebgqV9g/0?wx_fmt=png)

安全圈

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