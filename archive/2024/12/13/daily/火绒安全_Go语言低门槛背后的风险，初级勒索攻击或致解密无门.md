---
title: Go语言低门槛背后的风险，初级勒索攻击或致解密无门
url: https://mp.weixin.qq.com/s?__biz=MzI3NjYzMDM1Mg==&mid=2247520892&idx=1&sn=a3fd4dfff2b54bba0430406cb4a2c170&chksm=eb704c43dc07c555019e4e75070fba7f1123bb9e663e66f663545bb3c34afe467384b8496b6e&scene=58&subscene=0#rd
source: 火绒安全
date: 2024-12-13
fetch_date: 2025-10-06T19:39:24.452035
---

# Go语言低门槛背后的风险，初级勒索攻击或致解密无门

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/0icdicRft8tz4of5IyAQPS7NZu3ywIXU478j6MmX9TjtBNrVAbibfG01kA0YfjVNxzZqVBmRBP0h0zvibYU8zoqatQ/0?wx_fmt=jpeg)

# Go语言低门槛背后的风险，初级勒索攻击或致解密无门

火绒安全

火绒安全

# ![](https://mmbiz.qpic.cn/sz_mmbiz_gif/0icdicRft8tz4nrnOI1emtFr0UYnrLKytAvy2gia6ZuIUJs14h2pEIwpiaWPCTTuCQIDibx9dlfXoyrNyVEWb8DVUUA/640?wx_fmt=gif&from=appmsg)

Go 语言凭借其高效的并发处理能力和强大的标准库支持等特点，在开发效率和性能上具有一定的优势，备受软件开发者青睐。然而，这种优势也吸引了部分初学者以及勒索组织的目光，他们利用 Go 语言编写勒索病毒并进行传播，催生了各种基于 Go 语言的勒索实验样本和勒索组织样本。

近期，火绒工程师在日常关注安全动态时发现一个基于 Go 语言的勒索样本。分析发现，该样本会利用 AES 进行数据加密，并将加密秘钥发送至 youtube.com ，导致被加密文件完全无法恢复。推测该样本属于基于 Go 语言勒索样本中的实验样本。随后对基于 Go 语言的勒索样本进行调查分析发现，实验样本在该类勒索样本中较为常见，而勒索组织样本除了勒索步骤比较完善，使用的技术手段与实验样本仍有一定相似。火绒安全产品可对上述勒索木马进行拦截查杀，请广大用户及时更新病毒库以提高防御能力。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/0icdicRft8tz4of5IyAQPS7NZu3ywIXU47AMKgvxlicbjf0XLib75r3RBszoNbDu6w1IuDNEUCPJujuI6OsQ6YRvOQ/640?wx_fmt=png&from=appmsg)

查杀图

勒索病毒通常是黑客攻击链的最后一个环节，属于直接可以获利的病毒。在前期攻击中，黑客已将目标环境改造成可以执行任意程序而不被检测的状态。因此， 基于 Go 语言的勒索病毒无需采用免杀等特殊技术手段，便能直接进行加密和上传操作。本文将主要对勒索实验样本以及勒索组织样本分别进行简要分析。基于 Go 语言的勒索样本进行勒索的步骤概括流程图如下：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/0icdicRft8tz4of5IyAQPS7NZu3ywIXU47ktwtzlXGMfHzCFMia0NsDrQTySr9MSvk9srZye5ppD9nCIuH4riaRMVA/640?wx_fmt=png&from=appmsg)

基于 Go 语言的勒索样本进行勒索的步骤概括

**一**

**样本分析**

基于 Go 语言的勒索样本经常利用到的库函数按照使用先后顺序排列，有以下几种：

* crypto/rand.Read：获取随机数
* path/filepath.Walk：遍历文件
* crypto/aes.NewCipher：初始化 AES 加密器
* os.WriteFile：写勒索信或者将加密数据写入原文件
* encoding/json.Marshal：转化为 JSON 字符串
* net/http.Get/Post：接收或发送数据
* os/exec.Run：打开勒索信

###

### **勒索实验样本**

一些初学者或第一次开发勒索病毒的作者可能会制作出实验样本，这类样本的特点为勒索步骤不完整，例如缺少勒索信、勒索信无意义，或在对称加密过程中未能上传必要的数据等，最终导致受害者的数据无法被恢复，除非能够在内存中及时捕获密钥或在用户界面中获取相应密钥。而对于采用 RSA 非对称加密的样本，只有在私钥被保存至本地的情况下，才有可能实现数据恢复。

此次发现的勒索样本（下称 A 样本）即为实验样本，由于该样本最终将秘钥和用户标识符等数据发送至  youtube.com ，使得被加密文件无法恢复。此外，本文还将对同类型样本 B 和 C 进行简要阐述，展示实验样本的大致步骤和勒索信的无意义。

#### **A 样本**

A 样本调用 crypto/rand.Read 函数生成 1 字节的随机数，并通过计算从 a-z、A-Z 和 0-9 的字符集中选取一个字符，循环此操作九次，生成一个长度为 9 的 UserId 字符串，用于识别用户。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/0icdicRft8tz4of5IyAQPS7NZu3ywIXU47IgS818sII5TuGoPO3VG6eibbibgJvxzOa4ZDUgNyZgg16ys7RZ6yDE8Q/640?wx_fmt=png&from=appmsg)

获取随机 UserId 字符串

随后，使用一个 32 字节的随机密钥和 AES 加密算法，对 C:\Users 文件夹下的所有文件进行加密。加密完成后，创建以 [源文件名].mtxv21 命名的加密文件，并删除源文件。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/0icdicRft8tz4of5IyAQPS7NZu3ywIXU47Hm4P19u688lQicmiaibiaFCp4Wq3QQfu1EZj0Lv5IJpL1JRB02e9aej5BQ/640?wx_fmt=png&from=appmsg)

加密 Users 目录

还原后的加密算法如下。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/0icdicRft8tz4of5IyAQPS7NZu3ywIXU47odSvnLaouILjt68D5NGuBxYt5cHMjTK4n7fkjLqtZMw2J8whGtOqug/640?wx_fmt=png&from=appmsg)

AES 加密算法

接着，将 UserId 、加密目录以及 32 位加密秘钥通过 JSON 数据发送至 youtube.com 。这一操作使得勒索病毒的作者无法获取加密密钥，因此他们无法解密被加密的文件。即使受害者支付赎金也无法成功恢复数据。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/0icdicRft8tz4of5IyAQPS7NZu3ywIXU474X9VibGRaGYmUQOgBrhxmsTc4VdNprNxzDhNatxeibLJ0UibBnbwD15KQ/640?wx_fmt=png&from=appmsg)

发送 JSON 数据至 youtube.com

该 JSON 数据的内容格式与 Discord Webhook 请求体完全一致。如果将目标 URL 替换为  Discord Webhook 链接，那么信息将直接被链接指向的频道接收。在后续处理中，可以通过 ID 分辨用户，并利用加密目录和加密秘钥对加密文件进行恢复。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/0icdicRft8tz4of5IyAQPS7NZu3ywIXU47EHqdpXL2GePwooW7uw3Rm51f5lLia0QYXRtMaSZ2qGacmwXJwbn2F4w/640?wx_fmt=png&from=appmsg)

JSON 数据

其中的部分 JSON 数据键说明如下：

* avatar\_url：Webhook 消息的头像 URL
* embeds：嵌入对象
* fields：额外数据数组

在测试过程中存在桌面变黑的现象。分析发现，在 Win10 系统中，桌面背景图通常保存在

C:\Users\Administrator\AppData\Roaming\Microsoft\Windows\Themes\TranscodedWallpaper 路径中，该路径文件被加密则会导致桌面变黑的现象发生。

最后，该样本会打开勒索信 README-NOW.txt ，其中显示的 Your ID 即是 UserId。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/0icdicRft8tz4of5IyAQPS7NZu3ywIXU47CYwWXgVWdClD6ibV9bujh8a3JhC6C8D6Ik1libianurkx0QZYNaZBE0PQ/640?wx_fmt=png&from=appmsg)

勒索信

#### **B 样本**

B 样本首先获取随机 32 字符秘钥和 16 字符初始化向量。随后利用 AES 算法的 CFB 加密模式对文件进行加密，并且在该过程中并未保存秘钥。加密完成后，将当前文件移动至临时目录中，同时打开名为 readme.txt 的勒索信，但该勒索信中的内容并没有意义。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/0icdicRft8tz4of5IyAQPS7NZu3ywIXU47F75otg5AqJNvkwO0nhT4iaib8wMcacc3ydLaRxUbZLqfShGmxtYcyU6w/640?wx_fmt=png&from=appmsg)

获取随机秘钥和初始化向量

![](https://mmbiz.qpic.cn/sz_mmbiz_png/0icdicRft8tz4of5IyAQPS7NZu3ywIXU47GpiaBibKNCllE6EnFH5u8Cu0OyJQslNcpUEox1xmNslrqsicu2UvUP44g/640?wx_fmt=png&from=appmsg)

AES 算法 CFB 加密模式加密

![](https://mmbiz.qpic.cn/sz_mmbiz_png/0icdicRft8tz4of5IyAQPS7NZu3ywIXU472Ak9qgzzkRZHzzqthAU6DbIdh9fu80FBbfvhqL1BcEtYFicpk29sibiaQ/640?wx_fmt=png&from=appmsg)

移动至临时目录

![](https://mmbiz.qpic.cn/sz_mmbiz_png/0icdicRft8tz4of5IyAQPS7NZu3ywIXU47P9wIxhwxQYjzZbAEHffEhrW5ggic1QnabGPXH4BUCMULxfUdrAphGHQ/640?wx_fmt=png&from=appmsg)

readme.txt

#### **C 样本**

C 样本首先获取 Desktop、Documents、Pictures 目录路径。随后获取随机秘钥，同时利用 RC4 算法将获取的目录下的文件进行加密。在加密过程中，将生成的秘钥保存至 C:\Users\Administrator 目录下。加密完成后，将勒索信创建在用户桌面上。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/0icdicRft8tz4of5IyAQPS7NZu3ywIXU472bOSz3OGh9ZX6hVxAO4G4L3KjB0VVNKHMD6muSWicqtC55pvTeaHZ3g/640?wx_fmt=png&from=appmsg)

获取目录路径

![](https://mmbiz.qpic.cn/sz_mmbiz_png/0icdicRft8tz4of5IyAQPS7NZu3ywIXU47eUUM59QUcTHA2Qapibvj5PMictGXkLyyxMkQ7zkDNf1PnY05y2PHcKkw/640?wx_fmt=png&from=appmsg)

RC4 加密

![](https://mmbiz.qpic.cn/sz_mmbiz_png/0icdicRft8tz4of5IyAQPS7NZu3ywIXU4772Ficpu3kYeLtOQQOkHomSSM8oUoeYTTzTnAWjPP4ohThzhfWZGqmBA/640?wx_fmt=png&from=appmsg)

秘钥和勒索信

### **勒索组织样本**

与实验样本不同，勒索软件组织样本的勒索步骤完整，能够实现完整的勒索以及恢复的操作。除此之外，此类样本还具有获取系统信息、上传文件以及持久化等操作，但其主体逻辑还是对文件进行加密。

#### **LAPSUS$ 组织样本**

LAPSUS$ 组织样本首先通过向  hexalockbeta.000webhostapp.com/index.php 发送 GET 请求以获取用户信息。获取的信息如下：

* computername：利用 os.Hostname 获取电脑名。
* hwid：利用 wmic csproduct get UUID 获取计算机的唯一标识符。
* ip：默认 192.168.1.1
* method：默认 new
* password：30 字符随机秘钥

![](https://mmbiz.qpic.cn/sz_mmbiz_png/0icdicRft8tz4of5IyAQPS7NZu3ywIXU47yCDRiam1XVEOnmmSiaV6ibwaXgUjg2ULrm1Hzicl4vNibHotNl0pf2IpKKw/640?wx_fmt=png&from=appmsg)

发送 GET 请求

随后进行数据上传，并通过 Discord Webhook 将文件压缩包发送至指定 URL  https://discord.com/api/webhooks/1258768913898930306/rctIsQgwuuUEsHdFMdgzuCDXzgtpFv\_yKz1aGVa6xKXzqJpTLz5Gv8DxuaSOK\_z\_Z-Eb 中。压缩包内包含 Desktop、Documents、Downloads、Pictures、Music、Video 等目录下的文件。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/0icdicRft8tz4of5IyAQPS7NZu3ywIXU47mQ74yzHibjqrUHLHkFTM4kJpaulQVIeG12NBjtPxN9TKiaQPuznX5LQA/640?wx_fmt=png&from=appmsg)

压缩文件夹

接着生成随机秘钥和盐值，通过 pbkdf2 算法生成 32 个字符秘钥后，利用 AES-GCM 模式对 C:\Users 目录进行加密。最后打开勒索信。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/0icdicRft8tz4of5IyAQPS7NZu3ywIXU477l4UicB35n794neicBg5ibgSaCmicxAMvlZq4D9H9dnGsoQglFMIMnLaEg/640?wx_fmt=png&from=appmsg)

加密

![](https://mmbiz.qpic.cn/sz_mmbiz_png/0icdicRft8tz4of5IyAQPS7NZu3ywIXU479P3Lu3YUY6jE3UZoauC97wnMqYQge85w2k0XV0aljqgbmouuG4Tm1w/640?wx_fmt=png&from=appmsg)

勒索信

#### **GhostLocker 组织样本**

GhostLocker 组织样本首先会将自身复制到开机自启目录中。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/0icdicRft8tz4of5IyAQPS7NZu3ywIXU47mIl2bAC1ib6eW4ibTF5Nvs2QCJCwuTSXPcojMUjRWGoXVBfwSVPaiaH2A/640?wx_fmt=png&from=appmsg)

复制文件

接着，获取随机 32 字节秘钥，并通过 POST 请求将 JSON 数据发送至 http://94.103.91.246/addInfectioncrypto/aes 。JSON 数据中的有效字段为 id 和 key，其中，id 用于识别被勒索的受害者，而 key 用于后续文件的解密。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/0icdicRft8tz4of5IyAQPS7NZu3ywIXU47nwQcJicn4QfPhwwr1M8PshsETu25rTpvTFwXiaZdgK0qeJ38OejvnpxA/640?wx_fmt=png&from=appmsg)

发送 JSON 数据

随后，通过 AES-GCM 模式以及随机 32 字节秘钥对 C:\ 目录进行加密，在加密过程中会避开 Windows 文件夹。最后打开勒索信。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/0icdicRft8tz4of5IyAQPS7NZu3ywIXU47wZ5rOiaEoNoWQIVY6KiaaG1DGFBo8RFmk49t52r9IIWHtoI2HIcpnSeg/640?wx_fmt=png&from=appmsg)

AES-GCM 模式加密

![](https://mmbiz.qpic.cn/sz_mmbiz_png/0icdicRft8tz4of5IyAQPS7NZu3ywIXU47IoHWDd5UdbADqb2wAw7lUZTYDqHf9lWVibvTCeooHls19eqicH8AVd1A/640?wx_fmt=png&from=appmsg)

勒索信

同时我们发现，近年来基于 Go语言的勒索样本整体趋于工具化。其主体逻辑与加密器相似，主要通过基础函数来实现文件的遍历、加密、上传以及展示勒索信等操作。后续，我们将会持续关注基于 Go 语言勒索样本的发展动态，以应对该类勒索病毒的各种变化，提高火绒安全产品的查杀率以及防护能力。

**二**

**附录**

**HASH：**

![](https://mmbiz.qpic.cn/sz_mmbiz_png/0icdicRft8tz4of5IyAQPS7NZu3ywIXU477icyPKvmLDCy2YTQficWWxWH8ic0M80Q1VMI0IQKXJnA79gwgVW7QpZgw/640?wx_fmt=png&from=appmsg)

**讲点大白话**

有的小伙伴表示没有学过计算机知识，看不太懂这篇文章，那么你可以参考如下说明。

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/0icdicRft8tz6uZOjK6DcBJU9WZic2RZWq4ibT09BcicxZNpic1X8JsvdbAhicPbCWF3NYEFcHzFq2XbfsGyibLDaOKHWA/640?wx_fmt=gif&from=appmsg)

计算机星球里有一个大仓库，生活在这里的居民...