---
title: BluePhishing：一次同意，在别人租户里种下 AI Agent
url: https://mp.weixin.qq.com/s/zKA5seF-cnkYdPbwlkdz2Q
source: Doonsec's feed
date: 2026-11-12
fetch_date: 2026-11-13T09:03:46.346968
---

# BluePhishing：一次同意，在别人租户里种下 AI Agent

# BluePhishing：一次同意，在别人租户里种下 AI Agent

幻泉之洲

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

> 微软把 Entra 的身份体系延伸到了 AI Agent，做法和传统应用注册几乎一模一样。Proofpoint 盯上了这种相似性：诱导受害者同意一个恶意 Agent 蓝图，攻击者就能在对方租户里创建 Agent 身份、换令牌、按继承来的权限干活。这套手法被命名为 BluePhishing，本质是 OAuth 同意钓鱼的下一站。

2026 年 11 月 9 日 · Rachel Rabin

## 先把结论摆出来

* Microsoft Entra Agent Identity 把 Agent 纳入了 Entra，模型照搬传统应用，滥用空间也跟着照搬。
* Proofpoint 研究人员提出的 BluePhishing，是 OAuth 同意滥用的演进版，攻击者用 Agent 身份完成初始访问。
* 攻击者可以在蓝图里配好可继承权限和 requiredResourceAccess（RRA，所需资源访问），再用同意链接进入受害者租户。
* 受害者同意恶意蓝图后，攻击者能建立 Agent 身份，用租户 ID、用户或赞助者对象 ID 这类可发现的标识，在授权范围内操作。
* Agent 身份和同意流程的治理难度，让规模化、自动化的后渗透变得更省事。
* 这是研究性质的概念验证。Proofpoint 目前没有发现野外活动，新技术要随着平台和政策变化持续跟踪。

## Agent 身份为什么是个新入口

组织上 AI Agent 的速度，比身份治理跟上的速度要快。Entra 的 Agent 身份模型给了一套现成的能力，也顺手打开了一片没怎么画过地图的攻击面。

BluePhishing 的思路不复杂：社会工程受害者，让他对一个恶意 Agent 蓝图点下同意，攻击者就拿到了进入租户的落脚点。传统应用同意钓鱼里，攻击者用客户端凭据换取租户内的初始访问；BluePhishing 把同一套动作搬到了 Agent 生态里。利用的是可见性和治理的空白——很多人还没搞清楚 Agent 蓝图和 Agent 身份分别是什么，同意链接已经点完了。

一次同意，换来的不只是某个应用的权限，而是一个能在目标租户里持续造身份的主体。这个差别，后面会展开。

## 蓝图、主体、身份：三个容易混淆的物件

Microsoft Entra Agent ID 是一套身份与安全框架，把 Entra 扩展到 AI Agent，和现有的应用模型共享不少结构。理解攻击，先得把三个概念拆开。

**Agent 蓝图（agent blueprint）**相当于应用注册（app registration），定义 Agent 的模板，包括配置和凭据。**蓝图主体（blueprint principal）**相当于服务主体（service principal），是蓝图在某个租户里的代表。**Agent 身份（agent identity）**则是从蓝图创建出来的具体实例。

一个蓝图最多可以关联 250 个 Agent 身份[1]。这个数字不是安全阈值，更像是批量操作的配额。设计意图是让多个 Agent 身份带着委派权限，绑定到具体用户上下文，而不是覆盖整个租户。权限颗粒度变细是好事，问题出在创建权和继承机制的组合上。

![](https://mmbiz.qpic.cn/mmbiz_png/tbTbtBE6Tibc9QsbSmgkGlwmIFy7Im7NQRqXOJA5NQU7NazicNDxqEbsMu0dV139BkVibpXOERDic9WcibKZuGKfJLjgcs5u2ngouA2znVwiaWib8Q/640?wx_fmt=png&from=appmsg)

图 1：Agent 蓝图、蓝图主体与 Agent 身份之间的关系，可用 agent-permission-checker.pages.dev 查看

## 2026 年 11 月的默认开关

Microsoft 365 消息中心公告 MC1506733[2]写得很清楚：从 2026 年 11 月起，默认的 Microsoft Entra 用户就能创建 Agent 蓝图。这个默认值一开，暴露面从管理员群体扩散到普通用户。

很多企业的同意流程只盯管理员审批，普通用户创建 Agent 的通道不在审查范围内。攻击者要的就是这种盲区：不需要攻破管理员账号，只需要一个会点链接的人。

## BluePhishing 具体怎么打

攻击链的起点是钓鱼。攻击者把恶意 Agent 蓝图的同意链接发给受害者，诱导对方授权。这个蓝图托管在攻击者自己的租户里，运作方式类似多租户应用，可以往里添加客户端凭据。

受害者一点同意，蓝图主体就在受害者租户里建起来了。接下来这一步很刺眼：蓝图主体会自动被授予 **AgentIdentity.CreateAsManager** 应用权限。按照微软文档[3]，这个权限无法从主体上撤销。有了它，攻击者能拿到受害者租户里的 app-only Graph 令牌，在租户内创建 Agent 身份。新建的 Agent 身份会继承蓝图里配置的权限。

然后攻击者用自己准备的客户端凭据，为这些 Agent 身份换取令牌。访问是持久的，后续利用也有了落脚点。

![](https://mmbiz.qpic.cn/mmbiz_png/tbTbtBE6TibemphMZvr9nA2bgHOyCic64iaHzrTgYm0CFnSn2P5kEsh9aJiczO74tTHjcDYz4p7QQGVSWviaXbludIfGicFnejlv3oicHeNLcdoooM/640?wx_fmt=png&from=appmsg)

图 2：BluePhishing 攻击路径示意

把这条链和传统 OAuth 同意钓鱼放在一起看，差别就出来了。老剧本是“骗一次授权，用一个应用”，攻击者拿到的是某组 API 权限；BluePhishing 是“骗一次授权，拿到一台造身份的机器”，攻击者可以在目标租户里反复派生身份。CreateAsManager 不可撤销这一点，让事故响应从“撤销同意”变成“删主体或者断创建渠道”，动作更重，影响面也更大。说实话，这个权限设计在应急场景里有点激进。

## 攻击者需要准备什么

门槛比想象中低。攻击者要提供的东西，都在自己租户里生成：

* 蓝图的应用程序 ID（application ID）
* 客户端密钥（client secret）

还需要知道受害者的租户 ID（tenant ID）。租户 ID 从来不算秘密，登录页、邮件头、SharePoint 链接里都可能出现，收集起来不费劲。客户端密钥由攻击者自己创建，蓝图应用程序 ID 也是自己控制。真正需要“获取”的只有一项，而这一项通常公开可见。

这也是 BluePhishing 值得盯的原因：它不依赖漏洞利用，也不依赖高权限账号，靠的是一个默认开放的创建通道、一个不可撤销的权限，以及一次成功的点击。

接下来出场的是 Sponsor（赞助者）：受害者租户里的一个用户，职责只有一个——把代理身份建出来。门槛就这么高。而支撑这个门槛成立的，是一组更让人无语的事实。

蓝图要用到的那些值——租户 ID、应用 ID、客户端密钥——微软都不把它们归入敏感信息。这话站得住脚，因为泄露它们的路全是产品自己铺的。GetCredentialType 端点能在未认证状态下枚举用户，这是登录流程绕不开的功能；往 https://login.microsoftonline.com/{tenant\_name}/.well-known/openid-configuration 发一个请求，租户 ID 就原样吐回来。侦察阶段基本不产生摩擦。

### 配置蓝图：Sign-in audience 是那个真正的开关

攻击者在自己的租户（Tenant A）里配一个代理蓝图。要动的地方有四项：登录受众（Sign-in audience）、客户端密钥、应用与委托权限、必需资源访问（RRA，requiredResourceAccess）加可继承权限（inheritable permissions）。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/tbTbtBE6TibcrtibYLQEcwJ0iaBZHK3ficW2kEI0YwhmkicS4GwLaicuVqVSrcyoHKbxqcGM2VKj6lJHgQMB4yUGNMx8zBIYaSsFsO4KeanhVDyb0/640?wx_fmt=png&from=appmsg)

▲ 图 3：在攻击者控制的租户里配置好的代理蓝图

四项里真正设门槛的只有 Sign-in audience。它必须设成 AzureADMultipleOrgs，蓝图才能被别的租户同意，变成所谓的「第三方蓝图」。问题在于，Entra 管理门户压根不提供这个选项。要改，得走 Microsoft Graph、PowerShell，或者直接编辑蓝图清单。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/tbTbtBE6TibemMJWOCneVLZXCgc9udZDntdtyAFt4Elkhd9iakUREDkQHiaQ2UxK1KYOkS8icUBwy1tVJFtxaOV0JdK5MhXMd2AUh4OfTqMhw68/640?wx_fmt=png&from=appmsg)

▲ 图 4：通过 PowerShell 把登录受众设为「多个 Entra ID 租户」，门户里无法修改

这个取舍值得掰一掰。门户不暴露，等于挡住了普通管理员顺手把蓝图配成多租户。可攻击者本来就不走门户。限制只对守规矩的人生效，这是安全设计里反复出现的老问题——把合法用户的路径收窄，对恶意用户几乎零成本。

### 委托权限和应用权限，攻击者要的是后者

代理蓝图上能挂两类权限。委托权限（delegated permissions，令牌里体现为 scp 声明）是代某个已登录用户行事，通过代表用户（OBO，on-behalf-of）的 OAuth 流程换令牌，详见微软的代理 OBO 流程文档[4]。它能干什么，取决于那个用户本身能干什么。应用权限（application permissions，体现为 roles 声明）不带用户上下文，是纯应用身份，走自主应用 OAuth 流程[5]。

两条路的价值差得很远。应用权限一旦到手，整个租户都在射程内，一次同意就够。委托权限的收益上限被被钓鱼账号的权限死死卡住。攻击者的首选因此毫不含糊：想办法拿到管理员同意。

### RRA 与可继承权限：把一堆权限捆成一次点击

RRA 是把权限集合提前写死在蓝图上；可继承权限保证从这个蓝图派生出来的所有代理身份自动带上这些权限。微软这两件事放在同一份概念文档里讲[6]，本身就说明它们是绑在一起的。

设计初衷是简化部署：管理员配一次，后续派生的 agent 全部继承，不用逐个授权。

到了攻击者手里，这就成了一条捷径。把一堆高权限塞进 RRA，配好可继承，产出一个一次性同意链接。用户点一次，之后派生出来的每一个代理身份都揣着这些权限，不需要再问任何人。

![](https://mmbiz.qpic.cn/mmbiz_png/tbTbtBE6Tibdl4dzUzmXdNu2pzl3O7X7vac6oMFjlxnNph1WOJBHM2EdYP8lQCtGFlyvrCmn9QUlJ8bZymppd8BxunIgLJB0m1icG4u4OWGsY/640?wx_fmt=png&from=appmsg)

▲ 图 5：代理蓝图同意页第一步，显示发布状态

### 权限层的可见性缺口

按微软文档的说法，继承来的权限在 Entra 门户里看不到，用 Microsoft Graph 也查不到，只有运行时抓到的令牌内容里才有。

这一条对防守方是硬伤。事后审计 agent 身份，前提是看得见它拿了什么权限，才谈得上审。看不见，等于没有审计入口。

我的判断是：权限给多了不算最糟，权限不可见才最糟。授权过大，审计还有机会发现一次异常授权；权限不可见，连发现的机会都没有。攻击者要的是时间，防守方要的是线索，这个缺口刚好把线索掐断在源头。

### 同意链接是怎么拼出来的

代理的同意体验和 OAuth 应用很像，区别是 client\_id 的位置换成代理专属的标识符。管理员同意链接大致长这样：

https://login.microsoftonline.com/{tenant}/v2.0/adminconsent?client\_id={blueprint\_id}&scope=https://graph.microsoft.com/.default&redirect\_uri={redirect\_uri}

scope 里的 .default 表示授予蓝图 requiredResourceAccess 中预配置的全部权限。也就是说，链接里不需要逐个列 scope，一个 .default 就把整包权限端上桌了。

Web 重定向 URI 可以在对应的客户端应用上配，但同意链接要求 response\_type=none，交互式获取令牌的路径被堵死[7]。这一点反而降低了攻击者的操作复杂度：他不需要真把令牌接回去，只要用户在同意页面上点那一下。重定向去哪不重要，重要的是 Tenant A 里的蓝图已经把权限配齐了。

用户点同意之前，页面上会显示名称、发布者信息、是否由微软构建。这几项是用户唯一能拿来判断的依据。现实情况是，大部分人既不清楚「是否由微软构建」这一栏该看什么，也不会去核对发布者是谁。攻击者把发布者名字起得像模像样，这一关就过了。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/tbTbtBE6Tibf53fXlsNSDQFND8rOuZ6X6zPdVWurW0J85iaKPohEJSMTKFvicqgXxBNFt16DdRib9zvbZgL7Qsz7lDhQiaHXEEU3sWysqpoE2FlY/640?wx_fmt=jpeg&from=appmsg)

▲ 图 6：同意对话框第二步，提示权限会继承给派生代理

### 管理员同意与用户同意，两条难度不同的路

同意分两种。

应用权限必须管理员同意。这条路对攻击者最划算：一条链接，整个租户的权限一次性到手。代价是被钓鱼的那个用户本身得有授予管理员同意的权限。

用户同意只能授予委托权限，在那个用户自己的上下文里生效。碰上用户同意策略，用户没资格批，请求可以转给管理员审批。

转审批这个机制，本意是安全阀。可它的存在给了攻击者第二次机会：如果能编出一套说得过去的业务理由，管理员有可能批。成功率低得多，取决于管理员的判断力，属于弱路径。强路径还是直接钓一个有同意权限的账号，这也是为什么前面侦察阶段收集租户 ID、枚举用户这些动作看着不起眼，实际上是整条链路的前置条件。

还有一个容易被忽略的对比。传统 OAuth 应用同意钓鱼已经被玩了很多年，微软陆续加了发布者验证、用户同意策略这些拦截。代理身份的同意界面是新的，用户没见过，审计工具也未必覆盖。攻击者挑新东西下手，从来不是偶然。

用户同意这条路覆盖面更广——普通员工、低权限账号都可能点下去。但它有天花板：委派权限（delegated permissions，即"以某个用户身份行事"的权限）没法通过自主流兑换成令牌。想拿到能离线使用的令牌，还得再走一次用户同意，比如 OBO（On-Behalf-Of，服务代表用户向下一跳资源申请令牌的流程），中间又卡了一道人工确认。

这意味着攻击者从用户同意链接里拿到的，是一份"权限大礼包"却缺了提货单。测试里有个细节值得记下来：权限从蓝图主体静默继承到代理身份，只在用户同意链接授予的委派权限上出现；通过管理员同意链接授予的权限，grant source 显示的是"inherited from parent"（继承自父级）。两种链接换来的权限形态不一样，继承行为也不一样。

这个差异影响攻击者的路径选择。管理员同意一次给出的是更高的应用权限，但不会静默下沉；用户同意给的是委派权限，却会跟着代理身份一起走。实战里挑哪条链，取决于目标租户的同意策略配置。

## 创建蓝图主体

受害者点下同意链接的那一刻，受害者的租户里就被写入了一个蓝图主体（blueprint principal）。攻击者不需要任何后续交互。

![](https://mmbiz.qpic.cn/mmbiz_png/tbTbtBE6TibcESl7Ut8Cmoo7SibbSVDibVrJExDLJRHjQwfQRyGEtBW24MfODb5E0Vwwx4iaWx84lR3aLQAWNicMTybLNccHCPguM9NupBBJzicVo/640?wx_fmt=png&from=appmsg)

▲ 图 7：受害者租户中的蓝图主体，带管理员同意权限

默认情况下，蓝图主体自带一条隐式管理员同意权限 **AgentIdentity.CreateAsManager**，用途是让蓝图能创建与自身关联的代理身份。这条权限不需要任何人批准，是产品设计上为了让蓝图"能用"而预置的。

说实话，这一条是整个攻击链里最值得盯的地方。它不是配置疏漏，是默认行为。任何能被写入蓝图主体的租户，都默认附带了一个创建子身份的入口。

![](https://mmbiz.qpic.cn/mmbiz_png/tbTbtBE6TibclBLr5OCDdrFpAH2zOqd1kYPwNmeFsAulx7f7aaz77PCDKAic2uPmpoY1l33GsmhLXRugb4oPfSvgibwtu1HsCvrI4liaibmKib6JI/640?wx_fmt=png&from=appmsg)

▲ 图 8：AgentIdentity.CreateAsManager 隐式权限

## 创建代理身份

攻击者手里有受害者租户里的蓝图主体，加上自家租户里的蓝图凭据，就能在受害者租户里生出一堆代理身份。整个动作分两步。

### 第一步：以蓝图身份认证到受害者租户

攻击者向受害者租户的令牌端点发起客户端凭据（client credentials）请求：

POST https://login.microsoftonline.com/{tenant\_victim\_id}/oauth2/v2.0/token
Content-Type: application/x-www-form-urlencoded

client\_id={blueprint\_id}
&client\_secret={blueprint\_secret}
&scope=https://graph.microsoft.com/.default
&grant\_type=client\_credentials

返回的访问令牌里 roles 包含 AgentIdentity.Cre...