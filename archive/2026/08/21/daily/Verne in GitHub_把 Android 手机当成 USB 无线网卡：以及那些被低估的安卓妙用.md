---
title: 把 Android 手机当成 USB 无线网卡：以及那些被低估的安卓妙用
url: https://blog.einverne.info/post/2026/08/android-phone-as-usb-network-adapter-and-more.html
source: Verne in GitHub
date: 2026-08-21
fetch_date: 2026-08-22T02:50:49.628690
---

# 把 Android 手机当成 USB 无线网卡：以及那些被低估的安卓妙用

[Verne in GitHub](/)

* [Archive](/archive.html)
* [Categories](/categories.html)
* [Friends](/friends.html)
* [Tags](/tags.html)
* Other
  + [About](/about.html)
  + [投资笔记](https://invest.einverne.info/)
  + [券商推荐](https://broker.einverne.info/)
  + [图书分享](https://book.einverne.info/)
  + [相册](https://photo.einverne.info/)
  + [Kindle 笔记](https://kindle.einverne.info/)
  + [IPFS 镜像](https://ipfs.einverne.info/)
  + [服务状态](https://status.einverne.info/)
  + [在线嘟嘟](https://m.einverne.info/%40einverne)

# 把 Android 手机当成 USB 无线网卡：以及那些被低估的安卓妙用 一次 PVE 硬盘迁移救急，让我重新认识了抽屉里的旧手机

Posted on 08/21/2026
, Last modified on 08/21/2026
by [Ein Verne](https://x.com/einverne)
| [View revision history](https://github.com/einverne/einverne.github.io/commits/master/_posts/2026-08-21-android-phone-as-usb-network-adapter-and-more.md)

昨天我把一块装着 [[Proxmox VE]] 系统的硬盘从之前的 SER8 拆下来，插到 4 盘位的 Me Pro 上，本以为开机就能继续用，结果卡在了最基础的一步：Me Pro 的物理网口和我原来的网口对不上，物理网口变更了名字导致无法上网。屏幕上 PVE 的控制台在闪，`ip addr` 里却无法找到两个物理网口，Web 管理界面自然也打不开。

![一台安卓手机通过 USB 线连接服务器，充当无线网卡](https://pic.einverne.info/images/2026-08-21-10-00-00-android-usb-network-adapter.png)

在和 Claude 交流寻找解决方案的过程中，我看到 Claude 说「用手机 USB 共享网络」，先确保 PVE 有网络，然后利用网络更新 Kernel。我开始还有点疑惑，这样也可以，但是手边正好有一台 Pixel，顺手就用 Type-C 数据线链接了，然后在 Android 端切换到 USB tethering，在 PVE 查看，立马就能看到多出一张网卡，利用 `dhclient enxxx` 就可以获取 IP 地址，立马就能 ping 通网络。

这个功能是，当手机自己连着 Wi-Fi 的时候，它同样可以把这份 Wi-Fi 网络通过 USB 线转发出去。换句话说，一根数据线加一台安卓手机，就等价于一张即插即用的 USB 无线网卡。

这件事让我开始重新审视抽屉里那几台退役的安卓手机。它们其实是完整的 ARM 计算机：有 CPU、有内存、有存储、有电池（相当于自带 UPS）、有 Wi-Fi 和蓝牙、有摄像头和屏幕、有 USB OTG。我们只是习惯性地把它们当作「淘汰的手机」，而不是「一台便宜的、带屏幕的、待机功耗只有几瓦的小型服务器」。

## 从一次救急说起，USB 网络共享到底做了什么

要理解为什么这招好用，得先知道手机在 USB 那端到底扮演了什么角色。安卓设备通过 USB 连接电脑时，可以以不同的 USB Gadget 身份出现：MTP 模式下它是一个媒体设备，ADB 模式下它是一个调试设备，而打开 USB 网络共享之后，它把自己声明成了一个 USB 网络适配器。

具体用的协议一般是 RNDIS（Remote NDIS，微软定义的一套通过 USB 承载以太网帧的规范），近几年不少设备也改用了更标准、效率更高的 CDC-NCM。这两种协议在 Linux 内核里都有现成的驱动，分别是 `rndis_host` 和 `cdc_ncm`，属于早就编译进主流发行版内核的东西。所以主机侧不需要装任何厂商驱动，插上线之后内核就会枚举出一张新的以太网接口，传统命名是 `usb0`，在启用了 systemd 可预测网卡命名的系统上则是 `enx` 加上 MAC 地址的形式，比如 `enx0a1b2c3d4e5f`。

有意思的是手机这一侧。它并不是简单地做一个透明网桥，而是实实在在跑了一套小型路由：手机在这个 USB 网络接口上给自己分配 192.168.42.129 这个地址，同时启动一个 DHCP 服务，把 192.168.42.0/24 网段的地址发给通过 USB 连过来的主机，然后对出站流量做 NAT，把它们转发到当前的上游链路。这个上游链路可以是移动数据，也可以是手机正连着的 Wi-Fi。安卓的 tethering 框架并不关心上游是什么，它只负责把默认路由指向那条可用的链路。这正是「手机变无线网卡」的关键：Wi-Fi 进，USB 出。

顺带一提，Wi-Fi 热点用的是 192.168.43.0/24，蓝牙共享用的是 192.168.44.0/24，这三个网段是安卓 tethering 的固定约定。知道这个在排查问题时很有用，看到 192.168.42.129 这个网关地址，你就能确定链路走的是 USB 而不是别的。

## 在 Linux 主机上把这条链路跑起来

PVE 基于 Debian，所以下面的步骤在绝大多数 Debian 系发行版上通用。先把线插上，在手机的设置里找到「网络和互联网 - 热点与网络共享 - USB 网络共享」并打开。注意这个开关往往是灰的，直到系统检测到 USB 数据连接才会变为可点，而且它要求你用的是数据线而不是只能充电的线，这个坑我踩过不止一次。

打开之后回到主机，先确认内核有没有认出设备：

```
lsusb
ip link
dmesg | tail -20
```

正常情况下 `ip link` 里会多出一张 `usb0` 或 `enx` 开头的接口，`dmesg` 里能看到类似 `rndis_host ... register 'rndis_host' at usb-0000:00:14.0-2, RNDIS device, 0a:1b:2c:3d:4e:5f` 的日志。如果什么都没出现，先手动加载一次驱动：

```
modprobe rndis_host
modprobe cdc_ether
modprobe cdc_ncm
```

接口出来之后，临时用的话一条命令就够了：

```
ip link set usb0 up
dhclient usb0
```

拿到地址后 `ip route` 里会出现指向 192.168.42.129 的默认路由，此时 PVE 的 Web 界面就能通过这个新地址访问了。如果你希望它持久生效，可以在 `/etc/network/interfaces` 里加一段：

```
allow-hotplug usb0
iface usb0 inet dhcp
```

`allow-hotplug` 而不是 `auto` 是有讲究的，手机不一定一直插着，用 `auto` 会让开机时因为等待这张不存在的网卡而拖慢启动。

有一点需要提醒：这套方案更适合救急和临时维护，不适合长期作为服务器的主链路。手机会不断被主机供电，长时间维持在满电状态对锂电池不友好，而且系统更新、电话来电、后台清理都可能中断这条链路。我的做法是把它当成「带外管理通道」，用它把机器救活、把正式网络配置好，然后拔掉。

## 在 PVE 上使用 Android USB Gadget

PVE 的特殊之处在于它既是宿主机也是虚拟化平台，所以这张「手机网卡」有两种用法，要根据目的选择。

第一种是留在宿主机上，也就是我前面救急时用的方式。适合的场景是宿主机自己失联了，你需要一条通道进入 Web 管理界面。配置就是上面那几条命令，不需要动虚拟化相关的东西。如果你还希望虚拟机也能借道上网，不要试图把 `usb0` 桥接进 `vmbr0`，这条路走不通。原因在于 RNDIS 接口只会为它对面的那一个 MAC 地址学习和转发，安卓侧不接受来自多个 MAC 的帧，桥接之后虚拟机发出的包能出去但回不来。正确的做法是在宿主机上做 NAT：

```
sysctl -w net.ipv4.ip_forward=1
iptables -t nat -A POSTROUTING -o usb0 -j MASQUERADE
```

这样挂在 `vmbr0` 上的虚拟机把网关指向宿主机，就能通过手机出网。要持久化的话把 `net.ipv4.ip_forward=1` 写进 `/etc/sysctl.d/`，NAT 规则用 `iptables-persistent` 保存。

第二种是把手机整个直通给某台虚拟机，比如你想让 OpenWrt 或者软路由虚拟机直接管理这条上行链路。在 PVE 的 Web 界面里，选中虚拟机进入硬件页，添加 USB 设备，这里会给出两种绑定方式：按厂商和设备 ID，或者按 USB 端口。

对安卓设备一定要选按端口。这是个容易忽略但很关键的细节：手机在切换 USB 模式时会重新枚举，Product ID 跟着变，比如 Pixel 在纯充电、MTP、ADB、网络共享几种状态下报的 ID 各不相同（Vendor ID 固定是 Google 的 18d1，Product ID 却会在 4ee1、4ee2、4ee7 之间跳）。如果你按 ID 绑定，用户在手机上一点「USB 网络共享」，设备就从虚拟机眼前消失了。按端口绑定则只认物理插口，无论手机怎么切换模式都能保持连接。

命令行的写法是先用 `lsusb -t` 找到总线和端口号，再挂给虚拟机：

```
lsusb -t
qm set 100 -usb0 host=1-4
```

其中 `1-4` 表示 1 号总线的 4 号端口，`100` 是虚拟机的 VMID。如果插的是 USB 3 口，可以加上 `usb3=1`。这个操作支持热插拔，虚拟机不需要重启就能看到新设备，虚拟机内部同样会出现一张 `usb0`，配置方法和前面完全一致。

两种方式不能同时使用。设备一旦直通给虚拟机，宿主机上的 `usb0` 就会消失，所以如果你的目的是抢救宿主机本身，老老实实用第一种。

## 旧手机是一台被低估的 ARM 服务器

救急之后我顺着这个思路想下去，安卓能做的远不止转发网络。最有想象空间的是 [[Termux]]，它在不 root 的前提下提供了一个相当完整的 Linux 用户空间环境，有自己的包管理器 `pkg`，能装 Python、Node.js、Go、Rust、git、ffmpeg、nginx、openssh 这些常规工具。你可以在手机上跑一个 sshd，然后从笔记本 ssh 进去，体验和登录一台小型 VPS 没有本质区别。

实际能落地的场景不少：把 [[Syncthing]] 装在旧手机上，它就是一个永远在线的同步节点，比常开一台 NAS 省电得多；用 Termux 跑定时任务抓取数据、做备份；跑一个轻量的下载器，配合外接的 OTG 硬盘当离线下载盒子；甚至可以跑 [[copyparty]] 这类文件服务，把手机的存储变成局域网里的文件共享点。一台闲置的旧机器待机功耗大概在 2 到 5 瓦之间，比树莓派还低，而且自带屏幕和电池。

如果你需要的是更完整的发行版而不只是 Termux 的环境，[[Andronix]] 或者 Termux 自带的 `proot-distro` 可以在用户态跑起 Debian、Ubuntu、Arch 的根文件系统。性能会因为 proot 的系统调用拦截而打折扣，但对于跑一些依赖 glibc 的软件是够用的。

## 投屏、反向控制与调试

[[Scrcpy]] 是我用得最频繁的工具之一。它通过 ADB 把一个精简的 server 推到手机上，用 H.264 编码把屏幕流传回电脑，同时把电脑的键鼠事件注入回手机。延迟通常在 35 到 70 毫秒之间，实际体验接近于手机变成了电脑的一个窗口，可以直接用键盘打字、用鼠标操作，还能拖拽文件安装 APK。不需要 root，也不需要在手机上装任何应用。

配合 ADB 还能玩出更多花样。`adb reverse tcp:8080 tcp:8080` 可以做反向端口转发，让手机上的应用访问到你电脑本地的服务，调试移动端对接本地 API 的时候特别方便。`adb shell` 则是一个完整的命令行入口，很多在 UI 上被厂商藏起来的设置项，都能通过 `settings put` 直接改。

## 摄像头、显示器与各种外设

Android 14 开始，系统原生支持把手机作为 USB 摄像头使用，插上电脑就会被识别成一个标准 UVC 设备，不需要装任何驱动或者第三方软件。对于手上有旗舰旧机的人来说，这基本是白捡了一个画质远超普通笔记本内置摄像头的网络摄像头。如果你的系统版本较低，DroidCam 或者 IP Webcam 这类应用也能达到类似效果，只是要走 Wi-Fi 或者 USB 转发，多一层配置。

反过来，手机也可以当显示器。spacedesk 这类工具把手机变成 Windows 的扩展屏，出差时带一台平板或者旧手机，就多了一块放监控面板、放文档的副屏。

USB OTG 则打开了另一扇门。旧手机接上 OTG 线之后可以读取 U 盘、SD 读卡器、移动硬盘，也可以接键盘鼠标。我见过有人把旧手机加 OTG 键盘当成一个极简的写作机器，续航一整天。

## 应急启动盘与串口控制台

这两个用法比较小众，但真到需要的时候特别救命。

DriveDroid 可以把手机模拟成一个 USB 存储设备或者光驱，直接把手机里存放的 ISO 镜像挂载给目标电脑启动。这意味着你不需要随身带 U 盘和 [[Ventoy]]，手机里存几个常用的救援镜像就够了。代价是这个功能需要 root 权限，因为它要操作内核的 USB Gadget 配置接口。

另一个是串口控制台。很多服务器、交换机、软路由的管理口是 RJ45 转串口或者 USB 串口，配一根 USB 转 TTL 的线（CH340 或者 FTDI 芯片都行）和一个 OTG 转接头，再装一个 Serial USB Terminal 之类的应用，手机就变成了一台便携的串口终端。机房里不用再抱着笔记本蹲在机柜前，这个体验的差别是巨大的。

## 网络诊断与抓包

PCAPdroid 是一个不需要 root 的抓包工具，它的实现思路很巧妙：利用安卓的 VpnService API 把本机流量引到自己的虚拟接口上，然后落盘成 PCAP 文件。你可以按应用维度过滤，看某个 App 究竟往哪些域名发了请求，也可以把抓到的包导出用 Wireshark 分析。对于研究某个应用的网络行为、排查国内 App 的隐私问题，这是最低门槛的方案。

再加上各种 Wi-Fi 分析工具能看信道占用和信号强度，手机其实是一个相当称职的现场网络诊断设备。装修布网络、排查家里 Wi-Fi 死角的时候，比拿电脑方便太多。

## 那些容易踩的坑

数据线是第一个坑，也是最常见的一个。很多随手机附赠的线或者从充电宝里翻出来的线只有电源触点，没有数据线芯，插上去手机只会显示充电，USB 网络共享的开关始终点不亮。换一根确定能传数据的线，能省掉半小时的排查。

后台被杀是第二个坑。国内定制系统的省电策略非常激进，Termux 里跑着的服务可能在你锁屏几分钟后就被清掉。对策是在系统设置里把这个应用加入电池优化白名单，同时在 Termux 里执行 `termux-wake-lock` 持有唤醒锁。如果需要开机自启，装一个 Termux:Boot 插件，把启动脚本放到 `~/.termux/boot/` 下。

还有一个比较隐蔽的问题：从 Android 12 开始，系统引入了 phantom process 限制，会主动杀掉应用派生出的子进程，默认上限是 32 个。这对普通应用没影响，但 Termux 里跑多个服务很容易触发，表现为进程莫名其妙消失。可以通过 ADB 关掉这个监控：

```
adb shell device_config set_sync_disabled_for_tests persistent
adb shell device_config put activity_manager max_phantom_processes 2147483647
```

需要注意这个设置在部分系统重启后会失效，需要重新执行。

最后是应用来源。Termux 的 Google Play 版本早已停止维护，功能残缺且不再更新，务必从 F-Droid 或者官方 GitHub Release 安装。这类工具类应用普遍存在类似情况，装之前多确认一下渠道。

## 最后

这次 PVE 迁移带来的最大收获是让我意识到自己对手上工具的想象力实在有限。一台安卓手机被我们默认框定在「打电话、刷视频、拍照」的用途里，但它的底层是一个跑着 Linux 内核的通用计算设备，具备网络栈、USB Gadget、传感器、编解码硬件这些完整的能力。厂商的 UI 只是把这些能力包装成了消费级的形态，而这些能力本身一直都在。

抽屉里那几台旧手机，我打算挑一台出来常年插着电，跑 Termux 加 Syncthing 当同步节点，顺便当成随时可用的救急网卡。它的性能可能不如一台四五百块的迷你主机，但它已经在那里了，边际成本是零。在折腾家庭实验室这件事上，先把已有的东西用起来，往往比再买一件新的更有成就感。

## Related Posts

* [把 Android 手机当成 USB 无线网卡：以及那些被低估的安卓妙用](/post/2026/08/android-phone-as-usb-network-adapter-and-more.html) - 08/21/2026
* [小米平板 5 Pro 初体验及设置](/post/2022/01/xiaomi-pad-5-pro-first-impression.html) - 01/18/2022
* [不丢失数据 降级 Android 应用版本](/post/2021/12/downgrade-apk-without-lose-data.html) - 12/23/2021
* [Ubuntu 20.04 使用 MergerFS](/post/2021/10/ubuntu-20-04-mergerfs.html) - 10/...