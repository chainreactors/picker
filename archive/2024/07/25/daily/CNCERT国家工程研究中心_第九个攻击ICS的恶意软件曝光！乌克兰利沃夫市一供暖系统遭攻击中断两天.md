---
title: 第九个攻击ICS的恶意软件曝光！乌克兰利沃夫市一供暖系统遭攻击中断两天
url: https://mp.weixin.qq.com/s?__biz=MzUzNDYxOTA1NA==&mid=2247546023&idx=2&sn=22a8273e086ba477afeeacd3841520a1&chksm=fa938266cde40b70757316e613663fd6bc127fa365191fcd976c420af0078582bccd45635bec&scene=58&subscene=0#rd
source: CNCERT国家工程研究中心
date: 2024-07-25
fetch_date: 2025-10-06T17:44:13.221244
---

# 第九个攻击ICS的恶意软件曝光！乌克兰利沃夫市一供暖系统遭攻击中断两天

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/GoUrACT176nVLdoSAZoGfib9OFhdy7p7jUfAzXbXOcGibmmcnHvUdTwcCOhYqtU269y3zqxcuMWCcLiawicaVNbgfQ/0?wx_fmt=jpeg)

# 第九个攻击ICS的恶意软件曝光！乌克兰利沃夫市一供暖系统遭攻击中断两天

网络安全应急技术国家工程中心

**摘要：**据工业网络安全公司Dragos最新发布的研究报告，称其发现了迄今为止已知的第九个专门针对工业控制系统（ICS）的恶意软件-FrostyGoop。这是一个使用Modbus TCP通讯来对运营技术（OT）产生影响的ICS特定恶意软件。Dragos于2024年4月发现了FrostyGoop。该恶意软件可以直接使用Modbus与ICS进行交互，Modbus是全球所有工业部门和组织中使用的标准ICS协议。该恶意软件与2022年发现的ICS恶意软件PIPEDREAM不同，PIPEDREAM在其组件中使用Modbus通讯进行枚举。

此外，乌克兰安全局（Служба безпеки України）的网络安全态势中心（CSSC）向 Dragos分享了有关乌克兰利沃夫某地区能源公司遭受破坏性网络攻击的详细信息，这次攻击导致客户在两天内失去了供暖服务。Dragos评估认为FrostyGoop被用于此次攻击。一个相关的FrostyGoop配置文件包含了一个ENCO控制设备的IP地址，Dragos基于此中等信心地评估认为FrostyGoop被用于攻击那些对外开放TCP端口502的ENCO控制器。

Dragos并未将此次攻击归咎于任何国家或已知威胁行为者。不过，该公司确实指出，在2024年1月份的攻击中，存在与莫斯科的几个IP地址的连接。鉴于全球范围内广泛使用Modbus设备，这种威胁的广泛适用性凸显了对ICS网络可见性和Modbus流量监控的紧迫需求。检测并标记偏离正常行为的情况，以及识别利用Modbus协议的攻击模式和行为至关重要。这需要从最新的关于漏洞、攻击向量和针对Modbus系统的恶意软件的威胁情报中开发检测方法。

### **关键发现**

* FrostyGoop是第九个专门针对工业控制系统（ICS）的恶意软件。它是第一个使用Modbus通信对运营技术（OT）产生影响的ICS特定恶意软件。此前发现的分别是Trisis (Triton), CrashOverride (Industroyer), BlackEnergy2, Havex, Stuxnet, Industroyer2, PipeDream,和Fuxnet。
* 在2024年4月，Dragos发现了多个FrostyGoop二进制文件。FrostyGoop是用Golang编写的ICS专用恶意软件，通过502端口使用Modbus TCP直接与工业控制系统（ICS）交互。它是为Windows系统编译的，且在发现时，杀毒软件供应商并未检测到它具有恶意性。
* FrostyGoop能够读取和写入ICS设备的保持寄存器，这些寄存器包含输入、输出和配置信息。它接受可选的命令行执行参数，使用单独的配置文件指定目标IP地址和Modbus命令，并将输出记录到控制台和/或JSON文件中。
* 乌克兰安全局（Служба безпеки України）的网络安全形势中心（CSSC）向Dragos分享了关于一次针对乌克兰利沃夫市某市政区能源公司的网络攻击的详细信息。在零下温度期间，这次攻击破坏了供暖服务的电力供应，影响了超过600栋公寓楼。攻击者向ENCO控制器发送Modbus命令，导致测量不准确和系统故障，修复工作花费了将近两天时间。
* 调查显示，攻击者可能通过外部Mikrotik路由器的一个未确定的漏洞进入受害者网络。包括Mikrotik路由器、四个管理服务器和区供暖系统控制器在内的网络资产没有进行充分的分段，便于攻击的实施。
* FrostyGoop通过Modbus TCP与ICS设备通信的能力威胁到多个领域的重要基础设施。鉴于Modbus协议在工业环境中的普遍存在，这种恶意软件通过与传统和现代系统交互，可能在所有工业部门造成破坏。
* 乌克兰利沃夫市的事件强调了充分安全控制的重要性，包括OT原生监控。杀毒软件供应商未能检测到该恶意软件，突显出实施持续OT网络安全监控的重要性，需要具备ICS协议感知分析功能，以告知运营潜在风险。
* Dragos建议组织实施SANS世界级OT网络安全的5项关键控制措施。这些措施包括ICS事件响应、可防御架构、ICS网络可见性和监控、安全远程访问以及基于风险的漏洞管理。

### **FrostyGoop恶意软件解析**

FrostyGoop是第九个专门针对工业控制系统（ICS）的恶意软件，也是第一个利用Modbus通信对运营技术（OT）产生影响的ICS特定恶意软件。2024年4月，Dragos发现了多个FrostyGoop二进制文件。这些文件是用Golang编写的，能够通过502端口使用Modbus TCP直接与ICS交互，并为Windows系统编译。当时，杀毒软件供应商并未将其检测为恶意软件。

**1.读写能力**

FrostyGoop可以读取和写入ICS设备的保持寄存器，这些寄存器包含输入、输出和配置信息。它接受可选的命令行执行参数，使用单独的配置文件指定目标IP地址和Modbus命令，并将输出记录到控制台和/或JSON文件中。通过命令行参数或JSON配置文件，用户可以指定目标设备的IP地址、执行的Modbus命令模式（如读取保持寄存器、写入单个保持寄存器、写入多个保持寄存器）、目标ICS设备上的Modbus寄存器地址、JSON配置文件名称以及日志输出文件名。

**2.配置文件**

FrostyGoop的配置文件以JSON格式包含执行Modbus命令所需的信息。恶意软件读取文件，解析JSON数据，连接到文件中的IP地址，并向配置文件中指定的保持寄存器地址发送Modbus TCP命令。Dragos发现的一个示例配置文件名为“task\_test.json”，其IP地址属于ENCO控制设备。ENCO控制设备通常用于区域供热、热水和通风系统中的过程控制，监测温度、压力和绝缘等传感器参数。

**3.网络通信**

在网络通信方面，FrostyGoop通过Modbus TCP端口502与目标IP地址通信。目标IP地址可以通过恶意软件执行期间使用的参数或配置JSON文件中指定。一旦建立连接，FrostyGoop会向设备发送Modbus命令，并在接收到设备的响应后关闭连接并退出执行。FrostyGoop使用从公开的Github库中获取的Go Modbus库，支持三种Modbus命令：读取保持寄存器（命令码3）、写入单个寄存器（命令码6）和写入多个保持寄存器（命令码16）

**4.日志记录**

FrostyGoop的日志记录功能会将Modbus TCP通信的输出记录到Windows控制台和JSON文件中。执行时打开控制台窗口，如果指定了日志记录参数，则将输出记录到JSON文件中。通信期间，FrostyGoop会记录本地时间和日期、开始通信的目标IP地址、命令发送的保持寄存器、寄存器数量、设备响应的正负号以及响应时间。如果设备的响应包含异常，FrostyGoop会记录一个减号，例如，当保持寄存器不存在时，设备会向恶意软件发送异常。

### **攻击乌克兰利沃夫某供暖系统始末**

2024年1月22日晚至23日，乌克兰安全局（Служба безпеки України）下属的网络安全形势中心（CSSC）与Dragos共享了有关在乌克兰利沃夫市发生的一次针对市政区域能源公司的网络攻击详细信息。此次攻击影响了超过600栋公寓楼的集中供暖，造成居民在零下温度中忍受了将近两天的供暖中断。

调查显示，攻击者可能于2023年4月17日通过利用一个外部Mikrotik路由器上的未确定漏洞进入受害者网络。随后，他们在2023年4月20日和26日部署了一个类似于ReGeorg的带有隧道功能的webshell，并通过Tor IP地址访问。攻击者在2023年11月30日和12月14日获取了安全帐户管理器（SAM）注册表配置单元的内容，从系统中获取了用户凭证。2024年1月22日，攻击者通过L2TP连接到莫斯科的IP地址。

受害网络资产包括一个Mikrotik路由器、四台管理服务器和区域供热系统控制器，未进行充分的网络分段。取证调查显示，攻击者通过硬编码网络路由直接向供热系统控制器发送Modbus命令。受影响的控制器为ENCO控制器，攻击者将其固件从版本51和52降级到不具备监控功能的版本50，导致视图丧失。攻击者并未试图破坏控制器，而是让控制器报告错误的测量数据，导致系统操作错误和供暖丧失。

Dragos评估认为，最近报告的与ICS相关的恶意软件FrostyGoop被用于此次攻击。FrostyGoop使用Modbus协议，可能影响多个设备。相关配置文件“task\_test.json”包含一个属于暴露在互联网的ENCO控制设备的IP地址，Dragos据此中等置信度地评估FrostyGoop在此次攻击前已用于针对一个或多个TCP端口502可通过互联网访问的ENCO控制器。该安全供应商表示，它能够找到目前通过该协议通信的约46,000台互联网工业控制系统设备。

### **措施建议**

利沃夫能源公司因缺乏网络分段，导致攻击者从初始立足点横向移动至供暖系统控制器，并通过降级固件使系统监控失效，导致供暖中断。攻击者利用Modbus协议的弱点，展现了对ICS恶意软件的高度针对性利用。FrostyGoop恶意软件可能已用于攻击其他暴露于互联网的Modbus控制器，突显了ICS环境在网络安全方面的脆弱性。

针对FrostyGoop攻击乌克兰供暖系统的案例，dragos.com建议用户实施五项关键控制措施来提高网络安全性。

1. 工业控制系统（ICS）的事故响应：制定强有力的事故响应计划，特别是针对OT环境，确保快速隔离受影响设备，分析网络流量，恢复正常系统操作。

2. 可防御性架构：实施防御性架构，优先进行网络资产的分段，建立工业隔离区（DMZ），加强访问控制，使用物理或虚拟屏障防止直接访问关键系统。

3. ICS网络可见性与监控：持续监控OT网络流量，如Modbus通信，以检测和响应异常和威胁行为。

4. 安全远程访问：加强远程访问保护，部署多因素认证，确保所有远程连接都被记录和监控，使用VPN加密传输数据。

基于风险的漏洞管理：定期评估以识别和解决漏洞，特别是当存在积极利用的证据时，如果无法打补丁，则采取补偿控制措施如加强监控或限制性访问控制。

### **参考资源：**

1.https://www.darkreading.com/ics-ot-security/novel-ics-malware-sabotaged-water-heating-services-in-ukraine

2.https://www.securityweek.com/frostygoop-ics-malware-left-ukrainian-citys-residents-without-heating/

3.https://hub.dragos.com/hubfs/Reports/Dragos-FrostyGoop-ICS-Malware-Intel-Brief-0724\_.pdf

原文来源：安帝Andisec

“投稿联系方式：010-82992251   sunzhonghao@cert.org.cn”

![](https://mmbiz.qpic.cn/mmbiz_jpg/GoUrACT176n1NvL0JsVSB8lNDX2FCGZjW0HGfDVnFao65ic4fx6Rv4qylYEAbia4AU3V2Zz801UlicBcLeZ6gS6tg/640?wx_fmt=jpeg)

预览时标签不可点

阅读原文

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/GoUrACT176mrRug7icLIhX4EvNQjNgGRibia7K9qOLTR5PDfQiaUesU9xge7pnF8iciaxVC3JVkNqHA2pvQDnrM0hDVQ/0?wx_fmt=png)

网络安全应急技术国家工程中心

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/GoUrACT176mrRug7icLIhX4EvNQjNgGRibia7K9qOLTR5PDfQiaUesU9xge7pnF8iciaxVC3JVkNqHA2pvQDnrM0hDVQ/0?wx_fmt=png)

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