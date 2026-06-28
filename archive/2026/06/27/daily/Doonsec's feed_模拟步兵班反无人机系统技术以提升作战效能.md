---
title: 模拟步兵班反无人机系统技术以提升作战效能
url: https://mp.weixin.qq.com/s/O64oB575O7RqJGe7yn951g
source: Doonsec's feed
date: 2026-06-27
fetch_date: 2026-06-28T06:12:08.225200
---

# 模拟步兵班反无人机系统技术以提升作战效能

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/j4GUibt374qeT9Z9xxa55jTTKQ0SG0m2BI27iaXAVqoMRm0xwNk4Xwvyzrz4X9TKeMve11vnmgsutPN6qhnPDwLVUiaOIdJTnZBZIYuBtPUk2Q/0?wx_fmt=jpeg)

# 模拟步兵班反无人机系统技术以提升作战效能

原创

所长007
所长007

蓝军开源情报

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

关注****▲蓝军开源情报▲****和10万+情报研究员，一起成长

****【导读】****

2026年4月23日，美国纽约西点军校举办的年度唐纳德·R·基思将军纪念会议上，发表了《模拟步兵班反无人机技术以提高战斗力》的论文。

该论文研究应对美国陆军轻步兵编队在对抗先进小型无人机时装备不足的问题。论文运用系统工程方法，借助步兵战士模拟器，对五种原定于“全兵种机动概念聚焦作战实验”中测试的C-sUAS技术进行了定量分析，评估它们对步兵班生存能力和杀伤力的影响。

结果表明，通过降低被发现概率并强化信号特征管理，能显著提高部队在敌方无人机面前的生存率。研究建议步兵班配备“探测-跟踪-识别”系统以预警无人机威胁，并使用多光谱伪装斗篷以躲避探测；若部队需要在机动中防空，则建议配备自主反无人机地面车辆。

《模拟步兵班反无人机系统技术以提升作战效能》英文原文6页。扫码文末二维码，加入蓝军开源情报知识星球会员，免费下载本文原文。需要报告联系电话：19118805880（微信同号）。

关键词：小型无人机系统；反无人机系统；步兵战士模拟器；机动概念聚焦作战实验；生存能力；多光谱伪装斗篷

![](https://mmbiz.qpic.cn/mmbiz_png/j4GUibt374qcichYRib7QctwMrHOlYjhqRBdSjA3MFLs7oJe52olcD36zuAaAF0xKJEnia8SQ9sQqYGsRCm2Hnx9AltR3eiaelBn7UxM5TB8aAII/640?wx_fmt=png&from=appmsg)

这是蓝军开源情报的第 ****633****期分享

## 编译 l 所长007

## 来源 l 蓝军开源情报（ID：Lanjunqingbao） 转载请联系授权（微信号：19118805880）

一、简介

最近的冲突已经证明了小型无人驾驶航空系统的作战效能。sUAS的功能已融入所有作战职能，支持情报、监视和侦察，后勤保障，并能对装甲部队和下车步兵实施直接的致命打击。

本文所采用的方法严格遵循了经典的系统工程“V”型模型。系统工程的V型模型始于高层概念和需求，随后深入到工程设计和开发阶段。系统设计完成后，将依据早期概念设计阶段制定的标准进行测试和评估。

我们最初的研究定位是协助机动未来能力局规划并执行其2026年“全兵种机动概念聚焦作战实验”。我们挑选了五项原计划在CFWE-M中进行测试或已投入使用的技术，并使用步兵战士模拟器对它们进行了建模。

最初的利益相关者参与为我们选定的技术提供了系统和子系统需求，并使我们能够制定系统确认计划和子系统验证计划。在模拟中单独应用我们选择的技术后，我们根据利益相关者的数据对它们进行了验证。

随后，我们将这些技术整合到最终的模拟中，并针对系统需求对其进行了验证和确认。最后，我们通过模拟批量运行收集数据，并对这些数据进行分析，以为我们的利益相关者提供建议。在分析中，我们采用了2^5实验设计，每种处理组合进行40次重复，总共运行1280次。

二、模拟

步兵战士模拟器是一个基于代理的战斗模拟器，专为模拟步兵作战行动而设计。该平台使用户能够呈现战术行动和决策过程，同时整合了武器系统特征、设备性能数据以及环境变量。IWARS最初由多个美国陆军实验室和分析中心开发，通过测试不同的战术、技术和设备配置，提供适合评估步兵单位对新兴威胁（包括无人驾驶航空系统）反应的分析能力。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/j4GUibt374qfjpl9H7npp64lJudMvxe0Aj3OcSVDTEwgCNnibSbHrQX4HwXwmqrEckwEIhwIBJT6YgPC4bWbYCQXaiah9XwRExm5a79j9fkXS8/640?wx_fmt=png&from=appmsg)

图 1：图形模拟情况

在IWARS中，我们开发了一个模拟场景，描绘了一个处于静止的、修改过的纵队楔形队形中的建制步兵班阵地。如上图1所示，由五架固定翼单向攻击sUAS组成的机群（代表俄乌战争中使用的机型）被分配了独特的飞行路线，直接飞过该班的阵地。

在发现队形后，无人机自主机动，靠近已识别的战斗人员并执行自杀式攻击。选择步兵班而不是排级建制进行模拟，是为了反映现代冲突中的可观察趋势，特别是在乌克兰，部队越来越倾向于在更小、分散的队形中行动，以降低空中监视和无人机精确打击带来的脆弱性。

因此，在持续的sUAS威胁条件下，对班级行动进行建模能更真实地呈现现代战场上的生存能力和战术适应性。

为了确定用于分析的C-sUAS解决方案，除了美军当前使用的C-sUAS解决方案外，我们还选择了原计划在2026年CFWE-M进行测试的C-sUAS技术。对于每一项技术，我们都评估了排在配备和未配备该技术时的表现。我们的选择并不全面，未来的sUAS威胁可能需要不同的C-sUAS解决方案。

三、模拟结果

在图2中，我们可以看到在配备RAIDER、Poncho和DTI的情况下，友军拦截无人机数量的平均值和中位数均有所增加。然而，在其他技术中几乎没有发生变化。RAIDER的影响似乎最为显著，在整个模型中约增加了1架无人机的击落量。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/j4GUibt374qehdC7X8uVXKH6O7ZUp5nfNic8KXAW5p0L8N0KpICYg5t3WGGSVm7JNcgAibByicENs4YXibxFBZ1EY9ibR5uj3zEKViaa0Fvt5EJTaY/640?wx_fmt=png&from=appmsg)

图 2：无人机死亡率箱线图

![](https://mmbiz.qpic.cn/sz_mmbiz_png/j4GUibt374qczhZS5YAm6tWzUXThahzAKHqaONlD4Ql7LhiaJr9Am7eqS7YnHjfwdu85QmYvEiapjdQ0ak5worjnict5mb41jlhC76gwbEVnq10/640?wx_fmt=png&from=appmsg)

图 3：士兵死亡情况箱线图

图3：观察我们的蓝军生存率箱线图，我们可以看到在配备Poncho和DTI系统时，四分位数和平均值发生了明显的变化。Poncho在这里的变化最为显著；它平均减少了超过2名蓝军士兵的阵亡。DTI系统的标准差较大；蓝军阵亡人数减少1人是模拟效果的中位数，而效果的平均值则是蓝军阵亡人数略有下降。在此可视化中，其他技术之间几乎没有差异。

公式1（sUAS击落量）：sUAS击落量的多元线性回归分析在公式1中呈现。结果表明，在所有模拟技术的作用下，平均增加了2.515架sUAS被击落。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/j4GUibt374qd2n629WlU5oe4s15aV1FroYp1DsGgYy9ERnFSWibApViaWiczpAiawzeh15tomYOibiawL9J2HRG8EXh06az0P9TaakGKcgBLHevZAk/640?wx_fmt=png&from=appmsg)

当从模拟中移除不同的技术时，作为独立技术表现出显著影响的显示在下方。我们知道这些是显著的，因为通过我们的多元线性回归分析，它们的p值均低于0.05。

我们还对这些技术的交互作用进行了分析。在这里，我们发现显著的交互作用（p值低于0.05）是DTI-RAIDER、DTI-Shotgun、DTI-Poncho和BOSS-RAIDER。

正如我们所见，当DTI与RAIDER、Shotgun或Poncho结合使用时，它起到了预警系统的作用，使智能体能够摧毁威胁或隐藏自己。而关于BOSS和RAIDER的交互作用，可以解释为BOSS隐藏了RAIDER，从而给了它更多的交战时间，因为无人机清除RAIDER的目标会变得不那么清晰。

公式2（生存率）：关于蓝军阵亡人数的方程式，我们进行了同样的多元线性回归，发现具有显著影响的技术是DTI、RAIDER、Shotgun和Poncho。这是基于这些技术相关联的极低p值。

![](https://mmbiz.qpic.cn/mmbiz_png/j4GUibt374qdKoshsQ3jjLgv6uGwmibrSuLiaibKfyicibn8zpIWicYJQeun5E7jyLvkQZ4ZaqbVhB0hbeFm6IibShqib4pXPUm2huQ8viaian86NiaQDibE/640?wx_fmt=png&from=appmsg)

极低的p值表明这些技术对蓝军阵亡人数的增加或减少有显著影响。在比较所有这些系数时，我们根据采用所有技术时的蓝军阵亡人数（Y截距）对它们进行了缩放，平均阵亡人数为1.087人。

四、结论

无论部队的任务和处境如何，我们建议轻步兵班配备一套DTI系统，并且每位士兵都配备一件多光谱伪装斗篷，以取代他们的标准配备斗篷。标准配备和多光谱伪装斗篷之间的互换不会增加士兵的负重。

DTI系统为士兵增加了大约6磅的负重。这两种解决方案都显著增加了对sUAS的摧毁，并显著减少了友军的伤亡。为了获得最大效果，该班必须愿意牺牲机动性以降低可探测性。

当班组探测到无人机时，他们应停止移动，增加分散度，并用斗篷将自己完全隐藏起来。移动或不完整的斗篷覆盖会损害斗篷的有效性。如果部队无法保持静止，我们建议让自动C-sUAS无人驾驶地面车辆（类似于RAIDER）随行巡逻。

RAIDER对增加无人机的摧毁起到了最大的作用，并有可能将sUAS的注意力从友军部队引开。在运输部队时，需要考虑到像RAIDER这种系统的尺寸和重量。

鉴于装备霰弹枪时误伤率上升，我们不建议在没有进行大量C-sUAS霰弹枪训练并制定交战标准的情况下配备霰弹枪。我们不建议配备BOSS手榴弹——态势感知能力的丧失不值得换取生存率上的微小潜在提升。

未来的工作应在深入研究C-sUAS系统时整合新技术，并随着未保密的模拟技术数据发布来更新模拟系统。IWARS在模拟的复杂性上存在局限，因此使用更复杂的软件将有助于整合多样化的地形、火力及部队配置。

无论采用何种模拟平台，未来的研究都应涵盖复杂地形（如山地和植被）以及任务执行期间的C-sUAS行动。尽管IWARS在班排级分析中表现出色，但其他模拟环境或许能为更大范围的研究提供更强大的支持。Bohemia Interactive Simulation开发的现代合成训练与模拟环境Virtual Battlespace 4便是一个例子。

VBS4提供了更优秀的图形渲染、改进的物理建模、大规模地形融合，以及先进的联合与多域作战模拟，从而能更细致地呈现复杂的作战环境。未来模拟系统最重要的改进将是，随着模拟技术的实际能力被公开披露，及时准确地将其反映在模拟之中。

《模拟步兵班反无人机系统技术以提升作战效能》【目录】

一、简介

1.1 背景

1.2 研究方法

二、模拟

2.1 模拟场景

2.2 反sUAS平台

三、模拟结果

3.1 IWARS输出与统计分析

3.2 分析

四、结论

4.1 建议

4.2 未来工作

参考文献

获取资料目录：19118805880（微信同号）

![](https://mmbiz.qpic.cn/mmbiz_png/j4GUibt374qfyqwL8S6CUJiaQfNhtmRvHCF8IAFodhtE56GicHII70f5dJtzvAgiccFEFJgv1l7Y7iaP8NgP1Kn0Lo0NuMkuaibeElp4QXnOefobk/640?wx_fmt=png&from=appmsg)

**👇👇**

**加入蓝军开源情报星球会员******免费下载********3000****+****资料********

**👇👇**

## **原价999元！** **星球试运营期间199元！** **试运营结束，恢复原价！**

**扫码了解、加入**

**👇👇**

![](https://mmbiz.qpic.cn/mmbiz_png/j4GUibt374qeer81xJXCc4Tdw8U2UlNzQI9adxibygUqZSOdTw9ZNd3oibj0brEMT6q3iaPM2oPDYYnuEw6njh91j0xKSL7LBXLkNkQp79o5oNs/640?wx_fmt=png&from=appmsg)

预览时标签不可点

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/Dnib8qWYVeRr8RC005ItAdQ4c3r8noyVIpzjP52lXUWRMHxIcRgsB2JAiaqCtzg10AaibqtszMbbYHCU3vhS4bEXg/0?wx_fmt=png)

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