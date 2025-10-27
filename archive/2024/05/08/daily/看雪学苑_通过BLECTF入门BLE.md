---
title: 通过BLECTF入门BLE
url: https://mp.weixin.qq.com/s?__biz=MjM5NTc2MDYxMw==&mid=2458553587&idx=1&sn=555f3300fdfb937c866049ec95101e07&chksm=b18dbc7986fa356f385dbffe62de254e6d722f876becce0a78ebe8c2b742e83a71fd87bea561&scene=58&subscene=0#rd
source: 看雪学苑
date: 2024-05-08
fetch_date: 2025-10-06T17:16:51.793071
---

# 通过BLECTF入门BLE

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1UG7KPNHN8HsSUOEIQib0rTsR2FPmXo958pRIUuCJLe7aUVQjGJw3gQSanicEpBm0JelYSUiaO1vfR8YGJk61UnNw/0?wx_fmt=jpeg)

# 通过BLECTF入门BLE

Arahat0

看雪学苑

iot小白最近入门BLE，看到**yichen115**师傅关于BLECTF的文章，感觉挺不错的，同时去年该项目有了更新，就自己试着做了做。并且针对**yichen115**师傅文章没写的地方进行补充。

```
一

环境搭建
```

首先你得有一块`esp32`的板子跟一个支持linux平台的蓝牙适配器或者USB加密狗。

安装`esptool`工具，这是一个基于 Python、开源、独立于平台的实用程序，用于与 Espressif 芯片中的 ROM 引导加载程序进行通信。我们得用它来烧录。

```
sudo apt-get install esptool
```

构建`ble_ctf`项目，`/dev/ttyUSB0`是我们的串口名称。

```
git clone https://github.com/hackgnar/ble_ctf
cd ble_ctf
esptool -p /dev/ttyUSB0 -b 460800 --before default_reset --after hard_reset --chip esp32  write_flash --flash_mode dio --flash_size 2MB --flash_freq 40m 0x1000 build/bootloader/bootloader.bin 0x8000 build/partition_table/partition-table.bin 0x10000 build/ble_ctf.bin
```

##

```
二

相关知识
```

###

### hcitool

在打开蓝牙设备后，就可以使用`hcitool`工具来对`BLE`设备进行控制。

这个项目就需要使用`hcitool`搜索`BLE`设备来找到我们蓝牙设备的`MAC`地址。

```
sudo hcitool lescan
```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8HjiaWfocorkFzbboT7icxlVTkoicn1awBLmWFs4eXgiaUgj9ZG5GgQ9ojLKKfMZvicGqGwic0Xkic785tQQ/640?wx_fmt=png&from=appmsg)

###

### GATT

**通用属性配置文件（GATT）**详细描述了`BLE`设备建立连接后如何传输属性（数据），其中有三个相当重要的概念：**`Profile(配置文件)、Service(服务)、Characteristics(特征)`**，它们可以抽象成以下包含关系：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8HjiaWfocorkFzbboT7icxlVTGLL45A9K3YZiaSx9gRHGBls5LIhJ362TTSjicjKC41dCvqRibS9TSyqqA/640?wx_fmt=png&from=appmsg)

首先`GATT`主要是负责在两个已经连接的设备交互数据，定义了`BLE`网络堆栈的一般拓扑的`GAP`层把`BLE`设备区分为主机`Master(Central)`和从机`Slave(Perpherial)`。一般我们将`从机`具有的数据或者属性特征，称之为`Profile`（配置文件）。

一个或多个`Characteristic`组成一个`Service`，一个或多个`Service`组成`Profile。`

主机可以发现和获取从机的`Service`和`Characteristic`，然后与之通信。`Service`可以理解为一个功能集合，`Characteristic`是主从通信的最小单元，是一个抽象功能单元。

◆主机可主动向从机`Write`写入或`Read`读取数据。

◆从机可主动向主机`Notify`通知数据。

而在`GATT`层则区分为`Server`和`Client。`

◆客户端（Client）：客户端可以发送请求给GATT服务端，读取和写入存储在服务端的特征值`(Characteristics )。`

◆服务端（Server）：该设备包含由`GATT`客户端读取或写入的`Characteristic`，每当客户端发送请求时，服务端就会接受并执行相应的请求。

`Characteristic`一般包含以下特征：

◆UUID（Universally Unique Identifier）：用于唯一标识Characteristic。

◆Properties（属性）：指定了Characteristic的行为，例如读取、写入、通知等。

◆Value（值）：存储Characteristic的当前值。

◆Descriptors（描述符）：提供了关于Characteristic的更多信息，如读写权限、单位、格式等。

比如我现在的服务端是我的烧录了`BLECTF`的`esp32`，它由很多`Characteristic`组成。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8HjiaWfocorkFzbboT7icxlVTdObzsv2M2HKXxZMPHVe1xibHNmQwJGSO52wxpFWj0pKzG2SrugYohWQ/640?wx_fmt=png&from=appmsg)

拿着为0x45的`handle`举例，它就相当于某个`Characteristic`的编号

去读取这个0x45的`handle`的`Value/Descriptor`，可以得到以下信息。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8HjiaWfocorkFzbboT7icxlVTuAabvooqpPRtkVic0EZeK0Rd7bic8JohuZFLsfIaNFQ1y0FcX5EqYpJQ/640?wx_fmt=png&from=appmsg)

`1a`就是特征属性，代表权限。

`46`是这个特征的特征值的句柄 ，我们可以通过其去查看这个特征的描述。

`00 0f ff`是`UUID`的缩略。

通过0x46的`handle`去读取`Value/Descriptor`，得到的就是这个特征的描述。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8HjiaWfocorkFzbboT7icxlVTwEg7OicWK2Wfu6tsQ43HbCwJuc57UyDOVfhnQrwDlEoiacySIJjwwagw/640?wx_fmt=png&from=appmsg)

通过uuid去读取也是一样的结果。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8HjiaWfocorkFzbboT7icxlVT7SbaM27MWPGhnhPSmOX9FfnPDSwo0LUrMibvA9PWVk7TsiaNIvOA3Z9w/640?wx_fmt=png&from=appmsg)

在BLE中，我们有时候会看到`Attributes（属性）`，这是一个更一般的术语，用于表示`特征`中的各种信息。它可以包含`Characteristic`的UUID、Properties、Value、Descriptors等。Attributes用于描述和定义`特征`的各个方面，以便设备之间能够理解和交换数据。

### gatttool

`hcitool`对于`BLE`设备只能进行连接上的管理，如果需要更精细化的管理，就需要使用`gatttool。`

```
GATT commands
  --primary                                 用于进行主服务发现，查找蓝牙设备上的主服务
  --characteristics                         用于进行特征发现，查找指定主服务下的特征
  --char-read                               用于写入特征的值，需要指定一个句柄
  --char-write                              用于写入特征的值，不需要响应
  --char-write-req                          用于写入特征的值，需要响应
  --char-desc                               于进行特征描述符发现，查找指定特征下的描述符
  --listen                                  监听特征的通知和指示

Primary Services/Characteristics arguments
  -s, --start=0x0001                        用于指定起始句柄(可选)
  -e, --end=0xffff                          用于指定结束句柄(可选)
  -u, --uuid=0x1801                         用于指定16bit或者128bit的UUID(可选)

Characteristics Value/Descriptor Read/Write arguments
  -a, --handle=0x0001                       用于指定要读取或写入的特征或描述符的句柄
  -n, --value=0x0001                        用于指定要写入的特征值

Application Options:
  -i, --adapter=hciX                        用于指定本地适配器接口，如hci0
  -b, --device=MAC                          用于指定远程蓝牙设备的MAC地址
  -t, --addr-type=[public | random]         用于设置LE地址类型，可以选择公共地址还是随机地址，默认公共地址
  -m, --mtu=MTU                             用于指定ATT协议MTU大小
  -p, --psm=PSM                             用于指定GATT/ATT over BR/EDR的PSM
  -l, --sec-level=[low | medium | high]     用于设置安全级别，可以选择低、中、高，默认低安全级别
  -I, --interactive                         用于启用交互模式
```

交互模式下的命令。

```
help                                           显示帮助信息
exit                                           退出交互模式
quit                                           退出交互模式
connect         [address [address type]]       连接到远程设备
disconnect                                     断开与远程设备的连接
primary         [UUID]                         发现主要服务
included        [start hnd [end hnd]]          查找包含的服务
characteristics [start hnd [end hnd [UUID]]]   发现特征
char-desc       [start hnd] [end hnd]          发现特征描述符
char-read-hnd   <handle>                       通过句柄读取特征值/描述符
char-read-uuid  <UUID> [start hnd] [end hnd]   通过UUID读取特征值/描述符
char-write-req  <handle> <new value>           写入特征值（写请求）
char-write-cmd  <handle> <new value>           写入特征值（无响应）
sec-level       [low | medium | high]          设置安全级别，默认为低安全级别
mtu             <value>                        设置交换GATT/ATT的MTU（最大传输单元）
```

我们这里可以查看一下设备上所有的特征（Characteristic）。

```
gatttool -b 08:B6:1F:B9:59:72 --characteristics
```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8HjiaWfocorkFzbboT7icxlVTLN6vKp0yLwNuHDmxNKqjZlKLVXnfFHQLeLMdKOWgiaHkS7nRMyEyMmg/640?wx_fmt=png&from=appmsg)

`handle`是特征的句柄，`char properties`是特征的属性，`char value handle`是特征值的句柄，`uuid`是特征的通用唯一标识符。

```
三

关卡
```

◆使用`gatttool`查看分数

```
gatttool -b 08:B6:1F:B9:59:72 --char-read -a 0x002a|awk -F':' '{print $2}'|tr -d ' '|xxd -r -p;printf '\n'
```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8HjiaWfocorkFzbboT7icxlVTcA9EqWJAPtFczOn5Q9N8Zic87ypgianZh2elYpudV44ISW1mukgCOsAg/640?wx_fmt=png&from=appmsg)

◆使用`gatttool`提交flag获得分数

```
gatttool -b 08:B6:1F:B9:59:72 --char-write-req -a 0x002c -n $(echo -n "some flag value"|xxd -ps)
```

###

### Flag1

> Flag one is a gift! You can only obtain it by reading this document or peaking at the source code. In short, this flag is to get you familiar with doing a simple write to a BLE handle. Do the following to get your first flag. Make sure you replace the MAC address in the examples below with your devices mac address!

这关主要是让我们熟悉对`BLE`句柄的特征进行简单的写入。

首先，查看分数，初始分数为0/20。

```
gatttool -b 08:B6:1F:B9:59:72 --char-read -a 0x002a|awk -F':' '{print $2}'|tr -d ' '|xxd -r -p;printf '\n'
```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8HjiaWfocorkFzbboT7icxlVTcA9EqWJAPtFczOn5Q9N8Zic87ypgianZh2elYpudV44ISW1mukgCOsAg/640?wx_fmt=png&from=appmsg)

然后，提交向`0x2c`句柄提交flag。

```
gatttool -b 08:B6:1F:B9:59:72 --char-write-req -a 0x002c -n $(echo -n "12345678901234567890"|xxd -ps)
```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8HjiaWfocorkFzbboT7icxlVTVWootEtrX8Lozbo1heJ0ezIjMP3pV7v9XKcCpbVNjJCF82QyIKOWxg/640?wx_fmt=png&from=appmsg)

最后，检查我们的分数来查看flag是否被接受，发现分数变成了1/20。

```
gatttool -b 08:B6:1F:B9:59:72 --char-read -a 0x002a|awk -F':' '{print $2}'|tr -d ' '|xxd -r -p;printf '\n'
```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8HjiaWfocorkFzbboT7icxlVTUoS1ziciaSozFhpln3ianf1sJjsDUibjkdnMtgfR9ccTNLHiaAyibKvZ8xcA/640?wx_fmt=png&from=appmsg)

###

### Flag 0x002e

> Check out the ascii value of handle 0x002e and submit it to the flag submision handle 0x002c. If you are using gatttool, make sure you convert it to hex with xxd. If you are using bleah, you can send it as a string value.

读取0x002e句柄的特征，只需要`--char-read`加`-a`指定`0x002e。`

```
gattto...