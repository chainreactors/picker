---
title: 732字节Python脚本通杀所有Linux
url: https://mp.weixin.qq.com/s/80Rs5JStLYVl_virT2KWCQ
source: Doonsec's feed
date: 2026-05-01
fetch_date: 2026-05-02T04:55:28.305154
---

# 732字节Python脚本通杀所有Linux

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/4m3Pu8UEm8jUBicicYACVSOk7rBUVlVKj05hrkw42XRGu619PqVzqTqAe8GLmPDdRFynaT7nrR6AdzvP9wDN37BrmgXhLIAKuic0OOwHW3u0SU/0?wx_fmt=jpeg)

# 732字节Python脚本通杀所有Linux

原创

Faithtiann
Faithtiann

SEVENTEENSEC

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

**点击蓝字 关注我们**

**SEVENTEENSEC**

![](https://mmbiz.qpic.cn/mmbiz_png/bL2iaicTYdZn710IfjLq2GjCeJbfauy3eP0MNv9o4AHI2TSLSHMLH3qOCLBB8hZ7ia3VWiacBickgslKxBMxbNhmmDg/640?wx_fmt=png)

声明

⊙本文作者：Faithtiann

⊙本文字数：2051

⊙阅读时长：约10分钟

注：本文仅供安全研究与学习之用，由于传播、利用此文所提供的信息而造成的任何直接或者间接的后果及损失，由使用者承担全部法律及连带责任，作者及发布者不承担任何法律及连带责任

![](https://mmbiz.qpic.cn/mmbiz_gif/Ljib4So7yuWhsVYfr3PwkLGFZ0FmNEX7zggeMXLUy8qFbzh3dNSx4qom5TrnWcTf3hAK5c0JIKgRezicIBr0weww/640?wx_fmt=gif&from=appmsg)

**前言**

CVE-2026-31431（Copy Fail）是 Linux 内核中一个极为严重的本地提权漏洞。该漏洞潜伏在内核加密子系统中长达 9 年（自 2017 年内核版本 4.2 引入），允许拥有低权限的本地用户通过一段仅约 732 字节的 Python 脚本，稳定、无需竞态条件地获取系统的 root 权限。

![](https://mmbiz.qpic.cn/mmbiz_gif/Ljib4So7yuWhsVYfr3PwkLGFZ0FmNEX7zggeMXLUy8qFbzh3dNSx4qom5TrnWcTf3hAK5c0JIKgRezicIBr0weww/640?wx_fmt=gif&from=appmsg)

**漏洞原理**

**一、涉及的内核组件**

AF\_ALG 用户态接口

AF\_ALG是 Linux 内核提供的一种 socket 地址族，允许用户态程序直接调用内核空间实现的加密算法。其设计初衷是避免用户态与内核态之间的数据拷贝，提升加密操作的性能。

AEAD (Authenticated Encryption with Associated Data)

algif\_aead是 AF\_ALG 的 AEAD 加密接口实现。AEAD 是一种同时提供机密性（加密）和完整性（认证）的加密模式，典型代表如 AES-GCM、ChaCha20-Poly1305。

authencesn 模板

crypto/authencesn.c是内核中用于 IPsec 的认证加密模板，在标准的 AEAD 基础上增加了对扩展序列号（Extended Sequence Number）的处理。

**二、系统调用**

splice()是 Linux 内核提供的一种“零拷贝”数据传输机制，允许在两个文件描述符之间直接移动数据，而无需将数据拷贝到用户态缓冲区。当 splice()用于将文件数据导入内核时，它会将文件的“页缓存”（Page Cache）页面直接映射到内核的散射表（scatterlist）中。页缓存是 Linux 用于加速文件 I/O 的内存缓存机制——文件内容被加载到内存后，后续的读取可以直接从内存中进行。

关键特性：

- 页缓存页面通常被标记为“只读”（对于只读映射）

- 磁盘上的文件内容不会被修改

- 进程重启后，页缓存会被重新从磁盘加载

**三、漏洞核心：In-place 操作的逻辑缺陷**

漏洞的根源在于algif\_aead模块中 “In-place”操作与 “Out-of-place ”操作的处理逻辑错误。

In-place ：同一内存区域（源缓冲区） | 同一内存区域 （目标缓冲区）| 读写同一块内存，节省内存但需特殊处理

Out-of-place ：独立缓冲区（源缓冲区） | 独立缓冲区 （目标缓冲区）| 源和目标分离，更安全但消耗更多内存

在 2017 年（内核版本 4.2），内核引入了一项代码优化：在 algif\_aead中默认使用 “In-place” 操作，即源缓冲区和目标缓冲区指向同一块内存。这项优化在大多数场景下工作正常，但在与 authencesn模块和 splice()结合使用时，暴露出严重的逻辑缺陷。

**四、具体代码逻辑分析**

在 “crypto/authencesn.c”的解密路径中：

1. 攻击者通过 splice()将目标文件（如 /usr/bin/sudo）的页缓存映射到 AF\_ALG 接口的输入端。此时，这些页缓存页面在源 scatterlist 中，理论上应为“只读”。

2. algif\_aead因为使用了 in-place 操作模式，将源 scatterlist 同时作为目标 scatterlist 传入 authencesn的处理函数。

3.（漏洞点）authencesn在处理认证序列号时，需要在特定位置写入扩展序列号数据。但由于 in-place 模式下的逻辑缺陷，authencesn没有正确区分“只读源”和“可写目标"，而是直接将数据写入了页缓存页面。

4. 最终实现对任意可读文件页缓存的 “4 字节确定性写入”。

这是漏洞的核心利用原理。

Copy Fail 的独特危险在于：它不需要竞态条件，是确定性的逻辑错误。这意味着每次触发都会成功，极大地提高了攻击的可靠性。

![](https://mmbiz.qpic.cn/mmbiz_gif/Ljib4So7yuWhsVYfr3PwkLGFZ0FmNEX7zggeMXLUy8qFbzh3dNSx4qom5TrnWcTf3hAK5c0JIKgRezicIBr0weww/640?wx_fmt=gif&from=appmsg)

**漏洞复现**

安全提示：复现实验请在隔离的虚拟机环境中进行，切勿在生产系统上操作。

实验环境

ubuntu虚拟机

poc: https://github.com/theori-io/copy-fail-CVE-2026-31431

检查内核版本（2017年以后的内核均受影响）

uname -r

![](https://mmbiz.qpic.cn/mmbiz_png/4m3Pu8UEm8iaGDLWOiavvNIXU5q4SBM2cqtxRROjHiazPz0HRNpiaHn1AJ51G8cWrrVKav9WlBFlDshkBiaubPtuffYtOTXJQC033my1CMGhQTbg/640?wx_fmt=png&from=appmsg)

cat /etc/os-release | grep PRETTY\_NAME

![](https://mmbiz.qpic.cn/sz_mmbiz_png/4m3Pu8UEm8iaia8xM7tGblR5X9rP65qG05QzWKSUrcHclBDl7HN4Sau1QYk3fX7erq2icwnzRCuNq3wyeW6d8vEsbnNe5ba9ovNXLb1mP0aRG0/640?wx_fmt=png&from=appmsg)

确认当前权限身份

whoami

![](https://mmbiz.qpic.cn/mmbiz_png/4m3Pu8UEm8h5GHuPhaia5myZWeiaBf1bDsRoT4B66nonyWUcGHV6doUJC5KMHyiaM58VAarXeo1HLBH0ANoTt48ibdVj8tSCe5Ledxdzjm2RUZs/640?wx_fmt=png&from=appmsg)

id

![](https://mmbiz.qpic.cn/sz_mmbiz_png/4m3Pu8UEm8iaZjQqvPfepGRvm3YB5puAjiaZKKbH1ZgejK1ALmiakk9m8b1mWKBd6JnNyHQ45ZtvtYm2hpYJE5F2mVN9JfDTszNxbpDPtiaNiah4/640?wx_fmt=png&from=appmsg)

确认为普通用户身份，uid=1000，无 root 权限。这是攻击前的基准状态。

确认 AF\_ALG 可用

python3 -c "import socket; s = socket.socket(38, 5, 0); print('AF\_ALG available'); s.close()"

![](https://mmbiz.qpic.cn/mmbiz_png/4m3Pu8UEm8hn9GtQYKp3HD5g4Yz7SPwrF8a7vQEWofZp9pPdh9ib03Kkjj9n9tXhS293QJIxoQibvB5m0PQv5JSPFgaey0P7hIibJlUuwDiazE8/640?wx_fmt=png&from=appmsg)

执行poc

![](https://mmbiz.qpic.cn/mmbiz_png/4m3Pu8UEm8gD0ibfLKOVbLU7Yee9CPUjqibwH5xRvJNBZNE1htt1anNhpELfgXnyQhauTFVwTBBGhJ5NyzOmQm459L08pAeicCwhGauxRELLe4/640?wx_fmt=png&from=appmsg)

从普通用户（uid=1000）到 root（uid=0），一条命令完成提权

![](https://mmbiz.qpic.cn/mmbiz_gif/Ljib4So7yuWhsVYfr3PwkLGFZ0FmNEX7zggeMXLUy8qFbzh3dNSx4qom5TrnWcTf3hAK5c0JIKgRezicIBr0weww/640?wx_fmt=gif&from=appmsg)

**修复方案**

**官方补丁**

内核已经合入了修复补丁

改回 Out-of-place 模式——源缓冲区和目标缓冲区各用各的内存，从根本上消除只读页缓存被意外写入的可能。

**临时缓解**

生产系统如果暂时不能升内核，可以这么处理：

1.禁用AF\_ALG模块

```
modprobe -r algif_aeadecho "blacklist algif_aead" >> /etc/modprobe.d/blacklist-crypto.conf注意：这会影响IPsec、WireGuard等依赖内核加密的服务，评估后再操作。
```

2.容器环境加Seccomp限制

在Seccomp配置中禁止AF\_ALG（family 38）的socket调用，阻止容器内的利用。

3.AppArmor限制

在AppArmor profile中禁止AF\_ALG的创建。

**终极方案**

升内核

```
# Ubuntu/Debiansudo apt update && sudo apt upgrade linux-image-generic# RHEL/CentOSsudo yum update kernel# 然后重启sudo reboot
```

![](https://mmbiz.qpic.cn/mmbiz_gif/Ljib4So7yuWhsVYfr3PwkLGFZ0FmNEX7zggeMXLUy8qFbzh3dNSx4qom5TrnWcTf3hAK5c0JIKgRezicIBr0weww/640?wx_fmt=gif&from=appmsg)

**总结**

CVE-2026-31431核心问题在于内核为了优化性能引入in-place操作时，没有处理好只读页缓存的边界条件。但恰恰是这个"没处理好"，让任何本地低权限用户都有能力拿到root权限。

具有以下几个特点

利用简单：无需竞态条件，732 字节 Python 脚本即可提权

跨发行版通用：所有主流 Linux 发行版均受影响

隐蔽性强：仅修改内存页缓存，不触碰磁盘文件

建议所有 Linux 系统管理员立即检查内核版本并应用安全补丁。对于暂时无法更新的生产系统，应通过 Seccomp/AppArmor 等安全机制限制 AF\_ALG 接口的访问。

![](https://mmbiz.qpic.cn/mmbiz_gif/Ljib4So7yuWhsVYfr3PwkLGFZ0FmNEX7zggeMXLUy8qFbzh3dNSx4qom5TrnWcTf3hAK5c0JIKgRezicIBr0weww/640?wx_fmt=gif&from=appmsg)

**参考文献**

https://access.redhat.com/security/cve/cve-2026-31431

https://ubuntu.com/security/CVE-2026-31431

https://www.suse.com/security/cve/CVE-2026-31431.html

https://xint.io/blog/copy-fail-linux-distributions

https://avd.aliyun.com/detail?id=AVD-2026-31431

https://thehackernews.com/2026/04/new-linux-copy-fail-vulnerability.html

https://seclists.org/oss-sec/2026/q2/290

![](https://mmbiz.qpic.cn/mmbiz_gif/Ljib4So7yuWgwIJ2svTmD3XNSpBFCOE6gibb1htNqzfLXzmP84LEa6mO3ia2pU4h4DcmgYqQRoaveLfHicICiaFKAsg/640?wx_fmt=gif&from=appmsg)

**END**

![](https://mmbiz.qpic.cn/mmbiz_gif/Ljib4So7yuWgwIJ2svTmD3XNSpBFCOE6gibb1htNqzfLXzmP84LEa6mO3ia2pU4h4DcmgYqQRoaveLfHicICiaFKAsg/640?wx_fmt=gif&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_gif/Ljib4So7yuWiaZvzQWGW8xGYma0eamqH2lV0u8S7elr8u3INibfYv25JMIaTQV20VtcK6AD6UxppuzNSmAic18pG3g/640?wx_fmt=gif)

01

[CVE-2026-24061：潜伏11年的致命漏洞深度解析](https://mp.weixin.qq.com/s?__biz=Mzk2NDAwNzczNg==&mid=2247483982&idx=1&sn=71d6c4ef76e99215d9b954be98a269cf&scene=21#wechat_redirect)

02

[AI](https://mp.weixin.qq.com/s?__biz=Mzk2NDAwNzczNg==&mid=2247483891&idx=1&sn=000106066ba122d65230c48cb0ff1ce6&scene=21#wechat_redirect)[React2Shell 图形化漏洞检测利用工具](https://mp.weixin.qq.com/s?__biz=Mzk2NDAwNzczNg==&mid=2247483952&idx=1&sn=ccf1fe0d93cb80aa80b408f3a28a9575&scene=21#wechat_redirect)

03

[你的电脑里，有个"内鬼"叫DLL-----DLL劫持学习](https://mp.weixin.qq.com/s?__biz=Mzk2NDAwNzczNg==&mid=2247483940&idx=1&sn=bdb67ffcfa9fc6a94075f4f8b3e6ba5b&scene=21#wechat_redirect)

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/tibkFsH2X2WA7kS0WuSnAV8djMOSa6zSWf3icoDeWbphfBnMU2T8n4m9U9DtS2xWWPOK0sfOw92qxxkqj58SnSvA/0?wx_fmt=png)

SEVENTEENSEC

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/tibkFsH2X2WA7kS0WuSnAV8djMOSa6zSWf3icoDeWbphfBnMU2T8n4m9U9DtS2xWWPOK0sfOw92qxxkqj58SnSvA/0?wx_fmt=png)

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