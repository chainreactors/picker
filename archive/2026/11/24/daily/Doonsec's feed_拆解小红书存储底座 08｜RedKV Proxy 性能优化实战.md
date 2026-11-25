---
title: 拆解小红书存储底座 08｜RedKV Proxy 性能优化实战
url: https://mp.weixin.qq.com/s/oq3tDxarsJ2JLcB1qSBzOQ
source: Doonsec's feed
date: 2026-11-24
fetch_date: 2026-11-25T10:41:26.855183
---

# 拆解小红书存储底座 08｜RedKV Proxy 性能优化实战

# 拆解小红书存储底座 08｜RedKV Proxy 性能优化实战

原创

REDtech
REDtech

小红书技术REDtech

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

![](https://mmbiz.qpic.cn/mmbiz_jpg/P9Hs04VFGRnx0eTibUicEUeEymMC0297XicB7SHvFsEqo6A6ekuybZzlkLzk2LyfRWg4KicviaANrorO3YicULzcBibgnW6JibsvAQvTbYA35oibcY4c/640?wx_fmt=jpeg&from=appmsg)

**前言**

小红书统一存储数据库云平台是自研的一站式数据基础设施，覆盖 MySQL、Redis、RedKV、RedTable、RedVec 向量库、对象存储 ROS 等 10+ 产品，从缓存、事务到分析、AI 场景全都有托管服务。面对海量数据下选型分散、部署复杂和运维成本高的问题，团队将不同引擎整合为稳定、易用、低成本的产品矩阵。本篇聚焦其中的键值存储产品 RedKV，沿着 Proxy 与 InternalSDK 的请求链路，介绍如何减少 CPU 和内存开销、提升收发效率，并控制突发请求的长尾。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/P9Hs04VFGRmRpeA0YemjtgmRkWX7M3roJArebibIJosTRc5qZ1mic0Ga1hGvLibAzNpBCcmbVVEuFQurppjWgiaTayfxcysMAD6JIGJRoSDPaC0/640?wx_fmt=png&from=appmsg)

**01**

**沿着一次请求，找到真正的成本**

RedKV Proxy 为客户端提供 Redis 协议入口，V3 路径通过 InternalSDK 访问 KVServer。InternalSDK 的数据收发复用 Proxy 工作线程的事件循环，管理连接、请求队列和完成回调。

![](https://mmbiz.qpic.cn/mmbiz_png/P9Hs04VFGRmEy9YO3eekyntiazTO5PibyziciaZehLQtXywfexRjTia0fjMbGCMC7SNMFRRAaI5DoqwYsgEDKBu4YxGGB5JydElKUrKJ8notql0k/640?wx_fmt=png&from=appmsg)

*图 1：优化覆盖代理与 InternalSDK，后端执行成本单独评估。*

不同负载的瓶颈并不相同。小 GET 更容易受对象构造、解析和状态登记影响；大 GET/SET 更容易受内存搬运和收发批量影响；大 MGET 则可能长时间占用事件循环，让其他请求等待。

定位时，我们结合采样、反汇编和 I/O 计数，检查具体多做了什么。验证收益时关闭探针，隔离编译与测试负载，交替运行优化前后版本，同时观察吞吐、每请求 CPU 时间、P99 和错误计数。结果波动时补充预热、交换端口，保留不利窗口。

对照配置同样需要核实。早期 V2 使用静态路由，V3 使用真实拓扑，不能直接据此归因架构差距。补齐对照后，证据将关注点指向非路由提交中的对象搬运、构帧和队列记账。

**02**

**小请求：减少重复解析和状态搬运**

前端已经得到的命令、参数、key 和帧长，沿调用链交给 SDK，首次路由结果也继续复用。重试与拓扑变化仍重新选路。流式 RESP 定界按长度跳过数据体，常见命令分类和协议字段编码采用轻量路径。

请求对象由工作线程内的池复用，只重置实际使用的子请求，避免每次完整重建全部内联对象；过大的临时容量在归还时释放。内部提交通过引用转发，减少中间对象的移动与析构，公共接口仍保留原有所有权契约。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/P9Hs04VFGRlF9S66E0ib8jXoyVrGwKOnNoKQYWdoVwdIvBcQ9RCz4o9wJ1rChqGarO1ZuEibLFfNwwuIxnZEfaic2iahQDGtz7gncTHcJ4JN3YU/640?wx_fmt=png&from=appmsg)

*图 2：合并 SDK 内部存储，同时保留代理的请求身份保护。*

原先 SDK 通过独立哈希表保存完成回调。现在回调随请求进入既有队列，完成时直接取出。取消时，尚在待发队列的请求直接摘除；已进入传输队列的请求取走回调，保留占位，继续按顺序排空回复。代理侧仍按请求 ID 验证身份，避免迟到回复访问被对象池复用的地址。

正常递增 ID 可跳过查重扫描，持续乱序 ID 仍需线性查找，这是明确的适用边界。该改动在小 GET 独立对照中提升吞吐约 0.60%～1.47%。

路由侧增加读主快速路径、位图副本选择和按需建连；热点检测复用哈希指纹，减少完整 key 比较。缓存查询使用 namespace 与原始 key 的结构化索引，缓存命中及冷请求未命中时避免额外复制 key。

**03**

**大请求：让数据与所有权一起传递**

减少大 value 的复制，需要同时明确缓冲区何时可以释放。

普通三参数 SET 保留前端内存块链上的范围。V3 参数体达到 4KiB 时，可复用只读分片，仅构造 RKV 协议头与元信息，再聚合发送。发送队列持有缓冲所有权，部分写入只推进偏移，请求取消不会提前回收未发送数据。

GET 则从后端接收区直接提供回复视图。编码后的完整 RESP 回复达到 128B、且预算允许时，前端输出队列可持有接收块，直到发送完成。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/P9Hs04VFGRkCvHVOaOky6cfibaSqKcxTBBVx4100bvNibwlibdJj2b42QCuyklFWTbeZp93mgFSwOca1KxJPdu6kMpC43XJrcMOwylET6mzS70/640?wx_fmt=png&from=appmsg)

*图 3：借用按整块容量计费，慢客户端不能无限延长无预算的持有。*

这里的“零拷贝”针对代理用户态的整包复制，内核收发仍有复制。解压、聚合等路径也可能需要连续数据。预算不足时保留原处理路径，存在外部引用时不覆盖接收块，换块只搬移未解析尾部。

公共内存块默认从 4KiB 调为 16KiB，减少块数和元数据操作；池按需分配，默认硬上限为每工作线程 256MiB，空闲缓存另设上限。

压缩同样需要避免无效工作。V3 默认使用 LZ4，从 2KiB 开始尝试；低于阈值的普通 SET 继续走分片路径。解压先计算所需长度再申请空间，复用临时缓冲并释放过大容量。压缩收益取决于数据可压缩性和瓶颈位置。

**04**

**有界批处理，让吞吐与长尾一起改善**

同一轮产生的请求和回复，在事件循环末尾集中发送，减少重复调度。部分写入后按实际字节继续推进，不增加等待攒批的定时器。

![](https://mmbiz.qpic.cn/mmbiz_png/P9Hs04VFGRky1ZiaWCB4fTibY5xEuiaiaCapoYkloUKrCya9ZdVGeLwgTN0KhUnLjJHD98jd2AicgSL3WJJ35NjOEvJOybsgwaSMxJzpBNbJiaMibM/640?wx_fmt=png&from=appmsg)

*图 4：短请求保留原组批边界；大回复扩容受容量、协议和预算限制。*

短 GET 的一次发送仍可能包含很多分段。最终方案先按原来的 64 个分段上限选批：若每条完整帧均不超过 80B，就复制到最多 5KiB 的临时栈空间，以一个分段发送。这里付出小块复制，减少分段处理成本；长请求和混合批次继续使用原路径。

大 GET 的问题恰好在接收侧：旧回复仍被借用，后续半帧占住大部分空间，一些读取只能填入 2～4KiB 的块尾。满足大半帧、持续待收及预算等条件时，接收区有界扩一档。64KiB GET 的接收调用从约 1.06～1.10 次/请求降到 0.57～0.62 次，前端也能一次交付更多回复。

批处理还要及时让出执行机会。只限制顶层命令数量，无法约束 MGET 展开的后端工作量。因此输入处理增加 100μs 时间预算，在命令之间检查并续调度，单条巨型命令仍是边界。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/P9Hs04VFGRn00cRU93bKQjWyqLCm1Gl4HRJftpFZEnKtjNdvPgeSfNh97WBDh9xucIy7fPqSVDq6ZmzPX3myVibokVianFBYMBoM99qdFS9zI/640?wx_fmt=png&from=appmsg)

*图 5：时间预算检查发生在命令之间，时间块仅表示执行顺序。*

专项复现中，连续投递每条含 500 个 key 的大 MGET，另一连接的 PING P99 约从 375ms 降至 1.3ms。共享开发机的小 GET 对照也曾出现约 1.7%～2.95% 的吞吐下降，公平性检查有其成本。

队列管理则通过回写游标和直接摘链，避免每次完成都重扫队头，使 N 个请求、M 次回写的检查量降为 O(N+M)。共享预算释放时，只唤醒真实等待者，减少无关遍历。

**05**

**用端到端实验决定保留什么**

下表整理自各阶段独立 A/B 的历史记录，主要条件是 Linux 本机、单工作线程、三副本、只读主、关闭压缩和缓存、8 条连接，每连接最多 16 条请求在途。各行基线不同，收益不能相加，也不代表最新主干的整体性能提升。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/P9Hs04VFGRkm5nM31SnqL84vp3fVEHH9aPY8wq0HRicv6facYxHNDIumUsRmgsjNUpAic8d0yibCicbn7OLmtC0ZMSwcUqA70JGhUIQOpic8Siap8/640?wx_fmt=jpeg&from=appmsg)

收益之外的代价必须一起看。短请求合并首组吞吐下降 0.91%，pipeline 为 1 时没有明确收益；大回复扩容每触发连接多保留约 130KiB 工作区，大包后切回 8KiB 时出现约 1.51% 回退。

一次撤回实验更有启发性：解压回复直接交付前端，省掉一次复制，用户态 CPU 指标下降，但 4KiB/256KiB GET 吞吐分别下降 27.7%/20.1%。缓冲寿命延长改变了分配器复用，增加内核还页成本。最终保留了原池化复制路径。

缓存和副本读还涉及一致性取舍。缓存默认开启，每个工作线程的主 SDK 实例默认有 16MiB 逻辑预算，这不是进程内存上限。GET 按请求实际生效的读策略判断：LeaderOnly 跳过缓存读取，热回复仍可回填；READONLY 可覆盖读策略，其他允许缓存的策略可能返回旧值。

历史测试覆盖取消、迟到回复、部分写入、预算回退及慢读，并完成阶段性的集成与持续压力验证。这些结果不替代最新主干或生产规模验证。

后续将继续量化小 GET 的提交成本，评估多线程、多分片、跨机及混合大小负载。每项优化都要说清：省掉什么工作、增加什么成本、证据在哪些条件下成立。

**下一篇预告：**

下一篇（09 篇）将介绍多云存储网关在小红书的落地实践，敬请期待。

.

**作者简介**

* 文书：小红书非关系型数据库研发工程师，主要负责小红书KV存储内核开发。
* 叶天：小红书非关系型数据库团队负责人，关注非关系型数据库架构、产品的研发和交付。

**部门介绍：**

存储&数据库部，为小红书全业务场景打造行业一流的高可用、高可靠、高性能、低成本的存储和数据库类产品技术服务。团队致力于用精英化的组织和行业领先的技术理念，先于业务布局和行动，为公司业务的快速发展提供充足“弹药”，同时也让小红书存储和数据库成为行业该领域的标杆。

.

**招聘信息**

NoSQL数据库研发工程师/专家：小红书招聘

数据库中间件研发：小红书招聘

![](https://mmbiz.qpic.cn/sz_mmbiz_png/P9Hs04VFGRm0lGxbMlFAJ1Wqe6f3PYxR3zckSoW2AicUvy98uybIPn7Cbx0WuxZ7EooC5Riau4eBXSib64ibIBiaGyPkeI5vtice0F7Gl7h84fmYI/640?wx_fmt=png&from=appmsg)

精彩回顾：

[拆解小红书存储底座 00｜从孤岛走向融合：小红书存储与数据库架构进化](https://mp.weixin.qq.com/s?__biz=Mzg4OTc2MzczNg==&mid=2247496855&idx=1&sn=f426a8f58708ca0fbef34b7e3308e468&scene=21#wechat_redirect)

[拆解小红书存储底座 01｜多源数据传输总线 RedDTS 2.0](https://mp.weixin.qq.com/s?__biz=Mzg4OTc2MzczNg==&mid=2247496885&idx=1&sn=fcecfc62b3f876191ebaf931ace2ecc4&scene=21#wechat_redirect)

[拆解小红书存储底座 02｜让 AI 成为团队的一员：存储数据库助理实践](https://mp.weixin.qq.com/s?__biz=Mzg4OTc2MzczNg==&mid=2247496958&idx=1&sn=bafda0c7a7030b5542ae6c54f26876d5&scene=21#wechat_redirect)

[拆解小红书存储底座 03｜从存得下到读得快：小红书自研对象存储实践](https://mp.weixin.qq.com/s?__biz=Mzg4OTc2MzczNg==&mid=2247496995&idx=1&sn=4f8f5120b9fff8d77f0c8c9d9c590fee&scene=21#wechat_redirect)

[拆解小红书存储底座 04｜从对象到文件：RedStore SSD 引擎与 RedFS 的设计与实践](https://mp.weixin.qq.com/s?__biz=Mzg4OTc2MzczNg==&mid=2247497095&idx=1&sn=c498a5620224ad5b758fbcd3b4276e22&scene=21#wechat_redirect)

[拆解小红书存储底座 05｜RedTAO 2.0：万亿级图数据库的设计与实践](https://mp.weixin.qq.com/s?__biz=Mzg4OTc2MzczNg==&mid=2247497156&idx=1&sn=a65da187452ec808edf599fd8589362b&scene=21#wechat_redirect)

[拆解小红书存储底座 06｜RedDB：小红书自研多模数据库的设计与实践](https://mp.weixin.qq.com/s?__biz=Mzg4OTc2MzczNg==&mid=2247497170&idx=1&sn=0b57353788f1e32f852d516e58a7d6c6&scene=21#wechat_redirect)

[拆解小红书存储底座 07｜MySQL性能优化设计与实践](https://mp.weixin.qq.com/s?__biz=Mzg4OTc2MzczNg==&mid=2247497202&idx=1&sn=d31570ef4e2d1f732427a8e203a9f119&scene=21#wechat_redirect)

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/vxnkL2N86IsWfuArZ4Oibu3JjynORoXVKc5OaGgUib1G8yiam3A5HlC2PDpDw1qTu4lasuiakZ76vRsf3KJNKiaye5w/0?wx_fmt=png)

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
推荐
，轻点两下取消推荐
分享
留言
收藏
听过