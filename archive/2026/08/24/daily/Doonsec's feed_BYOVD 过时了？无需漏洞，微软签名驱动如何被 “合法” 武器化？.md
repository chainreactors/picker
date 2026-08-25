---
title: BYOVD 过时了？无需漏洞，微软签名驱动如何被 “合法” 武器化？
url: https://mp.weixin.qq.com/s/fwcren6Sj_4ZVufzV92T5w
source: Doonsec's feed
date: 2026-08-24
fetch_date: 2026-08-25T02:57:21.466258
---

# BYOVD 过时了？无需漏洞，微软签名驱动如何被 “合法” 武器化？

# BYOVD 过时了？无需漏洞，微软签名驱动如何被 “合法” 武器化？

decoylab
decoylab

吉宙实验室

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

![](https://mmbiz.qpic.cn/mmbiz_png/VQqGVAok0qrr96jCMf2fUOCIKxgiaLjW9mbsDwXiakPep3oN7aF6ubj2v5AcxWlfnTn5efRclibScianCiaRjZ4gFBA/640?from=appmsg)

点击蓝字

关注我～

一起发现更多精彩哟

![](https://mmbiz.qpic.cn/mmbiz_png/yD8EGuAMwkKtE35bkkAyaSqicNvicmnsHg3kbPYuhoLsickCwu559KCRMwmlYckjujRuQ2EJT3nrCDx7K8o3NzbZQ/640?from=appmsg)

最近，CheckPoint 发表了一篇可不依赖 BYOVD 技术对合法驱动进行滥用技术研究细节文章[1]，针对合法驱动，以往都是利用漏洞进行，而这一次却不是，当看到这篇报告时很感兴趣，想了解其中原理，以下是报告原文加上自己理解整理。

想一想，如果一个受信任的安全组件可以被重新利用，变成攻击者控制的内核原语，会怎么样？如果一个经过签名的微软修复驱动程序可以被指示从 Ring 0 执行任意文件和注册表操作而无需利用漏洞、避免内存损坏，又会怎么样？

CheckPoint 研究人员称这次发现是源于一次系统入侵事件响应调查，在调查过程中，发现终端遥测数据可疑，这些可疑的数据产生的源头是 Windows Defender，是由于一次修复行为产生，在 C:\Windows\System32\drivers 目录下出现一个随机命令的驱动程序，原始文件名 BTR.sys，驱动对应的服务名称也是随机化，注册表路径

```
HKLM\SYSTEM\CurrentControlSet\Services\mzqnjtaq
```

|  |  |  |
| --- | --- | --- |
| 键名 | 类型 | 数据 |
| Type | REG\_DWORD | [Kernel Driver] |
| Start | REG\_DWORD | [System Start] |
| ErrorControl | REG\_DWORD | [Ignore] |
| ImagePath | REG\_EXPAND\_SZ | \??\C:\Windows\System32\Drivers\mzqnjtaq.sys |
| Group | REG\_SZ | Boot Bus Extender |
| Args | REG\_SZ | C:\Windows\System32\Drivers\mzqnjtaq.sys:changelist |

研究人员认为以下几点和恶意内核加载器行为非常相似

* 系统重启前释放了一个驱动文件
* 创建了一个加载此驱动的临时服务名
* 有 RC4 加密数据
* 与驱动程序文件中的 ADS 流 (:changelist) 进行交互
* 执行后自动清理

其中 ADS 流中包含一个加密的二进制数据，用作驱动程序的配置输入。此驱动是由微软签名的合法文件，研究人员认为这可能是被攻击者利用或者滥用，最初他们的假设是攻击者利用了此驱动程序进行了后渗透利用，但最终证明该假设是错误的，这个行为是由 Defender 的合法修复引起的。

这一意外发现促使研究人员对 BTR.sys 进行了全面的逆向工程，揭示了未公开的功能、自定义协议以及出乎意料的强大内核执行模型。

BTR.sys 来自于 mpengine.dll，而 mpengine.dll 来自于 mpam-fe.exe。mpam-fe.exe 是 Windows Defender 防病毒软件的安全智能和病毒定义更新文件，里面包含了最新的病毒特征码，供手动更新使用，下载链接

```
https://go.microsoft.com/fwlink/?LinkID=121721&arch=x86https://go.microsoft.com/fwlink/?LinkID=121721&arch=x64https://go.microsoft.com/fwlink/?LinkID=121721&arch=arm64
```

文件大小 202MB 左右 (x86)，在资源表中存在 CAB 数据，大小占到了 99.8%

![](https://mmbiz.qpic.cn/sz_mmbiz_png/bCJqpmbtQZwHP2RIj6Izz4MicqE72x83E864ESRmG6b2FRBxic4nOI6b5M055ApTSqMGNp25wEs46SCPzRkK4YY20Ov0dR1qT8Sajbje6fF0Q/640?wx_fmt=png&from=appmsg)

将 CAB 数据 dump 出并尝试解压，里面包含 6 个文件

![](https://mmbiz.qpic.cn/mmbiz_png/bCJqpmbtQZxGZtOlEj0Oicfwic2vZbXFXHib2mPoXADRWl8qVwO9ibGbiaBs5xPLsuLia3bmcWInJfYibgGKWKH2xA4dYM8nibFbsGzQHvH3pVxfFc8/640?wx_fmt=png&from=appmsg)

作下简单说明：

* mpasbase.vdm - 随平台更新发布 (通常每月一次)，包含反间谍软件签名
* mpasdlta.vdm - 每日发布，仅包含新增的签名，在运行时加载数据库时，这些签名会在内存中与 mpasbase.vdm 进行合并
* mpavbase.vdm - 随平台更新发布 (通常每月一次)，包含反恶意软件签名
* mpavdlta.vdm - 每日发布，仅包含新增的签名，在运行时加载数据库时，这些签名会在内存中与 mpavbase.vdm 进行合并
* mpengine.dll - 实现了扫描器、模拟器、从 VDM 文件加载签名和签名处理等功能
* MpSigStub.exe - 主体文件运行后，用于更新病毒库

如果是自动更新，4 个 vdm 文件及 dll 文件会保存在以下目录中

```
C:\ProgramData\Microsoft\Windows Defender\Definition Updates\{随机 GUID}
```

最关键的文件是 mpengine.dll，关于它是如何解析 VDM 文件可单独另作一篇单独进行讨论

在它的资源表中，有一个内嵌的驱动文件数据，资源名为 BOOTTIMETOOL

![](https://mmbiz.qpic.cn/sz_mmbiz_png/bCJqpmbtQZwGQLiaxE0AJwJS3f1mqkdKcR6CngCZv2u0Kpq5gHWVJrk8Al731fzFYJdoxiacVClqP87iapIrt3Dx4FgmCwicVrw9991kRNsDz78/640?wx_fmt=png&from=appmsg)

而这个内嵌的驱动文件便是 BTR.sys

![](https://mmbiz.qpic.cn/mmbiz_png/bCJqpmbtQZzwdghuoAXZk3tM1ZiczQhoApvQVicjsmmk8RZtwbgqyKbNxYr3f2VibibHYPHbMwJqRJ1Zr7cSOGxaeCHtNvTgW5g2kKTW7vphzas/640?wx_fmt=png&from=appmsg)

从 mpengine.dll 中释放

![](https://mmbiz.qpic.cn/sz_mmbiz_png/bCJqpmbtQZzpPic1l3CPfprNtr9lEEictxsDbYokM1lvvMVTX8eGHliauK7gdaq6kxtcR0JVKEYwoqMiaDZLzicHCOxbCdk9ia6hDwBgzj0qt3JT0/640?wx_fmt=png&from=appmsg)

属于 "one-shot" 驱动，加载后完成预定的任务，汇报执行状态和结果，最后主动请求从系统中移除自己。

该驱动不提供 IOCTL 接口，而是读取服务注册表项中 Args 值指向的 Blob 配置数据，注册表路径

```
HKLM\SYSTEM\CurrentControlSet\Services\[随机值]\Args
```

![](https://mmbiz.qpic.cn/mmbiz_png/bCJqpmbtQZxiaz1hdpibGG5ugG4HOTpc3koVMym0QGYVicMljSFf97v5aLxS1juiaxgOfXqAvJuloKdokkHJtsAgbEOMiaVC0Pcsuj5YWYoG16uE/640?wx_fmt=png&from=appmsg)

Blob 配置数据包含 RC4 加密的 ADS 流

![](https://mmbiz.qpic.cn/sz_mmbiz_png/bCJqpmbtQZy1MTMKRfkBMiaJwUiaxicqfNTjlvYtvicar9PolJ7HoNDVG8fc2YWt1ibHiaJ9meNwSian8XhA3YdBBQ5U6m8CULe2SylsAOQt9vMsAU/640?wx_fmt=png&from=appmsg)

并受到加密和完整性检查的双重保护，以防止篡改，RC4 加密，KEY 硬编码在内

![](https://mmbiz.qpic.cn/mmbiz_png/bCJqpmbtQZxdKWIueauxBYDW6WGINoh8XibJbQnSVb5fWW1Bu1k5MpL9aajBBvPbAXdCSMwkibz9h5Fwve9BgmeRaibHPrvmDfxulE5z9J37Vc/640?wx_fmt=png&from=appmsg)

再做 CRC32 校验，它与标准 CRC32 实现稍有些许不同，在最后结果中并没有按位取反返回，所以这里的结果是标准 CRC32 校验值的再取反，即 ~CRC32

![](https://mmbiz.qpic.cn/sz_mmbiz_png/bCJqpmbtQZyymy3nMnGWZC5P5YTw54LadDD99U42N90mksyhgFQmlS7jJBeUAvGc3t6Mqmz7vdZibia4OTwaVzicUTzLTFYNIg49ia9uicmvibXF8/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/ic71wVtGetfHDu1wydMskOKuoXicunjouOlWhIdKVhicUw0VEEUibaahW73bFBktvxRUb7w5A9GS4POh7uqoAm4I8w/640)

![](https://mmbiz.qpic.cn/mmbiz_png/Bd7jlAWL2kJb0ad17GyZNCYMgklIXicN3a4gtzIPibVdu0k3QMYmTqXZcJbzKN4BCUdoPTPfNvEyOenQmWShIKUw/640)

![](https://mmbiz.qpic.cn/mmbiz_png/EeJSAMoAk9AaZBDONXq5mr1CnahhdFPRnN7Zk7c1R8mNJb1T2PCGUYiatym44rUOVbxzCHRByoeKaqz0Eh6o3ng/640)

BLOB 配置数据结构

![](https://mmbiz.qpic.cn/mmbiz_png/cZBtichFtVOicw0ecmyjicxsyvdEtIDcDaN5EoEiaejwr3qhO8FFapczeI7LbibJlGTxgjQIm6Avy8ISPuEPI6yus7Q/640)

![](https://mmbiz.qpic.cn/mmbiz_png/3QTIKn9jFuMib8ic1Qldejuib3qXtTqDpDTRq0ciaZRBbE4WGzg7K2FvVhaIJ4HM6gs06qqYzoiaz22FEF38R0Ozr8A/640)

![](https://mmbiz.qpic.cn/mmbiz_png/3AJf6zpEXO8e3OMs0hVse7E8dySmiaRe5p5vExYnzKGdUV6pMv9VmicM0ib4QIUj08lGtiaQp2dXbSn2coO8mK4yBg/640)

查看驱动文件的 BLOB ADS 流配置数据

```
Get-Item .\xxxxxxxx.sys -Stream *
```

![](https://mmbiz.qpic.cn/mmbiz_png/bCJqpmbtQZzI4K2QA6VVyuQRGcReBjicKtJ8mm176RzR1eusZWiaRma6h3avdyvQibRkpLOPgm7RYKBiaLAgbnOPpy0Pvw7hE0icGoCtWLPLIEjI/640?wx_fmt=png&from=appmsg)

提取 ADS 流数据并解密

```
$data = Get-Content .\xxxxxxxx.sys -Stream [ADS Stream name] -Raw -Encoding Byte[IO.File]::WriteAllBytes("[File Path]", $data)
```

![](https://mmbiz.qpic.cn/mmbiz_png/bCJqpmbtQZyibk8QAd27sTK3MiaCHVt2CRsZ602J8H9yp6Y4hiaIKMCPPn8H56OqpyiajHJgDhjeUovgkCt7UhIbanicKaH1dr5bMIvMoFZ2epRY/640?wx_fmt=png&from=appmsg)

解密后数据

![](https://mmbiz.qpic.cn/mmbiz_png/bCJqpmbtQZwDgpu3iaEUYht0YZwEY3eBsBEG9IpHtg7oGtxxWMTNOZQRFtmqBOYceibKVxPpHP8Ou5cn3lzWsDSASv5gkX300rvCLfUicDHFn0/640?wx_fmt=png&from=appmsg)

为方便查看定位，写了个模板来解析此结构

![](https://mmbiz.qpic.cn/sz_mmbiz_png/bCJqpmbtQZwQxmlHJUbpniaJKWzUmhb1ibFVbQAG8ViamTOd0jMB6bR4EDnNzcqHaYLsIlUGnG78qhXOjKSic2iaryBaT6UzbzTm7ls4OzS7e9ps/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/ic71wVtGetfHDu1wydMskOKuoXicunjouOlWhIdKVhicUw0VEEUibaahW73bFBktvxRUb7w5A9GS4POh7uqoAm4I8w/640)

![](https://mmbiz.qpic.cn/mmbiz_png/Bd7jlAWL2kJb0ad17GyZNCYMgklIXicN3a4gtzIPibVdu0k3QMYmTqXZcJbzKN4BCUdoPTPfNvEyOenQmWShIKUw/640)

![](https://mmbiz.qpic.cn/mmbiz_png/EeJSAMoAk9AaZBDONXq5mr1CnahhdFPRnN7Zk7c1R8mNJb1T2PCGUYiatym44rUOVbxzCHRByoeKaqz0Eh6o3ng/640)

Global Header

![](https://mmbiz.qpic.cn/mmbiz_png/cZBtichFtVOicw0ecmyjicxsyvdEtIDcDaN5EoEiaejwr3qhO8FFapczeI7LbibJlGTxgjQIm6Avy8ISPuEPI6yus7Q/640)

![](https://mmbiz.qpic.cn/mmbiz_png/3QTIKn9jFuMib8ic1Qldejuib3qXtTqDpDTRq0ciaZRBbE4WGzg7K2FvVhaIJ4HM6gs06qqYzoiaz22FEF38R0Ozr8A/640)

![](https://mmbiz.qpic.cn/mmbiz_png/3AJf6zpEXO8e3OMs0hVse7E8dySmiaRe5p5vExYnzKGdUV6pMv9VmicM0ib4QIUj08lGtiaQp2dXbSn2coO8mK4yBg/640)

开始 24 字节大小固定

|  |  |  |  |
| --- | --- | --- | --- |
| 偏移 | 大小 | 字段 | 描述 |
| 0x00 | 4 | Magic | 0xFEE1DEAD (小端序) |
| 0x04 | 4 | Version | 0x00000002 |
| 0x08 | 4 | PayloadOffset | 0x00000010 |
| 0x0C | 4 | GlobalCRC | ~CRC32 校验值 |
| 0x10 | 8 | TransID | 低 4 字节为 ~CRC32(Payload)，高 4 字节为 Size(Payload) |

注：以上结构包括后面提到的结构都是通过逆向工程获得，微软并没有公开文档记录

![](https://mmbiz.qpic.cn/mmbiz_png/ic71wVtGetfHDu1wydMskOKuoXicunjouOlWhIdKVhicUw0VEEUibaahW73bFBktvxRUb7w5A9GS4POh7uqoAm4I8w/640)

![](https://mmbiz.qpic.cn/mmbiz_png/Bd7jlAWL2kJb0ad17GyZNCYMgklIXicN3a4gtzIPibVdu0k3QMYmTqXZcJbzKN4BCUdoPTPfNvEyOenQmWShIKUw/640)

![](https://mmbiz.qpic.cn/mmbiz_png/EeJSAMoAk9AaZBDONXq5mr1CnahhdFPRnN7Zk7c1R8mNJb1T2PCGUYiatym44rUOVbxzCHRByoeKaqz0Eh6o3ng/640)

Global Payload

![](https://mmbiz.qpic.cn/mmbiz_png/cZBtichFtVOicw0ecmyjicxsyvdEtIDcDaN5EoEiaejwr3qhO8FFapczeI7LbibJlGTxgjQIm6Avy8ISPuEPI6yus7Q/640)

![](https://mmbiz.qpic.cn/mmbiz_png/3QTIKn9jFuMib8ic1Qldejuib...