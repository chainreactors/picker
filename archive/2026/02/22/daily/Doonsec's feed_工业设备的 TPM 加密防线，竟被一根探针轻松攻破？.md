---
title: 工业设备的 TPM 加密防线，竟被一根探针轻松攻破？
url: https://mp.weixin.qq.com/s/krolJbpabCByqBwBMo07Hg
source: Doonsec's feed
date: 2026-02-22
fetch_date: 2026-02-23T04:15:29.464020
---

# 工业设备的 TPM 加密防线，竟被一根探针轻松攻破？

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/ibO9kiauylaDpLKmBgessZXeBRr8UdTetmVZLQpkW2RfiaVn4eAa0ptnrhptxEJ4iaUZDtYplBkwuZbOOs6vDib3A0q1kLZyibhZOqZnlsYO2A5OQ/0?wx_fmt=jpeg)

# 工业设备的 TPM 加密防线，竟被一根探针轻松攻破？

原创

黑鸟
黑鸟

黑鸟

![]()

在小说阅读器中沉浸阅读

在数字化工业时代，我们总以为 “硬件级安全加密” 是数据防护的铜墙铁壁。尤其是 TPM 2.0 安全芯片，早已成为 Windows 电脑 BitLocker 加密、工业嵌入式设备全盘加密的核心标配，被厂商宣传为 “密钥永不离开芯片” 的安全底座。

但 2026 年 2 月瑞典安全厂商 Cyloq 发布的 CVE-2026-0714 漏洞研究，彻底打破了这一安全幻觉：一台主打 “高安全工业级” 的嵌入式设备，其 TPM 保护的磁盘加密密钥，竟能通过简单的物理总线监听，被完整窃取明文，全程无需破解芯片、无需篡改系统，只需要一根逻辑分析仪探针。

## 先搞懂三个核心概念

在看懂这场攻击前，我们先把三个关键技术点讲明白：

1. **TPM 2.0 安全芯片**

   可以理解为设备主板上一个独立的 “硬件安全保险箱”。它自带独立处理器和存储，专门存放加密密钥、做身份校验，理论上核心密钥永远不会离开芯片内部，就算系统被攻破，密钥也不会泄露。

   ![](https://mmbiz.qpic.cn/sz_mmbiz_png/ibO9kiauylaDoibBSo9jaiaw9O8oev5CXIzCyRWYJF9uT9ttvAiaDSAajppOj8HO1ic360p8aJiaVrUNoqNJyuDgsyBFXicjdu7MJyud8T0xfPO4WN4/640?wx_fmt=png&from=appmsg)
2. **LUKS 全盘加密**

   Linux 系统最主流的磁盘加密标准，也是绝大多数工业嵌入式 Linux 设备的加密方案。设备开机时，需要从 TPM 中获取解密密钥，才能解锁系统盘，没有密钥就算拆下硬盘也读不出数据。
3. **SPI 总线**

   主板上芯片之间通信的 “数据线”。绝大多数独立 TPM 芯片，都是通过 SPI 总线和设备的主处理器（SoC）通信，就像保险箱和主机之间的 “专属通道”。

   ![](https://mmbiz.qpic.cn/sz_mmbiz_png/ibO9kiauylaDqlxcZ17jTSvpQia877L4qgxic3tl6D6qcKnUjxJutskIhVorDgzbfZxEZric6pRE9LqUKTwnYF1GctjCMNsxAjbiaXatRbXrIzAUU/640?wx_fmt=png&from=appmsg)

## 漏洞核心：加密只做了一半

##

这次漏洞的影响目标，是摩莎（Moxa）UC-1222A 安全版工业计算机。这款设备主打工业现场数据采集、边缘网关场景，厂商明确宣传其搭载独立 TPM 2.0 芯片，提供硬件级全磁盘加密防护，是工业场景的 “高可靠安全设备”。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ibO9kiauylaDqlvicXRoxkiamdIC8QzdePgYPzkiaL8bXn2xTE73Q1y90k93FNEqv8wNxy9SxhPdjREKHEg3jDtXoESFeAQXSfshHL60YBAwibbw0/640?wx_fmt=png&from=appmsg)

而研究员发现的核心问题，戳中了绝大多数 TPM 应用的通病：**厂商只做了 “保险箱的门锁校验”，却没给 “通道里的运输过程” 做任何加密**。

设备开机时，会执行一套固定流程：

1. 主处理器向 TPM 芯片发送`TPM2_NV_Read`指令，申请读取存放 LUKS 解密密钥的 NV 存储空间；
2. TPM 芯片校验 PCR 策略（也就是开机环境是否合法），校验通过后，就把完整的 LUKS 解密密钥准备好；
3. 最关键的一步：密钥通过 SPI 总线，**以明文形式**从 TPM 芯片传输给主处理器。

## 攻击全过程：4 步拿走密钥，门槛低到惊人

##

研究员完整复现了这场攻击，全程只需要基础的硬件工具，就能完成，对工业设备的威胁极大。

为了进行被动总线嗅探攻击，使用了 Logic 8 Saleae 8 通道逻辑分析仪。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ibO9kiauylaDooB1wfwZltIuvys3hE8cRCQlpLm0bu6CVUuMv77tiaricbhfy9owtBpgWSj5iag45qjPBXqadZgqZ5O6OVPZ3lNV3IVDf5x2UROs/640?wx_fmt=png&from=appmsg)

### 第一步：固件分析，找到密钥传输的 “命门”

研究员先下载了设备的官方固件，解压后分析开机启动脚本，很快找到了关键代码：设备在开机早期，会通过`tpm2_nvread`工具，从 TPM 的指定 NV 索引中读取 LUKS 密钥，授权绑定了 PCR 策略。

这行代码直接确定了攻击目标：只要监听到 SPI 总线上`TPM2_NV_Read`指令的响应包，就能拿到密钥。

### 第二步：硬件搭线，给总线装个 “监听器”

这款设备用的是英飞凌 SLB9670 TPM 2.0 芯片，研究员找到了芯片上 SPI 总线的 4 个关键引脚：片选（CS）、时钟（SCLK）、主机发从机收（MOSI）、从机发主机收（MISO），用 8 通道逻辑分析仪，直接把探针接在了对应引脚上。

![](https://mmbiz.qpic.cn/mmbiz_svg/Q3auHgzwzM71qw2oDnvrw0Ibl4cISOwxq0tQysfYZYsN8OozDnM9Y0ib3xgLKStCh9lySabtSSwsS7QMlGYjf6E2rRrMXhddZUuKyRvlZW3lf5qJKSgHbeQ/640?wx_fmt=svg&from=appmsg)

整个过程只需要基础的焊接和硬件操作，不需要破坏设备核心电路，全程被动监听，不会触发设备的任何安全告警。

嗅探SPI总线过程

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/ibO9kiauylaDrP1kcujibvUwFVUaxbpgocuXxtlNOczctZTlkyQT72KLKd4ibqaIm1LiaNJYh7nO5JntQoqlIZv0F7IPZEBjqqR7WdrIcqxOibibkc/640?wx_fmt=jpeg&from=appmsg)

下图总结了 SPI 的完整命令-响应流程。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ibO9kiauylaDpVVoUdFPS4iafqGEf3x4UOs8bzWJ7PiafCj6fZuib5LkqCiaf8QjTXhQFej2ybqPbRXQK86ynyB777Gjxtm5FbA7PjVG7vTo17vDs/640?wx_fmt=png&from=appmsg)

###

### 第三步：开机抓包，定位明文密钥

研究员设置逻辑分析仪以 250MS/s 的采样率，完整录制设备开机约 50 秒的 SPI 总线流量。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ibO9kiauylaDpPPibo1JGZ4DK0dcwcpelg29iaojeK5a7EibUn47sSSXy9AeeYVWd26XFPCJTd1BOgOS4janAVdCMXAl6icPFa63K4Znqs4iakPz4U/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ibO9kiauylaDpE5bBb9QiaEUMqibe6pKhzNLNxwallGEb0mYQ1fXgn0Miat1EXElnxNR6J031oTMOPSeTfbia9DvfB5FXKqPGHNaGvyg3qlWbwG68/640?wx_fmt=png&from=appmsg)

通过自定义脚本解析流量，很快就定位到了`TPM2_NV_Read`指令的发送位置，再对应解析从 TPM 发回主机的响应包，直接提取出了 128 字节的完整 LUKS 明文密钥。

![](https://mmbiz.qpic.cn/mmbiz_png/ibO9kiauylaDovtm899Eteia3Y5icYvWzNXtibxNMtFCPjRL13OicCV976Ac3budeBtglyHs17bQuia5b0L9GFoib1Z6brP3uXicpON75iaA5qFH4L8eo/640?wx_fmt=png&from=appmsg)

### ![](https://mmbiz.qpic.cn/mmbiz_png/ibO9kiauylaDqCWz7Mn0OsvfzW11icQW0cw64wVhZA3sIAZaLSWU3RibzKPGP1bSKKPxp9ZJlFLmD9sibR2aFlcgpvozj970TXPAzbibX7icBCIicj0/640?wx_fmt=png&from=appmsg)

###

### 第四步：验证密钥，彻底攻破加密

为了确认密钥有效，研究员拆下了设备的 eMMC 闪存芯片，用专用读卡器读出了完整的磁盘镜像。最终用嗅探到的密钥，成功解锁并挂载了 LUKS 加密的磁盘分区，完整获取了设备内的所有数据，攻击完全成功。

### 密钥验证过程

###

为了验证密钥的有效性，使用热风焊接将eMMC闪存芯片拆焊下来，然后使用Allsocket eMMC153读卡器重新安装并读取芯片。具体过程如下所示。

#### 步骤 1：涂抹焊剂

在 eMMC 闪存芯片上涂抹焊剂。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ibO9kiauylaDqFINnXtfHKicmD7NbpFdNuCVLia5x2owA85kTKBPkdIC3Is17zlBBjU67mqxACK6UAfKYFZZC2Ffia4aaRHnzSmSB80cbcUicV8l4/640?wx_fmt=png&from=appmsg)

#### 步骤二：拆焊芯片

采用热焊法移除eMMC芯片。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ibO9kiauylaDrmNQBe3bySibVaicLedicB3S1Ssic1icLtyXaowhic4pjutickYJRhtkotd0Tm5lBSMXAvysAyAgfe1kwPGaIbtm299KfOia8adjClnFA/640?wx_fmt=png&from=appmsg)

#### 步骤 3：去除浆糊

使用软毛（尼龙）牙刷和 99% 异丙醇去除 eMMC 上的残留物，然后使其干燥。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ibO9kiauylaDrcTjdVoLEg9eH2RyW4SqFh7JAXohRXZyXoVMiaLKBybUq6zPryiazytufOZ9BvXRFHqDBAWibPXokDichUlIlwsGZJqMpQa6kNMDs/640?wx_fmt=png&from=appmsg)

#### 步骤 4：读取 eMMC 芯片数据

使用 Allsocket eMMC153 读取器读取 eMMC 数据，并将其制作成镜像。

```
sudo dd if=/dev/disk9s3 of=emmc_moxa_dump_full5.img bs=4m status=progress
```

![](https://mmbiz.qpic.cn/mmbiz_png/ibO9kiauylaDqk3C4703sLzO7OERKm3Q4oWjvmXslksAdNQxojr3licFeaHAqzWHDm0NQtbeR8oAftGExF6uDulJE58G34RGic9LNdMjLQnRlv8/640?wx_fmt=png&from=appmsg)

#### 步骤 5：挂载镜像并成功测试密码

加密镜像随后被挂载，此时输入了密码短语（即 LUKS 设备密钥）。下面的屏幕截图显示，输入密码短语后镜像已成功挂载。这验证了嗅探到的密码短语是正确的。

![](https://mmbiz.qpic.cn/mmbiz_png/ibO9kiauylaDqWuQuVh1Vj6kxIo5n23zTPgLFuibsmpSOObN2hFgqKbxx3fnZRA2qHbVtMZUEDxJnlY8vaNt7FL95gicvop792jIaeVJQuGJ6TM/640?wx_fmt=png&from=appmsg)

## 这次攻击，到底特殊在哪？

##

其实 TPM 总线嗅探攻击并非新鲜事，此前已经有大量针对 Windows BitLocker 加密的同类攻击。但这次研究，给整个工业物联网安全敲响了新的警钟：

1. **首次公开针对工业嵌入式设备的 TPM 嗅探攻击**

   此前的研究大多聚焦个人电脑，而工业设备往往部署在无人值守的野外、工厂现场，攻击者有充足的时间物理接触设备，风险比个人电脑高几个量级。
2. **首次发现`TPM2_NV_Read`指令的明文泄露风险**

   此前的 BitLocker 攻击，大多针对`TPM2_Unseal`指令，行业几乎默认只有这个指令会泄露密钥。而这次研究证明，厂商定制化的`TPM2_NV_Read`方案，同样会让密钥明文传输，大量使用同类定制方案的工业设备，都可能存在同款漏洞。
3. **打破了 “定制化比通用方案更安全” 的误区**

   很多工业厂商不用 Linux 生态通用的 Clevis 加密方案，自己写了开机解密脚本，却反而忽略了传输层的加密，留下了致命漏洞。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ibO9kiauylaDrSMKzxYXncMwykia2GdiagiaI5OicyrDofD162J61rDCFJTUiaLepIENffiaVcZmFClr1XcFgbwiaLAuu9fWmnzNXiaf9Jl5tqib1jotTw/640?wx_fmt=png&from=appmsg)

## 怎么防？解决方案早就有，只是厂商没做

##

针对这类总线嗅探攻击，TCG（可信计算组织）早就发布了官方的 CPU-TPM 总线防护指南，核心解决方案就是**TPM 参数加密**。

简单来说，就是主机和 TPM 芯片先通过非对称加密，建立一个加密的会话通道，之后所有指令和密钥的传输，都用这个会话密钥加密。就算攻击者监听到了总线流量，拿到的也是密文，无法还原出真实的密钥。

其中，加盐会话（Salted Session）方案，就算没有用户输入 PIN 码这类高熵值密钥，也能通过非对称加密建立安全通道，完全适配工业设备无人值守、无用户交互的开机场景，唯一的缺点只是开机时会增加极短的密钥交换耗时，完全在可接受范围内。

CVE-2026-0714 漏洞的本质，从来不是 TPM 芯片本身出了问题，而是厂商的安全实现只做了表面功夫：只关注了 TPM 芯片内部的权限校验，却忽略了芯片和主机之间的传输安全。

硬件级安全的根基，在于全流程的安全设计，任何一个环节的疏忽，都能让整套加密体系彻底崩塌。而对于设备使用者来说，也需要清醒地认识到：“搭载 TPM 安全芯片” 绝不等于 “绝对安全”，设备的物理防护、厂商的固件安全更新，同样是不可或缺的防护环节。

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