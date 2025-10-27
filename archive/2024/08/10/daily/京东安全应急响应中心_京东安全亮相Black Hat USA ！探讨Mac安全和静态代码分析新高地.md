---
title: 京东安全亮相Black Hat USA ！探讨Mac安全和静态代码分析新高地
url: https://mp.weixin.qq.com/s?__biz=MjM5OTk2MTMxOQ==&mid=2727837409&idx=1&sn=15967da65d6d556121d5ed7648a08821&chksm=8050a969b727207fc28c7d843bf37bb1e31fca80ab6ea2185b777393d8aa8c4fb36252193085&scene=58&subscene=0#rd
source: 京东安全应急响应中心
date: 2024-08-10
fetch_date: 2025-10-06T18:06:10.233746
---

# 京东安全亮相Black Hat USA ！探讨Mac安全和静态代码分析新高地

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/Z9MuUwaeeGJHa8w5rDjiaXewMQmyQ75P67PjjhibMp9V6udyUxDZ09BtQiaGAX6OKrZgdHM6nXGFwrLmGic62gl3Tw/0?wx_fmt=jpeg)

# 京东安全亮相Black Hat USA ！探讨Mac安全和静态代码分析新高地

邀您共享成果的

京东安全应急响应中心

**京东安全**

///2024 Black Hat USA

**8月3日至8月8日**，安全领域顶级盛会——美国黑帽子大会**Black Hat USA 2024**于美国拉斯维加斯成功举办。**京东安全獬豸实验室**成员亮相本次大会，与来自世界各地的安全专家、研究人员和从业者分享安全领域新成果。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Z9MuUwaeeGJ2W8rQMaDPxzJtw4XJQ0V9pjUndSnYIDyWNJsnwRaUmgGDysTjl4FmOtNVEolPEibguujTnQ3SmyQ/640?wx_fmt=png&from=appmsg)

**Mac安全新议题：**

**应用沙箱和AppData TCC的全面探讨**

京东安全獬豸实验室本次入选的议题之一名为：

Unveiling Mac Security: A Comprehensive Exploration of Sandboxing and AppData TCC。

安全实验室研究员基于Android和IoT安全领域的丰富经验，探讨了macOS 上应用沙箱和AppData TCC的安全漏洞。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/Z9MuUwaeeGJ2W8rQMaDPxzJtw4XJQ0V9w07jkZ5hv0GRFbwtwsVicUqKYGp0JicOZSCeozgs0soYxCBQ2AicAjakA/640?wx_fmt=jpeg&from=appmsg)

安全实验室研究员结合多个macOS系统上的系统特性，成功的将一个传统意义上无法被利用的漏洞转换为通用的应用沙箱逃逸，该漏洞存在时间超过5年且该漏洞利用手法在最新的macOS15.0上仍然可用。同时，实验室研究员深入研究了macOS上一套权限授予机制，随后借助其获得了mac平台任意文件读写的能力，该漏洞同样存在多年。此外，macOS 14.0 引入了新的 TCC 保护措施，防止非沙箱应用程序访问沙箱应用程序的私有容器文件夹。以前，启动恶意非沙箱应用程序可能会泄露微信、Slack 和 WhatsApp 等沙箱应用程序中的敏感数据。不过，由于有了新的 TCC 保护措施，这种情况在 macOS 上不再可能发生。实验室安全研究员深入分析了 macOS 如何实现这个 TCC 保护措施，并借助其漏洞再次实现了任意文件读写。

最后，实验室安全研究员也披露了其设计中存在的一个攻击面，并与其他操作系统中类似的机制进行了分析和对比。针对这一问题，研究员也给出了两种可行的终端防御思路：一是可以通过Endpoint Security Framework，对异常的symlink等文件操作进行监控，以探测可能进行的攻击；二是通过动态沙箱系统，对疑似恶意的样本在沙箱内动态执行，检测例如containerURLForSecurityApplicationGroupIdentifier等关键API的参数。

**JDoop：**

**提升Java Web应用安全的静态分析利器**

Blackhat Arsenal互动展示是Blackhat的另一大特色，展示来自全球各地技术极客开发的优秀安全工具。实验室研究员聚焦 Java Web 应用程序，展示了一款基于Doop改进的黑盒静态分析工具JDoop，目前可以扫描包括命令注入、SQL 注入、JDBC 反序列化等多种数据流类型的漏洞。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/Z9MuUwaeeGJ2W8rQMaDPxzJtw4XJQ0V9QqIoa1Sm7ziaoE3X96dojUiaufJcExtV4oWTCj451BZpaH0jpO2wkXXQ/640?wx_fmt=jpeg&from=appmsg)

实验室研究员分析了传统上下文敏感策略（context sensitive strategies）在JavaEE场景下表现不佳的原因，使用污点分析（taint analysis）技术在JDoop上提出了基于入口点保留上下文元素的新策略。同时，JDoop对于PT分析算法（PT analysis algorithms）中的污点传播（taint transfer）规则进行了改进，以解决Access Path问题。经过上述改进，JDoop在漏洞检测的准确性和效率方面有显著提升。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Z9MuUwaeeGJ2W8rQMaDPxzJtw4XJQ0V9pjUndSnYIDyWNJsnwRaUmgGDysTjl4FmOtNVEolPEibguujTnQ3SmyQ/640?wx_fmt=png&from=appmsg)

**獬豸实验室**

獬豸实验室 （Dawn Security Lab）是京东旗下专注前沿攻防技术研究和产品沉淀的安全研究实验室。重点关注移动端安全、系统安全、核心软件安全、机器人安全、IoT安全、广告流量反作弊等基础和业务技术研究。

实验室成员曾多次获得Pwn2Own冠军，在BlackHat、DEFCON、MOSEC、CanSecWest、GeekCon等顶级安全会议上发表演讲，发现Google、Apple、Samsung、小米、华为、Oppo等数百个CVE并获得致谢。曾获得2022年黑客奥斯卡-Pwnie Awards“最佳提权漏洞奖” ；同时也是华为漏洞奖励计划优秀合作伙伴，CNNVD一级支撑单位，GeekCon优秀合作伙伴。

**-加入京东安全-**

**獬豸实验室**正在招募各路英雄，想要加入崇尚技术创新的、用技术守护互联网安全的我们，欢迎投递简历至 **jsrc@jd.com**。

（邮件主题：姓名-投递岗位）

**安全研究员**

岗位职责：
从事操作系统、二进制、浏览器、App等方面的漏洞挖掘和研究工作。
岗位要求：
1. 有独立挖掘分析Android、iOS、macOS、Linux Kernel、Chrome等基础系统漏洞、编写exp能力，发现过原创CVE；
2. 有一定代码开发能力，譬如python、go、c/c++、Java等，了解静态代码分析、Fuzz等技术；
3. 有顶级安全会议演讲、论文，头部厂商致谢；
4. 善于团队合作，为人正直，基础扎实，不畏困难，积极向上。

**安全工程师**

熟悉漏洞挖掘或相关领域攻防技术或开发技术，能将攻防技术、开发经验有机结合到企业安全建设中，为集团消除风险。

岗位职责：
1. 参与集团基础风险消除项目，包括但不限于云原生安全、移动安全、iOT安全、系统安全、软件供应链安全、基础组件安全等；
2. 进行关键组件和系统、基础设施的前沿漏洞挖掘和研究；
3. 参与相关能力系统的研发，为业务部门提供安全能力；
4. 具有较好研发能力是加分项。

**后端开发工程师岗**

岗位职责：

1. 参与安全产品能力的需求讨论、设计，并负责相关功能的开发落地；

2. 按照项目排期，按时提交稳定、高质量代码，完成开发任务；

3. 负责系统的架构、技术、运维文档的编写、维护以及其他与项目相关工作；

4. 生产突发问题的排查、处理，重点、难点问题的攻关，突破。
岗位要求：
1. 3年以上互联网领域的设计与开发经验，具备扎实的开发基础，精通Java开发语言（Java）；
2. 熟练掌握IO、多线程开发技术，对事务、锁、并发等实现机制有深入了解；

3. 熟练使用Spring、Spring MVC等框架，并对框架原理有一定了解；
4. 熟悉SOA架构，对RPC、序列化、服务治理有相应了解；
5. 熟悉常用数据库软件(MySQL)的原理和使用，熟悉常用ORM和连接池组件,对数据库的优化有一定的理解；
6. 熟悉计算机网络基础原理、了解常用网络通信协议；

7. 热爱技术，对技术有不懈的追求，喜欢研究开源代码，良好的学习能力、团队协作能力和沟通能力，具备安全攻防经历、有安全相关开发经验优先.

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/Z9MuUwaeeGIlXfXZDFfRBZuzMIeAKzMfMxSjmvm8OnyrJCz9K2bnuL1L3wdTZMh5mibyKD3sbQB0Mia5qZCvxNTw/0?wx_fmt=png)

京东安全应急响应中心

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/Z9MuUwaeeGIlXfXZDFfRBZuzMIeAKzMfMxSjmvm8OnyrJCz9K2bnuL1L3wdTZMh5mibyKD3sbQB0Mia5qZCvxNTw/0?wx_fmt=png)

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