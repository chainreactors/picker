---
title: DIDCTF-2025平航杯-流量分析
url: https://mp.weixin.qq.com/s/9d2H2Ac-29H_FSYaQymbKg
source: Doonsec's feed
date: 2026-01-16
fetch_date: 2026-01-17T03:22:15.824458
---

# DIDCTF-2025平航杯-流量分析

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/HtG3DtQMd7MicwDPZlDyDVjCyByg9ohuaUSMf0VmH8KukuwibJicvuXTWxDtPfPGRkwJKPnbicLBc8n00Jdcoo781Q/0?wx_fmt=jpeg)

# DIDCTF-2025平航杯-流量分析

原创

北渚
北渚

南有禾木

![]()

在小说阅读器中沉浸阅读

# 前言

记录DIDCTF中的2025平航杯的流量分析题目，这个有点意思啊，没有弄老套的HTTP协议分析，搞了蓝牙流量和USB键盘流量。

还是第一次分析蓝牙的流量，还有键盘流量，之前练的太少了，这次又熟悉了一些。

题目与检材都来自DIDCTF平台：`https://forensics.didctf.com/`

# **案情介绍**

2025年4月，杭州滨江警方接到辖区内市民刘晓倩(简称：倩倩)报案称：其个人电子设备疑似遭人监控。经初步调查，警方发现倩倩的手机存在可疑后台活动，手机可能存在被木马控制情况；对倩倩计算机进行流量监控，捕获可疑流量包。遂启动电子数据取证程序。 警方通过对倩倩手机和恶意流量包的分析，锁定一名化名“起早王”的本地男子。经搜查其住所，警方查扣一台个人电脑和服务器。技术分析显示，该服务器中存有与倩倩设备内同源的特制远控木马，可实时窃取手机摄像头、手机通信记录等相关敏感文件。进一步对服务器溯源，发现“起早王”曾渗透其任职的科技公司购物网站，获得公司服务器权限，非法窃取商业数据并使用公司的服务器搭建Trojan服务并作为跳板机实施远控。 请你结合以上案例并根据相关检材，完成下面的勘验工作。

**检材下载**

下载链接：`https://pan.baidu.com/s/1gTA5rG3pe1uMw5_KH5fckw?pwd=wiki`

挂载/解压密码：`早起王的爱恋日记❤`

---

提示：第 1 - 5 题涉及检材"BLE"，第 6 - 9 题涉及检材"USBPcap"。

# 流量分析

## 1、请问侦查人员是用哪个接口进行抓到蓝牙数据包的（格式：DVI1-2.1）

GPT：

```
蓝牙数据流一般是：走 USB或 UART或 PCIe / SDIO
在系统中体现为 HCI（Host Controller Interface）
```

随便点开个流量包，看`Interface name`：`COM3-3.6`

![](https://mmbiz.qpic.cn/sz_mmbiz_png/HtG3DtQMd7MicwDPZlDyDVjCyByg9ohuaj1FyicHsFGqGow3ZkUy9Gblj9jazJW5ibpQUHrIYgxKwoNviaickAU6e8g/640?wx_fmt=png&from=appmsg)

## 2、起早王有一个用于伪装成倩倩耳机的蓝牙设备，该设备的原始设备名称为什么（格式：XXX\_xxx 具体大小写按照原始内容）

蓝牙的流量包之前没分析过，打开之后首先看到两种类型的包：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/HtG3DtQMd7MicwDPZlDyDVjCyByg9ohuaexpCoyhciblicWaMm6DOWrJtFMuMw9eACTFSbDHxwqqU1laYw3KpDN0w/640?wx_fmt=png&from=appmsg)

原地址都是MAC地址，目的地址一种是MAC地址，一种是Broadcast

查阅了一下资料：

```
MAC->Broadcast 表示蓝牙广播行为，还没有配对，所有蓝牙设备都能收到该广播包
MAC->MAC 表示已经配对，两个蓝牙设备进行点对点通信
```

从流量包中找到了第一个出现的`Device Name`，第9个包，前面几个都没有Device Name：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/HtG3DtQMd7MicwDPZlDyDVjCyByg9ohua2HNkgCL4Kgk3WMdcibeN6nPVoicScgIwdpLN1gjsLxBoWVWgR8Y0wwfw/640?wx_fmt=png&from=appmsg)

但是这个是不是伪装的不知道，所以把这个流量保存成json，打开后提取出所有的Device Name，提取出来的内容去重一下：

```
"btcommon.eir_ad.entry.device_name": "Flipper 123all"
"btcommon.eir_ad.entry.device_name": "PE-YQ\u000eG\"QC31 IH"
"btcommon.eir_ad.entry.device_name": "Flippe��+Fta�d"
"btcommon.eir_ad.entry.device_name": "LE-QqNG QC75 II"
"btcommon.eir_ad.entry.device_name": "LE-_ANG QC35 II"
"btcommon.eir_ad.entry.device_name": "Fli0�\u0006��N�G��`"
"btcommon.eir_ad.entry.device_name": "Nlipper 123al"
"btcommon.eir_ad.entry.device_name": "RAP"
"btcommon.eir_ad.entry.device_name": "�APOO 5.0"
"btcommon.eir_ad.entry.device_name": "RAPOO 5.0MS"
"btcommon.eir_ad.entry.device_name": "LA-�A�� qC�5 Iu"
"btcommon.eir_ad.entry.device_name": "QQ_WF_SP8OON"
"btcommon.eir_ad.entry.device_name": "QQ_WF_SP8OOF"
"btcommon.eir_ad.entry.device_name": "QQ_WF_SP8�s{"
"btcommon.eir_ad.entry.device_name": "LE-YANG`QC\u00135 Ei"
"btcommon.eir_ad.entry.device_name": "Cracked"
"btcommon.eir_ad.entry.device_name": "LE-YANG QS35 II"
"btcommon.eir_ad.entry.device_name": "QQ_\u0017����Q)�u"
"btcommon.eir_ad.entry.device_name": "LE-YANG QC3�\u0007\u0003\f"
"btcommon.eir_ad.entry.device_name": "Flipper$123all"
"btcommon.eir_ad.entry.device_name": "QQWWF_SP8LON"
"btcommon.eir_ad.entry.device_name": "QQ_Wf_SP8OON"
"btcommon.eir_ad.entry.device_name": "QQ_WF_SPE�<�"
"btcommon.eir_ad.entry.device_name": "QQ_WF_SP�N\r�"
"btcommon.eir_ad.entry.device_name": "QQ_WF_SP8OoH"
"btcommon.eir_ad.entry.device_name": "L"
"btcommon.eir_ad.entry.device_name": "QQ_WF_SP8OM~"
"btcommon.eir_ad.entry.device_name": "QQoOJ^\u000bF8OON"
"btcommon.eir_ad.entry.device_name": "QQ_WF_�j/�d"
"btcommon.eir_ad.entry.device_name": "QQ_WF+�y�/��"
"btcommon.eir_ad.entry.device_name": "Q�l�Q��\u00028OON"
"btcommon.eir_ad.entry.device_name": "QQG�~ïB�OON"
"btcommon.eir_ad.entry.device_name": "QQg�6��?��\u0006�"
"btcommon.eir_ad.entry.device_name": "QQ_W���\u0003hN�O"
"btcommon.eir_ad.entry.device_name": "QQ_WV?%�^N�|"
"btcommon.eir_ad.entry.device_name": "QQ_WF_SP8\u000foh"
"btcommon.eir_ad.entry.device_name": "QQ_WF�\u001fP:oIB"
"btcommon.eir_ad.entry.device_name": "QQ_WF_SP>��X"
"btcommon.eir_ad.entry.device_name": "QQ_WF_SP8_Gh"
"btcommon.eir_ad.entry.device_name": "QQ_WF_SP�\b�)"
"btcommon.eir_ad.entry.device_name": "QQ_WF_SP:W�\u0004"
"btcommon.eir_ad.entry.device_name": "QQ_WF_SP8O�O"
"btcommon.eir_ad.entry.device_name": "QQ_WF_�gXN�h"
"btcommon.eir_ad.entry.device_name": "QQ_WF_SP8O_�"
"btcommon.eir_ad.entry.device_name": "QQ_WF_�V��ma"
"btcommon.eir_ad.entry.device_name": "QQ_WF_�V�\u0002W "
"btcommon.eir_ad.entry.device_name": "QQ_WF_SP8~�h"
"btcommon.eir_ad.entry.device_name": "LE-YM.G QC35 II"
```

然后一个个搜了一下，就这个`Flipper 123all`最有可能是：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/HtG3DtQMd7MicwDPZlDyDVjCyByg9ohuasgx7rQiaUrBzB9a7xnU3p5uWWYbII7Aiam4u0XIgPjJ8HdiaTkTY4hujA/640?wx_fmt=png&from=appmsg)

答案：`Flipper_123all`（答案中间不是空格是下划线…………没看到题目里的标准格式，坑啊）

## 3、起早王有一个用于伪装成倩倩耳机的蓝牙设备，该设备修改成耳机前后的大写MAC地址分别为多少（格式：32位小写md5(原MAC地址\_修改后的MAC地址) ，例如md5(11:22:33:44:55:66\_77:88:99:AA:BB:CC)=a29ca3983de0bdd739c97d1ce072a392 ）

首先原始的MAC地址是已经拿到了：`80:e1:26:33:32:31`

![](https://mmbiz.qpic.cn/sz_mmbiz_png/HtG3DtQMd7MicwDPZlDyDVjCyByg9ohuaBWdBHtjpV8axPibCF05MnNPM4KqBhxsKeh2wxS9zrEKPh3wEQibicXJSg/640?wx_fmt=png&from=appmsg)

然后过滤这个MAC地址：`btle.advertising_address == 80:e1:26:33:32:31`

发现这个地址的流量在33011到43427之间消失了一段时间：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/HtG3DtQMd7MicwDPZlDyDVjCyByg9ohuatDuJjTom7vT7kEoQFsmJhCpNcz24mR2pyHgiaOqHgbhyp9BRXj9KmEA/640?wx_fmt=png&from=appmsg)

从33011号包开始找，找到出现的第一个`device_name`，这个是33244号包：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/HtG3DtQMd7MicwDPZlDyDVjCyByg9ohuasxjRh4LNyLTKkm7xzGUAibicohh5VFjY2faaC9JND9kWS1KrEUcNLcRQ/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/HtG3DtQMd7MicwDPZlDyDVjCyByg9ohua6qgZ43bEzBgV2paibPgNjmuVo4wflylZ3PLOQ0yz3uwr5YRDCqUUDwQ/640?wx_fmt=png&from=appmsg)

并且这个MAC地址与前面那个Flipper123 all只差一个数字：

```
80:e1:26:33:32:31
80:e1:26:35:32:31
```

所以应该就是这个`QQ_WF_SP8OON`，但是它现在的MAC是伪造的，找到它的原始MAC：`btcommon.eir_ad.entry.device_name == "QQ_WF_SP8OON"`

![](https://mmbiz.qpic.cn/sz_mmbiz_png/HtG3DtQMd7MicwDPZlDyDVjCyByg9ohuaOdrXScFnyxdUX9ohb67juicw6BWajC3OnQNcSSOdD7wgia8vjVjwfhlQ/640?wx_fmt=png&from=appmsg)

```
80:E1:26:33:32:31
52:00:52:10:13:14
md5(80:E1:26:33:32:31_52:00:52:10:13:14)=97d79a5f219e6231f7456d307c8cac68
```

## 4、流量包中首次捕获到该伪装设备修改自身名称的UTC+0时间为？（格式：2024/03/07 01:02:03.123）

直接在流量包的JSON中搜第一个出现的`QQ_WF_SP8OON`：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/HtG3DtQMd7MicwDPZlDyDVjCyByg9ohuaDRY05xSe304fN5ejPeibJ6KUeFSG1eFv1ib2KRCoXV67Vbrz3uHnNq9g/640?wx_fmt=png&from=appmsg)

然后直接看这个包的时间即可：`2025/04/09 02:31:26.710`

![](https://mmbiz.qpic.cn/sz_mmbiz_png/HtG3DtQMd7MicwDPZlDyDVjCyByg9ohuaI9PlotXZSicE5zoOYlYoTAyCkECibibiaSVtMT21sSTl1icCFw6j3IWhs3A/640?wx_fmt=png&from=appmsg)

## 5、起早王中途还不断尝试使用自己的手机向倩倩电脑进行广播发包，请你找出起早王手机蓝牙的制造商数据（格式：0x0102030405060708）

这个先回到第三题，提取出的所有`Device Name`，先去掉Flipper与QQ\_WF\_SP这两个已经确定是耳机的，然后搜了一下RAP原来是雷柏啊：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/HtG3DtQMd7MicwDPZlDyDVjCyByg9ohuaKYIloPp2nhmbIFKoNEia8RlDM3uE4L1EDZrcsp7jHpKX7ia0ibGVMsXsg/640?wx_fmt=png&from=appmsg)

这个也去掉:

```
"btcommon.eir_ad.entry.device_name": "PE-YQ\u000eG\"QC31 IH"
"btcommon.eir_ad.entry.device_name": "LE-QqNG QC75 II"
"btcommon.eir_ad.entry.device_name": "LE-_ANG QC35 II"
"btcommon.eir_ad.entry.device_name": "LA-�A�� qC�5 Iu"
"btcommon.eir_ad.entry.device_name": "LE-YANG`QC\u00135 Ei"
"btcommon.eir_ad.entry.device_name": "Cracked"
"btcommon.eir_ad.entry.device_name": "LE-YANG QS35 II"
"btcommon.eir_ad.entry.device_name": "LE-YANG QC3�\u0007\u0003\f"
"btcommon.eir_ad.entry.device_name": "Flipper$123all"
"btcommon.eir_ad.entry.device_name": "L"
"btcommon.eir_ad.entry.device_name": "LE-YM.G QC35 II"
```

然后在里面看到了`Cracked`，我去，那这个肯定就是了，过滤：`btcommon.eir_ad.entry.device_name == "Cracked"`

![](https://mmbiz.qpic.cn/sz_mmbiz_png/HtG3DtQMd7MicwDPZlDyDVjCyByg9ohuaIT0bHLUx1mnEUctsLCk3qbic8QCbmPCXDwTNNicNnhBcHdKiaStFmGADw/640?wx_fmt=png&from=appmsg)

点开一个：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/HtG3DtQMd7MicwDPZlDyDVjCyByg9ohuaiasLkneNP3yI9hGHia0iacUeRmv76XRg7cthlORrvPuFALO1uWttWZ2Ng/640?wx_fmt=png&from=appmsg)

```
以下回答来自GPT：

一、制造商数据在什么位置？

在 BLE 广播 / 扫描响应中，制造商数...