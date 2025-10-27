---
title: 失陷的控制器网络--OT网络中的深度横向移动
url: https://mp.weixin.qq.com/s?__biz=MzkyMzAwMDEyNg==&mid=2247534477&idx=1&sn=5a0718283ed3f3d6967286f1db3f4174&chksm=c1e9cbdcf69e42ca98ddf739e462dec6a4bb0dc1ceb64e1a5643b3c7e5aa740c9f34ff66239c&scene=58&subscene=0#rd
source: 关键基础设施安全应急响应中心
date: 2023-02-16
fetch_date: 2025-10-04T06:46:35.896922
---

# 失陷的控制器网络--OT网络中的深度横向移动

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/iaz5iaQYxGogucGxHiarZB8tTB7ib3seJFajgtn7kLcI4foKSuq4CiaFiafRKxOox7JZiaAuTiataR0M12sqyv6JQBiaznA/0?wx_fmt=jpeg)

# 失陷的控制器网络--OT网络中的深度横向移动

安帝科技

关键基础设施安全应急响应中心

作者 | 北京安帝科技有限公司

**Forescout Technologies****的Vedere实验室当地时间2月13日推出了其关于深度横向移动的重磅研究报告。报告首次系统披露了攻击者如何在OT网络的控制器级别(普渡模型的1级(L1))的不同网段和不同类型网络之间横向移动。研究者展示了攻击者如何在连接的基本过程控制系统(BPCS)/安全仪表系统(SIS)体系结构中跨越安全边界，或在PLC后面嵌套的现场总线网络中对设备进行详细操作，以绕过功能和安全限制。这些限制功能作为最后一道防线，用于禁止网络物理攻击产生最严重的后果。L1级由监控和向0级设备发送命令的系统组成，典型的示例包括可编程逻辑控制器(PLC)、远程终端单元(RTU)和智能电子设备(IED)等。**

![](https://mmbiz.qpic.cn/mmbiz_jpg/GoUrACT176mUJcOZvQJ9RWV9IV7zTgexic8WWkkkJyfblVFuS5MBNmNpVtq6vBH9hKmVAanQd32alkmzSoEyL0g/640?wx_fmt=jpeg)

作为本研究开发的概念证明的一部分，研究人员使用了两个Vedere实验室首次公开披露的新漏洞:：CVE-2022-45788和CVE-2022-45789，分别允许在施耐德电气Modicon PLC上远程代码执行和身份验证绕过。这两个漏洞的发现是此前OT: 2022的Icefall研究成果的一部分，但在供应商的要求下，当时没有披露。

在过去的几年中，安全研究人员已经演示了各种方法来获得来自不同供应商的L1设备上的低级远程代码执行(RCE)。像TRITON和INCONTROLLER这样的恶意软件已经表明，现实世界的威胁行为者既有能力也有兴趣开发这种能力。**然而，当涉及到L1设备的后续利用时，先前的工作主要集中在隐身性、持久性和演示后果和影响上，而横向移动很少受到关注。过去横向移动的重点是在同一网段的L1设备之间移动或在级别2及以上向上移动到SCADA系统，但没有考虑在L1更深地移动到嵌套设备网络或跨边界。**

因此研究人员认为，资产所有者经常忽略第1级的安全边界，并认为绕过控制器和现场设备强制执行的功能和安全限制是不可行的，即让限制或约束条件失效所需要的细粒度控制，攻击者是达不到的。尽管L1设备位于多个混合网络的交汇处，应该被视为安全边界，并且应该具有与处于类似位置的工作站相同的相应强化措施和风险配置。

![](https://mmbiz.qpic.cn/mmbiz_jpg/GoUrACT176mUJcOZvQJ9RWV9IV7zTgexUJoug1pK5P1gnAuvlUZaqico2aokmWoY1MB0ZPgicJib9EwYPicHdOeSeg/640?wx_fmt=jpeg)

图1：普渡企业参考架构-引自ANSI/ISA-62443-2-1

**深度横向移动使攻击者能够深入访问工业控制系统(ICS)，并跨越经常被忽视的安全边界，使他们能够执行细粒度和隐秘的操作，并超越功能和安全限制。Forescout重点研究了造成L1级深度横向运动的两个主要原因——边界交叉和细粒度控制。将这种横向移动纳入攻击者视线的主要原因是需要重新评估边界。**

**首先，研究人员关注交叉边界的问题。**希望引起人们对一阶连通性分析的常见谬误的注意，其中风险评估只考虑对直接可达系统或组件的影响。其次，希望同样地引起人们注意这样一个事实，即许多OT系统架构师和集成商，以及一些供应商和监管指南，继续根据本地可路由性评估链路安全性，并确定地呈现功能，因此想当然地认为某些链路(串行、点对点、不可路由)比实际更健壮。

报告指出，攻击者可能需要在级别1的加固或未经确认的边界周围移动，以跨越不同的网段，研究人员给出了级别1的区域跨界的一个例子，即BPCS和SIS之间的交互。另一个通常被低估的OT网络中L1边界是连接到由现场总线耦合器调节的第三方控制系统(如PU或跨公用设施接口)。

![](https://mmbiz.qpic.cn/mmbiz_png/GoUrACT176mUJcOZvQJ9RWV9IV7zTgexjbWTRFML3ibUF94YUh2B5MsgI7zp016jTMAE2DqJjVia032RBlLsDbXw/640?wx_fmt=png)

图2：处于多个网络交叉点的L1级设备（引自Vedere实验室研究报告）

研究人员还评估说，这些设备越来越智能，具有复杂的协议转换能力和带内固件更新。在现实世界中遇到过几个案例，资产所有者基于现场总线耦合器的‘愚蠢’性质的假设设计了安全架构，结果证明这实际上是一个‘智能’设备，具有比预期更大的攻击面和横向移动的潜力。

**在细粒度控制措施方面，Forescout的研究人员透露，攻击者可能希望深入到L1级系统，因为他们需要对嵌套设备进行非常细粒度的控制，或者绕过功能和安全约束。**

Vedere实验室评估称，攻击者若要实现更具破坏性的场景，将需要在太阳能逆变器（solar inverter）或UPS主模块的负责数字信号处理器(DSP)上获取代码执行能力。为了获得这种访问权限，攻击者首先需要横向移动通过通信模块，也可能通过主模块的应用程序处理器(AP)。这种深度横向移动对评估个体脆弱性的潜在影响具有重要意义。

Forescout透露，作为最近针对OT的黑客攻击浪潮的一部分，GhostSec组织攻击了尼加拉瓜ISP UFINET的一个暴露的M340控制器，将值0写入其所有的Modbus寄存器。新发现的漏洞，只影响Modicon PLC Unity系列。CVE-2022-45788是通过未记录的内存写操作进行RCE的一个例子。此外，虽然施耐德电气将CVE-2022-45788描述为与下载恶意项目文件有关，但此漏洞实际上运行在完全不同的(未记录的)功能集上，允许修改内部PLC内存，而不影响PLC运行状态或需要项目下载。

![](https://mmbiz.qpic.cn/mmbiz_png/GoUrACT176mUJcOZvQJ9RWV9IV7zTgex1RdOibpQ4JluyVpsSjxrpWxp6NKeC9X7WdcT9DTemv1IYyLuAKDafNA/640?wx_fmt=png)

图3：嵌套系统的示例体系结构（引自Vedere实验室研究报告）

Forescout表示，Modicon PLC在世界各地非常流行和广泛使用。根据公共数据估计受影响设备的数量是困难的，因为这些设备不应该通过互联网访问。然而，Forescout仍然能够看到近1000个PLC通过Shodan在线暴露，主要是电力行业(44%)，其次是制造业(19%)和农业(15%)。他们还发现了多个公共子网实例，可能由系统集成商或承包商使用，暴露了用于不同发电项目的Modicon PLC。

为了证明深度横向移动的可行性，Vedere实验室针对几个流行的PLC(施耐德电气Modicon M350、Allen-Bradley GuardLogix和WAGO 750系列)组成的嵌套设备设置开发了一个概念验证利用链。该设置旨在禁止直接或路由访问关键控制器和安全系统，展示了高能力对手可能采用的技术来规避此类限制。

报告称:“我们构建的场景表明，攻击者试图控制可移动桥梁基础设施，意图实施网络物理攻击，以全速关闭桥梁，安全系统被禁用，要么用锁杆驱动撞击轴承，要么在全速触发紧急停车，造成巨大的惯性力损坏桥梁。”“这种情况通常很难，甚至不可能通过中央SCADA接口进行简单控制。”

Vedere实验室发现，将某些链路(如串行、点对点、射频和耦合器)视为“如果它们对我们在常规以太网LAN网络上看到的许多相同问题免疫，则需要进行严格的重新评估。”设备受损的影响不仅限于链路的显式功能或其一级连接性。“仅仅因为它只暴露了几个Modbus寄存器，或者连接到一个无趣的设备上，并不意味着攻击者不能把这个链接变成其他东西，并把这个无趣的设备作为一个过渡点或支撑点，向更有趣（有价值）的目标移动。”

报告披露称:“随着攻击者通过深度横向移动实现访问，可能会放大攻击的影响。”“降低深度横向移动的风险需要仔细监控混合网络，以尽早发现对手，在普渡模型较低的级别上监测经常被忽视的安全边界，并加固互连和暴露的设备。”

Vedere实验室表示，要评估协议栈漏洞的潜在风险，应该考虑到这种深度横向移动的容易程度。例如，考虑CIP解析器中的漏洞。如果漏洞只能用于导致拒绝服务，那么在哪里进行解析非常重要。毕竟，以太网模块上的DoS和CPU模块上的DoS之间的区别就是失去通信和失去保护或控制之间的区别。但是，如果该漏洞可以用来实现代码执行，那么即使解析发生在通信模块上，仍然存在失去保护或控制的风险，因为攻击者有可能将该模块用作CPU模块的枢纽。

该研究提供了通过禁用设备上未使用的业务来加固L1设备和网络的缓解策略。例如，如果PLC上不需要UMAS over Ethernet，请禁用它。即使PLC是嵌套的，因为报告中展示了攻击者如何利用嵌套设备上的漏洞实施攻击。

Vedere实验室还建议使用深度包检测(DPI)防火墙和基于IP的访问控制列表来限制工程工作站和PLC之间的敏感流量。在只需要协议子集的情况下，可以使用DPI来进一步限制。从取证的角度来看，摄取包含此类恶意活动指示器的1级事件日志，并通过OT-DPI防火墙和/或一致性检查网关(包括点到点链接)强制隔离。

该报告补充说，根据风险的不同，某些跨越高度敏感网段的点对点链路可能需要以太网专用的插入式DPI防火墙。“对于具有相似配置文件的串行链路，可能需要考虑在带外收集数据的内联分路器(inline taps)。”

2022年6月，Vedere实验室还详细介绍了一种新的攻击方法，称为物联网勒索软件(Ransomware for IoT)或R4IoT。概念证明涵盖了下一代勒索软件，这些勒索软件利用物联网设备进行初始访问，以IT设备为目标部署勒索软件和加密货币，并利用糟糕的OT安全实践对业务运营造成物理中断。通过损害物联网、IT和OT资产，R4IoT超越了通常的加密和数据泄露，导致业务运营的物理中断。

### **参考资源：**

1、https://www.forescout.com/resources/l1-lateral-movement-report

2、https://industrialcyber.co/ics-security-framework/vedere-labs-details-deep-lateral-movement-in-ot-networks-provides-mitigation-strategies/

原文来源：CNCERT国家工程研究中心

“投稿联系方式：孙中豪 010-82992251   sunzhonghao@cert.org.cn”

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/iaz5iaQYxGogvC8qicuLNlkT5ibJnwu1leQiabRVqFk4Sb3q1fqrDhicLBNAqVY4REuTetY1zBYuUdic0nVhZR4FHpAfg/640?wx_fmt=jpeg)

预览时标签不可点

阅读原文

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/sz_mmbiz_png/iaz5iaQYxGogvgetLSfCMn2pt4xU0Fs6mWM4P98FUya5sz3BvAIzZam7WzZ5aA1kWkKBicptwLzVRicaqAhZ1pceiaA/0?wx_fmt=png)

关键基础设施安全应急响应中心

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/iaz5iaQYxGogvgetLSfCMn2pt4xU0Fs6mWM4P98FUya5sz3BvAIzZam7WzZ5aA1kWkKBicptwLzVRicaqAhZ1pceiaA/0?wx_fmt=png)

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