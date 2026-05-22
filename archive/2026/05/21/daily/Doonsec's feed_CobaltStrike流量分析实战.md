---
title: CobaltStrike流量分析实战
url: https://mp.weixin.qq.com/s/a8SqttZX18OsGC7eHKCzBw
source: Doonsec's feed
date: 2026-05-21
fetch_date: 2026-05-22T05:59:50.214446
---

# CobaltStrike流量分析实战

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/34E6IkhMl2EkQvovtDibKKeK9iclajCvnJDsAcBNia20yO8rw5JemhYkVsu4KjAKvpfpFPAtLIIbMv3NPPcrm2hwJME8xUiaScf5kaReVc1Mk4Q/0?wx_fmt=jpeg)

# CobaltStrike流量分析实战

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

# 前言

CobaltStrike 做蓝队的朋友应该都不陌生。攻击者用它来控制受害机器，通信过程还加密，抓到的包打开一看全是乱码。**但它的通信协议并不是无迹可寻**，摸清规律之后，解密没那么难。
这篇就聊聊，怎么从流量里挖出 CobaltStrike 的痕迹，拿到密钥，还原出攻击者到底干了什么。

---

# 一、通信流程拆解

CobaltStrike 的通信结构不算复杂，核心就两层：Stager 负责拉取真正的载荷，Beacon 负责持续跟 C2 服务器保持联系。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/34E6IkhMl2FoicNAx6ZeWe9lWj9dkusSyfBmPgUGqnZgAFSC3nZTtbCKbcYdMcHfU5MMcAe4BAVwqaS3moXyBKo5eavVR3RhvvJVWicfplCtU/640?wx_fmt=png&from=appmsg)

以最常见的**HTTP 通信 + Stager**模式为例，整个流程可以拆解成 6 步：
**第一步：拉取 Beacon 本体**
Stager 跑起来后，会先向 TeamServer 发一个 GET 请求，把真正的 Beacon 下载下来。这个请求的路径有个特点——经过`checksum8`算法计算后，32 位系统结果是**92**，64 位是**93**。
比如路径`/FJwV`，算出来就是 93，一眼就能对上号。
**第二步：初次心跳**
Beacon 被加载后，会发第一个心跳包。里面塞了不少信息：主机名、用户名、进程名、系统版本、CPU 架构，还有最关键的`raw_key`。这些数据用 Beacon 里内置的 RSA 公钥加密，一般藏在 Cookie 头部里，base64 编码。
请求路径可能长得像`/en_US/all.js`，伪装得挺像正常请求。
**第三步：密钥协商**
TeamServer 收到心跳后，用 RSA 私钥解密。然后双方各自用`raw_key`派生出两把钥匙：`aes_key`用来加密通信，`hmac_key`用来防篡改。之后 Beacon 就开始睡觉，默认 60 秒一轮。
**第四步：醒来要任务**
Beacon 睡醒后接着发心跳，问 TeamServer 有没有新任务。如果有，TeamServer 就回一个 AES 加密的指令包；没有就回个空包。
**第五步：执行并回传结果**
Beacon 拿到任务执行完，把结果用 POST 请求发回去，路径一般是`/submit.php?id=xxxx`。TeamServer 这边看结果是异步的。
**第六步：解密，等下一轮**
TeamServer 用 AES 解密结果，回显、记日志，然后继续等下一个心跳。

> Beacon 的工作模式就是这样：隔固定时间醒一次，问 C2 有没有任务，执行完把结果传回去，继续睡。机制本身不复杂，麻烦的是那几层加密。

---

# 二、流量里藏着哪些"马脚"

加密归加密，CobaltStrike 在流量特征上留了不少痕迹。

2.1 checksum8 路径特征
这是最明显的一个。未修改的 CobaltStrike，Stager 拉取 Beacon 时的请求路径必然满足 checksum8 = 92（32 位）或 93（64 位）。
算法很简单，就是把路径里非`/`的字符 ASCII 码求和，再对 256 取模：

```
defchecksum8(text:str) ->int:
iflen(text) <4:
return0
returnsum(ord(char)forcharintext.replace("/","")) %256
```

拿`/FJwV`试一把：
-F(70) + J(74) + w(119) + V(86) =**349**
-349 % 256 =**93**
**93 = 64 位后门特征值**。如果你在流量里看到类似的路径，警报就该响了。

2.2 固定的 URL 路径
除了 checksum8 动态生成的路径，还有一些**写死的路径**经常出现： -`/submit.php?id=xxx` -`/pixel.gif` -`/q.cgi` -`/en_US/all.js`
这些路径即使攻击者换了证书、改了配置，也很可能保留。看到它们，基本可以锁定 CobaltStrike。

2.3 TLS 层的 JA3 指纹
如果是 HTTPS 通信，在 Client Hello 里可以提取**JA3**值，Server Hello 里对应**JA3s**。这两个值跟操作系统强相关，每个系统基本固定。
在数据包 client hello 中，数据包有 JA3，其值和操作系统有关，每个操作系统都有固定的值。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/34E6IkhMl2FeP24GVEmoZUbZfSxcqWjkvClLerYpwibCLygVRyScGdeUEhOCiaGwKIHBQia9L3vPWXqWZgu1TnkRcZ8VHwlPbrAsEwawd4SthY/640?wx_fmt=png&from=appmsg)

也就是说，**即使证书是伪造的，JA3 指纹也能暴露真实身份**。

# 三、拿到密钥，撕开加密

识别出是 CobaltStrike 只是第一步。真正有价值的，是**解密通信内容**，看攻击者到底下发了什么命令、拿到了什么数据。

3.1 提取 Beacon 配置
先从 Stager 下载 Beacon 本体的响应包里，把载荷捞出来。然后用**1768.py**这个脚本解析配置：

```
python 1768.py beacon.bin
```

![](https://mmbiz.qpic.cn/mmbiz_png/34E6IkhMl2EJqB24oamiclsic669icicPibbNgZgpyLntsUdIDFI9yJa8C4ZpHYDUgTQE7aDfcEqGLdN6r5GLw17Irkw3LS5qBKCXaFfVgT9Idyk/640?wx_fmt=png&from=appmsg)

解析出来能看到一堆关键信息：

| 参数 | 示例值 | 含义 |
| --- | --- | --- |
| payload type | windows-beacon\_http-reverse\_http | 载荷类型 |
| port | 81 | C2 监听端口 |
| sleeptime | 60000 | 心跳间隔（60 秒） |
| maxgetsize | 1048576 | 最大 GET 请求大小 |
| jitter | 0 | 时间抖动 |
| publickey | RSA 公钥 | 加密用的 2048 位公钥 |
| server,get-uri | 192.168.111.128,/\_\_utm.gif | C2 地址和伪装的 GET 路径 |
| post-uri | /submit.php | POST 请求路径 |
| spawnto\_x86 | %windir%\syswow64\rundll32.exe | 32 位注入目标 |

> **publickey**是关键。拿到它，后面的解密才有抓手。
>
> ![](https://mmbiz.qpic.cn/mmbiz_png/34E6IkhMl2FADD81zUpBV09TOD7KiazF60URtCrSibdqmu4ibu3xFtKMMnaq6ic1qnUHAR0WGXJqOoDEiaFwS0dEvVjyOcaMnalFvzKGtGocSAibU/640?wx_fmt=png&from=appmsg)

3.2 获取 RSA 私钥
有公钥还不够，得拿到对应的私钥。两条路：
**方法一：从 TeamServer 本地文件提取**
如果能拿到攻击者 TeamServer 上的`.cobaltstrike.beacon_keys`文件，直接用脚本就能导出私钥：

```
importbase64
importjavaobj.v2asjavaobj
withopen("keys","rb")asfd:
pobj = javaobj.load(fd)
privateKey = pobj.array.value.privateKey.encoded.data
privateKey = (
b"-----BEGIN PRIVATE KEY-----\n"
+ base64.encodebytes(bytes(map(lambdax: x &0xFF, privateKey)))
+b"-----END PRIVATE KEY-----"
)
print(privateKey.decode())
```

![](https://mmbiz.qpic.cn/mmbiz_png/34E6IkhMl2FE36DS2VibiblDrdvzVhoqKiawZiaUXz4eRPwHWWaXAHeiceGAkSmZK7kWImzoFV0PlIicGMYabeESnWG2HlwkooagW6TL59ibhdicWOk/640?wx_fmt=png&from=appmsg)

**方法二：因数分解公钥（难度极大）**

从 Beacon 配置里提取 RSA 的 n 和 e，然后用 yafu 之类的工具分解 n 得到 p 和 q，再算出私钥。

![](https://mmbiz.qpic.cn/mmbiz_png/34E6IkhMl2E7jKoYSgnL5Olic57HvXALpv3b7KM4fEUIf45nuFm2aP8X34FbtjwvaMiczUEDgWNcqVK6wBUGf7wE6qBzcgwR6TqibE6vISYfc4/640?wx_fmt=png&from=appmsg)

**这条路基本走不通**。2048 位的 RSA，分解难度不是开玩笑的。想办法拿原密钥文件更现实。

3.3 解密元数据，拿到 raw\_key
有了私钥，就能解密 Beacon 发的第一个心跳包。元数据通常藏在 Cookie 头里，base64 编码。

用`cs-decrypt-metadata.py`脚本：

```
python cs-decrypt-metadata.py -p <私钥(hex格式)>
```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/34E6IkhMl2FFP7m4v1QWBKkO6ibfDkS1uXQfLwUyUQOTW0ian1UYRBQSSZcvia4a6xl1jFCPObBia3qVsvFh48p3FyicEv60o2eUzcOLzEzibmbC0/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/34E6IkhMl2EI1bmmiaXJGUcHGrrbYFICRia54yUubcQ5ZWbhQuicD2dfOzicI6sDSIrjWQf5UdUia6DIUib53veuOKhIDN6sssWGhldeTwbW5Wqf8/640?wx_fmt=png&from=appmsg)

解密后能得到**raw\_key**。这是后续所有解密的关键。

3.4 批量解密流量
拿到 raw\_key 之后，就可以派生出`aes_key`和`hmac_key`，然后批量解密整个会话。

用`cs-parse-traffic.py`，过滤出非 GET 的 HTTP 包（响应包是命令，POST 包是结果）：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/34E6IkhMl2FNB7QBDEPqOwuYFPEjtpF8e62BwBgiaNRgPalrtWia4k6RsLs1Y2wzPTtoXqgagNZicupq01ZicwBavIgKcMuFQe9NIYAlrCDcAkM/640?wx_fmt=png&from=appmsg)

```
python cs-parse-traffic.py
-r a4553adf7a841e1dcf708afc912275ee
-k a368237121ef51b094068a2e92304d46:b6315feb217bd87188d06870dd92855b
-e
-o res.txt
cs-spec.pcapng
```

参数说明： -`-r`：raw\_key -`-k`：HMAC\_KEY:AES\_KEY -`-e`：同时提取恶意 payload -`-o`：输出文件
跑完打开`res.txt`，攻击者下发的命令和回传的结果，全都明文躺在这里。

---

# 四、TeamServer 日志里的宝藏

除了抓包解密，如果能接触到 TeamServer 的环境，日志目录里东西不少。
日志一般在`Cobalt_Strike/logs/`下，按日期分文件夹（`YYMMDD`格式）。

**每个日期文件夹里都有什么：** -`events.log`—— 全局事件：谁登录了、Beacon 什么时候上线、监听器增删记录 -`weblog_.log`—— 对应端口的 web 服务日志，Stager 下载 Beacon 的记录就在这里 -`downloads.log`—— 从被控机下载文件的记录
**每个被攻击 IP 的子目录里：** -`beacon_.log`—— 和这个 Beacon 的所有交互：执行的命令、命令回显、元数据 -`keystrokes/`—— 键盘记录 -`screenshots.log`+`screenshots/`—— 截屏记录和实际图片
`beacon_.log`的格式长这样：

```
02/12 11:51:15 UTC [input] shell whoami
```

时间、操作员、执行的命令，一目了然。有时候这比解密流量更直接。

# 五、总结

识别 CobaltStrike 流量，checksum8 路径、固定 URI、JA3 指纹这几条规则基本够用了。拿到密钥之后解密通信内容，才能知道攻击者到底下了什么命令、回传了什么数据。运气好的话还能接触到 TeamServer 日志，那就是现成的证据链。
加密从来不是为了杜绝分析，只是让分析变麻烦。流程跑熟了，遇到这类流量心里也就有底了。

---

预览时标签不可点

阅读原文

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