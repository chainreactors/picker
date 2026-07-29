---
title: 网安原创文章推荐【2026/7/27】
url: https://mp.weixin.qq.com/s/dIdavNNMbbPSq0h6QBECdw
source: Doonsec's feed
date: 2026-07-28
fetch_date: 2026-07-29T05:02:03.152317
---

# 网安原创文章推荐【2026/7/27】

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/CZMNsicRfJACNSl7HdyHKbmuN9yIgfccLXUtPvkLZMNbZ6NB7kGnw4YibLE5Xia7bZO7Ewtrw6MGwf9a3vPmq4JOc5JnbV09UVqC2euJHeBjbU/0?wx_fmt=jpeg)

# 网安原创文章推荐【2026/7/27】

AJay13
AJay13

洞见网安

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

# 2026-07-27 微信公众号精选安全技术文章总览

> 洞见网安 2026-07-27

---

### 0x1 [内网横向手法汇总](https://mp.weixin.qq.com/s?__biz=MzkwMzQyMTg5OA==&mid=2247489478&idx=1&sn=ee5a7e40b4f620cdf0014abf55691b95&scene=21#wechat_redirect "内网横向手法汇总")

> Heihu Share 2026-07-27 23:05:23

![](https://mmbiz.qpic.cn/mmbiz_jpg/mS3YhqKWBR2lSEfDdYabGibctmROhnTjMSlY327XrMWqm0RDYyrng514VFqpsEVfCF1aO0vcu8NW2xibS13Fs4yRUUpaSLJ1RjU7TWpcPOomQ/640?wx_fmt=jpeg)

本文详细介绍了网络安全学习者进行内网横向移动的各种方式，包括通过远程桌面协议（RDP）、ToDesk、IPC$共享、PTH传递攻击、PTK密钥传递攻击和PTT票据传递攻击。文章深入分析了每种方式的攻击原理、利用条件和操作方法，并提供了相应的工具和命令示例。此外，还探讨了如何使用WMI命令、DCOM接口和WinRM服务进行远程操作，以及如何利用OXIDResolve接口和NTLM SSP进行信息收集和攻击。文章强调了不同用户在不同场景下的横向移动权限差异，并提供了相应的解决方案。最后，文章还介绍了如何利用各种横向移动工具进行C2上线，并提供了相应的实验结果和分析。

内网渗透

远程桌面

远程控制软件

IPC$ 共享

PTH攻击

PTK攻击

PTT攻击

WMIexec

WinRM

SMB协议

命令执行

---

### 0x2 [小记-域渗透工具逆向二开赋予免杀](https://mp.weixin.qq.com/s?__biz=MzkwODg4MDg0NQ==&mid=2247484973&idx=1&sn=bb13782b5dc0088e465fd0599a2c0cc3&scene=21#wechat_redirect "小记-域渗透工具逆向二开赋予免杀")

> UpRoot 2026-07-27 21:38:05

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/KA5KNdck7pdoaGHtn7eJAGHSjkFBiawlrmL6FggYYFFSTF3POVRnbT7AxcUiayqiaNlh1CzsnySrz9BhPhjc8DP6WFU6ic7QPg0fz5od2lBS7BE/640?wx_fmt=jpeg)

本文详细记录了一位网络安全学习者在尝试逆向和修改域渗透工具以实现免杀的过程。作者发现原工具已经不再具有免杀能力，于是通过逆向工程分析了工具的工作原理。作者首先尝试了解密核心代码，但由于解密算法复杂，转而通过IL指令编辑Main方法，将核心代码写入bin文件中。接着，作者尝试了多种方法来加载修改后的程序，但由于使用了域工具组件，无法通过杀毒软件的检测。为了进一步绕过杀毒软件，作者编写了一个自定义加载器，并尝试了多种方法来降低程序的熵，包括使用Base64编码和UUID。最后，作者讨论了如何绕过360云沙箱的检测，包括减少暴露面、禁止生成调试信息、签名和伪装白文件字符串。文章还提供了加载器的代码示例，并邀请读者共同探讨更好的解决方案。

网络安全

逆向工程

免杀技术

沙箱检测

代码分析

C# 编程

Windows 安全

---

### 0x3 [Fastjson 1.2.83 终极 RCE：AutoType 关了也没用？](https://mp.weixin.qq.com/s?__biz=MzkzMTM3ODg3Mw==&mid=2247484043&idx=1&sn=f00bb77e310ba7a0636b37743c44bfc2&scene=21#wechat_redirect "Fastjson 1.2.83 终极 RCE：AutoType 关了也没用？")

> 绿叶 GhostShield 2026-07-27 21:21:01

![](https://mmbiz.qpic.cn/mmbiz_jpg/YP80bMwCiaSDBGAg4gcVaKq7ywslurC0K3jxhVv80jb8DnHpwDe1m51qBBKlAIVtfHBq7Dia4uF3kzEq9mfFiceVnn0L23FZ7aibOH31gWa1TTU/640?wx_fmt=jpeg)

本文深入分析了Fastjson 1.2.83版本中一个绕过所有黑名单、不依赖AutoType的新攻击链，揭示了即使在AutoType关闭和safeMode开启的情况下，攻击者仍可通过特定的JSON解析漏洞远程执行任意代码。文章详细介绍了Fastjson的十年攻防历史，特别是在AutoType关闭后仍存在的安全风险。攻击者利用ASM生成非法类名，并通过Spring Boot FatJar和JDK 8环境远程拉取和执行恶意代码。文章还解释了ASM的使用原因、类名对齐的重要性以及如何通过@JSONType注解绕过安全检查。此外，文章还讨论了为什么RCE攻击在JDK 8上成功而在JDK 9+上失败，以及Spring Boot FatJar的作用。最后，文章提供了开启safeMode作为防御方案的建议。

JSON库漏洞

Java安全

AutoType绕过

RCE漏洞

安全补丁

黑名单与白名单

代码审计

Spring Boot安全

ASM工具

JDK版本差异

---

### 0x4 [Fastjson2 AutoType 哈希校验绕过致RCE分析](https://mp.weixin.qq.com/s?__biz=MzA4NTI4ODQ1Mw==&mid=2247484093&idx=1&sn=64493189e4b8b9e4ced498045a0cae92&scene=21#wechat_redirect "Fastjson2 AutoType 哈希校验绕过致RCE分析")

> 鉴帷安全 2026-07-27 17:37:33

![](https://mmbiz.qpic.cn/mmbiz_jpg/CrThU6KH4h5MVlRhT36AazXowrjRJNz9aibnlkjDIHiaF8LUkqIRd7zgWnXWWb2N6wOhgF06OicqcU65ibHbmicibibYlibicScKD8KffssLl5Ef0pNE/640?wx_fmt=jpeg)

本文详细分析了Fastjson2的AutoType哈希校验绕过漏洞，该漏洞存在于Fastjson2默认配置下未启用SupportAutoType时，由于对通用对象元素开头@type属性的处理方式导致。攻击者可以利用该漏洞通过FNV-1a哈希碰撞技术，使得URL形态的字符串进入应用的类加载器，进而实现任意代码执行。文章中分析了漏洞的关键位置和代码逻辑，解释了如何通过计算特定前缀的哈希值与白名单哈希进行匹配，绕过默认配置的校验机制。同时，文章也提供了漏洞的复现方法、可能存在的利用条件以及长亭给出的修复建议，包括完全禁用AutoType功能、开启SafeMode和配置WAF规则等，以减少此类风险的发生。

JSON处理漏洞

哈希碰撞攻击

任意代码执行

白名单校验绕过

安全配置漏洞

---

### 0x5 [关于 Fastjson2 2.0.62 默认配置风险的几点推测](https://mp.weixin.qq.com/s?__biz=MzI1MDkwNzQ4NA==&mid=2247484717&idx=1&sn=f72705026708c56a4e03ae6b022fc1b5&scene=21#wechat_redirect "关于 Fastjson2 2.0.62 默认配置风险的几点推测")

> MessFreeSecurity 2026-07-27 17:21:40

![](https://mmbiz.qpic.cn/mmbiz_jpg/8qOq10zFicMBnibdsLIhyG25EvkkrnuyL8p01CeLVITUfA4YkKbqofoze1icViaSdjmcWiahe6icZgf6IaFnz6gajUQXrBibLvEiam1m9qlBqgiarZAE/640?wx_fmt=jpeg)

本文分析了Fastjson2 2.0.62版本中可能存在的默认配置风险。通过公开补丁和本地实验推测，问题可能出现在关闭SupportAutoType后，通用Object解析仍可能处理对象首字段@type，并进入类型加载判断。文章指出，旧逻辑在计算类型名前缀的FNV-1a哈希时，似乎没有继续核对真实文本，而默认接受数组中存在一个特定的哈希值，这可能导致攻击者通过构造chosen-prefix碰撞，使URL形态的字符串得到相同哈希，进而进入TypeUtils.loadClass()。文章进一步推测，风险可能来自哈希被当成授权结果和URL/JAR字符串进入ClassLoader的后续链路。尽管公开补丁增加了真实前缀比较，但文章认为这仍然是一个默认配置可以触达的类加载风险，完整的RCE（远程代码执行）仍依赖于多个条件。文章建议在处置上可以先应用包含相同逻辑的修复，临时开启SafeMode，并限制业务JVM的非必要出站访问。

Fastjson 安全漏洞

JSON 解析器漏洞

类加载攻击

Java 安全

默认配置风险

漏洞利用研究

---

### 0x6 [Fastjson2 也没躲过去，默认关闭 AutoType，恶意 JSON 仍可能触发 RCE](https://mp.weixin.qq.com/s?__biz=MzkzNDIzNDUxOQ==&mid=2247508669&idx=3&sn=ad1c78ccaa3a8dc93d61f9729ad13549&scene=21#wechat_redirect "Fastjson2 也没躲过去，默认关闭 AutoType，恶意 JSON 仍可能触发 RCE")

> 独眼情报 2026-07-27 17:09:21

![](https://mmbiz.qpic.cn/mmbiz_jpg/cBGhzWwhSAiaHT3ULliaMVxg1pMwMM5MYXPfaSoI9U5CncNUASibAicenesH0tPNe6u5fm6hdOBVF5we7jrOyVAiaAGaJEU4tolvyJRzNhriaMRnI/640?wx_fmt=jpeg)

7月27日，长亭安全应急响应中心披露了一条Fastjson2远程代码执行漏洞。

---

### 0x7 [Redis 认证后RCE 漏洞 CVE-2026-25589](https://mp.weixin.qq.com/s?__biz=Mzg3NzkwMTYyOQ==&mid=2247491689&idx=1&sn=3c73b2f78ae1cc080e74ac695dbbcf26&scene=21#wechat_redirect "Redis 认证后RCE 漏洞 CVE-2026-25589")

> 不秃头的安全 2026-07-27 16:31:04

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/I2dhkmhKrSbBspHETetfM5QBkvM8zDgcOnj9d3lQ1JfcyA8jBq2VIB1fNbx03ZAfjicw3P9xtPzlxBujVZo9nsfXrsKHIg2jJia9Kph04aCyo/640?wx_fmt=jpeg)

2026年7月，Redis官方发布了两个高危漏洞CVE-2026-25589和QVD-2026-44936。CVE-2026-25589是RedisBloom模块TDigest数据结构的堆溢出，QVD-2026-44936则是Redis Streams消费者组中的一个双重释放缺陷。这两个漏洞都允许攻击者在认证后执行远程代码，以root权限接管服务器。漏洞影响Redis 6.2.22、7.4.9、8.6.4等版本，修复版本为Redis 8.8.0及以上。攻击者只需有效认证密码和特定命令权限即可利用这些漏洞。Redis官方建议升级至最新版本或禁用相关命令来缓解风险。

Redis 漏洞

远程代码执行

高危漏洞

认证后漏洞

堆溢出

漏洞复现

Docker 漏洞

安全漏洞修复

---

### 0x8 [都是草台班子?大多数免费VPN软件存在流量泄露、明文传输和隐私外泄问题](https://mp.weixin.qq.com/s?__biz=MzkxOTUyOTc0NQ==&mid=2247494386&idx=1&sn=2638b44fc7f113f723ddc72e8e451942&scene=21#wechat_redirect "都是草台班子?大多数免费VPN软件存在流量泄露、明文传输和隐私外泄问题")

> 二进制空间安全 2026-07-27 16:21:56

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/lLNNhhDrAC7qEhjgAyYibuJLOvQCuD7K5FGp1aHHA323k2icwXOuOAljVbviaNMia9uXy6tdW928LrLVotqmoWiaUORZxjicGNyhibNe05Yw5KlnaE/640?wx_fmt=jpeg)

VPN安全审计

移动应用安全

隐私保护

网络加密

DNS泄漏

中间人攻击

广告跟踪

安全测试工具

---

### 0x9 [【漏洞通告】Fastjson 1.2.83远程代码执行漏洞（CVE-2026-16723）](https://mp.weixin.qq.com/s?__biz=MzA4NjMwMzI3Mg==&mid=2247505407&idx=1&sn=b4c035e8f98a307541f284d54edb3644&scene=21#wechat_redirect "【漏洞通告】Fastjson 1.2.83远程代码执行漏洞（CVE-2026-16723）")

> 常行科技 2026-07-27 11:03:00

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/r8QjvJibulhS6FTmbFcianVCXaogFkNcM3Y5OiaCvmcbADVlZkLgbzmtZHHvY53EuWLntY3BOPKgB4KLLEibBJpEug/640?wx_fmt=jpeg)

检测业务是否存在此安全漏洞风险影响，请联系常行安服团队！

---

### 0xa [ModHeader插件，正常添加请求头、正常添加分组配置、去后门代码版](https://mp.weixin.qq.com/s?__biz=Mzk0NzQxNzY2OQ==&mid=2247490481&idx=1&sn=2de9df4edc9e58d6ac2048d872d67fda&scene=21#wechat_redirect "ModHeader插件，正常添加请求头、正常添加分组配置、去后门代码版")

> 犀利猪安全 2026-07-27 10:40:00

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/HcG7oBmFdNmNQpdq3O2kcBwgBaHW3HPADtprOaXCZ8obkkkafT89uyVcINLge83Wh68iamrC9PokJknaiabN1A2V4mvYIh6Uzwgk2Bm6CJvyc/640?wx_fmt=jpeg)

本文主要讨论了ModHeader插件的安全性问题。文章指出，ModHeader插件因存在恶意内容被浏览器插件商城下架。作者分析了插件可能存在的后门代码，并提供了替代品。同时，作者还分享了修改后的去后门代码版插件，并详细说明了如何下载、解压和配置使用该插件。文章强调，使用这些插件仅限于授权测试或学习，禁止用于非法测试或攻击。此外，文章还提到了一些与网络安全相关的资源信息，包括文库账号和交流群信息。

网络安全工具

插件安全

恶意代码分析

安全测试

浏览器安全

---

### 0xb [WebSocket 实战：基于协议特点的漏洞挖掘](https://mp.weixin.qq.com/s?__biz=Mzg3OTcxMjE2NQ==&mid=2247488006&idx=1&sn=f4380963e5a82f6e8817dc579b43d126&scene=21#wechat_redirect "WebSocket 实战：基于协议特点的漏洞挖掘")

> 逐影安全 2026-07-27 09:20:00

![](https://mmbiz.qpic.cn/mmbiz_jpg/l1kc4UTvhuqRHdRQaLCCLykYEp3ibkzLuqzh7E1cRbg3lWl9FljKVoXJic0W0Oricw23ica0ggLeOBeJE1u46VxF3wcg4lfklcRjH5PicmnCtBFM/640?wx_fmt=jpeg)

---

### 0xc [GitLab爆高危漏洞！普通用户一步到\"root\"，已有PoC流出](https://mp.weixin.qq.com/s?__biz=MzAxMjE3ODU3MQ==&mid=2650620453&idx=4&sn=45f648df82da932603459fbbd5268494&scene=21#wechat_redirect "GitLab爆高危漏洞！普通用户一步到\")

> 黑白之道 2026-07-27 08:42:00

![](https://mmbiz.qpic.cn/mmbiz_jpg/nGzNudUIJ6Mjocc2Jib1ExvVHuAdXGlCFDJOOwYryyBjPzDAOREY4bPJfylGLV5vsvuOrT36AMEqRqYc35eZTtefxfYSWvuY9RjQk7yLvx7M/640?wx_fmt=jpeg)

导语：2026年7月24日，安全公司depthfirst正式公开了GitLab一个高危认证...