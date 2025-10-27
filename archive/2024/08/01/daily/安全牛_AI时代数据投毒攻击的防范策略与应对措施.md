---
title: AI时代数据投毒攻击的防范策略与应对措施
url: https://mp.weixin.qq.com/s?__biz=MjM5Njc3NjM4MA==&mid=2651131344&idx=2&sn=ce634156f596a259bd91e712065efa30&chksm=bd15bd038a62341588be591c2c5ff6c9baed5d319f92595017fbb90b869f1dd232d2230f2594&scene=58&subscene=0#rd
source: 安全牛
date: 2024-08-01
fetch_date: 2025-10-06T18:05:17.236576
---

# AI时代数据投毒攻击的防范策略与应对措施

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/kuIKKC9tNkB5t26cWuyoYoCCa7VrajGaHic53eeQQhOarDYqCGBUnaKOjC0FoFlXYh5ILGrqQPHQBicu2IfkvIzg/0?wx_fmt=jpeg)

# AI时代数据投毒攻击的防范策略与应对措施

安全牛

以下文章来源于ISACA
，作者Prithiv

![](http://wx.qlogo.cn/mmhead/Q3auHgzwzM5pbwgfbqEFG6KjnytNoyNTNkTibmib1F4VetdD7KtV0ong/0)

**ISACA**
.

享誉全球的专业技术组织ISACA，致力于推动全球技术领域的人才、专业知识和学习的持续进步，构建全球化专业社区，助力个人的职业进步和企业的数字化转型。其颁发的CISA等认证受到安全、治理、审计、鉴证、风险、数据和隐私等领域从业者的高度认可。

人工智能 (AI) 正在对人们生活的几乎各个方面产生深远的影响，包括提高生产力和效率。AI驱动的系统使用算法和模型来处理和合成数据、学习数据中的模式和依赖关系，并做出类似于人类推理的决策。伴随着AI带来的巨大机遇，也伴随着一系列风险和潜在的危害，这些都可能损害AI的可信度。一种值得注意的对抗性攻击技术是数据投毒，它涉及操纵AI训练数据集以引入可能使对手受益的偏见。

在AI的背景下，数据投毒不仅仅是一个学术抽象概念；它是一颗定时炸弹，可能在现实世界中产生深远的有害影响。想象一下，智能聊天机器人喷出仇恨言论，被攻陷的电子邮件垃圾邮件过滤器允许恶意流量通过，或者自动驾驶汽车因数据篡改而做出严重误判，会产生怎样的后果。这些不仅仅是假设的场景；而且是真实的。它们都是现实世界的例子：微软的 Twitter 聊天机器人 Tay 在协同攻击后变得具有攻击性，垃圾邮件发送者试图歪曲 Gmail 垃圾邮件分类器，以及一项关于自动驾驶系统的研究发现虚假交通标志可以欺骗AI。

![](https://mmbiz.qpic.cn/mmbiz_png/iclpC61N24PniaBG2ZiaTW5I3mib6znocU8wkLyKvmrAJfs3qvRGhkIanvxFI7VRlX7mUDMTLj47UxdkFcGibl5UJ7A/640?wx_fmt=png&from=appmsg&wxfrom=13&tp=wxpic)

图1说明了投毒攻击如何注入恶意训练数据并改变 AI 模型的结果。例如，在自动驾驶系统的场景中，攻击者可能会插入伪造的数据标签对，用限速标志代替停车标志。这会使用错误的决策边界来训练AI模型，导致车辆继续行驶通过十字路口而不是停下来。

随着AI系统的激增和更广泛的采用，阻止数据投毒攻击并确保反映人类价值观的决策变得更加重要。未能有效管理风险的企业可能会使自己处于竞争劣势。

数据投毒详解

![](https://mmbiz.qpic.cn/mmbiz_png/iclpC61N24PlJtQuDRgThic7mU0JbzowQE91Zk3ibI8S2pD62a2Pz3IN3wLvZBV6z6klnhXLLw1ksoELlVJqSkECw/640?wx_fmt=png&from=appmsg&tp=wxpic&wxfrom=5&wx_lazy=1&wx_co=1)

图2说明了典型数据投毒攻击场景中的攻击者行为和技术以及应对攻击的措施。

![](https://mmbiz.qpic.cn/mmbiz_png/iclpC61N24PniaBG2ZiaTW5I3mib6znocU8wn5gpQVBPmSwEof30n6icdWa2ibFEJEOYaludaPEVPA5Td9tJnLbtIaicA/640?wx_fmt=png&from=appmsg&tp=wxpic&wxfrom=5&wx_lazy=1&wx_co=1)

**攻击动机**

![](https://mmbiz.qpic.cn/mmbiz_png/iclpC61N24PlJtQuDRgThic7mU0JbzowQE91Zk3ibI8S2pD62a2Pz3IN3wLvZBV6z6klnhXLLw1ksoELlVJqSkECw/640?wx_fmt=png&from=appmsg&tp=wxpic&wxfrom=5&wx_lazy=1&wx_co=1)

AI投毒攻击是指对手故意破坏训练数据或操纵AI算法的行为。发起攻击的对手可能是内部人士，例如心怀不满的现任或前任员工，也可能是外部黑客，其动机可能包括造成声誉和品牌损害、篡改AI决策的可信度或减缓和破坏AI的进程。AI驱动的系统。在某些情况下，疏忽的用户可能会无意中注入影响AI模型行为的恶意数据（可能是从公共来源收集的），从而无意中使AI模型面临风险。

**攻击类型**

![](https://mmbiz.qpic.cn/mmbiz_png/iclpC61N24PlJtQuDRgThic7mU0JbzowQE91Zk3ibI8S2pD62a2Pz3IN3wLvZBV6z6klnhXLLw1ksoELlVJqSkECw/640?wx_fmt=png&from=appmsg&tp=wxpic&wxfrom=5&wx_lazy=1&wx_co=1)

AI的进步创造了新的业务领域，同时迅速改变了威胁格局。这种扩大的攻击面吸引了拥有复杂工具和攻击方法的对手。与数据投毒相关的主要攻击类型包括：

* **分割视图投毒****-**AI驱动的系统，特别是AI驱动的生成语言模型，利用通过大规模网络抓取收集的大量数据集。分割视图投毒利用了收集时间和训练 AI 模型时间之间数据快照的变化。控制获取训练图像数据的一系列域名的攻击者可以注入恶意内容，从而导致将来重新下载投毒数据。
* **标签投毒-**标签切换攻击的重点是更改数据点的标签，而不是数据点本身。该技术旨在通过分配不正确的标签和错误分类数据来误导机器学习模型，从而导致错误的模型结果和决策。例如，恶意行为者渗透训练数据集并操纵分配给非法电子邮件子集的标签，将其分类从网络钓鱼更改为合法。在这种秘密的标签操作之后，AI模型会接受重新训练，有可能将投毒的数据集吸收到其决策过程中。
* **模型反转攻击-**攻击者可以利用AI模型的响应，并使用反转模型对其进行逆向工程，以推断出有关AI所训练的数据主体的个人信息。例如，攻击者可以使用数据主体的医疗状况或生物标记作为输入来推断个人的个人详细信息。

![](https://mmbiz.qpic.cn/mmbiz_jpg/iclpC61N24PniaBG2ZiaTW5I3mib6znocU8wsbO3wyCZ4P7kSZdQnIGerQtEXGCmgTQgBjf3ybiaxhaS8uFgUHIRqHw/640?wx_fmt=jpeg&from=appmsg&tp=wxpic&wxfrom=5&wx_lazy=1&wx_co=1)

**攻击强度**

**![](https://mmbiz.qpic.cn/mmbiz_png/iclpC61N24PlJtQuDRgThic7mU0JbzowQE91Zk3ibI8S2pD62a2Pz3IN3wLvZBV6z6klnhXLLw1ksoELlVJqSkECw/640?wx_fmt=png&from=appmsg&tp=wxpic&wxfrom=5&wx_lazy=1&wx_co=1)**

攻击者了解AI系统使用的分类器可以加速攻击强度并绕过AI系统的安全防御。根据攻击者对目标AI系统的了解程度，数据投毒攻击可以分为白盒、灰盒和黑盒攻击类型：

* **白盒攻击-**在这些攻击中，攻击者了解AI驱动的系统，包括训练数据、学习算法和训练参数。有了这些信息，对手就可以发起有针对最坏情况的攻击并破坏机器的训练过程。
* **灰盒攻击-**在这些攻击中，攻击者对AI驱动的系统有部分了解，包括从类似分布中采样的代理训练数据、代理分类器训练的学习算法和参数，这使得攻击者能够发起更真实的攻击场景。
* **黑盒攻击-**在这些攻击中，攻击者对AI驱动的系统知之甚少，只能使用模型输出（例如概率或置信度得分）查询目标系统。

对策

![](https://mmbiz.qpic.cn/mmbiz_png/iclpC61N24PlJtQuDRgThic7mU0JbzowQE91Zk3ibI8S2pD62a2Pz3IN3wLvZBV6z6klnhXLLw1ksoELlVJqSkECw/640?wx_fmt=png&from=appmsg&tp=wxpic&wxfrom=5&wx_lazy=1&wx_co=1)

数据投毒攻击是动态的，需要持续监控来识别迫在眉睫和新出现的威胁，并针对这些威胁制定适当的防御措施。可以采用针对数据投毒攻击的对策来识别和删除导致模型性能恶化的恶意数据。由于隔离和检查大量、高速数据中的模式极其困难，因此建议采用概率或统计防御技术，包括：

* **异常值消除-**在进行数据投毒攻击时，攻击者试图污染或修改尽可能少的数据点，并最大限度地提高其对分类的影响。因此，可以合理地假设对手更改的点将是数据集中的异常值。通过消除异常值，可以从数据集中删除相当一部分被篡改的数据。或者，可以扩充现有数据集以减轻数据中毒。这种主动方法有意将受控变化引入训练数据集，例如随机旋转、平移和噪声添加。数据增强的优点是扩展数据集，同时保持其固有特征。此外，样本量的增加削弱了任何毒害数据集的尝试。
* **合成建模-**该过程涉及创建多个不同的模型，通过使用许多不同的建模算法或不同的训练数据集来预测结果。总的原则是，具有轻微差异的模型不太可能犯相同的错误，从而带来更好的整体性能和安全性。合成建模有几种常见的方法：

* **模型平均-**尽管AI模型能够学习变量之间极其复杂的关系，但它们会受到高度方差的影响。任何给定模型所做的分类都取决于训练期间分配的随机初始权重。即使在同一数据集上训练的相同模型中，这些变化也会导致不同的预测。为了减少方差水平，可以将在相同数据上训练的多个模型的预测相加；然后选择具有最高组合预测分数的类别，从而产生整体预测。
* **加权模型平均-**模型平均方法的一个局限性是它认为每个模型同样擅长解决问题。然而，在许多情况下，既有非常好的模式，也有不太成功的模式。为了使平均值反映这一点，可以为每个模型的投票引入权重。这些权重可以通过根据单独的训练集评估所有模型并根据其性能为其分配权重来得出。
* **模型堆叠-**该方法基于加权模型平均，通过使用高阶模型来概括集成建模。一组m个集成模型将产生 m个分类。在另一个数据集上训练的高阶模型尝试学习如何使用集成分类来预测正确的输出。使用经过训练的高阶模型提供了一种有效且准确的方法来组合多个分类并减少方差。

* **数据分区-**数据分区是将训练数据分成离散子集的过程，以训练和测试学习模型。目标是确保所有模型都不会使用相同的数据进行训练，从而最大限度地减少数据投毒的可能性。数据分区有两种类型：

* **K-折叠交叉验证-**该技术涉及将数据集划分为 k 个大小相等的子集或折叠。这k个不同的模型被训练，每个折叠作为验证集一次；剩余的 k-1 折叠用于训练。一旦所有模型都经过训练，就可以通过平均来组合它们的分类以产生累积预测。
* **随机分割****-**折叠交叉验证方法的一种变体是将数据集随机分割为训练数据和验证数据。与之前的方法类似，这通过改变训练数据并减少投毒数据点的影响，使模型更能抵抗数据投毒。当怀疑数据集的大部分连续部分被污染时，这种方法可能更可取。

* **De-Pois方法-**De-Pois 方法旨在防止各种类型的数据投毒攻击。它的运行方式是创建一个模仿原始模型行为的模型，并使用干净的数据进行训练。为了获得干净的数据，De-Pois 方法采用生成对抗网络 (GAN) 来生成与干净的训练数据非常相似的合成数据。这些合成数据有效地增加了训练集的大小，并有助于教导模拟模型原始模型应该如何表现。一旦模拟模型经过训练，就可以将其用作评估新数据的指标。如果模拟模型的预测与原始模型的预测显着不同，则表明存在潜在的数据投毒尝试，并阻止模型对篡改数据进行训练。

结论

![](https://mmbiz.qpic.cn/mmbiz_png/iclpC61N24PlJtQuDRgThic7mU0JbzowQE91Zk3ibI8S2pD62a2Pz3IN3wLvZBV6z6klnhXLLw1ksoELlVJqSkECw/640?wx_fmt=png&from=appmsg&tp=wxpic&wxfrom=5&wx_lazy=1&wx_co=1)

在当今数据量呈指数级增长、AI驱动的系统和无处不在的数字化时代，风险比以往任何时候都更加真实和重大。数据投毒清楚地提醒人们AI系统的固有漏洞。因此，在保护数据驱动系统方面保持警惕和创新的重要性怎么强调也不为过。

尽管组织面临着寻找感知和管理数据投毒风险的新途径的挑战，但成功的风险缓解策略首先要了解不断变化的威胁形势，了解AI驱动的系统的防御可能受到损害的方式，并应用异常值消除、合成等保护措施。建模、数据分区和 De-Pois 方法，以最大限度地减少攻击者造成的损害。

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/kuIKKC9tNkBZmyIrtuKu5NvaM1vicN8Y6b8TFgIImLsIf7G7sbQcuymdibuezvQtS7YgVtEibUWQlqXsxiaviagrB9A/0?wx_fmt=png)

安全牛

向上滑动看下一个

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/kuIKKC9tNkBZmyIrtuKu5NvaM1vicN8Y6b8TFgIImLsIf7G7sbQcuymdibuezvQtS7YgVtEibUWQlqXsxiaviagrB9A/0?wx_fmt=png)

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