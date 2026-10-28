---
title: G.O.S.S.I.P 阅读推荐 2026-10-27 端到端加密的协作文档系统
url: https://mp.weixin.qq.com/s/IsIoNeu1wM2KnkOjo76zcA
source: Doonsec's feed
date: 2026-10-27
fetch_date: 2026-10-28T07:41:21.274753
---

# G.O.S.S.I.P 阅读推荐 2026-10-27 端到端加密的协作文档系统

# G.O.S.S.I.P 阅读推荐 2026-10-27 端到端加密的协作文档系统

原创

guess
guess

安全研究GoSSIP

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

与合作者一起写论文、与同事一起改申请书，我们早已习惯了“你敲一个字，我这边马上看到”。但如果文档里是需要保密的内容，就需要在保证**文档能被实时共同编辑**的同时，**不让云服务器看到文档的内容**。这篇来自USENIX Security 2026的论文End-to-End Encrypted Collaborative Documents研究的就是：**怎样让多人像使用腾讯文档、Google Docs一样共同编辑文档，同时让云服务器看不到文档内容。**例如，两名调查记者一起写报道，希望能实时看到对方的修改，又不想让提供云服务的公司看到调查材料。这篇文章给出了一套**端到端加密协作文档**（End-to-End Encrypted Collaborative Documents，**E2EE-CD**）的设计，并实现了原型系统。本文给出的E2EE-CD方案是基于Signal群组消息协议及平台来构建的，因此被取名为**SignalCD**。

作者的核心思路很容易理解：文档的编辑者，**把每一次编辑产生的更新，作为加密消息发送给协作者**，并由每个协作者**各自的设备完成文档合并**。服务器只负责转送密文，只有获得授权的设备才能解密密文，而后更新本地文档。在具体实现SignalCD时，作者基于Signal群组消息协议及平台，将每份协作文档对应到一个Signal群组，通过群组通信传递加密的编辑更新。Signal服务器负责转送密文，获得授权的协作者在自己的设备上解密，并使用Automerge将修改合并到本地文档中。这样，“安全传递更新”和“正确合并修改”就可以由两个模块分别完成，再组合成端到端加密的协作文档系统。

![](https://mmbiz.qpic.cn/mmbiz_png/eQ0Wf6rqolVOOX38FibdDIB0Cd2DmIvZDzk5ib0rh6ib74Tmeac0CLp8aTyb0Kf2SZNiaZaicicJMvH4wDxvQOcIFW03VYTXJ6SxiaDoI7fW8T9vjo/640?wx_fmt=png&from=appmsg)

上图展示了用户通过SignalCD创建、共享和协同编辑文档的流程。首先，用户通过扫码将SignalCD客户端关联到已有的Signal账户。在创建文档时，SignalCD建立一个对应的Signal群组，创建者成为首位成员；在共享文档时，用户提供协作者的电话号码或Signal用户名，系统将其加入该群组。编辑过程中，SignalCD首先调用Automerge将修改应用于本地文档，再将修改序列化，通过Signal群组以加密消息的形式发送。其他协作者收到消息后，将其反序列化为文档更新，并调用图中的协调机制Rec，即Automerge的合并机制，更新各自的本地副本。这样，Signal提供安全的消息传递，Automerge负责客户端的修改合并，使各副本在收到并处理相同更新后保持一致。整个方案并不要求服务器去阅读、理解或处理明文，也不依赖同态加密去完成密文文档的合并，而只需要协作者自己的设备来对内容进行处理。有人暂时离线时，其他人仍可继续修改；离线者重新上线后收取错过的更新，再在本地合并。

这里最关键的一步，是让每个人“自己合并”之后还能得到同一个结果。比如两个人同时在同一处输入文字，如果只按消息到达顺序拼接，一边可能得到“张三李四”，另一边却得到“李四张三”。为避免这种不一致，论文要求合并机制满足**强收敛性**（Strong convergence），通俗地说就是：从同一份文档出发，只要最后收齐了同一批修改，即使收到的先后顺序不同，最终文档也应一致。本文设计的SignalCD，利用Automerge来让设备按照共同的规则合并操作。

在SignalCD的具体设计与实现方面，作者先明确了安全协作文档应满足的功能与安全要求，例如：用户应能够与其他用户共享文档；管理员能够分配只读、读写或管理员权限；管理员应能够归档或删除文档；多名用户能共同编辑一份文档，并进行近实时的并发编辑；允许部分协作者离线，并在其重新上线后同步更新；从相同文档状态出发，各方在处理完同一批修改后，应得到一致的文档结果等。在此基础上，作者给出一个形式化模型，明确“**什么才算是安全的协作文档**”，给这些要求一个可检验的定义：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/eQ0Wf6rqolUlXGquicUibEp5Py9Z8UyickESStkiary749dc0yBjhjluuiaYcMUmoQBjhYG2kbWpdB4z2JF5XeQw07nlia2iaYuOibh6o4FsxFn13DY/640?wx_fmt=png&from=appmsg)

上图可以理解为一份作者定义的“系统行为规范”。以共享操作为例，FCD.share(uid, did, uid′, perm, msg)代表管理员uid想授予用户uid′文档did的访问权限perm，而后通知用户uid′并附上msg这段消息。下面的伪代码表示要实现这个目标所要进行的操作，第1行记录认证过程中允许向攻击者泄漏的信息，第2-4行检查授权条件并处理授权失败的情况，第5行更新用户uid′的权限，等等。这里第2行的if语句判定条件中，uid≠uid′代表授权发起人与授权接收人不同，T[did, uid]≠admin代表授权发起人对这份文档没有管理员权限，perm∉PermSet代表要授予的权限不属于系统支持的权限，以上任意一项成立时，授权操作被拒绝执行。因此，小编怀疑这里的uid≠uid′是笔误，应把≠改为=，即当授权发起人与授权接收人为同一人时，不执行授权操作，当然具体情况仍需向作者确认。

之后，作者证明了自己的方案满足这套要求，证明过程放在了原文的附录A，感兴趣的读者可以自行阅读（这里只放出了部分的截图）：

![](https://mmbiz.qpic.cn/mmbiz_png/eQ0Wf6rqolUVr7jXppIqFP2krMZAOCrRkegfCLgoWTz0tJgnLhUGZyFvY6GCoUzUSE6PbIOXQ3uQUiaiaXLF33SAHK2pbNibF0KjvGKHHd1TZE/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/eQ0Wf6rqolUaWTZC6LL2Gl2GFiaV4MKtgWoIUzNZsEnvORMk1zMllBg6EKezzexz5CIYj9V6WDQiawh2ZrE0D3DvRfyRThqTRuWYBiaL1a2Ziak/640?wx_fmt=png&from=appmsg)

此外，作者还指出，这套思路的价值在于可替换性：合并模块不必固定为Automerge，通信模块也不必固定为Signal。

实验方面，作者首先测试了加密、发消息、本地合并这一套流程，会不会慢到没法实现共同写作。实验部署在一台配备M2 Max芯片和32 GB内存的MacBook Pro的Docker容器中，由两个用户端使用两个Signal账号模拟协作过程，并通过真实Signal服务收发消息，同时设置了慢速与快速两种网络条件。在双人同步编辑实验中，每次单字符编辑都单独发送一条消息。下图中，最右侧的Total是一次更新的总延迟，可以看出实验测得的**端到端总延迟中位数约120 ms**。按照一般的打字节奏，通常对方还没输入下一个字，这一次修改就已显示出来。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/eQ0Wf6rqolXchDEiakxibK4eA9vic1Jjdl2Ribnjia0u4H9RtAXibLObWsYUTWGq9gBdUy7fIQtZqUqfN17keiaE8ricvV34ChdK2IGoib0OTq5ZzDM8/640?wx_fmt=png&from=appmsg)

论文另指出，单次更新的本地合并耗时不到2毫秒，相比网络传输耗时很小。这一结果说明该原型系统在该测试条件下可以实现实时协作。

此外，作者还测试了用户离线回来后的“补课”速度：启动一个新的signal-cli客户端大约需要2.4秒，之后每秒可以接收约460条单字符更新。对于一次粘贴很长一段文字的情况，作者测试了最多一次插入50,000个字符的操作，**本地合并耗时仍小于150毫秒**。

![](https://mmbiz.qpic.cn/mmbiz_png/eQ0Wf6rqolU3O41xSdewGjd8mW3LRDDN4icfXswM8kKkfRs5RFFvWu0mXZcnUK7ByOJ7OW3VrvEKGTmHF8ichHfuxTtzZOCjerRXU11HCvjCM/640?wx_fmt=png&from=appmsg)

这篇文章带给我们的启发是：当服务器无需理解编辑内容时，成熟的**加密通信**与**本地合并**机制，就足够组成一套实用的、端到端加密的协作系统。

---

原文链接：https://www.usenix.org/conference/usenixsecurity26/presentation/knabenhans

开源仓库：https://github.com/spring-epfl/signal-collaborative-documents

预览时标签不可点

不喜欢

![]()

微信扫一扫
关注该公众号

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/uicdfzKrO21EibxMcqx9KdafugxDicBiaW3cb1gyTuWooDCJjH1ibu8aibOiapYLq8BJMwNbIeUK1t0japdvmdqTfCxhg/0?wx_fmt=png)

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