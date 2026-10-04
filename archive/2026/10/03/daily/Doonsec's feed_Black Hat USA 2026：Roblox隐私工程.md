---
title: Black Hat USA 2026：Roblox隐私工程
url: https://mp.weixin.qq.com/s/usIOL7KckqjlQPc1sCwLQQ
source: Doonsec's feed
date: 2026-10-03
fetch_date: 2026-10-04T07:34:18.177385
---

# Black Hat USA 2026：Roblox隐私工程

# Black Hat USA 2026：Roblox隐私工程

原创

Max Luo
Max Luo

白帽子罗棋琛

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

# 把隐私权请求做成分布式系统：Roblox 的规模化实践

> Black Hat USA 2026 议题笔记：Privacy at Scale: Roblox's Infrastructure for Honoring User Privacy Rights

“删除我的数据”“给我一份数据副本”，从用户界面看只是两个按钮。落到大型互联网平台，却是一次跨数百个服务、多个存储引擎、缓存、索引和归档系统的分布式执行。任何一个数据副本被遗漏，删除就不完整；任何一个导出链路保护不足，原本用于保障隐私权的系统反而会成为高质量的数据外泄通道。

Hao Zhang 与 Yiwen Luo 的公开课件介绍了 Roblox 如何重构隐私基础设施：不把个人数据搬进中央平台，而是集中编排控制流，让持有数据的服务执行自己的删除和导出逻辑；数据目录负责回答“数据在哪里、谁负责、保留多久”，工作流引擎负责把一个请求展开为 600 多个子任务，中央审计系统负责留下可验证证据。

![议题课件封面](https://mmbiz.qpic.cn/sz_mmbiz_jpg/4yRoMuNP853jsIVFh7srFDpMsYPaHiboVQCtJcsCibxEsM6CEamxcib37NhianBuQy0UsyCBLQY9UfPswIPWYIUvXLOVhIiatSjI1t6d3duib03YM/640?from=appmsg)

*图 1：这份材料讨论的不是隐私政策文本，而是让访问、更正、删除等权利在分布式系统中真正执行的工程基础设施*

本文从安全工程角度拆解这套设计，重点关注身份核验、消息鉴权、幂等、完整性、法律保全、导出制品和审计证据。示例是根据课件架构抽象出的厂商无关实现，不代表 Roblox 内部代码。

## 1、真正困难的不是删除语句，而是找到所有副本

课件给出的 2026 年第一季度规模是：1.32 亿日活用户、600 多个服务、8 类存储引擎，约 20% 的服务或数据存储包含个人数据。用户量同比增长约 1.6 倍，隐私请求量却增长约 3.5 倍。

![Roblox 隐私请求的规模](https://mmbiz.qpic.cn/mmbiz_jpg/4yRoMuNP851C3iaJl5TDGGzLmWEkjYPf5GfzRhSDd3mjPfNHPicknUa5lRohgnVkZ48dSerjOO9yTjxu0QdQfrkNXDucsj7CK9cZaavl7EELw/640?from=appmsg)

*图 2：请求增长快于用户增长，且个人数据散布在 SQL、NoSQL、对象存储、数仓、KV、搜索、图数据库和内存存储中*

对单体应用，删除可能是一条带用户 ID 的 SQL；对微服务系统，同一身份会出现在用户资料、聊天、好友、支付、语音、搜索、广告、日志、实验、风控和备份中。数据还会变形：主表按 `user_id` 建索引，日志只有设备 ID，支付系统保留交易主体，搜索引擎保存反向索引，数据湖按日期分区。

因此，删除完整性不是“所有已知服务都返回 200”，而是两项条件同时成立：

text

```
删除完整性 = 数据位置清单完整           × 每个位置的处理语义正确           × 执行结果可验证
```

任何一项为零，整体保证就为零。课件用“漏掉一个就是一次违规”强调这一点。

![遗漏一个服务就会留下残余数据](https://mmbiz.qpic.cn/sz_mmbiz_jpg/4yRoMuNP851W6kdHzvuPic9ldRsUoQEibeysF5VInm1RrDnyGLY7Bt20MUI5ThibgvlfEkWJicnqyITN1HaggiayOpYnUOHicVpvj3hiaIM1ZcXpJY/640?from=appmsg)

*图 3：工作流成功率不能替代覆盖率；如果一个包含个人数据的服务从未进入清单，它甚至不会产生失败任务*

安全团队常从 API 网关或工作流引擎开始评审，这个顺序容易误导。首先要回答的是：新服务、新字段、新数据管道和影子存储如何被持续发现，谁为每一份数据负责，清单陈旧时系统如何阻止“成功”结案。

## 2、数据目录是执行前提，也是隐私系统的根信任

Roblox 的课件把最初押错的难题说得很直接：团队先尝试自动化删除，后来发现真正困难的是数据发现。删除动作只有在已知位置上才容易；数据位置却随服务拆分、字段增加、缓存引入和分析任务持续变化。

课件中的 Metadata Catalog 可以按用户定位相关存储，并给出负责人、个人信息字段、存储类型、保留策略和例外。核心不是提供一个搜索界面，而是让目录成为工作流生成任务的输入。

![隐私数据目录快照](https://mmbiz.qpic.cn/sz_mmbiz_jpg/4yRoMuNP8518a1IWF0RtxiaVibI9OGY0ZkhV3o0QLg0DmXRj6ITKFOsjwIX0IZ5PNB3ibHJwNyl1usvBEGybog8XPUicBXSibUcW8l2g38o0QpG0/640?from=appmsg)

*图 4：目录同时记录数据位置与执行上下文；“发现后再执行”避免编排器在未知覆盖范围上给出完成结论*

目录记录应有机器可读的最小结构，并且明确区分“系统声明”“自动发现”和“人工验证”：

yaml

```
apiVersion:privacy.platform/v1kind:PersonalDataStoremetadata:service:chat-servicerepository:platform/chatowner_group:chat-data-oncallcatalog_revision:1842spec:storage:engine:postgresresource:chat-prod.messagesregion:sgsubjects:identifiers: [user_id]   fields:- {name:sender_ip, class:online_identifier, source:scanner}     - {name:message_body, class:user_content, source:owner_review}   operations:erasure:custom_handleraccess_export:custom_handlerderived_copies:-chat-search-index-abuse-review-storeretention:default_days:365policy_id:RET-CHAT-07evidence:last_scanned_at:"2026-08-01T03:20:00Z"owner_attested_at:"2026-08-02T09:14:00Z"
```

这份清单本身就是高敏感资产。它描述了全公司的个人数据分布、数据库名称、负责人和保留逻辑，泄露后可直接帮助攻击者选目标。目录 API 要按用途授权：普通服务只能维护自己的条目；编排器只读取完成请求所需的子集；审计员访问脱敏视图；批量导出必须审批并记录。

目录还需要“失败关闭”的新鲜度门禁。例如目录超过 24 小时未同步、负责人为空、扫描发现了未归类字段，系统都不能把请求标记为完整：

sql

```
SELECT store_id, service_name, owner_group, last_scanned_at FROM privacy_catalog WHERE contains_personal_data =TRUEAND (     owner_group ISNULLOR erasure_mode ISNULLOR last_scanned_at < NOW() -INTERVAL'24 hours'OR unresolved_field_count >0   );
```

这类查询不直接删除数据，却比增加工作流并发更能提升实际覆盖率。

## 3、集中控制流，不集中个人数据

最朴素的设计是建设一台中央隐私引擎，让所有服务把数据交给它统一处理。这样便于管理，却会形成带宽瓶颈、单点故障和一个聚合全站个人数据的高价值目标。

Roblox 选择“中央协调、联邦执行”：中央平台只发送信号和收集状态，数据仍留在原服务，由最了解数据语义的团队维护 Handler。

![集中控制流而不是集中数据](https://mmbiz.qpic.cn/mmbiz_jpg/4yRoMuNP853ovBg7RIMiaNBAXUIiazGqbaunLRpp6ZUH0sfQGlLibGqGat0A5jCuJdlmDWM4vG7cJvUGMCZNbXe0TCJqMDSwlWWGnia4wZY6gB8/640?from=appmsg)

*图 5：编排器掌握请求状态和服务清单，但删除、导出与保留策略仍由数据所有者在本地执行*

这项架构决策同时解决了扩展性和责任边界。支付团队知道哪些交易数据不能简单物理删除，聊天团队知道消息与举报证据之间的关系，搜索团队知道如何删除派生索引。中央平台不需要理解所有业务 Schema，只需规定协议、安全属性和可验证结果。

代价是信任从一个中央服务分散到数百个 Handler。每个 Handler 都可能少删、过删、导出他人数据，或者把成功响应写在实际提交之前。平台因此应规定窄接口，而不是给处理器一个万能 SDK：

protobuf

```
message PrivacyTask {   string task_id = 1;   string request_id = 2;   string subject_id = 3;       // 平台内部不可逆映射 ID   Operation operation = 4;    // ERASE 或 EXPORTstring catalog_revision = 5;   string policy_revision = 6;   int64 issued_at_unix = 7;   int64 expires_at_unix = 8;   string nonce = 9;   bytes signature = 10; }  message TaskResult {   string task_id = 1;   ResultCode code = 2;   uint64 matched_records = 3;   uint64 changed_records = 4;   repeatedstring evidence_refs = 5;   bytes result_digest = 6; }
```

任务中不要放邮箱、手机号等可读身份，避免消息队列和 Trace 复制个人数据。内部 Subject ID 必须由经过认证的身份映射服务生成，Handler 不能接受模型或客户端直接提供的数据库条件。

## 4、一次请求是持续数小时的分布式执行

课件用 Temporal 承载中央编排：一个请求展开为 600 多个子任务，异步执行、水平扩展，并利用重试、超时和恢复能力处理长流程。

![中央编排与联邦执行](https://mmbiz.qpic.cn/sz_mmbiz_jpg/4yRoMuNP850iaoS6XWI22XppQXU7IuYmic2e7ibUXovCkhjZKtjs55Cgic29ScdMy5SibzBC5cdcuPCe1AteAVNHuXyzgHvmSjeUoib2BicLRsjVp4/640?from=appmsg)

*图 6：工作流引擎不直接处理数据，而是持续追踪每个服务 Handler 的执行状态*

完整流程分为五步：验证身份、预处理风险与法律状态、注册本次需要的 Worker、执行删除或导出、响应并在访问请求场景归档制品。

![隐私请求的五阶段工作流](https://mmbiz.qpic.cn/sz_mmbiz_jpg/4yRoMuNP850uiaxolPZYibF5NcE2icSwA3PhsrOWnicHPQiaNmVskGdjGBNDGL2SL57DMpz5HmVBiaibRocUrEjT24ndRb8w7Tr9TwJS9syiayc6be4/640?from=appmsg)

*图 7：身份核验发生在扇出之前；服务清单与策略版本应在同一请求中冻结，保证执行和审计口径一致*

分布式工作流最容易犯的错误，是把“重试”理解为重新发送一次 HTTP 请求。删除和导出必须在业务语义上幂等：同一个 `task_id` 执行两次，不能重复扣除资源、扩大删除范围或生成多个无人管理的导出包。

Handler 可以先使用唯一键登记任务，再在本地事务中完成业务变更与 Outbox 记录：

sql

```
BEGIN;  INSERT INTO privacy_task_execution(   task_id, request_id, operation, subject_id, status, started_at ) VALUES (   :task_id, :request_id, :operation, :subject_id, 'RUNNING', NOW() ) ON CONFLICT (task_id) DO NOTHING;  -- 若未插入，读取并返回既有结果，禁止重新扩大作用域。-- 删除语句只能使用服务端从 subject_id 解析出的固定条件。UPDATE user_profile SET email =NULL, display_name ='deleted-user', erased_at = NOW() WHERE internal_subject_id = :subject_id   AND erased_at ISNULL;  INSERT INTO privacy_task_outbox(task_id, event_type, created_at) VALUES (:task_id, 'ERASURE_COMPLETED', NOW());  UPDATE privacy_task_execution SET status ='COMPLETED', completed_at = NOW(), changed_records = :row_count WHERE task_id = :task_id;  COMMIT;
```

真实系统还要处理大表分批、对象存储、索引和异步派生副本。此时任务状态至少需要 `PENDING/RUNNING/WAITING/COMPLETED/FAILED/EXEMPTED`，不要用一个布尔值表示。`EXEMPTED` 必须关联具体政策版本与审批证据，不能成为 Handler 任意跳过删除的出口。

## 5、Handler 之间不存在“柔软的内网”

课件把安全底线概括为 No Soft Interior：每个 Handler 都鉴权，每条编排消息都签名并限定作用域；一切都可能重试；系统既不能过度删除，也不能少删，还必须命中正确主体和正确范围。

![隐私 Handler 的三项底线](https://mmbiz.qpic.cn/sz_mmbiz_jpg/4yRoMuNP852VgBNYOOqLQdy1NQibvrG13FDa4IX47yZ3MbK9h1bZ58rXoFBibOAt04hTsKI19ER0L9wxWESJAw92QF8u3xDIDiboWtsarU2eXI/640?from=appmsg)

*图 8：认证授权、幂等和完整性是三个独立目标，TLS 或内网身份不能替代另外两项*

消息签名需要覆盖所有会改变执行语义的字段，包括请求类型、Subject ID、目录版本、策略版本、时效和随机数。只签 `task_id` 没有意义，攻击者仍可篡改操作或主体。Handler 还应验证调用方工作负载身份、签名密钥用途和任务归属：

go

```
type TaskClaims struct { 	TaskID          string`json:"task_id"` 	RequestID       string`json:"request_id"` 	SubjectID       string`json:"subject_id"` 	Operation       string`json:"operation"` 	Service         string`json:"service"` 	CatalogRevision string`json:"catalog_revision"` 	IssuedAt        int64`json:"iat"` 	ExpiresAt       int64`json:"exp"` 	Nonce           string`json:"nonce"` }  funcAuthorizeTask(ctx context.Context, c TaskClaims, expectedService string)error { 	identity, err := workload.IdentityFromMTLS(ctx) 	if err != nil || identity != "spiffe://prod/privacy-orchestrator" { 		return errors.New("untrusted caller") 	} 	if c.Service != expectedService { 		return errors.New("task audience mismatch") 	} 	if c.Operation != "ERASE" && c.Operation != "EXPORT" { 		return errors.New("unsupported operation") 	} 	if time.Now().Unix() < c.IssuedAt-30 || time.Now().Unix() > c.ExpiresAt { 		return errors.New("task outside validity window") 	} 	if !nonceStore.ConsumeOnce(c.Nonce, c.ExpiresAt) { 		return errors.New("replayed task") 	} 	returnnil }
```

示例假定外层已经用固定算法和受信密钥验证了完整令牌签名。`ConsumeOnce` 要原子执行；任务因网络错误合法重试时，幂等表返回原结果，而不是重新消费同一个一次性入口...