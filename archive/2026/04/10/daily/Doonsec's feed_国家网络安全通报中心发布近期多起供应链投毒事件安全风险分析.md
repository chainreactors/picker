---
title: 国家网络安全通报中心发布近期多起供应链投毒事件安全风险分析
url: https://mp.weixin.qq.com/s/y16J_QJfRI5vT00hgsl7Kw
source: Doonsec's feed
date: 2026-04-10
fetch_date: 2026-04-11T04:15:11.479245
---

# 国家网络安全通报中心发布近期多起供应链投毒事件安全风险分析

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/8C1NLS8ickpfUyPQfC2k3pgOhAfQWWdROIufnia5iarwibtUQVcDJFvlMPiafFbKHKiba7MIg7hiajONhg21vXLX3gWGDFAOfCvxKia5ibicONAlhyoq0/0?wx_fmt=jpeg)

# 国家网络安全通报中心发布近期多起供应链投毒事件安全风险分析

安在

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

![图片](https://mmbiz.qpic.cn/mmbiz_gif/5eH7xATwT3icpLmjpDSQkXx16oAygiaJncke0vYYJvIkuzECibrQJcUW4oAedTuib1G9m372rleJRDNXNs54fBEVicg/640?wx_fmt=gif&wxfrom=5&wx_lazy=1&tp=webp)

国家通报中心监测发现，近期集中爆发多起供应链投毒攻击事件，攻击目标包括API研发工具Apifox、Python开发库LiteLLM以及JavaScript HTTP库Axios，涉及开源软件仓库和商用工具两大核心供应链场景。其中，Axios投毒事件因OpenClaw等大量AI应用及插件生态直接依赖该库，导致风险通过依赖链向终端用户进一步蔓延。三起供应链投毒事件呈现攻击隐蔽性强、影响范围广、危害程度高和传播速度快的共性特征，可造成凭据遭窃取、远程代码执行和敏感数据泄露等严重危害。

**一、供应链投毒风险分析**

**一是**攻击对象聚焦重点用户。开发运营人员往往拥有较高系统权限与密钥访问能力，使供应链投毒攻击具备较高潜在收益。二是攻击路径隐蔽易于扩散。投毒攻击通过账号劫持、上游依赖污染或发布渠道篡改等方式实施，无需用户主动交互即可触发风险，并可向下游环境快速传播。**三是**攻击危害呈现放大效应。单次投毒事件可进一步引发横向移动与二次投毒，使影响范围由开发者终端扩展至单位生产环境及核心业务系统。**四是**攻击检测阻断难度较大。相关恶意代码普遍采用混淆、自清除及反调试等技术手段，部分攻击还结合隐蔽通信机制运行，显著增加安全检测与拦截阻断难度。

**二、供应链安全防护建议**

当前，供应链安全事件已从偶发性风险演变为常态化、精准化的安全威胁，建议广大开发运维用户加强安全防范。**一是**甄别安装来源渠道。仅从官方仓库、官方渠道下载安装包和工具，谨慎下载安装第三方镜像、网盘、论坛等不明来源资源。重要组件建议使用稳定版本，初次安装或者更新前应核对官方发布的校验信息，确保未被篡改。**二是**加强开发环境管理。为不同项目搭建独立运行环境，避免将开发运维环境直接暴露在互联网，减少恶意代码获取系统权限、窃取信息或破坏文件的可能，不随意执行未知命令。**三是**强化风险防范处置。关注供应链官方安全公告和权威部门发布的安全预警信息，及时采取安装补丁、升级版本、更新配置等方式消除危害影响。官方未发布漏洞补丁前，可按规范操作回退至历史稳定版本，并清理本地缓存文件，防止恶意程序驻留。

文章来源微信公众号：国家网络安全通报中心

****END**

![图片](https://mmbiz.qpic.cn/mmbiz_jpg/5eH7xATwT38j3Ndib8YhjyiaBQhdzUe1AAfIzicyojXwPTCxD0QGZHhyRcRicJAHhUv382sYFibICoxjzktlJwEEPag/640?wx_fmt=jpeg&wxfrom=5&wx_lazy=1&tp=webp)

[![图片](https://mmbiz.qpic.cn/mmbiz_png/5eH7xATwT3ibILU2vpTY8kPMvg2uyDyibiaFibHCDibF1vCIjn2tNAKdNicq3Y45vuYuWNUDICSF8dZ206dy1Kzrehug/640?wx_fmt=png&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=3)](https://mp.weixin.qq.com/s?__biz=MzU5ODgzNTExOQ==&mid=2247651222&idx=1&sn=0674c7e57249a57240b5ed0fcd6cdcf2&scene=21#wechat_redirect)

[![图片](https://mmbiz.qpic.cn/mmbiz_png/5eH7xATwT38j3Ndib8YhjyiaBQhdzUe1AApXU9ib7vkMD4KMHhjVfkTqOCUrDibUaBDoH0OGGCMasLLJyv5xppK6rA/640?wx_fmt=png&wxfrom=5&wx_lazy=1&tp=webp)](https://mp.weixin.qq.com/s?__biz=MzU5ODgzNTExOQ==&mid=2247652102&idx=1&sn=8af8808f9055f99fa71020922d80058c&scene=21#wechat_redirect)

![图片](https://mmbiz.qpic.cn/mmbiz_jpg/5eH7xATwT38HPkvxLkOy5rLCeVBtj8H9SUbVPNZbibc4N2knPCDFjTKduRLhiaAZVQShUa2IZqsBShI2GG2dpqBg/640?wx_fmt=jpeg&wxfrom=5&wx_lazy=1&tp=webp)

点击这里阅读原文**

预览时标签不可点

阅读原文

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/5eH7xATwT39OIA4MxWIQmVzjc3H2rbMa0sv6no7gMEXOV63OW7hvwk4EDjOaurIkrnPOjBpCmIN00ELKRf16qg/0?wx_fmt=png)

安在

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/5eH7xATwT39OIA4MxWIQmVzjc3H2rbMa0sv6no7gMEXOV63OW7hvwk4EDjOaurIkrnPOjBpCmIN00ELKRf16qg/0?wx_fmt=png)

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