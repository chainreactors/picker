---
title: 联邦学习开源框架FATE-Flow 源码分析
url: https://mp.weixin.qq.com/s?__biz=MzIyODYzNTU2OA==&mid=2247494117&idx=1&sn=ef34d6d8e0b6bff9b71addecc569bb6c&chksm=e84c4f3adf3bc62cbf708906a4173e3503fe35613848b002f15bd2e5e75d7d0cabc29d02de20&scene=58&subscene=0#rd
source: 绿盟科技研究通讯
date: 2023-01-12
fetch_date: 2025-10-04T03:39:53.837472
---

# 联邦学习开源框架FATE-Flow 源码分析

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/hiayDdhDbxUaZsGv76kAutXkicbFhibGZnqcnuEiaSLUOm9A2GHLuwnpU7WpfDGiaOdQKxwXJmUDLibE0V0sx2ymwpUw/0?wx_fmt=jpeg)

# 联邦学习开源框架FATE-Flow 源码分析

原创

创新研究院

绿盟科技研究通讯

![](https://mmbiz.qpic.cn/mmbiz_gif/hiayDdhDbxUaZsGv76kAutXkicbFhibGZnqZ5iaTDmyXYokKFze6GAOIdy4Oq1na0ckKQgUprXFFUmfEjhiaBDyibVAg/640?wx_fmt=gif)

一.  FATE整体架构

FATE是首个工业级的开源联邦学习框架，据中国信通院数据显示，55%的国内隐私计算产品是基于或参考了开源项目，其中以FATE开源项目为主。FATE实现了基于同态加密和安全多方计算的安全协议。FATE支持横纵向联邦学习场景，包含了多种联邦学习算法，包括逻辑回归、secure boost、深度学习等。FATE提供了联邦学习全流程的解决方案，具备开箱即用的特点。FATE整体架构和基本流程如下图1、2所示，本篇文章将主要介绍联邦学习任务调度的核心：FATE-Flow。

![](https://mmbiz.qpic.cn/mmbiz_png/hiayDdhDbxUaZsGv76kAutXkicbFhibGZnqTHRK8yQ7DbcQTv0PvI0JyIiaWhtbbLmmodJiaU7zicLMT9ahTZ3qwpWDQ/640?wx_fmt=png)

图1：FATE整体架构

![](https://mmbiz.qpic.cn/mmbiz_png/hiayDdhDbxUaZsGv76kAutXkicbFhibGZnq9yP6bpzPayOjksv8qJHZxZrGC1LJ8okok7lzCc9uK9gDVHYslfibWTg/640?wx_fmt=png)

图2：FATE流程

二.  FATE-Flow架构

FATE-Flow提供了端到端的联邦学习任务流水线管理模块，架构如图3所示。

![](https://mmbiz.qpic.cn/mmbiz_png/hiayDdhDbxUaZsGv76kAutXkicbFhibGZnq7VkibEXsrg8hPjmWSFpdsAfZw9JRKd51Nwud1L01thyTj1tibxyV1VHg/640?wx_fmt=png)

图3：FATE-Flow流程

在FATE-Flow中，由如下几个关键模块：

* DAG：定义了流水线，使用JSON格式的DSL来定义DAG。
* DSL Parser：是调度的核心，通过 DSL parser 解析到上下游关系及依赖。
* Job Scheduler：一个DAG作为一个Job，而DAG中的节点称为Task，一个Job由若干Task组成。
* Task Controller：最小的调度单位，FATE-Flow将Task的执行独立为隔离的进程。
* Data Manager：用作数据的上传、下载等。
* Resource Manager: 负责计算整个Job需要的资源的大小，返回资源申请状态等。只有多方资源申请成功，才会向各方发送start job指令。

提交一个Job的流程如下：Job首先提交到Queue中，JobScheduler解析DAG加入到Task Queue中，调度 Executor执行，同时这个任务会分发到联邦学习的各个参与方。在任务执行中会收集参与方状态，进行下一步的调度。Task stat记录Task的状态信息，例如启动时间、运行状态、结束时间、超时时间等。如果Task运行时间超过默认超时时间、异常终止或者正常运行，则启动shutdown，结束进程，清理任务，同步到所有联邦参与方，保证任务的一致性。

三.  源码分析

FATE-Flow后端使用的是Flask，Flask是一个轻量级的python web框架，FATE-Flow server的程序入口是在python/fate\_flow/fate\_flow\_server.py。如图4所示，通过源码分析，我们发现启动了两个server：9380端口的http server 和9360端口的grpc server。http接口用作自身api的调用，而grpc 则用作参与方间函数调用。

![](https://mmbiz.qpic.cn/mmbiz_png/hiayDdhDbxUaZsGv76kAutXkicbFhibGZnqSGUAEM0ymRgFu7Te0MoFFScytj3Uo7utCQsHyibfEnem6GhIiaJ1JpgA/640?wx_fmt=png)

图4：Flask启动http server

熟悉Flask的朋友都知道，Flask使用蓝图来组装不同的组件，在Fate-Flow server中同样如此。在apps目录下构成了后端程序的基本组件，其中主要包含：

* checkpoint\_app: 数据/模型更新
* component\_app.py：获取组件详情，验证组件参数
* data\_access\_app.py：数据上传及下载
* info\_app.py：获取mysql、fateboard、eggroll版本信息
* job\_app.py：核心，提供job、task、查询等接口
* table\_app.py：数据表的操作，通过mysql导入数据也是在这里完成的
* tracking\_app.py：获取组件的状态，包括获得组件的输出也是在这里完成的
* version\_app.py：显示FATE相关版本信息，其中docker-compose部署healthy检查就是通过此接口。
* log\_app.py：负责log相关接口，解决了之前版本中fateboard无法获取部分log的bug
* permission\_app.py：权限控制相关接口
* model\_app.py：模型下载、部署，用作在线推理

3.1

轮询检测与调度

如图5所示，Detector每5s执行一次，负责检测运行中、结束的Job、Task、资源等；而DAGScheduler每2s执行一次，依次调度waiting、running、ready、rerun状态的Job，更新结束 Job的状态。

![](https://mmbiz.qpic.cn/mmbiz_png/hiayDdhDbxUaZsGv76kAutXkicbFhibGZnqFoI5IllsQhgQ4ibckZwkQibZDVcSgcEpVrW3gB7QksEa6NImVxUzUJ9Q/640?wx_fmt=png)

图5：两个轮询方法

3.2

从提交Job分析源码

job\_app接收请求

用户通过flow client cli提交任务，其实是向FATE-Flow server的9380端口发送http请求，在job\_app中接受请求后，调用DAGScheduler.submit。

DAGScheduler提交Job

如图6所示，DAGScheduler的submit方法生成Job id，进行Job相关配置，调用FederatedScheuler.create\_job方法通知各方创建Job。这一步实际上是调用了federated\_command 方法，通过grpc向各参与方发送rpc或http请求。initiator为每一方、每一个task初始化，并记录在数据库中（见t\_tack表）。如果均未出错，则将Job的状态设置为WAITING。

![](https://mmbiz.qpic.cn/mmbiz_png/hiayDdhDbxUaZsGv76kAutXkicbFhibGZnqbRPHDaFxVrXGeXhlV2X5y56FAiccL17uQoA0viagBsYqWGJTicrblaRXA/640?wx_fmt=png)

图6：发送http或rpc请求各方创建Job

![](https://mmbiz.qpic.cn/mmbiz_png/hiayDdhDbxUaZsGv76kAutXkicbFhibGZnq1uppw5G6Xd1pjrkcds90XgZaUkuMhabLVHUvoTEia3oTCDQdGTlCyiaw/640?wx_fmt=png)

图7：initiator记录Task信息

DAGScheduler调度waiting的Job

在2.1 节中我们提到过，DAGScheduler每2s一次调度Job。对于waiting状态的Job，DAGScheduler首先检查Job的状态是否被取消，然后尝试在各方申请资源，如果资源申请成功则调用start\_job开始Job，向各个参与方发送开始Job的请求。各个参与方在收到请求后，将Job状态改为RUNNING。

![](https://mmbiz.qpic.cn/mmbiz_png/hiayDdhDbxUaZsGv76kAutXkicbFhibGZnqZgKXpicv85yfqzvgsvcGkk3h2s6BCPpiaTzZ7lX7cUQ7TaD1YyR67kicw/640?wx_fmt=png)

图8：各参与方开始Job

DAGScheduler调度running的Job

对于running状态的Job，实际调用的是TaskScheduler.schedule方法，在该方法中，获取所有Task，并将Task的状态同步。对于WAITTING状态的Task，调用start\_task方法开启Task。initiator 向各方发送start task的rpc请求。

![](https://mmbiz.qpic.cn/mmbiz_png/hiayDdhDbxUaZsGv76kAutXkicbFhibGZnqahTU4DVpFaX1tVZgg9KoqvibwFvzrxNHtRWXBfqyA1mpgHd2lJQUYEw/640?wx_fmt=png)

图9：向各方发送start\_task请求

TaskController执行Task

在收到start\_task的rpc请求后，各方调用TaskController的start\_task方法，对于eggroll引擎来说，实际上是启动python子进程。

![](https://mmbiz.qpic.cn/mmbiz_png/hiayDdhDbxUaZsGv76kAutXkicbFhibGZnqJ5MP5scNa890TxDic7PTOgFtjsibp2iaRibEyKgKPYL4dzA71UM7GBNO3w/640?wx_fmt=png)

图10：启动python子进程

**计算Task、Job状态**

在完成Task后会计算各参与方的状态，如图11所示，分为以下几种情况：全部都是waiting状态、存在interrupt状态、存在running状态、waiting和success状态、全部都是end状态。

![](https://mmbiz.qpic.cn/mmbiz_png/hiayDdhDbxUaZsGv76kAutXkicbFhibGZnqabmvp3l7emWdyqiaf9szRU3AUl5hrdpNF4kcbkKSP2iaOb0wJDibh3gow/640?wx_fmt=png)

图11：状态计算

四.  结语

如果说FederatedML是大脑，那么FATE-Flow就是骨架。FATE-Flow从整个任务生命周期的管理，到上层对外暴露API结构，在整个联邦学习中起着举足轻重的作用。无论是各个厂商在开发自家的隐私计算平台，还是个人用户使用命令行工具，其实都是在与FATE-Flow server打交道。在最新的1.9版本中，FATE-Flow也增加了新的功能：例如授权认证、负载均衡等。由于篇幅所限，本文仅从Job提交的角度来分析FATE-Flow的流程，感兴趣的同学也可阅读相关源码。

内容编辑：创新研究院  高翔

责任编辑：创新研究院  陈佛忠

本公众号原创文章仅代表作者观点，不代表绿盟科技立场。所有原创内容版权均属绿盟科技研究通讯。未经授权，严禁任何媒体以及微信公众号复制、转载、摘编或以其他方式使用，转载须注明来自绿盟科技研究通讯并附上本文链接。

**关于我们**

绿盟科技研究通讯由绿盟科技创新研究院负责运营，绿盟科技创新研究院是绿盟科技的前沿技术研究部门，包括星云实验室、天枢实验室和孵化中心。团队成员由来自清华、北大、哈工大、中科院、北邮等多所重点院校的博士和硕士组成。

绿盟科技创新研究院作为“中关村科技园区海淀园博士后工作站分站”的重要培养单位之一，与清华大学进行博士后联合培养，科研成果已涵盖各类国家课题项目、国家专利、国家标准、高水平学术论文、出版专业书籍等。

我们持续探索信息安全领域的前沿学术方向，从实践出发，结合公司资源和先进技术，实现概念级的原型系统，进而交付产品线孵化产品并创造巨大的经济价值。

![](https://mmbiz.qpic.cn/mmbiz_jpg/hiayDdhDbxUbrbTJxY0Qv9BtgtXZsYVvaVUtlPicCUV6qDBGgZnrxicAMwvibG73JUu0w1UweTicfkuTRIyJyt77C5Q/640.jpeg?wx_fmt=jpeg&wxfrom=5&wx_lazy=1&wx_co=1&retryload=2)

**长按上方二维码，即可关注我**

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/hiayDdhDbxUYc15Dsy8RcPfwerHzBEhBVQk20S88RRtnlBS56ZnUv3JStz1JUyyBicDvreCNoDaJZ8ul5xxtWRmg/0?wx_fmt=png)

绿盟科技研究通讯

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/hiayDdhDbxUYc15Dsy8RcPfwerHzBEhBVQk20S88RRtnlBS56ZnUv3JStz1JUyyBicDvreCNoDaJZ8ul5xxtWRmg/0?wx_fmt=png)

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