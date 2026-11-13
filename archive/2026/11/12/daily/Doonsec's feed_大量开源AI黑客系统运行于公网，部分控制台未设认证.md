---
title: 大量开源AI黑客系统运行于公网，部分控制台未设认证
url: https://mp.weixin.qq.com/s/IYrtQc2Wa4abGv3yQd9b4A
source: Doonsec's feed
date: 2026-11-12
fetch_date: 2026-11-13T08:58:16.200095
---

# 大量开源AI黑客系统运行于公网，部分控制台未设认证

# 大量开源AI黑客系统运行于公网，部分控制台未设认证

FreeBuf

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

![FreeBuf](https://mmbiz.qpic.cn/mmbiz_gif/icBE3OpK1IX1KXRgTKaibklxQN695m0fiapevDmW3XyvwcHbNNobj4auIbN8ElBGMosDOCCfjiaDDFBullQMcJC1ERteyUgSFQa5SZDTPCH5IL0/640?wx_fmt=gif)

![](https://mmbiz.qpic.cn/mmbiz_png/icBE3OpK1IX1e9KVJ59JoouYhBUgSXPhzW9ibk5Ym4Spn5hiaRm4nNdgcZ1UKWYq99rUJbDyzNzjlJZmnicBxiaZ3H6J4ouwYzPsnCyEBSGIVUHw/640?wx_fmt=png&from=appmsg)

目前多款AI驱动的黑客与渗透测试框架正运行在可公开访问的互联网服务器上，部分框架的管理控制台未设置身份认证，完全对外开放。

2026年11月7日的Shodan快照数据显示，公网共有1428个服务属于ARTEX系列、419个服务匹配PentAGI特征、173个服务匹配Agent Zero特征，可见这类工具的传播范围已经十分广泛。

这类平台将语言模型与安全工具连接，支持Agent运行命令、核查结果并自主决策下一步操作。

这类工具可用于合法授权的渗透测试，但攻击者同样能利用这些功能，自动完成侦察、漏洞利用、凭据窃取等活动。不过，仅凭服务可被公网访问这一点，无法证明对应服务器正用于犯罪活动。

GitGuardian研究人员在11月9日发布的技术调查报告中，披露了这些暴露在公网的框架部署实例。本次调查针对的是两用框架的不安全部署问题，并非新发现的恶意软件家族。

研究团队共梳理了约45个开源项目，为其中41个项目提取了特征指纹，防御方可借助这些指纹定位公网上的相关部署实例。

![](https://mmbiz.qpic.cn/mmbiz_png/icBE3OpK1IX1pldBYBHrf6XG0BydlHtcSxwKrCfmdmQC6shwlbuHvaHjxZOLGEdnbeY707ozhIcO9gVLnnYGibaZjgvMLlB1bwaF3xSm1fg1U/640?wx_fmt=png&from=appmsg)

Part01

32款AI黑客框架分为五类

GitGuardian共将32款框架分为五大类：网络攻击自动化类、Web应用与API测试类、C2集成类、编码Agent封装类、研究原型类。其余项目均为这些框架的分支或变种。在受评估的41款框架中，11款默认开启Web管理界面，18款仅在特定配置下才会对外暴露服务，或根页面无明显识别特征，剩余12款未设置网络监听端口。

PentAGI可调度Agent调用Nmap、Metasploit、sqlmap等工具，这种设计能支持Agent在资产发现、漏洞测试、报告生成环节之间自动流转，与此前PentAGI渗透测试自动化相关报道中的描述一致。GitGuardian共统计到419个匹配PentAGI特征的服务，其中233个使用默认证书；通过页面标题、证书特征单独检索得到的结果数量存在差异，不可将不同维度的检索结果直接相加，统计独立服务器的总数量。

Agent Zero的认证缺失问题更为明显。在173个匹配特征的服务中，134个显示登录页面，剩余39个完全开放无需认证。GitGuardian指出，Agent Zero是一款默认未配置身份认证的通用Agent，并非专门的黑客工具。本次统计将其纳入范畴，是因为目前已出现攻击者尝试利用该工具的案例，且功能强大的Agent可被公网直接访问本身就会带来风险。

ARTEX是公网可见规模最大的框架家族。GitGuardian提到，原项目作者在收到滥用举报后，已于10月8日删除原始项目，但删除当周就出现了102个代码分支和同名代码仓库。此前针对ARTEX窃取GitHub凭据事件的报道显示，攻击者可利用暴露的应用密钥访问Azure Key Vault等云资源。

Part02

框架内置能力有限

Agent自主调用工具仍存安全风险

研究团队在代码审计中，还区分了框架内置功能与Agent可自主组装的任务模块。仅Pojun、Cybermes、Xalgorix、AIRecon四款框架内置了与Agent连通的密钥扫描器。所有受评估框架均未内置GitHub数据抓取模块。其余部分项目仅提供扫描功能的使用说明，并未实际集成可用的扫描器；包括PentAGI在内的受评估工具，均未检测到密钥搜寻能力。

但这类功能缺失并不代表没有风险。几乎所有框架都提供Shell访问和Web访问能力，语言模型可在运行过程中自行获取缺失的工具，或搭建对应的工作流。此前关于AI Agent凭据暴露风险的相关报道也提到，即便不存在恶意代码，Agent的常规活动也可能将密钥带入日志、交互记录或模型上下文当中。

对防御方而言，二者的区别十分关键：暴露的管理控制台属于明确的访问控制风险，而特征指纹匹配仅能作为发现线索。GitGuardian本次仅公开了检测特征说明，未公布暴露实例的目标清单，方便各机构排查自身的相关部署。不同检索规则得到的统计结果存在差异，因此企业在将检索结果判定为暴露部署或入侵证据前，必须先完成核实验证。

Part03

公布失陷检测指标

![](https://mmbiz.qpic.cn/sz_mmbiz_png/icBE3OpK1IX0EyfALPcRVmiaS9MYrLTe0oO9ibOUpuF3DHtd3zuzX3bpbVRQe3Dha24tQ5iaSUDmzVFMl2ybeqfQCWrlNIh2f4yCHibnxtPu1jiaU/640?wx_fmt=png&from=appmsg)

注：相关IP地址与域名均会做无害化处理（例如将.替换为[.]），防止意外触发解析或跳转。仅可在MISP、VirusTotal或企业内部SIEM等受控威胁情报平台中恢复原始地址。

参考来源：

AI Hacking Frameworks Like ARTEX, PentAGI, and Agent Zero Found Running on Internet-Accessible Servers

https://cybersecuritynews.com/ai-hacking-frameworks/

###

### **推荐阅读**

[![](https://mmbiz.qpic.cn/mmbiz_png/icBE3OpK1IX3Wh05Z0rN9nVQTjUXnyXs6uYnM9oo6THt2FhXmXzcuMkHbceiatCbhz8mR2zDd0yicfXLAnN2mwPzVRz1C0ibPQ0ocMnNt16QAkg/640?wx_fmt=png&from=appmsg)](https://mp.weixin.qq.com/s?__biz=MjM5NjA0NjgyMA==&mid=2651349303&idx=1&sn=86458815b0d0b880c32e19864a449a98&scene=21#wechat_redirect)

###

### **电报讨论**

![](https://mmbiz.qpic.cn/sz_mmbiz_png/icBE3OpK1IX2cCEVtIlLczLq1S4rms9uYa8x5Xedy0Il667ib20FMyHawNapLuHBl3peZxWoStYkAJdBcMicfmy9icChQA8uKfBib5EPaMicU5ykw/640?wx_fmt=png&from=appmsg)

![扫码加入AI安全交流群](https://mmbiz.qpic.cn/mmbiz_png/icBE3OpK1IX0Py7ibxdLKXia1pMziaic5vIE9XPXG9OGaeJDa07iaG10eicuzhW59nwpF5msHiaYZvfMqCNkx2aFDiaMzm3oAf4rTaHXU5UAI1mUYgts/640?wx_fmt=png)

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/qq5rfBadR3ibLOEAnkkKa2dHtqcjZ55KLsqibib6n4UDNUhLIuMRdAJ9ibfZkSK5LViaGJLEQN7p9OGo7mNnVv3EmkQ/0?wx_fmt=png)

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