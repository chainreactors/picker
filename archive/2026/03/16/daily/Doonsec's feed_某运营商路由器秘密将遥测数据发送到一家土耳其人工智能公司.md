---
title: 某运营商路由器秘密将遥测数据发送到一家土耳其人工智能公司
url: https://mp.weixin.qq.com/s/tXYdslOUTxujKuW5oaKlqA
source: Doonsec's feed
date: 2026-03-16
fetch_date: 2026-03-17T04:14:59.249880
---

# 某运营商路由器秘密将遥测数据发送到一家土耳其人工智能公司

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/ibO9kiauylaDqt8qXiaZXLPoGd8hFSTxCtmRWJ3IibVsRemouuU68NvyaWupk2uxvFBWOKDNREf0MGvRmleicdWIsDyeEHc8fMfNfQwCFMX3sX0s/0?wx_fmt=jpeg)

# 某运营商路由器秘密将遥测数据发送到一家土耳其人工智能公司

安全内参

![]()

在小说阅读器中沉浸阅读

编者荐语：

该数据收集行为的影响范围，早已不局限于 Odido 的签约用户。哪怕你的邻居使用的是荷兰 KPN、Ziggo 等其他运营商的路由器，也会被 Odido 的设备扫描并记录相关信息。

以下文章来源于黑鸟
，作者黑鸟

![](http://wx.qlogo.cn/mmhead/X4XEGYefSBSxrDYncLtKiacf7vZpHQnuLDMVc1rQjZsw9xYSM6kSCezibImssYuBjTibclnyop737M/0)

**黑鸟**
.

一介草民，深耕威胁情报领域多年，自封威胁分析师，APT狩猎者，战略忽悠分析师。 专注推送一切前沿高科技/人工智能、网络安全分析、敌我战略分析、数据挖掘、情报扩线、网络武器分析、社会工程学、一切开源情报、军事分析忽悠等。

家用路由器，本该是你家中最值得信任的网络设备。你的手机、笔记本电脑、智能电视，所有智能设备都通过它接入网络。

那么，当运营商提供的路由器，正在秘密将你内网所有设备的详细分析数据，发送给一家境外 AI 公司时，意味着什么？

最新发现，荷兰运营商 Odido（前身为荷兰 T-Mobile）向用户提供的合勤 Zyxel T-56 路由器进行网络流量分析后，证实该设备会持续将联网设备的 MAC 地址、设备名称、流量使用统计数据，甚至周边 WiFi 网络信息，发送给 Lifemote，一家向全球运营商销售 WiFi 分析服务的土耳其 AI 公司。

荷兰数据保护局（Autoriteit Persoonsgegevens，简称 AP）已明确表态，MAC 地址属于法定个人数据。而面对多方质询，Odido 仅回应称：“我们的隐私声明已发布在官方网站上。”

## **在《电讯报》(De Telegraaf) 对此进行询问后，Odido 似乎已停止了这种做法。**

![](https://mmbiz.qpic.cn/mmbiz_png/ibO9kiauylaDp2lZKQicGD6U9nw2ILqgCicsn9YLN0jSzyFjmkYBw6iavkkfQHPN12m6U8OibgibseaZo0eCcibziabVfjE6hjRPuKHjdQmTR7VEX1fs/640?wx_fmt=png&from=appmsg)

Odido 是荷兰电信运营商（前身为 T-Mobile Netherlands，2023年更名为 Odido），提供移动、固定宽带（主要是 Glasvezel 光纤）和电视服务。作为它的互联网客户，通常会从 Odido 免费或包含在订阅中获得一台 modem/router 组合设备（常称为 Odido-router 或 modem），用于连接家庭网络。

渗透测试工程师西普克・梅勒马，对自己 Odido 配套的合勤 Zyxel T-56 路由器的出站网络流量进行了拦截与深度分析，最终发现了令人震惊的事实：该路由器会定期向 Lifemote 运营的服务器发送详细的遥测数据，具体包括：

* 接入该网络的所有设备的 MAC 地址（媒体访问控制地址，设备的唯一网络识别码）；
* 设备自定义名称（往往包含大量个人信息，比如 “萨拉的 iPhone”“彼得的工作笔记本”）；
* 单设备流量使用数据（每台设备的上传、下载流量详情）；
* 周边邻居路由器的 WiFi 网络 SSID（服务集标识符，即 WiFi 名称）与 MAC 地址；
* 热点信息与网络性能指标。

##

Lifemote 是一家土耳其 AI 企业，核心业务是为全球运营商提供 WiFi 数据分析与网络优化服务。其商业模式十分清晰：运营商将 Lifemote 的软件嵌入旗下的路由器固件中，Lifemote 则通过收集、分析海量路由器回传的数据，为运营商输出网络性能、设备行为、WiFi 质量相关的分析洞察。

![](https://mmbiz.qpic.cn/mmbiz_png/ibO9kiauylaDrn16BJ1NQQqqCfFOG05bSD2bEM3jtj8N4ZU0bDwdtRvJIE6LGVD0THpv8FbrqPA2ZuYHLj1oLxWQYiaLBtQFJEClyjib27ElKGg/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/ibO9kiauylaDo96b54c8HxsyfcOh498mRyZhiaoib0ucNb0l0TtPErsONS8wLWy6mMUZEkfibGnHLOATdoicwJAnsdVP81H4KXWribu5oTY9EjRrDc/640?wx_fmt=png&from=appmsg)

从表面来看，这似乎是一项合规的商业服务 —— 运营商需要掌握路由器的运行故障，从而减少客服咨询量。但问题在于，其数据收集的范围，早已远远超出了网络诊断的合理必要限度。

收集所有接入设备的 MAC 地址与设备名称，对诊断 WiFi 干扰毫无必要；扫描并上报周边 WiFi 网络信息，与用户自家路由器的运行性能更是毫无关联。而将所有这些数据发送至欧盟境外的土耳其，更是引发了关于数据保护合规性的严重质疑。

周边 WiFi 网络的 MAC 地址，能以惊人的精度锁定路由器的物理位置。多年来，谷歌、苹果等企业通过街景采集车、移动设备，已对全球数百万个 WiFi 路由器的 MAC 地址与物理地址进行了测绘匹配。只要掌握了某台路由器周边的 WiFi 网络信息，无需 GPS、无需 IP 地址，就能精准定位其所在位置。

在美国，移民与海关执法局（ICE）就曾利用商业采购的 WiFi 与位置相关数据，追踪并拘捕相关人员。尽管荷兰与美国的执法环境不同，但核心风险完全一致：一旦这些数据进入第三方数据库，你就彻底失去了对它的控制权，没人能保证它会被谁访问、被如何使用。

每一台 WiFi 路由器都会广播自身唯一的 MAC 地址（也叫 BSSID）。谷歌、苹果等企业已将数百万个这类地址与物理位置一一对应，形成了庞大的数据库。如果 Lifemote 的数据库中，包含了你家路由器周边的 WiFi MAC 地址，这些数据就能与现有 WiFi 位置数据库交叉匹配，精准锁定你的家庭住址，全程无需你的 IP 地址或 GPS 坐标。

本次事件中最离谱的一点，莫过于合勤 Zyxel T-56 路由器会主动扫描周边 WiFi 网络，并将邻居路由器的 SSID 与 MAC 地址一并发送给 Lifemote。

这意味着，该数据收集行为的影响范围，早已不局限于 Odido 的签约用户。哪怕你的邻居使用的是荷兰 KPN、Ziggo 等其他运营商的路由器，也会被 Odido 的设备扫描并记录相关信息。这些邻居从未同意过 Odido 的隐私政策，从未与 Odido 签订过服务合同，甚至和 Lifemote 没有任何交集。

但他们的路由器唯一识别码、网络名称，依然被发送到了土耳其的服务器上。

路由器的分析数据能清晰还原一个家庭的生活规律，有多少台活跃设备、住户何时在家、使用什么类型的智能设备。而这些，正是广告公司、数据中间商、AI 训练机构趋之若鹜的行为数据。

本次路由器遥测数据丑闻曝光的几周前，Odido 刚刚发生了一起大规模数据泄露事件：黑客组织 ShinyHunters 声称窃取了 2100 万条用户记录，其中包含护照号、银行账户（IBAN）等核心敏感信息，最终经核实受影响用户规模达 620 万。两起事件接连发生，让这家电信运营商对用户数据的随意态度暴露无遗。

如果你是 Odido 的用户，或是任何担心运营商路由器遥测追踪的用户，可通过以下具体步骤保护自身隐私：

### 1. 检查路由器管理后台设置

登录路由器的管理面板（通常地址为 192.168.1.1 或 192.168.0.1），查找所有标注为分析、遥测、“提升用户体验” 的相关设置，禁用所有向第三方发送数据的选项。针对合勤 T-56 路由器，重点查找与 Lifemote 相关的设置，以及远程管理选项。

### 2. 更换为自有路由器

最彻底、最有效的解决方案：用自己购买的路由器，替换运营商提供的设备。在荷兰，法律赋予用户 “自由选择调制解调器 / 路由器” 的法定权利（vrije modemkeuze）。你可以购买知名品牌的合规路由器，将其接入光纤 / DSL 终端设备，同时彻底停用运营商的路由器。没有运营商预装的固件，就不会有运营商嵌入的数据分析程序。

### 3. 开启 MAC 地址随机化

现代操作系统（iOS 14 及以上、Android 10 及以上、Windows 10/11、macOS Sonoma 及以上），均支持针对每个 WiFi 网络随机化设备的 MAC 地址。即便路由器仍在上报 MAC 地址，也无法通过该地址追踪你的固定设备。你可以在每台设备的 WiFi 设置中开启该功能。

##

详细技术细节

荷兰安全研究者 Sipke Mellema 于 2026 年 3 月 3 日在领英发布完整研究成果，披露荷兰运营商 Odido 向用户提供的 Zyxel EX5601-T1 家用路由器存在两项严重安全问题：一是设备会将用户家庭内网及周边网络的敏感分析数据，未经有效加密传输至第三方企业 Lifemote；二是设备存在可被稳定利用的远程代码执行漏洞，攻击者可通过中间人攻击篡改设备拉取的更新脚本，直接获取路由器的 root 权限。研究者在 3 月 8 日补充更新称，已监测不到设备去往 Lifemote 的网络请求，推测 Odido 已对相关问题进行了静默修复。

若安全从业者或测试者想要复现这一研究过程，需格外注意相关合规与法律风险。例如，切勿仅针对运营商管理 VLAN 进行入侵操作 —— 该环境并非漏洞百出、毫无管控的公开测试网络，而是运营商的内部专用核心网络，违规操作将面临极高的合规追责与法律风险。

## 核心调查结果

1. **未加密 HTTP 拉取执行脚本，可直接获取 root 权限**

   Odido 路由器在每次新建 WAN 连接时，会通过明文 HTTP 协议从远程服务器拉取 bash 更新脚本并直接以高权限执行。测试者可通过中间人攻击篡改该脚本内容，在路由器上植入恶意指令，稳定获取设备的 root shell 最高权限。
2. **TLS 证书验证被强制关闭，加密流量完全可劫持**

   该路由器的数据分析与上报脚本中，开发人员为 curl 工具添加了`-k`（--insecure）参数，强制关闭了 TLS 证书有效性验证。这意味着攻击者可通过自签名证书发起中间人攻击，完整劫持并读取设备本该加密传输的用户分析数据，流量内容完全暴露。
3. **批量收集用户敏感隐私数据，用于第三方 AI 训练**

   该路由器会持续向 Lifemote 公司上传多维度的用户敏感数据，包括家庭内网中所有联网设备的名称、MAC 地址、网络连接状态与流量使用详情，周边 WiFi 网络的 SSID 名称与 MAC（BSSID）地址，以及路由器自身的运行状态、网络配置等分析数据。据悉，Lifemote 公司主打 “面向运营商的 AI 驱动家庭 Wi-Fi 解决方案”，这些从用户家庭网络中采集的数据，将被直接用于其 AI 模型训练。研究者明确指出，用户家庭内网的敏感数据在未获得充分知情同意的前提下，被用于第三方企业的 AI 训练，存在严重的隐私泄露与滥用风险；同时该漏洞的利用门槛极低，也具备极高的网络安全研究价值。

   ![](https://mmbiz.qpic.cn/sz_mmbiz_png/ibO9kiauylaDq6AXop8wZQSUwjmE0x70ALnXfkCP5aQmWJJE99vHK67OoWT6pXJaDGVfftEzLNEia2xNhmUJMn1V8JGxibib0SPGZu7Sb9mao7xI/640?wx_fmt=png&from=appmsg)

该研究项目中，研究者搭建了一套可控的中间人测试环境，核心使用一台三口 APU 设备串联部署在家庭路由器与运营商光猫之间，在 APU 上基于 Debian 系统通过 mitmproxy 工具，对自身的 WAN 流量发起透明中间人攻击。研究者的初始测试目标，仅为排查家庭网络中是否存在关闭 TLS 证书验证、存在安全隐患的物联网设备，而 Odido 运营商定制路由器的这一严重缺陷，完全超出了研究者的预期。

这是APU的照片。所以那根黄色线缆作为普通网络设备在路由器里，而那些黑色线缆则从调制解调器拉到路由器的WAN口。

![](https://mmbiz.qpic.cn/mmbiz_jpg/ibO9kiauylaDo95ZEZeagq9pxIibsk5zfAek0vhWvyJL2qMwtTqq5n5ZaMcgZYhJ88Hc3LRAPZ4YZADn4w6vQTE1gVmVSNk0X3Cfajh18h3W0c/640?wx_fmt=jpeg&from=appmsg)

为完成 APU 的环境配置与流量监听，研究者首先在桥接模式下对 WAN 流量进行被动嗅探。通过 APU 的 1 号、2 号网口，将光猫到路由器 WAN 口的物理链路做了环回桥接，使所有 WAN 流量完整流经 APU 设备，随后通过`tcpdump -e`命令抓取并分析流经的 VLAN 标签流量。

测试过程中，研究者识别出三个运营商网络的关键 VLAN：用于运营商内部设备管理的 VLAN 100、承载家庭用户互联网访问业务的 VLAN 300，以及用于 IPTV 电视业务的 VLAN 640（研究者未对该业务 VLAN 开展测试）。同时，为规避运营商可能在网络侧启用的 MAC 地址过滤机制，研究者伪造了路由器的 WAN 口 MAC 地址；此外，APU 的 3 号网口直连路由器的 LAN 侧，保障研究者在测试全过程中，可持续通过 SSH 协议稳定访问路由器设备。相关测试拓扑结构见下图：

![](https://mmbiz.qpic.cn/mmbiz_png/ibO9kiauylaDqaF6e4VPr2L9oN7n2QzzNh1lE78RkiaQov3fEGAA4icibdoxXWfOGrmcbthu4icjVlWS8LBiasSQ22QxIQKniaX6a4LEmb22KUThmAo/640?wx_fmt=png&from=appmsg)

完成基础网络拓扑部署后，研究者配置了端口转发规则，将 80（HTTP）与 443（HTTPS）端口的入站流量全部路由至本地 8080 端口，并通过自定义的 alert.py 脚本启动 mitmproxy 透明代理。

```
/root/mitmproxy/mitmdump --mode transparent --listen-port 8080 --set block_global=false --scripts /root/mitmproxy/alert.py
```

该脚本核心实现三项功能：

* 监测到设备发起未加密的 HTTP 连接时，立即发布告警并完整记录请求与响应内容；
* 监测到客户端接受自签名 TLS 证书、存在证书验证缺陷时，立即发布告警；
* 两种场景下均留存完整的流量日志，用于定位发起不安全连接的设备与具体行为。

mitmproxy 启动后，研究者立即收到了明文 HTTP 连接的告警，所有告警均指向`dream.tmn.lifemote.com`域名的请求，目标正是 Odido 路由器用于功能更新的 bash 脚本。

```
2026-03-03 01:27:18.016955 PLAIN HTTP to 3.73.3.59 - http://dream.tmn.lifemote.com/v1/scripts?type=ex5601-t1 2026-03-03 01:29:31.131995 PLAIN HTTP to 3.73.3.59 - http://dream.tmn.lifemote.com/v1/scripts%3Ftype=ex5601-t1 2026-03-03 01:41:13.346041 PLAIN HTTP to 63.182.243.74 - http://dream.tmn.lifemote.com/v1/scripts?type=ex5601-t1 2026-03-03 01:41:46.092295 PLAIN HTTP to 3.73.3.59 - http://dream.tmn.lifemote.com/v1/scripts?type=ex5601-t1
```

这些是明文与“dream.tmn.lifemote.com”的联系。那到底是怎么回事？日志中可以看到，这是一个用于更新 Odido 路由器的 shell 脚本。

```
![](https://mmbiz.qpic.cn/sz_mmbiz_png/ibO9kiauylaDqkoiaWm5MHzADZuJTmlMf7Rq5ib1lic5micJcALicQibMnGibGjlqeSRCibuw8YMZiaeoAYb54fGich5JOuibB22XcXoZ9Hhz86hCwMELUIY/640?wx_fmt=png&from=appmsg)
```

基于这一缺陷，研究者修改了 mitmproxy 脚本，在路由器拉取的更新脚本中插入了反弹shell 植入指令，由于涉事路由器为 64 位 ARM 架构的 Zyxel EX5601-T1，研究者通过`aarch64-linux-gnu-gcc`交叉编译了适配的反弹shell 二进制文件，通过篡改后的脚本完成文件复制与执行操作。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ibO9kiauylaDp4Fiarz6XRpmWmtZWdic97Fd7Jss9Ta5UC4EbicXSJhRDhjicD1ElKWJvmMIXeMX5jRVwgkTfzI2uohO9D7fneU4I8tBXE2ePc1fA/640?wx_fmt=png&from=appmsg)

重启 mitmproxy 并重新插拔路由器 WAN 链路后，设备在新建 WAN 连接时拉取了被篡改的更新脚本，研究者成功获取了路由器的 root shell 最高权限。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ibO9kiauylaDrOSYRYHzSmG5tGtPTulvJ5hYh9KfhfSJ2f4f6M5NhUxq6buiaWclwcPbiccS8nDicnNkQYd...