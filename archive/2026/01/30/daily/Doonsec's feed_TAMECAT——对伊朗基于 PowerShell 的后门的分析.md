---
title: TAMECAT——对伊朗基于 PowerShell 的后门的分析
url: https://mp.weixin.qq.com/s/nXdoudRIwABdkOhjLfkhEQ
source: Doonsec's feed
date: 2026-01-30
fetch_date: 2026-01-31T04:02:31.995620
---

# TAMECAT——对伊朗基于 PowerShell 的后门的分析

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/pcgSUGCDdKK3gRukXpicwVcms4jrutMn8ne3H5IChdW6ibzDvPJBiaaEGedn4Rib9Qia6ge5CjvFPQDVfK4SRqQoibKA/0?wx_fmt=jpeg)

# TAMECAT——对伊朗基于 PowerShell 的后门的分析

原创

网络安全9527
网络安全9527

安全圈的那点事儿

![]()

在小说阅读器中沉浸阅读

**TAMECAT**是一款基于 PowerShell 的恶意软件，能够执行各种命令来收集敏感信息。以色列国家数字署的报告深入分析了 TAMECAT 的模块化特性及其功能。该恶意软件被伊朗国家支持的网络间谍组织APT42用于其间谍活动。以色列的报告显示，TAMECAT 已被部署在针对高价值高级国防和政府官员的间谍活动中。该组织利用社会工程学手段，在获取受害者环境访问权限之前，会与受害者建立长期的信任关系。本文将概述 TAMECAT 的功能及其数据窃取方式。

以色列国家数字署公布了TAMECAT可用内存模块的详细说明。其中包括利用远程调试、屏幕截图以及暂停Chrome浏览器进行数据收集等功能，从Microsoft Edge浏览器中提取数据。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/pcgSUGCDdKK3gRukXpicwVcms4jrutMn8h9mWAzbNFPofTNKlV0gsnoKmT8jzB8icdrkxTz3YLlPPKp8XIjs48vQ/640?wx_fmt=png&from=appmsg)

分析中，研究人员指出，该恶意软件从一个 Telegram 机器人接收指令。该恶意软件利用来自该机器人的消息下载其他脚本。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/pcgSUGCDdKK3gRukXpicwVcms4jrutMn8wOibX4sQHaUADlKv5YdaRDIibnWMTJI0tGBJpp7w0mfCClico5Pz4NV6w/640?wx_fmt=png&from=appmsg)

**恶意软件分析**

本文分析的入侵样本首先是一个 VBScript 脚本，用于下载 TAMECAT 的第一阶段。该脚本会检查系统上运行的杀毒软件，从而确定其下载第二阶段时使用的是 conhost 和 PowerShell，还是 cmd.exe 和 curl。本次分析所用的样本可在VirusTotal上找到。

|  |  |
| --- | --- |
| **SHA256** | 5404e39f2f175a0fc993513ee52be3679a64c69c79e32caa656fbb7645965422 |
| **SHA1** | 3fd06c930ddc4b1914151f69454c087a42413a24 |
| **MD5** | d7bf138d1aa2b70d6204a2f3c3bc72a7 |
| **ssdeep** | 24:W/AndhKaG2Ds6w8NlrZ5OGPeAbqf+PvENPB3B3CNdHPdYqf+PveBE:YghhG2D68NVfOGPLZvEN9hUhOveE |
| **文件大小** | 1.25   KB |
| **文件类型** | VBA |

![](https://mmbiz.qpic.cn/sz_mmbiz_png/pcgSUGCDdKK3gRukXpicwVcms4jrutMn8TZ0g4ELQUOs3lCokUOeXx6Av4qcXzr9u5zoM4H1vDibtun6YI8VXF1g/640?wx_fmt=png&from=appmsg)

当 VBScript 文件执行时，它会使用 WMI 获取主机上已安装的防病毒产品列表。然后，该列表用于确定下载第二阶段所需的脚本解释器。如果防病毒产品列表中包含“indows”，则 VBScript 使用 conhost 启动 PowerShell。PowerShell 脚本使用*wget*下载加载器 TAMECAT (081419a484bbf99f278ce636d445b9d8)。文件下载完成后，脚本将使用 PowerShell 执行。该脚本使用混淆命令来执行下载的 PowerShell 脚本。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/pcgSUGCDdKK3gRukXpicwVcms4jrutMn8O62PvWlnOr8bE22SPA2GibGE5HvxbGKE3TwvuLwEhbwnhY0to1Mlibng/640?wx_fmt=png&from=appmsg)

这条经过混淆处理的命令解码后如下：

|  |  |
| --- | --- |
| **混淆命令** | **反混淆命令** |
| gcm | Get-Command |
| **\*ee?p\*** | 调用表达式 |

如果杀毒软件列表中没有 Windows，那么 VBScript 脚本会使用 cmd.exe 和 curl 下载另一段恶意软件。分析时，该链接已失效，因此无法分析其有效载荷。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/pcgSUGCDdKK3gRukXpicwVcms4jrutMn8r6QHer1yaoymQQY3n7W6HBTM0D9rV7L7U8LdD2BfGUKkhqElDO0icJg/640?wx_fmt=png&from=appmsg)

**Nconf.txt（TAMECAT PowerShell 加载器）**

这是托管在 tebi[.]io 上的TAMECAT 加载器。该脚本包含多个变量（每个变量包含一个值数组）以及两个函数。这些函数用于解码数据和执行其他代码。该样本可在Triage和VirusTotal上找到。

|  |  |
| --- | --- |
| **SHA256** | bd1f0fb085c486e97d82b6e8acb3977497c59c3ac79f973f96c395e7f0ca97f8 |
| **SHA1** | 0ef4f7a8d7b1d34e10faa0bca1dcb76a518dd417 |
| **MD5** | 081419a484bbf99f278ce636d445b9d8 |
| **ssdeep** | 192:ENampkg6c3iKtzYC4+HxeycEUj/Pv9w7EczGRThbD5eROPURDcEaoY62DFRWJCXu:Ia8h3BKDWx2lszGN5DeOPURwvoX2RRY |
| **文件大小** | 10.34   KB |
| **文件类型** | PowerShell |

![](https://mmbiz.qpic.cn/sz_mmbiz_png/pcgSUGCDdKK3gRukXpicwVcms4jrutMn8GuFHDHNeZc3Urz8KK28rXRFao5ZheFLqGOD3FjeYXZHvrFnxRDCmow/640?wx_fmt=png&from=appmsg) ![](https://mmbiz.qpic.cn/sz_mmbiz_png/pcgSUGCDdKK3gRukXpicwVcms4jrutMn8sKghYC6QASgvj6GdOicceHW2V79YQA3s1Cf1Gf4rxqmlH7sPXXp2icTQ/640?wx_fmt=png&from=appmsg)

该Gorba函数定义了两个参数，分别称为$te12和$k12ey。这些参数的值在脚本末尾定义，如下表所示。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/pcgSUGCDdKK3gRukXpicwVcms4jrutMn82UyIPIF9DSPUaDSakbmzlStrNfd1gzpyP9sc6spKpIOHyGMVuR5AMA/640?wx_fmt=png&from=appmsg)

|  |  |
| --- | --- |
| 参数 | **值** |
| **$te12** | v+UDXK47mBGgYqTbOXjXVD6MzhZenTfVf6CKxQFp2+AiPHMvmA2a4IiBz4rOi8ffxWdXFtrPk6UABw1b6oBPsW1VV/HNU0mf8jH7xsoBAHY5Sp6vdYc7WGZ6SYO72KIH/hOyBlS5wc7Y86wJR9naW+0nINCYZV6RyD5t/fDpqEoRYW6dHwoebLECkEck/N5C1jhlFHaoS51QKSfgraHI5iRiT6pfpqUN   eJHbYz3VYuo/j2FZ6f5BCJgXoHKPmf4pUSwSZH0qQSa98blmdAH+tG7jc3AUE76IHx4xkzxAldO/4b97duoI6rm+Ucy3rRHHrVnPQ0TvvTvudD/LDBwn3DkNcKSTDvEQDwIgni/MU7BOwklcE1+qQjabXTGr+CrL0c53dNA4OGNYkBAnLokjcoNxKmxbCSK3oSdFEz2+htgPMOjq14IGoPSOWcPX2CVK |
| **$k12ey** | T2r0y1M1e1n1o0w1 |

*$k12ey*参数中存储的值与 Volexity 在PowerStar的一个变体中识别出的值相同。Volexity 共享的 Yara 规则与本次分析中观察到的命令非常吻合。

脚本随后尝试从一个经过 base64 编码的 URL 下载 TAMECAT 的下一阶段。该 PowerShell 脚本在网络流量中使用了硬编码的用户代理。脚本使用downstring 命令从 tebi[.]io 获取文本。脚本对 URL 进行了 base64 编码，并在解码之前丢弃了编码字符串的前 3 个字节。该脚本尝试下载名为 df32s.txt 的文件中的文本，该文件包含经过 base64 编码的内容。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/pcgSUGCDdKK3gRukXpicwVcms4jrutMn8LvwxhunZhFfXUGdjpPg93wUiaFfU3TK5TjVqibOW2VmtbW6PibnDM1VxQ/640?wx_fmt=png&from=appmsg)

|  |  |
| --- | --- |
| User-Agent | Mozilla/5.0（Windows NT   10.0；Win64；x64）AppleWebKit/537.36（KHTML，如 Gecko）Chrome/119.0.0.0 Safari/537.36 |

![](https://mmbiz.qpic.cn/sz_mmbiz_png/pcgSUGCDdKK3gRukXpicwVcms4jrutMn8gQy0Y0UTNI3B3RPyX6RO9OGfN8gxwXrtyDunp1DaHd6sekCMQNQlaA/640?wx_fmt=png&from=appmsg) ![](https://mmbiz.qpic.cn/sz_mmbiz_png/pcgSUGCDdKK3gRukXpicwVcms4jrutMn80HRY85P5b6HSEdJAayVhiaUF5Nc3XrxutudAevcNrk22Su7ibETU9pQA/640?wx_fmt=png&from=appmsg)

该脚本对文件内容进行 base64 解码，然后对每个字节执行以下操作：

* 对每一位进行按位取反运算，并转换为二进制。
* 转换为字符串，并提取从第 24 个字符开始的 8 个字符。
* 转换为字节

完成此操作后，脚本会将字节转换为 UTF-8 编码的字符串。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/pcgSUGCDdKK3gRukXpicwVcms4jrutMn8rALcOSqHdFp0hgv7wbXexYY0v1ic59JCbDccC8zBurUyLyfbqib3jwkw/640?wx_fmt=png&from=appmsg)

解码后的内容揭示了一个附加函数，该函数使用存储在 $te12 中的值执行。此函数定义了一个 AES 解密器，用于在对存储在 $te12 中的值进行 base64 解码后对其进行解密。

|  |  |
| --- | --- |
| **AES  设置** | 值 |
| **块大小** | 128 |
| **密钥大小** | 256 |
| 密钥 | kNz0CXiP0wEQnhZXYbvraigXvRVYHk1B |
| **IV** | 0T9r1y1M2e0N0o1w |

![](https://mmbiz.qpic.cn/sz_mmbiz_png/pcgSUGCDdKK3gRukXpicwVcms4jrutMn854ia9SFIwExkw7ORac12W8GqrUKveJOHgW1rPk7ZqAM8pycIJyia20ZA/640?wx_fmt=png&from=appmsg)

将解码后的字符串传递给*Borjol*函数。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/pcgSUGCDdKK3gRukXpicwVcms4jrutMn8UgiaWemBgKBYNbeticqZ6SS2TEhfqG0bacthhkhaJUQ3gg8zElMthHrQ/640?wx_fmt=png&from=appmsg)

解密后的数据包含以下几种数据处理函数。

|  |  |
| --- | --- |
| **函数名称** | **描述** |
| Borjoly | 首先解码 Base64 编码的数据，然后使用 AES 算法对其进行解密。 |
| Borpos | 使用 AES 加密数据 |
| **x** | 将 base64 编码的字符转换为 UTF-8 编码的字符串。 |
| **xs** | 生成一个随机的 16 个字符的字符串 |

该 PowerShell 脚本使用这些函数来操纵数据，并试图窃取数据。该脚本会写入一个字母数字字符串，谷歌认为这是受害者的标识符%LocalAppData%\config.txt。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/pcgSUGCDdKK3gRukXpicwVcms4jrutMn8wBmFvGhMDmal85JhjPzWZmMfhLKRLut0ep5C9MGEf4pJFiccHr0fzpg/640?wx_fmt=png&from=appmsg)

脚本随后在目录中创建一个名为 Chrome 的新目录%LocalAppData%。脚本在该目录中定义了SessionUrl用于网络通信的主机名。此参数的值是一个hxxps://accurate-sprout-porpoise[.]glitch[.]me，它在函数中被定义为全局参数Borjol。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/pcgSUGCDdKK3gRukXpicwVcms4jrutMn8BKibrb0hSCoR9AcS0D6Pr0dCgPEynh9dzTBr9LflHrhrnY58hFbpbSQ/640?wx_fmt=png&from=appmsg)

脚本随后会收集操作系统相关信息，包括：

* 操作系统
* 计算机名
* Token (GILNH9LX6TCZ9V8ZZSUF) - $configtxt

  参数中指定的值。

然后，这些数据会被传递给 Borpos 函数进行加密，之后通过 POST 请求发送到目标域hxxps://accurate-sprout-porpoise[.]glitch[.]me。密钥即为值kNz0CXiP0wEQnhZXYbvraigXvRVYHk1B，初始化向量 (IV) 使用 xs 函数创建。脚本还会添加一个标头Content-DPR，用于存储 IV 值。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/pcgSUGCDdKK3gRukXpicwVcms4jrutMn80KgAHWY4Vvibn09s7aM6Hwlc93VzEpmy7puE0pIKmY1P4EvH0bGxh4w/640?wx_fmt=png&from=appmsg)

|  |
| --- |
| function xs() {      return  - join ((65..90)  +  (97..122) | Get - Random  - Count 16 | % {          [char]$\_      }  )  } |

恶意软件随后等待C2服务器的响应。如果状态码不是400且响应不为空，则脚本调用Borjoly函数来解码来自C2服务器的响应。数据以¶分隔，包含以下四个值：

+ language
+ Command
+ ThreadName
+ StartStop

![](https://mmbiz.qpic.cn/sz_mmbiz_png/pcgSUGCDdKK3gRukXpicwVcms4jrutMn8O4RqibUIgDn2CALd2oHND5WS4LacMibLpwtgsdnzvCpWRto9MlbU1Jiag/640?wx_fmt=png&from=appmsg)

该命令采用 base64 编码格式。谷歌发现，*$Language*参数将用于执行 PowerShell 或 C# 代码，而*$StartStop*参数将用于下载其他内容、执行或终止命令。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/pcgSUGCDdKK3gRukXpicwVcms4jrutMn8hZ1cIlosnQ6qTUGvSxWicIapWVKyLKQ1iaZM9rsEgJeSF57jrbgrPo2A/640?wx_fmt=png&from=appmsg)

**结论**

TAMECAT 是一款基于PowerShell 的恶意软件，APT42 曾将其用于间谍活动。它经历了多次迭代，不同变种之间存在诸多相似之处。这些相似之处包括在数组中使用 Base64 编码的字符串、使用数组片段生成代码以及 PowerShell 字符串替换和通配符。此外，还观察到 TAMECAT 的开发者使用 Discord 和 Telegram 等平台作为 C2 通信渠道。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/pcgSUGCDdKK3gRukXpicwVcms4jrutMn8Nw1GZEO3ibMF4ArbecuPAOqxicqNdolC8ukQNohE8urnvANhBoxFMV5A/640?wx_fmt=pn...