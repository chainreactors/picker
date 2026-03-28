---
title: THE CAR HACKER’S HANDBOOK 第三章与第四章解读
url: https://mp.weixin.qq.com/s/-rRPURbNyA_eg7eL8Jg98A
source: Doonsec's feed
date: 2026-03-27
fetch_date: 2026-03-28T04:14:27.706128
---

# THE CAR HACKER’S HANDBOOK 第三章与第四章解读

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/94kIPh1QgiaCeRDBOiabqicwVicmn6E8eohfzvou2Mt8TibcFXKicsDMh4cqj72QEYex4dlhMrZ7zHf9Ct4eBSewh6eM8wCGmgR2M9SmHZwOibyySQ/0?wx_fmt=jpeg)

# THE CAR HACKER’S HANDBOOK 第三章与第四章解读

原创

朝阳
朝阳

Sec朝阳

![]()

在小说阅读器中沉浸阅读

## 第三章：车辆与 SOCKETCAN 通信

并非所有总线都通过 OBD-II 连接器。本章将设置 SocketCAN 系统，用来更方便的和汽车沟通。

大众集团贡献了最初的 SocketCAN 实现，内置 CAN 芯片和卡驱动、外部 USB 和串口 CAN 设备以及虚拟 CAN 设备。can-utils 包提供多种应用程序和工具，用于与 CAN 网络设备交互。

SocketCAN 与 Linux 网络协议栈相连，这使得创建支持 CAN 的工具变得非常容易。套接字 CAN 应用可以使用标准 C 套接字调用，并采用自定义网络协议家族 PF\_CAN。此功能使内核能够处理 CAN 设备驱动程序，并与现有网络硬件接口，提供通用接口和用户空间工具。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/94kIPh1QgiaBaLibNgX3TDcq1ZHI3SMtT8Uu6Zc6wa3A27KY3YvGZ8Xq29BWU0qrjPibwp08YDSv1uOqSy4Ue3tHNYY7hiazjqv3cFFnCVZib6UM/640?wx_fmt=png&from=appmsg)

传统的 CAN 软件则有自己的协议，通常与字符设备通信，比如串口驱动程序，然后是实际的硬件驱动程序。左侧的 SocketCAN 是在 Linux 内核中实现的。

### 设置 can-utils 以连接到 CAN 设备

apt-get install can-utils

### 配置内置芯片组

下一步取决于我们的硬件，如果在找 CAN 嗅探器，应该查看支持 Linux 驱动列表，确保设备兼容。

例如：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/94kIPh1QgiaBTCT2Rell7fNAGiaC84qNNIpcFeUgibhcxkZcEJ2I3KcjcmC69hhYALS0s7LSUunBrrKcwvOGh9frTDxn6z00JfhENgL6Q9Zdg8/640?wx_fmt=png&from=appmsg)

CAN 控制器，如 SJA1000,通常内置于 ISA、PCI 和 PCMCIA 卡或其他嵌入式硬件中。例如，EMS PCMCIA 卡驱动实现了对其 SJA1000 芯片的访问。当我们将 EMS PCMCIA 卡插入电脑中，ems\_pcmcia 模块会加载到内核中，内核则需要加载 sja1000 模块和 can\_dev 模块。

can\_dev 模块提供标准配置接口，例如用于设置 CAN 控制器的比特率。

Linux 内核的模块化概念通用适用于通过总线硬件连接 CAN 控制器的 CAN 硬件驱动程序，如 kvaser\_pci。

### 建立虚拟 CAN 网络

如果你没有 CAN 硬件，我们可以搭建一个虚拟 CAN 网络进行测试。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/94kIPh1QgiaCA3EQftBWibpJPh8E5LIv9DrFIEnKGia84qmerD1gTicaMLddXrR5ic3xJYibCLvbUnibIjfqNHtH2pngXssOtINNiaicgyMOwW2Yq2Xs/640?wx_fmt=png&from=appmsg)

激活 CAN 模块，linux 自带。

```
sudo ip link add dev vcan0 type vcan
sudo ip link set up vcan0
```

创建虚拟接口

![](https://mmbiz.qpic.cn/mmbiz_png/94kIPh1QgiaAEjUNH17jWUJ9vFvm9ibm1haiaRnjyYic5SlSXF46Nib7M3tHJIgiaDyuyfWXmsbBpRJ2BLcfA6hib9rJEqG8cpABn9iclDl5f47HYIQ/640?wx_fmt=png&from=appmsg)

然后我们安装一下工具包。

#### 嗅探并过滤噪音

这里做一个完整的实验来模拟。

首先我们开一个终端来监听 can 线。

 cansniffer -c vcan0

![](https://mmbiz.qpic.cn/mmbiz_png/94kIPh1QgiaDp6DmUrK7WfdhoQpeKOQUfrZW7eIbxGvOicG0hv5folicjXmtDK68TjNYjeicibUwLPic9AU3hgsFlbqibGlDiaVmXx8H64gQaiaDBRG0/640?wx_fmt=png&from=appmsg)

接下来我们发送噪音。

 cangen vcan0 -g 10 -I 123 -L 8

![](https://mmbiz.qpic.cn/sz_mmbiz_png/94kIPh1QgiaCPt1qjnWn6yaqXsICuAJGcfXW7MibqcFZmRN6ic4eR9nDUURc8bC6ETzvd5ib0ptA5Ua1ABhicd0cicBZzsqEae90keyURRfbMpGzI/640?wx_fmt=png&from=appmsg)

如果我们想去除某个噪音，就可以在 cansniffer 窗口按 -(减号)，然后输入 123 再按回车，ID 123 会从列表消失。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/94kIPh1QgiaADAORj0hTVmoZwgxqjibo0NoiaRavxtk0qeKbYLOvFFcra3Oiag8h7w2WxRcG2fvOGIoutFxJ2zzibpdTiaULNZf4pPjIl7UCPgxY8/640?wx_fmt=png&from=appmsg)

#### 记录总线数据

找到可疑 ID 后，我们要把它录下来，这里使用 candump。

我们能看到多了一个这样的日志文件。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/94kIPh1QgiaC5JK0z30ichk5OHzVda0aowPUGt9rlLztG7PuiayqNfon7SRUEDwIcxlHrHPCvj6niaGfUFT0iav9KdUsFR2FRG4sOs6oM7a3rR5k/640?wx_fmt=png&from=appmsg)

#### 重放攻击

我们捕获到数据包后能发现如下，cansend vcan0 5A1#11223344 正是我们发送的数据。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/94kIPh1QgiaDZSpqVoQJ5kwns2W2066zxLeBC7j9BZAAD7amhMpZwXCMkc9rd35DaDbc3Q3FTicwpLol6VQa7B79OgZDFKKm3ERngK1licSOC8/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/94kIPh1QgiaBF1pibAUWBmicxTIzl3wQtqVS3amhaPWxOyE3soOo3uDTbLRg9uTxyBRPjwKKo0gjNiaxBK1hX2pRlSvCcsq6qkwC7FUQqiamibgnU/640?wx_fmt=png&from=appmsg)

当我们重放后，发现 CAN 线收到了信息，证明重放成功。

## 第四章：诊断与日志记录

### DTC 诊断故障码

可以把汽车比喻为一个监测系统，我们发送一个不该发的包，或拔掉一个传感器，汽车就会在(PCM 动力控制模块) 上记下一笔，这就是 DTC。

RAM 存储(软故障)：断电后擦除。

持久存储(硬故障)：记载 PCM 上，支持掉电保护。

#### 故障等级

Class A(确认故障)：比如排放系统坏了，秒亮灯。

Class B(嫌疑故障)：比如某个传感器报错一次，汽车不会立刻亮灯，会把这个故障存为 Pending(待定) ，接下来在几次行驶中又错了，他才亮灯。

Class C/D(轻微)：可能只是提醒你去保养，或者根本不亮灯。

有时候我们测试完发现仪表盘没亮灯，不代表没触发故障，要用 03 指令去读有无 Pending 故障。

#### DTC 格式

DTC 是一种五字符的字母数字代码。例如，我们会看到像是 P0477 (排气压力控制阀) 和 U0151 (与约束控制模块失去通讯) 这样的代码。

第一个字节位置的代码代表了设置代码组件的基本功能。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/94kIPh1QgiaBibRS1CsFMmeYYoDcTRf90ibP5biczCibIsFtx2rtfTJW4DX0G1XHO7WEm8ic0aTHDFONDVXlsk2Z8Nbz6Ink7mAlKic2IGORmzFc4E/640?wx_fmt=png&from=appmsg)

当设置为 3 时，字节 2 既是 SAE 定义的标准，也是制造商特定的。最初 3 仅供制造商试验，但越来越多的压力推动将 3 标准化为标准代码。

![](https://mmbiz.qpic.cn/mmbiz_png/94kIPh1QgiaCYGcrwXvsDiczqxm4OibGnMmNyMd8icPJcZDQ7TDh6wPbo58ibg6pkC6hibEp25QmT8icQQAgA1XTyCCV9HfichdoJiaIak3Xgibno0REE/640?wx_fmt=png&from=appmsg)

撤了前两位，其他角色都是一对一的，参考 表 4-1 了解前两位分配方式。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/94kIPh1QgiaCRKu2IibrTIDdly08uA0IictVSGQkGibD2ZYDicRrhtfiarkgUgZd5umhicMHTMuPKS1oobdbRawXJaDD9B1brLEl6VEoKaWrTMDKKs/640?wx_fmt=png&from=appmsg)

### 暴力破解诊断模式

每个厂商都有自己的专有模式和 PID，通常可以通过"收购"的经销商软件、工具或暴力破解获得。

最简单的是CaringCaribou（CC）的开源工具。

### 自动事故通知系统

自动事故通知(ACN)系统是一种电话归属系统，主要用于联系车辆制造商或第三方，提供事件信息。

ACN 是每个制造商特有的，每个系统发送的信息也是不同的。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/94kIPh1QgiaACkicDgohlYy1W3yrOJFaz3M0cLl80Srjk7YIsgVo11bTuGawvTkmRWxQ3rOfq8tIZN17Ru4ysY2dibPxpibkAsIRib09Hlzbr4OE/640?wx_fmt=png&from=appmsg)

### 攻击视角

攻击者会盯上车辆的故障码(DTC) 和冻结帧(Freeze Frame) 数据，用来销毁证据。

冻结帧记录是故障发生那一瞬间的数据快照。因为记录有延迟，攻击者发送那种闪电式的工具，冻结帧根本抓不住，或者事后利用 0x04 指令清空记录，调查员就无法看出车辆是自然损坏还是被攻击。

当 DTC 当成雷达，反向探测漏洞

攻击者在车辆进行 FUZZ ，会把 DTC 当成反馈信号。

 通过 **0x08 模式** 探测厂商私有的 PID（指令集），会发现很多意想不到的结果。

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/HgEiaULLGWT1rh31vZg2fMe2vyiarFdM38QmFs6j6WLf5Zfu9LJDicbib1e9j0N4OpgeCiaFPXzmXbElD1sdZM3AwHg/0?wx_fmt=png)

Sec朝阳

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/HgEiaULLGWT1rh31vZg2fMe2vyiarFdM38QmFs6j6WLf5Zfu9LJDicbib1e9j0N4OpgeCiaFPXzmXbElD1sdZM3AwHg/0?wx_fmt=png)

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