---
title: 同一份数据，美智库看到我方软肋，我们看到\"一起沉船\"
url: https://mp.weixin.qq.com/s/zBhXxzz3uhy1uFQ_0tTN4A
source: Doonsec's feed
date: 2026-07-02
fetch_date: 2026-07-03T05:44:00.315473
---

# 同一份数据，美智库看到我方软肋，我们看到\"一起沉船\"

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/JpuBd4Q1JicuomlxS6T1gWQzYvaNABe0GqFufXe5kw8VyQMaR8noU9GObh6BgpicHVUsQowticyIVZCuWN34NcPSCzD41UePSkGv2ugojpdJsU/0?wx_fmt=jpeg)

# 同一份数据，美智库看到我方软肋，我们看到"一起沉船"

原创

罗城OSINT
罗城OSINT

百灵猫开源情报分析师

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

本报告基于CSIS 《海峡困境》 报告的原始数据集，但提出不同的核心命题：台海阻断并非美国可安全操控的对华优势杠杆，而是约束美国盟伴体系、自身供应链与印太作战能力的**共享脆弱性节点**——一把**双刃杠杆**。报告采用结构化分析工作流，经统计复核与网络模拟，从四个维度为这一命题提供证据链。

## 核心发现

一、从台湾海峡贸易额占各自海运总贸易额的比例来看，美国在东亚的两个主要盟伴——韩国和日本——分别有**39.7%和35.6%**的海运贸易需要经过台湾海峡，这一比例已接近中国大陆的水平（**40.2%**），而中国台湾（**45.4%**）甚至超过了中国大陆。这意味着台海一旦被封锁，对美国盟伴体系造成的相对经济冲击，**可能不亚于对中国大陆的冲击**。

二、美国经台湾海峡的贸易呈现明显的进口大于出口（进口1020亿 vs 出口620亿），更值得注意的是吕宋海峡的逆差（进口1340亿 vs 出口370亿）高达**970亿**——这指向美国在第一岛链内的**供应链上游依赖**。

三、美军在印太的关键后勤节点高度依赖南海海峡网络（**10个关键节点中有8个**依赖海峡通行自由），战略海运能力仅存约**59%**，补给线不对称（美军>**5000海里** vs 解放军约**70海里**）构成结构性劣势。正在建设的替代路线（棉兰老燃料枢纽、巴新备用港、阿留申北极线）均处于**早期阶段**。

四、网络模拟显示马六甲海峡与台湾海峡构成南海贸易**“双枢纽”**——各自中断将影响约**4.4万亿美元**贸易和**38个**主要经济体。差异不在覆盖广度而在分布结构：台湾海峡的影响高度集中于中国大陆——中国大陆占该海峡受影响贸易总额的**29.4%**，而马六甲海峡的影响分布更均匀。

## 引言：CSIS 《海峡困境》 报告及其数据

本报告的数据基础是CSIS（美国战略与国际研究中心）2026年7月1日发布的 《海峡困境：分析南海贸易通道》 报告配套数据集，覆盖全球198个经济体在南海及周边海域八大海峡的海运贸易数据。**报告原文、中文译文及原始数据已上传至知识星球，文末扫码即可获取。**

值得一提的是，我们在使用该数据时发现一处字段说明错误：CSIS官方字段说明将Total*Trade*%标注为“百分比”字段，但在实际分析中，我们发现该列实际存储的是贸易绝对值而非比例——仅美国一项即显示为2885.451，若按百分比解读则毫无意义。经与原始数据交叉验证，确认该列为贸易总额（单位：十亿美元），字段说明有误。

CSIS报告的核心结论是：中国大陆海运贸易高度依赖台湾海峡（12880亿美元，占其海运总贸易额的**40.2%**），一旦台海发生冲突，中国大陆将承受最大的贸易冲击——报告称之为**“台湾海峡困境”**。

这一判断在数据层面成立，但它只呈现了问题的一个侧面。当我们把分析视角从中国大陆扩展到整个东亚贸易网络，同一组数据揭示了另一层结构：美国在东亚的主要盟伴对台湾海峡的相对依赖程度，**与中国大陆处于同一水平区间**。换言之，CSIS所定义的**“中国困境”**，同时也是**“盟伴困境”**。以下从四个方向展开这一命题的证据链。

## 一、方向A：盟伴的台海依赖度——“谁比中国大陆更脆弱？”

下图展示各主要经济体对台湾海峡与马六甲海峡的贸易依赖度对比。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/JpuBd4Q1JicuftN8cwEbgkWGEu6YJ99VLqDEBZES6j4gzPKTm9SXUWc7bAcic4wAibjH7UZBOHEPDzmz7iaYPavPnE8ibicu9SpvnkXpdLod61GPk/640?from=appmsg)

### 台湾海峡依赖度排名

“台海贸易占比”的计算方法为：各经济体经台湾海峡的海运贸易额 ÷ 其全球海运贸易总额 × 100%。

下图按这一比例降序排列前30个经济体。排名居首的是阿曼（**53.1%**），其后依次为中国台湾（**45.4%**）、伊拉克（**44.2%**）等，中国大陆以**40.2%**排在第六位。美国盟伴中，韩国（**39.7%**）排第七，日本（**35.6%**）排第十二，与中国大陆处于同一水平区间。韩国和日本作为美国正式盟伴，其经济对台海航线的依赖构成美国在台海问题上的**“盟伴困境”**——保护盟伴的义务与暴露于供应链断裂风险之间形成矛盾。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/JpuBd4Q1JictD7PgtT7fm9FiaC2YYqvpDBxl9OLNIP4JJ0pcO9Mjgh3oTlePwvVvFwehg5WB5y3lic83PxceBr5NNxfvj0GbrbogRWMagKiclPI/640?from=appmsg)

### 区域统计检验

| 组别 | 样本量 | 均值 | 中位数 | 标准差 |
| --- | --- | --- | --- | --- |
| 美国盟伴（7个） | 7 | 29.3% | 35.6% | 7.3 |
| 中国大陆 | 1 | 40.2% | 40.2% | — |
| 中国台湾 | 1 | 45.4% | 45.4% | — |
| 其他大型经济体（≥500亿） | 9 | 9.8% | 7.9% | 6.8 |

单因素方差分析（ANOVA）比较美国盟伴组与其他大型经济体组的台海依赖度差异：F值显著，p值低于0.05。盟伴组均值高于对照组，但由于对照组样本量有限，该结果应视为探索性证据而非确认性检验。从描述统计上看，韩国和日本分别有39.7%和35.6%的海运贸易经过台湾海峡，与中国大陆的40.2%处于同一水平区间；而对照组中其他大型经济体的这一比例**均不足25%，差距明显**。

| 经济体 | 台海占比 | 马六甲占比 | 差值 | 台海进口占比 | 海运总贸易 |
| --- | --- | --- | --- | --- | --- |
| 美国 | 5.7% | 6.2% | -0.5% | 7.2% | 28855亿 |
| 澳大利亚 | 24.8% | 13.7% | +11.1% | 18.6% | 5476亿 |
| 新加坡 | 24.4% | 32.3% | -7.9% | 17.6% | 3807亿 |
| 日本 | 35.6% | 23.4% | +12.3% | 35.5% | 11577亿 |
| 韩国 | 39.7% | 23.0% | +16.7% | 42.3% | 7562亿 |
| 中国台湾 | 45.4% | 19.3% | +26.1% | 28.3% | 5172亿 |
| 中国大陆 | 40.2% | 30.0% | +10.2% | 58.5% | 32047亿 |

*注：①台海占比 = 经台湾海峡的海运贸易额 ÷ 该经济体全球海运贸易总额；②马六甲占比 = 经马六甲海峡的海运贸易额 ÷ 该经济体全球海运贸易总额；③差值 = 台海占比 − 马六甲占比，正值表示对台湾海峡的依赖高于马六甲海峡；④台海进口占比 = 经台湾海峡的进口额 ÷ 该经济体全球海运进口总额。*

这意味着台海航运一旦被阻断，遭受冲击的并非中国大陆一方——**美国盟伴体系也将同步承受损失**，且从相对比例来看，这些损失的程度不亚于中国大陆。美国如果将台海航线作为施压工具，**首先承受压力的并非其目标方，而是其自身的盟伴网络**。

## 二、方向B：美国的进口盲区

美国经台湾海峡的总贸易额为1640亿美元，仅占其海运总量的**5.7%**，看似风险有限。但将进口与出口分离，不对称性立即暴露。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/JpuBd4Q1JicvxpiaLsEPUOXWR3iahkOEK22v8Xdk5b2BwQfx298iaKmk040LLaWibQUpNNGrC2e7clqSzMmsiaerux61UX0HL5Oolon1XJDej4GMA/640?from=appmsg)

美国在多个海峡的贸易都呈现系统性进口额高于出口额的特征。吕宋海峡逆差居首（进口1340亿 vs 出口370亿，逆差**970亿**），台湾海峡（逆差400亿）和马六甲海峡（逆差300亿）次之。三海峡合计逆差约**1680亿美元**。

进口额高于出口额的贸易结构，通常意味着该经济体依赖从对方进口制成品和中间品。吕宋海峡连接南海与菲律宾海、是第一岛链东缘的重要通道，其高逆差可能反映美国从东亚（尤其是中国大陆、日本、韩国）的此类商品经由此航线。这揭示了一个**战略盲区**：美国在推动**“供应链去风险”**的同时，其进口航线对南海海峡网络的依赖可能被**系统性低估**。

### 盟伴的“台海vs马六甲”格局

下图展示各经济体在台湾海峡与马六甲海峡之间的依赖结构差异。东亚各经济体——中国大陆、韩国、日本和中国台湾——均呈现对台湾海峡的贸易依赖度高于马六甲海峡的特征，澳大利亚虽也偏台海（台海24.8% > 马六甲13.8%），但暴露程度明显低于韩日。美国是唯一**“两者接近”**的域外国家。新加坡则偏马六甲。这意味着台海冲突对不同盟伴的经济冲击**高度差异化**——韩国和日本面临其主通道被切断的风险，而新加坡、澳大利亚受影响的程度明显较低。

![](https://mmbiz.qpic.cn/mmbiz_png/JpuBd4Q1JicuatZAB1GZjTodAbP3GxnicPUcHGialzA0JFkfzrHFQsSKlcu6XN9fKXZvfYTsdfibylVPlJibj4hY7JVubzsNgMtYjJJELd2q2YEc/640?from=appmsg)

这一差异化暴露程度直接影响美国在台海危机中的联盟管理难度：受影响最严重的盟伴（韩国、日本）恰恰是美军在东亚最重要的驻在地，其合作意愿与承受能力将直接决定联盟行动的可维持性。

换言之，美国并非台海博弈的外部裁判，而是**同一网络的体系内参与者**。试图以台海航运为施压工具的操作者，**其自身供应链同样暴露在杠杆之下**。

## 三、方向C：美军印太后勤的“海峡依赖”

美国在印太的军事存在**高度依赖**南海海峡网络的通行自由。以下基于2024—2025年公开军事分析、国会证词和防务新闻报道梳理美军后勤补给线对海峡网络的依赖关系。

（注：本节基于公开军事分析、防务新闻和国会证词的定性归纳，与A、B、D节基于CSIS贸易数据的定量分析属于不同证据层级，不可直接类比。）

美军在印太面临三个结构性的后勤困境：

第一，**补给线不对称**。美军从西海岸到东亚前线超过**5000海里**，解放军跨越台湾海峡约**70海里**。这一差距使美军在持续冲突中的后勤保障处于根本性不利。

第二，**战略海运能力持续萎缩**。截至2025年，军事海运司令部战略海运船只完好率已降至约**59%**，每年海运承载能力减少9—18万平方米，合格商船船员缺口超过**1800人**。

第三，**前置基地均处于打击威胁范围内**。驻日（横须贺、嘉手纳）、关岛、菲律宾等多数关键节点处于中国大陆中程打击威胁范围。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/JpuBd4Q1Jict5n1iblqStwoiciaicBfbk9Wzh7TNpQviazicnQMibtfOcnnSqGwnSv7bEXFCcx80RFozOvBVgpc6qxVMgNTO0stWz85hOxXYZ2ymt5w/640?from=appmsg)

### 关键后勤节点的海峡依赖

上表显示：美军印太**10个关键后勤节点中有8个**高度依赖南海海峡通行自由。台湾海峡、吕宋海峡、马六甲海峡构成美军西太平洋补给线的**“铁三角”**——每一处中断都将产生连锁效应。

正在建设的替代路线包括菲律宾棉兰老岛的燃料枢纽（2025年启动招标）、巴布亚新几内亚的备用港口评估，以及阿拉斯加—阿留申群岛的“北极替代线”概念。但这些方案**均处于早期阶段**，短期内无法实质缓解海峡依赖。

综合来看，美军印太后勤对南海海峡网络的深度依赖意味着，台海冲突不仅冲击盟伴经济，更直接影响美军的作战维持能力。军事执行者同样受同一杠杆的反向约束。

#### 参考来源

[1] USNI Proceedings, “Bring Back the Destroyer Tender,” Feb 2025 — https://www.usni.org/magazines/proceedings/2025/february/bring-back-destroyer-tender

[2] Baird Maritime, “The dangerous collapse of US strategic sealift capacity,” 2025 — https://www.bairdmaritime.com/security/naval/naval-auxiliary-support/opinion-the-dangerous-collapse-of-us-strategic-sealift-capacity

[3] Maritime Executive, “Op-Ed: U.S. Sealift Forces Are Unprepared for a Fight in the Pacific,” 2025 — https://maritime-executive.com/editorials/op-ed-u-s-sealift-forces-are-unprepared-for-a-fight-in-the-pacific

[4] AUSA Spotlight 25-1, “Contested Logistics in the Indo-Pacific,” Jul 2025 — https://ausa.org/publications/spotlight/contested-logistics-in-the-indo-pacific

[5] DLA, “REFORPAC 2025 and the friction of distribution,” 2025 — https://www.dla.mil/About-DLA/News/News-Article-View/Article/4431053/reforpac-2025-and-the-friction-of-distribution/

[6] USNI News, “Pentagon Eyes Southern Philippines as Refueling Hub,” Jul 2025 — https://news.usni.org/2025/07/22/pentagon-eyes-southern-philippines-as-refueling-base-for-u-s-warships-military-aircraft

[7] USSC, “Federation is deterrence: The US defence industrial agenda in the Indo-Pacific,” Mar 2025 — https://www.ussc.edu.au/federation-is-deterrence-the-us-defence-industrial-and-technology-integration-agenda-in-the-indo-pacific

[8] Ted Stevens Center, “Preserving and Projecting: Arctic Lines of Communication,” Apr 2025 — https://tedstevensarcticcenter.org/wp-content/uploads/2025/04/EB\_Preserving\_and\_Projecting\_08Apr25.pdf

[9] FY2025 NDAA, Sections 1235-1238 — https://www.govinfo.gov/content/pkg/CREC-2025-09-04/pdf/CREC-2025-09-04-senate.pdf

## 四、方向D：网络关键节点分析

CSIS报告的核心概念是**“海峡困境”**——各海峡作为孤立阻塞点的重要性。网络视角要求回答另一个问题：如果某个海峡被移除（因冲突、封锁或自然灾害中断通行），全球贸易网络发生什么？

### 海峡移除模拟方法

模拟步骤：①筛选全球海运贸易额≥1000亿美元的经济体（n=41）；②对每条海峡，统计经该海峡贸易额>100亿美元的经济体数量及其贸易总额；③计算受影响贸易总额占样本总海运贸易的比例；④计算“集中度”——受影响贸易额中最大单一经济体占比（反映该海峡中断的影响是否集中于少数经济体）。

此方法不同于单纯加总各海峡贸易额（存在重复计数），而是模拟“该海峡不可用时”各经济体直接暴露的贸易敞口。

![](https://mmbiz.qpic.cn/mmbiz_png/JpuBd4Q1JicuVMxUdPp41cwgvQeuzkCkAAiciaSw4gUZHdaJjeuicfqJVudoribHOsXxGtWd1pibYibs9emSpdyRxx2YqgH8lpffFKtnNp526SELwg/640?from=appmsg)

| 海峡 | 受影响经济体数 | 受影响贸易额 | 占样本海运% | 集中度（最大占比） |
| --- | --- | --- | --- | --- |
| 吕宋海峡 | 38个 | 43850亿 | 28.1% | 21.9% |
| 台湾海峡 | 38个 | 43750亿 | 28.0% | 29.4% |
| 巽他海峡 | 13个 | 6180亿 | 4.0% | 34.7% |
| 龙目海峡 | 9个 | 5370亿 | 3.4% | 37.1% |
| 望加锡海峡 | 10个 | 4830亿 | 3.1% | 35.3% |
| 巴拉巴克海峡 | 5个 | 3090亿 | 2.0% | 37.1% |
| 民都洛海峡 | 3个 | 2260亿 | 1.4% | 54.9% |

模拟结果显示：...