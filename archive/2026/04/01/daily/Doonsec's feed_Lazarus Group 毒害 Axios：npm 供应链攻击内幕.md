---
title: Lazarus Group 毒害 Axios：npm 供应链攻击内幕
url: https://mp.weixin.qq.com/s/7T497sYqye1KlL4gh9UJew
source: Doonsec's feed
date: 2026-04-01
fetch_date: 2026-04-02T04:28:39.323047
---

# Lazarus Group 毒害 Axios：npm 供应链攻击内幕

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/zNsFJyIuL0GyK6OPjgrNsa3qEC34GsFe1SnVuiaBe0uO97tcibGGAl3OrT3keBFutVgxFaWR8eHHD3QBfEicsCJAwTlZAVfR4icjf0Dlh0lFeu0/0?wx_fmt=jpeg)

# Lazarus Group 毒害 Axios：npm 供应链攻击内幕

Ots安全

![]()

在小说阅读器中沉浸阅读

**威胁简报**

**恶意软件**

**漏洞攻击**

针对昨日Axios npm 供应链投毒事件，ThreatBook 进行了深入的样本分析和攻击追踪。基于长期追踪关键 APT 组织所积累的威胁情报，我们将此次攻击活动归因于 Lazarus Group，并在此基础上进一步识别出其他相关的基础设施和攻击指标（IOC 列于附录中）。

此次事件影响重大。作为 JavaScript 生态系统中最基础的依赖项之一，Axios 的年下载量超过 36 亿次，并且有超过 17.4 万个项目直接或间接依赖于它。许多用户在安装 OpenClaw 及相关软件时已经感染了恶意代码。Windows、macOS 和 Linux 系统均受到影响。建议用户立即检查是否存在回调sfrclak.com。

样品分析

在此次攻击中，Lazarus 劫持了 Axios 的维护者账户，发布了恶意版本，并暗中植入了恶意依赖项plain-crypto-js@4.2.1。该软件包利用安装后钩子自动执行脚本，下载远程访问木马，从而入侵设备并窃取数据。攻击流程如下：

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/zNsFJyIuL0GOYPH348J4USqWgTVspje11OBNhIH17PfToelC243ibcoGdYjwJcMialsc6TNQAdfJ4LKQkh7QFIm6bKBXiaItvYVlWicibn0ic5OW0/640?wx_fmt=webp&from=appmsg)

plain-crypto-js@4.2.1Axios npm 仓库被注入了恶意代码，影响 Axios 版本 1.14.1 和 0.30.4。该package.json恶意代码引入了一个 postinstall 触发器，用于执行恶意setup.js文件。

![](https://mmbiz.qpic.cn/mmbiz_jpg/zNsFJyIuL0EwobXE6dvLXM9uUGyTlpYefz07TCPdaGoPcrhLTbliceryy1l4ZIxNIjup5t8z1leHLB4yoHPLPkyGYjvXPZlvA3I66PXrgRTE/640?wx_fmt=webp&from=appmsg)

运行setup.js的是经过混淆处理的 JavaScript 代码。

![](https://mmbiz.qpic.cn/mmbiz_jpg/zNsFJyIuL0F8PyqeDZLV85xOlY2w9hRCjIibAEicickrEaic6BWibLHfeXGOwxvqRjYaEKfIoTqMMvGCfugBQuICb7pYWA86mUyCRwian71gfTLkk/640?wx_fmt=webp&from=appmsg)

此JS文件的功能是检测主机平台，使用相关的packages.npm.org/URL作为参数下载适用于主机系统的有效载荷，并执行后续木马程序的下载，该木马程序携带攻击者的C2\_url参数C2\_url。http://sfrclak.com:8000/6202033

| 平台 | 下载位置 | POST 请求参数 |
| --- | --- | --- |
| Linux | `/tmp/ld.py` | `packages.npm.org/product2` |
| Windows | `%TEMP%\6202033.ps1` | `packages.npm.org/product1` |
| macOS | `/Library/Caches/com.apple.act.mond` | `packages.npm.org/product0` |

后续有效载荷的文件哈希值按操作系统列在附录的“先前披露的 IOC”部分中。

以下分析以 macOS/Library/Caches/com.apple.act.mond有效载荷为例。该木马程序使用 C++ 编写，有两个版本：一个用于 ARM 架构，另一个用于 x86\_64 架构。

木马程序运行后C2\_url，首先会收集主机基本信息，包括主机名、用户名、操作系统类型和版本、CPU 信息、系统时间和用户进程列表。

![](https://mmbiz.qpic.cn/mmbiz_jpg/zNsFJyIuL0EultC2HRHJqfuxHyGP2V47mW2VzGqMM5JqKVJ9SfYXaOxSfSw3csB1TTkJJT9jHNszGth7gGXQwbJu5UKkQxicicr4VYd0pNxXs/640?wx_fmt=webp&from=appmsg)

http://sfrclak.com:8000/6202033然后，它使用硬编码的 UA向参数中提供的 C2 发送信标： mozilla/4.0 (compatible; msie 8.0; windows nt 5.1; trident/4.0)。

![](https://mmbiz.qpic.cn/mmbiz_jpg/zNsFJyIuL0Hz7kicKibKKoCw0nBa5P7hRejWIpyIug5RMcZ6OKEmh3YQ5Kic3xhHa0sIILq1ZUnYF02TRQeBnicrRt1vYvca97WqzfT2Dr7r1PM/640?wx_fmt=webp&from=appmsg)

该木马的主要功能支持解析 C2 命令并执行相应的基本远程控制功能：进程终止、shell 执行、进程注入（DoActionIjt）、脚本执行（DoRunScpt/ DoActionScpt）以及从指定路径收集目录信息（DoActionDir）。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/zNsFJyIuL0EH3D8X0SLRruIz1Iq8waXZ6icL5DkUQzkETW6ibLqHXbwLkr17Ks7iaqjVHMRfbNnnn0ddjvqb5OWocvzew5q788zl2f9pMMRj8M/640?wx_fmt=webp&from=appmsg)

同时，Linuxld.py有效载荷和 Windows 有效载荷temp.ps1是同一木马的不同语言版本，功能完全相同。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/zNsFJyIuL0GTJeahHMOrp5DSEKjWeBiczbxicBWoicVPBp7SiaNQRibgWgvRHbJ4P7s1Lcia6365NEHhkIiczZdI4RtVAgxyDbdXhpqkjhTMPuj7DI/640?wx_fmt=webp&from=appmsg)

ThreatBook 研究团队利用上述木马的特征开展威胁狩猎，识别出与此次事件相关的多个其他样本。详情请参阅附录中的“新增入侵指标 (IOC)”部分。

归因分析

ThreatBook 的分析发现，此次事件中发现的木马与 Lazarus APT 组织使用的 WAVESHAPER 木马（Mandiant 于 2026 年 2 月披露）在战术、技术和程序 (TTP)、木马行为及相关狩猎规则、网络通信用户代理 (UA)、后续有效载荷投放路径、主机信息收集方法以及 API 调用参数等方面高度相似。我们可以确认它们具有共同的来源。以下是详细分析。

1. 拉撒路历史攻击战术、技术和程序相关性

在此次攻击中，首先感染 macOS 受害者的二进制木马位于以下路径：

/Library/Caches/com.apple.act.mond

将此与 Mandiant 在 2026 年 2 月披露的 UNC1069 活动中报告的 WAVESHAPER 木马投放路径进行比较（ThreatBook 将其归因于 Lazarus）：

/Library/Caches/com.apple.mond

这两条路径完全相同，文件名也高度相似。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/zNsFJyIuL0FSicv1vawHRXN8O4mt7npzN07wIu1rdY0E6yKxDTefK20VQ8tjicU0MtIibe13uz1aFkuic50kiagjg34qgyZicz9Wxo8Pjn0bx1iaPM/640?wx_fmt=other&from=appmsg)

参考资料：谷歌威胁情报

https://cloud.google.com/blog/topics/threat-intelligence/unc1069-targets-cryptocurrency-ai-social-engineering

在 ThreatBook 于 2025 年下半年捕获的 Lazarus 攻击活动中，Nukesped 木马的投放路径/Library/Caches/System Settings与此次供应链投毒事件中的木马投放目录一致。此外，该木马用于收集 macOS 用户进程列表的命令和参数sh -c ps -eo user,pid,command也完全相同。

![](https://mmbiz.qpic.cn/mmbiz_jpg/zNsFJyIuL0EdD9zib419eJiaBHibdhLiazPXlZiaGYW2gljRc8cO3SUKltk63pDYIwyGtgWHyyLYrIDYfWjVmNbMdcIvmVfNMiah4rkUfw8RVwBkI/640?wx_fmt=webp&from=appmsg)

图片：本次事件中 com.apple.act.mond 木马收集进程列表的过程

2. WAVESHAPER 木马相关性

ThreatBook 暂时无法获取 Mandiant 披露报告中提到的 WAVESHAPER 样本（MD5：）c91725905b273e81e9cc6983a11c8d60。然而，通过对比该报告中描述的木马行为和相关狩猎规则，我们发现com.apple.act.mond当前事件中的木马与 WAVESHAPER 木马高度相似——两者都是 C++ macOS 木马，并且基本主机信息收集功能完全相同。

![](https://mmbiz.qpic.cn/mmbiz_jpg/zNsFJyIuL0E08iaQunPQnMsXCEuI6cypxKdrwwM6Quw0Brlia8nxsZxxPBwibdHtwkm8hnKTUpac4zTo28dF0b5VJrXKBcmMaCVl8kjHsxrs1M/640?wx_fmt=webp&from=appmsg)

图片：Mandiant 公开的 WAVESHAPER 及其功能和特性。

![](https://mmbiz.qpic.cn/mmbiz_jpg/zNsFJyIuL0FM8SxpGoxJlkL05SicmMhXXeib7w0oRNKicUJ0miaZZccEhb4mevDJaqMBJx8VQLvibx6ICnSuibMQhKZWklFO9cAsxTq4fWfzM9Ddw/640?wx_fmt=other&from=appmsg)

图片：com.apple.act.mond 木马主函数中的主机信息收集

与 Mandiant 发布的 YARA 检测规则进行进一步比较（G\_Backdoor\_WAVESHAPER\_1）：

```
rule G_Backdoor_WAVESHAPER_1 {
  meta:
    author = "Google Threat Intelligence Group (GTIG)"
    date_created = "2025-11-03"
    date_modified = "2025-11-03"
    md5 = "c91725905b273e81e9cc6983a11c8d60"
    rev = 1
  strings:
    $str1 = "mozilla/4.0 (compatible; msie 8.0; windows nt 5.1; trident/4.0)"
    $str2 = "/tmp/.%s"
    $str3 = "grep \"Install Succeeded\" /var/log/install.log | awk '{print $1, $2}'"
    $str4 = "sysctl -n hw.model"
    $str5 = "sysctl -n machdep.cpu.brand_string"
    $str6 = "sw_vers --ProductVersion"
  condition:
    all of them
}
```

当前木马程序中硬编码的网络通信用户代理（UA mozilla/4.0 (compatible; msie 8.0; windows nt 5.1; trident/4.0)）、后续有效载荷投放路径、主机信息收集方法以及API调用参数都高度一致。我们可以确认，该木马程序com.apple.act.mond与WAVESHAPER木马程序具有共同的代码来源。

![](https://mmbiz.qpic.cn/mmbiz_jpg/zNsFJyIuL0Gn3ia1jdEFR8BxaAB1uLYGFyp1ya5uOB59hqR3tz1gaJUb50DzGr8zPNv2OCBfYqL18C5w5dza0q0MibEUT5UuuVt5GoupicHKGU/640?wx_fmt=webp&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_jpg/zNsFJyIuL0FBNiaqv8Sibz4NjicQ0ctnOyuictd8RW8iaZoD7ziaYuIgyk4icmwxTfq9DICib6VlHDOVjfZPXXzBKKx0y3zTRzqS88yvSG5ek6psQibA/640?wx_fmt=webp&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_jpg/zNsFJyIuL0E5zZBJliacbiayLu41KCiaaO5icXH4chxiaMBTkAIZ6ibW578qR8qm1UMfDvMxCicMOWYErkzp2I2sMoUtfuuENGEIZSputiadN1n3aqs/640?wx_fmt=webp&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_jpg/zNsFJyIuL0HmN57CFONhp8Gqic5cchegicXXbiczMvyUPgXESLeEQDYgicuWibQveXEAyCQm8udPZADB6h0nLVJiaXhticXF4lYKt4BbsLaaS8icRv4/640?wx_fmt=other&from=appmsg)

根据上述归因分析，我们评估认为，com.apple.act.mond当前事件中使用的木马是 WAVESHAPER 木马，而其背后的威胁组织是 Lazarus APT 组织。

附录

先前披露的IOC

C2

* sfrclak.com
* http://sfrclak.com:8000/6202033
* 142.11.206.73

Hash-SHA256

```
Linux (ld.py) fcb81618bb15edfdedfb638b4c08a2af9cac9ecfa551af135a8402bf980375cf
Windows (6202033.ps1) 617b67a8e1210e4fc87c92d1d1da45a2f311c08d26e89b12307cf583c900d101
Windowspersistence (system.bat) f7d335205b8d7b20208fb3ef93ee6dc817905dc3ae0c10a0b164f4e7d07121cd
macOS (com.apple.act.mond) 92ff08773995ebc8d55ec4b8e1a225d0d1e51efa4ef88b8849d0071230c9645a
```

New IOCs

C2

* callnrwise.com
* 142.11.196.73
* 142.11.199.73

Hash

```
5b5fbc627502c5797d97b206b6dcf537889e6bea6d4e81a835e103e311690e22
46f5eea70d536f7affe40409d7aaa5fa0009f0dc4538ba2867cb7569737db859
8c8f5f095d65d3f33ce89a77dfbe84a79bb29d2e0073a57a23dcc014d0683c2e
506690fcbd10fbe6f2b85b49a1fffa9d984c376c25ef6b73f764f670e932cab4
4465bdeaddc8c049a67a3d5ec105b2f07dae72fa080166e51b8f487516eb8d07
ed8560c1ac7ceb6983ba995124d5917dc1a00288912387a6389296637d5f815c
```

**END**

![](https://mmbiz.qpic.cn/mmbiz_jpg/zNsFJyIuL0HwVTlkWibWzfg0Cw69NMnnoRJibKyQJ3z6aIB1MBdibKjW0AMCEUVJkVkDRvzum3vIdu7cWibAAUqN15tW6YGgb7HRXYkFGzSDpxA/640?wx_fmt=jpeg&from=appmsg)

公众号内容都来自国外平台-所有文章可通过点击阅读原文到达原文地址或参考地址

排版 编辑 | Ots 小安

采集 翻译 | Ots Ai牛马

公众号 | AnQuan7 (Ots安全)

预览时标签不可点

阅读原文

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/sz_mmbiz_png/rWGOWg48tadhkzMbpPpSw6NfJHUgsHudwQFGS0EobaB49HVwda7L2eJiaDMvwpakagffpPgepM6gBZzpCncMMHg/0?wx_fmt=png)

Ots安全

向上滑动看下一个

知道了

![]()
微信扫一扫
使用小程序

取消
允许

取消
...