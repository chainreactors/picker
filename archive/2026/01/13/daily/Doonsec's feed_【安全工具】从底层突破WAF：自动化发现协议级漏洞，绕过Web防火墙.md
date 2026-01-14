---
title: 【安全工具】从底层突破WAF：自动化发现协议级漏洞，绕过Web防火墙
url: https://mp.weixin.qq.com/s/9bN76uwbuVx6Eubt0eJ4ag
source: Doonsec's feed
date: 2026-01-13
fetch_date: 2026-01-14T03:33:25.543825
---

# 【安全工具】从底层突破WAF：自动化发现协议级漏洞，绕过Web防火墙

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/iazag5vDeG2fJIrWXPMKJDEkXpPuias5JzvMSEE9wBfSLia5X58pfU0hPf3yfeO2VLgibDrg8n0P2LW1YSCGDVxiclw/0?wx_fmt=jpeg)

# 【安全工具】从底层突破WAF：自动化发现协议级漏洞，绕过Web防火墙

原创

whoami0002

SecurityPaper

![]()

在小说阅读器中沉浸阅读

# 什么是协议级 WAF 规避？

简单来说，协议级 WAF 规避是指利用 WAF 和 Web 应用在解析 HTTP 协议时的差异，构造特殊的请求来绕过 WAF 的检测，同时让 Web 应用按照攻击者的意图执行。

#### WAFManis

*WAFManis*是一个协议级 WAF 规避挖掘框架，用于发现 WAF 和 Web 应用程序之间的解析歧义。

![概述](https://mmbiz.qpic.cn/mmbiz_png/iazag5vDeG2fJIrWXPMKJDEkXpPuias5JzEwMh7W4lbBwGxJ9wLrU2kEv2KQG8H0LA39v0jQWMhNI2aAVM1j4KQQ/640?wx_fmt=png&from=appmsg)

WAFManis 是一个专门用于发现协议级 WAF 规避漏洞的自动化框架，由安全研究人员开发，并在 2024 年 IEEE 安全与隐私研讨会（S&P '24）上发表了相关论文。

#### 核心特性 ✨

#### 1. **协议级模糊测试**

WAFManis 通过对 HTTP 请求进行系统性的模糊测试，自动生成各种可能触发解析歧义的请求变体。它不仅仅是在参数层面进行测试，而是深入到 HTTP 协议本身的解析层面。

#### 2. **自动化漏洞挖掘**

框架集成了多个核心模块：

* **Generator（生成器）**：生成各种 HTTP 请求变体
* **Mutator（变异器）**：对现有请求进行智能变异
* **Fuzzer（模糊测试器）**：基于 Atheris 进行高效的模糊测试
* **WAF Validator（WAF 验证器）**：验证请求是否被 WAF 拦截
* **Webapp Validator（Web 应用验证器）**：验证请求是否被 Web 应用接受

#### 3. **发现解析歧义**

框架的核心目标是发现 WAF 和 Web 应用之间的解析差异。当同一个请求：

* ✅ 被 WAF 判定为"安全"（放行）
* ✅ 被 Web 应用判定为"需要处理"（执行）

这就发现了一个潜在的规避漏洞！

#### 引用

```
@INPROCEEDINGS {,
    author = {Q. Wang and J. Chen and Z. Jiang and R. Guo and X. Liu and C. Zhang and H. Duan},
    booktitle = {2024 IEEE Symposium on Security and Privacy (SP)},
    title = {Break the Wall from bottom: Automated Discovery of Protocol-Level Evasion Vulnerabilities in Web Application Firewalls},
    year = {2024},
    volume = {},
    issn = {2375-1207},
    pages = {128-128},
    keywords = {waf;fuzz;protocol-level waf evasion;security},
    doi = {10.1109/SP54263.2024.00129},
    url = {https://doi.ieeecomputersociety.org/10.1109/SP54263.2024.00129},
    publisher = {IEEE Computer Society},
    address = {Los Alamitos, CA, USA},
    month = {may}
}
```

#### 🌟 想深入学习安全技术？

欢迎加入我们的**安全技术知识星球**！

在这里，你可以：

* 🔥 **第一时间**获取最新的安全漏洞和攻击技术分析
* 📚 **系统学习**从基础到高级的安全攻防知识
* 💡 **实战案例**分享真实的渗透测试和漏洞挖掘经验
* 🤝 **技术交流**与安全大牛和同行深度讨论
* 🎯 **工具分享**获取各种安全工具的详细使用教程
* 📖 **独家资料**包括漏洞报告、技术文档、学习路线图

**限时优惠**：前 100 名加入的伙伴，享受特别价格！

安全技术日新月异，只有持续学习才能跟上节奏。加入我们，一起在安全路上成长！🚀

![](https://mmbiz.qpic.cn/mmbiz_jpg/iazag5vDeG2c6ianUsxfiblBZd75NATDx1ibibIH6MbNEx1buuhLMm73hdEW2MibxWftMoCWRhibXNuhI8ynPKaTCXDLA/640?wx_fmt=jpeg)

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/iazag5vDeG2exlukbZwEVKyIohKDySVQPQXJw5KrBSsqITHv1B8mjkLrJ0vJlibicfsHng5MPDsIGD4biaRjziaZX8g/0?wx_fmt=png)

SecurityPaper

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/iazag5vDeG2exlukbZwEVKyIohKDySVQPQXJw5KrBSsqITHv1B8mjkLrJ0vJlibicfsHng5MPDsIGD4biaRjziaZX8g/0?wx_fmt=png)

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