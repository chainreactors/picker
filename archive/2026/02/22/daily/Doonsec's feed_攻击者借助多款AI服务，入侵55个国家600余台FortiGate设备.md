---
title: 攻击者借助多款AI服务，入侵55个国家600余台FortiGate设备
url: https://mp.weixin.qq.com/s/elhS-Yrk4MFCekb5oaOlRw
source: Doonsec's feed
date: 2026-02-22
fetch_date: 2026-02-23T04:16:35.318242
---

# 攻击者借助多款AI服务，入侵55个国家600余台FortiGate设备

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/icBE3OpK1IX39ibPF0icwEYmoA0iaib0BZuDvxtgk9Y4a7KBYWn0yC8ic9yxS4MpkpCqXHGpHtGvP2nySzVrIcSQia7UdUmh7pk88a62av9HYoAYlY/0?wx_fmt=jpeg)

# 攻击者借助多款AI服务，入侵55个国家600余台FortiGate设备

FreeBuf

![]()

在小说阅读器中沉浸阅读

![](https://mmbiz.qpic.cn/mmbiz_gif/qq5rfBadR38jUokdlWSNlAjmEsO1rzv3srXShFRuTKBGDwkj4gvYy34iajd6zQiaKl77Wsy9mjC0xBCRg0YgDIWg/640?wx_fmt=gif)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/icBE3OpK1IX2nw76ibH55Zgy1qsTOnZ02Y7B3ejGpULTiacGZR20JbR7v9n8EIDyOmcnLZRYDs7kj7Mdibbdb7jhlFhrjYgVJF8SbtoUhBianpp8/640?wx_fmt=png&from=appmsg)

##

**Part01**

## ****大规模入侵事件概述****

2026年1月11日至2月18日期间，一个以经济利益为动机的威胁行为体利用多种商用生成式AI服务，成功入侵了55个国家超过600台FortiGate设备。此次攻击活动标志着AI技术降低网络攻击的技术门槛，使个人或小型团队能够执行以往需要大规模专业团队才能完成的攻击。

威胁行为体的初始访问完全依赖于对暴露在互联网上的FortiGate管理界面进行凭据利用，未涉及0Day漏洞或新型攻击技术。攻击者通过系统性地扫描443、8443、10443和4443端口，识别出使用弱密码或重复密码且仅采用单因素认证的设备。

**Part02**

## ****高价值配置数据泄露****

从FortiGate设备提取的配置文件被证明具有极高价值，包含：可恢复密码的SSL-VPN用户凭据、管理员凭据、完整网络拓扑数据、IPsec VPN对等配置以及揭示内部架构的防火墙策略。攻击者使用AI辅助的Python脚本对这些配置进行解析、解密和组织，实现了高效的规模化凭据收集。

攻击目标呈现机会主义特征而非针对特定行业，这与自动化大规模扫描行为一致。但亚马逊威胁情报部门发现，当同一实体的多台FortiGate设备被入侵时，会形成组织级入侵模式，包括与托管服务提供商部署相关的设备集群。受感染设备主要集中在南亚、拉丁美洲、加勒比地区、西非、北欧和东南亚。

**Part03**

## ****AI驱动的攻击流水线****

亚马逊威胁情报确认，威胁行为体在攻击每个阶段都至少依赖两种不同的商用大语言模型服务。其中一种LLM作为主要工具开发者和攻击规划者，另一种则作为在已入侵网络中横向移动的辅助工具。

在一个记录案例中，攻击者将完整的受害者网络拓扑（包括IP地址、主机名、有效凭据和已识别服务）直接输入AI服务，并要求提供逐步横向移动指导。亚马逊分析师将此操作描述为"网络犯罪的AI驱动流水线"。

**Part04**

## ****攻击手法技术细节****

攻击者在入侵后采用结构化方法：部署带有Mimikatz模块的Meterpreter对域控制器实施DCSync攻击，成功从多个Active Directory环境中提取完整的NTLM凭据数据库。在至少一起已确认的入侵事件中，域管理员账户使用了从FortiGate配置中复用的明文密码或独立设置的弱密码。

横向移动通过哈希传递、票据传递和NTLM中继攻击实现。攻击者专门针对Veeam备份与复制服务器，使用PowerShell脚本和编译的解密工具，通过破坏备份基础设施为后续勒索软件部署消除恢复能力。

**Part05**

## ****攻击者技术局限性****

##

尽管规模庞大，亚马逊分析显示攻击者存在持续的技术局限。他们在面对强化防护环境时屡屡失败（其操作笔记中有记载），并会放弃防御有效的目标，这证实其优势在于AI增强的效率和规模而非技术深度。

他们用Go和Python编写的AI生成侦察框架显示出初级开发特征：重复注释函数名、通过字符串匹配进行简单JSON解析以及空文档存根。

**Part06**

## ****相关漏洞信息****

##

![](https://mmbiz.qpic.cn/mmbiz_png/icBE3OpK1IX3MLsqR8VAD8B2bianr4iaicsoAkgDsSoT33t1xuuuMOickEZicpF28dSy2HviaoicicN791VMBoNaIw9j0mX8WqXInSlqAOAfK2wbeyuA/640?wx_fmt=png&from=appmsg)

**Part07**

## ****防御建议与IOC信息****

##

亚马逊已与相关行业伙伴共享入侵指标以协调受影响国家的应对措施。使用FortiGate设备的组织应立即：

* 将管理界面从互联网隔离
* 对所有VPN和管理访问强制实施多因素认证
* 轮换SSL-VPN和管理凭据
* 审计Active Directory中的DCSync活动（事件ID 4662）

鉴于此次攻击主要依赖包括Impacket、gogo和Nuclei在内的合法开源工具而非传统基于签名的IOC方法，强烈建议监控以下异常行为：

* VPN认证异常模式
* Active Directory非预期复制
* 备份服务器上未经授权的PowerShell模块加载

相关IOC如下图：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/icBE3OpK1IX3xXoibr096S5VE5dA9xicLfKSARfpC0vUagyIPtCDv5lMoXVkWXXaicBtKzOfjbYvHmWX8H1X88SPX2wYX1pKrc6EbiblHaia3VZhw/640?wx_fmt=png&from=appmsg)

**参考来源：**

Hackers Leveraging Multiple AI Services to Compromise 600+ FortiGate Devices

https://cybersecuritynews.com/600-fortigate-devices-hacked/

---

###

###

###

**推荐阅读**

[![](https://mmbiz.qpic.cn/sz_mmbiz_png/icBE3OpK1IX2W4PauSPeWFzibFnIaueGohexvlxGHlyQqibmSVMWnic1pgOiclspWRg4QB7OUqibzIeV7g8PQScBQcTOX8rGTGrk6t1tVfKCicKqZ8/640?wx_fmt=png&from=appmsg)](https://mp.weixin.qq.com/s?__biz=MjM5NjA0NjgyMA==&mid=2651334873&idx=1&sn=891ff82faea84feac5d8284ffe647d63&scene=21#wechat_redirect)

### **电台讨论**![](https://mmbiz.qpic.cn/mmbiz_png/qq5rfBadR3ibzefibicmDdQl5gbj0kdRbbL9PLvNj4Fx7nTwB10Y86ibaau2wMNuvs9xibztEUaON1ehhL0XgD8G5iaQ/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/qq5rfBadR3ibvNluUKZ6RPy7h2fbYibRbLQDHPFqj89KkFsXBRibx5YTLiaTUfFOy9PKicps3l56iazUPNQrwdhkZ7jA/640?wx_fmt=png&from=appmsg)

**![](https://mmbiz.qpic.cn/mmbiz_png/qq5rfBadR3ibqyrdrvYXibMZM7K7gQW9ymeNepaIkpwPmicPSSoVicLBPXZ3a19uvVicYOjUZOibNeYRbrIOToCHjLAg/640?wx_fmt=png&from=appmsg)**

预览时标签不可点

阅读原文

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/qq5rfBadR3ibLOEAnkkKa2dHtqcjZ55KLsqibib6n4UDNUhLIuMRdAJ9ibfZkSK5LViaGJLEQN7p9OGo7mNnVv3EmkQ/0?wx_fmt=png)

FreeBuf

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