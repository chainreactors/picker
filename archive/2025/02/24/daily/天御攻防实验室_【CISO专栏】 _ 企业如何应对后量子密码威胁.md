---
title: 【CISO专栏】 | 企业如何应对后量子密码威胁
url: https://mp.weixin.qq.com/s?__biz=MzU0MzgyMzM2Nw==&mid=2247486268&idx=1&sn=768496b28b1a1134a77c378aa605a2ab&chksm=fb04c854cc734142726054d2ab71b4d282797aa374e46019c440fea183a417600b1f212b950d&scene=58&subscene=0#rd
source: 天御攻防实验室
date: 2025-02-24
fetch_date: 2025-10-06T20:36:29.707546
---

# 【CISO专栏】 | 企业如何应对后量子密码威胁

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/hPq2VZ0zUBBIYCjaxwbyaAfQJUSR675tjD9LB5jF8gJ7EpCQmnJkmepPwicS0gBFPfye7v7ZgG9K5eRfricndxJw/0?wx_fmt=jpeg)

# 【CISO专栏】 | 企业如何应对后量子密码威胁

原创

天御

天御攻防实验室

![](https://mmbiz.qpic.cn/sz_mmbiz_png/hPq2VZ0zUBAjbQ8J7Xfm61hMtowFgJYhvibIobWCIQp0a7HwuzDB5nHVVyvvUicnqEBRvRuqqWhcREOCuQz2X76A/640?wx_fmt=other&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

![](https://mmbiz.qpic.cn/mmbiz_svg/L3Qib0nCc28kiapaXx6yNO55P5HlE5K5KPeSAjibuQB36kIUdWs5ZVzic20R5FzeTKae8vbINVEw6wlcgKa6R3ZqJyzYfRb6Z531/640?wx_fmt=svg&from=appmsg&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp)

**【CISO】专栏**

![](https://mmbiz.qpic.cn/mmbiz_svg/L3Qib0nCc28kiapaXx6yNO55P5HlE5K5KPXIUDVn0iapYjG2yy97z0lLcM24iaxtvIURGVzAzErSBnM9ZAYQl7U12fvcpic6PLTwm/640?wx_fmt=svg&from=appmsg&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp)

在这个数字化转型加速、地缘政治日趋复杂的时代，网络安全已然成为国家战略和企业发展的重中之重。随着中美战略竞争加剧、全球供应链重构、数据主权意识觉醒，传统的网络安全治理模式正面临前所未有的挑战与机遇。

作为一个面向企业高管、CISO、CIO以及国家监管部门领导的专业专栏，我们将深入探讨数字时代下的网络安全治理新范式。在这里，您将看到：

**战略视角**- 深度解析地缘政治变局下的网络安全新形势
- 剖析中美科技竞争背景下的数据主权与技术自主
- 探讨"零信任"架构在新形势下的战略价值
- 研判供应链安全治理的创新模式

**治理实践**- 网络安全投资战略：从成本中心到价值创造
- 数据安全合规：应对跨境数据流动的挑战
- 人才梯队建设：打造新时代网络安全铁军
- 安全创新：AI驱动的主动防御体系建设

**领导力建设**- CISO角色进化：从技术专家到战略领导者
- 董事会沟通：让网络安全成为战略议题
- 跨部门协同：构建全员安全文化
- 危机管理：重大安全事件的领导力法则

本专栏将邀请业界资深CISO、监管专家、智库专家进行深度对话，分享最佳实践，展望未来趋势。我们期待与各位读者一起，在这个充满挑战与机遇的时代，共同探索网络安全治理之道，护航组织数字化转型，共筑国家网络安全防线。

随着量子计算技术的快速发展，传统加密体系正面临前所未有的挑战。谷歌、微软、IBM等科技巨头的研究表明，密码分析相关量子计算机（CRQC）可能在2032-2040年间出现，届时现有非对称加密算法（如RSA、ECC）将被轻易破解。尽管这一威胁的时间线尚存不确定性，但迁移到后量子密码（PQC）的复杂性和长期性要求企业必须立即行动。以下从战略规划到技术落地的维度，为企业提供应对方案。

![](http://mmbiz.qpic.cn/sz_mmbiz_jpg/hPq2VZ0zUBDPcrVkIEIGfhoDxlTvUqadL92v5upicfGpdHhJoKyoXWuTHpDKCUJk4FyNF3rhty2Jg1BLANRAGRA/640?wx_fmt=other&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

# 一、认清威胁：量子计算对企业的核心风险

### 1. "现在存储，以后解密"（SNDL）攻击的真实性与局限性

威胁本质：美国国家安全局（NSA）已开始大规模截获加密数据，待CRQC成熟后集中破解。此类攻击针对的是当前使用传统加密算法（如RSA、ECC）保护的数据，尤其是那些通过脆弱密钥层级加密的敏感信息。

#### 风险范围：

* 高价值目标优先

  ：攻击者将CRQC视为稀缺资源，优先破解能直接获取操控权的密钥（如身份认证、软件签名密钥），而非普通通信数据。
* 长期数据暴露

  ：若企业涉及国防情报、核心知识产权（IP）、国家安全级通信，或使用单一主密钥保护全量历史数据的架构，则面临极高风险。

#### 客观评估：

* 多数企业（如零售、普通制造业）的日常数据对攻击者价值有限，无需过度恐慌。
* 但需警惕"密钥中心化"架构——少量密钥泄露可能导致历史数据全面沦陷。

### 2. "历史数据否认"（SNRL）风险

若未采用抗量子签名，攻击者可能伪造长期合同、交易记录、法律文件，引发商业纠纷或合规危机。

### 3. 系统瘫痪风险

传统加密算法一旦被攻破，依赖其的身份认证、软件更新验证、通信协议（如TLS）将直接失效，导致业务中断。例如：

* 攻击者破解TLS密钥后，可劫持企业云服务通信。
* 软件签名密钥泄露可能导致供应链投毒攻击。

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/hPq2VZ0zUBBx2ESUwvicgTOfTm1Otk2tv0jvPWFeaWeawQUfRuIichBCuk3sxT9YcXGtx6ib9jdenUHMIKuMYSDRg/0?wx_fmt=png)

天御攻防实验室

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/hPq2VZ0zUBBx2ESUwvicgTOfTm1Otk2tv0jvPWFeaWeawQUfRuIichBCuk3sxT9YcXGtx6ib9jdenUHMIKuMYSDRg/0?wx_fmt=png)

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