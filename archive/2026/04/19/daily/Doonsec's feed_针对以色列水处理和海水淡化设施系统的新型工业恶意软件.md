---
title: 针对以色列水处理和海水淡化设施系统的新型工业恶意软件
url: https://mp.weixin.qq.com/s/YPPtIt-drbPAgA3ZT6rOrQ
source: Doonsec's feed
date: 2026-04-19
fetch_date: 2026-04-20T04:52:09.148568
---

# 针对以色列水处理和海水淡化设施系统的新型工业恶意软件

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/ibO9kiauylaDqUU27J8nXGkG5RQTsr2ULmLHNqiatiadFD8KWzPiaeEHFaPDx5Say6eWZZ8aFKaUIxe46r9zPjUicDH9WlzK3TL6Pj7ktYicz4ibYeI/0?wx_fmt=jpeg)

# 针对以色列水处理和海水淡化设施系统的新型工业恶意软件

原创

黑鸟
黑鸟

黑鸟

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

海外安全厂商发布了一份分析报告，揭示了一款专门针对工业控制系统的新型恶意软件。这款名为 ZionSiphon 的恶意软件将攻击目标锁定在以色列的水处理和海水淡化设施上，具备破坏供水系统关键控制功能的能力。

ZionSiphon 是一款专门为攻击工业控制系统设计的恶意软件。它整合了多种常见的主机攻击能力，包括权限提升、持久化驻留和可移动介质传播，同时加入了针对水处理和海水淡化环境的特定攻击逻辑。

![](https://mmbiz.qpic.cn/mmbiz_png/ibO9kiauylaDoJte2Q9w23fkunoR4VMrBvgt8jGd36s8AsWEUMnFENxrvIWr7a7tIlFicmWVmfAiaTlUcfr8598mib8Sdzgyhh9ZQ2UhS8GYc8dA/640?wx_fmt=png&from=appmsg)

这款恶意软件的最终目标是破坏供水系统中的氯气投加控制和压力控制设备。

如果攻击成功，可能会导致饮用水中氯气含量异常，对公众健康造成严重威胁。不过，分析的这个样本存在一些明显的技术缺陷，目前还无法正常执行其预定的攻击功能。

ZionSiphon 最显著的特征是其硬编码的以色列 IP 地址范围。恶意软件在执行任何操作之前，会首先检查本地主机的 IP 地址是否属于以下几个以色列网段：

* 2.52.0.0 至 2.55.255.255
* 79.176.0.0 至 79.191.255.255
* 212.150.0.0 至 212.150.255.255

这些 IP 地址范围全部位于以色列境内，表明攻击者的目标非常明确。

![](https://mmbiz.qpic.cn/mmbiz_png/ibO9kiauylaDrgvozoDyme1wcaqvgURfYFv4nDMPyV4LNtjdzKNHQ6G7rk9dbZh0loujs2viculfqQJt484LRIHvgUdC2Tek5yEhIyCRvOWoVo/640?wx_fmt=png&from=appmsg)

恶意软件的二进制文件中包含了两段经过 Base64 编码的字符串，这些字符串不具备任何实际功能，但清晰地揭示了攻击者的政治立场。第一段解码后内容为："支持我们在伊朗、巴勒斯坦和也门的兄弟，反对XXX侵略。我是 0xICS。"

第二段字符串提到了以色列城市迪莫纳，解码后内容为："XX特拉维夫和海法的居民。" 迪莫纳是以色列内盖夫沙漠中的一座城市，以西蒙・佩雷斯内盖夫核研究中心所在地而闻名。

![](https://mmbiz.qpic.cn/mmbiz_png/ibO9kiauylaDpxADpSOkbYoPFRrSNPP2XKSnwSVNFDwyek32FgqRKQPcPnzE0icWpG8Gvp8wHj4r1shDKUCSBQdS084SEtn77MkFFc9BcrNZia8/640?wx_fmt=png&from=appmsg)

除了地理定位，ZionSiphon 还包含了一系列与以色列供水基础设施相关的关键词。

这些关键词包括：

* Mekorot：以色列国家水务公司，负责管理全国的供水系统
* Sorek、Hadera、Ashdod、Palmachim：以色列四大海水淡化厂
* Shafdan：以色列中央污水处理和回收设施

恶意软件会检查系统中是否运行着与海水淡化、反渗透、氯气处理和工厂控制相关的进程，同时扫描特定的目录和配置文件。只有当系统同时满足地理条件和环境条件时，恶意软件才会激活其攻击功能。

![](https://mmbiz.qpic.cn/mmbiz_png/ibO9kiauylaDr4l40U0gicgtjyCDjicMHIe1GPjsDdl8ZpWm2sYsxRwcZ4QWdKs26ycU1atekrvDLOoEaoezhOw9YW98OEB3ia7A8k5cpEcYoAKI/640?wx_fmt=png&from=appmsg)

ZionSiphon 首先会检查自身是否以管理员权限运行。如果没有，它会通过 PowerShell 启动一个新的进程，并请求管理员权限。这是恶意软件获取系统控制权的第一步。

![](https://mmbiz.qpic.cn/mmbiz_png/ibO9kiauylaDoJ35WzFaibhC5iaRc0Y1oIEqFJlspP7c3Vibia75k4o0jbR99JeVFqmCGEmVfImRs5GcjMrHrxicybrYGGpBxl8DGIh9hYCZ6SPic74/640?wx_fmt=png&from=appmsg)

为了在系统重启后仍然能够运行，ZionSiphon 会将自身复制到本地应用数据目录，并命名为 svchost.exe。这是一个常见的 Windows 系统进程名称，攻击者试图以此来伪装恶意软件。

![](https://mmbiz.qpic.cn/mmbiz_png/ibO9kiauylaDp22icqh3NKLhWCaV60jghLvvwibse6Bme38nq5Wr1lNYRWnQfwOGrmSE7xzTibW1kyialOEy8WxboX0icyz9t80o20lCyAAMSP0Iec/640?wx_fmt=png&from=appmsg)

随后，恶意软件会在 Windows 注册表的启动项中创建一个名为 SystemHealthCheck 的键值，指向恶意软件的路径。同时，它会将复制的文件设置为隐藏属性，以降低被发现的可能性。

![](https://mmbiz.qpic.cn/mmbiz_png/ibO9kiauylaDofXNNgtcXdEKALKE5mzNAFeLRENx0w8hBFusOGkOkriaLvlvHiagBOic1B2JhHy1DpXOxoPrMOrG0PibJqDNmAmYhFzgRNTaVF2bg/640?wx_fmt=png&from=appmsg)

ZionSiphon 的目标判定分为两个步骤：

1. 国家检查：验证本地 IP 地址是否属于以色列
2. 环境检查：验证系统是否为水处理或海水淡化设施

只有当两个检查都通过时，恶意软件才会执行后续的攻击操作。如果国家检查失败，恶意软件会立即启动自毁程序。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ibO9kiauylaDqNKPk3mEtfY4EA5sZK0WNV3wfPs9Ae6ICoxxbNOTy0qBAQIajAleaBHB8avtVqvmERw0nZUtdt0yXQ62XnJccMXickEvyyCuNg/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ibO9kiauylaDqkZOPAeDl88KqHDWrM8zendW7LW98mqFEwP7ibXpiaPUOicZiahiaqKyiasZSbpTfKQy6iateib3QlHW7P2qBoHCMe5bu5l0zGNFygDSQ/640?wx_fmt=png&from=appmsg)

“ **IsDamDesalinationPlant** ()”函数随后评估主机是否类似于相关的工业环境。它首先扫描正在运行的进程名称，查找前面提到的硬编码字符串，然后检查是否存在任何硬编码的目录或文件。

其逻辑很明确：**只有当地理条件和与海水淡化或水处理相关的特定环境条件都满足时，相关恶意代码才会激活。**

![](https://mmbiz.qpic.cn/mmbiz_png/ibO9kiauylaDpeVHemUwcUPAjjOfo3OLjiawUYwrFB6uP9eFvzB2FiaGKImOIJN6ERDsPN3XTRa3LvDpJDVularLmFzb2iaibfI8QeShNLGOj4VRA/640?wx_fmt=png&from=appmsg)

###

如果系统不符合攻击条件，ZionSiphon 会执行自毁操作。它会删除注册表中的启动项，在临时目录中创建一个日志文件，然后生成一个批处理文件来删除自身。这个批处理文件会反复尝试删除恶意软件的可执行文件，直到成功为止，最后再删除自己。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ibO9kiauylaDowWUhmsLcyibqYLU6UuBRTA2ibk1J8HxhrZFXWwwj69B6dAc8WofPMx43GeG406eqesun6puPg822mAbT1RxtuBgXyeP9YJrfa8/640?wx_fmt=png&from=appmsg)

一旦确认目标有效，ZionSiphon 的第一个动作就是篡改本地配置文件。它会搜索一系列与水处理和工业控制系统相关的配置文件，包括：

* C:\DesalConfig.ini
* C:\ROConfig.ini
* C:\ChlorineControl.dat
* C:\SalinityControl.ini

当找到任何一个这样的文件时，恶意软件会在文件末尾追加以下内容：

* Chlorine\_Dose=10
* Chlorine\_Pump=ON
* Chlorine\_Flow=MAX
* Chlorine\_Valve=OPEN
* RO\_Pressure=80

这些配置项会强制系统将氯气投加量设置为最大值，并将反渗透系统的压力提高到 80。这可能会导致饮用水中氯气含量超标，对人体健康造成危害，同时也可能损坏水处理设备。

![](https://mmbiz.qpic.cn/mmbiz_png/ibO9kiauylaDozIJWouBd5vxPcB5Ort64ZJKoIRPK2TsIB6wccHFia9GSJbORL4T17QJeKAZGeVOq1ibLupvJp8ffNNMOrcW7ALBLzhfNFWhhZA/640?wx_fmt=png&from=appmsg)

###

如果没有找到上述配置文件，ZionSiphon 会进入网络扫描阶段。它会获取本地子网的 / 24 前缀，然后对 1 到 255 之间的所有主机进行扫描。

![](https://mmbiz.qpic.cn/mmbiz_png/ibO9kiauylaDqpcdX15IiaNZxibjqXiaku1eQ1maZJBQkibFEibRfUUE9oz6LnZNpPPicjj63cBR0yMSAAibalqrVulSa166VxrFmR1uQOyM7vtUYufw/640?wx_fmt=png&from=appmsg)

恶意软件会探测三个常见的工业控制协议端口：

* 502 端口：Modbus 协议
* 20000 端口：DNP3 协议
* 102 端口：S7comm 协议

对于每个开放的端口，ZionSiphon 会进行简单的协议验证。它会向远程设备发送一个空字节，然后根据响应来判断设备使用的协议类型。

在这三个协议中，Modbus 协议的攻击逻辑最为完善。恶意软件会读取目标设备的保持寄存器，寻找与氯气投加量相关的寄存器。如果找到符合条件的寄存器，它会将其值设置为 100。如果没有找到，它会使用硬编码的寄存器地址进行写入操作。

![](https://mmbiz.qpic.cn/mmbiz_png/ibO9kiauylaDrVRjKuQCV31nsbWyjEFsVmmdkzAs47oh4f6OP0Pv1R8Ncia15v6yqHMQEpTyCLe6vj8OFLkDoVRah0YAYRlBwTr18darla6ck8/640?wx_fmt=png&from=appmsg)

相比之下，DNP3 和 S7comm 协议的攻击逻辑还很不完善。恶意软件中只包含了这两个协议的头部信息，没有完整的命令结构，无法执行有效的攻击操作。这表明攻击者可能还在开发这些功能。

ZionSiphon 还具备通过 USB 设备传播的能力。它会扫描系统中的可移动驱动器，并将自身复制到每个驱动器上，命名为 svchost.exe。复制的文件会被设置为隐藏和系统属性。

然后，恶意软件会为 USB 驱动器根目录下的每个文件创建一个快捷方式。这些快捷方式的目标指向隐藏的恶意软件副本，图标则使用 Windows 通用文件图标。当用户点击这些看起来像正常文件的快捷方式时，就会在不知不觉中运行恶意软件。

![](https://mmbiz.qpic.cn/mmbiz_png/ibO9kiauylaDpMEwe54hkZp1BnulFYWk3EDP3bOsTRvVh6qeOlzLTtdH7iaI6eJT6TAkia3UCSmjG76LN7GEP4guNia8CUVxCicYPrPnfL7fFgC94/640?wx_fmt=png&from=appmsg)

## 为什么这个版本无法正常工作

尽管 ZionSiphon 具备完整的攻击框架，但分析的这个样本存在一个致命的缺陷。在国家检查函数中，恶意软件会将 IP 地址范围对应的字符串与加密后的 "Israel" 字符串进行比较。

![](https://mmbiz.qpic.cn/mmbiz_png/ibO9kiauylaDp2UoznRc9JzAMianKcoMZlptibGrtiaFdicYaEkicN9OUxsWuBHm727FuYQOo6uDKezyrglbQn8K4EB7VXZB91EurXyGiaewDnYVRlM/640?wx_fmt=png&from=appmsg)

然而，由于加密函数的实现错误，加密后的 "Israel" 字符串与硬编码的字符串永远无法匹配。这导致即使系统的 IP 地址属于以色列，国家检查也会失败，恶意软件会直接进入自毁流程。

此外，DNP3 和 S7comm 协议的攻击逻辑也不完整，无法执行有效的攻击操作。这些问题表明，这个版本的 ZionSiphon 可能是一个开发中的版本，或者是在部署过程中出现了错误。

![](https://mmbiz.qpic.cn/mmbiz_png/ibO9kiauylaDrCMDPLyu37GygpbOnlW9JNA2cNs0Nl5YVSxBf1JTM82hicaWkVPdiaIktwQzFwg5Lzhqb8Gxx7PibibZa9Qg3bEBz7ib148sRSlVUE/640?wx_fmt=png&from=appmsg)

ZionSiphon 的出现标志着针对关键基础设施的网络攻击正在不断演变。虽然这个样本还不完善，但它展示了攻击者已经具备了针对工业控制系统进行精准攻击的能力。

这款恶意软件的特点在于：

* 明确的政治动机和地理目标
* 针对特定行业的深度定制
* 整合了多种攻击技术
* 具备直接破坏工业过程的能力

即使在未完成的状态下，ZionSiphon 也向我们发出了一个明确的警告。随着攻击者对工业控制系统的了解不断加深，未来可能会出现更加复杂和危险的恶意软件。

对于供水、能源、交通等关键基础设施运营者来说，加强网络安全防护已经刻不容缓。这包括：

* 建立 IT 和 OT 环境的全面可见性
* 实施异常检测和行为分析
* 加强员工的网络安全意识培训
* 制定完善的应急响应计划

##

ZionSiphon 是网络威胁不断进化的又一个例证。

虽然这次攻击因为技术缺陷而未能成功。

恶意软件MD5:eb89f018e6c3a8e9de0a0452acb16e76

往期:[冒充知名开发者骗过AI合并恶意代码到主分支](https://mp.weixin.qq.com/s?__biz=MzAxOTM1MDQ1NA==&mid=2451186423&idx=1&sn=47e60ed553b0f7c39ba19120af9b6ee9&scene=21#wechat_redirect)

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/ibO9kiauylaDqicDvERLTuy6Yo2PUS5sCSLCWBlXcichCYke51phlZqJvemVicckicq5cDX67WMuDvDmWX3HQaiaFCeKnMRuEVv2jsQCv90kc27HwE/640?wx_fmt=jpeg&from=appmsg)

预览时标签不可点

阅读原文

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/sz_mmbiz_png/V9abY6oHTkqrJPe3BMSmUuUaQMPJDnWTSrtbtXBAZSMfj0iaxiaMvM6cnIDqLXBbescHHicaricGUU0tHjJ4BqISKw/0?wx_fmt=png)

黑鸟

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/V9abY6oHTkqrJPe3BMSmUuUaQMPJDnWTSrtbtXBAZSMfj0iaxiaMvM6cnIDqLXBbescHHicaricGUU0tHjJ4BqISKw/0?wx_fmt=png)

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