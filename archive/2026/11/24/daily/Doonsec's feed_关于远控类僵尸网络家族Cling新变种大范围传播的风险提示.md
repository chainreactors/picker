---
title: 关于远控类僵尸网络家族Cling新变种大范围传播的风险提示
url: https://mp.weixin.qq.com/s/evZ9pVgU1aeoXbH1OgsKHQ
source: Doonsec's feed
date: 2026-11-24
fetch_date: 2026-11-25T10:40:21.908652
---

# 关于远控类僵尸网络家族Cling新变种大范围传播的风险提示

# 关于远控类僵尸网络家族Cling新变种大范围传播的风险提示

绿盟科技

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

以下文章来源于国家互联网应急中心CNCERT
，作者CNCERT

![](https://wx.qlogo.cn/mmhead/Q3auHgzwzM7x2UYGIAGwcwufoYr2R16synysQjwIEVJzwyjBcVT8Cg/0)

**国家互联网应急中心CNCERT**
.

国家计算机网络应急技术处理协调中心（简称“国家互联网应急中心”，英文简称CNCERT或CNCERT/CC），成立于2001年8月，为非政府非盈利的网络安全技术中心，是中国计算机网络应急处理体系中的牵头单位。

![](https://mmbiz.qpic.cn/mmbiz_png/aoXpXT1UJRgf8gaicNlle1rOEwXqD6WrQDcQk3iaAsucOxYoJmfcQqCg0qrAObheSnStArW0kysg5M0XBicOgJyuIDXuyeKc1Ly2uiaRBkIKrG4/640?wx_fmt=png&from=appmsg)

感谢绿盟科技伏影实验室在本报告的样本分析工作中做出的重要贡献。

一、概述

近期，国家互联网应急中心（CNCERT）监测发现，僵尸网络家族 Cling 的新变种正在大范围传播，主要针对 Linux 服务器及 IoT 设备。该木马采用创新性的通信机制，隐匿能力极强：其控制端隐匿于公共 STUN 服务之中，指令嵌入 STUN 事务标识（Transaction ID）字段，使控制流量隐藏于海量正常 STUN 交互之中，传统监测手段难以有效察觉。

 Cling木马演变速度极快，存在多个版本，本次传播的变种整体功能较为精简，移除了漏洞传播、代理、DDoS等模块，仅保留命令执行、程序下载与执行等核心功能，修复了早期版本控制端响应事务标识异常的缺陷，并使用ChaCha20算法对关键信息加密存储，伪装更难识破。攻击者的核心目的并非发动 DDoS 攻击，而是长期控制受害主机，将其作为投递其他恶意软件的跳板，危害性极高。2026年11月09日至11月20日期间，CNCERT监测发现该僵尸网络感染的日上线肉鸡数最高达到2730台，累计已有5600台设备受其感染。现将其主要情况分析披露如下。

二、恶意样本分析

![](https://mmbiz.qpic.cn/sz_mmbiz_png/aoXpXT1UJRhqYyTvichmZ9dKAILqDnCZc2Rq7Lu4icsN5Yiak6nanOC7wro5lBmFQanVt6mfFibE1lFkAnXicfRp3IjjUWIQhB7CyLXsIdbuKx4I/640?wx_fmt=png&from=appmsg)

图 1 Cling僵尸网络

1.传播方式

研究表明，新变种剥离了漏洞利用模块，监测到当前变种主要通过CVE-2021-35394传播，早期版本部分常用漏洞如下：

CVE-2016-10372（Eir D1000 router RCE）

CVE-2023-41011（FiberHome SR1041F router RCE）

CVE-2014-8361（Realtek SDK RCE）

CVE-2023-26801（LB-LINK routers RCE）

CVE-2024-3721（TBK DVR RCE）

CVE-2025-34037（Linksys RCE ）

CVE-2016-20016（MVPower CCTV DVR RCE）

2.通信机制

Cling木马将控制端隐匿于公共 STUN 服务之中，指令嵌入 STUN 事务标识（Transaction ID）字段，使其具备极高的灵活性与隐匿性。STUN 是查询 NAT 映射地址的标准协议，其报文头含一个 12 字节的“事务标识”字段，本应是一段随机数。Cling 新变种把控制数据藏进这个字段，使控制流量与正常 STUN 交互在外观上几乎无法区分。

![](https://mmbiz.qpic.cn/mmbiz_png/aoXpXT1UJRj8lLCTOazZnqhfoGCIsh4V3DEcnkcsnhCSCj4NthwjhctnlvgfPc9SopGLEiaTLxgjXjDDpVEC0Mp9LEic1tJFzj3kTK4IRo7kY/640?wx_fmt=png&from=appmsg)

图 2 Cling木马 STUN 上线与控制机制

伪装身份：木马内置 13 个 ChaCha20加密的STUN 服务器地址，其中 12 个为公共 STUN 服务器，1个为攻击者控制的 C&C，伪装成 STUN 服务参与交互，从嫌疑对象中彻底隐身。

获取 NAT 映射端口： 木马周期性向全部 13 个服务器发送标准 STUN Binding Request，合法 STUN 服务器正常响应，木马由此获知自身在 NAT 后的公网映射端口。该端口是后续接收指令的入口。

发送自定义注册消息：木马随后向全部服务器发送不符合 STUN 规范的自定义注册消息，携带映射端口和感染标签。合法 STUN 服务器按协议丢弃该异常消息；受控 C&C 服务器接收并记录，从而获知 bot 的映射端口和感染标签。

隐藏内容：之后 C&C 向该映射端口发送指令，指令藏在 STUN 报文的事务标识字段里，前 2 字节为识别标记、后 10 字节为加密任务参数。由于事务标识本就是随机值，控制数据与正常响应外观一致。

伪装来源：控制端下发指令时把源地址伪装成 Google STUN，让防守方看到的是一台全球知名 STUN 服务发来的正常流量。

3.核心功能

本次捕获的木马具备四类远程指令，可管理执行任务，并按需部署其他程序：

命令执行：连接指定服务器，获取并解密命令后交由系统运行。

程序加载：指令提供任务编号和下载服务器地址，木马先停止同编号旧任务，再下载新程序并赋予执行权限后启动。该能力使其可作为投递其他恶意软件的入口。

任务停止：按编号结束此前下载并启动的子进程。

节点更新：用指令给出的新地址替换列表中的节点，使后续上报能随控制要求调整。

4.持久化与对抗

配置加密：新变种采用 ChaCha20 隐藏内置配置、控制参数和远程命令，进一步提升了其隐匿性。

替换系统工具：木马替换常用下载工具“wget”。

开机自启：并向已有的 /etc/inittab、/etc/init.d/rcS、/etc/rc.d/rc.boot 追加执行项，实现开机持久化。

单实例自保策略：木马监听58346端口，以占用本地地址限制重复运行，该方法在传统僵尸网络家族Mirai中常用。还会尝试向 /proc/self/oom\_score\_adj 写入 -1000，降低因内存不足而被终止的可能。

5.版本更新

Cling木马演变速度极快，存在多个版本，本次传播的变种主要有如下特点：

加密增强：部分旧版本未加密关键信息，本次捕获版本均采用 ChaCha20 隐藏内置配置信息，提高隐匿性。

功能精简：移除内置的扫描、漏洞利用、代理、DDoS等功能，保留命令执行与程序下载执行，功能重心转向控制主机的持续利用。

隐匿改进：修改早期版本真实控制端响应事务标识与STUN服务器回复数据存在差异的缺陷，伪装更难识破，进一步提升了通信的隐蔽性。

控制端调整：C&C更换为新的ip。

三、感染规模

通过监测分析发现，2026年11月09日至20日期间，Cling 僵尸网络在我国境内感染肉鸡规模约5600台，境内日上线肉鸡数量最高达2730台。其感染量变化趋势如下：

![](https://mmbiz.qpic.cn/mmbiz_png/aoXpXT1UJRjdPPGYBgH1X3sa9icQQlmNlrbreicbVOQChmHSYNOib10dyBC1Ox2hS4KZccFadw0MKC4RUTcib1JRuGtoon01MOxxzYvWkW9bTxE/640?wx_fmt=png&from=appmsg)

图 3 境内感染终端数量

四、总结

Cling 木马借用 STUN 服务完成上线登记，再把指令藏入事务标识字段，以常见协议交互掩护控制联系，这种隐匿通信设计在现有僵尸网络中较为少见。其功能集中于远程执行、程序部署和持续运行，体现出攻击者对已控主机长期利用的侧重。工具替换、启动项持久化与进程隐藏增加了排查和清理的复杂性，该木马已对Linux服务器与IoT设备生态构成现实威胁，需要持续监测和高度警惕。

五、防范建议

请广大网民和网络运营者强化风险意识，加强安全防范，避免不必要的经济损失，主要建议包括：

1.及时梳理资产清单，修复相关系统漏洞，包括历史漏洞和最新曝光漏洞，IoT设备应同步升级固件。

2.加强口令强度，避免使用弱口令，密码设置应包含大小写字母、数字和符号，建议使用16位或更长密码，不同设备使用不同口令并定期更换。

3.安装终端防护软件，定期全盘查杀；重点排查异常进程、异常外连，以及本提示所列特征字符串。

4.加强STUN异常流量监测，重点核查周期性向多个STUN节点（UDP 3478）发送的注册流量，以及非随机、呈固定结构的事务标识。

5.加强主机侧专项排查，重点检查/etc/inittab、/etc/rc.d/rc.boot等位置的.alya启动项。

6.发现主机感染后，立即核实受控情况与入侵途径，对受害主机隔离清理，并及时向属地主管部门报告。

六、相关IoC

样本MD5:

84ced85e53bc326f8b11115ae4bc24a7

65d94c9dddea41ef4690f193fbc54ec3

92533318fb6f0365eefd25090e7df146

be719987bf96fa16ac98b7c2a280cc74

e37b94dfcaa56924142c344edcb3652a

79de772daa218e25a812ecbedca08476

606f2fee6fa4b3ca556187c9ee709f3d

b672e3238742504faa93d5a7cb8d0ea0

dc11a0e68e5235e36480ddf14f08afbe

76021af2d82cade790dd87d3af0f80c9

16ef618bf21a3322c6793be87d553f08

fe35c5b3cfa118fdf8e1afb9a134e084

下载地址：

http[:]//202.110.70.60:800/alya.x86

http[:]//202.110.70.60:800/alya.mipsel

http[:]//202.110.70.60:800/alya.arc

http[:]//202.110.70.60:800/alya.mips

http[:]//202.110.70.60:800/alya.x86\_64

http[:]//202.110.70.60:800/alya.m68k

http[:]//202.110.70.60:800/alya.i486

http[:]//202.110.70.60:800/alya.sparc

http[:]//202.110.70.60:800/alya.powerpc

http[:]//58.211.144.243:800/alya.mipsel

http[:]//58.211.144.243:800/alya.mips

http[:]//58.211.144.243:800/alya.x86\_64

http[:]//58.211.144.243:800/alya.i486

http[:]//58.211.144.243:800/alya.arc

http[:]//58.211.144.243:800/alya.powerpc

http[:]//58.211.144.243:800/alya.m68k

http[:]//118.45.196.225:800

http[:]//120.193.219.210:800

C&C：

209.99.188[.]119

---

![](https://mmbiz.qpic.cn/sz_mmbiz_png/aoXpXT1UJRjias1f0ya4xRXa4ksGEFrPEojCsltT0hVibveROdPV42mpAdAJ03ZynIbRRGesKGHW6SVz6yoibOjibVta2vrBeLnOOBSm58vorQ0/640?wx_fmt=png&from=appmsg)

预览时标签不可点

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/IpYUt4DIvZdVG48kyKzfbsCZgbic4jefJ6F15TxiapECa320rEtgtRviapHs904HG7PED0vIA6454w37HictgJjTMQ/0?wx_fmt=png)

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
推荐
，轻点两下取消推荐
分享
留言
收藏
听过