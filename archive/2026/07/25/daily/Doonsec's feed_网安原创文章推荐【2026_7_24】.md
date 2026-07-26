---
title: 网安原创文章推荐【2026/7/24】
url: https://mp.weixin.qq.com/s/tij1QK2ggxei9r2SyIzqXA
source: Doonsec's feed
date: 2026-07-25
fetch_date: 2026-07-26T05:22:47.861175
---

# 网安原创文章推荐【2026/7/24】

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/CZMNsicRfJADib2CO8zL76ianHXXy1FT7s9rPyuJ9d1sQoyErctojyXpU5awiaJCROFsO9aFtPfnBTKSh5icPxW7TicXDpOgrSYKmHicOYTtSibsjOQ/0?wx_fmt=jpeg)

# 网安原创文章推荐【2026/7/24】

AJay13
AJay13

洞见网安

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

# 2026-07-24 微信公众号精选安全技术文章总览

> 洞见网安 2026-07-24

---

### 0x1 [新型恶意广告攻击:在浏览器里现场组装恶意软件](https://mp.weixin.qq.com/s?__biz=MzAxOTM1MDQ1NA==&mid=2451187797&idx=1&sn=10be81e53cbb8e4b8c8268074191fe22&scene=21#wechat_redirect "新型恶意广告攻击:在浏览器里现场组装恶意软件")

> 黑鸟 2026-07-24 23:28:26

![](https://mmbiz.qpic.cn/mmbiz_jpg/ibO9kiauylaDqxeowUFltlvibNumibKHSibMf5gVicPC94KATUWTQMaN5orVicBdTpnc3aRusBdgSfxxFLRia4vt2bubxQMeBjjkVyxqrflZxoT7DY8/640?wx_fmt=jpeg)

近日，安全厂商Confiant披露了一项名为SourTrade的新型恶意广告活动，该活动自2024年底开始活跃，主要通过冒充知名交易平台和加密货币平台的广告进行引流。与传统的恶意广告不同，SourTrade不在网络上传播完整的恶意程序，而是在受害者的浏览器中本地组装恶意软件，从而绕过了大部分安全检测。攻击者通过创建高度仿真的钓鱼页面，引导用户下载所谓的免费会员、新人奖励等，实际目的是在用户的浏览器中完成恶意软件的组装。这种攻击方式在亚太和拉美地区广泛传播，支持25种语言。攻击过程中，恶意软件的组装分为四个阶段，包括搭建传输通道、获取组装指令、本地拼接和伪装成同源下载。由于恶意软件的组件和组装说明书的传输，以及最终在用户浏览器内存中完成组装，传统的文件哈希和特征码检测手段失效。针对此类攻击，用户应养成良好的上网习惯，警惕不明来源的下载，并通过官方渠道下载软件，以减少受攻击的风险。

恶意软件攻击

广告钓鱼

浏览器攻击

内存执行

安全检测规避

跨平台攻击

社会工程学

技术分析

---

### 0x2 [Fastjson 二次发包实战其实也难以利用](https://mp.weixin.qq.com/s?__biz=MzU3MDg2NDI4OA==&mid=2247492062&idx=1&sn=d963ee2f337e360cc0e21d552ae98973&scene=21#wechat_redirect "Fastjson 二次发包实战其实也难以利用")

> 轩公子谈技术 2026-07-24 19:52:00

![](https://mmbiz.qpic.cn/mmbiz_jpg/16lHuWzRRdvOrsjMsd1IapyTMrjQB2JpepNZZEGWyqGYzGAVc6CpVKMFxQwtXcOsGuTqLB3iao3PhIcy0jiaOEwfNX3gw8dpLdnnaL3ORVhhI/640?wx_fmt=jpeg)

本文详细探讨了利用Fastjson库中的漏洞进行远程代码执行（RCE）的几种尝试和失败原因。文章首先介绍了利用文件描述符（FD）进行“二次发包”的方法，试图通过下载恶意JAR文件到临时文件并利用文件描述符再次加载，但在JDK 8环境下由于临时文件和FD的快速释放而失败。接着，文章尝试通过预测FD偏移量来精确加载恶意类，但由于FD的不可预测性和时序竞争问题再次失败。最后，文章提出直接使用`jar:file`协议指定本地文件路径进行加载的方法，并通过文件上传接口结合路径穿越漏洞成功实现RCE。文章深入分析了每个步骤的原理、失败原因以及关键约束条件，并总结了FD二次发包在实战中不适用的重要原因，包括JDK版本依赖、FD偏移量不可预测、时序竞争无法消除以及盲打带来的副作用。

Fastjson

远程代码执行 (RCE)

Java 安全

SSRF (服务器端请求伪造)

文件描述符 (FD) 利用

类加载器 (ClassLoader)

缓存中毒

JDK 版本漏洞

竞态条件 (Race Condition)

文件上传漏洞利用

---

### 0x3 [msaRAT 技术分析：借用浏览器构建隐蔽 C2 通道](https://mp.weixin.qq.com/s?__biz=MzkyMjM0ODAwNg==&mid=2247488931&idx=1&sn=f228ad8268fa8d13ac1f9c1a0b19d9dd&scene=21#wechat_redirect "msaRAT 技术分析：借用浏览器构建隐蔽 C2 通道")

> TIPFactory情报工厂 2026-07-24 18:26:00

![](https://mmbiz.qpic.cn/mmbiz_jpg/UhfibIyPpmuNz7SGVia3Phmiat99Uro6P3FuB9icNSHEI5ZDqouJMT0sib8ia5RaqmSx34b5R9U6dz7vt4icUrBQ2ZITDGq8FDtHRhEtf6ukreKux4/640?wx_fmt=jpeg)

msaRAT 是 Chaos 勒索软件团伙使用的一种 Rust 远控木马。它最特殊的地方不是又增加了一套自定义网络协议，而是让恶意进程完全避开外网连接：RAT 只与本机浏览器的 Chrome DevTools Protocol（CDP...

---

### 0x4 [红队免杀加载器--Dynloader](https://mp.weixin.qq.com/s?__biz=Mzk0MDczMzYxNw==&mid=2247485851&idx=1&sn=0747ff676dd02b4ec262155db2912599&scene=21#wechat_redirect "红队免杀加载器--Dynloader")

> 安全天书 2026-07-24 18:25:39

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/EYGYnyEdzQVJ99pmvzfNO0ZeItt8Opib5AxuWH3rDNPEfnicd7RzSTOcj6HAj2WX2Mp7dR0ExvXknFUPLMPOkUUsU0yFDOOnUeiaUQiaOT4ffjY/640?wx_fmt=jpeg)

本文介绍了一款名为DynLoader的模块化Windows加载器，该工具专注于规避EDR（终端检测和响应）系统。DynLoader集成了多种技术，包括间接系统调用（Tartarus Gate / Hell's Gate），手动PE解析与分区映射，API哈希与动态解析，以及无文件HTTP交付（支持AES加密选项）。文章强调了这些技术、思路和工具的合法用途仅限于安全测试和防御研究，禁止用于非法目的。文章还提到了一个红队技术交流圈子，分享了一系列相关工具和文章，包括免杀工具、后渗透工具、钓鱼手法、武器化工具等，并邀请读者加入交流学习。同时，文章也警告读者不要利用文章中的信息进行非法测试，并说明了作者不对使用这些信息造成的后果承担责任。

红队攻击

免杀技术

网络安全测试

EDR规避

Windows安全

渗透测试

软件分析

HTTP传输

加密技术

---

### 0x5 [好靶场 | 空验证码参数绕过](https://mp.weixin.qq.com/s?__biz=MzYyMjc0MTIzNg==&mid=2247483872&idx=1&sn=04b09914668a67a8e5da20d054a0f8f3&scene=21#wechat_redirect "好靶场 | 空验证码参数绕过")

> 探玄Geek 2026-07-24 18:10:25

![](https://mmbiz.qpic.cn/mmbiz_jpg/FfcQhWeOnVgOJwJsLowBibuQ1CBCICzXo8VHqIic2IhAy42ibeDV4hFBmNoy15GpE6QRVpEY7ribicNcnwSUdUYSzPdqdbEIAPZw2cAudrE8vnBQ/640?wx_fmt=jpeg)

使用空参数绕过登录验证码限制

---

### 0x6 [Wordpress7.0 wp2shell 未授权RCE（CVE-2026-63030 / CVE-2026-60137）](https://mp.weixin.qq.com/s?__biz=MzkwNzMyNjU0MQ==&mid=2247484346&idx=1&sn=749018d8cbde606a72975d9cdadd6915&scene=21#wechat_redirect "Wordpress7.0 wp2shell 未授权RCE（CVE-2026-63030 / CVE-2026-60137）")

> LR的安全自留地 2026-07-24 15:59:43

![](https://mmbiz.qpic.cn/mmbiz_jpg/gIBYXIMwxtsw3qOEqhQeJq1hdXWZDlXkyS6kseew47vg1ZOmZiaOqwdsPPO830BeACMUBKTcE4PequrveibXB5JJSkxRgxhLVmM7ic2VCCO9yk/640?wx_fmt=jpeg)

2026年了，在AI时代下总感觉什么都有可能，但是看到Wordpress居然能有原生未授权RCE还是感觉不可思议

---

### 0x7 [工具更新｜DDDL v1.1.1 功能更新 追加 POC](https://mp.weixin.qq.com/s?__biz=MzkwOTUwMTc1OA==&mid=2247484587&idx=1&sn=2e9ce5ff4689c644a844b17229af7620&scene=21#wechat_redirect "工具更新｜DDDL v1.1.1 功能更新 追加 POC")

> 迷人安全 2026-07-24 15:28:24

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/Oiag47y540y90iaMqw6ibMbIOTC1KrqLulVYkLkIbp7uNG1POSibk0frq3DwOdKNe8NWL0JfZa3RZibqNA9nzcK3MvicssQMy9HBs12buR9GTgdVg/640?wx_fmt=jpeg)

工具更新｜POC 更新到 5430 workflow 更新至 1931 指纹近 2w

---

### 0x8 [Bread 域渗透靶机](https://mp.weixin.qq.com/s?__biz=MzYzNjQzNTI4OA==&mid=2247489040&idx=1&sn=f46fbaf879adcf162bff68f842892bb7&scene=21#wechat_redirect "Bread 域渗透靶机")

> Serendipity的小屋 2026-07-24 13:59:41

![](https://mmbiz.qpic.cn/mmbiz_jpg/T5C6icTcSx9Micmvc027KTdmKeUdvkLiaM86ZTn2iaymlP0laQII9X9AWJ5jFic7Y5AhIUICC6P3bYu3P30Vkk7MgCYXibR9lXzWzy7aZXKupAKmg/640?wx_fmt=jpeg)

继续学习📖

---

### 0x9 [谷歌凭证钓鱼网站 - 冒充谷歌登录页面](https://mp.weixin.qq.com/s?__biz=MzYzOTMyNTUzNw==&mid=2247485479&idx=1&sn=0e4aa5eec9fe155e665d107da6cfafdd&scene=21#wechat_redirect "谷歌凭证钓鱼网站 - 冒充谷歌登录页面")

> 威胁情报Z分析 2026-07-24 12:55:01

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/0LGiaGIrzXuk0X5Iiac2UVQtNwiaTIQDKMCa6LOJA0K4jAErWvzVzQpkJjy3GGX5jHINkiaq0GiasTDo6JrE7tRPzH8nkhBxCKsNiabicCniaicXo1X4/640?wx_fmt=jpeg)

该网站收集受害者的电子邮件地址，然后重定向到密码页面，并似乎支持第二阶段验证（verify-code.php）

---

### 0xa [靶场SQL注入篇(下):sqli2 Base64 绕过 + sqli3 登录盲注，补齐 tamper 与 sqlmap 进阶](https://mp.weixin.qq.com/s?__biz=MzI5NDg0ODkwMQ==&mid=2247488177&idx=1&sn=9c113c93378325e86cd9bd330ad60b9c&scene=21#wechat_redirect "靶场SQL注入篇(下):sqli2 Base64 绕过 + sqli3 登录盲注，补齐 tamper 与 sqlmap 进阶")

> 六边形攻防安全 2026-07-24 12:31:00

![](https://mmbiz.qpic.cn/mmbiz_jpg/FaZFJ7xrqJZ584yxnibTPvXYKgO4OOMy8C09QGRLl2VLibCwspKUT3WYSkIXaV04INH3nlTSE3pGjIRZ18pedxFsCd9mOgFhJbsEGokInZuQc/640?wx_fmt=jpeg)

六边形攻防靶场SQL注入篇第三篇 完结篇

---

### 0xb [SharedRoot：剖析Claude Cowork沙箱逃逸](https://mp.weixin.qq.com/s?__biz=MjM5Mzc4MzUzMQ==&mid=2650265773&idx=1&sn=337fc87c1e0647c20bbe071099fc4978&scene=21#wechat_redirect "SharedRoot：剖析Claude Cowork沙箱逃逸")

> 骨哥说事 2026-07-24 09:03:54

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/TKdPSwEibsZiaowwZptJnfOKGX42glV737m3NXJHjdnjvKmNeOy6TBQ5qFpONgzZdaSZe60eeEPOTXzHOEKMugYmic7V4EKZPaBVuMSgHuFFLA/640?wx_fmt=jpeg)

声明：文章中涉及的程序(方法)可能带有攻击性，仅供安全研究与教学之用，读者将其信息做其他用途，由用户承担全部法

---

### 0xc [WordPress 核心级 RCE：为什么这次不是插件背锅？](https://mp.weixin.qq.com/s?__biz=MzU0MzQ2NzIyMw==&mid=2247488622&idx=1&sn=9111f1212cb66da1702dca84ee12e4f4&scene=21#wechat_redirect "WordPress 核心级 RCE：为什么这次不是插件背锅？")

> NowSec 2026-07-24 08:00:00

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/njVhCYJqSqn3lu7icrmUeFOc0sWlic49wyDnJibr9HmcoECnP9lJ9QYcwPKmwic0nkAXuG0RHjbhRNibCXmZibDUocuJ23KWwpXKauVMLBMx7EtwE/640?wx_fmt=jpeg)

wp2shell说明Core漏洞同样会成为入口

---

### 0xd [新型Spirals勒索软件利用IIS Web Shell和PsExec在不到24小时内加密一家IT公司](https://mp.weixin.qq.com/s?__biz=MzIxNDg5ODQxMg==&mid=2247488249&idx=1&sn=50892d546f3f195517090d168f7611d2&scene=21#wechat_redirect "新型Spirals勒索软件利用IIS Web Shell和PsExec在不到24小时内加密一家IT公司")

> 暗镜 2026-07-24 06:00:00

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/zdwoicOrrJb1ibicXgSGe4chwx26OlAv22qWLAnFhRXCtAw0d2gUmiceLJGSgD3D1DzKtRmd4fEh9EPl41Jlsx08A2AuNQAEP8f3o5IPpMzd0lk/640?wx_fmt=jpeg)

2026年6月，一种名为“Spirals”的、此前从未出现过的勒索软件家族袭击了南亚一家IT服务公司。

---

### 0xe [【核弹级】天塌了！CVE-2026-57517 Control Web Panel 盲SQL注入 无需登录直接RCE](https://mp.weixin.qq.com/s?__biz=MzkyMzcyMjgwNA==&mid=2247484307&idx=1&sn=9a179298f52fe99ac96c67444c2a6e49&scene=21#wechat_redirect "【核弹级】天塌了！CVE-2026-57517 Control Web Panel 盲SQL注入 无需登录直接RCE")

> 爱坤sec 2026-07-24 02:30:00

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/uqtLGQlJSxVWciavNSdALyQhDTuibB7CMupaibXsCFgo15eXsmjoKkw07CSLAzf9fBFylKE8U94XIBvhkwNPBKvb6AJNtKwnyrce978xIT81y4/640?wx_fmt=jpeg)

CWP ≤ 0.9.8.1224 未授权盲SQL注入漏洞，CVSS 9.8 核弹级，MySQL root权限写入webshell实现RCE，无需登录直接拿shell
...