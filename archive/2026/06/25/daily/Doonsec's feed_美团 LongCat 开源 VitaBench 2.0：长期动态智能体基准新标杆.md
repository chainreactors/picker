---
title: 美团 LongCat 开源 VitaBench 2.0：长期动态智能体基准新标杆
url: https://mp.weixin.qq.com/s/HoiUxYnyJuh2_xdxmg8s8Q
source: Doonsec's feed
date: 2026-06-25
fetch_date: 2026-06-26T06:05:54.298278
---

# 美团 LongCat 开源 VitaBench 2.0：长期动态智能体基准新标杆

![cover_image](http://mmecoa.qpic.cn/mmecoa_jpg/V95GN2mm0Dy4aqvVwYrdqOeW07eGiaY629IAulialq9egAJXvtce6BC74CQ4jv1ibeJnIPtF0uIxAccKBmdUkibibUdKeKjSSqzxk0wT15vSBR7A/0?wx_fmt=jpeg)

# 美团 LongCat 开源 VitaBench 2.0：长期动态智能体基准新标杆

龙猫LongCat
龙猫LongCat

美团技术团队

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

![](https://mmbiz.qpic.cn/sz_mmbiz_png/JhVy5CXYiaoje0ag7FhF7lSzj8lNAjialTwvcxmRugpcmyqlL1V9vjdWdeFN03Yzw8bop8NHAg71flGcoWWHom1uiaF0c1PLo8NEMvsBuDuSZ8/640?wx_fmt=png&from=appmsg#imgIndex=0)

**一个经常加班的白领，一个带着孩子出游的父亲，你的AI助理能分清他们需要什么样的服务吗？现实是，它常常分不清。**

AI能执行你明确的指令，却很难记住那些藏在场景和身份背后的真实需求。它们是真的无法理解，还是“情商”不够高呢？

自去年10月发布了 **VitaBench 1.0**，首次定义了生活场景下智能体任务的复杂度，美团 LongCat 团队再次推出 **VitaBench 2.0，**它不再仅仅关注任务有多难，而是将目光投向了更深层次的挑战。

**VitaBench 2.0 是首个真实生活场景下面向长期动态用户建模的智能体评测基准，它系统性地评测大语言模型在长期、真实、动态的用户互动中个性化与主动性的能力。**

**🚀 VitaBench 2.0 的 核心“硬核”看点：**

* **高难度业界首创**：首次将智能体场景与丰富用户生态相结合，打造面向长期动态用户建模的智能体基准。其包含56名真实特征用户、819个复杂任务、超2000个动态偏好及66个可执行工具。
* **超长跨度动态追踪**：平均每位用户包含**2093个交互事件**，平均时间跨度长达**1580天**，严格按时间线向 Agent 暴露，真实还原用户偏好的演进与漂移。
* **统一评测生态**：针对长文本上下文学习（In-context learning）与智能体记忆策略（Memory Strategy）的统一评测平台。

![](https://mmbiz.qpic.cn/mmbiz_png/JhVy5CXYiaogKdufxYTESAuA0WNfMQSsDdH7ibZmZTGH41tenDLo826GgbU1M8R8jg9sIB0qnfgfG6T8mJopGnt9xYb0t8l4zibzPJ79dEuayY/640?wx_fmt=png&from=appmsg#imgIndex=1)

能得出这些结论，得益于VitaBench 2.0的核心设计。它不再是简单的问答，而是围绕三大创新构建了一个前所未有的评测体系。

![](https://mmbiz.qpic.cn/mmbiz_png/JhVy5CXYiaojjGUCHfo1tCKwYMM8hJCqibUB52hvqDpZvWIayaAn1c9bOKy0sgQz4ojMRHKwbp1FpmL13KFel1SWlm43dqegA0Ria8clicceR2Q/640?wx_fmt=png&from=appmsg#imgIndex=2)

VitaBench 2.0 概览图

![](https://mmbiz.qpic.cn/sz_mmbiz_png/JhVy5CXYiaoialEB1ZLq3qG0lic8DoODHgto7nLv4zGeXzD3tT74wTUvKKibGEjibkZ3tK1dc7xoqTD7Gibn02UJ5GiaibviaQmq9A6wwtXfbVEJWjwc/640?wx_fmt=png&from=appmsg#imgIndex=3)

不同于一次性的问答，VitaBench 2.0为 56位虚拟用户，在送餐、到店、差旅等多个真实领域中，构建了包含2000多种动态偏好、跨度长达数年的生活轨迹。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/JhVy5CXYiaoiaFe8br8C2iaFib1wFR5e1SRbasH8q2ge2Sud1gC43MziclvKfQKgH04Duy2aic2Gjv2VpxnWThXaANKDMEAyiaLwz6UGCHcKtnhF9E/640?wx_fmt=png&from=appmsg#imgIndex=4)

VitaBench 2.0 用户画像统计图

这背后是庞大而真实的数据支撑。**如下图所示**，这些图表直观地展示了我们构建的用户画像和偏好分布的真实性与复杂性。

![](https://mmbiz.qpic.cn/mmbiz_png/JhVy5CXYiaoiaayBKibzuJpfKfsUQGrjYbDHx0LQiaw9KWxkKIc2CFJUnpTOgHUiaJibhgMPUI4WZs8OHW1LrcUH1pqSP5EaZJVKtQyNuNIv0OMBI/640?wx_fmt=png&from=appmsg#imgIndex=5)

VitaBench 2.0 用户偏好统计图

具体来说，这个数据生态包含：

* **56个拟真用户**，每个用户都拥有基于真实世界统计数据构建的独特身份、习惯和需求。
* **819个可执行任务**，贯穿于用户的整个生命周期。
* 用户的偏好不是静态标签，而是会随着时间、事件而动态演变，平均每个用户的偏好会发生**超过48次**动态变化。

这些偏好被巧妙地嵌入到碎片化的互动历史中，包括对话记录和行为日志（如浏览、搜索、下单）。智能体必须像侦探一样，从这些混杂着“信号”与“噪音”的线索中，持续对用户进行理解。

![](https://mmbiz.qpic.cn/mmbiz_png/JhVy5CXYiaojPDtoycW7iaOzxaTjFicvENYxn3RBpePQpCZxwcY47Hq33K1iaCwibB1g1iaichT4rNEkFgIw1R7PkDLQUek1DxCYSWUe2zpeu93Xzk/640?wx_fmt=png&from=appmsg#imgIndex=6)

传统的Agent评测关注“单个任务是否完成”，而VitaBench 2.0的核心目标是评测“智能体是否在持续理解一个动态的人”。

为此，我们将评测的时间轴拉长到了前所未有的尺度，用户的平均交互周期长达**1580天（约4.3年），**最长甚至达到2974天。在这漫长的时间线里，智能体需要不断地**提取、利用、并更新**对用户的理解，才能在后续的任务中做出正确决策。这从根本上改变了评测的焦点，从单次任务的成功，转向了对用户偏好的考核。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/JhVy5CXYiaohUVKCPOibLyZI3q4Zb5JMgv19RicRuEn36tibrq7HvRouZ4icEwtRryjrzAnwRWcZBAWicrS9Z1M4t2DCc3iaCBwsxCyEplBBiby8XR0/640?wx_fmt=png&from=appmsg#imgIndex=7)

为了探究记忆在长期用户建模中的作用，VitaBench 2.0搭建了**首个真实用户场景下的统一长期智能体评测平台**，通过可扩展的接口，让两种代表性机制在此对决：

* **智能体记忆：AI自己决定记住什么、忘记什么，主动维护一个精炼的用户档案。**
* **RAG记忆：**像一个外部搜索引擎，根据当前任务检索最相关的历史片段。

通过对比这两种模式，我们可以清晰地看到不同记忆架构，以及同架构下的不同设计对个性化决策的真实影响，从而回答“AI应该如何记忆”这一关键问题。同时，为了考验AI的“眼力劲”，我们还设计了**主动性任务**。在这些任务中，AI必须意识到信息不足并主动提问，而不是盲目决策。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/JhVy5CXYiaogWqicXPYicreM8u9O0fnKwVWdpkHAcCxdkCpR5va03WtyDszvo7llb1OPwAcGIKtTTaEwMS0f3A4KAwRqKAkxScsr5EXm0AaUUA/640?wx_fmt=png&from=appmsg#imgIndex=8)

VitaBench 2.0不仅给出了总分，更用数据揭示了模型们犯错的具体原因。如下表所示，这是主要模型在不同记忆设置下的性能排行榜。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/JhVy5CXYiaohyVExOa1hySeAOGWnO6CicewefOQTQWfDljdyTCElnlz0CjWrmMKOUgVk2GR2Ejfq2OGia6ia53eVpepDYvkzcp94xwf2AfHJVW8/640?wx_fmt=png&from=appmsg#imgIndex=9)

主要模型在不同记忆设置下的性能表现

从排行榜可以看出，即使在能看到全部历史记录的“开卷”模式下，最强的模型Claude-Opus-4.6的平均分也刚过0.5，说明从海量信息中准确提炼偏好本身就比较困难。而一旦切换到更真实的记忆模式，模型的表现出现了不同程度的下滑。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/JhVy5CXYiaohgfLEelyAql7MgCbvz2EeJjkfVnRJ2dX0YgS42RHeNMTZxI0nGh6GQxKREU5S4coVOQwfxCh87icMOskOreVUcEVu2zN747dWg/640?wx_fmt=png&from=appmsg#imgIndex=10)

如下图所示，随着任务序列索引增加（即时间推移），所有模型的平均性能都在下降。这说明，无论是处理超长上下文的能力，还是记忆模块的累积误差，都严重限制了AI的长期服务能力。

**更关键的是，记忆并没有成为解药。** 对比实验结果发现，大部分模型在接入Agentic Memory或RAG Memory后，性能反而低于直接使用全历史记录的场景——**记忆不是装上就好**，如何正确更新、检索和利用，才是真正的挑战。

![](https://mmbiz.qpic.cn/mmbiz_png/JhVy5CXYiaohnK6m81rQyzRRiavmOSV4MeLRyo6YoF1xo6ylAq6c1E8Ig0Xd4l6WMCHW7WUkliaycF9NBEaIiaX17ibmGHkX2N2REK3vlfBV41HE/640?wx_fmt=png&from=appmsg#imgIndex=11)

模型性能随任务序列（时间）的衰减分析

![](https://mmbiz.qpic.cn/mmbiz_png/JhVy5CXYiaohrOiaodNe2sicPheJaG90qX8zOg6JkXRBxIuhhyFwP1W3GFPXxajDpyZ2ILP6yzWJVXBMsibdAe9qPxfCZaanicmfljjvmgnABlBY/640?wx_fmt=png&from=appmsg#imgIndex=12)

一个常见的假设是，开启模型的“思考模式”能提升其表现。然而，VitaBench 2.0 的实验结果给出了相反的答案：**开启思考模式，在个性化任务上并不总是有帮助。**

下图展示了模型在开启/关闭思考模式下的性能与效率关系。横轴是完成任务所需的交互轮数（越少越好），纵轴是平均性能（越高越好），理想的模型应位于左上角。可以看到，开启思考模式的点并没有稳定地比关闭模式更优越。

![](https://mmbiz.qpic.cn/mmbiz_png/JhVy5CXYiaojKhppzfT4g9CIpkJ9Bw6Ru3ibcwA37ZTektLpgm4cAM49CxInD8PXh1Y50As3BY5WzWFWnE1ic3BiaqhbZJa8hNo2VXKOSLfbsMc/640?wx_fmt=png&from=appmsg#imgIndex=13)

开启/关闭思考模式下的模型性能与效率

![](https://mmbiz.qpic.cn/mmbiz_png/JhVy5CXYiaoiaPUibRej76WysAzhvSwjOXewb9CQBYCicAKoibPSN0X0icialpXWclqrZwnFGvC7Nldmk2kS5jfTZUjtxF5S0ayibwLUxUMDZa3DM98/640?wx_fmt=png&from=appmsg#imgIndex=14)

模型普遍缺乏在信息不足时主动提问的“**眼力见**”。所有模型家族在需要主动提问的任务上，得分都出现了“断崖式”下跌。例如，Claude家族的平均分从46.0骤降至27.4。这表明，AI倾向于“想当然”，而不是在不确定时“多问一句”。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/JhVy5CXYiaojEU0bUBS0eAkLTYe3Udn1gQ54rJjbEkicIM57Gb9iaT5jUDadkC8fDqBAIOicOxgQLyquFiawf5wIYpMm8mibwyibCZ2cZ0hKorb1sw/640?wx_fmt=png&from=appmsg#imgIndex=15)

模型在主动性任务上的性能表现

![](https://mmbiz.qpic.cn/sz_mmbiz_png/JhVy5CXYiaoga8e5h4CVsq8H6rwMtoe0GF38RAX9jiaxBfzgGUE8fOZMI63G3dO5jHtmWVv6HlSx2qcib7jSn6VxIt99d4Uq83HHHVq33RD53Q/640?wx_fmt=png&from=appmsg#imgIndex=16)

为了分离“提取偏好”和“利用偏好”这两个难题，我们直接把真实用户偏好告诉模型。虽然性能有所提升，但仍有很大进度空间。**即便把真实偏好直接告诉模型，多数模型仍然失败。**这说明，即使拥有了准确的用户画像，在高压、多约束的决策中正确应用这些偏好，本身就是一个巨大的挑战。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/JhVy5CXYiaoiaG51uYgAiaNgQuGLJicOibMCTduxbs6JLBTYKoR9FzdiaWMlqEa2tUcianfcicaOwQxibQSZIOKAA7Gd1ePiac4k7HZaPFjkuHcPN83nE/640?wx_fmt=png&from=appmsg#imgIndex=17)

在提供真实偏好下的模型性能

![](https://mmbiz.qpic.cn/mmbiz_png/JhVy5CXYiaoiaLt8IMjyxoibUApwofiaEYyyag2ic3p2Hu4t61s7ialWRgteQicXu7osVABjnXQ0Pb1asyfMw9gC9GrdTTvEvHzaR6ib1jOBvHzXM4A/640?wx_fmt=png&from=appmsg#imgIndex=18)

我们对模型的失败原因进行了分类统计。在由**66个真实工具**构成的复杂生活服务场景中，早期模型更多地犯下工具使用错误（A类），例如选错API或填错参数。而更强的模型（如DeepSeek-V4-Pro）虽然工具用得更好了，但在偏好理解和应用（B类）上的失败却成了主要矛盾。这表明随着模型基础能力的提升，**个性化已是当前 Agent 的最大瓶颈。**

![](https://mmbiz.qpic.cn/mmbiz_png/JhVy5CXYiaojlGNVn3Oxkl111cuPONqic68tLPs9rhpmlw36KneqjQ3XUA5uicC6qgmHWgUicrAqZtZ9xhTsnewuia1SJYVnkHovAellLDibNzZjo/640?wx_fmt=png&from=appmsg#imgIndex=19)

模型失败模式分析（DeepSeek家族为例）

![](https://mmbiz.qpic.cn/sz_mmbiz_png/JhVy5CXYiaohiaVT1W4qpRewOc0AOFnC67m17uiaiaex08g7D1BID8ibXXdLWU0EIicLjmicA5NXeGFjwm7A1URZ89pAwwWfb0ORhJbfH9RonAClxY/640?wx_fmt=png&from=appmsg#imgIndex=20)

VitaBench 2.0清晰地揭示了，当前AI在成为“高情商助理”的路上，依然任重道远。

它的核心价值，在于推动了评测范式的演进：**从单点任务到长期陪伴，从被动执行到主动沟通，从黑盒到透明。** 这使得VitaBench 2.0成为一座连接技术与产品的“桥梁”，它用可量化的数据回答了“我的AI为什么不够好用”的问题，并为开发者指明了模型在“服务于人”这一终极目标上的具体短板。

我们希望，VitaBench 2.0能成为一个起点，激发更多研究关注智能体的个性化、记忆和主动性，共同推动AI从一个强大的“工具”进化为一个有温度的“伙伴”。

**VitaBench 2.0 已开源，欢迎各大模型前来接受“情商”大考。**

**🚀 开源链接**：****

* ****Paper:****

  <https://arxiv.org/abs/2605.27141>

* **HomePage:**

  <https://vitabench2.github.io/>
* ****GitHub:****

  **<https://github.com/meituan-longcat/vitabench-2.0>**
* **HuggingFace：**

  **<https://huggingface.co/datasets/meituan-longcat/VitaBench-2.0>**

![](https://mmecoa.qpic.cn/sz_mmecoa_gif/V95GN2mm0DyAv1GPbCKwzRn0FJLRg6hMwq7qEUtdWnOMxdHjoRVxgQB2EqUGHykTxwxq8JRtdPbQmWvkUSNsLxxDNbqqibcq6Tyibp3cTrDmU/640?wx_fmt=gif&from=appmsg)

![](https://mmecoa.qpic.cn/sz_mmecoa_png/V95GN2mm0DwViajPwVeb1YTd0gEctbhDToJficJotF8KF03eqrlZgcoDNpLic0OGQIAd5ibZsxzL4Y...