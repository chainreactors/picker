---
title: 疑似APT-C-13（Sandworm）组织利用SSH+TOR隧道实现隐蔽持久化的攻击活动分析
url: https://mp.weixin.qq.com/s/nJpqvXCYV3ZdvNgYGrG4ow
source: Doonsec's feed
date: 2026-04-21
fetch_date: 2026-04-22T04:43:04.335860
---

# 疑似APT-C-13（Sandworm）组织利用SSH+TOR隧道实现隐蔽持久化的攻击活动分析

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/Emmib7pWXrXKibf0QibribicXgJRuUBmvdZ2vLAVswcrNC0OluicIBVDl6Oe2XHdtZExufcXK48wZ6on4b14PWicVQvJx9s2KdSCAlJ5ZWmYjxiczkU/0?wx_fmt=jpeg)

# 疑似APT-C-13（Sandworm）组织利用SSH+TOR隧道实现隐蔽持久化的攻击活动分析

原创

高级威胁研究院
高级威胁研究院

360威胁情报中心

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

**APT-C-13**

**Sandworm**

APT-C-13（Sandworm）组织（又名FROZENBARENTS）是一个具有国家背景的高级持续性威胁组织，长期从事全球网络间谍活动。该组织以高度隐蔽性和战略针对性著称，主要针对政府机构、外交部门、能源企业及科研组织，旨在窃取政治、军事和科技情报。自2014年以来，该组织不断升级其活动，综合运营社会工程学、零日漏洞及多层代理网络（如TOR）实施定向渗透攻击，具备长期潜伏、精准打击与持续监控的典型特征。

**一、概述**

# 近期360高级威胁研究院捕获APT-C-13组织利用SSH与TOR嵌套隧道技术实施定向攻击的多个恶意样本，这些样本在受害机与攻击者之间搭建了一条双重加密的“匿名直梯”，从而让攻击者能够肆无忌惮的进行敏感信息窃取。鉴于这类攻击很少被披露，因此本文详细介绍整个攻击流程，希望相关企业和个人能够提高安全防范意识，采取有效措施保护企业资产和用户财产免受损失。

**二、攻击活动分析**

## 1.攻击流程分析

APT-C-13组织通过鱼叉邮件投递携带恶意LNK文件的ZIP压缩包，诱骗用户执行后，LNK文件会在用户配置文件目录及其子文件夹中递归搜索诱饵压缩包并多层解压至指定位置，随后运行主控脚本创建SSH与TOR两个计划任务以构建复杂通信链路。其中TOR任务利用HiddenServicePort特性将受害机本地关键服务端口（如SMB/445、RDP/3389）映射至Onion匿名域名，使攻击者无需穿透入站防火墙即可通过Tor节点全球直连内网；同时SSH任务在Tor隧道内部署轻量化SSH服务端，通过PubkeyAuthentication公钥认证和自定义Subsystem子系统配置，形成兼具强加密性与权限控制的隐蔽远程管理通道，有效规避传统流量审计。整个攻击流程如下所示。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Emmib7pWXrXIF6eUn7vicOlwLkBAqWw8Z7ybyUTK175eff6amcmZD9z9eg2wehbIWKCCCXUXC0giahVBouDZ7SxSnglLicxfQ44Um5YDzqJLBtU/640?wx_fmt=png&from=appmsg)

## 2.载荷投递分析

近期我们捕获了该组织多个攻击样本，下面以其中一个ZIP压缩包进行分析。

|  |  |
| --- | --- |
| MD5 | 2156c270ffe8e4b23b67efed191b9737 |
| 文件名称 | Iskhod\_7582\_Predstavlenie\_na\_naznachenie.zip |
| 文件大小 | 11.73 MB (12304687 bytes) |

解压该恶意压缩包后，发现其中包含两个精心伪装的组件：一个是图标和文件名刻意模仿PDF文档的LNK快捷方式文件，另一个是设置了隐藏属性的虚假系统文件夹"$RECYCLE.BIN"，该目录通过属性伪装成Windows回收站系统目录以迷惑用户。

![](https://mmbiz.qpic.cn/mmbiz_png/Emmib7pWXrXJWACKZzfVZib1fwPjrvGX7wKWhJFNI8pOzYGxb874mOglQNo06uWwQpu8baMP9UoicABdHGBuJ1cVKz1wCO5bpLIjLN1Vib9uaIg/640?wx_fmt=png)

提取该LNK文件的命令行参数，如下所示。

![](https://mmbiz.qpic.cn/mmbiz_png/Emmib7pWXrXJVEsYeQgqMibb0jMMLaSXAjKwDoYV7fwU6n0wUlQSCkZuFKtl4zlHerjqSlibMv6gD7Exic6diaI4j2oqcNYrQnsLoiaoMRR5351ko/640?wx_fmt=png)

该LNK主要功能是释放多个恶意载荷并执行，其流程是：首先在当前用户的配置文件目录及其子文件夹中递归搜索自身诱饵压缩包（Iskhod\_7582\_Predstavlenie\_na\_naznachenie.zip），将其解压至AppData\Roaming\uuidPeriod目录后，定位其中伪装在$RECYCLE.BIN路径下的无后缀文件employeeTrigger并将其强制重命名为.zip格式，随即将其二次解压至AppData\Roaming\outlook目录，最终读取解压出的currentSessionTrigger文件内容，将其作为PowerShell指令启动一个隐蔽无窗口（Hidden）的进程在后台静默执行。其解压后所有的文件如下所示。

![](https://mmbiz.qpic.cn/mmbiz_png/Emmib7pWXrXLzCFwauZxjxWMJibCxwcuibX4dX45yeV4McdP7iac1VDVibnRdUnxjJpL8ACHEKiabvLMibVaK1sBOTBgvicCjdGY6LMtjamSoAxiaOAc/640?wx_fmt=png)

为了方便阐述，这里先把该目录中所有的文件功能都列举出来。

1）核心控制与启动

|  |  |  |
| --- | --- | --- |
| **文件名** | **功能** | **详细说明** |
| currentSessionTrigger | 恶意载荷主控脚本 (Payload) | 攻击的核心控制逻辑。负责环境检测、展示诱饵 PDF、注册计划任务以实现持久化，并启动 Tor 和 SSH 服务。 |
| Iskhod\_7582\_...pdf | 诱饵文档 (Decoy) | 正常的 PDF 文件。脚本运行后会将其打开给用户看，以掩盖恶意软件正在后台安装的事实。 |
| externalCustomerDate.xml | 计划任务配置 (SSH) | 用于注册名为 OperagxRepairTask 的任务，确保 operagx.exe (SSH) 在开机/登录时自动运行。 |
| previousAdminResult.xml | 计划任务配置 (Tor) | 用于注册名为 DropboxRepairTask 的任务，确保 dropbox.exe (Tor) 在开机/登录时自动运行。 |

2）伪装的服务端程序 (Executables)

|  |  |  |  |
| --- | --- | --- | --- |
| **文件名** | **真实身份** | **伪装对象** | **功能说明** |
| dropbox.exe | Tor服务端(`tor.exe`) | Dropbox 云盘 | 负责连接Tor。读取 statusMap 配置，将本地端口映射到 .onion 域名。 |
| operagx.exe | SSH 服务端 (`sshd.exe`) | Opera GX 浏览器 | OpenSSH 的守护进程。读取 statePointer 配置，监听本地端口，等待攻击者通过 Tor 隧道连接。 |
| safari.exe | 流量混淆插件 (obfs4proxy) | Safari 浏览器 | Tor 的插件。将 Tor 流量伪装成普通 TCP 流量，防止被防火墙或流量审计设备发现。 |
| obsstudio.exe | SFTP 服务端 (`sftp-server`) | OBS 直播软件 | 配合 SSH 使用，允许攻击者通过加密通道从受害电脑上传或下载文件。 |
| ssh-shellhost.exe | SSH 终端主机 | (无明显伪装) | OpenSSH 的辅助组件，用于支持在 Windows 上执行 Shell 命令。 |

3）配置文件与密钥 (Configs & Keys)

| **文件名** | **真实身份** | **功能说明** |
| --- | --- | --- |
| statePointer | SSH 配置文件 (sshd\_config) | 指导 operagx.exe 监听本地端口 20321，并指定密钥文件位置。 |
| statusMap | Tor 配置文件 (torrc) | 指导 dropbox.exe 创建隐藏服务，暴露 SSH(22)、RDP(3389)、SMB(445) 等端口。 |
| indexWeight | 攻击者公钥 (authorized\_keys) | 存储了攻击者的 SSH 公钥。攻击者凭此密钥即可免密码登录受害主机。 |
| localResponseSummary | 主机私钥 (ssh\_host\_key) | 受害机的 SSH 服务端私钥，用于建立加密连接时的身份验证。 |
| localResponseSummary.pub | 主机公钥 | 受害机的 SSH 服务端公钥。 |

## 3.攻击组件分析

1）主控脚本分析

Lnk文件运行后，其首先加载的是主控脚本currentSessionTrigger，该文件具体内容如下所示：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Emmib7pWXrXI1khRuziaevicCFb5od65iaQbnHgJia5wE7C8qibyKmefhicvjfCribV5bB7meIyDRe1ugclzLMNSHiaN1ZanrCEDD8qeRAlicf1UINAdQ/640?wx_fmt=png)

currentSessionTrigger脚本作为整个攻击链的初始化核心，集成了环境检测、反取证及持久化部署功能。脚本运行开始即执行严格的沙箱及虚拟机检测逻辑，通过校验%APPDATA%\Microsoft\Windows\Recent路径下的.lnk文件数量（阈值≥10）以及系统当前运行的进程总数（阈值≥50）来判定宿主环境。若任一条件未满足，脚本将判定当前环境为虚拟机或分析沙箱并立即终止运行。在确认环境安全后，脚本会立即执行诱饵展示与痕迹清除操作：将伪装的 PDF 文档（Iskhod\_7582\_Predstavlenie\_na\_naznachenie.pdf）移动至用户的 Downloads目录并调用系统命令打开，以此转移受害者注意力。打开的诱饵文档如下所示。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Emmib7pWXrXJcnf8ALCAy46J4BACicJKlDtHWPXZaU1kVeAc8swqsniaSwklRCoMuBG6GmGtIsbQ4Lp72n1HjKV3MiapQFnKRtmviaf0hpT7dQvk/640?wx_fmt=png)

随后，主控脚本递归删除释放目录（uuidPeriod）及脚本自身文件，最大限度消除磁盘取证痕迹。在确保单实例运行方面，脚本创建了名为Global\ratingMethod的系统互斥体，一旦检测到同名互斥体存在即退出，防止多重实例冲突。紧接着，脚本通过读取并修改预置的XML模板（externalCustomerDate.xml 与 previousAdminResult.xml），将模板中的$UserId占位符替换为当前环境的“域名\用户名”，并据此注册名为OperagxRepairTask和DropboxRepairTask的两个计划任务。这两个任务分别伪装成Opera GX浏览器和Dropbox的修复程序，实现了恶意载荷的开机自启与持久化驻留。

脚本最后阶段是建立C2通信通道。脚本进入循环等待状态，持续监测%APPDATA%\outlook\exceptionTag\hostname文件（由Tor服务端启动后生成的隐藏服务标识）是否生成。一旦获取到该文件，脚本读取其前56字节的主机名片段，结合当前用户名与硬编码版本号（3-vquemoxm），拼接成查询参数。随后，脚本调用系统curl命令，通过参数--socks5-hostname localhost:9050强制流量经由本地Tor代理转发，并配合 --retry 1000 及 --retry-all-errors 参数确保持续高频重试，最终将受害者的上线信息发送至硬编码的暗网C2地址（kvk46su7d2qi6g4n43syp4zbsf2rihnc6ztj77qtc2ojvewjqvqilnqd.onion），完成整个攻击链的闭环。下图是Tor服务端运行后的hostname。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Emmib7pWXrXI998dpSJ9cibrzBUEXxccyjIZynylLY5q4veWJ8zxTf8ow2fDyDwtkJqP0B4iamGENgbjsEemtx2sbceDD6BqsjiagdZrVl6oB8k/640?wx_fmt=png)

2）计划任务分析

在主控脚本中会加载两个XML配置文件，以创建两个计划任务，这两个计划任务具体内容如下：

![](https://mmbiz.qpic.cn/mmbiz_png/Emmib7pWXrXJicTUdz4XI7ic8VmiaSicibQL5Ye2ap4ZibFV4x2jnOv6buPCQ3V4J43wtRzy0v4FTdfQ30RO50vKMl30icZxyvyGxhsjMym08FyXL44/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/Emmib7pWXrXLIp1ThPKUichTTQ1m9E7MIu3icujm45LgY1aAicSXwFEkdQTkUNF4tsQBiaJN412blrhKgpVqSePWXzDic0j8gvFehTQnGpGYRkFkU/640?wx_fmt=png&from=appmsg)

从这两个XML文件可以看到其核心触发机制配置为 LogonTrigger，即在用户登录时自动执行。模板中的$UserId字段设为占位符，配合前序 PowerShell 脚本的执行逻辑，该字段会在运行时被动态替换为受害者的“域名\用户名”，从而确保恶意任务精准挂载至受攻陷的用户账户下，实现开机即运行。

此外，为了确保恶意载荷的隐蔽性与运行稳定性，配置文件启用了一系列激进的设置。任务被标记为true，使其在任务计划程序的默认UI视图中不可见，以此逃避管理员的常规检查。同时，配置极大地放宽了运行限制：PT0S将执行时限设为 0（即无限制），允许恶意进程无限期常驻后台；而false与false则强制任务即使在笔记本电脑未连接电源的电池模式下也能启动且不被系统终止，绕过了常规的电源节能策略。

最后，通过传递参数 --headless，攻击者指示conhost在不创建任何可见窗口的情况下启动目标程序。被启动的二进制文件operagx.exe和dropbox.exe分别伪装成合法的Opera GX浏览器和Dropbox 云盘进程，实际上是SSH服务端和Tor服务端。此外，启动参数 -f statePointer 和 -f statusMap 进一步指定了软件运行所需的特定配置文件，确保了攻击组件按预定逻辑加载并建立连接。

3）SSH与TOR配置文件分析

下图分别是Tor客户端与SSH客户端配置

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Emmib7pWXrXKJHnOAGoDdydkibR4a32ONGqK5V0nrefFbKF3rK6u9eT8MSZAP7RYzsyJuHGf0cUSiaE4mR2kFpbvftpnVMQf8w1A3ysrMwjmEw/640?wx_fmt=png&from=appmsg)

a. SSH 服务端配置 (statePointer)：构建隐蔽内网后门

statePointer是一个经过自定义的OpenSSH服务端配置文件，配合伪装成operagx.exe 的 SSHD程序运行。该配置文件的核心策略是“隐蔽监听”：服务被强制绑定在本地回环地址127.0.0.1的非标准高位端口20321上。这意味着该SSH服务不直接对公网开放，防火墙无法从外部扫描到该端口，仅接受来自本机Tor隧道的流量。在身份验证方面，配置明确禁用了密码登录 (PasswordAuthentication no) ，并指定 AppData\Roaming\outlook\indexWeight 为公钥文件(AuthorizedKeysFile)，确保只有持有特定私钥的攻击者才能访问，有效防止了暴力破解和管理员的偶然发现。此外，攻击者还对文件传输功能进行了进程伪装，将SFTP子系统指向名为obsstudio.exe的程序 ，使其在进程列表中看起来像是OBS直播推流软件，从而混淆视听。

b. Tor隐藏服务配置 (statusMap)：打通暗网穿透隧道

statusMap是标准的Tor客户端配置文件(torrc)，配合伪装成dropbox.exe的Tor程序使用，其目的是将受害主机的本地服务暴露给暗网。配置首先指定HiddenServiceDir 为 "exceptionTag/" ，Tor启动后会在此目录生成私钥和 .onion域名，确立受害主机的暗网身份。随后，攻击者定义了一组精密的“端口映射矩阵”，将Tor网络的虚拟端口流量转发至本地敏感端口：外部访问Tor的20322端口被直接导向本地的SSH服务（20321），构成了主要的控制通道；同时，配置还暴露了Windows的SMB端口 (445映射为11435)和RDP远程桌面端口(3389 映射为13893) ，这表明攻击者意图进行文件窃取、横向移动甚至获取完全的图形化控制权。此外，配置中还包含 12192 和 14763 等非标准端口的映射 ，为后续攻击预留的端口。为了进一步隐藏踪迹，Tor的运行数据目录被命名为opera，试图伪装成浏览器缓存数据。

攻击者通过SSH与TOR隧道相互配合，可以在受害者核心网络中建立一个永久、匿名、加密、且能全权远程控制的“影子管理台”，以达到窃取敏感信息的目的。

**三、逃避与混淆技术**

APT-C-13组织针对受害者网络环境中的流量审查、IP封锁等情况也做出了考量，下图是Tor在运行时加载的网桥配置文件。

![](https://mmbiz.qpi...