---
title: 不用羡慕Mac用户！Win端Codex入门教程，一样能用爽
url: https://mp.weixin.qq.com/s/TfhAeiKYBjCvF9GcLrsb5g
source: Doonsec's feed
date: 2026-06-18
fetch_date: 2026-06-19T07:00:08.805275
---

# 不用羡慕Mac用户！Win端Codex入门教程，一样能用爽

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/WCtibmYn046h7Jd4MEtfEAiaT9bNcDqo2J1C8am11l0mVEeHG6fibER63Q4Yj2LK0VWNicT3OPGjiadC1XjFjSfNHBQ2WArqnnwALmMIYU9bfiayc/0?wx_fmt=jpeg)

# 不用羡慕Mac用户！Win端Codex入门教程，一样能用爽

玄月调查小组

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

编者荐语：

/goal 给我赚到一个小目标

以下文章来源于矩阵哨兵
，作者矩阵哨兵

![](http://wx.qlogo.cn/mmhead/VNMic85jx3X7dflQtnx0yZkNFuYWm4tCyT1vyfVN3QClWAMwunpib9TeDDbqsYC4GuCzpFrnew5hU/0)

**矩阵哨兵**
.

重构认知边界，让AI成为你的第二大脑

市面上有很多Codex教程，但大多数都是针对于mac端，针对Win端的零基础配置指南很少，有些小白甚至卡在了微软商店安装Codex的步骤上，本篇文章致力于做最细节的Win端Codex入门指南，欢迎点赞收藏~

## Codex app安装

众所周知在微软商店下载东西体验是真的蛋疼，经常重试断连。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/WCtibmYn046hc4CDwCbETjD416Oy5SOPW1gmUl9jqvKicJdwpzEeyPAhlnQVT8KUJYLL4zFHaNIh2JwFnY94MNibYWvIfypvN7VBAIFNDHET2U/640?wx_fmt=png&from=appmsg)

这里我分享下在微软商店下载东西的焚决： https://store.rg-adguard.net/

在这个网站中粘贴想下载的微软商店软件链接，然后选择下载渠道，一般选fast，如果不行就顺延，如这里我们输入codex的微软商店链接： https://www.microsoft.com/zh-cn/p/codex/9plm9xgg6vks

![](https://mmbiz.qpic.cn/mmbiz_png/WCtibmYn046gyXDkgG5cY7YRd1IKWibibtyCic3M80XjmQE3ctFnRGJGHMobxm7UldB73Ohe0ibZtn9ib6RdnOed5qmre4wH6nuQJmLG2UiclxPhTM/640?wx_fmt=png&from=appmsg)

它会帮我们提取对应的软件离线安装包，点击下载的msix文件，我们就获得了codex的本地离线安装包了，再也不用担心微软商店无法下载的问题了。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/WCtibmYn046jsXBPu9AQ1ojbHqC9dCO0mkRu5ZeUVibzr3h3eHLbC2VusuBup6ljCcxpib3ZBtP2dibqPuQvP5lvicjUhCNcMF469n5HEIiamv5CI/640?wx_fmt=png&from=appmsg)

## codex api key配置

首次启动时，codex会问你如何登录，考虑到很多朋友都使用API KEY调用大模型，这里我们选择"sign in another way"进入api key配置页面。

![](https://mmbiz.qpic.cn/mmbiz_png/WCtibmYn046ia300Kf6CDSCbS3cyoMOZibx524SPpCVicpQ69Itg109Vdia5iaVQGYmov4FVPy64OPbJxzSD8xKQYAXRHgIhBS5RvrMH1tSW6skWI/640?wx_fmt=png&from=appmsg)

这里的api key是openai官方的api key，这我们肯定是没有的，所以随便填一个就行。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/WCtibmYn046iaGGnqqVx9ia0O3pLaIfxsnnIDNdrvGZgBAJMZYQarX3NTNCsSF2DwUwdnyY3OysInaOeFRl9Hdn99keHt7eSfZkUBrITkKF3sg/640?wx_fmt=png&from=appmsg)

接着我们退出codex，因为关闭codex后默认会把程序放后台，我们需要手动exit才能彻底退出。

![](https://mmbiz.qpic.cn/mmbiz_png/WCtibmYn046glXuW8LCT7EI77fticpgwOqro1aJtiatbCzQrcOdaLzSCQh7BNH2ovZ1dH0R6cD2nOZXg1IVKAXSQGP37TdwCXGaKXrCiahKibFaE/640?wx_fmt=png&from=appmsg)

下面开始配置key，我们打开此电脑，在路径一栏输入`%USERPROFILE%\.codex`。

![](https://mmbiz.qpic.cn/mmbiz_png/WCtibmYn046gZ1BbGh7pCY8AtJL2lPZ4Fuwq0QBicoble2EM6rZbJojEFE7DSgGicfEpGfsPfJJicWr5cEoFoWyDn3baBqprhHhKMzgI8I5zPoA/640?wx_fmt=png&from=appmsg)

进入codex配置文件夹后，我们需要编辑config.toml和auth.json。

config.toml里面放的是openai的供应商配置，我们在文件顶部加入如下参考内容：

```
# 自动审批，减少人工介入
approval_policy = "on-request"
sandbox_mode = "workspace-write"
approvals_reviewer = "auto_review"
# 默认供应商配置
model_provider = "hachimi"
model = "gpt-5.5"
model_reasoning_effort = "high"
network_access = "enabled"
# 隐私设置，关闭数据收集
disable_response_storage = true
windows_wsl_setup_acknowledged = true
model_verbosity = "high"
# 模型供应商
[model_providers.hachimi]
name = "hachimi"
base_url = "https://sub.hachimi-ai.com/v1" # 按需修改
wire_api = "responses"
requires_openai_auth = true
```

具体含义这里的model\_providers配置可以自己更改，只要支持responses接口的大模型都行。如果大模型不支持responses，需要通过completions等项目中转。

然后我们修改auth.json中的OPENAI\_API\_KEY，改为模型供应商对应的key。

```
{
  "auth_mode": "apikey",
  "OPENAI_API_KEY": "sk-xxx"
}
```

配置完成后我们重新打开codex，并设置沙盒，这里会弹出UAC，我们点击确定就行。

![](https://mmbiz.qpic.cn/mmbiz_png/WCtibmYn046g8AQWF2hYg51wchFLiaZI3ib4mF1fNic6zR4GNkBHQpKrsa6dWw1DllgMOHEKibY7g0s8TMSBfJGIkvEWqtuXO5VfUXpaKMHd97Lw/640?wx_fmt=png&from=appmsg)

## 解锁API模式插件

默认情况下使用API模式发现插件是未解锁，或者是不全的。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/WCtibmYn046h2TnWtvz3BpmoViaFhOkVu1xoZAepRr4mFq32pmw6ACkppmicLEvocJMODWD1jyWTKDspdQmPQ1kicg7PGiadSCDCxicaCRsACnZjk/640?wx_fmt=png&from=appmsg)

这里我分享个神器：CodexPlusPlus，这个开源项目可以让API KEY模式的codex恢复满血：https://github.com/BigPizzaV3/CodexPlusPlus

![](https://mmbiz.qpic.cn/mmbiz_png/WCtibmYn046ia5WCCicPp2gR61GcSeGzhTazmoo0qBlAaibjaQQhFkeicrA6Mk38ohsRH2dAaDZutztdxpPrDQS2qU43RJqgb85LCibZHkSykTjgo/640?wx_fmt=png&from=appmsg)

在releases中下载x64版本并安装，然后我们打开桌面端的codex++图标，便可以看到插件都解锁了。自此，codex 安装圆满结束。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/WCtibmYn046jt9e9wKxjAYUrdJNOWWcoIZAR2wwmC94VdE7jGDjJHAWSuYqN6qicCkMqpVCFRnE2JGwaFzA4zbhfVHqrMEp1jPDRKkpq7DMicA/640?wx_fmt=png&from=appmsg)

## codex配置

codex常规配置中，我们可以按需选择codex工作模式是**编程**还是**日常任务**，权限建议开启**默认权限**和**自动审核**，另外，在未安装wsl情况下务必选择**智能体环境**为**Windows原生**。

![](https://mmbiz.qpic.cn/mmbiz_png/WCtibmYn046jwrFN15IZpzYxqibXYBUbc3iaGWxowWTyMCtMGtVV4giaGG0Ded2TSibe0icCwtlkMNAZ1OASyujjLiavpkOQTyoaIWTQZibkc6icrDsw/640?wx_fmt=png&from=appmsg)

在个性化配置中，我们可以定制codex的个性，如果希望codex记住曾经的对话，建议开启codex的记忆功能。

![](https://mmbiz.qpic.cn/mmbiz_png/WCtibmYn046gXDLGuocHr8EVibTLCjgicM2LFjhlIajKdN0Xc3F75PliaIAy5R4wv55bEHJkqbbqowWIPwhibc9bHDjVwNG1LxmlSyRuclbd984o/640?wx_fmt=png&from=appmsg)

## codex 插件

下面是codex我个人认为最核心的功能：强大的插件和技能系统，我们可以选择不同的插件市场的插件。左上角则可以切换到技能市场。

![](https://mmbiz.qpic.cn/mmbiz_png/WCtibmYn046iagKTrgPyMaFubUVABeDkb9ibeUYAvEfvooiak71GoYA8xebwFmXTqpJZyPghEdRBJ1N3JmNDlaZ20n7g7RI15y0zvo4cZ7bOHFE/640?wx_fmt=png&from=appmsg)

这里简单介绍下**插件**和**技能**的区别：

* **技能**（Skill）可以理解为工作流程/操作手册，它告诉 Codex「这类任务应该按什么步骤、用什么规范、参考哪些资料来做」。
* **插件**（Plugin）可以理解为技能和工具的**集合**，它把一个或多个 skill、外部 app 集成、MCP server 配置等打包成可安装、可共享的东西。

在聊天框中我们可以通过/来快速搜索skills或插件。

![](https://mmbiz.qpic.cn/mmbiz_png/WCtibmYn046hB11AKDKt9Sib7nWSw9A6b0VwibfD1iajBq7yLpb7qztVvaPWiauW59cTsxmOQeTdAmowmBAjJbZibiaGYFhV8ycH7Womr7uwwP2Ngc/640?wx_fmt=png&from=appmsg)

下面我通过几个常见的codex应用场景来展示下插件和技能的用法~

## 常见应用场景

我们首先新建个空白项目，在这个空白项目中我会演示codex的常见应用场景。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/WCtibmYn046jZrXrsJbUhnMnIzfunibibDibjUHaaO26U6zreDiahvlRGQfb7Z6QI6Jq4Jia8Y8JuicYu72evIpo8J52SapBMWzb9GPXOicdBAOekZ8/640?wx_fmt=png&from=appmsg)

### 画图

codex自带生成图片技能，我们通过image Gen插件调用gpt-image-2生成图片。让它画一幅《蜜雪冰城大战东方明珠》的电影海报图，感受下至今最牛逼的生图模型~

![](https://mmbiz.qpic.cn/mmbiz_png/WCtibmYn046ia75sRxyM4EJmKZq9HC20m0oSwIMWooHDWNkDZ2XM5xkb96MmaLHRYAqPaQ2iaIkiaiaZSNZ0ricUKlo17GLkGSOVHZZSZZg4X7hYI/640?wx_fmt=png&from=appmsg)

what's up！这是什么鬼？为什么生成的图片如此抽象？

![](https://mmbiz.qpic.cn/sz_mmbiz_png/WCtibmYn046iaF0TNOjyicQpEGKVJdSSlFAvO0Bv76dpqCgx9xpkMeeJM9ZldwukJIt1RLQyQIO74PpfJ3fbapxbnzRiakQMayG2x3thWxIkXKs/640?wx_fmt=png&from=appmsg)

这是因为目前codex++在生图技能上有点小bug，会通过svg用代码"手绘"图片。解决方法如下：

首先，我们设置下环境变量，打开powershell输入命令设置中转站地址和密钥：

```
setx OPENAI_BASE_URL "https://sub.hachimi-ai.com/v1"
setx OPENAI_API_KEY "sk-xxx"
```

接着我们需要指定codex使用生图技能的**CLI**模式生成图片。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/WCtibmYn046iaMib0zA91VAIhyomDeKGtIeoZIYvX1ibDCQiaicWd2I8JsFS4wkU4LSvZX2aeGbczvgicpcdwzruXvzkU2UBdwV0cha3yMMldPqo5k/640?wx_fmt=png&from=appmsg)

这下对味了~

![](https://mmbiz.qpic.cn/sz_mmbiz_png/WCtibmYn046h5MXQZmK2Atsdn4ibkvoNoXyGmsXIPuhQkBYwM9R6ZPepd0IbprZgn9vdnjBqE2YXKdKA0Dm1soprmOKqZrdjhgjSfjmsjqAf8/640?wx_fmt=png&from=appmsg)

### 代码

众所周知，codex的本职工作是写代码，我们可以直接在对话栏给codex下发任务。这里我给大家介绍下两个经常被忽略，但又非常实用的Agent模式。

#### 计划模式和追求目标

codex除了默认模式外，还有两个单独的模式：**计划模式**和**追求目标**。

**计划模式**一般在目标不够清晰的时候用，codex会通过让你做选择题的方式帮你理清需求。

**追求目标模式**则在你的需求已经很清晰，希望codex不达目的誓不罢休的时候使用，开启后codex如果中途遇到问题，不会像普通模式一样停下来询问你，而是自己想办法解决。

![](https://mmbiz.qpic.cn/mmbiz_png/WCtibmYn046jj9u1w0ElPGvFwdzqiaB3q6F5jaibm7XFZicldJaZS3dQWYhiaiaebS3ojBvh1mFL2ibS3oAPMo6UJk2NNDD1bbf3N4xn69xAB5RMjo/640?wx_fmt=png&from=appmsg)

这里着重讲下计划模式，初次使用codex这类工具的朋友可能经常发现ai做的和自己的需求有不小的偏差，这主要是因为ai没有读懂你的需求。这时候计划模式帮助就很大。比如我这里提出一个模糊的需求：写一个展示当前最火游戏的网站。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/WCtibmYn046j6MQgAJQFDM67c1oUyUzJfPzytfuiaw9LMGvia2pxkYxfeK2DMTH3R0AHloEIwDGkTePtIBpRsXjibpG5BicWzHweiaAwLicpAHqG10/640?wx_fmt=png&from=appmsg)

codex会询问多个问题并给出多个选项，再完成几个选择后，codex会生成一份详细的计划，如果看了没问题我们可以让codex直接实施该计划。

![](https://mmbiz.qpic.cn/mmbiz_png/WCtibmYn046j48CJ9h2S2W9THrRrqSR9x6OUQszIKBYaMicCIY2NNYQ0c0oyOCQN4gb7icQcyYOPh2VeKOFelEsNAotFs8Pq7LQdwR17ZY1K9k/640?wx_fmt=png&from=appmsg)

codex写完后，右侧可以看到生成的网站，我们可以对此进行反馈让codex反工修改。

#### 并行任务

另外，codex可同时处理多个任务，并且显示出每个任务的状态，我们可以同时让他做多个任务，非常方便。

![](https://mmbiz.qpic.cn/mmbiz_png/WCtibmYn046iaGkLePOX8U8qUAK5Gd5xPvwnKcRHs2DdjVz1rTcyhvkah23Nz1bxlBJfdQF8VzkKE5HLsDbUgVz3TcEXibMKVibUPAWw8Lg2vxg/640?wx_fmt=png&from=appmsg)

#### 分支会话

有时候我们希望以某个回答为起点创建分支，我们可以点击消息左下角的派生符号，这里code...