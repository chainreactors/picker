---
title: 汽车ECU的Bootloader设计：UDS协议与刷写流程——0x34/0x36/0x37服务深度解析
url: https://mp.weixin.qq.com/s/57kqfgv50pXC8eYK4nnLbg
source: Doonsec's feed
date: 2026-09-26
fetch_date: 2026-09-27T07:21:07.867755
---

# 汽车ECU的Bootloader设计：UDS协议与刷写流程——0x34/0x36/0x37服务深度解析

# 汽车ECU的Bootloader设计：UDS协议与刷写流程——0x34/0x36/0x37服务深度解析

谈思实验室

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

点击上方蓝字谈思实验室

获取更多汽车网络安全资讯

[![](https://mmbiz.qpic.cn/mmbiz_png/zQ19N6bPViaBvgQxffuoSxCK5zHBjMe1zHgWJ84eiapLGn9OJxaSDIkr7ZxqlZePY6F37BhEGKickoLHqodK770FzBXHPlIuxyHCSicGTiaF5FP4/640?wx_fmt=png&from=appmsg)](https://mp.weixin.qq.com/s?__biz=MzIzOTc2OTAxMg==&mid=2247580896&idx=1&sn=36a65f68d014c79310fdeb0e1e55b6b0&scene=21#wechat_redirect)

**01**

**前言：为什么ECU Bootloader是汽车电子的"生命线"**

在现代汽车中，ECU（电子控制单元）数量已从早期的十几个增长到如今的百余个，软件复杂度呈指数级增长。一辆高端智能汽车的软件代码量超过1亿行，远超波音787的1400万行。这意味着 OTA（Over-The-Air）远程升级 和 售后诊断刷写 已成为汽车电子的刚需能力 。

Bootloader是ECU中预烧录的一段固化程序，负责上电初始化、程序加载，并预留"编程后门"——当外部诊断工具通过CAN/Ethernet发送特定UDS指令序列时，ECU从应用模式切换到编程会话模式，执行固件更新 。

本文将深入解析UDS协议中刷写最核心的三个服务： 0x34（请求下载）、0x36（传输数据）、0x37（请求退出传输） ，从报文格式、状态机设计到安全机制，提供完整的Bootloader实现方案。

**02**

**ECU Flash内存布局与Bootloader架构**

**2.1 Flash分区设计**

Bootloader的设计始于Flash内存布局的合理规划。典型汽车ECU的Flash分区如下：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/zQ19N6bPViaCTIFdXWDLhbficaQE0ZTneuUITfUB0vsAw5qG9kEicQlQnQ2QynQocuKliaNic3wpPjM26zD4IQbYF16wsfhudDBWRmElic83pjqPc/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/zQ19N6bPViaC4JxCiaCFk1jRy05KrmjLF9Ds7XqnbFJmf8rmMnBus9HrO3JCoAiba7sKc2zeI1t44ts85MnA96dVYWI1nNV47z27fOLewP0624/640?wx_fmt=png&from=appmsg)

**2.2 Bootloader启动流程**

ECU上电后的启动流程是Bootloader设计的核心：

1. 上电/复位 ：硬件初始化（时钟、GPIO、中断向量表）
2. 执行Bootloader ：检查更新标志位（存储在Data Flash或EEPROM中）
3. 判断分支 ：

   更新标志=1：进入UDS编程会话，等待刷写

   更新标志=0且App有效：校验App完整性（CRC/Checksum），通过后跳转

   App无效：停留在Bootloader，等待救援刷写

**03**

**UDS刷写三段式流程**

UDS（Unified Diagnostic Services，ISO 14229-1）定义了完整的ECU刷写流程，分为三个阶段 ：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/zQ19N6bPViaBferzZldiaceHBUOnNZSaSgicM6SHoHoFPCIOqhXnDjRmElYmCB6XLHvIh452ibkCOKibibNs7m3qibSazSmibccIphicDcbdzVF8qW2k/640?wx_fmt=png&from=appmsg)

**3.1 预编程阶段（Pre-Programming）**

预编程阶段为刷写创造"安静"的环境，防止其他ECU干扰：

![](https://mmbiz.qpic.cn/mmbiz_png/zQ19N6bPViaAtY8VUQpGO0MVCrGzVuubcv1Z0x41nRaQk0yjwAsBEvyVfNvh4F7nno9Ziak5Mdn4GAsLOGnPdDzHQxjnbkanX4EZxiaLA63edE/640?wx_fmt=png&from=appmsg)

**3.2 主编程阶段（Main Programming）**

主编程阶段是刷写的核心，执行 0x34→0x36循环→0x37 的标准序列：

![](https://mmbiz.qpic.cn/mmbiz_png/zQ19N6bPViaC3G5nYGZZ13DjcMD2n43buAzBKJU1R8ficEAmibL3A8hDAEl5Imib3SWqD3cvaomiaj4F1xbSXYZcyj8wE76eCQ7PCUJFUjNrJzRM/640?wx_fmt=png&from=appmsg)

**3.3 后编程阶段（Post-Programming）**

后编程阶段恢复ECU正常运行状态：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/zQ19N6bPViaBCMORcrKicrjibBEGyPTzZYib8ediauCkvTONYNs0G6rDwKgq0gicGemR0jVWzHB9fPBmm6Huk4JibZZCTtiaNx86a2eQHXVY5A3jneU/640?wx_fmt=png&from=appmsg)

**04**

**核心服务详解：0x34 / 0x36 / 0x37**

**4.1 0x34 请求下载（Request Download）**

0x34服务是刷写的"敲门砖"——告诉ECU"我要开始传数据了，准备好接收！"

![](https://mmbiz.qpic.cn/sz_mmbiz_png/zQ19N6bPViaCznMiaKMpWntyWDa23t3nU3tvfSohfR9NsYvotPF9lKHBxOgpvGdv4H9tV7WQfraS50icyhYmRxWeGib8jnB2LZdupxGuHicHZ4ibI/640?wx_fmt=png&from=appmsg)

请求报文格式 ：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/zQ19N6bPViaCCEOJb0icwgmgREEic9YxPMN8mWMbtEoOSroiaywibXV7qDcjiciapBicABgzOMWmfY3KMDicuQ9ibbRueXOZnbUTqChkOTc2wRzmMrIP4/640?wx_fmt=png&from=appmsg)

响应报文格式 ：

![](https://mmbiz.qpic.cn/mmbiz_png/zQ19N6bPViaAmSbbYa9jcW6ZHjEPqUibIlohEzicyhJfKUxIAeu5S8kpTFeuUf1SibfFR5DtuYbHS6qJa7JOKT0tSto0fgh6ZHTkpdMbseSXEZw/640?wx_fmt=png&from=appmsg)

关键参数解读 ：

* maxNumberOfBlockLength ：ECU告诉Tester"我每次最多能接收多少字节"。Tester在后续的0x36服务中，每块数据长度必须≤此值（减去SID和blockSequenceCounter的2字节）
* dataFormatIdentifier ：支持压缩刷写。0x01表示传输的是压缩数据，ECU接收后需解压再写入Flash。压缩刷写可将传输数据量减少60%~70%，显著提升刷写效率

**4.2 0x36 传输数据（Transfer Data）**

0x36服务是"搬运工"——按照0x34协商的参数，将固件数据分块传输到ECU 。

请求报文格式 ：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/zQ19N6bPViaCx25BPVnqicYfFMXib3xKJAzfchbWiat7KO1AVW0iblOnyLVvjClrpiaibLZCCzcMwicVm3cVhWNRMCcQOBEJntuPica0APCfzPwES2Zc/640?wx_fmt=png&from=appmsg)

响应报文格式 ：

![](https://mmbiz.qpic.cn/mmbiz_png/zQ19N6bPViaAT34XfYUxciaqbSR4ejaVicr20grDp5nPayJGHTcvg8GG9Mrmt6dJsQBaZh605wicacjJoOEibtctcJ749Fo9uicfwDLWvprSUlIbk/640?wx_fmt=png&from=appmsg)

blockSequenceCounter机制 ：

* 从0x01开始递增，每发送一块数据+1
* 到达0xFF后绕回0x00（不是0x01！）
* ECU通过计数器检测：丢包（计数器不连续）、重发（计数器重复）、乱序（计数器异常）

NRC 0x78（ResponsePending） ：

0x36服务是UDS中最常返回NRC 0x78的服务之一。因为ECU接收到数据后需要执行Flash擦除/编程操作，耗时可能超过P2\*最大响应时间（通常为5秒）。此时ECU先回复0x78"正在处理"，处理完成后再回复最终响应 。

**4.3 0x37 请求退出传输（Request Transfer Exit）**

0x37服务是"结束通知"——告诉ECU"本次数据传完了，请做收尾工作"。

请求报文 ：仅1字节SID=0x37，无参数

响应报文 ：仅1字节SID=0x77（0x37+0x40），无参数

关键行为 ：

* ECU收到0x37后，执行Flash编程完成操作（如刷新缓存、写入校验值）
* 若之前的0x34/0x36未完成（如数据长度不足），返回NRC 0x24（请求序列错误）
* 0x37成功后，必须执行0x31服务校验完整性，否则新固件可能无效

**05**

**Bootloader状态机设计**

Bootloader的核心是一个严格的状态机，确保刷写流程的顺序性和安全性：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/zQ19N6bPViaAOsEqFURhSdfTTpwext9liaibQr3bibZqNjxrq56l10eUnmiceXqtVt7ibRg5Zp5HW66icAiasIXMGQaQICgfzhkVDZPpEGOrU9YbbFk/640?wx_fmt=png&from=appmsg)

**5.1 状态定义**

![](https://mmbiz.qpic.cn/mmbiz_png/zQ19N6bPViaCOb3eYOKO2ukPfZMympFiawlTCEQukzjxCZMunrMXtBGPa73jGUOicZGgJZsVGU5Uj8bmSY1yNa2EYOyxapGhAQQiaf1LWTlYk4A/640?wx_fmt=png&from=appmsg)

**5.2 状态转换条件**

![](https://mmbiz.qpic.cn/sz_mmbiz_png/zQ19N6bPViaC3ZCiaw1QzvN598Stdt6Tqib6zBs0GmJgIiaBpKnLpGGEneNkfZ70YAPWu0y1lZ4CM0xvtxRC3Y2nhgnqQuVfFAp4QhRicujEU2rM/640?wx_fmt=png&from=appmsg)

**06**

**安全访问：0x27种子-密钥机制**

刷写是ECU最敏感的操作，必须防止未授权访问。UDS 0x27服务提供基于 种子-密钥（Seed-Key） 的挑战-响应认证机制 ：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/zQ19N6bPViaBUOAURdtupX40QIkVJeBxiaiaNeyEUkeGJWNLAv2pj3dyFJEv5Gzkkn4jokbq2EWMmxr47hyNBpvcViayVLrTicJ8v4lqoCwq5iaKQ/640?wx_fmt=png&from=appmsg)

**6.1 认证流程**

1. 请求种子 ：Tester发送 27 01 （requestSeed），请求ECU生成随机种子
2. 返回种子 ：ECU回复 67 01 XX XX XX XX ，返回4字节随机种子
3. 计算密钥 ：Tester和ECU使用相同的算法（如AES-128、HMAC-SHA256）计算密钥： Key = f(Seed, Secret)
4. 发送密钥 ：Tester发送 27 02 YY YY YY YY ，提交计算结果
5. 验证通过 ：ECU本地计算并比对，一致则回复 67 02 ，解锁安全等级

**6.2 安全等级**

![](https://mmbiz.qpic.cn/mmbiz_png/zQ19N6bPViaBsT1EiaMcTMeV1lE0Zh7ia6WVtNdvJQAKLa5XGTvkq7icHg7r1uS4eg9ibN9h7PaCqtzz3iayfaDkJvicefWfMnzgLbqwltwjcU0tgM/640?wx_fmt=png&from=appmsg)

**6.3 防暴力破解机制**

* 失败次数限制 ：连续3次错误后锁定10分钟
* 种子时效性 ：种子有效期通常为5秒，超时需重新请求
* 密钥算法保密 ：算法和密钥存储在HSM（硬件安全模块）中，不可读取

**07**

**刷写时序与CAN报文实战**

以下是一个完整的刷写时序示例，展示了Tester与ECU之间的CAN报文交互：

![](https://mmbiz.qpic.cn/mmbiz_png/zQ19N6bPViaA2yzyskN48L8vqv0X9oKLxVZtWaOQXhEnRT8416gmlDepdCNrBXlaOJqyP5gjNy6OsTQib3E5w7ULlgHFs7QSMGtbsNeWxd2Jo/640?wx_fmt=png&from=appmsg)

**7.1 预编程阶段报文**

![](https://mmbiz.qpic.cn/sz_mmbiz_png/zQ19N6bPViaCmEOtIhtqe43BlwRtDjXD05DnMRBS0a5JksI60XXZncCoZZTibfh33pARsCAf14esWL3Hr6WFOLtgWIMKS6qRjE6OYQgAYXhiaA/640?wx_fmt=png&from=appmsg)

**7.2 主编程阶段报文**

![](https://mmbiz.qpic.cn/sz_mmbiz_png/zQ19N6bPViaDpvYNhrc9hsaXX1iaK9G1ebeiavrfMw3j2A0HlBXCyr2HZiaiawGzeF4BUQn60BAFfKP80GUKOMIjA7jWfOJpZtZIH67wZ7wnNyaQ/640?wx_fmt=png&from=appmsg)

**7.3 后编程阶段报文**

![](https://mmbiz.qpic.cn/mmbiz_png/zQ19N6bPViaBHAMcanRShcN0T8RgicaaMwIG41DMMwfmqeNJlnF2qyNcdSOY2TibCFsC0BianuBxbNYfaSvoUD9fOOI0FjmohfkYCyYK2vicfbHo/640?wx_fmt=png&from=appmsg)

**08**

**刷写失败恢复机制**

刷写过程中任何环节都可能失败， robust的Bootloader必须具备完善的恢复机制：

![](https://mmbiz.qpic.cn/mmbiz_png/zQ19N6bPViaAjJCxv7qYwyWr4zBYcy6uLj6cQpCv2gMYpGic37o0ZG5keI3A9SJiciaeL7ANcqP2Djym3uRVDeadFDha9FSdQpOmT7RaVpIsGF4/640?wx_fmt=png&from=appmsg)

**8.1 常见故障与恢复策略**

![](https://mmbiz.qpic.cn/mmbiz_png/zQ19N6bPViaDGmUVnIicenbbsAlDuiciculiasO9zQFoFTibRtHpnXicHPO2qzdh1lWLxutjLH9LwX6eNYbX0Xm6Wvmcib0fqVRtu92mucRAreSpfs4/640?wx_fmt=png&from=appmsg)

**8.2 A/B双分区机制**

A/B双分区是现代Bootloader的标配，确保刷写失败时系统可恢复：

1. 新固件写入B区 ：不影响正在运行的A区App
2. 校验通过后切换启动标志 ：下次启动从B区运行
3. 校验失败则继续从A区启动 ：系统始终可用

![](https://mmbiz.qpic.cn/sz_mmbiz_png/zQ19N6bPViaCVFpqm4NzhHgTRfVwsfH82dXicfxtenuT7AB4tJPibCEd4XInxeNXZtQIZqR98JxDfo1VXErjVF4U104QHcOKk7VNicwbFrnGhEQ/640?wx_fmt=png&from=appmsg)

**09**

**Bootloader核心代码实现**

**9.1 0x34服务处理**

![](https://mmbiz.qpic.cn/mmbiz_png/zQ19N6bPViaAND8PPASvelZhntvKq4Cs05nQYiaSL9RtBlHooaZSqbnibK9XH0IqnO0H3oicFAQLTjRAnCoNKPKswaZp4n6vK6Y0SYiaiaLw3axuY/640?wx_fmt=png&from=appmsg)

**9.2 0x36服务处理**

![](https://mmbiz.qpic.cn/sz_mmbiz_png/zQ19N6bPViaCQdq8caWVbU2LNicyGwYrjYcElfRj8SasAwxhHaUbn7uEUFPSRJbRGMB9YUsQNoWx2b8GW22O2vk9uLcGYwE772k8l4icicTA5FQ/640?wx_fmt=png&from=appmsg)

**9.3 0x37服务处理**

![](https://mmbiz.qp...