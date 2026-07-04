---
title: 阿塞拜疆国家安全局（DTX）xa0数据库出售事件
url: https://mp.weixin.qq.com/s/xIVrY6jWc9C3Ogpijga45g
source: Doonsec's feed
date: 2026-07-03
fetch_date: 2026-07-04T05:45:10.266978
---

# 阿塞拜疆国家安全局（DTX）xa0数据库出售事件

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/es3jUghv8r80Zon8G6qK30ZDxtga4OBZWe3qprRQmHgq5rE3rGGQKwbU3pzD2777bibGvsfvE0JKZxia99SSMnJo4WbPFVmg0W5ticEwQcVpUE/0?wx_fmt=jpeg)

# 阿塞拜疆国家安全局（DTX） 数据库出售事件

原创

NightTeam
NightTeam

夜组OSINT

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

## 执行摘要

2026年7月2日前后，黑客在暗网论坛宣称持有并出售 **阿塞拜疆国家安全局（DTX）** 的完整数据库，包含2026年6月28日最新更新的全量个人信息、军事状态及2026-2027年度任务分配。

![](https://mmbiz.qpic.cn/mmbiz_png/es3jUghv8ribvAFicUOzjic0urmOYmOMsF0rmJxUa0BzxsDNwYrJicWvBvMqUKiaPLtbp0jKZVCoVpm522eESHOvx8IZ6lA0lcSYP25x7ohiclEYo/640?wx_fmt=png&from=appmsg)

## 泄露数据字段分析

![](https://mmbiz.qpic.cn/sz_mmbiz_png/es3jUghv8ricOF0VX2CTKSGDtKcFj8MnWRWB7J3FZpUTZwtQ6FIpBBoFKxzHb344j0WWpH66IPROkR0SqKgIr8AXGTILLlcV5z6Kju19z2PY/640?wx_fmt=png&from=appmsg)![](https://mmbiz.qpic.cn/sz_mmbiz_png/es3jUghv8ric5WjribYLOj20pOP2kibAUQSLia8qBJpeYbhXQn7Nwou2tXpEbeM5keAeRACTOaGaboKyrAVb8ib5bTWnatub2cVicSKzIflq1rluY/640?wx_fmt=png&from=appmsg)![](https://mmbiz.qpic.cn/mmbiz_png/es3jUghv8ricPlcnWxRGRYjsmynDUpq0gTDJvCnlxsHVRx0Ol1Fovx1ZISATvtPPtelXubAUuOA1PrrAA9HZvPP8YzCWKopZ13PL7ePibpFEM/640?wx_fmt=png&from=appmsg)

| 类别 | 字段 | 情报价值 |
| --- | --- | --- |
| **基础身份** | 名（First Name）、姓（Last Name）、父名（Father's Name）、全名（Full Name）、母名（Mother's Name） | 完整身份链，可用于家族关联分析 |
| **证件信息** | 国民身份证号（National ID Number）、卡号（Card Number）、证件签发日期（ID Issue Date）、证件到期日（ID Expiration Date）、签发机关（ID Issuing Authority） | 证件全周期信息，可用于伪造或验证 |
| **生物特征** | 出生日期（Date of Birth）、血型（Blood Type） | 生物特征数据的泄露增加身份盗用和针对性攻击风险 |
| **地理信息** | 出生地（Place of Birth）、完整详细居住地址（Full and Detailed Residential Address） | 可用于地理定位和社区画像 |
| **家庭信息** | 婚姻状况（Marital Status）、子女数量（Number of Children） | 家庭结构暴露 |
| **通讯信息** | 最后一次电话号码签发日期（Date of Last Phone Number Issuance） | 通讯行为元数据 |
| **军事信息** | 兵役状态（Military Status）、军衔（Military Rank） | **高敏感** : 暴露国家军事人员编制信息 |
| **任务信息** | 2026年已执行/待执行任务（Tasks executed or to be executed in 2026）、2027年待执行任务（Tasks to be executed in 2027） | **极高敏感** : 暴露国家安全机构当前和未来的行动计划 |

## DTX机构背景

**阿塞拜疆国家安全局（Dövlət Təhlükəsizliyi Xidməti, DTX）** 是阿塞拜疆的主要国家安全和情报机构，其职责涵盖：

* 国家安全情报收集与分析
* 反间谍与反恐怖主义
* 国家机密信息保护
* 边境安全与移民管控（公民身份数据库管理）
* 网络安全与关键基础设施防护

DTX作为阿塞拜疆的"国家安全守护者"，自身全量公民数据库遭泄露构成机构性的安全失败。

### 数据真实性评估

| 信号维度 | 正向信号 | 负向信号 |
| --- | --- | --- |
| **数据字段特异性** | 字段列表极为详尽，涵盖18个数据类别，远远超出普通诈骗者能够虚构的细节水平 | — |
| **数据时效性** | 声称更新至2026年6月28日（4天前），若属实则为"热数据"，具有极高行动价值 | 距泄露仅4天，数据如此"新鲜"可能不真实 |
| **机构合理性** | DTX确实负责阿塞拜疆公民身份数据库管理（数据来源机构自洽） | — |
| **论坛地位** | "Immortal"等级暗示长期活跃或付费会员，非一次性账户 | 声望值=0，无任何已验证交易记录 |
| **验证材料** | 提供了4张数据库截图（.webp格式） | 截图仅展示了表格界面，无法验证数据真实性和规模 |
| **行为者警告** | 明确警告"不诚心者勿扰"——典型的真实卖家行为模式 | — |
| **文件格式说明** | 主动声明"因转换为Excel格式可能存在数据错误"——增加了操作细节的可信度 | — |
| **数据规模** | 未明确声明记录总数——异常：通常卖家会以此作为卖点 | ⚠️ 未声明数据规模是重大疑点 |

**初步判断：数据字段描述的专业性和详尽程度不支持"完全虚构"假设。DTX确实负责公民身份数据库管理。但缺乏验证材料且未声明数据规模使得真实性无法确认。存在以下场景：**

1. **真实泄露（概率：中）**：DTX内部系统遭渗透或内部人员泄密，数据被导出贩卖
2. **部分真实（概率：中低）**：数据真实但规模被夸大（例如仅是某个地区或部门的子集）
3. **拼接伪造（概率：中低）**：利用多个公开泄露源拼凑而成的合成数据库
4. **反情报诱饵（概率：低）**：针对阿塞拜疆敌对情报机构的蜜罐操作

## 威胁行为者分析："0cx00iq"

**ID命名分析**："0cx00iq" 的命名模式：

* "0cx" 可能是变体拼写或代码
* "00iq" 可能暗示"零智商"的自嘲或反讽
* 该ID在Telegram和Breached论坛保持一致，表明建立了一定的品牌连续性

**行为模式研判**

| 信号 | 研判 |
| --- | --- |
| **论坛等级 Immortal** | 暗示该账号在Breached平台有较高活跃度或付费等级——非临时/路过账号 |
| **声望值=0** | 但可能从未完成过可验证的交易，或交易未被社区评分系统捕获 |
| **积分250** | 中等积分水平，符合活跃但非顶级卖家特征 |
| **双重Telegram存在** | 频道+账号的配置表明其有持续运营意图（频道用于广播更新，账号用于交易沟通） |
| **Session ID提供** | 提供端到端加密通讯选项，表明具备基本OPSEC意识 |
| **警告措辞** | "不诚心者勿扰"——典型暗网卖家话术，用于过滤低质量买家 |

## DTX泄露影响评估

| 影响维度 | 评级 | 分析 |
| --- | --- | --- |
| **国家安全影响** | **极高** | 若数据真实，阿塞拜疆全量公民身份数据库将落入敌对情报机构手中，构成国家级安全灾难 |
| **军事安全影响** | **极高** | 兵役状态、军衔、2026-2027任务分配信息暴露将直接危及DTX行动安全和现役人员 |
| **公民隐私影响** | **极高** | 完整身份+生物特征+家庭+地址的全套个人信息暴露将导致大规模身份盗用和针对性犯罪 |
| **机构声誉影响** | **灾难性** | 国家安全机构自身数据库被完整导出贩卖——构成该机构历史上最严重的安全失败 |
| **地缘政治影响** | **高** | 高加索地区地缘博弈中，阿塞拜疆公民数据落入亚美尼亚、俄罗斯、伊朗或土耳其情报机构手中将改变情报力量平衡 |

**重点关切：军事任务字段**

DTX数据库中"2026年已执行/待执行任务"和"2027年待执行任务"字段是本次泄露中最具行动安全破坏力的内容。若数据真实：

* 当前正在进行的DTX情报行动将被直接暴露
* 长期渗透的卧底/线人可能被反向识别
* 2027年度的行动计划将成为对手手中的"剧本"

## DTX数据库泄露总结

1. **若为真实，构成国家灾难级安全事件**：国家安全机构的公民全量数据库被完整导出贩卖，在情报史上属于极为罕见和严重的事件。
2. **军事行动安全面临直接破坏**：2026-2027年任务分配字段的暴露可能使DTX的现有和计划行动被对手提前掌握。
3. **真实性待验证**：数据描述的详尽性支持真实性假设，但缺乏数据规模声明、无独立验证渠道、行为者信用记录为空等因素使得判断存在较大不确定性。
4. **卖家画像**：0cx00iq 显示出一个具备基本OPSEC意识、有持续运营意图（Telegram频道+账号）、但信用记录尚待建立的卖家形象。

## 威胁情报全球监控系统

由全球威胁情报系统（cti.libaisec.com）实时监测发现，订阅会员即可查看威胁情报详情及原文。

![cti.libaisec.com](https://mmbiz.qpic.cn/mmbiz_jpg/es3jUghv8r8DhC4fjxJnxIfSmn2lg9Uf4vWcJftqX4rN1g3Qgr8aHIu1iaK0fFQrs4ZIcibmVgRCIu4xh0yUkEAvT3aShWUmvUNxibx63PYTxY/640?wx_fmt=jpeg&from=appmsg)

cti.libaisec.com

**监测内容**

* 数据泄露事件
* 勒索软件事件
* DDoS攻击事件
* 恶意软件事件
* 访问权限售卖
* 网页篡改事件
* 日志泄露事件
* 网络钓鱼事件
* 漏洞情报监控
* ......

系统会员了解及订阅可联系以下微信，备注来源【威胁情报】

![威胁情报](https://mmbiz.qpic.cn/mmbiz_png/es3jUghv8ric93zBcJHdfbcibS3Tre5cF6v6TWhZHTmuS5iaic02EM83DDiaPCzBPIicNyK9GFyINicl37aqBphIWianC0RxkldWEYA5zP1mIcYmyLE/640?wx_fmt=png&from=appmsg)

威胁情报

预览时标签不可点

阅读原文

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/GLyX5CgG8A1AjQiarwFHPJibeWbc1nhED6yPPhcfplNAzMjXJx106p9J3HaRZUNyBAhECfklMPvyOsReia0qaVV8A/0?wx_fmt=png)

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