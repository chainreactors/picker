---
title: 最新Deepseek dsh红队模式安装与验证
url: https://mp.weixin.qq.com/s/ykj51mcgAVue-zwZlrnznA
source: Doonsec's feed
date: 2026-09-23
fetch_date: 2026-09-24T06:56:51.099102
---

# 最新Deepseek dsh红队模式安装与验证

# 最新Deepseek dsh红队模式安装与验证

原创

小智
小智

智榜样网络安全学习中心

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

2026年 AI 红队项目的口径趋向相同，把模型调配成黑客，用一句话来进行渗透，比的是**谁的agent更厉害**。

在角色设定当中有纪律，比如证据能够复现，不确定标有疑似，资金接口没有自动执行，两万字之后上下文压缩就松开：**它把“可能”写成“确认”，替你签字**。更为棘手的是门禁是由它自己来判定的：你让它进行过，它回到“已经通过检查”，它开没开的文件，你是查不到的。 SeaOf0和dsh - redteam - model相反的情况：**不去训练模型，不去调用权重**，将deepseek的Deepseek - harness当作一层“人设加上工作手册加上强制插件”，把**32道阶段的门当作模型需要调用的器具**，把判定写进gate - log. md里面。8月进行建仓，MIT，10模式加上17插件，得到582星。

本文仅仅做一件事情：**装上它并且证明装上**。门如何划分门内如何校验运行期如何跑这些都不属于本文的范畴。

## 装了什么

先对依赖关系进行说明：**此项目并非是独立的工具**。它的主要使用者是dshWeb，它自身仅仅提供“预设（preset）”以及“插件（Chengin）”这两种扩展形式。项目自身的说明是很直白的，它是对deepseek - harness进行赋能的项目，**先安装dsh然后再安装它**。

每一种模式都包含自身所具有的四层的资产，按照dsh模式去设计约定的组织：

**模式的自包含四层资产**

| 层 | 文件 | 职责 |
| --- | --- | --- |
| persona | `agent.cordis.yml` 的 `persona` 节 | 角色、认识论、边界、报告纪律 |
| playbook | `skills/<mode>-playbook/SKILL.md` | 方法论与门禁文本契约 |
| skills | `skills/` | 可加载技能 |
| refs | `refs/` | 外部知识库（原文索引化，零本机路径） |

此四层并非并列的文件，而是**“越向下越具体”**。persona属于宪法范畴，playbook属于业务流程体系，skills属于操作手册领域，refs属于参考资料范畴。**判定一个模式是否良好，关键在于这四层是否相互矛盾。**

这里存在一个很容易被忽视的细节，得单独说一说。**模式的入口文件 `preset.yml` 薄得几乎可以忽略**——`redteam` 模式的完整内容是这样：

```
name: redteam 安全研究员
description: 安全领域总入口与多任务总控：适合便捷通用场景、多任务协同与轻量级安全任务。
order: 0
```

真正的重量全在后面：同一个模式目录下的 `agent.cordis.yml` 有 46 KB，里面的 `persona` 节用中英双语写死了十二条共性条款和一组铁律；`skills/pentest-playbook/SKILL.md` 有 80 KB。**所以"模式"的本质不是那行名字，而是它的 persona 与 playbook**——想改造它，改的是这两处，不是 `preset.yml`。

### 1.2 十个模式与十七个插件

十个模式的定位如下表。

**十个工作模式**

| 模式 | 定位 | 什么时候进 |
| --- | --- | --- |
| `redteam` 安全研究员 | 通用总入口，**无 Gate 强制链路** | 普通提问、多任务协同、深度任务的中转站 |
| `pentest` 渗透测试 | Web/API/app/小程序全等级 | 拿到域名或 ip:port 做黑盒 |
| `code-audit` 代码审计 | 白盒与动静态审计 | 有源码要读 |
| `binary-analysis` 二进制分析 | 病毒分析、逆向、脱壳还原 | 有样本要还原 |
| `attack-defense` 攻防评估 | 多主线：web 打点 + 内网（Windows/Linux、有无监测、域、云内网） | 整体评估、内外网全链 |
| `av-evasion` 免杀对抗 | 攻击视角免杀，shell/loader/C2 变形 | 要对抗检测 |
| `incident-response` 应急溯源 | Windows/Linux 应急排查 | 挖矿、蠕虫、木马处置 |
| `cloud-security` 云安全攻防 | 云平台与云原生渗透 | 云账号、K8s、容器 |
| `ctf-solver` CTF 解题 | 题面登记、模块路由、解题循环、flag 台账 | 比赛 |
| `asset-mapping` 资产测绘 | FOFA/Hunter/Quake/ZoomEye/Shodan + 子域/DNS/ICP + 指纹，产出六工作表资产清册 | 先摸清自己或客户的家底 |

注意`redteam`那个括号里面的内容，它是**唯一没有Gate强制链路的模式**。不是没有做完，而是设计：在通用场景当中强行套上门禁只会让交互变慢。**深度的任务请切换专业的模式**，这是作者自身重指出的。

下面这四张图是其实际界面的模样，分别为任务台，攻防评估，代码审计，二进制解析这四个视角。**它们并非示意图，而是web端实际的读数。**

作战大屏redteam的任务台，九种模式跨越会话聚合成果的总数以及风险等级的占比

![任务台视图](https://mmbiz.qpic.cn/mmbiz_jpg/ibzm8nWOdauMbpIhKtsQTDNBwkmm7ZCjDW3A2xYoQNOicU8z0mic8ibafoCDOZicaSFIUYxx3YUibCjKFgx1rEckKJG84pDPz2Hic9c6OchFs0ia45Y/640?wx_fmt=other&from=appmsg)

任务台视图

攻防评估模式的成果页，按风险等级与来源分账，支持导出总览 MD / 报告包 HTML

![攻防评估模式](https://mmbiz.qpic.cn/sz_mmbiz_jpg/ibzm8nWOdauN42p7P540Jicp4N5MuHAbFH3SickdgYtXRxNPaC9BZx6OJ3Mtru5Q3ZwA2709QkhWPialNLrSRUTpyxTARUu2zibd1IFpEA2ticjEE/640?wx_fmt=other&from=appmsg)

攻防评估模式

代码审计模式的成果页，类目分布与来源分布分层统计

![代码审计模式](https://mmbiz.qpic.cn/sz_mmbiz_jpg/ibzm8nWOdauMNbIfLjCKemiaUUPFrrx0lzYsl7O9LGWauIWW7daN3Tzf8m4fvndno4Ggo16XgbvUEt5S6bygBiaWIKgQ3x6bfmyCKOCrEyOALY/640?wx_fmt=other&from=appmsg)

代码审计模式

二进制分析模式的成果页，产品类型、家族分布、壳与保护三项独立统计

![二进制分析模式](https://mmbiz.qpic.cn/mmbiz_jpg/ibzm8nWOdauMc9jvnQ2XCv6OD2uLOMeNg4rjlrWxYBWzJd4iaetvWnavNEKR90nEIc6Hw0SATy5ybYR17z8n2XiclUS0RQGgoG9OfibS1AlAvmA/640?wx_fmt=other&from=appmsg)

二进制分析模式

**十七个插件不是平铺在同一个平面上**，这是理解它扩展机制的关键。**挂载位置决定了工具对哪些模式可见**：

**十七个插件的两个平面**

| 平面 | 插件 | 可见范围 |
| --- | --- | --- |
| 宿主平面 | `dsh-stage-gate` 、`dsh-route-boost`、`dsh-sec-enforce`、`dsh-refusal-guard`、`dsh-trace-vault`、`dsh-auto-advance`、`dsh-product-subagents`、`dsh-mcp-studio`、`dsh-redteam-results`、`dsh-hunter`、`dsh-campaign-memory`、`dsh-mode-group`、`dsh-session-pulse`、`dsh-attack-atlas`、`dsh-webshell-mgr` | 全部十个模式 |
| preset 平面 | `dsh-scanner-tools` 、`dsh-semgrep-audit` | 仅 pentest / attack-defense / cloud-security / ctf-solver / asset-mapping 五模式可见 `nuclei_scan` 等扫描工具 |

preset平面这一行**属于安全边界的设计，并非是配置方面存在疏漏的情况**。CTF进行解题以及应急溯源的模式没有主动扫描的工具，原因是**这两种任务本来不应该针对目标去进行nuclei**。反过来如果你在ctf - solver的会话当中看不见扫描器的话，那就是错误的。

Hunter狩猎的插件，是FOFA / Hu / Quake这三个平台的资产聚合情况，支持“标记授权”再进行实测

![hunter 狩猎](https://mmbiz.qpic.cn/mmbiz_jpg/ibzm8nWOdauOpV4wFAfuR2TbMyxUMcKiaZCoe3J6YCgXstNbcE0430AzTJicAJibck8wGjqdGNibpYrOkmE4ibmacLXel0ZnHyibQBz6pjvjKKH4T0/640?wx_fmt=other&from=appmsg)

hunter 狩猎

webshell 管理插件，生成器 → 协议自动识别连接 → 命令执行 / 文件管理 / 数据库操作的作战台

![webshell 管理](https://mmbiz.qpic.cn/mmbiz_jpg/ibzm8nWOdauMaOCd785WOsvBmp48O0Mic3J77IOxibRSgGqK9xYpYKW9GucTLRQzvTWRU9xXkkNChiaFd8K3hEQ2UiaQiclibko9LhcTHbRcQsrbRg/640?wx_fmt=other&from=appmsg)

webshell 管理

### 1.3 双层防线堵的是两类不同的失效

项目README把设计原则写成一句话，**文章纪律persona / playbook和运行时强制插件两个双层的防线**。这句话是值得去阐释的，因为它是全文非常关键的部分机制层面的阐述。

先问问：**为什么不能仅仅借助persona把纪律写死**？

因为persona乃是文章。**会被压缩、被更靠前内容所稀释、会被绕开模型自身合理化的内容**。会话短的时候能够起到作用，会话时长过长临近性就没有了。作者清晰地阐述插件设计方面的说明：**persona常用的条款是在长时间的会话被压缩之后丧失临近特性**。

于是就出现了第二层，**把可以被机器判定的区域，从文章要求转变成为工具调用**。区别在哪些地方？

文章所规定的：在确定P1七个产物是齐全的之后开展开测工作。**模型可以认为自己已经具备。**工具开展调用的相关操作：开启stage\_gate模式，stage，workspace，之后返回pass : false, missing : }。**模型获取到的结果呈现出失败的状态**，并且**这个判断被添加到Gate - log. md里面，你之后可以进行查看**。

`dsh - stage - gate`的README里面存在一句用来定义这件事的原文：**结构检查可以被机器判断**，文件是存在或者是非空的，需要进行标记操作，表格行完整，产物希望进行登记。**语义门禁归到复核员那里，结构已经完整通过了。**

它不存在假设插件可以判定所有的事情。机器能够判定文件是否存在、表格是否填满、希在是否在等情况。**不能够机械地去判定这一攻击链是否成立**，n - A的原因是否是真实的，并且在工具的返回值当中用`manual`字段逐一列出来，让模型不可以把“结构已经过了”的错误看作“全部已经完成了”

此乃整个设计的最为坚实之处：**它明晰自身的界限，并且将界限写入接口之中**。

## 如何安装？

**检查 Node 版本**

```
node -v
```

安装dsh

```
npx -y @deepseek-ai/dsh web
```

![image-20260923135744083](https://mmbiz.qpic.cn/sz_mmbiz_jpg/ibzm8nWOdauMK0byicbz75y1r1Y4hRaLoWtNyAMWP6Sc5qvPWwbdbTxomRszF6AZIG9ia9xZqkolXyArhWnlwlVFliadTuicFibJROEFxeiaFeBLXc/640?wx_fmt=other&from=appmsg)

image-20260923135744083

浏览器打开界面

![image-20260923141141447](https://mmbiz.qpic.cn/sz_mmbiz_jpg/ibzm8nWOdauP459D3miaI5DSK8k9jhUhwR1fL4b6MnlbptBT5EEwRHkl4l7sBVPnPvtibsFiamicXOzZQ3NParriaGFJ755NVzIaj8MurkpeH2mNw/640?wx_fmt=other&from=appmsg)

image-20260923141141447

安装插件

```
dsh plugin --profile web add github:SeaOf0/dsh-redteam-model
```

![image-20260923141528479](https://mmbiz.qpic.cn/mmbiz_jpg/ibzm8nWOdauO5dpgOlmV02jFmcR5r9pjp2KEGKAnkLLXx6H12qsOic0UcseFZo1jMbYsW5JYJmPGUExOvxvzHoOXp5fRxTWahXuNicPo2eWnTA/640?wx_fmt=other&from=appmsg)

image-20260923141528479

在设置中启用所有模式和插件

![image-20260923142000318](https://mmbiz.qpic.cn/sz_mmbiz_jpg/ibzm8nWOdauMkRVZaIBgkekYNkUniahktk2ZE7DvRgq5uAAHEVLEgcNRickJF2nvzPsF4X4Y7UgAibmqhD4IWibIHvN8uM28iaZpD849EMNKrzlok/640?wx_fmt=other&from=appmsg)

image-20260923142000318

确保是这个样子

![image-20260923142026359](https://mmbiz.qpic.cn/sz_mmbiz_jpg/ibzm8nWOdauMp7NE4zic8PdW5E6OrLwHyusdFnAIEAiatLGE5gpwQH9Rr6P5iaicvZMuCdhiasiciaUPupEH4haaibqJTOH3zJZpgjjiaPpR2G2EibKwCg/640?wx_fmt=other&from=appmsg)

image-20260923142026359

全部安装完成后重启dsh，就能在会话中模式选择中看到安全研究员和专业安全模式

```
npx -y @deepseek-ai/dsh web
```

![image-20260923142404395](https://mmbiz.qpic.cn/sz_mmbiz_jpg/ibzm8nWOdauPyM4wibDqkkrjKDocC04PeaKkLToXUZiapA28ddZyPXUXY5ojcCR6bg0cUrlhDEkpBkje5FHpubC6NQss3ew5DiaKHH3z3ia0NyHY/640?wx_fmt=other&from=appmsg)

image-20260923142404395

![image-20260923142509199](https://mmbiz.qpic.cn/mmbiz_jpg/ibzm8nWOdauM9sCzZzkmhFKVwI40CmBYhANn41SD61wBeribo38aLVvicEEPYvqbLLdDm6YZwibXKGXuC9UpYgLIIDhzT6RIRwl6QdboLMn5SM4/640?wx_fmt=other&from=appmsg)

image-20260923142509199

### 单元小结

让我们来总结这个学习单元，首先我们确定这个项目并非独立的工具而是dsh浏览器的预设以及插件的集合；随后我们拆解一个模式下的四层的资产，发现`preset. yoml`仅仅是门牌，实际的重量是**persona以及playbook**；接，我们对表2，表3进行对照，明确十个模式以及十七插件，并且区分宿主平面和preset平面两个具有可见性的层级；最终我们阐释双层防线是如何存在的— —文章会伴随会话的延长而失去作用，**结构校验能够作为不可自我辩解的工具来进行调用**。

## 🎁 互动与福利

**分享本文到朋友圈，点赞+在看+关注，一键三联，可以凭截图找老师领取**

上千**学习资料+工具**哦

![22919c6e4ef945aa9a9cbf0f6df4f6ff](https://mmbiz.qpic.cn/sz_mmbiz_jpg/ibzm8nWOdauOBpVykzCwoIMLHhQ0A0d4JopfTYNX5bicUZkNErRH4EYmibnktT2x0iajAslq1CGBunjoZC6UiaE7Ges2J7eJKqEIibAuiafohPw0wo/640?wx_fmt=other&from=appmsg)

22919c6e4ef945aa9a9cbf0f6df4f6ff

**分享后扫码加我！**

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/rYoibTlMQ1MpHdawUKrSwglIRtuj0JaKrsHFZKjEmiac6PBmXbWcK5fMZDnDJQHn3m...