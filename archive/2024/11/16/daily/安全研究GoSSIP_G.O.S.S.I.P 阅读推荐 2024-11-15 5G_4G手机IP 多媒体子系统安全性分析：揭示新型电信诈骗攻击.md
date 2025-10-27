---
title: G.O.S.S.I.P 阅读推荐 2024-11-15 5G/4G手机IP 多媒体子系统安全性分析：揭示新型电信诈骗攻击
url: https://mp.weixin.qq.com/s?__biz=Mzg5ODUxMzg0Ng==&mid=2247499205&idx=1&sn=1d73f0f3956a77bf13dd40102e1b544b&chksm=c063d31cf7145a0ac183f1eef8f69ee75ace35abe828e1d7dc0eebcdcb2964901704433bdb64&scene=58&subscene=0#rd
source: 安全研究GoSSIP
date: 2024-11-16
fetch_date: 2025-10-06T19:18:03.967198
---

# G.O.S.S.I.P 阅读推荐 2024-11-15 5G/4G手机IP 多媒体子系统安全性分析：揭示新型电信诈骗攻击

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/uicdfzKrO21H58cvTyFaiaAKkqSZA5OqsIkYmUDia5QnZJSlcAic6JVIaBBkHxUibibmvcrDfcKibJapicaVFVibDiaoV8iaQ/0?wx_fmt=jpeg)

# G.O.S.S.I.P 阅读推荐 2024-11-15 5G/4G手机IP 多媒体子系统安全性分析：揭示新型电信诈骗攻击

Jingwen

安全研究GoSSIP

今天为大家推荐的论文是来自Mobicom 2024的IMS is Not That Secure on Your 5G/4G Phones，由密歇根大学Guan-Hua Tu完成并投稿。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/uicdfzKrO21H58cvTyFaiaAKkqSZA5OqsIibHUWHhR5ZVnXvUIEM9xbY1e3jVYoLUIqTicAv8W7D9BzVy78pMUx9CQ/640?wx_fmt=png&from=appmsg)

**摘要**

本文对 IP 多媒体子系统（IP Multimedia Subsystem, IMS）在当前 5G/4G 移动设备上的安全性进行了详细分析。IMS 是在移动网络中利用IP 技术提供多媒体通信服务（如语音、视频通话和SMS短信）的核心系统。尽管 3GPP 在过去二十年里不断更新 IMS 系统以增强其安全性，使其能够支持 4G LTE、5G NR 以及 Wi-Fi 等多种无线接入网络，**但主要的安全性增强集中于网络基础设施，而手机设备端的 IMS 安全性未能及时升级**。

这种差异导致了设备端（如Android手机）出现许多新的安全漏洞和攻击途径。本文揭示了四个新的漏洞，并开发了三个概念验证攻击，展示了这些漏洞的潜在威胁：

* NameSpoofing攻击，一种短信欺骗攻击，可以任意伪造发送者的名称，这在网络中是被禁止的 （如图1）。

  ![](https://mmbiz.qpic.cn/sz_mmbiz_png/uicdfzKrO21H58cvTyFaiaAKkqSZA5OqsI7cic7dGvUeiavwuCkFkXXSf7tHe2fJib4XEHb9dxm7AX8Qhvefgbhvw7A/640?wx_fmt=png&from=appmsg)

  图1 NameSpoofing攻击效果
* DoS-ALL攻击，一种新型的拒绝服务攻击（DoS），可以阻止IMS客户端通过Wi-Fi、4G LTE和5G NR访问所有接入网络（如图2）。

  ![](https://mmbiz.qpic.cn/sz_mmbiz_png/uicdfzKrO21H58cvTyFaiaAKkqSZA5OqsIfNog9BFQcFCb5w1jX6AJKjDRySA3JX4rQXw01FU0GibUCEBxSS3iavQw/640?wx_fmt=png&from=appmsg)

  图2 DOS-ALL攻击效果。IMS services over Wi-Fi(左),4G (中),和5G (右）
* ViIMS-ANY攻击，利用IMS视频通话（Video over IMS, ViIMS）作为两个恶意移动设备之间的隐蔽通信渠道，伪造视频流传输任意信息，从而绕过运营商的服务策略。

**IMS 的架构与安全概述**

![](https://mmbiz.qpic.cn/sz_mmbiz_png/uicdfzKrO21H58cvTyFaiaAKkqSZA5OqsIn4Q0JT9SicVvMiclsAr4As0NicVONUMLHjgLc79nqDmYicwVYrVKxw1GUQ/640?wx_fmt=png&from=appmsg)

图3 (a)5G/4G 移动网络架构与(b)安全; (c)移动终端架构与漏洞。

5G/4G移动网络架构分为控制平面和用户平面（图3 （a）），用户流量从用户设备（User Equipment，UE， 包含SIM卡）经过无线接入网络到核心网络，最终进入互联网或IMS。控制平面管理用户的注册、认证和移动性，而用户平面通过多个IP流支持不同的服务质量（QoS）等级，以保障多媒体服务和移动宽带服务的性能。

5G/4G的安全架构分为应用、服务和传输三层 （图3 （b）），具有四个安全域以保障不同的通信安全。该架构显示，**应用和移动设备之间的访问缺乏明确的保护**。

移动设备（User Equipment，ME）架构由软件和硬件组成（图3 （c）），其中软件部分包括操作系统和应用程序，应用程序分为IMS和非IMS应用。硬件部分包括应用处理器和蜂窝调制解调器，调制解调器提供蜂窝协议支持，并通过TFT(Traffic Flow Template)功能将数据包与指定的IP流关联。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/uicdfzKrO21H58cvTyFaiaAKkqSZA5OqsI3yMZjicuyAMhYJrWEE7vaiaToxqtxgSCFayHDicsGUBD3d0sy3YibBzMDg/640?wx_fmt=png&from=appmsg)

图4 IMS服务信令流

在 IMS 中，信令消息用于建立、维护和终止 IMS 会话，如短信和电话（图4）。

**漏洞与攻击分析**

1. 漏洞 V1：IMS 信令路由未保护

IMS 信令缺乏严格的路由保护，**攻击者可以将信令消息重定向到非 IMS 服务器，导致设备无法与 IMS 服务器正常通信**。这一漏洞主要由以下原因造成：

Linux根据目标IP查询路由表，以找到最佳匹配项并做出路由决策。“本地”路由表的优先级高于IMS信令路由表（图5）。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/uicdfzKrO21H58cvTyFaiaAKkqSZA5OqsIUMy540eHHib2Czzz5QUz7p9za9ZsfwcmhniaBqn8qKOhAA6vfQ8xd8Cg/640?wx_fmt=png&from=appmsg)

图5 Routing Policy Database(RPDB)中路由表的查询优先级。

接下来研究利用了两个发现：

发现1. 攻击者是否可以向本地表添加路由规则？可以，我们可以通过VPN或Wi-Fi接口向本地表插入规则。

发现2. 攻击者是否可以将IMS服务器IP分配给VPN/Wi-Fi接口？可以，恶意VPN可以使用Java API，而恶意Wi-Fi可以使用DHCP （图6）。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/uicdfzKrO21H58cvTyFaiaAKkqSZA5OqsIdNBlhXkcWIgVLmRrBVG297Z9DnJbtVyx1nWTk0L0fLvyzVxZ1o9Ilw/640?wx_fmt=png&from=appmsg)

图6 Local路由表中添加VPN网络接口，并分配IMS服务器地址

攻击方式：利用这一漏洞，攻击者可以配置用户的 Wi-Fi 或 VPN 网络接口，使其指向 IMS 服务器的 IP 地址。而研究人员发现，IMS 服务器的 IP 地址在一个区域内十分稳定有限，而同一个网络接口可以同时被分配多个IP地址。这样一来，所有的 IMS 信令消息都被重定向，导致设备无法正常使用 IMS 服务（DoS-ALL攻击）。实验表明，在多个 Android 系统版本和不同运营商的网络中，这种攻击都能实现。

2. 漏洞 V2：IMS 信令来源无限制

IMS 信令在实现上依赖于双向的 IPsec 安全关联（Security Associations，简称 SA），其目的是保护信令消息的加密性和完整性。然而，研究表明，**IMS 标准并未规定信令消息必须来自 IMS 服务器，这意味着恶意应用可以向 IMS 客户端发送伪造的信令消****息**。因此研究发现，Android 8及以下版本手机，可从任意地址向IMS client发送伪造的信令消息（如SMS）。Android 8以上版本手机虽然会检查是否从IMS server地址发送，但利用漏洞v1可以绕过该安全机制。

攻击方式：实际中，这一漏洞可以被用来进行短信来源伪造攻击（NameSpoofing），攻击者可以伪造短信的发送者，使其显示特定的昵称，从而增加攻击的隐蔽性和欺骗性。

例如，攻击者可以在短信发送者字段中填入“认证自 Verizon 的 Mark Zuckerberg”，使接收者误以为这条信息是由合法的IMS服务器发出的（如图7）。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/uicdfzKrO21H58cvTyFaiaAKkqSZA5OqsIk9ZicneHOWAG3x6xOPVia2FHupDvggpqyTqNRDN3fw3icjDa4GwCj9ic0A/640?wx_fmt=png&from=appmsg)

图7 IMS信令伪造短信并显示任意发送者名字

3. 漏洞 V3：IMS 视频数据传输不安全

本文研究发现，**IMS 在视频数据传输中没有使用加密保护机制，导致视频数据在传输过程中处于明文状态（图9）**。并且不同于语音数据由硬件部分控制从modem直接传输到基站，视频数据流是从应用处理器（Application Processor）中生成的，有root情况下，可轻易被恶意应用劫持。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/uicdfzKrO21H58cvTyFaiaAKkqSZA5OqsIg5QpljFdEgW9Mls4mRGySEiah02oeT3osiaUUIoDQX2pG3DQlnQgt80A/640?wx_fmt=png&from=appmsg)

图8 IMS视频数据以明文传输

攻击方式：攻击者可以使用 IMS 视频通道传输非视频数据，而不易被网络发现。例如，恶意用户可以通过伪造视频数据包，将敏感数据放入伪造视频数据包中。

4. 漏洞 V4：IMS 视频数据来源无限制

研究还发现，**设备端的调制解调器无法验证从应用处理器过来的 IMS 视频数据的来源**。因为流量流模板（Traffic Flow Template，TFT），基于五元组（源/目标IP地址、源/目标端口号、协议ID）信息将数据包与每个指定的IP流关联。而这五个元素可以用IP Spoofing被轻易伪造。这意味着，IMS 视频会话中可以注入由非 IMS 客户端发起的数据包。

攻击方式：利用此漏洞，攻击者可以绕过 IMS 视频传输的安全机制，以隐蔽的方式传输大量非视频数据，将敏感数据发送至远端，绕过运营商的监控（图9）。与普通数据通道不同，IMS 视频通道具有更高的传输优先级和稳定性，攻击者因此可以在拥塞环境中继续隐蔽通信。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/uicdfzKrO21H58cvTyFaiaAKkqSZA5OqsIvVdDia4GhibEdG7rEmxiaaVc64u9sODdOK01JPQTIia1iblYDwNl4FNerhg/640?wx_fmt=png&from=appmsg)

图9 ViIMS-ANY攻击示意图

**解决方案与评估**

针对这些漏洞，我们提出了符合 3GPP 标准的应对方案，以改善 IMS 的整体安全性。

1. 限制 IMS 路由

针对漏洞 V1 和 V2，研究人员提出了限制 IMS 路由的解决方案。该解决方案包括以下两方面：

（1）禁止本地网络接口使用 IMS 服务器的 IP 地址：确保 IMS 信令消息只能通过指定的 IMS 服务器传输，避免信令被恶意程序拦截。

（2）阻止本地应用与 IMS 客户端直接通信：手机系统应当强制限制 IMS 信令的路由，确保所有 IMS 消息来源合法，避免恶意应用伪造信令。

2. 保护 IMS 媒体会话

研究人员建议在 IMS 客户端和调制解调器之间建立安全通信通道，以保护 IMS 视频数据的来源真实性。采用基于 DHKE（Diffie-Hellman Key Exchange）的密钥交换协议，通过利用原有的IMS安全通信通道，在 IMS 客户端和调制解调器之间建立共享的加密密钥，以保护 IMS 视频数据的端到端安全性。这种方法确保即使设备被恶意控制，通信安全性依然能够得到保证。

**结论**

尽管 IMS 在基础设施层面的安全性已经取得显著进展，设备端的安全性尚未得到足够关注，暴露出多种安全风险。本文分析了设备端的 IMS 安全漏洞并提出了相应的解决方案。我们已将所有已识别的漏洞报告给相关方，包括移动操作系统供应商、手机制造商和运营商。同时，也向他们提供了建议的补救措施。Google, Samsung正在积极修复相关问题。未来，手机制造商、网络运营商和标准化组织需共同努力，进一步提高 IMS 的设备端安全性，确保用户通信的隐私和安全。

论文地址:

https://www.researchgate.net/publication/380996237\_IMS\_is\_Not\_That\_Secure\_on\_Your\_5G4G\_Phones

作者简介：

石婧文，现为密歇根州立大学计算机科学与工程系博士候选人，师从Guan-Hua Tu教授。研究生毕业于中国科学院，导师须成忠与叶可江教授，本科毕业于湖南大学，指导老师为肖晟教授。曾在AT&T实验室、洛斯阿拉莫斯国家实验室以及阿里云担任研究实习生。主要研究领域涵盖移动系统与网络安全、分布式系统与人工智能系统结合。近期研究方向聚焦5G物联网与车联网、O-RAN技术。期待与各界同行共同探索，交流学习！

个人主页: https://shijingwen.github.io

导师主页：https://www.cse.msu.edu/~ghtu/

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/uicdfzKrO21EibxMcqx9KdafugxDicBiaW3cb1gyTuWooDCJjH1ibu8aibOiapYLq8BJMwNbIeUK1t0japdvmdqTfCxhg/0?wx_fmt=png)

安全研究GoSSIP

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/uicdfzKrO21EibxMcqx9KdafugxDicBiaW3cb1gyTuWooDCJjH1ibu8aibOiapYLq8BJMwNbIeUK1t0japdvmdqTfCxhg/0?wx_fmt=png)

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