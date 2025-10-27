---
title: 【高级持续性威胁追踪】解析APT攻击事件之软件供应链攻击
url: https://mp.weixin.qq.com/s?__biz=Mzg2NjgzNjA5NQ==&mid=2247517657&idx=1&sn=ff37f877c5a51b3b54cfb610d30064a2&chksm=ce460ec9f93187df8ad92161c16adefd0b5416d1b240c259c05e1e2a3591f7c5bd7d64e74df6&scene=58&subscene=0#rd
source: 深信服千里目安全实验室
date: 2023-03-07
fetch_date: 2025-10-04T08:49:41.863642
---

# 【高级持续性威胁追踪】解析APT攻击事件之软件供应链攻击

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/w8NHw6tcQ5zWSibPB7Y20xYB8EOibmiaib0JMe7sg6OePag4sYXXczRwbzHBU06Bbf4v3fvrcUGcIrravUWI2qX0MQ/0?wx_fmt=jpeg)

# 【高级持续性威胁追踪】解析APT攻击事件之软件供应链攻击

深瞻情报实验室

深信服千里目安全技术中心

**概述**

供应链攻击技术是APT攻击组织常用的攻击技术之一，也是最近一些年APT攻击组织使用最多的攻击方式之一，主要针对特定的企业和用户进行定向攻击活动，供应链攻击方式多种多样，软件供应链攻击是供应链攻击当中比较主流的一种攻击方式，基于软件源代码、开源软件第三方包和软件开发工具相关等攻击都是软件供应链攻击。

基于软件源代码的攻击方式，APT攻击组织攻陷软件供应商之后，然后将恶意代码直接嵌入到软件供应商的软件代码当中，然后通过软件供应商将包含有恶意代码的软件分发给该软件供应商的企业客户，导致所有使用该软件的企业客户全部中招，这种供应链攻击方式非常隐蔽，也是危害最大的一种攻击方式，此前SolarWinds供应链攻击事件就是一种基于软件源代码的攻击方式。

基于开源软件第三方包的攻击方式，APT攻击组织利用PyPI、NPM等第三方包进行供应链攻击，这种攻击方式可以定向攻击一些大型企业的开发人员，再通过窃取这些开发人员的登录凭证等信息之后，进行后续的渗透攻击活动，渗透到企业内网，进行更隐蔽的APT攻击活动。

基于软件开发工具相关的攻击方式，APT攻击组织利用伪造的包含恶意软件的软件开发工具或者被感染了恶意代码的软件开发工具的工程项目文件，诱骗企业开发人员安装或使用这些软件开发工具和工程项目文件，安装木马后门进行下一步的攻击活动，Lazarus APT攻击组织就曾利用这种攻击方式，通过感染了恶意代码的软件开发工具的工程项目文件，定向攻击安全研究人员，此前XCodeGhost供应链攻击事件也是这种基于软件开发工具的攻击方式。

三种攻击方式中，基于软件源代码的攻击方式是最隐蔽，最难发现，也是技术难度最高的一种攻击方式，因为它需要先通过其他攻击方式对相应的软件供应商企业进行定向攻击之后，再进行后面的基于软件源代码的供应链攻击活动，同时需要确保在攻陷软件供应商之后长时间不被该供应商企业发现，这是非常难的，同时还需要向供应商相应的软件植入恶意代码，整个过程也需要做的非常隐蔽，所以这种攻击方式是很难实现的,基于开源软件第三方包和基于软件开发工具相关的软件攻应链攻击方式是相对容易实现的供应链攻击方式。

深信服蓝军APT研究团队一直致力于研究各种APT组织攻击手法TTPs等，基于一些真实的攻击事件对软件供应链攻击活动进行了深入的研究，分析了基于开源软件第三方向的攻击方式和基于软件开发工具相关的攻击方式。

**分析**

2023年1月，安全研究人员披露了某攻击者针对一款领先的流行机器学习框架PyTorch进行供应链攻击活动，PyTorch是一个流行的Python开源机器学习库，总下载量约1.8亿次，提供了广泛的工具来训练和部署机器学习模型，特别适合深度学习。

第三方包解压之后，在runtime目录下包含恶意脚本和恶意程序，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/w8NHw6tcQ5zWSibPB7Y20xYB8EOibmiaib0JxgZnfibDNP84jxL2sxbBvkzLeRysu7JIXC9bsVVULuBkYfvqPZINrcA/640?wx_fmt=png)

通过\_\_init\_\_.py初始化脚本，启动目录下的triton恶意程序，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/w8NHw6tcQ5zWSibPB7Y20xYB8EOibmiaib0JmwkocaBXsHE12m123WqfWOJqIKuaIB4IwLFWgPMAcLVJMpHajvReaQ/640?wx_fmt=png)

利用PyPI第三方包进行软件供应链攻击，主要通过在PyPI第三方包程序setup.py和\_\_init\_\_.py脚本里面加入经过编码混淆过的恶意代码，相关POC工具代码，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/w8NHw6tcQ5zWSibPB7Y20xYB8EOibmiaib0Ju7UmXIGI84Hz5MBnVGWMhe8GVB2UUkA5YZkeWn5IK25ORCYm42H3GQ/640?wx_fmt=png)

2021年1月，深信服蓝军APT研究团队披露了Lazarus APT组织通过在VS项目中设置预构建事件命令，进行基于软件开发工具相关的供应链攻击，当运行受感染的VS软件开发工具的工程项目文件之后，恶意代码会调用rundll32执行VS项目中附带的恶意64位的DLL文件，感染后的VS软件开发工具的工程项目文件，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/w8NHw6tcQ5zWSibPB7Y20xYB8EOibmiaib0Jpb1RjgpaYfUOWyAGjI1EeibBric2GWdhguuzgEjLSl8NMOkhJI9PRnew/640?wx_fmt=png)

Lazarus APT组织通过上述的供应链攻击方式，目的是为了定向盗取安全研究人员的0day漏洞等，近日该攻击方式的POC被公开，深信服蓝军APT研究团队第一时间进行了跟踪分析，主要分为两步，第一步搜索vcxproj程序源文件，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/w8NHw6tcQ5zWSibPB7Y20xYB8EOibmiaib0JGgCGv2gWOP0TecaVibyAtUeq6FAgxkzZibv2TLlWJRcjFcJnpNiaxtj1Q/640?wx_fmt=png)

然后对该源文件进行感染，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/w8NHw6tcQ5zWSibPB7Y20xYB8EOibmiaib0JhIKep2w3xhBVzGWQPDPRNrThiaJ7Kd0LEt00DGiaLJ5Bd9vwy6peGB3A/640?wx_fmt=png)

针对上面基于开源软件第三方包和基于软件开发工具相关的两种攻击活动，安全厂商可以针对开源软件的第三方包和软件开发工具的相关工程文件进行安全扫描，检测里面是否包含相关恶意代码特征等，同时可以检测第三方包的版本信息、描述字段等包信息特征。

**总结**

供应链攻击技术是最近几年APT组织攻击使用的最常用的攻击技术，未来随着全球云计算虚拟化等平台的高速发展，基于软件供应链攻击的活动可能会越来越多，要检测这种类型的攻击活动，不仅需要安全厂商各种安全产品，包含云(情报层面)+端(样本层面)+网(流量层面)联动，同时还需要专业的安全人员基于自己丰富安全经验才有可能发现这种高端隐蔽的APT攻击活动，事实证明，目前披露的一些高端的APT攻击组织往往在供应链攻击方面做的非常隐蔽，例如像SolarWinds这种APT攻击活动确实很难发现。

深信服蓝军APT研究团队专注全球高级威胁事件的跟踪与分析，拥有一套完善的自动化分析溯源系统以及外部威胁监控系统，能够快速精准的对 APT 组织使用的攻击样本进行自动化分析和关联，同时积累并完善了几十个 APT 以及网络犯罪威胁组织的详细画像，并成功帮助客户应急响应处置过多个 APT 及网络犯罪威胁组织攻击事件，未来随着安全对抗的不断升级，威胁组织会研究和使用更多新型的 TTP，深信服蓝军APT研究团队会持续监控，并对全球发现的新型安全事件进行深入分析与研究。

**参考链接**

`https://mp.weixin.qq.com/s/n8vqqHdzj1j_Cf_HgBTsnQ`

`https://medium.com/checkmarx-security/py-torch-a-leading-ml-framework-was-poisoned-with-malicious-dependency-e30f88242964`

`https://www.fortinet.com/blog/threat-research/more-supply-chain-attacks-via-new-malicious-python-packages-in-pypi`

`https://checkmarx.com/blog/how-npm-packages-were-used-to-spread-phishing-links/`

`https://blog.phylum.io/phylum-discovers-another-attack-on-pypi`

预览时标签不可点

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