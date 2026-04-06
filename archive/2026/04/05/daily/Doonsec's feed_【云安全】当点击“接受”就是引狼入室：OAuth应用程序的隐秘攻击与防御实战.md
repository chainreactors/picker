---
title: 【云安全】当点击“接受”就是引狼入室：OAuth应用程序的隐秘攻击与防御实战
url: https://mp.weixin.qq.com/s/djm5KQAYv4YRYdYukYhBVQ
source: Doonsec's feed
date: 2026-04-05
fetch_date: 2026-04-06T04:39:39.445842
---

# 【云安全】当点击“接受”就是引狼入室：OAuth应用程序的隐秘攻击与防御实战

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/tbTbtBE6TibeHibFjk8cae4EMWhUnu4LyicLTAGpEtL9DMbpKkC7uY5pEI9LLia2aEfh37nZO8WvcYYubzARxy09h1icdibp66jCpa08plh1S8ke8/0?wx_fmt=jpeg)

# 【云安全】当点击“接受”就是引狼入室：OAuth应用程序的隐秘攻击与防御实战

幻泉之洲

![]()

在小说阅读器中沉浸阅读

> 攻击者利用微软Entra ID中的OAuth应用进行权限提升和持久化已成常态。这类恶意应用混杂在海量合法集成中，很难肉眼分辨。我们分析了多起真实攻击活动，开发了自动化检测工具OAuth Apps Scout，已帮助数十家组织揪出潜伏的“内鬼”。本文将深度剖析攻击手法演变、检测逻辑，并提供一份可落地的防御清单。

你会给这个应用点“接受”吗？

![](https://mmbiz.qpic.cn/mmbiz_jpg/tbTbtBE6TibeFeOmdFvrSo3WyGoYucIhFicqcVElibCwlQzibz1RmrzHmqFc9GIDPo61m9UOtNmMNNc8Nicyhb9iaLjFjSkb0zq7ISfSxY5lMjTwk/640?wx_fmt=jpeg)

▲ 看起来是标准微软提示，但名字开头是零而不是字母O

在真实环境中发现这个通过同形异义字（Homoglyph）的攻击后，我们开始调查。事情远比想象中大。调查最终牵扯出超过20家公司，横跨三场不同的恶意OAuth应用攻击活动。它暴露了Azure服务主体管理中的一个普遍盲区。

## OAuth应用与“同意”到底是什么？

一个微软Entra应用始于一个应用对象，它驻留在应用最初注册的租户（即“主租户”）中。这个应用对象就像一个蓝图：每当该应用在其他租户中被使用时，Entra就会在那里创建一个对应的服务主体。

你可以把OAuth应用想象成你雇佣来家里干活的三方承包商。你不会给他们万能钥匙（你的密码），而是给他们一个特定的门禁卡（一组权限），这张卡只能让他们进入厨房和地下室。

在Azure世界里，“同意”就是这张门禁卡。当你看到一个请求访问你个人资料或文件的权限提示时，点击“接受”就是在告诉Azure：“我足够信任这个开发者，愿意授予他们这组特定权限。”

## 从全局应用到本地身份的转换

这里就变得对安全团队非常“有趣”了。你使用的大多数应用，比如微软Teams，实际上并不“生活”在你的环境里。它们托管在开发者（即微软）的Azure环境中。

但为了让Teams在你的公司里运转，你的Azure租户需要一种能在本地识别和管理它的方式。这就形成了一种双重关系：

* 应用对象：位于开发者主租户中的全局“蓝图”。
* 服务主体：你在本地针对这个应用的“实例”。

如下图所示，虽然Teams只有一个全局应用ID，但每个使用它的公司都有自己唯一的服务主体ID。

![](https://mmbiz.qpic.cn/mmbiz_jpg/tbTbtBE6TibdBWr7jHXgpXa2ah2ZlEx4ZX5LyXJLibcYIia0wvSdJHBeEpqz1XkcSpsr7hUJnvcaOO2Yj7dGXbtTSQK4mJV0CwXwqQ0oO10ung/640?wx_fmt=other&from=appmsg)

▲ 全局应用与本地服务主体的关系示意图

## Azure OAuth应用的真正风险

危险在于，我们都患上了“同意疲劳症”。弹窗一出现，想赶紧干活，大脑还没反应过来就点了“接受”。攻击者赌的就是这个。他们给恶意应用起个看起来合法的名字，然后坐等一个不了解情况或时间紧迫的用户为他们开门。

攻击流程通常是这样的：

1. **创建虚假应用**

   ：攻击者先在自己的Azure环境中创建一个应用。他们给它起个像“Adobe”这样看起来合法的名字。为了增强可信度，还会配置一个熟悉的图标和看起来正儿八经的主页URL。
2. **钓鱼骗取登录**

   ：攻击成功的关键是让一个人做出选择——登录这个应用。攻击者发出钓鱼邮件，谎称用户需要“更新Adobe设置”或“验证账户”。目的就是让用户点击链接，跳转到真正的微软登录页面。
3. **获取“同意”**

   ：用户登录后，会看到一个请求数据访问权限的提示。因为应用名和图标看起来很真，用户常常会点“接受”。这一下，用户就无意中把攻击者的应用“添加”进了他们公司的租户。如图所示，这会在受害者的租户内创建一个新的服务主体（本地实例），而攻击者仍然控制着全局应用。
4. **捕获访问权限**

   ：一旦点击“接受”，登录流程就完成了。但访问令牌没有去往正常的着陆页，而是发到了攻击者的重定向URL。有了这个令牌，攻击者无需知道密码就能访问用户的文件或邮件了。
5. **实现持久化**

   ：如前所述，通过授予同意，受害租户为攻击者控制的应用创建了一个服务主体。这个服务主体独立于用户的登录会话和凭据而持续存在，只要授予的权限有效，应用就能继续访问资源。和传统的凭据窃取不同，这种访问能扛过密码重置、多因素认证，甚至用户离职，除非OAuth授权或服务主体被明确删除。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/tbTbtBE6TibeC4muKfjsghuVwIyn0INH0gkPnBicymhIBh2TBafMk705iaIJwCRR5lb7CRkskvj2f0MRibfACDSe6CUHwFPJ4rjpBK3y8JKb84Q/640?wx_fmt=webp&from=appmsg)

## 一场艰难的“寻鬼”狩猎开始了

很明显，恶意OAuth应用构成了真实且持久的风险。部分原因是它们长得太像合法的SaaS集成，而且孤立评估很困难——扫一眼很难判断应用是好是坏。

为此，我们分析了多个真实的恶意OAuth应用，想搞清楚它们和正常应用的区别在哪，这些差别能不能用来系统性地揪出其他坏家伙。

一个典型案例是伪装成DocuSign集成的应用。单看这个应用似乎没问题，但放在更广的上下文里一比较，和真正的官方DocuSign应用相比就露出了好几处马脚：

* **应用名称**

  ：恶意应用的名字高度模仿知名SaaS服务，看起来很真。但它的发布者未经验证，跟它声称代表的品牌扯不上关系。
* **发布者验证**

  ：官方应用是经过发布者验证的，恶意应用没有。
* **主页**

  ：恶意应用没指定主页，官方应用配置的是官网。
* **无关或可疑的回复URL**

  ：恶意应用的重定向URI指向与声称服务无关的基础设施，在这个例子里还用了免费托管子域名。
* **奇怪的应用所有者名称和域名**

  ：所属租户和关联域名与号称的服务不匹配，进一步削弱了应用的合法性。
* **应用普及度**

  ：真正的DocuSign应用在很多组织里都能找到，而恶意应用只在少数几个环境里出现。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/tbTbtBE6TibcVgTJW24m1Nw00hg4LrZmCQAfT1LgXD3qPUP0rf3Vibe9zsgtIAhQz9LnTP8ibtcl56WIIty29P6L7voBB5SqdYaafJHYaIgU7k/640?wx_fmt=webp&from=appmsg)

## 从研究到工具：将OAuth应用检测落地

手动调查了几个恶意应用后，我们想把这些洞察变成一条自动化流水线，能主动检测未来的恶意活动。最终的结果是一个多阶段分析流水线，它能逐步丰富OAuth应用数据、降低噪音，既能检测新发现的可疑应用，也能跨环境进行线索关联以揪出攻击者的活动。

流水线包含四个主要阶段：

### 第一阶段：提取与建立基线

我们从汇集各环境观察到的OAuth应用开始，重点关注第三方集成。基于这些数据，我们建立了一个常见应用ID和名称的基线，并过滤掉那些在多个环境广泛出现的应用——这些更有可能是合法的SaaS服务。这个基线会在后续阶段重复使用，用来识别模仿或偏离已知集成的应用。剩下的应用，我们会提取出进行比较分析所需的关键特征。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/tbTbtBE6Tibcpibs1oHvCE2xazHicErjI4Xuz2rHwkdjf8SctMKIakejpkM66xiaCFcgvxSqA1DaRvBR2yicXc1Kx7KcE0yvyRrS0j2LY6rXHltQ/640?wx_fmt=webp&from=appmsg)

### 第二阶段：特征丰富化

为每个发现的应用元数据添加额外上下文，以便更好地评估其合法性和风险。这个丰富化过程整合了多个信号，包括：

* **应用名分析**

  ：将应用名与发现阶段确定的常见名称基线进行比对，以检测潜在的伪装或品牌冒用企图。
* **主页URL评估**

  ：检查主页URL是否为空、占位或可疑页面，并交叉比对DNS信息以评估域名的合法性。
* **回复URL分析**

  ：分析重定向URI，提取域名所有权和DNS特征，帮助识别与声称服务无关的基础设施。
* **所有权与发布者上下文**

  ：丰富发布者名称、租户ID和关联域名信息，以深入了解运营该应用的主体。
* **采用度与权限使用情况**

  ：纳入租户分布情况和应用请求的权限，以了解应用在实践中的使用方式，并突出异常或高风险行为。

![](https://mmbiz.qpic.cn/mmbiz_jpg/tbTbtBE6TibdhDmaXMKsjDCyGeznjIcFNrqExr1uY1sfe1spPibjzgCglT0yRUuJVxlg63ibE7Ko79bMdUnJiakPlZwDXYJXpXt5350Wq8fuhMs/640?wx_fmt=webp&from=appmsg)

### 第三阶段：决策与优先级排序

为了给待调查的OAuth应用排序，我们对丰富后的信号应用加权评分机制。模型不依赖单一指标，而是结合多个微弱信号——比如异常的权限使用、低的租户普及度、与已知集成的名称相似度、可疑的回复或主页URL——为每个应用分配风险分数。这种评分方法有助于凸显值得深入检查的应用，同时降低那些可能只表现出一个孤立异常特征的良性集成带来的噪音。

### 第四阶段：AI辅助的上下文评估

分析中我们发现，OAuth应用评估的某些方面天生具有上下文依赖性。比如回复URL是否与声称的服务匹配，或者域名是否与给定的应用名相符，这些指标单靠严格规则很难评估。为了解决这个问题，我们加入了AI辅助评估步骤，它会整体考量应用的元数据。这一步通过推理信号之间的关系（而非孤立地评估每个信号），来帮助判断应用的整体可信度。

### 第五阶段：线索关联与攻击活动发现

最后，流水线能够通过共享的指标（如回复URL、所有权域名、应用元数据、命名习惯）进行跨环境关联。通过在不同环境中关联这些信号，我们能够对相关的OAuth应用进行聚类，并识别出在多个组织中运作的、有组织的攻击活动。这能将焦点从孤立检测转移到攻击活动层面的可见性，从而更深入地了解攻击者在实际环境中如何重复使用和调整OAuth应用。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/tbTbtBE6Tibe3T6svBejc0nf1ibibWsrXmAadgjJh9ULGzr1Riaa17YxCiaOqMIicibp4qg4mSBl7VI8gQ2I4Gth5y1nSgqS9gkOTzKLN5f2zMG9f8/640?wx_fmt=webp&from=appmsg)

## 在实战中识别恶意OAuth模式

举个我们检测到的真实恶意OAuth活动的具体例子：我们的检测流水线发现了一场在2025年初活跃的大规模攻击活动。该活动涉及19个不同的OAuth应用，冒用了Adobe、DocuSign、OneDrive等知名品牌，并针对了多个组织。Proofpoint研究团队也独立报告了同一活动[1]。在这些应用中，我们观察到了明显的协调迹象，包括基础设施复用——最明显的是共享的回复URL和占位符或空白的主页。

攻击流程依赖诱使用户向虚假文档共享应用授予OAuth同意，从而使攻击者能够在不触发MFA或异常登录警报的情况下获得长期访问权限。一旦同意被授予，攻击者便能读取用户邮件和文件，通过委托权限维持访问，并在不产生可疑认证活动的情况下窃取数据。文末提供了与此活动相关的入侵指标(IOCs)列表。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/tbTbtBE6Tibebgbvn3ayL9EfG94pfaS9ZzkFXRRbpMXfJQyYoFvwaxLp7Un4VicXic1elQIYJyvxNjSEP3OJicR3aJU3wHkS8s0Bcb15GmayTtQ/640?wx_fmt=jpeg&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_jpg/tbTbtBE6TibepsxWaNLict9PMLopjNBggKm9FlGycqriaJoUAwcVWNDtQkmricfyJ2BdVgpDtpuOD7N6OsVtxJEwc82hxL0DCibickUbs9zicP9vD4/640?wx_fmt=webp&from=appmsg)

## 攻击者潜行术的进化：2019 vs. 2025

我们的模型能从去年的数据中找出问题，但我们想看看这个趋势能追溯到多早。考虑到OAuth应用被滥用的历史很长，我们用更早几年的数据评估了模型。

这让我们发现了可追溯到2019年的另外7个恶意应用。这些应用使用了西里尔字母同形异义字，用视觉相同的非拉丁字母替换拉丁字母，来模仿合法的微软服务。

**2019年常见的被仿冒应用：**

* ОпeDrive for Business （使用西里尔字母“п”）
* Sharеpoiпt Cloud （使用西里尔字母“п”）
* Мicгoѕоft. Сloud App Ѕесuгity （使用西里尔字母“г”）

这些同形异义字应用在超过50个组织中被发现，突显了传统检测方法存在长期盲区。

### 2025年：策略转变

将这些老式攻击活动与我们2025年的最新发现进行对比，攻击者手法的进化一目了然。攻击者已不再冒充微软本身，而是开始利用像Adobe和DocuSign这类第三方生产力工具的信任。

现代攻击者的隐匿性高得多。他们摒弃了“明显的”域名仿冒，转而使用复杂的URL结构和看起来合法的SaaS平台来托管他们的重定向点。

| 特征 | 2019（同形异义字） | 2019（明显仿冒） | 2025（现代） |
| --- | --- | --- | --- |
| 应用名 | ShaгеPoint Cloud | 0365 Access | DocuSign |
| 目标品牌 | 微软 | 微软 | 第三方（DocuSign/Adobe） |
| 回复URL | sharepoint.microzoftonline.com | officemtr.com:8081/office | ynapaletsteamworkspace.myclickfunnels.com/ |
| 隐匿级别 | 中等（视觉层面） | 低级 | 高级（上下文层面） |

## 给防御者的干货建议

检测恶意OAuth应用是可以做到的，它理应是现代身份安全的关键支柱。从2019年的“克隆微软”到2025年的“冒牌SaaS”，攻击者在进化，但他们并非无迹可寻。他们依然在OAuth协议的框架内运作，这就必然留下可检测的痕迹。

### 攻击者留下的“面包屑”

即使最高明的攻击者，也会在这四个方面留下可识别的标记：

* **应用元数据**

  ：检测网络钓鱼的传统策略同样适用于OAuth应用；留意那些暗示紧迫性或模仿可信工具的名称。
* **回复URL**

  ：仔细分析重定向URI。攻击者经常把着陆页藏在像ClickFunnels或GitHub Pages这样的可信SaaS平台上，以绕过安全过滤。由于这些平台被许多合法企业使用，安全工具很难在不造成重大破坏的情况下直接屏蔽它们。这是个常见手法，之前已被其他安全公司记录过，包括CheckPoint、Infosecurity[2]和 iZOOlogic[3]。
* **请求的权限范围**

  ：像Mail.Read或Files.ReadWrite.All这样的高风险权限，一旦由外部、未经验证的发布者请求，就应该总是触发警报。
* **基础设施**

  ：每个恶意应用都关联着一个源租户和一个已验证（或未验证）的域名。了解租户的详细信息和关联域名的声誉至关重要。

### 可操作的防御策略

我们认为本文讨论的检测模型，任何有能力的蓝队现在都可以实施。为了加强你的安全态势，我们建议采取多层次的方法：

1. **限制用户同意**

   ：限制非管理用户向未经验证发布者的应用授予同意的能力。
2. **盘点与审计**

   ：定期导出并审查你环境中所有OAuth授权的列表。查找那些仅由1或2个用户同意的应用，这些“低普及度”应用往往是针对性钓鱼的结果。
3. **监控“首次出现”的应用**

   ：对你租户中首次出现的任何应用发出警报，特别是当回复URL与已知的企业服务不匹配时。
4. **为回复URL建立基线**

   ：使用正则表达式或威胁情报源来扫描回复URL中的可疑字符串或已知的恶意托管模式。

攻击者赌的就是你对熟悉名字的信任。而这个模型把力量交还给了防御者，证明只要你找对地方，再隐秘的应用也会留下痕迹。

## 入侵指标（IOC）

| Name | AppId | OwnerTenantId | OwnerTenantDomains | Last Seen |
| --- | --- | --- | --- | --- |
| Adobe | c4d0b015-689a-4bcf-b69b-3ed5005fddb6 | 9c036328-3aba-4d35-aceb-6456f9420b31 | thermion.se; thermionse.mail.onmicrosoft.com; thermionse.onmicrosoft.com | 2025 |
| PDF | a69a0f78-a77c-451c-b090-b766425caee2 | 31aca3e6-069d-4baa-89b7-6502006fe99e | lnsrc.org; lnsrclub.onmicrosoft.com | 2025 |
| Adobe | 58427324-4e5d-4441-b029-cd2d532b47d7 | 619849e9-5192-4c3f-b0f3-8469980c3958 | nceconomicresourcecou...