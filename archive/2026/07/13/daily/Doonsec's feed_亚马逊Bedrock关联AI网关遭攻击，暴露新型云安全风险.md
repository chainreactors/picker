---
title: 亚马逊Bedrock关联AI网关遭攻击，暴露新型云安全风险
url: https://mp.weixin.qq.com/s/9QwcK0uZJDaTKyqIlXsq5Q
source: Doonsec's feed
date: 2026-07-13
fetch_date: 2026-07-14T04:43:42.021112
---

# 亚马逊Bedrock关联AI网关遭攻击，暴露新型云安全风险

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/8C1NLS8ickpcQI3W6KAERt7d2G5mazLzpx72yWVZkIwIlucEFU8Yk5Ac5QPm9UmsqhiadvrbXvLiaOfdvbzAzLj3yoeNT2xoLiaSTwd7DWwK4Vg/0?wx_fmt=jpeg)

# 亚马逊Bedrock关联AI网关遭攻击，暴露新型云安全风险

走狗是狗哥
走狗是狗哥

安在

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

![图片](https://mmbiz.qpic.cn/mmbiz_gif/5eH7xATwT3icpLmjpDSQkXx16oAygiaJncke0vYYJvIkuzECibrQJcUW4oAedTuib1G9m372rleJRDNXNs54fBEVicg/640?wx_fmt=gif&wxfrom=5&wx_lazy=1&tp=webp)

本次入侵沿用了常见的云攻击套路，但专家指出，更值得警惕的是：AI网关正逐渐成为身份、权限与模型访问的核心枢纽。

一场最终植入挖矿恶意程序的云入侵事件，向企业暴露了一项更严峻的风险：AI网关将云身份、权限与基础模型的访问权限集中在单一高权限系统中。

网络安全公司Darktrace的研究人员发现，攻击者攻陷了一台作为亚马逊Bedrock的LiteLLM代理的AWSEC2实例，最终植入了XMRig挖矿恶意程序，同时还试图滥用云身份与AI服务。

尽管攻击最终仅用于挖矿，但研究人员表示，更核心的隐患在于AI网关集中了模型访问、身份凭证与云权限，使其成为高价值攻击目标。

专家认为，本次攻击手法并不新鲜，与过往的云攻击技术一致。

BeyondTrust首席信息安全官肖恩・马隆表示：“剥离AI相关的包装来看，这是至少2018年起就屡见不鲜的云入侵模式：SSH端口对公网开放、暴力破解尝试、通用XMRig挖矿程序，以及反复连接矿池的行为。”

“哪怕是针对AI的攻击环节——窃取凭证探测Bedrock模型访问权限——在2024年也已有了专门命名：大模型劫持(LLMjacking)。”

不过马隆也认同Darktrace研究人员对潜在影响范围的判断。他解释道：“AI网关将凭证、云权限与模型访问权限汇聚到单一关键节点，一次常规入侵就能攻陷高价值资产。”

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/8C1NLS8ickpedZ5eiar4QhGhiccmvDsibMVEBPZqxUfdWdI8CTtyiaTo4rqYKOsHfrRGwibsic9y4S7jQNY1GPoTXiaic94513KqP90N6vtmwGQcicJww/640?wx_fmt=jpeg&from=appmsg)

**攻击沿用已知入侵路径**

据Darktrace介绍，被攻陷的EC2实例用于承载LiteLLM代理服务，关联的IAM角色具备亚马逊Bedrock资源的访问权限。

研究人员虽无法最终确认初始入侵途径，但表示本次攻击的流程与常见云入侵事件完全一致。

植入挖矿程序前，该实例的SSH端口对公网开放，22端口可被任意地址访问。

Darktrace观测到大量入站SSH连接尝试，大多来自同一个外部IP地址，表明攻击者大概率实施了暴力破解。

不久后，该主机下载了包含XMRig挖矿恶意程序的ZIP压缩包，随后通过HTTPS协议反复连接已知矿池。

Darktrace强调，由于缺少主机层面的日志，无法确认SSH相关活动是否直接导致了系统沦陷。

但SSH端口暴露、挖矿程序下载、后续矿池通信的时间线高度吻合，足以说明这台EC2实例已被攻破，并被挪用于非法算力活动。

**AI网关沦陷危害极大**

本次披露还详细记录了另一项单独观测到的可疑IAM活动，事件发生在一天之后，涉及另一个AWS身份。

异常行为包括：来自越南IP地址的GetSendQuota接口调用、枚举并调用亚马逊Bedrock基础模型的尝试，以及使用随机生成用户名创建新IAM用户的操作。

这类行为通常与凭证泄露后建立持久化权限的手法相关。不过Darktrace无法将该IAM活动与本次LiteLLM代理入侵事件直接关联。

Sectigo高级研究员杰森・索罗科表示，本次事件的重点不在于挖矿程序本身，而在于被攻陷的系统。

他指出：“这类网关正逐渐成为身份、模型访问、提示词、日志与策略的调度中枢。”

“当一台网关的SSH端口对外暴露，或是绑定了宽泛的IAM权限时，它就不再是一台普通的EC2实例，而是整个AI业务的控制点。”

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/8C1NLS8ickpegKr9I0W2D9mGiaQCmicehmGsUgaz9icNzeTFRXias3xhxbLJMpR0wRU1IgbIibpmnDFgbTb9mE9iccia9c9TicZk20fVBIYLejx5apCo/640?wx_fmt=jpeg&from=appmsg)

索罗科补充道，为防范此类攻击，安全团队应关闭公网管理入口、尽可能移除长期密钥、收紧IAM权限范围、监控Bedrock及模型的访问模式，并将工作负载遥测数据与控制平面事件做关联分析。

Darktrace表示其协助及时遏制了本次攻击。

研究人员在周四正式发布的博客文章中提到：“Darktrace托管威胁检测服务捕获了本次挖矿活动，并由Darktrace安全运营中心完成研判。”本文提前获取了该博客内容。

“经核查后，该告警已升级同步至客户。这一预警让客户及时得知了AWS环境中存在的资源滥用行为。”

**安在企业（用户）会员服务**

**助力全生命周期安全意识提升**

“安在企业（用户）会员服务”，为所有企业提供一站式的网络安全支援服务，包括意识宣传、培训教育、效果检验、专业圈子、知识社区、专业培训、参选评奖等多个板块，助力网安从业者高效履职，实现个人与企业安全能力同步升级。

**[小投入大防护！安在推出企业（用户）会员服务](https://mp.weixin.qq.com/s?__biz=MzU5ODgzNTExOQ==&mid=2247652102&idx=1&sn=8af8808f9055f99fa71020922d80058c&scene=21#wechat_redirect)，点击标题阅读详情。**

深度贴合企业不同规模、安全水平投入以及员工安全意识的不同发展阶段，特设5级安全意识培训服务体系，为企业用户量身匹配适配的安全意识解决方案。

![图片](https://mmbiz.qpic.cn/mmbiz_jpg/8C1NLS8ickpfxauQUKv5E2gfFrpMBAz1Um7FAY4ontydFQQ1ZKtH1AnXs3kfYxtOYX55xrRBM2pFYicz2sqACyjd4u1CO2iaAFCYLIbgMGS58M/640?wx_fmt=jpeg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=2)

![图片](https://mmbiz.qpic.cn/sz_mmbiz_jpg/8C1NLS8ickpevFQuuGbgqzRQXxpZt2NQG9gkeSfhrKIBL6NVagjD9IYhtko4pjEdkrmiaAFfGAYPQN06Cs2MSLG4HGqExqL1OJ9n0ZSmibwO9Q/640?wx_fmt=jpeg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=1)

本文展示所有类型素材，均包含在企业（用户）会员服务中，如有意向，欢迎垂询。

**加入诸子云知识星球**

获取更多“安全意识资料”和“网络安全报告”

![](https://mmbiz.qpic.cn/sz_mmbiz_png/8C1NLS8ickpevtB5U1iad3jHVWSBznd4wGSnt15KjDpDvdDAzWfLewNRoKHVyCNTCEIVkuJAZOyUvKSibQZJfe43xQsofxEKuB4xuj2gzBG4EM/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/8C1NLS8ickpfphwUVRfsnQ4tHXQicImFKOyric81wyOR6UtibaU9W2nPpF2bIflBltg8S0vJMmYEDrEkWN30lpxicg5YUyLDu0fAlCgX3ibJBX8Ys/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/8C1NLS8ickpcHLAPdhJaKhut2fLyfnDD0ofblclhTxwQtdjZ9Wnsgw7qtANaolbmpYLhf9mCW9ib2vDial19qZnEibibEZkAcOVPZVTA9QsD5EeY/640?wx_fmt=jpeg&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/8C1NLS8ickpcaBf7luDbkibnkcG6SFanyicuIePMSYCXyZ4dpRTDOuRkj4IwafHmia3a61q1QmasWkERH6vhD4eicgePFZCERRib6zAefEHxWz3cY/640?wx_fmt=jpeg&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_jpg/8C1NLS8ickpcoibvzpu3KUfibMYf9yTU7VWPXP10LBBkle2fQKqqdVk7zLYiaoh0bHWxmovw4aqY0icMXYfqY2TW0LibL3W2NVG5u6ibA9aDyzsF8I/640?wx_fmt=jpeg&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/8C1NLS8ickpfHuRbxczmKK36HLRfSVxysIgBAQMVFSdVGCDascdwN2jmE6LickWQ9nyK1k0fVcibLIYwaseCvT2VtXEoVubWyMLdmf9jRo59JY/640?wx_fmt=jpeg&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/8C1NLS8ickpd5O3toB6xb2AkuS2RcTBYTLu0nY8LibtS5iaZCyjdwbYYvsFA52ib67sdZdjG5Irwcs962K5KttO7qbKW4eEBYNtKkJUKBfHGI0s/640?wx_fmt=jpeg&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_jpg/8C1NLS8ickpd8PSnWIlP6x8ytDuhBpQc307z6BWzOD6flZLjlIYYXXU1NKpN5gXPjeq2mAPqgJm6Bd82h2IOL1rNSU0REl8Z7LOmpoU1NjS4/640?wx_fmt=jpeg&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_jpg/8C1NLS8ickpcGyRCee3d61E6ibYFh5VeHPicnicIloE3Iia6Bvud9Ok8cJOYYu0s4aIIXNltmfiagic87u2yvKdIDY6Px4iaaFwOh1h0B17rs0nibSlo/640?wx_fmt=jpeg&from=appmsg)

**<**

**滑动查看下一张图片**

**>**

******END****

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