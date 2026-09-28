---
title: 【教程】开源情报-社交媒体、地理位置与图像
url: https://mp.weixin.qq.com/s/JTNb-6dn5xTXhluGJ1WQuA
source: Doonsec's feed
date: 2026-09-27
fetch_date: 2026-09-28T07:53:32.030305
---

# 【教程】开源情报-社交媒体、地理位置与图像

# 【教程】开源情报-社交媒体、地理位置与图像

原创

丁爸
丁爸

丁爸 情报分析师的工具箱

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

![](https://mmbiz.qpic.cn/mmbiz_png/no8YFGgia2NFY1W4q6papmv62EufhfRtiaYB3gOdesRnWOGYPEibXBicrdykN1j4rAIJW0wm9CHaRIkPhFtwutVbzqqvHnYnbByh1Tbd9qNx8hk/640?wx_fmt=png&from=appmsg)

目录

引言　关于本教程

第一章　人员搜索引擎与情报采集基础

1.1 人员搜索引擎的价值

1.2 常用免费人员搜索引擎

1.3 两项核心任务：记录与枢轴

1.4 案例演示：从角色名到真实人物

1.5 数据验证与多源聚合

第二章　Facebook 分析

2.1 社交媒体为何是情报富矿

2.2 Facebook 上可获取的数据

2.3 Graph Search 的变迁

2.4 检索与筛选技巧

2.5 合规边界

第三章　LinkedIn 数据分析

3.1 平台定位与情报价值

3.2 个人与组织画像

3.3 泄露数据的作用

第四章　Instagram 分析

4.1 平台概述

4.2 内容与位置线索

4.3 辅助工具与数据抓取

4.4 使用边界

第五章　Twitter 数据分析

5.1 平台概述与关键概念

5.2 推文检索与关系网络

5.3 行为与情绪分析

5.4 位置线索

第六章　地理位置定位

6.1 为什么需要定位

6.2 元数据取证

6.3 视觉线索提取

6.4 地图与影像比对

6.5 典型案例：Strava 热力图

第七章　图像与地图

7.1 图像情报的价值

7.2 反向图像检索

7.3 街景与相册球

7.4 卫星与航空影像

7.5 图像分析工作流

第八章　合规、伦理与操作安全

8.1 法律法规层

8.2 伦理准则层

8.3 操作安全层

附录A　常用工具清单

附录B　术语表

# **引言　关于本教程**

开源情报（Open Source Intelligence，OSINT）是指围绕公开可获取的信息开展的系统化采集、处理、分析与验证，并最终形成可供决策使用的情报产品。与依赖秘密手段的传统情报不同，OSINT 的生命力在于**合法、可复现、可验证**：任何一名调查人员，只要掌握正确的方法，都能在公开渠道中还原出目标的人物画像、社会关系、活动轨迹与行为规律。

本教程聚焦 OSINT 实践中与调查工作结合最紧密的一个分支——**社交媒体、地理位置与图像**。这三个主题并非彼此独立：社交媒体提供了海量的人物与关系数据，图像承载了最直观的现场证据，而地理位置则把“谁”与“在哪里、做什么”连接起来。三者相互印证，构成完整的情报链条。

|  |
| --- |
| **内容来源与定位**  本教程以 SANS 学院 SEC487《Open Source (OSINT) Intelligence Gathering and Analysis》课程第 3 部分 487.3 “Social Media, Geolocation, and Imagery”为蓝本进行中文改编：保留其知识框架、方法要点与典型案例，补充中文语境下的说明，并重新绘制全部概念示意图。教程面向开源情报分析人员、情报学研究者、安全与合规从业者以及新闻调查人员。 |
| **学习目标**  ① 理解开源情报的基本流程与合规底线；② 掌握人员搜索引擎的使用与“枢轴”调查方法；③ 熟悉 Facebook、LinkedIn、Instagram、Twitter 等平台的数据特征与采集思路；④ 能够对图像进行元数据与视觉线索的地理定位分析；⑤ 建立多源交叉验证与风险管控的职业习惯。 |

![](https://mmbiz.qpic.cn/sz_mmbiz_png/no8YFGgia2NFyichkOaGCfhKP4PHPkIOf6RosuQB6iahUCLuplwbGiavA2yZyk7yUF9mZ7spUxaeO1O0J1m8peXtspib5vr2AicDVYMY4Mgu8WnSA/640?wx_fmt=png&from=appmsg)

图 1　本教程知识地图：覆盖人员搜索与四大社交平台、地理位置与图像分析共 7 大模块

开源情报工作并非“一次性检索”，而是一个循环往复的过程。下图概括了从需求到产出的完整情报循环：每一次分析中发现的“枢轴点”，都会驱动下一轮更有针对性的采集，直至信息收敛、结论可信。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/no8YFGgia2NFm2SlfiaBcGDJOuuoicuY2oyHW5ia7536yOpXdPomhyP1sTVyxPRHuuc9UwPUWXo8ZExeMibKLUIPXkuBDtcLIo7tS9XebLVyrFhU/640?wx_fmt=png&from=appmsg)

图 2　开源情报分析流程（情报循环）：需求—采集—处理—分析—产出，并形成反馈闭环

# **第一章　人员搜索引擎与情报采集基础**

调查往往从一个人名开始。人员搜索引擎（People Search Engines）是专为“找人”而设计的检索工具，它把分散在公开记录、社交平台与商业数据库中的碎片信息聚合到一处，从而极大压缩调查所需的时间。

## **1.1 人员搜索引擎的价值**

通用搜索引擎收录的是“万物”的信息，而人员搜索引擎聚焦于**人**及其关联信息。借助这类工具，分析人员可以围绕以下维度快速建立初步档案：

· **姓名**：目标的全名、曾用名与拼写变体；

· **地址**：现居地、历史居住地及邮政编码；

· **电话**：座机与移动号码，以及号码归属线索；

· **用户名与社交媒体**：目标可能使用的账号名与平台入口。

当一次检索返回多个同名结果时，分析人员需要提供更具体的限定条件（如年龄段、城市或州）来缩小范围，并对每一条结果进行甄别，而不能默认“第一条就是目标”。

## **1.2 常用免费人员搜索引擎**

部分人员搜索引擎会免费开放一部分数据，其余则引导用户付费获取。以下工具是实践中较常使用的免费入口：

|  |  |
| --- | --- |
| **工具** | **主要用途与特点** |
| peekyou.com | 以用户名与社交账号关联见长，可发现同名账号 |
| thatsthem.com | 可直接返回姓名、地址、电话、邮箱等综合记录 |
| truepeoplesearch.com | 以居住地址与电话为核心，结果较为结构化 |
| cubib.com | 聚合公开记录，提供人物与关系线索 |
| zabasearch.com | 老牌人物检索，覆盖地址与电话历史 |
| radaris.com | 综合人物档案，提供关系网络与背景信息 |

![](https://mmbiz.qpic.cn/mmbiz_png/no8YFGgia2NEey4g4mvobN2UQ48syjloaPyDQ2laAqqoTKXYQbfZWnngvMG6AZ4bvHiaQOJicJaa2hekMQEKWYwUzTKcM4Hpv8LbBmUVjibCSKU/640?wx_fmt=png&from=appmsg)

 图 1-1　示例：多款免费人员搜索引擎

（Radaris、That’sThem、TruePeopleSearch、PeekYou、ZabaSearch）

需要注意的是，不同站点可能**共用同一后端数据**——界面不同、数据同源。因此在其中一个站点提交“移除信息”请求，可能会连带影响其他站点的检索结果。这一现象本身也是情报线索。

## **1.3 两项核心任务：记录与枢轴**

在人员搜索引擎上，分析人员必须完成两项最关键的工作：

1.**完整记录**所有与目标相关的数据，用于后续核验与印证；

2.**识别枢轴点**（pivot point）——即可以作为新检索输入的字段，如地址、电话或账号名。

“枢轴”是 OSINT 调查的核心动作：把一条检索结果中的可靠字段，作为下一轮检索的起点。例如，检索“Inigo Montoya”返回一个位于西班牙的地址，接着以该地址为输入再次检索，就可能牵出更多与该地址相关的人物与事件。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/no8YFGgia2NE1qHGNILRDQicn7QpeiaXJDv5TDPmV0evXqXibpbPlJs6icKuVialwfgu7NdAKaf8mWhaLWhkWJ7MvHIOpkzmyR9iasoUgna4QOA1PU/640?wx_fmt=png&from=appmsg)

图 1-2　人员搜索引擎的“枢轴”工作流：姓名—地址—电话/邮箱—社交账号，循环收敛

## **1.4 案例演示：从角色名到真实人物**

原文以《公主新娘》（The Princess Bride）中“Inigo Montoya”一角为例：该角色由演员 Mandy Patinkin 饰演。以“Mandy Patinkin”为关键词在 thatsthem.com 上进行检索，返回了两条详细记录，分别对应康涅狄格州与纽约州的两处地址，并附有电话与邮箱。

面对多条结果，分析人员不能简单取用。由于目标活跃于演艺圈、工作地点常在纽约，**纽约的记录更可能是目标本人**；但仍需借助其他公开记录对其进行验证或证伪，并把地址放到地图上比对，观察其是否符合目标的生活与工作习惯。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/no8YFGgia2NEGv5c5DbbDEHaibj6gEqF8t1uOrHBwFyiaqByS4iccRJBz4YjrgqJCY8MGQXjGwWxdE0eSJ3npVn8FZLlkv1hosDA0njCwYrktrg/640?wx_fmt=png&from=appmsg)

图 1-3　示例：thatsthem.com 返回的两条“Mandy Patinkin”记录（含地址、电话、邮箱）

|  |
| --- |
| **方法论提示**  人员搜索引擎的结果只能作为“线索”而非“结论”。每一条记录都应追问三个问题：它与其他来源是否一致？它是否指向同一人？它能否被独立来源证实？ |

## **1.5 数据验证与多源聚合**

单一来源的信息永远不足以支撑结论。OSINT 分析强调**多源交叉验证**（corroboration）：把社交媒体痕迹、地图与影像、公开记录与泄露数据等不同来源的证据聚合起来，一致则提升置信度，冲突则回到采集阶段寻找更多证据。

![](https://mmbiz.qpic.cn/mmbiz_png/no8YFGgia2NGrxWcgIEqicZ7HqpMHbcqqMgibTDdh19Ehnic80mIhujQXqcmRl17iawopiaHx1DtpIuATtzf5s8VR97MSTdCm6Jg6siaKzG9CCdEgo/640?wx_fmt=png&from=appmsg)

图 1-4　多源交叉验证：不同来源的证据汇聚为可信结论，并给出置信度评估

# **第二章　Facebook 分析**

社交平台是开源情报的“信息富矿”。了解人们为何使用社交媒体、以及平台允许公开展示哪些信息，是高效采集的前提。

## **2.1 社交媒体为何是情报富矿**

人们使用社交媒体的动因多种多样：与他人分享、维系社会关系、塑造“专家”形象，以及单纯的“围观他人”。这些动因共同决定了平台上沉淀了丰富的人物、关系、观点与位置数据。对情报分析而言，社交媒体不仅提供目标自述的信息，也提供了其亲友、同事所透露的间接信息。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/no8YFGgia2NEwtw93LDO0ibCWt0Vq4My4pHrqmVlHoNTnNJfTlCRBTQraDrINbjhuwrhOoJX5oXmmj3f3pV3albS5QuwIZiav8GtBd8yOGukf0/640?wx_fmt=png&from=appmsg)

图 2-1　社交媒体的使用动机（分享、维系关系、专家形象、围观）

不同平台的数据“丰度”各异。下表从五个维度对人员搜索引擎与主流社交平台进行了对比，有助于在调查初期选择正确的信息源。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/no8YFGgia2NHeS2Uw6HibBwc1H3vHyLXWgA7y8NsrJicmzd1KAMwQHhhiapaOsRkBvT0jt1rCBnaLHcUA8fnxznGXj7wRSXHTWntULoibSt6Ip8s/640?wx_fmt=png&from=appmsg)

图 2-2　主流社交平台可采集的数据维度对比（● 丰富　◐ 部分　○ 有限/需授权）

## **2.2 Facebook 上可获取的数据**

如果目标使用 Facebook，该平台往往能提供极为丰富的公开信息，包括：

· 目标本人的**照片与视频**；

· 目标表达过的**喜好与倾向**（点赞、分享）；

· 目标的**好友关系网络**；

· 目标加入的**群组**；

· 目标“到访过”的**地点**（签到、标签）；

· 目标**受邀与参加过的事件**。

平台同时设置了访问控制，会在一定程度上限制可获取的内容。分析人员需要在合规前提下，评估这些控制措施的影响，并采用相应的方法获取公开可达的数据。

## **2.3 Graph Search 的变迁**

|  |
| --- |
| **重要变化提醒**  2019 年夏季，Facebook 对站内搜索进行了根本性调整，改变了搜索的编码、语法与词汇体系。大量旧工具与旧文档一夜之间失效。因此，凡是在 2019 年 6 月之前撰写的 Facebook 搜索教程，都应被视为“历史资料”，不能直接照搬。 |

这一变化对隐私倡导者而言是进步，但对情报调查与执法工作造成了不少困难——许多过去依赖的搜索功能与人物、地点关联查询已不再可用。分析人员需要重新学习新的检索方法，并优先掌握相对稳定、长期有效的思路（如公开主页浏览、关系网络梳理等），而非依赖易变的语法技巧。

## **2.4 检索与筛选技巧**

Facebook 的搜索界面支持按类别（人物、帖子、照片、视频、主页）切换，并支持在结果中追加筛选条件。例如，回到“人物”类别后，选择“城市”筛选并输入城市名，可以快速把结果限定到特定地区。

![](https://mmbiz.qpic.cn/mmbiz_png/no8YFGgia2NFL0oZYYtTBGIOQUUBIaHxiaRLf5uLAFZrGDQhWP8RibvRt81OHfsS75zfcjOrIKkKqNwP1M9MYf8VBicebFxXUrljhTeq9omS2Og/640?wx_fmt=png&from=appmsg)

图 2-3　示例：在 Facebook 中通过“城市”筛选缩小人物检索范围

实务建议：**先用宽泛条件确定候选集合，再用地点、教育、工作等维度逐步收敛**；对每一条结果保留截图与访问时间，以便复现与举证。

## **2.5 合规边界**

Facebook 的信息采集必须在平台条款与适用法律框架内进行。分析人员应只处理公开可见内容，不使用虚假身份诱导、不突破访问控制、不诱导他人泄露信息。采集到的个人数据应遵循最小必要原则，并在完成分析后妥善处置。

# **第三章　LinkedIn 数据分析**

LinkedIn 把职业世界与社交媒体结合，是了解目标职业轨迹、组织关系与专业网络的首选平台。

## **3.1 平台定位与情报价值**

截至 2019 年，LinkedIn 已拥有超过 6.45 亿注册用户，覆盖 200 多个国家和地区。其核心价值在于帮助人们建立、维护与拓展职业网络。对情报分析而言，LinkedIn 上的用户数据、连接关系与分享内容，是了解个人与组织的重要来源。

由于平台沉淀了大量可公开浏览的职业信息，它也被广泛用于**公司/组织画像**（如人员规模、部门结构、关键岗位）以及社会工程学攻击的情报准备。

|  |
| --- |
| **职业风险提示**  LinkedIn 上公开的姓名、职位、单位、邮箱格式与同事关系，足以支撑一次高度可信的社工攻击。对个人而言，应审慎评估公开的粒度；对分析人员而言，应清楚这类数据的双刃剑属性。 |

## **3.2 个人与组织画像**

围绕 LinkedIn 的采集通常从三个层面展开：

· **个人层面**：教育经历、任职单位、职位名称、在岗时间与技能标签；

· **组织层面**：公司主页、业务描述、人员构成与招聘动态；

· **关系层面**：同事、上下级与跨机构连接，用于还原组织网络。

## **3.3 泄露数据的作用**

除平台自身内容外，历史上多次发生的大规模数据泄露，也深刻影响了对 LinkedIn 数据的利用。例如 ICWatch 之类的泄露数据检索站点，允许按姓名、邮箱、电话、公司等字段检索历史泄露记录，结果形态与 LinkedIn 数据相似，但可能包含邮箱与电话号码等更敏感字段。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/no8YFGgia2NGWuSAibrw1lvp6XKiaBnJkJgpslLGmJ0xOD6bgR4iaiayyVZMzbibS4oCVX6M2bPreOr5LQYVebPHBrKxgqA8kT706OgVBblCbvEaI/640?wx_fmt=png&from=appmsg)

图 3-1　示例：ICWatch 泄露数据检索界面，支持按公司、地点、职位等筛选

分析人员在使用此类数据时必须格外审慎：确认数据来源的合法性与使用授权，避免处理与调查目标无关的第三方个人信息。

# **第四章　Instagram 分析**

Instagram 是以图像与短视频为核心内容的社交平台，其“视觉优先”的特性使其在位置线索与现场信息方面价值突出。

## **4.1 平台概述**

Instagram 的主要用途是与关注者分享照片和视频。账号可分为**公开**与**私密**两类：公开账号的全部内容不受保护；私密账号则需要先获得账号持有人批准才能查看内容。平台虽提供网页版，但绝大多数用户通过手机应用发布与浏览。

Instagram 注册免费，且在当时无需邮箱或手机验证，创建新账号快速简便——这既降低了使用门槛，也为调查中的账号追溯带来一定挑战。

## **4.2 内容与位置线索**

Instagram 的照片、视频、文字说明与话题标签，常常包含丰富的位置线索：地标建筑、店铺招牌、街景特征，以及显式的位置标签。这些线索与其他证据结合后，可以支撑...