---
title: 【实战】针对在某次医疗项目中关于C/S架构系统的渗透测试小TIPS 附工具
url: https://mp.weixin.qq.com/s/p08Rn6eYLB9SWWUE8gMYKg
source: Doonsec's feed
date: 2026-05-23
fetch_date: 2026-05-24T05:58:35.562766
---

# 【实战】针对在某次医疗项目中关于C/S架构系统的渗透测试小TIPS 附工具

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/EZicQGyMXoOn7YgtM8Qib0sfA5uiafPEkl161viahjW7BpiatRRzCt07OFTicwjvDmDNQJOCiaKevy2Pz5bBlkwg6EbceO7sg0ASx4SpBZkiaEichVIQ/0?wx_fmt=jpeg)

# 【实战】针对在某次医疗项目中关于C/S架构系统的渗透测试小TIPS 附工具

原创

渗透测试
渗透测试

渗透测试

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/z3TOtprWtZ9QhmHGYehZ9F79iaM3xOhmgcYjHLAK13P2LwibhTATEUlktbw5lRvOwhHng1gibia05VDWGOnzFPAIkg/640?wx_fmt=other&wxfrom=13&wx_lazy=1&wx_co=1&randomid=d3ftoiiz&watermark=1&tp=wxpic#imgIndex=0)

**点击上方蓝字******关注【渗透测试】不迷路****

        本文复盘一次医疗 C/S 系统授权渗透测试的完整过程。初始阶段常规信息收集、弱口令与逆向分析均未突破，后通过断网报错定位 Oracle 数据库，借助进程内存提取工具成功获取数据库账号密码。实战之余，同步详解 C/S 架构的 4 种类型及安全差异，总结两层架构的核心风险与测试要点，兼具实操性与知识性。

该文章仅用于技术交流，请勿将工具用于非法用途。

#### 前言

  记录一次授权的渗透测试，充满了巧合，也算比较有意思直接记录一下，图片打码比较重，但关键信息都留着，应该不影响阅读！👍

天崩开局一个登录框

![](https://mmbiz.qpic.cn/sz_mmbiz_png/EZicQGyMXoOkNEmDVhyzKMO47t6icNKpOORkdn2f3RFDrALiamBWvOZNYzrHzVmvpZkFB7jfjibWqurPJfTPchVtyoHtKbjhVT2onvuktsAQQiao/640?wx_fmt=png&from=appmsg)

系统仅有登录框，常规信息收集、弱口令、注入、查配置文件、客户端逆向（Ghidra/IDA/x64dbg）均无突破。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/EZicQGyMXoOluzG89RIjbH0sNfzlp9nDIib4ZUVNUZRP1hc1m1gQkr8iaicoPHpicQvPgGRAV7YlY8NOyWVk58sDibSsAbM9ymHheAdcf2UIibUlLg/640?wx_fmt=png&from=appmsg)

抓包，看到直接连的1521 Oracle数据库。

![](https://mmbiz.qpic.cn/mmbiz_png/EZicQGyMXoOmCHTyiayQ1LLNAmNCHV8m52ls0vHrvtTSH94ibTMA7dUhgA0jtRmcNM8SiciayTUJrQ7r0fzoFSPP6qIUaYlzsdVdmu9F4pgthoWQ/640?wx_fmt=png&from=appmsg)

Tpis 断开网络  点击登录查看响应状态

```
断网抓包 + 报错分析：断网点击登录，报错含ORA-03114，直接锁定后端为Oracle 数据库（1521 端口）。
```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/EZicQGyMXoOkL09dRZWicuJM4L1JORKiam5OJ5iclcrdY6FOvsRV84jRc25PNI7aiabM2xhdZUma8T0sAIMpgCKCSQWVA5pCHt6SxbJN2oZnUWSk/640?wx_fmt=png&from=appmsg)

通过提示（校验工号失败:错误提示:打开数据集错误!(ORA-03114: 未连接到 ORALCE)）

可以看出来登录时会去连接数据库，（但是我这里把网络断开了，所以显示了数据库的报错）

```
通过报错判断数据库为Oracle
```

打开火绒剑🗡进行**进程监控分析**

![](https://mmbiz.qpic.cn/sz_mmbiz_png/EZicQGyMXoOkhpSMbONh82gMicicQvk1ibg0tQHdoKp1iawllSicOqjsrN2yMwD80ib25jQKLK1SuXKzRMmQRhE3CIj9dAEeE9YXcNhm9AtQia1lI7g/640?wx_fmt=png&from=appmsg)

火绒剑官方已经宣布下线了

![](https://mmbiz.qpic.cn/mmbiz_png/EZicQGyMXoOmRAI2SSYCDSK8aUp51IkgGoJmlefLPFG2tbJu23lHsQWuKVHXgIyMlZDmjWicV0vicQicwjTvIlQqvmicGvBK7DmBUGlx1rSF8rxs/640?wx_fmt=png&from=appmsg)

进程里面已经加载了该应用，选择应用搜索字符串

![](https://mmbiz.qpic.cn/mmbiz_png/EZicQGyMXoOkVjMbb71xWdZo3AMRNtBy3IZ6DyDva9JLJibUjqFDibU3maDh6OhJtj3nfnQKAe0KjG8DtItkPPSMfeBf4xFOCMop7bD86roXkA/640?wx_fmt=png&from=appmsg)

搜索刚才数据库的提示 》提取内存字符串：

```
打开数据库集错误！校验工号失败:错误提示:打开数据集错误!(ORA-03114:未连接到ORALCE)iduserpasswordData SourceUser ID......等关键字
```

![](https://mmbiz.qpic.cn/mmbiz_png/EZicQGyMXoOmDicicFLaRZdFnSKlGJicByqGY3SndxpmGSZOFFsd80P8F4iasyOf20Sicj5uWiaoN94rKxcvEJ8xV7E7EBwywMpSqjT6d0SQnpsb1o/640?wx_fmt=png&from=appmsg)

提取内存字符串

![](https://mmbiz.qpic.cn/sz_mmbiz_png/EZicQGyMXoOnjN5YOicy8b4DTkOMnQXavQSjibnmu8jWJcVPRGWuzQrZ6P9a5pA4fDpEiaibnr2nXuW72icpUoHmicCgFeWKzbQibfEtXMdacUqpvEg/640?wx_fmt=png&from=appmsg)

在打开的内存字符串中搜索数据库连接的关键字

![](https://mmbiz.qpic.cn/mmbiz_png/EZicQGyMXoOlVF4s7QxJEf7LouZaCCY5xHReA99nG7PbMynveP8iayM2RL2kMKruWcJBV7rnu50toJkMcpQ4flibyebSdOMic3CMchyt8t7tZPg/640?wx_fmt=png&from=appmsg)

通过C&S架构的客户端得到数据库用户名密码，尝试连接

![](https://mmbiz.qpic.cn/mmbiz_png/EZicQGyMXoOmqyAkB3VaDbs3nVB4vZzxUqicazKI5xSZ2fibJDoR8MWgictZ7fdRhrLibfMkptvT74maYPbhMF6mSq9LnyviaMAPytMryRHxLcl1U/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/EZicQGyMXoOnXOUXwI8NbkwF4W5tt3nzkxQQ2DOXjT7wic5fzcFaib7mibuiaXky10NficD26xIubr8z7DRNe02yuJTw6ibHtCGRYeKgiaqsc1rOEcU/640?wx_fmt=png&from=appmsg)

点到为止得到数据库内容提交报告，所以没有继续深入。

火绒剑官方已经宣布下线了可以试试其他工具ProcessExplorer

管理员权限运行 ProcessHacker 选择需要导出内存的应用

![](https://mmbiz.qpic.cn/mmbiz_png/EZicQGyMXoOmyzSxQquU3mhB20jnr4YvlHtzz9QcXian0SXZkWANSU2CChs0qlhmI81MYd7k5h7R3MYn4ynDbl2Ut88icXFmt1swCtDUd1sMyw/640?wx_fmt=png&from=appmsg)

点击 “Create dump file..” 后选择保存文件到本地，搜索可能出现泄露的关键字。

```
iduserpasswordData SourceUser ID
```

🎁文中工具获取方式

👇关注公众号，后台回复关键词 " 0228 "获取👇

C/S（客户端/服务器）系统的架构可以根据其复杂性、功能分布和业务逻辑的处理方式进行分类。以下是几种常见的C/S架构模式，从简单到复杂排列：

---

### 1. 两层架构

这是最经典、最简单的C/S架构形式，通常被称为“胖客户端”架构。

* **结构**：**客户端** ←→ **服务器**（通常是**数据库服务器**）
* **职责划分**：

+ 主要负责数据存储、管理和执行客户端发来的SQL命令。

+ 提供用户界面（UI）
+ 执行业务逻辑（如数据验证、计算规则）
+ 直接向服务器发起数据库查询（如 ODBC, JDBC 连接）

+ **客户端**：
+ **服务器**：

* **优点**：

+ 结构简单，开发速度快。
+ 客户端功能强大，响应速度快（因为业务逻辑在本地执行）。

* **缺点**：

+ **部署和维护困难**：“胖客户端”需要在每台电脑上安装和更新，成本高。
+ **可伸缩性差**：数据库连接数有限，大量客户端直接连接会导致数据库性能瓶颈。
+ **安全性差**：业务逻辑暴露在客户端，容易被逆向分析；数据库连接字符串和凭证可能硬编码在客户端。

* **典型应用**：早期的企业内部管理系统（如财务、库存管理系统），使用PowerBuilder、Delphi或VB开发的应用。

---

### 2. 三层架构

这是目前最常见、最主流的C/S架构，通过引入一个中间层来解决两层架构的问题，也被称为“瘦客户端”架构。

* **结构**：**客户端** ←→ **应用服务器** ←→ **数据库服务器**
* **职责划分**：

+ 专注于**数据层**，负责数据存储，只接受来自应用服务器的请求。

+ 承载**核心业务逻辑**（也称为“业务层”或“中间层”）。
+ 处理客户端的请求，执行复杂的计算和业务流程，然后与数据库交互。
+ 通常通过API（如 RESTful API, gRPC, SOAP）与客户端通信。

+ 专注于**表示层**，只负责提供用户界面和展示数据。
+ 业务逻辑极少或没有（因此被称为“瘦客户端”）。

+ **客户端**：
+ **应用服务器**：
+ **数据库服务器**：

* **优点**：

+ **易于维护和更新**：业务逻辑集中在应用服务器，升级时无需更新所有客户端。
+ **可伸缩性强**：可以通过增加应用服务器实例来应对高并发，与数据库连接池配合良好。
+ **安全性更高**：客户端不直接访问数据库，数据库结构被隐藏。
+ **复用性好**：同一套业务逻辑API可以被Web端、移动端等多种客户端复用。

* **缺点**：

+ 系统结构更复杂，开发和部署成本相对较高。
+ 网络通信开销增加，如果应用服务器性能不佳可能成为瓶颈。

* **典型应用**：绝大多数现代企业级应用、在线游戏服务器、金融服务系统等。技术上，应用服务器可能由Java EE（Spring Boot）、.NET Core、Node.js、Python（Django/Flask）等框架实现。

---

### 3. N层架构

三层架构的扩展，将应用服务器层的不同职责进一步拆分，形成更多、更专业的层次。

* **结构**：例如：**客户端** ←→ **Web服务器** ←→ **应用服务器** ←→ **数据库服务器**
* **职责划分**：

+ **Web服务器**：负责静态内容托管、负载均衡、SSL终止等。
+ **应用服务器**：专注射业务逻辑。
+ **缓存层**：加入Redis、Memcached等，减轻数据库压力。
+ **消息队列**：加入Kafka、RabbitMQ等，处理异步任务和解耦服务。

* **优点**：

+ 更高的灵活性、可扩展性和可靠性。每个层级可以独立扩展和优化。

* **缺点**：

+ 架构非常复杂，运维成本高。

* **典型应用**：大型互联网应用，如电商平台、社交网络等。

---

### 4. 点对点架构

一种特殊的分布式C/S架构，其中每个节点（Peer）既可以作为客户端请求服务，也可以作为服务器提供服务。

* **结构**：**节点** <--> **节点** <--> **节点**
* **职责划分**：没有中心服务器的概念（或只有一个弱中心用于协调），所有节点地位平等，共享资源（如计算能力、存储空间、带宽）。
* **优点**：

+ 去中心化，抗摧毁性强。
+ 可扩展性极佳，节点越多，系统整体能力越强。

* **缺点**：

+ 管理困难，安全性挑战大（如恶意节点）。
+ 网络环境复杂，服务质量（QoS）难以保证。

* **典型应用**：比特币/区块链网络、BitTorrent等文件共享系统、某些即时通讯协议。

### 总结对比

| 架构类型 | 核心特点 | 优点 | 缺点 | 适用场景 |
| --- | --- | --- | --- | --- |
| **两层架构** | 客户端直接连数据库，逻辑在客户端 | 简单、开发快、响应快 | 难部署、难扩展、不安全 | 传统桌面应用，小型内部系统 |
| **三层架构** | 客户端-应用服务器-数据库 | 易维护、高扩展、更安全 | 结构较复杂 | **现代企业应用的主流选择** |
| **N层架构** | 三层架构的细化，引入缓存、队列等 | 极高扩展性、灵活性、可靠性 | 非常复杂，运维成本高 | 大型、高并发互联网应用 |
| **点对点架构** | 去中心化，节点互为客户端/服务器 | 去中心化、扩展性强 | 管理难、安全性挑战大 | 文件共享、区块链、分布式计算 |

在选择C/S架构时，需要根据项目的**规模、性能要求、安全需求、团队能力和运维成本**来综合决定。目前，**三层架构**因其在可维护性和扩展性上的优异平衡，是绝大多数C/S系统的首选。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/EZicQGyMXoOnicr8ohvk3DzpDzaicJW9FYsdwMwTDHxquyFVSvGoF9sVZeteF4ibuqE2lASrbicWTDO10S7c15FwRO18dwKu9gXgl52VOuSicy5r8/640?wx_fmt=jpeg&from=appmsg)

****星球介绍****

**自研工具、二开工具、免杀工具、漏洞复现、教程等资源、漏洞挖掘分析、网络安全相关资料分享。**

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/z3TOtprWtZicXY4BSgJe6I89QuKm2PibuDBNN2203zA5Tiapib5ROJkjVPds83kicPcK9stfcKlt1Fx4SXibtJHFC0xw/640?wx_fmt=png&from=appmsg&watermark=1&wxfrom=5&wx_lazy=1&tp=wxpic#imgIndex=16)

## ✅AiScan-N使用反馈

![图片](https://mmbiz.qpic.cn/sz_mmbiz_jpg/z3TOtprWtZ9QhmHGYehZ9F79iaM3xOhmgI7DL7frM1jlf8MYvB3ms38IPZicqVX4RibKKYzdOzW6fKAznYpf76LsQ/640?wx_fmt=jpeg&from=appmsg&watermark=1&wxfrom=5&wx_lazy=1&tp=wxpic#imgIndex=11)

🎁获取方式(加入付费****星球****)

客服支持 💬：24小时在线解答，不怕有问题！

![图片](https://mmbiz.qpic.cn/sz_mmbiz_jpg/z3TOtprWtZ9QhmHGYehZ9F79iaM3xOhmgtHyZGGib9XEJbYqeIZLVhWRcPdRltoe7hn1JNZhHFsjbyLibckKeb5Xg/640?wx_fmt=jpeg&watermark=1&wxfrom=5&wx_lazy=1&tp=wxpic#imgIndex=12)

💎**终身使用权**：购买即可获得星球所有工具的永久使用权，终身使用所有工具及未来升级版本。

🖥️ **多设备支持**：所有工具采用一机一码授权，支持多台自用电脑激活，灵活无忧。

🏆**一次购买，终身受益！**享受无忧售后服务、技术支持与永久更新

##

[【渗透实战】记一次某医院LIS系统SQL Server数据库提权（有手就行）](https://mp.weixin.qq.com/s?__biz=Mzg2ODY3NDYxNA==&mid=2247484557&idx=1&sn=c7a38342cfe2b8840ec5634e93ff9ea7&scene=21#wechat_redirect)

[APP渗透测试小白必看：记一次简单纯捡漏实战技巧，让你轻松上手不再是梦](https://mp.weixin.qq.com/s?__biz=Mzg2ODY3NDYxNA==&mid=2247485912&idx=1&sn=9f9ae2e69d26237bd82dfe0086115a1f&scene=21#wechat_redirect)

[实战 | 记一次在梦里对内网某员工信息管理系统的渗透测试](https://mp.weixin.qq.com/s?__biz=Mzg2ODY3NDYxNA==&mid=2247485610&idx=1&sn=cd662dbd922fbd2c7f7bfe207b41957d&scene=21#wechat_redirect)

**免责声明**

该项目仅供网络安全研究使用...