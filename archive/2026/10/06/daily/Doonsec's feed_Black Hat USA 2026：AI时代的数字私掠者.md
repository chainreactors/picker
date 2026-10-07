---
title: Black Hat USA 2026：AI时代的数字私掠者
url: https://mp.weixin.qq.com/s/xekzV0vMAdBuZuH9V0Luzg
source: Doonsec's feed
date: 2026-10-06
fetch_date: 2026-10-07T07:52:36.125329
---

# Black Hat USA 2026：AI时代的数字私掠者

# Black Hat USA 2026：AI时代的数字私掠者

原创

Max Luo
Max Luo

白帽子罗棋琛

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

# 当网络战被外包：AI 与勒索时代的数字私掠者

面对勒索团伙、诈骗园区和受国家庇护的攻击组织，企业最直观的挫败感是：攻击者可以跨境、换壳、租用第三方基础设施，防守方却受司法管辖、证据规则和企业授权边界约束。于是，“让私营安全公司反向入侵攻击者”会周期性地重新进入政策讨论。

Black Hat USA 2026 公开课件《Cyberspace Pirates》把这种方案类比为历史上的私掠许可（Letters of Marque）：国家能力跟不上对手规模时，授权已有船、人员和知识的私人主体追击敌方，并用经济收益提供激励。材料随后用 authority、capacity、governance 三个缺口，以及 control、liability、scope、incentives、de-confliction 五项测试，评估网络私掠能否成为可治理的公共政策。

这不是一篇支持或反对 hack back 的口号文章。对安全工程师更重要的问题是：主动防御、协同基础设施处置和未经授权入侵之间的边界在哪里；一条归因结论能否承受国家行为；共享云资源误伤后由谁负责；AI 把行动速度提升几个数量级时，审批和停止机制是否还能工作。

本文依据公开课件、美国国会与政府公开文件整理，不以现场参会视角叙述，也不构成法律意见。截至 2026 年 8 月 10 日，文中涉及的三项美国联邦法案均仍停留在提案阶段，不能视为企业开展境外主动入侵的现行授权。

## 1、问题不是防守方不努力，而是制度和对手不对称

课件将困境概括为三个结构性因素：资源、人员与时间上的规模差距；攻击者对全球基础设施的触达和预置；跨境引渡与执法形成的 sanctuary wall。民主法治体系要求授权、证据和问责，而对手可以让国家、承包商、犯罪团伙和基础设施提供者之间的关系保持模糊。

![网络威慑的结构错配](https://mmbiz.qpic.cn/mmbiz_jpg/4yRoMuNP853phKAg6iaKwcQOHap2yW5ch534JicIXjBvGI2icYWiajE3ia8wSFICgns7pnic7XEk17Mb6R9oAdWibVn876zqbGlrO3nWexXU44hQQY/640?from=appmsg)

*图 1：能力规模、全球可达性与司法避风港共同削弱传统威慑*

但“政府反应慢”不能直接推出“企业应该反向入侵”。这中间至少有三道不同问题：

text

```
Authority   谁依法作出跨境、破坏性或情报收集决定？ Capacity    谁拥有人员、基础设施、速度和专业能力？ Governance  谁限定目标、处置冲突、审计过程并承担后果？
```

私营部门确实可能补足 capacity；如果 authority 和 governance 没有同时解决，只是把国家原本需要承担的升级、误伤和赔偿风险转移给更难监督的代理人。

## 2、先给“主动防御”分层，否则讨论一定失焦

安全行业经常把 threat hunting、deception、sinkhole、账号接管协助、域名查封和远程破坏统称为 active defense。它们的法律与技术风险完全不同。一个可执行的分层模型是：

yaml

```
response_capability_tiers:tier_0_observe:examples: [collect_telemetry, hunt, preserve_evidence]     leaves_owned_boundary:falsetier_1_defend:examples: [block, isolate, rotate_credentials, deploy_deception]     leaves_owned_boundary:falsetier_2_cooperative_disruption:examples: [provider_takedown, registrar_suspension, court_ordered_sinkhole]     third_party_authorization_required:truetier_3_remote_access:examples: [enter_suspected_c2, alter_remote_data, seize_remote_asset]     unauthorized_by_default:truetier_4_state_operation:examples: [intelligence_collection, destructive_operation, asset_seizure]     sovereign_authority_required:true
```

Tier 0—1 是企业日常防守。Tier 2 通过云厂商、注册商、执法机关或法院命令完成，行动发生在有权控制该资产的主体边界内。Tier 3—4 才进入课件所讨论的 hack back 或数字私掠问题。购买威胁情报、通知 ISP、向被控服务器发送 abuse report，都不等于获得进入该服务器的许可。

## 3、2026年的法案仍是提案，不是Hack Back许可证

课件列出三项立法动向。H.R. 4988《Scam Farms Marque and Reprisal Authorization Act of 2025》于 2025 年 8 月 15 日提交众议院，并转交众议院外交事务委员会；截至本文日期，Congress.gov 状态仍为 Introduced。

H.R. 9697《Cyber Letters of Marque and Reprisal Act》和参议院对应案 S. 5000 均在 2026 年 7 月 15 日提出。H.R. 9697 转交众议院外交事务委员会；S. 5000 经二读后转交参议院外交关系委员会。它们尚未通过两院，更没有成为法律。

![美国网络私掠立法动向](https://mmbiz.qpic.cn/mmbiz_jpg/4yRoMuNP851jqEpScm5gEwWMOIogdVib7ibV87dqGSUdYeibbsj8Qz1YmxOugEpxIjfSHWsicLiayaVQVElFaJG5vjXdOVSSosIuBm1qYHV8mGfg/640?from=appmsg)

*图 2：课件展示的是正在进行的政策辩论，而不是已经生效的授权框架*

H.R. 9697 文本提议允许总统向私人实体签发针对 designated cyberthreat 的联邦 commission，范围包括情报收集、数据恢复、数字资产处置和恶意基础设施 disruption；持有人需记录活动与资产至少五年，并对明确授权的行为提供责任保护。

课件把经济条款概括成“15% asset bounty”，正式文本更细：总统可以要求持有人把最多 15% 的追回资产上缴美国，用于维持后续 bounty program；另有 bounty 和线索奖励条款。它不是简单规定“操作者固定拿走 15%”。这种差异说明政策评审必须读 bill text，不能只转述标题或演示页。

![授权能力与治理缺口](https://mmbiz.qpic.cn/sz_mmbiz_jpg/4yRoMuNP852vh4l1Fy9Pa6V0BwHPTRFgq7kau0v9C6XRia0rujK6vVd8Jkykx3sXmQvxV92tTRoBlGfflAz7GBSM0icZF1R93AmR9icIOMOnwM/640?from=appmsg)

*图 3：课件认为现有提案主要补 authority 与 capacity，治理细节仍不足*

## 4、现行CFAA不会因为目标在境外就自动消失

18 U.S.C. §1030（CFAA）禁止多类未经授权访问和造成损害的行为。“protected computer”的定义覆盖用于或影响州际、国际商业或通信的计算机，也明确可能包含位于美国境外、但影响美国州际或国际商业/通信的设备。

因此，“攻击者是罪犯”“服务器在美国之外”“IP 出现在 IOC 列表”都不是私人主体的通用抗辩。更不能把政府战略中“激励私营部门识别和干扰对手网络”的政策表述，直接转换成某家公司的操作授权。政策目标、刑事法律和某次行动的书面 authority 是三个不同层级。

企业可以在执行控制面写死这条边界，避免分析员或 Agent 把情报判断直接变成远程动作：

rego

```
package cyber_response.authorization  default allow := false  allow if {   input.action in {"observe", "block_owned_asset", "preserve_evidence"}   input.asset.owner_id == input.organization.id }  allow if {   input.action == "provider_requested_takedown"   input.provider_ticket.approved == true   input.provider_ticket.asset_id == input.asset.id }  deny_reason := "remote access requires sovereign or asset-owner authorization" if {   input.action in {"remote_login", "alter_remote_data", "deploy_code", "seize_asset"}   not input.authorization.sovereign_order_id   not input.authorization.asset_owner_consent_id }
```

这类 policy-as-code 不是法律判断引擎，但能把默认行为设为 fail closed：没有可核对的授权对象，就不向远程执行层发放凭据或网络能力。

## 5、委托武力的核心风险是Principal-Agent问题

国家（principal）希望代理人只打击已指定对手、控制附带影响并把资产返还受害者；私人操作者（agent）可能追求赏金、市场声誉或技术战果。双方掌握的信息不对称：执行者最了解实际目标与效果，授权方往往在行动后才看到报告。

![委托武力的制度结构](https://mmbiz.qpic.cn/sz_mmbiz_jpg/4yRoMuNP851KTnj4cjE8S0knmOgWvIHhoHOqIEZ4dojUIhXXduUChzLPWPtGGDpiaEWSVla1FM9ngzxFb1k8qvr7VCwLW8As7nwuegyrKQvw/640?from=appmsg)

*图 4：政策争论横跨行政、国会、产业和专家群体，不存在简单共识*

如果奖励与追回金额挂钩，操作者会偏好容易变现的数字资产，而不是社会危害最大但难以获利的基础设施；如果仅要求事后报告，失败、误伤与未授权扩展都可能被选择性披露；如果给予广泛免责，受影响的无辜第三方又缺少救济。

最小审计记录必须在行动前生成，并由独立系统追加签名：

json

```
{"operation_id":"op-2026-0042","authority":{"instrument_id":"signed-order-reference","issuer":"authorized-government-office","valid_from":"2026-08-10T00:00:00Z","valid_until":"2026-08-10T04:00:00Z"},"target":{"designated_entity_id":"registry-entry-reference","asset_ids":["immutable-target-manifest-sha256"],"confidence":0.97},"allowed_effects":["collect","isolate-designated-service"],"forbidden_effects":["wipe","self-propagate","access-co-tenant"],"stop_conditions":["ownership-changed","ally-asset-detected","telemetry-lost"],"approvals":["legal","operations","deconfliction"],"log_chain_previous_hash":"sha256:..."}
```

日志字段不能在行动后补录。目标 manifest、有效期、允许效果和停止条件应成为执行器的机器约束，而不是 PDF 附件里的自然语言建议。

## 6、共享基础设施让“打击C2”变成多租户变更

现代恶意基础设施大量建立在云主机、CDN、域名注册商、被入侵网站、代理网络和住宅 IP 上。同一个地址可能同时承载正常租户；同一 bucket、API token 或 hypervisor 的影响边界远大于一条 IOC。

![历史私掠退出的网络类比](https://mmbiz.qpic.cn/mmbiz_jpg/4yRoMuNP852139KN2eJK1X3JpU7JniaFZ6ZdRcGWEV997dWswetp7xFmznNTlPayDIe7Evja3pCMaEgKdHcy2wskOGLeED8SnqeHC54ibEemM/640?from=appmsg)

*图 5：历史上的中立船只误伤与今天的共享基础设施 spillover 具有相同治理难题*

IP、域名和 TLS certificate 只能作为候选边，不应直接成为打击目标。威胁情报平台可以先做保守聚类，把共享基础设施和时间窗口纳入条件：

cypher

```
MATCH (c:Campaign)-[r:OBSERVED_ON]->(a:Asset) WHERE r.confidence >= 0.8   AND r.last_seen >= datetime() - duration('P7D') OPTIONAL MATCH (a)<-[:USES]-(t:Tenant) WITH c, a, collect(DISTINCT t.id) AS tenants,      count(DISTINCT t) AS tenant_count RETURN c.id AS campaign,        a.id AS asset,        a.provider AS provider,        tenant_count,        tenants,        CASE          WHEN tenant_count = 1 AND a.owner_verified THEN 'candidate_for_provider_action'          ELSE 'shared_or_uncertain_do_not_touch'        END AS disposition
```

即便 `tenant_count=1`，也只能成为提交给 provider 的处置候选，不能自动授权登录、删除或破坏。云厂商掌握控制平面与租户映射，通常比外部团队更适合执行账号冻结、网络隔离和镜像保全。

## 7、归因必须能承受从情报结论升级为国家行为

课件将对手优势描述为“他们不挂旗，我们却要留下国会记录”：国家、承包商、网络犯罪和默许之间的边界可以刻意模糊。情报报告中的“linked to”允许一定不确定性；一旦要查封资产、投放代码或产生跨境影响，相同置信表述未必够用。

![模糊代理人与公开问责](https://mmbiz.qpic.cn/sz_mmbiz_jpg/4yRoMuNP852NmXbgAoJYmtgk3aDHR1sV3unIU4JnxSxDkecgogcmsyqJt1jNrbXla0h3NibVo9XoG4dGNOPOLXJia5aYwWNibO5sF9CwaZ3Igg/640?from=appmsg)

*图 6：透明度是民主治理的必要条件，却也提高行动前归因与公开说明成本*

不要把多个弱相关 IOC 简单相加成 95% 置信度。证据经常不独立：相同 malware family、相同 hosting ASN 和相同工作时间可能都来自同一份上游报告。比较稳妥的证据对象需要记录来源、独立性和反证：

python

```
from dataclasses import dataclass  @dataclass(frozen=True)classEvidence:     source_id: str     family: str     reliability: float     relevance: float     supports: booldefconservative_score(items: list[Evidence]) -> float:     # 同一证据族只保留最强项，避免重复 IOC 被当成独立确认     strongest: dict[str, Evidence] = {}     for item in items:         if item.family notin strongest or (             item.reliability * item.relevance             > strongest[item.family].reliability * strongest[item.family].relevance         ):             strongest[item.family] = item      support = sum(e.reliability * e.relevance for e in strongest.values() if e.supports)     contradiction = sum(         e.reliability * e.relevance for e in strongest.values() ifnot e.supports     )     returnmax(0.0, min(1.0, support / max(support + contradiction + 1.0, 1...