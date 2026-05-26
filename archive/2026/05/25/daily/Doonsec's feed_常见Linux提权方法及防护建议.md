---
title: 常见Linux提权方法及防护建议
url: https://mp.weixin.qq.com/s/gZVYIlFbxWLnWdWQy3x8KA
source: Doonsec's feed
date: 2026-05-25
fetch_date: 2026-05-26T06:01:16.145877
---

# 常见Linux提权方法及防护建议

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/Gdu7PMCZg1Wh6g6yYScDmw1OwiaicfIa96dPFwGOj7uYhibKbzsbe6BSv8HARsl0fEjQ5UDwgu61nPNoDFhUJEp7EC73XxKibfmNWMdaxQrXfLA/0?wx_fmt=jpeg)

# 常见Linux提权方法及防护建议

搜狐安全

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

![](https://mmbiz.qpic.cn/mmbiz_png/Gdu7PMCZg1XpcWL2G9sm2ibTRQTtNdzxbATId63MWkjDLKQLx7RoyrGTUeAa7txGF2qV6LTNzMrGY1cksaQZrXsLibP1hdqzKQEDyppFRHXibA/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/vS6eQicRY6DAILuiaPanZx5LaibWTlBwRd3w5FCFhdn0BVIgqakmJDhHSrmdIXaQUtYzGWic4Wvic95JO45tlWZibFuw/640?wx_fmt=png)

![](https://mmbiz.qpic.cn/mmbiz_png/ibiam3zEgeEV5NCZHFlFGjd1Xfcq3GtWaheaQ6AiaZIXOu9grVg2JWZgON6VRKHdMw3FGzH0xCXa1w71HqPcicXURA/640?wx_fmt=png)

Linux系统通过严格的用户和组权限模型实现多用户隔离，每个进程和文件都有明确的读、写、执行权限归属。在这种设计下，普通用户只能访问自身拥有的资源，而root用户则拥有系统的完全控制权。

提权（Privilege Escalation），就是指攻击者从一个低权限账户（如Web服务运行的www-data用户、或通过弱口令获取的普通SSH账户）出发，利用系统配置缺陷或软件漏洞，将自身权限提升至root权限的过程。

在真实的攻防场景中，提权往往是整个攻击链中承上启下的关键一步。攻击者通过Web漏洞、弱口令等方式获得的初始立足点通常是低权限的；只有完成提权，才能进一步横向移动、安装持久化后门、窃取核心数据。理解提权的常见手法，是做好防御的前提。

![](https://mmbiz.qpic.cn/mmbiz_png/aFb4Q75OW00TY4hfnVcdkRcCPKVSEdAfXKwiaCIRMztick8iaQJ5ic5ePp3knJ2fp249qPtgYGtvbr17NXuQSTKAfw/640?wx_fmt=png)

![](https://mmbiz.qpic.cn/mmbiz_png/icTPiaaqor4ibZ6bExU5nT2CNpeNibcSIJpHc63evNrLibyjq68g4ZgXlIC4FfHW5Hd5W75zwgMOyY69tJz6B0nYHKA/640?wx_fmt=png)

![](https://mmbiz.qpic.cn/mmbiz_gif/2Dkp7U8D8pM29mxCMDMwNrl5MC6Bia8clV6blVZ4X92GhoiaqDibkKjeuibkSeerbrVksRxaFFYUyic0O9icPKxuColQ/640?&wx_fmt=gif)

常见提权方法与案例

一

SUID提权

**原理简介**

SUID（Set User ID）是Linux文件系统的一种特殊权限位。当一个可执行文件被设置了SUID位且文件所有者为root时，任何用户执行该程序，进程将以文件所有者（root）的权限运行，而非执行者自身的权限。

很多系统工具（如passwd、sudo自身、ping）必须具有SUID权限才能完成需要特权的操作。但问题在于，如果某些程序具有SUID权限却又允许用户执行任意系统命令，它们就成了通往root的“后门”。

**提权案例**

1、利用find命令提权

通过 find / -perm -4000 -print 2>/dev/null 查找具有SUID 权限的程序，发现find命令具有SUID权限，此时普通用户可以利用find命令进行提权到root权限。find的-exec选项本用于对搜索结果执行指定命令，但由于SUID-root上下文的存在，执行命令时进程继承了文件所有者的root权限。

![](https://mmbiz.qpic.cn/mmbiz_png/Gdu7PMCZg1ULkH1lx1tXzBYCTBldsCjV8GzickdDkqlWl4kZo5NgEIqiaMCRSNSq3P8iaqxrN1QWjMKYyicfNn6HNdC9L2bBkCIP0sDfJib0Tflk/640?wx_fmt=png&from=appmsg)

2、利用vim提权

当一个可执行文件被设置了 SUID 位后，普通用户执行它，会暂时获得该文件所有者（通常是 root）的权限。Vim 强大的功能（尤其是执行外部命令和脚本的能力），让这变得非常危险。当赋予vim程序SUID权限时，可通过如下命令进行提权，使得普通用户获取root权限。

![](https://mmbiz.qpic.cn/mmbiz_png/Gdu7PMCZg1UZ8I67KpT7vfkoxmEWNJvaGMGY6u3icicsvOicnfdGra9CIDF65FWicRgcdYQMVcRDdzMPQpCduFyniaK3NzSX9TZJjUUHQEicBGWj0/640?wx_fmt=png&from=appmsg)

**安全建议**

1、使用find / -perm -4000 -type f命令定期审计系统中的SUID文件清单，确保每一项都有明确的业务必要性。

2、对不需要SUID权限的程序及时移除SUID位：chmod u-s /path/to/binary。

![图片](https://mmbiz.qpic.cn/mmbiz_png/MHUYuRza9XXs6ZgPXPgq4d0EamTH6xXcMNoCuad3NGhB6S5ehibqZF6DYedz1aVQuKYbqvjclEkKgLVJRGWpeiaw/640?&wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp#imgIndex=1)

二

SUDO提权

**原理简介**

sudo（Superuser Do）是Linux权限管理的核心工具，允许系统管理员在/etc/sudoers文件中精细定义哪些用户或组可以以哪些身份（默认root）执行哪些命令。

sudo的设计初衷是践行“最小权限原则”——运维人员日常使用普通账户，仅在需要时通过sudo临时提权。但实际配置中，过度授权、危险命令放行以及sudo自身的代码漏洞，往往让这道“安全阀门”变成直达root的通道。攻击者拿到低权限账户后，通常以sudo -l命令作为提权路径探测的第一步。

sudo提权的攻击面主要分为两类：配置不当和软件漏洞。

**提权案例**

1、配置不当类提权

这是最常见的一类sudo提权，典型场景包括：

授予了可以执行任意命令的权限：配置user ALL=(ALL) ALL或user ALL=(ALL) NOPASSWD: ALL，攻击者直接`sudo /bin/bash`即可获得root 权限。

授予了高风险单命令：如devuser ALL=(root) NOPASSWD: /usr/bin/python3，攻击者可通过`sudo python3 -c 'import os; os.system("/bin/bash")'`实现逃逸。

环境变量劫持：若sudoers中配置了Defaults env\_keep += "LD\_PRELOAD"，攻击者可编译恶意动态库并通过`sudo LD_PRELOAD=/tmp/malicious.so /bin/ls`的方式在root权限下加载恶意代码。

如下，由于为普通用户错误配置sudo，授予了可以执行任意命令的权限，导致普通用户无需密码可提权至root权限。

![](https://mmbiz.qpic.cn/mmbiz_png/Gdu7PMCZg1UzfAyMN7MRnuYN1ANtQYlRC0ia7MgQjmZ2kqL1U72I7KPcWOYwY9TjyXm3ZtTn1TW1NKMkN0baAonIkNqKQ2V4AYH0DA5ZpBT8/640?wx_fmt=png&from=appmsg)

授予了高风险单个命令可执行权限，此时可以利用该命令提权为root权限

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Gdu7PMCZg1WY0vBG53sicP3Yt94AvzBEt0wibQaxKVc4gvf0T93quiaNIaja09OB9vj01EIty1Y8tiarWVuPcGR3XIEIibxBqglYvTPlLevcrUHA/640?wx_fmt=png&from=appmsg)

2、sudo漏洞类提权

以CVE-2021-3156：Sudo 堆缓冲区溢出漏洞为例，该漏洞是由于sudo解析命令行参数时发生了基于堆的缓冲区溢出。导致任何本地用户都可以利用此漏洞获得root权限。

如下在受影响的Linux系统上执行提权程序，成功获取root权限。

![](https://mmbiz.qpic.cn/mmbiz_png/Gdu7PMCZg1UU9hcLoTuibNn1O8WWicRT2L8ezWkSCW7LAL16ibEuJnLcqyJ20dicAXgVkhgkOPSzxboYvSaVV6bm8B5aED8cYfcG0KwMxLiakcoo/640?wx_fmt=png&from=appmsg)

**安全建议**

1、遵循最小权限原则：避免配置ALL=(ALL) ALL或NOPASSWD: ALL；精确到具体命令+参数；能不给NOPASSWD就不给；定期审查sudo -l输出和/etc/sudoers配置。

2、及时更新sudo至安全版本，确保不受已知漏洞影响。

3、开启并集中收集sudo审计日志（/var/log/auth.log），监控异常的sudo调用模式。

![图片](https://mmbiz.qpic.cn/mmbiz_png/MHUYuRza9XXs6ZgPXPgq4d0EamTH6xXcMNoCuad3NGhB6S5ehibqZF6DYedz1aVQuKYbqvjclEkKgLVJRGWpeiaw/640?&wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp#imgIndex=1)

三

内核漏洞提权

**原理简介**

内核漏洞提权是最直接、也是最危险的一类提权方式。由于Linux内核运行在系统的最高特权级，一旦攻击者利用内核缺陷执行任意代码，便能直接获得root权限。这类漏洞通常源于内存管理、文件系统、加密子系统等内核关键组件中的竞态条件、缓冲区溢出或逻辑缺陷。

**提权案例**

1、Dirty Pipe（CVE-2022-0847）

Dirty Pipe是2022年最具影响力的内核提权漏洞之一。其原理是：内核管道（pipe）的缓冲区在某些情况下未正确清除标志位，导致攻击者可以通过管道向任意只读文件（包括/etc/passwd）中写入数据，最终实现提权。攻击者只需编译并运行公开的PoC代码，即可将一个低权限用户添加到/etc/passwd中并赋予root权限，或者直接覆写具有SUID权限的二进制文件来植入后门。

![](https://mmbiz.qpic.cn/mmbiz_png/Gdu7PMCZg1WjIb3jRHMxFzdWdfN6dicNVjwT3klRfTRz4R07VZVh3k14wJRMR8JVoVrFqNnu2QKqZflVFPHFKZorBLvuBWE5icqGgJUriada8A/640?wx_fmt=png&from=appmsg)

2、Copy Fail提权（CVE-2026-31431）

该漏洞源于内核 crypto: algif\_aead 模块在处理 AEAD操作时的逻辑缺陷，可导致本地低权限攻击者通过 AF\_ALG 加密接口向任意可读文件的页缓存（page cache）写入受控的少量数据，进而篡改 setuid 等特权二进制文件，实现本地权限提升至 root。

![](https://mmbiz.qpic.cn/mmbiz_png/Gdu7PMCZg1WxJiaYmyfUQHbNxicic5JvJnhbKibXbWicPVic2Cryg2lVKtsd2fUwwkXia8ooZic9B8nd0bhrwiccyicYORxdEeytd2eXia1y30cZaMhTic8/640?wx_fmt=png&from=appmsg)

3、Linux Dirty Frag 提权漏洞（CVE-2026-43284）

该漏洞源于 xfrm-ESP（自2017年）和RxRPC（自2023年）两个独立模块的逻辑缺陷，同样利用splice()等零拷贝路径污染sk\_buff的frag成员，实现对页缓存的写入，从而在几乎所有主流Linux发行版上稳定提权，本地普通用户可无条件提权至 root 。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Gdu7PMCZg1UVUicrmzCKcjZs2mNvme3BnVXeXYlI8bunumVmAmno5icdAcZykS7oNAta9sgHksI8OibDEH421GnibxtlJCSfyDutMwukPUzoFO0/640?wx_fmt=png&from=appmsg)

4、Linux Kernel Fragnesia 提权漏洞（CVE-2026-46300）

该漏洞源于内核合并socket缓冲区时未能正确传播共享分片标记，导致攻击者可以将只读文件页缓存误当作ESP密文进行原地解密。利用此漏洞，本地非特权用户可通过splice和espintcp ULP组合操作，逐字节篡改文件页缓存（如/usr/bin/su），从而在不写入磁盘的情况下执行提权代码获取root权限。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Gdu7PMCZg1XUXZLH6YVtkicIWGvRCoSfZFt8ZzDVnDc6NuXo3rpN1uzLPXaZicsqKAP0wJ1HlxSibSfe9q9BxXMPCqud6P90ftLKiaYYamWPlqw/640?wx_fmt=png&from=appmsg)

**安全建议**

1、保持内核更新：及时更新内核至安全版本，确保不受已知漏洞影响。

2、最小化本地访问面：限制能登录系统的用户和来源范围。

![](https://mmbiz.qpic.cn/mmbiz_gif/2Dkp7U8D8pM29mxCMDMwNrl5MC6Bia8clV6blVZ4X92GhoiaqDibkKjeuibkSeerbrVksRxaFFYUyic0O9icPKxuColQ/640?&wx_fmt=gif)

总结

![](https://mmbiz.qpic.cn/mmbiz_png/vS6eQicRY6DAILuiaPanZx5LaibWTlBwRd3w5FCFhdn0BVIgqakmJDhHSrmdIXaQUtYzGWic4Wvic95JO45tlWZibFuw/640?wx_fmt=png)

![](https://mmbiz.qpic.cn/mmbiz_png/ibiam3zEgeEV5NCZHFlFGjd1Xfcq3GtWaheaQ6AiaZIXOu9grVg2JWZgON6VRKHdMw3FGzH0xCXa1w71HqPcicXURA/640?wx_fmt=png)

Linux提权是网络攻防中最具“实战价值”的技术领域之一，其攻击面主要来自三大方向：

1、SUID提权源于文件权限配置的“设计特性”——合理的SUID是必需的，但范围失控就成了后门。防御的关键在于持续审计SUID文件清单，对已知高危程序（find、vim、less等）严格排查，对不需要SUID权限的程序及时移除SUID位。

2、sudo提权分为配置不当（占比最高）和软件漏洞两类。sudo漏洞表明，即使sudo设计精良，其复杂特性（如chroot）也可能引入新的攻击向量。防御核心是“最小权限原则”——精准授权每一项sudo规则，并及时修补sudo自身漏洞。

3、内核漏洞提权是最底层、最危险的攻击方式。从经典的Dirty Cow（竞态条件）到Copy Fail（纯逻辑缺陷、仅需732字节脚本），内核缺陷一旦被利用几乎必然导致完全沦陷。防御手段包括：保持内核及时更新、禁用不必要内核模块、最小化本地访问面。

最后需要强调一条防范策略——限制SSH访问面：禁用不必要的root远程登录、启用SSH密钥认证、通过防火墙限制可登录的来源IP，能够从根本上降低攻击者获得用于提权的初始立足点的概率。在保障业务稳定运行的前提下，每一层访问控制和安全配置的严格到位，都是构筑系统防御纵深的关键。

![](https://mmbiz.qpic.cn/mmbiz_png/aFb4Q75OW00TY4hfnVcdkRcCPKVSEdAfXKwiaCIRMztick8iaQJ5ic5ePp3knJ2fp249qPtgYGtvbr17NXuQSTKAfw/640?wx_fmt=png)

![](https://mmbiz.qpic.cn/mmbiz_png/icTPiaaqor4ibZ6bExU5nT2CNpeNibcSIJpHc63evNrLibyjq68g4ZgXlIC4FfHW5Hd5W75zwgMOyY69tJz6B0nYHKA/640?wx_fmt=png)

![图片](https://mmbiz.qpic.cn/mmbiz_png/pUZUYTD28aBicPG8sba5NHSJ4wdW6fs2AHx2PcicU6yBQUbb1TsWFnYXtmXD7X0T8xvzceibPw57gY919J7cEt18A/640?wx_fmt=other&wxfrom=5&wx_lazy=1&wx_co=1&randomid=pz97pidk&tp=webp)

参考

奇安信CERT

    长亭安全应急响应中心

![图片](https://mmbiz.qpic.cn/mmbiz_png/Qvc3iaVjc5XwexerxgYHuNia5BjtSC4s99ibuB1t8anvHGPZUcGPzeh4ysQNCfYrfoHx21AWaxRibuUPJ9RIcjPlqw/640?wx_fmt=other&wxfrom=5&wx_lazy=1&wx_co=1&randomid=g13zrwj...