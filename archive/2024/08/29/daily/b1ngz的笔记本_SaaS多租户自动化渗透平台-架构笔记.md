---
title: SaaS多租户自动化渗透平台-架构笔记
url: https://mp.weixin.qq.com/s?__biz=MzkwNDE5NzUyMA==&mid=2247483694&idx=1&sn=f790233f79f52fb60fcd1aefa25d4820&chksm=c08be5d1f7fc6cc7f5fa27679972bc7dd8dfb48f8ed254e6918279760ca158d03fc69593778c&scene=58&subscene=0#rd
source: b1ngz的笔记本
date: 2024-08-29
fetch_date: 2025-10-06T18:05:20.778652
---

# SaaS多租户自动化渗透平台-架构笔记

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/1JicUwKQqRQ5hTLganMZaSHT8NXyajiagnbhZU3GezrBhflRfDIHsbTeU8dmbfRaibUwFZfpfHo2lzyuiaPC5DT5gA/0?wx_fmt=jpeg)

# SaaS多租户自动化渗透平台-架构笔记

原创

b1ngz

b1ngz的笔记本

0x01. 简介

---

在 2022 年初，我写了一篇 “[云化分布式自动化渗透测试平台 - 架构笔记](https://mp.weixin.qq.com/s?__biz=MzkwNDE5NzUyMA==&mid=2247483673&idx=1&sn=88b42a078e291a2f9b3ef8de515731cf&scene=21#wechat_redirect)” ，介绍了我与团队师傅在 SaaS 自动化渗透平台架构设计方面的一些想法和初步实践，距今已过去两年多的时间。在这段时间里，遇到了很多新的问题和挑战，同时也有很多新的想法。在 23 年底，经过内部讨论，并结合业务发展情况，我们对整个平台进行了一次完全的重构，这篇笔记介绍了重构背后的一些思考、新架构的设计思路，以及架构的整体情况

PS：🔥 公司正在广纳人才，详见 “0x06. 招聘” 或 复制访问下方链接在线查看职位详情和投递简历

**https://app.mokahr.com/su/5wsls**

#

#

# 0x02. 问题和挑战

---

在平台建设过程中，会不断产生新的需求，和更复杂的业务场景需要满足，但平台架构很难在短时间内进行频繁改动。因此对于大多数情况，只能进行“修修补补”的操作，经过两年多的日积月累，历史架构设计和技术选型的问题逐步暴露，无法很好地满足业务发展的需求。

关于平台架构设计和技术选型部分的问题，可总结为：

* 扫描节点无法独立部署：对于一个子任务的运行，可概括为三步 1. 从数据库查询所需参数，2. 执行具体逻辑，3. 保存结果入库。这里既有业务代码（1、3 两步，Python 编写），又包含引擎逻辑（第 2 步 GRPC 调用 Golang）。业务代码部分是一个大的后端项目，即节点的运行需要同时将后端和引擎服务运行起来，二者较为耦合，使得节点服务无法独立部署
* 扫描节点无法外置部署：因所有服务是在一个 VPC 内进行通信，节点执行任务需要访问 DB、队列等服务，但考虑到安全性、稳定性等原因，无法直接将服务暴露在公网，使得在目标存在网络访问限制（如只允许某个地区 IP 访问）、多云多地域出口 IP 等需求等场景下无法很好的支持。此外，外部环境可能是非受信环境，节点运行包含部分 Python 代码和配置，存在泄露风险
* 网络连接稳定性强依赖：起初选择了 RabbitMQ 作为消息队列，为了确保消息能成功的发送和执行，启用了双向 Ack，当 Client 与 Server 间的通信因为伸缩、维护、网络不稳定等不可避免原因出现中断时，RabbitMQ 会认为消费者异常（实际还在运行），从而将消息交由其他消费者处理，导致业务层和消息队列的状态不一致，出现一次任务多个运行实例的情况。此外，RabbitMQ 无法直接查看正在被执行的消息内容（unack 状态），无法自定义控制失败重试过程等限制，使得问题的排查、处理复杂和困难
* 后端框架不透明不灵活：此前我们选择了 Django REST Framework 作为后端业务层框架，借助成熟的生态和丰富的接口方法，实现了高效开发。但同时也存在一些问题，例如 Django ORM 提供的很多方法，内部都有一定程度的封装，会使得用户较难直观地知道背后的执行逻辑。在多人协作时，会给复杂需求代码实现 Review、问题定位排查和性能优化带来一定困难。此外，部分复杂的查询（如无 foreign key 表 join、自定义的 join 条件）在 Django ORM 下较难实现，灵活性上不足。而 Django/DRF 和 Django ORM 的强关联，使得集成和同时使用其他 DB 层框架等实现能力扩展的需求变得困难

另一方面，平台在设计之初的定位是支撑内部渗透项目和攻防演练。而随着业务和平台的发展，内部也在考虑商业化的可行性，从而给平台带了新的需求和挑战

* 控制研发成本：因现有平台与内部系统有一定耦合，以及存在前述的设计和选型问题，无法直接进行改造后作为商业版。而开发和维护两套不同的平台，在现有人力下无法支撑。因此，需要考虑如何尽可能减少重复工作，降低开发和维护成本
* 数据安全保障：平台是 SaaS 化形态，数据存储在云端，客户对数据的安全性非常敏感，因此需要从设计上考虑安全隔离的方案，特别是不同客户间的数据隔离
* 合法合规保障：如果扫描流量走平台出口，会涉及到授权和法律风险。因此扫描节点需要由客户来提供，即需要能够支持扫描节点的私有化部署

# **0x03. 解决思路**

---

对于上述问题和挑战，解决思路如下

* 解耦扫描节点服务：将引擎和后端代码完全剥离，让扫描节点成为一个独立服务，即后端将子任务运行所需的所有参数发送给扫描节点，扫描节点仅负责执行，完成后将结果发送回后端服务，进行异步的处理和入库
* 打破VPC网络边界：对不适合直接暴露在公网上的服务（如消息队列）进行二次封装，使⽤如 HTTPS 等⽅式与 VPC 外部扫描节点进⾏通信，解决网络边界和安全性问题
* 替换消息队列实现：基于 Redis Stream 开发新的消息队列服务，解决网络连接稳定性强依赖问题。并实现更加灵活的消息发送、任务运行观测、失败重试控制等能力
* 替换后端开发框架：使用 Flask-RESTful + SQLAlchemy 代替 DRF 和 Django ORM，并参考 DRF View、Serialize、FIlter 的设计，对 Flask-RESTful 进行封装，使得二者在写法上类似，更易上手
* 一套代码两个环境：为了减少维护成本，这里采用只维护一套新平台代码的方案。但因内外部的功能和限制上有一些区别，这里通过角色权限和代码逻辑处理等方式来进行兼容。另外考虑到安全性，内外部是两套独立的环境，互不相通
* 多租户设计和改造：为了实现数据安全隔离，以及避免为每个客户搭建一套独立的环境导致维护成本过高，这里采用了存储层和扫描节点独立，其他服务共享的方案。即每个租户拥有独立的数据库、消息队列空间等，实现逻辑或实例级别的隔离。而对于后端 API、任务调度等服务，进行多租户的底层库封装（业务代码无感），支持根据用户或任务所属租户动态选择 DB，以及动态租户配置加载等能力
* 多种节点运行模式：对于商业版，主要以客户在自己的 ECS 实例上运行扫描节点的方式为主。在内部版，以 K8S 动态创建 Pod 的方式来实现更灵活高效的节点管理。此外，理论上只要部署环境能够运行 docker 容器，并且机器配置和网络带宽能满足需求，均可部署和运行扫描节点
* 构建安全中台服务：因需要同时支撑内外部的使用需求，为了避免重复开发和实现无感的能力升级，这里将需要的公共安全能力抽取出来，统一到 SaaS 安全中台进行维护
* 开发运营运维平台：因多租户的设计，客户环境较多，为了能够高效方便的管理客户信息、环境配置，以及问题排查和定位，需要有一个上层的独立管理平台来进行支撑

# 0x04. 平台架构

---

新平台架构示意图如下

![](https://mmbiz.qpic.cn/mmbiz_png/1JicUwKQqRQ5hTLganMZaSHT8NXyajiagnbBEO9pSDsAp8G9W0Z6ugPbHfAicF5qujWKgzqz8TFKib9cNKQYQKe62A/640?wx_fmt=png&from=appmsg)

如上图所示，平台由四大部分组成

1. SaaS 自动化渗透平台：图中蓝色部分，多租户架构设计，由业务层、存储层、基础服务、监控层等十余个服务组成，也是用户与平台交互的主要入口
2. 外部扫描节点：图中右下角黄色部分，部署在不同云、环境下的扫描节点，通过 HTTPS + 双向证书校验进行通信和身份认证
3. SaaS 安全中台：图中最上方绿色部分，通过 HTTPS 接口为内外部自动化渗透平台提供安全原子能力支撑
4. 外部云基础设施：图中左下方橙色部分，通过云厂商 API 管理外部云资源，提供机器管理、代理服务、端口转发等功能

这里对平台中关键服务和新增模块的功能进行进一步的介绍

* 扫描节点连接器：负责与扫描节点进行通信，包括任务获取、结果回传、状态回传、任务中止检查、节点更新等，同时对消息队列、存储服务等内部服务进行封装和屏蔽
* 消息队列：基于 Redis Stream 封装的消息队列服务，包括提供与队列通信的 API Server 和负责处理消息重回队列等后台任务的 Watcher 服务
* 扫描任务调度：根据配置的策略，对扫描任务进行调度，避免出现某个租户下的任务把所有资源占满等、实现动态调整租户任务并发能力等
* 结果处理：异步处理消息队列中的扫描任务执行结果，包括成功结果入库、任务状态 cache、ack 消息、失败消息重试等
* 队列监控：定时检查队列中消息是否存在异常，如是否有堆积、消息是否长时间未完成、消费者离线消息重回队列等
* 运营运维管理：独立平台，负责客户环境管理、用户管理、角色权限配置、配置管理、扫描节点监控、消息队列监控、更新部署、规则包管理和下发等

对于扫描子任务的运行过程，如下图所示

![](https://mmbiz.qpic.cn/mmbiz_png/1JicUwKQqRQ5hTLganMZaSHT8NXyajiagn4nFEfXLGqX7fia19ibSImYz7AyJ2f8TM0QDYwlwoCj5Txo52dn50Kxfw/640?wx_fmt=png&from=appmsg)

图中包括 8 个步骤

1. 扫描任务通常包含多个步骤，每个步骤会将任务拆分成更小的单元，即子任务，发送到消息队列，进行并发执行
2. 扫描节点定时请求节点连接器，获取要执行的子任务
3. 节点连接器内部会根据节点所属的租户，查询对应的队列是否有消息，然后返回
4. 扫描节点收到任务后，根据参数执行对应的操作
5. 扫描节点执行完成后，会将执行情况回传给节点连接器，包括任务执行状态，任务结果等
6. 节点连接器收到任务回传数据后，会进行

1. 缓解队列消息状态，用于队列监控服务检查消息状态
2. 将结果存入消息队列，等待异步处理

7. 结果处理服务定时从消息队列中获取要处理的任务数据
8. 结果处理服务首先会统一更新业务层任务状态，然后根据不同的任务状态进行不同的操作

1. 任务成功：结果入库、ACK 队列消息
2. 任务失败：请求队列接口对消息进行 Delay 重试
3. 任务中止：ACK 队列消息

# 0x05. 总结

---

本文介绍了为满足商业化需求，同时解决历史架构设计和技术选型问题的背景下，我和团队师傅在 SaaS 自动化渗透平台架构设计的又一次探索和实践，重点解决了扫描节点私有化部署、多租户服务改造、多租户数据隔离等问题。目前新平台已基本成型，并投入使用，我们计划在后续推动旧版向新平台迁移，完成内外部版本的统一

另外后续会不定期地分享关于 SaaS 自动化渗透平台建设和安全研发的一些实践经验和想法，感兴趣的朋友可以微信扫码、或搜索 “b1ngz的笔记本”，关注一波！

![](https://mmbiz.qpic.cn/mmbiz_png/1JicUwKQqRQ5hTLganMZaSHT8NXyajiagnLBs6Eic0MCdrLsNQSuia473CWt9yVkJHIoIFnVYRx653TNswLK9NCgAQ/640?wx_fmt=png&from=appmsg)

# 0x06. 招聘

---

🔥 目前公司正在广纳人才，包括研发、安服、产品、销售、售前等多种类型数十个岗位，复制访问下方链接可看到在招职位详情和在线简历投递

**https://app.mokahr.com/su/5wsls**

**🔥 另外团队目前急招后端研发**，工作地点北京，团队介绍和 JD 如下，感兴趣的师傅可通过以下方式咨询和投递简历，同时也欢迎技术交流

* 邮箱投递：binlin.yan@chaitin.com
* 微信投递：xiaobing1024

团队介绍：我们是长亭科技-产品研发中心-协同创新团队，团队直线汇报给公司创始人

团队职责：深入协同安服，将一线安全攻防经验，转换为自动化平台和工具，通过实战反馈，不断打磨优化，赋能公司业务，构筑公司核心竞争力。同时我们也在积极探索商业化，并取得不错的进展

团队项目：

* SaaS 自动化渗透平台：为安服渗透项目、攻防演练提供工具和平台支持，包括内部版、商业版
* 攻防知识库：支撑公司各产品线的统一知识管理、运营、共享平台，包括漏洞、指纹、POC、利用等
* SaaS 安全实训平台：集学习、训练、考试一体化综合人才培养解决方案，包括内部版、商业版

* 比赛平台：为客户提供 CTF、AWD、安全运营等多赛制的一站式竞赛解决方案和平台支撑

🔥 后端研发 JD：

注：可同时参与上述多个项目的后端开发

1. 具有扎实的计算机基础、网络基础和编程基础
2. 掌握如 Python、Golang 等任意一门开发语言和相关 Web 框架，追求良好的代码风格和质量
3. 掌握如 PostgreSQL、Redis、Elasticsearch、MongoDB 等任意一种数据库的使用
4. 熟悉 Linux 环境操作，掌握 Git、Docker 等工具的使用
5. 具备较强的逻辑思维分析能力，对解决具有挑战性问题充满激情
6. 具有良好的沟通和团队协作能力、热爱技术、责任心强

# 0x07. 参考

---

|  |  |  |
| --- | --- | --- |
| 1 | [云化分布式自动化渗透测试平台 - 架构笔记](https://mp.weixin.qq.com/s?__biz=MzkwNDE5NzUyMA==&mid=2247483673&idx=1&sn=88b42a078e291a2f9b3ef8de515731cf&scene=21#wechat_redirect) | [https://mp.weixin.qq.com/s/HmPLUNDbasuzGHS4K1IG5Q](https://mp.weixin.qq.com/s?__biz=MzkwNDE5NzUyMA==&mid=2247483673&idx=1&sn=88b42a078e291a2f9b3ef8de515731cf&scene=21#wechat_redirect) |
| 2 | [自动化安全工具平台 - 架构笔记](https://mp.weixin.qq.com/s?__biz=MzkwNDE5NzUyMA==&mid=2247483657&idx=1&sn=890bfd44726b334ccaecc5195086aab4&scene=21#wechat_redirect) | [https://mp.weixin.qq.com/s/OMhS9yFlcpI9KOQduSxq9g](https://mp.weixin.qq.com/s?__biz=MzkwNDE5NzUyMA==&mid=2247483657&idx=1&sn=890bfd44726b334ccaecc5195086aab4&scene=21#wechat_redirect) |
| 3 | RabbitMQ Consumer Acknowledgements and Publisher Confirms | https://www.rabbitmq.com/docs/confirms |
| 4 | Flask-RESTful | https://flask-restful.readthedocs.io/en/latest/ |
| 5 | Django ORM vs SQLAlchemy | https://ebs-integrator.com/en/blog/django-orm-vs-sql-alchemy |
| 6 | Example of what SQLAlchemy can do, and Django ORM cannot | https://stackoverflow.com/a/18207001 |
| 7 | SQLAlchemy - The Database Toolkit for Python | https://www.sqlalchemy.org/ |
| 8 | What is multi-tenancy (multi-tenant architecture)? | https://www.techtarget.com/whatis/definition/multi-tenancy |
| 9 | Redis Stream | https://redis.io/docs/latest/develop/data-types/streams/ |
| 10 | Low-latency message queue & broker software | https://redis.io/solutions/messaging/ |
| 11 | Two-way SSL Authentication for REST | https://docs.solace.com/Security/Two-Way-SSL-Authentication.htm |

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/1JicUwKQqRQ55wM3w3dGtfible0uicxQeDqyFZBPL9LV5FLHudXIBZsRxbhaxISNqOoRWHX5vtKtOicIkBYCwlsrJQ/0?wx_fmt=png)

b1ngz的笔记本

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/1JicUwKQqRQ55wM3w3dGtfible0uicxQeDqyFZBPL9LV5FLHudXIBZsRxbhaxISNqOoRWHX5vtKtOicIkBYCwlsrJQ/0?wx_fmt=png)

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