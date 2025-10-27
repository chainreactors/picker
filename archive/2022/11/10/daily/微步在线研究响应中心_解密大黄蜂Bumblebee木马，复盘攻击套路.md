---
title: 解密大黄蜂Bumblebee木马，复盘攻击套路
url: https://mp.weixin.qq.com/s?__biz=Mzg5MTc3ODY4Mw==&mid=2247497032&idx=1&sn=ebd4b8185eb9b3ea4d49d124ff4b25dc&chksm=cfca965cf8bd1f4a09dd8cf6eb59bffee4c9e4e2c3c6d0ef60496fb358d04429ad1b4c4d096b&scene=58&subscene=0#rd
source: 微步在线研究响应中心
date: 2022-11-10
fetch_date: 2025-10-03T22:15:18.368476
---

# 解密大黄蜂Bumblebee木马，复盘攻击套路

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/fFyp1gWjicMKVDTib0yhEmrTSEEkBJ4giaZY8mo5MrrhJ83Rd6wza18wViaKMRqo3HYxh138WYu1icn1tfyQgtIPziag/0?wx_fmt=jpeg)

# 解密大黄蜂Bumblebee木马，复盘攻击套路

原创

两块钱一斤

微步在线研究响应中心

![](https://mmbiz.qpic.cn/mmbiz_jpg/fFyp1gWjicMJasbTOEml0jviatLrkYy1A6NxWSic8LyMWIV3XiaIwhuEfBBeU85PnFkDpcfdWgSGrMXmLlRrTbqJIg/640?wx_fmt=jpeg)

1

**概述**

2022年3月，谷歌威胁分析团队追踪为Conti组织提供初始化访问的团伙时，发现了新的木马家族。该木马与C2服务器通信时会使用特殊代号“bumblebee”作为User-Agent字段，因此将其命名为Bumblebee(大黄蜂)。

在同一时间段内，曾经非常活跃的开门器木马BazarLoader C2活跃节点不断减少，且之前投递BazarLoader木马的多个团伙也开始转向投递Bumblebee木马。二者此消彼长的时间点非常吻合，由此可以认为Bumblebee是取代BazarLoader的下一代开门器木马。

根据监测，近几个月来Bumblebee感染活动非常活跃，几乎每天都会出现新的木马样本和C2服务器。微步情报局对Bumblebee木马的背后团伙、攻击事件及手法、资产通信进行了深入的分析，目前主要的结论如下：

* Bumblebee木马主要通过伪装成收款单，项目文档等内容的钓鱼邮件进行传播。主要攻击美洲和欧洲地区，对各种制造、互联网、金融等行业均有涉及。虽然国内只有与之相关的企业间接受害，但不排除未来不会被纳入到直接攻击的区域中。
* Bumblebee木马一直处在开发和营运的状态。在最近版本的木马中新增加了下载执行插件的功能，说明作者开始将木马功能模块化，并为开发更复杂的木马功能载荷做准备。同时对历史样本梳理后发现，至少有3个团伙长期投递使用该木马。
* Bumblebee木马感染机器后会投递CobaltStrike，Sliver等后渗透木马，并以该主机为落脚点攻击渗透整个域内网络。攻击完成后，黑客团伙会将窃取的登录凭证或访问能力售卖给勒索团伙，投递Conti、Quantum、Diavol等勒索病毒，最终导致敏感文件泄露和主机被勒索。
* 微步情报局通过对该木马通信协议的详细分析并进一步依赖于自有的网络空间测绘系统对全网进行的分析，累计发现了数百台Bumblebee活跃的主控服务器，主要位于美国和欧洲地区，这也与Bumblebee主要攻击的区域相吻合。
* 微步线通过对相关样本、IP 和域名的溯源分析，提取多条相关 IOC ，可用于威胁情报检测。微步在线威胁感知平台 TDP 、本地威胁情报管理平台 TIP 、威胁情报云 API 、互联网安全接入服务 OneDNS 、主机威胁检测与响应平台 OneEDR 等均已支持对团伙的检测。

![](https://mmbiz.qpic.cn/mmbiz_png/fFyp1gWjicMKVDTib0yhEmrTSEEkBJ4giaZvfhbPeLGj9iaficx63S8pBzUj4yqHo97QhKqicxzOJZxj0HpXYrCuab7A/640?wx_fmt=png)

2

**团伙分析**

### **2.1团伙画像**

从涉及Bumblebee木马的历史攻击来看，Bumblebee木马被多个售卖初始访问的黑客团伙所使用，这些团伙的通用画像为：

|  |  |
| --- | --- |
| **团伙画像** | |
| **特点** | **描述** |
| **平台** | Windows |
| **攻击目标** | 互联网、银行、制造、医疗等行业 |
| **攻击地区** | 欧洲地区、美洲地区 |
| **攻击目的** | 作为勒索攻击的开门器，售卖失陷主机给其他黑客，投递勒索病毒 |
| **攻击向量** | 邮件钓鱼 |
| **武器库** | MLNK，Bumblebee木马  CobaltStrike，Sliver，Meterpreter  Procdump，AdFind，CURL，7za.exe，Rclone  Anydesk，ConnectWise，Atera |

### **2.2攻击流程**

![](https://mmbiz.qpic.cn/mmbiz_png/fFyp1gWjicMKVDTib0yhEmrTSEEkBJ4giaZa0Nbb4NLM15ib0UZPDaPQ2L81qCAxw6icXmpMjLvknJPzDmlbhvl8UNQ/640?wx_fmt=png)

### **2.3技术特点**

* 使用比较流行的ZIP-> ISO,VHD -> LNK -> BAT-> DLL序列载荷加载方式；
* 使用WMI调用的方式查询主机敏感信息和创建傀儡进程；
* 选择使用比较冷门的WSS协议（Websocket + TLS/SSL）进行通信，使用JSON而不是二进制字节序列作为网络通信的格式；
* Bumblebee木马会根据主机所在域不同而下发不同的载荷，当主机在一个有效的域内时，下发CS、Sliver等木马继续渗透域内网络。而当主机所在组名为WORKGROUP工作组时下发Vidar等窃密木马。

### **2.4资产特点**

木马涉及的网络资产主要用于两种功能：一是存储木马载荷，用于受害者主动或被动触发下载到本地；二是在木马成功执行后的接收回连请求，下发执行其他载荷。Bumblebee木马通常使用Google Storage、OneDrive、TransferXL等公开的文件存储和共享服务平台存储木马载荷，将下载链接放在钓鱼邮件中，诱导用户下载执行。

![](https://mmbiz.qpic.cn/mmbiz_png/fFyp1gWjicMKVDTib0yhEmrTSEEkBJ4giaZyee6xSNkEB2KMAYZR5JlibL4xg5elWlnSt4TrBKwaX5o87Ciazp2iaZuA/640?wx_fmt=png)

木马的C2回连控制服务地址以IP地址+端口的方式硬编码在样本中，且IP上也未绑定任何域名。当使用浏览器直接访问时，会显示网站证书为非法的自签名证书，而不校验证书访问时会返回”404 page not found”页面。

![](https://mmbiz.qpic.cn/mmbiz_png/fFyp1gWjicMKVDTib0yhEmrTSEEkBJ4giaZwwep50dcw5uFHlVYlpmLqA4kQIXibbHyHadY3m93tianJZ2Pia31fvfjw/640?wx_fmt=png)

3

**样本分析**

### **3.1基本信息**

伪装成发票或文档的钓鱼邮件会指示受害者点击链接下载对应的文件。链接通常指向Google Storage，OneDrive，TransferXL等公开的文件存储和共享服务平台，访问即可下载到包含ISO镜像或VHD虚拟磁盘的ZIP压缩包。

![](https://mmbiz.qpic.cn/mmbiz_png/fFyp1gWjicMKVDTib0yhEmrTSEEkBJ4giaZyee6xSNkEB2KMAYZR5JlibL4xg5elWlnSt4TrBKwaX5o87Ciazp2iaZuA/640?wx_fmt=png)

当用户解压并在浏览器中点击挂载后，就只能看到伪装成文件夹图标的快捷方式(LNK文件)。双击快捷方式就会启动执行隐藏的BAT脚本

![](https://mmbiz.qpic.cn/mmbiz_png/fFyp1gWjicMKVDTib0yhEmrTSEEkBJ4giaZ6OvicxchHia8O2PHmeIHRKAhfE1vXNCVg5WoAJDOzkk9Y9GIa0SCKmeg/640?wx_fmt=png)

BAT脚本使用单字符变量替换进行混淆，执行后会将Bumblebee木马载荷拷贝到Temp目录下，并调用Rundll32或RegSvr32程序加载执行。

![](https://mmbiz.qpic.cn/mmbiz_png/fFyp1gWjicMKVDTib0yhEmrTSEEkBJ4giaZ6Zqspvym6KJFnSDvVTibgtoql2zTuGQZU3dJQiamRkKaMSBGQBeTO24w/640?wx_fmt=png)

### **3.2详细分析**

Bumblebee木马载荷加载执行后，外层加载器负责解密执行真正的Bumblebee载荷。加载器加载的方式比较特别，通过hook NtOpenFile, NtCreateSection, NtMapViewOfSection 3个关键函数劫持LoadLibraryA函数的执行逻辑，然后调用LoadLibraryA函数加载gdiplus.dll模块，从而映射加载内嵌的PE文件。

![](https://mmbiz.qpic.cn/mmbiz_png/fFyp1gWjicMKVDTib0yhEmrTSEEkBJ4giaZkicIPmfAeTddYENVD73Hk0KGLWldULLLiaxhvBGFgrGSrPVoW6shL1fg/640?wx_fmt=png)

加载完成后，木马在动态库入口创建新的线程执行木马逻辑，并且在创建时使用THREAD\_CREATE\_FLAGS\_HIDE\_FROM\_DEBUGGER 标志位向调试器隐藏该线程，达到反调试的目的。

![](https://mmbiz.qpic.cn/mmbiz_png/fFyp1gWjicMKVDTib0yhEmrTSEEkBJ4giaZHbsFV6d6Xp7jOiaMTAJqEicibSZW74YHgMugXV7DkoVfGXR5FkbAVvtoA/640?wx_fmt=png)

木马启动执行后会判断执行环境是否为真实环境。木马作者使用以下开源项目al-khaser中的部分代码，通过用户名，硬件信息，进程列表，特殊文件等多种方式检测虚拟机、沙箱和分析环境。
开源项目：

al-khaser（https://github.com/LordNoteworthy/al-khaser）

![](https://mmbiz.qpic.cn/mmbiz_png/fFyp1gWjicMKVDTib0yhEmrTSEEkBJ4giaZHpytRx6CMIeyyZhMOWlzUwZPyxQN5wbHlhPCI7cN50EicbEekJWxF3Q/640?wx_fmt=png)

![](https://mmbiz.qpic.cn/mmbiz_png/fFyp1gWjicMKVDTib0yhEmrTSEEkBJ4giaZtz0I525fTGIZ1ZG3Qln18fSGp8WGu5ia7qHeBWMOmCSrDwyklhlcQ1A/640?wx_fmt=png)

并且木马会创建一个单独的线程，约每半分钟一次实时监控进程列表中是否存在分析工具的进程，一旦检测到，则结束自身逻辑的执行。

![](https://mmbiz.qpic.cn/mmbiz_png/fFyp1gWjicMKVDTib0yhEmrTSEEkBJ4giaZu2n6oLuxCBpVoeicBSILJMFdXJwMfBAjd0ZnRznE4sxm5n59Qe9EG9Q/640?wx_fmt=png)

![](https://mmbiz.qpic.cn/mmbiz_png/fFyp1gWjicMKVDTib0yhEmrTSEEkBJ4giaZoVlsdSJKy14Aaianu1tIjUHRyT7MGicsiaga8zlp8n0d4rHDK6YPpibvHw/640?wx_fmt=png)

通过检测后，木马解密C2地址和收集主机信息进行上线。木马内嵌RC4密钥，用于解密URI字符串，C2地址列表和加解密与服务器通信的流量内容。

![](https://mmbiz.qpic.cn/mmbiz_png/fFyp1gWjicMKVDTib0yhEmrTSEEkBJ4giaZZDBIjO9jQUTQOspFC61YDGhHqibaZv6UVs2Of32euPh2HX0S4RK9HVQ/640?wx_fmt=png)

木马连接的C2地址硬编码在样本中，在连接前会使用密钥解密，从而得到一段使用逗号分割的C2地址列表。

![](https://mmbiz.qpic.cn/mmbiz_png/fFyp1gWjicMKVDTib0yhEmrTSEEkBJ4giaZicgGK3PqxjiajkbSWWBsI7NmP6qoNbrOv8e23EeS4DLBA6YjicaIRx40A/640?wx_fmt=png)

在这个列表中会包含一些非443端口的C2地址，猜测可能是作者故意为之，用于对抗配置解析或自动化提取IOC的功能。

![](https://mmbiz.qpic.cn/mmbiz_png/fFyp1gWjicMKVDTib0yhEmrTSEEkBJ4giaZPibiaZdbCMic4FhkE84KeMWs7TvBsEAJYa22Sol1FFyu40Qbnxgb8a8vg/640?wx_fmt=png)

当环境检测通过后，木马会使用WSS(Websocket + TLS/SSL)协议与C2服务器进行通信完成上线和请求任务执行，请求和响应的数据均为JSON格式，并且使用RC4算法进行加密。

![](https://mmbiz.qpic.cn/mmbiz_png/fFyp1gWjicMKVDTib0yhEmrTSEEkBJ4giaZW8eribiczRBfvDKj0Z5FBdWTGyDYruOrXqG1552VnmzwQia92Zx1dO27g/640?wx_fmt=png)

木马使用用户名和系统UUID拼接的字符串，计算MD5作为用于标识主机的client\_id， 然后拼接上线请求client\_ping字段值为”FORTHEEMPEROR”，从而形成上线包。

![](https://mmbiz.qpic.cn/mmbiz_png/fFyp1gWjicMKVDTib0yhEmrTSEEkBJ4giaZwvmQr2avH4GsbJgH2kvr3QBQLeDJZSLhSqXa7KA58nBZ8GDlRa2K2A/640?wx_fmt=png)

发送上线包后会收到服务器端的响应内容，其中session字段用于请求任务的会话Token，完成上线。

![](https://mmbiz.qpic.cn/mmbiz_png/fFyp1gWjicMKVDTib0yhEmrTSEEkBJ4giaZq83anwSLrQ2mN32LNFnXwrGKSpX6HOr9A31Va1Vib3EywOyMRZiaozdQ/640?wx_fmt=png)

使用上线获得的session，并将系统自身的版本信息，用户名，所属于的域以及木马本身所属的组和版本信息发送至服务器，请求任务执行。

![](https://mmbiz.qpic.cn/mmbiz_png/fFyp1gWjicMKVDTib0yhEmrTSEEkBJ4giaZHibpg8Cibbzg8Q1NM85qq0W9FHVvzBP6Uq2L5v6WhOWPxKscFK1SIwwg/640?wx_fmt=png)

任务响应会包含一个任务状态字段和任务内容字段，任务内容可以包括多个任务，每个任务有task\_id标识，并且有对应的命令和对应的数据内容。木马根据响应任务，解析命令和对应的数据，完成对应的任务。

![](https://mmbiz.qpic.cn/mmbiz_png/fFyp1gWjicMKVDTib0yhEmrTSEEkBJ4giaZVNJRp51Sr48eSrscKSHAMx8NnLUJJT1vdOufazVkhFWDxJC88V84xA/640?wx_fmt=png)

从样本中注册命令回调函数部分的代码，可以得到木马目前支持的所有控制命令，包括完成下载运行其他载荷，执行命令，创建计划任务驻留等功能。

![](https://mmbiz.qpic.cn/mmbiz_png/fFyp1gWjicMKVDTib0yhEmrTSEEkBJ4giaZpVLdCgCNibahBxDibxK4SXZlqcKNtq1PyPLicGfV7PWHVE7B7lV3Stf3Q/640?wx_fmt=png)

具体命令名和功能如下：

|  |  |
| --- | --- |
| **命令** | **功能** |
| shi | 将任务中的载荷以shellcode形式注入执行 |
| dij | 将任务中的载荷以动态库形式注入到新创建的ImagingDevices.exe, wab.exe, or wabmig.exe进程中执行 |
| dex | 将任务中的载荷保存到文件wab.exe，并调用WMI创建新进程执行 |
| sdl | 卸载自身 |
| ins | 将Bumblebee木马文件转移到APPDATA目录下，创建计划任务进行驻留 |
| gdt | 执行shell命令 |
| plg | 执行插件，现阶段功能与dij命令相同 |

##

##

##

4

**关联分析**

### **4.1版本信息**

Bumblebee木马自出现以来，一直处于维护开发状态。通过比对不同版本的样本发现：从三月份开始出现到现在半年多的时间里，木马进行了多次更新升级，不断完善控制功能和对抗安全产品的检测。其中包括：

* 由仅支持单个的C2地址升级为支持C2地址列表
* 使用RC4算法加密C2地址列表和受控端与控制端之间的通信流量
* 添加反虚拟机，反沙箱，反分析工具等对抗手段
* 通信协议由HTTPS协议升级为WSS(Websocket + TLS/SSL)
* 添加执行命令的功能

并且在最近更新的版本中，木马的控制命令新增了名为“plg”（plugin）的控制命令，并且代码中包含了RPC服务基础代码，推测是为了将木马进行模块化的拆分和实现更为复杂和完善的木马插件功能。

![](https://mmbiz.qpic.cn/mmbiz_png/fFyp1gWjicMKVDTib0yhEmrTSEEkBJ4giaZu8H9OxYAZ2RJ1sgSY9OSEjibABlllafj4ed9dNvbiblh1AHlekwqNTicg/640?wx_fmt=png)

![](https://mmbiz.qpic.cn/mmbiz_png/fFyp1gWjicMKVDTib0yhEmrTSEEkBJ4giaZ4iaLy4MJ1VbC30qjNGmiam18US4zciao8DAWvrz7TqHy6zBpfyt3Hqngg/640...