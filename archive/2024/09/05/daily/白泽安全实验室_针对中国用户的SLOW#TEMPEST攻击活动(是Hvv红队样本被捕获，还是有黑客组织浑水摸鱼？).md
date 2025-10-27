---
title: 针对中国用户的SLOW#TEMPEST攻击活动(是Hvv红队样本被捕获，还是有黑客组织浑水摸鱼？)
url: https://mp.weixin.qq.com/s?__biz=MzI0MTE4ODY3Nw==&mid=2247492310&idx=1&sn=81d1c876dacb5f88f297f39d46e34ff3&chksm=e90dc8fcde7a41ea501a941068b7f90dc68429aec1df0d5ee3cf5367683be8be01e8f04603d1&scene=58&subscene=0#rd
source: 白泽安全实验室
date: 2024-09-05
fetch_date: 2025-10-06T18:27:48.417042
---

# 针对中国用户的SLOW#TEMPEST攻击活动(是Hvv红队样本被捕获，还是有黑客组织浑水摸鱼？)

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/NpPydsaAMIO544JSnpfZmIP1kA3oSNWBwv5Pg9s4o0qib1dcrDa9ZxowI95xuFxpic78yMxbTiagEKV4b8GPUJkFA/0?wx_fmt=jpeg)

# 针对中国用户的SLOW#TEMPEST攻击活动(是Hvv红队样本被捕获，还是有黑客组织浑水摸鱼？)

BaizeSec

白泽安全实验室

**事件概述：**

网络安全厂商Securonix近期揭露了一个名为SLOW#TEMPEST的隐蔽网络攻击活动，该活动专门针对讲中文的用户。攻击者通过钓鱼邮件分发含有Cobalt Strike植入程序的恶意ZIP文件，利用这些文件在受害者的计算机上建立初始感染，并成功在目标系统内进行横向移动、建立持久性，在超过两周的时间内保持隐蔽。攻击活动显示出明显的针对性，所有C2基础设施均位于国内，且使用的诱饵和文件命名均采用中文，表明攻击者对中国国内用户有明确的攻击意图。不过攻击活动被披露后有国内技术爱好者，分析怀疑这是前不久国内搞Hvv时红队样本被有些安全公司捕获曝光，不过也还有另外一种可能就是有一些黑客组织在Hvv期间浑水摸鱼。

**攻击目标及策略分析：**

* **目标定位：**攻击活动似乎专门针对中国境内的受害者，文件名和诱饵大部分用中文书写。此外，所有命令与控制（C2）基础设施均由腾讯云托管，进一步证实了中国是此次攻击的主要目标。
* **攻击手段：**尽管无法确定确切的攻击源头和初始攻击向量，但根据恶意样本的遥测数据分析，大部分恶意文件和代码源自国内，且攻击手法符合传统的钓鱼邮件策略。

**攻击过程技术细节分析：**

**1.初始感染：**攻击始于包含在压缩文件（.zip）中的快捷方式（.lnk）文件。例如，一个名为“20240739人员名单信息.zip”的样本文件。这些ZIP文件有时被密码保护，这是Qakbot威胁行为者常用的策略，密码通常在钓鱼邮件正文中提供。对ZIP文件内容进行加密，确保基于电子邮件的防病毒软件无法正确检查和标记任何包含的内容。

**2.诱饵文件与初始代码分析：**恶意LNK文件执行时，会引用一个包含“MACOS”元数据文件的奇怪目录结构中的可执行文件。其中一个目录被命名为“其他信息”。这种目录结构可能用于迷惑用户，使其认为文件来源于Mac系统，而实际上它们包含的是Windows恶意软件。

**3.DLL劫持与Cobalt Strike植入执行：**攻击者利用DLL劫持技术执行Cobalt Strike植入程序，该程序允许攻击者对系统进行持久且隐蔽的访问。在本案例中，攻击者通过劫持合法的Microsoft签名可执行文件LicensingUI.exe来执行恶意DLL，这是一种未记录的DLL劫持技术。Cobalt Strike植入程序配置为通过加密的网络流量与C2服务器通信，使用“Malleable\_C2\_Instructions”来规避基于网络的检测。

**4.后开发利用-攻击者手动操作：**攻击者完全控制目标主机后，进行了一系列活动，包括建立阶段性目录、下载额外的枚举和攻击工具。攻击者创建了目录C:\Windows\Temp\tmp用于存储和执行多个工具，如端口转发工具iox.exe、网络扫描工具fscan.exe、网络侦察工具netspy.exe等。

**5.权限提升与持久性：**攻击者通过创建计划任务“windowsinspectionupdate”来维持对被破坏环境的持久访问。此任务被配置为定期执行恶意可执行文件lld.exe，该文件用于执行存储在tmp.log中的shellcode。此外，攻击者通过提升内置访客帐户的权限，将其添加到管理员组并分配新密码，从而在被破坏的系统中隐藏自己的活动。

**6.横向移动与凭证收集：**攻击者主要通过RDP进行网络横向移动，他们首先尝试使用最初被泄露的帐户登录到其他系统。成功建立RDP连接后，攻击者使用工具如fscan.exe和netspy.exe对内部网络进行侦察和扫描。攻击者还使用凭证盗窃工具如sharpdecryptpwd.exe从浏览器中提取存储的凭据，并使用Mimikatz从Cobalt Strike进程中转储Windows凭据。

**总结：**

研究人员发现的SLOW#TEMPEST活动揭示了一个高度组织化和复杂的网络攻击，针对讲中文的用户。尽管没有确凿证据将此攻击与任何已知的APT组织联系起来，但很可能是由经验丰富的攻击者精心策划，他们熟悉CobaltStrike等先进技术框架以及一系列其他后开发工具的使用。攻击的复杂性体现在其对初始入侵、持久性、权限提升和跨网络横向移动的系统性技术方法上。

**参考附件：**

**附件1：MITRE ATT&CK 矩阵**

|  |  |
| --- | --- |
| **攻击****策略** | **攻击****技术** |
| **初始访问** | T1078.001：有效帐户：默认帐户  T1566.001：网络钓鱼：鱼叉式网络钓鱼附件 |
| **收集** | T1560：存档收集的数据 |
| **命令和控制** | T1132：数据编码 |
| **凭证访问** | T1003：操作系统凭证转储  T1555：来自密码存储的凭证 |
| **防御闪避** | T1070.004：指示器删除：文件删除  T1562.001：削弱防御：禁用或修改工具  T1574.001：劫持执行流：DLL 搜索顺序劫持  T1620：反射代码加载 |
| **发现** | T1033：系统所有者/用户发现  T1057：进程发现  T1069：权限组发现：域组 T1082：系统信息发现 |
| **执行** | T1059.001：命令和脚本解释器：PowerShell  T1059.003：命令和脚本解释器：Windows 命令外壳  T1059.006：命令和脚本解释器：Python  T1569.002：系统服务：服务执行  T1204.001：用户执行：恶意链接  T1204.002：用户执行：恶意文件 |
| **横向移动** | T1021.001：远程服务：远程桌面协议  T1550.002：使用备用身份验证材料：传递哈希 |
| **坚持** | T1053：计划任务/作业 |
| **外泄** | T1041：通过 C2 通道渗漏 |

**附件2：恶意文件HASH**

**SHA256**

8e77101d3f615a58b8d759e8b82ca3dffd4823b9f72dc5c6989bb4311bdffa86

04bcf25d07e5cf060e742325d6123242f262888705acac649f8d5010a5eb6a87

c35ea8498ed7ae33513e26fac321fecf0fc9306dda8c783904968e3c51648c37

3a9b64a61f6373ee427f27726460e7047b21ddcfd1d0d45ee4145192327a0408

28030E8CF4C9C39665A0552E82DA86781B00F099E240DB83F1D1A3AE0E990AB6

1BA77DD1F5BF31D45FDB160C52EBE5829EC373350CDE35818FB90D45352B3601

1189D34E983A6FC9D2DC37AD591287C9E3E4D4BA83F66C7EDE692C36274BA648

706BD7E05F275814C3B86EEC1A87148662029D91D0CE9B80386AAFFE7AA3753B

C6CF82919B809967D9D90EA73772A8AA1C1EB3BC59252D977500F64F1A0D6731

0BD048E0BCE956EDFBCEE6EDF32B8B67E08275BD38125B40A98665FAB4926C9D

97C5CD06B543B0BDB270666092348EFBA0A9670AF05B11F3B56BF4B418DEC43A

7DC0E13A5F1A70C4E41F4B92372259B050A395104650D57385ECAA148481AE5C

1F510DED0D181B4636E83C69B66C92465DC0E64F6DB946FA4C246E7741F66141

9F650117288B26312E84F32E23783FE3C81FCBA771C8AE58119BE92344C006CC

7DC0E13A5F1A70C4E41F4B92372259B050A395104650D57385ECAA148481AE5C

EFE53F18D282516149BC6FEAC44C17DDE9F0704D95598AECBA3E7D734727B07E

33A910162EAFE750316ADFAD4AB0955BE24C1BA048C2EC236C95E4A795C42932

参考链接：

https://www.securonix.com/blog/from-cobalt-strike-to-mimikatz-slowtempest/

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/NpPydsaAMIN7MdZNibeGNoAT8tqwpL0jiaadMrz99YH3koiadd3bCWZXicyNqlId4PnibcJCj8JabAOvibc5uBn4G7Ow/0?wx_fmt=png)

白泽安全实验室

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/NpPydsaAMIN7MdZNibeGNoAT8tqwpL0jiaadMrz99YH3koiadd3bCWZXicyNqlId4PnibcJCj8JabAOvibc5uBn4G7Ow/0?wx_fmt=png)

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