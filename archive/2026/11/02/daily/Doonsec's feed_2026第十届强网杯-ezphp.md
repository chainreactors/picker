---
title: 2026第十届强网杯-ezphp
url: https://mp.weixin.qq.com/s/DqDHQWi9yEJSHetzC_V_DQ
source: Doonsec's feed
date: 2026-11-02
fetch_date: 2026-11-03T08:48:58.208315
---

# 2026第十届强网杯-ezphp

# 2026第十届强网杯-ezphp

原创

識.
識.

0xNyx

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

这道题就很明显是前几天爆出的热门CVE，php2webshell

sqlmap扫一下，万能密码注一下

![](https://mmbiz.qpic.cn/sz_mmbiz_png/icPMQgcMTD2fgLHTvIKK4m7KGluaVh3x2ZRsxbfdUDwiaCMfseKFIB1w1vzVxNB0piaQeGaibKbJ4nJGZM6MSbv4hgIicxvGUicYibLuVQzRBgzOjA/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/icPMQgcMTD2euofZa9m1U70AdEj75G6u9KAibEecZicYzcQfhOEfScaia6u6uS3iabltaAINTOUuicp34ic8yVokdVlib4YTdzTnrJkaKTGfGgoHMkk/640?wx_fmt=png&from=appmsg)

dirsearch扫一下

![](https://mmbiz.qpic.cn/mmbiz_png/icPMQgcMTD2fAkS1pslK0xDic8R4peFGMdEy79O1Fc3LmKoVB9yxLicTqQ1Jm9TCU4zfp2EjKEmoxxhH8EPFRiasRJqneRNq6vszYofMzjD4EzM/640?wx_fmt=png&from=appmsg)

访问flag.php

![](https://mmbiz.qpic.cn/mmbiz_png/icPMQgcMTD2dh9uNmw7yFV5WicibNxmIjVJXtT8SDK7JdFq3GSnmzWlApU9hJDd560T8qj0fTCxQIRM6XxQqN8LNJ6HfowFicjyo5CYCtnVicLeo/640?wx_fmt=png&from=appmsg)

代码审计

![](https://mmbiz.qpic.cn/sz_mmbiz_png/icPMQgcMTD2fyTxJHCAB7DXFBpqB5VkKYwAbXiahibAF9a8MUhNf2VXic9DlHjYQf0LkF1Eibicw885Et0WUKicibYgBkV5G5IWCz8ycM3iaVIW5xxnM/640?wx_fmt=png&from=appmsg)

再 `GET /status.php` 拿版本号（`{"versionstring":"34.0.3", ...}`），`GET /ocs-provider/` 确认这个目录存在且可访问——后面 webshell 就写这里。

指纹

![](https://mmbiz.qpic.cn/mmbiz_png/icPMQgcMTD2cgekUzJ8HxoWdpKkoyT1PjyiaUom3UGdWyOSj0dnoSzfnvHUjDFrOrSxmZl3eK9x58Ih7Er8usXwrhIR533PF8XwxWz5Aj2Vfo/640?wx_fmt=png&from=appmsg)

SSRF 打本机 80

![](https://mmbiz.qpic.cn/sz_mmbiz_png/icPMQgcMTD2dGfJs1ORCh86z3wuhlnu8LoDaL4hVJ78x8TrMHuUWc7ic1Dm3DPnUx5SmqNicUzmaGomNlfDIo2FaUPBpN3Ohfsh4Fg6cZjUhZ4/640?wx_fmt=png&from=appmsg)

假flag

这是 `/opt/ctf/internal/flag.txt` 的内容，**诱饵**。

body 是**二次编码**的：`%2520` 被 PHP 解一层变 `%20`，再被 curl 解一层才是空格。少解这一层，`$url` 里就会直接出现裸 CR/LF。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/icPMQgcMTD2ekycykLWA32c9ltop4PsG5SKAnffQ5C8M4ic90Bd5NjicDLYICVMbOGhyzEccbcIBxbTPBMarAiaicelNqrgxy8qCKDEJkBDu5AUU/640?wx_fmt=png&from=appmsg)

从 Redis 读这个会话

![](https://mmbiz.qpic.cn/mmbiz_png/icPMQgcMTD2e2DibI8dXO1TVSUHkVd9vdgp3NIXh47hpTNZbsm2bjN2tMZbwnKqpqIXib6m0iapsB0KtEYWF8UBaibCWpgTOpYgoB3OHlv5aEwh0/640?wx_fmt=png&from=appmsg)

`$420` 是 RESP 长度头，后面 420 字节原样留着，包 07 要用。

这里的空格要**两层**：报文里写 `%2520`，PHP 解一层变 `%20`，curl 再解一层才是空格。只写 `%20` 的话 PHP 直接把裸空格塞进 URL，curl 拿到的 selector 就变了——实测返回**空**，不报错，很容易卡住。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/icPMQgcMTD2d4oiayibmyk5KmHM74l8EBUrra4tq6mbytiaHGlrCbjMLt0gKThP1IRYjTQKjpgmibbngZFNMmvicaKEG9bjxEy0MuaGcOPgupTDuQ/640?wx_fmt=png&from=appmsg)

**注入**

![](https://mmbiz.qpic.cn/sz_mmbiz_png/icPMQgcMTD2ck6s1VrJlrYmQv8pbQpLfXYIeEfamccQv9HbZ2nshCv4HAIWhFbA0ZVC5wkVnwzaiaoc9vnkUH4LWz9sqFkuxY9Qj4KVF62bm8/640?wx_fmt=png&from=appmsg)

这个 body 解开一层后就是一条 RESP 命令（下面是示意，真实字节是中间夹着`\r\n`的）：

代码块

```
*3
$3  SET
$49 PHPREDIS_SESSION:3201b05300aa9136b3719909f84ab270
$937 <420字节原会话>test|<512字节 payload>
```

`SID`一共出现 3 处：包 06 的键、包 07 的键、包 08 的 Cookie，换的时候三处一起换。

* `Content-Length: 1669`就是这一行 body 的字节数，手改内容后别忘同步；
* `$937`= 420 + 5(`test|`) + 512，写错会`-ERR Protocol error`；
* 成功返回 `+OK`。

验证 shell

![](https://mmbiz.qpic.cn/sz_mmbiz_png/icPMQgcMTD2e1SVeuzuzTXDX6mg7JXBmGRNia15ssm1GrBScpPOKu3fOr4AdySEWCEXv5yrkNhRzP7IkNayUGCA7SDldTRk4A46dY00lkdyBc/640?wx_fmt=png&from=appmsg)

取 flag

![](https://mmbiz.qpic.cn/sz_mmbiz_png/icPMQgcMTD2dkC0Qkf6BGRAtribHzEjyIpw2TibQLu9bibKEOy7Xs1vrEjRSt2gibmQIQPF3HIkps22DxqB06OkoYINY0DTwvWASbOuk29IRKt5Q/640?wx_fmt=png&from=appmsg)

构造payload的思路

![](https://mmbiz.qpic.cn/mmbiz_jpg/icPMQgcMTD2djJe8XOgScDNMmUFAT3qqytWfARxRq4icV4enCMjHb2h2yB4wPWs76s9TafLHfA4vysNnGaDyA4fct0m4iaGACN452Vlsf0icibUs/640?wx_fmt=jpeg)

这道题还是比较人性的

只是思路上复杂一些，代码审计方面的困难较大。这是**CVE-2024-40624**

* 缺陷在`library/includes/functions.php`的`get_tracks()`，它直接反序列化用户可控的 cookie；
* 官方 PoC 写得很直白：用`phpggc`的`Guzzle/FW1`往任意路径写 PHP，然后执行命令。

换句话说，**这题是 CVE-2024-40624 的“CTF 复刻场景”**：同样的链，只是注入点从“cookie 反序列化”换成了“能写 Redis 的 session”。

![](https://mmbiz.qpic.cn/mmbiz_png/icPMQgcMTD2e98SHsQh5W1eYXPJcQUC7qokGJrMlZTST0cgt2So0EdIWHmfYwSww27lIpGemHZkmsgdOIGk2mOZ4S3lplibrQ972Wq79xHzT4/640?wx_fmt=png&from=appmsg)

预览时标签不可点

不喜欢

![]()

微信扫一扫
关注该公众号

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/icPMQgcMTD2ceTCkDez0Piat8aPQyHu06KEJDNNd4u19ZCweicJEoK4tnFV6nQBcXzmV90K7UTllfDM75weNK6tmntI3BhMrkMiaU9bg5ZiaL1EM/0?wx_fmt=png)

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