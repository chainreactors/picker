---
title: Coruna:一个强大iOS漏洞利用工具包的神秘之旅
url: https://mp.weixin.qq.com/s/jik3V1LPFwnyC3hq1jO1Bg
source: Doonsec's feed
date: 2026-03-07
fetch_date: 2026-03-08T04:04:24.874185
---

# Coruna:一个强大iOS漏洞利用工具包的神秘之旅

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/lWEOEB1GOU3LCbXEI0gPQHHuibRSY7XORm99ZibtEaibHARb0ELdMmE6UepT6NL5UHjHTABkDfbBUzyoTzwKD1hiaGDaFb8MC5aODGngAr2CAGw/0?wx_fmt=jpeg)

# Coruna:一个强大iOS漏洞利用工具包的神秘之旅

GTIG
GTIG

赛博知识驿站

![]()

在小说阅读器中沉浸阅读

# 引言

Google威胁情报小组(GTIG)发现了一个针对苹果iPhone的全新强大漏洞利用工具包。这个被开发者内部命名为"`Coruna`"的工具包,覆盖了从iOS 13.0(2019年9月发布)到iOS 17.2.1(2023年12月发布)的广泛版本,内含**5条完整的iOS漏洞利用链**和**总计23个漏洞**。

真正令人惊艳的,是这个工具包的技术含金量——它不仅集大成地整合了iOS漏洞,更令人警惕的是,**其中最先进的漏洞利用了非公开的攻击技术和缓解措施绕过手段**。

### 从商业监控到网络犯罪:一场"二手零日漏洞"的流转

Coruna的传播轨迹,为我们揭示了**高级攻击能力如何在不同威胁行为者之间扩散**的惊人现象。

2025年,GTIG追踪到这个工具包经历了三次截然不同的"转手":

1. 1. **起点:商业监控**——最初由某监控厂商的客户在高度定向的行动中使用
2. 2. **升级:国家级间谍活动**——随后被`UNC6353`(疑似俄罗斯间谍组织)部署在针对乌克兰用户的水坑攻击中
3. 3. **失控:大规模金融诈骗**——最终落入`UNC6691`手中,在大规模诈骗活动中泛滥

**这种扩散路径如何发生,目前尚不清楚**,但无疑指向了一个活跃的"二手零日漏洞"黑市。更危险的是,多个威胁行为者现在已经掌握了这些先进的攻击技术,可以将其与新发现的漏洞重新组合使用。

### 防护建议:升级是唯一出路

值得庆幸的是,**Coruna工具包对最新版本的iOS已经失效**。我们强烈建议:

* • **立即将iPhone更新到最新iOS版本**
* • 如果无法更新,请启用锁定模式[1]以增强安全防护

所有相关网站和域名已被添加到Google安全浏览[2]黑名单,保护用户免受进一步攻击。

---

### 发现时间线

![时间线图](https://mmbiz.qpic.cn/sz_mmbiz_png/lWEOEB1GOU2kyiaeO05kjAcAb0D2tsbOlkDG5aXKos8ocdIUYb4T0WP8pia6d7VCz3qibuKibOYiaAZbZN9eEvtWujnFKA0J04SO50SnzLhM6icY0/640?wx_fmt=png&from=appmsg)

时间线图

*图1:Coruna iOS漏洞利用工具包发现时间线*

---

### 第一幕:商业监控的影子

**2025年2月**,我们捕获了一个iOS漏洞利用链的部分代码,使用者是某监控公司的客户。这些漏洞被整合进一个此前从未见过的JavaScript框架中,采用了简单但独特的混淆技术:

```
[16, 22, 0, 69, 22, 17, 23, 12, 6, 17].map(x => {return String.fromCharCode(x ^ 101);}).join("")
```

这个框架会先进行设备指纹识别,收集各种数据点来判断设备是否真实,以及具体的iPhone型号和iOS版本。然后根据收集到的信息,加载相应的WebKit远程代码执行(RCE)漏洞,接着是指针认证码(PAC)绕过。

![JavaScript代码](https://mmbiz.qpic.cn/mmbiz_png/lWEOEB1GOU1z1OwtD4CYbxxFEl5tDOHsFbAjcSNLCjbkPA37MDBMMCpKflltlpicy8zApYCnpkAX5816RmpqTQG7PuMGr2Nc3Kib411XgTUno/640?wx_fmt=png&from=appmsg)

JavaScript代码

*图2:Coruna漏洞利用工具包的反混淆JavaScript代码*

当时我们恢复了针对iOS 17.2设备的WebKit RCE,确认其为`CVE-2024-23222`——这是一个此前被识别的零日漏洞,苹果在2024年1月22日的iOS 17.3更新中修复,但**没有致谢任何外部研究人员**。

![RCE漏洞代码](https://mmbiz.qpic.cn/mmbiz_png/lWEOEB1GOU2ib6oTP2UPZpSmMGiaviaq2ia3jgYg03NvjwAourIdA3Z1tEZ9SZ5xWnul0URtO9SrWX2pTpz0Zjf07h89XWov40vmCI4d4jdZco4/640?wx_fmt=png&from=appmsg)

RCE漏洞代码

*图3:利用CVE-2024-23222的RCE漏洞在野外的实际投放方式*

---

### 第二幕:针对乌克兰的水坑攻击

**2025年夏季**,我们在`cdn.uacounter[.]com`上发现了相同的JavaScript框架。这个网站以隐藏iframe的形式被加载到许多被入侵的乌克兰网站上——从工业设备、零售工具到本地服务和电商网站,无所不包。

框架只针对特定地理位置的iPhone用户投放。我们收集到的WebKit RCE包括`CVE-2024-23222`、`CVE-2022-48503`和`CVE-2023-43000`,随后服务器被关闭。我们与乌克兰计算机应急响应小组(CERT-UA)合作,清理了所有被入侵的网站。

---

### 第三幕:诈骗网站的全链条收集

**2025年底**,我们在大量虚假网站上发现了这个JavaScript框架,大多与金融相关,投放的正是同一个iOS漏洞利用工具包。

这些网站试图诱导用户使用iOS设备访问,如图4所示,这是从一个假冒的WEEX加密货币交易所网站截取的画面:

![诱导弹窗](https://mmbiz.qpic.cn/mmbiz_png/lWEOEB1GOU0SdGcApyuhxTrep1AQiaicH7SkicxZLEecPswhRFfMtuYIpfKGstQ6bQpdAv9F112QHDYGbCZfwDxrWy6KCsXKAOiae1ibpiaAuKSOQ/640?wx_fmt=png&from=appmsg)

诱导弹窗

*图4:假冒加密货币交易所网站上的弹窗,试图引导用户访问漏洞利用页面*

用户通过iOS设备访问这些网站时,无论地理位置如何,都会被注入一个隐藏的iframe,投放漏洞利用工具包。

![漏洞代码截图](https://mmbiz.qpic.cn/sz_mmbiz_png/lWEOEB1GOU1lp8AoSia1TlmGQHpibic0Npy7GV41IicQ62WuypNw1NrkLDHXg5WoJBWicor0ftwZX0qMcsMOQ7vJv1cEB9w346baejt53Sj9VNdI/640?wx_fmt=png&from=appmsg)

漏洞代码截图

*图5:从诈骗网站恢复的CVE-2024-23222漏洞利用代码截图*

我们恢复了所有混淆的漏洞利用代码,包括最终载荷。在进一步分析中,我们发现攻击者部署了工具包的调试版本,**以明文形式留下了所有漏洞利用代码,包括它们的内部代号**。正是在这时,我们得知这个工具包很可能在内部被命名为"`Coruna`"。

总共收集了数百个样本,覆盖**5条完整的iOS漏洞利用链**,能够针对运行iOS 13.0(2019年9月发布)到iOS 17.2.1(2023年12月发布)的各种iPhone型号。

---

### Coruna工具包:工程化的艺术

这个框架的工程化水平极高,各个漏洞利用组件自然衔接,使用通用的工具和框架组合在一起。该工具包执行以下独特操作:

* • **智能规避**:如果设备处于锁定模式或用户在隐私浏览模式,立即退出
* • **资源加密**:使用独特的硬编码cookie生成资源URL
* • **哈希寻址**:资源通过哈希引用,需要使用独特cookie通过`sha256(COOKIE + ID)[:40]`推导其URL
* • **分段加密**:RCE和PAC绕过未加密投放,但二进制载荷使用ChaCha20加密,每个blob都有唯一密钥
* • **自定义格式**:载荷打包在以`0xf00dbeef`为头的自定义文件格式中,使用LZW算法压缩

图6展示了从网络角度看,一台运行iOS 15.8.5的iPhone XR被感染的完整过程:

![感染流程](https://mmbiz.qpic.cn/mmbiz_png/lWEOEB1GOU0hCPo3v4JT7SBicuSjcLiaOicy0icC3oX4bJ16TMibnJAvicjj2oTlCMiamXTrRMHjntKNQzCticz68MiaJj5eIux39MeQkf9DKYZr4eicw/640?wx_fmt=png&from=appmsg)

感染流程

*图6:iOS 15.8.5上投放的Coruna漏洞利用链*

---

### 漏洞全景:23个漏洞的完整拼图

这个工具包的核心价值在于**全面的iOS漏洞集合**。这些漏洞有详尽的文档、注释和说明,均以地道的英语撰写。最先进的漏洞使用了**非公开的攻击技术和缓解措施绕过**。

下表总结了我们正在进行的分析,涵盖各种漏洞利用链。由于调查仍在进行,某些CVE关联可能会修订。**总计23个漏洞,覆盖iOS 13到iOS 17.2.1**。

| **类型** | **代号** | **目标版本** | **修复版本** | **CVE** |
| --- | --- | --- | --- | --- |
| WebContent R/W | buffout | 13 → 15.1.1 | 15.2 | CVE-2021-30952 |
| WebContent R/W | jacurutu | 15.2 → 15.5 | 15.6 | CVE-2022-48503 |
| WebContent R/W | bluebird | 15.6 → 16.1.2 | 16.2 | 无CVE |
| WebContent R/W | terrorbird | 16.2 → 16.5.1 | 16.6 | CVE-2023-43000 |
| WebContent R/W | cassowary | 16.6 → 17.2.1 | 16.7.5, 17.3 | CVE-2024-23222 |
| WebContent PAC绕过 | breezy | 13 → 14.x | ? | 无CVE |
| WebContent PAC绕过 | breezy15 | 15 → 16.2 | ? | 无CVE |
| WebContent PAC绕过 | seedbell | 16.3 → 16.5.1 | ? | 无CVE |
| WebContent PAC绕过 | seedbell\_16\_6 | 16.6 → 16.7.12 | ? | 无CVE |
| WebContent PAC绕过 | seedbell\_17 | 17 → 17.2.1 | ? | 无CVE |
| 沙箱逃逸 | IronLoader | 16.0 → 16.3.1/16.4.0 | 15.7.8, 16.5 | CVE-2023-32409 |
| 沙箱逃逸 | NeuronLoader | 16.4.0 → 16.6.1 | 17.0 | 无CVE |
| 权限提升 | Neutron | 13.X | 14.2 | CVE-2020-27932 |
| 权限提升(信息泄露) | Dynamo | 13.X | 14.2 | CVE-2020-27950 |
| 权限提升 | Pendulum | 14 → 14.4.x | 14.7 | 无CVE |
| 权限提升 | Photon | 14.5 → 15.7.6 | 15.7.7, 16.5.1 | CVE-2023-32434 |
| 权限提升 | Parallax | 16.4 → 16.7 | 17.0 | CVE-2023-41974 |
| 权限提升 | Gruber | 15.2 → 17.2.1 | 16.7.6, 17.3 | 无CVE |
| PPL绕过 | Quark | 13.X | 14.5 | 无CVE |
| PPL绕过 | Gallium | 14.x | 15.7.8, 16.6 | CVE-2023-38606 |
| PPL绕过 | Carbone | 15.0 → 16.7.6 | 17.0 | 无CVE |
| PPL绕过 | Sparrow | 17.0 → 17.3 | 16.7.6, 17.4 | CVE-2024-23225 |
| PPL绕过 | Rocket | 17.1 → 17.4 | 16.7.8, 17.5 | CVE-2024-23296 |

*表1:CVE与代号映射表*

值得注意的是,**Photon和Gallium利用的漏洞也曾被用作零日漏洞**,是卡巴斯基在2023年发现的三角行动[3]的一部分。

Coruna工具包还内嵌了可重用模块,简化了上述漏洞的利用。例如,有一个名为`rwx_allocator`的模块,使用多种技术绕过各种缓解措施,防止在用户态分配RWX内存页。内核漏洞利用也嵌入了各种内部模块,允许绕过基于内核的缓解措施,如内核模式PAC。

---

### 最终载荷:加密货币窃取器

在漏洞利用链的最后,一个名为`PlasmaLoader`(GTIG追踪为`PLASMAGRID`)的加载器二进制文件,使用`com.apple.assistd`作为标识符,促进与内核组件的通信。加载器将自己注入到`powerd`中——一个在iOS上以root权限运行的守护进程。

**注入的载荷并没有展现出我们从监控厂商那里预期看到的常规功能,而是专注于窃取金融信息**:

* • 解码磁盘上图像中的二维码
* • 分析文本块以查找BIP39[4]助记词序列或特定关键词(如"backup phrase"或"bank account")
* • 如果在Apple备忘录中发现此类文本,将发送回C2服务器

更重要的是,载荷能够远程收集和运行额外模块,配置从`http://<C2 URL>/details/show.html`获取。配置和额外模块都被压缩为7-ZIP存档,受唯一硬编码密码保护。

大多数识别出的模块设计统一,都是通过函数钩子窃取以下应用程序的加密货币钱包或敏感信息:

* • BitKeep、Bitpie、Coin98、Coinbase Wallet
* • Exodus、imToken、Krystal、MetaMask
* • MyTonWallet、Phantom、Ronin Wallet、Solflare
* • TokenPocket、Tonhub、Tonkeeper、TronLink
* • Trust Wallet、Uniswap

所有这些模块都包含用**中文编写的日志**:

```
<PlasmaLogger> %s[%d]: CorePayload 管理器初始化成功,尝试启动...
```

一些注释甚至包含表情符号,其写作方式暗示**可能是由大语言模型生成的**。

网络通信通过HTTPS进行,收集的数据使用AES加密后POST提交,密钥为静态字符串的SHA256哈希。植入程序包含硬编码C2列表,但有备用机制。它嵌入了自定义域名生成算法(DGA),使用字符串"`lazarus`"作为种子生成可预测域名列表。域名为15个字符,使用`.xyz`作为顶级域名。攻击者使用Google的公共DNS解析器验证域名是否激活。

---

### 结论

Google一直是帕尔马尔进程[5]的坚定参与者,该进程旨在建立共识,限制间谍软件行业造成的危害。我们共同致力于制定国际规范和框架,限制这些强大技术的滥用,保护全球人权。

这些努力建立在早期政府行动的基础上,包括美国政府采取的措施[6]限制政府使用间谍软件,以及首个国际承诺[7]采取类似努力。

---

### 致谢

我们要感谢Google Project Zero[8]和Apple安全工程与架构团队在整个调查过程中的合作。

---

### 威胁指标(IOCs)

##### Implant

|  |  |
| --- | --- |
| **bundleId** | **SHA-256** |
| `com.apple.assistd` | `2a9d21ca07244932939c6c58699448f2147992c1f49cd3bc7d067bd92cb54f3a` |

##### Modules

|  |  |
| --- | --- |
| **bundleId** | **SHA-256** |
| `com.apple.springboard` | `18394fcc096344e0730e49a0098970b1c53c137f679cff5c7ff8902e651cd8a3` |
| `com.bitkeep.os` | `6eafd742f58db21fbaf5fd7636e6653446df04b4a5c9bca9104e5dfad34f547c` |
| `com.bitpie.wallet` | `42cc02cecd65f22a3658354c5a5efa6a6ec3d716c7fbbcd12df1d1b077d2591b` |
| `coin98.crypto.finance.insights` | `0dff17e3aa12c4928273c70a2e0a6fff25d3e43c0d1b71056abad34a22b03495` |
| `org.toshi.distribution` | `05b5e4070b3b8a130b12ea96c5526b4615fcae121bb802b1a10c3a7a70f39901` |
| `exodus-movement.exodus` | `10bd8f2f8bb9595664bb9160fbc4136f1d796cb5705c551f7ab8b9b1e658085c` |
| `im.token.app` | `91d44c1f62fd863556aac0190cbef3b46abc4cbe880f80c580a1d258f0484c30` |
| `com.kyrd.krystal.ios` | `721b46b43b7084b98e51ab00606f08a6ccd30...