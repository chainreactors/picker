---
title: 针对以哈网络战Wiper攻击武器的详细分析
url: https://mp.weixin.qq.com/s?__biz=MzA4ODEyODA3MQ==&mid=2247489000&idx=1&sn=308a54b3928acd98b5933a47fda9f383&chksm=902fbac0a75833d64e078d768fbe61dd3a19bf0514f3bced1191233089083c91a4edf5ad66d7&scene=58&subscene=0#rd
source: 安全分析与研究
date: 2024-10-10
fetch_date: 2025-10-06T18:53:29.367185
---

# 针对以哈网络战Wiper攻击武器的详细分析

![cover_image](http://mmbiz.qpic.cn/mmbiz_jpg/oibWJqH5OVmVFvtma7JB1zjBJicolfKxVU8fQqpYy6b32ayNVNC7qPia577dG9Siaa7kWLFXr608g6kPstcibsKeMdQ/0?wx_fmt=jpeg)

# 针对以哈网络战Wiper攻击武器的详细分析

原创

pandazhengzheng

安全分析与研究

**安全分析与研究**

专注于全球恶意软件的分析与研究

前言概述

原文首发出处：

https://xz.aliyun.com/t/13961

先知社区 作者：熊猫正正

随着全球网络安全战的爆发，各种Wiper类型的恶意软件被大量应用到了国与国之间的网络战，成为网络战的重要攻击武器，专门针对敌对国的基础设施进行网络攻击行动，破坏敌国的各种关键基础设施，此前俄乌网络战的期间就使用了大量的Wiper攻击武器进行网络攻击。

此前Google安全团队发布了以色列与哈马斯网络战争相关报告，报告下载链接：

https://services.google.com/fh/files/misc/tool-of-first-resort-israel-hamas-war-cyber.pdf，有兴趣的朋友可以下载研究一下，同时提供了相关的IOCS，IOCS链接：

https://github.com/google/threat-team/tree/main/2024/2024-02-14-tool-of-first-resort-israel-hamas-war-cybert，笔者针对以哈网络战中使用的几种Wiper攻击武器进行了详细分析。

详细分析

**2.1 CHILLWIPE Wiper恶意软件**

CHILLWIPE恶意软件是一款SH脚本类型的攻击样本，主要针对Linux系统，伪装成F5漏洞更新程序，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmVFvtma7JB1zjBJicolfKxVUVjkCicEFOzhTwACMDnTFGXTR0KmoHyofPxibibdgK1dJsB11GUWmUicylQ/640?wx_fmt=png)

删除系统所有用户帐号，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmVFvtma7JB1zjBJicolfKxVUJKEAVG0or3ibhaWjofnb5nH7o2xuoFOfKEKkgZd528hibWxic2dItWaJg/640?wx_fmt=png)

删除系统包含的文件，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmVFvtma7JB1zjBJicolfKxVUBFrwaQVF9g3TAGsxVYadU2Iler7fpzhic6lkHrpv7gnJjTDeGqibvtmQ/640?wx_fmt=png)

通过Telegram发送相关消息到远程服务器，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmVFvtma7JB1zjBJicolfKxVUOAU3WY5re1fYe0G3IK3e2Vib0sInh1fLoARJAUlVysuNhwYEklzHSicQ/640?wx_fmt=png)

删除系统文件，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmVFvtma7JB1zjBJicolfKxVUwzMsJGecIQbarbqJ7fibiaQIDcUmvwgofmB0772Qw8NJBAjK6ibRRAUmQ/640?wx_fmt=png)

最后重启系统。

**2.2 COOLWIPE Wiper恶意软件**

COOLWIPE恶意软件是一款使用C#编写的NET类型的攻击样本，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmVFvtma7JB1zjBJicolfKxVUAuJIh7ZsdoH7p9YjricWBre6X6qjAib7MJ5UPoiaZfibx3iaZUqrvu95g9g/640?wx_fmt=png)

它同样伪装成F5漏洞更新程序，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmVFvtma7JB1zjBJicolfKxVUBWB1MfR0keK5XHLPx6tvluiceu10h3PNalmFm2Kysic4OVcSu5uiaibXmQ/640?wx_fmt=png)

点击Update按钮之后，会在系统目录下生成一个恶意软件，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmVFvtma7JB1zjBJicolfKxVUuN86CBDyibooA1YuWia0AvqhtVn7M0TawjZasicMliaT2QFwBn1XRYibr1Q/640?wx_fmt=png)

生成的Hatef.exe恶意程序，对系统中的文件进行覆盖或删除操作，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmVFvtma7JB1zjBJicolfKxVUhUCM5cV7z4P3x1RX3eCSk62ic7yl9b1lcXKodehlDKgG4337BRhmpicA/640?wx_fmt=png)

具体操作，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmVFvtma7JB1zjBJicolfKxVUuaRmbWBmsrcia1qzibu1AXMxBfaJbtWGzqK7lQQMbcGJpDBjO6yJ4Fog/640?wx_fmt=png)

然后通过Telegram发送系统主机相关信息和操作消息到远程服务器，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmVFvtma7JB1zjBJicolfKxVUw32OumlWdib9yarCYfEqZCqgMgw3uGBGGGSWNsb742K4ibUDrCajUqpQ/640?wx_fmt=png)

**2.3 DUNE BiBi Wiper恶意软件**

DUNE BiBi Wiper恶意软件包含Windows和Linux两个平台的攻击样本，笔者分别对这两个平台攻击样本进行详细分析。

**2.3.1 Windows平台恶意软件**

判断是否带有参数，参数为系统目录路径，如果带参数，则遍历参数目录下的文件，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmVFvtma7JB1zjBJicolfKxVUn5jBOtcodF4L3P1ibCKOLAWicQrUDzkMJdFP1icibXNyE3hbtaucSkDO5A/640?wx_fmt=png)

如果不带有参数，则遍历C:\Users目录下的文件，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmVFvtma7JB1zjBJicolfKxVUaichqJdATcYKoS3Wc7YGCGVtMZMSibesWlvWx759RCrD4bHGFuic4sCZA/640?wx_fmt=png)

获取操作系统主机信息，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmVFvtma7JB1zjBJicolfKxVU7eVdLwh5Rk15HssoQZTu1ODZA19qoFfOLa5X7r5wwQZUvmxWqpaSvQ/640?wx_fmt=png)

显示被损坏操作系统磁盘文件目录，以及系统主机信息，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmVFvtma7JB1zjBJicolfKxVUJflpjt1lpUkicHoJwxbSjx3fRLqkYwv1ZI2WotkynAEe0yk1icB2cqGw/640?wx_fmt=png)

调用CMD命令，删除磁盘卷影复本、禁用系统启动修复等，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmVFvtma7JB1zjBJicolfKxVUrry23xoicTGzheeO71zt4AykQtBW88y5bPba13BtXNqIUcrZr8U61xQ/640?wx_fmt=png)

相关命令，如下：

cmd.exe /c vssadmin delete shadows /quIet /all

cmd.exe /c wmic shadowcopy delete

cmd.exe /c bcdedit /set {default} bootstatuspolicy ignoreallfailures

cmd.exe /c bcdedit /set {default} recoveryenabled no

遍历目录下的文件，重命名文件并损坏文件，通过写入与目标文件长度相同的随机数据替换原文件内容，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmVFvtma7JB1zjBJicolfKxVUEcJHIiaia6mI8efWBwZbAm6TJAR1iaF36yZed9LRc5b2FoR8SjB2eV8Bg/640?wx_fmt=png)

填充写入随机数据内容，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmVFvtma7JB1zjBJicolfKxVUvOH2qneib6iaXow4tUibu2blbnlnic1GMLQm8mo3NpoY8JIqhGQicV2vaQA/640?wx_fmt=png)

如果文件后缀名为EXE、SYS、DLL等后缀，则不损坏，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmVFvtma7JB1zjBJicolfKxVUHOeL795vtPGDW9A805Qn6y7HPYkibibaF1LtpQftPWjEtnFic7v2hlyXQ/640?wx_fmt=png)

重命名后的文件名为[随机字符串名].BiBi[随机数]，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmVFvtma7JB1zjBJicolfKxVUiaBEOZoiadHsicJkibPRd4pwic7DHJicjZAeVZVeoajdE3pwYmuWtzS0ohZA/640?wx_fmt=png)

显示轮数、统计状态等信息，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmVFvtma7JB1zjBJicolfKxVUGeNT4iamPryrWlsjzQBeHuG563zkVDjJ3aI2BUDRMPbTBWcNCH6G1uA/640?wx_fmt=png)

恶意样本运行之后，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmVFvtma7JB1zjBJicolfKxVUkk0ARFDOfAIs7icGDT0Kib3ia9G5iazmAYOaubcZwh4Rczic4dWjV2oUPQQ/640?wx_fmt=png)

**2.3.2 Linux平台恶意软件**

Linux平台DUNE BiBi Wiper恶意软件的功能与Windows平台的类似，恶意样本运行之后，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmVFvtma7JB1zjBJicolfKxVU1gxvlqKbzCViaqxHKjiabovrcoicR7uSGqZvjlm8lFuFnXN45Co5twXqQ/640?wx_fmt=png)

损坏的文件的文件名，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmVFvtma7JB1zjBJicolfKxVUGNQuKIk14IIOGlaV0FYk4n9KFg81JZ95jIgPDrATYXL8VgoDRKo8mQ/640?wx_fmt=png)

判断是否有参数，没有参数，则遍历/目录下的文件，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmVFvtma7JB1zjBJicolfKxVUmarkiaiaFQtrPMNjLBQiavVJ1sfZ3uAmBE2JeQQgzXwQNmSjK70VqYOUA/640?wx_fmt=png)

显示被损坏操作系统磁盘文件目录，以及系统主机信息，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmVFvtma7JB1zjBJicolfKxVUkQHBNl6Qky4B9QzSn49JbsCpAH4Os3H5QmVuic6V9AiantnjbKhzhCnw/640?wx_fmt=png)

生成随机数据，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmVFvtma7JB1zjBJicolfKxVUg9k9Dnib91VYoVc1r9icW5LbZclHiaxCkHD5pEQiaudicUlTFhjCfTv1M7g/640?wx_fmt=png)

写入文件，损坏文件，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmVFvtma7JB1zjBJicolfKxVUHosN8hSRub9KxYc8PCz6aI53Z0iabc4NB96mZujgOItuVaS377ubjxg/640?wx_fmt=png)

通过上面的分析，可以发现Wiper类型的攻击样本与勒索类型的攻击样本非常相似，区别在于勒索类型的攻击样本按特定的方式和黑客的密钥加密文件，加密后的文件可以通过黑客的私钥解密，同时会留下勒索提示信息文件供受害者联系，交赎金之后提供解密工具解密文件，但大部分Wiper类型的攻击样本，主要作用就是破坏系统文件，通过直接删除或擦除改写磁盘系统文件内容达到破坏主机系统文件的目的，不要求支付赎金，也不会生成勒索提示信息文件，被破坏的系统文件一般也很难恢复。

威胁情报

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmVFvtma7JB1zjBJicolfKxVUWiby4libz3Nia8wW5D0nc9F1F2WmKZjicDY2edhOBI2bUBqicSbicKRiajibHw/640?wx_fmt=png)

总结结尾

未来可能还会有更多的国与国之间会发起网络安全战，这些网络安全战中Wiper攻击武器起到了至关重要的作用，同时也是网络安全战最重要的攻击武器，通过些攻击武器可以破坏敌对国家的重要基础设施。

恶意软件、勒索、APT、黑产明年仍然是全球企业面临的最大的安全威胁，同时也是全球网络犯罪的最主要经济来源，是最需要安全厂商密切关注和研究的方向，未来攻击者仍然会不断的开发新的恶意软件，研究各种新的攻击技术，使用新的攻击手法，进行更复杂的攻击活动，这将会不断增加安全威胁分析和情报人员分析溯源应急响应的难度，安全研究人员需要不断提升自己的安全能力，更好的应对未来各种威胁挑战，安全对抗会持续升级，这是一个长期的过程，也正如笔者一直说的，做安全不是一个结果，做安全是一个过程，因为永远没有结果，各种网络安全威胁会不断变化和升级，我们需要快速应对这些威胁。

预览时标签不可点

阅读原文

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmVcFgYKtoVnKR7h3pkl3AyxwS0l7iagicAJnYjEQhwIuZgR3RR65DLpJh2TGZS82DY7CjsBUmiaAl7BQ/0?wx_fmt=png)

安全分析与研究

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmVcFgYKtoVnKR7h3pkl3AyxwS0l7iagicAJnYjEQhwIuZgR3RR65DLpJh2TGZS82DY7CjsBUmiaAl7BQ/0?wx_fmt=png)

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