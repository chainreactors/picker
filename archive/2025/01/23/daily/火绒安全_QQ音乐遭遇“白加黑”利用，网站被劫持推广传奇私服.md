---
title: QQ音乐遭遇“白加黑”利用，网站被劫持推广传奇私服
url: https://mp.weixin.qq.com/s?__biz=MzI3NjYzMDM1Mg==&mid=2247521743&idx=1&sn=7d0d609cffb045d031bdba1a74baee80&chksm=eb704bf0dc07c2e6f4ce1baf70c50eae31af800684d54c7bb88be8c67e11cdd0d9cef32321a1&scene=58&subscene=0#rd
source: 火绒安全
date: 2025-01-23
fetch_date: 2025-10-06T20:11:37.564119
---

# QQ音乐遭遇“白加黑”利用，网站被劫持推广传奇私服

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/0icdicRft8tz55bHvlaCfHAGxaoycszib0E339G3zvjDExmK0iaPcVICUC2gTDh7Vicj5myAnjV2ibhVzico6HGGaYm7g/0?wx_fmt=jpeg)

# QQ音乐遭遇“白加黑”利用，网站被劫持推广传奇私服

原创

火绒安全

火绒安全

# ![](https://mmbiz.qpic.cn/sz_mmbiz_gif/0icdicRft8tz4nrnOI1emtFr0UYnrLKytAvy2gia6ZuIUJs14h2pEIwpiaWPCTTuCQIDibx9dlfXoyrNyVEWb8DVUUA/640?wx_fmt=gif&from=appmsg)

网络劫持攻击一直是网络安全领域的常见威胁，攻击者通过篡改网络请求或植入恶意代码，将用户劫持至非法页面，从而实现恶意目的。这种攻击手段不仅干扰用户的正常网络体验，还可能带来隐私泄露和设备安全风险。

近期，火绒威胁情报中心监测到 QQ 音乐目录下存在异常进程自启现象。经溯源分析，确认该进程文件为 2021 年版本的 QQMusic.exe文件。攻击者利用“白加黑”技术加载恶意 DLL 文件，解压出劫持网页模块，随后安装用于劫持网页的恶意驱动，最终达成将指定网址劫持至私服发布页面的攻击目的。此外，该恶意驱动还可检测 ARK 工具驱动，并对其进行断链以隐藏自身驱动，同时对安全软件的通信进行干扰。目前，火绒安全产品可对上述病毒进行拦截查杀，建议广大用户及时更新病毒库以提高防御能力。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/0icdicRft8tz55bHvlaCfHAGxaoycszib0EyyhQ0M80BHYb6ofj82J1OQncYAWcm6ibSV9iaH15PB22KCvbrLYsQTFg/640?wx_fmt=png&from=appmsg)

查杀图

劫持前网站页面为：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/0icdicRft8tz55bHvlaCfHAGxaoycszib0Ee4ZKeL2kHDpZibVqLkJ2l1GYlDY2fPMiaGwECDlmc8OickzFpaSH4m3OQ/640?wx_fmt=png&from=appmsg)

原网站

劫持后网站页面为：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/0icdicRft8tz55bHvlaCfHAGxaoycszib0EPuIHe7EevHd4oJ2KsIe7lGmAnYOQYp2ULEfCuNG2B8OeX9OZibwuiarQ/640?wx_fmt=png&from=appmsg)

劫持后网站

**一**

**溯源分析**

在进行溯源时，我们发现早在 2021 年就存在一种利用 ManicTimeVico.exe （实际为 QQMusic.exe 文件）实施白加黑手段的病毒。然而，此次发现与 2021 年的情况有所不同，其源头大部分来自于传奇私服，还有一小部分为游戏修改器和模拟器等。相关的恶意文件名有《完美公益[1.01].exe》、《2k25西瓜修改器.exe》、《krkr-incomplete-load.exe》（吉里吉里模拟器）等。

在调查过程中我们还注意到，这些传奇私服大部分是通过蓝奏云下载的。而蓝奏云下载链接疑似被劫持，导致实际下载链接被篡改为阿里云 oss 链接，最终致使用户下载到携带病毒的文件。

以下是下载该病毒时用到的链接：（其中包含各种各样的传奇私服文件。）

* lanzouxx.oss-cn-hangzhou.aliyuncs.com
* fs1832075456.oss-accelerate.aliyuncs.com
* lanzoc.oss-cn-hangzhou.aliyuncs.com
* fs839268.oss-cn-shenzhen.aliyuncs.com
* lanzoa.oss-cn-hangzhou.aliyuncs.com
* lanzog.oss-cn-hangzhou.aliyuncs.com
* lanzod.oss-cn-hangzhou.aliyuncs.com
* lanzoi.oss-cn-hangzhou.aliyuncs.com
* lanzok.oss-cn-hangzhou.aliyuncs.com
* lanzof.oss-cn-hangzhou.aliyuncs.com
* lanzob.oss-cn-hangzhou.aliyuncs.com
* lanzoj.oss-cn-hangzhou.aliyuncs.com

以下是 2022 年 11 月 21 日某贴主发布的蓝奏云下载地址被劫持的警示帖子截图：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/0icdicRft8tz55bHvlaCfHAGxaoycszib0EiaemgWoJVRCibmGY0j60hLKLY6iaF9ETzFEHibEl9lAzBto8vwpSNXQMicw/640?wx_fmt=png&from=appmsg)

蓝奏云链接劫持帖子截图

**二**

**样本分析**

基于上述溯源发现，下面将以“完美公益 [1.01].exe”为例进行分析。（其他样本与该样本类似，仅仅是其中释放的原文件不一样。）

该样本的执行逻辑可以分为以下三个阶段：

* 初始阶段：样本首先释放并运行原始文件，即传奇私服程序，随后下载配置文件并检查指定文件和注册表决定进入哪条分支。
* 下载劫持模块：第一分支和第二分支负责下载劫持模块。尽管第三分支由于无法成功下载文件，所以我们无法确切判断它是否也会执行下载劫持模块的操作，但在分类上我们依然将其归到这一阶段当中。
* 劫持模块：劫持模块中实现劫持操作，将指定网页劫持至传奇私服发布页。

该样本执行流程图如下：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/0icdicRft8tz55bHvlaCfHAGxaoycszib0EmPXbgbeXZvibTs7083PBHwqpMx0Ioo1DyN7D4xfEofMVL8O6cFlSbuw/640?wx_fmt=png&from=appmsg)

流程图

**初始阶段**

**执行原程序：**样本首先进行的操作是提取自身资源中的 bitmap - 0x80 - 0x409，接着将其取反，以此作为文件名，随后在 C 盘下创建一个名为“完美公益 [1.01]”的目录。完成这一步后，样本会再次提取资源 bitmap - 0x74 - 0x409，并取反后作为文件数据，最终生成一个名为“完美公益 [1.01].exe”的可执行文件并执行它。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/0icdicRft8tz55bHvlaCfHAGxaoycszib0ENtbdlaxAq0eF0qW53ocMeL3vPExW3J92GUpVQH4XVGr7xyzV7XibTYg/640?wx_fmt=png&from=appmsg)

执行原文件

![](https://mmbiz.qpic.cn/sz_mmbiz_png/0icdicRft8tz55bHvlaCfHAGxaoycszib0EwpPicjVuYH5OFK19IKTKY2SjMSVU6ia1tVWicSmIzw5yIeZcHaxJ6iawtA/640?wx_fmt=png&from=appmsg)

资源中的原程序

**下载配置文件：**通过链接 http://d\_1.largesder.com:8888 下载 ii.html文件，之后利用井字符号分割其内容，并分别赋值。所赋的值后续会用于检查特定文件是否存在、确定需要等待的秒数，以及判断是否进入**第三分支**等情况。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/0icdicRft8tz55bHvlaCfHAGxaoycszib0E6oczGEQUkYHOKujJJUXzSeSbISOedQsM5ZQEpFfINGIbGDS9qQljEA/640?wx_fmt=png&from=appmsg)

下载 ii.html 并分割赋值

**随后分别检查以下内容是否存在：**

文件夹：其检查结果会对是否进入**第二分支**产生影响。

* C:/Program Files (x86)/DB Commander 2000 PRO/
* C:/Program Files/DB Commander 2000 PRO/

注册表：尚未分析出是否会有影响。

* SOFTWARE\Microsoft\Terminal Server Client\Default\MRU0
* SOFTWARE\Microsoft\Terminal Server Client\Default\MRU1
* HKEY\_LOCAL\_MACHINE\SYSTEM\CurrentControlSet\Services\VMnetDHCP

创建 C:\ProgramData\ttt7.ini 和 C:\ProgramData\t7.ini。

**设置以下注册表值为 0，以禁用用户账户控制（UAC）：**

* SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Policies\\System\\ConsentPromptBehaviorAdmin
* SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Policies\\System\\EnableLUA
* SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Policies\\System\\PromptOnSecureDesktop

![](https://mmbiz.qpic.cn/sz_mmbiz_png/0icdicRft8tz55bHvlaCfHAGxaoycszib0E2d8ia2QBsbZ9NVLQ6GThv8jOc0gmcNRRWHCn8HnEx8CmNt6qSvfqibew/640?wx_fmt=png&from=appmsg)

禁用 UAC

**检查安全软件进程：**对 kxetray.exe、360Safe.exe、360Tray.exe 等进程进行检查。其中，是否存在 360 相关进程会对是否进入**第一分支**产生影响。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/0icdicRft8tz55bHvlaCfHAGxaoycszib0EMalceOnBp7iaXM45dkZkTMN0y06jicCHBLISymBvsQjfYymqgTUf3iakg/640?wx_fmt=png&from=appmsg)

检查安全软件

**下载劫持模块阶段**

**第一分支**

**第一分支进入条件：**检测是否存在 360 进程，如果存在则会进入第一分支。此过程中有断网操作，推测其目的是对抗 360 云端上传检测。

**下载文件：**进入分支后，下载云端配置、解压器及QQ 音乐白加黑模块加载器三个文件。

**解压执行：**下载文件后判断 FFDPS.tmp 中数据是否为 123，如果是 123 则利用解压器 rr.exe 和密码 FASJKLVFDAJKLCDSA434JKLFDS 解压 startups.jpg 至 C:\Users\Administrator\AppData\Local\Temp 目录中，随后执行 playtomenu.exe。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/0icdicRft8tz55bHvlaCfHAGxaoycszib0EgCExnWlynzkJXULG9ZYceFJ7w7I5SfA9FSphF2LNC1htsNP3jo2Qww/640?wx_fmt=png&from=appmsg)

下载链接对应表

***playtomenu.exe***

**程序功能：**具备反沙箱等功能以防止恶意行为被分析，通过断网解压执行的方式来逃避云端上传检测，并且能够实现持久化操作。

**文件膨胀：**playtomenu.exe 文件经过膨胀，文件大小接近 100MB。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/0icdicRft8tz55bHvlaCfHAGxaoycszib0EhrtBXgSnboiagDWiaV6jPhDrCe2tVWTvAOG0LOIIJ5T6Yccic39QjUicjw/640?wx_fmt=png&from=appmsg)

充满 0x08 数据

**反沙箱等防止恶意行为分析：**检测磁盘大小、查看当前进程文件的路径及最后修改时间、检查是否为管理员等。

**检测磁盘大小：**判断 C 盘剩余大小是否小于 10GB。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/0icdicRft8tz55bHvlaCfHAGxaoycszib0Eqrhg7naufWVDuDv0rlN67DkAfzVQrkHnSJLlrAibezY75NvpmxocVJg/640?wx_fmt=png&from=appmsg)

检查 C 盘大小

**检测文件信息和路径：**获取 playtomenu.exe 文件的最后修改时间及文件路径，并对这些信息进行验证，查看其是否与特定的时间  2020/02/03 11:41:30 和路径 C:\Users\Administrator\Desktop\playtomenu.exe 完全一致，当两个条件均满足时，程序才会继续执行后续操作。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/0icdicRft8tz55bHvlaCfHAGxaoycszib0EyWnGXOcLyYZmanIXchQCj18uw8XqXgQLGZymt9Rdqqiaib4hxB4x7pkQ/640?wx_fmt=png&from=appmsg)

检查修改时间和路径

**管理员检测：**利用 IsUserAnAdmin 函数检查用户是否为管理员，如果不是管理员则会打开五子棋程序，目前尚未明确作者意图。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/0icdicRft8tz55bHvlaCfHAGxaoycszib0EdrXz7TGtJ3GIX5IFaN0bM0sicLVyvTDDZUo0icjsn6tsezUX347VKbGw/640?wx_fmt=png&from=appmsg)

五子棋截图

**下载文件：**该样本后续会下载以下内容。需要注意的是，对于 FFDPS\_1.tmp 这一文件，只有其中的数据为 123 时才会继续运行，否则将直接终止进程。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/0icdicRft8tz55bHvlaCfHAGxaoycszib0EpgP13MGuCz7LXCiavGia1rTWHNZicyg0cDV6gsYiaPZg3PnX7oM4qStVUQ/640?wx_fmt=png&from=appmsg)

下载链接与文件路径对应表

**判断系统版本：**获取 Windows 系统的版本信息，以此选择符合版本的 ipconfig.exe 来实现断网操作。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/0icdicRft8tz55bHvlaCfHAGxaoycszib0EV92iaCBibbYOJHlNPvajWaXmeicnbSU2UMVT3yYWAaN36x3vLzpowgjCA/640?wx_fmt=png&from=appmsg)

获取 Windows 版本

**断网逃避云端上传：**利用解压器和密码 H7C9V7A9X7V9D7AC6V9D9A 对不同版本的 ipconfig.exe进行解压。当系统版本为 Windows 10 时，执行命令行 YJUSA.exe /v9f8s7a 来实现断网操作（这里的 YJUSA.exe /v9f8s7a 与 ipconfig.exe /release 功能相对应）。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/0icdicRft8tz55bHvlaCfHAGxaoycszib0EhXicXnIUgcrkgAia3A6OibX38JanniaSJdkHRpNU1Jal4BUrtyM6oV86uQ/640?wx_fmt=png&from=appmsg)

释放和重新获取 IP 地址

**检测断网是否成功：**释放 IP 地址后，设备将无法联网，此时尝试连接 www.baidu.com，若无法连接则开始利用密码 H7C9V7A9X7V9D7AC6V9DA9A 解压 nsWrsIrkxL.jpg，从而解压出 QQ 音乐白加黑模块。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/0icdicRft8tz55bHvlaCfHAGxaoycszib0E4MfW8Hictl3mic4tPLV6L67lcBqGQXicEC6vibO67IjQeMUfcdueERsnYw/640?wx_fmt=png&from=appmsg)

所有文件

![](https://mmbiz.qpic.cn/sz_mmbiz_png/0icdicRft8tz55bHvlaCfHAGxaoycszib0E9ve8qO45p5vq4nPiadOicAdvu5ib9HBghGdiauEIzlAB7ranc4yOx9tqYg/640?wx_fmt=png&from=appmsg)

文件说明

**实现持久化：**在解压后执行 Application.exe，并传入参数 " powershell Start-Process C:\Users\Administrator\AppData\Local\Temp\rn.lnk -Verb RunAs " 和 "C:Windows\system32\WindowsPowerShell\v1.0\powershell.exe"。此操作目的在于利用 powershell.exe 和管理员模式来执行 rn.lnk，即利用 zip 解压器解压出 ManicTimeVico.exe 的快捷方式，并将其放置在 APPDATA 下的启动项目录中，实现持久化操作。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/0icdicRft8tz55b...