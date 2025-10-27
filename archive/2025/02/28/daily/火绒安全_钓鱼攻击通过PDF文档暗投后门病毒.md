---
title: 钓鱼攻击通过PDF文档暗投后门病毒
url: https://mp.weixin.qq.com/s?__biz=MzI3NjYzMDM1Mg==&mid=2247524506&idx=1&sn=d74006a215de392a907da006f6e67d8b&chksm=eb70bea5dc0737b315d222238d0b2f4abb4114ef928bd7245d962ed1474b2163b423c6ae796b&scene=58&subscene=0#rd
source: 火绒安全
date: 2025-02-28
fetch_date: 2025-10-06T20:38:51.998758
---

# 钓鱼攻击通过PDF文档暗投后门病毒

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/0icdicRft8tz4uRvLNHJQ8Z1TtXVK15YefMb4sJS8VMrltxn8Ppu7sAgWovBg6AnfDUKB1nEC3B9Zwd2czyFMXPw/0?wx_fmt=jpeg)

# 钓鱼攻击通过PDF文档暗投后门病毒

原创

火绒安全

火绒安全

# ![](https://mmbiz.qpic.cn/sz_mmbiz_gif/0icdicRft8tz4nrnOI1emtFr0UYnrLKytAvy2gia6ZuIUJs14h2pEIwpiaWPCTTuCQIDibx9dlfXoyrNyVEWb8DVUUA/640?wx_fmt=gif&from=appmsg)

钓鱼攻击是一种高度隐蔽且极具欺骗性的网络威胁，攻击者通过伪装成银行、保险公司、税务机构或其他可信机构的官方文件，诱导受害者点击下载恶意文件。而在生活和工作中，电子文档作为常用工具，可能也不会让我们“心生防备”。因此电子文档可以成为网络钓鱼攻击的常用媒介，攻击者可以通过表象的“电子文档”来掩盖快捷方式和隐藏文件夹实际的恶意行为，并且电子文档的复杂性和灵活性也导致恶意代码潜藏很深，难以被普通用户察觉，令个人和企业面临财务损失和数据泄露的风险。

近期，火绒威胁情报中心检测到恶意钓鱼PDF样本攻击量增多，且个别样本通过伪装成快捷方式和隐藏文件夹的方式进行传播。经火绒工程师分析，该木马程序采用双重攻击机制：一方面通过VBS脚本执行Python加载器，另一方面利用“白加黑”技术执行恶意文件，最终部署Cobalt Strike远控后门。建议日常可以通过关注可疑的发件人地址、不寻常的链接或过于紧急的要求来规避此风险。同时技术防护手段也不可或缺，如安装可靠的安全软件，对邮件和文件进行实时扫描和检测，监控异常的网络行为。目前，火绒安全产品已具备对该类恶意钓鱼PDF样本的精准识别与拦截能力，能够有效保障用户系统安全。为了进一步增强系统防护能力，火绒安全建议广大用户及时更新病毒库。这将确保您的系统能够抵御最新威胁，防范潜在安全风险。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/0icdicRft8tz4uRvLNHJQ8Z1TtXVK15YefNaAukdoTrvFayPmOvnMKSOUTPW3rrZbpyqX6UIAhEcTQr6aTS98ZDw/640?wx_fmt=png&from=appmsg)

查杀图

样本执行流程图如下：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/0icdicRft8tz4uRvLNHJQ8Z1TtXVK15YefFsk6BnGpFaXY9ibFHpBO6jKpxt3rNickNfNibmDavRExiaRovD3wdv8Jow/640?wx_fmt=png&from=appmsg)

流程图

**一**

**样本分析**

**Loader动静态分析**

该样本的初始传播载体是一个压缩包文件，其中包含被设置为受系统保护的隐藏文件夹（**+s +h**），能够利用快捷方式文件和隐藏的文件夹进行恶意钓鱼攻击。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/0icdicRft8tz4uRvLNHJQ8Z1TtXVK15YefHNkLY57jlzBcwUFZ2Hw2XrHLPLWAJibmsDBpU2xohvMcTkHEAibvRILA/640?wx_fmt=png&from=appmsg)

木马快捷方式利用

![](https://mmbiz.qpic.cn/sz_mmbiz_png/0icdicRft8tz4uRvLNHJQ8Z1TtXVK15YeflYLgJm3Siao3iadpnNGUW6uwCy9G2CUgaa6K0qWicePRqmt7wp4rhp4ibA/640?wx_fmt=png&from=appmsg)

默认隐藏受保护文件

![](https://mmbiz.qpic.cn/sz_mmbiz_png/0icdicRft8tz4uRvLNHJQ8Z1TtXVK15YefibKVHYNPtpH6tPFHFvoZIekPlgJAYspuKOZQlD8iarjC73cJCquNiaZQw/640?wx_fmt=png&from=appmsg)

显示木马文件夹

首先，样本通过隐藏的快捷方式文件触发WScript.exe，以执行文件夹中的恶意libmultiprocessing.vbs脚本。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/0icdicRft8tz4uRvLNHJQ8Z1TtXVK15Yef2v1pka5CsoicpAtElj5ibSNxL04emr3VYIvIvW4OQdNgKmIC72rYzcVQ/640?wx_fmt=png&from=appmsg)

执行恶意脚本

随后，通过该脚本获取当前目录并加载木马程序。具体执行流程如下：

1. **调用Python加载Shellcode**：首先，此脚本利用系统内的Python环境执行Python Loader。随后，利用Python Loader加载并执行一段Shellcode。该Shellcode用于实现后续操作中木马程序的下载与执行。
2. **利用默认程序打开PDF**：为了掩盖其恶意行为，此脚本会调用默认程序打开样本文件中的PDF文件，诱导用户认为当前操作处于正常状态。
3. **启动白加黑木马**：接着，此脚本进一步执行“白加黑”木马（即VMwareXferlogs.exe文件）。随后，该木马利用合法程序加载恶意DLL，以绕过安全软件的检测。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/0icdicRft8tz4uRvLNHJQ8Z1TtXVK15Yefyyc7v3hkHQqA38uY3SUEHx9UILRJoJTreJ1MnOzzuiaLU86McI9AKzw/640?wx_fmt=png&from=appmsg)

libmultiprocessing.vbs脚本

对其中的Python Loader进行分析发现，该Python Loader的核心功能是将整个Python程序打包进压缩包，并通过RC4对Linsce文件中的恶意代码Shellcode进行解密与内存加载。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/0icdicRft8tz4uRvLNHJQ8Z1TtXVK15YefpC7jfeNXvDHfLYBhtWnHI9XegQicc53H02p8nYObylsibmdVK8hJzUDA/640?wx_fmt=png&from=appmsg)

Python程序打包

![](https://mmbiz.qpic.cn/sz_mmbiz_png/0icdicRft8tz4uRvLNHJQ8Z1TtXVK15Yef1oDBo0CVDt9usfLDknjuxZJlQa7KWuxziaCiaG994fUmELIaEUyWYn4g/640?wx_fmt=png&from=appmsg)

内存加载恶意代码

随后，解密恶意代码Shellcode并写入文件。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/0icdicRft8tz4uRvLNHJQ8Z1TtXVK15YefYdE5NLToa5Pdeiax1WiaaVm6RXjAz6ibCBJgqDyHgRtSOPFKFytJPWBWg/640?wx_fmt=png&from=appmsg)

解密恶意代码

该恶意代码使用自修改代码（SMC）技术，通过动态调试，将解密后的程序从内存中重新转储（dump）。

对转储后的恶意代码进行分析发现，其首先会对PE文件进行修复，随后将PE代码加载到内存中以实现恶意行为。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/0icdicRft8tz4uRvLNHJQ8Z1TtXVK15YefCTWTgjAsRckCQ5rq1ErFwKQz1I9ic2bibPAfwD94PRSC6aL4dIWmicFZg/640?wx_fmt=png&from=appmsg)

修复PE

对内存中的PE文件转储（dump）进行分析发现，其为重写版的Cobalt Strike木马。对VMwareXferlogs.exe白加黑样本进行分析发现，其同样为重写版的Cobalt Strike木马。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/0icdicRft8tz4uRvLNHJQ8Z1TtXVK15Yef6MJ8L8dt2vKiajFicLy3LN1TCDYKECE5ibXBUQwCbia1oIZmIBBnjood8g/640?wx_fmt=png&from=appmsg)

BOF API

![](https://mmbiz.qpic.cn/sz_mmbiz_png/0icdicRft8tz4uRvLNHJQ8Z1TtXVK15YefmFW5dTnNZ1LHyTgUPE5pF4W8CKMN7ibBq5kzicMFeOBH9UbqOGYW4DLg/640?wx_fmt=png&from=appmsg)

反射内存加载

**后门分析**

对Cobalt Strike后门进行分析发现，该后门首先判断系统时间是否达到2025年1月16日。若当前系统日期在2025年1月16日之前，则继续执行代码；否则将退出进程。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/0icdicRft8tz4uRvLNHJQ8Z1TtXVK15Yef3SicWvdTULoPuA8Uphk8Z9qNF1qrrAJ6QE6jXawMxIFh7cnRlDeMU5Q/640?wx_fmt=png&from=appmsg)

时间判断

接着，获取系统信息，并利用RSA与AES加密算法对这些信息进行加密，之后发送心跳包。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/0icdicRft8tz4uRvLNHJQ8Z1TtXVK15YefaEburdV1U6kWBrTtgV9ibENfr5xgIt8rGQElQAYK0ctyHdJvKgjgu6g/640?wx_fmt=png&from=appmsg)

设置加密算法

![](https://mmbiz.qpic.cn/sz_mmbiz_png/0icdicRft8tz4uRvLNHJQ8Z1TtXVK15YeffnCvFe0h5xQY1YEqiczlGqpY60kW2p732OmsIIibJoZt2O7ZH5ibicm20g/640?wx_fmt=png&from=appmsg)

获取系统信息

![](https://mmbiz.qpic.cn/sz_mmbiz_png/0icdicRft8tz4uRvLNHJQ8Z1TtXVK15YefWib7PLL4mBooYKFiaTM3lV6iax6UHfIuVmSibyvEkuqjMiaApHcvdNxvbqQ/640?wx_fmt=png&from=appmsg)

数据加密

随后，通过字符串解密(减去7和乘以16)算法解密配置信息。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/0icdicRft8tz4uRvLNHJQ8Z1TtXVK15YefLzBWS2uQRfS2gB37gz2icwvNcBYWtJLibeicrlE2Ak6L4c8mgiaFibjy4aA/640?wx_fmt=png&from=appmsg)

字符解密算法

![](https://mmbiz.qpic.cn/sz_mmbiz_png/0icdicRft8tz4uRvLNHJQ8Z1TtXVK15YefX0vVn2wxE3dng7GD5cWEAp0mklLsl4hpkrp87ZicMu71mZxom8BQa5Q/640?wx_fmt=png&from=appmsg)

解密配置信息

之后，发送数据，接收回传数据，进行任务处理。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/0icdicRft8tz4uRvLNHJQ8Z1TtXVK15YefhMAibx2ht3YZGqgZaO35ksZ06SlgPCsf84owrFy4ic7v6t0U9alQykvA/640?wx_fmt=png&from=appmsg)

任务处理

该后门功能如下：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/0icdicRft8tz4uRvLNHJQ8Z1TtXVK15Yefk3efMT1SZJOf2gqn4jgic4NgL5mjmcBF29POTOVOCARDwrTIzpwZSOQ/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/0icdicRft8tz4uRvLNHJQ8Z1TtXVK15YefgaZW4FM8x5fZp1Kic7RvhQiaVwOAdeYQibj4YhtYH9he99r57eWcrvX9w/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/0icdicRft8tz4uRvLNHJQ8Z1TtXVK15YefyPqZh14Mf4XKLCiayHfN99DoL9UiaDYXxWDv3nNGbN71nosht0UFW69A/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/0icdicRft8tz4uRvLNHJQ8Z1TtXVK15YefXRauickpGfDTP39HHfXGgDjI7YTqRzgvsFUn1dkSw7YQyqZSCHlCbSw/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/0icdicRft8tz4uRvLNHJQ8Z1TtXVK15YefwiaIniaHsmUPRoouuNNVBTQ7DQA10WuFpL4CKPJ8D0NYrEeAdqbPdWrQ/640?wx_fmt=png&from=appmsg)

任务号与对应功能

![](https://mmbiz.qpic.cn/sz_mmbiz_png/0icdicRft8tz4uRvLNHJQ8Z1TtXVK15Yefg3dFFyHpzBc1ctIznQpU2re2yPX0ibKeaEF09gmoX88ADC1SOpRIEZg/640?wx_fmt=png&from=appmsg)

获取进程列表

![](https://mmbiz.qpic.cn/sz_mmbiz_png/0icdicRft8tz4uRvLNHJQ8Z1TtXVK15YefKibiaxz7JVRhPoMT0QvseBCfYA7haBZ8MfU7gOcYdLARSrqscxSNich7w/640?wx_fmt=png&from=appmsg)

创建管道CMD执行命令

**二**

**附录**

**C&C：**

![](https://mmbiz.qpic.cn/sz_mmbiz_png/0icdicRft8tz4uRvLNHJQ8Z1TtXVK15YeflJgMUbESNuqfrlOIvVib21YNTibicVGE6FicXL0rCkobUPwKH6GiagBSLxw/640?wx_fmt=png&from=appmsg)

**HASH：**

![](https://mmbiz.qpic.cn/sz_mmbiz_png/0icdicRft8tz4uRvLNHJQ8Z1TtXVK15YefIyKltpyibo7d6Ly7TpuDcea4kuaghID16z4A81Lmxm5T01UIrSB4M8Q/640?wx_fmt=png&from=appmsg)

预览时标签不可点

个人观点，仅供参考

修改于

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/sz_mmbiz_png/0icdicRft8tz5V9C96RXn1xV11tycAnWHXCicgKqfOS3JOw7jrIJckWH6Hg0bnXibjicPZs1ET2KwtvsRs41ZhCxh2A/0?wx_fmt=png)

火绒安全

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/0icdicRft8tz5V9C96RXn1xV11tycAnWHXCicgKqfOS3JOw7jrIJckWH6Hg0bnXibjicPZs1ET2KwtvsRs41ZhCxh2A/0?wx_fmt=png)

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