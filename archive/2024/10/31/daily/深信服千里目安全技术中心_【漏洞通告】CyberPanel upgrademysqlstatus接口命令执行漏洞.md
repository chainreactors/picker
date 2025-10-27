---
title: 【漏洞通告】CyberPanel upgrademysqlstatus接口命令执行漏洞
url: https://mp.weixin.qq.com/s?__biz=Mzg2NjgzNjA5NQ==&mid=2247523812&idx=2&sn=eb2f4b3b34ac1799bcb461c02fb1e6f3&chksm=ce4616f4f9319fe2cee38c81934e037f2f6a972955ed5fa0bd7ae9d1f3d2419b572ac1a5e19b&scene=58&subscene=0#rd
source: 深信服千里目安全技术中心
date: 2024-10-31
fetch_date: 2025-10-06T18:58:01.162330
---

# 【漏洞通告】CyberPanel upgrademysqlstatus接口命令执行漏洞

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/w8NHw6tcQ5waNMhibhgL2ibkyZ3pvzTGpkPP1qZAoWicBiaBmiaaPINmE9XzBSeFUJDfSlZ0GgfbvHxwpiavN3opMVrg/0?wx_fmt=jpeg)

# 【漏洞通告】CyberPanel upgrademysqlstatus接口命令执行漏洞

深瞳漏洞实验室

深信服千里目安全技术中心

![](https://mmbiz.qpic.cn/mmbiz_gif/w8NHw6tcQ5xicMsH3PR9W3GoybdY7Wk4BibXsxYH2xDDM2dicf9D3n99jJ6dM3iabSnvWF2CtTiaoLChqn9DVhgJFFQ/640?wx_fmt=gif&from=appmsg)

**漏洞名称：**

CyberPanel upgrademysqlstatus接口命令执行漏洞

**组件名称：**

CyberPanel

**影响范围：**

CyberPanel 2.3.5
CyberPanel 2.3.6

**漏洞类型：**

命令执行

**利用条件：**

1、用户认证：不需要用户认证

2、前置条件：默认配置

3、触发方式：远程

**综合评价：**

<综合评定利用难度>：容易，能造成远程代码执行。

<综合评定威胁等级>：严重，能造成远程代码执行。

**官方解决方案：**

已发布

**漏洞分析**

![](https://mmbiz.qpic.cn/mmbiz_gif/w8NHw6tcQ5xicMsH3PR9W3GoybdY7Wk4BtGgIUa5ibsnETXb6ZqTeHZ67F14OZ8WXSuEGRTdjP3eOT45yYxuy2Qg/640?wx_fmt=gif&from=appmsg)

**组件介绍**

CyberPanel 是一个开源的托管控制面板，它是为 VPS 和 Dedicated Servers 设计的，用于简化网站和服务的管理。

![](https://mmbiz.qpic.cn/mmbiz_gif/w8NHw6tcQ5xicMsH3PR9W3GoybdY7Wk4BtGgIUa5ibsnETXb6ZqTeHZ67F14OZ8WXSuEGRTdjP3eOT45yYxuy2Qg/640?wx_fmt=gif&from=appmsg)

**漏洞简介**

2024年10月30日，深瞳漏洞实验室监测到一则CyberPanel组件存在命令执行漏洞的信息，漏洞威胁等级：严重。

CyberPanel的upgrademysqlstatus接口存在命令执行漏洞，未授权的**攻击者可以利用该漏洞执行任意命令，导致服务器失陷。**

**影响范围**

目前受影响的CyberPanel版本：

CyberPanel 2.3.5
CyberPanel 2.3.6

**解决方案**

![](https://mmbiz.qpic.cn/mmbiz_gif/w8NHw6tcQ5xicMsH3PR9W3GoybdY7Wk4BtGgIUa5ibsnETXb6ZqTeHZ67F14OZ8WXSuEGRTdjP3eOT45yYxuy2Qg/640?wx_fmt=gif&from=appmsg)

**官方修复建议**

官方已发布最新版本修复该漏洞，请受影响用户将CyberPanel更新到2.3.7及以上版本，下载链接：https://github.com/usmannasir/cyberpanel/tree/v2.3.7

![](https://mmbiz.qpic.cn/mmbiz_gif/w8NHw6tcQ5xicMsH3PR9W3GoybdY7Wk4BtGgIUa5ibsnETXb6ZqTeHZ67F14OZ8WXSuEGRTdjP3eOT45yYxuy2Qg/640?wx_fmt=gif&from=appmsg)

**深信服解决方案**

**1.风险资产发现**

支持对CyberPanel的主动检测，可批量检出业务场景中该事件的**受影响资产**情况，相关产品如下：

**【深信服云镜YJ】** 已发布资产检测方案，指纹ID:0010456。

**2.漏洞主动检测**

支持对CyberPanel upgrademysqlstatus接口命令执行漏洞的主动检测，可批量快速检出业务场景中是否存在**漏洞风险**，相关产品如下：

**【深信服云镜YJ】**预计2024年11月03日发布检测方案，规则ID:SF-2024-01240。

**【深信服漏洞评估工具TSS】**预计2024年11月04日发布检测方案，规则ID:SF-2024-01241。

**【深信服安全托管服务MSS】**预计2024年11月04日发布检测方案（需要具备TSS组件能力），规则ID:SF-2024-01241。

**【深信服安全检测与响应平台XDR】**预计2024年11月03日发布检测方案（需要具备云镜组件能力），规则ID:SF-2024-01240。

**3.漏洞安全监测**

支持对CyberPanel upgrademysqlstatus接口命令执行漏洞的监测，可依据流量收集实时监控业务场景中的**受影响资产情况，快速检查受影响范围**，相关产品及服务如下：

**【深信服安全感知管理平台SIP】**预计2024年11月08日发布监测方案，规则ID:11027772。

**【深信服安全托管服务MSS】**预计2024年11月08日发布监测方案（需要具备SIP组件能力），规则ID:11027772。

**【深信服安全检测与响应平台XDR】**预计2024年11月08日发布监测方案，规则ID:11027772。

**4.漏洞安全防护**

支持对CyberPanel upgrademysqlstatus接口命令执行漏洞的防御，**可阻断****攻击者针对该事件的入侵行为**，相关产品及服务如下：

**【深信服下一代防火墙AF】**预计2024年11月08日发布防护方案，规则ID:11027772。

**【深信服Web应用防火墙WAF】**预计2024年11月08日发布防护方案，规则ID:11027772。

**【深信服安全托管服务MSS】**预计2024年11月08日发布防护方案（需要具备AF组件能力），规则ID:11027772。

**【深信服安全检测与响应平台XDR】**预计2024年11月08日发布防护方案（需要具备AF组件能力），规则ID:11027772。

**参考链接**

https://dreyand.rs/code/review/2024/10/27/what-are-my-options-cyberpanel-v236-pre-auth-rce

**时间轴**

**2024/10/30**

深瞳漏洞实验室监测到CyberPanel upgrademysqlstatus接口命令执行漏洞信息。

**2024/10/30**

深瞳漏洞实验室发布漏洞通告。

点击**阅读原文**，及时关注并登录深信服**智安全平台**，可轻松查询漏洞相关解决方案。

![](https://mmbiz.qpic.cn/mmbiz_png/w8NHw6tcQ5waNMhibhgL2ibkyZ3pvzTGpkLib4osf35L2D5ukBQGYQfiaZgOoA48ic3y6dgvjiauKO8e4N6vf95CWSeg/640?wx_fmt=png&from=appmsg)![](https://mmbiz.qpic.cn/mmbiz_png/w8NHw6tcQ5xicMsH3PR9W3GoybdY7Wk4BHMAPEeGfdttFLtASTZPZ2YAt56yiawEHSeKI2vnbfAvJXfRLpwKHictw/640?wx_fmt=png&from=appmsg)

预览时标签不可点

阅读原文

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/w8NHw6tcQ5xUEmJGibg2JE8nVwwxzibBrJTEzuyfhPTuTZeyvTviay6rzGOGrHkAO45vyyibnV1FZThckmmfFfM6BA/0?wx_fmt=png)

深信服千里目安全技术中心

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/w8NHw6tcQ5xUEmJGibg2JE8nVwwxzibBrJTEzuyfhPTuTZeyvTviay6rzGOGrHkAO45vyyibnV1FZThckmmfFfM6BA/0?wx_fmt=png)

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