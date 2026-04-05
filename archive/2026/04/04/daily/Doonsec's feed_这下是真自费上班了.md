---
title: 这下是真自费上班了
url: https://mp.weixin.qq.com/s/hIqe6D_PHXx8Krnk4O31JQ
source: Doonsec's feed
date: 2026-04-04
fetch_date: 2026-04-05T04:31:19.938554
---

# 这下是真自费上班了

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/OxxhRu5yCXskmlMc3hsWb1N06RGEH84DceLEDj1txSoRk4fDnWxCxJrjVJfJu7Q0ukObxotZDoWa8IONXaV4mHX1xiayiaQ9oKzzrMP3TtWzg/0?wx_fmt=jpeg)

# 这下是真自费上班了

原创

招财大土豆
招财大土豆

大土豆的菜栏

![]()

在小说阅读器中沉浸阅读

我现在是一个躺得很平的人，技术也不搞，漏洞也不挖，每天上班就摸鱼，摸鱼到下班

最近部门里的人被 AI 卷到了，然后这股风气卷到了德国，躺得好好的我也被卷了起来

那么就学吧，LLM，MCP，Skill，Agent，Plugin 还有最近特别火的 OpenClaw，以及随之而来各种 Claw

简单理解 LLM 是脑子，MCP 相当于给一个脑子装上了手，所以前段时间有很多 MCP，比如 IDA MCP，JEB MCP，这样 LLM 就可以自己调用这些软件的接口去做逆向分析，而不用我们一段段代码拷贝给 LLM 了

Skill 可以理解为流程固化，比如先干什么，再干什么，然后还有分层加载的概念，可以减少上下文占用，我的理解是它能够减少对用户的专业要求

Plugin 像是复杂版本的 Skill，带有各种 Skill，Agent，Hook 等东西

举个例子，比如我要开发个应用，那么就可以装 SuperPowers 这个 Plugin

* https://github.com/obra/superpowers

它里面有一二十个 Skill，在没有装这个 Plugin 的情况下，可能 ClaudCode 就直接开干了

装了这个 Plugin 之后，ClaudeCode 就会基于 brainstorming 一个个问题问清楚我的真实想法，确定好后使用 write-plans 把完整的开发计划写入到本地 markdown 文件中，接着再用 using-git-worktrees 执行代码版本管理，开发好的代码先在分支上测试，用户确认好后再合入主干，以及这里还会用到 subagent-driven-development 的模式来节约当前对话上下文

![](https://mmbiz.qpic.cn/sz_mmbiz_png/OxxhRu5yCXskKazf1OE5k9EM7d7UwNoPfc7CtBKzP1fW39lotjqHLBL7jUOjSt0TiaJ4ibsrBz0vEMicuOVp21YppxSialiblDP084U1LwFlXOd8/640?wx_fmt=png&from=appmsg)

以上就是我说的减少对用户的专业要求，有了这么一套 Skill，用户实际上不需要特别多的研发经验，也能享受专业的全套研发服务

唯一的缺点是这一套下来很费 Token，一个问题能干掉一个 Session 的额度（用超大杯吃到饱走 API 调用的富裕单位请无视这条

由于 Skill 带有脚本执行的能力，所以出了个新名词叫做 Skill 投毒，用比较热门的推特搜索 Skill 讲解下

* https://clawhub.ai/jaaneek/x-search

推特搜索 Skill 就一个 SKILL.md 和 search.py 文件，那么如果脚本里有恶意的代码，就会把你电脑里的漏洞偷光光

![](https://mmbiz.qpic.cn/mmbiz_png/OxxhRu5yCXtf0H0sdOicBjnbZbQT3X9q6efcL0oWRPiaVHEJdD2BaKgbibnm13QlIte1dloGcb18JntzN6MJDGlibCvwrOuEibXwEqhO8uFkia3BM/640?wx_fmt=png&from=appmsg)

说到这我突然有个想法，可以搞一个原创漏洞区块链项目，类似 NFT，只不过这里的数据单位是加密后的漏洞证明，可以证明这个漏洞是你先挖到的，对于漏洞奖励计划来说，这也是一种应对上报者质疑重复漏洞或者已知漏洞的一种公开透明的方案

这个项目我看看能不能找王多鱼投一下

再就是 OpenClaw，也就是大家说的龙虾，一开始我确实想买 Mac Mini，但是德区的数码产品很贵，即使是最低配的也要 699 欧元，下不去手，所以就放弃了

![](https://mmbiz.qpic.cn/sz_mmbiz_png/OxxhRu5yCXsU12mz36CT3QF31gTgkEgCm0TrENA77RiaicxpUBibSEu4nuMepUx50y4mp9tSOoGbVjlmpS8aWNNWnbd57OFArJzoZlWtL8pbT4/640?wx_fmt=png&from=appmsg)

我手上有一台 Macbook Pro，直接装的话安全风险比较大，所以先用 Windows 笔记本安装尝了尝鲜，结果拉了坨大的，Windows 安装 OpenClaw 真的很难用

正当为难之际，刚好看到了腾讯爬 OpenClaw 的 ClawHub 仓库事件，ClawHub 是 OpenClaw 的官方 Skill 仓库

* https://clawhub.ai/

![](https://mmbiz.qpic.cn/mmbiz_png/OxxhRu5yCXvX2GAuNFJicqv0LOSJHYxEdpBE9aLEJ7gT4WWSib5ES3jicWsbqvoSkagM3jFNibIoVEdiaJAJTiciavdcx7YiahibUNA8mS4tytsgonuY/640?wx_fmt=png&from=appmsg)

腾讯爬了人家的仓库还自己搞了一套一样的，对外口径是说减少人家服务器的压力

* https://skillhub.tencent.com/#categories

![](https://mmbiz.qpic.cn/sz_mmbiz_png/OxxhRu5yCXuQg8eIlQlQtvQCN2vfEt3JPCNrnPj05o6q06cQCX1fZiaMibT1cNB2fjMljZAtqF8dbz1UibicPM0Y6RZblRFJccvkQRq57Va1MN0/640?wx_fmt=png&from=appmsg)

还被 Peter 吐槽了一把

![](https://mmbiz.qpic.cn/mmbiz_png/OxxhRu5yCXuSs9YQ2qsNMVGQvrOFVTBIJhIdL60EwiaqjcIA9GKRzrFUmmBwzIEJYN4z0yFqmPkHlicPDj5H4mmg0sdpLickB1O1EOksA1xVhI/640?wx_fmt=png&from=appmsg)

结果没多久腾讯就成了社区赞助商，而且占俩广告位，有钱真好啊

Peter：看人真准！

![](https://mmbiz.qpic.cn/sz_mmbiz_png/OxxhRu5yCXvzIYlDDr4ksL7C9DsYSHcibKNicPhQbibLKV0IrSia9uQd69ch7csbWfH1a9pHkBMxzCqhhfrHqRa94jSP4m9JD1icayAp1U2IYMib0/640?wx_fmt=png&from=appmsg)

在这个期间，腾讯云也没闲着，火速推出了养虾套餐，199 一年的云服务套餐，一键安装

* https://cloud.tencent.com/act/pro/openclaw#T1

我买的是右下角那个，左上角这个 88 一年的配置稍显逊色，不过也还行

![](https://mmbiz.qpic.cn/mmbiz_png/OxxhRu5yCXsyh2wZOUbxoqCfFmSGAcDKqWDdIgNTj0XxMhs95uS8WcwiaGquvr4dWrDwW6GxSiaPcZxpq5OZicsBsJvw9rhz6ibiay7Ah6zTh9Ec/640?wx_fmt=png&from=appmsg)

管理起来非常方便，配模型，绑通道，Skill 也封装好了接口

![](https://mmbiz.qpic.cn/sz_mmbiz_png/OxxhRu5yCXtciadCgKfRbaxQ2ice3LwUrltr0ibibksRUMTg4kibRp7ialRbvibaA5FNzXF8eyj0Wjic2XatutxZ5bKB6ibpRFQnTaYFJ0XRkpalYnPM/640?wx_fmt=png&from=appmsg)

虾有了，就缺个脑子，OpenAI 和 Anthropic 家的脑子太贵我接不起，国内的 GLM 单买也挺贵的，各厂的 Coding Plan 因为时差问题我也熬不了夜去抢，就暂时用了 GLM 的免费试用装

* https://cloud.tencent.com/act/pro/codingplan#buy

![](https://mmbiz.qpic.cn/mmbiz_png/OxxhRu5yCXuM4SaxNgKzvVsvhsaBfxbJFlUtQcXHzu8xibepwFIw2NYvB3iafX5aSFoHlJNhnnsg8lkEPceic6cZCibjqq914wGSh8yX2CwzbI4/640?wx_fmt=png&from=appmsg)

现在拖着拖着，这个虾我已经不想养了

另外我还听说一些公司已经全面接入 Claude，还把 Token 用量当做 KPI 进行考核，甚至鼓励员工自己学习 AI，学习 AI 的钱也能报销，我真的很羡慕

相比之下，我的单位在 AI 时代就像一只笨重的大乌龟，到现在都没有一个拿来即用的内部大模型服务，有的工贼自费购买外部的模型提高工作产出，现在整得大家都要自费买外部的大模型服务

前段时间我跟内部一哥们磨了一小时嘴皮子要个 API，最后一问模型参数才35b，当时就给我整笑了

然后我又去找另一个组织的接口人，看看能不能给我提供个 API，人家说只给他们部门的人用

巧妇难为无米之炊，我不得不订阅了一些，比如 Claude，还有 Poe，真是服了

这就像什么呢，有人喊我上门安个洗衣机，结果洗衣机要我自己掏钱给人家买，牌子还得是嘉格纳的

是时候喊出那个口号了：去有算力的地方！

话又说回来，虾不养，技术得学，我最近在搞智能体的定制，前两天跟我的专属知识库建设顾问家浩聊天（主要也是问他问题不用消耗 Token，能工智人），他给我分享了二次开发 OpenCode 来定制智能体的经验，OpenCode 是一个开源的 Coding Agent，坊间都说 OpenCode 是 ClaudeCode 的平替，实际用下来还是差点意思（也可能是我的模型差点意思，因为我是用自己电脑跑的Qwen3.5-35b-a3b）

这玩意儿的定制在这里就不过多说了，大家有兴趣可以去官网看看

* https://opencode.ai/

但是 OpenCode 是针对编程的 Agent，如果要做普适性任务的智能体定制，还是想点别的

比如 LangChain 就很适合来做简单的智能体，执行顺序相对固定的操作，基于 LangChain 开发就不再需要自己写 LLM 调用代码了，可以理解为 SDK

如果要做固定流程，尤其是涉及复杂业务状态的场景，就可以考虑 LangGraph，我们需要先定义好一个由节点和边组成的流程图，LangGraph 能够根据当前执行状态来决定下一步要调用的路径，所以它很适合用于构建一套流程相对固定但又需要在一些步骤上利用 LLM 提高质量的 Workflow

LangChain 和 LangGraph 都是 LangChain 团队开发的，他们近期又推出了 DeepAgents，LangChain 和 LangGraph 本质上还是人类定义流程，但是 DeepAgents 是大模型来生成执行流程，先思考，然后拆解任务，不断循环，直至执行结果达到用户要求

另外社区上也有很多开源的框架，我觉得都差不多

比如字节开源的 DeerFlow，去年是 1.0 版本，主要是做深度研究相关的工作（我感觉用来做 Insight 很好用），现在开源了 2.0，深度研究变成了其中一个 Skill，属于是拿来即用即汇报的一个好东西？

* https://deerflow.tech/

看着字节开源了这么多 AI 相关的框架，我感觉这样的单位真好，不知道还招不招人

![](https://mmbiz.qpic.cn/sz_mmbiz_png/OxxhRu5yCXuaXC9ib0uZu49g4U539NEZLXCuxmvqkAoAKY2CCwthktcmlpSkqp5mrR8tDl8EjU8bPfTvMZXGhkHsQCRAq8tY0Nvy0d4v2vCs/640?wx_fmt=png&from=appmsg)

最近我发现一哥们，他的几篇文章都给我很好的启发，就是能拓宽挖洞的思维边界的那种

第一篇是《From an Android Hook to RCE: $5000 Bounty》

* https://blog.voorivex.team/from-an-android-hook-to-rce-5000-bounty

大家如果挖掘 APK 漏洞，这篇文章我真的墙裂推荐阅读，讲的是作者如何逆向分析应用的数据包加解密流程，理解应用与服务端的交互模式，最后控制云服务的过程，非常有意思

这篇文章对我的启示是不要只盯着本地那堆代码，典型的漏洞挖着挖着也就没了，可以看应用与云服务交互的过程，从本地去攻击云服务

![](https://mmbiz.qpic.cn/sz_mmbiz_png/OxxhRu5yCXtI3BP6VCvQlMwtHv3E81oD3uCfldcAZiaiblGiaWtBnXUcTRz0n4RdZ6yo66aSI26M6LHZP5fGGnS0jxvBMWK9Do05cPnicPic6YdI/640?wx_fmt=png&from=appmsg)

第二篇是《uXSS on Samsung Browser [CVE-2025-58485 SVE-2025-1879]》

* https://blog.voorivex.team/uxss-on-samsung-browser-cve-2025-58485-sve-2025-1879

如果只看具体的调用链，这个漏洞是有防御的，通过检查当前是否是模拟器以及调用者包名等信息，严格检查了调用者

![](https://mmbiz.qpic.cn/mmbiz_png/OxxhRu5yCXufkC3AaoLWViaicw0GyDiaLFiblNSxpcV93RNP2HvMhaxiaSxb4842le7wL0Hk8SU1QnEnyO8Uh1GicAWFnvsexkq2aPhickw6otq9dQ/640?wx_fmt=png&from=appmsg)

但实际上另一个 Activity 也能调用到这个漏洞点，直接就能在打开的 Tab 页面上执行任意 JavaScript 代码

![](https://mmbiz.qpic.cn/sz_mmbiz_png/OxxhRu5yCXvh3VR6gYftTBlZAibwmcjpYlqEdiaYRibFm2rsGBYFzyd9s5NIGp0txSFVc4BduQajUlaNJic3GqIHiaDxp0FK5jyXxvuUDIJd1icvY/640?wx_fmt=png&from=appmsg)

那么实话实说，这个漏洞如果给我挖的话，我肯定挖不到，因为我没有想过这种攻击场景，浏览器的 UXSS 我潜意识里觉得应该是同源策略那一套东西，思维定势要不得！

今年的 BlackHat Asia 有几个有趣的议题

《VsyncBreaker: Subverting Screen Trust via State Disruption and ONE-WAY Flooding》：从标题理解，是用 ONE-WAY 模式疯狂给 SurfaceFlinger 发送请求，造成 VSYNC 调度队列的非预期，简单说就是用户看到的屏幕内容和点击的屏幕内容不是一个东西（我猜的，不熟悉，但感兴趣）

![](https://mmbiz.qpic.cn/sz_mmbiz_png/OxxhRu5yCXsGmvBiaUw4oqPlf0K4llhYuu9csjMQ9TKauuuLlrsn6c1WWGxvX8sCt0fbH1uFXDf2Ab1WAqKsRuzXGuWn1Kg4gFh7IVFPgRko/640?wx_fmt=png&from=appmsg)

《Bad Vibes - Pwning Coding Agents 70 Times With The Same Bugs》：针对编程智能体的攻击

![](https://mmbiz.qpic.cn/sz_mmbiz_png/OxxhRu5yCXuR3RVH9fMADoG1vNLOra7wVmn0OxxSdXRQwbyOPdgQiausXbkjE3Pr6KuibjjAqEN3ic4cMhOUNKp2icRdic1MryOVb6VSDfBtsNiaQ/640?wx_fmt=png&from=appmsg)

还有一个议题，搞好了我觉得能卖钱

《The Curious Case About Apple and Its Intelligence》：这个议题主要是探讨对一个具有 OS 级别 AI 的系统取证后，如何区分哪些行为是 AI 做的，哪些是人做的

![](https://mmbiz.qpic.cn/sz_mmbiz_png/OxxhRu5yCXvOumQ83MiamUh1rUEUG8SEENlgcyR8k8pcTqNQ01zICqXmvHIVNSI9vfLo6NuxdsDXia9RnlnhNmZb6ibFJTmGgWxfUic0MFvRibQE/640?wx_fmt=png&from=appmsg)

接下来讲点安全圈的

Anthropic 最近在代码安全审计上发了很大力，先是吹了一把他们的大模型发现了 500+ 个漏洞，这里面没有 CVE 或者致谢啥的，所以对这 500+ 个漏洞的真实性我持保留意见

* https://red.anthropic.com/2026/zero-days/

![](https://mmbiz.qpic.cn/sz_mmbiz_png/OxxhRu5yCXvlZ4VfUr3jbGHdE61krhiaJ4sIOhd7tG2qEicyGnMVG7HTx21jOXtsQVxlmicxGFCmP2Thlwic3Yia7cYogC6KSRIBuj5h86Xn0SMM/640?wx_fmt=png&from=appmsg)

紧接着又说他们挖了火狐浏览器二十多个中高危漏洞，由于漏洞已经经过 Mozilla 二次验证所以瓜保熟

* https://www.anthropic.com/news/mozilla-firefox-security

![](https://mmbi...