---
title: TPC-C too simple？一文详解 TPC-E：TPC-C 的升级版
url: https://mp.weixin.qq.com/s?__biz=MzI1MzYzMjE0MQ==&mid=2247509226&idx=1&sn=b00442b19de31d4a1ffbd64a762f20f3&chksm=e9d36f08dea4e61ea6a49a57173fc04c3e9f22dd9996886c73159869da61f7e45d07c53ca383&scene=58&subscene=0#rd
source: 字节跳动技术团队
date: 2024-08-25
fetch_date: 2025-10-06T18:02:42.352873
---

# TPC-C too simple？一文详解 TPC-E：TPC-C 的升级版

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/5EcwYhllQOhIogOQhodD9em5ZG7AlpW4dSoPcrVeVujV3PVaQzgUk6sRdZIb3myRLqSib4icY17JoiaIbc6KtGeNQ/0?wx_fmt=jpeg)

# TPC-C too simple？一文详解 TPC-E：TPC-C 的升级版

康荣

字节跳动技术团队

# 从 TPC-C 到 TPC-E

在数据库评测领域， TPC-C 可能是最出名的OLTP 基准测试（benchmark）之一了。各大数据库产品为展现其性能强大，纷纷在 TPC-C 性能榜上你方唱罢我登场。Oracle 一度独占鳌头，阿里 OceanBase、 腾讯 TD-SQL 也轮番登顶。达梦、TiDB、TBase 等等也纷纷用 TPC-C 作为自身产品的性能衡量标准。不仅如此，TPC-C 也在许多下游任务中频繁亮相，例如参数调优任务、负载预测任务、索引推荐任务等等。

然而，TPC-C 作为一个1992 年推出的 OLTP benchmark，库表结构、事务类型、业务场景都显得“过于简单”了。为了应对数据库领域的发展，TPC 委员会在 2007 年推出了下一代 OLTP 基准测试：TPC-E。

在 TPC-E 官网 上，官方开宗明义：**「TPC-E 比」** **「TPC-C」** **「更加复杂，因为它的事务类型更多样化、库表结构和执行结构更复杂」**：

> ❝
>
> TPC-E is more complex than previous OLTP benchmarks such as TPC-C because of its diverse transaction types, more complex database and overall execution structure.
>
> ❞

TPC-E 相比 TPC-C 的复杂性是显而易见的，我们仅列举一些：

|  | TPC-C | TPC-E |
| --- | --- | --- |
| 模拟场景 | 简单的批发商系统 | 复杂的证券交易所系统 |
| 事务类型 | 5 种 | 12 种 |
| 库表 | 9 张表 | 33 张表 |
| 数据生成 | 随机数，均匀分布 | 真实数据规律，有倾斜（skew） |
| 复杂 join | 最多 2 表 join | 最多 7 表 join |
| 读写比 | 1.9:1 | 9.7:1（读负载比例更高） |

相比 TPC-C 威名赫赫，TPC-E 由于其复杂而显得小众，在工业界和学术界并没有被广泛地用于性能测试。然而在 TPC-C 已经被研究透彻、各大厂商的评测中纷纷“过度优化”的如今，TPC-E 基准测试不失为一种新的、良好的补充。

本文接下来你会看到：

1. **「概览全貌」**：对 TPC-E 做一份详细的讲解，展现 TPC-E 的场景、库表与事务全貌。
2. **「实践挑战」**：借助 “MySQL 索引优化” 这一场景，展现 TPC-E 对现有技术带来的新的挑战。
3. **「原理解析」**：深入SQL 级别，完全拆解 TPC-E 的 12 种事务类型，知其然也知其所以然。
4. **「轻松上手」**：绕过 Github 暗坑，在 MySQL 上编译和运行 TPC-E。

# 概览全貌

![](https://mmbiz.qpic.cn/sz_mmbiz_png/5EcwYhllQOhIogOQhodD9em5ZG7AlpW4TibCyg86iaibBHkPtnl7RIjbTYPFKwUlt3iazahwAdyMspibrcCW3wQfBew/640?wx_fmt=png&from=appmsg)

TPC-E 的场景是股票交易，涉及客户、经纪行和市场三种角色的复杂交互

TPC-E（Transaction Processing Performance Council - E）是一个模拟复杂在线交易处理（OLTP）环境的基准测试。它通过一系列事务来模拟一个股票经纪行的日常业务活动，这些活动涉及客户账户管理、交易执行以及与金融市场的互动。整个业务场景中包含了客户、经纪商、市场数据和后台处理等关键要素。

这里我们从角色（Role）、事务和关系表三部分来展现 TPC-E 全貌。

## 3种角色

TPC-E 模拟的是证券交易所，证券交易的买卖过程会涉及到下面三种角色：

* **「Brokerage（经纪行）」** ：在 TPC-E 基准测试中，经纪行的角色通常由 `Customer Emulator`（客户模拟器）组件扮演。它模拟了客户与经纪行的交互，包括提交交易请求、查询账户信息、执行市场分析等。经纪行角色负责处理客户的交易订单，管理客户账户，并提供市场数据。

+ 注意，事务有一种类别是 Brokerage initiated，但代码中并没有单独的 broker emulator，因为 broker 通常是应答customer 的要求，broker 参与的事务就放到 CE 中模拟

* **「Customer（客户）」** ：客户角色代表了实际使用经纪行服务的个人或机构投资者。在 TPC-E 中，客户角色通过 `Customer Emulator` 组件模拟，执行各种交易活动，如买卖证券、查询持仓情况、查看市场动态等。客户角色的目的是评估经纪行提供的服务和交易平台的性能。
* **「Market（市场）」** ：市场角色在 TPC-E 中由 `Market Exchange Emulator`（市场交易所模拟器）组件扮演。它模拟了股票市场的实际运作，包括股票价格的变动、交易的执行、市场数据的发布等。市场角色为经纪行和客户提供了交易的场所和必要的市场信息。

这三个角色在 TPC-E 中的主要区别在于它们在交易过程中的职责和功能。经纪行负责处理交易和客户账户，客户负责发起交易和查询，而市场则提供了交易发生的环境和数据。

## 12 种事务：一个故事

TPC-E 共包含了 12 种类型的事务，为了便于理解，让我们用一个故事串讲一下。

在一个充满活力的交易日，客户们忙碌地通过经纪行的交易平台进行股票买卖。他们首先会检查自己的账户情况，了解自己的资产和持仓（`Customer-Position` 事务），然后根据市场动态（`Market-Feed` 事务）和特定证券的详细信息（`Security-Detail` 事务）来制定交易策略。在做出决策之前，他们可能会监控市场趋势（`Market-Watch` 事务），或者回顾过去的交易记录（`Trade-Lookup` 事务），以分析证券的历史表现。经纪行管理者会生成不同经纪商的交易报告，用于评估各个经纪商的表现（`Broker-Volume` 事务）。一旦客户决定买卖某只股票，他们会下达交易指令（`Trade-Order` 事务）。这些指令会被提交到市场交易所，并在交易完成后收到交易结果（`Trade-Result` 事务）。这些结果包括了交易的最终确认、成交价格以及可能的税务影响。客户可以通过查看交易状态（`Trade-Status` 事务）来跟踪他们的交易是否成功执行。在交易过程中，客户可能会需要更新或修改他们的交易指令（`Trade-Update` 事务）。同时，为了保持数据的准确性和最新性，经纪行会定期进行数据维护（`Data-Maintenance` 事务），包括更新客户账户信息、税务信息以及市场数据。在交易日结束时，经纪行需要清理数据库，取消任何未完成或错误的交易（`Trade-Cleanup` 事务），以确保第二天的交易能够顺利进行。这个过程包括从数据库中移除所有挂起的交易请求，更新交易历史记录，并确保所有交易数据都是最新的。

## 33 张关系表

TPC-E 共涉及 33 张表：

* **「Customer Tables」**：9 张表，描述了与客户相关的表，包括账户信息（`CUSTOMER_ACCOUNT`）、税务信息（`CUSTOMER_TAXRATE`）等。
* **「Broker Tables」**：9 张表，与经纪商相关的表，如经纪商（`BROKER`）、现金交易（`CASH_TRANSACTION`）、费用（`CHARGE`）等。
* **「Market Tables」**：11 张表，与市场相关的表，如公司（`COMPANY`）、每日市场数据（`DAILY_MARKET`）、交易所（`EXCHANGE`）等。
* **「Dimension Tables」**：维度表，如地址（`ADDRESS`）、状态类型（`STATUS_TYPE`）、税率（`TAXRATE`）等。

TPC 委员会公布的 TPC-E 标准文件（pdf）中事无巨细的讲解了 TPC-E 各方面内容，其中2.2.4 ~ 2.2.7 描述库表设计，感兴趣的同学可以深入了解下：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/5EcwYhllQOhIogOQhodD9em5ZG7AlpW4cYyharicrSZoia5EbaIne0GneuuhpfDa9nIdJGc8vza1QukPU3Xsoseg/640?wx_fmt=png&from=appmsg)

## 衡量标准：tpsE

TPC-E 衡量的标准是 tpsE（transactions- per-second-E，每秒成交量）。在 TPC-E 对真实场景的模拟中，用户和经纪商可能经过许多次的观望、选择、评估，才会达成一笔交易。因此，TPC-E 的性能取决于 `Trade-Result` 事务完成的数量。例如，如果一个客户执行了一项交易，并且该交易被成功处理（即交易请求被接受并执行，Trade-Result + 1），那么这将被视为完成了一个 tpsE。仅仅查看订单或执行其他非交易类型的操作通常不会计算在内。Trade-Result 事务与全部事务的比例基本稳定（例如 10%），也意味着 tpsE 基本可以反映数据库执行的事务总量。考虑到TPC-E 的事务通常较为复杂（单个事务会包含数十条 SQL），在我们执行 TPC-E 测试时，尽管最终显示的 tpsE 只有 100 上下，但实际执行的 SQL 已经超过数十万条。

# 原理解析：深入 SQL 看事务

TPC-E 比 TPC-C 的复杂体现在事务的复杂。TPC-C 包含 5 种事务，SQL 模板共 29 条，而 TPC-E 包含 12 种事务，SQL 模板超过 120 条。在一些复杂的 TPC-E 事务中（例如 Trade-Order），包含 6 个阶段（称为 Frame），每个阶段中会执行多轮”子事务“。由此，在各种任务（参数调优、规格调优、索引推荐）走到深水区后，对事务细节的了解就很有必要了。

下面我们会逐一分析各个事务的事务逻辑概述和 SQL 细节。必要的地方我们会结合 TPCE 负载发生器的源码进行解析。

## 事务分类

![](https://mmbiz.qpic.cn/sz_mmbiz_png/5EcwYhllQOhIogOQhodD9em5ZG7AlpW4U0eEE7QNpj0cPS6H5n6BwqamWz7cgNp6K0kW9UsLGmc33IsPXUUjTQ/640?wx_fmt=png&from=appmsg)

TPC-E 的事务可以按照它们的功能和特征进行分类。根据文档中的描述，这些事务主要可以分为以下几类：

1. **「客户发起的事务（Customer Initiated）」** ：

1. 这些事务模拟了客户与系统交互的场景，如查询账户信息、执行交易等。
2. 例如：Customer-Position（客户持仓查询）、Market-Watch（市场观察）、一部分 Trade-Lookup（交易查询）、Security-Detail（证券详情查询）、Trade-Order（交易委托）、Trade-Status（交易状态查询）、一部分 Trade-Update（交易更新）。

2. **「经纪商发起的事务（Brokerage Initiated）」** ：

1. 这些事务模拟了经纪商内部处理的场景，如生成报告、管理账户等。
2. 例如：Broker-Volume（经纪商成交量）。一部分 Trade-Lookup；一部分 Trade-Update

3. **「市场触发的事务（Market Triggered）」** ：

1. 这些事务模拟了市场活动对系统的影响，如市场数据更新、市场动态跟踪等。
2. 例如：Market-Feed（市场数据更新）、Trade-Result

4. **「其他」**：

1. Trade-Cleanup、Data-Maintenance

我们结合 Github 源码进行分析。tpce-mysql 中，`DBConnection.h` 文件包含几个 enum，可以作为印证，如下：

```
/*
Customer Emulator System Under Test
由用户
*/
enum eCESUTStmt
{
        // Customer-Position 有2 阶段、4 sql。文档是3 阶段（Frame），但第三阶段只有 commit ，其他有意义的 sql 是对得上的。
    CESUT_STMT_CPF1_1,
    // Market-Watch（市场观察）
    CESUT_STMT_MWF1_1a,
    // Security-Detail（证券详情查询）
    CESUT_STMT_SDF1_1,
    // Trade-Lookup（交易查询），非常巨大的事务
        CESUT_STMT_TLF1_1,
        // Trade-Order（交易委托）
        CESUT_STMT_TOF1_1,
        //Trade-Status（交易状态查询）
        CESUT_STMT_TSF1_1,
        // Trade-Update（交易更新）
        CESUT_STMT_TUF1_1,
}

/*
Market Exchange Emulator SUT
*/
enum eMEESUTStmt
{
    // 极其巨大的事务
    MEESUT_STMT_TRF1_1,
    // Market-Feed（市场数据更新）
    MEESUT_STMT_MFF1_1,
};

/*
Data Maintenance SUT
*/
enum eDMSUTStmt
{
    // Trade-Cleanup，开测前初始化；
    DMSUT_STMT_TCF1_2,
};

// 其他无对应代码 enum 的：
// Broker-Volume（经纪商成交量）：只有一个 frame、一句 sql，无 enum
```

除了上述分类，事务还可以根据它们的读写特性进行区分：

* **「读事务（Read-Only）」** ：这类事务主要涉及数据的读取，不会导致数据的修改。例如，客户查询账户信息（Customer-Position）或查看市场数据（Market-Watch）。
* **「读写事务（Read-Write）」** ：这类事务既涉及数据的读取也涉及数据的写入，可能会改变数据库的状态。例如，执行交易（Trade-Order）会创建新的交易记录，更新客户账户（Trade-Update）会改变账户的持仓信息。
* **「写事务（Write-Only）」** ：这类事务主要涉及数据的写入，不涉及数据的读取。例如，数据维护（Data-Maintenance）事务可能会更新或删除数据库中的记录。

概括来看：

1. **「Broker-Volume (BV)」** - 模拟**「经纪行」**内部业务处理，例如生成关于不同经纪人业绩、潜力的报告。
2. **「Customer-Position (CP)」** - 模拟**「客户」**查询其账户的持仓情况。根据所有资产的当前市场价值总结其账户价值。
3. **「Market-Feed (MF)」** - 模拟跟踪当前市场活动，处理来自**「市场交易所」**的“股票行情”数据。
4. **「Market-Watch (MW)」** - 允许**「客户」**跟踪一组证券的当前日常趋势（上涨或下跌），基于客户的当前持仓、观察列表或特定行业。
5. **「Security-Detail (SD)」** - 模拟**「客户」**访问特定证券（`Security`）的详细信息，如进行研究以决定是否执行交易。
6. **「Trade-Lookup (TL)」** - 模拟信息检索，以回答关于一组交易的问题，可能涉及市场分析、交易历史审查或特定客户持仓分析。
7. **「Trade-Order (TO)」** - 模拟**「客户、经纪人」** 或授权第三方购买或出售证券的过程，包括验证授权、执行市场价买卖、限价买卖以及提供财务影响估计。
8. **「Trade-Result (TR)」** - 模拟完成股票市场交易的过程，更新客户持仓，记录交易结果和历史信息。这是由 **「market 市场交易所」** 负责记录的
9. **「Trade-Status (TS)」** - 提供特定交易集合的状态更新，模拟**「客户」**查看其账户的最近交易活动摘要。
10. **「Trade-Update (TU)」** - 模拟对一组交易进行轻微修正或更新，类似于**「客户」**或**「经纪人」**审查交易并进行小的编辑修正。
11. **「Data-Maintenance (DM)」** - 模拟对主要静态数据进行定期修改，如更新参考数据。
12. **「Trade-Cleanup (TC)」** - 用于取消数据库中任何待处理或已提交的交易，通常在测试运行前将数据库恢复到已知状态。

## Broker-Volume

**「Broker-Volume 事务逻辑概述」** 在 TPC-E 基准测试的第 3.3.1 章节中，Broker-Volume 事务是一个典型的读操作，它模拟了经纪行内部生成经纪人业绩报告的场景。这个事务的核心目标是计算每个经纪人在特定时间段内的交易量，这通常涉及到对挂单限价订单（TRADE\_REQUEST）的汇总分析。

**「SQL 细节」** Broker-Volume 事务的 SQL 查询设计要实现以下目标：

1. **「选择经纪人列表」**：确定需要生成报告的经纪人。
2. **「检索挂单限价订单」**：从 TRADE\_REQUEST 表中检索每个经纪人的订单信息。
3. **「计算总交易量」**：对每个经纪人的订单数量和价格进行计算，得出总交易量。
4. **「排序结果」**：将经纪人按照总交易量降序排列，以便展示业绩最好的经纪人。

以下是 Broker-Volume 事务的 SQL 伪代码：

```...