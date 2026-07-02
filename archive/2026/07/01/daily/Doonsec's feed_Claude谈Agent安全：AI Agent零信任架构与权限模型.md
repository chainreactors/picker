---
title: Claude谈Agent安全：AI Agent零信任架构与权限模型
url: https://mp.weixin.qq.com/s/wJSCFQkL67mT7W76GOmGtw
source: Doonsec's feed
date: 2026-07-01
fetch_date: 2026-07-02T05:52:33.568786
---

# Claude谈Agent安全：AI Agent零信任架构与权限模型

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/YuBibjKRq0Lf3I1EFA3kw3YAOHYQ4HNk4icXeIt8iazxj49tXdyaJYcPg0B5crqEhf0FGYQicmicQBaiawIux8ybl0lGV3SxXf9HPzPrQT6Z0EJAA/0?wx_fmt=jpeg)

# Claude谈Agent安全：AI Agent零信任架构与权限模型

原创

高渐离
高渐离

落水轩

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

这篇文章核心内容均来自于claude的官方博客。

对于Agent安全，Anthropic认为有上中下三策。即高级要求，企业级要求和基础要求。

其中高级要求就是给包括金融机构，国家重要部门等地方提出的安全建设需求。

企业级要求是给大部分企业提出的安全建设需求。你通过这个方式，能够满足绝大部分对抗场景。基础要求就是最低要求。（但是我看了下，它里面提的有些项目下的最低要求，其实挺难的。而有些项目下的最高要求，感觉国内大部分公司都有。）

安全风险

Agent是根据用户的提问，调用工具，完成对应的工作。在claude里面，我们能看到，有记忆，上下文，工具定义等。

由此可知，Agent存在以下安全问题：

首先用户输入部分可能存在安全问题。包括prompt注入等。

其次调用工具部分，很容易形成工具的误用。

再次就是权限部分，Agent的权限问题

之后关于Agent本身的记忆和上下文可能被污染。

最后一个问题就是供应链安全问题。Agent本身使用的大模型和三方库。使用的工具的三方库等

## Agent零信任

这个部分核心是围绕着Agent的身份，认证，授权，访问控制。

然后是可观测，可审计。

最后是可恢复。

还花了一点篇幅，讲了下输入输出的校验检测。

### 身份和认证

*Agent的身份这里有个很有意思的点，Agent应该为每个实例颁布一个身份。也就是说，假如企业里面有个Log Analysis的Agent。这个Log Analysis的Agent，每次被用户唤起，都应该创建一个唯一的身份id。而不是统一叫Log Analysis。*

*然后这个唯一id，应该是加密串，从这个串里可以解出很多这个Agent的自身信息。从而避免id伪造。*

Anthropic认为，这个是个基础要求。这个点，我感觉绝大部分企业都没做到。

企业级要求呢，则是要为Agent提供一个证书，并且定期轮换。

高级要求则是把证书写在HSM或者TPM里面。

上面讲的是Agent本身的身份。

当Agent调用外部服务，需要认证时，应该使用短期的token校验，类似于jwt token。这个是基础要求。

企业级的要求，则是开启双向tls，避免中间人攻击。

而高级需求则是要求认证信息来自于可信硬件环境。

### 权限和访问控制

权限和访问控制部分，要求跟人差不多。

*基础要求是给最小权限。企业级要求是基于访问时的时间，位置，数据敏感程度和风险分数动态核验。高级要求是根据情报等对每一步操作进行访问控制。而不仅仅是在session开始时做一次。*

这部分做过风控的很容易理解。

有的系统没风控，只是给人设置一个最小权限。他完成认证就能做他权限范围内的事。有的系统只做了登录风控，发现他登录很异常，就加强权限管控。还有的系统是持续风控，在系统里的每一步操作都进行核验。

它举例说，一个写邮件的Agent，不应该具备财务部门的文件分享权限。设置Agent不允许在非工作时间调用某些操作。或者Agent如果通不过某个挑战，则认为有问题。

*我个人感觉这里的难点是管控措施。对于Agent的管控措施是啥呢？不允许它做这一步？还是它做的时候要进一步验证信息？验证哪些信息呢？可能把全部操作信息，提交审批，是一种管控方式。问题是如何判定操作合法性。*

关于权限的范围，基础要求是要有静态的权限列表，企业级要求则是根据任务动态申请权限。高级要求则是在任务完成时自动收回权限。

另一个访问控制的核心点，就是具备对资源访问的限制能力。这里的资源访问指的是包括网络，文件等资源。基础要求是使用网络策略，限制Agent中不必要的东西向流量。例如仅允许部分域名访问。企业级要求是使用沙箱，例如gVisor。高级要求是使用硬件级别的隔离沙箱。

### 观测 审计

观测部分基础要求是记录工具调用，数据访问，外部通讯，行为细节和上下文。（我感觉这个对很多公司而言，已经是高级要求了）。企业级要求则是日志文件只可追加，避免篡改，多备份。高级要求是收集该日志到日志中心，用来挖掘异常访问。

其实这个部分，只要基础要求做好，其他几个都是水到渠成的事情。

它还提到了，要能基于日志还原整个行为链路。那么就需要对Agent的id，请求的id等进行完整记录，方便还原。

### 异常检测与响应

异常检测部分基础要求是，定义好Agent的行为模式，在偏离时告警。企业级要求则是，建立Agent行为基线，使用统计学方式识别异常。高级要求则是动态建立行为基线并使用AI进行检测。

响应部分它这里的建议是，让大模型帮你提取上下文信息，并作初步研判。人来做决定。

响应的基础要求是，创建一个调查的Agent。这个Agent进行事件的查询分析和总结。缩短人的事件分析时间。建立标准的响应流程。更高级的要求，是对高确定性的事件执行自动化处置流程。包括结束可疑Agent的Session。吊销对应的证书。最高级的要求则是，使用soar进行自动化事件响应。按事件等级进行自动化响应，多个系统间配合进行联动处置。

### 完整性和可恢复

这里有个点很有意思，Agent的行为其实是通过配置文件进行控制的。所以，配置即代码。

完整性对于Agent的基础要求是，Agent的配置要通过版本管理系统进行管理。我相信这一点大部分企业都没做到。企业级要求则是，对确定的配置进行签名，仅允许签名的配置进行部署。高级要求是使用不可修改镜像。Agent镜像只能被替换，不能被修改。

可恢复基础要求是记录回滚流程，企业级要求则是基于健康检查的回滚，高级要求则是自愈，自动化修复。

## 当前企业级Agent实现中的问题

## 问题一 隔离与管控

当前企业级Agent实现中，第一个问题就是，企业级Agent的sandbox中，托管的是openclaw的实例。openclaw的编排系统和执行是在一起的。这个用法跟claude的managed agent天然不一样。claude的managed agents里，系统架构上，编排系统和执行系统就是天然隔离的。控制面和执行面完全隔离。

当然，你如果说，基于egress proxy控制访问，对openclaw实例是一样的。

但要把openclaw里面，涉及到的复杂的各种tool的key抽取出来，就需要进行一番改造。尤其是，如果里面涉及到db等相关资源访问时。

这里有个方案就是，在openclaw中注册的mcp记录，统一指向某个固定的mcp代理。整体不持有相关的key。在被指向的mcp代理服务中，动态获得key并进行注入。在沙箱上设置策略，只有指定的mcp服务可以被连接，其他都被拒绝。

### 问题二 权限模型

第二个问题是关于Agent的身份和权限问题。Agent到底是代表人去操作呢，还是作为一个服务具备单独的权限？这个一直是大家的争议点。

如果是代表人操作，那么是否要在整个Agent的调用周期透传用户身份呢？如果是作为一个单独服务，那这个服务具备哪些权限也要定义清楚。

代表人操作，在整个Agent的调用周期透传用户身份，本身会为整个调用链路带来复杂度。个人助理类的Agent必须要走这条链路，去操作所有暴露给用户的三方服务。

企业内的Agent，更多应该是使用类似于服务类Agent的方式进行提供。用户使用Agent需要进行权限申请。Agent本身也有严格的权限列表定义。

很多企业级Agent并未显式的定义清楚自身的权限列表。更不用提Agent的使用，也是人人可用。

大家做的仅仅是启动一个托管的openclaw实例，在启动时，压根都没定义这个Agent是做啥的，它的权限是啥，具备访问哪些资源的权限。还处在探索Agent使用的阶段。而不是严格按照数字员工的角色模型，进行权限配置。

####

## Claude是怎么实现的？

#

## 隔离与管控 gVisor + Vault

这里讲的企业内部的Agent安全，使用场景更像是Claude Managed Agents这个产品。云端托管运行的Agent。

在这个产品里面，Claude最为人称道的两个设计：

1. 凭证信息托管 Vault
2. 沙箱 gVisor

![](https://mmbiz.qpic.cn/sz_mmbiz_png/YuBibjKRq0Lexr5Neg3AMGNsRjHxnzqdaBBX9QxbSWLhz5KgWrrW46STWsdVdHnib3DBlGBY38TOp4krn9EWP7oN9U5oOUzTbcd2McocPG0n4/640?wx_fmt=png&from=appmsg)

这里有两个点：

1. 沙箱内http请求是通过egress proxy走的，注入的环境变量。指定了包括http\_proxy等环境变量。这个环境变量里面，有加密一个jwt token，作为这个代理的密码。这个jwt token里可以解出这个Agent的id。里面包括了container id，session id，企业id，过期时间等字段。从而构成唯一的agent id。本身jwt token中带签名字段，从而保证不可篡改
2. 用户对外部mcp的操作，通过控制面api注册后，这些mcp的凭证全部由控制面管控，放在vault里，不暴露给sandbox

基于gVisor可以控制允许调用的api，基于egress proxy可以控制允许的三方域名访问。

权限  Claude Tag权限模型

Claude Tag是Claude官方提供的类似于数字员工的形态。

管理员可以配置某个Claude Tag具备的权限（例如操作代码库，查日志，访问数据库等。允许使用哪些mcp，哪些connector，哪些skill）。然后普通员工可以把这个Claude Tag拉到Slack工作群里，给它委派工作。这个Claude Tag具备管理员配置的初始权限，同时也具备所在的工作群拥有的权限。（例如你可以在claude的配置后台中，指定某个群具备访问薪资待遇的skill权限，那这个群里的Claude Tag就能访问薪资待遇）

这里最有意思的点是，这个Slack群里的员工可能本来都没有这些权限，通过指派Claude Tag完成了对应的事情。例如，本来大家都没法查数据库，让这个数字员工查完，把结论发了出来。

看起来这不是一个安全的设计。但Claude在自己博客里指出，数字员工的能力，取决于它的权限有多大。

管理员需要在claude管理页，设置好Claude Tag的全局权限和各个群组具备的skill connector mcp的权限。

![](https://mmbiz.qpic.cn/mmbiz_png/YuBibjKRq0LfVQ23aOFqoqXQV9iawMLa1jnhu5Hg2x79upwGYYfIdia0Ue8qXyMruPOY0ZOoThnXFTicLiaHGsppVadWzibHBwuAWywfby3JIxGRM/640?wx_fmt=png&from=appmsg)

参考文档：

https://claude.com/blog/agent-identity-access-model

https://claude.com/blog/enterprise-managed-auth

https://claude.com/blog/whats-new-in-claude-managed-agents

https://claude.com/blog/zero-trust-for-ai-agents

https://pluto.security/blog/inside-claude-managed-agents/

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/ZrnQ9cTzz1WOsZoFuzvcqld7856xdZUXcXVmW7W3IPYG61GL78m6ILibka5ibzU3jtSBwNcKWUibiboYRfGwuTTOSA/0?wx_fmt=png)

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